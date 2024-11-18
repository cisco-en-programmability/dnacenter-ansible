#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)


DOCUMENTATION = r"""
---
module: compliance_device_by_id_info
short_description: Information module for Compliance Device By Id Info
description:
- This module represents an alias of the module compliance_device_by_id_v1_info
version_added: '3.1.0'
extends_documentation_fragment:
  - cisco.dnac.module_info
author: Rafael Campos (@racampos)
options:
  headers:
    description: Additional headers.
    type: dict
  deviceUuid:
    description:
    - DeviceUuid path parameter. Device Id.
    type: str
  category:
    description:
    - >
      Category query parameter. Category can have any value among 'INTENT', 'RUNNING_CONFIG' , 'IMAGE' , 'PSIRT' ,
      'DESIGN_OOD' , 'EOX' , 'NETWORK_SETTINGS'.
    type: str
  complianceType:
    description:
    - >
      ComplianceType query parameter. Specify "Compliance type(s)" separated by commas. The Compliance type can be
      'APPLICATION_VISIBILITY', 'EOX', 'FABRIC', 'IMAGE', 'NETWORK_PROFILE', 'NETWORK_SETTINGS', 'PSIRT',
      'RUNNING_CONFIG', 'WORKFLOW'.
    type: str
  diffList:
    description:
    - DiffList query parameter. Diff list pass true to fetch the diff list.
    type: bool
requirements:
- dnacentersdk >= 2.4.9
- python >= 3.5
seealso:
- name: Cisco DNA Center documentation for Compliance ComplianceDetailsOfDeviceV1
  description: Complete reference of the ComplianceDetailsOfDeviceV1 API.
  link: https://developer.cisco.com/docs/dna-center/#!compliance-details-of-device-v-1
notes:
  - SDK Method used are
    compliance.Compliance.compliance_details_of_device_v1,

  - Paths used are
    get /dna/intent/api/v1/compliance/{deviceUuid}/detail,
  - It should be noted that this module is an alias of compliance_device_by_id_v1_info

"""

EXAMPLES = r"""
- name: Get all Compliance Device By Id Info
  cisco.dnac.compliance_device_by_id_info:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    headers: "{{my_headers | from_json}}"
    category: string
    complianceType: string
    diffList: True
    deviceUuid: string
  register: result

"""
RETURN = r"""
dnac_response:
  This alias returns the output of compliance_device_by_id_v1_info.
"""
