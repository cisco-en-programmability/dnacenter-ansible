#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)


DOCUMENTATION = r"""
---
module: site_health_info
short_description: Information module for Site Health Info
description:
- This module represents an alias of the module site_health_v1_info
version_added: '3.1.0'
extends_documentation_fragment:
  - cisco.dnac.module_info
author: Rafael Campos (@racampos)
options:
  headers:
    description: Additional headers.
    type: dict
  siteType:
    description:
    - SiteType query parameter. Site type AREA or BUILDING (case insensitive).
    type: str
  offset:
    description:
    - Offset query parameter. Offset of the first returned data set entry (Multiple of 'limit' + 1).
    type: float
  limit:
    description:
    - Limit query parameter. Max number of data entries in the returned data set 1,50. Default is 25.
    type: float
  timestamp:
    description:
    - Timestamp query parameter. Epoch time(in milliseconds) when the Site Hierarchy data is required.
    type: float
requirements:
- dnacentersdk >= 2.4.9
- python >= 3.5
seealso:
- name: Cisco DNA Center documentation for Sites GetSiteHealthV1
  description: Complete reference of the GetSiteHealthV1 API.
  link: https://developer.cisco.com/docs/dna-center/#!get-site-health-v-1
notes:
  - SDK Method used are
    sites.Sites.get_site_health_v1,

  - Paths used are
    get /dna/intent/api/v1/site-health,
  - It should be noted that this module is an alias of site_health_v1_info

"""

EXAMPLES = r"""
- name: Get all Site Health Info
  cisco.dnac.site_health_info:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    headers: "{{my_headers | from_json}}"
    siteType: string
    offset: 0
    limit: 0
    timestamp: 0
  register: result

"""
RETURN = r"""
dnac_response:
  This alias returns the output of site_health_v1_info.
"""
