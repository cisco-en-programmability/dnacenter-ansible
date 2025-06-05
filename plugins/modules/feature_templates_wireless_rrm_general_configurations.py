#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)
DOCUMENTATION = r"""
---
module: feature_templates_wireless_rrm_general_configurations
short_description: Resource module for Feature Templates Wireless Rrm General Configurations
description:
  - This module represents an alias of the module feature_templates_wireless_rrm_general_configurations_v1
version_added: '6.18.0'
extends_documentation_fragment:
  - cisco.dnac.module
author: Rafael Campos (@racampos)
options:
  designName:
    description: The feature template design name. `Note ` The following characters
      are not allowed % & < > ' /.
    type: str
  featureAttributes:
    description: Feature Templates Wireless Rrm General Configurations's featureAttributes.
    suboptions:
      coverageHoleDetection:
        description: Global Coverage Hole Detection.
        type: bool
      monitoringChannels:
        description: The monitoringChannels attribute represents the scope of monitoring
          channels.
        type: str
      neighborDiscoverType:
        description: The neighborDiscoverType attribute represents the type of neighbor
          discovery.
        type: str
      radioBand:
        description: Radio Band 2_4GHZ is supported only on Cisco IOS-XE based Wireless
          Controllers running 17.9.1 and above.
        type: str
      throughputThreshold:
        description: Throughput Threshold.
        type: int
    type: dict
  unlockedAttributes:
    description: Attributes unlocked in design can be changed at device provision
      time. `Note ` unlockedAttributes can only contain the attributes defined under
      featureAttributes.
    elements: str
    type: list
requirements:
  - dnacentersdk >= 2.4.9
  - python >= 3.5
seealso:
  - name: Cisco DNA Center documentation for Wireless CreateRRMGeneralConfigurationFeatureTemplateV1
    description: Complete reference of the CreateRRMGeneralConfigurationFeatureTemplateV1
      API.
    link:
      https://developer.cisco.com/docs/dna-center/#!create-rrm-general-configuration-feature-template
notes:
  - SDK Method used are wireless.Wireless.create_r_r_m_general_configuration_feature_template_v1,
  - Paths used are post /dna/intent/api/v1/featureTemplates/wireless/rrmGeneralConfigurations,
  - It should be noted that this module is an alias of feature_templates_wireless_rrm_general_configurations_v1
"""
EXAMPLES = r"""
- name: Create
  cisco.dnac.feature_templates_wireless_rrm_general_configurations:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    designName: string
    featureAttributes:
      coverageHoleDetection: true
      monitoringChannels: string
      neighborDiscoverType: string
      radioBand: string
      throughputThreshold: 0
    unlockedAttributes:
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
