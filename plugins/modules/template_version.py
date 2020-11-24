#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright: (c) 2020, first last <email>
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

ANSIBLE_METADATA = {
    "metadata_version": "0.0.1",
    "status": ["preview"],
    "supported_by": "community",
}

DOCUMENTATION = r"""
---
module: template_version
short_description: Manage TemplateVersion objects of ConfigurationTemplates
description:
- Creates Versioning for the current contents of the template.
- Returns the versions of a specified template.
version_added: '1.0'
author: first last (@GitHubID)
options:
  comments:
    description:
    - TemplateVersionRequestDTO's comments.
    type: str
  templateId:
    description:
    - TemplateVersionRequestDTO's templateId.
    type: str
  template_id:
    description:
    - TemplateId path parameter.
    - Required for state query.
    type: str

requirements:
- dnacentersdk
seealso:
# Reference by module name
- module: cisco.dnac.plugins.module_utils.definitions.template_version
# Reference by Internet resource
- name: TemplateVersion reference
  description: Complete reference of the TemplateVersion object model.
  link: https://developer.cisco.com/docs/dna-center/api/1-3-3-x
# Reference by Internet resource
- name: TemplateVersion reference
  description: SDK reference.
  link: https://dnacentersdk.readthedocs.io/en/latest/api/api.html#v2-1-1-summary
"""

EXAMPLES = r"""
- name: version_template
  cisco.dnac.template_version
    dnac_host: dnac
    dnac_username: admin
    dnac_password: SomeSecretPassword
    state: create  # required
    comments: SomeValue  # string
    templateId: SomeValue  # string
  delegate_to: localhost
  
- name: get_template_versions
  cisco.dnac.template_version
    dnac_host: dnac
    dnac_username: admin
    dnac_password: SomeSecretPassword
    state: query  # required
    template_id: SomeValue  # string, required
  delegate_to: localhost
  register: query_result
  
"""

RETURN = """
version_template:
    description: Creates Versioning for the current contents of the template.
    returned: success
    type: dict
    contains:
    response:
      description: TemplateVersionRequestDTO's response.
      returned: success
      type: dict
      contains:
        taskId:
          description: It is the template version's taskId.
          returned: success
          type: dict
        url:
          description: It is the template version's url.
          returned: success
          type: str
          sample: '<url>'

    version:
      description: TemplateVersionRequestDTO's version.
      returned: success
      type: str
      sample: '1.0'

get_template_versions:
    description: Returns the versions of a specified template.
    returned: always
    type: dict
    contains:
    payload:
      description: It is the template version's payload.
      returned: always
      type: list
      contains:
        name:
          description: It is the template version's name.
          returned: always
          type: str
          sample: '<name>'
        projectName:
          description: It is the template version's projectName.
          returned: always
          type: str
          sample: '<projectname>'
        projectId:
          description: It is the template version's projectId.
          returned: always
          type: str
          sample: '<projectid>'
        templateId:
          description: It is the template version's templateId.
          returned: always
          type: str
          sample: '<templateid>'
        versionsInfo:
          description: It is the template version's versionsInfo.
          returned: always
          type: list
          contains:
            id:
              description: It is the template version's id.
              returned: always
              type: str
              sample: '478012'
            description:
              description: It is the template version's description.
              returned: always
              type: str
              sample: '<description>'
            versionTime:
              description: It is the template version's versionTime.
              returned: always
              type: int
              sample: 0

        composite:
          description: It is the template version's composite.
          returned: always
          type: bool
          sample: false


"""
