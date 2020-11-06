#!/usr/bin/env python

import json
from dnacentersdk import api


ERR_WRONG_METHOD = "Wrong method '{}'"
ERR_STATE_NOT_SUPPORTED = "State '{}' not supported by this module"
ERR_UNKNOWN = "Unknown error. More than one operation matched the given arguments"
ERR_NO_MATCHING_OPERATION = "There are no matching operations for the given arguments"


def msg(message, arg=""):
    return message.format(arg)

def dnac_argument_spec():
    return dict(
        dnac_host=dict(type='str', required=True),
        dnac_port=dict(type='int', required=False, default=443),
        dnac_username=dict(type='str', default='admin', aliases=['user']),
        dnac_password=dict(type='str', no_log=True),
        dnac_verify=dict(type='bool', default=True),
        dnac_version=dict(type='str', default="2.1.1"),
        state=dict(type='str', default='present', choices=['absent', 'delete', 'present', 'create', 'update', 'query']),
        #use_proxy=dict(type='bool', default=True),
        #use_ssl=dict(type='bool', default=True),
        #validate_certs=dict(type='bool', default=True),
    )


class Parameter(object):

    def __init__(self, param):
        self.__dict__ = param
        if self._is_object() or self._is_object_array():
            _schema = self.schema
            self.schema = []
            for param in _schema:
                new_param = Parameter(param)
                self.schema.append(new_param)

    def _get_type(self):
        if self.type == "string":
            return "str"
        elif self.type == "boolean":
            return "bool"
        elif self.type == "integer":
            return "int"
        elif self.type == "number":
            return "int"
        elif self.type == "array":
            return "list"
        elif self.type == "any":
            return "raw"
        elif self.type == "object":
            return "dict"

    def is_required(self):
        _required = False
        if "required" in self.__dict__.keys():
            _required = self.required
        return _required

    def _is_enum(self):
        return "enum" in self.__dict__.keys()

    def _get_choices(self):
        return list(map(str.lower, self.enum))

    def _has_default(self):
        return "default" in self.__dict__.keys()

    def get_dict(self):
        outer_dict = dict()
        inner_dict = dict()
        inner_dict["type"] = self._get_type()
        inner_dict["required"] = self.is_required()
        if self._is_enum():
            inner_dict["choices"] = self._get_choices()
        if self._has_default():
            inner_dict["default"] = self.default
        outer_dict[self.name] = inner_dict
        return outer_dict

    def _is_object(self):
        return self.type == "object"

    def _is_object_array(self):
        if "array_type" in self.__dict__.keys():
            return self.type == "array" and self.array_type == "object"
        else:
            return False

    # TO DO: Add logic to validate parameters of type 'array of objects'
    # Right now if a parameter is an array of objects, we're not validating its schema
    def has_valid_schema(self, module_params, missing_params={}): 
        if self._is_object():
            if not module_params:
                if self.is_required():
                    missing_params.update({"root": [self.name]})
                    return False
                else:
                    return True
            result = True
            for param in self.schema:
                if param.name in module_params.keys():
                    result = result and param.has_valid_schema(module_params.get(param.name), missing_params)
                else:
                    if param.is_required():
                        result = False
                        if self.name not in missing_params.keys():
                            missing_params.update({self.name: []})
                        missing_params[self.name].append(param.name)
            return result
        else:
            return True



