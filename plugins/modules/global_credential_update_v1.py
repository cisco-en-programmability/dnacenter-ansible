#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)
DOCUMENTATION = r"""
---
module: global_credential_update_v1
short_description: Resource module for Global Credential Update V1
description:
  - Manage operation update of the resource Global Credential Update V1.
  - Update global credential for network devices in sites.
version_added: '3.1.0'
extends_documentation_fragment:
  - cisco.dnac.module
author: Rafael Campos (@racampos)
options:
  globalCredentialId:
    description: GlobalCredentialId path parameter. Global credential Uuid.
    type: str
  siteUuids:
    description: List of siteUuids where credential is to be updated.
    elements: str
    type: list
requirements:
  - dnacentersdk >= 2.4.9
  - python >= 3.5
seealso:
  - name: Cisco DNA Center documentation for Discovery UpdateGlobalCredentialsV1
    description: Complete reference of the UpdateGlobalCredentialsV1 API.
    link: https://developer.cisco.com/docs/dna-center/#!update-global-credentials
notes:
  - SDK Method used are discovery.Discovery.update_global_credentials_v1,
  - Paths used are put /dna/intent/api/v1/global-credential/{globalCredentialId},
"""
EXAMPLES = r"""
- name: Update by id
  cisco.dnac.global_credential_update_v1:
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
