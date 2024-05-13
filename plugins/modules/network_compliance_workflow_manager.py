#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright (c) 2024, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

"""Ansible module to perform Network Compliance Operations on devices in Cisco Catalyst Center."""
from __future__ import absolute_import, division, print_function

__metaclass__ = type
__author__ = ("Rugvedi Kapse, Madhan Sankaranarayanan")

DOCUMENTATION = r"""
---
module: network_compliance_workflow_manager
short_description: Network Compliance module for managing network compliance tasks on reachable device(s) in Cisco Catalyst Center.
description:
- Perform compliance checks or sync configurations on reachable devices using IP Address(s) or Site.
- API to perform full compliance checks or specific category checks on reachable device(s).
- API to sync device configuration on device(s).
version_added: "6.14.0"
extends_documentation_fragment:
  - cisco.dnac.workflow_manager_params
author: Rugvedi Kapse (@rukapse)
        Madhan Sankaranarayanan (@madhansansel)
options:
  config_verify:
    description: Set to True to verify the Cisco Catalyst Center config after applying the playbook config.
    type: bool
    default: False
  state:
    description: State of Cisco Catalyst Center after module completion.
    type: str
    choices: [ merged ]
    default: merged
  config:
    description: List of device details for running a compliance check or synchronizing device configuration.
    type: list
    elements: dict
    required: True
    suboptions:
      ip_address_list:
        description: List of IP addresses of devices to run a compliance check on or synchronize device configurations.
                     Either "ip_address_list" or "site_name" is required for module to execute.
                     If both "site_name" and "ip_address_list" are provided, operations are performed on devices that are present in both the
                     "ip_address_list" and the specified site.
                     (e.g. ["204.1.2.2", "204.1.2.5", "204.1.2.4"])
        type: list
        elements: str
      site_name:
        description: When "site_name" is specified, the module executes the operation on all the devices located within the specified site.
                     This is a string value that should represent the complete hierarchical path of the site.
                     Either "site_name" or "ip_address_list" is required for module to execute.
                     If both "site_name" and "ip_address_list" are provided, operations are performed on devices that are present in both the
                     "ip_address_list" and the specified site.
                     (e.g. "Global/USA/San Francisco/Building_2/floor_1")
        type: str
      run_compliance:
        description: Determines if a full compliance check should be triggered on the devices specified in the "ip_address_list" and/or "site_name".
                     if it is True then compliance will be triggered for all categories.
                     If it is False then compliance will be not be triggered even if run_compliance categories are provided.
        type: bool
        default: True
      run_compliance_categories:
        description: Specifying compliance categories allows you to trigger compliance checks only for the mentioned categories.
                     Category can have one or more values from among the options "INTENT", "RUNNING_CONFIG", "IMAGE", "PSIRT", "EOX", "NETWORK_SETTINGS".
                     Category "INTENT" is mapped to compliance types "NETWORK_SETTINGS", "NETWORK_PROFILE", "WORKFLOW", "FABRIC", "APPLICATION_VISIBILITY".
                     If "run_compliance" is False then compliance will be not be triggered even if "run_compliance_categories" are provided.
                     (e.g. ["INTENT", "RUNNING_CONFIG", "IMAGE", "PSIRT", "EOX", "NETWORK_SETTINGS"])
        type: list
        elements: str
      sync_device_config:
        description: Determines whether to synchronize the device configuration on the devices specified in the "ip_address_list" and/or "site_name".
                     Sync device configuration, primarily addresses the status of the `RUNNING_CONFIG`.
                     If set to True, and if `RUNNING_CONFIG` status is non-compliant this operation would commit device running configuration
                     to startup by issuing "write memory" to device.
        type: bool
        default: False

requirements:
- dnacentersdk == 2.7.0
- python >= 3.9
notes:
  - SDK Methods used are
    compliance.Compliance.run_compliance
    compliance.Compliance.commit_device_configuration
    task.Task.get_task_by_id
    task.Task.get_task_tree
    compliance.Compliance.get_compliance_detail

  - Paths used are
    post /dna/intent/api/v1/compliance/
    post /dna/intent/api/v1/network-device-config/write-memory
    get /dna/intent/api/v1/task/{taskId}
    get /dna/intent/api/v1/task/{taskId}/tree
    get /dna/intent/api/v1/compliance/detail
"""

EXAMPLES = r"""
- name: Run Compliance check on device(s) using IP address list (run_compliance by default is True)
  cisco.dnac.network_compliance_workflow_manager:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    dnac_log_level: "{{dnac_log_level}}"
    dnac_log: False
    config:
      - ip_address_list: ["204.1.2.2", "204.1.2.5", "204.1.2.4"]

- name: Run Compliance check on device(s) using IP address list
  cisco.dnac.network_compliance_workflow_manager:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    dnac_log_level: "{{dnac_log_level}}"
    dnac_log: False
    config:
      - ip_address_list: ["204.1.2.2", "204.1.2.5", "204.1.2.4"]
        run_compliance: True

- name: Run Compliance check on device(s) using Site
  cisco.dnac.network_compliance_workflow_manager:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    dnac_log_level: "{{dnac_log_level}}"
    dnac_log: False
    config:
      - site_name: "Global/USA/San Francisco/Building_1/floor_1"
        run_compliance: True

- name: Run Compliance check on device(s) using both IP address list and Site
  cisco.dnac.network_compliance_workflow_manager:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    dnac_log_level: "{{dnac_log_level}}"
    dnac_log: False
    config:
      - ip_address_list: ["204.1.2.2", "204.1.2.5", "204.1.2.4"]
        site_name: "Global/USA/San Francisco/Building_1/floor_1"
        run_compliance: True

- name: Run Compliance check with specific categories on device(s) using IP address list
  cisco.dnac.network_compliance_workflow_manager:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    dnac_log_level: "{{dnac_log_level}}"
    dnac_log: False
    config:
      - ip_address_list: ["204.1.2.2", "204.1.2.5", "204.1.2.4"]
        run_compliance: True
        run_compliance_categories: ["INTENT", "RUNNING_CONFIG", "IMAGE", "PSIRT"]

- name: Run Compliance check with specific categories on device(s) using Site
  cisco.dnac.network_compliance_workflow_manager:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    dnac_log_level: "{{dnac_log_level}}"
    dnac_log: False
    config:
      - site_name: "Global/USA/San Francisco/Building_1/floor_1"
        run_compliance: True
        run_compliance_categories: ["INTENT", "RUNNING_CONFIG", "IMAGE", "PSIRT"]

- name: Run Compliance check with specific categories on device(s) using both IP address list and Site
  cisco.dnac.network_compliance_workflow_manager:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    dnac_log_level: "{{dnac_log_level}}"
    dnac_log: False
    config:
      - ip_address_list: ["204.1.2.2", "204.1.2.5", "204.1.2.4"]
        site_name: "Global/USA/San Francisco/Building_1/floor_1"
        run_compliance: True
        run_compliance_categories: ["INTENT", "RUNNING_CONFIG", "IMAGE", "PSIRT"]

- name: Sync Device Configuration on device(s) using IP address list
  cisco.dnac.network_compliance_workflow_manager:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    dnac_log_level: "{{dnac_log_level}}"
    dnac_log: False
    config:
      - site_name: "Global"
        sync_device_config: True
        run_compliance: False

- name: Sync Device Configuration on device(s) using Site
  cisco.dnac.network_compliance_workflow_manager:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    dnac_log_level: "{{dnac_log_level}}"
    dnac_log: False
    config:
      - site_name: "Global/USA/San Francisco/Building_1/floor_1"
        sync_device_config: True
        run_compliance: False

- name: Sync Device Configuration on device(s) using both IP address list and Site
  cisco.dnac.network_compliance_workflow_manager:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    dnac_log_level: "{{dnac_log_level}}"
    dnac_log: False
    config:
      - ip_address_list: ["204.1.2.2", "204.1.2.5", "204.1.2.4"]
        site_name: "Global/USA/San Francisco/Building_1/floor_1"
        sync_device_config: True
        run_compliance: False

- name: Run Compliance and Sync Device Configuration using both IP address list and Site
  cisco.dnac.network_compliance_workflow_manager:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    dnac_log_level: "{{dnac_log_level}}"
    dnac_log: False
    config:
      - ip_address_list: ["204.1.2.2", "204.1.2.5", "204.1.2.4"]
        site_name: "Global/USA/San Francisco/Building_1/floor_1"
        run_compliance: True
        run_compliance_categories: ["INTENT", "RUNNING_CONFIG", "IMAGE", "PSIRT"]
        sync_device_config: True
"""

