#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: event_subscription_syslog
short_description: Resource module for Event Subscription Syslog
description:
- Manage operations create and update of the resource Event Subscription Syslog.
version_added: '1.0.0'
author: Rafael Campos (@racampos)
options:
  payload:
    description: Event Subscription Syslog's payload.
    suboptions:
      description:
        description: Event Subscription Syslog's description.
        type: str
      filter:
        description: Event Subscription Syslog's filter.
        suboptions:
          eventIds:
            description: Event Subscription Syslog's eventIds.
            elements: str
            type: list
        type: dict
      name:
        description: Event Subscription Syslog's name.
        type: str
      subscriptionEndpoints:
        description: Event Subscription Syslog's subscriptionEndpoints.
        suboptions:
          instanceId:
            description: Event Subscription Syslog's instanceId.
            type: str
          subscriptionDetails:
            description: Event Subscription Syslog's subscriptionDetails.
            suboptions:
              connectorType:
                description: Event Subscription Syslog's connectorType.
                type: str
            type: dict
        type: list
      subscriptionId:
        description: Event Subscription Syslog's subscriptionId.
        type: str
      version:
        description: Event Subscription Syslog's version.
        type: str
    type: list
requirements:
- dnacentersdk
seealso:
# Reference by Internet resource
- name: Event Subscription Syslog reference
  description: Complete reference of the Event Subscription Syslog object model.
  link: https://dnacentersdk.readthedocs.io/en/latest/api/api.html#v3-0-0-summary
"""

EXAMPLES = r"""
- name: Update all
  cisco.dnac.event_subscription_syslog:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    state: present

- name: Create
  cisco.dnac.event_subscription_syslog:
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
