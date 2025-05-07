#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)
DOCUMENTATION = r"""
---
module: application_sets
short_description: Resource module for Application Sets
description:
  - This module represents an alias of the module application_sets_v1
version_added: '3.1.0'
extends_documentation_fragment:
  - cisco.dnac.module
author: Rafael Campos (@racampos)
options:
  id:
    description: Id query parameter.
    type: str
  payload:
    description: Application Sets's payload.
    elements: dict
    suboptions:
      name:
        description: Name.
        type: str
    type: list
requirements:
  - dnacentersdk >= 2.4.9
  - python >= 3.5
seealso:
  - name: Cisco DNA Center documentation for Application Policy CreateApplicationSetV1
    description: Complete reference of the CreateApplicationSetV1 API.
    link: https://developer.cisco.com/docs/dna-center/#!create-application-set
  - name: Cisco DNA Center documentation for Application Policy DeleteApplicationSetV1
    description: Complete reference of the DeleteApplicationSetV1 API.
    link: https://developer.cisco.com/docs/dna-center/#!delete-application-set
notes:
  - SDK Method used are application_policy.ApplicationPolicy.create_application_set_v1,
    application_policy.ApplicationPolicy.delete_application_set_v1,
  - Paths used are post /dna/intent/api/v1/application-policy-application-set, delete
    /dna/intent/api/v1/application-policy-application-set,
  - It should be noted that this module is an alias of application_sets_v1
"""
EXAMPLES = r"""
- name: Delete all
  cisco.dnac.application_sets:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    state: absent
    id: string
- name: Create
  cisco.dnac.application_sets:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    state: present
    payload:
      - name: string
"""
RETURN = r"""
dnac_response:
  description: A dictionary or list with the response returned by the Cisco DNAC Python SDK
  returned: always
  type: dict
  sample: >
    {
      "taskId": "string",
      "url": "string"
    }
"""