class Function(object):

    def __init__(self, name, params, response_schema, family, method):
        self.name = name
        self.params = []
        self.family = family
        self.method = method
        for param in params:
            new_param = Parameter(param)
            self.params.append(new_param)
        self.response_schema = response_schema
        self.existing_object = {}

    def get_required_params(self, object=False):
        required_params = []
        for param in self.params:
            if param.is_required():
                if object:
                    required_params.append(param)
                else:
                    required_params.append(param.name)
        return required_params

    # Returns true if all the params required by this function are 
    # present in the module_params passed to the Ansible module
    def has_required_params(self, module_params):
        return set(self.get_required_params()).issubset(module_params.keys())

    # Returns true if all the module_params passed to the Ansible module
    # are required by this function
    def needs_passed_params(self, module_params):
        return set(module_params.keys()).issubset(self.get_required_params())

    def _has_valid_request_schema(self, module_params, missing_params={}):
        result = True
        for param in self.params:
            result = result and param.has_valid_schema(module_params.get(param.name), missing_params)
        return result

    def _has_valid_response_schema(self, response):
        if self.response_schema.get("type") == "array":
            if isinstance(response, list):
                return True
            elif isinstance(response, dict):
                return "response" in response.keys()
        elif self.response_schema.get("type") == "object":
            if isinstance(response, dict):
                return set(response.keys()).issubset(self.response_schema.get("properties"))                
        else:
            return False

    # Executes the function with the passed parameters
    def exec(self, dnac_api, module_params):
        family = getattr(dnac_api, self.family) 
        func = getattr(family, self.name)
        if self.method == "put":
            self.existing_object.update(module_params)
            module_params = self.existing_object
        missing_params = {}
        if self._has_valid_request_schema(module_params, missing_params):
            response = func(**module_params)
            if self._has_valid_response_schema(response):
                result = Result(response=response, 
                                function_name=self.name)
            else:
                result = Result(success=False, 
                                function_name=self.name,
                                error="The response received from DNAC doesn't match the response schema for this function.",
                                response=response
                                )
                
        else:
            result = Result(success=False, 
                            function_name=self.name,
                            error="Provided arguments do not comply with the function schema",
                            response = {
                                "sdk_function": "{}.{}".format(self.family, self.name),
                                "missing_params": missing_params
                            })
                
        return result


    


class Result(object):
    def __init__(self, response, function_name, success=True, error=""):
        self.response = response
        self.success = success
        self.error = error
        self.function_name = function_name

    def get_response(self):
        return {"dnac_response": self.response, "sdk_function": self.function_name}

    def get_error(self):
        return self.error
    
    def is_successful(self):
        return self.success


class ModuleDefinition(object):

    def __init__(self, module_definition):
        self.name = module_definition.get("name")
        self.family = module_definition.get("family")
        _params = module_definition.get("parameters")
        _operations = module_definition.get("operations")
        _response_schema = module_definition.get("responses")
        self.methods = ["post", "put", "delete", "get"]
        #self.operations = dict.fromkeys(self.methods, [])
        self.operations = dict()

        for method, func_list in _operations.items():
            func_obj_list = []
            for func_name in func_list:
                function = Function(
                            name=func_name, 
                            params=_params.get(func_name),
                            response_schema=_response_schema.get(func_name),
                            family=self.family, 
                            method=method
                            )
                func_obj_list.append(function)
            self.operations[method] = func_obj_list
        
        self.state = dict(zip(self.methods, ["present", "present", "absent", "query"]))
        self.common_params = dnac_argument_spec().keys()
        
    # Strips the common module parameters from the passed parameters
    def strip_common_params(self, module_params):
        return { k: v for k, v in module_params.items() if k not in self.common_params }

    # Strips all unused parameters (those that were not explicitly passed by the user)
    def strip_unused_params(self, module_params):
        return { k: v for k, v in module_params.items() if v != None }

    # Strips off the passed params that are optional for the functions a given method
    def _strip_optional_params(self, module_params, method):
        return { k: v for k, v in module_params.items() if k in self._get_required_params(method) }


    # Retrieves all the functions supported by this module
    def get_functions(self):
        functions = []
        for func_list in self.operations.values():
            for function in func_list:
                functions.append(function)
        return functions

    # Retrieves a specific function by name
    def get_function(self, function_name):
        for function in self.get_functions():
            if function.name == function_name:
                return function
        return None

    # Retrieves a list with the parameters that are required
    # by at least one of the functions of a given method
    def _get_required_params(self, method):
        required_params = []
        if method in self.operations.keys():
            for function in self.operations[method]:
                for param in function.get_required_params():
                    required_params.append(param)
        return required_params

    # Retrieves a list with the parameters that are required
    # by all the functions supported by this module
    def _get_common_required_params(self):
        functions = self.get_functions()
        common_required_params = functions[0].get_required_params()
        for i in range(1, len(functions)):
            # Gets the intersection of two lists
            common_required_params = \
                    [item for item in common_required_params if item in functions[i].get_required_params()]
        return common_required_params


    # Retrieves a dictionary with all the parameters supported by this module
    # This dictionary is later used to instantiate the AnsibleModule class
    def get_argument_spec_dict(self):
        param_dict = dict()
        for function in self.get_functions():
            for param in function.params:    
                param_dict.update(param.get_dict())
        
        # If a parameter is required by all functions in a module
        # then it's a required parameter of the module
        for param, attr in param_dict.items():
            attr["required"] = param in self._get_common_required_params()

        return param_dict

    def get_required_if_list(self):
        return []


    def get_put_function(self):
        if "put" in self.operations.keys():
            return self.operations["put"][0], {"msg": "Success"}
        else:
            return None, {"msg": "This module doesn't have a 'put' function"}


    # Retrieves the function that exactly matches the given method and module parameters.
    def choose_function(self, method, module_params):
        
        if method in self.methods:
            ops = self.operations.get(method)
        else:
            message = msg(ERR_WRONG_METHOD, method) # Wrong method '{}'
            return None, {"msg": message}

        if len(ops) == 0:
            message = msg(ERR_STATE_NOT_SUPPORTED, self.state.get(method)) # State '{}' not supported by this module
            return None, {"msg": message}
    
        valid_ops = []

        non_optional_params = self._strip_optional_params(module_params, method)
        for function in ops:
            if function.has_required_params(module_params) and function.needs_passed_params(non_optional_params):
                valid_ops.append(function)


        if len(valid_ops) == 0:
            message = msg(ERR_NO_MATCHING_OPERATION) # "There are no matching operations for the given arguments"
            return None, {"msg": message}
        
        elif len(valid_ops) == 1:
            function = valid_ops[0] 
            return function, {"msg": "Success"}

        else:
            message = msg(ERR_UNKNOWN) # Unknown error. More than one operation matched the given arguments.
            return None, {"msg": message}
        

