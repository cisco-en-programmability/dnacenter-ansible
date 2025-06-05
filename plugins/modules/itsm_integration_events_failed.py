#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)
DOCUMENTATION = r"""
---
module: itsm_integration_events_failed
short_description: Resource module for Itsm Integration Events Failed
description:
  - This module represents an alias of the module itsm_integration_events_failed_v1
version_added: '3.1.0'
extends_documentation_fragment:
  - cisco.dnac.module
author: Rafael Campos (@racampos)
options:
  payload:
    description: Itsm Integration Events Failed's payload.
    elements: str
    type: list
requirements:
  - dnacentersdk >= 2.4.9
  - python >= 3.5
seealso:
  - name: Cisco DNA Center documentation for ITSM RetryIntegrationEventsV1
    description: Complete reference of the RetryIntegrationEventsV1 API.
    link: https://developer.cisco.com/docs/dna-center/#!retry-integration-events
notes:
  - SDK Method used are itsm.Itsm.retry_integration_events_v1,
  - Paths used are post /dna/intent/api/v1/integration/events,
  - It should be noted that this module is an alias of itsm_integration_events_failed_v1
"""
EXAMPLES = r"""
- name: Create
  cisco.dnac.itsm_integration_events_failed:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    state: present
    payload:
      - string
"""
RETURN = r"""
dnac_response:
  description: A dictionary or list with the response returned by the Cisco DNAC Python SDK
  returned: always
  type: dict
  sample: >
    {
      "executionId": "string",
      "executionStatusUrl": "string",
      "message": "string"
    }
"""
