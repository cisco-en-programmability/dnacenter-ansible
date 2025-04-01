#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright (c) 2024, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)
from __future__ import absolute_import, division, print_function
__metaclass__ = type
__author__ = ("Abinash Mishra, Madhan Sankaranarayanan, Syed Khadeer Ahmed, Ajith Andrew J")
DOCUMENTATION = r"""
---
module: provision_workflow_manager
short_description: Resource module for provision related functions
description:
  - Manage operations related to wired and wireless provisioning
  - API to re-provision provisioned devices
  - API to un-provision provisioned devices
version_added: '6.6.0'
extends_documentation_fragment:
  - cisco.dnac.workflow_manager_params
author: Abinash Mishra (@abimishr) Madhan Sankaranarayanan (@madhansansel) Syed Khadeer
  Ahmed(@syed-khadeerahmed) Ajith Andrew J (@ajithandrewj)
options:
  config_verify:
    description: Set to true to verify the Cisco Catalyst Center config after applying
      the playbook config.
    type: bool
    default: false
  state:
    description: The state of Cisco Catalyst Center after module completion.
    type: str
    choices: [merged, deleted]
    default: merged
  config:
    description:
      - List of details of device being managed.
    type: list
    elements: dict
    required: true
    suboptions:
      management_ip_address:
        description: Management Ip Address of the device.
        type: str
        required: true
      provisioning:
        description:
          - Specifies whether the user intends to perform site assignment only or
            full provisioning for a wired device.
          - Set to 'false' to carry out site assignment only.
          - Set to 'true' to proceed with provisioning to a site.
        type: bool
        required: false
        default: true
      force_provisioning:
        description:
          - Determines whether to force reprovisioning of a device.
          - A device cannot be re-provisioned to a different site.
          - The 'provisioning' option should not be set to 'false' for 'force_provisioning'
            to take effect.
          - Set to 'true' to enforce reprovisioning, even if the device is already
            provisioned.
          - Set to 'false' to skip provisioning for devices that are already provisioned.
        type: bool
        required: false
        default: false
      site_name_hierarchy:
        description: Name of the site where the device will be added. This parameter
          is required for provisioning the device and assigning it to a site.
        type: str
        required: true
      managed_ap_locations:
        description:
          - Specifies the site locations allocated for Access Points (APs).
          - Renamed to 'primary_managed_ap_locations' starting from Cisco Catalyst
            version 2.3.7.6 to differentiate between primary and secondary managed
            AP locations.
          - Backward compatibility is maintained; either 'managed_ap_locations' or
            'primary_managed_ap_locations' can be specified, with no changes required
            after upgrades.
          - Either 'managed_ap_locations' or 'primary_managed_ap_locations' can be
            used interchangeably, but only one of them is mandatory and must be provided.
        type: list
        elements: str
      primary_managed_ap_locations:
        description:
          - Specifies the site locations assigned to primary managed Access Points
            (APs).
          - Introduced as the updated name for 'managed_ap_locations' starting from
            Cisco Catalyst version 2.3.7.6.
          - Backward compatible with 'managed_ap_locations'; either parameter can
            be specified without requiring changes after upgrades.
          - Mandatory for provisioning wireless devices if 'managed_ap_locations'
            is not used.
          - Supported in Cisco Catalyst version 2.3.7.6 and later.
        type: list
        elements: str
      secondary_managed_ap_locations:
        description:
          - Specifies the site locations assigned to secondary managed Access Points
            (APs).
          - Introduced in Cisco Catalyst version 2.3.7.6 to allow differentiation
            between primary and secondary managed AP locations.
          - Mandatory for provisioning wireless devices in scenarios where secondary
            AP locations are required.
        type: list
        elements: str
      dynamic_interfaces:
        description:
          - A list of dynamic interfaces on the wireless controller.
          - Each entry represents an interface with associated configuration details.
        type: list
        elements: dict
        suboptions:
          interface_name:
            description: The name of the interface.
            type: str
          vlan_id:
            description: The VLAN ID associated with the interface.
            type: str
          interface_ip_address:
            description: The IP address assigned to the interface.
            type: str
          interface_netmask_in_c_i_d_r:
            description: The netmask of the interface in CIDR format (e.g., 24 for
              255.255.255.0).
            type: str
          interface_gateway:
            description: The gateway IP address for the interface.
            type: str
          lag_or_port_number:
            description: The port number or LAG (Link Aggregation Group) identifier.
            type: str
      skip_ap_provision:
        description:
          - If set to 'true', Access Point (AP) provisioning will be skipped during
            the workflow.
          - Use this option when AP provisioning is not required as part of the current
            operation.
          - Supported in Cisco Catalyst version 2.3.7.6 and later.
        type: bool
        default: false
      rolling_ap_upgrade:
        description:
          - Configuration options for performing a rolling upgrade of Access Points
            (APs) in phases.
          - Allows control over the gradual rebooting of APs during the upgrade process.
          - Supported in Cisco Catalyst version 2.3.7.6 and later.
        type: dict
        suboptions:
          enable_rolling_ap_upgrade:
            description:
              - Enable or disable the rolling AP upgrade feature.
              - If set to 'true', APs will be upgraded in batches based on the specified
                reboot percentage.
              - Supported in Cisco Catalyst version 2.3.7.6 and later.
            type: bool
            default: false
          ap_reboot_percentage:
            description:
              - The percentage of APs to reboot simultaneously during an upgrade.
              - Supported in Cisco Catalyst version 2.3.7.6 and later.
              - Must be either 5, 15 or 25 representing the proportion of APs to reboot
                at once.
            type: int
requirements:
  - dnacentersdk == 2.4.5
  - python >= 3.9
notes:
  - SDK Methods used are sites.Sites.get_site, devices.Devices.get_network_device_by_ip,
    task.Task.get_task_by_id, sda.Sda.get_provisioned_wired_device, sda.Sda.re_provision_wired_device,
    sda.Sda.provision_wired_device, wireless.Wireless.provision
  - Paths used are get /dna/intent/api/v1/site get /dna/intent/api/v1/network-device/ip-address/{ipAddress}
    get /dna/intent/api/v1/task/{taskId} get /dna/intent/api/v1/business/sda/provision-device
    put /dna/intent/api/v1/business/sda/provision-device post /dna/intent/api/v1/business/sda/provision-device
    post /dna/intent/api/v1/wireless/provision
  - Added 'provisioning' option in v6.16.0
  - Added provisioning and reprovisioning of wireless devices in v6.16.0
"""
EXAMPLES = r"""
- name: Provision a wireless device to a site
  cisco.dnac.provision_workflow_manager:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    dnac_log: true
    state: merged
    config:
      - site_name_hierarchy: Global/USA/San Francisco/BGL_18
        management_ip_address: 204.192.3.40
        managed_ap_locations:
          - Global/USA/San Francisco/BGL_18/Test_Floor2
        dynamic_interfaces:
          - vlan_id: 1866
            interface_name: Vlan1866
            interface_ip_address: 204.192.6.200
            interface_gateway: 204.192.6.1
- name: Provision a wireless device to a site for version - 2.3.7.6
  cisco.dnac.provision_workflow_manager:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    dnac_log: true
    state: merged
    config:
      - site_name_hierarchy: Global/USA/San Francisco/BGL_18
        management_ip_address: 204.192.3.40
        primary_managed_ap_locations:
          - Global/USA/San Francisco/BGL_18/Test_Floor2
        secondary_managed_ap_locations:
          - Global/USA/San Francisco/BGL_18/Test_Floor1
        dynamic_interfaces:
          - interface_name: Vlan1866
            vlan_id: 1866
            interface_ip_address: 204.192.6.200
            interface_gateway: 204.192.6.1
        skip_ap_provision: false
        rolling_ap_upgrade:
          enable_rolling_ap_upgrade: false
          ap_reboot_percentage: 5
- name: Provision a wired device to a site
  cisco.dnac.provision_workflow_manager:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    dnac_log: true
    state: merged
    config:
      - site_name_hierarchy: Global/USA/San Francisco/BGL_18
        management_ip_address: 204.192.3.40
- name: Re-Provision a wired device to a site forcefully
  cisco.dnac.provision_workflow_manager:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    dnac_log: true
    state: merged
    config:
      - site_name_hierarchy: Global/USA/San Francisco/BGL_18
        management_ip_address: 204.192.3.40
        force_provisioning: true
- name: Assign a wired device to a site
  cisco.dnac.provision_workflow_manager:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    dnac_log: true
    state: merged
    config:
      - site_name_hierarchy: Global/USA/San Francisco/BGL_18
        management_ip_address: 204.192.3.40
        provisioning: false
- name: Provision a wireless device to a site
  cisco.dnac.provision_workflow_manager:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    dnac_log: true
    state: merged
    config_verify: true
    config:
      - site_name_hierarchy: Global/USA/RTP/BLD11
        management_ip_address: 204.192.12.201
        managed_ap_locations:
          - Global/USA/RTP/BLD11/BLD11_FLOOR1
- name: Unprovision a device from a site
  cisco.dnac.provision_workflow_manager:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    dnac_log: true
    state: deleted
    config_verify: true
    config:
      - management_ip_address: 204.1.2.2
"""
RETURN = r"""
# Case_1: Successful creation/updation/deletion of provision
response_1:
  description: A dictionary with details of provision is returned
  returned: always
  type: dict
  sample: >
    {
      "response":
      {
        "response": String,
        "version": String
        },
      "msg": String
    }
# Case_2: Error while creating a provision
response_2:
  description: A list with the response returned by the Cisco Catalyst Center Python SDK
  returned: always
  type: list
  sample: >
    {
      "response": [],
      "msg": String
    }
# Case_3: Already exists and requires no update
response_3:
  description: A dictionary with the exisiting details as returned by the Cisco Cisco Catalyst Center  Python SDK
  returned: always
  type: dict
  sample: >
    {
      "response": String,
      "msg": String
    }
"""
import time
import re
from ansible.module_utils.basic import AnsibleModule
from ansible_collections.cisco.dnac.plugins.module_utils.dnac import (
    DnacBase,
    validate_list_of_dicts
)


