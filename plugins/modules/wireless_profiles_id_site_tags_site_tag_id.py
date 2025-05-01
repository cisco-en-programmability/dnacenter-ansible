#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)
DOCUMENTATION = r"""
---
module: wireless_profiles_id_site_tags_site_tag_id
short_description: Resource module for Wireless Profiles Id Site Tags Site Tag Id
description:
  - This module represents an alias of the module wireless_profiles_id_site_tags_site_tag_id_v1
version_added: '6.17.0'
extends_documentation_fragment:
  - cisco.dnac.module
author: Rafael Campos (@racampos)
options:
  apProfileName:
    description: Ap Profile Name.
    type: str
  flexProfileName:
    description: Flex Profile Name.
    type: str
  id:
    description: Id path parameter. Wireless Profile Id.
    type: str
  siteIds:
    description: Site Ids.
    elements: str
    type: list
  siteTagId:
    description: SiteTagId path parameter. Site Tag Id.
    type: str
  siteTagName:
    description: Use English letters, numbers, special characters except <, /, '.*',
      ? and leading/trailing space.
    type: str
requirements:
  - dnacentersdk >= 2.4.9
  - python >= 3.5
seealso:
  - name: Cisco DNA Center documentation for Wireless DeleteASpecificSiteTagFromAWirelessProfileV1
    description: Complete reference of the DeleteASpecificSiteTagFromAWirelessProfileV1
      API.
    link:
      https://developer.cisco.com/docs/dna-center/#!delete-a-specific-site-tag-from-a-wireless-profile
  - name: Cisco DNA Center documentation for Wireless UpdateASpecificSiteTagForAWirelessProfileV1
    description: Complete reference of the UpdateASpecificSiteTagForAWirelessProfileV1
      API.
    link:
      https://developer.cisco.com/docs/dna-center/#!update-a-specific-site-tag-for-a-wireless-profile
notes:
  - SDK Method used are wireless.Wireless.delete_a_specific_site_tag_from_a_wireless_profile_v1,
    wireless.Wireless.update_a_specific_site_tag_for_a_wireless_profile_v1,
  - Paths used are delete /dna/intent/api/v1/wirelessProfiles/{id}/siteTags/{siteTagId},
    put /dna/intent/api/v1/wirelessProfiles/{id}/siteTags/{siteTagId},
  - It should be noted that this module is an alias of wireless_profiles_id_site_tags_site_tag_id_v1
"""
EXAMPLES = r"""
- name: Update by id
  cisco.dnac.wireless_profiles_id_site_tags_site_tag_id:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    state: present
    apProfileName: string
    flexProfileName: string
    id: string
    siteIds:
      - string
    siteTagId: string
    siteTagName: string
- name: Delete by id
  cisco.dnac.wireless_profiles_id_site_tags_site_tag_id:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    state: absent
    id: string
    siteTagId: string
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
