#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright: (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: flow_analysis
short_description: Manage FlowAnalysis objects of PathTrace
description:
- Returns a summary of all flow analyses stored. Results can be filtered by specified parameters.
- >
   Initiates a new flow analysis with periodic refresh and stat collection options. Returns a request id and a task
   id to get results and follow progress.
- Returns result of a previously requested flow analysis by its Flow Analysis id.
- Deletes a flow analysis request by its id.
version_added: '1.0.0'
author: Rafael Campos (@racampos)
options:
  dest_ip:
    description:
    - Destination IP address.
    type: str
  dest_port:
    description:
    - Destination port.
    type: str
  gt_create_time:
    description:
    - Analyses requested after this time.
    type: str
  last_update_time:
    description:
    - Last update time.
    type: str
  limit:
    description:
    - Number of resources returned.
    type: str
  lt_create_time:
    description:
    - Analyses requested before this time.
    type: str
  offset:
    description:
    - Start index of resources returned (1-based).
    type: str
  order:
    description:
    - Order by this field.
    type: str
  periodic_refresh:
    description:
    - Is analysis periodically refreshed?.
    type: bool
  protocol:
    description:
    - Protocol query parameter.
    - FlowAnalysisRequest's protocol.
    type: str
  sort_by:
    description:
    - Sort by this field.
    type: str
  source_ip:
    description:
    - Source IP address.
    type: str
  source_port:
    description:
    - Source port.
    type: str
  status:
    description:
    - Status query parameter.
    type: str
  task_id:
    description:
    - Task ID.
    type: str
  controlPath:
    description:
    - FlowAnalysisRequest's controlPath.
    type: bool
  destIP:
    description:
    - FlowAnalysisRequest's destIP.
    - Required for state create.
    type: str
  destPort:
    description:
    - FlowAnalysisRequest's destPort.
    type: str
  inclusions:
    description:
    - FlowAnalysisRequest's inclusions (list of strings).
    type: list
  periodicRefresh:
    description:
    - FlowAnalysisRequest's periodicRefresh.
    type: bool
  sourceIP:
    description:
    - FlowAnalysisRequest's sourceIP.
    - Required for state create.
    type: str
  sourcePort:
    description:
    - FlowAnalysisRequest's sourcePort.
    type: str
  flow_analysis_id:
    description:
    - Flow analysis request id.
    type: str
    required: True

requirements:
- dnacentersdk
seealso:
# Reference by module name
- module: cisco.dnac.plugins.module_utils.definitions.flow_analysis
# Reference by Internet resource
- name: FlowAnalysis reference
  description: Complete reference of the FlowAnalysis object model.
  link: https://developer.cisco.com/docs/dna-center/api/1-3-3-x
# Reference by Internet resource
- name: FlowAnalysis reference
  description: SDK reference.
  link: https://dnacentersdk.readthedocs.io/en/latest/api/api.html#v2-1-1-summary
"""

EXAMPLES = r"""
- name: retrives_all_previous_pathtraces_summary
  cisco.dnac.flow_analysis:
    state: query  # required
    dest_ip: SomeValue  # string
    dest_port: SomeValue  # string
    gt_create_time: SomeValue  # string
    last_update_time: SomeValue  # string
    limit: SomeValue  # string
    lt_create_time: SomeValue  # string
    offset: SomeValue  # string
    order: SomeValue  # string
    periodic_refresh: True  # boolean
    protocol: SomeValue  # string
    sort_by: SomeValue  # string
    source_ip: SomeValue  # string
    source_port: SomeValue  # string
    status: SomeValue  # string
    task_id: SomeValue  # string
  register: nm_retrives_all_previous_pathtraces_summary

- name: initiate_a_new_pathtrace
  cisco.dnac.flow_analysis:
    state: create  # required
    destIP: SomeValue  # string, required
    sourceIP: SomeValue  # string, required
    controlPath: True  # boolean
    destPort: SomeValue  # string
    inclusions:
    - SomeValue  # string
    periodicRefresh: True  # boolean
    protocol: SomeValue  # string
    sourcePort: SomeValue  # string

- name: retrieves_previous_pathtrace
  cisco.dnac.flow_analysis:
    state: query  # required
    flow_analysis_id: SomeValue  # string, required
  register: nm_retrieves_previous_pathtrace

- name: deletes_pathtrace_by_id
  cisco.dnac.flow_analysis:
    state: delete  # required
    flow_analysis_id: SomeValue  # string, required

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
  sample: path_trace.deletes_pathtrace_by_id
missing_params:
  description: Provided arguments do not comply with the schema of the DNA Center Python SDK function
  returned: when the function request schema is not satisfied
  type: list
  sample:
"""
