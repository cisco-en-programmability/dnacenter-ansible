#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)


DOCUMENTATION = r"""
---
module: pnp_virtual_account_deregister
short_description: Resource module for Pnp Virtual Account Deregister
description:
- This module represents an alias of the module pnp_virtual_account_deregister_v1
version_added: '3.1.0'
extends_documentation_fragment:
  - cisco.dnac.module
author: Rafael Campos (@racampos)
options:
  domain:
    description: Domain query parameter. Smart Account Domain.
    type: str
  name:
    description: Name query parameter. Virtual Account Name.
    type: str
requirements:
- dnacentersdk >= 2.4.9
- python >= 3.5
seealso:
- name: Cisco DNA Center documentation for Device Onboarding (PnP) DeregisterVirtualAccountV1
  description: Complete reference of the DeregisterVirtualAccountV1 API.
  link: https://developer.cisco.com/docs/dna-center/#!deregister-virtual-account-v-1
notes:
  - SDK Method used are
    device_onboarding_pnp.DeviceOnboardingPnp.deregister_virtual_account_v1,

  - Paths used are
    delete /dna/intent/api/v1/onboarding/pnp-settings/vacct,
  - It should be noted that this module is an alias of pnp_virtual_account_deregister_v1

"""

EXAMPLES = r"""
- name: Delete all
  cisco.dnac.pnp_virtual_account_deregister:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    domain: string
    name: string

"""
RETURN = r"""
dnac_response:
  This alias returns the output of pnp_virtual_account_deregister_v1.
"""
