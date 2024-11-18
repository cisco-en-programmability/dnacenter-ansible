#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)


DOCUMENTATION = r"""
---
module: network_profiles_for_sites_site_assignments_bulk_delete
short_description: Resource module for Network Profiles For Sites Site Assignments Bulk Delete
description:
- This module represents an alias of the module network_profiles_for_sites_site_assignments_bulk_delete_v1
version_added: '6.15.0'
extends_documentation_fragment:
  - cisco.dnac.module
author: Rafael Campos (@racampos)
options:
  profileId:
    description: ProfileId path parameter. The `id` of the network profile, retrievable
      from `GET /intent/api/v1/networkProfilesForSites`.
    type: str
  siteId:
    description: SiteId query parameter. The `id` of the site, retrievable from `GET
      /intent/api/v1/sites`.
    type: str
requirements:
- dnacentersdk >= 2.4.9
- python >= 3.5
seealso:
- name: Cisco DNA Center documentation for Site Design UnassignsANetworkProfileForSitesFromMultipleSitesV1
  description: Complete reference of the UnassignsANetworkProfileForSitesFromMultipleSitesV1 API.
  link: https://developer.cisco.com/docs/dna-center/#!unassigns-a-network-profile-for-sites-from-multiple-sites-v-1
notes:
  - SDK Method used are
    site_design.SiteDesign.unassigns_a_network_profile_for_sites_from_multiple_sites_v1,

  - Paths used are
    delete /dna/intent/api/v1/networkProfilesForSites/{profileId}/siteAssignments/bulk,
  - It should be noted that this module is an alias of network_profiles_for_sites_site_assignments_bulk_delete_v1

"""

EXAMPLES = r"""
- name: Delete all
  cisco.dnac.network_profiles_for_sites_site_assignments_bulk_delete:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    profileId: string
    siteId: string

"""
RETURN = r"""
dnac_response:
  description:
    - This alias returns the output of network_profiles_for_sites_site_assignments_bulk_delete_v1.
"""