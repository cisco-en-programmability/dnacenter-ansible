#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)


DOCUMENTATION = r"""
---
module: topology_layer_3_info
short_description: Information module for Topology Layer 3 Info
description:
- This module represents an alias of the module topology_layer_3_v1_info
version_added: '3.1.0'
extends_documentation_fragment:
  - cisco.dnac.module_info
author: Rafael Campos (@racampos)
options:
  headers:
    description: Additional headers.
    type: dict
  topologyType:
    description:
    - TopologyType path parameter. Type of topology(OSPF,ISIS,etc).
    type: str
requirements:
- dnacentersdk >= 2.4.9
- python >= 3.5
seealso:
- name: Cisco DNA Center documentation for Topology GetL3TopologyDetailsV1
  description: Complete reference of the GetL3TopologyDetailsV1 API.
  link: https://developer.cisco.com/docs/dna-center/#!get-l-3-topology-details-v-1
notes:
  - SDK Method used are
    topology.Topology.get_l3_topology_details_v1,

  - Paths used are
    get /dna/intent/api/v1/topology/l3/{topologyType},
  - It should be noted that this module is an alias of topology_layer_3_v1_info

"""

EXAMPLES = r"""
- name: Get Topology Layer 3 Info by id
  cisco.dnac.topology_layer_3_info:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    headers: "{{my_headers | from_json}}"
    topologyType: string
  register: result

"""
RETURN = r"""
dnac_response:
  description:
    - This alias returns the output of topology_layer_3_v1_info.
"""
