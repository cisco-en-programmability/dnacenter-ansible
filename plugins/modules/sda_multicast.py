#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)
DOCUMENTATION = r"""
---
module: sda_multicast
short_description: Resource module for Sda Multicast
description:
  - This module represents an alias of the module sda_multicast_v1
version_added: '6.15.0'
extends_documentation_fragment:
  - cisco.dnac.module
author: Rafael Campos (@racampos)
options:
  payload:
    description: Sda Multicast V1's payload.
    elements: dict
    suboptions:
      fabricId:
        description: ID of the fabric site (updating this field is not allowed).
        type: str
      replicationMode:
        description: Replication Mode deployed in the fabric site.
        type: str
    type: list
requirements:
  - dnacentersdk >= 2.4.9
  - python >= 3.5
seealso:
  - name: Cisco DNA Center documentation for SDA UpdateMulticastV1
    description: Complete reference of the UpdateMulticastV1 API.
    link: https://developer.cisco.com/docs/dna-center/#!update-multicast
notes:
  - SDK Method used are sda.Sda.update_multicast_v1,
  - Paths used are put /dna/intent/api/v1/sda/multicast,
  - It should be noted that this module is an alias of sda_multicast_v1
"""
EXAMPLES = r"""
- name: Update all
  cisco.dnac.sda_multicast:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    state: present
    payload:
      - fabricId: string
        replicationMode: string
"""
RETURN = r"""
dnac_response:
  description: A dictionary or list with the response returned by the Cisco DNAC Python SDK
  returned: always
  type: dict
  sample: >
    {
      "response": {
        "taskId": "string",
        "url": "string"
      },
      "version": "string"
    }
"""
