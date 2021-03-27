#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright: (c) 2020, Rafael Campos <rcampos@altus.cr>
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

ANSIBLE_METADATA = {
    "metadata_version": "0.0.1",
    "status": ["preview"],
    "supported_by": "community",
}

DOCUMENTATION = r"""
---
module: event_subscription
short_description: Manage EventSubscription objects of EventManagement
description:
- Delete EventSubscriptions.
- Gets the list of Subscriptions's based on provided offset and limit.
- Subscribe SubscriptionEndpoint to list of registered events.
- Update SubscriptionEndpoint to list of registered events.
- Returns the Count of EventSubscriptions.
version_added: '1.0.0'
author: Rafael Campos (@racampos)
options:
  subscriptions:
    description:
    - List of EventSubscriptionId's for removal.
    - Required for state delete.
    type: str
  event_ids:
    description:
    - List of subscriptions related to the respective eventIds.
    - Required for state query.
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
    - Required for state query.
    type: bool

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
"""

EXAMPLES = r"""
- name: delete_event_subscriptions
  cisco.dnac.event_subscription:
    state: delete  # required
    subscriptions: SomeValue  # string, required
  
- name: get_event_subscriptions
  cisco.dnac.event_subscription:
    state: query  # required
    event_ids: SomeValue  # string
    limit: 1  #  number
    offset: 1  #  number
    order: SomeValue  # string
    sort_by: SomeValue  # string
  register: query_result
  
- name: create_event_subscriptions
  cisco.dnac.event_subscription:
    state: create  # required
    payload:  # required
    - filter:  # required
        eventIds:
        - SomeValue  # string
      subscriptionId: SomeValue  # string
      version: SomeValue  # string
      name: SomeValue  # string
      description: SomeValue  # string
      subscriptionEndpoints:
      - instanceId: SomeValue  # string
        subscriptionDetails:
          name: SomeValue  # string
          url: SomeValue  # string
          method: SomeValue  # string
          connectorType: SomeValue  # string
  
- name: update_event_subscriptions
  cisco.dnac.event_subscription:
    state: update  # required
    payload:  # required
    - filter:  # required
        eventIds:
        - SomeValue  # string
      subscriptionId: SomeValue  # string
      version: SomeValue  # string
      name: SomeValue  # string
      description: SomeValue  # string
      subscriptionEndpoints:
      - instanceId: SomeValue  # string
        subscriptionDetails:
          name: SomeValue  # string
          url: SomeValue  # string
          method: SomeValue  # string
          connectorType: SomeValue  # string
  
- name: count_of_event_subscriptions
  cisco.dnac.event_subscription:
    state: query  # required
    event_ids: SomeValue  # string, required
    count: True  # boolean, required
  register: query_result
  
"""

RETURN = """
delete_event_subscriptions:
    description: Delete EventSubscriptions.
    returned: success
    type: dict
    contains:
      statusUri:
      description: Status Uri, property of the response body.
      returned: success
      type: str
      sample: '<statusuri>'

get_event_subscriptions:
    description: Gets the list of Subscriptions's based on provided offset and limit.
    returned: always
    type: dict
    contains:
      payload:
      description: It is the event subscription's payload.
      returned: always
      type: list
      contains:
        version:
          description: It is the event subscription's version.
          returned: always
          type: str
          sample: '1.0'
        name:
          description: It is the event subscription's name.
          returned: always
          type: str
          sample: '<name>'
        description:
          description: It is the event subscription's description.
          returned: always
          type: str
          sample: '<description>'
        subscriptionEndpoints:
          description: It is the event subscription's subscriptionEndpoints.
          returned: always
          type: list
          contains:
            instanceId:
              description: It is the event subscription's instanceId.
              returned: always
              type: str
              sample: '<instanceid>'
            id:
              description: It is the event subscription's id.
              returned: always
              type: str
              sample: '478012'
            subscriptionDetails:
              description: It is the event subscription's subscriptionDetails.
              returned: always
              type: dict
              contains:
                name:
                  description: It is the event subscription's name.
                  returned: always
                  type: str
                  sample: '<name>'
                url:
                  description: It is the event subscription's url.
                  returned: always
                  type: str
                  sample: '<url>'
                method:
                  description: It is the event subscription's method.
                  returned: always
                  type: str
                  sample: '<method>'
                connectorType:
                  description: It is the event subscription's connectorType.
                  returned: always
                  type: str
                  sample: '<connectortype>'


        filter:
          description: It is the event subscription's filter.
          returned: always
          type: dict
          contains:
            eventIds:
              description: It is the event subscription's eventIds.
              returned: always
              type: list



create_event_subscriptions:
    description: Subscribe SubscriptionEndpoint to list of registered events.
    returned: success
    type: dict
    contains:
      statusUri:
      description: Status Uri, property of the response body.
      returned: success
      type: str
      sample: '<statusuri>'

update_event_subscriptions:
    description: Update SubscriptionEndpoint to list of registered events.
    returned: changed
    type: dict
    contains:
      statusUri:
      description: Status Uri, property of the response body.
      returned: changed
      type: str
      sample: '<statusuri>'

count_of_event_subscriptions:
    description: Returns the Count of EventSubscriptions.
    returned: always
    type: dict
    contains:
      response:
      description: Response, property of the response body.
      returned: always
      type: int
      sample: 0

"""
