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
"""

RETURN = r"""
data_0:
    description: Claim a device based on DNA-C Site based design process. Different parameters are required for different device platforms.
    returned: success,changed,always
    type: dict
    contains:
        response:
            description: SiteProvisionRequest's response.
            returned: success,changed,always
            type: str
            sample: '<response>'
        version:
            description: SiteProvisionRequest's version.
            returned: success,changed,always
            type: str
            sample: '1.0'

"""

from ansible.module_utils.basic import AnsibleModule
from ansible_collections.cisco.dnac.plugins.module_utils.dnac import (
    ModuleDefinition,
    DNACModule,
    dnac_argument_spec,
)
from ansible_collections.cisco.dnac.plugins.module_utils.definitions.pnp_device_site_claim import (
    module_definition,
)


def main():

    moddef = ModuleDefinition(module_definition)

    argument_spec = dnac_argument_spec()
    argument_spec.update(moddef.get_argument_spec_dict())

    required_if = moddef.get_required_if_list()

    module = AnsibleModule(
        argument_spec=argument_spec, supports_check_mode=False, required_if=required_if
    )

    dnac = DNACModule(module, moddef)

    state = module.params.get("state")

    if state == "create":
        dnac.disable_validation()
        dnac.exec("post")

    dnac.exit_json()


if __name__ == "__main__":
    main()
