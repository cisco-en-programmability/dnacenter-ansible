#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: event_subscription
short_description: Resource module for Event Subscription
description:
- Manage operations create, update and delete of the resource Event Subscription.
- Subscribe SubscriptionEndpoint to list of registered events.
- Delete EventSubscriptions.
- Update SubscriptionEndpoint to list of registered events.
version_added: '3.1.0'
extends_documentation_fragment:
  - cisco.dnac.module
author: Rafael Campos (@racampos)
options:
  payload:
    description: Event Subscription's payload.
    elements: dict
    suboptions:
      description:
        description: Description.
        type: str
      filter:
        description: Event Subscription's filter.
        suboptions:
          eventIds:
            description: Event Ids.
            elements: str
            type: list
        type: dict
      name:
        description: Name.
        type: str
      subscriptionEndpoints:
        description: Event Subscription's subscriptionEndpoints.
        elements: dict
        suboptions:
          instanceId:
            description: Instance Id.
            type: str
          subscriptionDetails:
            description: Event Subscription's subscriptionDetails.
            suboptions:
              connectorType:
                description: Connector Type.
                type: str
              method:
                description: Method.
                type: str
              name:
                description: Name.
                type: str
              url:
                description: Url.
                type: str
            type: dict
        type: list
      subscriptionId:
        description: Subscription Id.
        type: str
      version:
        description: Version.
        type: str
    type: list
  subscriptions:
    description: Subscriptions query parameter. List of EventSubscriptionId's for removal.
    type: str
requirements:
- dnacentersdk >= 2.4.9
- python >= 3.5
notes:
  - SDK Method used are
    event_management.EventManagement.create_event_subscriptions,
    event_management.EventManagement.delete_event_subscriptions,
    event_management.EventManagement.update_event_subscriptions,

  - Paths used are
    post /dna/intent/api/v1/event/subscription,
    delete /dna/intent/api/v1/event/subscription,
    put /dna/intent/api/v1/event/subscription,

"""

EXAMPLES = r"""
- name: Delete all
  cisco.dnac.event_subscription:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    state: absent
    subscriptions: string

- name: Update all
  cisco.dnac.event_subscription:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    state: present
    payload:
    - description: string
      filter:
        eventIds:
        - string
      name: string
      subscriptionEndpoints:
      - instanceId: string
        subscriptionDetails:
          connectorType: string
          method: string
          name: string
          url: string
      subscriptionId: string
      version: string

- name: Create
  cisco.dnac.event_subscription:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    state: present
    payload:
    - description: string
      filter:
        eventIds:
        - string
      name: string
      subscriptionEndpoints:
      - instanceId: string
        subscriptionDetails:
          connectorType: string
          method: string
          name: string
          url: string
      subscriptionId: string
      version: string

"""

RETURN = r"""
dnac_response:
  description: A dictionary or list with the response returned by the Cisco DNAC Python SDK
  returned: always
  type: dict
  sample: >
    {
      "statusUri": "string"
    }
"""
