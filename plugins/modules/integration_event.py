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
module: integration_event
short_description: Manage IntegrationEvent objects of Itsm
description:
- Used to retrieve the list of integration events that failed to create tickets in ITSM.
- Allows retry of multiple failed ITSM event instances. The retry request payload can be given as a list of strings: ["instance1","instance2","instance3",..] A minimum of one instance Id is mandatory. The list of failed event instance Ids can be retrieved using the 'Get Failed ITSM Events' API in the 'instanceId' attribute.
version_added: '1.0'
author: first last (@GitHubID)
options:
    instance_id:
        description:
        - Instance Id of the failed event as in the Runtime Dashboard.
        type: str
    payload:
        description:
        - An object to send in the Request body.
        type: list
        required: True

requirements:
- dnacentersdk
seealso:
# Reference by module name
- module: cisco.dnac.plugins.module_utils.definitions.integration_event
# Reference by Internet resource
- name: IntegrationEvent reference
  description: Complete reference of the IntegrationEvent object model.
  link: https://developer.cisco.com/docs/dna-center/api/1-3-3-x
# Reference by Internet resource
- name: IntegrationEvent reference
  description: SDK reference.
  link: https://dnacentersdk.readthedocs.io/en/latest/api/api.html#v2-1-1-summary
'''

EXAMPLES = r'''
'''

RETURN = r'''
data_0:
    description: Used to retrieve the list of integration events that failed to create tickets in ITSM.
    returned: success,changed,always
    type: list
    contains:
        instanceId:
            description: It is the integration event's instanceId.
            returned: success,changed,always
            type: str
            sample: 'sample_string'
        eventId:
            description: It is the integration event's eventId.
            returned: success,changed,always
            type: str
            sample: 'sample_string'
        name:
            description: It is the integration event's name.
            returned: success,changed,always
            type: str
            sample: 'sample_string'
        type:
            description: It is the integration event's type.
            returned: success,changed,always
            type: str
            sample: 'sample_string'
        category:
            description: It is the integration event's category.
            returned: success,changed,always
            type: str
            sample: 'sample_string'
        domain:
            description: It is the integration event's domain.
            returned: success,changed,always
            type: str
            sample: 'sample_string'
        subDomain:
            description: It is the integration event's subDomain.
            returned: success,changed,always
            type: str
            sample: 'sample_string'
        severity:
            description: It is the integration event's severity.
            returned: success,changed,always
            type: str
            sample: 'sample_string'
        source:
            description: It is the integration event's source.
            returned: success,changed,always
            type: str
            sample: 'sample_string'
        timestamp:
            description: It is the integration event's timestamp.
            returned: success,changed,always
            type: int
            sample: 0
        enrichmentInfo:
            description: It is the integration event's enrichmentInfo.
            returned: success,changed,always
            type: dict
            contains:
                eventStatus:
                    description: It is the integration event's eventStatus.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                errorCode:
                    description: It is the integration event's errorCode.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                errorDescription:
                    description: It is the integration event's errorDescription.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                responseReceivedFromITSMSystem:
                    description: It is the integration event's responseReceivedFromITSMSystem.
                    returned: success,changed,always
                    type: dict

        description:
            description: It is the integration event's description.
            returned: success,changed,always
            type: str
            sample: 'sample_string'


data_1:
    description: Allows retry of multiple failed ITSM event instances. The retry request payload can be given as a list of strings: ["instance1","instance2","instance3",..] A minimum of one instance Id is mandatory. The list of failed event instance Ids can be retrieved using the 'Get Failed ITSM Events' API in the 'instanceId' attribute.
    returned: success,changed,always
    type: dict
    contains:
        executionId:
            description: Execution Id, property of the response body.
            returned: success,changed,always
            type: str
            sample: 'sample_string'
        executionStatusUrl:
            description: Execution Status Url, property of the response body.
            returned: success,changed,always
            type: str
            sample: 'sample_string'
        message:
            description: Message, property of the response body.
            returned: success,changed,always
            type: str
            sample: 'sample_string'

'''

from ansible.module_utils.basic import AnsibleModule
from ansible_collections.cisco.dnac.plugins.module_utils.dnac import ModuleDefinition, DNACModule, dnac_argument_spec
from ansible_collections.cisco.dnac.plugins.module_utils.definitions.integration_event import module_definition


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