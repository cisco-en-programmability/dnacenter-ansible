#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright: (c) 2020, Rafael Campos <rcampos@altus.cr>
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

ANSIBLE_METADATA = {
    "metadata_version": "0.0.1",
    "status": ["preview"],
    "supported_by": "community",
}

DOCUMENTATION = r"""
---
module: device_enrichment_details
short_description: Manage DeviceEnrichmentDetails objects of Devices
description:
- Enriches a given network device context (device id or device Mac Address or device management IP address) with details about the device and neighbor topology.
version_added: '1.0.0'
author: Rafael Campos (@racampos)
options:
  headers:
    description:
    - Adds the header parameters.
    type: dict
    required: True

requirements:
- dnacentersdk
seealso:
# Reference by module name
- module: cisco.dnac.plugins.module_utils.definitions.device_enrichment_details
# Reference by Internet resource
- name: DeviceEnrichmentDetails reference
  description: Complete reference of the DeviceEnrichmentDetails object model.
  link: https://developer.cisco.com/docs/dna-center/api/1-3-3-x
# Reference by Internet resource
- name: DeviceEnrichmentDetails reference
  description: SDK reference.
  link: https://dnacentersdk.readthedocs.io/en/latest/api/api.html#v2-1-1-summary
"""

EXAMPLES = r"""
- name: get_device_enrichment_details
  cisco.dnac.device_enrichment_details:
    state: query  # required
    headers:  # required
  register: query_result

"""

RETURN = """
"""
