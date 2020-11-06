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
module: discovery_job
short_description: Manage DiscoveryJob objects of Discovery
description:
- Returns the list of discovery jobs for the given Discovery ID. The results can be optionally filtered based on IP. Discovery ID can be obtained using the "Get Discoveries by range" API.
- Returns the list of discovery jobs for the given IP.
version_added: '1.0'
author: first last (@GitHubID)
options:
    id:
        description:
        - Discovery ID.
        type: str
        required: True
    ip_address:
        description:
        - IpAddress query parameter.
        type: str
    limit:
        description:
        - Limit query parameter.
        type: int
    offset:
        description:
        - Offset query parameter.
        type: int
    name:
        description:
        - Name query parameter.
        type: str

requirements:
- dnacentersdk
seealso:
# Reference by module name
- module: cisco.dnac.plugins.module_utils.definitions.discovery_job
# Reference by Internet resource
- name: DiscoveryJob reference
  description: Complete reference of the DiscoveryJob object model.
  link: https://developer.cisco.com/docs/dna-center/api/1-3-3-x
# Reference by Internet resource
- name: DiscoveryJob reference
  description: SDK reference.
  link: https://dnacentersdk.readthedocs.io/en/latest/api/api.html#v2-1-1-summary
'''

EXAMPLES = r'''
'''

RETURN = r'''
data_0:
    description: Returns the list of discovery jobs for the given Discovery ID. The results can be optionally filtered based on IP. Discovery ID can be obtained using the "Get Discoveries by range" API.
    returned: success,changed,always
    type: dict
    contains:
        response:
            description: Response, property of the response body (list of objects).
            returned: success,changed,always
            type: list
            contains:
                attributeInfo:
                    description: It is the discovery job's attributeInfo.
                    returned: success,changed,always
                    type: dict
                cliStatus:
                    description: It is the discovery job's cliStatus.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                discoveryStatus:
                    description: It is the discovery job's discoveryStatus.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                endTime:
                    description: It is the discovery job's endTime.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                httpStatus:
                    description: It is the discovery job's httpStatus.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                id:
                    description: It is the discovery job's id.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                inventoryCollectionStatus:
                    description: It is the discovery job's inventoryCollectionStatus.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                inventoryReachabilityStatus:
                    description: It is the discovery job's inventoryReachabilityStatus.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                ipAddress:
                    description: It is the discovery job's ipAddress.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                jobStatus:
                    description: It is the discovery job's jobStatus.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                name:
                    description: It is the discovery job's name.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                netconfStatus:
                    description: It is the discovery job's netconfStatus.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                pingStatus:
                    description: It is the discovery job's pingStatus.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                snmpStatus:
                    description: It is the discovery job's snmpStatus.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                startTime:
                    description: It is the discovery job's startTime.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                taskId:
                    description: It is the discovery job's taskId.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'

        version:
            description: Version, property of the response body.
            returned: success,changed,always
            type: str
            sample: 'sample_string'

data_1:
    description: Returns the list of discovery jobs for the given IP.
    returned: success,changed,always
    type: dict
    contains:
        response:
            description: Response, property of the response body (list of objects).
            returned: success,changed,always
            type: list
            contains:
                attributeInfo:
                    description: It is the discovery job's attributeInfo.
                    returned: success,changed,always
                    type: dict
                cliStatus:
                    description: It is the discovery job's cliStatus.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                discoveryStatus:
                    description: It is the discovery job's discoveryStatus.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                endTime:
                    description: It is the discovery job's endTime.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                httpStatus:
                    description: It is the discovery job's httpStatus.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                id:
                    description: It is the discovery job's id.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                inventoryCollectionStatus:
                    description: It is the discovery job's inventoryCollectionStatus.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                inventoryReachabilityStatus:
                    description: It is the discovery job's inventoryReachabilityStatus.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                ipAddress:
                    description: It is the discovery job's ipAddress.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                jobStatus:
                    description: It is the discovery job's jobStatus.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                name:
                    description: It is the discovery job's name.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                netconfStatus:
                    description: It is the discovery job's netconfStatus.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                pingStatus:
                    description: It is the discovery job's pingStatus.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                snmpStatus:
                    description: It is the discovery job's snmpStatus.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                startTime:
                    description: It is the discovery job's startTime.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                taskId:
                    description: It is the discovery job's taskId.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'

        version:
            description: Version, property of the response body.
            returned: success,changed,always
            type: str
            sample: 'sample_string'

'''

from ansible.module_utils.basic import AnsibleModule
from ansible_collections.cisco.dnac.plugins.module_utils.dnac import ModuleDefinition, DNACModule, dnac_argument_spec
from ansible_collections.cisco.dnac.plugins.module_utils.definitions.discovery_job import module_definition


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

    dnac.exit_json()


if __name__ == "__main__":
    main()