#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: fabric_site_health_summaries_v1_info
short_description: Information module for Fabric Site Health Summaries V1
description:
- Get all Fabric Site Health Summaries V1.
- Get a paginated list of Fabric sites Networks with health summary.
version_added: '6.17.0'
extends_documentation_fragment:
  - cisco.dnac.module_info
author: Rafael Campos (@racampos)
options:
  headers:
    description: Additional headers.
    type: dict
  startTime:
    description:
    - >
      StartTime query parameter. Start time from which API queries the data set related to the resource. It must
      be specified in UNIX epochtime in milliseconds. Value is inclusive.
    type: float
  endTime:
    description:
    - >
      EndTime query parameter. End time to which API queries the data set related to the resource. It must be
      specified in UNIX epochtime in milliseconds. Value is inclusive.
    type: float
  limit:
    description:
    - Limit query parameter. Maximum number of records to return.
    type: float
  offset:
    description:
    - >
      Offset query parameter. Specifies the starting point within all records returned by the API. It's one based
      offset. The starting value is 1.
    type: float
  sortBy:
    description:
    - SortBy query parameter. A field within the response to sort by.
    type: str
  order:
    description:
    - Order query parameter. The sort order of the field ascending or descending.
    type: str
  id:
    description:
    - >
      Id query parameter. The list of entity Uuids. (Ex."6bef213c-19ca-4170-8375-b694e251101c") Examples
      id=6bef213c-19ca-4170-8375-b694e251101c (single entity uuid requested) id=6bef213c-19ca-4170-8375-
      b694e251101c&id=32219612-819e-4b5e-a96b-cf22aca13dd9&id=2541e9a7-b80d-4955-8aa2-79b233318ba0 (multiple
      entity uuid with '&' separator).
    type: str
  attribute:
    description:
    - >
      Attribute query parameter. The list of FabricSite health attributes. Please refer to
      ```fabricSiteAttributes``` section in the Open API specification document mentioned in the description.
    type: str
  view:
    description:
    - >
      View query parameter. The specific summary view being requested. A maximum of 3 views can be queried at a
      time per request. Please refer to ```fabricSiteViews``` section in the Open API specification document
      mentioned in the description.
    type: str
requirements:
- dnacentersdk >= 2.4.9
- python >= 3.5
seealso:
- name: Cisco DNA Center documentation for SDA ReadListOfFabricSitesWithTheirHealthSummaryV1
  description: Complete reference of the ReadListOfFabricSitesWithTheirHealthSummaryV1 API.
  link: https://developer.cisco.com/docs/dna-center/#!read-list-of-fabric-sites-with-their-health-summary
notes:
  - SDK Method used are
    sda.Sda.read_list_of_fabric_sites_with_their_health_summary_v1,

  - Paths used are
    get /dna/data/api/v1/fabricSiteHealthSummaries,

"""

EXAMPLES = r"""
- name: Get all Fabric Site Health Summaries V1
  cisco.dnac.fabric_site_health_summaries_v1_info:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    headers: "{{my_headers | from_json}}"
    startTime: 0
    endTime: 0
    limit: 0
    offset: 0
    sortBy: string
    order: string
    id: string
    attribute: string
    view: string
  register: result

