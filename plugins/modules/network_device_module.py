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
    required: True
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
"""

EXAMPLES = r"""
- name: get_modules
  cisco.dnac.network_device_module
    dnac_host: dnac
    dnac_username: admin
    dnac_password: SomeSecretPassword
    state: query  # required
    device_id: SomeValue  # string, required
    limit: SomeValue  # string
    name_list: SomeValue  # string
    offset: SomeValue  # string
    operational_state_code_list: SomeValue  # string
    part_number_list: SomeValue  # string
    vendor_equipment_type_list: SomeValue  # string
  delegate_to: localhost
  register: query_result
  
- name: get_module_info_by_id
  cisco.dnac.network_device_module
    dnac_host: dnac
    dnac_username: admin
    dnac_password: SomeSecretPassword
    state: query  # required
    id: SomeValue  # string, required
  delegate_to: localhost
  register: query_result
  
- name: get_module_count
  cisco.dnac.network_device_module
    dnac_host: dnac
    dnac_username: admin
    dnac_password: SomeSecretPassword
    state: query  # required
    device_id: SomeValue  # string, required
    count: True  # boolean, required
    name_list: SomeValue  # string
    operational_state_code_list: SomeValue  # string
    part_number_list: SomeValue  # string
    vendor_equipment_type_list: SomeValue  # string
  delegate_to: localhost
  register: query_result
  
"""

RETURN = """
get_modules:
    description: Returns modules by specified device id.
    returned: always
    type: dict
    contains:
    response:
      description: Response, property of the response body (list of objects).
      returned: always
      type: list
      contains:
        assemblyNumber:
          description: It is the network device module's assemblyNumber.
          returned: always
          type: str
          sample: '<assemblynumber>'
        assemblyRevision:
          description: It is the network device module's assemblyRevision.
          returned: always
          type: str
          sample: '<assemblyrevision>'
        attributeInfo:
          description: It is the network device module's attributeInfo.
          returned: always
          type: dict
        containmentEntity:
          description: It is the network device module's containmentEntity.
          returned: always
          type: str
          sample: '<containmententity>'
        description:
          description: It is the network device module's description.
          returned: always
          type: str
          sample: '<description>'
        entityPhysicalIndex:
          description: It is the network device module's entityPhysicalIndex.
          returned: always
          type: str
          sample: '<entityphysicalindex>'
        id:
          description: It is the network device module's id.
          returned: always
          type: str
          sample: '478012'
        isFieldReplaceable:
          description: It is the network device module's isFieldReplaceable.
          returned: always
          type: str
          sample: '<isfieldreplaceable>'
        isReportingAlarmsAllowed:
          description: It is the network device module's isReportingAlarmsAllowed.
          returned: always
          type: str
          sample: '<isreportingalarmsallowed>'
        manufacturer:
          description: It is the network device module's manufacturer.
          returned: always
          type: str
          sample: '<manufacturer>'
        moduleIndex:
          description: It is the network device module's moduleIndex.
          returned: always
          type: int
          sample: 0
        name:
          description: It is the network device module's name.
          returned: always
          type: str
          sample: '<name>'
        operationalStateCode:
          description: It is the network device module's operationalStateCode.
          returned: always
          type: str
          sample: '<operationalstatecode>'
        partNumber:
          description: It is the network device module's partNumber.
          returned: always
          type: str
          sample: '<partnumber>'
        serialNumber:
          description: It is the network device module's serialNumber.
          returned: always
          type: str
          sample: '<serialnumber>'
        vendorEquipmentType:
          description: It is the network device module's vendorEquipmentType.
          returned: always
          type: str
          sample: '<vendorequipmenttype>'

    version:
      description: Version, property of the response body.
      returned: always
      type: str
      sample: '1.0'

get_module_info_by_id:
    description: Returns Module info by id.
    returned: always
    type: dict
    contains:
    response:
      description: Response, property of the response body.
      returned: always
      type: dict
      contains:
        assemblyNumber:
          description: It is the network device module's assemblyNumber.
          returned: always
          type: str
          sample: '<assemblynumber>'
        assemblyRevision:
          description: It is the network device module's assemblyRevision.
          returned: always
          type: str
          sample: '<assemblyrevision>'
        attributeInfo:
          description: It is the network device module's attributeInfo.
          returned: always
          type: dict
        containmentEntity:
          description: It is the network device module's containmentEntity.
          returned: always
          type: str
          sample: '<containmententity>'
        description:
          description: It is the network device module's description.
          returned: always
          type: str
          sample: '<description>'
        entityPhysicalIndex:
          description: It is the network device module's entityPhysicalIndex.
          returned: always
          type: str
          sample: '<entityphysicalindex>'
        id:
          description: It is the network device module's id.
          returned: always
          type: str
          sample: '478012'
        isFieldReplaceable:
          description: It is the network device module's isFieldReplaceable.
          returned: always
          type: str
          sample: '<isfieldreplaceable>'
        isReportingAlarmsAllowed:
          description: It is the network device module's isReportingAlarmsAllowed.
          returned: always
          type: str
          sample: '<isreportingalarmsallowed>'
        manufacturer:
          description: It is the network device module's manufacturer.
          returned: always
          type: str
          sample: '<manufacturer>'
        moduleIndex:
          description: It is the network device module's moduleIndex.
          returned: always
          type: int
          sample: 0
        name:
          description: It is the network device module's name.
          returned: always
          type: str
          sample: '<name>'
        operationalStateCode:
          description: It is the network device module's operationalStateCode.
          returned: always
          type: str
          sample: '<operationalstatecode>'
        partNumber:
          description: It is the network device module's partNumber.
          returned: always
          type: str
          sample: '<partnumber>'
        serialNumber:
          description: It is the network device module's serialNumber.
          returned: always
          type: str
          sample: '<serialnumber>'
        vendorEquipmentType:
          description: It is the network device module's vendorEquipmentType.
          returned: always
          type: str
          sample: '<vendorequipmenttype>'

    version:
      description: Version, property of the response body.
      returned: always
      type: str
      sample: '1.0'

get_module_count:
    description: Returns Module Count.
    returned: always
    type: dict
    contains:
    response:
      description: Response, property of the response body.
      returned: always
      type: int
      sample: 0
    version:
      description: Version, property of the response body.
      returned: always
      type: str
      sample: '1.0'

"""
