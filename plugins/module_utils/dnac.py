#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import (absolute_import, division, print_function)
__metaclass__ = type
try:
    from cryptography.fernet import Fernet
    HAS_FERNET = True
except ImportError:
    HAS_FERNET = False
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
    import ipaddress
except ImportError:
    LOGGING_IN_STANDARD = False
else:
    LOGGING_IN_STANDARD = True
import os.path
import copy
import json
# import datetime
import inspect
import re
import socket
import time
import traceback


class DnacBase():

    """Class contains members which can be reused for all intent modules"""

    __metaclass__ = ABCMeta
    __is_log_init = False

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
        self.verify_diff_state_apply = {'merged': self.verify_diff_merged,
                                        'deleted': self.verify_diff_deleted,
                                        'replaced': self.verify_diff_replaced,
                                        'overridden': self.verify_diff_overridden,
                                        'gathered': self.verify_diff_gathered,
                                        'rendered': self.verify_diff_rendered,
                                        'parsed': self.verify_diff_parsed
                                        }
        self.dnac_log = dnac_params.get("dnac_log")
        self.max_timeout = self.params.get('dnac_api_task_timeout')

        self.payload = module.params
        self.dnac_version = int(self.payload.get("dnac_version").replace(".", ""))
        self.dnac_version_in_integer = int(self.payload.get("dnac_version").replace(".", ""))
        self.dnac_version_in_string = self.payload.get("dnac_version")
        # Dictionary to store multiple versions for easy maintenance and scalability
        # To add a new version, simply update the 'dnac_versions' dictionary with the new version string as the key
        # and the corresponding version number as the value.
        self.dnac_versions = {
            "2.2.2.3": 2223,
            "2.2.3.3": 2233,
            "2.3.3.0": 2330,
            "2.3.5.3": 2353,
            "2.3.7.6": 2376,
            "2.3.7.9": 2379,
            # Add new versions here, e.g., "2.4.0.0": 2400
        }

        # Dynamically create variables based on dictionary keys
        for version_key, version_value in self.dnac_versions.items():
            setattr(self, "version_" + version_key.replace(".", "_"), version_value)

        if self.dnac_log and not DnacBase.__is_log_init:
            self.dnac_log_level = dnac_params.get("dnac_log_level") or 'WARNING'
            self.dnac_log_level = self.dnac_log_level.upper()
            self.validate_dnac_log_level()
            self.dnac_log_file_path = dnac_params.get("dnac_log_file_path") or 'dnac.log'
            self.validate_dnac_log_file_path()
            self.dnac_log_mode = 'w' if not dnac_params.get("dnac_log_append") else 'a'
            self.setup_logger('logger')
            self.logger = logging.getLogger('logger')
            DnacBase.__is_log_init = True
            self.log('Logging configured and initiated', "DEBUG")
        else:
            # If dnac_log is False, return an empty logger
            self.logger = logging.getLogger('empty_logger')
            self.logger.addHandler(logging.NullHandler())

        self.log('Cisco Catalyst Center parameters: {0}'.format(dnac_params), "DEBUG")
        self.supported_states = ["merged", "deleted", "replaced", "overridden", "gathered", "rendered", "parsed"]
        self.result = {"changed": False, "diff": [], "response": [], "warnings": []}

    def get_ccc_version_as_string(self):
        return self.dnac_version_in_string

    def get_ccc_version_as_integer(self):
        return self.dnac_version_in_integer

    def get_ccc_version_as_int_from_str(self, dnac_version):
        return self.dnac_versions.get(dnac_version)

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
        return self

    def verify_diff_merged(self):
        # Implement logic to verify the merged resource configuration
        self.merged = True
        return self

    def verify_diff_deleted(self):
        # Implement logic to verify the deleted resource
        self.deleted = True
        return self

    def verify_diff_replaced(self):
        # Implement logic to verify the replaced resource
        self.replaced = True
        return self

    def verify_diff_overridden(self):
        # Implement logic to verify the overwritten resource
        self.overridden = True
        return self

    def verify_diff_gathered(self):
        # Implement logic to verify the gathered data about the resource
        self.gathered = True
        return self

    def verify_diff_rendered(self):
        # Implement logic to verify the rendered configuration template
        self.rendered = True
        return self

    def verify_diff_parsed(self):
        # Implement logic to verify the parsed configuration file
        self.parsed = True
        return self

    def setup_logger(self, logger_name):
        """Set up a logger with specified name and configuration based on dnac_log_level"""
        level_mapping = {
            'INFO': logging.INFO,
            'DEBUG': logging.DEBUG,
            'WARNING': logging.WARNING,
            'ERROR': logging.ERROR,
            'CRITICAL': logging.CRITICAL
        }
        level = level_mapping.get(self.dnac_log_level, logging.WARNING)

        logger = logging.getLogger(logger_name)
        # formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(module)s: %(funcName)s: %(lineno)d --- %(message)s', datefmt='%m-%d-%Y %H:%M:%S')
        formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s', datefmt='%m-%d-%Y %H:%M:%S')

        file_handler = logging.FileHandler(self.dnac_log_file_path, mode=self.dnac_log_mode)
        file_handler.setFormatter(formatter)

        logger.setLevel(level)
        logger.addHandler(file_handler)

    def validate_dnac_log_level(self):
        """Validates if the logging level is string and of expected value"""
        if self.dnac_log_level not in ('INFO', 'DEBUG', 'WARNING', 'ERROR', 'CRITICAL'):
            raise ValueError("Invalid log level: 'dnac_log_level:{0}'".format(self.dnac_log_level))

    def validate_dnac_log_file_path(self):
        """
        Validates the specified log file path, ensuring it is either absolute or relative,
        the directory exists, and has a .log extension.
        """
        # Convert the path to absolute if it's relative
        dnac_log_file_path = os.path.abspath(self.dnac_log_file_path)

        # Validate if the directory exists
        log_directory = os.path.dirname(dnac_log_file_path)
        if not os.path.exists(log_directory):
            raise FileNotFoundError("The directory for log file '{0}' does not exist.".format(dnac_log_file_path))

    def log(self, message, level="WARNING", frameIncrement=0):
        """Logs formatted messages with specified log level and incrementing the call stack frame
        Args:
            self (obj, required): An instance of the DnacBase Class.
            message (str, required): The log message to be recorded.
            level (str, optional): The log level, default is "info".
                                   The log level can be one of 'DEBUG', 'INFO', 'WARNING', 'ERROR', or 'CRITICAL'.
        """

        if self.dnac_log:
            # of.write("---- %s ---- %s@%s ---- %s \n" % (d, info.lineno, info.function, msg))
            # message = "Module: " + self.__class__.__name__ + ", " + message
            class_name = self.__class__.__name__
            callerframerecord = inspect.stack()[1 + frameIncrement]
            frame = callerframerecord[0]
            info = inspect.getframeinfo(frame)
            log_message = " %s: %s: %s: %s \n" % (class_name, info.function, info.lineno, message)
            log_method = getattr(self.logger, level.lower())
            log_method(log_message)

    def check_return_status(self):
        """API to check the return status value and exit/fail the module"""

        # self.log("status: {0}, msg:{1}".format(self.status, self.msg), frameIncrement=1)
        frame = inspect.currentframe().f_back
        line_no = frame.f_lineno
        self.log(
            "Line No: {line_no} status: {status}, msg: {msg}"
            .format(line_no=line_no, status=self.status, msg=self.msg), "DEBUG"
        )
        if "failed" in self.status:
            self.module.fail_json(msg=self.msg, response=self.result.get('response', []))
        elif "exited" in self.status:
            self.module.exit_json(**self.result)
        elif "invalid" in self.status:
            self.module.fail_json(msg=self.msg, response=self.result.get('response', []))

    def is_valid_password(self, password):
        """
        Check if a password is valid.
        Args:
            self (object): An instance of a class that provides access to Cisco Catalyst Center.
            password (str): The password to be validated.
        Returns:
            bool: True if the password is valid, False otherwise.
        Description:
            The function checks the validity of a password based on the following criteria:
            - Minimum 8 characters.
            - At least one lowercase letter.
            - At least one uppercase letter.
            - At least one digit.
            - At least one special character
        """

        pattern = r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[-=\\;,./~!@#$%^&*()_+{}[\]|:?]).{8,}$"

        return re.match(pattern, password) is not None

    def is_valid_email(self, email):
        """
        Validate an email address.
        Args:
            self (object): An instance of a class that provides access to Cisco Catalyst Center.
            email (str): The email address to be validated.
        Returns:
            bool: True if the email is valid, False otherwise.
        Description:
            This function checks if the provided email address is valid based on the following criteria:
            - It contains one or more alphanumeric characters or allowed special characters before the '@'.
            - It contains one or more alphanumeric characters or dashes after the '@' and before the domain.
            - It contains a period followed by at least two alphabetic characters at the end of the string.
        The allowed special characters before the '@' are: ._%+-.
        """

        # Define the regex pattern for a valid email address
        pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        # Use re.match to see if the email matches the pattern
        if re.match(pattern, email):
            return True
        else:
            return False

    def get_dnac_params(self, params):
        """Store the Cisco Catalyst Center parameters from the playbook"""

        dnac_params = {"dnac_host": params.get("dnac_host"),
                       "dnac_port": params.get("dnac_port"),
                       "dnac_username": params.get("dnac_username"),
                       "dnac_password": params.get("dnac_password"),
                       "dnac_version": params.get("dnac_version"),
                       "dnac_verify": params.get("dnac_verify"),
                       "dnac_debug": params.get("dnac_debug"),
                       "dnac_log": params.get("dnac_log"),
                       "dnac_log_level": params.get("dnac_log_level"),
                       "dnac_log_file_path": params.get("dnac_log_file_path"),
                       "dnac_log_append": params.get("dnac_log_append")
                       }
        return dnac_params

    def get_task_details(self, task_id):
        """
        Get the details of a specific task in Cisco Catalyst Center.
        Args:
            self (object): An instance of a class that provides access to Cisco Catalyst Center.
            task_id (str): The unique identifier of the task for which you want to retrieve details.
        Returns:
            dict or None: A dictionary containing detailed information about the specified task,
            or None if the task with the given task_id is not found.
        Description:
            If the task with the specified task ID is not found in Cisco Catalyst Center, this function will return None.
        """

        result = None
        response = self.dnac._exec(
            family="task",
            function='get_task_by_id',
            params={"task_id": task_id}
        )

        self.log('Task Details: {0}'.format(str(response)), 'DEBUG')
        self.log("Retrieving task details by the API 'get_task_by_id' using task ID: {0}, Response: {1}".format(task_id, response), "DEBUG")

        if response and isinstance(response, dict):
            result = response.get('response')

        return result

    def get_device_details_limit(self):
        """
        Retrieves the limit for 'get_device_list' API to collect the device details..
        Parameters:
            self (object): An instance of a class that provides access to Cisco Catalyst Center.
        Returns:
            int: The limit for 'get_device_list' api device details, which is set to 500 by default.
        Description:
            This method returns a predefined limit for the number of device details that can be processed or retrieved
            from 'get_device_list' api. Currently, the limit is set to a fixed value of 500.
        """

        api_response_limit = 500
        return api_response_limit

    def check_task_response_status(self, response, validation_string, api_name, data=False):
        """
        Get the site id from the site name.

        Parameters:
            self - The current object details.
            response (dict) - API response.
            validation_string (str) - String used to match the progress status.
            api_name (str) - API name.
            data (bool) - Set to True if the API is returning any information. Else, False.

        Returns:
            self
        """

        if not response:
            self.msg = (
                "The response from the API '{api_name}' is empty."
                .format(api_name=api_name)
            )
            self.status = "failed"
            return self

        if not isinstance(response, dict):
            self.msg = (
                "The response from the API '{api_name}' is not a dictionary."
                .format(api_name=api_name)
            )
            self.status = "failed"
            return self

        response = response.get("response")
        if response.get("errorcode") is not None:
            self.msg = response.get("response").get("detail")
            self.status = "failed"
            return self

        task_id = response.get("taskId")
        start_time = time.time()
        while True:
            end_time = time.time()
            if (end_time - start_time) >= self.max_timeout:
                self.msg = "Max timeout of {max_timeout} sec has reached for the task id '{task_id}'. " \
                           .format(max_timeout=self.max_timeout, task_id=task_id) + \
                           "Exiting the loop due to unexpected API '{api_name}' status.".format(api_name=api_name)
                self.log(self.msg, "WARNING")
                self.status = "failed"
                break

            task_details = self.get_task_details(task_id)
            self.log('Getting task details from task ID {0}: {1}'.format(task_id, task_details), "DEBUG")

            if task_details.get("isError") is True:
                if task_details.get("failureReason"):
                    self.msg = str(task_details.get("failureReason"))
                    string_check = "check task tree"
                    if string_check in self.msg.lower():
                        time.sleep(self.params.get('dnac_task_poll_interval'))
                        self.msg = self.check_task_tree_response(task_id)
                else:
                    self.msg = str(task_details.get("progress"))
                self.status = "failed"
                break

            if validation_string in task_details.get("progress").lower():
                self.result['changed'] = True
                if data is True:
                    self.msg = task_details.get("data")
                self.status = "success"
                break

            self.log("Progress is {0} for task ID: {1}".format(task_details.get('progress'), task_id), "DEBUG")

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

        self.log("Execution Id: {0}".format(execid), "DEBUG")
        response = self.dnac._exec(
            family="task",
            function='get_business_api_execution_details',
            params={"execution_id": execid}
        )
        self.log("Response for the current execution: {0}".format(response))
        return response

    def check_execution_response_status(self, response, api_name):
        """
        Checks the reponse status provided by API in the Cisco Catalyst Center

        Parameters:
            response (dict) - API response
            api_name (str) - API name

        Returns:
            self
        """

        if not response:
            self.msg = (
                "The response from the API '{api_name}' is empty."
                .format(api_name=api_name)
            )
            self.status = "failed"
            return self

        if not isinstance(response, dict):
            self.msg = (
                "The response from the API '{api_name}' is not a dictionary."
                .format(api_name=api_name)
            )
            self.status = "failed"
            return self

        execution_id = response.get("executionId")
        start_time = time.time()
        while True:
            end_time = time.time()
            if (end_time - start_time) >= self.max_timeout:
                self.msg = "Max timeout of {max_timeout} sec has reached for the execution id '{execution_id}'. "\
                           .format(max_timeout=self.max_timeout, execution_id=execution_id) + \
                           "Exiting the loop due to unexpected API '{api_name}' status.".format(api_name=api_name)
                self.log(self.msg, "WARNING")
                self.status = "failed"
                break

            execution_details = self.get_execution_details(execution_id)
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

    def check_string_dictionary(self, task_details_data):
        """
        Check whether the input is string dictionary or string.

        Parameters:
            task_details_data (string) - Input either string dictionary or string.

        Returns:
            value (dict) - If the input is string dictionary, else returns None.
        """

        try:
            value = json.loads(task_details_data)
            if isinstance(value, dict):
                return value
        except json.JSONDecodeError:
            pass
        return None

    def get_device_ip_from_device_id(self, site_id):
        """
        Retrieve the management IP addresses and their corresponding instance UUIDs of devices associated with a specific site in Cisco Catalyst Center.

        Args:
            site_id (str): The ID of the site to be retrieved.

        Returns:
            dict: A dictionary mapping management IP addresses to their instance UUIDs, or an empty dict if no devices found.
        """

        mgmt_ip_to_instance_id_map = {}

        try:
            response = self.get_device_ids_from_site(site_id)

            if not response:
                raise ValueError("No response received from get_device_ids_from_site")

            self.log("Received API response from 'get_device_ids_from_site': {0}".format(str(response)), "DEBUG")

            for device_id in response:
                device_response = self.dnac._exec(
                    family="devices",
                    function="get_device_by_id",
                    op_modifies=True,
                    params={"id": device_id}
                )

                management_ip = device_response.get("response", {}).get("managementIpAddress")
                instance_uuid = device_response.get("response", {}).get("instanceUuid")
                if management_ip and instance_uuid:
                    mgmt_ip_to_instance_id_map[management_ip] = instance_uuid
                else:
                    self.log("Management IP or instance UUID not found for device ID: {0}".format(device_id), "WARNING")

        except Exception as e:
            self.log("Unable to fetch the device(s) associated with the site '{0}' due to {1}".format(site_id, str(e)), "ERROR")
            return {}

        if not mgmt_ip_to_instance_id_map:
            self.log("No reachable devices found at Site: {0}".format(site_id), "INFO")

        return mgmt_ip_to_instance_id_map

    def get_sites_type(self, site_name):
        """
        Get the type of a site in Cisco Catalyst Center.
        Parameters:
            self (object): An instance of a class used for interacting with Cisco Catalyst Center.
            site_name (str): The name of the site for which to retrieve the type.
        Returns:
            site_type (str or None): The type of the specified site, or None if the site is not found.
        Description:
            This function queries Cisco Catalyst Center to retrieve the type of a specified site. It uses the
            get_site API with the provided site name, extracts the site type from the response, and returns it.
            If the specified site is not found, the function returns None, and an appropriate log message is generated.
        """

        try:
            response = self.get_site(site_name)
            if self.get_ccc_version_as_integer() <= self.get_ccc_version_as_int_from_str("2.3.5.3"):
                site = response.get("response")
                site_additional_info = site[0].get("additionalInfo")

                for item in site_additional_info:
                    if item["nameSpace"] == "Location":
                        site_type = item.get("attributes").get("type")
            else:
                self.log("Received API response from 'get_sites': {0}".format(str(response)), "DEBUG")
                site = response.get("response")
                site_type = site[0].get("type")

        except Exception as e:
            self.msg = "Error while fetching the site '{0}' and the specified site was not found in Cisco Catalyst Center.".format(site_name)
            self.log(self.msg, "ERROR")
            self.module.fail_json(msg=self.msg, response=[self.msg])

        return site_type

    def get_device_ids_from_site(self, site_id):
        """
        Retrieve device IDs associated with a specific site in Cisco Catalyst Center.

        Args:
            site_id (str): The unique identifier of the site.

        Returns:
            list: A list of device IDs associated with the site.
                Returns an empty list if no devices are found or if an error occurs.
        """

        device_ids = []

        if self.dnac_version <= self.version_2_3_5_3:
            try:
                response = self.dnac._exec(
                    family="sites",
                    function="get_membership",
                    op_modifies=True,
                    params={"site_id": site_id},
                )

                if response and "device" in response:
                    for device in response.get("device", []):
                        for item in device.get("response", []):
                            device_ids.append(item.get("instanceUuid"))

                self.log("Retrieved device IDs from membership for site '{0}': {1}".format(site_id, device_ids), "DEBUG")

            except Exception as e:
                self.log("Error retrieving device IDs from membership for site '{0}': {1}".format(site_id, str(e)), "ERROR")

        else:
            try:
                response = self.dnac._exec(
                    family="site_design",
                    function="get_site_assigned_network_devices",
                    op_modifies=True,
                    params={"site_id": site_id},
                )

                if response and "response" in response:
                    for device in response.get("response", []):
                        device_ids.append(device.get("deviceId"))

                self.log("Retrieved device IDs from assigned devices for site '{0}': {1}".format(site_id, device_ids), "DEBUG")

            except Exception as e:
                self.log("Error retrieving device IDs from assigned devices for site '{0}': {1}".format(site_id, str(e)), "ERROR")

        if not device_ids:
            self.log("No devices found for site '{0}'".format(site_id), "INFO")

        return device_ids

    def get_site_id(self, site_name):
        """
        Retrieve the site ID and check if the site exists in Cisco Catalyst Center based on the provided site name.

        Args:
            - site_name (str): The name or hierarchy of the site to be retrieved.

        Returns:
            - tuple (bool, str or None): A tuple containing:
                1. A boolean indicating whether the site exists (True if found, False otherwise).
                2. The site ID (str) if the site exists, or None if the site does not exist or an error occurs.

        Criteria:
            - This function calls `get_site()` to retrieve site details from the Cisco Catalyst Center SDK.
            - If the site exists, its ID is extracted from the response and returned.
            - If the site does not exist or if an error occurs, an error message is logged, and the function returns a status of 'failed'.
        """

        try:
            response = self.get_site(site_name)
            if response is None:
                raise ValueError
            self.log("Received API response from 'get_site': {0}".format(str(response)), "DEBUG")
            site = response.get("response")
            site_id = site[0].get("id")
            site_exists = True

        except Exception as e:
            self.status = "failed"
            self.msg = ("An exception occurred: Site '{0}' does not exist in the Cisco Catalyst Center.".format(site_name))
            self.result['response'] = self.msg
            self.log(self.msg, "ERROR")
            self.check_return_status()

        return (site_exists, site_id)

    def get_site(self, site_name):
        """
        Retrieve site details from Cisco Catalyst Center based on the provided site name.
        Args:
            - site_name (str): The name or hierarchy of the site to be retrieved.
        Returns:
            - response (dict or None): The response from the API call, typically a dictionary containing site details.
                                    Returns None if an error occurs or if the response is empty.
        Criteria:
            - This function uses the Cisco Catalyst Center SDK to execute the 'get_sites' function from the 'site_design' family.
            - If the response is empty, a warning is logged.
            - Any exceptions during the API call are caught, logged as errors, and the function returns None.
        """

        if self.dnac_version <= self.version_2_3_5_3:
            try:
                response = self.dnac._exec(
                    family="sites",
                    function='get_site',
                    op_modifies=True,
                    params={"name": site_name},
                )

                if not response:
                    self.log("The response from 'get_site' is empty.", "WARNING")
                    return None

                self.log("Received API response from 'get_site': {0}".format(str(response)), "DEBUG")
                return response

            except Exception as e:
                self.log("An error occurred in 'get_site':{0}".format(e), "ERROR")
                return None

        else:
            try:
                response = self.dnac._exec(
                    family="site_design",
                    function='get_sites',
                    op_modifies=True,
                    params={"name_hierarchy": site_name},
                )

                if not response:
                    self.log("The response from 'get_sites' is empty.", "WARNING")
                    return None

                self.log("Received API response from 'get_sites': {0}".format(str(response)), "DEBUG")
                return response

            except Exception as e:
                self.log("An error occurred in 'get_sites':{0}".format(e), "ERROR")
                return None

    def assign_device_to_site(self, device_ids, site_name, site_id):
        """
        Assign devices to the specified site.

        Parameters:
            self (object): An instance of a class used for interacting with Cisco Catalyst Center.
            device_ids (list): A list of device IDs to assign to the specified site.
            site_name (str): The complete path of the site location.
            site_id (str): The ID of the specified site location.

        Returns:
            bool: True if the devices are successfully assigned to the site, otherwise False.

        Description:
            Assigns the specified devices to the site. If the assignment is successful, returns True.
            Otherwise, logs an error and returns False along with error details.
        """
        assign_network_device_to_site = {
            'deviceIds': device_ids,
            'siteId': site_id,
        }
        self.log("Assigning devices to site before update: {0}, {1}".
                 format(site_name, str(assign_network_device_to_site)), "INFO")
        try:
            response = self.dnac._exec(
                family="site_design",
                function='assign_network_devices_to_a_site',
                op_modifies=True,
                params=assign_network_device_to_site
            )
            self.log("Response from assigning devices to site: {0}, {1}, {2} .".format(
                site_name, str(assign_network_device_to_site), str(response["response"])), "INFO")

            self.check_tasks_response_status(response, api_name='assign_device_to_site')
            if self.result["changed"]:
                return True
            else:
                self.msg = "Failed to receive a valid response from site assignment API: {0}, {1}".format(site_name,
                                                                                                          str(assign_network_device_to_site))
                self.log(self.msg, "ERROR")
                self.status = "failed"
                self.module.fail_json(msg=self.msg)

        except Exception as e:
            msg = "Failed to assign devices to site: {0}, {1}.".format(site_name,
                                                                       str(assign_network_device_to_site))
            self.log(msg + str(e), "ERROR")
            site_assgin_details = str(e)
            self.status = "failed"
            self.module.fail_json(msg=msg, response=site_assgin_details)

    def generate_key(self):
        """
        Generate a new encryption key using Fernet.
        Returns:
            - key (bytes): A newly generated encryption key.
        Criteria:
            - This function should only be called if HAS_FERNET is True.
        """
        if HAS_FERNET:
            return {"generate_key": Fernet.generate_key()}
        else:
            error_message = "The 'cryptography' library is not installed. Please install it using 'pip install cryptography'."
            return {"error_message": error_message}

    def encrypt_password(self, password, key):
        """
        Encrypt a plaintext password using the provided encryption key.
        Args:
            - password (str): The plaintext password to be encrypted.
            - key (bytes): The encryption key used to encrypt the password.
        Returns:
            - encrypted_password (bytes): The encrypted password as bytes.
        Criteria:
            - This function should only be called if HAS_FERNET is True.
            - The password should be encoded to bytes before encryption.
        """
        try:
            fernet = Fernet(key)
            encrypted_password = fernet.encrypt(password.encode())
            return {"encrypt_password": encrypted_password}
        except Exception as e:
            return {"error_message": "Exception occurred while encrypting password: {0}".format(e)}

    def decrypt_password(self, encrypted_password, key):
        """
        Decrypt an encrypted password using the provided encryption key.
        Args:
            - encrypted_password (bytes): The encrypted password as bytes to be decrypted.
            - key (bytes): The encryption key used to decrypt the password.
        Returns:
            - decrypted_password (str): The decrypted plaintext password.
        Criteria:
            - This function should only be called if HAS_FERNET is True.
            - The encrypted password should be decoded from bytes after decryption.
        """
        try:
            fernet = Fernet(key)
            decrypted_password = fernet.decrypt(encrypted_password).decode()
            return {"decrypt_password": decrypted_password}
        except Exception.InvalidToken:
            return {"error_message": "Invalid decryption token."}
        except Exception as e:
            return {"error_message": "Exception occurred while decrypting password: {0}".format(e)}

    def camel_to_snake_case(self, config):
        """
        Convert camel case keys to snake case keys in the config.

        Parameters:
            config (list) - Playbook details provided by the user.

        Returns:
            new_config (list) - Updated config after eliminating the camel cases.
        """

        if isinstance(config, dict):
            new_config = {}
            for key, value in config.items():
                new_key = re.sub(r'([a-z0-9])([A-Z])', r'\1_\2', key).lower()
                if new_key != key:
                    self.log("{0} will be deprecated soon. Please use {1}.".format(key, new_key), "DEBUG")
                new_value = self.camel_to_snake_case(value)
                new_config[new_key] = new_value
        elif isinstance(config, list):
            return [self.camel_to_snake_case(item) for item in config]
        else:
            return config
        return new_config

    def update_site_type_key(self, config):
        """
        Replace 'site_type' key with 'type' in the config.

        Parameters:
            config (list or dict) - Configuration details.

        Returns:
            updated_config (list or dict) - Updated config after replacing the keys.
        """

        if isinstance(config, dict):
            new_config = {}
            for key, value in config.items():
                if key == "site_type":
                    new_key = "type"
                else:
                    new_key = re.sub(r'([a-z0-9])([A-Z])', r'\1_\2', key).lower()
                new_value = self.update_site_type_key(value)
                new_config[new_key] = new_value
        elif isinstance(config, list):
            return [self.update_site_type_key(item) for item in config]
        else:
            return config

        return new_config

    def is_valid_ipv4(self, ip_address):
        """
        Validates an IPv4 address.

        Parameters:
            ip_address - String denoting the IPv4 address passed.

        Returns:
            bool - Returns true if the passed IP address value is correct or it returns
            false if it is incorrect
        """

        try:
            socket.inet_aton(ip_address)
            octets = ip_address.split('.')
            if len(octets) != 4:
                return False
            for octet in octets:
                if not 0 <= int(octet) <= 255:
                    return False
            return True
        except socket.error:
            return False

    def is_valid_ipv6(self, ip_address):
        """
        Validates an IPv6 address.

        Parameters:
            ip_address - String denoting the IPv6 address passed.

        Returns:
            bool: True if the IPv6 address is valid, otherwise False
        """
        pattern = re.compile(r"""
            ^(([0-9a-fA-F]{1,4}:){7}([0-9a-fA-F]{1,4}|:))|
            (([0-9a-fA-F]{1,4}:){1,7}:)|
            (([0-9a-fA-F]{1,4}:){1,6}:[0-9a-fA-F]{1,4})|
            (([0-9a-fA-F]{1,4}:){1,5}(:[0-9a-fA-F]{1,4}){1,2})|
            (([0-9a-fA-F]{1,4}:){1,4}(:[0-9a-fA-F]{1,4}){1,3})|
            (([0-9a-fA-F]{1,4}:){1,3}(:[0-9a-fA-F]{1,4}){1,4})|
            (([0-9a-fA-F]{1,4}:){1,2}(:[0-9a-fA-F]{1,4}){1,5})|
            (([0-9a-fA-F]{1,4}:){1}(:[0-9a-fA-F]{1,4}){1,6})|
            (:((:[0-9a-fA-F]{1,4}){1,7}|:))|
            (fe80:(:[0-9a-fA-F]{0,4}){0,4}%[0-9a-zA-Z]{1,})|
            (::(ffff(:0{1,4}){0,1}:){0,1}(([0-9]{1,3}\.){3}[0-9]{1,3}))|
            (([0-9a-fA-F]{1,4}:){1,4}:(([0-9]{1,3}\.){3}[0-9]{1,3}))$
            """, re.VERBOSE | re.IGNORECASE)
        return pattern.match(ip_address) is not None

    def map_config_key_to_api_param(self, keymap=None, data=None):
        """
        Converts keys in a dictionary from CamelCase to snake_case and creates a keymap.

        Parameters:
            keymap (dict): Already existing key map dictionary to add to or empty dict {}.
            data (dict or list): Input data where keys need to be mapped using the key map.

        Returns:
            dict: A dictionary with the original keys as values and the converted snake_case
                    keys as keys.

        Example:
            functions = Accesspoint(module)
            keymap = functions.map_config_key_to_api_param(keymap, device_data)
        """

        if keymap is None:
            keymap = {}

        if isinstance(data, dict):
            keymap.update(keymap)

            for key, value in data.items():
                new_key = re.sub(r'([a-z0-9])([A-Z])', r'\1_\2', key).lower()
                keymap[new_key] = key

                if isinstance(value, dict):
                    self.map_config_key_to_api_param(keymap, value)
                elif isinstance(value, list):
                    for item in value:
                        if isinstance(item, dict):
                            self.map_config_key_to_api_param(keymap, item)

        elif isinstance(data, list):
            for item in data:
                if isinstance(item, dict):
                    self.map_config_key_to_api_param(keymap, item)

        return keymap

    def pprint(self, jsondata):
        """
        Pretty prints JSON/dictionary data in a readable format.

        Parameters:
            jsondata (dict): Dictionary data to be printed.

        Returns:
            str: Formatted JSON string.
        """
        try:
            return json.dumps(jsondata, indent=4, separators=(',', ': '))
        except (TypeError, ValueError) as e:
            raise TypeError("Invalid input for JSON serialization: {0}".format(str(e)))

    def check_status_api_events(self, status_execution_id):
        """
        Checks the status of API events in Cisco Catalyst Center until completion or timeout.
        Args:
            self (object): An instance of a class used for interacting with Cisco Catalyst Center.
            status_execution_id (str): The execution ID for the event to check the status.
        Returns:
            dict or None: The response from the API once the status is no longer "IN_PROGRESS",
                        or None if the maximum timeout is reached.
        Description:
            This method repeatedly checks the status of an API event in Cisco Catalyst Center using the provided
            execution ID. The status is checked at intervals specified by the 'dnac_task_poll_interval' parameter
            until the status is no longer "IN_PROGRESS" or the maximum timeout ('dnac_api_task_timeout') is reached.
            If the status becomes anything other than "IN_PROGRESS" before the timeout, the method returns the
            response from the API. If the timeout is reached first, the method logs a warning and returns None.
        """

        events_response = None
        start_time = time.time()

        while True:
            end_time = time.time()
            if (end_time - start_time) >= self.max_timeout:
                self.log("""Max timeout of {0} sec has reached for the execution id '{1}' for the event and unexpected
                        api status so moving out of the loop.""".format(self.max_timeout, status_execution_id), "WARNING")
                break
            # Now we check the status of API Events for configuring destination and notifications
            response = self.dnac._exec(
                family="event_management",
                function='get_status_api_for_events',
                op_modifies=True,
                params={"execution_id": status_execution_id}
            )
            self.log("Received API response from 'get_status_api_for_events': {0}".format(str(response)), "DEBUG")
            if response['apiStatus'] != "IN_PROGRESS":
                events_response = response
                break
            time.sleep(self.params.get('dnac_task_poll_interval'))

        return events_response

    def is_valid_server_address(self, server_address):
        """
        Validates the server address to check if it's a valid IPv4, IPv6 address, or a valid hostname.
        Args:
            self (object): An instance of a class used for interacting with Cisco Catalyst Center.
            server_address (str): The server address to validate.
        Returns:
            bool: True if the server address is valid, otherwise False.
        """
        # Check if the address is a valid IPv4 or IPv6 address
        try:
            ipaddress.ip_address(server_address)
            return True
        except ValueError:
            pass

        # Define the regex for a valid hostname
        hostname_regex = re.compile(
            r'^('  # Start of the string
            r'([A-Za-z0-9]+([A-Za-z0-9-]*[A-Za-z0-9])?\.)+[A-Za-z]{2,6}|'  # Domain name (e.g., example.com)
            r'localhost|'  # Localhost
            r'(\d{1,3}\.)+\d{1,3}|'  # Custom IPv4-like format (e.g., 2.2.3.31.3.4.4)
            r'[A-Fa-f0-9:]+$'  # IPv6 address (e.g., 2f8:192:3::40:41:41:42)
            r')$'  # End of the string
        )

        # Check if the address is a valid hostname
        if hostname_regex.match(server_address):
            return True

        return False

    def is_path_exists(self, file_path):
        """
        Check if the file path 'file_path' exists or not.

        Parameters:
            file_path (string) - Path of the provided file.

        Returns:
            True/False (bool) - True if the file path exists, else False.
        """

        current_working_directory = os.getcwd()
        final_file_path = os.path.join(current_working_directory, file_path)
        self.log(str(final_file_path))
        if not os.path.exists(final_file_path):
            self.log("The specified path '{0}' is not valid. Please provide a valid path.".format(final_file_path), "ERROR")
            return False

        return True

    def is_json(self, file_path):
        """
        Check if the file in the file path is JSON or not.

        Parameters:
            file_path (string) - Path of the provided file.

        Returns:
            True/False (bool) - True if the file is in JSON format, else False.
        """

        try:
            with open(file_path, 'r') as file:
                json.load(file)
                return True

        except (ValueError, FileNotFoundError):
            self.log("The provided file '{0}' is not in JSON format".format(file_path), "CRITICAL")
            return False

    def check_task_tree_response(self, task_id):
        """
        Returns the task tree response of the task ID.

        Parameters:
            task_id (string) - The unique identifier of the task for which you want to retrieve details.

        Returns:
            error_msg (str) - Returns the task tree error message of the task ID.
        """

        response = self.dnac._exec(
            family="task",
            function='get_task_tree',
            params={"task_id": task_id}
        )
        self.log("Retrieving task tree details by the API 'get_task_tree' using task ID: {task_id}, Response: {response}"
                 .format(task_id=task_id, response=response), "DEBUG")
        error_msg = ""
        if response and isinstance(response, dict):
            result = response.get('response')
            error_messages = []
            for item in result:
                if item.get("isError") is True:
                    error_messages.append(item.get("progress"))

            if error_messages:
                error_msg = ". ".join(error_messages) + "."

        return error_msg

    def get_task_details_by_id(self, task_id):
        """
        Get the details of a specific task in Cisco Catalyst Center.

        Args:
            self (object): An instance of a class that provides access to Cisco Catalyst Center.
            task_id (str): The unique identifier of the task for which you want to retrieve details.
        Returns:
            dict or None: A dictionary containing detailed information about the specified task,
            or None if the task with the given task_id is not found.
        Description:
            Call the API 'get_task_details_by_id' to get the details along with the
            failure reason. Return the details.
        """
        # Need to handle exception
        task_details = None
        try:
            response = self.dnac._exec(
                family="task",
                function="get_task_details_by_id",
                params={"id": task_id}
            )
            if not isinstance(response, dict):
                self.log("Invalid response received when fetching task details for task ID: {}".format(task_id), "ERROR")
                return task_details

            task_details = response.get("response")
            self.log("Task Details: {task_details}".format(task_details=task_details), "DEBUG")
        except Exception as e:
            # Log an error message and fail if an exception occurs
            self.log_traceback()
            self.msg = (
                "An error occurred while executing API call to Function: 'get_task_details_by_id' "
                "due to the the following exception: {0}.".format(str(e))
            )
            self.fail_and_exit(self.msg)
        return task_details

    def get_tasks_by_id(self, task_id):
        """
        Get the tasks of a task ID in Cisco Catalyst Center.

        Args:
            self (object): An instance of a class that provides access to Cisco Catalyst Center.
            task_id (str): The unique identifier of the task for which you want to retrieve details.
        Returns:
            dict or None: A dictionary status information about the specified task,
            or None if the task with the given task_id is not found.
        Description:
            Call the API 'get_tasks_by_id' to get the status of the task.
            Return the details along with the status of the task.
        """
        # Need to handle exception
        task_status = None
        try:
            response = self.dnac._exec(
                family="task",
                function="get_tasks_by_id",
                params={"id": task_id}
            )
            self.log('Task Details: {response}'.format(response=response), 'DEBUG')
            self.log("Retrieving task details by the API 'get_tasks_by_id' using task ID: {task_id}, Response: {response}"
                     .format(task_id=task_id, response=response), "DEBUG")

            if not isinstance(response, dict):
                self.log("Failed to retrieve task details for task ID: {}".format(task_id), "ERROR")
                return task_status

            task_status = response.get('response')
            self.log("Task Status: {task_status}".format(task_status=task_status), "DEBUG")
        except Exception as e:
            # Log an error message and fail if an exception occurs
            self.log_traceback()
            self.msg = (
                "An error occurred while executing API call to Function: 'get_tasks_by_id' "
                "due to the the following exception: {0}.".format(str(e))
            )
            self.fail_and_exit(self.msg)
        return task_status

    def check_tasks_response_status(self, response, api_name):
        """
        Get the task response status from taskId

        Parameters:
            self: The current object details.
            response (dict): API response.
            api_name (str): API name.
        Returns:
            self (object): The current object with updated desired Fabric Transits information.
        Description:
            Poll the function 'get_tasks_by_id' until it returns either 'SUCCESS' or 'FAILURE'
            state or till it reaches the maximum timeout.
            Log the task details and return self.
        """

        if not response:
            self.msg = "response is empty"
            self.status = "exited"
            return self

        if not isinstance(response, dict):
            self.msg = "response is not a dictionary"
            self.status = "exited"
            return self

        task_info = response.get("response")
        if task_info.get("errorcode") is not None:
            self.msg = response.get("response").get("detail")
            self.status = "failed"
            return self

        task_id = task_info.get("taskId")
        start_time = time.time()
        while True:
            elapsed_time = time.time() - start_time
            if elapsed_time >= self.max_timeout:
                self.msg = "Max timeout of {max_timeout} sec has reached for the task id '{task_id}'. " \
                           .format(max_timeout=self.max_timeout, task_id=task_id) + \
                           "Exiting the loop due to unexpected API '{api_name}' status.".format(api_name=api_name)
                self.log(self.msg, "WARNING")
                self.status = "failed"
                break

            task_details = self.get_tasks_by_id(task_id)
            self.log('Getting tasks details from task ID {task_id}: {task_details}'
                     .format(task_id=task_id, task_details=task_details), "DEBUG")

            task_status = task_details.get("status")
            if task_status == "FAILURE":
                details = self.get_task_details_by_id(task_id)
                self.msg = details.get("failureReason")
                self.status = "failed"
                break

            elif task_status == "SUCCESS":
                self.result["changed"] = True
                self.log("The task with task ID '{task_id}' is executed successfully."
                         .format(task_id=task_id), "INFO")
                break

            self.log("Progress is {status} for task ID: {task_id}"
                     .format(status=task_status, task_id=task_id), "DEBUG")

        return self

    def set_operation_result(self, operation_status, is_changed, status_message, log_level, additional_info=None):
        """
        Update the result of the operation with the provided status, message, and log level.
        Parameters:
            - operation_status (str): The status of the operation ("success" or "failed").
            - is_changed (bool): Indicates whether the operation caused changes.
            - status_message (str): The message describing the result of the operation.
            - log_level (str): The log level at which the message should be logged ("INFO", "ERROR", "CRITICAL", etc.).
            - additional_info (dict, optional): Additional data related to the operation result.
        Returns:
            self (object): An instance of the class.
        Note:
            - If the status is "failed", the "failed" key in the result dictionary will be set to True.
            - If data is provided, it will be included in the result dictionary.
        """
        # Update the result attributes with the provided values
        self.status = operation_status
        self.result.update({
            "status": operation_status,
            "msg": status_message,
            "response": status_message,
            "changed": is_changed,
            "failed": operation_status == "failed",
            "data": additional_info or {}  # Include additional_info if provided, else an empty dictionary
        })

        # Log the message at the specified log level
        self.log(status_message, log_level)

        return self

    def fail_and_exit(self, msg):
        """Helper method to update the result as failed and exit."""
        self.set_operation_result("failed", False, msg, "ERROR")
        self.check_return_status()

    def log_traceback(self):
        """
        Logs the full traceback of the current exception.
        """
        # Capture the full traceback
        full_traceback = traceback.format_exc()

        # Log the traceback
        self.log("Traceback: {0}".format(full_traceback), "DEBUG")

    def check_timeout_and_exit(self, loop_start_time, task_id, task_name):
        """
        Check if the elapsed time exceeds the specified timeout period and exit the while loop if it does.
        Parameters:
            - loop_start_time (float): The time when the while loop started.
            - task_id (str): ID of the task being monitored.
            - task_name (str): Name of the task being monitored.
        Returns:
            bool: True if the elapsed time exceeds the timeout period, False otherwise.
        """
        # If the elapsed time exceeds the timeout period
        elapsed_time = time.time() - loop_start_time
        if elapsed_time > self.params.get("dnac_api_task_timeout"):
            self.msg = "Task {0} with task id {1} has not completed within the timeout period of {2} seconds.".format(
                task_name, task_id, int(elapsed_time))

            # Update the result with failure status and log the error message
            self.set_operation_result("failed", False, self.msg, "ERROR")
            return True

        return False

    def get_taskid_post_api_call(self, api_family, api_function, api_parameters):
        """
        Executes the specified API call with given parameters and logs responses.

        Parameters:
            api_family (str): The API family (e.g., "sda").
            api_function (str): The API function (e.g., "add_port_assignments").
            api_parameters (dict): The parameters for the API call.
        """
        try:

            self.log("Requested payload for the the function: '{0}' is: '{1}'".format(api_function, api_parameters), "INFO")

            # Execute the API call
            response = self.dnac._exec(
                family=api_family,
                function=api_function,
                op_modifies=True,
                params=api_parameters,
            )

            self.log(
                "Response received from API call to Function: '{0}' from Family: '{1}' is Response: {2}".format(
                    api_function, api_family, str(response)
                ),
                "DEBUG"
            )

            # Process the response if available
            response_data = response.get("response")
            if not response_data:
                self.log(
                    "No response received from API call to Function: '{0}' from Family: '{1}'.".format(
                        api_function, api_family
                    ), "WARNING"
                )
                return None

            # Update result and extract task ID
            self.result.update(dict(response=response_data))
            task_id = response_data.get("taskId")
            self.log(
                "Task ID received from API call to Function: '{0}' from Family: '{1}', Task ID: {2}".format(
                    api_function, api_family, task_id
                ), "INFO"
            )
            return task_id

        except Exception as e:
            # Log an error message and fail if an exception occurs
            self.log_traceback()
            self.msg = (
                "An error occurred while executing API call to Function: '{0}' from Family: '{1}'. "
                "Parameters: {2}. Exception: {3}.".format(api_function, api_family, api_parameters, str(e))
            )
            self.fail_and_exit(self.msg)

    def get_task_status_from_tasks_by_id(self, task_id, task_name, success_msg):
        """
        Retrieves and monitors the status of a task by its task ID.

        This function continuously checks the status of a specified task using its task ID.
        If the task completes successfully, it updates the message and status accordingly.
        If the task fails or times out, it handles the error and updates the status and message.

        Parameters:
        - task_id (str): The unique identifier of the task to monitor.
        - task_name (str): The name of the task being monitored.
        - success_msg (str): The success message to set if the task completes successfully.

        Returns:
        - self: The instance of the class with updated status and message.
        """
        loop_start_time = time.time()

        while True:
            response = self.get_tasks_by_id(task_id)

            # Check if response is returned
            if not response:
                self.msg = "Error retrieving task status for '{0}' with task_id '{1}'".format(task_name, task_id)
                self.set_operation_result("failed", False, self.msg, "ERROR")
                break

            status = response.get("status")
            end_time = response.get("endTime")

            # Check if the elapsed time exceeds the timeout
            if self.check_timeout_and_exit(loop_start_time, task_id, task_name):
                break

            # Check if the task has completed (either success or failure)
            if end_time:
                if status == "FAILURE":
                    get_task_details_response = self.get_task_details_by_id(task_id)
                    failure_reason = get_task_details_response.get("failureReason")
                    if failure_reason:
                        self.msg = (
                            "Failed to execute the task {0} with Task ID: {1}."
                            "Failure reason: {2}".format(task_name, task_id, failure_reason)
                        )
                    else:
                        self.msg = (
                            "Failed to execute the task {0} with Task ID: {1}.".format(task_name, task_id)
                        ).format(task_name, task_id)
                    self.set_operation_result("failed", False, self.msg, "ERROR")
                    break
                elif status == "SUCCESS":
                    self.msg = success_msg
                    self.set_operation_result("success", True, self.msg, "INFO")
                    break

            time.sleep(self.params.get("dnac_task_poll_interval"))
        return self


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
            "length_max": 255 # Optional: maximum allowed length
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


def validate_integer_within_range(item, param_spec, param_name, invalid_params):
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
    try:
        item = validation.check_type_int(item)
    except TypeError as e:
        invalid_params.append("{0}: value: {1} {2}".format(param_name, item, str(e)))
        return item

    min_value = param_spec.get("range_min", 1)
    if param_spec.get("range_max") and not (min_value <= item <= param_spec["range_max"]):
        invalid_params.append(
            "{0}: {1} : The item exceeds the allowed range of min: {2} and max: {3}".format(
                param_name, item, param_spec.get("range_min"), param_spec.get("range_max"))
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
                "int": validate_integer_within_range,
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


RATE_LIMIT_MESSAGE = "Rate Limit exceeded"
RATE_LIMIT_RETRY_AFTER = 15


class DNACSDK(object):
    def __init__(self, params):
        self.result = dict(changed=False, result="")
        self.validate_response_schema = params.get("validate_response_schema")
        self.logger = logging.getLogger('dnacentersdk')
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
                self.logger.addHandler(logging.StreamHandler())
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
        family_name = family
        function_name = function
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

            if response and isinstance(response, dict) and response.get("executionId"):
                execution_id = response.get("executionId")
                exec_details_params = {"execution_id": execution_id}
                exec_details_func = getattr(
                    getattr(self.api, "task"), "get_business_api_execution_details"
                )

                while True:
                    execution_details = exec_details_func(**exec_details_params)
                    if execution_details.get("status") == "SUCCESS":
                        break

                    bapi_error = execution_details.get("bapiError")
                    if bapi_error:
                        if RATE_LIMIT_MESSAGE in bapi_error:
                            self.logger.warning("!!!!! %s !!!!!", RATE_LIMIT_MESSAGE)
                            time.sleep(RATE_LIMIT_RETRY_AFTER)
                            return self._exec(
                                family_name, function_name, params, op_modifies, **kwargs
                            )

                        self.logger.debug(bapi_error)
                        break

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
