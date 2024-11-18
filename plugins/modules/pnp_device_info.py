#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)


DOCUMENTATION = r"""
---
module: pnp_device_info
short_description: Information module for Pnp Device Info
description:
- This module represents an alias of the module pnp_device_v1_info
version_added: '3.1.0'
extends_documentation_fragment:
  - cisco.dnac.module_info
author: Rafael Campos (@racampos)
options:
  headers:
    description: Additional headers.
    type: dict
  limit:
    description:
    - Limit query parameter. Limits number of results.
    type: int
  offset:
    description:
    - Offset query parameter. Index of first result.
    type: int
  sort:
    description:
    - Sort query parameter. Comma seperated list of fields to sort on. 
    elements: str
    type: list
  sortOrder:
    description:
    - SortOrder query parameter. Sort Order Ascending (asc) or Descending (des).
    type: str
  serialNumber:
    description:
    - SerialNumber query parameter. Device Serial Number. 
    elements: str
    type: list
  state_:
    description:
    - State query parameter. Device State. 
    elements: str
    type: list
  onbState:
    description:
    - OnbState query parameter. Device Onboarding State. 
    elements: str
    type: list
  name:
    description:
    - Name query parameter. Device Name. 
    elements: str
    type: list
  pid:
    description:
    - Pid query parameter. Device ProductId. 
    elements: str
    type: list
  source:
    description:
    - Source query parameter. Device Source. 
    elements: str
    type: list
  workflowId:
    description:
    - WorkflowId query parameter. Device Workflow Id. 
    elements: str
    type: list
  workflowName:
    description:
    - WorkflowName query parameter. Device Workflow Name. 
    elements: str
    type: list
  smartAccountId:
    description:
    - SmartAccountId query parameter. Device Smart Account. 
    elements: str
    type: list
  virtualAccountId:
    description:
    - VirtualAccountId query parameter. Device Virtual Account. 
    elements: str
    type: list
  lastContact:
    description:
    - LastContact query parameter. Device Has Contacted lastContact > 0.
    type: bool
  macAddress:
    description:
    - MacAddress query parameter. Device Mac Address.
    type: str
  hostname:
    description:
    - Hostname query parameter. Device Hostname.
    type: str
  siteName:
    description:
    - SiteName query parameter. Device Site Name.
    type: str
  id:
    description:
    - Id path parameter.
    type: str
requirements:
- dnacentersdk >= 2.4.9
- python >= 3.5
seealso:
- name: Cisco DNA Center documentation for Device Onboarding (PnP) GetDeviceByIdV1
  description: Complete reference of the GetDeviceByIdV1 API.
  link: https://developer.cisco.com/docs/dna-center/#!get-device-by-id-v-1
- name: Cisco DNA Center documentation for Device Onboarding (PnP) GetDeviceListSiteManagementV1
  description: Complete reference of the GetDeviceListSiteManagementV1 API.
  link: https://developer.cisco.com/docs/dna-center/#!get-device-list-site-management-v-1
notes:
  - SDK Method used are
    device_onboarding_pnp.DeviceOnboardingPnp.get_device_by_id_v1,
    device_onboarding_pnp.DeviceOnboardingPnp.get_device_list,

  - Paths used are
    get /dna/intent/api/v1/onboarding/pnp-device,
    get /dna/intent/api/v1/onboarding/pnp-device/{id},
  - It should be noted that this module is an alias of pnp_device_v1_info

"""

EXAMPLES = r"""
- name: Get all Pnp Device Info
  cisco.dnac.pnp_device_info:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    headers: "{{my_headers | from_json}}"
    limit: 0
    offset: 0
    sort: []
    sortOrder: string
    serialNumber: []
    state_: []
    onbState: []
    name: []
    pid: []
    source: []
    workflowId: []
    workflowName: []
    smartAccountId: []
    virtualAccountId: []
    lastContact: True
    macAddress: string
    hostname: string
    siteName: string
  register: result

- name: Get Pnp Device Info by id
  cisco.dnac.pnp_device_info:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    headers: "{{my_headers | from_json}}"
    id: string
  register: result

"""
RETURN = r"""
dnac_response:
  description:
    - This alias returns the output of pnp_device_v1_info.
"""
