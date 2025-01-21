#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: sites_time_zone_settings_v1
short_description: Resource module for Sites Time Zone Settings V1
description:
- Manage operation update of the resource Sites Time Zone Settings V1.
- >
   Set time zone settings for a site; `null` values indicate that the setting will be inherited from the parent site;
   empty objects `{}` indicate that the settings is unset.
version_added: '6.15.0'
extends_documentation_fragment:
  - cisco.dnac.module
author: Rafael Campos (@racampos)
options:
  id:
    description: Id path parameter. Site Id.
    type: str
  timeZone:
    description: Sites Time Zone Settings's timeZone.
    suboptions:
      identifier:
        description: Time zone that corresponds to the site's physical location. The
          site time zone is used when scheduling device provisioning and updates. Example
          GMT.
        type: str
    type: dict
requirements:
- dnacentersdk >= 2.4.9
- python >= 3.5
seealso:
- name: Cisco DNA Center documentation for Network Settings SetTimeZoneForASiteV1
  description: Complete reference of the SetTimeZoneForASiteV1 API.
  link: https://developer.cisco.com/docs/dna-center/#!set-time-zone-for-a-site
notes:
  - SDK Method used are
    network_settings.NetworkSettings.set_time_zone_for_a_site_v1,

  - Paths used are
    put /dna/intent/api/v1/sites/{id}/timeZoneSettings,

"""

EXAMPLES = r"""
- name: Update all
  cisco.dnac.sites_time_zone_settings_v1:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    state: present
    id: string
    timeZone:
      identifier: string

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
        "url": "string",
        "taskId": "string"
      }
    }
"""
