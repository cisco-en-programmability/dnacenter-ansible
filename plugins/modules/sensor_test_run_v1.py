#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)
DOCUMENTATION = r"""
---
module: sensor_test_run_v1
short_description: Resource module for Sensor Test Run V1
description:
  - Manage operation update of the resource Sensor Test Run V1.
  - Intent API to run a deployed SENSOR test.
version_added: '3.1.0'
extends_documentation_fragment:
  - cisco.dnac.module
author: Rafael Campos (@racampos)
options:
  templateName:
    description: Template Name.
    type: str
requirements:
  - dnacentersdk >= 2.4.9
  - python >= 3.5
seealso:
  - name: Cisco DNA Center documentation for Sensors RunNowSensorTestV1
    description: Complete reference of the RunNowSensorTestV1 API.
    link: https://developer.cisco.com/docs/dna-center/#!run-now-sensor-test
notes:
  - SDK Method used are sensors.Sensors.run_now_sensor_test_v1,
  - Paths used are put /dna/intent/api/v1/sensor-run-now,
"""
EXAMPLES = r"""
- name: Update all
  cisco.dnac.sensor_test_run_v1:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    templateName: string
"""
RETURN = r"""
dnac_response:
  description: A dictionary or list with the response returned by the Cisco DNAC Python SDK
  returned: always
  type: dict
  sample: >
    {}
"""
