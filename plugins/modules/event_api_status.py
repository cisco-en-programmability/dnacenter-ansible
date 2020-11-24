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
module: event_api_status
short_description: Manage EventApiStatus objects of EventManagement
description:
- Get the Status of events API calls with provided executionId as mandatory path parameter.
version_added: '1.0'
author: first last (@GitHubID)
options:
  execution_id:
    description:
    - Execution ID.
    type: str
    required: True

requirements:
- dnacentersdk
seealso:
# Reference by module name
- module: cisco.dnac.plugins.module_utils.definitions.event_api_status
# Reference by Internet resource
- name: EventApiStatus reference
  description: Complete reference of the EventApiStatus object model.
  link: https://developer.cisco.com/docs/dna-center/api/1-3-3-x
# Reference by Internet resource
- name: EventApiStatus reference
  description: SDK reference.
  link: https://dnacentersdk.readthedocs.io/en/latest/api/api.html#v2-1-1-summary
"""

EXAMPLES = r"""
- name: get_status_api_for_events
  cisco.dnac.event_api_status
    dnac_host: dnac
    dnac_username: admin
    dnac_password: SomeSecretPassword
    state: query  # required
    execution_id: SomeValue  # string, required
  delegate_to: localhost
  register: query_result
  
"""

RETURN = """
get_status_api_for_events:
    description: Get the Status of events API calls with provided executionId as mandatory path parameter.
    returned: always
    type: dict
    contains:
    errorMessage:
      description: Error Message, property of the response body.
      returned: always
      type: dict
    apiStatus:
      description: Api Status, property of the response body.
      returned: always
      type: str
      sample: '<apistatus>'
    statusMessage:
      description: Status Message, property of the response body.
      returned: always
      type: str
      sample: '<statusmessage>'

"""
