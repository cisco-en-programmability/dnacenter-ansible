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
module: device_replacement
short_description: Manage DeviceReplacement objects of DeviceReplacement
description:
- Get list of replacement devices with replacement details and it can filter replacement devices based on Faulty Device Name,Faulty Device Platform, Replacement Device Platform, Faulty Device Serial Number,Replacement Device Serial Number, Device Replacement status, Product Family.
- Marks device for replacement.
- UnMarks device for replacement.
- Get replacement devices count.
version_added: '1.0'
author: first last (@GitHubID)
options:
    family:
        description:
        - List of families[Routers, Switches and Hubs, AP].
        type: str
    faulty_device_name:
        description:
        - Faulty Device Name.
        type: str
    faulty_device_platform:
        description:
        - Faulty Device Platform.
        type: str
    faulty_device_serial_number:
        description:
        - Faulty Device Serial Number.
        type: str
    limit:
        description:
        - Limit query parameter.
        type: int
    offset:
        description:
        - Offset query parameter.
        type: int
    replacement_device_platform:
        description:
        - Replacement Device Platform.
        type: str
    replacement_device_serial_number:
        description:
        - Replacement Device Serial Number.
        type: str
    replacement_status:
        description:
        - Device Replacement status [READY-FOR-REPLACEMENT, REPLACEMENT-IN-PROGRESS, REPLACEMENT-SCHEDULED, REPLACED, ERROR, NETWORK_READINESS_REQUESTED, NETWORK_READINESS_FAILED].
        type: str
    sort_by:
        description:
        - SortBy this field. SortBy is mandatory when order is used.
        type: str
    sort_order:
        description:
        - Order on displayName[ASC,DESC].
        type: str
    payload:
        description:
        - An object to send in the Request body.
        type: list
        required: True
        elements: dict
        suboptions:
            creationTime:
                description:
                - It is the device replacement's creationTime.
                type: int
            family:
                description:
                - It is the device replacement's family.
                type: str
            faultyDeviceId:
                description:
                - It is the device replacement's faultyDeviceId.
                type: str
                required: True
            faultyDeviceName:
                description:
                - It is the device replacement's faultyDeviceName.
                type: str
            faultyDevicePlatform:
                description:
                - It is the device replacement's faultyDevicePlatform.
                type: str
            faultyDeviceSerialNumber:
                description:
                - It is the device replacement's faultyDeviceSerialNumber.
                type: str
            id:
                description:
                - It is the device replacement's id.
                type: str
            neighbourDeviceId:
                description:
                - It is the device replacement's neighbourDeviceId.
                type: str
            networkReadinessTaskId:
                description:
                - It is the device replacement's networkReadinessTaskId.
                type: str
            replacementDevicePlatform:
                description:
                - It is the device replacement's replacementDevicePlatform.
                type: str
            replacementDeviceSerialNumber:
                description:
                - It is the device replacement's replacementDeviceSerialNumber.
                type: str
            replacementStatus:
                description:
                - It is the device replacement's replacementStatus.
                type: str
                required: True
            replacementTime:
                description:
                - It is the device replacement's replacementTime.
                type: int
            workflowId:
                description:
                - It is the device replacement's workflowId.
                type: str

    count:
        description:
        - If true gets the number of objects.
        type: bool
        required: True

requirements:
- dnacentersdk
seealso:
# Reference by module name
- module: cisco.dnac.plugins.module_utils.definitions.device_replacement
# Reference by Internet resource
- name: DeviceReplacement reference
  description: Complete reference of the DeviceReplacement object model.
  link: https://developer.cisco.com/docs/dna-center/api/1-3-3-x
# Reference by Internet resource
- name: DeviceReplacement reference
  description: SDK reference.
  link: https://dnacentersdk.readthedocs.io/en/latest/api/api.html#v2-1-1-summary
