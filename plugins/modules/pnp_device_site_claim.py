#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright: (c) 2020, first last <email>
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

ANSIBLE_METADATA = {
    "metadata_version": "0.0.1",
    "status": ["preview"],
    "supported_by": "community",
}

DOCUMENTATION = r"""
---
module: pnp_device_site_claim
short_description: Manage PnpDeviceSiteClaim objects of DeviceOnboardingPnp
description:
- Claim a device based on DNA-C Site based design process. Different parameters are required for different device platforms.
version_added: '1.0'
author: first last (@GitHubID)
options:
  deviceId:
    description:
    - SiteProvisionRequest's deviceId.
    type: str
  siteId:
    description:
    - SiteProvisionRequest's siteId.
    type: str
  type:
    description:
    - SiteProvisionRequest's type.
    - Available values are 'Default', 'AccessPoint', 'StackSwitch', 'Sensor' and 'MobilityExpress'.
    type: str

requirements:
- dnacentersdk
seealso:
# Reference by module name
- module: cisco.dnac.plugins.module_utils.definitions.pnp_device_site_claim
# Reference by Internet resource
- name: PnpDeviceSiteClaim reference
  description: Complete reference of the PnpDeviceSiteClaim object model.
  link: https://developer.cisco.com/docs/dna-center/api/1-3-3-x
# Reference by Internet resource
- name: PnpDeviceSiteClaim reference
  description: SDK reference.
  link: https://dnacentersdk.readthedocs.io/en/latest/api/api.html#v2-1-1-summary
"""

EXAMPLES = r"""
- name: claim_a_device_to_a_site
  cisco.dnac.pnp_device_site_claim
    dnac_host: dnac
    dnac_username: admin
    dnac_password: SomeSecretPassword
    state: create  # required
    deviceId: SomeValue  # string
    siteId: SomeValue  # string
    type: SomeValue  # string, valid values: 'Default', 'AccessPoint', 'StackSwitch', 'Sensor', 'MobilityExpress'.
  delegate_to: localhost
  
"""

RETURN = """
claim_a_device_to_a_site:
    description: Claim a device based on DNA-C Site based design process. Different parameters are required for different device platforms.
    returned: success
    type: dict
    contains:
    response:
      description: SiteProvisionRequest's response.
      returned: success
      type: str
      sample: '<response>'
    version:
      description: SiteProvisionRequest's version.
      returned: success
      type: str
      sample: '1.0'

"""
