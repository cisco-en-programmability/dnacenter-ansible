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
module: trigger_image_distribution
short_description: Manage TriggerImageDistribution objects of SoftwareImageManagementSwim
description:
- Distributes a software image on a given device. Software image must be imported successfully into DNA Center before it can be distributed.
version_added: '1.0'
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

RETURN = """
trigger_software_image_distribution:
    description: Distributes a software image on a given device. Software image must be imported successfully into DNA Center before it can be distributed.
    returned: success
    type: dict
    contains:
    response:
      description: DistributeDTO's response.
      returned: success
      type: dict
      contains:
        taskId:
          description: It is the trigger image distribution's taskId.
          returned: success
          type: dict
        url:
          description: It is the trigger image distribution's url.
          returned: success
          type: str
          sample: '<url>'

    version:
      description: DistributeDTO's version.
      returned: success
      type: str
      sample: '1.0'

"""
