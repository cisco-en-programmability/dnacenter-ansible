#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)


DOCUMENTATION = r"""
---
module: discovery_range_delete
short_description: Resource module for Discovery Range Delete
description:
- This module represents an alias of the module discovery_range_delete_v1
version_added: '3.1.0'
extends_documentation_fragment:
  - cisco.dnac.module
author: Rafael Campos (@racampos)
options:
  recordsToDelete:
    description: RecordsToDelete path parameter. Number of records to delete from the
      starting index.
    type: int
  startIndex:
    description: StartIndex path parameter. Starting index for the records.
    type: int
requirements:
- dnacentersdk >= 2.7.2
- python >= 3.5
seealso:
- name: Cisco DNA Center documentation for Discovery DeleteDiscoveryBySpecifiedRangeV1
  description: Complete reference of the DeleteDiscoveryBySpecifiedRangeV1 API.
  link: https://developer.cisco.com/docs/dna-center/#!delete-discovery-by-specified-range-v-1
notes:
  - SDK Method used are
    discovery.Discovery.delete_discovery_by_specified_range_v1,

  - Paths used are
    delete /dna/intent/api/v1/discovery/{startIndex}/{recordsToDelete},
  - It should be noted that this module is an alias of discovery_range_delete_v1

"""

EXAMPLES = r"""
- name: Delete all
  cisco.dnac.discovery_range_delete:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    recordsToDelete: 0
    startIndex: 0

"""
RETURN = r"""
dnac_response:
  description:
    - This alias returns the output of discovery_range_delete_v1.
"""