RETURN = r"""
#Case_1: Response when Network Compliance operations are performed successfully on device/s.
sample_response_2:
  description: A dictionary with the response returned by the Cisco Catalyst Center Python SDK
  returned: always
  type: dict
  sample: >
    {
      "status": "string",
      "changed": bool,
      "msg": "string"
      "response": {
        "taskId": "string",
        "url": "string"
      },
      "version": "string"
    }

#Case_2: Response when Error Occurs in performing Run Compliance or Sync Device Configuration operation on device/s.
sample_response_3:
  description: A dictionary with the response returned by the Cisco Catalyst Center Python SDK
  returned: always
  type: dict
  sample: >
    {
      "changed": bool,
      "msg": "string"
    }
"""

import time
from ansible.module_utils.basic import AnsibleModule
from ansible_collections.cisco.dnac.plugins.module_utils.dnac import (
    DnacBase,
    validate_list_of_dicts
)


class NetworkCompliance(DnacBase):
    """Class containing member attributes for network_compliance_workflow_manager module"""

    def __init__(self, module):
        """
        Initialize an instance of the class.
        Parameters:
          - module: The module associated with the class instance.
        Returns:
          The method does not return a value.
        """

        super().__init__(module)

    def validate_input(self):
        """
        Validate the fields provided in the playbook against a predefined specification
        to ensure they adhere to the expected structure and data types.
        Parameters:
            state (optional): A state parameter that can be used to customize validation
                              based on different conditions.
        Returns:
            object: An instance of the class with updated attributes:
              - self.msg: A message describing the validation result.
              - self.status: The status of the validation (either "success" or "failed").
              - self.validated_config: If successful, a validated version of the "config" parameter.
        Description:
            This method validates the fields provided in the playbook against a predefined specification.
            It checks if the required fields are present and if their data types match the expected types.
            If any parameter is found to be invalid, it logs an error message and sets the validation status to "failed".
            If the validation is successful, it logs a success message and returns an instance of the class
            with the validated configuration.
        """

        if not self.config:
            self.msg = "config not available in playbook for validation"
            self.status = "success"
            self.log(self.msg, "ERROR")
            return self

        temp_spec = {
            "ip_address_list": {"type": "list", "elements": "str", "required": False},
            "site_name": {"type": "str", "required": False},
            "run_compliance": {"type": "bool", "required": False, "default": True},
            "run_compliance_categories": {"type": "list", "elements": "str", "required": False},
            "sync_device_config": {"type": "bool", "required": False, "default": False},
        }

        # Validate device params
        valid_temp, invalid_params = validate_list_of_dicts(
            self.config, temp_spec
        )

        if invalid_params:
            self.msg = "Invalid parameters in playbook: {0}".format(invalid_params)
            self.log(self.msg, "ERROR")
            self.status = "failed"
            return self

        self.validated_config = valid_temp

        self.msg = "Successfully validated playbook configuration parameters using 'validated_input': {0}".format(str(valid_temp))
        self.log(self.msg, "INFO")
        self.status = "success"

        return self

    def validate_ip4_address_list(self, ip_address_list):
        """
        Validates the list of IPv4 addresses provided in the playbook.
        Parameters:
            ip_address_list (list): A list of IPv4 addresses to be validated.
        Description:
            This method iterates through each IP address in the list and checks if it is a valid IPv4 address.
            If any address is found to be invalid, it logs an error message and fails.
            After validating all IP addresses, it logs a success message.
        """

        for ip in ip_address_list:
            if not self.is_valid_ipv4(ip):
                self.msg = "IP address {0} is not valid".format(ip)
                self.log(self.msg, "ERROR")
                self.module.fail_json(self.msg)

        self.log("Successfully validated the IP address/es: {0}".format(ip_address_list), "DEBUG")

    def validate_run_compliance_paramters(self, mgmt_ip_instance_id_map, run_compliance, run_compliance_categories):
        """
        Validate and prepare parameters for running compliance checks.
        Parameters:
            - mgmt_ip_instance_id_map (dict): A dictionary mapping management IP addresses to device instance IDs.
            - run_compliance (bool or None): A boolean indicating whether to run compliance checks.
            - run_compliance_categories (list): A list of compliance categories to check.
        Returns:
        tuple: A tuple containing two dictionaries:
            - run_compliance_params: Parameters for running compliance checks.
            - compliance_detail_params: Parameters for compliance detail.
        Notes:
            - This method prepares parameters for running compliance checks based on the provided inputs.
            - If invalid categories are provided in `run_compliance_categories`, a `ValueError` is raised.
            - If `run_compliance_categories` is provided and neither `run_compliance` nor `run_compliance_categories` is set, an error
              is logged and the method fails.
            - If `run_compliance` is set and `run_compliance_categories` is not, full compliance checks are triggered.
            - If both `run_compliance` and `run_compliance_categories` are set, compliance checks are triggered for specific categories.
        """
        run_compliance_params = {}
        compliance_detail_params = {}
        valid_categories = ["INTENT", "RUNNING_CONFIG", "IMAGE", "PSIRT", "EOX", "NETWORK_SETTINGS"]

        if run_compliance_categories:
            # Validate the categories provided
            if not all(category.upper() in valid_categories for category in run_compliance_categories):
                msg = "Invalid category provided. Valid categories are {0}.".format(valid_categories)
                self.log(msg, "ERROR")
                self.module.fail_json(msg)

            if run_compliance:
                # run_compliance_params
                run_compliance_params["deviceUuids"] = list(mgmt_ip_instance_id_map.values())
                run_compliance_params["triggerFull"] = False
                categories_copy = run_compliance_categories.copy()
                run_compliance_params["categories"] = categories_copy

                # compliance_detail_params
                compliance_detail_params["deviceUuids"] = ",".join(list(mgmt_ip_instance_id_map.values()))
                compliance_types = run_compliance_categories
                if "INTENT" in compliance_types:
                    compliance_types.remove("INTENT")
                    compliance_types.extend(["NETWORK_PROFILE", "APPLICATION_VISIBILITY", "WORKFLOW", "FABRIC", "NETWORK_SETTINGS"])
                compliance_types = list(set(compliance_types))
                compliance_detail_params["complianceType"] = "', '".join(compliance_types)
                compliance_detail_params["complianceType"] = "'" + compliance_detail_params['complianceType'] + "'"
            # Case when run_compliance_categories provided but run_compliance = False
            else:
                msg = "Since run_compliance is set to {0}, even though run_compliance_categories are provided {1}, ".format(
                    run_compliance, run_compliance_categories)
                msg += "Run Compliance Check will not be executed."
                self.log(msg, "WARNING")

        elif run_compliance:
            # run_compliance_params
            run_compliance_params["deviceUuids"] = list(mgmt_ip_instance_id_map.values())
            run_compliance_params["triggerFull"] = True

            # compliance_detail_params
            compliance_detail_params["deviceUuids"] = ",".join(list(mgmt_ip_instance_id_map.values()))

        return run_compliance_params, compliance_detail_params

    def site_exists(self, site_name):
        """
        Checks the existence of a site in Cisco Catalyst Center.
        Parameters:
            site_name (str): The name of the site to be checked.
        Returns:
            tuple: A tuple containing two values:
                - site_exists (bool): Indicates whether the site exists (True) or not (False).
                - site_id (str or None): The ID of the site if it exists, or None if the site is not found.
        Description:
            This method queries Cisco Catalyst Center to determine if a site with the provided name exists.
            If the site is found, it sets "site_exists" to True and retrieves the site"s ID.
            If the site does not exist, "site_exists" is set to False, and "site_id" is None.
            If an exception occurs during the site lookup, an error message is logged, and the module fails.
        """

        site_exists = False
        site_id = None
        response = None

        # Attempt to retrieve site information from Catalyst Center
        try:
            response = self.dnac._exec(
                family="sites",
                function="get_site",
                op_modifies=True,
                params={"name": site_name},
            )
            self.log("Response received post 'get_site' API call: {0}".format(str(response)), "DEBUG")

            # Process the response if available
            if response:
                site = response.get("response")
                site_id = site[0].get("id")
                site_exists = True
            else:
                self.log("No response received from the 'get_site' API call.", "ERROR")

        except Exception as e:
            # Log an error message and fail if an exception occurs
            self.log("An error occurred while retrieving site details for Site '{0}' using 'get_site' API call: {1}".format(site_name, str(e)), "ERROR")

        if not site_exists:
            msg = "An error occurred while retrieving site details for Site '{0}'. Please verify that the site exists.".format(site_name)
            self.log(msg, "ERROR")
            self.module.fail_json(msg=msg)

        return (site_exists, site_id)

    def get_device_ids_from_ip(self, ip_address_list):
        """
        Retrieves the device IDs based on the provided list of IP addresses from Cisco Catalyst Center.
        Parameters:
            ip_address_list (list): A list of IP addresses of devices for which you want to retrieve the device IDs.
        Returns:
            dict: A dictionary mapping management IP addresses to their instance UUIDs.
        Description:
            This method queries Cisco Catalyst Center for device information using the provided IP addresses.
            For each IP address in the list, it attempts to fetch the device information using the "get_device_list" API.
            If the device is found and reachable, it extracts the device ID and maps it to the corresponding IP address.
            If any error occurs during the process, it logs an error message and continues to the next IP address.
        """

        mgmt_ip_instance_id_map = {}

        # Iterate through the provided list of IP addresses
        for device_ip in ip_address_list:
            try:
                # Query Cisco Catalyst Center for device information using the IP address
                response = self.dnac._exec(
                    family="devices",
                    function="get_device_list",
                    op_modifies=True,
                    params={"managementIpAddress": device_ip}
                )
                self.log("Response received post 'get_device_list' API call: {0} ".format(str(response)), "DEBUG")

                # Check if a valid response is received
                if response.get("response"):
                    response = response.get("response")
                    if not response:
                        continue
                    for device_info in response:
                        if device_info["reachabilityStatus"] == "Reachable":
                            device_id = response[0]["id"]
                            mgmt_ip_instance_id_map[device_ip] = device_id
                else:
                    # If unable to retrieve device information, log an error message
                    self.log("Unable to retrieve device information for {0}. Please ensure that the device exists and is reachable.".format(device_ip), "ERROR")

            except Exception as e:
                # Log an error message if any exception occurs during the process
                self.log("Error while fetching device ID for device: '{0}' from Cisco Catalyst Center: {1}".format(device_ip, str(e)), "ERROR")

        if not mgmt_ip_instance_id_map:
            msg = "Error occurred while retrieving device details (Device UUID) using the 'get_device_list' API "
            msg += "for the following device(s): {0}".format(ip_address_list)
            self.log(msg, "ERROR")
            self.module.fail_json(msg=msg)

        return mgmt_ip_instance_id_map

    def get_device_ids_from_site(self, site_name, site_id):
        """
        Retrieves the management IP addresses and their corresponding instance UUIDs of devices associated with a specific site in Cisco Catalyst Center.

        Parameters:
            site_name (str): The name of the site whose devices" information is to be retrieved.
            site_id (str): The unique identifier of the site.

        Returns:
            dict: A dictionary mapping management IP addresses to their instance UUIDs.

        Description:
            This method queries Cisco Catalyst Center to fetch the list of devices associated with the provided site.
            It then extracts the management IP addresses and their instance UUIDs from the response.
            Devices that are not reachable are logged as critical errors, and the function fails.
            If no reachable devices are found for the specified site, it logs an error message and fails.

        """
        mgmt_ip_instance_id_map = {}

        site_params = {
            "site_id": site_id,
        }

        # Attempt to retrieve device information associated with the site
        try:
            response = self.dnac._exec(
                family="sites",
                function="get_membership",
                op_modifies=True,
                params=site_params,
            )
            self.log("Response received post 'get_membership' API Call: {0} ".format(str(response)), "DEBUG")

            # Process the response if available
            if response:
                response = response["device"]
                # Iterate over the devices in the site membership
                for item in response:
                    if item["response"]:
                        for item_dict in item["response"]:
                            # Check if the device is reachable
                            if item_dict["reachabilityStatus"] == "Reachable":
                                mgmt_ip_instance_id_map[item_dict["managementIpAddress"]] = item_dict["instanceUuid"]
                            else:
                                msg = "Unable to get deviceId  for device {0} in site {1} as its status is {2}".format(
                                    item["managementIpAddress"], site_name, item["reachabilityStatus"])
                                self.log(msg, "CRITICAL")
                                self.module.fail_json(msg=msg)
            else:
                # If unable to retrieve device information, log an error message
                self.log("No response received from API call to get membership information for site. {0}".format(site_name), "ERROR")

        except Exception as e:
            # Log an error message if any exception occurs during the process
            self.log("Unable to fetch the device(s) associated to the site '{0}' due to {1}".format(site_name, str(e)), "ERROR")

        if not mgmt_ip_instance_id_map:
            msg = "Error retrieving device details using the 'get_membership' API from Site: {0}".format(site_name)
            self.log(msg, "ERROR")
            self.module.fail_json(msg=msg)

        return mgmt_ip_instance_id_map

    def get_device_id_list(self, ip_address_list, site_name):
        """
        Get the list of unique device IDs for a specified list of management IP addresses or devices associated with a site
        in Cisco Catalyst Center.
        Parameters:
            ip_address_list (list): The management IP addresses of devices for which you want to retrieve the device IDs.
            site_name (str): The name of the site for which you want to retrieve the device IDs.
        Returns:
            dict: A dictionary mapping management IP addresses to device IDs for the specified devices.
        Description:
            This method queries Cisco Catalyst Center to retrieve the unique device IDs associated with devices having the
            specified IP addresses or belonging to the specified site.
        """

        # Initialize a dictionary to store management IP addresses and their corresponding device IDs
        mgmt_ip_instance_id_map = {}

        # Check if both site name and IP address list are provided
        if site_name:
            (site_exists, site_id) = self.site_exists(site_name)
            if site_exists:
                # Retrieve device IDs associated with devices in the site
                site_mgmt_ip_instance_id_map = self.get_device_ids_from_site(site_name, site_id)
                mgmt_ip_instance_id_map.update(site_mgmt_ip_instance_id_map)

        if ip_address_list:
            # Retrieve device IDs associated with devices having specified IP addresses
            iplist_mgmt_ip_instance_id_map = self.get_device_ids_from_ip(ip_address_list)
            mgmt_ip_instance_id_map.update(iplist_mgmt_ip_instance_id_map)

        return mgmt_ip_instance_id_map

    def is_sync_required(self, modified_response, mgmt_ip_instance_id_map):
        """
        Determine if synchronization of device configurations is required.

        Args:
            modified_response (dict): A dictionary containing modified responses for each device.
            mgmt_ip_instance_id_map (dict): A dictionary mapping management IP addresses to instance IDs.

        Returns:
            tuple: A tuple containing a boolean indicating whether synchronization is required
                   and a message explaining the result.

        Note:
            This method categorizes devices based on compliance status ("COMPLIANT", "NON_COMPLIANT", "OTHER")
            and checks if synchronization is necessary. If all devices are "COMPLIANT", synchronization is not
            required. If there are devices that are not "NON_COMPLIANT", synchronization is also not required.
        """
        task_name = "Sync Device Configuration"
        required = True
        msg = ""

        # Validate if sync is required
        self.log("Compliance Report for {0} operation for device(s) {1} : {2}".format(
            task_name, list(mgmt_ip_instance_id_map.keys()), modified_response), "INFO")

        # Categorize the devices based on status - "COMPLIANT", "NON_COMPLIANT", "OTHER"(status other than COMPLIANT and NON_COMPLIANT)
        categorized_devices = {"COMPLIANT": {}, "NON_COMPLIANT": {}, "OTHER": {}}
        for ip_address, compliance_type in modified_response.items():
            status = compliance_type[0]["status"]
            if status == "NON_COMPLIANT":
                categorized_devices["NON_COMPLIANT"][ip_address] = compliance_type
            elif status == "COMPLIANT":
                categorized_devices["COMPLIANT"][ip_address] = compliance_type
            else:
                categorized_devices["OTHER"][ip_address] = compliance_type

        self.log("Devices Categorized based on Compliance status: {0}".format(categorized_devices), "INFO")

        # Validate if all devices are "COMPLIANT" - then sync not required
        if len(categorized_devices["COMPLIANT"]) == len(mgmt_ip_instance_id_map):
            msg = "Device(s) {0} are already compliant with the RUNNING_CONFIG compliance type. Therefore, {1} is not required.".format(
                list(mgmt_ip_instance_id_map.keys()), task_name)
            required = False
        elif len(categorized_devices["NON_COMPLIANT"]) != len(mgmt_ip_instance_id_map):
            required = False
            msg = ("The operation {0} cannot be performed on one or more of the devices "
                   "{1} because the status of the RUNNING_CONFIG compliance type is not "
                   "as expected; it should be NON_COMPLIANT."
                   ).format(task_name, list(mgmt_ip_instance_id_map.keys()))

        return required, msg

    def get_want(self, config):
        """
        Determines the desired state based on the provided configuration.
        Parameters:
            config (dict): The configuration specifying the desired state.
        Returns:
            dict: A dictionary containing the desired state parameters.
        Description:
            This method processes the provided configuration to determine the desired state. It validates the presence of
            either "ip_address_list" or "site_name" and constructs parameters for running compliance checks and syncing
            device configurations based on the provided configuration. It also logs the desired state for reference.
        """

        # Initialize parameters
        run_compliance_params = {}
        sync_device_config_params = {}
        compliance_detail_params = {}
        compliance_detail_params_sync = {}
        compliance_details = {}

        # Store input parameters
        ip_address_list = config.get("ip_address_list")
        site_name = config.get("site_name")
        run_compliance = config.get("run_compliance")
        run_compliance_categories = config.get("run_compliance_categories")
        sync_device_config = config.get("sync_device_config")

        # Validate either ip_address_list OR site_name is present
        if not any([ip_address_list, site_name]):
            msg = "ip_address_list is {0} and site_name is {1}. Either the ip_address_list or the site_name must be provided.".format(
                ip_address_list, site_name)
            self.log(msg, "ERROR")
            self.module.fail_json(msg=msg)

        # Validate if a network compliance operation is present
        if not any([run_compliance, run_compliance_categories, sync_device_config]):
            msg = "No actions were requested. This network compliance module can perform the following tasks: Run Compliance Check or Sync Device Config."
            self.log(msg, "ERROR")
            self.module.fail_json(msg)
            return self

        # Validate valid ip_addresses
        if ip_address_list:
            self.validate_ip4_address_list(ip_address_list)
            # Remove Duplicates from list
            ip_address_list = list(set(ip_address_list))

        # Retrieve device ID list
        mgmt_ip_instance_id_map = self.get_device_id_list(ip_address_list, site_name)
        if not mgmt_ip_instance_id_map:
            # Log an error message if mgmt_ip_instance_id_map is empty
            msg = "Failed to retrieve device IDs for the provided IP addresses: {0} or site name: {1}.".format(ip_address_list, site_name)
            self.log(msg, "ERROR")
            self.module.fail_json(msg)

        # Run Compliance Paramters
        run_compliance_params, compliance_detail_params = self.validate_run_compliance_paramters(
            mgmt_ip_instance_id_map, run_compliance, run_compliance_categories)

        # Sync Device Configuration Parameters
        if sync_device_config:
            sync_device_config_params = {
                "deviceId": list(mgmt_ip_instance_id_map.values())
            }

            compliance_detail_params_sync = {
                "deviceUuid": ",".join(list(mgmt_ip_instance_id_map.values())),
                "complianceType": "RUNNING_CONFIG"
            }

            # Validate if Sync Device Configuration is required on the device(s)
            response = self.get_compliance_detail(compliance_detail_params_sync)
            if not response:
                msg = "Error occurred when retrieving Compliance Report to identify if Sync Device Config Operation "
                msg += "is required on device(s): {0}".format(list(mgmt_ip_instance_id_map.keys()))
                self.log(msg)
                self.module.fail_json(msg)

            compliance_details = self.modify_compliance_response(response, mgmt_ip_instance_id_map)
            required, msg = self.is_sync_required(compliance_details, mgmt_ip_instance_id_map)
            if not required:
                self.log(msg, "ERROR")
                self.module.fail_json(msg)

        # Construct the "want" dictionary containing the desired state parameters
        want = {}
        want = dict(
            ip_address_list=ip_address_list,
            site_name=site_name,
            mgmt_ip_instance_id_map=mgmt_ip_instance_id_map,
            run_compliance_params=run_compliance_params,
            sync_device_config_params=sync_device_config_params,
            compliance_detail_params=compliance_detail_params,
            compliance_detail_params_sync=compliance_detail_params_sync,
            compliance_details=compliance_details
        )
        self.want = want
        self.log("Desired State (want): {0}".format(str(self.want)), "INFO")

        return self

    def get_compliance_detail(self, compliance_detail_params):
        """
        Execute the GET compliance detail operation.
        Args:
            compliance_detail_params (dict): A dictionary containing parameters for the compliance detail operation.
        Returns:
            dict: A dictionary containing details of the compliance detail response.
            Returns None if there is an error.
        """
        # Execute the GET compliance detial operation
        try:
            response = self.dnac_apply["exec"](
                family="compliance",
                function="get_compliance_detail",
                params=compliance_detail_params,
                op_modifies=True
            )
            self.log("Response received post 'get_compliance_detail' API call: {0}".format(str(response)), "DEBUG")

            if response:
                response = response.response
            else:
                self.log("No response received from the 'get_compliance_detail' API call.", "ERROR")
            return response

        # Log and handle any exceptions that occur during the execution
        except Exception as e:
            self.msg = "An error occurred while retrieving Compliance Details using 'get_compliance_detail' API call "
            self.msg += "for {0}: {1}".format(compliance_detail_params, str(e))
            self.update_result("failed", False, self.msg, "ERROR")
            self.check_return_status()

    def modify_compliance_response(self, response, mgmt_ip_instance_id_map):
        """
        Modifies the compliance response by mapping device UUIDs to management IP addresses.
        Parameters:
            response (list of dict): The original compliance response.
            mgmt_ip_instance_id_map (dict): Mapping of management IP addresses to instance IDs.
        Returns:
            dict: Modified compliance response with management IP addresses as keys.
        Description:
            This method takes the original compliance response and maps device UUIDs to their corresponding management
            IP addresses using the provided mapping. It then constructs a modified response where each IP address is a key
            associated with a list of compliance items related to that device.
        """
        modified_response = {}
        ip_address = None

        for item in response:
            device_uuid = item.get("deviceUuid")

            # Find the corresponding management IP address for the device UUID
            for ip, uuid in mgmt_ip_instance_id_map.items():
                if uuid == device_uuid:
                    ip_address = ip
                    break

            # If the IP address is found, add the item to the modified response
            # If ip_address and item.get("status")!= "NOT_APPLICABLE":
            if ip_address:
                if ip_address not in modified_response:
                    modified_response[ip_address] = []
                modified_response[ip_address].append(item)

        return modified_response

    def run_compliance(self, run_compliance_params):
        """
        Executes a compliance check operation in Cisco DNA Center.
        Parameters:
            run_compliance_params (dict): Parameters for running the compliance check.
        Returns:
            str or None: Task ID of the API task created, or None if unsuccessful.
        Description:
            This method initiates a compliance check operation in Cisco DNA Center by calling the "run_compliance" function
            from the "compliance" family of APIs. It passes the provided parameters and updates the result accordingly.
        """

        # Execute the compliance check operation
        try:
            response = self.dnac_apply["exec"](
                family="compliance",
                function="run_compliance",
                params=run_compliance_params,
                op_modifies=True,
            )
            self.log("Response received post 'run_compliancee' API call is {0}".format(str(response)), "DEBUG")

            if response:
                self.result.update(dict(response=response["response"]))
                self.log("Task Id for the 'run_compliance' task  is {0}".format(response.response.get("taskId")), "INFO")
                return response.response.get("taskId")
            else:
                self.log("No response received from the 'run_compliance' API call.", "ERROR")
                return None

        # Log and handle any exceptions that occur during the execution
        except Exception as e:
            self.msg = "An error occurred while executing the 'run_compliance' operation for {0}: {1}".format(run_compliance_params, str(e))
            self.update_result("failed", False, self.msg, "ERROR")
            self.check_return_status()

    def sync_device_config(self, sync_device_config_params):
        """
        Synchronize the device configuration using the specified parameters.
        Parameters:
            - sync_device_config_params (dict): Parameters for synchronizing the device configuration.
        Returns:
            task_id (str): The ID of the task created for the synchronization operation.
        Note:
            This method initiates the synchronization of device configurations by making an API call to the Cisco DNA Center.
            It logs the response received from the API call and extracts the task ID from the response for further monitoring.
            If an error occurs during the API call, it will be caught and logged.
        """
        # Make an API call to synchronize device configuration
        try:
            response = self.dnac_apply["exec"](
                family="compliance",
                function="commit_device_configuration",
                params=sync_device_config_params,
                op_modifies=True,
            )
            self.log("Response received post 'commit_device_configuration' API call is {0}".format(str(response)), "DEBUG")

            if response:
                self.result.update(dict(response=response["response"]))
                self.log("Task Id for the 'commit_device_configuration' task  is {0}".format(response.response.get("taskId")), "INFO")
                # Return the task ID
                return response.response.get("taskId")
            else:
                self.log("No response received from the 'commit_device_configuration' API call.", "ERROR")
                return None

        # Log the error if an exception occurs during the API call
        except Exception as e:
            self.msg = "Error occurred while synchronizing device configuration for {0}: {1}".format(sync_device_config_params, str(e))
            self.update_result("failed", False, self.msg, "ERROR")
            self.check_return_status()

    def get_task_status(self, task_id, task_name):
        """
        Retrieve the status of a task by its ID.
        Parameters:
            - task_id (str): The ID of the task whose status is to be retrieved.
            - task_name (str): The name of the task.
        Returns:
            response (dict): The response containing the status of the task.
        Note:
            This method makes an API call to retrieve the task status and logs the status information.
            If an error occurs during the API call, it will be caught and logged.
        """

        # Make an API call to retrieve the task tree
        try:
            response = self.dnac_apply["exec"](
                family="task",
                function="get_task_by_id",
                params=dict(task_id=task_id),
                op_modifies=True,
            )
            self.log("Response received post 'get_task_by_id' API Call for the Task {0} with Task id {1} "
                     "is {2}".format(task_name, str(task_id), str(response)), "DEBUG")

            if response:
                response = response.response
            else:
                self.log("No response received from the 'get_task_by_id' API call.", "CRITICAL")
            return response

        # Log the error if an exception occurs during the API call
        except Exception as e:
            self.msg = "Error occurred while retrieving 'get_task_by_id' for Task {0} with Task id {1}: {2}".format(task_name, task_id, str(e))
            self.update_result("failed", False, self.msg, "ERROR")
            self.check_return_status()

    def get_task_tree(self, task_id, task_name):
        """
        Retrieve the tree of a task by its ID.
        Parameters:
            - task_id (str): The ID of the task whose status is to be retrieved.
            - task_name (str): The name of the task.
        Returns:
            response (dict): The response containing the status of the task.
        Note:
            This method makes an API call to retrieve the task status and logs the status information.
            If an error occurs during the API call, it will be caught and logged.
        """

        # Make an API call to retrieve the task status
        try:
            response = self.dnac_apply["exec"](
                family="task",
                function="get_task_tree",
                params=dict(task_id=task_id),
                op_modifies=True,
            )
            self.log("Response received post 'get_task_tree' API call for the Task {0} with Task id {1} "
                     "is {2}".format(task_name, str(task_id), str(response)), "DEBUG")
            if response:
                response = response.response
            else:
                self.log("No response received from the 'get_task_tree' API call.", "CRITICAL")
            return response

        # Log the error if an exception occurs during the API call
        except Exception as e:
            self.msg = "Error occurred while retrieving 'get_task_tree' for Task {0} with task id {1}: {2}".format(task_name, task_id, str(e))
            self.update_result("failed", False, self.msg, "ERROR")
            self.check_return_status()

    def update_result(self, status, changed, msg, log_level, data=None):
        """
        Update the result of the operation with the provided status, message, and log level.
        Parameters:
            - status (str): The status of the operation ("success" or "failed").
            - changed (bool): Indicates whether the operation caused changes.
            - msg (str): The message describing the result of the operation.
            - log_level (str): The log level at which the message should be logged ("INFO", "ERROR", "CRITICAL", etc.).
            - data (dict, optional): Additional data related to the operation result.
        Returns:
            self (object): An instance of the class.
        Note:
            - If the status is "failed", the "failed" key in the result dictionary will be set to True.
            - If data is provided, it will be included in the result dictionary.
        """

        # Update the result attributes with the provided values
        self.status = status
        self.result["status"] = status
        self.result["msg"] = msg
        self.result["changed"] = changed

        # Log the message at the specified log level
        self.log(msg, log_level)

        # If the status is "failed", set the "failed" key to True
        if status == "failed":
            self.result["failed"] = True

        # If additional data is provided, include it in the result dictionary
        if data:
            self.result["data"] = data

        return self

    def exit_while_loop(self, start_time, task_id, task_name, response):
        """
        Check if the elapsed time exceeds the specified timeout period and exit the while loop if it does.
        Parameters:
            - start_time (float): The time when the while loop started.
            - task_id (str): ID of the task being monitored.
            - task_name (str): Name of the task being monitored.
            - response (dict): Response received from the task status check.
        Returns:
            bool: True if the elapsed time exceeds the timeout period, False otherwise.
        """

        # If the elapsed time exceeds the timeout period
        if time.time() - start_time > 360:
            if response.get("data"):
                # If there is data in the response, include it in the error message
                self.msg = "Task {0} with task id {1} has not completed within the timeout period. Task Status: {2} ".format(
                    task_name, task_id, response.get("data"))
            else:
                # If there is no data in the response, generate a generic error message
                self.msg = "Task {0} with task id {1} has not completed within the timeout period.".format(
                    task_name, task_id)

            # Update the result with failure status and log the error message
            self.update_result("failed", False, self.msg, "ERROR")
            return True

        return False

    def handle_error(self, task_name, mgmt_ip_instance_id_map, failure_reason=None):
        """
        Handle error encountered during task execution.
        Parameters:
            - task_name (str): Name of the task being performed.
            - mgmt_ip_instance_id_map (dict): Mapping of management IP addresses to instance IDs.
            - failure_reason (str, optional): Reason for the failure, if available.
        Returns:
            self (object): An instance of the class used for interacting with Cisco Catalyst Center.
        """

        # If failure reason is provided, include it in the error message
        if failure_reason:
            self.msg = "An error occurred while performing {0} on device(s): {1}. The operation failed due to the following reason: {2}".format(
                task_name, list(mgmt_ip_instance_id_map.keys()), failure_reason)
        # If no failure reason is provided, generate a generic error message
        else:
            self.msg = "An error occurred while performing {0} on device(s): {1}".format(
                task_name, list(mgmt_ip_instance_id_map.keys()))

        # Update the result with failure status and log the error message
        self.update_result("failed", False, self.msg, "ERROR")

        return self

    def get_compliance_task_status(self, task_id, mgmt_ip_instance_id_map):
        """
        This function retrieves the status of compliance check tasks in Cisco Catalyst Center.
        Parameters:
            - task_id: The ID of the compliance check task.
            - mgmt_ip_instance_id_map: A mapping of management IP addresses to instance IDs.
        Returns:
            self (object): An instance of a class used for interacting with Cisco Catalyst Center.
        Description:
            This function continuously checks the status of a compliance check task until completion.
            It handles various scenarios such as task completion, task failure, or errors during execution.
            Upon successful completion, it logs the modified compliance response and updates the result accordingly.
        """

        task_name = "Run Compliance Check"
        start_time = time.time()

        while True:
            response = self.get_task_status(task_id, task_name)

            # Check if response returned
            if not response:
                self.msg = "Error retrieving Task status for {0} with Task Id: {1}".format(task_name, task_id)
                self.update_result("failed", False, self.msg, "ERROR")
                break

            # Check if the elapsed time exceeds the timeout
            if self.exit_while_loop(start_time, task_id, task_name, response):
                break

            # Handle error if task execution encounters an error
            if response.get("isError"):
                failure_reason = response.get("failureReason")
                self.handle_error(task_name, mgmt_ip_instance_id_map, failure_reason)
                break

            # Check if task completed successfully
            elif not response.get("isError") and "success" in response.get("progress").lower():
                # Task completed successfully
                self.msg = "{0} has completed successfully on device(s): {1}".format(task_name, list(mgmt_ip_instance_id_map.keys()))

                # Retrieve and modify compliance check details
                response = self.get_compliance_detail(self.want.get("compliance_detail_params"))
                if not response:
                    self.msg = "Error Occurred when retrieving Compliance Report after {0} with Task Id {1} for device(s) {2}".format(
                        task_name, task_id, list(mgmt_ip_instance_id_map.keys()))
                    self.update_result("failed", False, self.msg, "ERROR")
                    break

                modified_response = self.modify_compliance_response(response, mgmt_ip_instance_id_map)
                self.log("Compliance Report for {0} operation for device(s) {1} : {2}".format(
                    task_name, list(mgmt_ip_instance_id_map.keys()), modified_response), "INFO")

                # Update result with modified response
                self.update_result("success", True, self.msg, "INFO")
                break

            # Check if task failed
            elif "failed" in response.get("progress").lower():
                self.msg = "Failed to {0} on the following device(s): {1}".format(task_name, list(mgmt_ip_instance_id_map.keys()))
                self.update_result("failed", False, self.msg, "CRITICAL")
                break

        return self

    def get_sync_config_task_status(self, task_id, mgmt_ip_instance_id_map):
        """
        This function manages the status of device configuration synchronization tasks in Cisco Catalyst Center.
        Parameters:
            - task_id: ID of the synchronization task
            - mgmt_ip_instance_id_map: Mapping of management IP addresses to instance IDs
        Returns:
            self (object): An instance of a class used for interacting with Cisco Catalyst Center.
        Description:
            It validates if synchronization is required, categorizes devices based on compliance status, and checks task completion status.
            If all devices are already compliant, it logs a success message. If some devices have unexpected statuses, it logs an error.
            It continuously checks the task status until completion, updating the result accordingly.
        """

        task_name = "Sync Device Configuration"
        start_time = time.time()

        while True:
            success_devices = []
            failed_devices = []

            response = self.get_task_tree(task_id, task_name)

            # Check if response returned
            if not response:
                self.msg = "Error retrieving Task Tree for the task_name {0} task_id {1}".format(task_name, task_id)
                self.update_result("failed", False, self.msg, "ERROR")
                break

            # Check if the elapsed time exceeds the timeout
            if self.exit_while_loop(start_time, task_id, task_name, response):
                break

            # Handle error if task execution encounters an error
            if response[0].get("isError"):
                failure_reason = response.get("failureReason")
                self.handle_error(task_name, mgmt_ip_instance_id_map, failure_reason)
                break

            for item in response[1:]:
                progress = item["progress"]
                for ip, device_id in mgmt_ip_instance_id_map.items():
                    if device_id in progress and "copy_Running_To_Startup=Success" in progress:
                        success_devices.append(ip)
                    elif device_id in progress and "copy_Running_To_Startup=Failed" in progress:
                        failed_devices.append(ip)

            success_devices = set(success_devices)
            failed_devices = set(failed_devices)

            # Check conditions and print messages accordingly
            if len(set(success_devices)) == len(mgmt_ip_instance_id_map):
                self.msg = "{0} has completed successfully on device(s): {1}".format(task_name, success_devices)
                self.update_result("success", True, self.msg, "INFO")
                break
            elif (failed_devices and
                  len(success_devices) < len(mgmt_ip_instance_id_map) and
                  len(failed_devices) + len(success_devices) == len(mgmt_ip_instance_id_map)):
                self.msg = "{0} task has failed on device(s): {1} and succeeded on device(s): {2}".format(
                    task_name, failed_devices, success_devices)
                self.update_result("failed", True, self.msg, "CRITICAL")
                break
            elif len(failed_devices) == len(mgmt_ip_instance_id_map):
                self.msg = "{0} task has failed on device(s): {1}".format(task_name, failed_devices)
                self.update_result("failed", False, self.msg, "CRITICAL")
                break

        return self

    def get_diff_merged(self):
        """
        This method is designed to Perform Network Compliance Actions in Cisco Catalyst Center.
        Parameters: None
        Returns:
            self (object): An instance of a class used for interacting with Cisco Catalyst Center.
        Description:
            This method orchestrates  compliance check operation and device configuration synchronization tasks specified in a playbook.
            It ensures all required tasks are present, executes them, and checks their status, facilitating smooth playbook execution.
        """

        # Action map for different network compliance operations
        action_map = {
            "run_compliance_params": (self.run_compliance, self.get_compliance_task_status),
            "sync_device_config_params": (self.sync_device_config, self.get_sync_config_task_status)
        }

        # Iterate through the action map and execute specified actions
        for action_param, (action_func, status_func) in action_map.items():

            # Execute the action and check its status
            if self.want.get(action_param):
                result_task_id = action_func(self.want.get(action_param))
                self.log("Performing {0}".format(action_func.__name__), "DEBUG")
                if not result_task_id:
                    self.msg = "An error occurred while retrieving the task_id of the {0} operation.".format(action_func.__name__)
                    self.update_result("failed", False, self.msg, "CRITICAL")
                else:
                    status_func(result_task_id, self.want.get("mgmt_ip_instance_id_map")).check_return_status()

        return self

    def verify_diff_merged(self, config):
        """
        Verify the success of the "Sync Device Configuration" operation.
        Parameters:
            config (dict): A dictionary containing the configuration details.
        Returns:
            self (object): An instance of a class used for interacting with Cisco Catalyst Center.
        Description:
            This method verifies the success of the "Sync Device Configuration" operation in the context of network compliance management.
            It checks if the configuration includes the option to synchronize device configurations (`sync_device_config`).
            If this option is present, the function proceeds to compare compliance details before and after executing the synchronization operation.
            It logs relevant information at each step and concludes by determining whether the synchronization was successful.
        """
        if config.get("sync_device_config"):
            # Get compliance details before running sync_device_config
            compliance_details_before = self.want.get("compliance_details")
            self.log("Compliance details before running sync_device_config: {0}".format(compliance_details_before), "INFO")

            # Get compliance details after running sync_device_config
            response = self.get_compliance_detail(self.want.get("compliance_detail_params_sync"))
            if not response:
                self.msg = "Error occured when Retrieving Compliance Details after for verifying configuration."
                self.update("failed", False, self.msg, "ERROR")
                self.check_return_status()

            compliance_details_after = self.modify_compliance_response(response, self.want.get("mgmt_ip_instance_id_map"))
            self.log("Compliance details after running sync_device_config: {0}.".format(compliance_details_after), "INFO")

            all_statuses_before = []
            all_statuses_after = []
            for ip_address, compliance_type in compliance_details_before.items():
                status = compliance_type[0]["status"]
                all_statuses_before.append(status)

            if len(set(all_statuses_before)) == 1 and all_statuses_before[0] == "NON_COMPLIANT":
                for ip_address, compliance_type in compliance_details_after.items():
                    status = compliance_type[0]["status"]
                    all_statuses_after.append(status)
                if len(set(all_statuses_after)) == 1 and all_statuses_after[0] == "COMPLIANT":
                    self.log("Verified the success of the Sync Device Configuration operation.")
                else:
                    self.log(
                        "Sync Device Configuration operation may have been unsuccessful "
                        "since not all devices have 'COMPLIANT' status after the operation.",
                        "WARNING"
                    )
            else:
                self.log("Sync_device_config may not have been performed since devices have status other than 'NON_COMPLIANT'.", "WARNING")
        else:
            self.log("Verification of configuration is not required.", "INFO")
        return self


