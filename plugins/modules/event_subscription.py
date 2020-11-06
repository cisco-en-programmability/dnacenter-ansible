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
module: event_subscription
short_description: Manage EventSubscription objects of EventManagement
description:
- Delete EventSubscriptions.
- Gets the list of Subscriptions's based on provided offset and limit.
- Subscribe SubscriptionEndpoint to list of registered events.
- Update SubscriptionEndpoint to list of registered events.
- Returns the Count of EventSubscriptions.
version_added: '1.0'
author: first last (@GitHubID)
options:
    subscriptions:
        description:
        - List of EventSubscriptionId's for removal.
        type: str
    event_ids:
        description:
        - List of subscriptions related to the respective eventIds.
        type: str
    limit:
        description:
        - The number of Subscriptions's to limit in the resultset whose default value 10.
        type: int
    offset:
        description:
        - The number of Subscriptions's to offset in the resultset whose default value 0.
        type: int
    order:
        description:
        - Order query parameter.
        type: str
    sort_by:
        description:
        - SortBy field name.
        type: str
    payload:
        description:
        - An object to send in the Request body.
        type: list
        required: True
        elements: dict
        suboptions:
            description:
                description:
                - It is the event subscription's description.
                type: str
            filter:
                description:
                - It is the event subscription's filter.
                type: dict
                required: True
                suboptions:
                    eventIds:
                        description:
                        - It is the event subscription's eventIds.
                        type: list

            name:
                description:
                - It is the event subscription's name.
                type: str
            subscriptionEndpoints:
                description:
                - It is the event subscription's subscriptionEndpoints.
                type: list
                elements: dict
                suboptions:
                    instanceId:
                        description:
                        - It is the event subscription's instanceId.
                        type: str
                    subscriptionDetails:
                        description:
                        - It is the event subscription's subscriptionDetails.
                        type: dict
                        suboptions:
                            connectorType:
                                description:
                                - It is the event subscription's connectorType.
                                type: str
                            method:
                                description:
                                - It is the event subscription's method.
                                type: str
                            name:
                                description:
                                - It is the event subscription's name.
                                type: str
                            url:
                                description:
                                - It is the event subscription's url.
                                type: str


            subscriptionId:
                description:
                - It is the event subscription's subscriptionId.
                type: str
            version:
                description:
                - It is the event subscription's version.
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
- module: cisco.dnac.plugins.module_utils.definitions.event_subscription
# Reference by Internet resource
- name: EventSubscription reference
  description: Complete reference of the EventSubscription object model.
  link: https://developer.cisco.com/docs/dna-center/api/1-3-3-x
# Reference by Internet resource
- name: EventSubscription reference
  description: SDK reference.
  link: https://dnacentersdk.readthedocs.io/en/latest/api/api.html#v2-1-1-summary
'''

EXAMPLES = r'''
'''

RETURN = r'''
data_0:
    description: Delete EventSubscriptions.
    returned: success,changed,always
    type: dict
    contains:
        statusUri:
            description: Status Uri, property of the response body.
            returned: success,changed,always
            type: str
            sample: 'sample_string'

data_1:
    description: Gets the list of Subscriptions's based on provided offset and limit.
    returned: success,changed,always
    type: list
    contains:
        version:
            description: It is the event subscription's version.
            returned: success,changed,always
            type: str
            sample: 'sample_string'
        name:
            description: It is the event subscription's name.
            returned: success,changed,always
            type: str
            sample: 'sample_string'
        description:
            description: It is the event subscription's description.
            returned: success,changed,always
            type: str
            sample: 'sample_string'
        subscriptionEndpoints:
            description: It is the event subscription's subscriptionEndpoints.
            returned: success,changed,always
            type: list
            contains:
                instanceId:
                    description: It is the event subscription's instanceId.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                id:
                    description: It is the event subscription's id.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                subscriptionDetails:
                    description: It is the event subscription's subscriptionDetails.
                    returned: success,changed,always
                    type: dict
                    contains:
                        name:
                            description: It is the event subscription's name.
                            returned: success,changed,always
                            type: str
                            sample: 'sample_string'
                        url:
                            description: It is the event subscription's url.
                            returned: success,changed,always
                            type: str
                            sample: 'sample_string'
                        method:
                            description: It is the event subscription's method.
                            returned: success,changed,always
                            type: str
                            sample: 'sample_string'
                        connectorType:
                            description: It is the event subscription's connectorType.
                            returned: success,changed,always
                            type: str
                            sample: 'sample_string'


        filter:
            description: It is the event subscription's filter.
            returned: success,changed,always
            type: dict
            contains:
                eventIds:
                    description: It is the event subscription's eventIds.
                    returned: success,changed,always
                    type: list



data_2:
    description: Subscribe SubscriptionEndpoint to list of registered events.
    returned: success,changed,always
    type: dict
    contains:
        statusUri:
            description: Status Uri, property of the response body.
            returned: success,changed,always
            type: str
            sample: 'sample_string'

data_3:
    description: Update SubscriptionEndpoint to list of registered events.
    returned: success,changed,always
    type: dict
    contains:
        statusUri:
            description: Status Uri, property of the response body.
            returned: success,changed,always
            type: str
            sample: 'sample_string'

data_4:
    description: Returns the Count of EventSubscriptions.
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
from ansible_collections.cisco.dnac.plugins.module_utils.definitions.event_subscription import module_definition


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

    elif state == "delete":
        dnac.exec("delete")

    elif state == "create":
        dnac.disable_validation()
        dnac.exec("post")

    elif state == "update":
        dnac.disable_validation()
        dnac.exec("put")

    dnac.exit_json()


if __name__ == "__main__":
    main()