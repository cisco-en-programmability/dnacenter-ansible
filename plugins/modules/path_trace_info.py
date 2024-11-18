#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)


DOCUMENTATION = r"""
---
module: path_trace_info
short_description: Information module for Path Trace Info
description:
- This module represents an alias of the module path_trace_v1_info
version_added: '3.1.0'
extends_documentation_fragment:
  - cisco.dnac.module_info
author: Rafael Campos (@racampos)
options:
  headers:
    description: Additional headers.
    type: dict
  periodicRefresh:
    description:
    - PeriodicRefresh query parameter. Is analysis periodically refreshed?.
    type: bool
  sourceIP:
    description:
    - SourceIP query parameter. Source IP address.
    type: str
  destIP:
    description:
    - DestIP query parameter. Destination IP address.
    type: str
  sourcePort:
    description:
    - SourcePort query parameter. Source port.
    type: float
  destPort:
    description:
    - DestPort query parameter. Destination port.
    type: float
  gtCreateTime:
    description:
    - GtCreateTime query parameter. Analyses requested after this time.
    type: float
  ltCreateTime:
    description:
    - LtCreateTime query parameter. Analyses requested before this time.
    type: float
  protocol:
    description:
    - Protocol query parameter.
    type: str
  status:
    description:
    - Status query parameter.
    type: str
  taskId:
    description:
    - TaskId query parameter. Task ID.
    type: str
  lastUpdateTime:
    description:
    - LastUpdateTime query parameter. Last update time.
    type: float
  limit:
    description:
    - Limit query parameter. Number of resources returned.
    type: float
  offset:
    description:
    - Offset query parameter. Start index of resources returned (1-based).
    type: float
  order:
    description:
    - Order query parameter. Order by this field.
    type: str
  sortBy:
    description:
    - SortBy query parameter. Sort by this field.
    type: str
  flowAnalysisId:
    description:
    - FlowAnalysisId path parameter. Flow analysis request id.
    type: str
requirements:
- dnacentersdk >= 2.4.9
- python >= 3.5
seealso:
- name: Cisco DNA Center documentation for Path Trace RetrievesAllPreviousPathtracesSummaryV1
  description: Complete reference of the RetrievesAllPreviousPathtracesSummaryV1 API.
  link: https://developer.cisco.com/docs/dna-center/#!retrieves-all-previous-pathtraces-summary-v-1
- name: Cisco DNA Center documentation for Path Trace RetrievesPreviousPathtraceV1
  description: Complete reference of the RetrievesPreviousPathtraceV1 API.
  link: https://developer.cisco.com/docs/dna-center/#!retrieves-previous-pathtrace-v-1
notes:
  - SDK Method used are
    path_trace.PathTrace.retrieves_all_previous_pathtraces_summary_v1,
    path_trace.PathTrace.retrieves_previous_pathtrace_v1,

  - Paths used are
    get /dna/intent/api/v1/flow-analysis,
    get /dna/intent/api/v1/flow-analysis/{flowAnalysisId},
  - It should be noted that this module is an alias of path_trace_v1_info

"""

EXAMPLES = r"""
- name: Get all Path Trace Info
  cisco.dnac.path_trace_info:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    headers: "{{my_headers | from_json}}"
    periodicRefresh: True
    sourceIP: string
    destIP: string
    sourcePort: 0
    destPort: 0
    gtCreateTime: 0
    ltCreateTime: 0
    protocol: string
    status: string
    taskId: string
    lastUpdateTime: 0
    limit: 0
    offset: 0
    order: string
    sortBy: string
  register: result

- name: Get Path Trace Info by id
  cisco.dnac.path_trace_info:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    headers: "{{my_headers | from_json}}"
    flowAnalysisId: string
  register: result

"""
RETURN = r"""
dnac_response:
  This alias returns the output of path_trace_v1_info.
"""