"""
RETURN = r"""
dnac_response:
  description: A dictionary or list with the response returned by the Cisco DNAC Python SDK
  returned: always
  type: list
  elements: dict
  sample: >
    [
      {
        "id": "string",
        "name": "string",
        "goodHealthPercentage": 0,
        "goodHealthDeviceCount": 0,
        "totalDeviceCount": 0,
        "poorHealthDeviceCount": 0,
        "fairHealthDeviceCount": 0,
        "associatedL2VnCount": 0,
        "associatedL3VnCount": 0,
        "networkProtocol": "string",
        "connectivityGoodHealthPercentage": 0,
        "connectivityTotalHealthDeviceCount": 0,
        "connectivityGoodHealthDeviceCount": 0,
        "connectivityPoorHealthDeviceCount": 0,
        "connectivityFairHealthDeviceCount": 0,
        "infraGoodHealthPercentage": 0,
        "infraTotalHealthDeviceCount": 0,
        "infraGoodHealthDeviceCount": 0,
        "infraFairHealthDeviceCount": 0,
        "infraPoorHealthDeviceCount": 0,
        "controlPlaneGoodHealthPercentage": 0,
        "controlPlaneTotalHealthDeviceCount": 0,
        "controlPlaneGoodHealthDeviceCount": 0,
        "controlPlanePoorHealthDeviceCount": 0,
        "controlPlaneFairHealthDeviceCount": 0,
        "pubsubInfraVnGoodHealthPercentage": 0,
        "pubsubInfraVnTotalHealthDeviceCount": 0,
        "pubsubInfraVnGoodHealthDeviceCount": 0,
        "pubsubInfraVnPoorHealthDeviceCount": 0,
        "pubsubInfraVnFairHealthDeviceCount": 0,
        "bgpEvpnGoodHealthPercentage": {},
        "bgpEvpnTotalHealthDeviceCount": 0,
        "bgpEvpnGoodHealthDeviceCount": 0,
        "bgpEvpnPoorHealthDeviceCount": 0,
        "bgpEvpnFairHealthDeviceCount": 0,
        "ctsEnvDataDownloadGoodHealthPercentage": 0,
        "ctsEnvDataDownloadTotalHealthDeviceCount": 0,
        "ctsEnvDataDownloadGoodHealthDeviceCount": 0,
        "ctsEnvDataDownloadPoorHealthDeviceCount": 0,
        "ctsEnvDataDownloadFairHealthDeviceCount": 0,
        "aaaStatusGoodHealthPercentage": 0,
        "aaaStatusTotalHealthDeviceCount": 0,
        "aaaStatusGoodHealthDeviceCount": 0,
        "aaaStatusPoorHealthDeviceCount": 0,
        "aaaStatusFairHealthDeviceCount": 0,
        "portChannelGoodHealthPercentage": 0,
        "portChannelTotalHealthDeviceCount": 0,
        "portChannelGoodHealthDeviceCount": 0,
        "portChannelPoorHealthDeviceCount": 0,
        "portChannelFairHealthDeviceCount": 0,
        "peerScoreGoodHealthPercentage": {},
        "peerScoreTotalHealthDeviceCount": 0,
        "peerScoreGoodHealthDeviceCount": 0,
        "peerScorePoorHealthDeviceCount": 0,
        "peerScoreFairHealthDeviceCount": 0,
        "lispSessionGoodHealthPercentage": 0,
        "lispSessionTotalHealthDeviceCount": 0,
        "lispSessionGoodHealthDeviceCount": 0,
        "lispSessionPoorHealthDeviceCount": 0,
        "lispSessionFairHealthDeviceCount": 0,
        "borderToControlPlaneGoodHealthPercentage": 0,
        "borderToControlPlaneTotalHealthDeviceCount": 0,
        "borderToControlPlaneGoodHealthDeviceCount": 0,
        "borderToControlPlanePoorHealthDeviceCount": 0,
        "borderToControlPlaneFairHealthDeviceCount": 0,
        "bgpBgpSiteGoodHealthPercentage": 0,
        "bgpBgpSiteTotalHealthDeviceCount": 0,
        "bgpBgpSiteGoodHealthDeviceCount": 0,
        "bgpBgpSitePoorHealthDeviceCount": 0,
        "bgpBgpSiteFairHealthDeviceCount": 0,
        "bgpPubsubSiteGoodHealthPercentage": 0,
        "bgpPubsubSiteTotalHealthDeviceCount": 0,
        "bgpPubsubSiteGoodHealthDeviceCount": 0,
        "bgpPubsubSitePoorHealthDeviceCount": 0,
        "bgpPubsubSiteFairHealthDeviceCount": 0,
        "bgpPeerInfraVnScoreGoodHealthPercentage": 0,
        "bgpPeerInfraVnTotalHealthDeviceCount": 0,
        "bgpPeerInfraVnGoodHealthDeviceCount": 0,
        "bgpPeerInfraVnPoorHealthDeviceCount": 0,
        "bgpPeerInfraVnFairHealthDeviceCount": 0
      }
    ]
"""