class Provision(DnacBase):

    """
    Class containing member attributes for provision workflow module
    """
    def __init__(self, module):
        super().__init__(module)
        self.device_type = None

    def validate_input(self, state=None):

        """
        Validate the fields provided in the playbook.
        Checks the configuration provided in the playbook against a predefined specification
        to ensure it adheres to the expected structure and data types.
        Args:
            self: The instance of the class containing the 'config' attribute to be validated.
        Returns:
            The method returns an instance of the class with updated attributes:
                - self.msg: A message describing the validation result.
                - self.status: The status of the validation (either 'success' or 'failed').
                - self.validated_config: If successful, a validated version of the
                  'config' parameter.
        Example:
            To use this method, create an instance of the class and call 'validate_input' on it.
            If the validation succeeds, 'self.status' will be 'success' and
            'self.validated_config' will contain the validated configuration. If it fails,
            'self.status' will be 'failed', and 'self.msg' will describe the validation issues.
        """

        if not self.config:
            self.msg = "config not available in playbook for validation"
            self.status = "success"
            return self

        provision_spec = {
            "management_ip_address": {'type': 'str', 'required': True},
            "site_name_hierarchy": {'type': 'str', 'required': False},
            "managed_ap_locations": {'type': 'list', 'required': False,
                                     'elements': 'str'},
            "primary_managed_ap_locations": {'type': 'list', 'required': False,
                                             'elements': 'str'},
            "secondary_managed_ap_locations": {'type': 'list', 'required': False,
                                               'elements': 'str'},
            "dynamic_interfaces": {'type': 'list', 'required': False,
                                   'elements': 'dict'},
            "skip_ap_provision": {'type': 'bool', 'required': False},
            "rolling_ap_upgrade": {'type': 'dict', 'required': False},
            "provisioning": {'type': 'bool', 'required': False, "default": True},
            "force_provisioning": {'type': 'bool', 'required': False, "default": False}
        }
        if state == "merged":
            provision_spec["site_name_hierarchy"] = {'type': 'str', 'required': True}
            missing_params = []
            for config_item in self.config:
                if "site_name_hierarchy" not in config_item or config_item["site_name_hierarchy"] is None:
                    missing_params.append("site_name_hierarchy")
                if "management_ip_address" not in config_item or config_item["management_ip_address"] is None:
                    missing_params.append("management_ip_address")

            if missing_params:
                self.msg = "Missing or invalid required parameter(s): {0}".format(', '.join(missing_params))
                self.status = "failed"
                return self

        valid_provision, invalid_params = validate_list_of_dicts(
            self.config, provision_spec
        )
        if invalid_params:
            self.msg = "Invalid parameters in playbook: {0}".format(
                "\n".join(invalid_params))
            self.log(str(self.msg), "ERROR")
            self.status = "failed"
            return self

        self.validated_config = valid_provision
        self.msg = "Successfully validated playbook configuration parameters using 'validate_input': {0}".format(str(valid_provision))
        self.log(str(self.msg), "INFO")
        self.status = "success"
        return self

    def get_dev_type(self):
        """
        Fetches the type of device (wired/wireless)

        Parameters:
          - self: The instance of the class containing the 'config' attribute
                  to be validated.
        Returns:
          The method returns an instance of the class with updated attributes:
          str: The type of the device ('wired' or 'wireless'), or None if the device is
              unrecognized, not present, or an error occurs.
        Example:
          Post creation of the validated input, we use this method to get the
          type of the device.
        """
        try:
            dev_response = self.dnac_apply['exec'](
                family="devices",
                function='get_network_device_by_ip',
                params={"ip_address": self.validated_config["management_ip_address"]}
            )

            self.log("The device response from 'get_network_device_by_ip' API is {0}".format(str(dev_response)), "DEBUG")

            dev_dict = dev_response.get("response", {})
            if not dev_dict:
                self.log("Invalid response received from the API 'get_network_device_by_ip'. 'response' is empty or missing.", "WARNING")
                return None

            device_family = dev_dict.get("family")
            if not device_family:
                self.log("Device family is missing in the response.", "WARNING")
                return None

            if device_family == "Wireless Controller":
                device_type = "wireless"
            elif device_family in ["Switches and Hubs", "Routers"]:
                device_type = "wired"
            else:
                device_type = None

            self.log("The device type is {0}".format(device_type), "INFO")

            return device_type

        except Exception as e:
            msg = (
                "The Device - {0} not present in the Cisco Catalyst Center."
                .format(self.validated_config.get("management_ip_address"))
            )
            self.log(msg, "INFO")

            return None

    def get_device_id(self):
        """
        Fetches the UUID of the device added in the inventory

        Parameters:
          - self: The instance of the class containing the 'config' attribute
                  to be validated.
        Returns:
          The method returns the serial number of the device as a string. If it fails, it returns None.
        Example:
          After creating the validated input, this method retrieves the
          UUID of the device.
        """

        dev_response = self.dnac_apply['exec'](
            family="devices",
            function='get_network_device_by_ip',
            params={"ip_address": self.validated_config["management_ip_address"]}
        )

        self.log("The device response from 'get_network_device_by_ip' API is {0}".format(str(dev_response)), "DEBUG")
        dev_dict = dev_response.get("response")
        device_id = dev_dict.get("id")

        self.log("Device ID of the device with IP address {0} is {1}".format(self.validated_config["management_ip_address"], device_id), "INFO")
        return device_id

    def get_serial_number(self):
        """
        Fetches the serial number of the device

        Parameters:
          - self: The instance of the class containing the 'config' attribute
                  to be validated.
        Returns:
          The method returns the serial number of the device as a string. If it fails, it returns None.
        Example:
          After creating the validated input, this method retrieves the
          serial number of the device.
        """

        try:
            response = self.dnac_apply['exec'](
                family="devices",
                function='get_network_device_by_ip',
                params={"ip_address": self.validated_config["management_ip_address"]}
            )

        except Exception as e:
            self.log("An error occurred while fetching the serial number: {0}".format(str(e)), "ERROR")
            return None

        if not (response or response.get("response")):
            self.log("No response received from 'get_network_device_by_ip' API or it's invalid.", "ERROR")
            return None

        self.log("The device response from 'get_network_device_by_ip' API is {0}".format(str(response)), "DEBUG")
        dev_dict = response.get("response")
        serial_number = dev_dict.get("serialNumber")

        if not serial_number:
            self.log("Serial number not found in the response.", "ERROR")
            return None

        self.log("Serial Number of the device is {0}".format(str(serial_number)), "INFO")

        return serial_number

    def get_task_status(self, task_id=None):
        """
        Fetches the status of the task once any provision API is called

        Parameters:
          - self: The instance of the class containing the 'config' attribute
                  to be validated.
          - task_id: Task_id of the provisioning task.
        Returns:
          The method returns the status of the task_id used to track provisioning.
          Returns True if task is not failed otheriwse returns False.
        Example:
          Post creation of the provision task, this method fetheches the task
          status.

        """
        result = False
        params = {"task_id": task_id}
        while True:
            response = self.dnac_apply['exec'](
                family="task",
                function='get_task_by_id',
                params=params
            )
            self.log("Response collected from 'get_task_by_id' API is {0}".format(str(response)), "DEBUG")
            response = response.response
            self.log("Task status for the task id {0} is {1}".format(str(task_id), str(response.get("progress"))), "INFO")
            if response.get('isError') or re.search(
                'failed', response.get('progress'), flags=re.IGNORECASE
            ):
                msg = 'Provision task with id {0} has not completed - Reason: {1}'.format(
                    task_id, response.get("failureReason"))
                self.module.fail_json(msg=msg)
                return False

            if (
                response.get('progress') in ["TASK_PROVISION", "TASK_MODIFY_PUT"]
                and response.get("isError") is False
            ) or "deleted successfully" in response.get('progress'):

                result = True
                break

            time.sleep(3)
        self.result.update(dict(provision_task=response))
        return result

    def get_execution_status_wireless(self, execution_id=None):
        """
        Fetches the status of the BAPI once site wireless provision API is called

        Parameters:
          - self: The instance of the class containing the 'config' attribute
                  to be validated.
          - execution_id: execution_id of the BAPI API.
        Returns:
          The method returns the status of the BAPI used to track wireless provisioning.
          Returns True if the status is not failed, otheriwse returns False.
        Example:
          Post creation of the provision task, this method fetheches the task
          status.

        """
        result = False
        params = {"execution_id": execution_id}
        while True:
            response = self.dnac_apply['exec'](
                family="task",
                function="get_business_api_execution_details",
                params=params
            )
            self.log("Response collected from 'get_business_api_execution_details' API is {0}".format(str(response)), "DEBUG")
            self.log("Execution status for the execution id {0} is {1}".format(str(execution_id), str(response.get("status"))), "INFO")
            if response.get('bapiError') or response.get("status") == "FAILURE":
                if response.get("bapiError") == "Device was already provisioned , please use provision update API to reprovision the device":
                    msg = "Performing reprovisioning of wireless device"
                    result = True
                    self.perform_wireless_reprovision()
                    break
                msg = 'Wireless provisioning execution with id {0} has not completed - Reason: {1}'.format(
                    execution_id, response.get("bapiError"))
                self.module.fail_json(msg=msg)
                return False

            if response.get('status') == 'SUCCESS':
                result = True
                break

            time.sleep(3)
        self.result.update(dict(assignment_task=response))
        return result

    def get_site_type(self, site_name_hierarchy=None):
        """
        Fetches the type of site

        Parameters:
          - self: The instance of the class containing the 'config' attribute
                  to be validated.
          - site_name_hierarchy: Name of the site collected from the input.
        Returns:
          - site_type: A string indicating the type of the site (area/building/floor).
        Example:
          Post creation of the validated input, this method gets the
          type of the site.
        """

        try:
            response = self.dnac_apply['exec'](
                family="sites",
                function='get_site',
                params={"name": site_name_hierarchy}
            )
        except Exception:
            self.log("Exception occurred as \
                site '{0}' was not found".format(site_name_hierarchy), "CRITICAL")
            self.module.fail_json(msg="Site not found", response=[])

        if response:
            self.log("Received site details\
                for '{0}': {1}".format(site_name_hierarchy, str(response)), "DEBUG")
            site = response.get("response")
            site_additional_info = site[0].get("additionalInfo")
            for item in site_additional_info:
                if item["nameSpace"] == "Location":
                    site_type = item.get("attributes").get("type")
                    self.log("Site type for site name '{1}' : {0}".format(site_type, site_name_hierarchy), "INFO")

        return site_type

    def is_device_assigned_to_site(self, uuid):
        """
        Checks if a device, specified by its UUID, is assigned to any site.

        Parameters:
          - self: The instance of the class containing the 'config' attribute
                  to be validated.
          - uuid (str): The UUID of the device to check for site assignment.
        Returns:
          - boolean:  True if the device is assigned to a site, False otherwise.

        """

        self.log("Checking site assignment for device with UUID: {0}".format(uuid), "INFO")
        try:
            site_response = self.dnac_apply['exec'](
                family="devices",
                function='get_device_detail',
                params={"search_by": uuid ,
                        "identifier": "uuid"}
            )
            self.log("Response collected from the API 'get_device_detail' {0}".format(site_response))
            site_response = site_response.get("response")
            if site_response.get("location"):
                return True
            else:
                return False
        except Exception as e:
            msg = "Failed to find device with UUID {0} due to: {1}".format(uuid, e)
            self.log(msg, "CRITICAL")
            self.module.fail_json(msg=msg)

    def is_device_assigned_to_site_v1(self, uuid):
        """
        Checks if a device, specified by its UUID, is assigned to any site.

        Parameters:
          - self: The instance of the class containing the 'config' attribute
                  to be validated.
          - uuid (str): The UUID of the device to check for site assignment.
        Returns:
          - tuple: (bool, Optional[str])
            - True and the site name if the device is assigned to a site.
            - False and None if not assigned or in case of an error..

        """

        self.log("Checking site assignment for device with UUID: {0}".format(uuid), "INFO")
        try:
            site_api_response = self.dnac_apply['exec'](
                family="site_design",
                function='get_site_assigned_network_device',
                params={"id": uuid}
            )

            self.log("Response collected from the API 'get_site_assigned_network_device' {0}".format(site_api_response))
            site_response = site_api_response.get("response")

            if site_response:
                site_name = site_response.get("siteNameHierarchy")
                if site_name:
                    self.log("Device with UUID {0} is assigned to site: {1}".format(uuid, site_name), "INFO")
                    return True, site_name

            self.log("Device with UUID {0} is not assigned to any site.".format(uuid), "INFO")
            return False, None

        except Exception as e:
            msg = "Failed to find device with UUID {0} due to: {1}".format(uuid, e)
            self.log(msg, "CRITICAL")
            self.module.fail_json(msg=msg)

    def get_device_site_by_uuid(self, uuid):
        """
        Checks if a device is assigned to any site.

        Parameters:
        - self: The instance of the class containing the 'config' attribute
                to be validated.
        - uuid (str): The UUID of the device to check for site assignment.
        Returns:
        - location (str): The location of the site if the device is assigned,
                            None otherwise.
        """

        self.log("Checking site assignment for device with UUID: {0}".format(uuid), "INFO")

        try:
            site_response = self.dnac_apply['exec'](
                family="devices",
                function='get_device_detail',
                params={"search_by": uuid, "identifier": "uuid"}
            )
            self.log("Response collected from the API 'get_device_detail': {0}".format(site_response))

            site_response = site_response.get("response")
            if site_response and site_response.get("location"):
                location = site_response.get("location")
                return location
            else:
                self.log("No site assignment found for device with UUID: {0}".format(uuid), "INFO")
                return None

        except Exception as e:
            msg = "Failed to find device with location for UUID {0} due to: {1}".format(uuid, e)
            self.log(msg, "CRITICAL")
            self.module.fail_json(msg=msg)

    def get_wired_params(self):
        """
        Prepares the payload for provisioning of the wired devices

        Parameters:
          - self: The instance of the class containing the 'config' attribute
                  to be validated.
        Returns:
          The method returns an instance of the class with updated attributes:
          - wired_params: A dictionary containing all the values indicating
                          management IP address of the device and the hierarchy
                          of the site.
        Example:
          Post creation of the validated input, it fetches the required
          paramters and stores it for further processing and calling the
          parameters in other APIs.
        """

        site_name = self.validated_config.get("site_name_hierarchy")

        (site_exits, site_id) = self.get_site_id(site_name)

        if site_exits is False:
            msg = "Site {0} doesn't exist".format(site_name)
            self.log(msg, "CRITICAL")
            self.module.fail_json(msg=msg)

        if self.validated_config.get("provisioning") is True:
            wired_params = {
                "deviceManagementIpAddress": self.validated_config["management_ip_address"],
                "siteNameHierarchy": site_name
            }
        else:
            wired_params = {
                "device": [
                    {
                        "ip": self.validated_config["management_ip_address"]
                    }
                ],
                "site_id": site_id
            }

        self.log("Parameters collected for the provisioning of wired device:{0}".format(wired_params), "INFO")
        return wired_params

    def get_wireless_params(self):
        """
        Prepares the payload for provisioning of the wireless devices

        Parameters:
          - self: The instance of the class containing the 'config' attribute
                  to be validated.
        Returns:
          The method returns an instance of the class with updated attributes:
          - wireless_params: A list of dictionary containing all the values indicating
                          management IP address of the device, hierarchy
                          of the site, AP Location of the wireless controller and details
                          of the interface
        Example:
          Post creation of the validated input, it fetches the required
          paramters and stores it for further processing and calling the
          parameters in other APIs.
        """
        ap_locations = self.validated_config.get("primary_managed_ap_locations") or self.validated_config.get("managed_ap_locations")
        wireless_params = [
            {
                "site": self.validated_config.get("site_name_hierarchy"),
                "managedAPLocations": ap_locations,
            }
        ]

        if not ap_locations :
            self.log("Validating AP locations: {0}".format(ap_locations), "DEBUG")
            self.msg = "Missing Managed AP Locations or Primary Managed AP Locations: Please specify the intended location(s) for the wireless device \
                within the site hierarchy."
            self.set_operation_result("failed", False, self.msg, "ERROR").check_return_status()

        ap_locations = self.validated_config.get("primary_managed_ap_locations") or self.validated_config.get("managed_ap_locations")

        self.floor_names = []
        for ap_loc in ap_locations:
            self.log("Processing AP location: {0}".format(ap_loc), "DEBUG")
            site_type = self.get_site_type(site_name_hierarchy=ap_loc)
            self.log("Resolved site type for AP location '{0}': '{1}'".format(ap_loc, site_type), "DEBUG")

            if site_type == "floor":
                self.log("Adding '{0}' to floor names list".format(ap_loc), "DEBUG")
                self.floor_names.append(ap_loc)
            elif site_type == "building":
                self.log("Building site type detected for '{0}'. Retrieving floor details.".format(ap_loc), "DEBUG")
                building_name = ap_loc + ".*"
                floors = self.get_site(building_name)

                for item in floors['response']:
                    if item.get('type') == 'floor':
                        self.log("Floor found: '{0}' for building '{1}'".format(item['nameHierarchy'], ap_loc), "DEBUG")
                        self.floor_names.append(item['nameHierarchy'])
                    elif 'additionalInfo' in item:
                        for additional_info in item['additionalInfo']:
                            if 'attributes' in additional_info and additional_info['attributes'].get('type') == 'floor':
                                self.log("Floor found in additionalInfo: '{0}' for building '{1}'".format(item['siteNameHierarchy'], ap_loc), "DEBUG")
                                self.floor_names.append(item['siteNameHierarchy'])
            else:
                self.log("Invalid site type detected for '{0}'. Managed AP Location must be building or floor.".format(ap_loc), "CRITICAL")
                self.module.fail_json(msg="Managed AP Location must be building or floor", response=[])

        self.log("Final list of floor names: {0}".format(self.floor_names), "DEBUG")

        wireless_params[0]["dynamicInterfaces"] = []
        if self.validated_config.get("dynamic_interfaces"):
            for interface in self.validated_config.get("dynamic_interfaces"):
                interface_dict = {
                    "interfaceIPAddress": interface.get("interface_ip_address"),
                    "interfaceNetmaskInCIDR": interface.get("interface_netmask_in_c_i_d_r"),
                    "interfaceGateway": interface.get("interface_gateway"),
                    "lagOrPortNumber": interface.get("lag_or_port_number"),
                    "vlanId": interface.get("vlan_id"),
                    "interfaceName": interface.get("interface_name")
                }
                wireless_params[0]["dynamicInterfaces"].append(interface_dict)

        wireless_params[0]["skip_ap_provision"] = self.validated_config.get("skip_ap_provision")
        wireless_params[0]["primaryManagedAPLocationsSiteIds"] = ap_locations
        wireless_params[0]["secondaryManagedAPLocationsSiteIds"] = self.validated_config.get("secondary_managed_ap_locations")

        if self.validated_config.get("rolling_ap_upgrade"):
            rolling_ap_upgrade = self.validated_config["rolling_ap_upgrade"]
            wireless_params[0]["rolling_ap_upgrade"] = rolling_ap_upgrade

        response = self.dnac_apply['exec'](
            family="devices",
            function='get_network_device_by_ip',
            params={"ip_address": self.validated_config["management_ip_address"]}
        )

        self.log("Response collected from 'get_network_device_by_ip' is:{0}".format(str(response)), "DEBUG")
        wireless_params[0]["deviceName"] = response.get("response").get("hostname")
        wireless_params[0]["device_id"] = response.get("response").get("id")
        self.log("Parameters collected for the provisioning of wireless device:{0}".format(wireless_params), "INFO")
        return wireless_params

    def get_want(self, config):
        """
        Get all provision related informantion from the playbook
        Args:
            self: The instance of the class containing the 'config' attribute to be validated.
            config: validated config passed from the playbook
        Returns:
            The method returns an instance of the class with updated attributes:
                - self.want: A dictionary of paramters obtained from the playbook
                - self.msg: A message indicating all the paramters from the playbook are
                collected
                - self.status: Success
        Example:
            It stores all the paramters passed from the playbook for further processing
            before calling the APIs
        """

        self.validated_config = config
        self.want = {}
        self.device_ip = self.validated_config["management_ip_address"]
        state = self.params.get("state")

        self.want["device_type"] = self.get_dev_type()

        if self.want["device_type"] == "wired":
            self.want["prov_params"] = self.get_wired_params()
        elif self.want["device_type"] == "wireless":
            if state.lower() == "merged":
                self.want["prov_params"] = self.get_wireless_params()
        else:
            self.log("Passed devices are neither wired or wireless devices", "WARNING")

        self.msg = "Successfully collected all parameters from playbook " + \
            "for comparison"
        self.log(self.msg, "INFO")
        self.status = "success"
        return self

    def perform_wireless_reprovision(self):
        """
        This method performs the reprovisioning of a wireless device. Since, we don't have any
        APIs to get provisioned wireless devices, so we are reprovisioning based on the failure
        condition of the device
        Parameters:
            - self: The instance of the class containing the 'config' attribute
                  to be validated.
        Returns:
            object: An instance of the class with updated results and status
            based on the processing of differences.
        Example:
            If wireless device is already provisioned, this method calls the provision update
            API and handles it accordingly
        """
        device_id = self.get_device_id()
        self.log("Retrieved device ID: {0}".format(device_id), "DEBUG")
        prov_params = self.want.get("prov_params")[0]
        already_provisioned_site = self.get_device_site_by_uuid(device_id)

        if already_provisioned_site != self.site_name:
            self.log("Device re-provisioning logic triggered.", "INFO")
            self.msg = ("Error in re-provisioning a wireless device '{0}' - the device is already associated "
                        "with Site: {1} and cannot be re-provisioned to Site {2}.".format(self.device_ip, already_provisioned_site, self.site_name))
            self.log(self.msg, "ERROR")
            self.result['response'] = self.msg
            self.status = "failed"
            self.check_return_status()

        param = [
            {
                "deviceName": prov_params.get("deviceName"),
                "site": prov_params.get("site"),
                "managedAPLocations": self.floor_names,
                "dynamicInterfaces": prov_params.get("dynamicInterfaces")
            }
        ]

        try:
            headers_payload = {"__persistbapioutput": "true"}
            response = self.dnac_apply['exec'](
                family="wireless",
                function="provision_update",
                op_modifies=True,
                params={"payload": param,
                        "headers": headers_payload}
            )
            self.log("Wireless provisioning response collected from 'provision_update' API is: {0}".format(str(response)), "DEBUG")
            execution_id = response.get("executionId")
            self.get_execution_status_wireless(execution_id=execution_id)
            self.result["changed"] = True
            self.result['msg'] = "Wireless device with IP address {0} got re-provisioned successfully".format(self.validated_config["management_ip_address"])
            self.result['diff'] = self.validated_config
            self.result['response'] = execution_id
            self.log(self.result['msg'], "INFO")
            return self
        except Exception as e:
            self.log("Parameters are {0}".format(self.want))
            self.msg = "Error in wireless re-provisioning of {0} due to {1}".format(self.validated_config["management_ip_address"], e)
            self.log(self.msg, "ERROR")
            self.status = "failed"
            return self

    def get_device_provision_status_for_wlc(self):
        """
        Retrieves the provisioning status of a device based on its management IP address.

        Returns:
            str: The provisioning status of the device, either 'success' or 'failed'.
        Description:
            Depending on the Cisco Catalyst Center (CCC) version, this function calls different APIs to
            check if a device is provisioned. It handles both wired and wireless device provisioning
            checks and logs relevant status and errors.
        """

        status = "failed"
        device_management_ip = self.validated_config.get("management_ip_address")
        self.log("Checking provisioning status for device with management IP '{0}' '".format(device_management_ip), "DEBUG")
        try:
            status_response = self.dnac_apply['exec'](
                family="sda",
                function="get_provisioned_wired_device",
                params={"device_management_ip_address": device_management_ip},
            )

            if isinstance(status_response, dict):
                self.log("Received API response for device '{0}': {1}".format(device_management_ip, status_response), "DEBUG")
                status = status_response.get("status", "failed")
            else:
                self.log("Invalid or empty response received for device with management IP '{}'".format(device_management_ip), "DEBUG")

        except Exception as e:
            self.log("Device '{0}' is not provisioned due to error: {1}".format(device_management_ip, str(e)), "ERROR")
            status = "failed"

        self.log("Final provisioning status for device '{}': '{}'".format(device_management_ip, status), "DEBUG")
        return status

    def get_diff_merged(self):
        """
        Process and merge device provisioning differences.

        Args:
            self: An instance of a class used for interacting with Cisco Catalyst Center.

        Returns:
            self: An instance of the class with updated results and status based on
            the processing of device provisioning differences.

        Description:
            - Processes device provisioning differences by checking device types and provisioning statuses.
            - Handles both wired and wireless devices:
                1. Wired Devices:
                    - Provisions the device if required.
                    - Uses the `provision_wired_device()` function to perform provisioning.
                2. Wireless Devices:
                    - Checks the current provisioning status.
                    - If already provisioned and `force_provisioning` is not enabled, logs a message and exits.
                    - Otherwise, it proceeds with provisioning using `provision_wireless_device()`.
            - Applies version-based checks using `compare_dnac_versions()`:
                - Devices running ≤ 2.3.5.3 always follow this provisioning logic.
                - Wireless devices running ≥ 2.3.7.6 also follow this logic.
            - If these conditions are not met, bulk provisioning for wired devices is handled via `provision_bulk_wired_device()`.
            - Any errors encountered are logged appropriately.
        """

        # Retrieve the current Cisco Catalyst Center version for comparison
        ccc_version = self.get_ccc_version()
        self.log("Fetched CCC version: {0}".format(ccc_version), "DEBUG")

        # Check if provisioning should be handled based on DNAC version:
        # - If DNAC version is ≤ 2.3.5.3, always proceed with provisioning logic.
        # - If DNAC version is ≥ 2.3.7.6 AND the device is wireless, follow wireless provisioning logic.

        if (
            self.compare_dnac_versions(ccc_version, "2.3.5.3") <= 0
            or (
                self.compare_dnac_versions(ccc_version, "2.3.7.6") >= 0
                and self.device_type == 'wireless'
            )
        ):
            # Fetch device details from validated config
            self.log("Proceeding with provisioning logic based on CCC version and device type", "DEBUG")
            device_type = self.want.get("device_type")
            to_force_provisioning = self.validated_config.get("force_provisioning")
            to_provisioning = self.validated_config.get("provisioning")
            self.device_ip = self.validated_config["management_ip_address"]
            self.site_name = self.validated_config["site_name_hierarchy"]
            self.log("Device Type: {0}, Device IP: {1}, Site: {2}".format(device_type, self.device_ip, self.site_name), "DEBUG")

            if device_type == "wired":
                self.log("Initiating provisioning for wired device: {0}".format(self.device_ip), "INFO")
                self.provision_wired_device(to_provisioning, to_force_provisioning)

            elif device_type == "wireless":
                self.log("Checking provisioning status for wireless device: {0}".format(self.device_ip), "DEBUG")
                status = self.get_device_provision_status_for_wlc()
                if status == 'success':

                    if not to_force_provisioning:
                        self.msg = "Wireless Device '{0}' is already provisioned.".format(self.device_ip)
                        self.set_operation_result("success", False, self.msg, "INFO")
                        return self

                self.log("Starting wireless device provisioning...", "INFO")
                self.provision_wireless_device()

            else:
                self.msg = "Exception occurred while getting the device type, device '{0}' is not present in the cisco catalyst center".format(self.device_ip)
                self.set_operation_result("failed", False, self.msg, "ERROR").check_return_status()

        else:
            self.log("Skipping individual provisioning. Initiating bulk provisioning for wired devices.", "INFO")
            self.provision_bulk_wired_device()

        return self

    def provision_bulk_wired_device(self):
        """
        Provisions or reprovisions wired network devices in bulk based on the given validated configuration.

        Args:
            self: An instance of a class used for interacting with network devices.

        Returns:
            self: The updated instance with provisioning results.

        Description:
            This method:
            - Identifies devices that need provisioning or reprovisioning.
            - Checks their current provision status.
            - Logs and updates provisioning status accordingly.
            - Ensures already provisioned devices are not unnecessarily reprovisioned unless forced.
            - Updates the instance with provisioning results and logs messages accordingly.
        """

        provision_params, reprovision_params, self.device_ips = [], [], []
        already_provisioned_devices = []

        self.reprovisioned_device, self.provisioned_device, self.already_provisioned_devices = [], [], []
        success_msg, provision_needed, reprovision_needed = [], [], []
        self.log("Starting bulk wired device provisioning process.", "INFO")

        for config in self.validated_config:
            device_ip = config.get("management_ip_address")

            if device_ip not in self.device_dict['wired']:
                self.log("Skipping device '{0}': Not a wired device.".format(device_ip), "DEBUG")
                continue

            site_name = config.get("site_name_hierarchy")
            site_id_tuple = self.get_site_id(site_name)
            site_id = site_id_tuple[1]
            self.device_ips.append(device_ip)

            network_device_id = self.get_device_ids_from_device_ips([device_ip]).get(device_ip)
            if not network_device_id:
                self.log("Skipping device '{0}': Device ID not found.".format(device_ip), "ERROR")
                continue

            provision_id, status = self.get_device_provision_status(network_device_id, device_ip)
            self.log("Device '{0}': provision_id='{1}', status='{2}'".format(device_ip, provision_id, status), "DEBUG")

            to_force_provisioning = config.get("force_provisioning", False)
            to_provisioning = config.get("provisioning", False)

            if not to_provisioning and status != "success":
                self.log("Provisioning not required; assigning device '{0}' to site '{1}' (site_id: {2}).".format(device_ip, site_name, site_id), "INFO")
                if self.assign_device_to_site([network_device_id], site_name, site_id):
                    success_msg.append("Wired Device '{0}' is assigned to site {1}.".format(device_ip, site_name))

                continue

            if status == "success":
                if not to_force_provisioning:
                    self.already_provisioned_devices.append(device_ip)
                    success_msg.append("Wired Device '{0}' is already provisioned.".format(device_ip))
                    self.log(success_msg[-1], "INFO")

                    if not to_provisioning:
                        self.msg = ("Cannot assign a provisioned device to the site. "
                                    "The device is already provisioned. "
                                    "To re-provision the device, set both 'provisioning' and 'force_provisioning' to 'true', "
                                    "or unprovision the device and try again.")
                        self.set_operation_result("failed", False, self.msg, "ERROR")
                    continue

                self.log("Device '{0}' requires reprovisioning.".format(device_ip), "INFO")
                reprovision_needed.append(device_ip)
                reprovision_params.append({
                    "id": provision_id,
                    "siteId": site_id,
                    "networkDeviceId": network_device_id
                })

            else:
                if to_provisioning:
                    self.log("Device '{0}' requires provisioning.".format(device_ip), "INFO")
                    provision_needed.append(device_ip)
                    provision_params.append({
                        "siteId": site_id,
                        "networkDeviceId": network_device_id
                    })

        self.log("Provisioning/Reprovisioning evaluation:", "INFO")
        self.log("Provision Needed: {0}".format(provision_needed), "INFO")
        self.log("Reprovision Needed: {0}".format(reprovision_needed), "INFO")

        if set(already_provisioned_devices) == set(self.device_ips):
            self.msg = "All devices are already provisioned: {0}".format(already_provisioned_devices)
            self.set_operation_result("success", False, self.msg, "INFO")
            return self

        if reprovision_params:
            self.reprovision_wired_device(reprovision_params, device_ips=reprovision_needed)
            re_prov_success_msg = "re-provisioning of the device(s) '{0}' completed successfully.".format(reprovision_needed)
            success_msg.append(re_prov_success_msg)

        if provision_params:
            for i in range(0, len(provision_params), 100):
                batch_params = provision_params[i:i + 100]
                batch_devices = provision_needed[i:i + 100]
                self.log("Provisioning of the device(s) - {0} with the param - {1}".format(batch_devices, batch_params), "INFO")
                self.initialize_wired_provisioning(batch_params, device_ips=batch_devices)
                success_msg.append("Provisioning of the device(s) '{0}' completed successfully.".format(batch_devices))

        if success_msg:
            self.msg = success_msg
            self.set_operation_result("success", True, self.msg, "INFO")

        self.log("Bulk wired device provisioning process completed.", "INFO")
        return self

    def get_device_type(self):
        """
        Classifies devices as 'wired' or 'wireless' based on their family type from the Cisco DNA Center API.

        This function queries each device in `validated_config` to determine whether it is a wired or wireless device.
        The classification is stored in `self.device_dict`.

        Returns:
            dict: A dictionary with classified devices: {'wired': [list of wired device IPs], 'wireless': [list of wireless device IPs]}.
        """

        device_dict = {"wired": [], "wireless": []}

        for device in self.validated_config:
            ip_address = device.get("management_ip_address")
            if not ip_address:
                self.log("Skipping device with missing management IP address.", "WARNING")
                continue

            self.log("Fetching device details for IP: {0}".format(ip_address), "INFO")

            try:
                dev_response = self.dnac_apply['exec'](
                    family="devices",
                    function='get_network_device_by_ip',
                    params={"ip_address": ip_address}
                )

            except Exception as e:
                error_message = (
                    "The Device - {0} is already deleted from the Inventory or not present in the Cisco Catalyst Center."
                    .format(device["management_ip_address"])
                )
                self.log(error_message, "WARNING")
                continue

            if not dev_response or "response" not in dev_response:
                self.log("Invalid or empty response received for device '{0}': {1}".format(ip_address, str(dev_response)), "ERROR")
                continue

            self.log("Device response for '{0}': {1}".format(ip_address, str(dev_response)), "DEBUG")

            self.log("The device response from 'get_network_device_by_ip' API is {0}".format(str(dev_response)), "DEBUG")
            dev_dict = dev_response.get("response")
            device_family = dev_dict.get("family", None)

            if device_family == "Wireless Controller":
                device_type = "wireless"
            elif device_family in ["Switches and Hubs", "Routers"]:
                device_type = "wired"
            else:
                device_type = None

            self.log("The device type for IP {0} is {1}".format(device["management_ip_address"], device_type), "INFO")

            if device_type:
                device_dict[device_type].append(device["management_ip_address"])

        self.device_dict = device_dict
        self.log("Final device classification: {0}".format(device_dict), "INFO")

        return device_dict

    def get_device_provision_status(self, device_id, device_ip=None):
        """
        Retrieves the provisioning status and provision ID of a device based on its device ID.

        Args:
            device_id (str): The ID of the device for which provisioning status is to be retrieved.

        Returns:
            tuple: A tuple containing:
                - provision_id (str or None): The provision ID of the device if provisioned, None otherwise.
                - status (str): The status of the provisioning process, either 'success' or 'failed'.
        Description:
            Depending on the Cisco Catalyst Center (CCC) version, this function calls different APIs to
            check if a device is provisioned. It handles both wired and wireless device provisioning
            checks and logs relevant status and errors.

        """
        provision_id = None
        status = "failed"

        if isinstance(self.validated_config, list):
            device_management_ip = device_ip
        else:
            device_management_ip = self.validated_config.get("management_ip_address")

        self.log("Checking provisioning status for device with management IP '{0}' and ID '{1}'".format(device_management_ip, device_id), "DEBUG")
        if self.compare_dnac_versions(self.get_ccc_version(), "2.3.5.3") <= 0:
            self.log("Using 'get_provisioned_wired_device' API for Catalyst Center version <= 2.3.5.3", "DEBUG")
            try:
                status_response = self.dnac_apply['exec'](
                    family="sda",
                    function="get_provisioned_wired_device",
                    params={"device_management_ip_address": device_management_ip},
                )
                if status_response:
                    self.log("Received API response for device '{0}' from 'get_provisioned_wired_device' "
                             ": {1}".format(device_management_ip, status_response), "DEBUG")
                    status = status_response.get("status")
                else:
                    self.log("No status response received for wired device with management IP '{0}'".format(device_management_ip), "DEBUG")
            except Exception as e:
                self.log("Device '{0}' is not provisioned due to error: {1}".format(device_management_ip, str(e)), "ERROR")
                status = "failed"

        else:
            self.log("Using 'get_provisioned_devices' API for Catalyst Center version > 2.3.5.3", "DEBUG")
            try:
                api_response = self.dnac._exec(
                    family="sda",
                    function='get_provisioned_devices',
                    params={
                        "networkDeviceId": device_id
                    }
                )
                if api_response:
                    self.log("API response for device '{0}' from 'get_provisioned_devices': {1}".format(device_management_ip, api_response), "DEBUG")
                    provisioned_devices = api_response.get('response')
                    provision_id = provisioned_devices[0].get('id') if provisioned_devices else None

                    if provisioned_devices:
                        status = "success"
                    else:
                        status = "failed"

                    self.log("Provisioned devices found for '{0}': {1}".format(device_management_ip, bool(provisioned_devices)), "DEBUG")
                else:
                    self.log("No API response received for device '{0}' provisioning check".format(device_management_ip), "DEBUG")

            except Exception as e:
                self.msg = "Error in 'get_provisioned_devices' for device '{0}': {1}".format(device_management_ip, str(e))
                self.log(self.msg, "ERROR")
                self.result['response'] = self.msg

        self.log("Provision status for device with management IP '{0}': status='{1}', "
                 "provision_id='{2}'".format(device_management_ip, status, provision_id), "DEBUG")
        return provision_id, status

    def provision_wired_device(self, to_provisioning, to_force_provisioning):
        """
        Handle wired device provisioning.

        Args:
            self: An instance of a class used for interacting with Cisco Catalyst Center.
            to_provisioning (bool): Indicates if the device should be provisioned.
            to_force_provisioning (bool): Indicates if the device should be forcefully reprovisioned.

        Returns:
            self: An instance of the class with updated results and status based on
            the provisioning operation.

        Description:
            This function manages the provisioning of a wired device in Cisco Catalyst Center.
            It checks the current provisioning status of the device and, based on the flags
            `to_provisioning` and `to_force_provisioning`, decides whether to provision, reprovision,
            or skip the process. The function sends appropriate API requests, logs the outcomes,
            and updates the instance with provisioning status, task details, and any changes made.
            In case of errors, it logs them and sets the status to 'failed'.
        """
        device_id = self.get_device_id()
        self.log("Device ID retrieved: {0}".format(device_id), "DEBUG")

        provision_id , status = self.get_device_provision_status(device_id)
        self.log("Provision ID and status for device ID '{0}': provision_id='{1}', status='{2}'".format(device_id, provision_id, status), "DEBUG")

        site_exist, site_id = self.get_site_id(self.site_name)
        self.log("Site ID retrieval for site '{0}': site_exist={1}, site_id='{2}'".format(self.site_name, site_exist, site_id), "DEBUG")

        reprovision_param = [{"id": provision_id, "siteId": site_id, "networkDeviceId": device_id}]
        provision_params = [{"siteId": site_id, "networkDeviceId": device_id}]

        self.log("Reprovision parameters prepared: {0}".format(reprovision_param), "DEBUG")
        self.log("Provision parameters prepared: {0}".format(provision_params), "DEBUG")

        if status == "success":
            if not to_force_provisioning:
                self.result["changed"] = False
                msg = "Wired Device '{0}' is already provisioned.".format(self.validated_config.get("management_ip_address"))
                self.result['msg'] = msg
                self.result['response'] = msg
                self.log(msg, "INFO")
                return self

            if not to_provisioning:
                self.msg = ("Cannot assign a provisioned device to the site. "
                            "The device is already provisioned. "
                            "To re-provision the device, ensure that both 'provisioning' and 'force_provisioning' are set to 'true'. "
                            "Alternatively, unprovision the device and try again.")
                self.log(self.msg, "ERROR")
                self.status = "failed"
                return self

            self.reprovision_wired_device(reprovision_param)
            return self

        self.log("Checking if provisioning is required based on status.", "INFO")
        if not to_provisioning:
            self.log("Provisioning not required; assigning device '{0}' to site '{1}' with site "
                     "ID '{2}'.".format(device_id, self.site_name, site_id), "INFO")
            self.assign_device_to_site([device_id], self.site_name, site_id)
        else:
            if self.compare_dnac_versions(self.get_ccc_version(), "2.3.5.3") <= 0:
                self.log("Catalyst Center Version is 2.3.5.3 or earlier; directly initializing provisioning with parameters.", "INFO")
                self.initialize_wired_provisioning(provision_params)
            else:
                self.log("Catalyst Center Version is later than 2.3.5.3; checking if device '{0}' is assigned to site.".format(device_id), "INFO")

                is_device_assigned_to_a_site, device_site_name = self.is_device_assigned_to_site_v1(device_id)
                if is_device_assigned_to_a_site:
                    if device_site_name != self.site_name:
                        self.msg = (
                            "Error in provisioning a wired device '{0}' - the device is already associated "
                            "with a Site {1} and cannot be provisioned to Site {2}."
                        ).format(self.device_ip, device_site_name, self.site_name)
                        self.set_operation_result("failed", False, self.msg, "ERROR").check_return_status()
                    else:
                        self.log("Device '{0}' is already assigned to site. Proceeding with provisioning.".format(device_id), "DEBUG")
                        self.initialize_wired_provisioning(provision_params)
                else:
                    self.log("Device '{0}' is not assigned to site '{1}'. Assigning device and "
                             "initializing provisioning.".format(device_id, self.site_name), "DEBUG")
                    self.assign_device_to_site([device_id], self.site_name, site_id)
                    self.initialize_wired_provisioning(provision_params)

        return self

    def reprovision_wired_device(self, reprovision_param, device_ips=None):
        """
        Reprovision a wired device.

        Args:
            self: An instance of a class used for interacting with Cisco Catalyst Center.

        Returns:
            self: An instance of the class with updated results and status after the
            wired device has been reprovisioned.

        Description:
            This function handles the reprovisioning of a wired device in Cisco Catalyst Center.
            It sends an API request to the 're_provision_wired_device' endpoint using the device's
            provisioning parameters. The function tracks the task status and updates the class instance
            with the reprovisioning status, task ID, and other relevant details. If an error occurs during
            the reprovisioning process, it logs the error and adjusts the status accordingly.
        """
        if self.compare_dnac_versions(self.get_ccc_version(), "2.3.5.3") <= 0:
            self.log("Starting reprovisioning of wired device using 're_provision_wired_device' API.", "DEBUG")
            try:
                response = self.dnac_apply['exec'](
                    family="sda",
                    function="re_provision_wired_device",
                    op_modifies=True,
                    params=self.want["prov_params"],
                )
                taskid = response.get("taskId")
                self.log("Received task ID '{0}' for wired device reprovisioning.".format(taskid), "DEBUG")
                while True:
                    result = self.get_task_details(taskid)
                    self.log("Checking task status for ID '{0}': {1}".format(taskid, result), "DEBUG")
                    if "processcfs_complete=true" in result.get("data"):
                        self.msg = ("Wired Device '{0}' re-provisioning completed successfully.".format(self.device_ip))
                        self.log(self.msg, "INFO")
                        self.result["changed"] = True
                        self.result['msg'] = ("Wired Device '{0}' re-provisioning completed successfully.".format(self.device_ip))
                        self.result['response'] = self.msg
                        self.log(self.result['msg'], "INFO")
                        return self

                    elif result.get("isError") is True:
                        self.log("Error in task status for wired device reprovisioning. Task ID: '{0}'".format(taskid), "ERROR")
                        raise Exception

            except Exception as e:
                self.msg = "Error in re-provisioning device '{0}' due to {1}".format(self.device_ip, str(e))
                self.log(self.msg, "ERROR")
                self.result['response'] = self.msg
                self.status = "failed"
                self.check_return_status()
        else:
            try:
                self.log("Starting reprovisioning of wired device using 're_provision_devices' API.", "DEBUG")
                response = self.dnac_apply['exec'](
                    family="sda",
                    function="re_provision_devices",
                    op_modifies=True,
                    params={"payload": reprovision_param}
                )
                self.log("Received response for 're_provision_devices': {0}".format(response), "DEBUG")
                self.check_tasks_response_status(response, api_name='re_provision_devices')
                self.log("Task status after 're_provision_devices' execution: {0}".format(self.status), "DEBUG")

                if self.status not in ["failed", "exited"]:
                    self.msg = ("Wired Device '{0}' re-provisioning completed successfully.".format(device_ips))
                    self.set_operation_result("success", True, self.msg, "INFO")

            except Exception as e:
                self.msg = "Error in re-provisioning device '{0}' due to {1}".format(device_ips, str(e))
                self.set_operation_result("failed", False, self.msg, "ERROR").check_return_status()

    def initialize_wired_provisioning(self, provision_params, device_ips=None):
        """
        Provision a wired device.

        Args:
            self: An instance of a class used for interacting with Cisco Catalyst Center.

        Returns:
            self: An instance of the class with updated results and status after the wired
            device has been provisioned.

        Description:
            This function handles the provisioning of a wired device in Cisco Catalyst Center.
            It sends an API request to the 'provision_wired_device' endpoint with the required
            parameters. If provisioning is successful, the class instance is updated with the
            provisioning status, task ID, and execution details. In case of any errors during
            provisioning, it logs the error and updates the status accordingly.
        """

        if self.compare_dnac_versions(self.get_ccc_version(), "2.3.5.3") <= 0:
            try:
                self.log("Starting wired device provisioning with 'provision_wired_device' API.", "DEBUG")
                response = self.dnac_apply['exec'](
                    family="sda",
                    function="provision_wired_device",
                    op_modifies=True,
                    params=self.want["prov_params"],
                )
                if response:
                    self.log("Received API response from 'provision_wired_device': {0}".format(str(response)), "DEBUG")
                    if self.status not in ["failed", "exited"]:
                        success_msg = "Provisioning of the device '{0}' completed successfully.".format(self.device_ip)
                        self.log(success_msg, "INFO")
                        self.result["changed"] = True
                        self.result['msg'] = success_msg
                        self.result['response'] = success_msg
                        return self

            except Exception as e:
                self.msg = "Error in provisioning device '{0}' due to {1}".format(self.device_ip, str(e))
                self.log(self.msg, "ERROR")
                self.status = "failed"
                self.result['response'] = self.msg
                self.check_return_status()
        else:
            try:
                self.log("Starting wired device provisioning with 'provision_devices' API.", "DEBUG")
                response = self.dnac._exec(
                    family="sda",
                    function='provision_devices',
                    op_modifies=True,
                    params={"payload": provision_params}
                )
                if response:
                    self.log("Received API response from 'provision_devices': {0}".format(str(response)), "DEBUG")
                    self.check_tasks_response_status(response, api_name='provision_device')

                    if self.status not in ["failed", "exited"]:
                        success_msg = "Provisioning of the device(s) '{0}' completed successfully.".format(device_ips)
                        self.set_operation_result("success", True, self.msg, "INFO")

                    if self.status in ['failed', 'exited']:
                        fail_reason = self.msg
                        self.log("Exception occurred during 'provisioned_devices': {0}".format(str(fail_reason)), "ERROR")
                        self.msg = "Error in provisioned device '{0}' due to {1}".format(device_ips, str(fail_reason))
                        self.set_operation_result("failed", False, self.msg, "ERROR").check_return_status()

            except Exception as e:
                self.msg = "Error in provisioning device '{0}' due to {1}".format(device_ips, str(e))
                self.set_operation_result("failed", False, self.msg, "ERROR").check_return_status()

    def provision_wireless_device(self):
        """
        Provision a wireless device.

        Args:
            self: An instance of a class used for interacting with Cisco Catalyst Center.
            want (dict): A dictionary containing the provisioning parameters for the wireless device.

        Returns:
            self: An instance of the class with updated results and status based on
            the provisioning operation.

        Description:
            This function is responsible for provisioning a wireless device in Cisco Catalyst Center.
            It sends a request using the 'provision' API and handles the execution status.
            If an error occurs during the provisioning process, it logs the error and updates
            the instance status accordingly.
        """

        self.log("Starting provisioning process for wireless device", "INFO")

        prov_params = self.want.get("prov_params")
        if not prov_params or not isinstance(prov_params, list) or not prov_params[0]:
            self.log("Error: 'prov_params' is missing or improperly formatted. Expected a non-empty list.", "ERROR")
            self.status = "failed"
            self.result['response'] = "Provisioning aborted due to missing or invalid 'prov_params'."
            return self

        prov_params_data = prov_params[0]
        device_uid = prov_params_data.get("device_id")
        site_name = self.validated_config.get("site_name_hierarchy")
        primary_ap_location = prov_params_data.get("primaryManagedAPLocationsSiteIds")
        secondary_ap_location = prov_params_data.get("secondaryManagedAPLocationsSiteIds")
        site_exist, site_id = self.get_site_id(site_name)

        self.log("Provisioning wireless device with device_id: {0}".format(device_uid), "DEBUG")
        self.log("Site name: {0}".format(site_name), "DEBUG")
        self.log("Primary AP location: {0}".format(primary_ap_location), "DEBUG")
        self.log("Secondary AP location: {0}".format(secondary_ap_location), "DEBUG")

        if self.compare_dnac_versions(self.get_ccc_version(), "2.3.7.6") >= 0:
            primary_ap_location_site_id_list = []
            secondary_ap_location_site_id_list = []

            if primary_ap_location:
                self.log("Processing primary access point locations", "INFO")
                for primary_sites in primary_ap_location:
                    self.log("Retrieving site ID for primary location: {0}".format(primary_sites), "DEBUG")
                    site_exist, primary_ap_location_site_id = self.get_site_id(primary_sites)
                    primary_ap_location_site_id_list.append(primary_ap_location_site_id)

            if secondary_ap_location:
                self.log("Processing secondary access point locations", "INFO")
                for secondary_sites in secondary_ap_location:
                    self.log("Retrieving site ID for secondary location: {0}".format(secondary_sites), "DEBUG")
                    site_exist, secondary_ap_location_site_id = self.get_site_id(secondary_sites)
                    secondary_ap_location_site_id_list.append(secondary_ap_location_site_id)

        if self.compare_dnac_versions(self.get_ccc_version(), "2.3.5.3") <= 0:

            param = [
                {
                    "deviceName": prov_params[0].get("deviceName"),
                    "site": prov_params[0].get("site"),
                    "managedAPLocations": self.floor_names,
                    "dynamicInterfaces": prov_params[0].get("dynamicInterfaces")
                }
            ]

            self.log("Detected Catalyst Center version <= 2.3.5.3; using old provisioning method", "INFO")
            try:
                response = self.dnac_apply['exec'](
                    family="wireless",
                    function="provision",
                    op_modifies=True,
                    params={"payload": param}
                )
                execution_id = response.get("executionId")
                self.log("Received execution ID for provisioning: {0}".format(execution_id), "DEBUG")
                self.get_execution_status_wireless(execution_id=execution_id)
                self.result["changed"] = True
                self.result['msg'] = "Wireless device provisioned successfully"
                self.result['diff'] = self.validated_config
                self.result['response'] = execution_id
                self.log(self.result['msg'], "INFO")
                return self

            except Exception as e:
                self.msg = "Error in wireless provisioning: {0}".format(str(e))
                self.log(self.msg, "ERROR")
                self.status = "failed"
                self.result['response'] = self.msg
                self.check_return_status()

        else:
            self.log("Detected Catalyst Center version > 2.3.5.3; using new provisioning method", "INFO")
            self.log("Checking if device is assigned to the site", "INFO")
            is_device_assigned_to_a_site, device_site_name = self.is_device_assigned_to_site_v1(device_uid)

            if is_device_assigned_to_a_site is False:
                self.log("Device {0} is not assigned to site {1}; assigning now.".format(device_uid, site_name), "INFO")
                self.assign_device_to_site([device_uid], site_name, site_id)

            device_id = self.get_device_id()
            self.log("Retrieved device ID: {0}".format(device_id), "DEBUG")

            is_device_assigned_to_a_site, device_site_name = self.is_device_assigned_to_site_v1(device_uid)

            if is_device_assigned_to_a_site is True:
                if device_site_name != self.site_name:
                    self.msg = ("Error in re-provisioning a wireless device '{0}' - the device is already associated "
                                "with a Site {1} and cannot be re-provisioned to Site {2}.".format(self.device_ip, device_site_name, self.site_name))
                    self.log(self.msg, "ERROR")
                    self.result['response'] = self.msg
                    self.status = "failed"
                    self.check_return_status()

            if primary_ap_location or secondary_ap_location:
                self.log("Assigning managed AP locations to device ID: {0}".format(device_uid), "INFO")
                try:
                    self.log("Assigning managed AP locations for the WLC", "INFO")
                    response = self.dnac_apply['exec'](
                        family="wireless",
                        function="assign_managed_ap_locations_for_w_l_c",
                        op_modifies=True,
                        params={'device_id': device_uid,
                                'primaryManagedAPLocationsSiteIds':
                                    primary_ap_location_site_id_list,
                                'secondaryManagedAPLocationsSiteIds':
                                    secondary_ap_location_site_id_list,
                                }
                    )
                    self.log("API response from 'assign_managed_ap_locations_for_w_l_c': {}".format(str(response)), "DEBUG")
                    if response:
                        self.log("Received API response from 'assign_managed_ap_locations_for_w_l_c': {0}".format(str(response)), "DEBUG")
                        self.check_tasks_response_status(response, api_name='assign_managed_ap_locations_for_w_l_c')
                        if self.status not in ["failed", "exited"]:
                            self.log("wireless Device '{0}' assign_managed_ap_locations_for_w_l_c completed successfully.".format(self.device_ip), "INFO")

                        if self.status == 'failed':
                            fail_reason = self.msg
                            self.log("Exception occurred during 'assign_managed_ap_locations_for_w_l_c': {0}".format(str(fail_reason)), "ERROR")
                            self.msg = "Error in 'assign_managed_ap_locations_for_w_l_c' '{0}' due to {1}".format(self.device_ip, str(fail_reason))
                            self.log(self.msg, "ERROR")
                            self.status = "failed"
                            self.result['response'] = self.msg
                            self.check_return_status()

                except Exception as e:
                    self.log("Exception occurred during 'assign_managed_ap_locations_for_w_l_c': {0}".format(str(e)), "ERROR")
                    self.msg = "Error in 'assign_managed_ap_locations_for_w_l_c' '{0}' due to {1}".format(self.device_ip, str(e))
                    self.log(self.msg, "ERROR")
                    self.status = "failed"
                    self.result['response'] = self.msg
                    self.check_return_status()

            self.log("Starting wireless controller provisioning for device ID: {0}".format(device_uid), "INFO")
            prov_params = self.want.get("prov_params")[0]
            payload = {
                'device_id': prov_params.get('device_id'),
                'interfaces': []
            }

            self.log("Processing interfaces if they exist", "INFO")
            self.log("Building payload for wireless provisioning", "INFO")
            if 'dynamicInterfaces' in prov_params:
                self.log("Processing dynamic interfaces", "INFO")
                for interface in prov_params['dynamicInterfaces']:
                    cleaned_interface = {}
                    for k, v in interface.items():
                        if v is not None:
                            cleaned_interface[k] = v
                        else:
                            self.log("No dynamic interfaces found in provisioning parameters", "DEBUG")
                    payload['interfaces'].append(cleaned_interface)
                    self.log("Processed dynamic interface: {0}".format(cleaned_interface), "DEBUG")

            skip_ap_provision = prov_params.get('skip_ap_provision')
            self.log("Processing 'rolling_ap_upgrade' if it exists", "INFO")

            if skip_ap_provision is not None:
                payload['skipApProvision'] = skip_ap_provision
                self.log("Set 'skip_ap_provision'  to: {0}".format(skip_ap_provision), "DEBUG")
            else:
                self.log("'skip_ap_provision'  is not specified", "DEBUG")

            self.log("Processing rolling AP upgrade settings", "INFO")
            if 'rolling_ap_upgrade' in prov_params:
                self.log("Found 'rolling_ap_upgrade' in provisioning parameters", "DEBUG")
                rolling_ap_upgrade = {}
                for k, v in prov_params['rolling_ap_upgrade'].items():
                    if v is not None:
                        rolling_ap_upgrade[k] = v
                        self.log("Processed 'rolling_ap_upgrade': {0}".format(rolling_ap_upgrade), "DEBUG")
                    else:
                        self.log("No 'rolling_ap_upgrade' found in provisioning parameters", "DEBUG")
                payload['rollingApUpgrade'] = rolling_ap_upgrade

            try:
                response = self.dnac_apply['exec'](
                    family="wireless",
                    function="wireless_controller_provision",
                    op_modifies=True,
                    params=payload
                )

                if response:
                    self.log("Received API response from 'wireless_controller_provision': {0}".format(str(response)), "DEBUG")
                    self.check_tasks_response_status(response, api_name='wireless_controller_provision')
                    if self.status not in ["failed", "exited"]:
                        self.log("wireless Device '{0}' provisioning completed successfully.".format(self.device_ip), "INFO")
                        self.result["changed"] = True
                        self.result['msg'] = "Provisioning of the wireless device '{0}' completed successfully.".format(self.device_ip)
                        self.result['response'] = "Provisioning of the wireless device '{0}' completed successfully.".format(self.device_ip)
                        self.log(self.result['msg'], "INFO")
                        return self
            except Exception as e:
                self.log("Exception occurred during provisioning: {0}".format(str(e)), "ERROR")
                self.msg = "Error in provisioning wireless device '{0}' due to {1}".format(self.device_ip, str(e))
                self.log(self.msg, "ERROR")
                self.status = "failed"
                self.result['response'] = self.msg
                self.check_return_status()

    def get_diff_deleted(self):
        """
        Delete from provision database
        Args:
            self: An instance of a class used for interacting with Cisco Catalyst Center
        Returns:
            self: An instance of the class with updated results and status based on
            the deletion operation.
        Description:
            This function is responsible for removing devices from the Cisco Catalyst Center PnP GUI and
            raise Exception if any error occured.
        """

        device_type = self.want.get("device_type")
        if device_type is None:
            self.msg = (
                "The Device - {0} is already deleted from the Inventory or not present in the Cisco Catalyst Center."
                .format(self.validated_config.get("management_ip_address"))
            )
            self.set_operation_result("success", False, self.msg, "INFO")
            return self

        if device_type != "wired":
            self.result['msg'] = "APIs are not supported for the device"
            self.log(self.result['msg'], "CRITICAL")
            return self

        device_id = self.get_device_id()
        provision_id , status = self.get_device_provision_status(device_id)

        if status != "success":
            self.result['msg'] = "Device associated with the passed IP address is not provisioned"
            self.log(self.result['msg'], "CRITICAL")
            self.result['response'] = self.want["prov_params"]
            return self

        if self.compare_dnac_versions(self.get_ccc_version(), "2.3.5.3") <= 0:

            try:
                response = self.dnac_apply['exec'](
                    family="sda",
                    function="delete_provisioned_wired_device",
                    op_modifies=True,
                    params={
                        "device_management_ip_address": self.validated_config["management_ip_address"]
                    },
                )
                self.log("Response collected from the 'delete_provisioned_wired_device' API is : {0}".format(str(response)), "DEBUG")

                task_id = response.get("taskId")
                deletion_info = self.get_task_status(task_id=task_id)
                self.result["changed"] = True
                self.result['msg'] = "Deletion done Successfully"
                self.result['diff'] = self.validated_config
                self.result['response'] = task_id
                self.log(self.result['msg'], "INFO")
                return self

            except Exception as e:
                self.msg = "Error in delete provisioned device '{0}' due to {1}".format(self.device_ip, str(e))
                self.log(self.msg, "ERROR")
                self.status = "failed"
                self.result['response'] = self.msg
                self.check_return_status()

        else:
            try:
                response = self.dnac._exec(
                    family="sda",
                    function='delete_provisioned_devices',
                    op_modifies=True,
                    params={'networkDeviceId': device_id},
                )
                self.log("Received API response from 'delete_provisioned_devices': {0}".format(str(response)), "DEBUG")
                self.check_tasks_response_status(response, api_name='delete_provisioned_devices')

                if self.status not in ["failed", "exited"]:
                    self.result["changed"] = True
                    self.result['msg'] = "Deletion done Successfully for the device '{0}' ".format(self.validated_config["management_ip_address"])
                    self.result['diff'] = self.validated_config
                    self.result['response'] = self.result['msg']
                    self.log(self.result['msg'], "INFO")
                    return self

                if self.status in ['failed', 'exited']:
                    fail_reason = self.msg
                    self.log("Exception occurred during 'delete_provisioned_devices': {0}".format(str(fail_reason)), "ERROR")
                    self.msg = "Error in delete provisioned device '{0}' due to {1}".format(self.device_ip, str(fail_reason))
                    self.log(self.msg, "ERROR")
                    self.status = "failed"
                    self.result['response'] = self.msg
                    self.check_return_status()

            except Exception as e:
                self.msg = "Error in delete provisioned device '{0}' due to {1}".format(self.device_ip, str(e))
                self.log(self.msg, "ERROR")
                self.status = "failed"
                self.result['response'] = self.msg
                self.check_return_status()

    def verify_diff_merged(self):
        """
        Verify the merged status(Creation/Updation) of Discovery in Cisco Catalyst Center.
        Args:
            - self (object): An instance of a class used for interacting with Cisco Catalyst Center.
            - config (dict): The configuration details to be verified.
        Return:
            - self (object): An instance of a class used for interacting with Cisco Catalyst Center.
        Description:
            This method checks the merged status of a configuration in Cisco Catalyst Center by
            retrieving the current state (have) and desired state (want) of the configuration,
            logs the states, and validates whether the specified device(s) exists in the DNA
            Center configuration's Inventory Database in the provisioned state.
        """
        if (
            self.compare_dnac_versions(self.get_ccc_version(), "2.3.5.3") <= 0
            or (
                self.compare_dnac_versions(self.get_ccc_version(), "2.3.7.6") >= 0
                and self.device_type == 'wireless'
            )
        ):
            self.log("validate Cisco Catalyst Center config for merged state", "INFO")
            self.log("Desired State (want): {0}".format(str(self.want)), "INFO")

            device_type = self.want.get("device_type")
            provisioning = self.validated_config.get("provisioning")
            site_name_hierarchy = self.validated_config.get("site_name_hierarchy")
            uuid = self.get_device_id()
            if provisioning is False:
                if self.is_device_assigned_to_site(uuid) is True:
                    self.log("Requested device is already added to the site {0}".format(site_name_hierarchy), "INFO")
                else:
                    self.log("Requested device is not added to the site {0}".format(site_name_hierarchy), "INFO")
                return self

            if device_type == "wired":
                try:
                    status_response = self.dnac_apply['exec'](
                        family="sda",
                        function="get_provisioned_wired_device",
                        params={
                            "device_management_ip_address": self.validated_config["management_ip_address"]
                        },
                    )
                except Exception:
                    status_response = {}
                self.log("Wired device's status Response collected from 'get_provisioned_wired_device' API is:{0}".format(str(status_response)), "DEBUG")
                status = status_response.get("status")
                self.log("The provisioned status of the wired device is {0}".format(status), "INFO")

                if status == "success":
                    self.log("Requested wired device is alread provisioned", "INFO")

                else:
                    self.log("Requested wired device is not provisioned", "INFO")

            else:
                self.log("Currently we don't have any API in the Cisco Catalyst Center to fetch the provisioning details of wireless devices", "INFO")

        else:
            for config in self.validated_config:
                device_ip = config.get("management_ip_address")
                self.device_ips.append(device_ip)
                device_id = self.get_device_ids_from_device_ips([device_ip])

                # Ensure device_id exists before proceeding
                network_device_id = device_id.get(device_ip)
                if not network_device_id:
                    self.log("Device ID not found for IP {}".format(device_ip), "ERROR")
                    continue

                provision_id, status = self.get_device_provision_status(network_device_id, device_ip)
                self.log(
                    "Provision ID and status for device '{0}': provision_id='{1}', status='{2}'".format(
                        device_ip, provision_id, status
                    ),
                    "DEBUG",
                )

                if status == "success":
                    self.log("Requested wired device is alread provisioned", "INFO")

                else:
                    self.log("Requested wired device is not provisioned", "INFO")

        return self

    def verify_diff_deleted(self):
        """
        Verify the deletion status of Discovery in Cisco Catalyst Center.
        Args:
            - self (object): An instance of a class used for interacting with Cisco Catalyst Center.
            - config (dict): The configuration details to be verified.
        Return:
            - self (object): An instance of a class used for interacting with Cisco Catalyst Center.
        Description:
            This method checks the deletion status of a configuration in Cisco Catalyst Center.
            It validates whether the specified discovery(s) exists in the Cisco Catalyst Center configuration's
            Inventory Database in the provisioned state.
        """
        self.log("validate Cisco Catalyst Center config for deleted state", "INFO")
        self.log("Desired State (want): {0}".format(str(self.want)), "INFO")

        device_type = self.want.get("device_type")
        if device_type == "wired":
            try:
                status_response = self.dnac_apply['exec'](
                    family="sda",
                    function="get_provisioned_wired_device",
                    params={
                        "device_management_ip_address": self.validated_config["management_ip_address"]
                    },
                )
            except Exception:
                status_response = {}
            self.log("Wired device's status Response collected from 'get_provisioned_wired_device' API is:{0}".format(str(status_response)), "DEBUG")
            status = status_response.get("status")
            self.log("The provisioned status of the wired device is {0}".format(status), "INFO")

            if status == "success":
                self.log("Requested wired device is in provisioned state and is not unprovisioned", "INFO")

            else:
                self.log("Requested wired device is unprovisioned", "INFO")

        else:
            self.log("Currently we don't have any API in the Cisco Catalyst Center to fetch the provisioning details of wireless devices")
        self.status = "success"

        return self


