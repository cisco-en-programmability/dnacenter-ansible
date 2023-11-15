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
      cliTransport:
        description: Network Device's cliTransport.Required for Adding Network Devices.
        type: str
      computeDevice:
        description: ComputeDevice flag.
        type: bool
      enablePassword:
        description: Network Device's enablePassword.
        type: str
      extendedDiscoveryInfo:
        description: Network Device's extendedDiscoveryInfo.
        type: str
      httpPassword:
        description: Network Device's httpPassword.Required for Adding Compute, Meraki, Firepower Management Devices.
        type: str
      httpPort:
        description: Network Device's httpPort.Required for Adding Compute, Firepower Management Devices.
        type: str
      httpSecure:
        description: HttpSecure flag.
        type: bool
      httpUserName:
        description: Network Device's httpUserName.Required for Adding Compute,Firepower Management Devices.
        type: str
      id:
        description: Id path parameter. Device ID.Required for Deleting Device.
        type: str
      ipAddress:
        description: Network Device's ipAddress.Required for Adding/Deleting/Resyncing Device except Meraki Devices.
        elements: str
        type: list
      merakiOrgId:
        description: Network Device's merakiOrgId.
        elements: str
        type: list
      netconfPort:
        description: Network Device's netconfPort.
        type: str
      password:
        description: Network Device's password.Required for Adding Network Device.
        type: str
      serialNumber:
        description: Network Device's serialNumber.
        type: str
      snmpAuthPassphrase:
        description: Network Device's snmpAuthPassphrase.Required for Adding Network, Compute, Third Party Devices.
        type: str
      snmpAuthProtocol:
        description: Network Device's snmpAuthProtocol.
        type: str
        default: "SHA"
      snmpMode:
        description: Network Device's snmpMode.
        type: str
        default: "AUTHPRIV"
      snmpPrivPassphrase:
        description: Network Device's snmpPrivPassphrase.Required for Adding Network, Compute, Third Party Devices.
        type: str
      snmpPrivProtocol:
        description: Network Device's snmpPrivProtocol.Required for Adding Network, Compute, Third Party Devices.
        type: str
        default: "AES128"
      snmpROCommunity:
        description: Network Device's snmpROCommunity.Required for Adding V2C Devices.
        type: str
        default: public
      snmpRWCommunity:
        description: Network Device's snmpRWCommunity.Required for Adding V2C Devices.
        type: str
        default: private
      snmpRetry:
        description: Network Device's snmpRetry.
        type: int
        default: 3
      snmpTimeout:
        description: Network Device's snmpTimeout.
        type: int
        default: 5
      snmpUserName:
        description: Network Device's snmpUserName.Required for Adding Network, Compute, Third Party Devices.
        type: str
      snmpVersion:
        description: Network Device's snmpVersion.
        type: str
        default: "v3"
      type:
        description: Network Device's type.
        type: str
        default: "NETWORK_DEVICE"
      updateMgmtIPaddressList:
        description: Network Device's updateMgmtIPaddressList.
        elements: dict
        suboptions:
          existMgmtIpAddress:
            description: Network Device's existMgmtIpAddress.
            type: str
          newMgmtIpAddress:
            description: Network Device's newMgmtIpAddress.
            type: str
        type: list
      userName:
        description: Network Device's userName.Required for Adding Network Device.
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
- name: Add new device in Inventory with full credentials
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
      - cliTransport: string
        computeDevice: true
        enablePassword: string
        extendedDiscoveryInfo: string
        httpPassword: string
        httpPort: string
        httpSecure: true
        httpUserName: string
        ipAddress:
        - string
        merakiOrgId:
        - string
        netconfPort: string
        password: string
        serialNumber: string
        snmpAuthPassphrase: string
        snmpAuthProtocol: string
        snmpMode: string
        snmpPrivPassphrase: string
        snmpPrivProtocol: string
        snmpROCommunity: string
        snmpRWCommunity: string
        snmpRetry: 3
        snmpTimeout: 5
        snmpUserName: string
        snmpVersion: string
        type: string
        updateMgmtIPaddressList:
        - existMgmtIpAddress: string
          newMgmtIpAddress: string
        userName: string
        deviceResync: false

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
      - ipAddress: string
        httpUserName: string
        httpPassword: string
        httpPort: string
        snmpAuthPassphrase: string
        snmpAuthProtocol: string
        snmpMode: string
        snmpPrivPassphrase: string
        snmpPrivProtocol: string
        snmpRetry:  3
        snmpTimeout: 5
        snmpUserName: string
        userName: string
        deviceResync: false
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
      - httpPassword: string
        deviceResync: false
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
      - ipAddress: string
        httpUserName: string
        httpPassword: string
        httpPort: string
        deviceResync: false
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
      - ipAddress: string
        snmpAuthPassphrase: string
        snmpAuthProtocol: string
        snmpMode: string
        snmpPrivPassphrase: string
        snmpPrivProtocol: string
        snmpRetry:  3
        snmpTimeout: 5
        snmpUserName: string
        deviceResync: false
        type: "THIRD_PARTY_DEVICE"

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
      - ipAddress: string
        deviceResync: True
        forceSync: False

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
      - cleanConfig: false
        id: string

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
        Args:
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

        temp_spec = {'cliTransport': {'default': "telnet", 'type': 'str'},
                     'computeDevice': {'type': 'bool'},
                     'enablePassword': {'type': 'str'},
                     'extendedDiscoveryInfo': {'type': 'str'},
                     'httpPassword': {'type': 'str'},
                     'httpPort': {'type': 'str'},
                     'httpSecure': {'type': 'bool'},
                     'httpUserName': {'type': 'str'},
                     'ipAddress': {'type': 'list', 'elements': 'str'},
                     'merakiOrgId': {'type': 'list', 'elements': 'str'},
                     'netconfPort': {'type': 'str'},
                     'password': {'type': 'str'},
                     'serialNumber': {'type': 'str'},
                     'snmpAuthPassphrase': {'type': 'str'},
                     'snmpAuthProtocol': {'default': "SHA", 'type': 'str'},
                     'snmpMode': {'default': "AUTHPRIV", 'type': 'str'},
                     'snmpPrivPassphrase': {'type': 'str'},
                     'snmpPrivProtocol': {'default': "AES128", 'type': 'str'},
                     'snmpROCommunity': {'default': "public", 'type': 'str'},
                     'snmpRWCommunity': {'default': "private", 'type': 'str'},
                     'snmpRetry': {'default': 3, 'type': 'int'},
                     'snmpTimeout': {'default': 5, 'type': 'int'},
                     'snmpUserName': {'type': 'str'},
                     'snmpVersion': {'default': "v3", 'type': 'str'},
                     'updateMgmtIPaddressList': {'type': 'list', 'elements': 'dict'},
                     'userName': {'type': 'str'},
                     'deviceResync': {'type': 'bool'},
                     'forceSync': {'type': 'bool'}
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

    def device_exists_in_dnac(self, want_device):
        """
        Check which devices already exists in Cisco DNA Center and return both device_exist and device_not_exist in dnac.
        Args:
            want_device (list): A list of devices you want to check for existence in Cisco DNA Center.
        Returns:
            list: A list of devices that exist in Cisco DNA Center.
        Description:
            Queries Cisco DNA Center to check which devices from 'want_device' are already present. If a device is found
            in Cisco DNA Center, its management IP address is included in the list of devices that exist.
        Example:
            To use this method, create an instance of the class and call 'device_exists_in_dnac' on it,
            passing a list of devices you want to check. The method returns a list of management IP addresses
            for devices that exist in Cisco DNA Center.
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
            log(str(response))
            response = response.get("response")
            for ip in response:
                device_ip = ip["managementIpAddress"]
                device_in_dnac.append(device_ip)

        return device_in_dnac

    def mandatory_parameter(self, config):
        """
        Check for and validate mandatory parameters for adding network devices in Cisco DNA Center.
        Args:
            config (dict): A dictionary containing the configuration details for adding a network device to Cisco DNA Center.
        Returns:
            dict: The input `config` dictionary if all mandatory parameters are present.
        Description:
            It will check the mandatory parameters for adding the devices in Cisco DNA Center.
        """

        device_type = self.config[0].get("type", "NETWORK_DEVICE")
        params_dict = {
            "NETWORK_DEVICE": ["enablePassword", "ipAddress", "password", "snmpUserName", "snmpAuthPassphrase", "snmpPrivPassphrase", "userName"],
            "COMPUTE_DEVICE": ["ipAddress", "httpUserName", "httpPassword", "httpPort", "snmpUserName", "snmpAuthPassphrase", "snmpPrivPassphrase"],
            "MERAKI_DASHBOARD": ["httpPassword"],
            "FIREPOWER_MANAGEMENT_SYSTEM": ["ipAddress", "httpUserName", "httpPassword"],
            "THIRD_PARTY_DEVICE": ["ipAddress", "snmpUserName", "snmpAuthPassphrase", "snmpPrivPassphrase"]
        }

        params_list = params_dict.get(device_type, [])
        mandatory_params_absent = []
        for param in params_list:
            if param not in config:
                mandatory_params_absent.append(param)

        if mandatory_params_absent:
            self.msg = "Mandatory paramters {0} not present".format(mandatory_params_absent)
            self.result['msg'] = "Required parameters {0} for adding devices are not present".format(mandatory_params_absent)
            self.status = "failed"
        else:
            self.result['msg'] = "Required paramter for Adding the devices in Inventory are present."
            self.msg = "Required paramter for Adding the devices in Inventory are present."
            self.status = "success"

        return self

    def get_have(self, config):
        """
        Retrieve and check device information with Cisco DNA Center to determine if devices already exist.
        Args:
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
        want_device = config.get("ipAddress")

        # Get the list of device that are present in Cisco DNA Center
        device_in_dnac = self.device_exists_in_dnac(want_device)
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
        Args:
            self (object): An instance of a class used for interacting with Cisco DNA Center.
            params (dict): A dictionary containing device parameters retrieved from the playbook.
        Returns:
            dict: A dictionary containing the extracted device parameters.
        Description:
            This function will extract and store parameters in dictionary for adding, updating, editing, or deleting devices Cisco DNA Center.
        """

        device_param = {
            "cli_transport": params.get("cliTransport"),
            "enable_password": params.get("enablePassword"),
            "password": params.get("password"),
            "ipaddress": params.get("ipAddress"),
            "snmp_auth_passphrase": params.get("snmpAuthPassphrase"),
            "snmp_protocol": params.get("snmpAuthProtocol"),
            "snmp_mode": params.get("snmpMode"),
            "snmp_priv_passphrase": params.get("snmpPrivPassphrase"),
            "snmp_priv_protocol": params.get("snmpPrivProtocol"),
            "snmp_read_community": params.get("snmpROCommunity"),
            "snmp_write_community": params.get("snmpRWCommunity"),
            "snmp_retry": params.get("snmpRetry"),
            "snmp_timeout": params.get("snmpTimeout"),
            "snmp_username": params.get("snmpUserName"),
            "username": params.get("userName"),
            "compute_device": params.get("computeDevice"),
            "extended_discovery_info": params.get("extendedDiscoveryInfo"),
            "http_password": params.get("httpPassword"),
            "http_port": params.get("httpPort"),
            "http_secure": params.get("httpSecure"),
            "http_username": params.get("httpUserName"),
            "meraki_org_id": params.get("merakiOrgId"),
            "netconf_port": params.get("netconfPort"),
            "serial_number": params.get("serialNumber"),
            "snmp_version": params.get("snmpVersion"),
            "type": params.get("type"),
            "update_management_ip_list": params.get("updateMgmtIPaddressList"),
            "force_sync": params.get("forceSync")
        }

        return device_param

    def get_device_ids(self, device_ips):
        """
        Get the list of unique device IDs for list of specified management IP addresses of devices in Cisco DNA Center.
        Args:
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
                    response = response.get("response")[0]
                    device_id = response["id"]
                    device_ids.append(device_id)

            except Exception as e:
                error_message = "Error while fetching device from Cisco DNA Center - {0}".format(str(e))
                self.log(error_message)
                raise Exception(error_message)

        return device_ids

    def get_want(self, config):
        """
        Get all the device related information from playbook that is needed to be
        add/update/delete/resync device in Cisco DNA Center.
        Args:
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
        Args:
            self (object): An instance of a class used for interacting with Cisco DNA Center.
            config (dict): A dictionary containing the desired device configuration and relevant information from the playbook.
        Returns:
            object: An instance of the class with updated results and status based on the processing of differences.
        Description:
            The function processes the differences and, depending on the changes required, it may add, update,
            or resynchronize devices in Cisco DNA Center.
            The updated results and status are stored in the class instance for further use.
        """

        device_added = False
        device_updated = False

        devices_to_add = self.have["device_not_in_dnac"]
        device_type = self.config[0].get("type", "NETWORK_DEVICE")
        device_resynced = self.config[0].get("deviceResync", "False")
        self.result['log'] = []

        if device_resynced:
            # Code for triggers the resync operation using the retrieved device IDs and force sync parameter.
            device_ips = config.get("ipAddress")
            device_ids = self.get_device_ids(device_ips)
            try:
                force_sync = self.config[0].get("forceSync", "False")
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
                    self.log("Device Resynced Successfully")
                    self.log("Resynced devices are :" + str(device_ips))
                    msg = "Device " + str(device_ips) + " Resynced Successfully !!"
                    self.result['log'].append(msg)

                    return self

            except Exception as e:
                error_message = "Error while Resyncing device in Cisco DNA Center - {0}".format(str(e))
                self.log(error_message)
                raise Exception(error_message)

        if not devices_to_add:
            # Write code for device updation
            device_updated = True

            log("Devices {0} are present in Cisco DNA Center and updated successfully".format(config['ipAddress']))
            msg = "Devices {0} present in Cisco DNA Center and updated successfully".format(config['ipAddress'])
            self.result['log'].append(msg)
            self.status = "success"
            return self

        # If we want to add device in inventory
        self.mandatory_parameter(config).check_return_status()
        config['ipAddress'] = devices_to_add
        config['type'] = device_type
        if device_type == "FIREPOWER_MANAGEMENT_SYSTEM":
            config['httpPort'] = self.config[0].get("httpPort", "443")

        try:
            response = self.dnac._exec(
                family="devices",
                function='add_device',
                op_modifies=True,
                params=config,
            )

            log(str(response))
            device_added = True

            if device_added or device_updated:
                if response and isinstance(response, dict):
                    task_id = response.get('response').get('taskId')
                    while True:
                        execution_details = self.get_task_details(task_id)

                        if '/task/' in execution_details.get("progress"):
                            self.status = "success"
                            self.result['changed'] = True
                            self.result['response'] = execution_details
                            break
                        elif execution_details.get("isError") and execution_details.get("failureReason"):
                            self.msg = "Device Addition/Updation get failed because of {0}".format(execution_details.get("failureReason"))
                            self.status = "failed"
                            break

                    log("Device Added Successfully")
                    log("Added devices are :" + str(devices_to_add))
                    msg = "Device " + str(devices_to_add) + " added Successfully !!"
                    self.result['log'].append(msg)

        except Exception as e:
            error_message = "Error while Adding device in Cisco DNA Center - {0}".format(str(e))
            self.log(error_message)
            raise Exception(error_message)

        return self

    def get_diff_deleted(self, config):
        """
        Delete devices in Cisco DNA Center based on device IP Address.
        Args:
            self (object): An instance of a class used for interacting with Cisco DNA Center
            config (dict): A dictionary containing the list of device IP addresses to be deleted.
        Returns:
            object: An instance of the class with updated results and status based on the deletion operation.
        Description:
            This function is responsible for removing devices from the Cisco DNA Center inventory and
            raise Exception if any error occured.
        """

        device_to_delete = config.get("ipAddress")
        self.result['msg'] = []

        for device_ip in device_to_delete:
            if device_ip not in self.have.get("device_in_dnac"):
                self.result['changed'] = False
                msg = "The device {0} is not present in Cisco DNA Center so can't perform delete operation".format(device_ip)
                self.msg = msg
                self.status = "success"
                self.result['msg'].append(msg)
                continue

            device_id = self.get_device_ids([device_ip])
            try:
                response = self.dnac._exec(
                    family="devices",
                    function='delete_device_by_id',
                    params={"id": device_id[0]},
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

            except Exception as e:
                error_message = "Error while Deleting device from Cisco DNA Center - {0}".format(str(e))
                self.log(error_message)
                raise Exception(error_message)

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
