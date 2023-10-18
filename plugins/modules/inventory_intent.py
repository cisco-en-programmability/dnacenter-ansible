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
version_added: '3.1.0'
extends_documentation_fragment:
  - cisco.dnac.intent_params
author: Abhishek Maheshwari (@abmahesh)
options:
  state:
    description: The state of DNAC after module completion.
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
        description: Network Device's cliTransport.
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
        description: Network Device's httpPassword.
        type: str
      httpPort:
        description: Network Device's httpPort.
        type: str
      httpSecure:
        description: HttpSecure flag.
        type: bool
      httpUserName:
        description: Network Device's httpUserName.
        type: str
      id:
        description: Id path parameter. Device ID.
        type: str
      ipAddress:
        description: Network Device's ipAddress.
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
        description: Network Device's password.
        type: str
      serialNumber:
        description: Network Device's serialNumber.
        type: str
      snmpAuthPassphrase:
        description: Network Device's snmpAuthPassphrase.
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
        description: Network Device's snmpPrivPassphrase.
        type: str
      snmpPrivProtocol:
        description: Network Device's snmpPrivProtocol.
        type: str
        default: "AES128"
      snmpROCommunity:
        description: Network Device's snmpROCommunity.
        type: str
        default: public
      snmpRWCommunity:
        description: Network Device's snmpRWCommunity.
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
        description: Network Device's snmpUserName.
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
        description: Network Device's userName.
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
  description: A dictionary or list with the response returned by the Cisco DNAC Python SDK
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
    """Class containing member attributes for site intent module"""

    def __init__(self, module):
        super().__init__(module)
        self.supported_states = ["merged", "deleted"]

    def validate_input(self):
        """Validate the fields provided in the playbook"""

        if not self.config:
            self.msg = "config not available in playbook for validation"
            self.status = "failed"
            return self

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
                     'resync': {'type': 'bool'}
                     }

        # Validate site params
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
        self.log(str(valid_temp))
        self.msg = "Successfully validated input"
        self.status = "success"
        return self

    def device_exists_in_dnac(self, want_device):
        """Check which devices already exists in DNAC and return both device_exist and device_not_exist in dnac """

        device_in_dnac = []
        response = None

        try:
            response = self.dnac._exec(
                family="devices",
                function='get_device_list',
            )

        except Exception as e:
            self.log("There is error while fetching device from DNAC")

        if response:
            self.log(str(response))
            response = response.get("response")
            for ip in response:
                device_ip = ip["managementIpAddress"]
                device_in_dnac.append(device_ip)

        return device_in_dnac

    def get_device_id(self, device_ip):
        try:
            response = self.dnac._exec(
                family="devices",
                function='get_device_list',
                params={"managementIpAddress": device_ip},
            )

        except Exception as e:
            self.log("There is error while fetching device from DNAC")
        response = response.get("response")[0]
        device_id = response.get("id")

        return device_id

    def get_execution_details(self, task_id):

        response = None
        response = self.dnac._exec(
            family="task",
            function='get_task_by_id',
            params={"task_id": task_id}
        )

        self.log(str(response))

        if response and isinstance(response, dict):
            return response.get('response')

    def mandatory_parameter(self, config):

        try:
            device_type = config.type
        except Exception as e:
            device_type = "NETWORK_DEVICE"

        mandatory_params_absent = []
        if device_type == "NETWORK_DEVICE":
            params_list = ["enablePassword", "ipAddress", "password", "snmpAuthPassphrase", "snmpPrivPassphrase", "snmpUserName", "userName"]

            for param in params_list:
                if param not in config:
                    mandatory_params_absent.append(param)

            if mandatory_params_absent:
                self.msg = "Mandatory paramters {0} not present".format(mandatory_params_absent)
                self.result['msg'] = "Required parameters {0} for adding devices are not present".format(mandatory_params_absent)
                self.status = "failed"
                self.module.fail_json(msg=self.msg, response=self.result)

        return config

    def get_have(self, config):
        """Get the device details from DNAC"""

        have = {}
        want_device = config.get("ipAddress")

        # Get the list of device that are present in DNAC
        device_in_dnac = self.device_exists_in_dnac(want_device)
        device_not_in_dnac = []

        for ip in want_device:
            if ip not in device_in_dnac:
                device_not_in_dnac.append(ip)

        self.log("Device Exists in DNAC : " + str(device_in_dnac))
        have["want_device"] = want_device
        have["device_in_dnac"] = device_in_dnac
        have["device_not_in_dnac"] = device_not_in_dnac

        self.have = have

        return self

    def get_device_params(self, params):
        """Store device parameters from the playbook for device Add/Update/Edit/Delete processing in DNAC"""

        device_param = {
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
            "update_management_ip_list": params.get("updateMgmtIPaddressList")
        }

        return device_param

    def get_want(self, config):
        """Get all the device related information from playbook
        that is needed to be add/update/delete/resync device in DNAC"""

        want = {}
        device_params = self.get_device_params(config)
        want["device_params"] = device_params

        self.want = want
        self.msg = "Successfully collected all parameters from playbook " + \
                   "for comparison"
        self.status = "success"
        return self

    def get_diff_merged(self, config):
        """Update/Create site info in DNAC with fields provided in DNAC"""

        device_added = False
        device_updated = False
        device_resynced = False

        devices_to_add = self.have["device_not_in_dnac"]
        self.result['msg'] = []

        if not devices_to_add:
            # Write code for device updation
            device_updated = True

            self.log("Devices {0} are present in DNAC and updated successfully".format(config['ipAddress']))
            msg = "Devices {0} present in DNAC and updated successfully".format(config['ipAddress'])
            self.result['msg'].append(msg)
            self.status = "success"
            return self

        else:
            # If we want to add device in inventory
            config = self.mandatory_parameter(config)
            config['ipAddress'] = devices_to_add
            del config['resync']

            try:
                response = self.dnac._exec(
                    family="devices",
                    function='add_device',
                    op_modifies=True,
                    params=config,
                )

                self.log(str(response))
                device_added = True

            except Exception as e:
                self.log("There is error while adding devices in DNAC")

        if device_added or device_updated:
            if response and isinstance(response, dict):
                task_id = response.get('response').get('taskId')
                while True:
                    execution_details = self.get_execution_details(task_id)

                    if '/task/' in execution_details.get("progress"):
                        self.result['changed'] = True
                        self.result['response'] = execution_details
                        break

                    elif execution_details.get("isError") and execution_details.get("failureReason"):
                        self.module.fail_json(msg=execution_details.get("failureReason"),
                                              response=execution_details)
                        break

                self.log("Device Added Successfully")
                self.log("Added devices are :" + str(devices_to_add))
                msg = "Device " + str(devices_to_add) + " added Successfully !!"
                self.result['msg'].append(msg)

        return self

    def get_diff_deleted(self, config):
        """Call DNAC API to delete devices with provided inputs"""

        device_to_delete = config.get("ipAddress")
        self.result['msg'] = []

        for device_ip in device_to_delete:
            if device_ip in self.have.get("device_in_dnac"):
                device_id = self.get_device_id(device_ip)
                try:
                    response = self.dnac._exec(
                        family="devices",
                        function='delete_device_by_id',
                        params={"id": device_id},
                    )

                except Exception as e:
                    self.log("There is error while deleting the device from DNAC")

                if response and isinstance(response, dict):
                    if response and isinstance(response, dict):
                        task_id = response.get('response').get('taskId')
                    while True:
                        execution_details = self.get_execution_details(task_id)

                        if 'success' in execution_details.get("progress"):
                            self.result['changed'] = True
                            self.result['response'] = execution_details
                            break

                        elif execution_details.get("isError") and execution_details.get("failureReason"):
                            self.module.fail_json(msg=execution_details.get("failureReason"),
                                                  response=execution_details)
                            break

            else:
                self.result['changed'] = False
                msg = "The device {0} is not present in DNAC so can't perform delete operation".format(device_ip)
                self.result['msg'].append(msg)

        return self


def main():
    """ main entry point for module execution
    """

    element_spec = {'dnac_host': {'required': True, 'type': 'str'},
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
