#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)


DOCUMENTATION = r"""
---
module: integration_settings_itsm_instances_info
short_description: Information module for Integration Settings Itsm Instances Info
description:
- This module represents an alias of the module integration_settings_itsm_instances_v1_info
version_added: '6.14.0'
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
- name: Cisco DNA Center documentation for ITSM Integration GetAllITSMIntegrationSettingsV1
  description: Complete reference of the GetAllITSMIntegrationSettingsV1 API.
  link: https://developer.cisco.com/docs/dna-center/#!get-all-itsm-integration-settings-v-1
notes:
  - SDK Method used are
    itsm_integration.ItsmIntegration.get_all_itsm_integration_settings_v1,

  - Paths used are
    get /dna/intent/api/v1/integration-settings/itsm/instances,
  - It should be noted that this module is an alias of integration_settings_itsm_instances_v1_info

"""

EXAMPLES = r"""
- name: Get all Integration Settings Itsm Instances Info
  cisco.dnac.integration_settings_itsm_instances_info:
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
  description:
    - This alias returns the output of integration_settings_itsm_instances_v1_info.
"""