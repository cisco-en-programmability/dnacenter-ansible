#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)
DOCUMENTATION = r"""
---
module: event_webhook_info
short_description: Information module for Event Webhook Info
description:
  - This module represents an alias of the module event_webhook_v1_info
version_added: '6.14.0'
extends_documentation_fragment:
  - cisco.dnac.module_info
author: Rafael Campos (@racampos)
options:
  headers:
    description: Additional headers.
    type: dict
  webhookIds:
    description:
      - WebhookIds query parameter. List of webhook configurations.
    type: str
  offset:
    description:
      - Offset query parameter. The number of webhook configuration's to offset in
        the resultset whose default value 0.
    type: float
  limit:
    description:
      - Limit query parameter. The number of webhook configuration's to limit in the
        resultset whose default value 10.
    type: float
  sortBy:
    description:
      - SortBy query parameter. SortBy field name.
    type: str
  order:
    description:
      - Order query parameter.
    type: str
requirements:
  - dnacentersdk >= 2.4.9
  - python >= 3.5
seealso:
  - name: Cisco DNA Center documentation for Event Management GetWebhookDestinationV1
    description: Complete reference of the GetWebhookDestinationV1 API.
    link: https://developer.cisco.com/docs/dna-center/#!get-webhook-destination
notes:
  - SDK Method used are event_management.EventManagement.get_webhook_destination_v1,
  - Paths used are get /dna/intent/api/v1/event/webhook,
  - It should be noted that this module is an alias of event_webhook_v1_info
"""
EXAMPLES = r"""
- name: Get all Event Webhook Info
  cisco.dnac.event_webhook_info:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    headers: "{{my_headers | from_json}}"
    webhookIds: string
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
  type: dict
  sample: >
    {
      "errorMessage": {
        "errors": [
          "string"
        ]
      },
      "apiStatus": "string",
      "statusMessage": [
        {
          "version": "string",
          "tenantId": "string",
          "webhookId": "string",
          "name": "string",
          "description": "string",
          "url": "string",
          "method": "string",
          "trustCert": true,
          "headers": [
            {
              "name": "string",
              "value": "string",
              "defaultValue": "string",
              "encrypt": true
            }
          ],
          "isProxyRoute": true
        }
      ]
    }
"""
