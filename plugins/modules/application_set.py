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
module: application_set
short_description: Manage ApplicationSet objects of ApplicationPolicy
description:
- Delete existing application-set by it's id.
- Get appllication-sets by offset/limit or by name.
- Create new custom application-set/s.
- Get the number of existing application-sets.
version_added: '1.0'
author: first last (@GitHubID)
options:
  id:
    description:
    - Id query parameter.
    - Required for state delete.
    type: str
  limit:
    description:
    - Limit query parameter.
    type: int
  name:
    description:
    - Name query parameter.
    type: str
  offset:
    description:
    - Offset query parameter.
    type: int
  payload:
    description:
    - An object to send in the Request body.
    - Required for state create.
    type: list
    elements: dict
    suboptions:
      name:
        description:
        - It is the application set's name.
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
- module: cisco.dnac.plugins.module_utils.definitions.application_set
# Reference by Internet resource
- name: ApplicationSet reference
  description: Complete reference of the ApplicationSet object model.
  link: https://developer.cisco.com/docs/dna-center/api/1-3-3-x
# Reference by Internet resource
- name: ApplicationSet reference
  description: SDK reference.
  link: https://dnacentersdk.readthedocs.io/en/latest/api/api.html#v2-1-1-summary
"""

EXAMPLES = r"""
- name: delete_application_set
  cisco.dnac.application_set
    dnac_host: dnac
    dnac_username: admin
    dnac_password: SomeSecretPassword
    state: delete  # required
    id: SomeValue  # string, required
  delegate_to: localhost
  
- name: get_application_sets
  cisco.dnac.application_set
    dnac_host: dnac
    dnac_username: admin
    dnac_password: SomeSecretPassword
    state: query  # required
    limit: 1  #  number
    name: SomeValue  # string
    offset: 1  #  number
  delegate_to: localhost
  register: query_result
  
- name: create_application_set
  cisco.dnac.application_set
    dnac_host: dnac
    dnac_username: admin
    dnac_password: SomeSecretPassword
    state: create  # required
    payload:  # required
    - name: SomeValue  # string
  delegate_to: localhost
  
- name: get_application_sets_count
  cisco.dnac.application_set
    dnac_host: dnac
    dnac_username: admin
    dnac_password: SomeSecretPassword
    state: query  # required
    count: True  # boolean, required
  delegate_to: localhost
  register: query_result
  
"""

RETURN = """
delete_application_set:
    description: Delete existing application-set by it's id.
    returned: success
    type: dict
    contains:
    response:
      description: Response, property of the response body.
      returned: success
      type: dict
      contains:
        taskId:
          description: It is the application set's taskId.
          returned: success
          type: str
          sample: 'aeed229047801200e0ef563dbb9a71c2'
        url:
          description: It is the application set's url.
          returned: success
          type: str
          sample: '<url>'

    version:
      description: Version, property of the response body.
      returned: success
      type: str
      sample: '1.0'

get_application_sets:
    description: Get appllication-sets by offset/limit or by name.
    returned: always
    type: dict
    contains:
    response:
      description: Response, property of the response body (list of objects).
      returned: always
      type: list
      contains:
        id:
          description: It is the application set's id.
          returned: always
          type: str
          sample: '478012'
        identitySource:
          description: It is the application set's identitySource.
          returned: always
          type: dict
          contains:
            id:
              description: It is the application set's id.
              returned: always
              type: str
              sample: '478012'
            type:
              description: It is the application set's type.
              returned: always
              type: str
              sample: '<type>'

        name:
          description: It is the application set's name.
          returned: always
          type: str
          sample: '<name>'


create_application_set:
    description: Create new custom application-set/s.
    returned: success
    type: dict
    contains:
    response:
      description: Response, property of the response body.
      returned: success
      type: dict
      contains:
        taskId:
          description: It is the application set's taskId.
          returned: success
          type: str
          sample: 'aeed229047801200e0ef563dbb9a71c2'
        url:
          description: It is the application set's url.
          returned: success
          type: str
          sample: '<url>'

    version:
      description: Version, property of the response body.
      returned: success
      type: str
      sample: '1.0'

get_application_sets_count:
    description: Get the number of existing application-sets.
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
