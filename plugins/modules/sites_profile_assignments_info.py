#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)


DOCUMENTATION = r"""
---
module: sites_profile_assignments_info
short_description: Information module for Sites Profile Assignments Info
description:
- This module represents an alias of the module sites_profile_assignments_v1_info
version_added: '6.15.0'
extends_documentation_fragment:
  - cisco.dnac.module_info
author: Rafael Campos (@racampos)
options:
  headers:
    description: Additional headers.
    type: dict
  siteId:
    description:
    - SiteId path parameter. The `id` of the site, retrievable from `/dna/intent/api/v1/sites`.
    type: str
  offset:
    description:
    - Offset query parameter. The first record to show for this page; the first record is numbered 1.
    type: float
  limit:
    description:
    - Limit query parameter. The number of records to show for this page;The minimum is 1, and the maximum is 500.
    type: float
requirements:
- dnacentersdk >= 2.4.9
- python >= 3.5
seealso:
- name: Cisco DNA Center documentation for Site Design RetrievesTheListOfNetworkProfilesThatTheGivenSiteHasBeenAssignedV1
  description: Complete reference of the RetrievesTheListOfNetworkProfilesThatTheGivenSiteHasBeenAssignedV1 API.
  link: https://developer.cisco.com/docs/dna-center/#!retrieves-the-list-of-network-profiles-that-the-given-site-has-been-assigned
notes:
  - SDK Method used are
    site_design.SiteDesign.retrieves_the_list_of_network_profiles_that_the_given_site_has_been_assigned_v1,

  - Paths used are
    get /dna/intent/api/v1/sites/{siteId}/profileAssignments,
  - It should be noted that this module is an alias of sites_profile_assignments_v1_info

"""

EXAMPLES = r"""
- name: Get all Sites Profile Assignments Info
  cisco.dnac.sites_profile_assignments_info:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    headers: "{{my_headers | from_json}}"
    offset: 0
    limit: 0
    siteId: string
  register: result

"""
RETURN = r"""
dnac_response:
  description: A dictionary or list with the response returned by the Cisco DNAC Python SDK
  returned: always
  type: dict
  sample: >
    {
      "response": [
        {
          "id": "string"
        }
      ],
      "version": "string"
    }
"""