class ObjectExistenceCriteria(object):

    def __init__(self, dnac, get_function, get_params, list_field):
        self.dnac = dnac
        self.get_function = get_function
        self.get_params = get_params
        self.list_field = list_field
        self.WARN_OBJECT_EXISTS = "Object already exists"
        self.ERR_INVALID_GET_FUNC = "Function is not a 'get' function. Could not determine if object exists."
        self.ERR_NO_GET_FUNCTION = "This module doesn't support the requested 'get' function"
        
    def object_exists(self):
        function = self.dnac.moddef.get_function(self.get_function)
        if function:
            if function.method != "get":
                self.dnac.fail_json(msg=self.ERR_INVALID_GET_FUNC)
            else:
                family = getattr(self.dnac.api, function.family) 
                func = getattr(family, function.name)
                response = func(**self.get_params)
                for obj in response.get(self.list_field):
                    if self._object_is_equal(obj, self.dnac.params):
                        self.dnac.existing_object = self._transform_params(obj)
                        return True
                return False
        else:
            self.dnac.fail_json(msg=self.ERR_NO_GET_FUNCTION)

    
    def _object_is_equal(self, existing_object, candidate_params):
        pass

    def _transform_params(self, existing_object):
        return existing_object

    


class DNACModule(object):

    def __init__(self, module, moddef):
        self.module = module
        self.params = module.params
        self.response = None
        self.result = dict(changed=False)
        self.error = dict(code=None, text=None)
        self.api = api.DNACenterAPI(username=self.params.get('dnac_username'),
                        password=self.params.get('dnac_password'),
                        base_url="https://{}:{}".format(self.params.get('dnac_host'), self.params.get('dnac_port')),
                        version=self.params.get('dnac_version'),
                        verify=self.params.get('dnac_verify'))
        self.moddef = moddef
        self.params = self.moddef.strip_common_params(self.params)
        self.params = self.moddef.strip_unused_params(self.params)
        self.existing_object = {}   

       
    def exec(self, method):
        if method == "put":
            function, status = self.moddef.get_put_function()
            if not function:
                self.fail_json(msg=status.get("msg"))
            function.existing_object = self.existing_object
        else:
            function, status = self.moddef.choose_function(method, self.params)
            if not function:
                self.fail_json(msg=status.get("msg"))
        result = function.exec(self.api, self.params)

        if result.is_successful():
            self.result.update(result.get_response())
        else:
            self.fail_json(result.get_error(), **result.get_response()) #TO DO: If the module fails don't return a dictionary with "dnac_response"

    def disable_validation(self):
        self.params["active_validation"] = False



    def fail_json(self, msg, **kwargs):
        # Return error information, if we have it
        if self.error.get('code') is not None and self.error.get('text') is not None:
            self.result['error'] = self.error

        self.result.update(**kwargs)
        self.module.fail_json(msg=msg, **self.result)

    def exit_json(self, **kwargs):
        self.result.update(**kwargs)
        self.module.exit_json(**self.result)




def main():
    pass


if __name__ == '__main__':
    main()
