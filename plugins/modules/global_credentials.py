#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: global_credentials
short_description: Resource module for Global Credentials
description:
  - Manage operations create, update and delete of the resource Global Credentials.
  - API to add new global credential.
  - API to delete global credential by the given identifier.
  - API to update the global credential by the given identifier.
version_added: '6.46.0'
extends_documentation_fragment:
  - cisco.dnac.module
author: Rafael Campos (@racampos)
options:
  id:
    description: Id path parameter. Unique identifier of the global credential. Accepts comma separated values.
    type: str
requirements:
  - dnacentersdk >= 2.11.0
  - python >= 3.12
seealso:
  - name: Cisco DNA Center documentation for Network Settings AddsNewGlobalCredential
    description: Complete reference of the AddsNewGlobalCredential API.
    link: https://developer.cisco.com/docs/dna-center/#!adds-new-global-credential
  - name: Cisco DNA Center documentation for Network Settings DeleteGlobalCredentialByTheGivenIdentifier
    description: Complete reference of the DeleteGlobalCredentialByTheGivenIdentifier API.
    link: https://developer.cisco.com/docs/dna-center/#!delete-global-credential-by-the-given-identifier
  - name: Cisco DNA Center documentation for Network Settings UpdateGlobalCredentialByTheGivenIdentifer
    description: Complete reference of the UpdateGlobalCredentialByTheGivenIdentifer API.
    link: https://developer.cisco.com/docs/dna-center/#!update-global-credential-by-the-given-identifer
notes:
  - SDK Method used are
    network_settings.NetworkSettings.adds_new_global_credential,
    network_settings.NetworkSettings.delete_global_credential_by_the_given_identifier,
    network_settings.NetworkSettings.update_global_credential_by_the_given_identifer,
  - Paths used are
    post /dna/intent/api/v1/globalCredentials,
    delete /dna/intent/api/v1/globalCredentials/{id},
    put /dna/intent/api/v1/globalCredentials/{id},
"""

EXAMPLES = r"""
---
- name: Create
  cisco.dnac.global_credentials:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    state: present
- name: Delete by id
  cisco.dnac.global_credentials:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    state: absent
    id: string
- name: Update by id
  cisco.dnac.global_credentials:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    state: present
    id: string
"""
RETURN = r"""
dnac_response:
  description: A dictionary or list with the response returned by the Cisco DNAC Python SDK
  returned: always
  type: dict
  sample: >
    {
      "response": {
        "taskId": "string",
        "url": "string"
      },
      "version": "string"
    }
"""
