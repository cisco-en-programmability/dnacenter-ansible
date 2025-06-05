#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)
DOCUMENTATION = r"""
---
module: wireless_profiles_id_site_tags_bulk
short_description: Resource module for Wireless Profiles Id Site Tags Bulk
description:
  - This module represents an alias of the module wireless_profiles_id_site_tags_bulk_v1
version_added: '6.17.0'
extends_documentation_fragment:
  - cisco.dnac.module
author: Rafael Campos (@racampos)
options:
  id:
    description: Id path parameter. Network profile id.
    type: str
  items:
    description: Root.
    type: list
    elements: dict
    suboptions:
      apProfileName:
        description: Ap Profile Name.
        type: str
      flexProfileName:
        description: Flex Profile Name.
        type: str
      siteIds:
        description: Site Ids.
        type: list
        elements: str
      siteTagName:
        description: Use English letters, numbers, and special characters except `<`,
          `/`, `.*`, `?`, and leading/trailing spaces.
        type: str
requirements:
  - dnacentersdk >= 2.4.9
  - python >= 3.5
seealso:
  - name: Cisco DNA Center documentation for Wireless CreateMultipleSiteTagsForAWirelessProfileInBulkV1
    description: Complete reference of the CreateMultipleSiteTagsForAWirelessProfileInBulkV1
      API.
    link:
      https://developer.cisco.com/docs/dna-center/#!create-multiple-site-tags-for-a-wireless-profile-in-bulk
notes:
  - SDK Method used are wireless.Wireless.create_multiple_site_tags_for_a_wireless_profile_in_bulk_v1,
  - Paths used are post /dna/intent/api/v1/wirelessProfiles/{id}/siteTags/bulk,
  - It should be noted that this module is an alias of wireless_profiles_id_site_tags_bulk_v1
"""
EXAMPLES = r"""
- name: Create
  cisco.dnac.wireless_profiles_id_site_tags_bulk:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    id: string
    items:
      - apProfileName: string
        flexProfileName: string
        siteIds:
          - string
        siteTagName: string
"""
RETURN = r"""
dnac_response:
  description: A dictionary or list with the response returned by the Cisco DNAC Python SDK
  returned: always
  type: dict
  sample: >
    {
      "response": {
        "taskId": "string",
        "url": "string"
      },
      "version": "string"
    }
"""
