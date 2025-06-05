#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)
DOCUMENTATION = r"""
---
module: cisco_imcs_id_info
short_description: Information module for Cisco Imcs Id Info
description:
  - This module represents an alias of the module cisco_imcs_id_v1_info
version_added: '6.17.0'
extends_documentation_fragment:
  - cisco.dnac.module_info
author: Rafael Campos (@racampos)
options:
  headers:
    description: Additional headers.
    type: dict
  id:
    description:
      - Id path parameter. The unique identifier for this Cisco IMC configuration.
    type: str
requirements:
  - dnacentersdk >= 2.4.9
  - python >= 3.5
seealso:
  - name: Cisco DNA Center documentation for Cisco IMC RetrievesTheCiscoIMCConfigurationForACatalystCenterNodeV1
    description: Complete reference of the RetrievesTheCiscoIMCConfigurationForACatalystCenterNodeV1
      API.
    link:
      https://developer.cisco.com/docs/dna-center/#!retrieves-the-cisco-imc-configuration-for-a-catalyst-center-node
notes:
  - SDK Method used are
    cisco_i_m_c.CiscoIMC.retrieves_the_cisco_i_m_c_configuration_for_a_catalyst_center_node_v1,
  - Paths used are get /dna/system/api/v1/ciscoImcs/{id},
  - It should be noted that this module is an alias of cisco_imcs_id_v1_info
"""
EXAMPLES = r"""
- name: Get Cisco Imcs Id Info by id
  cisco.dnac.cisco_imcs_id_info:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    headers: "{{my_headers | from_json}}"
    id: string
  register: result
"""
RETURN = r"""
dnac_response:
  description: A dictionary or list with the response returned by the Cisco DNAC Python SDK
  returned: always
  type: dict
  sample: >
    {
      "response": {
        "id": "string",
        "nodeId": "string",
        "ipAddress": "string",
        "username": "string"
      },
      "version": "string"
    }
"""
