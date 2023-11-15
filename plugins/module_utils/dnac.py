#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import (absolute_import, division, print_function)
__metaclass__ = type
try:
    from dnacentersdk import api, exceptions
except ImportError:
    DNAC_SDK_IS_INSTALLED = False
else:
    DNAC_SDK_IS_INSTALLED = True
from ansible.module_utils._text import to_native
from ansible.module_utils.common import validation
from abc import ABCMeta, abstractmethod
try:
    import logging
except ImportError:
    LOGGING_IN_STANDARD = False
else:
    LOGGING_IN_STANDARD = True
import os.path
import copy
import datetime
import inspect


class DnacBase():

    """Class contains members which can be reused for all intent modules"""

    __metaclass__ = ABCMeta

    def __init__(self, module):
        self.module = module
        self.params = module.params
        self.config = copy.deepcopy(module.params.get("config"))
        self.have = {}
        self.want = {}
        self.validated_config = []
        self.msg = ""
        self.status = "success"
        dnac_params = self.get_dnac_params(self.params)
        self.dnac = DNACSDK(params=dnac_params)
        self.dnac_apply = {'exec': self.dnac._exec}
        self.get_diff_state_apply = {'merged': self.get_diff_merged,
                                     'deleted': self.get_diff_deleted,
                                     'replaced': self.get_diff_replaced,
                                     'overridden': self.get_diff_overridden,
                                     'gathered': self.get_diff_gathered,
                                     'rendered': self.get_diff_rendered,
                                     'parsed': self.get_diff_parsed
                                     }
        self.dnac_log = dnac_params.get("dnac_log")
        log(str(dnac_params))
        self.supported_states = ["merged", "deleted", "replaced", "overridden", "gathered", "rendered", "parsed"]
        self.result = {"changed": False, "diff": [], "response": [], "warnings": []}

    @abstractmethod
    def validate_input(self):
        if not self.config:
            self.msg = "config not available in playbook for validation"
            self.status = "failed"
            return self

    def get_diff_merged(self):
        # Implement logic to merge the resource configuration
        self.merged = True
        return self

    def get_diff_deleted(self):
        # Implement logic to delete the resource
        self.deleted = True
        return self

    def get_diff_replaced(self):
        # Implement logic to replace the resource
        self.replaced = True
        return self

    def get_diff_overridden(self):
        # Implement logic to overwrite the resource
        self.overridden = True
        return self

    def get_diff_gathered(self):
        # Implement logic to gather data about the resource
        self.gathered = True
        return self

    def get_diff_rendered(self):
        # Implement logic to render a configuration template
        self.rendered = True
        return self

    def get_diff_parsed(self):
        # Implement logic to parse a configuration file
        self.parsed = True
        return True

    def log(self, message, frameIncrement=0):
        """Log messages into dnac.log file"""

        if self.dnac_log:
            message = "Module: " + self.__class__.__name__ + ", " + message
            log(message, (1 + frameIncrement))

    def check_return_status(self):
        """API to check the return status value and exit/fail the module"""

        self.log("status: {0}, msg:{1}".format(self.status, self.msg), frameIncrement=1)
        if "failed" in self.status:
            self.module.fail_json(msg=self.msg, response=[])
        elif "exited" in self.status:
            self.module.exit_json(**self.result)
        elif "invalid" in self.status:
            self.module.fail_json(msg=self.msg, response=[])

    def get_dnac_params(self, params):
        """Store the DNAC parameters from the playbook"""

        dnac_params = {"dnac_host": params.get("dnac_host"),
                       "dnac_port": params.get("dnac_port"),
                       "dnac_username": params.get("dnac_username"),
                       "dnac_password": params.get("dnac_password"),
                       "dnac_verify": params.get("dnac_verify"),
                       "dnac_debug": params.get("dnac_debug"),
                       "dnac_log": params.get("dnac_log")
                       }
        return dnac_params

    def get_task_details(self, task_id):
        """
        Get the details of a specific task in Cisco DNA Center.
        Args:
            self (object): An instance of a class that provides access to Cisco DNA Center.
            task_id (str): The unique identifier of the task for which you want to retrieve details.
        Returns:
            dict or None: A dictionary containing detailed information about the specified task,
            or None if the task with the given task_id is not found.
        Description:
            If the task with the specified task ID is not found in Cisco DNA Center, this function will return None.
        """

        result = None
        response = self.dnac._exec(
            family="task",
            function='get_task_by_id',
            params={"task_id": task_id}
        )

        log(str(response))

        if response and isinstance(response, dict):
            result = response.get('response')

        return result

    def check_task_response_status(self, response, validation_string):
        """
        Get the site id from the site name.

        Parameters:
            self - The current object details.
            response (dict) - API response.
            validation_string (string) - String used to match the progress status.

        Returns:
            self
        """

        if not response:
            self.msg = "response is empty"
            self.status = "exited"
            return self

        if not isinstance(response, dict):
            self.msg = "response is not a dictionary"
            self.status = "exited"
            return self

        task_id = response.get("response").get("taskId")
        while True:
            task_details = self.get_task_details(task_id)
            self.log(str(task_details))

            if task_details.get("isError") is True:
                self.msg = str(task_details.get("progress"))
                self.status = "failed"
                break

            if validation_string in task_details.get("progress").lower():
                self.result['changed'] = True
                self.status = "success"
                break

            self.log("progress set to {0} for taskid: {1}"
                     .format(task_details.get('progress'), task_id))

        return self

    def reset_values(self):
        """Reset all neccessary attributes to default values"""

        self.have.clear()
        self.want.clear()

    def get_execution_details(self, execid):
        """
        Get the execution details of an API

        Parameters:
            execid (str) - Id for API execution

        Returns:
            response (dict) - Status for API execution
        """

        self.log("Execution Id " + str(execid))
        response = self.dnac._exec(
            family="task",
            function='get_business_api_execution_details',
            params={"execution_id": execid}
        )
        self.log("Response for the current execution" + str(response))
        return response

    def check_execution_response_status(self, response):
        """
        Checks the reponse status provided by API in the DNAC

        Parameters:
            response (dict) - API response

        Returns:
            self
        """

        self.log(str(response))
        if not response:
            self.msg = "response is empty"
            self.status = "failed"
            return self

        if not isinstance(response, dict):
            self.msg = "response is not a dictionary"
            self.status = "failed"
            return self

        executionid = response.get("executionId")
        while True:
            execution_details = self.get_execution_details(executionid)
            if execution_details.get("status") == "SUCCESS":
                self.result['changed'] = True
                self.msg = "Successfully executed"
                self.status = "success"
                break

            if execution_details.get("bapiError"):
                self.msg = execution_details.get("bapiError")
                self.status = "failed"
                break

        return self


