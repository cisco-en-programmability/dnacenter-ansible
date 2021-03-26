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
module: global_credential_snmpv2_write_community
short_description: Manage GlobalCredentialSnmpv2WriteCommunity objects of Discovery
description:
- Adds global SNMP write community.
- Updates global SNMP write community.
version_added: '1.0'
author: Rafael Campos (@racampos)
options:
  payload:
    description:
    - An object to send in the Request body.
    - Required for state create.
    type: list
    elements: dict
    suboptions:
      comments:
        description:
        - It is the global credential snmpv2 write community's comments.
        type: str
      credentialType:
        description:
        - It is the global credential snmpv2 write community's credentialType.
        type: str
      description:
        description:
        - It is the global credential snmpv2 write community's description.
        type: str
      id:
        description:
        - It is the global credential snmpv2 write community's id.
        type: str
      instanceTenantId:
        description:
        - It is the global credential snmpv2 write community's instanceTenantId.
        type: str
      instanceUuid:
        description:
        - It is the global credential snmpv2 write community's instanceUuid.
        type: str
      writeCommunity:
        description:
        - It is the global credential snmpv2 write community's writeCommunity.
        type: str
        required: True

  comments:
    description:
    - SNMPv2WriteCommunityDTO's comments.
    type: str
  credentialType:
    description:
    - SNMPv2WriteCommunityDTO's credentialType.
    - Available values are 'GLOBAL' and 'APP'.
    type: str
  description:
    description:
    - SNMPv2WriteCommunityDTO's description.
    type: str
  id:
    description:
    - SNMPv2WriteCommunityDTO's id.
    type: str
  instanceTenantId:
    description:
    - SNMPv2WriteCommunityDTO's instanceTenantId.
    type: str
  instanceUuid:
    description:
    - SNMPv2WriteCommunityDTO's instanceUuid.
    type: str
  writeCommunity:
    description:
    - SNMPv2WriteCommunityDTO's writeCommunity.
    - Required for state update.
    type: str

requirements:
- dnacentersdk
seealso:
# Reference by module name
- module: cisco.dnac.plugins.module_utils.definitions.global_credential_snmpv2_write_community
# Reference by Internet resource
- name: GlobalCredentialSnmpv2WriteCommunity reference
  description: Complete reference of the GlobalCredentialSnmpv2WriteCommunity object model.
  link: https://developer.cisco.com/docs/dna-center/api/1-3-3-x
# Reference by Internet resource
- name: GlobalCredentialSnmpv2WriteCommunity reference
  description: SDK reference.
  link: https://dnacentersdk.readthedocs.io/en/latest/api/api.html#v2-1-1-summary
"""

EXAMPLES = r"""
- name: create_snmp_write_community
  cisco.dnac.global_credential_snmpv2_write_community:
    state: create  # required
    payload:  # required
    - writeCommunity: SomeValue  # string, required
      comments: SomeValue  # string
      credentialType: SomeValue  # string
      description: SomeValue  # string
      id: SomeValue  # string
      instanceTenantId: SomeValue  # string
      instanceUuid: SomeValue  # string
  - name: update_snmp_write_community
  cisco.dnac.global_credential_snmpv2_write_community:
    state: update  # required
    writeCommunity: SomeValue  # string, required
    comments: SomeValue  # string
    credentialType: SomeValue  # string, valid values: 'GLOBAL', 'APP'.
    description: SomeValue  # string
    id: SomeValue  # string
    instanceTenantId: SomeValue  # string
    instanceUuid: SomeValue  # string
  """

RETURN = """
create_snmp_write_community:
    description: Adds global SNMP write community.
    returned: success
    type: dict
    contains:
    response:
      description: SNMPv2WriteCommunityDTO's response.
      returned: success
      type: dict
      contains:
        taskId:
          description: It is the global credential snmpv2 write community's taskId.
          returned: success
          type: dict
        url:
          description: It is the global credential snmpv2 write community's url.
          returned: success
          type: str
          sample: '<url>'

    version:
      description: SNMPv2WriteCommunityDTO's version.
      returned: success
      type: str
      sample: '1.0'

update_snmp_write_community:
    description: Updates global SNMP write community.
    returned: changed
    type: dict
    contains:
    response:
      description: SNMPv2WriteCommunityDTO's response.
      returned: changed
      type: dict
      contains:
        taskId:
          description: It is the global credential snmpv2 write community's taskId.
          returned: changed
          type: dict
        url:
          description: It is the global credential snmpv2 write community's url.
          returned: changed
          type: str
          sample: '<url>'

    version:
      description: SNMPv2WriteCommunityDTO's version.
      returned: changed
      type: str
      sample: '1.0'

"""
