#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: app_policy_info
short_description: Information module for App Policy
description:
- Get all App Policy.
version_added: '3.1.0'
extends_documentation_fragment:
  - cisco.dnac.module_info
author: Rafael Campos (@racampos)
options:
  headers:
    description: Additional headers.
    type: dict
  policyScope:
    description:
    - PolicyScope query parameter. Policy scope name.
    type: str
requirements:
- dnacentersdk >= 2.3.1
- python >= 3.5
seealso:
# Reference by Internet resource
- name: App Policy reference
  description: Complete reference of the App Policy object model.
  link: https://dnacentersdk.readthedocs.io/en/latest/api/api.html#v3-0-0-summary
"""

EXAMPLES = r"""
- name: Get all App Policy
  cisco.dnac.app_policy_info:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    headers:
      custom: value
    policyScope: string
  register: result

"""

RETURN = r"""
dnac_response:
  description: A dictionary or list with the response returned by the Cisco DNAC Python SDK
  returned: always
  type: dict
  sample: >
    {
      "response": [
        {
          "id": "string",
          "instanceId": 0,
          "displayName": "string",
          "instanceCreatedOn": 0,
          "instanceUpdatedOn": 0,
          "instanceVersion": 0,
          "createTime": 0,
          "deployed": true,
          "isSeeded": true,
          "isStale": true,
          "lastUpdateTime": 0,
          "name": "string",
          "namespace": "string",
          "provisioningState": "string",
          "qualifier": "string",
          "resourceVersion": 0,
          "targetIdList": [
            {}
          ],
          "type": "string",
          "cfsChangeInfo": [
            {}
          ],
          "customProvisions": [
            {}
          ],
          "deletePolicyStatus": "string",
          "internal": true,
          "isDeleted": true,
          "isEnabled": true,
          "isScopeStale": true,
          "iseReserved": true,
          "policyScope": "string",
          "policyStatus": "string",
          "priority": 0,
          "pushed": true,
          "advancedPolicyScope": {
            "id": "string",
            "instanceId": 0,
            "displayName": "string",
            "instanceCreatedOn": 0,
            "instanceUpdatedOn": 0,
            "instanceVersion": 0,
            "name": "string",
            "advancedPolicyScopeElement": [
              {
                "id": "string",
                "instanceId": 0,
                "displayName": "string",
                "instanceCreatedOn": 0,
                "instanceUpdatedOn": 0,
                "instanceVersion": 0,
                "groupId": [
                  "string"
                ],
                "ssid": [
                  {}
                ]
              }
            ]
          },
          "contractList": [
            {}
          ],
          "exclusiveContract": {
            "id": "string",
            "instanceId": 0,
            "displayName": "string",
            "instanceCreatedOn": 0,
            "instanceUpdatedOn": 0,
            "instanceVersion": 0,
            "clause": [
              {
                "id": "string",
                "instanceId": 0,
                "displayName": "string",
                "instanceCreatedOn": 0,
                "instanceUpdatedOn": 0,
                "instanceVersion": 0,
                "priority": 0,
                "type": "string",
                "relevanceLevel": "string",
                "deviceRemovalBehavior": "string",
                "hostTrackingEnabled": true
              }
            ]
          },
          "identitySource": {
            "id": "string",
            "instanceId": 0,
            "displayName": "string",
            "instanceCreatedOn": 0,
            "instanceUpdatedOn": 0,
            "instanceVersion": 0,
            "state": "string",
            "type": "string"
          },
          "producer": {
            "id": "string",
            "instanceId": 0,
            "displayName": "string",
            "instanceCreatedOn": 0,
            "instanceUpdatedOn": 0,
            "instanceVersion": 0,
            "scalableGroup": [
              {
                "idRef": "string"
              }
            ]
          },
          "consumer": {
            "id": "string",
            "instanceId": 0,
            "displayName": "string",
            "instanceCreatedOn": 0,
            "instanceUpdatedOn": 0,
            "instanceVersion": 0,
            "scalableGroup": [
              {
                "idRef": "string"
              }
            ]
          }
        }
      ],
      "version": "string"
    }
"""