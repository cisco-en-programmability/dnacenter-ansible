#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2022, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)
from __future__ import absolute_import, division, print_function

__metaclass__ = type
__author__ = ("Abinash Mishra, Phan Nguyen")

DOCUMENTATION = r"""
---
module: discovery_intent
short_description: Resource module for discovery related functions
description:
- Manage operations discover devices using IP address/range, CDP, LLDP and delete discoveries
- API to discover a device or multiple devices
- API to delete a discovery of a device or multiple devices
version_added: '6.6.0'
extends_documentation_fragment:
  - cisco.dnac.intent_params
author: Abinash Mishra (@abimishr)
        Phan Nguyen (phannguy)
options:
  state:
    description: The state of DNAC after module completion.
    type: str
    choices: [ merged, deleted ]
    default: merged
  config:
    description:
    - List of details of device being managed.
    type: list
    elements: dict
    required: true
    suboptions:
      devices_list:
        description: List of devices with details necessary for discovering the devices.
        type: list
        elements: dict
        required: true
        suboptions:
          name:
            description: Hostname of the device
            type: str
          ip:
            description: Management IP address of the device
            type: str
            required: true
      discovery_type:
        description: Type of discovery (SINGLE/RANGE/MULTI RANGE/CDP/LLDP/CIDR)
        type: str
        required: true
      cdp_level:
        description: Total number of levels that are there in cdp's method of discovery
        type: int
        default: 16
      lldp_level:
        description: Total number of levels that are there in lldp's method of discovery
        type: int
        default: 16
      start_index:
        description: Start index for the header in fetching global v2 credentials
        type: int
      enable_password_list:
        description: List of enable passwords for the CLI crfedentials
        type: list
        elements: str
      records_to_return:
        description: Number of records to returnfor the header in fetching global v2 credentials
        type: int
      http_read_credential:
        description: HTTP read credentials for hosting a device
        type: dict
      http_write_credential:
        description: HTTP write credentials for hosting a device
        type: dict
      ip_filter_list:
        description: List of IP adddrsess that needs to get filtered out from the IP addresses added
        type: list
        elements: str
      discovery_name:
        description: Name of the discovery task
        type: dict
      netconf_port:
        description: Port for the netconf credentials
        type: str
      password_list:
        description: List of passwords for the CLI credentials
        type: list
        elements: str
      username_list:
        description: List of passwords for the CLI credentials
        type: list
        elements: str
      preferred_mgmt_ip_method:
        description: Preferred method for the management of the IP (None/UseLoopBack)
        type: str
        default: None
      protocol_order:
        description: Order of protocol (ssh/telnet) in which device connection will be tried. For example, 'telnet' - only telnet - 'ssh,
            telnet' - ssh with higher order than telnet
        type: str
      retry:
        description: Number of times to try establishing connection to device
        type: int
      snmp_auth_passphrase:
        description: Auth Pass phrase for SNMP
        type: str
      snmp_auth_protocol:
        description: SNMP auth protocol (SHA/MD5)
        type: str
      snmp_mode:
        description: Mode of SNMP (AUTHPRIV/AUTHNOPRIV/NOAUTHNOPRIV)
        type: str
      snmp_priv_passphrase:
        description: Pass phrase for SNMP privacy
        type: str
      snmp_priv_protocol:
        description: SNMP privacy protocol (DES/AES128)
        type: str
      snmp_ro_community:
        description: Snmp RO community of the devices to be discovered
        type: str
      snmp_ro_community_desc:
        description: Description for Snmp RO community
        type: str
      snmp_rw_community:
        description: Snmp RW community of the devices to be discovered
        type: str
      snmp_rw_community_desc:
        description: Description for Snmp RW community
        type: str
      snmp_username:
        description: SNMP username of the device
        type: str
      snmp_version:
        description: Version of SNMP (v2/v3)
        type: str
        required: true
      timeout:
        description: Time to wait for device response in seconds
        type: int
requirements:
- dnacentersdk == 2.6.10
- python >= 3.5
notes:
  - SDK Method used are
    discovery.Discovery.get_all_global_credentials_v2,
    discovery.Discovery.start_discovery,
    task.Task.get_task_by_id,
    discovery.Discovery.get_discoveries_by_range,
    discovery.Discovery.get_discovered_network_devices_by_discovery_id',
    discovery.Discovery.delete_discovery_by_id

  - Paths used are
    get /dna/intent/api/v2/global-credential
    post /dna/intent/api/v1/discovery
    get /dna/intent/api/v1/task/{taskId}
    get /dna/intent/api/v1/discovery/{startIndex}/{recordsToReturn}
    get /dna/intent/api/v1/discovery/{id}/network-device
    delete /dna/intent/api/v1/discovery/{id}

"""

