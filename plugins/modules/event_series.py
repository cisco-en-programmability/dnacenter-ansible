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
module: event_series
short_description: Manage EventSeries objects of EventManagement
description:
- Get the list of Published Notifications.
- Get the Count of Published Notifications.
version_added: '1.0'
author: first last (@GitHubID)
options:
    category:
        description:
        - Category .
        type: str
    domain:
        description:
        - Domain .
        type: str
    end_time:
        description:
        - EndTime .
        type: str
    event_ids:
        description:
        - The registered EventIds should be provided.
        type: str
    limit:
        description:
        - Limit whose default value 10.
        type: int
    offset:
        description:
        - Offset whose default value 0.
        type: int
    order:
        description:
        - Order query parameter.
        type: str
    severity:
        description:
        - Severity .
        type: str
    sort_by:
        description:
        - SortBy field name.
        type: str
    source:
        description:
        - Source .
        type: str
    start_time:
        description:
        - StartTime .
        type: str
    sub_domain:
        description:
        - SubDomain .
        type: str
    type:
        description:
        - Type .
        type: str
    count:
        description:
        - If true gets the number of objects.
        type: bool
        required: True

requirements:
- dnacentersdk
seealso:
# Reference by module name
- module: cisco.dnac.plugins.module_utils.definitions.event_series
# Reference by Internet resource
- name: EventSeries reference
  description: Complete reference of the EventSeries object model.
  link: https://developer.cisco.com/docs/dna-center/api/1-3-3-x
# Reference by Internet resource
- name: EventSeries reference
  description: SDK reference.
  link: https://dnacentersdk.readthedocs.io/en/latest/api/api.html#v2-1-1-summary
'''

EXAMPLES = r'''
'''

RETURN = r'''
data_0:
    description: Get the list of Published Notifications.
    returned: success,changed,always
    type: dict
    contains:
        instanceId:
            description: Instance Id, property of the response body.
            returned: success,changed,always
            type: str
            sample: 'sample_string'
        eventId:
            description: Event Id, property of the response body.
            returned: success,changed,always
            type: str
            sample: 'sample_string'
        name:
            description: Name, property of the response body.
            returned: success,changed,always
            type: str
            sample: 'sample_string'
        namespace:
            description: Namespace, property of the response body.
            returned: success,changed,always
            type: str
            sample: 'sample_string'
        description:
            description: Description, property of the response body.
            returned: success,changed,always
            type: str
            sample: 'sample_string'
        type:
            description: Type, property of the response body.
            returned: success,changed,always
            type: str
            sample: 'sample_string'
        category:
            description: Category, property of the response body.
            returned: success,changed,always
            type: str
            sample: 'sample_string'
        severity:
            description: Severity, property of the response body.
            returned: success,changed,always
            type: int
            sample: 0
        timestamp:
            description: Timestamp, property of the response body.
            returned: success,changed,always
            type: int
            sample: 0
        domain:
            description: Domain, property of the response body.
            returned: success,changed,always
            type: str
            sample: 'sample_string'
        subDomain:
            description: Sub Domain, property of the response body.
            returned: success,changed,always
            type: str
            sample: 'sample_string'
        source:
            description: Source, property of the response body.
            returned: success,changed,always
            type: str
            sample: 'sample_string'
        context:
            description: Context, property of the response body.
            returned: success,changed,always
            type: str
            sample: 'sample_string'
        details:
            description: Details, property of the response body.
            returned: success,changed,always
            type: dict
        tenantId:
            description: Tenant Id, property of the response body.
            returned: success,changed,always
            type: str
            sample: 'sample_string'

data_1:
    description: Get the Count of Published Notifications.
    returned: success,changed,always
    type: dict
    contains:
        response:
            description: Response, property of the response body.
            returned: success,changed,always
            type: int
            sample: 0

'''

from ansible.module_utils.basic import AnsibleModule
from ansible_collections.cisco.dnac.plugins.module_utils.dnac import ModuleDefinition, DNACModule, dnac_argument_spec
from ansible_collections.cisco.dnac.plugins.module_utils.definitions.event_series import module_definition


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