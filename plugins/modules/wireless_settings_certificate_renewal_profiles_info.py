#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: wireless_settings_certificate_renewal_profiles_info
short_description: Information module for Wireless Settings Certificate Renewal Profiles
description:
  - Get all Wireless Settings Certificate Renewal Profiles.
  - Get Wireless Settings Certificate Renewal Profiles by id.
  - GET LSC Certificate Renewal Profile by ID. - > Retrieves the access point certificate renewal profiles that are created
    in the catalyst centre network design for wireless. Filtering can be done on access point certificate renewal profile
    name and renewal type.
version_added: '6.46.0'
extends_documentation_fragment:
  - cisco.dnac.module_info
author: Rafael Campos (@racampos)
options:
  headers:
    description: Additional headers.
    type: dict
  lscProfileName:
    description:
      - >
        LscProfileName query parameter. Access point certificate renewal profile name. Use this query parameter
        to obtain the details of access point certificate renewal profile by its name.
    type: str
  renewalType:
    description:
      - >
        RenewalType query parameter. Access point certificate renewal profile renewal type. Use this query
        parameter to obtain the details of access point certificate renewal profile by its renewal type name.
        Example STAGGERED, ONESHOT.
    type: str
  limit:
    description:
      - Limit query parameter. Pagination limit.
    type: int
  offset:
    description:
      - Offset query parameter. Pagination offset.
    type: int
  id:
    description:
      - Id path parameter. LSC Certificate Renewal Profile ID.
    type: str
requirements:
  - dnacentersdk >= 2.11.0
  - python >= 3.12
seealso:
  - name: Cisco DNA Center documentation for Wireless GETLSCCertificateRenewalProfileByID
    description: Complete reference of the GETLSCCertificateRenewalProfileByID API.
    link: https://developer.cisco.com/docs/dna-center/#!g-etlsc-certificate-renewal-profile-by-id
  - name: Cisco DNA Center documentation for Wireless GetLSCCertificateRenewalProfiles
    description: Complete reference of the GetLSCCertificateRenewalProfiles API.
    link: https://developer.cisco.com/docs/dna-center/#!get-lsc-certificate-renewal-profiles
notes:
  - SDK Method used are
    wireless.Wireless.get_l_s_c_certificate_renewal_profile_by_id,
    wireless.Wireless.get_l_s_c_certificate_renewal_profiles,
  - Paths used are
    get /dna/intent/api/v1/wirelessSettings/certificateRenewalProfiles,
    get /dna/intent/api/v1/wirelessSettings/certificateRenewalProfiles/{id},
"""

EXAMPLES = r"""
---
- name: Get all Wireless Settings Certificate Renewal Profiles
  cisco.dnac.wireless_settings_certificate_renewal_profiles_info:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    headers: "{{my_headers | from_json}}"
    lscProfileName: string
    renewalType: string
    limit: 0
    offset: 0
  register: result
- name: Get Wireless Settings Certificate Renewal Profiles by id
  cisco.dnac.wireless_settings_certificate_renewal_profiles_info:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    headers: "{{my_headers | from_json}}"
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
      "lscProfileName": "string",
      "renewalType": "string",
      "renewalDueInDays": 0,
      "CalendarProfileSetting": {
        "schedulerType": "string",
        "duration": {
          "schedulerDay": [
            "string"
          ],
          "schedulerStartTime": "string",
          "schedulerEndTime": "string",
          "schedulerDate": "string"
        }
      }
    }
"""