EXAMPLES = r"""
- name: Execute discovery devices
  cisco.dnac.discovery_intent:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    dnac_log: True
    state: merged
    config:
        - device_list:
            - name: string
              ip: string
          discovery_type: string
          cdp_level: string
          lldp_level: string
          start_index: integer
          enable_pasword_list: list
          records_to_return: integer
          http_read_credential: string
          http_write_credential: string
          ip_filter_list: list
          discovery_name: string
          password_list: list
          preffered_mgmt_ip_method: string
          protocol_order: string
          retry: integer
          snmp_auth_passphrase: string
          snmp_auth_protocol: string
          snmp_mode: string
          snmp_priv_passphrse: string
          snmp_priv_protocol: string
          snmp_ro_community: string
          snmp_ro_community_desc: string
          snmp_rw_community: string
          snmp_rw_community_desc: string
          snmp_username: string
          snmp_version: string
          timeout: integer
          username_list: list
"""

RETURN = r"""
#Case_1: When the device(s) are discovered successfully.
response_1:
  description: A dictionary with the response returned by the Cisco DNAC Python SDK
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

#Case_2: Given device details or SNMP mode are not provided
response_2:
  description: A list with the response returned by the Cisco DNAC Python SDK
  returned: always
  type: list
  sample: >
    {
      "response": [],
      "msg": String
    }

#Case_3: Error while deleting a discovery
response_3:
  description: A string with the response returned by the Cisco DNAC Python SDK
  returned: always
  type: dict
  sample: >
    {
      "response": String,
      "msg": String
    }
"""
from ansible.module_utils.basic import AnsibleModule
from ansible_collections.cisco.dnac.plugins.module_utils.dnac import (
    DnacBase,
    validate_list_of_dicts
)
import time
import re


