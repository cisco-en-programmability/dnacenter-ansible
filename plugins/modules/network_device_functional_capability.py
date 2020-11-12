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
module: network_device_functional_capability
short_description: Manage NetworkDeviceFunctionalCapability objects of Devices
description:
- Returns the functional-capability for given devices.
- Returns functional capability with given Id.
version_added: '1.0'
author: first last (@GitHubID)
options:
    device_id:
        description:
        - Accepts comma separated deviceid's and return list of functional-capabilities for the given id's. If invalid or not-found id's are provided, null entry will be returned in the list.
        type: str
    function_name:
        description:
        - FunctionName query parameter.
        type: str
    id:
        description:
        - Functional Capability UUID.
        type: str
        required: True

requirements:
- dnacentersdk
seealso:
# Reference by module name
- module: cisco.dnac.plugins.module_utils.definitions.network_device_functional_capability
# Reference by Internet resource
- name: NetworkDeviceFunctionalCapability reference
  description: Complete reference of the NetworkDeviceFunctionalCapability object model.
  link: https://developer.cisco.com/docs/dna-center/api/1-3-3-x
# Reference by Internet resource
- name: NetworkDeviceFunctionalCapability reference
  description: SDK reference.
  link: https://dnacentersdk.readthedocs.io/en/latest/api/api.html#v2-1-1-summary
"""

EXAMPLES = r"""
"""

RETURN = r"""
data_0:
    description: Returns the functional-capability for given devices.
    returned: success,changed,always
    type: dict
    contains:
        response:
            description: Response, property of the response body (list of objects).
            returned: success,changed,always
            type: list
            contains:
                attributeInfo:
                    description: It is the network device functional capability's attributeInfo.
                    returned: success,changed,always
                    type: dict
                deviceId:
                    description: It is the network device functional capability's deviceId.
                    returned: success,changed,always
                    type: str
                    sample: '<deviceid>'
                functionalCapability:
                    description: It is the network device functional capability's functionalCapability.
                    returned: success,changed,always
                    type: list
                    contains:
                        attributeInfo:
                            description: It is the network device functional capability's attributeInfo.
                            returned: success,changed,always
                            type: dict
                        functionDetails:
                            description: It is the network device functional capability's functionDetails.
                            returned: success,changed,always
                            type: list
                            contains:
                                attributeInfo:
                                    description: It is the network device functional capability's attributeInfo.
                                    returned: success,changed,always
                                    type: dict
                                id:
                                    description: It is the network device functional capability's id.
                                    returned: success,changed,always
                                    type: str
                                    sample: '478012'
                                propertyName:
                                    description: It is the network device functional capability's propertyName.
                                    returned: success,changed,always
                                    type: str
                                    sample: '<propertyname>'
                                stringValue:
                                    description: It is the network device functional capability's stringValue.
                                    returned: success,changed,always
                                    type: str
                                    sample: '<stringvalue>'

                        functionName:
                            description: It is the network device functional capability's functionName.
                            returned: success,changed,always
                            type: str
                            sample: '<functionname>'
                        functionOpState:
                            description: It is the network device functional capability's functionOpState.
                            returned: success,changed,always
                            type: str
                            sample: '<functionopstate>'
                        id:
                            description: It is the network device functional capability's id.
                            returned: success,changed,always
                            type: str
                            sample: '478012'

                id:
                    description: It is the network device functional capability's id.
                    returned: success,changed,always
                    type: str
                    sample: '478012'

        version:
            description: Version, property of the response body.
            returned: success,changed,always
            type: str
            sample: '1.0'

data_1:
    description: Returns functional capability with given Id.
    returned: success,changed,always
    type: dict
    contains:
        response:
            description: Response, property of the response body.
            returned: success,changed,always
            type: dict
            contains:
                attributeInfo:
                    description: It is the network device functional capability's attributeInfo.
                    returned: success,changed,always
                    type: dict
                functionDetails:
                    description: It is the network device functional capability's functionDetails.
                    returned: success,changed,always
                    type: list
                    contains:
                        attributeInfo:
                            description: It is the network device functional capability's attributeInfo.
                            returned: success,changed,always
                            type: dict
                        id:
                            description: It is the network device functional capability's id.
                            returned: success,changed,always
                            type: str
                            sample: '478012'
                        propertyName:
                            description: It is the network device functional capability's propertyName.
                            returned: success,changed,always
                            type: str
                            sample: '<propertyname>'
                        stringValue:
                            description: It is the network device functional capability's stringValue.
                            returned: success,changed,always
                            type: str
                            sample: '<stringvalue>'

                functionName:
                    description: It is the network device functional capability's functionName.
                    returned: success,changed,always
                    type: str
                    sample: '<functionname>'
                functionOpState:
                    description: It is the network device functional capability's functionOpState.
                    returned: success,changed,always
                    type: str
                    sample: '<functionopstate>'
                id:
                    description: It is the network device functional capability's id.
                    returned: success,changed,always
                    type: str
                    sample: '478012'

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
from ansible_collections.cisco.dnac.plugins.module_utils.definitions.network_device_functional_capability import (
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
