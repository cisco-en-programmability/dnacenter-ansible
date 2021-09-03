#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: event_subscription_email_info
short_description: Information module for Event Subscription Email
description:
- Get all Event Subscription Email.
version_added: '1.0.0'
author: Rafael Campos (@racampos)
options:
  headers:
    description: Additional headers.
    type: dict
  eventIds:
    description:
    - >
      EventIds query parameter. List of email subscriptions related to the respective eventIds (Comma separated
      event ids).
    type: str
  offset:
    description:
    - Offset query parameter. The number of Subscriptions's to offset in the resultset whose default value 0.
    type: int
  limit:
    description:
    - Limit query parameter. The number of Subscriptions's to limit in the resultset whose default value 10.
    type: int
  sortBy:
    description:
    - SortBy query parameter. SortBy field name.
    type: str
  order:
    description:
    - Order query parameter.
    type: str
requirements:
- dnacentersdk
seealso:
# Reference by Internet resource
- name: Event Subscription Email reference
  description: Complete reference of the Event Subscription Email object model.
  link: https://dnacentersdk.readthedocs.io/en/latest/api/api.html#v3-0-0-summary
"""

EXAMPLES = r"""
- name: Get all Event Subscription Email
  cisco.dnac.event_subscription_email_info:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    headers:
      custom: value
    eventIds: string
    offset: 0
    limit: 0
    sortBy: string
    order: string
  register: result

"""

RETURN = r"""
dnac_response:
  description: A dictionary or list with the response returned by the Cisco DNAC Python SDK
  returned: always
  type: list
  elements: dict
  sample: >
    [
      {
        "version": "string",
        "subscriptionId": "string",
        "name": "string",
        "description": "string",
        "subscriptionEndpoints": [
          {
            "instanceId": "string",
            "subscriptionDetails": {
              "connectorType": "string",
              "instanceId": "string",
              "name": "string",
              "description": "string",
              "fromEmailAddress": "string",
              "toEmailAddresses": [
                "string"
              ],
              "subject": "string"
            },
            "connectorType": "string"
          }
        ],
        "filter": {
          "eventIds": [
            "string"
          ],
          "others": [
            "string"
          ],
          "domainsSubdomains": [
            "string"
          ],
          "types": [
            "string"
          ],
          "categories": [
            "string"
          ],
          "severities": [
            "string"
          ],
          "sources": [
            "string"
          ]
        },
        "isPrivate": "string",
        "tenantId": "string"
      }
    ]
"""
