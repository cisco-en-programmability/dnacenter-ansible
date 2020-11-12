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
module: file_namespace
short_description: Manage FileNamespace objects of File
description:
- Returns list of available namespaces.
- Returns list of files under a specific namespace.
version_added: '1.0'
author: first last (@GitHubID)
options:
    name_space:
        description:
        - A listing of fileId's.
        type: str
        required: True

requirements:
- dnacentersdk
seealso:
# Reference by module name
- module: cisco.dnac.plugins.module_utils.definitions.file_namespace
# Reference by Internet resource
- name: FileNamespace reference
  description: Complete reference of the FileNamespace object model.
  link: https://developer.cisco.com/docs/dna-center/api/1-3-3-x
# Reference by Internet resource
- name: FileNamespace reference
  description: SDK reference.
  link: https://dnacentersdk.readthedocs.io/en/latest/api/api.html#v2-1-1-summary
"""

EXAMPLES = r"""
"""

RETURN = r"""
data_0:
    description: Returns list of available namespaces.
    returned: success,changed,always
    type: dict
    contains:
        response:
            description: Response, property of the response body (list of strings).
            returned: success,changed,always
            type: list
        version:
            description: Version, property of the response body.
            returned: success,changed,always
            type: str
            sample: '1.0'

data_1:
    description: Returns list of files under a specific namespace.
    returned: success,changed,always
    type: dict
    contains:
        response:
            description: Response, property of the response body (list of objects).
            returned: success,changed,always
            type: list
            contains:
                attributeInfo:
                    description: It is the file namespace's attributeInfo.
                    returned: success,changed,always
                    type: dict
                downloadPath:
                    description: It is the file namespace's downloadPath.
                    returned: success,changed,always
                    type: str
                    sample: '<downloadpath>'
                encrypted:
                    description: It is the file namespace's encrypted.
                    returned: success,changed,always
                    type: bool
                    sample: false
                fileFormat:
                    description: It is the file namespace's fileFormat.
                    returned: success,changed,always
                    type: str
                    sample: '<fileformat>'
                fileSize:
                    description: It is the file namespace's fileSize.
                    returned: success,changed,always
                    type: str
                    sample: '<filesize>'
                id:
                    description: It is the file namespace's id.
                    returned: success,changed,always
                    type: str
                    sample: '478012'
                md5Checksum:
                    description: It is the file namespace's md5Checksum.
                    returned: success,changed,always
                    type: str
                    sample: '<md5checksum>'
                name:
                    description: It is the file namespace's name.
                    returned: success,changed,always
                    type: str
                    sample: '<name>'
                nameSpace:
                    description: It is the file namespace's nameSpace.
                    returned: success,changed,always
                    type: str
                    sample: '<namespace>'
                sftpServerList:
                    description: It is the file namespace's sftpServerList.
                    returned: success,changed,always
                    type: list
                sha1Checksum:
                    description: It is the file namespace's sha1Checksum.
                    returned: success,changed,always
                    type: str
                    sample: '<sha1checksum>'
                taskId:
                    description: It is the file namespace's taskId.
                    returned: success,changed,always
                    type: dict

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
from ansible_collections.cisco.dnac.plugins.module_utils.definitions.file_namespace import (
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