def log(msg, frameIncrement=0):
    with open('dnac.log', 'a') as of:
        callerframerecord = inspect.stack()[1 + frameIncrement]
        frame = callerframerecord[0]
        info = inspect.getframeinfo(frame)
        d = datetime.datetime.now().replace(microsecond=0).isoformat()
        of.write("---- %s ---- %s@%s ---- %s \n" % (d, info.lineno, info.function, msg))


def is_list_complex(x):
    return isinstance(x[0], dict) or isinstance(x[0], list)


def has_diff_elem(ls1, ls2):
    return any((elem not in ls1 for elem in ls2))


def compare_list(list1, list2):
    len_list1 = len(list1)
    len_list2 = len(list2)
    if len_list1 != len_list2:
        return False

    if len_list1 == 0:
        return True

    attempt_std_cmp = list1 == list2
    if attempt_std_cmp:
        return True

    if not is_list_complex(list1) and not is_list_complex(list2):
        return set(list1) == set(list2)

    # Compare normally if it exceeds expected size * 2 (len_list1==len_list2)
    MAX_SIZE_CMP = 100
    # Fail fast if elem not in list, thanks to any and generators
    if len_list1 > MAX_SIZE_CMP:
        return attempt_std_cmp
    else:
        # not changes 'has diff elem' to list1 != list2 ':lists are not equal'
        return not (has_diff_elem(list1, list2)) or not (has_diff_elem(list2, list1))


