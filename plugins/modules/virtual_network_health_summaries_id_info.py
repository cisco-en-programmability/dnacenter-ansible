#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)


DOCUMENTATION = r"""
---
module: virtual_network_health_summaries_id_info
short_description: Information module for Virtual Network Health Summaries Id Info
description:
- This module represents an alias of the module virtual_network_health_summaries_id_v1_info
version_added: '6.17.0'
extends_documentation_fragment:
  - cisco.dnac.module_info
author: Rafael Campos (@racampos)
options:
  headers:
    description: Additional headers.
    type: dict
  id:
    description:
    - Id path parameter. Unique virtual networks id.
    type: str
  endTime:
    description:
    - >
      EndTime query parameter. End time to which API queries the data set related to the resource. It must be
      specified in UNIX epochtime in milliseconds. Value is inclusive.
    type: float
  startTime:
    description:
    - >
      StartTime query parameter. Start time from which API queries the data set related to the resource. It must
      be specified in UNIX epochtime in milliseconds. Value is inclusive.
    type: float
  attribute:
    description:
    - Attribute query parameter. The interested fields in the request. For valid attributes, verify the documentation.
    type: str
  view:
    description:
    - >
      View query parameter. The specific summary view being requested. This is an optional parameter which can be
      passed to get one or more of the specific health data summaries associated with virtual networks.
    type: str
requirements:
- dnacentersdk >= 2.4.9
- python >= 3.5
seealso:
- name: Cisco DNA Center documentation for SDA ReadVirtualNetworkWithItsHealthSummaryFromIdV1
  description: Complete reference of the ReadVirtualNetworkWithItsHealthSummaryFromIdV1 API.
  link: https://developer.cisco.com/docs/dna-center/#!read-virtual-network-with-its-health-summary-from-id
notes:
  - SDK Method used are
    sda.Sda.read_virtual_network_with_its_health_summary_from_id_v1,

  - Paths used are
    get /dna/data/api/v1/virtualNetworkHealthSummaries/{id},
  - It should be noted that this module is an alias of virtual_network_health_summaries_id_v1_info

"""

EXAMPLES = r"""
- name: Get Virtual Network Health Summaries Id Info by id
  cisco.dnac.virtual_network_health_summaries_id_info:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    headers: "{{my_headers | from_json}}"
    endTime: 0
    startTime: 0
    attribute: string
    view: string
    id: string
  register: result

"""
RETURN = r"""
dnac_response:
  description: A dictionary or list with the response returned by the Cisco DNAC Python SDK
  returned: always
  type: dict
  sample: >
    {
      "response": {
        "id": "string",
        "name": "string",
        "networkProtocol": "string",
        "vlan": {},
        "vnid": 0,
        "layer": {},
        "totalFabricSites": 0,
        "associatedL3Vn": {},
        "totalEndpoints": 0,
        "goodHealthPercentage": 0,
        "totalDeviceCount": 0,
        "goodHealthDeviceCount": 0,
        "fairHealthDeviceCount": 0,
        "poorHealthDeviceCount": 0,
        "noHealthDeviceCount": 0,
        "vnFabricControlPlaneGoodHealthPercentage": 0,
        "vnFabricControlPlaneTotalDeviceCount": 0,
        "vnFabricControlPlaneGoodHealthDeviceCount": 0,
        "vnFabricControlPlanePoorHealthDeviceCount": 0,
        "vnFabricControlPlaneFairHealthDeviceCount": 0,
        "vnFabricControlPlaneNoHealthDeviceCount": 0,
        "vnServicesHealthPercentage": 0,
        "vnServicesTotalDeviceCount": 0,
        "vnServicesGoodHealthDeviceCount": 0,
        "vnServicesPoorHealthDeviceCount": 0,
        "vnServicesFairHealthDeviceCount": 0,
        "vnServicesNoHealthDeviceCount": 0,
        "vnExitHealthPercentage": 0,
        "vnExitTotalDeviceCount": 0,
        "vnExitGoodHealthDeviceCount": 0,
        "vnExitPoorHealthDeviceCount": 0,
        "vnExitFairHealthDeviceCount": 0,
        "vnExitNoHealthDeviceCount": 0,
        "vnStatusHealthPercentage": {},
        "vnStatusTotalDeviceCount": 0,
        "vnStatusGoodHealthDeviceCount": 0,
        "vnStatusPoorHealthDeviceCount": 0,
        "vnStatusFairHealthDeviceCount": 0,
        "vnStatusNoHealthDeviceCount": 0,
        "pubsubSessionGoodHealthPercentage": 0,
        "pubsubSessionTotalDeviceCount": 0,
        "pubsubSessionGoodHealthDeviceCount": 0,
        "pubsubSessionPoorHealthDeviceCount": 0,
        "pubsubSessionFairHealthDeviceCount": 0,
        "pubsubSessionNoHealthDeviceCount": 0,
        "multiCastGoodHealthPercentage": {},
        "multiCastTotalDeviceCount": 0,
        "multiCastGoodHealthDeviceCount": 0,
        "multiCastPoorHealthDeviceCount": 0,
        "multiCastFairHealthDeviceCount": 0,
        "multiCastNoHealthDeviceCount": 0,
        "internetAvailGoodHealthPercentage": 0,
        "internetAvailTotalDeviceCount": 0,
        "internetAvailGoodHealthDeviceCount": 0,
        "internetAvailPoorHealthDeviceCount": 0,
        "internetAvailFairHealthDeviceCount": 0,
        "internetAvailNoHealthDeviceCount": 0,
        "bgpPeerGoodHealthPercentage": 0,
        "bgpPeerTotalDeviceCount": 0,
        "bgpPeerGoodHealthDeviceCount": 0,
        "bgpPeerPoorHealthDeviceCount": 0,
        "bgpPeerFairHealthDeviceCount": 0,
        "bgpPeerNoHealthDeviceCount": 0,
        "vniGoodHealthPercentage": {},
        "vniTotalDeviceCount": 0,
        "vniGoodHealthDeviceCount": 0,
        "vniPoorHealthDeviceCount": 0,
        "vniFairHealthDeviceCount": 0,
        "vniNoHealthDeviceCount": 0
      }
    }
"""
