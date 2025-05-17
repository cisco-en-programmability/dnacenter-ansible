#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)
DOCUMENTATION = r"""
---
module: backups_id_v1_info
short_description: Information module for Backups Id V1
description:
  - Get Backups Id V1 by id.
  - This api is used to get a specific backup based on the provided `backup id`.
version_added: '6.18.0'
extends_documentation_fragment:
  - cisco.dnac.module_info
author: Rafael Campos (@racampos)
options:
  headers:
    description: Additional headers.
    type: dict
  id:
    description:
      - Id path parameter. The `id` of the backup to be retrieved.
    type: str
requirements:
  - dnacentersdk >= 2.4.9
  - python >= 3.5
seealso:
  - name: Cisco DNA Center documentation for Backup GetBackupByIdV1
    description: Complete reference of the GetBackupByIdV1 API.
    link: https://developer.cisco.com/docs/dna-center/#!get-backup-by-id
notes:
  - SDK Method used are backup.Backup.get_backup_by_id_v1,
  - Paths used are get /dna/system/api/v1/backups/{id},
"""
EXAMPLES = r"""
- name: Get Backups Id V1 by id
  cisco.dnac.backups_id_v1_info:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    headers: "{{my_headers | from_json}}"
    id: string
  register: result
"""
RETURN = r"""
dnac_response:
  description: A dictionary or list with the response returned by the Cisco DNAC Python SDK
  returned: always
  type: dict
  sample: >
    {
      "response": {},
      "version": "string"
    }
"""
