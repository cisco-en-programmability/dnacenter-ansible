#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: global_credential_update
short_description: Resource module for Global Credential Update
description:
- Manage operation update of the resource Global Credential Update.
- Update global credential for network devices in site(s).
version_added: '3.1.0'
extends_documentation_fragment:
  - cisco.dnac.module
author: Rafael Campos (@racampos)
options:
  globalCredentialId:
    description: GlobalCredentialId path parameter. ID of global-credential.
    type: str
  siteUuids:
    description: Global Credential Update's siteUuids.
    elements: str
    type: list
requirements:
- dnacentersdk >= 2.4.0
- python >= 3.5
seealso:
# Reference to SDK documentation of current version
- name: SDK function delete_global_credentials_by_id used
  link: https://dnacentersdk.rtfd.io/en/latest/api/api.html#dnacentersdk.api.v2_2_3_3.discovery.Discovery.delete_global_credentials_by_id

- name: SDK function update_global_credentials used
  link: https://dnacentersdk.rtfd.io/en/latest/api/api.html#dnacentersdk.api.v2_2_3_3.discovery.Discovery.update_global_credentials

- name: Paths used on the module Global Credential Update
  description: |-
    put /dna/intent/api/v1/global-credential/{globalCredentialId}
"""

EXAMPLES = r"""
- name: Update by id
  cisco.dnac.global_credential_update:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    globalCredentialId: string
    siteUuids:
    - string

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
