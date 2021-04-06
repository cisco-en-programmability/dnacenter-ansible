#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright: (c) 2020, Rafael Campos <rcampos@altus.cr>
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: trigger_image_distribution
short_description: Manage TriggerImageDistribution objects of SoftwareImageManagementSwim
description:
- Distributes a software image on a given device. Software image must be imported successfully into DNA Center before it can be distributed.
version_added: '1.0.0'
author: Rafael Campos (@racampos)
options:
  payload:
    description:
    - An object to send in the Request body.
    type: list
    required: True
    elements: dict
    suboptions:
      deviceUuid:
        description:
        - It is the trigger image distribution's deviceUuid.
        type: str
      imageUuid:
        description:
        - It is the trigger image distribution's imageUuid.
        type: str


requirements:
- dnacentersdk
seealso:
# Reference by module name
- module: cisco.dnac.plugins.module_utils.definitions.trigger_image_distribution
# Reference by Internet resource
- name: TriggerImageDistribution reference
  description: Complete reference of the TriggerImageDistribution object model.
  link: https://developer.cisco.com/docs/dna-center/api/1-3-3-x
# Reference by Internet resource
- name: TriggerImageDistribution reference
  description: SDK reference.
  link: https://dnacentersdk.readthedocs.io/en/latest/api/api.html#v2-1-1-summary
"""

EXAMPLES = r"""
- name: trigger_software_image_distribution
  cisco.dnac.trigger_image_distribution:
    state: create  # required
    payload:  # required
    - deviceUuid: SomeValue  # string
      imageUuid: SomeValue  # string

"""

RETURN = r"""
dnac_response:
  description: A dictionary with the response returned by the DNA Center Python SDK
  returned: always
  type: dict
  sample: {"response": 29, "version": "1.0"}
sdk_function:
  description: The DNA Center SDK function used to execute the task
  returned: always
  type: str
  sample: application_policy.get_application_sets
missing_params:
  description: Provided arguments do not comply with the schema of the DNA Center Python SDK function
  returned: when the function request schema is not satisfied
  type: list
  sample:
"""
