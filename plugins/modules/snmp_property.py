#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright: (c) 2020, first last <email>
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

ANSIBLE_METADATA = {
    'metadata_version': '0.0.1',
    'status': ['preview'],
    'supported_by': 'community'
}

DOCUMENTATION = r'''
---
module: snmp_property
short_description: Manage SnmpProperty objects of Discovery
description:
- Returns SNMP properties.
- Adds SNMP properties.
version_added: '1.0'
author: first last (@GitHubID)
options:
    payload:
        description:
        - An object to send in the Request body.
        type: list
        required: True
        elements: dict
        suboptions:
            id:
                description:
                - It is the snmp property's id.
                type: str
            instanceTenantId:
                description:
                - It is the snmp property's instanceTenantId.
                type: str
            instanceUuid:
                description:
                - It is the snmp property's instanceUuid.
                type: str
            intValue:
                description:
                - It is the snmp property's intValue.
                type: int
            systemPropertyName:
                description:
                - It is the snmp property's systemPropertyName.
                type: str


requirements:
- dnacentersdk
seealso:
# Reference by module name
- module: cisco.dnac.plugins.module_utils.definitions.snmp_property
# Reference by Internet resource
- name: SnmpProperty reference
  description: Complete reference of the SnmpProperty object model.
  link: https://developer.cisco.com/docs/dna-center/api/1-3-3-x
# Reference by Internet resource
- name: SnmpProperty reference
  description: SDK reference.
  link: https://dnacentersdk.readthedocs.io/en/latest/api/api.html#v2-1-1-summary
'''

EXAMPLES = r'''
'''

RETURN = r'''
data_0:
    description: Returns SNMP properties.
    returned: success,changed,always
    type: dict
    contains:
        response:
            description: Response, property of the response body (list of objects).
            returned: success,changed,always
            type: list
            contains:
                id:
                    description: It is the snmp property's id.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                instanceTenantId:
                    description: It is the snmp property's instanceTenantId.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                instanceUuid:
                    description: It is the snmp property's instanceUuid.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                intValue:
                    description: It is the snmp property's intValue.
                    returned: success,changed,always
                    type: int
                    sample: 0
                systemPropertyName:
                    description: It is the snmp property's systemPropertyName.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'

        version:
            description: Version, property of the response body.
            returned: success,changed,always
            type: str
            sample: 'sample_string'

data_1:
    description: Adds SNMP properties.
    returned: success,changed,always
    type: dict
    contains:
        response:
            description: SystemPropertyNameAndIntValueDTO's response.
            returned: success,changed,always
            type: dict
            contains:
                taskId:
                    description: It is the snmp property's taskId.
                    returned: success,changed,always
                    type: dict
                url:
                    description: It is the snmp property's url.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'

        version:
            description: SystemPropertyNameAndIntValueDTO's version.
            returned: success,changed,always
            type: str
            sample: 'sample_string'

'''

from ansible.module_utils.basic import AnsibleModule
from ansible_collections.cisco.dnac.plugins.module_utils.dnac import ModuleDefinition, DNACModule, dnac_argument_spec
from ansible_collections.cisco.dnac.plugins.module_utils.definitions.snmp_property import module_definition


def main():

    moddef = ModuleDefinition(module_definition)

    argument_spec = dnac_argument_spec()
    argument_spec.update(moddef.get_argument_spec_dict())

    required_if = moddef.get_required_if_list()
    
    module = AnsibleModule(
        argument_spec=argument_spec,
        supports_check_mode=False,
        required_if=required_if
    )

    dnac = DNACModule(module, moddef)

    state = module.params.get("state")

    if state == "query":
        dnac.exec("get")

    elif state == "create":
        dnac.disable_validation()
        dnac.exec("post")

    dnac.exit_json()


if __name__ == "__main__":
    main()