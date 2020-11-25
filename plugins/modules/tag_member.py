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
module: tag_member
short_description: Manage TagMember objects of Tag
description:
- Returns tag members specified by id.
- Adds members to the tag specified by id.
- Removes Tag member from the tag specified by id.
- Returns the number of members in a given tag.
- Updates tag membership. As part of the request payload through this API, only the specified members are added / retained to the given input tags. Possible values of memberType attribute in the request payload can be queried by using the /tag/member/type API.
- Returns list of supported resource types.
version_added: '1.0'
author: first last (@GitHubID)
options:
  id:
    description:
    - Tag ID.
    type: str
    required: True
  member_type:
    description:
    - Entity type of the member. Possible values can be retrieved by using /tag/member/type API.
    - MemberType query parameter.
    type: str
    required: True
  level:
    description:
    - Level query parameter.
    type: str
  limit:
    description:
    - Used to Number of maximum members to return in the result.
    type: str
  member_association_type:
    description:
    - Indicates how the member is associated with the tag. Possible values and description. 1) DYNAMIC : The member is associated to the tag through rules. 2) STATIC – The member is associated to the tag manually. 3) MIXED – The member is associated manually and also satisfies the rule defined for the tag.
    - MemberAssociationType query parameter.
    type: str
  offset:
    description:
    - Used for pagination. It indicates the starting row number out of available member records.
    type: str
  member_id:
    description:
    - TagMember id to be removed from tag.
    - Required for state delete.
    type: str
  count:
    description:
    - If true gets the number of objects.
    - Required for state query.
    type: bool
  memberToTags:
    description:
    - TagMemberDTO's memberToTags.
    type: dict
    suboptions:
      key:
        description:
        - It is the tag member's key.
        type: list

  memberType:
    description:
    - TagMemberDTO's memberType.
    type: str

requirements:
- dnacentersdk
seealso:
# Reference by module name
- module: cisco.dnac.plugins.module_utils.definitions.tag_member
# Reference by Internet resource
- name: TagMember reference
  description: Complete reference of the TagMember object model.
  link: https://developer.cisco.com/docs/dna-center/api/1-3-3-x
# Reference by Internet resource
- name: TagMember reference
  description: SDK reference.
  link: https://dnacentersdk.readthedocs.io/en/latest/api/api.html#v2-1-1-summary
"""

EXAMPLES = r"""
- name: get_tag_members_by_id
  cisco.dnac.tag_member:
    state: query  # required
    id: SomeValue  # string, required
    member_type: SomeValue  # string, required
    level: SomeValue  # string
    limit: SomeValue  # string
    member_association_type: SomeValue  # string
    offset: SomeValue  # string
  register: query_result
  
- name: add_members_to_the_tag
  cisco.dnac.tag_member:
    state: create  # required
    id: SomeValue  # string, required
  
- name: remove_tag_member
  cisco.dnac.tag_member:
    state: delete  # required
    id: SomeValue  # string, required
    member_id: SomeValue  # string, required
  
- name: get_tag_member_count
  cisco.dnac.tag_member:
    state: query  # required
    id: SomeValue  # string, required
    member_type: SomeValue  # string, required
    count: True  # boolean, required
    level: SomeValue  # string
    member_association_type: SomeValue  # string
  register: query_result
  
- name: updates_tag_membership
  cisco.dnac.tag_member:
    state: update  # required
    memberToTags:
      key:
      - SomeValue  # string
    memberType: SomeValue  # string
  
- name: get_tag_resource_types
  cisco.dnac.tag_member:
    state: query  # required

  register: query_result
  
"""

RETURN = """
get_tag_members_by_id:
    description: Returns tag members specified by id.
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
        instanceUuid:
          description: It is the tag member's instanceUuid.
          returned: always
          type: str
          sample: '<instanceuuid>'


add_members_to_the_tag:
    description: Adds members to the tag specified by id.
    returned: success
    type: dict
    contains:
    version:
      description: List[entry«string,list«string»»]'s version.
      returned: success
      type: str
      sample: '1.0'
    response:
      description: List[entry«string,list«string»»]'s response.
      returned: success
      type: dict
      contains:
        taskId:
          description: It is the tag member's taskId.
          returned: success
          type: dict
        url:
          description: It is the tag member's url.
          returned: success
          type: str
          sample: '<url>'


remove_tag_member:
    description: Removes Tag member from the tag specified by id.
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
          description: It is the tag member's taskId.
          returned: success
          type: dict
        url:
          description: It is the tag member's url.
          returned: success
          type: str
          sample: '<url>'


get_tag_member_count:
    description: Returns the number of members in a given tag.
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

updates_tag_membership:
    description: Updates tag membership. As part of the request payload through this API, only the specified members are added / retained to the given input tags. Possible values of memberType attribute in the request payload can be queried by using the /tag/member/type API.
    returned: changed
    type: dict
    contains:
    version:
      description: TagMemberDTO's version.
      returned: changed
      type: str
      sample: '1.0'
    response:
      description: TagMemberDTO's response.
      returned: changed
      type: dict
      contains:
        taskId:
          description: It is the tag member's taskId.
          returned: changed
          type: dict
        url:
          description: It is the tag member's url.
          returned: changed
          type: str
          sample: '<url>'


get_tag_resource_types:
    description: Returns list of supported resource types.
    returned: always
    type: dict
    contains:
    version:
      description: Version, property of the response body.
      returned: always
      type: str
      sample: '1.0'
    response:
      description: Response, property of the response body (list of strings).
      returned: always
      type: list

"""
