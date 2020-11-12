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
module: wireless_ap_provision
short_description: Manage WirelessApProvision objects of Wireless
description:
- Access Point Provision and ReProvision.
version_added: '1.0'
author: first last (@GitHubID)
options:
    payload:
        description:
        - An object to send in the Request body.
        type: list
        required: True
        elements: dict
        suboptions:
            executionId:
                description:
                - It is the wireless ap provision's executionId.
                type: str
            executionUrl:
                description:
                - It is the wireless ap provision's executionUrl.
                type: str
            message:
                description:
                - It is the wireless ap provision's message.
                type: str


requirements:
- dnacentersdk
seealso:
# Reference by module name
- module: cisco.dnac.plugins.module_utils.definitions.wireless_ap_provision
# Reference by Internet resource
- name: WirelessApProvision reference
  description: Complete reference of the WirelessApProvision object model.
  link: https://developer.cisco.com/docs/dna-center/api/1-3-3-x
# Reference by Internet resource
- name: WirelessApProvision reference
  description: SDK reference.
  link: https://dnacentersdk.readthedocs.io/en/latest/api/api.html#v2-1-1-summary
"""

EXAMPLES = r"""
"""

RETURN = r"""
data_0:
    description: Access Point Provision and ReProvision.
    returned: success,changed,always
    type: dict
    contains:
        executionId:
            description: Execution Id, property of the response body.
            returned: success,changed,always
            type: str
            sample: '<executionid>'
        executionUrl:
            description: Execution Url, property of the response body.
            returned: success,changed,always
            type: str
            sample: '<executionurl>'
        provisionTasks:
            description: Provision Tasks, property of the response body.
            returned: success,changed,always
            type: dict
            contains:
                success:
                    description: It is the wireless ap provision's success.
                    returned: success,changed,always
                    type: list
                    contains:
                        taskId:
                            description: It is the wireless ap provision's taskId.
                            returned: success,changed,always
                            type: str
                            sample: 'aeed229047801200e0ef563dbb9a71c2'
                        taskUrl:
                            description: It is the wireless ap provision's taskUrl.
                            returned: success,changed,always
                            type: str
                            sample: '<taskurl>'

                failure:
                    description: It is the wireless ap provision's failure.
                    returned: success,changed,always
                    type: dict
                    contains:
                        taskId:
                            description: It is the wireless ap provision's taskId.
                            returned: success,changed,always
                            type: str
                            sample: 'aeed229047801200e0ef563dbb9a71c2'
                        taskUrl:
                            description: It is the wireless ap provision's taskUrl.
                            returned: success,changed,always
                            type: str
                            sample: '<taskurl>'
                        failureReason:
                            description: It is the wireless ap provision's failureReason.
                            returned: success,changed,always
                            type: str
                            sample: '<failurereason>'



"""

from ansible.module_utils.basic import AnsibleModule
from ansible_collections.cisco.dnac.plugins.module_utils.dnac import (
    ModuleDefinition,
    DNACModule,
    dnac_argument_spec,
)
from ansible_collections.cisco.dnac.plugins.module_utils.definitions.wireless_ap_provision import (
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
