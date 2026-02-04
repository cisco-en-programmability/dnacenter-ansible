#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: filter_group_associations
short_description: Resource module for Filter Group Associations
description:
  - Manage operation create of the resource Filter Group Associations. - > Creates association between a filter group and
    entity. For detailed information about the usage of the API, please refer to the Open API specification document - https
    //github.com/cisco-en-programmability/catalyst- center-api-specs/blob/main/Assurance/CE_Cat_Center_Org-FilterGroups-1.0.0-resolved.yaml.
version_added: '6.46.0'
extends_documentation_fragment:
  - cisco.dnac.module
author: Rafael Campos (@racampos)
options:
  entityId:
    description: Entity Id.
    type: str
  entityName:
    description: Entity Name.
    type: str
  entityType:
    description: Entity Type.
    type: str
  filterGroupId:
    description: Filter Group Id.
    type: str
  headers:
    description: Additional headers.
    type: dict
requirements:
  - dnacentersdk >= 2.11.0
  - python >= 3.12
seealso:
  - name: Cisco DNA Center documentation for Devices CreateFilterGroupAssociation
    description: Complete reference of the CreateFilterGroupAssociation API.
    link: https://developer.cisco.com/docs/dna-center/#!create-filter-group-association
notes:
  - SDK Method used are
    devices.Devices.create_filter_group_association,
  - Paths used are
    post /dna/intent/api/v1/filterGroupAssociations,
"""

EXAMPLES = r"""
---
- name: Create
  cisco.dnac.filter_group_associations:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    state: present
    entityId: string
    entityName: string
    entityType: string
    filterGroupId: string
    headers: '{{my_headers | from_json}}'
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
