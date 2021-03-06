#!/usr/bin/env python
from __future__ import (absolute_import, division, print_function)
__metaclass__ = type
try:
    from dnacentersdk import api
except ImportError:
    DNAC_SDK_IS_INSTALLED = False
else:
    DNAC_SDK_IS_INSTALLED = True
from ansible.module_utils.basic import AnsibleModule
from ansible.module_utils._text import to_native
from ansible_collections.cisco.dnac.plugins.module_utils.exceptions import (
    InvalidFunction,
    StateNotSupported,
    NoMatchingOperation,
    MultipleOperations,
)
try:
    from ansible.errors import AnsibleActionFail
except ImportError:
    ANSIBLE_ERRORS_INSTALLED = False
else:
    ANSIBLE_ERRORS_INSTALLED = True


def dnac_argument_spec(idempotent=False):
    argument_spec = dict(
        dnac_host=dict(type="str", required=True),
        dnac_port=dict(type="int", required=False, default=443),
        dnac_username=dict(type="str", default="admin", aliases=["user"]),
        dnac_password=dict(type="str", no_log=True),
        dnac_verify=dict(type="bool", default=True),
        dnac_version=dict(type="str", default="2.1.1"),
        validate_response_schema=dict(type="bool", default=True),
    )
    if idempotent:
        argument_spec.update(
            state=dict(
                type="str",
                required=True,
                choices=["present", "absent", "query"],
            )
        )
    else:
        argument_spec.update(
            state=dict(
                type="str",
                required=True,
                choices=["create", "delete", "update", "query"],
            )
        )
    return argument_spec


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

    def is_artificial(self):
        _artificial = False
        if "artificial" in self.__dict__.keys():
            _artificial = self.artificial
        return _artificial

    def _is_enum(self):
        return "enum" in self.__dict__.keys()

    def _get_choices(self):
        return self.enum

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
    def has_valid_schema(self, module_params, missing_params=None):
        if not missing_params:
            missing_params = {}
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
                    result = result and param.has_valid_schema(
                        module_params.get(param.name), missing_params
                    )
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

    def _get_param_by_name(self, param_name):
        for param in self.params:
            if param.name == param_name:
                return param
        return None

    def get_required_params(self, object=False):
        required_params = []
        for param in self.params:
            if param.is_required():
                if object:
                    required_params.append(param)
                else:
                    required_params.append(param.name)
        return required_params

    def fix_overlapping_params(self, params):
        if self.name in ["get_device_list", "get_device_count", "add_a_workflow", "update_workflow"]:
            if "_state" in params:
                params["state"] = params.pop("_state")
        return params

    def strip_artificial_params(self, module_params):
        for param_name in list(module_params):
            param = self._get_param_by_name(param_name)
            if param:
                if param.is_artificial():
                    module_params.pop(param_name)
        return module_params

    # Returns true if all the params required by this function are
    # present in the module_params passed to the Ansible module
    def has_required_params(self, module_params):
        return set(self.get_required_params()).issubset(module_params.keys())

    # Returns true if all the module_params passed to the Ansible module
    # are required by this function
    def needs_passed_params(self, module_params):
        return set(module_params.keys()).issubset(self.get_required_params())

    def has_valid_request_schema(self, module_params, missing_params=None):
        if not missing_params:
            missing_params = {}
        result = True
        for param in self.params:
            result = result and param.has_valid_schema(
                module_params.get(param.name), missing_params
            )
        return result

    def has_valid_response_schema(self, response):
        if self.response_schema:
            if self.response_schema.get("type") == "array":
                if isinstance(response, list):
                    return True
                elif isinstance(response, dict):
                    return "response" in response.keys()
            elif self.response_schema.get("type") == "object":
                if isinstance(response, dict):
                    return set(response.keys()).issubset(
                        self.response_schema.get("properties")
                    )
            else:
                return False
        else:
            return False


