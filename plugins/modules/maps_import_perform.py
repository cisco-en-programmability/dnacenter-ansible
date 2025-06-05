#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)
DOCUMENTATION = r"""
---
module: maps_import_perform
short_description: Resource module for Maps Import Perform
description:
  - This module represents an alias of the module maps_import_perform_v1
version_added: '6.14.0'
extends_documentation_fragment:
  - cisco.dnac.module
author: Rafael Campos (@racampos)
options:
  importContextUuid:
    description: ImportContextUuid path parameter. The unique import context UUID
      given by a previous call of Start Import API.
    type: str
requirements:
  - dnacentersdk >= 2.4.9
  - python >= 3.5
seealso:
  - name: Cisco DNA Center documentation for Sites ImportMapArchivePerformImportV1
    description: Complete reference of the ImportMapArchivePerformImportV1 API.
    link: https://developer.cisco.com/docs/dna-center/#!import-map-archive-perform-import
notes:
  - SDK Method used are sites.Sites.import_map_archive_perform_import_v1,
  - Paths used are post /dna/intent/api/v1/maps/import/{importContextUuid}/perform,
  - It should be noted that this module is an alias of maps_import_perform_v1
"""
EXAMPLES = r"""
- name: Create
  cisco.dnac.maps_import_perform:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    importContextUuid: string
"""
RETURN = r"""
dnac_response:
  description: A dictionary or list with the response returned by the Cisco DNAC Python SDK
  returned: always
  type: dict
  sample: >
    {}
"""
