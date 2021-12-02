#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: business_sda_hostonboarding_ssid_ippool
short_description: Resource module for Business Sda Hostonboarding Ssid Ippool
description:
- Manage operations create and update of the resource Business Sda Hostonboarding Ssid Ippool.
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
- dnacentersdk >= 2.4.0
- python >= 3.5
seealso:
# Reference by Internet resource
- name: Business Sda Hostonboarding Ssid Ippool reference
  description: Complete reference of the Business Sda Hostonboarding Ssid Ippool object model.
  link: https://dnacentersdk.readthedocs.io/en/latest/api/api.html#v3-0-0-summary
"""

EXAMPLES = r"""
- name: Create
  cisco.dnac.business_sda_hostonboarding_ssid_ippool:
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
  cisco.dnac.business_sda_hostonboarding_ssid_ippool:
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
  type: list
  sample: >
    [
      {
        "executionId": "string",
        "executionStatusURL": "string",
        "message": "string"
      }
    ]
"""