def main():
    """
    main entry point for module execution
    """

    # Define the specification for the module"s arguments
    element_spec = {"dnac_host": {"required": True, "type": "str"},
                    "dnac_port": {"type": "str", "default": "443"},
                    "dnac_username": {"type": "str", "default": "admin", "aliases": ["user"]},
                    "dnac_password": {"type": "str", "no_log": True},
                    "dnac_verify": {"type": "bool", "default": "True"},
                    "dnac_version": {"type": "str", "default": "2.2.3.3"},
                    "dnac_debug": {"type": "bool", "default": False},
                    "dnac_log_level": {"type": "str", "default": "WARNING"},
                    "dnac_log_file_path": {"type": "str", "default": "dnac.log"},
                    "dnac_log_append": {"type": "bool", "default": True},
                    "dnac_log": {"type": "bool", "default": False},
                    "validate_response_schema": {"type": "bool", "default": True},
                    "config_verify": {"type": "bool", "default": False},
                    "dnac_api_task_timeout": {"type": "int", "default": 1200},
                    "dnac_task_poll_interval": {"type": "int", "default": 2},
                    "config": {"required": True, "type": "list", "elements": "dict"},
                    "state": {"default": "merged", "choices": ["merged"]}
                    }

    # Initialize the Ansible module with the provided argument specifications
    module = AnsibleModule(argument_spec=element_spec,
                           supports_check_mode=False)

    # Initialize the NetworkCompliance object with the module
    ccc_network_compliance = NetworkCompliance(module)

    # Get the state parameter from the provided parameters
    state = ccc_network_compliance.params.get("state")

    # Check if the state is valid
    if state not in ccc_network_compliance.supported_states:
        ccc_network_compliance.status = "invalid"
        ccc_network_compliance.msg = "State {0} is invalid".format(state)
        ccc_network_compliance.check_return_status()

    # Validate the input parameters and check the return status
    ccc_network_compliance.validate_input().check_return_status()

    # Get the config_verify parameter from the provided parameters
    config_verify = ccc_network_compliance.params.get("config_verify")

    # Iterate over the validated configuration parameters
    for config in ccc_network_compliance.validated_config:
        ccc_network_compliance.get_want(config).check_return_status()
        ccc_network_compliance.get_diff_state_apply[state]().check_return_status()
        if config_verify:
            ccc_network_compliance.verify_diff_state_apply[state](config).check_return_status()

    # Exit with the result obtained from the NetworkCompliance object
    module.exit_json(**ccc_network_compliance.result)


if __name__ == "__main__":
    main()
