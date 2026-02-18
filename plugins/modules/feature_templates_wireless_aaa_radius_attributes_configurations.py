#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: feature_templates_wireless_aaa_radius_attributes_configurations
short_description: Resource module for Feature Templates Wireless Aaa Radius Attributes Configurations
description:
  - Manage operations create, update and delete of the resource Feature Templates Wireless Aaa Radius Attributes Configurations.
  - This API allows users to create a AAA Radius Attributes configuration feature template.
  - This API allows users to delete a specific AAA Radius Attributes configuration feature template by ID.
  - This API allows users to update the details of a specific AAA Radius Attributes configuration feature template by ID.
version_added: '6.18.0'
extends_documentation_fragment:
  - cisco.dnac.module
author: Rafael Campos (@racampos)
options:
  designName:
    description: The feature template design name. `Note ` The following characters are not allowed % & < > ' /.
    type: str
  featureAttributes:
    description: Feature Templates Wireless Aaa Radius Attributes Configurations's featureAttributes.
    suboptions:
      calledStationId:
        description: Called Station Identifier (calledStationId).
        type: str
    type: dict
  id:
    description: Id path parameter. AAA Radius Attributes Configuration Feature Template Id.
    type: str
  unlockedAttributes:
    description: Attributes unlocked in design can be changed at device provision time. `Note ` unlockedAttributes can only
      contain the attributes defined under featureAttributes.
    elements: str
    type: list
requirements:
  - dnacentersdk >= 2.11.0
  - python >= 3.12
seealso:
  - name: Cisco DNA Center documentation for Wireless CreateAAARadiusAttributesConfigurationFeatureTemplate
    description: Complete reference of the CreateAAARadiusAttributesConfigurationFeatureTemplate API.
    link: https://developer.cisco.com/docs/dna-center/#!create-aaa-radius-attributes-configuration-feature-template
  - name: Cisco DNA Center documentation for Wireless DeleteAAARadiusAttributesConfigurationFeatureTemplate
    description: Complete reference of the DeleteAAARadiusAttributesConfigurationFeatureTemplate API.
    link: https://developer.cisco.com/docs/dna-center/#!delete-aaa-radius-attributes-configuration-feature-template
  - name: Cisco DNA Center documentation for Wireless UpdateAAARadiusAttributesConfigurationFeatureTemplate
    description: Complete reference of the UpdateAAARadiusAttributesConfigurationFeatureTemplate API.
    link: https://developer.cisco.com/docs/dna-center/#!update-aaa-radius-attributes-configuration-feature-template
notes:
  - SDK Method used are
    wireless.Wireless.create_aaa_radius_attributes_configuration_feature_template,
    wireless.Wireless.delete_aaa_radius_attributes_configuration_feature_template,
    wireless.Wireless.update_aaa_radius_attributes_configuration_feature_template,
  - Paths used are
    post /dna/intent/api/v1/featureTemplates/wireless/aaaRadiusAttributesConfigurations,
    delete /dna/intent/api/v1/featureTemplates/wireless/aaaRadiusAttributesConfigurations/{id},
    put /dna/intent/api/v1/featureTemplates/wireless/aaaRadiusAttributesConfigurations/{id},
"""

EXAMPLES = r"""
---
- name: Create
  cisco.dnac.feature_templates_wireless_aaa_radius_attributes_configurations:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    state: present
    designName: string
    featureAttributes:
      calledStationId: string
    unlockedAttributes:
      - string
- name: Delete by id
  cisco.dnac.feature_templates_wireless_aaa_radius_attributes_configurations:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    state: absent
    id: string
- name: Update by id
  cisco.dnac.feature_templates_wireless_aaa_radius_attributes_configurations:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    state: present
    designName: string
    featureAttributes:
      calledStationId: string
    id: string
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
