#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)
DOCUMENTATION = r"""
---
module: path_trace
short_description: Resource module for Path Trace
description:
  - This module represents an alias of the module path_trace_v1
version_added: '3.1.0'
extends_documentation_fragment:
  - cisco.dnac.module
author: Rafael Campos (@racampos)
options:
  controlPath:
    description: Control path tracing.
    type: bool
  destIP:
    description: Destination IP address.
    type: str
  destPort:
    description: Destination Port, range 1-65535.
    type: str
  flowAnalysisId:
    description: FlowAnalysisId path parameter. Flow analysis request id.
    type: str
  inclusions:
    description: Subset of {INTERFACE-STATS, QOS-STATS, DEVICE-STATS, PERFORMANCE-STATS,
      ACL-TRACE}.
    elements: str
    type: list
  periodicRefresh:
    description: Periodic refresh of path for every 30 sec.
    type: bool
  protocol:
    description: Protocol - one of TCP, UDP - checks both when left blank.
    type: str
  sourceIP:
    description: Source IP address.
    type: str
  sourcePort:
    description: Source Port, range 1-65535.
    type: str
requirements:
  - dnacentersdk >= 2.4.9
  - python >= 3.5
seealso:
  - name: Cisco DNA Center documentation for Path Trace InitiateANewPathtraceV1
    description: Complete reference of the InitiateANewPathtraceV1 API.
    link: https://developer.cisco.com/docs/dna-center/#!initiate-a-new-pathtrace
  - name: Cisco DNA Center documentation for Path Trace DeletesPathtraceByIdV1
    description: Complete reference of the DeletesPathtraceByIdV1 API.
    link: https://developer.cisco.com/docs/dna-center/#!deletes-pathtrace-by-id
notes:
  - SDK Method used are path_trace.PathTrace.deletes_pathtrace_by_id_v1, path_trace.PathTrace.initiate_a_new_pathtrace_v1,
  - Paths used are post /dna/intent/api/v1/flow-analysis, delete /dna/intent/api/v1/flow-analysis/{flowAnalysisId},
  - It should be noted that this module is an alias of path_trace_v1
"""
EXAMPLES = r"""
- name: Create
  cisco.dnac.path_trace:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    state: present
    controlPath: true
    destIP: string
    destPort: string
    inclusions:
      - string
    periodicRefresh: true
    protocol: string
    sourceIP: string
    sourcePort: string
- name: Delete by id
  cisco.dnac.path_trace:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    state: absent
    flowAnalysisId: string
"""
RETURN = r"""
dnac_response:
  description: A dictionary or list with the response returned by the Cisco DNAC Python SDK
  returned: always
  type: dict
  sample: >
    {
      "response": {
        "flowAnalysisId": "string",
        "taskId": "string",
        "url": "string"
      },
      "version": "string"
    }
"""
