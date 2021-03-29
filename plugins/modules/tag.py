#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright: (c) 2020, Rafael Campos <rcampos@altus.cr>
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

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
version_added: '1.0.0'
author: Rafael Campos (@racampos)
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
"""
