#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)


DOCUMENTATION = r"""
---
module: configuration_template_info
short_description: Information module for Configuration Template Info
description:
- This module represents an alias of the module configuration_template_v1_info
version_added: '3.1.0'
extends_documentation_fragment:
  - cisco.dnac.module_info
author: Rafael Campos (@racampos)
options:
  headers:
    description: Additional headers.
    type: dict
  projectId:
    description:
    - ProjectId query parameter. Filter template(s) based on project UUID.
    type: str
  softwareType:
    description:
    - SoftwareType query parameter. Filter template(s) based software type.
    type: str
  softwareVersion:
    description:
    - SoftwareVersion query parameter. Filter template(s) based softwareVersion.
    type: str
  productFamily:
    description:
    - ProductFamily query parameter. Filter template(s) based on device family.
    type: str
  productSeries:
    description:
    - ProductSeries query parameter. Filter template(s) based on device series.
    type: str
  productType:
    description:
    - ProductType query parameter. Filter template(s) based on device type.
    type: str
  filterConflictingTemplates:
    description:
    - FilterConflictingTemplates query parameter. Filter template(s) based on confliting templates.
    type: bool
  tags:
    description:
    - Tags query parameter. Filter template(s) based on tags. 
    elements: str
    type: list
  projectNames:
    description:
    - ProjectNames query parameter. Filter template(s) based on project names. 
    elements: str
    type: list
  unCommitted:
    description:
    - UnCommitted query parameter. Filter template(s) based on template commited or not.
    type: bool
  sortOrder:
    description:
    - SortOrder query parameter. Sort Order Ascending (asc) or Descending (des).
    type: str
  templateId:
    description:
    - TemplateId path parameter. TemplateId(UUID) to get details of the template.
    type: str
  latestVersion:
    description:
    - LatestVersion query parameter. LatestVersion flag to get the latest versioned template.
    type: bool
requirements:
- dnacentersdk >= 2.4.9
- python >= 3.5
seealso:
- name: Cisco DNA Center documentation for Configuration Templates GetsDetailsOfAGivenTemplateV1
  description: Complete reference of the GetsDetailsOfAGivenTemplateV1 API.
  link: https://developer.cisco.com/docs/dna-center/#!gets-details-of-a-given-template-v-1
- name: Cisco DNA Center documentation for Configuration Templates GetsTheTemplatesAvailableV1
  description: Complete reference of the GetsTheTemplatesAvailableV1 API.
  link: https://developer.cisco.com/docs/dna-center/#!gets-the-templates-available-v-1
notes:
  - SDK Method used are
    configuration_templates.ConfigurationTemplates.get_template_details,
    configuration_templates.ConfigurationTemplates.gets_the_templates_available_v1,

  - Paths used are
    get /dna/intent/api/v1/template-programmer/template,
    get /dna/intent/api/v1/template-programmer/template/{templateId},
  - It should be noted that this module is an alias of configuration_template_v1_info

"""

EXAMPLES = r"""
- name: Get all Configuration Template Info
  cisco.dnac.configuration_template_info:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    headers: "{{my_headers | from_json}}"
    projectId: string
    softwareType: string
    softwareVersion: string
    productFamily: string
    productSeries: string
    productType: string
    filterConflictingTemplates: True
    tags: []
    projectNames: []
    unCommitted: True
    sortOrder: string
  register: result

- name: Get Configuration Template Info by id
  cisco.dnac.configuration_template_info:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    headers: "{{my_headers | from_json}}"
    latestVersion: True
    templateId: string
  register: result

"""
RETURN = r"""
dnac_response:
  This alias returns the output of configuration_template_v1_info.
"""
