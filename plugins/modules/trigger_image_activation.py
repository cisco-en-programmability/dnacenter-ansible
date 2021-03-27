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
module: trigger_image_activation
short_description: Manage TriggerImageActivation objects of SoftwareImageManagementSwim
description:
- Activates a software image on a given device. Software image must be present in the device flash.
version_added: '1.0.0'
author: Rafael Campos (@racampos)
options:
  schedule_validate:
    description:
    - ScheduleValidate, validates data before schedule (Optional).
    type: bool
  payload:
    description:
    - An object to send in the Request body.
    type: list
    required: True
    elements: dict
    suboptions:
      activateLowerImageVersion:
        description:
        - It is the trigger image activation's activateLowerImageVersion.
        type: bool
      deviceUpgradeMode:
        description:
        - It is the trigger image activation's deviceUpgradeMode.
        type: str
      deviceUuid:
        description:
        - It is the trigger image activation's deviceUuid.
        type: str
      distributeIfNeeded:
        description:
        - It is the trigger image activation's distributeIfNeeded.
        type: bool
      imageUuidList:
        description:
        - It is the trigger image activation's imageUuidList.
        type: list
      smuImageUuidList:
        description:
        - It is the trigger image activation's smuImageUuidList.
        type: list


requirements:
- dnacentersdk
seealso:
# Reference by module name
- module: cisco.dnac.plugins.module_utils.definitions.trigger_image_activation
# Reference by Internet resource
- name: TriggerImageActivation reference
  description: Complete reference of the TriggerImageActivation object model.
  link: https://developer.cisco.com/docs/dna-center/api/1-3-3-x
# Reference by Internet resource
- name: TriggerImageActivation reference
  description: SDK reference.
  link: https://dnacentersdk.readthedocs.io/en/latest/api/api.html#v2-1-1-summary
"""

EXAMPLES = r"""
- name: trigger_software_image_activation
  cisco.dnac.trigger_image_activation:
    state: create  # required
    payload:  # required
    - activateLowerImageVersion: True  # boolean
      deviceUpgradeMode: SomeValue  # string
      deviceUuid: SomeValue  # string
      distributeIfNeeded: True  # boolean
      imageUuidList:
      - SomeValue  # string
      smuImageUuidList:
      - SomeValue  # string
    schedule_validate: True  # boolean
  
"""

RETURN = """
trigger_software_image_activation:
    description: Activates a software image on a given device. Software image must be present in the device flash.
    returned: success
    type: dict
    contains:
      response:
      description: ActivateDTO's response.
      returned: success
      type: dict
      contains:
        taskId:
          description: It is the trigger image activation's taskId.
          returned: success
          type: dict
        url:
          description: It is the trigger image activation's url.
          returned: success
          type: str
          sample: '<url>'

    version:
      description: ActivateDTO's version.
      returned: success
      type: str
      sample: '1.0'

"""
