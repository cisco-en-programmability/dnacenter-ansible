#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: fabric_site_health_summaries_count_v1_info
short_description: Information module for Fabric Site Health Summaries Count V1
description:
- Get all Fabric Site Health Summaries Count V1.
- Get a count of Fabric sites. Use available query parameters to get the count of a subset of fabric sites.
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
  id:
    description:
    - >
      Id query parameter. The list of entity Uuids. (Ex."6bef213c-19ca-4170-8375-b694e251101c") Examples
      id=6bef213c-19ca-4170-8375-b694e251101c (single entity uuid requested) id=6bef213c-19ca-4170-8375-
      b694e251101c&id=32219612-819e-4b5e-a96b-cf22aca13dd9&id=2541e9a7-b80d-4955-8aa2-79b233318ba0 (multiple
      entity uuid with '&' separator).
    type: str
requirements:
- dnacentersdk >= 2.4.9
- python >= 3.5
seealso:
- name: Cisco DNA Center documentation for SDA ReadFabricSiteCountV1
  description: Complete reference of the ReadFabricSiteCountV1 API.
  link: https://developer.cisco.com/docs/dna-center/#!read-fabric-site-count
notes:
  - SDK Method used are
    sda.Sda.read_fabric_site_count_v1,

  - Paths used are
    get /dna/data/api/v1/fabricSiteHealthSummaries/count,

"""

EXAMPLES = r"""
- name: Get all Fabric Site Health Summaries Count V1
  cisco.dnac.fabric_site_health_summaries_count_v1_info:
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
        "count": 0
      },
      "version": "string"
    }
"""
