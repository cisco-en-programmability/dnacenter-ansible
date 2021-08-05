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
version_added: '1.0.0'
author: Rafael Campos (@racampos)
options:
  payload:
    description: Event Subscription's payload.
    suboptions:
      description:
        description: Event Subscription's description.
        type: str
      filter:
        description: Event Subscription's filter.
        suboptions:
          eventIds:
            description: Event Subscription's eventIds.
            elements: str
            type: list
        type: dict
      name:
        description: Event Subscription's name.
        type: str
      subscriptionEndpoints:
        description: Event Subscription's subscriptionEndpoints.
        suboptions:
          instanceId:
            description: Event Subscription's instanceId.
            type: str
          subscriptionDetails:
            description: Event Subscription's subscriptionDetails.
            suboptions:
              connectorType:
                description: Event Subscription's connectorType.
                type: str
              method:
                description: Event Subscription's method.
                type: str
              name:
                description: Event Subscription's name.
                type: str
              url:
                description: Event Subscription's url.
                type: str
            type: dict
        type: list
      subscriptionId:
        description: Event Subscription's subscriptionId.
        type: str
      version:
        description: Event Subscription's version.
        type: str
    type: list
  subscriptions:
    description: Subscriptions query parameter. List of EventSubscriptionId's for removal.
    type: str
requirements:
- dnacentersdk
seealso:
# Reference by Internet resource
- name: Event Subscription reference
  description: Complete reference of the Event Subscription object model.
  link: https://dnacentersdk.readthedocs.io/en/latest/api/api.html#v3-0-0-summary
"""

EXAMPLES = r"""
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