def main():

    """
    main entry point for module execution
    """

    element_spec = {'dnac_host': {'required': True, 'type': 'str'},
                    'dnac_port': {'type': 'str', 'default': '443'},
                    'dnac_username': {'type': 'str', 'default': 'admin', 'aliases': ['user']},
                    'dnac_password': {'type': 'str', 'no_log': True},
                    'dnac_verify': {'type': 'bool', 'default': 'True'},
                    'dnac_version': {'type': 'str', 'default': '2.2.3.3'},
                    'dnac_debug': {'type': 'bool', 'default': False},
                    'dnac_log': {'type': 'bool', 'default': False},
                    "dnac_log_level": {"type": 'str', "default": 'WARNING'},
                    "dnac_log_file_path": {"type": 'str', "default": 'dnac.log'},
                    "dnac_log_append": {"type": 'bool', "default": True},
                    "config_verify": {"type": 'bool', "default": False},
                    'dnac_api_task_timeout': {'type': 'int', "default": 1200},
                    'dnac_task_poll_interval': {'type': 'int', "default": 2},
                    'validate_response_schema': {'type': 'bool', 'default': True},
                    'config': {'required': True, 'type': 'list', 'elements': 'dict'},
                    'state': {'default': 'merged', 'choices': ['merged', 'deleted']}
                    }
    module = AnsibleModule(argument_spec=element_spec,
                           supports_check_mode=False)
    ccc_provision = Provision(module)
    config_verify = ccc_provision.params.get("config_verify")

    state = ccc_provision.params.get("state")
    if state not in ccc_provision.supported_states:
        ccc_provision.status = "invalid"
        ccc_provision.msg = "State {0} is invalid".format(state)
        ccc_provision.check_return_status()

    ccc_provision.validate_input(state=state).check_return_status()

    is_version_valid = ccc_provision.compare_dnac_versions(ccc_provision.get_ccc_version(), "2.3.7.6") >= 0

    if is_version_valid:
        ccc_provision.log("Fetching device types from Cisco Catalyst Center.", "INFO")
        device_dict = ccc_provision.get_device_type()
        ccc_provision.log("Device classification result: {0}".format(device_dict), "DEBUG")

    if is_version_valid and state == "merged":
        for device_type, devices in device_dict.items():
            if not devices:
                ccc_provision.log("No devices found for type '{0}', skipping.".format(device_type), "INFO")
                continue

            ccc_provision.log("Processing {0} devices: {1}".format(device_type, devices), "INFO")
            ccc_provision.reset_values()

            if device_type == "wired":
                ccc_provision.device_type = "wired"
                ccc_provision.log("Applying configuration for wired devices.", "INFO")
                ccc_provision.get_diff_state_apply[state]().check_return_status()
                if config_verify:
                    ccc_provision.log("Verifying configuration for wired devices.", "INFO")
                    ccc_provision.verify_diff_state_apply[state]().check_return_status()
            else:
                ccc_provision.device_type = "wireless"
                for config in ccc_provision.validated_config:
                    device_ip = config.get("management_ip_address")
                    if device_ip in ccc_provision.device_dict['wireless']:
                        ccc_provision.log("Applying configuration for wireless device: {0}".format(device_ip), "INFO")
                        ccc_provision.reset_values()
                        ccc_provision.get_want(config).check_return_status()
                        ccc_provision.get_diff_state_apply[state]().check_return_status()
                        if config_verify:
                            ccc_provision.log("Verifying configuration for wireless device: {0}".format(device_ip), "INFO")
                            ccc_provision.verify_diff_state_apply[state]().check_return_status()

    else:
        for config in ccc_provision.validated_config:
            ccc_provision.log("Processing device with management IP: {0}".format(config.get("management_ip_address")), "INFO")
            ccc_provision.reset_values()
            ccc_provision.get_want(config).check_return_status()
            ccc_provision.get_diff_state_apply[state]().check_return_status()
            if config_verify:
                ccc_provision.log("Verifying configuration for device with management IP: {0}".format(config.get("management_ip_address")), "INFO")
                ccc_provision.verify_diff_state_apply[state]().check_return_status()

    module.exit_json(**ccc_provision.result)


if __name__ == '__main__':
    main()
