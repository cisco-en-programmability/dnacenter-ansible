#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)


DOCUMENTATION = r"""
---
module: topology_layer_2_info
short_description: Information module for Topology Layer 2 Info
description:
- This module represents an alias of the module topology_layer_2_v1_info
version_added: '3.1.0'
extends_documentation_fragment:
  - cisco.dnac.module_info
author: Rafael Campos (@racampos)
options:
  headers:
    description: Additional headers.
    type: dict
  vlanID:
    description:
    - VlanID path parameter. Vlan Name for e.g Vlan1, Vlan23 etc.
    type: str
requirements:
- dnacentersdk >= 2.4.9
- python >= 3.5
seealso:
- name: Cisco DNA Center documentation for Topology GetTopologyDetailsV1
  description: Complete reference of the GetTopologyDetailsV1 API.
  link: https://developer.cisco.com/docs/dna-center/#!get-topology-details-v-1
notes:
  - SDK Method used are
    topology.Topology.get_topology_details_v1,

  - Paths used are
    get /dna/intent/api/v1/topology/l2/{vlanID},
  - It should be noted that this module is an alias of topology_layer_2_v1_info

"""

EXAMPLES = r"""
- name: Get Topology Layer 2 Info by id
  cisco.dnac.topology_layer_2_info:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    headers: "{{my_headers | from_json}}"
    vlanID: string
  register: result

"""
RETURN = r"""
dnac_response:
  This alias returns the output of topology_layer_2_v1_info.
"""
