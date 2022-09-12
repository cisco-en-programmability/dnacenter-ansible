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
- >
   Claim a device based on DNA-C Site based design process. Different parameters are required for different device
   platforms.
version_added: '3.1.0'
extends_documentation_fragment:
  - cisco.dnac.module
author: Rafael Campos (@racampos)
options:
  configInfo:
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
    version_added: 4.2.0
  deviceId:
    description: Pnp Device Claim To Site's deviceId.
    type: str
  gateway:
    description: Pnp Device Claim To Site's gateway.
    type: str
    version_added: 6.4.0
  hostname:
    description: Pnp Device Claim To Site's hostname.
    type: str
    version_added: 4.2.0
  imageId:
    description: Pnp Device Claim To Site's imageId.
    type: str
  imageInfo:
    description: Pnp Device Claim To Site's imageInfo.
    suboptions:
      imageId:
        description: Pnp Device Claim To Site's imageId.
        type: str
      skip:
        description: Skip flag.
        type: bool
    type: dict
    version_added: 4.2.0
  ipInterfaceName:
    description: Pnp Device Claim To Site's ipInterfaceName.
    type: str
    version_added: 6.4.0
  removeInactive:
    description: RemoveInactive flag.
    type: bool
    version_added: 6.4.0
  rfProfile:
    description: Pnp Device Claim To Site's rfProfile.
    type: str
    version_added: 6.1.0
  siteId:
    description: Pnp Device Claim To Site's siteId.
    type: str
  staticIP:
    description: Pnp Device Claim To Site's staticIP.
    type: str
    version_added: 6.4.0
  subnetMask:
    description: Pnp Device Claim To Site's subnetMask.
    type: str
  type:
    description: Pnp Device Claim To Site's type.
    type: str
  vlanId:
    description: Pnp Device Claim To Site's vlanId.
    type: str
    version_added: 6.4.0
requirements:
- dnacentersdk >= 2.5.4
- python >= 3.5
seealso:
- name: Cisco DNA Center documentation for Device Onboarding (PnP) ClaimADeviceToASite
  description: Complete reference of the ClaimADeviceToASite API.
  link: https://developer.cisco.com/docs/dna-center/#!claim-a-device-to-a-site
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
    gateway: string
    hostname: string
    imageId: string
    imageInfo:
      imageId: string
      skip: true
    ipInterfaceName: string
    removeInactive: true
    rfProfile: string
    siteId: string
    staticIP: string
    subnetMask: string
    type: string
    vlanId: string

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
