#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)


DOCUMENTATION = r"""
---
module: event_subscription_count_info
short_description: Information module for Event Subscription Count Info
description:
- This module represents an alias of the module event_subscription_count_v1_info
version_added: '3.1.0'
extends_documentation_fragment:
  - cisco.dnac.module_info
author: Rafael Campos (@racampos)
options:
  headers:
    description: Additional headers.
    type: dict
  eventIds:
    description:
    - EventIds query parameter. List of subscriptions related to the respective eventIds.
    type: str
requirements:
- dnacentersdk >= 2.4.9
- python >= 3.5
seealso:
- name: Cisco DNA Center documentation for Event Management CountOfEventSubscriptionsV1
  description: Complete reference of the CountOfEventSubscriptionsV1 API.
  link: https://developer.cisco.com/docs/dna-center/#!count-of-event-subscriptions
notes:
  - SDK Method used are
    event_management.EventManagement.count_of_event_subscriptions_v1,

  - Paths used are
    get /dna/intent/api/v1/event/subscription/count,
  - It should be noted that this module is an alias of event_subscription_count_v1_info

"""

EXAMPLES = r"""
- name: Get all Event Subscription Count Info
  cisco.dnac.event_subscription_count_info:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    headers: "{{my_headers | from_json}}"
    eventIds: string
  register: result

"""
RETURN = r"""
dnac_response:
  description: A dictionary or list with the response returned by the Cisco DNAC Python SDK
  returned: always
  type: dict
  sample: >
    {
      "response": 0
    }
"""
