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
module: site
short_description: Manage Site objects of Sites
description:
- Get Site with area/building/floor with specified hierarchy.
- Creates Site with area/building/floor with specified hierarchy.
- Delete Site with area/building/floor by SiteId.
- Update Site area/building/floor with specified hierarchy and new values.
- API to get Site count.
version_added: '1.0'
author: first last (@GitHubID)
options:
  limit:
    description:
    - Number of Sites to be retrieved.
    type: str
  name:
    description:
    - SiteNameHierarchy (ex: global/groupName).
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
    - Required for states absent and present.
    type: str
  type:
    description:
    - Type (ex: area, building, floor).
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
  register: query_result
  
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
    type: SomeValue  # string, required, valid values: 'area', 'building', 'floor'.
  
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
    type: SomeValue  # string, required, valid values: 'area', 'building', 'floor'.
  
- name: get_site_count
  cisco.dnac.site:
    state: query  # required
    count: True  # boolean, required
    site_id: SomeValue  # string
  register: query_result
  
"""

RETURN = """
get_site:
    description: Get Site with area/building/floor with specified hierarchy.
    returned: always
    type: dict
    contains:
    response:
      description: Response, property of the response body (list of objects).
      returned: always
      type: list
      contains:
        parentId:
          description: It is the Site's parentId.
          returned: always
          type: str
          sample: '<parentid>'
        name:
          description: It is the Site's name.
          returned: always
          type: str
          sample: '<name>'
        additionalInfo:
          description: It is the Site's additionalInfo.
          returned: always
          type: list
        siteHierarchy:
          description: It is the Site's SiteHierarchy.
          returned: always
          type: str
          sample: '<sitehierarchy>'
        siteNameHierarchy:
          description: It is the Site's SiteNameHierarchy.
          returned: always
          type: str
          sample: '<sitenamehierarchy>'
        instanceTenantId:
          description: It is the Site's instanceTenantId.
          returned: always
          type: str
          sample: '<instancetenantid>'
        id:
          description: It is the Site's id.
          returned: always
          type: str
          sample: '478012'


create_site:
    description: Creates Site with area/building/floor with specified hierarchy.
    returned: success
    type: dict
    contains:
    executionId:
      description: Execution Id, property of the response body.
      returned: success
      type: str
      sample: '<executionid>'
    executionStatusUrl:
      description: Execution Status Url, property of the response body.
      returned: success
      type: str
      sample: '<executionstatusurl>'
    message:
      description: Message, property of the response body.
      returned: success
      type: str
      sample: '<message>'

delete_site:
    description: Delete Site with area/building/floor by SiteId.
    returned: success
    type: dict
    contains:
    status:
      description: Status, property of the response body.
      returned: success
      type: str
      sample: '<status>'
    message:
      description: Message, property of the response body.
      returned: success
      type: str
      sample: '<message>'

update_site:
    description: Update Site area/building/floor with specified hierarchy and new values.
    returned: changed
    type: dict
    contains:
    result:
      description: Result, property of the response body.
      returned: changed
      type: str
      sample: '<result>'
    response:
      description: Response, property of the response body.
      returned: changed
      type: dict
      contains:
        endTime:
          description: It is the Site's endTime.
          returned: changed
          type: str
          sample: '<endtime>'
        version:
          description: It is the Site's version.
          returned: changed
          type: str
          sample: '1.0'
        startTime:
          description: It is the Site's startTime.
          returned: changed
          type: str
          sample: '<starttime>'
        progress:
          description: It is the Site's progress.
          returned: changed
          type: str
          sample: '<progress>'
        data:
          description: It is the Site's data.
          returned: changed
          type: str
          sample: '<data>'
        serviceType:
          description: It is the Site's serviceType.
          returned: changed
          type: str
          sample: '<servicetype>'
        operationIdList:
          description: It is the Site's operationIdList.
          returned: changed
          type: list
        isError:
          description: It is the Site's isError.
          returned: changed
          type: str
          sample: '<iserror>'
        rootId:
          description: It is the Site's rootId.
          returned: changed
          type: str
          sample: '<rootid>'
        instanceTenantId:
          description: It is the Site's instanceTenantId.
          returned: changed
          type: str
          sample: '<instancetenantid>'
        id:
          description: It is the Site's id.
          returned: changed
          type: str
          sample: '478012'

    status:
      description: Status, property of the response body.
      returned: changed
      type: str
      sample: '<status>'

get_site_count:
    description: API to get Site count.
    returned: always
    type: dict
    contains:
    response:
      description: Response, property of the response body.
      returned: always
      type: str
      sample: '<response>'
    version:
      description: Version, property of the response body.
      returned: always
      type: str
      sample: '1.0'

"""