def fn_comp_key(k, dict1, dict2):
    return dnac_compare_equality(dict1.get(k), dict2.get(k))


def dnac_compare_equality(current_value, requested_value):
    # print("dnac_compare_equality", current_value, requested_value)
    if requested_value is None:
        return True
    if current_value is None:
        return True
    if isinstance(current_value, dict) and isinstance(requested_value, dict):
        all_dict_params = list(current_value.keys()) + list(requested_value.keys())
        return not any((not fn_comp_key(param, current_value, requested_value) for param in all_dict_params))
    elif isinstance(current_value, list) and isinstance(requested_value, list):
        return compare_list(current_value, requested_value)
    else:
        return current_value == requested_value


def simple_cmp(obj1, obj2):
    return obj1 == obj2


def get_dict_result(result, key, value, cmp_fn=simple_cmp):
    if isinstance(result, list):
        if len(result) == 1:
            if isinstance(result[0], dict):
                result = result[0]
                if result.get(key) is not None and result.get(key) != value:
                    result = None
            else:
                result = None
        else:
            for item in result:
                if isinstance(item, dict) and (item.get(key) is None or item.get(key) == value):
                    result = item
                    return result
            result = None
    elif not isinstance(result, dict):
        result = None
    elif result.get(key) is not None and result.get(key) != value:
        result = None
    return result


def dnac_argument_spec():
    argument_spec = dict(
        dnac_host=dict(type="str", required=True),
        dnac_port=dict(type="int", required=False, default=443),
        dnac_username=dict(type="str", default="admin", aliases=["user"]),
        dnac_password=dict(type="str", no_log=True),
        dnac_verify=dict(type="bool", default=True),
        dnac_version=dict(type="str", default="2.2.3.3"),
        dnac_debug=dict(type="bool", default=False),
        validate_response_schema=dict(type="bool", default=True),
    )
    return argument_spec


def validate_str(item, param_spec, param_name, invalid_params):
    """
    This function checks that the input `item` is a valid string and confirms to
    the constraints specified in `param_spec`. If the string is not valid or does
    not meet the constraints, an error message is added to `invalid_params`.

    Args:
        item (str): The input string to be validated.
        param_spec (dict): The parameter's specification, including validation constraints.
        param_name (str): The name of the parameter being validated.
        invalid_params (list): A list to collect validation error messages.

    Returns:
        str: The validated and possibly normalized string.

    Example `param_spec`:
        {
            "type": "str",
            "length_max": 255  # Optional: maximum allowed length
        }
    """

    item = validation.check_type_str(item)
    if param_spec.get("length_max"):
        if 1 <= len(item) <= param_spec.get("length_max"):
            return item
        else:
            invalid_params.append(
                "{0}:{1} : The string exceeds the allowed "
                "range of max {2} char".format(param_name, item, param_spec.get("length_max"))
            )
    return item


def validate_int(item, param_spec, param_name, invalid_params):
    """
    This function checks that the input `item` is a valid integer and conforms to
    the constraints specified in `param_spec`. If the integer is not valid or does
    not meet the constraints, an error message is added to `invalid_params`.

    Args:
        item (int): The input integer to be validated.
        param_spec (dict): The parameter's specification, including validation constraints.
        param_name (str): The name of the parameter being validated.
        invalid_params (list): A list to collect validation error messages.

    Returns:
        int: The validated integer.

    Example `param_spec`:
        {
            "type": "int",
            "range_min": 1,     # Optional: minimum allowed value
            "range_max": 100    # Optional: maximum allowed value
        }
    """

    item = validation.check_type_int(item)
    min_value = 1
    if param_spec.get("range_min") is not None:
        min_value = param_spec.get("range_min")
    if param_spec.get("range_max"):
        if min_value <= item <= param_spec.get("range_max"):
            return item
        else:
            invalid_params.append(
                "{0}:{1} : The item exceeds the allowed "
                "range of max {2}".format(param_name, item, param_spec.get("range_max"))
            )
    return item


