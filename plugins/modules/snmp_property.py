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
module: snmp_property
short_description: Manage SnmpProperty objects of Discovery
description:
- Returns SNMP properties.
- Adds SNMP properties.
version_added: '1.0'
author: first last (@GitHubID)
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
  cisco.dnac.snmp_property
    dnac_host: dnac
    dnac_username: admin
    dnac_password: SomeSecretPassword
    state: query  # required

  delegate_to: localhost
  register: query_result
  
- name: create_update_snmp_properties
  cisco.dnac.snmp_property
    dnac_host: dnac
    dnac_username: admin
    dnac_password: SomeSecretPassword
    state: create  # required
    payload:  # required
    - id: SomeValue  # string
      instanceTenantId: SomeValue  # string
      instanceUuid: SomeValue  # string
      intValue: 1  #  integer
      systemPropertyName: SomeValue  # string
  delegate_to: localhost
  
"""

RETURN = """
get_snmp_properties:
    description: Returns SNMP properties.
    returned: always
    type: dict
    contains:
    response:
      description: Response, property of the response body (list of objects).
      returned: always
      type: list
      contains:
        id:
          description: It is the snmp property's id.
          returned: always
          type: str
          sample: '478012'
        instanceTenantId:
          description: It is the snmp property's instanceTenantId.
          returned: always
          type: str
          sample: '<instancetenantid>'
        instanceUuid:
          description: It is the snmp property's instanceUuid.
          returned: always
          type: str
          sample: '<instanceuuid>'
        intValue:
          description: It is the snmp property's intValue.
          returned: always
          type: int
          sample: 0
        systemPropertyName:
          description: It is the snmp property's systemPropertyName.
          returned: always
          type: str
          sample: '<systempropertyname>'

    version:
      description: Version, property of the response body.
      returned: always
      type: str
      sample: '1.0'

create_update_snmp_properties:
    description: Adds SNMP properties.
    returned: success
    type: dict
    contains:
    response:
      description: SystemPropertyNameAndIntValueDTO's response.
      returned: success
      type: dict
      contains:
        taskId:
          description: It is the snmp property's taskId.
          returned: success
          type: dict
        url:
          description: It is the snmp property's url.
          returned: success
          type: str
          sample: '<url>'

    version:
      description: SystemPropertyNameAndIntValueDTO's version.
      returned: success
      type: str
      sample: '1.0'

"""
