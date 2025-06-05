#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)
DOCUMENTATION = r"""
---
module: business_sda_hostonboarding_ssid_ippool_v1
short_description: Resource module for Business Sda Hostonboarding Ssid Ippool V1
description:
  - Manage operations create and update of the resource Business Sda Hostonboarding
    Ssid Ippool V1.
  - Add SSID to IP Pool Mapping.
  - Update SSID to IP Pool Mapping.
version_added: '4.0.0'
extends_documentation_fragment:
  - cisco.dnac.module
author: Rafael Campos (@racampos)
options:
  scalableGroupName:
    description: Scalable Group Name.
    type: str
  siteNameHierarchy:
    description: Site Name Hierarchy.
    type: str
  ssidNames:
    description: List of SSIDs.
    elements: str
    type: list
  vlanName:
    description: VLAN Name.
    type: str
requirements:
  - dnacentersdk >= 2.4.9
  - python >= 3.5
seealso:
  - name: Cisco DNA Center documentation for Fabric Wireless AddSSIDToIPPoolMappingV1
    description: Complete reference of the AddSSIDToIPPoolMappingV1 API.
    link: https://developer.cisco.com/docs/dna-center/#!add-ssid-to-ip-pool-mapping
  - name: Cisco DNA Center documentation for Fabric Wireless UpdateSSIDToIPPoolMappingV1
    description: Complete reference of the UpdateSSIDToIPPoolMappingV1 API.
    link: https://developer.cisco.com/docs/dna-center/#!update-ssid-to-ip-pool-mapping
notes:
  - SDK Method used are fabric_wireless.FabricWireless.add_ssid_to_ip_pool_mapping_v1,
    fabric_wireless.FabricWireless.update_ssid_to_ip_pool_mapping_v1,
  - Paths used are post /dna/intent/api/v1/business/sda/hostonboarding/ssid-ippool,
    put /dna/intent/api/v1/business/sda/hostonboarding/ssid-ippool,
"""
EXAMPLES = r"""
- name: Create
  cisco.dnac.business_sda_hostonboarding_ssid_ippool_v1:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    state: present
    scalableGroupName: string
    siteNameHierarchy: string
    ssidNames:
      - string
    vlanName: string
- name: Update all
  cisco.dnac.business_sda_hostonboarding_ssid_ippool_v1:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    state: present
    scalableGroupName: string
    siteNameHierarchy: string
    ssidNames:
      - string
    vlanName: string
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
