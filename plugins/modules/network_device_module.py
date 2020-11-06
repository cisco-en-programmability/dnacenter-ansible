#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright: (c) 2020, first last <email>
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

ANSIBLE_METADATA = {
    'metadata_version': '0.0.1',
    'status': ['preview'],
    'supported_by': 'community'
}

DOCUMENTATION = r'''
---
module: network_device_module
short_description: Manage NetworkDeviceModule objects of Devices
description:
- Returns modules by specified device id.
- Returns Module info by id.
- Returns Module Count.
version_added: '1.0'
author: first last (@GitHubID)
options:
    device_id:
        description:
        - DeviceId query parameter.
        type: str
    limit:
        description:
        - Limit query parameter.
        type: str
    name_list:
        description:
        - NameList query parameter.
        type: str
    offset:
        description:
        - Offset query parameter.
        type: str
    operational_state_code_list:
        description:
        - OperationalStateCodeList query parameter.
        type: str
    part_number_list:
        description:
        - PartNumberList query parameter.
        type: str
    vendor_equipment_type_list:
        description:
        - VendorEquipmentTypeList query parameter.
        type: str
    id:
        description:
        - Id path parameter.
        type: str
        required: True
    count:
        description:
        - If true gets the number of objects.
        type: bool
        required: True

requirements:
- dnacentersdk
seealso:
# Reference by module name
- module: cisco.dnac.plugins.module_utils.definitions.network_device_module
# Reference by Internet resource
- name: NetworkDeviceModule reference
  description: Complete reference of the NetworkDeviceModule object model.
  link: https://developer.cisco.com/docs/dna-center/api/1-3-3-x
# Reference by Internet resource
- name: NetworkDeviceModule reference
  description: SDK reference.
  link: https://dnacentersdk.readthedocs.io/en/latest/api/api.html#v2-1-1-summary
'''

EXAMPLES = r'''
'''

RETURN = r'''
data_0:
    description: Returns modules by specified device id.
    returned: success,changed,always
    type: dict
    contains:
        response:
            description: Response, property of the response body (list of objects).
            returned: success,changed,always
            type: list
            contains:
                assemblyNumber:
                    description: It is the network device module's assemblyNumber.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                assemblyRevision:
                    description: It is the network device module's assemblyRevision.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                attributeInfo:
                    description: It is the network device module's attributeInfo.
                    returned: success,changed,always
                    type: dict
                containmentEntity:
                    description: It is the network device module's containmentEntity.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                description:
                    description: It is the network device module's description.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                entityPhysicalIndex:
                    description: It is the network device module's entityPhysicalIndex.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                id:
                    description: It is the network device module's id.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                isFieldReplaceable:
                    description: It is the network device module's isFieldReplaceable.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                isReportingAlarmsAllowed:
                    description: It is the network device module's isReportingAlarmsAllowed.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                manufacturer:
                    description: It is the network device module's manufacturer.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                moduleIndex:
                    description: It is the network device module's moduleIndex.
                    returned: success,changed,always
                    type: int
                    sample: 0
                name:
                    description: It is the network device module's name.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                operationalStateCode:
                    description: It is the network device module's operationalStateCode.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                partNumber:
                    description: It is the network device module's partNumber.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                serialNumber:
                    description: It is the network device module's serialNumber.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                vendorEquipmentType:
                    description: It is the network device module's vendorEquipmentType.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'

        version:
            description: Version, property of the response body.
            returned: success,changed,always
            type: str
            sample: 'sample_string'

data_1:
    description: Returns Module info by id.
    returned: success,changed,always
    type: dict
    contains:
        response:
            description: Response, property of the response body.
            returned: success,changed,always
            type: dict
            contains:
                assemblyNumber:
                    description: It is the network device module's assemblyNumber.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                assemblyRevision:
                    description: It is the network device module's assemblyRevision.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                attributeInfo:
                    description: It is the network device module's attributeInfo.
                    returned: success,changed,always
                    type: dict
                containmentEntity:
                    description: It is the network device module's containmentEntity.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                description:
                    description: It is the network device module's description.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                entityPhysicalIndex:
                    description: It is the network device module's entityPhysicalIndex.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                id:
                    description: It is the network device module's id.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                isFieldReplaceable:
                    description: It is the network device module's isFieldReplaceable.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                isReportingAlarmsAllowed:
                    description: It is the network device module's isReportingAlarmsAllowed.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                manufacturer:
                    description: It is the network device module's manufacturer.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                moduleIndex:
                    description: It is the network device module's moduleIndex.
                    returned: success,changed,always
                    type: int
                    sample: 0
                name:
                    description: It is the network device module's name.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                operationalStateCode:
                    description: It is the network device module's operationalStateCode.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                partNumber:
                    description: It is the network device module's partNumber.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                serialNumber:
                    description: It is the network device module's serialNumber.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                vendorEquipmentType:
                    description: It is the network device module's vendorEquipmentType.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'

        version:
            description: Version, property of the response body.
            returned: success,changed,always
            type: str
            sample: 'sample_string'

data_2:
    description: Returns Module Count.
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
            sample: 'sample_string'

'''

from ansible.module_utils.basic import AnsibleModule
from ansible_collections.cisco.dnac.plugins.module_utils.dnac import ModuleDefinition, DNACModule, dnac_argument_spec
from ansible_collections.cisco.dnac.plugins.module_utils.definitions.network_device_module import module_definition


def main():

    moddef = ModuleDefinition(module_definition)

    argument_spec = dnac_argument_spec()
    argument_spec.update(moddef.get_argument_spec_dict())

    required_if = moddef.get_required_if_list()
    
    module = AnsibleModule(
        argument_spec=argument_spec,
        supports_check_mode=False,
        required_if=required_if
    )

    dnac = DNACModule(module, moddef)

    state = module.params.get("state")

    if state == "query":
        dnac.exec("get")

    dnac.exit_json()


if __name__ == "__main__":
    main()