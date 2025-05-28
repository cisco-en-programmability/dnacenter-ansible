#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)
DOCUMENTATION = r"""
---
module: backup_configuration_v1_info
short_description: Information module for Backup Configuration V1
description:
  - Get all Backup Configuration V1.
  - This api is used to get the backup configuration.
version_added: '6.18.0'
extends_documentation_fragment:
  - cisco.dnac.module_info
author: Rafael Campos (@racampos)
options:
  headers:
    description: Additional headers.
    type: dict
requirements:
  - dnacentersdk >= 2.4.9
  - python >= 3.5
seealso:
  - name: Cisco DNA Center documentation for Backup GetBackupConfigurationV1
    description: Complete reference of the GetBackupConfigurationV1 API.
    link: https://developer.cisco.com/docs/dna-center/#!get-backup-configuration
notes:
  - SDK Method used are backup.Backup.get_backup_configuration_v1,
  - Paths used are get /dna/system/api/v1/backupConfiguration,
"""
EXAMPLES = r"""
- name: Get all Backup Configuration V1
  cisco.dnac.backup_configuration_v1_info:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    headers: "{{my_headers | from_json}}"
  register: result
"""
RETURN = r"""
dnac_response:
  description: A dictionary or list with the response returned by the Cisco DNAC Python SDK
  returned: always
  type: dict
  sample: >
    {
      "dataRetention": 0,
      "id": "string",
      "isEncryptionPassPhraseAvailable": true,
      "mountPath": "string",
      "type": "string"
    }
"""
