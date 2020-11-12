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
module: import_image_url
short_description: Manage ImportImageUrl objects of SoftwareImageManagementSwim
description:
- Fetches a software image from remote file system (using URL for HTTP/FTP) and uploads to DNA Center. Supported image files extensions are bin, img, tar, smu, pie, aes, iso, ova, tar_gz and qcow2.
version_added: '1.0'
author: first last (@GitHubID)
options:
    schedule_at:
        description:
        - Epoch Time (The number of milli-seconds since January 1 1970 UTC) at which the distribution should be scheduled (Optional) .
        type: str
    schedule_desc:
        description:
        - Custom Description (Optional).
        type: str
    schedule_origin:
        description:
        - Originator of this call (Optional).
        type: str
    payload:
        description:
        - An object to send in the Request body.
        type: list
        required: True
        elements: dict
        suboptions:
            applicationType:
                description:
                - It is the import image url's applicationType.
                type: str
            imageFamily:
                description:
                - It is the import image url's imageFamily.
                type: str
            sourceURL:
                description:
                - It is the import image url's sourceURL.
                type: str
            thirdParty:
                description:
                - It is the import image url's thirdParty.
                type: bool
            vendor:
                description:
                - It is the import image url's vendor.
                type: str


requirements:
- dnacentersdk
seealso:
# Reference by module name
- module: cisco.dnac.plugins.module_utils.definitions.import_image_url
# Reference by Internet resource
- name: ImportImageUrl reference
  description: Complete reference of the ImportImageUrl object model.
  link: https://developer.cisco.com/docs/dna-center/api/1-3-3-x
# Reference by Internet resource
- name: ImportImageUrl reference
  description: SDK reference.
  link: https://dnacentersdk.readthedocs.io/en/latest/api/api.html#v2-1-1-summary
"""

EXAMPLES = r"""
"""

RETURN = r"""
data_0:
    description: Fetches a software image from remote file system (using URL for HTTP/FTP) and uploads to DNA Center. Supported image files extensions are bin, img, tar, smu, pie, aes, iso, ova, tar_gz and qcow2.
    returned: success,changed,always
    type: dict
    contains:
        response:
            description: ImageImportFromUrlDTO's response.
            returned: success,changed,always
            type: dict
            contains:
                taskId:
                    description: It is the import image url's taskId.
                    returned: success,changed,always
                    type: dict
                url:
                    description: It is the import image url's url.
                    returned: success,changed,always
                    type: str
                    sample: '<url>'

        version:
            description: ImageImportFromUrlDTO's version.
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
from ansible_collections.cisco.dnac.plugins.module_utils.definitions.import_image_url import (
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
