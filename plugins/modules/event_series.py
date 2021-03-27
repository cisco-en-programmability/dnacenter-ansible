#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright: (c) 2020, Rafael Campos <rcampos@altus.cr>
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

ANSIBLE_METADATA = {
    "metadata_version": "0.0.1",
    "status": ["preview"],
    "supported_by": "community",
}

DOCUMENTATION = r"""
---
module: event_series
short_description: Manage EventSeries objects of EventManagement
description:
- Get the list of Published Notifications.
- Get the Count of Published Notifications.
version_added: '1.0.0'
author: Rafael Campos (@racampos)
options:
  category:
    description:
    - Category .
    type: str
  domain:
    description:
    - Domain .
    type: str
  end_time:
    description:
    - EndTime .
    type: str
  event_ids:
    description:
    - The registered EventIds should be provided.
    type: str
  limit:
    description:
    - Limit whose default value 10.
    type: int
  offset:
    description:
    - Offset whose default value 0.
    type: int
  order:
    description:
    - Order query parameter.
    type: str
  severity:
    description:
    - Severity .
    type: str
  sort_by:
    description:
    - SortBy field name.
    type: str
  source:
    description:
    - Source .
    type: str
  start_time:
    description:
    - StartTime .
    type: str
  sub_domain:
    description:
    - SubDomain .
    type: str
  type:
    description:
    - Type .
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
- module: cisco.dnac.plugins.module_utils.definitions.event_series
# Reference by Internet resource
- name: EventSeries reference
  description: Complete reference of the EventSeries object model.
  link: https://developer.cisco.com/docs/dna-center/api/1-3-3-x
# Reference by Internet resource
- name: EventSeries reference
  description: SDK reference.
  link: https://dnacentersdk.readthedocs.io/en/latest/api/api.html#v2-1-1-summary
"""

EXAMPLES = r"""
- name: get_notifications
  cisco.dnac.event_series:
    state: query  # required
    category: SomeValue  # string
    domain: SomeValue  # string
    end_time: SomeValue  # string
    event_ids: SomeValue  # string
    limit: 1  #  number
    offset: 1  #  number
    order: SomeValue  # string
    severity: SomeValue  # string
    sort_by: SomeValue  # string
    source: SomeValue  # string
    start_time: SomeValue  # string
    sub_domain: SomeValue  # string
    type: SomeValue  # string
  register: query_result
  
- name: count_of_notifications
  cisco.dnac.event_series:
    state: query  # required
    count: True  # boolean, required
    category: SomeValue  # string
    domain: SomeValue  # string
    end_time: SomeValue  # string
    event_ids: SomeValue  # string
    severity: SomeValue  # string
    source: SomeValue  # string
    start_time: SomeValue  # string
    sub_domain: SomeValue  # string
    type: SomeValue  # string
  register: query_result
  
"""

RETURN = """
get_notifications:
    description: Get the list of Published Notifications.
    returned: always
    type: dict
    contains:
      instanceId:
      description: Instance Id, property of the response body.
      returned: always
      type: str
      sample: '<instanceid>'
    eventId:
      description: Event Id, property of the response body.
      returned: always
      type: str
      sample: '<eventid>'
    name:
      description: Name, property of the response body.
      returned: always
      type: str
      sample: '<name>'
    namespace:
      description: Namespace, property of the response body.
      returned: always
      type: str
      sample: '<namespace>'
    description:
      description: Description, property of the response body.
      returned: always
      type: str
      sample: '<description>'
    type:
      description: Type, property of the response body.
      returned: always
      type: str
      sample: '<type>'
    category:
      description: Category, property of the response body.
      returned: always
      type: str
      sample: '<category>'
    severity:
      description: Severity, property of the response body.
      returned: always
      type: int
      sample: 0
    timestamp:
      description: Timestamp, property of the response body.
      returned: always
      type: int
      sample: 0
    domain:
      description: Domain, property of the response body.
      returned: always
      type: str
      sample: '<domain>'
    subDomain:
      description: Sub Domain, property of the response body.
      returned: always
      type: str
      sample: '<subdomain>'
    source:
      description: Source, property of the response body.
      returned: always
      type: str
      sample: '<source>'
    context:
      description: Context, property of the response body.
      returned: always
      type: str
      sample: '<context>'
    details:
      description: Details, property of the response body.
      returned: always
      type: dict
    tenantId:
      description: Tenant Id, property of the response body.
      returned: always
      type: str
      sample: '<tenantid>'

count_of_notifications:
    description: Get the Count of Published Notifications.
    returned: always
    type: dict
    contains:
      response:
      description: Response, property of the response body.
      returned: always
      type: int
      sample: 0

"""
