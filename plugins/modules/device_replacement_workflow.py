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
module: device_replacement_workflow
short_description: Manage DeviceReplacementWorkflow objects of DeviceReplacement
description:
- API to trigger RMA workflow that will replace faulty device with replacement device with same configuration and images.
version_added: '1.0.0'
author: Rafael Campos (@racampos)
options:
  faultyDeviceSerialNumber:
    description:
    - DeviceReplacementWorkflowDTO's faultyDeviceSerialNumber.
    type: str
    required: True
  replacementDeviceSerialNumber:
    description:
    - DeviceReplacementWorkflowDTO's replacementDeviceSerialNumber.
    type: str
    required: True

requirements:
- dnacentersdk
seealso:
# Reference by module name
- module: cisco.dnac.plugins.module_utils.definitions.device_replacement_workflow
# Reference by Internet resource
- name: DeviceReplacementWorkflow reference
  description: Complete reference of the DeviceReplacementWorkflow object model.
  link: https://developer.cisco.com/docs/dna-center/api/1-3-3-x
# Reference by Internet resource
- name: DeviceReplacementWorkflow reference
  description: SDK reference.
  link: https://dnacentersdk.readthedocs.io/en/latest/api/api.html#v2-1-1-summary
"""

EXAMPLES = r"""
- name: deploy_device_replacement_workflow
  cisco.dnac.device_replacement_workflow:
    state: create  # required
    faultyDeviceSerialNumber: SomeValue  # string, required
    replacementDeviceSerialNumber: SomeValue  # string, required
  
"""

RETURN = """
deploy_device_replacement_workflow:
    description: API to trigger RMA workflow that will replace faulty device with replacement device with same configuration and images.
    returned: success
    type: dict
    contains:
      response:
      description: DeviceReplacementWorkflowDTO's response.
      returned: success
      type: dict
      contains:
        taskId:
          description: It is the device replacement workflow's taskId.
          returned: success
          type: dict
        url:
          description: It is the device replacement workflow's url.
          returned: success
          type: str
          sample: '<url>'

    version:
      description: DeviceReplacementWorkflowDTO's version.
      returned: success
      type: str
      sample: '1.0'

"""
