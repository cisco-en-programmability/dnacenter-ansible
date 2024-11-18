#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)


DOCUMENTATION = r"""
---
module: sda_site_member_member_info
short_description: Information module for Sda Site Member Member Info
description:
- This module represents an alias of the module sda_site_member_member_v1_info
version_added: '6.14.0'
extends_documentation_fragment:
  - cisco.dnac.module_info
author: Rafael Campos (@racampos)
options:
  headers:
    description: Additional headers.
    type: dict
  id:
    description:
    - Id path parameter. Site Id.
    type: str
  offset:
    description:
    - Offset query parameter. Offset/starting index for pagination.
    type: str
  limit:
    description:
    - Limit query parameter. Number of devices to be listed. Default and max supported value is 500.
    type: str
  memberType:
    description:
    - MemberType query parameter. Member type (This API only supports the 'networkdevice' type).
    type: str
  level:
    description:
    - >
      Level query parameter. Depth of site hierarchy to be considered to list the devices. If the provided value
      is -1, devices for all child sites will be listed.
    type: str
requirements:
- dnacentersdk >= 2.4.9
- python >= 3.5
seealso:
- name: Cisco DNA Center documentation for Sites GetDevicesThatAreAssignedToASiteV1
  description: Complete reference of the GetDevicesThatAreAssignedToASiteV1 API.
  link: https://developer.cisco.com/docs/dna-center/#!get-devices-that-are-assigned-to-a-site-v-1
notes:
  - SDK Method used are
    sites.Sites.get_devices_that_are_assigned_to_a_site_v1,

  - Paths used are
    get /dna/intent/api/v1/site-member/{id}/member,
  - It should be noted that this module is an alias of sda_site_member_member_v1_info

"""

EXAMPLES = r"""
- name: Get all Sda Site Member Member Info
  cisco.dnac.sda_site_member_member_info:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    headers: "{{my_headers | from_json}}"
    offset: string
    limit: string
    memberType: string
    level: string
    id: string
  register: result

"""
RETURN = r"""
dnac_response:
  This alias returns the output of sda_site_member_member_v1_info.
"""
