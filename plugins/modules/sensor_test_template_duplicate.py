#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)


DOCUMENTATION = r"""
---
module: sensor_test_template_duplicate
short_description: Resource module for Sensor Test Template Duplicate
description:
- This module represents an alias of the module sensor_test_template_duplicate_v1
version_added: '3.1.0'
extends_documentation_fragment:
  - cisco.dnac.module
author: Rafael Campos (@racampos)
options:
  newTemplateName:
    description: Destination test template name.
    type: str
  templateName:
    description: Source test template name.
    type: str
requirements:
- dnacentersdk >= 2.4.9
- python >= 3.5
seealso:
- name: Cisco DNA Center documentation for Sensors DuplicateSensorTestTemplateV1
  description: Complete reference of the DuplicateSensorTestTemplateV1 API.
  link: https://developer.cisco.com/docs/dna-center/#!duplicate-sensor-test-template-v-1
notes:
  - SDK Method used are
    sensors.Sensors.duplicate_sensor_test_template_v1,

  - Paths used are
    put /dna/intent/api/v1/sensorTestTemplate,
  - It should be noted that this module is an alias of sensor_test_template_duplicate_v1

"""

EXAMPLES = r"""
- name: Update all
  cisco.dnac.sensor_test_template_duplicate:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    newTemplateName: string
    templateName: string

"""
RETURN = r"""
dnac_response:
  description:
    - This alias returns the output of sensor_test_template_duplicate_v1.
"""
