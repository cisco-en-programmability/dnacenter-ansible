#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)
DOCUMENTATION = r"""
---
module: sda_fabrics_vlan_to_ssids_fabric_id
short_description: Resource module for Sda Fabrics Vlan To Ssids Fabric Id
description:
  - This module represents an alias of the module sda_fabrics_vlan_to_ssids_fabric_id_v1
version_added: '6.15.0'
extends_documentation_fragment:
  - cisco.dnac.module
author: Rafael Campos (@racampos)
options:
  fabricId:
    description: FabricId path parameter. The 'fabricId' represents the Fabric ID
      of a particular Fabric Site.
    type: str
  payload:
    description: Sda Fabrics Vlan To Ssids Fabric Id's payload.
    elements: dict
    suboptions:
      ssidDetails:
        description: Sda Fabrics Vlan To Ssids Fabric Id's ssidDetails.
        elements: dict
        suboptions:
          name:
            description: Name of the SSID.
            type: str
          securityGroupTag:
            description: Represents the name of the Security Group. Example Auditors,
              BYOD, Developers, etc.
            type: str
        type: list
      vlanName:
        description: Vlan Name.
        type: str
    type: list
requirements:
  - dnacentersdk >= 2.4.9
  - python >= 3.5
seealso:
  - name: Cisco DNA Center documentation for Fabric Wireless AddUpdateOrRemoveSSIDMappingToAVLANV1
    description: Complete reference of the AddUpdateOrRemoveSSIDMappingToAVLANV1 API.
    link:
      https://developer.cisco.com/docs/dna-center/#!add-update-or-remove-ssid-mapping-to-avlan
notes:
  - SDK Method used are fabric_wireless.FabricWireless.add_update_or_remove_ssid_mapping_to_a_vlan_v1,
  - Paths used are put /dna/intent/api/v1/sda/fabrics/{fabricId}/vlanToSsids,
  - It should be noted that this module is an alias of sda_fabrics_vlan_to_ssids_fabric_id_v1
"""
EXAMPLES = r"""
- name: Update all
  cisco.dnac.sda_fabrics_vlan_to_ssids_fabric_id:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    state: present
    fabricId: string
    payload:
      - ssidDetails:
          - name: string
            securityGroupTag: string
        vlanName: string
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