def validate_bool(item, param_spec, param_name, invalid_params):
    """
    This function checks that the input `item` is a valid boolean value. If it does
    not represent a valid boolean value, an error message is added to `invalid_params`.

    Args:
        item (bool): The input boolean value to be validated.
        param_spec (dict): The parameter's specification, including validation constraints.
        param_name (str): The name of the parameter being validated.
        invalid_params (list): A list to collect validation error messages.

    Returns:
        bool: The validated boolean value.
    """

    return validation.check_type_bool(item)


def validate_list(item, param_spec, param_name, invalid_params):
    """
    This function checks if the input `item` is a valid list based on the specified `param_spec`.
    It also verifies that the elements of the list match the expected data type specified in the
    `param_spec`. If any validation errors occur, they are appended to the `invalid_params` list.

    Args:
        item (list): The input list to be validated.
        param_spec (dict): The parameter's specification, including validation constraints.
        param_name (str): The name of the parameter being validated.
        invalid_params (list): A list to collect validation error messages.

    Returns:
        list: The validated list, potentially normalized based on the specification.
    """

    try:
        if param_spec.get("type") == type(item).__name__:
            keys_list = []
            for dict_key in param_spec:
                keys_list.append(dict_key)
            if len(keys_list) == 1:
                return validation.check_type_list(item)

            temp_dict = {keys_list[1]: param_spec[keys_list[1]]}
            try:
                if param_spec['elements']:
                    get_spec_type = param_spec['type']
                    get_spec_element = param_spec['elements']
                    if type(item).__name__ == get_spec_type:
                        for element in item:
                            if type(element).__name__ != get_spec_element:
                                invalid_params.append(
                                    "{0} is not of the same datatype as expected which is {1}".format(element, get_spec_element)
                                )
                    else:
                        invalid_params.append(
                            "{0} is not of the same datatype as expected which is {1}".format(item, get_spec_type)
                        )
            except Exception as e:
                item, list_invalid_params = validate_list_of_dicts(item, temp_dict)
                invalid_params.extend(list_invalid_params)
        else:
            invalid_params.append("{0} : is not a valid list".format(item))
    except Exception as e:
        invalid_params.append("{0} : comes into the exception".format(e))

    return item


def validate_dict(item, param_spec, param_name, invalid_params):
    """
    This function checks if the input `item` is a valid dictionary based on the specified `param_spec`.
    If the dictionary does not match the expected data type specified in the `param_spec`,
    a validation error is appended to the `invalid_params` list.

    Args:
        item (dict): The input dictionary to be validated.
        param_spec (dict): The parameter's specification, including validation constraints.
        param_name (str): The name of the parameter being validated.
        invalid_params (list): A list to collect validation error messages.

    Returns:
        dict: The validated dictionary.
    """

    if param_spec.get("type") != type(item).__name__:
        invalid_params.append("{0} : is not a valid dictionary".format(item))
    return validation.check_type_dict(item)


def validate_list_of_dicts(param_list, spec, module=None):
    """Validate/Normalize playbook params. Will raise when invalid parameters found.
    param_list: a playbook parameter list of dicts
    spec: an argument spec dict
          e.g. spec = dict(ip=dict(required=True, type='bool'),
                           foo=dict(type='str', default='bar'))
    return: list of normalized input data
    """

    v = validation
    normalized = []
    invalid_params = []

    for list_entry in param_list:
        valid_params_dict = {}
        if not spec:
            # Handle the case when spec becomes empty but param list is still there
            invalid_params.append("No more spec to validate, but parameters remain")
            break
        for param in spec:
            item = list_entry.get(param)
            log(str(item))
            if item is None:
                if spec[param].get("required"):
                    invalid_params.append(
                        "{0} : Required parameter not found".format(param)
                    )
                else:
                    item = spec[param].get("default")
                    valid_params_dict[param] = item
                    continue
            data_type = spec[param].get("type")
            switch = {
                "str": validate_str,
                "int": validate_int,
                "bool": validate_bool,
                "list": validate_list,
                "dict": validate_dict,
            }

            validator = switch.get(data_type)
            if validator:
                item = validator(item, spec[param], param, invalid_params)
            else:
                invalid_params.append(
                    "{0}:{1} : Unsupported data type {2}.".format(param, item, data_type)
                )

            choice = spec[param].get("choices")
            if choice:
                if item not in choice:
                    invalid_params.append(
                        "{0} : Invalid choice provided".format(item)
                    )

            no_log = spec[param].get("no_log")
            if no_log:
                if module is not None:
                    module.no_log_values.add(item)
                else:
                    msg = "\n\n'{0}' is a no_log parameter".format(param)
                    msg += "\nAnsible module object must be passed to this "
                    msg += "\nfunction to ensure it is not logged\n\n"
                    raise Exception(msg)

            valid_params_dict[param] = item
        normalized.append(valid_params_dict)

    return normalized, invalid_params


