#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright: (c) 2020, Rafael Campos <rcampos@altus.cr>
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: topology
short_description: Manage Topology objects of Topology
description:
- Returns Layer 2 network Topology by specified VLAN ID.
- Returns the Layer 3 network Topology by routing protocol.
- Returns the raw physical Topology by specified criteria of nodeType.
- Returns site Topology.
- Returns the list of VLAN names.
version_added: '1.0.0'
author: Rafael Campos (@racampos)
options:
  vlan_id:
    description:
    - Vlan Name for e.g Vlan1, Vlan23 etc.
    type: str
    required: True
  layer2:
    description:
    - If true retrieves the layer 2 Topology.
    type: bool
    required: True
  topology_type:
    description:
    - Type of Topology(OSPF,ISIS,etc).
    type: str
    required: True
  layer3:
    description:
    - If true retrieves the layer 3 Topology.
    type: bool
    required: True
  node_type:
    description:
    - NodeType query parameter.
    type: str
  physical:
    description:
    - If true retrieves the physical Topology.
    type: bool
    required: True
  site:
    description:
    - If true retrieves the site Topology.
    type: bool
    required: True
  vlan:
    description:
    - If true retrieves the vlan Topology.
    type: bool
    required: True

requirements:
- dnacentersdk
seealso:
# Reference by module name
- module: cisco.dnac.plugins.module_utils.definitions.topology
# Reference by Internet resource
- name: Topology reference
  description: Complete reference of the Topology object model.
  link: https://developer.cisco.com/docs/dna-center/api/1-3-3-x
# Reference by Internet resource
- name: Topology reference
  description: SDK reference.
  link: https://dnacentersdk.readthedocs.io/en/latest/api/api.html#v2-1-1-summary
"""

EXAMPLES = r"""
- name: get_topology_details
  cisco.dnac.topology:
    state: query  # required
    vlan_id: SomeValue  # string, required
    layer2: True  # boolean, required
  register: query_result

- name: get_l3_topology_details
  cisco.dnac.topology:
    state: query  # required
    topology_type: SomeValue  # string, required
    layer3: True  # boolean, required
  register: query_result

- name: get_physical_topology
  cisco.dnac.topology:
    state: query  # required
    physical: True  # boolean, required
    node_type: SomeValue  # string
  register: query_result

- name: get_site_topology
  cisco.dnac.topology:
    state: query  # required
    site: True  # boolean, required
  register: query_result

- name: get_vlan_details
  cisco.dnac.topology:
    state: query  # required
    vlan: True  # boolean, required
  register: query_result

"""

RETURN = """
"""
