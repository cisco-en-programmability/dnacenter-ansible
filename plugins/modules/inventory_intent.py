#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2022, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import absolute_import, division, print_function

__metaclass__ = type
__author__ = ("Madhan Sankaranarayanan, Abhishek Maheshwari")

DOCUMENTATION = r"""
---
module: inventory_intent
short_description: Resource module for Network Device
description:
- Manage operations create, update and delete of the resource Network Device.
- Adds the device with given credential.
- Deletes the network device for the given Id.
- Sync the devices provided as input.
version_added: '6.8.0'
extends_documentation_fragment:
  - cisco.dnac.intent_params
author: Abhishek Maheshwari (@abmahesh)
        Madhan Sankaranarayanan (@madhansansel)
options:
  state:
    description: The state of Cisco DNA Center after module completion.
    type: str
    choices: [ merged, deleted ]
    default: merged
  config:
    description: List of devices with credentails to perform Add/Update/Delete/Resync operation
    type: list
    elements: dict
    required: True
    suboptions:
      cli_transport:
        description: Device's cli transport protocol. Required for Adding Network Devices.
        type: str
      compute_device:
        description: Compute Device flag.
        type: bool
      enable_password:
        description: Device's enable password.
        type: str
      extended_discovery_info:
        description: Device's extended discovery info.
        type: str
      http_password:
        description: Device's http password. Required for Adding Compute, Meraki, Firepower Management Devices.
        type: str
      http_port:
        description: Device's http port number. Required for Adding Compute, Firepower Management Devices.
        type: str
      http_secure:
        description: HttpSecure flag.
        type: bool
      http_username:
        description: Device's http username. Required for Adding Compute,Firepower Management Devices.
        type: str
      id:
        description: Id path parameter that is Device ID. Required for Deleting/Updating Device Roles.
        type: str
      ip_address:
        description: Device's ipAddress. Required for Adding/Updating/Deleting/Resyncing Device except Meraki Devices.
        elements: str
        type: list
      meraki_org_id:
        description: Device's meraki org id.
        elements: str
        type: list
      netconf_port:
        description: Device's netconf port.
        type: str
      username:
        description: Network Device's username. Required for Adding Network Device.
        type: str
      password:
        description: Device's password. Required for Adding Network Device.
            Also needed for file encryption while exporting device in a csv file.
        type: str
      serial_number:
        description: Device's serial number.
        type: str
      snmp_auth_passphrase:
        description: Device's snmp auth passphrase. Required for Adding Network, Compute, Third Party Devices.
        type: str
      snmp_auth_protocol:
        description: Device's snmp Auth Protocol.
        type: str
        default: "SHA"
      snmp_mode:
        description: Device's snmp Mode.
        type: str
        default: "AUTHPRIV"
      snmp_priv_passphrase:
        description: Device's snmp Private Passphrase. Required for Adding Network, Compute, Third Party Devices.
        type: str
      snmp_priv_protocol:
        description: Device's snmp Private Protocol. Required for Adding Network, Compute, Third Party Devices.
        type: str
        default: "AES128"
      snmp_ro_community:
        description: Device's snmp ROCommunity. Required for Adding V2C Devices.
        type: str
        default: public
      snmp_rw_community:
        description: Device's snmp RWCommunity. Required for Adding V2C Devices.
        type: str
        default: private
      snmp_retry:
        description: Device's snmp Retry.
        type: int
        default: 3
      snmp_timeout:
        description: Device's snmp Timeout.
        type: int
        default: 5
      snmp_username:
        description: Device's snmp Username. Required for Adding Network, Compute, Third Party Devices.
        type: str
      snmp_version:
        description: Device's snmp Version.
        type: str
        default: "v3"
      type:
        description: Select Device's type from NETWORK_DEVICE, COMPUTE_DEVICE, MERAKI_DASHBOARD, THIRD_PARTY_DEVICE, FIREPOWER_MANAGEMENT_SYSTEM.
        type: str
        default: "NETWORK_DEVICE"
      update_mgmt_ipaddresslist:
        description: Network Device's update Mgmt IPaddress List.
        type: list
        elements: dict
        suboptions:
          exist_mgmt_ipaddress:
            description: Device's existing Mgmt IpAddress.
            type: str
          new_mgmt_ipaddress:
            description: Device's new Mgmt IpAddress.
            type: str
      force_sync:
        description: If forcesync is true then device sync would run in high priority thread if available, else the sync will fail.
        type: bool
        default: false
      clean_config:
        description: Required if need to delete the Provisioned device by clearing current configuration.
        type: bool
        default: false
      role:
        description: Role of device which can be ACCESS, CORE, DISTRIBUTION, BORDER ROUTER, UNKNOWN.
        type: str
        default: "ACCESS"
      role_source:
        description: role source for the Device.
        type: str
        default: "AUTO"
      name:
        description: Name of Global User Defined Field. Required for creating/deleting UDF and then assigning it to device.
        type: str
      description:
        description: Info about the global user defined field. Also used while updating interface details.
        type: str
      value:
        description: Value to assign to tag with or without the same user defined field name.
        type: str
      admin_status:
        description: Status of Interface of a device, it can be (UP/DOWN).
        type: str
      vlan_id:
        description: Unique Id number assigned to a VLAN within a network.
        type: int
      voice_vlan_id:
        description: Identifier used to distinguish a specific VLAN that is dedicated to voice traffic.
        type: int
      deployment_mode:
        description: Preview/Deploy [Preview means the configuration is not pushed to the device. Deploy makes the configuration pushed to the device]
        type: str
        default: "Deploy"
      site_name:
        description: Required for Provisioning of Wired and Wireless Devices.
        type: str
      operation_enum:
        description: enum(CREDENTIALDETAILS, DEVICEDETAILS) 0 to export Device Credential Details Or 1 to export Device Details.
        type: str
      parameters:
        description: List of device parameters that needs to be exported to file.
        type: str


requirements:
- dnacentersdk >= 2.5.5
- python >= 3.5
seealso:
- name: Cisco DNA Center documentation for Devices AddDevice2
  description: Complete reference of the AddDevice2 API.
  link: https://developer.cisco.com/docs/dna-center/#!add-device
- name: Cisco DNA Center documentation for Devices DeleteDeviceById
  description: Complete reference of the DeleteDeviceById API.
  link: https://developer.cisco.com/docs/dna-center/#!delete-device-by-id
- name: Cisco DNA Center documentation for Devices SyncDevices2
  description: Complete reference of the SyncDevices2 API.
  link: https://developer.cisco.com/docs/dna-center/#!sync-devices
notes:
  - SDK Method used are
    devices.Devices.add_device,
    devices.Devices.delete_device_by_id,
    devices.Devices.sync_devices,

  - Paths used are
    post /dna/intent/api/v1/network-device,
    delete /dna/intent/api/v1/network-device/{id},
    put /dna/intent/api/v1/network-device,

  - Removed 'managementIpAddress' options in v4.3.0.
"""

