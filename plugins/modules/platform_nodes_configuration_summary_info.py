#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)


DOCUMENTATION = r"""
---
module: platform_nodes_configuration_summary_info
short_description: Information module for Platform Nodes Configuration Summary Info
description:
- This module represents an alias of the module platform_nodes_configuration_summary_v1_info
version_added: '3.1.0'
extends_documentation_fragment:
  - cisco.dnac.module_info
author: Rafael Campos (@racampos)
options:
  headers:
    description: Additional headers.
    type: dict
requirements:
- dnacentersdk >= 2.4.9
- python >= 3.5
seealso:
- name: Cisco DNA Center documentation for Platform Configuration CiscoDNACenterNodesConfigurationSummaryV1
  description: Complete reference of the CiscoDNACenterNodesConfigurationSummaryV1 API.
  link: https://developer.cisco.com/docs/dna-center/#!cisco-dna-center-nodes-configuration-summary-v-1
notes:
  - SDK Method used are
    platform_configuration.PlatformConfiguration.nodes_configuration_summary,

  - Paths used are
    get /dna/intent/api/v1/nodes-config,
  - It should be noted that this module is an alias of platform_nodes_configuration_summary_v1_info

"""

EXAMPLES = r"""
- name: Get all Platform Nodes Configuration Summary Info
  cisco.dnac.platform_nodes_configuration_summary_info:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    headers: "{{my_headers | from_json}}"
  register: result

"""
RETURN = r"""
dnac_response:
  This alias returns the output of platform_nodes_configuration_summary_v1_info.
"""
