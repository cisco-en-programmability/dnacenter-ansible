#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)


DOCUMENTATION = r"""
---
module: icap_settings_configuration_models_preview_activity_id
short_description: Resource module for Icap Settings Configuration Models Preview Activity Id
description:
- This module represents an alias of the module icap_settings_configuration_models_preview_activity_id_v1
version_added: '6.17.0'
extends_documentation_fragment:
  - cisco.dnac.module
author: Rafael Campos (@racampos)
options:
  previewActivityId:
    description: PreviewActivityId path parameter. Activity from the POST /deviceConfigugrationModels
      task response.
    type: str
requirements:
- dnacentersdk >= 2.4.9
- python >= 3.5
seealso:
- name: Cisco DNA Center documentation for Sensors DiscardsTheICAPConfigurationIntentByActivityIDV1
  description: Complete reference of the DiscardsTheICAPConfigurationIntentByActivityIDV1 API.
  link: https://developer.cisco.com/docs/dna-center/#!discards-the-icap-configuration-intent-by-activity-id
notes:
  - SDK Method used are
    sensors.Sensors.discards_the_i_cap_configuration_intent_by_activity_id_v1,

  - Paths used are
    delete /dna/intent/api/v1/icapSettings/configurationModels/{previewActivityId},
  - It should be noted that this module is an alias of icap_settings_configuration_models_preview_activity_id_v1

"""

EXAMPLES = r"""
- name: Delete by id
  cisco.dnac.icap_settings_configuration_models_preview_activity_id:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    previewActivityId: string

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
