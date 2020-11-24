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
module: events
short_description: Manage Events objects of EventManagement
description:
- Gets the list of registered Events with provided eventIds or tags as mandatory.
- Get the count of registered Events with provided eventIds or tags as mandatory.
version_added: '1.0'
author: first last (@GitHubID)
options:
  tags:
    description:
    - The registered Tags should be provided.
    type: str
    required: True
  event_id:
    description:
    - The registered EventId should be provided.
    type: str
  limit:
    description:
    - The number of Registries to limit in the resultset whose default value 10.
    type: int
  offset:
    description:
    - The number of Registries to offset in the resultset whose default value 0.
    type: int
  order:
    description:
    - Order query parameter.
    type: str
  sort_by:
    description:
    - SortBy field name.
    type: str
  count:
    description:
    - If true gets the number of objects.
    type: bool
    required: True

requirements:
- dnacentersdk
seealso:
# Reference by module name
- module: cisco.dnac.plugins.module_utils.definitions.events
# Reference by Internet resource
- name: Events reference
  description: Complete reference of the Events object model.
  link: https://developer.cisco.com/docs/dna-center/api/1-3-3-x
# Reference by Internet resource
- name: Events reference
  description: SDK reference.
  link: https://dnacentersdk.readthedocs.io/en/latest/api/api.html#v2-1-1-summary
"""

EXAMPLES = r"""
- name: get_events
  cisco.dnac.events
    dnac_host: dnac
    dnac_username: admin
    dnac_password: SomeSecretPassword
    state: query  # required
    tags: SomeValue  # string, required
    event_id: SomeValue  # string
    limit: 1  #  number
    offset: 1  #  number
    order: SomeValue  # string
    sort_by: SomeValue  # string
  delegate_to: localhost
  register: query_result
  
- name: count_of_events
  cisco.dnac.events
    dnac_host: dnac
    dnac_username: admin
    dnac_password: SomeSecretPassword
    state: query  # required
    tags: SomeValue  # string, required
    count: True  # boolean, required
    event_id: SomeValue  # string
  delegate_to: localhost
  register: query_result
  
"""

RETURN = """
get_events:
    description: Gets the list of registered Events with provided eventIds or tags as mandatory.
    returned: always
    type: dict
    contains:
    payload:
      description: It is the Events's payload.
      returned: always
      type: list
      contains:
        eventId:
          description: It is the Events's eventId.
          returned: always
          type: str
          sample: '<eventid>'
        nameSpace:
          description: It is the Events's nameSpace.
          returned: always
          type: str
          sample: '<namespace>'
        name:
          description: It is the Events's name.
          returned: always
          type: str
          sample: '<name>'
        description:
          description: It is the Events's description.
          returned: always
          type: str
          sample: '<description>'
        version:
          description: It is the Events's version.
          returned: always
          type: str
          sample: '1.0'
        category:
          description: It is the Events's category.
          returned: always
          type: str
          sample: '<category>'
        domain:
          description: It is the Events's domain.
          returned: always
          type: str
          sample: '<domain>'
        subDomain:
          description: It is the Events's subDomain.
          returned: always
          type: str
          sample: '<subdomain>'
        type:
          description: It is the Events's type.
          returned: always
          type: str
          sample: '<type>'
        tags:
          description: It is the Events's tags.
          returned: always
          type: list
        severity:
          description: It is the Events's severity.
          returned: always
          type: int
          sample: 0
        details:
          description: It is the Events's details.
          returned: always
          type: dict
        subscriptionTypes:
          description: It is the Events's subscriptionTypes.
          returned: always
          type: list


count_of_events:
    description: Get the count of registered Events with provided eventIds or tags as mandatory.
    returned: always
    type: dict
    contains:
    response:
      description: Response, property of the response body.
      returned: always
      type: int
      sample: 0

"""