class ModuleDefinition(object):
    def __init__(self, module_definition):
        self.name = module_definition.get("name")
        self.family = module_definition.get("family")
        _params = module_definition.get("parameters")
        _operations = module_definition.get("operations")
        _response_schema = module_definition.get("responses")
        self.methods = ["post", "put", "delete", "get"]
        self.operations = dict()

        for method, func_list in _operations.items():
            func_obj_list = []
            for func_name in func_list:
                function = Function(
                    name=func_name,
                    params=_params.get(func_name),
                    response_schema=_response_schema.get(func_name),
                    family=self.family,
                    method=method,
                )
                func_obj_list.append(function)
            self.operations[method] = func_obj_list

        self.state = dict(zip(self.methods, ["present", "present", "absent", "query"]))
        self.common_params = dnac_argument_spec().keys()

    # Strips the common module parameters from the passed parameters
    def strip_common_params(self, module_params):
        return {k: v for k, v in module_params.items() if k not in self.common_params}

    # Strips all unused parameters (those that were not explicitly passed by the user)
    def strip_unused_params(self, module_params):
        return {k: v for k, v in module_params.items() if v is not None}

    # Strips off the passed params that are optional for the functions a given method
    def _strip_optional_params(self, module_params, method):
        return {
            k: v
            for k, v in module_params.items()
            if k in self._get_required_params(method)
        }

    # Retrieves all the functions supported by this module
    def get_functions(self):
        functions = []
        for func_list in self.operations.values():
            for function in func_list:
                functions.append(function)
        return functions

    # Retrieves a specific function by name
    def get_function_by_name(self, function_name):
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
            common_required_params = [
                item
                for item in common_required_params
                if item in functions[i].get_required_params()
            ]
        return common_required_params

    # Retrieves a dictionary with all the parameters supported by this module
    # This dictionary is later used to instantiate the AnsibleModule class
    def get_argument_spec_dict(self):
        param_dict = dnac_argument_spec()
        for function in self.get_functions():
            for param in function.params:
                param_dict.update(param.get_dict())

        # If a parameter is required by all functions in a module
        # then it's a required parameter of the module
        for param, attr in param_dict.items():
            attr["required"] = param in self._get_common_required_params()

        return param_dict

    # TODO: Validate the conditional param requirements
    def get_required_if_list(self):
        return []

    def get_put_function(self):
        if "put" in self.operations.keys():
            return self.operations["put"][0]
        else:
            raise InvalidFunction()

    def get_post_function(self):
        if "post" in self.operations.keys():
            return self.operations["post"][0]
        else:
            raise InvalidFunction()

    # Retrieves the function that exactly matches the given method and module parameters.
    def choose_function(self, method, module_params):
        ops = self.operations.get(method)
        if len(ops) == 0:
            raise StateNotSupported()
        valid_ops = []
        non_optional_params = self._strip_optional_params(module_params, method)
        for function in ops:
            if function.has_required_params(
                module_params
            ) and function.needs_passed_params(non_optional_params):
                valid_ops.append(function)
        if len(valid_ops) == 0:
            raise NoMatchingOperation()
        elif len(valid_ops) == 1:
            return valid_ops[0]
        else:
            raise MultipleOperations()


