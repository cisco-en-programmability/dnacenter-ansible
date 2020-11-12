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
module: client_health
short_description: Manage ClientHealth objects of Clients
description:
- Returns Overall Client Health information by Client type (Wired and Wireless) for any given point of time.
version_added: '1.0'
author: first last (@GitHubID)
options:
    timestamp:
        description:
        - Epoch time(in milliseconds) when the Client health data is required.
        type: int

requirements:
- dnacentersdk
seealso:
# Reference by module name
- module: cisco.dnac.plugins.module_utils.definitions.client_health
# Reference by Internet resource
- name: ClientHealth reference
  description: Complete reference of the ClientHealth object model.
  link: https://developer.cisco.com/docs/dna-center/api/1-3-3-x
# Reference by Internet resource
- name: ClientHealth reference
  description: SDK reference.
  link: https://dnacentersdk.readthedocs.io/en/latest/api/api.html#v2-1-1-summary
"""

EXAMPLES = r"""
"""

RETURN = r"""
data_0:
    description: Returns Overall Client Health information by Client type (Wired and Wireless) for any given point of time.
    returned: success,changed,always
    type: dict
    contains:
        response:
            description: Response, property of the response body (list of objects).
            returned: success,changed,always
            type: list
            contains:
                siteId:
                    description: It is the client health's siteId.
                    returned: success,changed,always
                    type: str
                    sample: '<siteid>'
                scoreDetail:
                    description: It is the client health's scoreDetail.
                    returned: success,changed,always
                    type: list
                    contains:
                        scoreCategory:
                            description: It is the client health's scoreCategory.
                            returned: success,changed,always
                            type: dict
                            contains:
                                scoreCategory:
                                    description: It is the client health's scoreCategory.
                                    returned: success,changed,always
                                    type: str
                                    sample: '<scorecategory>'
                                value:
                                    description: It is the client health's value.
                                    returned: success,changed,always
                                    type: str
                                    sample: '<value>'

                        scoreValue:
                            description: It is the client health's scoreValue.
                            returned: success,changed,always
                            type: int
                            sample: 0
                        clientCount:
                            description: It is the client health's clientCount.
                            returned: success,changed,always
                            type: int
                            sample: 0
                        clientUniqueCount:
                            description: It is the client health's clientUniqueCount.
                            returned: success,changed,always
                            type: int
                            sample: 0
                        starttime:
                            description: It is the client health's starttime.
                            returned: success,changed,always
                            type: int
                            sample: 0
                        endtime:
                            description: It is the client health's endtime.
                            returned: success,changed,always
                            type: int
                            sample: 0
                        scoreList:
                            description: It is the client health's scoreList.
                            returned: success,changed,always
                            type: list
                            contains:
                                scoreCategory:
                                    description: It is the client health's scoreCategory.
                                    returned: success,changed,always
                                    type: dict
                                    contains:
                                        scoreCategory:
                                            description: It is the client health's scoreCategory.
                                            returned: success,changed,always
                                            type: str
                                            sample: '<scorecategory>'
                                        value:
                                            description: It is the client health's value.
                                            returned: success,changed,always
                                            type: str
                                            sample: '<value>'

                                scoreValue:
                                    description: It is the client health's scoreValue.
                                    returned: success,changed,always
                                    type: int
                                    sample: 0
                                clientCount:
                                    description: It is the client health's clientCount.
                                    returned: success,changed,always
                                    type: int
                                    sample: 0
                                clientUniqueCount:
                                    description: It is the client health's clientUniqueCount.
                                    returned: success,changed,always
                                    type: int
                                    sample: 0
                                starttime:
                                    description: It is the client health's starttime.
                                    returned: success,changed,always
                                    type: int
                                    sample: 0
                                endtime:
                                    description: It is the client health's endtime.
                                    returned: success,changed,always
                                    type: int
                                    sample: 0
                                scoreList:
                                    description: It is the client health's scoreList.
                                    returned: success,changed,always
                                    type: list
                                    contains:
                                        scoreCategory:
                                            description: It is the client health's scoreCategory.
                                            returned: success,changed,always
                                            type: dict
                                            contains:
                                                scoreCategory:
                                                    description: It is the client health's scoreCategory.
                                                    returned: success,changed,always
                                                    type: str
                                                    sample: '<scorecategory>'
                                                value:
                                                    description: It is the client health's value.
                                                    returned: success,changed,always
                                                    type: str
                                                    sample: '<value>'

                                        scoreValue:
                                            description: It is the client health's scoreValue.
                                            returned: success,changed,always
                                            type: int
                                            sample: 0
                                        clientCount:
                                            description: It is the client health's clientCount.
                                            returned: success,changed,always
                                            type: int
                                            sample: 0
                                        clientUniqueCount:
                                            description: It is the client health's clientUniqueCount.
                                            returned: success,changed,always
                                            type: dict
                                        starttime:
                                            description: It is the client health's starttime.
                                            returned: success,changed,always
                                            type: int
                                            sample: 0
                                        endtime:
                                            description: It is the client health's endtime.
                                            returned: success,changed,always
                                            type: int
                                            sample: 0





"""

from ansible.module_utils.basic import AnsibleModule
from ansible_collections.cisco.dnac.plugins.module_utils.dnac import (
    ModuleDefinition,
    DNACModule,
    dnac_argument_spec,
)
from ansible_collections.cisco.dnac.plugins.module_utils.definitions.client_health import (
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
