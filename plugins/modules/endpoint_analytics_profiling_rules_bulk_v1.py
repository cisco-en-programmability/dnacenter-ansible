#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: endpoint_analytics_profiling_rules_bulk_v1
short_description: Resource module for Endpoint Analytics Profiling Rules Bulk V1
description:
  - Manage operation create of the resource Endpoint Analytics Profiling Rules Bulk
    V1.
  - >
    This API imports the given list of profiling rules. For each record, 1- If 'ruleType'
    for a record is not 'Custom
    Rule', then it is rejected. 2- If 'ruleId' is provided in the input record,.
version_added: '6.16.0'
extends_documentation_fragment:
  - cisco.dnac.module
author: Rafael Campos (@racampos)
options:
  profilingRules:
    description: Endpoint Analytics Profiling Rules Bulk's profilingRules.
    elements: dict
    suboptions:
      clusterId:
        description: Unique identifier for ML cluster. Only applicable for 'ML Rule'.
        type: str
      conditionGroups:
        description: Endpoint Analytics Profiling Rules Bulk's conditionGroups.
        suboptions:
          condition:
            description: Endpoint Analytics Profiling Rules Bulk's condition.
            suboptions:
              attribute:
                description: Endpoint Analytics Profiling Rules Bulk's attribute.
                type: str
              attributeDictionary:
                description: Endpoint Analytics Profiling Rules Bulk's attributeDictionary.
                type: str
              operator:
                description: Endpoint Analytics Profiling Rules Bulk's operator.
                type: str
              value:
                description: Endpoint Analytics Profiling Rules Bulk's value.
                type: str
            type: dict
          conditionGroup:
            description: Endpoint Analytics Profiling Rules Bulk's conditionGroup.
            elements: str
            type: list
          operator:
            description: Endpoint Analytics Profiling Rules Bulk's operator.
            type: str
          type:
            description: Endpoint Analytics Profiling Rules Bulk's type.
            type: str
        type: dict
      isDeleted:
        description: Flag to indicate whether the rule was deleted.
        type: bool
      lastModifiedBy:
        description: User that last modified the rule. It is read-only, and is ignored
          if provided as part of input request.
        type: str
      lastModifiedOn:
        description: Timestamp (in epoch milliseconds) of last modification. It is
          read-only, and is ignored if provided as part of input request.
        type: int
      pluginId:
        description: Plugin for the rule. Only applicable for 'Cisco Default' rules.
        type: str
      rejected:
        description: Flag to indicate whether rule has been rejected by user or not.
          Only applicable for 'ML Rule'.
        type: bool
      result:
        description: Endpoint Analytics Profiling Rules Bulk's result.
        suboptions:
          deviceType:
            description: List of device types determined by the current rule.
            elements: str
            type: list
          hardwareManufacturer:
            description: List of hardware manufacturers determined by the current
              rule.
            elements: str
            type: list
          hardwareModel:
            description: List of hardware models determined by the current rule.
            elements: str
            type: list
          operatingSystem:
            description: List of operating systems determined by the current rule.
            elements: str
            type: list
        type: dict
      ruleId:
        description: Unique identifier for the rule. This is normally generated by
          the system, and client does not need to provide it for rules that need to
          be newly created.
        type: str
      ruleName:
        description: Human readable name for the rule.
        type: str
      rulePriority:
        description: Priority for the rule.
        type: int
      ruleType:
        description: Type of the rule.
        type: str
      ruleVersion:
        description: Version of the rule.
        type: int
      sourcePriority:
        description: Source priority for the rule.
        type: int
      usedAttributes:
        description: List of attributes used in the rule. Only applicable for 'Cisco
          Default' rules.
        elements: str
        type: list
    type: list
requirements:
  - dnacentersdk >= 2.4.9
  - python >= 3.5
notes:
  - SDK Method used are a_i_endpoint_analytics.AIEndpointAnalytics.import_profiling_rules_in_bulk_v1,
  - Paths used are post /dna/intent/api/v1/endpoint-analytics/profiling-rules/bulk,
"""

EXAMPLES = r"""
- name: Create
  cisco.dnac.endpoint_analytics_profiling_rules_bulk_v1:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    profilingRules:
      - clusterId: string
        conditionGroups:
          condition:
            attribute: string
            attributeDictionary: string
            operator: string
            value: string
          conditionGroup:
            - string
          operator: string
          type: string
        isDeleted: true
        lastModifiedBy: string
        lastModifiedOn: 0
        pluginId: string
        rejected: true
        result:
          deviceType:
            - string
          hardwareManufacturer:
            - string
          hardwareModel:
            - string
          operatingSystem:
            - string
        ruleId: string
        ruleName: string
        rulePriority: 0
        ruleType: string
        ruleVersion: 0
        sourcePriority: 0
        usedAttributes:
          - string
"""
RETURN = r"""
dnac_response:
  description: A dictionary or list with the response returned by the Cisco DNAC Python SDK
  returned: always
  type: dict
  sample: >
    {}
"""