"""

EXAMPLES = r"""
"""

RETURN = r"""
data_0:
    description: Get list of replacement devices with replacement details and it can filter replacement devices based on Faulty Device Name,Faulty Device Platform, Replacement Device Platform, Faulty Device Serial Number,Replacement Device Serial Number, Device Replacement status, Product Family.
    returned: success,changed,always
    type: dict
    contains:
        response:
            description: Response, property of the response body (list of objects).
            returned: success,changed,always
            type: list
            contains:
                creationTime:
                    description: It is the device replacement's creationTime.
                    returned: success,changed,always
                    type: int
                    sample: 0
                family:
                    description: It is the device replacement's family.
                    returned: success,changed,always
                    type: str
                    sample: '<family>'
                faultyDeviceId:
                    description: It is the device replacement's faultyDeviceId.
                    returned: success,changed,always
                    type: str
                    sample: '<faultydeviceid>'
                faultyDeviceName:
                    description: It is the device replacement's faultyDeviceName.
                    returned: success,changed,always
                    type: str
                    sample: '<faultydevicename>'
                faultyDevicePlatform:
                    description: It is the device replacement's faultyDevicePlatform.
                    returned: success,changed,always
                    type: str
                    sample: '<faultydeviceplatform>'
                faultyDeviceSerialNumber:
                    description: It is the device replacement's faultyDeviceSerialNumber.
                    returned: success,changed,always
                    type: str
                    sample: '<faultydeviceserialnumber>'
                id:
                    description: It is the device replacement's id.
                    returned: success,changed,always
                    type: str
                    sample: '478012'
                neighbourDeviceId:
                    description: It is the device replacement's neighbourDeviceId.
                    returned: success,changed,always
                    type: str
                    sample: '<neighbourdeviceid>'
                networkReadinessTaskId:
                    description: It is the device replacement's networkReadinessTaskId.
                    returned: success,changed,always
                    type: str
                    sample: '<networkreadinesstaskid>'
                replacementDevicePlatform:
                    description: It is the device replacement's replacementDevicePlatform.
                    returned: success,changed,always
                    type: str
                    sample: '<replacementdeviceplatform>'
                replacementDeviceSerialNumber:
                    description: It is the device replacement's replacementDeviceSerialNumber.
                    returned: success,changed,always
                    type: str
                    sample: '<replacementdeviceserialnumber>'
                replacementStatus:
                    description: It is the device replacement's replacementStatus.
                    returned: success,changed,always
                    type: str
                    sample: '<replacementstatus>'
                replacementTime:
                    description: It is the device replacement's replacementTime.
                    returned: success,changed,always
                    type: int
                    sample: 0
                workflowId:
                    description: It is the device replacement's workflowId.
                    returned: success,changed,always
                    type: str
                    sample: '<workflowid>'

        version:
            description: Version, property of the response body.
            returned: success,changed,always
            type: str
            sample: '1.0'

data_1:
    description: Marks device for replacement.
    returned: success,changed,always
    type: dict
    contains:
        response:
            description: DeviceReplacementDataDTO's response.
            returned: success,changed,always
            type: dict
            contains:
                taskId:
                    description: It is the device replacement's taskId.
                    returned: success,changed,always
                    type: dict
                url:
                    description: It is the device replacement's url.
                    returned: success,changed,always
                    type: str
                    sample: '<url>'

        version:
            description: DeviceReplacementDataDTO's version.
            returned: success,changed,always
            type: str
            sample: '1.0'

data_2:
    description: UnMarks device for replacement.
    returned: success,changed,always
    type: dict
    contains:
        response:
            description: DeviceReplacementDataDTO's response.
            returned: success,changed,always
            type: dict
            contains:
                taskId:
                    description: It is the device replacement's taskId.
                    returned: success,changed,always
                    type: dict
                url:
                    description: It is the device replacement's url.
                    returned: success,changed,always
                    type: str
                    sample: '<url>'

        version:
            description: DeviceReplacementDataDTO's version.
            returned: success,changed,always
            type: str
            sample: '1.0'

data_3:
    description: Get replacement devices count.
    returned: success,changed,always
    type: dict
    contains:
        response:
            description: Response, property of the response body.
            returned: success,changed,always
            type: int
            sample: 0
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
from ansible_collections.cisco.dnac.plugins.module_utils.definitions.device_replacement import (
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

    elif state == "create":
        dnac.disable_validation()
        dnac.exec("post")

    elif state == "update":
        dnac.disable_validation()
        dnac.exec("put")

    dnac.exit_json()


if __name__ == "__main__":
    main()