EXAMPLES = r"""
- name: Add/Update new device in Inventory with full credentials
  cisco.dnac.inventory_intent:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    dnac_log: False
    state: merged
    config:
      - cli_transport: string
        compute_device: true
        enable_password: string
        extended_discovery_info: string
        http_password: string
        http_port: string
        http_secure: true
        http_username: string
        ip_address:
        - string
        meraki_org_id:
        - string
        netconf_port: string
        password: string
        serial_number: string
        snmp_auth_passphrase: string
        snmp_auth_protocol: string
        snmp_mode: string
        snmp_priv_passphrase: string
        snmp_priv_protocol: string
        snmp_ro_community: string
        snmp_rw_community: string
        snmp_retry: 3
        snmp_timeout: 5
        snmp_username: string
        snmp_version: string
        type: string
        update_mgmt_ipaddresslist:
        - exist_mgmt_ipaddress: string
          new_mgmt_ipaddress: string
        username: string
        device_resync: false

- name: Add new Compute device in Inventory with full credentials.Inputs needed for Compute Device
  cisco.dnac.inventory_intent:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    dnac_log: False
    state: merged
    config:
      - ip_address: string
        http_username: string
        http_password: string
        http_port: string
        snmp_auth_passphrase: string
        snmp_auth_protocol: string
        snmp_mode: string
        snmp_priv_passphrase: string
        snmp_priv_protocol: string
        snmp_retry:  3
        snmp_timeout: 5
        snmp_username: string
        username: string
        device_resync: false
        type: "COMPUTE_DEVICE"

- name: Add new Meraki device in Inventory with full credentials.Inputs needed for Meraki Device.
  cisco.dnac.inventory_intent:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    dnac_log: False
    state: merged
    config:
      - http_password: string
        device_resync: false
        type: "MERAKI_DASHBOARD"

- name: Add new Firepower Management device in Inventory with full credentials.Input needed to add Device.
  cisco.dnac.inventory_intent:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    dnac_log: False
    state: merged
    config:
      - ip_address: string
        http_username: string
        http_password: string
        http_port: string
        device_resync: false
        type: "FIREPOWER_MANAGEMENT_SYSTEM"

- name: Add new Third Party device in Inventory with full credentials.Input needed to add Device.
  cisco.dnac.inventory_intent:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    dnac_log: False
    state: merged
    config:
      - ip_address: string
        snmp_auth_passphrase: string
        snmp_auth_protocol: string
        snmp_mode: string
        snmp_priv_passphrase: string
        snmp_priv_protocol: string
        snmp_retry:  3
        snmp_timeout: 5
        snmp_username: string
        device_resync: false
        type: "THIRD_PARTY_DEVICE"

- name: Associate Wired Devices to site and Provisioned it in Inventory
  cisco.dnac.inventory_intent:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    dnac_log: False
    state: merged
    config:
      - ip_address: string
        provision_wired_device:
          site_name: "{{item.site_name}}"

- name: Update Device Role with IP Address
  cisco.dnac.inventory_intent:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    dnac_log: False
    state: merged
    config:
      - ip_address: string
        device_updated: true
        update_device_role:
          role: string
          role_source: string

- name: Update Interface details with IP Address
  cisco.dnac.inventory_intent:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    dnac_log: False
    state: merged
    config:
      - ip_address: string
        device_updated: true
        update_interface_details:
          description: str
          admin_status: str
          vlan_id: int
          voice_vlan_id: int

- name: Export Device Details in a CSV file Interface details with IP Address
  cisco.dnac.inventory_intent:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    dnac_log: False
    state: merged
    config:
      - ip_address: string
        export_device_list:
          password: str
          operation_enum: str
          parameters: str

- name: Create Global User Defined with IP Address
  cisco.dnac.inventory_intent:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    dnac_log: False
    state: merged
    config:
      - ip_address: string
        add_user_defined_field:
          name: string
          description: string
          value: string

- name: Resync Device with IP Addresses
  cisco.dnac.inventory_intent:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    dnac_log: False
    state: merged
    config:
      - ip_address: string
        device_resync: True
        force_sync: False

- name: Reboot AP Devices with IP Addresses
  cisco.dnac.inventory_intent:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    dnac_log: False
    state: merged
    config:
      - ip_address: string
        reboot_device: True

- name: Delete Device by id
  cisco.dnac.inventory_intent:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    dnac_log: False
    state: deleted
    config:
      - ip_address: string
        clean_config: false
        id: string

- name: Delete Global User Defined Field with name
  cisco.dnac.inventory_intent:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    dnac_log: False
    state: deleted
    config:
    - ip_address: string
      add_user_defined_field:
        name: string

"""

RETURN = r"""

dnac_response:
  description: A dictionary or list with the response returned by the Cisco DNA Center Python SDK
  returned: always
  type: dict
  sample: >
    {
      "response": {
        "taskId": "string",
        "url": "string"
      },
      "version": "string"
    }
"""

import csv
from datetime import datetime
from io import StringIO
from ansible.module_utils.basic import AnsibleModule
from ansible_collections.cisco.dnac.plugins.module_utils.dnac import (
    DnacBase,
    validate_list_of_dicts,
    log,
)


