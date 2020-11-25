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
module: tag
short_description: Manage Tag objects of Tag
description:
- Returns the Tags for given filter criteria.
- Creates Tag with specified Tag attributes.
- Updates a Tag specified by id.
- Deletes a Tag specified by id.
- Returns Tag specified by Id.
- Returns Tag count.
version_added: '1.0'
author: first last (@GitHubID)
options:
  additional_info_attributes:
    description:
    - AdditionalInfo.attributes query parameter.
    type: str
  additional_info_name_space:
    description:
    - AdditionalInfo.nameSpace query parameter.
    type: str
  field:
    description:
    - Available field names are :'name,id,parentId,type,additionalInfo.nameSpace,additionalInfo.attributes'.
    type: str
  level:
    description:
    - Level query parameter.
    type: str
  limit:
    description:
    - Limit query parameter.
    type: str
  name:
    description:
    - Tag name is mandatory when filter operation is used.
    - TagDTO's name.
    - Name query parameter.
    type: str
  offset:
    description:
    - Offset query parameter.
    type: str
  order:
    description:
    - Available values are asc and des.
    type: str
  size:
    description:
    - Size in kilobytes(KB).
    type: str
  sort_by:
    description:
    - Only supported attribute is name. SortyBy is mandatory when order is used.
    type: str
  system_tag:
    description:
    - SystemTag query parameter.
    type: str
  description:
    description:
    - TagDTO's description.
    type: str
  dynamicRules:
    description:
    - TagDTO's dynamicRules (list of objects).
    type: list
    elements: dict
    suboptions:
      memberType:
        description:
        - It is the Tag's memberType.
        type: str
      rules:
        description:
        - It is the Tag's rules.
        type: dict
        suboptions:
          items:
            description:
            - It is the Tag's items.
            type: list
          name:
            description:
            - It is the Tag's name.
            type: str
          operation:
            description:
            - It is the Tag's operation.
            type: str
          value:
            description:
            - It is the Tag's value.
            type: str
          values:
            description:
            - It is the Tag's values.
            type: list


  id:
    description:
    - TagDTO's id.
    - Tag ID.
    - Required for states absent and query.
    type: str
  instanceTenantId:
    description:
    - TagDTO's instanceTenantId.
    type: str
  systemTag:
    description:
    - TagDTO's systemTag.
    type: bool
  attribute_name:
    description:
    - AttributeName query parameter.
    type: str
  name_space:
    description:
    - NameSpace query parameter.
    type: str
  count:
    description:
    - If true gets the number of objects.
    - Required for state query.
    type: bool

requirements:
- dnacentersdk
seealso:
# Reference by module name
- module: cisco.dnac.plugins.module_utils.definitions.tag
# Reference by Internet resource
- name: Tag reference
  description: Complete reference of the Tag object model.
  link: https://developer.cisco.com/docs/dna-center/api/1-3-3-x
# Reference by Internet resource
- name: Tag reference
  description: SDK reference.
  link: https://dnacentersdk.readthedocs.io/en/latest/api/api.html#v2-1-1-summary
"""

EXAMPLES = r"""
- name: get_tag
  cisco.dnac.tag:
    state: query  # required
    additional_info_attributes: SomeValue  # string
    additional_info_name_space: SomeValue  # string
    field: SomeValue  # string
    level: SomeValue  # string
    limit: SomeValue  # string
    name: SomeValue  # string
    offset: SomeValue  # string
    order: SomeValue  # string
    size: SomeValue  # string
    sort_by: SomeValue  # string
    system_tag: SomeValue  # string
  register: query_result
  
- name: create_tag
  cisco.dnac.tag:
    state: present  # required
    description: SomeValue  # string
    dynamicRules:
    - memberType: SomeValue  # string
      rules:
        values:
        - SomeValue  # string
        items: None
        operation: SomeValue  # string
        name: SomeValue  # string
        value: SomeValue  # string
    id: SomeValue  # string
    instanceTenantId: SomeValue  # string
    name: SomeValue  # string
    systemTag: True  # boolean
  
- name: update_tag
  cisco.dnac.tag:
    state: present  # required
    description: SomeValue  # string
    dynamicRules:
    - memberType: SomeValue  # string
      rules:
        values:
        - SomeValue  # string
        items: None
        operation: SomeValue  # string
        name: SomeValue  # string
        value: SomeValue  # string
    id: SomeValue  # string
    instanceTenantId: SomeValue  # string
    name: SomeValue  # string
    systemTag: True  # boolean
  
- name: delete_tag
  cisco.dnac.tag:
    state: absent  # required
    id: SomeValue  # string, required
  
- name: get_tag_by_id
  cisco.dnac.tag:
    state: query  # required
    id: SomeValue  # string, required
  register: query_result
  
- name: get_tag_count
  cisco.dnac.tag:
    state: query  # required
    count: True  # boolean, required
    attribute_name: SomeValue  # string
    level: SomeValue  # string
    name: SomeValue  # string
    name_space: SomeValue  # string
    size: SomeValue  # string
    system_tag: SomeValue  # string
  register: query_result
  
