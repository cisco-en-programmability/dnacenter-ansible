#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: wireless_settings_certificate_renewal_profiles_count_info
short_description: Information module for Wireless Settings Certificate Renewal Profiles Count
description:
  - Get all Wireless Settings Certificate Renewal Profiles Count. - > Retrieves the count of access point certificate renewal
    profiles that are created in the catalyst centre network design for wireless.
version_added: '6.46.0'
extends_documentation_fragment:
  - cisco.dnac.module_info
author: Rafael Campos (@racampos)
options:
  headers:
    description: Additional headers.
    type: dict
requirements:
  - dnacentersdk >= 2.11.0
  - python >= 3.12
seealso:
  - name: Cisco DNA Center documentation for Wireless GetLSCCertificateRenewalProfileCount
    description: Complete reference of the GetLSCCertificateRenewalProfileCount API.
    link: https://developer.cisco.com/docs/dna-center/#!get-lsc-certificate-renewal-profile-count
notes:
  - SDK Method used are
    wireless.Wireless.get_l_s_c_certificate_renewal_profile_count,
  - Paths used are
    get /dna/intent/api/v1/wirelessSettings/certificateRenewalProfiles/count,
"""

EXAMPLES = r"""
---
- name: Get all Wireless Settings Certificate Renewal Profiles Count
  cisco.dnac.wireless_settings_certificate_renewal_profiles_count_info:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    headers: "{{my_headers | from_json}}"
  register: result
"""
RETURN = r"""
dnac_response:
  description: A dictionary or list with the response returned by the Cisco DNAC Python SDK
  returned: always
  type: dict
  sample: >
    {
      "response": {
        "count": 0
      },
      "version": "string"
    }
"""
