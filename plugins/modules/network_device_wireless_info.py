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
module: network_device_wireless_info
short_description: Manage NetworkDeviceWirelessInfo objects of Devices
description:
- Returns the wireless lan controller info with given device ID.
version_added: '1.0'
author: first last (@GitHubID)
options:
    id:
        description:
        - Device ID.
        type: str
        required: True

requirements:
- dnacentersdk
seealso:
# Reference by module name
- module: cisco.dnac.plugins.module_utils.definitions.network_device_wireless_info
# Reference by Internet resource
- name: NetworkDeviceWirelessInfo reference
  description: Complete reference of the NetworkDeviceWirelessInfo object model.
  link: https://developer.cisco.com/docs/dna-center/api/1-3-3-x
# Reference by Internet resource
- name: NetworkDeviceWirelessInfo reference
  description: SDK reference.
  link: https://dnacentersdk.readthedocs.io/en/latest/api/api.html#v2-1-1-summary
"""

EXAMPLES = r"""
"""

RETURN = r"""
data_0:
    description: Returns the wireless lan controller info with given device ID.
    returned: success,changed,always
    type: dict
    contains:
        response:
            description: Response, property of the response body.
            returned: success,changed,always
            type: dict
            contains:
                adminEnabledPorts:
                    description: It is the network device wireless info's adminEnabledPorts.
                    returned: success,changed,always
                    type: list
                apGroupName:
                    description: It is the network device wireless info's apGroupName.
                    returned: success,changed,always
                    type: str
                    sample: '<apgroupname>'
                deviceId:
                    description: It is the network device wireless info's deviceId.
                    returned: success,changed,always
                    type: str
                    sample: '<deviceid>'
                ethMacAddress:
                    description: It is the network device wireless info's ethMacAddress.
                    returned: success,changed,always
                    type: str
                    sample: '<ethmacaddress>'
                flexGroupName:
                    description: It is the network device wireless info's flexGroupName.
                    returned: success,changed,always
                    type: str
                    sample: '<flexgroupname>'
                id:
                    description: It is the network device wireless info's id.
                    returned: success,changed,always
                    type: str
                    sample: '478012'
                instanceTenantId:
                    description: It is the network device wireless info's instanceTenantId.
                    returned: success,changed,always
                    type: str
                    sample: '<instancetenantid>'
                instanceUuid:
                    description: It is the network device wireless info's instanceUuid.
                    returned: success,changed,always
                    type: str
                    sample: '<instanceuuid>'
                lagModeEnabled:
                    description: It is the network device wireless info's lagModeEnabled.
                    returned: success,changed,always
                    type: bool
                    sample: false
                netconfEnabled:
                    description: It is the network device wireless info's netconfEnabled.
                    returned: success,changed,always
                    type: bool
                    sample: false
                wirelessLicenseInfo:
                    description: It is the network device wireless info's wirelessLicenseInfo.
                    returned: success,changed,always
                    type: str
                    sample: '<wirelesslicenseinfo>'
                wirelessPackageInstalled:
                    description: It is the network device wireless info's wirelessPackageInstalled.
                    returned: success,changed,always
                    type: bool
                    sample: false

        version:
            description: Version, property of the response body.
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
from ansible_collections.cisco.dnac.plugins.module_utils.definitions.network_device_wireless_info import (
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

    if state == "query":
        dnac.exec("get")

    dnac.exit_json()


if __name__ == "__main__":
    main()
