#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: filter_groups
short_description: Resource module for Filter Groups
description:
  - Manage operations create, update and delete of the resource Filter Groups.
  - Creates filter group with given filters.
  - For detailed information about the usage of the API, please refer to the Open API specification document
    https //github.com/cisco-en-programmability/catalyst-center-api-specs/blob/main/Assurance/
    CE_Cat_Center_Org-FilterGroups-1.0.0-resolved.yaml.
  - Deletes the given filter group.
  - For detailed information about the usage of the API, please refer to the Open API specification document
    https //github.com/cisco-en-programmability/catalyst-center-api-specs/blob/main/Assurance/
    CE_Cat_Center_Org-FilterGroups-1.0.0-resolved.yaml.
  - Updates the filter group for given id. The request payload should contain complete definition of the Filter Group.
  - For detailed information about the usage of the API, please refer to the Open API specification document
    https //github.com/cisco-en-programmability/catalyst-center-api-specs/blob/main/Assurance/
    CE_Cat_Center_Org-FilterGroups-1.0.0-resolved.yaml.
version_added: '6.46.0'
extends_documentation_fragment:
  - cisco.dnac.module
author: Rafael Campos (@racampos)
options:
  filters:
    description: Filter Groups's filters.
    elements: dict
    suboptions:
      key:
        description: Key.
        type: str
      operator:
        description: Operator.
        type: str
      value:
        description: Value.
        type: str
    type: list
  headers:
    description: Additional headers.
    type: dict
  id:
    description: Id path parameter. The id of the filter group to be deleted.
    type: str
  name:
    description: Name.
    type: str
  type:
    description: Type.
    type: str
requirements:
  - dnacentersdk >= 2.11.0
  - python >= 3.12
seealso:
  - name: Cisco DNA Center documentation for Devices CreateFilterGroup
    description: Complete reference of the CreateFilterGroup API.
    link: https://developer.cisco.com/docs/dna-center/#!create-filter-group
  - name: Cisco DNA Center documentation for Devices DeleteAFilterGroup
    description: Complete reference of the DeleteAFilterGroup API.
    link: https://developer.cisco.com/docs/dna-center/#!delete-a-filter-group
  - name: Cisco DNA Center documentation for Devices UpdateFilterGroup
    description: Complete reference of the UpdateFilterGroup API.
    link: https://developer.cisco.com/docs/dna-center/#!update-filter-group
notes:
  - SDK Method used are
    devices.Devices.create_filter_group,
    devices.Devices.delete_a_filter_group,
    devices.Devices.update_filter_group,
  - Paths used are
    post /dna/intent/api/v1/filterGroups,
    delete /dna/intent/api/v1/filterGroups/{id},
    put /dna/intent/api/v1/filterGroups/{id},
"""

EXAMPLES = r"""
---
- name: Create
  cisco.dnac.filter_groups:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    state: present
    filters:
      - key: string
        operator: string
        value: string
    headers: '{{my_headers | from_json}}'
    name: string
    type: string
- name: Delete by id
  cisco.dnac.filter_groups:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    state: absent
    headers: '{{my_headers | from_json}}'
    id: string
- name: Update by id
  cisco.dnac.filter_groups:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    state: present
    filters:
      - key: string
        operator: string
        value: string
    headers: '{{my_headers | from_json}}'
    id: string
    name: string
    type: string
"""
RETURN = r"""
dnac_response:
  description: A dictionary or list with the response returned by the Cisco DNAC Python SDK
  returned: always
  type: dict
  sample: >
    {
      "id": "string"
    }
"""
