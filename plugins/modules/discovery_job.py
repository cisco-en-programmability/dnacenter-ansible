#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright: (c) 2020, Rafael Campos <rcampos@altus.cr>
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: discovery_job
short_description: Manage DiscoveryJob objects of Discovery
description:
- >
   Returns the list of discovery jobs for the given Discovery ID. The results can be optionally filtered based on IP.
   Discovery ID can be obtained using the "Get Discoveries by range" API.
- Returns the list of discovery jobs for the given IP.
version_added: '1.0.0'
author: Rafael Campos (@racampos)
options:
  id:
    description:
    - Discovery ID.
    type: str
    required: True
  ip_address:
    description:
    - IpAddress query parameter.
    - Required for state query.
    type: str
  limit:
    description:
    - Limit query parameter.
    type: int
  offset:
    description:
    - Offset query parameter.
    type: int
  name:
    description:
    - Name query parameter.
    type: str

requirements:
- dnacentersdk
seealso:
# Reference by module name
- module: cisco.dnac.plugins.module_utils.definitions.discovery_job
# Reference by Internet resource
- name: DiscoveryJob reference
  description: Complete reference of the DiscoveryJob object model.
  link: https://developer.cisco.com/docs/dna-center/api/1-3-3-x
# Reference by Internet resource
- name: DiscoveryJob reference
  description: SDK reference.
  link: https://dnacentersdk.readthedocs.io/en/latest/api/api.html#v2-1-1-summary
"""

EXAMPLES = r"""
- name: get_list_of_discoveries_by_discovery_id
  cisco.dnac.discovery_job:
    state: query  # required
    id: SomeValue  # string, required
    ip_address: SomeValue  # string
    limit: 1  #  integer
    offset: 1  #  integer
  register: nm_get_list_of_discoveries_by_discovery_id

- name: get_discovery_jobs_by_ip
  cisco.dnac.discovery_job:
    state: query  # required
    ip_address: SomeValue  # string, required
    limit: 1  #  integer
    name: SomeValue  # string
    offset: 1  #  integer
  register: nm_get_discovery_jobs_by_ip

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
  sample: discovery.get_discovery_jobs_by_ip
missing_params:
  description: Provided arguments do not comply with the schema of the DNA Center Python SDK function
  returned: when the function request schema is not satisfied
  type: list
  sample:
"""