class DnacDiscovery(DnacBase):
    def __init__(self, module):
        super().__init__(module)
        self.creds_ids_list = []

    def validate_input(self):
        """
        Validate the fields provided in the playbook.  Checks the
        configuration provided in the playbook against a predefined
        specification to ensure it adheres to the expected structure
        and data types.

        Parameters:
          - self: The instance of the class containing the 'config' attribute
                  to be validated.
        Returns:
          The method returns an instance of the class with updated attributes:
          - self.msg: A message describing the validation result.
          - self.status: The status of the validation (either 'success' or 'failed').
          - self.validated_config: If successful, a validated version of the
                                   'config' parameter.
        Example:
          To use this method, create an instance of the class and call
          'validate_input' on it.If the validation succeeds, 'self.status'
          will be 'success'and 'self.validated_config' will contain the
          validated configuration. If it fails, 'self.status' will be
          'failed', and 'self.msg' will describe the validation issues.
        """

        if not self.config:
            self.msg = "config not available in playbook for validation"
            self.status = "success"
            return self

        discovery_spec = {
            'cdp_level': {'type': 'int', 'required': False,
                          'default': 16},
            'discovery_type': {'type': 'str', 'required': True},
            'enable_password_list': {'type': 'list', 'required': False,
                                     'elements': 'str'},
            'devices_list': {'type': 'list', 'required': True,
                             'elements': 'dict'},
            'start_index': {'type': 'int', 'required': False},
            'records_to_return': {'type': 'int', 'required': False},
            'http_read_credential': {'type': 'dict', 'required': False},
            'http_write_credential': {'type': 'dict', 'required': False},
            'ip_filter_list': {'type': 'list', 'required': False,
                               'elements': 'str'},
            'lldp_level': {'type': 'int', 'required': False,
                           'default': 16},
            'discovery_name': {'type': 'dict', 'required': False,
                               'default': 'discovery_{}'.format(time.time())},
            'netconf_port': {'type': 'str', 'required': False},
            'password_list': {'type': 'list', 'required': False,
                              'elements': 'str'},
            'preferred_mgmt_ip_method': {'type': 'str', 'required': False,
                                         'default': 'None'},
            'protocol_order': {'type': 'str', 'required': False},
            'retry': {'type': 'int', 'required': False},
            'snmp_auth_passphrase': {'type': 'str', 'required': False},
            'snmp_auth_protocol': {'type': 'str', 'required': False},
            'snmp_mode': {'type': 'str', 'required': False},
            'snmp_priv_passphrase': {'type': 'str', 'required': False},
            'snmp_priv_protocol': {'type': 'str', 'required': False},
            'snmp_ro_community': {'type': 'str', 'required': False},
            'snmp_ro_community_desc': {'type': 'str', 'required': False},
            'snmp_rw_community': {'type': 'str', 'required': False},
            'snmp_rw_community_desc': {'type': 'str', 'required': False},
            'snmp_username': {'type': 'str', 'required': False},
            'snmp_version': {'type': 'str', 'required': True},
            'timeout': {'type': 'str', 'required': False},
            'username_list': {'type': 'list', 'required': False,
                              'elements': 'str'}
        }

        # Validate discovery params
        valid_discovery, invalid_params = validate_list_of_dicts(
            self.config, discovery_spec
        )
        if invalid_params:
            self.msg = "Invalid parameters in playbook: {0}".format(
                "\n".join(invalid_params))
            self.status = "failed"
            return self

        self.validated_config = valid_discovery
        self.log(str(valid_discovery))

        self.msg = "Successfully validated input"
        self.status = "success"
        return self

    def get_creds_ids_list(self):
        return self.creds_ids_list

    def get_dnac_global_credentials_v2_info(self):
        response = self.dnac_apply['exec'](
            family="discovery",
            function='get_all_global_credentials_v2',
            params=self.validated_config[0].get('headers'),
        )
        response = response.get('response')
        for value in response.values():
            if not value:
                continue
            self.creds_ids_list.extend(element.get('id') for element in value)

        if not self.creds_ids_list:
            msg = 'Not found any credentials to discover'
            self.module.fail_json(msg=msg)

        self.result.update(dict(credential_ids=self.creds_ids_list))

    def get_devices_list_info(self):
        devices_list = self.validated_config[0].get('devices_list')
        self.result.update(dict(devices_info=devices_list))
        return devices_list

    def preprocessing_devices_info(self, devices_list=None):
        if devices_list is None:
            devices_list = []
        ip_address_list = [device['ip'] for device in devices_list]
        if self.validated_config[0].get('discovery_type') == "SINGLE":
            ip_address_list = ip_address_list[0]
        else:
            ip_address_list = list(
                map(
                    lambda x: '{0}-{value}'.format(x, value=x),
                    ip_address_list
                )
            )
            ip_address_list = ','.join(ip_address_list)
        return ip_address_list

    def create_params(self, credential_ids=None, ip_address_list=None):
        if credential_ids is None:
            credential_ids = []
        if ip_address_list is None:
            ip_address_list = ''
        new_object_params = {}
        new_object_params['cdpLevel'] = self.validated_config[0].get('cdp_level')
        new_object_params['discoveryType'] = self.validated_config[0].get('discovery_type')
        new_object_params['enablePasswordList'] = self.validated_config[0].get(
            'enable_password_list')
        new_object_params['globalCredentialIdList'] = credential_ids
        new_object_params['httpReadCredential'] = self.validated_config[0].get(
            'http_read_credential')
        new_object_params['httpWriteCredential'] = self.validated_config[0].get(
            'http_write_credential')
        new_object_params['ipAddressList'] = ip_address_list
        new_object_params['ipFilterList'] = self.validated_config[0].get('ip_filter_list')
        new_object_params['lldpLevel'] = self.validated_config[0].get('lldp_level')
        new_object_params['name'] = self.validated_config[0].get('discovery_name')
        new_object_params['netconfPort'] = self.validated_config[0].get('netconf_port')
        new_object_params['passwordList'] = self.validated_config[0].get('password_list')
        new_object_params['preferredMgmtIPMethod'] = self.validated_config[0].get(
            'preferred_mgmt_ip_method')
        new_object_params['protocolOrder'] = self.validated_config[0].get('protocol_order')
        new_object_params['retry'] = self.validated_config[0].get('retry')
        new_object_params['snmpAuthPassphrase'] = self.validated_config[0].get(
            'snmp_auth_Passphrase')
        new_object_params['snmpAuthProtocol'] = self.validated_config[0].get(
            'snmp_auth_protocol')
        new_object_params['snmpMode'] = self.validated_config[0].get('snmp_mode')
        new_object_params['snmpPrivPassphrase'] = self.validated_config[0].get(
            'snmp_priv_passphrase')
        new_object_params['snmpPrivProtocol'] = self.validated_config[0].get(
            'snmp_priv_protocol')
        new_object_params['snmpROCommunity'] = self.validated_config[0].get(
            'snmp_ro_community')
        new_object_params['snmpROCommunityDesc'] = self.validated_config[0].get(
            'snmp_ro_community_desc')
        new_object_params['snmpRWCommunity'] = self.validated_config[0].get(
            'snmp_rw_community')
        new_object_params['snmpRWCommunityDesc'] = self.validated_config[0].get(
            'snmp_rw_community_desc')
        new_object_params['snmpUserName'] = self.validated_config[0].get(
            'snmp_username')
        new_object_params['snmpVersion'] = self.validated_config[0].get('snmp_version')
        new_object_params['timeout'] = self.validated_config[0].get('timeout')
        new_object_params['userNameList'] = self.validated_config[0].get('user_name_list')
        return new_object_params

    def create_discovery(self, credential_ids=None, ip_address_list=None):
        if credential_ids is None:
            credential_ids = []
        if ip_address_list is None:
            ip_address_list = ''
        result = self.dnac_apply['exec'](
            family="discovery",
            function="start_discovery",
            params=self.create_params(
                credential_ids=credential_ids, ip_address_list=ip_address_list),
            op_modifies=True,
        )

        self.result.update(dict(discovery_result=result))
        return result.response.get('taskId')

    def get_task_status(self, task_id=None):
        if task_id is None:
            task_id = ''
        result = False
        params = dict(task_id=task_id)
        while True:
            response = self.dnac_apply['exec'](
                family="task",
                function='get_task_by_id',
                params=params,
            )
            response = response.response
            if response.get('isError') or re.search(
                'failed', response.get('progress'), flags=re.IGNORECASE
            ):
                msg = 'Discovery task with id {0} has not completed - Reason: {1}'.format(
                    task_id, response.get("failureReason"))
                self.module.fail_json(msg=msg)
                return False

            if response.get('progress') != 'In Progress':
                result = True
                break
            time.sleep(3)

        self.result.update(dict(discovery_task=response))
        return result

    def lookup_discovery_by_range_via_name(self):
        params = dict(
            start_index=self.validated_config[0].get("start_index"),
            records_to_return=self.validated_config[0].get("records_to_return"),
            headers=self.validated_config[0].get("headers"),
        )

        response = self.dnac_apply['exec'](
            family="discovery",
            function='get_discoveries_by_range',
            params=params
        )
        return next(
            filter(
                lambda x: x['name'] == self.validated_config[0].get('discovery_name'),
                response.response
            ), None
        )

    def get_discoveries_by_range_until_success(self):
        result = False
        discovery = self.lookup_discovery_by_range_via_name()
        if not discovery:
            msg = 'Cannot find any discovery task with name {0} -- Discovery result: {1}'.format(
                self.validated_config[0].get("discovery_name"), discovery)
            self.module.fail_json(msg=msg)

        while True:
            discovery = self.lookup_discovery_by_range_via_name()
            if discovery.get('discoveryCondition') == 'Complete':
                result = True
                break
            time.sleep(3)

        if not result:
            msg = 'Cannot find any discovery task with name {0} -- Discovery result: {1}'.format(
                self.validated_config[0].get("discovery_name"), discovery)
            self.module.fail_json(msg=msg)

        self.result.update(dict(discovery_range=discovery))
        return discovery

    def get_discovery_device_info(self, discovery_id=None, task_id=None):
        if discovery_id is None:
            discovery_id = ''
        if task_id is None:
            task_id = ''
        params = dict(
            id=discovery_id,
            task_id=task_id,
            headers=self.validated_config[0].get("headers"),
        )
        result = False
        response = []
        count = 0
        while True:
            response = self.dnac_apply['exec'](
                family="discovery",
                function='get_discovered_network_devices_by_discovery_id',
                params=params,
            )
            devices = response.response
            if all(res.get('reachabilityStatus') == 'Success' for res in devices):
                result = True
                break
            else:
                count += 1

            if count == 3:
                break

            time.sleep(3)

        if not result:
            msg = 'Discovery network device with id {0} has not completed'.format(discovery_id)
            self.module.fail_json(msg=msg)

        self.result.update(dict(discovery_device_info=devices))
        return result

    def get_exist_discovery(self):
        discovery = self.lookup_discovery_by_range_via_name()
        if not discovery:
            self.result.update(dict(exist_discovery=discovery))
            return None
        have = dict(exist_discovery=discovery)
        self.have = have
        self.result.update(dict(exist_discovery=discovery))
        return discovery

    def delete_exist_discovery(self, params):
        response = self.dnac_apply['exec'](
            family="discovery",
            function="delete_discovery_by_id",
            params=params,
        )
        self.result.update(dict(delete_discovery=response))
        return response.response.get('taskId')

    def get_diff_merged(self):
        self.get_dnac_global_credentials_v2_info()
        devices_list_info = self.get_devices_list_info()
        ip_address_list = self.preprocessing_devices_info(devices_list_info)
        exist_discovery = self.get_exist_discovery()
        if exist_discovery:
            params = dict(id=exist_discovery.get('id'))
            discovery_task_id = self.delete_exist_discovery(params=params)
            complete_discovery = self.get_task_status(task_id=discovery_task_id)
        discovery_task_id = self.create_discovery(
            credential_ids=self.get_creds_ids_list(), ip_address_list=ip_address_list)
        complete_discovery = self.get_task_status(task_id=discovery_task_id)
        discovery_task_info = self.get_discoveries_by_range_until_success()
        result = self.get_discovery_device_info(discovery_id=discovery_task_info.get('id'))
        self.result["changed"] = True
        self.result['msg'] = "Discovery Created Successfully"
        self.result['diff'] = self.validated_config
        self.result['response'] = discovery_task_id
        self.result.update(dict(msg='Discovery Created Successfully'))
        return self

    def get_diff_deleted(self):
        exist_discovery = self.get_exist_discovery()
        if exist_discovery:
            params = dict(id=exist_discovery.get('id'))
            discovery_task_id = self.delete_exist_discovery(params=params)
            complete_discovery = self.get_task_status(task_id=discovery_task_id)
            self.result["changed"] = True
            self.result['msg'] = "Discovery Deleted Successfully"
            self.result['diff'] = self.validated_config
            self.result['response'] = discovery_task_id
        else:
            self.result['msg'] = "Discovery {0} Not Found".format(
                self.validated_config[0].get("discovery_name"))
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

    dnac_discovery = DnacDiscovery(module)

    state = dnac_discovery.params.get("state")
    if state not in dnac_discovery.supported_states:
        dnac_discovery.status = "invalid"
        dnac_discovery.msg = "State {0} is invalid".format(state)
        dnac_discovery.check_return_status()

    dnac_discovery.validate_input().check_return_status()
    for config in dnac_discovery.validated_config:
        dnac_discovery.get_diff_state_apply[state]().check_return_status()

    module.exit_json(**dnac_discovery.result)


if __name__ == '__main__':
    main()
