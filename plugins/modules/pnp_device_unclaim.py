#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)


DOCUMENTATION = r"""
---
module: pnp_device_unclaim
short_description: Resource module for Pnp Device Unclaim
description:
- This module represents an alias of the module pnp_device_unclaim_v1
version_added: '3.1.0'
extends_documentation_fragment:
  - cisco.dnac.module
author: Rafael Campos (@racampos)
options:
  deviceIdList:
    description: Pnp Device Unclaim's deviceIdList.
    elements: str
    type: list
requirements:
- dnacentersdk >= 2.4.9
- python >= 3.5
seealso:
- name: Cisco DNA Center documentation for Device Onboarding (PnP) UnClaimDeviceV1
  description: Complete reference of the UnClaimDeviceV1 API.
  link: https://developer.cisco.com/docs/dna-center/#!un-claim-device
notes:
  - SDK Method used are
    device_onboarding_pnp.DeviceOnboardingPnp.un_claim_device_v1,

  - Paths used are
    post /dna/intent/api/v1/onboarding/pnp-device/unclaim,
  - It should be noted that this module is an alias of pnp_device_unclaim_v1

"""

EXAMPLES = r"""
- name: Create
  cisco.dnac.pnp_device_unclaim:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    deviceIdList:
    - string

"""
RETURN = r"""
dnac_response:
  description: A dictionary or list with the response returned by the Cisco DNAC Python SDK
  returned: always
  type: dict
  sample: >
    {
      "jsonArrayResponse": [
        {}
      ],
      "jsonResponse": {},
      "message": "string",
      "statusCode": 0
    }
"""
