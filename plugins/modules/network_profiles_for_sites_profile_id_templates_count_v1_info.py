#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: network_profiles_for_sites_profile_id_templates_count_v1_info
short_description: Information module for Network Profiles For Sites Profile Id Templates Count V1
description:
- Get all Network Profiles For Sites Profile Id Templates Count V1.
- Retrieves the count of all CLI templates attached to a network profile by the profile ID.
version_added: '6.17.0'
extends_documentation_fragment:
  - cisco.dnac.module_info
author: Rafael Campos (@racampos)
options:
  headers:
    description: Additional headers.
    type: dict
  profileId:
    description:
    - >
      ProfileId path parameter. The `id` of the network profile, retrievable from `GET
      /intent/api/v1/networkProfilesForSites`.
    type: str
requirements:
- dnacentersdk >= 2.4.9
- python >= 3.5
seealso:
- name: Cisco DNA Center documentation for Network Settings RetrieveCountOfCLITemplatesAttachedToANetworkProfileV1
  description: Complete reference of the RetrieveCountOfCLITemplatesAttachedToANetworkProfileV1 API.
  link: https://developer.cisco.com/docs/dna-center/#!retrieve-count-of-cli-templates-attached-to-a-network-profile
notes:
  - SDK Method used are
    network_settings.NetworkSettings.retrieve_count_of_cli_templates_attached_to_a_network_profile_v1,

  - Paths used are
    get /dna/intent/api/v1/networkProfilesForSites/{profileId}/templates/count,

"""

EXAMPLES = r"""
- name: Get all Network Profiles For Sites Profile Id Templates Count V1
  cisco.dnac.network_profiles_for_sites_profile_id_templates_count_v1_info:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    headers: "{{my_headers | from_json}}"
    profileId: string
  register: result

"""
RETURN = r"""
dnac_response:
  description: A dictionary or list with the response returned by the Cisco DNAC Python SDK
  returned: always
  type: dict
  sample: >
    {
      "version": "string",
      "response": {
        "count": 0
      }
    }
"""
