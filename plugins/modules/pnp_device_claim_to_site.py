#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: pnp_device_claim_to_site
short_description: Resource module for Pnp Device Claim To Site
description:
- Manage operation create of the resource Pnp Device Claim To Site.
- Claim a device based on DNA-C Site based design process. Different parameters are required for different device platforms.
version_added: '3.1.0'
extends_documentation_fragment:
  - cisco.dnac.module
author: Rafael Campos (@racampos)
options:
  configInfo:
    version_added: '4.2.0'
    description: Pnp Device Claim To Site's configInfo.
    suboptions:
      configId:
        description: Pnp Device Claim To Site's configId.
        type: str
      configParameters:
        description: Pnp Device Claim To Site's configParameters.
        elements: dict
        suboptions:
          key:
            description: Pnp Device Claim To Site's key.
            type: str
          value:
            description: Pnp Device Claim To Site's value.
            type: str
        type: list
    type: dict
  deviceId:
    description: Pnp Device Claim To Site's deviceId.
    type: str
  hostname:
    version_added: '4.2.0'
    description: Pnp Device Claim To Site's hostname.
    type: str
  imageInfo:
    version_added: '4.2.0'
    description: Pnp Device Claim To Site's imageInfo.
    suboptions:
      imageId:
        description: Pnp Device Claim To Site's imageId.
        type: str
      skip:
        description: Skip flag.
        type: bool
    type: dict
  rfProfile:
    version_added: '6.1.0'
    description: Pnp Device Claim To Site's rfProfile.
    type: str
  siteId:
    description: Pnp Device Claim To Site's siteId.
    type: str
  type:
    description: Pnp Device Claim To Site's type.
    type: str
requirements:
- dnacentersdk >= 2.4.8
- python >= 3.5
notes:
  - SDK Method used are
    device_onboarding_pnp.DeviceOnboardingPnp.claim_a_device_to_a_site,

  - Paths used are
    post /dna/intent/api/v1/onboarding/pnp-device/site-claim,

"""

EXAMPLES = r"""
- name: Create
  cisco.dnac.pnp_device_claim_to_site:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    configInfo:
      configId: string
      configParameters:
      - key: string
        value: string
    deviceId: string
    hostname: string
    imageInfo:
      imageId: string
      skip: true
    siteId: string
    rfProfile: string
    type: string

"""

RETURN = r"""
dnac_response:
  description: A dictionary or list with the response returned by the Cisco DNAC Python SDK
  returned: always
  type: dict
  sample: >
    {
      "response": "string",
      "version": "string"
    }
"""
