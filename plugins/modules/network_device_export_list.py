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
module: network_device_export_list
short_description: Manage NetworkDeviceExportList objects of Devices
description:
- Exports the selected network device to a file.
version_added: '1.0'
author: first last (@GitHubID)
options:
    deviceUuids:
        description:
        - ExportDeviceDTO's deviceUuids (list of strings).
        type: list
        required: True
    id:
        description:
        - ExportDeviceDTO's id.
        type: str
    operationEnum:
        description:
        - ExportDeviceDTO's operationEnum.
        - Available values are 'CREDENTIALDETAILS' and 'DEVICEDETAILS'.
        type: str
    parameters:
        description:
        - ExportDeviceDTO's parameters (list of strings).
        type: list
    password:
        description:
        - ExportDeviceDTO's password.
        type: str

requirements:
- dnacentersdk
seealso:
# Reference by module name
- module: cisco.dnac.plugins.module_utils.definitions.network_device_export_list
# Reference by Internet resource
- name: NetworkDeviceExportList reference
  description: Complete reference of the NetworkDeviceExportList object model.
  link: https://developer.cisco.com/docs/dna-center/api/1-3-3-x
# Reference by Internet resource
- name: NetworkDeviceExportList reference
  description: SDK reference.
  link: https://dnacentersdk.readthedocs.io/en/latest/api/api.html#v2-1-1-summary
"""

EXAMPLES = r"""
"""

RETURN = r"""
data_0:
    description: Exports the selected network device to a file.
    returned: success,changed,always
    type: dict
    contains:
        response:
            description: ExportDeviceDTO's response.
            returned: success,changed,always
            type: dict
            contains:
                taskId:
                    description: It is the network device export list's taskId.
                    returned: success,changed,always
                    type: dict
                url:
                    description: It is the network device export list's url.
                    returned: success,changed,always
                    type: str
                    sample: '<url>'

        version:
            description: ExportDeviceDTO's version.
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
from ansible_collections.cisco.dnac.plugins.module_utils.definitions.network_device_export_list import (
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
