#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: filter_group_aassociations_delete
short_description: Resource module for Filter Group Aassociations Delete
description:
  - Manage operation delete of the resource Filter Group Aassociations Delete. - > Deletes the association between filter
    group and entity. For detailed information about the usage of the API, please refer to the Open API specification document
    - https //github.com/cisco-en-programmability/catalyst- center-api-specs/blob/main/Assurance/CE_Cat_Center_Org-FilterGroups-1.0.0-resolved.yaml.
version_added: '6.46.0'
extends_documentation_fragment:
  - cisco.dnac.module
author: Rafael Campos (@racampos)
options:
  headers:
    description: Additional headers.
    type: dict
  id:
    description: Id path parameter. Association id.
    type: str
requirements:
  - dnacentersdk >= 2.11.0
  - python >= 3.12
seealso:
  - name: Cisco DNA Center documentation for Devices DeleteFilterGroupAssociation
    description: Complete reference of the DeleteFilterGroupAssociation API.
    link: https://developer.cisco.com/docs/dna-center/#!delete-filter-group-association
notes:
  - SDK Method used are
    devices.Devices.delete_filter_group_association,
  - Paths used are
    delete /dna/intent/api/v1/filterGroupAassociations/{id},
"""

EXAMPLES = r"""
---
- name: Delete by id
  cisco.dnac.filter_group_aassociations_delete:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    headers: '{{my_headers | from_json}}'
    id: string
"""
RETURN = r"""
dnac_response:
  description: A dictionary or list with the response returned by the Cisco DNAC Python SDK
  returned: always
  type: dict
  sample: >
    {}
"""
