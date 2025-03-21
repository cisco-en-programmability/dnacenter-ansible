#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)


DOCUMENTATION = r"""
---
module: 
  icap_settings_configuration_models_preview_activity_id_network_device_status_details_info
short_description: Information module for Icap Settings Configuration Models Preview
  Activity Id Network Device Status Details Info
description:
  - This module represents an alias of the module 
    icap_settings_configuration_models_preview_activity_id_network_device_status_details_v1_info
version_added: '6.17.0'
extends_documentation_fragment:
  - cisco.dnac.module_info
author: Rafael Campos (@racampos)
options:
  headers:
    description: Additional headers.
    type: dict
  previewActivityId:
    description:
      - PreviewActivityId path parameter. Activity from the POST /deviceConfigugrationModels
        task response.
    type: str
requirements:
  - dnacentersdk >= 2.4.9
  - python >= 3.5
seealso:
  - name: Cisco DNA Center documentation for Sensors GetICAPConfigurationStatusPerNetworkDeviceV1
    description: Complete reference of the GetICAPConfigurationStatusPerNetworkDeviceV1
      API.
    link: 
      https://developer.cisco.com/docs/dna-center/#!get-icap-configuration-status-per-network-device
notes:
  - SDK Method used are sensors.Sensors.get_i_cap_configuration_status_per_network_device_v1,
  - Paths used are get 
    /dna/intent/api/v1/icapSettings/configurationModels/{previewActivityId}/networkDeviceStatusDetails,
  - It should be noted that this module is an alias of 
    icap_settings_configuration_models_preview_activity_id_network_device_status_details_v1_info                                                    # noqa: E501
"""

EXAMPLES = r"""
- name: Get all Icap Settings Configuration Models Preview Activity Id Network Device
    Status Details Info
  cisco.dnac.icap_settings_configuration_models_preview_activity_id_network_device_status_details_info:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    headers: "{{my_headers | from_json}}"
    previewActivityId: string
  register: result
"""
RETURN = r"""
dnac_response:
  description: A dictionary or list with the response returned by the Cisco DNAC Python SDK
  returned: always
  type: dict
  sample: >
    {
      "response": [
        {
          "networkDeviceId": "string",
          "status": "string"
        }
      ],
      "version": "string"
    }
"""
