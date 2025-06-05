#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)
DOCUMENTATION = r"""
---
module: swim_trigger_distribution_v1
short_description: Resource module for Swim Trigger Distribution V1
description:
  - Manage operation create of the resource Swim Trigger Distribution V1.
  - >
    Distributes a software image on a given device. Software image must be imported
    successfully into DNA Center
    before it can be distributed.
version_added: '3.1.0'
extends_documentation_fragment:
  - cisco.dnac.module
author: Rafael Campos (@racampos)
options:
  payload:
    description: Swim Trigger Distribution's payload.
    elements: dict
    suboptions:
      deviceUuid:
        description: Swim Trigger Distribution's deviceUuid.
        type: str
      imageUuid:
        description: Swim Trigger Distribution's imageUuid.
        type: str
    type: list
requirements:
  - dnacentersdk >= 2.4.9
  - python >= 3.5
seealso:
  - name: Cisco DNA Center documentation for Software Image Management (SWIM) TriggerSoftwareImageDistributionV1
    description: Complete reference of the TriggerSoftwareImageDistributionV1 API.
    link:
      https://developer.cisco.com/docs/dna-center/#!trigger-software-image-distribution
notes:
  - SDK Method used are
    software_image_management_swim.SoftwareImageManagementSwim.trigger_software_image_distribution_v1,
  - Paths used are post /dna/intent/api/v1/image/distribution,
"""
EXAMPLES = r"""
- name: Create
  cisco.dnac.swim_trigger_distribution_v1:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    payload:
      - deviceUuid: string
        imageUuid: string
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
