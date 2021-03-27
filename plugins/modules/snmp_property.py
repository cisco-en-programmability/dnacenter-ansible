#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright: (c) 2020, Rafael Campos <rcampos@altus.cr>
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

ANSIBLE_METADATA = {
    "metadata_version": "0.0.1",
    "status": ["preview"],
    "supported_by": "community",
}

DOCUMENTATION = r"""
---
module: snmp_property
short_description: Manage SnmpProperty objects of Discovery
description:
- Returns SNMP properties.
- Adds SNMP properties.
version_added: '1.0.0'
author: Rafael Campos (@racampos)
options:
  payload:
    description:
    - An object to send in the Request body.
    - Required for state create.
    type: list
    elements: dict
    suboptions:
      id:
        description:
        - It is the snmp property's id.
        type: str
      instanceTenantId:
        description:
        - It is the snmp property's instanceTenantId.
        type: str
      instanceUuid:
        description:
        - It is the snmp property's instanceUuid.
        type: str
      intValue:
        description:
        - It is the snmp property's intValue.
        type: int
      systemPropertyName:
        description:
        - It is the snmp property's systemPropertyName.
        type: str


requirements:
- dnacentersdk
seealso:
# Reference by module name
- module: cisco.dnac.plugins.module_utils.definitions.snmp_property
# Reference by Internet resource
- name: SnmpProperty reference
  description: Complete reference of the SnmpProperty object model.
  link: https://developer.cisco.com/docs/dna-center/api/1-3-3-x
# Reference by Internet resource
- name: SnmpProperty reference
  description: SDK reference.
  link: https://dnacentersdk.readthedocs.io/en/latest/api/api.html#v2-1-1-summary
"""

EXAMPLES = r"""
- name: get_snmp_properties
  cisco.dnac.snmp_property:
    state: query  # required

  register: query_result
  
- name: create_update_snmp_properties
  cisco.dnac.snmp_property:
    state: create  # required
    payload:  # required
    - id: SomeValue  # string
      instanceTenantId: SomeValue  # string
      instanceUuid: SomeValue  # string
      intValue: 1  #  integer
      systemPropertyName: SomeValue  # string
  
"""

RETURN = """
"""
