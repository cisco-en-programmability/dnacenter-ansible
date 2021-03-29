#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright: (c) 2020, Rafael Campos <rcampos@altus.cr>
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: global_credential
short_description: Manage GlobalCredential objects of Discovery
description:
- Returns global credential for the given credential sub type.
- Deletes global credential for the given ID.
- Update global credential for network devices in site(s).
- Returns the credential sub type for the given Id.
version_added: '1.0.0'
author: Rafael Campos (@racampos)
options:
  credential_sub_type:
    description:
    - Credential type as CLI / SNMPV2_READ_COMMUNITY / SNMPV2_WRITE_COMMUNITY / SNMPV3 / HTTP_WRITE / HTTP_READ / NETCONF.
    - Required for state query.
    type: str
  order:
    description:
    - Order query parameter.
    type: str
  sort_by:
    description:
    - SortBy query parameter.
    type: str
  global_credential_id:
    description:
    - ID of global-credential.
    - Global credential Uuid.
    type: str
    required: True
  siteUuids:
    description:
    - SitesInfoDTO's siteUuids (list of strings).
    type: list
  id:
    description:
    - Global Credential ID.
    - Required for state query.
    type: str

requirements:
- dnacentersdk
seealso:
# Reference by module name
- module: cisco.dnac.plugins.module_utils.definitions.global_credential
# Reference by Internet resource
- name: GlobalCredential reference
  description: Complete reference of the GlobalCredential object model.
  link: https://developer.cisco.com/docs/dna-center/api/1-3-3-x
# Reference by Internet resource
- name: GlobalCredential reference
  description: SDK reference.
  link: https://dnacentersdk.readthedocs.io/en/latest/api/api.html#v2-1-1-summary
"""

EXAMPLES = r"""
- name: get_global_credentials
  cisco.dnac.global_credential:
    state: query  # required
    credential_sub_type: SomeValue  # string, required
    order: SomeValue  # string
    sort_by: SomeValue  # string
  register: query_result

- name: delete_global_credentials_by_id
  cisco.dnac.global_credential:
    state: delete  # required
    global_credential_id: SomeValue  # string, required

- name: update_global_credentials
  cisco.dnac.global_credential:
    state: update  # required
    global_credential_id: SomeValue  # string, required
    siteUuids:
    - SomeValue  # string

- name: get_credential_sub_type_by_credential_id
  cisco.dnac.global_credential:
    state: query  # required
    id: SomeValue  # string, required
  register: query_result

"""

RETURN = """
"""