class DnacDevice(DnacBase):
    """Class containing member attributes for Inventory intent module"""

    def __init__(self, module):
        super().__init__(module)
        self.supported_states = ["merged", "deleted"]

    def validate_input(self):
        """
        Validate the fields provided in the playbook.
        Checks the configuration provided in the playbook against a predefined specification
        to ensure it adheres to the expected structure and data types.
        Paramters:
            self: The instance of the class containing the 'config' attribute to be validated.
        Returns:
            The method returns an instance of the class with updated attributes:
                - self.msg: A message describing the validation result.
                - self.status: The status of the validation (either 'success' or 'failed').
                - self.validated_config: If successful, a validated version of the 'config' parameter.
        Example:
            To use this method, create an instance of the class and call 'validate_input' on it.
            If the validation succeeds, 'self.status' will be 'success' and 'self.validated_config'
            will contain the validated configuration. If it fails, 'self.status' will be 'failed', and
            'self.msg' will describe the validation issues.
        """

        temp_spec = {'cli_transport': {'default': "telnet", 'type': 'str'},
                     'compute_device': {'type': 'bool'},
                     'enable_password': {'type': 'str'},
                     'extended_discovery_info': {'type': 'str'},
                     'http_password': {'type': 'str'},
                     'http_port': {'type': 'str'},
                     'http_secure': {'type': 'bool'},
                     'http_username': {'type': 'str'},
                     'ip_address': {'type': 'list', 'elements': 'str'},
                     'meraki_org_id': {'type': 'list', 'elements': 'str'},
                     'netconf_port': {'type': 'str'},
                     'password': {'type': 'str'},
                     'serial_number': {'type': 'str'},
                     'snmp_auth_passphrase': {'type': 'str'},
                     'snmp_auth_protocol': {'default': "SHA", 'type': 'str'},
                     'snmp_mode': {'default': "AUTHPRIV", 'type': 'str'},
                     'snmp_priv_passphrase': {'type': 'str'},
                     'snmp_priv_protocol': {'default': "AES128", 'type': 'str'},
                     'snmp_ro_community': {'default': "public", 'type': 'str'},
                     'snmp_rw_community': {'default': "private", 'type': 'str'},
                     'snmp_retry': {'default': 3, 'type': 'int'},
                     'snmp_timeout': {'default': 5, 'type': 'int'},
                     'snmp_username': {'type': 'str'},
                     'snmp_version': {'default': "v3", 'type': 'str'},
                     'update_mgmt_ipaddresslist': {'type': 'list', 'elements': 'dict'},
                     'username': {'type': 'str'},
                     'update_device_role': {'type': 'dict'},
                     'device_resync': {'type': 'bool'},
                     'force_sync': {'type': 'bool'},
                     'clean_config': {'type': 'bool'},
                     'add_user_defined_field': {'type': 'dict'},
                     'upate_interface_details': {'type': 'dict'},
                     'deployment_mode': {'default': 'Deploy', 'type': 'str'},
                     'provision_wired_device': {'type': 'dict'}
                     }

        # Validate device params
        valid_temp, invalid_params = validate_list_of_dicts(
            self.config, temp_spec
        )

        if invalid_params:
            self.msg = "Invalid parameters in playbook: {0}".format(
                "\n".join(invalid_params)
            )
            self.status = "failed"
            return self

        self.validated_config = valid_temp
        log(str(valid_temp))
        self.msg = "Successfully validated input"
        self.status = "success"

        return self

    def device_exists_in_dnac(self):
        """
        Check which devices already exists in Cisco DNA Center and return both device_exist and device_not_exist in dnac.
        Paramters:
            self (object): An instance of a class used for interacting with Cisco Cisco DNA Center.
        Returns:
            list: A list of devices that exist in Cisco DNA Center.
        Description:
            Queries Cisco DNA Center to check which devices are already present in Cisco DNA Center and store
            its management IP address in the list of devices that exist.
        Example:
            To use this method, create an instance of the class and call 'device_exists_in_dnac' on it,
            The method returns a list of management IP addressesfor devices that exist in Cisco DNA Center.
        """

        device_in_dnac = []

        try:
            response = self.dnac._exec(
                family="devices",
                function='get_device_list',
            )

        except Exception as e:
            error_message = "Error while fetching device from Cisco DNA Center - {0}".format(str(e))
            self.log(error_message)
            raise Exception(error_message)

        if response:
            self.log(str(response))
            response = response.get("response")
            for ip in response:
                device_ip = ip["managementIpAddress"]
                device_in_dnac.append(device_ip)

        return device_in_dnac

    def is_udf_exist(self, field_name):
        """
        Check if a Global User Defined Field exists in Cisco DNA Center based on its name.
        Paramters:
            self (object): An instance of a class used for interacting with Cisco DNA Center.
            field_name (str): The name of the Global User Defined Field.
        Returns:
            bool: True if the Global User Defined Field exists, False otherwise.
        Description:
            The function sends a request to Cisco DNA Center to retrieve all Global User Defined Fields
            with the specified name. If matching field is found, the function returns True, indicating that
            the field exists else returns False.
        """

        response = self.dnac._exec(
            family="devices",
            function='get_all_user_defined_fields',
            params={"name": field_name},
        )
        self.log(str(response))
        udf = response.get("response")

        if (len(udf) == 1):
            return True

        message = "Global User Defined Field with name - {0} doesnot exist in Cisco DNA Center".format(field_name)
        self.log(message)

        return False

    def create_user_defined_field(self):
        """
        Create a Global User Defined Field in Cisco DNA Center based on the provided configuration.
        Paramters:
            self (object): An instance of a class used for interacting with Cisco DNA Center.
        Returns:
            self (object): An instance of a class used for interacting with Cisco DNA Center.
        Description:
            The function retrieves the configuration for adding a user-defined field from the configuration object,
            sends the request to Cisco DNA Center to create the field, and logs the response.
        """
        try:
            payload = self.config[0].get('add_user_defined_field')
            response = self.dnac._exec(
                family="devices",
                function='create_user_defined_field',
                params=payload,
            )
            self.log(str(response))
            response = response.get("response")
            field_name = self.config[0].get('add_user_defined_field').get('name')
            self.log("Global User Defined Field with name - {0} created successfully").format(field_name)
            self.status = "success"

        except Exception as e:
            error_message = "Error while Creating Global User Defined Field in Cisco DNA Center - {0}".format(str(e))
            log(error_message)

        return self

    def add_field_to_devices(self, device_ids):
        """
        Add a Global user-defined field with specified details to a list of devices in Cisco DNA Center.
        Paramters:
            self (object): An instance of a class used for interacting with Cisco DNA Center.
            device_ids (list): A list of device IDs to which the user-defined field will be added.
        Returns:
            self (object): An instance of a class used for interacting with Cisco DNA Center.
        Description:
            The function retrieves the details of the user-defined field from the configuration object,
            including the field name and default value then iterates over list of device IDs, creating a payload for
            each device and sending the request to Cisco DNA Center to add the user-defined field.
        """
        field_details = self.config[0].get('add_user_defined_field')
        field_name = field_details.get('name')
        field_value = field_details.get('value', '1')
        for device_id in device_ids:
            payload = {}
            payload['name'] = field_name
            payload['value'] = field_value
            udf_param_dict = {
                'payload': [payload],
                'device_id': device_id
            }
            try:
                response = self.dnac._exec(
                    family="devices",
                    function='add_user_defined_field_to_device',
                    params=udf_param_dict,
                )
                self.log(str(response))
                response = response.get("response")
                self.status = "success"
                self.result['changed'] = True

            except Exception as e:
                error_message = "Error while Adding Global UDF to device in Cisco DNA Center - {0}".format(str(e))
                log(error_message)
                self.status = "failed"
                self.result['changed'] = False

        return self

    def provisioned_wired_device(self):
        """
        Provision wired devices in Cisco DNA Center.
        Paramters:
            self (object): An instance of a class used for interacting with Cisco DNA Center.
        Returns:
            self (object): An instance of the class with updated result, status, and log.
        Description:
            This function provisions wired devices in Cisco DNA Center based on the configuration provided.
            It retrieves the site name and IP addresses of the devices from the configuration,
            attempts to provision each device, and monitors the provisioning process.
        """

        site_name = self.config[0].get('provision_wired_device').get("site_name")
        device_ips = self.config[0].get("ip_address")
        provision_count = 0

        for device_ip in device_ips:
            try:
                provision_wired_params = {
                    'deviceManagementIpAddress': device_ip,
                    'siteNameHierarchy': site_name,
                }
                response = self.dnac._exec(
                    family="sda",
                    function='provision_wired_device',
                    op_modifies=True,
                    params=provision_wired_params,
                )

                if response.get("status") == "failed":
                    description = response.get("description")
                    error_msg = "Cannot do Provisioning for device {0} beacuse of {1}".format(device_ip, description)
                    self.log(error_msg)
                    continue
                task_id = response.get("taskId")

                while True:
                    execution_details = self.get_task_details(task_id)
                    self.log(execution_details.get("progress"))

                    if 'TASK_PROVISION' in execution_details.get("progress"):
                        self.result['changed'] = True
                        self.result['response'] = execution_details
                        provision_count += 1
                        break
                    elif execution_details.get("isError") and execution_details.get("failureReason"):
                        self.msg = "Device Provisioning get failed because of {0}".format(execution_details.get("failureReason"))
                        self.status = "failed"
                        break

            except Exception as e:
                error_message = "Error while Provisioning the device {0} in Cisco DNA Center - {1}".format(device_ip, str(e))
                self.log(error_message)

        if provision_count == len(device_ips):
            self.status = "success"
            msg = "Wired Device get provisioned Successfully !!"
        elif provision_count == 0:
            self.status = "failed"
            msg = "Wired Device Provisioning get failed"
        else:
            self.status = "success"
            msg = "Wired Device get provisioned Successfully Partially for {0} devices!!".format(provision_count)
        self.log(msg)

        return self

    def get_udf_id(self, field_name):
        """
        Get the ID of a Global User Defined Field in Cisco DNA Center based on its name.
        Paramters:
            self (object): An instance of a class used for interacting with Cisco Cisco DNA Center.
            field_name (str): The name of the Global User Defined Field.
        Returns:
            str: The ID of the Global User Defined Field.
        Description:
            The function sends a request to Cisco DNA Center to retrieve all Global User Defined Fields
            with the specified name and extracts the ID of the first matching field.If successful, it returns
            the ID else returns None.
        """
        try:
            response = self.dnac._exec(
                family="devices",
                function='get_all_user_defined_fields',
                params={"name": field_name},
            )
            self.log(str(response))
            udf = response.get("response")
            udf_id = udf[0].get("id")

        except Exception as e:
            error_message = "Cannot get the Id of Global UDF - from Cisco DNA Center - {0}".format(str(e))
            log(error_message)

        return udf_id

    def mandatory_parameter(self):
        """
        Check for and validate mandatory parameters for adding network devices in Cisco DNA Center.
        Paramters:
            self (object): An instance of a class used for interacting with Cisco Cisco DNA Center.
        Returns:
            dict: The input `config` dictionary if all mandatory parameters are present.
        Description:
            It will check the mandatory parameters for adding the devices in Cisco DNA Center.
        """

        device_type = self.config[0].get("type", "NETWORK_DEVICE")
        params_dict = {
            "NETWORK_DEVICE": ["enable_password", "ip_address", "password", "snmp_username", "snmp_auth_passphrase", "snmp_priv_passphrase", "username"],
            "COMPUTE_DEVICE": ["ip_address", "http_username", "http_password", "http_port", "snmp_username", "snmp_auth_passphrase", "snmp_priv_passphrase"],
            "MERAKI_DASHBOARD": ["http_password"],
            "FIREPOWER_MANAGEMENT_SYSTEM": ["ip_address", "http_username", "http_password"],
            "THIRD_PARTY_DEVICE": ["ip_address", "snmp_username", "snmp_auth_passphrase", "snmp_priv_passphrase"]
        }

        params_list = params_dict.get(device_type, [])

        mandatory_params_absent = []
        for param in params_list:
            if param not in self.config[0]:
                mandatory_params_absent.append(param)

        if mandatory_params_absent:
            self.msg = "Mandatory paramters {0} not present".format(mandatory_params_absent)
            self.result['msg'] = "Required parameters {0} for adding devices are not present".format(mandatory_params_absent)
            self.status = "failed"
        else:
            self.msg = "Required parameter for Adding the devices in Inventory are present."
            self.status = "success"

        return self

    def get_have(self, config):
        """
        Retrieve and check device information with Cisco DNA Center to determine if devices already exist.
        Paramters:
            self (object): An instance of a class used for interacting with Cisco Cisco DNA Center.
            config (dict): A dictionary containing the configuration details of devices to be checked.
        Returns:
            dict: A dictionary containing information about the devices in the playbook, devices that exist in
            Cisco DNA Center, and devices that are not present in Cisco DNA Center.
        Description:
            This function checks the specified devices in the playbook against the devices existing in Cisco DNA Center with following keys:
            - "want_device": A list of devices specified in the playbook.
            - "device_in_dnac": A list of devices that already exist in Cisco DNA Center.
            - "device_not_in_dnac": A list of devices that are not present in Cisco DNA Center.
        """

        have = {}
        want_device = config.get("ip_address")

        # Get the list of device that are present in Cisco DNA Center
        device_in_dnac = self.device_exists_in_dnac()
        device_not_in_dnac = []

        for ip in want_device:
            if ip not in device_in_dnac:
                device_not_in_dnac.append(ip)

        log("Device Exists in Cisco DNA Center : " + str(device_in_dnac))
        have["want_device"] = want_device
        have["device_in_dnac"] = device_in_dnac
        have["device_not_in_dnac"] = device_not_in_dnac

        self.have = have

        return self

    def get_device_params(self, params):
        """
        Extract and store device parameters from the playbook for device processing in Cisco DNA Center.
        Paramters:
            self (object): An instance of a class used for interacting with Cisco DNA Center.
            params (dict): A dictionary containing device parameters retrieved from the playbook.
        Returns:
            dict: A dictionary containing the extracted device parameters.
        Description:
            This function will extract and store parameters in dictionary for adding, updating, editing, or deleting devices Cisco DNA Center.
        """

        device_param = {
            "cliTransport": params.get("cli_transport"),
            "enablePassword": params.get("enable_password"),
            "password": params.get("password"),
            "ipAddress": params.get("ip_address"),
            "snmpAuthPassphrase": params.get("snmp_auth_passphrase"),
            "snmpAuthProtocol": params.get("snmp_auth_protocol"),
            "snmpMode": params.get("snmp_mode"),
            "snmpPrivPassphrase": params.get("snmp_priv_passphrase"),
            "snmpPrivProtocol": params.get("snmp_priv_protocol"),
            "snmpROCommunity": params.get("snmp_ro_community"),
            "snmpRWCommunity": params.get("snmp_rw_community"),
            "snmpRetry": params.get("snmp_retry"),
            "snmpTimeout": params.get("snmp_timeout"),
            "snmpUserName": params.get("snmp_username"),
            "userName": params.get("username"),
            "computeDevice": params.get("compute_device"),
            "extendedDiscoveryInfo": params.get("extended_discovery_info"),
            "httpPassword": params.get("http_password"),
            "httpPort": params.get("http_port"),
            "httpSecure": params.get("http_secure"),
            "httpUserName": params.get("http_username"),
            "merakiOrgId": params.get("meraki_org_id"),
            "netconfPort": params.get("netconf_port"),
            "serialNumber": params.get("serial_number"),
            "snmpVersion": params.get("snmp_version"),
            "type": params.get("type"),
            "updateMgmtIPaddressList": params.get("update_mgmt_ipaddresslist"),
            "forceSync": params.get("force_sync"),
            "cleanConfig": params.get("clean_config")
        }

        if device_param.get("updateMgmtIPaddressList"):
            temp_dict = device_param.get("updateMgmtIPaddressList")[0]
            device_param["updateMgmtIPaddressList"][0] = {}

            device_param["updateMgmtIPaddressList"][0].update(
                {
                    "existMgmtIpAddress": temp_dict.get("exist_mgmt_ipaddress"),
                    "newMgmtIpAddress": temp_dict.get("new_mgmt_ipaddress")
                })

        return device_param

    def get_device_ids(self, device_ips):
        """
        Get the list of unique device IDs for list of specified management IP addresses of devices in Cisco DNA Center.
        Paramters:
            self (object): An instance of a class used for interacting with Cisco DNA Center.
            device_ips (list): The management IP addresses of devices for which you want to retrieve the device IDs.
        Returns:
            list: The list of unique device IDs for the specified devices.
        Description:
            Queries Cisco DNA Center to retrieve the unique device ID associated with a device having the specified
            IP address. If the device is not found in Cisco DNA Center, it raises an exception.
        """

        device_ids = []
        for device_ip in device_ips:
            try:
                response = self.dnac._exec(
                    family="devices",
                    function='get_device_list',
                    params={"managementIpAddress": device_ip}
                )

                if response:
                    self.log(str(response))
                    response = response.get("response")
                    if len(response) == 0:
                        continue
                    device_id = response[0]["id"]
                    device_ids.append(device_id)

            except Exception as e:
                error_message = "Error while fetching device from Cisco DNA Center - {0}".format(str(e))
                log(error_message)
                raise Exception(error_message)

        return device_ids

    def get_interface_from_ip(self, device_ip):
        """
        Get the interface ID for a device in Cisco DNA Center based on its IP address.
        Paramters:
            self (object): An instance of a class used for interacting with Cisco DNA Center.
            device_ip (str): The IP address of the device.
        Returns:
            str: The interface ID for the specified device.
        Description:
          The function sends a request to Cisco DNA Center to retrieve the interface information
          for the device with the provided IP address and extracts the interface ID from the
          response, and returns the interface ID.
        """

        try:
            response = self.dnac._exec(
                family="devices",
                function='get_interface_by_ip',
                params={"ip_address": device_ip}
            )
            self.log(str(response))
            response = response.get("response")

            if len(response) > 0:
                interface_id = response[0]["id"]
                self.log("Fetch Interface Id for device {0} successfully !!".format(device_ip))
                return interface_id

        except Exception as e:
            error_message = "Error while fetching Interface Id from Cisco DNA Center - {0}".format(str(e))
            log(error_message)
            raise Exception(error_message)

    def get_want(self, config):
        """
        Get all the device related information from playbook that is needed to be
        add/update/delete/resync device in Cisco DNA Center.
        Paramters:
            self (object): An instance of a class used for interacting with Cisco DNA Center.
            config (dict): A dictionary containing device-related information from the playbook.
        Returns:
            dict: A dictionary containing the extracted device parameters and other relevant information.
        Description:
            Retrieve all the device-related information from the playbook needed for adding, updating, deleting,
            or resyncing devices in Cisco DNA Center.
        """

        want = {}
        device_params = self.get_device_params(config)
        want["device_params"] = device_params

        self.want = want
        self.msg = "Successfully collected all parameters from the playbook "
        self.status = "success"

        return self

    def get_diff_merged(self, config):
        """
        Merge and process differences between existing devices and desired device configuration in Cisco DNA Center.
        Paramters:
            self (object): An instance of a class used for interacting with Cisco DNA Center.
            config (dict): A dictionary containing the desired device configuration and relevant information from the playbook.
        Returns:
            object: An instance of the class with updated results and status based on the processing of differences.
        Description:
            The function processes the differences and, depending on the changes required, it may add, update,
            or resynchronize devices in Cisco DNA Center.
            The updated results and status are stored in the class instance for further use.
        """

        devices_to_add = self.have["device_not_in_dnac"]
        device_type = self.config[0].get("type", "NETWORK_DEVICE")
        device_resynced = self.config[0].get("device_resync", False)
        device_updated = self.config[0].get("device_updated", False)
        device_reboot = self.config[0].get("reboot_device", False)
        self.result['log'] = []

        if device_reboot:
            device_ips = self.config[0].get("ip_address")
            ap_mac_address_list = []
            # get and store the apEthernetMacAddress of given devices
            for device_ip in device_ips:
                response = self.dnac._exec(
                    family="devices",
                    function='get_device_list',
                    params={"managementIpAddress": device_ip}
                )
                response = response.get('response')[0]
                if response['apEthernetMacAddress'] is not None:
                    ap_mac_address_list.append(response['apEthernetMacAddress'])

            if len(ap_mac_address_list) == 0:
                self.status = "failed"
                self.result['changed'] = False
                msg = "Cannot find the AP devices for Rebooting"
                self.log(msg)
                self.msg = msg
                return self

            # Now call the Reboot Access Point API
            reboot_params = {
                "apMacAddresses": ap_mac_address_list
            }
            response = self.dnac._exec(
                family="wireless",
                function='reboot_access_points',
                op_modifies=True,
                params=reboot_params,
            )
            self.log(str(response))

            if response and isinstance(response, dict):
                task_id = response.get('response').get('taskId')
                while True:
                    execution_details = self.get_task_details(task_id)
                    if 'url' in execution_details.get("progress"):
                        self.status = "success"
                        self.result['changed'] = True
                        self.result['response'] = execution_details
                        break
                    elif execution_details.get("isError") and execution_details.get("failureReason"):
                        self.msg = "AP Device Reboot get failed because of {0}".format(execution_details.get("failureReason"))
                        self.status = "failed"
                        break
                self.log("AP Devices Rebooted Successfully and Rebooted devices are :" + str(device_ips))
                msg = "Device " + str(device_ips) + " Rebooted Successfully !!"
                self.result['log'].append(msg)

            return self

        if self.config[0].get('export_device_list'):

            device_ips = self.config[0].get("ip_address")
            device_uuids = []
            try:
                for device_ip in device_ips:
                    response = self.dnac._exec(
                        family="devices",
                        function='get_device_list',
                        params={"managementIpAddress": device_ip}
                    )
                    response = response.get('response')
                    if len(response) > 0:
                        device_uuids.append(response[0]["id"])

                # Now all device UUID get collected so call the export device list API

                export_device_details = self.config[0].get('export_device_list')
                payload_params = {
                    "deviceUuids": device_uuids,
                    "password": export_device_details.get("password"),
                    "operationEnum": export_device_details.get("operation_enum", "1"),
                    "paramters": export_device_details.get("paramters")
                }
                response = self.dnac._exec(
                    family="devices",
                    function='export_device_list',
                    op_modifies=True,
                    params=payload_params,
                )
                self.log(str(response))
                response = response.get("response")
                task_id = response.get("taskId")
                # With this task ID call the Get Task Details API
                task_resp = self.dnac._exec(
                    family="task",
                    function='get_task_by_id',
                    op_modifies=True,
                    params={"task_id": task_id},
                )

                while True:
                    execution_details = self.get_task_details(task_id)

                    if execution_details.get("additionalStatusURL"):
                        file_id = execution_details.get("additionalStatusURL").split("/")[-1]
                        break
                    elif execution_details.get("isError") and execution_details.get("failureReason"):
                        failed_reason = execution_details.get("failureReason")
                        msg = "Could not get the File ID because of {0} so can't export device details in csv file".format(failed_reason)
                        self.msg = msg
                        self.log(msg)
                        self.status = "failed"
                        return self

                # With this File ID call the Download File by FileID API
                response = self.dnac._exec(
                    family="file",
                    function='download_a_file_by_fileid',
                    op_modifies=True,
                    params={"file_id": file_id},
                )

                device_data = []
                encoded_resp = response.data.decode(encoding='utf-8')
                self.log(str(encoded_resp))

                # Parse the CSV-like string into a list of dictionaries
                csv_reader = csv.DictReader(StringIO(encoded_resp))
                for row in csv_reader:
                    device_data.append(row)

                current_date = datetime.now()
                formatted_date = current_date.strftime("%m-%d-%Y")
                file_name = "devices-" + str(formatted_date) + ".csv"

                # Write the data to a CSV file
                with open(file_name, 'w', newline='') as csv_file:
                    fieldnames = device_data[0].keys()
                    csv_writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
                    csv_writer.writeheader()
                    csv_writer.writerows(device_data)

                msg = "Device Details Exported Successfully to the CSV file - {0}".format(file_name)
                self.log(msg)
                self.status = "success"
                self.result['changed'] = True
                self.result['log'].append(msg)

            except Exception as e:
                msg = "Cannot Export the Device Details into CSV file for {0}".format(str(device_ips))
                self.log(msg)
                self.status = "failed"
                self.msg = msg

            return self

        if self.config[0].get('add_user_defined_field'):
            field_name = self.config[0].get('add_user_defined_field').get('name')

            if field_name is None:
                self.msg = "Mandatory paramter for User Define Field - name is missing"
                self.status = "failed"
                return self

            # Check if the Global User defined field exist if not then create it with given field name
            udf_exist = self.is_udf_exist(field_name)
            if not udf_exist:
                # Create the Global UDF
                self.create_user_defined_field().check_return_status()

            # Get device Id with its IP Address
            device_ips = self.config[0].get("ip_address")
            device_ids = self.get_device_ids(device_ips)

            if len(device_ids) == 0:
                self.msg = "Can't Assign Global User Defined Field to device as device's are not present in Cisco DNA Center"
                self.status = "failed"
                self.result['changed'] = False
                return self

            # Now add code for adding Global UDF to device with Id
            self.add_field_to_devices(device_ids).check_return_status()

            self.result['changed'] = True
            log_msg = "Global User Defined Added with name {0} added to device Successfully !".format(field_name)
            log(log_msg)
            self.result['log'].append(log_msg)

            return self

        if device_resynced:
            # Code for triggers the resync operation using the retrieved device IDs and force sync parameter.
            device_ips = config.get("ip_address")
            device_ids = self.get_device_ids(device_ips)

            if len(device_ids) == 0:
                self.msg = "Cannot perform the Resync operation as device's are not present in Cisco DNA Center"
                self.status = "failed"
                self.result['changed'] = False
                return self

            try:
                force_sync = self.config[0].get("force_sync", "False")
                resync_param_dict = {
                    'payload': device_ids,
                    'force_sync': force_sync
                }
                response = self.dnac._exec(
                    family="devices",
                    function='sync_devices_using_forcesync',
                    op_modifies=True,
                    params=resync_param_dict,
                )
                self.log(str(response))

                if response and isinstance(response, dict):
                    task_id = response.get('response').get('taskId')

                    while True:
                        execution_details = self.get_task_details(task_id)

                        if 'Synced' in execution_details.get("progress"):
                            self.status = "success"
                            self.result['changed'] = True
                            self.result['response'] = execution_details
                            break
                        elif execution_details.get("isError") and execution_details.get("failureReason"):
                            self.msg = "Device Resynced get failed because of {0}".format(execution_details.get("failureReason"))
                            self.status = "failed"
                            break
                    self.log("Device Resynced Successfully and Resynced devices are :" + str(device_ips))
                    msg = "Device " + str(device_ips) + " Resynced Successfully !!"
                    self.result['log'].append(msg)

                    return self

            except Exception as e:
                error_message = "Error while Resyncing device in Cisco DNA Center - {0}".format(str(e))
                self.log(error_message)
                raise Exception(error_message)

        config['type'] = device_type
        if device_type == "FIREPOWER_MANAGEMENT_SYSTEM":
            config['http_port'] = self.config[0].get("http_port", "443")

        if device_updated:
            device_to_update = self.config[0].get("ip_address")
            # First check if device present in Cisco DNA Center or not
            device_present = False
            for device in device_to_update:
                if device in self.have.get("device_in_dnac"):
                    device_present = True
                    break

            if not device_present:
                msg = "Cannot perform Update operation as device - {0} not present in Cisco DNA Center".format(str(device_to_update))
                self.status = "success"
                self.result['changed'] = False
                self.result['response'] = msg
                self.log(msg)
                return self

            if self.config[0].get('update_device_role'):
                for device_ip in device_to_update:
                    device_id = self.get_device_ids([device_ip])
                    device_role_args = self.config[0].get('update_device_role')

                    if 'role' not in device_role_args or 'role_source' not in device_role_args:
                        self.msg = "Mandatory paramter(role/sourceRole) to update Device Role are missing"
                        self.status = "failed"
                        return self

                    # Check if the same role of device is present in dnac then no need to change the state
                    response = self.dnac._exec(
                        family="devices",
                        function='get_device_list',
                        params={"managementIpAddress": device_ip}
                    )
                    response = response.get('response')[0]

                    if response.get('role') == device_role_args.get('role'):
                        self.status = "success"
                        self.result['changed'] = False
                        log_msg = "Device Role - {0} same in Cisco DNA Center as well, no updation needed".format(device_role_args.get('role'))
                        self.result['log'] = log_msg
                        continue

                    device_role_params = {
                        'role': device_role_args.get('role'),
                        'roleSource': device_role_args.get('role_source'),
                        'id': device_id[0]
                    }

                    try:
                        response = self.dnac._exec(
                            family="devices",
                            function='update_device_role',
                            op_modifies=True,
                            params=device_role_params,
                        )
                        self.log(str(response))

                        if response and isinstance(response, dict):
                            task_id = response.get('response').get('taskId')

                            while True:
                                execution_details = self.get_task_details(task_id)

                                if 'successfully' in execution_details.get("progress"):
                                    self.status = "success"
                                    self.result['changed'] = True
                                    self.result['response'] = execution_details
                                    log("Device Role Updated Successfully")
                                    msg = "Device " + str(device_to_update) + " Role updated Successfully !!"
                                    self.result['log'].append(msg)
                                    break
                                elif execution_details.get("isError") and execution_details.get("failureReason"):
                                    self.msg = "Device Role Updation get failed because of {0}".format(execution_details.get("failureReason"))
                                    self.status = "failed"
                                    break

                    except Exception as e:
                        error_message = "Error while Updating device role in Cisco DNA Center - {0}".format(str(e))
                        self.log(error_message)
                        raise Exception(error_message)

                return self

            if self.config[0].get('update_interface_details'):
                # Call the Get interface details by device IP API and fetch the interface Id
                for device_ip in device_to_update:
                    interface_id = self.get_interface_from_ip(device_ip)
                    # Now we call update interface details api with required parameter
                    try:
                        interface_params = self.config[0].get('update_interface_details')
                        temp_params = {
                            'description': interface_params.get('description', ''),
                            'adminStatus': interface_params.get('admin_status'),
                            'voiceVlanId': interface_params.get('voice_vlan_id'),
                            'vlanId': interface_params.get('vlan_id')
                        }
                        payload_params = {}
                        for key, value in temp_params.items():
                            if value is not None:
                                payload_params[key] = value

                        update_interface_params = {
                            'payload': payload_params,
                            'interface_uuid': interface_id,
                            'deployment_mode': interface_params.get('deployment_mode', 'Deploy')
                        }
                        response = self.dnac._exec(
                            family="devices",
                            function='update_interface_details',
                            op_modifies=True,
                            params=update_interface_params,
                        )
                        self.log(str(response))

                        if response and isinstance(response, dict):
                            task_id = response.get('response').get('taskId')

                            while True:
                                execution_details = self.get_task_details(task_id)

                                if 'SUCCESS' in execution_details.get("progress"):
                                    self.status = "success"
                                    self.result['changed'] = True
                                    self.result['response'] = execution_details
                                    log_msg = "Update Interface Details for device {0} Added Successfully".format(device_ip)
                                    log(log_msg)
                                    self.result['log'].append(log_msg)
                                    break
                                elif execution_details.get("isError") and execution_details.get("failureReason"):
                                    self.msg = "Interface Updation get failed because of {0}".format(execution_details.get("failureReason"))
                                    self.status = "failed"
                                    break

                    except Exception as e:
                        error_message = "Error while Updating Interface Details in Cisco DNA Center - {0}".format(str(e))
                        self.status = "success"
                        self.result['changed'] = False
                        log_msg = "Port actions are only supported on user facing/access ports as it's not allowed or No Updation required"
                        self.result['log'] = log_msg

                return self

            # Update Device details and credentails
            try:
                self.mandatory_parameter().check_return_status()
                response = self.dnac._exec(
                    family="devices",
                    function='sync_devices',
                    op_modifies=True,
                    params=self.want.get("device_params"),
                )

                self.log(str(response))

                if response and isinstance(response, dict):
                    task_id = response.get('response').get('taskId')

                    while True:
                        execution_details = self.get_task_details(task_id)

                        if execution_details.get("endTime"):
                            self.status = "success"
                            self.result['changed'] = True
                            self.result['response'] = execution_details
                            break
                        elif execution_details.get("isError") and execution_details.get("failureReason"):
                            self.msg = "Device Updation get failed because of {0}".format(execution_details.get("failureReason"))
                            self.status = "failed"
                            break

                    log("Device Updated Successfully")
                    log("Updated devices are :" + str(device_to_update))
                    msg = "Device " + str(device_to_update) + " updated Successfully !!"
                    self.result['log'].append(msg)

            except Exception as e:
                error_message = "Error while Updating device in Cisco DNA Center - {0}".format(str(e))
                self.log(error_message)
                raise Exception(error_message)

            msg = "Devices {0} present in Cisco DNA Center and updated successfully".format(config['ip_address'])
            self.log(msg)
            self.result['log'].append(msg)
            self.status = "success"

            return self

        # If we want to add device in inventory
        config['ip_address'] = devices_to_add
        self.mandatory_parameter().check_return_status()
        try:
            response = self.dnac._exec(
                family="devices",
                function='add_device',
                op_modifies=True,
                params=self.want.get("device_params"),
            )
            self.log(str(response))

            if response and isinstance(response, dict):
                task_id = response.get('response').get('taskId')

                while True:
                    execution_details = self.get_task_details(task_id)

                    if '/task/' in execution_details.get("progress"):
                        self.status = "success"
                        self.result['response'] = execution_details

                        if len(devices_to_add) > 0:
                            self.result['changed'] = True
                            log("Device Added Successfully")
                            log("Added devices are :" + str(devices_to_add))
                            msg = "Device " + str(devices_to_add) + " added Successfully !!"
                            self.result['log'].append(msg)
                            break
                        msg = "Devices " + str(self.config[0].get("ip_address")) + " already present in Cisco DNA Center"
                        self.result['log'].append(msg)
                        break
                    elif execution_details.get("isError") and execution_details.get("failureReason"):
                        self.msg = "Device Addition get failed because of {0}".format(execution_details.get("failureReason"))
                        self.status = "failed"
                        break

        except Exception as e:
            error_message = "Error while Adding device in Cisco DNA Center - {0}".format(str(e))
            self.log(error_message)
            raise Exception(error_message)

        # Once device get added we will assign device to site and Provisioned it
        if self.config[0].get('provision_wired_device'):
            self.provisioned_wired_device()

        return self

    def get_diff_deleted(self, config):
        """
        Delete devices in Cisco DNA Center based on device IP Address.
        Paramters:
            self (object): An instance of a class used for interacting with Cisco DNA Center
            config (dict): A dictionary containing the list of device IP addresses to be deleted.
        Returns:
            object: An instance of the class with updated results and status based on the deletion operation.
        Description:
            This function is responsible for removing devices from the Cisco DNA Center inventory and
            also unprovsioned and removed wired provsion devices from the Inventory page and also delete
            the Global User Defined Field that are associated to the devices.
        """

        device_to_delete = config.get("ip_address")
        provision_device = self.config[0].get('delete_provision_device', 'False')
        self.result['msg'] = []

        if self.config[0].get('add_user_defined_field'):
            field_name = self.config[0].get('add_user_defined_field').get('name')
            udf_id = self.get_udf_id(field_name)

            if udf_id is None:
                msg = "Global UDF - {0} is not present in Cisco DNA Center".format(field_name)
                self.msg = msg
                self.status = "success"
                self.result['changed'] = False
                self.result['msg'].append(msg)
                return self

            try:
                response = self.dnac._exec(
                    family="devices",
                    function='delete_user_defined_field',
                    params={"id": udf_id},
                )
                if response and isinstance(response, dict):
                    task_id = response.get('response').get('taskId')

                    while True:
                        execution_details = self.get_task_details(task_id)

                        if 'success' in execution_details.get("progress"):
                            self.msg = "Global UDF - {0} Deleted Successfully from Cisco DNA Center".format(field_name)
                            self.status = "success"
                            self.result['changed'] = True
                            self.result['response'] = execution_details
                            break
                        elif execution_details.get("isError") and execution_details.get("failureReason"):
                            self.msg = "Global UDF Deletion get failed because of {0}".format(execution_details.get("failureReason"))
                            self.status = "failed"
                            break
            except Exception as e:
                error_message = "Error while Deleting Global UDF from Cisco DNA Center - {0}".format(str(e))
                self.log(error_message)
                raise Exception(error_message)

            return self

        for device_ip in device_to_delete:
            if device_ip not in self.have.get("device_in_dnac"):
                self.result['changed'] = False
                msg = "The device {0} is not present in Cisco DNA Center so can't perform delete operation".format(device_ip)
                self.msg = msg
                self.status = "success"
                self.result['changed'] = False
                self.result['msg'].append(msg)
                continue

            try:
                provision_params = {
                    "device_management_ip_address": device_ip
                }
                prov_respone = self.dnac._exec(
                    family="sda",
                    function='get_provisioned_wired_device',
                    params=provision_params,
                )

                if prov_respone.get("status") == "success":
                    response = self.dnac._exec(
                        family="sda",
                        function='delete_provisioned_wired_device',
                        params=provision_params,
                    )
                    if response.get("status") == "success":
                        msg = "Wired device {0} unprovisioned successfully.".format(device_ip)
                        self.log(msg)
                        self.result['changed'] = True
                        self.status = "success"
                    else:
                        msg = response.get("description")
                        self.log(msg)
                        self.status = "failed"

            except Exception as e:
                device_id = self.get_device_ids([device_ip])
                delete_params = {
                    "id": device_id[0],
                    "clean_config": self.config[0].get("clean_config", False)
                }
                response = self.dnac._exec(
                    family="devices",
                    function='delete_device_by_id',
                    params=delete_params,
                )

                if response and isinstance(response, dict):
                    task_id = response.get('response').get('taskId')

                    while True:
                        execution_details = self.get_task_details(task_id)

                        if 'success' in execution_details.get("progress"):
                            self.msg = "Device Deleted Successfully from Cisco DNA Center"
                            self.status = "success"
                            self.result['changed'] = True
                            self.result['response'] = execution_details
                            break
                        elif execution_details.get("isError") and execution_details.get("failureReason"):
                            self.msg = "Device Deletion get failed because of {0}".format(execution_details.get("failureReason"))
                            self.status = "failed"
                            break

        return self


