#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: sda_layer3_virtual_networks_delete
short_description: Resource module for Sda Layer3 Virtual Networks Delete
description:
  - Manage operation delete of the resource Sda Layer3 Virtual Networks Delete.
  - Deletes a layer 3 virtual network based on id.
version_added: '6.46.0'
extends_documentation_fragment:
  - cisco.dnac.module
author: Rafael Campos (@racampos)
options:
  id:
    description: Id path parameter. ID of the layer 3 virtual network.
    type: str
requirements:
  - dnacentersdk >= 2.11.0
  - python >= 3.12
seealso:
  - name: Cisco DNA Center documentation for SDA DeleteLayer3VirtualNetworkById
    description: Complete reference of the DeleteLayer3VirtualNetworkById API.
    link: https://developer.cisco.com/docs/dna-center/#!delete-layer-3-virtual-network-by-id
notes:
  - SDK Method used are
    sda.Sda.delete_layer3_virtual_network_by_id,
  - Paths used are
    delete /dna/intent/api/v1/sda/layer3VirtualNetworks/{id},
"""

EXAMPLES = r"""
---
- name: Delete by id
  cisco.dnac.sda_layer3_virtual_networks_delete:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    id: string
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
