#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright: (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: site
short_description: Manage Site objects of Sites
description:
- Get Site with area/building/floor with specified hierarchy.
- Creates Site with area/building/floor with specified hierarchy.
- Delete Site with area/building/floor by SiteId.
- Update Site area/building/floor with specified hierarchy and new values.
- API to get Site count.
version_added: '1.0.0'
author: Rafael Campos (@racampos)
options:
  limit:
    description:
    - Number of Sites to be retrieved.
    type: str
  name:
    description:
    - SiteNameHierarchy (ex global/groupName).
    type: str
  offset:
    description:
    - Offset/starting row.
    type: str
  site_id:
    description:
    - Site id to which Site details to retrieve.
    - Site id to which Site details to be deleted.
    - Site id to which Site details to be updated.
    - Site id to retrieve Site count.
    - Required for states present and absent.
    type: str
  type:
    description:
    - Type (ex area, building, floor).
    - Type, property of the request body.
    - Required for state present.
    type: str
  site:
    description:
    - Site, property of the request body.
    type: dict
    required: True
    suboptions:
      area:
        description:
        - It is the Site's area.
        type: dict
        suboptions:
          name:
            description:
            - It is the Site's name.
            type: str
          parentName:
            description:
            - It is the Site's parentName.
            type: str

      building:
        description:
        - It is the Site's building.
        type: dict
        suboptions:
          address:
            description:
            - It is the Site's address.
            type: str
          latitude:
            description:
            - It is the Site's latitude.
            type: int
          longitude:
            description:
            - It is the Site's longitude.
            type: int
          name:
            description:
            - It is the Site's name.
            type: str
          parentName:
            description:
            - It is the Site's parentName.
            type: str

      floor:
        description:
        - It is the Site's floor.
        type: dict
        suboptions:
          height:
            description:
            - It is the Site's height.
            type: int
          length:
            description:
            - It is the Site's length.
            type: int
          name:
            description:
            - It is the Site's name.
            type: str
          parentName:
            description:
            - It is the Site's parentName.
            type: str
          rfModel:
            description:
            - It is the Site's rfModel.
            type: str
          width:
            description:
            - It is the Site's width.
            type: int


  count:
    description:
    - If true gets the number of objects.
    - Required for state query.
    type: bool

requirements:
- dnacentersdk
seealso:
# Reference by module name
- module: cisco.dnac.plugins.module_utils.definitions.site
# Reference by Internet resource
- name: Site reference
  description: Complete reference of the Site object model.
  link: https://developer.cisco.com/docs/dna-center/api/1-3-3-x
# Reference by Internet resource
- name: Site reference
  description: SDK reference.
  link: https://dnacentersdk.readthedocs.io/en/latest/api/api.html#v2-1-1-summary
"""

EXAMPLES = r"""
- name: get_site
  cisco.dnac.site:
    state: query  # required
    limit: SomeValue  # string
    name: SomeValue  # string
    offset: SomeValue  # string
    site_id: SomeValue  # string
    type: SomeValue  # string
  register: nm_get_site

- name: create_site
  cisco.dnac.site:
    state: present  # required
    site:  # required
      area:
        name: SomeValue  # string
        parentName: SomeValue  # string
      building:
        name: SomeValue  # string
        address: SomeValue  # string
        parentName: SomeValue  # string
        latitude: 1  #  number
        longitude: 1  #  number
      floor:
        name: SomeValue  # string
        parentName: SomeValue  # string
        rfModel: SomeValue  # string
        width: 1  #  number
        length: 1  #  number
        height: 1  #  number
    type: # valid values are 'area',
      # 'building',
      # 'floor'.
      SomeValue  # string, required

- name: delete_site
  cisco.dnac.site:
    state: absent  # required
    site_id: SomeValue  # string, required

- name: update_site
  cisco.dnac.site:
    state: present  # required
    site_id: SomeValue  # string, required
    site:  # required
      area:
        name: SomeValue  # string
        parentName: SomeValue  # string
      building:
        name: SomeValue  # string
        address: SomeValue  # string
        parentName: SomeValue  # string
        latitude: 1  #  number
        longitude: 1  #  number
      floor:
        name: SomeValue  # string
        rfModel: SomeValue  # string
        width: 1  #  number
        length: 1  #  number
        height: 1  #  number
    type: # valid values are 'area',
      # 'building',
      # 'floor'.
      SomeValue  # string, required

- name: get_site_count
  cisco.dnac.site:
    state: query  # required
    count: True  # boolean, required
    site_id: SomeValue  # string
  register: nm_get_site_count

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
  sample: sites.create_site
missing_params:
  description: Provided arguments do not comply with the schema of the DNA Center Python SDK function
  returned: when the function request schema is not satisfied
  type: list
  sample:
"""