class ObjectExistenceCriteria(object):
    def __init__(self, dnac, get_function, get_params, list_field):
        self.dnac = dnac
        self.get_function = get_function
        self.get_params = get_params
        self.list_field = list_field
        self.WARN_OBJECT_EXISTS = "Object already exists"
        self.ERR_INVALID_GET_FUNC = (
            "Function is not a 'get' function. Could not determine if object exists."
        )
        self.ERR_NO_GET_FUNCTION = (
            "This module doesn't support the requested 'get' function"
        )

    def object_exists(self):
        function = self.dnac.moddef.get_function_by_name(self.get_function)
        if function:
            if function.method != "get":
                self.dnac.fail_json(msg=self.ERR_INVALID_GET_FUNC)
            else:
                func = self.dnac.get_func(function)
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
    def __init__(self, moddef, params, verbosity):
        self.params = params
        self.verbosity = verbosity
        self.result = dict(changed=False)
        self.validate_response_schema = self.params.get("validate_response_schema")
        if DNAC_SDK_IS_INSTALLED:
            self.api = api.DNACenterAPI(
                username=self.params.get("dnac_username"),
                password=self.params.get("dnac_password"),
                base_url="https://{dnac_host}:{dnac_port}".format(
                    dnac_host=self.params.get("dnac_host"), dnac_port=self.params.get("dnac_port")
                ),
                version=self.params.get("dnac_version"),
                verify=self.params.get("dnac_verify"),
            )
        else:
            self.fail_json(msg="DNA Center Python SDK is not installed. Execute 'pip install dnacentersdk'")
        self.moddef = moddef
        self.params = self.moddef.strip_common_params(self.params)
        self.params = self.moddef.strip_unused_params(self.params)
        self.existing_object = {}

        if self.params.get("filename") and self.params.get("filepath"):
            filename = self.params.pop("filename")
            filepath = self.params.pop("filepath")
            self.params.setdefault(
                "multipart_fields", {"file": (filename, open(filepath, "rb"))}
            )
            self.params.setdefault("multipart_monitor_callback", None)

    def changed(self):
        self.result["changed"] = True

    def get_func(self, function):
        try:
            family = getattr(self.api, function.family)
            func = getattr(family, function.name)
        except Exception as e:
            self.fail_json(msg=e)
        return func

    def exec(self, method):
        if method == "put":
            try:
                function = self.moddef.get_put_function()
                self.existing_object.update(self.params)
                self.params = self.existing_object
            except InvalidFunction:
                self.fail_json(msg="This module doesn't have a 'put' function")
        elif method == "post":
            try:
                function = self.moddef.get_post_function()
            except InvalidFunction:
                self.fail_json(msg="This module doesn't have a 'post' function")
        elif method in ("get", "delete"):
            try:
                function = self.moddef.choose_function(method, self.params)
            except StateNotSupported:
                self.fail_json(
                    msg="State '{state}' not supported by this module".format(
                        state=self.moddef.state.get(method)
                    )
                )
            except NoMatchingOperation:
                self.fail_json(
                    msg="There are no matching operations for the given arguments"
                )
            except MultipleOperations:
                self.fail_json(
                    msg="More than one operation matched the given arguments."
                )
        else:
            self.fail_json(msg="Wrong method '{method}'".format(method=method))

        self.result.update(
            dict(sdk_function="{family}.{name}".format(family=function.family, name=function.name))
        )
        self.params = function.fix_overlapping_params(function.strip_artificial_params(self.params))
        func = self.get_func(function)
        missing_params = dict()
        if function.has_valid_request_schema(self.params, missing_params):
            try:
                response = func(**self.params)
            except Exception as e:
                self.fail_json(
                    msg=(
                        "An error occured when executing operation."
                        " The error was: {error}"
                    ).format(error=to_native(e))
                )

            if (
                function.has_valid_response_schema(response)
                or not self.validate_response_schema
            ):
                self.result.update(dict(dnac_response=response))
            else:
                if self.verbosity >= 3:
                    self.result.update(dict(dnac_response=response))
                self.fail_json(
                    msg=(
                        "The response received from DNAC doesn't match the response schema for this function."
                        " Consider setting the 'validate_response_schema' argument to False."
                    )
                )
        else:
            self.result.update(dict(missing_params=missing_params))
            self.fail_json(
                msg="Provided arguments do not comply with the function schema"
            )

    def disable_validation(self):
        self.params["active_validation"] = False

    def fail_json(self, msg, **kwargs):
        self.result.update(**kwargs)
        raise AnsibleActionFail(msg, kwargs)

    def exit_json(self):
        return self.result


def main():
    pass


if __name__ == "__main__":
    main()
