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
module: pnp_device_site_config_preview
short_description: Manage PnpDeviceSiteConfigPreview objects of DeviceOnboardingPnp
description:
- Triggers a preview for site-based Day 0 Configuration.
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
- module: cisco.dnac.plugins.module_utils.definitions.pnp_device_site_config_preview
# Reference by Internet resource
- name: PnpDeviceSiteConfigPreview reference
  description: Complete reference of the PnpDeviceSiteConfigPreview object model.
  link: https://developer.cisco.com/docs/dna-center/api/1-3-3-x
# Reference by Internet resource
- name: PnpDeviceSiteConfigPreview reference
  description: SDK reference.
  link: https://dnacentersdk.readthedocs.io/en/latest/api/api.html#v2-1-1-summary
"""

EXAMPLES = r"""
- name: preview_config
  cisco.dnac.pnp_device_site_config_preview:
    state: create  # required
    deviceId: SomeValue  # string
    siteId: SomeValue  # string
    type: SomeValue  # string, valid values: 'Default', 'AccessPoint', 'StackSwitch', 'Sensor', 'MobilityExpress'.
  
"""

RETURN = """
preview_config:
    description: Triggers a preview for site-based Day 0 Configuration.
    returned: success
    type: dict
    contains:
    response:
      description: SiteProvisionRequest's response.
      returned: success
      type: dict
      contains:
        complete:
          description: It is the pnp device site config preview's complete.
          returned: success
          type: bool
          sample: false
        config:
          description: It is the pnp device site config preview's config.
          returned: success
          type: str
          sample: '<config>'
        error:
          description: It is the pnp device site config preview's error.
          returned: success
          type: bool
          sample: false
        errorMessage:
          description: It is the pnp device site config preview's errorMessage.
          returned: success
          type: str
          sample: '<errormessage>'
        expiredTime:
          description: It is the pnp device site config preview's expiredTime.
          returned: success
          type: int
          sample: 0
        rfProfile:
          description: It is the pnp device site config preview's rfProfile.
          returned: success
          type: str
          sample: '<rfprofile>'
        sensorProfile:
          description: It is the pnp device site config preview's sensorProfile.
          returned: success
          type: str
          sample: '<sensorprofile>'
        siteId:
          description: It is the pnp device site config preview's siteId.
          returned: success
          type: str
          sample: '<siteid>'
        startTime:
          description: It is the pnp device site config preview's startTime.
          returned: success
          type: int
          sample: 0
        taskId:
          description: It is the pnp device site config preview's taskId.
          returned: success
          type: str
          sample: 'aeed229047801200e0ef563dbb9a71c2'

    version:
      description: SiteProvisionRequest's version.
      returned: success
      type: str
      sample: '1.0'

"""