def main():
    """ main entry point for module execution
    """

    element_spec = {'dnac_host': {'type': 'str', 'required': True, },
                    'dnac_port': {'type': 'str', 'default': '443'},
                    'dnac_username': {'type': 'str', 'default': 'admin', 'aliases': ['user']},
                    'dnac_password': {'type': 'str', 'no_log': True},
                    'dnac_verify': {'type': 'bool', 'default': 'True'},
                    'dnac_version': {'type': 'str', 'default': '2.2.3.3'},
                    'dnac_debug': {'type': 'bool', 'default': False},
                    'dnac_log': {'type': 'bool', 'default': False},
                    'validate_response_schema': {'type': 'bool', 'default': True},
                    'config': {'required': True, 'type': 'list', 'elements': 'dict'},
                    'state': {'default': 'merged', 'choices': ['merged', 'deleted']}
                    }

    module = AnsibleModule(argument_spec=element_spec,
                           supports_check_mode=False)

    dnac_device = DnacDevice(module)
    state = dnac_device.params.get("state")

    if state not in dnac_device.supported_states:
        dnac_device.status = "invalid"
        dnac_device.msg = "State {0} is invalid".format(state)
        dnac_device.check_return_status()

    dnac_device.validate_input().check_return_status()

    for config in dnac_device.validated_config:
        dnac_device.reset_values()
        dnac_device.get_want(config).check_return_status()
        dnac_device.get_have(config).check_return_status()
        dnac_device.get_diff_state_apply[state](config).check_return_status()

    module.exit_json(**dnac_device.result)


if __name__ == '__main__':
    main()
