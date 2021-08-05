#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: event_subscription_email
short_description: Resource module for Event Subscription Email
description:
- Manage operations create and update of the resource Event Subscription Email.
version_added: '1.0.0'
author: Rafael Campos (@racampos)
options:
  payload:
    description: Event Subscription Email's payload.
    suboptions:
      description:
        description: Event Subscription Email's description.
        type: str
      filter:
        description: Event Subscription Email's filter.
        suboptions:
          eventIds:
            description: Event Subscription Email's eventIds.
            elements: str
            type: list
        type: dict
      name:
        description: Event Subscription Email's name.
        type: str
      subscriptionEndpoints:
        description: Event Subscription Email's subscriptionEndpoints.
        suboptions:
          instanceId:
            description: Event Subscription Email's instanceId.
            type: str
          subscriptionDetails:
            description: Event Subscription Email's subscriptionDetails.
            suboptions:
              connectorType:
                description: Event Subscription Email's connectorType.
                type: str
              fromEmailAddress:
                description: Event Subscription Email's fromEmailAddress.
                type: str
              subject:
                description: Event Subscription Email's subject.
                type: str
              toEmailAddresses:
                description: Event Subscription Email's toEmailAddresses.
                elements: str
                type: list
            type: dict
        type: list
      subscriptionId:
        description: Event Subscription Email's subscriptionId.
        type: str
      version:
        description: Event Subscription Email's version.
        type: str
    type: list
requirements:
- dnacentersdk
seealso:
# Reference by Internet resource
- name: Event Subscription Email reference
  description: Complete reference of the Event Subscription Email object model.
  link: https://dnacentersdk.readthedocs.io/en/latest/api/api.html#v3-0-0-summary
"""

EXAMPLES = r"""
- name: Update all
  cisco.dnac.event_subscription_email:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    state: present

- name: Create
  cisco.dnac.event_subscription_email:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    state: present

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
