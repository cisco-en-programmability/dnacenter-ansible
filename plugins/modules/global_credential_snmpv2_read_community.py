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
module: global_credential_snmpv2_read_community
short_description: Manage GlobalCredentialSnmpv2ReadCommunity objects of Discovery
description:
- Adds global SNMP read community.
- Updates global SNMP read community.
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
      comments:
        description:
        - It is the global credential snmpv2 read community's comments.
        type: str
      credentialType:
        description:
        - It is the global credential snmpv2 read community's credentialType.
        type: str
      description:
        description:
        - It is the global credential snmpv2 read community's description.
        type: str
      id:
        description:
        - It is the global credential snmpv2 read community's id.
        type: str
      instanceTenantId:
        description:
        - It is the global credential snmpv2 read community's instanceTenantId.
        type: str
      instanceUuid:
        description:
        - It is the global credential snmpv2 read community's instanceUuid.
        type: str
      readCommunity:
        description:
        - It is the global credential snmpv2 read community's readCommunity.
        type: str
        required: True

  comments:
    description:
    - SNMPv2ReadCommunityDTO's comments.
    type: str
  credentialType:
    description:
    - SNMPv2ReadCommunityDTO's credentialType.
    - Available values are 'GLOBAL' and 'APP'.
    type: str
  description:
    description:
    - SNMPv2ReadCommunityDTO's description.
    type: str
  id:
    description:
    - SNMPv2ReadCommunityDTO's id.
    type: str
  instanceTenantId:
    description:
    - SNMPv2ReadCommunityDTO's instanceTenantId.
    type: str
  instanceUuid:
    description:
    - SNMPv2ReadCommunityDTO's instanceUuid.
    type: str
  readCommunity:
    description:
    - SNMPv2ReadCommunityDTO's readCommunity.
    - Required for state update.
    type: str

requirements:
- dnacentersdk
seealso:
# Reference by module name
- module: cisco.dnac.plugins.module_utils.definitions.global_credential_snmpv2_read_community
# Reference by Internet resource
- name: GlobalCredentialSnmpv2ReadCommunity reference
  description: Complete reference of the GlobalCredentialSnmpv2ReadCommunity object model.
  link: https://developer.cisco.com/docs/dna-center/api/1-3-3-x
# Reference by Internet resource
- name: GlobalCredentialSnmpv2ReadCommunity reference
  description: SDK reference.
  link: https://dnacentersdk.readthedocs.io/en/latest/api/api.html#v2-1-1-summary
"""

EXAMPLES = r"""
- name: create_snmp_read_community
  cisco.dnac.global_credential_snmpv2_read_community:
    state: create  # required
    payload:  # required
    - readCommunity: SomeValue  # string, required
      comments: SomeValue  # string
      credentialType: SomeValue  # string
      description: SomeValue  # string
      id: SomeValue  # string
      instanceTenantId: SomeValue  # string
      instanceUuid: SomeValue  # string
  
- name: update_snmp_read_community
  cisco.dnac.global_credential_snmpv2_read_community:
    state: update  # required
    readCommunity: SomeValue  # string, required
    comments: SomeValue  # string
    credentialType: SomeValue  # string, valid values: 'GLOBAL', 'APP'.
    description: SomeValue  # string
    id: SomeValue  # string
    instanceTenantId: SomeValue  # string
    instanceUuid: SomeValue  # string
  
"""

RETURN = """
create_snmp_read_community:
    description: Adds global SNMP read community.
    returned: success
    type: dict
    contains:
    response:
      description: SNMPv2ReadCommunityDTO's response.
      returned: success
      type: dict
      contains:
        taskId:
          description: It is the global credential snmpv2 read community's taskId.
          returned: success
          type: dict
        url:
          description: It is the global credential snmpv2 read community's url.
          returned: success
          type: str
          sample: '<url>'

    version:
      description: SNMPv2ReadCommunityDTO's version.
      returned: success
      type: str
      sample: '1.0'

update_snmp_read_community:
    description: Updates global SNMP read community.
    returned: changed
    type: dict
    contains:
    response:
      description: SNMPv2ReadCommunityDTO's response.
      returned: changed
      type: dict
      contains:
        taskId:
          description: It is the global credential snmpv2 read community's taskId.
          returned: changed
          type: dict
        url:
          description: It is the global credential snmpv2 read community's url.
          returned: changed
          type: str
          sample: '<url>'

    version:
      description: SNMPv2ReadCommunityDTO's version.
      returned: changed
      type: str
      sample: '1.0'

"""
