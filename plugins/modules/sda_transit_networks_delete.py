#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: sda_transit_networks_delete
short_description: Resource module for Sda Transit Networks Delete
description:
  - Manage operation delete of the resource Sda Transit Networks Delete.
  - Deletes a transit network based on id.
version_added: '6.46.0'
extends_documentation_fragment:
  - cisco.dnac.module
author: Rafael Campos (@racampos)
options:
  id:
    description: Id path parameter. ID of the transit network.
    type: str
requirements:
  - dnacentersdk >= 2.11.0
  - python >= 3.12
seealso:
  - name: Cisco DNA Center documentation for SDA DeleteTransitNetworkById
    description: Complete reference of the DeleteTransitNetworkById API.
    link: https://developer.cisco.com/docs/dna-center/#!delete-transit-network-by-id
notes:
  - SDK Method used are
    sda.Sda.delete_transit_network_by_id,
  - Paths used are
    delete /dna/intent/api/v1/sda/transitNetworks/{id},
"""

EXAMPLES = r"""
---
- name: Delete by id
  cisco.dnac.sda_transit_networks_delete:
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
