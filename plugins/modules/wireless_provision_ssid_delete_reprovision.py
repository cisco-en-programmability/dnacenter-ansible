#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)
DOCUMENTATION = r"""
---
module: wireless_provision_ssid_delete_reprovision
short_description: Resource module for Wireless Provision Ssid Delete Reprovision
description:
  - This module represents an alias of the module wireless_provision_ssid_delete_reprovision_v1
version_added: '3.1.0'
extends_documentation_fragment:
  - cisco.dnac.module
author: Rafael Campos (@racampos)
options:
  headers:
    description: Additional headers.
    type: dict
  managedAPLocations:
    description: ManagedAPLocations path parameter. List of managed AP locations (Site
      Hierarchies). This parameter needs to be encoded as per UTF-8 encoding.
    type: str
  ssidName:
    description: SsidName path parameter. SSID Name. This parameter needs to be encoded
      as per UTF-8 encoding.
    type: str
requirements:
  - dnacentersdk >= 2.4.9
  - python >= 3.5
seealso:
  - name: Cisco DNA Center documentation for Wireless DeleteSSIDAndProvisionItToDevicesV1
    description: Complete reference of the DeleteSSIDAndProvisionItToDevicesV1 API.
    link:
      https://developer.cisco.com/docs/dna-center/#!delete-ssid-and-provision-it-to-devices
notes:
  - SDK Method used are wireless.Wireless.delete_ssid_and_provision_it_to_devices_v1,
  - Paths used are delete /dna/intent/api/v1/business/ssid/{ssidName}/{managedAPLocations},
  - It should be noted that this module is an alias of wireless_provision_ssid_delete_reprovision_v1
"""
EXAMPLES = r"""
- name: Delete by id
  cisco.dnac.wireless_provision_ssid_delete_reprovision:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    headers: '{{my_headers | from_json}}'
    managedAPLocations: string
    ssidName: string
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
