#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)


DOCUMENTATION = r"""
---
module: reserve_ip_subpool_info
short_description: Information module for Reserve Ip Subpool Info
description:
- This module represents an alias of the module reserve_ip_subpool_v1_info
version_added: '3.1.0'
extends_documentation_fragment:
  - cisco.dnac.module_info
author: Rafael Campos (@racampos)
options:
  headers:
    description: Additional headers.
    type: dict
  siteId:
    description:
    - >
      SiteId query parameter. Site id of site from which to retrieve associated reserve pools. Either siteId (per
      site queries) or ignoreInheritedGroups must be used. They can also be used together.
    type: str
  offset:
    description:
    - Offset query parameter. Offset/starting row. Indexed from 1.
    type: float
  limit:
    description:
    - >
      Limit query parameter. Number of reserve pools to be retrieved. Default is 25 if not specified. Maximum
      allowed limit is 500.
    type: float
  ignoreInheritedGroups:
    description:
    - >
      IgnoreInheritedGroups query parameter. Ignores pools inherited from parent site. Either siteId or
      ignoreInheritedGroups must be passed. They can also be used together.
    type: str
  poolUsage:
    description:
    - PoolUsage query parameter. Can take values empty, partially-full or empty-partially-full.
    type: str
  groupName:
    description:
    - GroupName query parameter. Name of the group.
    type: str
requirements:
- dnacentersdk >= 2.4.9
- python >= 3.5
seealso:
- name: Cisco DNA Center documentation for Network Settings GetReserveIPSubpoolV1
  description: Complete reference of the GetReserveIPSubpoolV1 API.
  link: https://developer.cisco.com/docs/dna-center/#!get-reserve-ip-subpool-v-1
notes:
  - SDK Method used are
    network_settings.NetworkSettings.get_reserve_ip_subpool_v1,

  - Paths used are
    get /dna/intent/api/v1/reserve-ip-subpool,
  - It should be noted that this module is an alias of reserve_ip_subpool_v1_info

"""

EXAMPLES = r"""
- name: Get all Reserve Ip Subpool Info
  cisco.dnac.reserve_ip_subpool_info:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    headers: "{{my_headers | from_json}}"
    siteId: string
    offset: 0
    limit: 0
    ignoreInheritedGroups: string
    poolUsage: string
    groupName: string
  register: result

"""
RETURN = r"""
dnac_response:
  This alias returns the output of reserve_ip_subpool_v1_info.
"""