class DNACSDK(object):
    def __init__(self, params):
        self.result = dict(changed=False, result="")
        self.validate_response_schema = params.get("validate_response_schema")
        if DNAC_SDK_IS_INSTALLED:
            self.api = api.DNACenterAPI(
                username=params.get("dnac_username"),
                password=params.get("dnac_password"),
                base_url="https://{dnac_host}:{dnac_port}".format(
                    dnac_host=params.get("dnac_host"), dnac_port=params.get("dnac_port")
                ),
                version=params.get("dnac_version"),
                verify=params.get("dnac_verify"),
                debug=params.get("dnac_debug"),
            )
            if params.get("dnac_debug") and LOGGING_IN_STANDARD:
                logging.getLogger('dnacentersdk').addHandler(logging.StreamHandler())
        else:
            self.fail_json(msg="DNA Center Python SDK is not installed. Execute 'pip install dnacentersdk'")

    def changed(self):
        self.result["changed"] = True

    def object_created(self):
        self.changed()
        self.result["result"] = "Object created"

    def object_updated(self):
        self.changed()
        self.result["result"] = "Object updated"

    def object_deleted(self):
        self.changed()
        self.result["result"] = "Object deleted"

    def object_already_absent(self):
        self.result["result"] = "Object already absent"

    def object_already_present(self):
        self.result["result"] = "Object already present"

    def object_present_and_different(self):
        self.result["result"] = "Object already present, but it has different values to the requested"

    def object_modify_result(self, changed=None, result=None):
        if result is not None:
            self.result["result"] = result
        if changed:
            self.changed()

    def is_file(self, file_path):
        return os.path.isfile(file_path)

    def extract_file_name(self, file_path):
        return os.path.basename(file_path)

    def _exec(self, family, function, params=None, op_modifies=False, **kwargs):
        try:
            family = getattr(self.api, family)
            func = getattr(family, function)
        except Exception as e:
            self.fail_json(msg=e)

        try:
            if params:
                file_paths_params = kwargs.get('file_paths', [])
                # This substitution is for the import file operation
                if file_paths_params and isinstance(file_paths_params, list):
                    multipart_fields = {}
                    for (key, value) in file_paths_params:
                        if isinstance(params.get(key), str) and self.is_file(params[key]):
                            file_name = self.extract_file_name(params[key])
                            file_path = params[key]
                            multipart_fields[value] = (file_name, open(file_path, 'rb'))

                    params.setdefault("multipart_fields", multipart_fields)
                    params.setdefault("multipart_monitor_callback", None)

                if not self.validate_response_schema and op_modifies:
                    params["active_validation"] = False

                response = func(**params)
            else:
                response = func()
        except exceptions.dnacentersdkException as e:
            self.fail_json(
                msg=(
                    "An error occured when executing operation."
                    " The error was: {error}"
                ).format(error=to_native(e))
            )
        return response

    def fail_json(self, msg, **kwargs):
        self.result.update(**kwargs)
        raise Exception(msg)

    def exit_json(self):
        return self.result


def main():
    pass


if __name__ == "__main__":
    main()
