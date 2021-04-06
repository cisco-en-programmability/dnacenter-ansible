#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright: (c) 2020, Rafael Campos <rcampos@altus.cr>
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

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

RETURN = r"""
dnac_response:
  description: A dictionary with the response returned by the DNA Center Python SDK
  returned: always
  type: dict
  sample: {"response": 29, "version": "1.0"}
sdk_function:
  description: The DNA Center SDK function used to execute the task
  returned: always
  type: str
  sample: application_policy.get_application_sets
missing_params:
  description: Provided arguments do not comply with the schema of the DNA Center Python SDK function
  returned: when the function request schema is not satisfied
  type: list
  sample:
"""