"""

RETURN = """
get_tag:
    description: Returns the Tags for given filter criteria.
    returned: always
    type: dict
    contains:
    version:
      description: Version, property of the response body.
      returned: always
      type: str
      sample: '1.0'
    response:
      description: Response, property of the response body (list of objects).
      returned: always
      type: list
      contains:
        systemTag:
          description: It is the Tag's systemTag.
          returned: always
          type: bool
          sample: false
        description:
          description: It is the Tag's description.
          returned: always
          type: str
          sample: '<description>'
        dynamicRules:
          description: It is the Tag's dynamicRules.
          returned: always
          type: list
          contains:
            memberType:
              description: It is the Tag's memberType.
              returned: always
              type: str
              sample: '<membertype>'
            rules:
              description: It is the Tag's rules.
              returned: always
              type: dict
              contains:
                values:
                  description: It is the Tag's values.
                  returned: always
                  type: list
                items:
                  description: It is the Tag's items.
                  returned: always
                  type: list
                operation:
                  description: It is the Tag's operation.
                  returned: always
                  type: str
                  sample: '<operation>'
                name:
                  description: It is the Tag's name.
                  returned: always
                  type: str
                  sample: '<name>'
                value:
                  description: It is the Tag's value.
                  returned: always
                  type: str
                  sample: '<value>'


        name:
          description: It is the Tag's name.
          returned: always
          type: str
          sample: '<name>'
        id:
          description: It is the Tag's id.
          returned: always
          type: str
          sample: '478012'
        instanceTenantId:
          description: It is the Tag's instanceTenantId.
          returned: always
          type: str
          sample: '<instancetenantid>'


create_tag:
    description: Creates Tag with specified Tag attributes.
    returned: success
    type: dict
    contains:
    version:
      description: TagDTO's version.
      returned: success
      type: str
      sample: '1.0'
    response:
      description: TagDTO's response.
      returned: success
      type: dict
      contains:
        taskId:
          description: It is the Tag's taskId.
          returned: success
          type: dict
        url:
          description: It is the Tag's url.
          returned: success
          type: str
          sample: '<url>'


update_tag:
    description: Updates a Tag specified by id.
    returned: changed
    type: dict
    contains:
    version:
      description: TagDTO's version.
      returned: changed
      type: str
      sample: '1.0'
    response:
      description: TagDTO's response.
      returned: changed
      type: dict
      contains:
        taskId:
          description: It is the Tag's taskId.
          returned: changed
          type: dict
        url:
          description: It is the Tag's url.
          returned: changed
          type: str
          sample: '<url>'


delete_tag:
    description: Deletes a Tag specified by id.
    returned: success
    type: dict
    contains:
    version:
      description: Version, property of the response body.
      returned: success
      type: str
      sample: '1.0'
    response:
      description: Response, property of the response body.
      returned: success
      type: dict
      contains:
        taskId:
          description: It is the Tag's taskId.
          returned: success
          type: dict
        url:
          description: It is the Tag's url.
          returned: success
          type: str
          sample: '<url>'


get_tag_by_id:
    description: Returns Tag specified by Id.
    returned: always
    type: dict
    contains:
    version:
      description: Version, property of the response body.
      returned: always
      type: str
      sample: '1.0'
    response:
      description: Response, property of the response body.
      returned: always
      type: dict
      contains:
        systemTag:
          description: It is the Tag's systemTag.
          returned: always
          type: bool
          sample: false
        description:
          description: It is the Tag's description.
          returned: always
          type: str
          sample: '<description>'
        dynamicRules:
          description: It is the Tag's dynamicRules.
          returned: always
          type: list
          contains:
            memberType:
              description: It is the Tag's memberType.
              returned: always
              type: str
              sample: '<membertype>'
            rules:
              description: It is the Tag's rules.
              returned: always
              type: dict
              contains:
                values:
                  description: It is the Tag's values.
                  returned: always
                  type: list
                items:
                  description: It is the Tag's items.
                  returned: always
                  type: list
                operation:
                  description: It is the Tag's operation.
                  returned: always
                  type: str
                  sample: '<operation>'
                name:
                  description: It is the Tag's name.
                  returned: always
                  type: str
                  sample: '<name>'
                value:
                  description: It is the Tag's value.
                  returned: always
                  type: str
                  sample: '<value>'


        name:
          description: It is the Tag's name.
          returned: always
          type: str
          sample: '<name>'
        id:
          description: It is the Tag's id.
          returned: always
          type: str
          sample: '478012'
        instanceTenantId:
          description: It is the Tag's instanceTenantId.
          returned: always
          type: str
          sample: '<instancetenantid>'


get_tag_count:
    description: Returns Tag count.
    returned: always
    type: dict
    contains:
    version:
      description: Version, property of the response body.
      returned: always
      type: str
      sample: '1.0'
    response:
      description: Response, property of the response body.
      returned: always
      type: int
      sample: 0

"""
