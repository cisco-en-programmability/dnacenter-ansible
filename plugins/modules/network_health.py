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
module: network_health
short_description: Manage NetworkHealth objects of Topology
description:
- Returns Overall Network Health information by Device category (Access, Distribution, Core, Router, Wireless) for any given point of time.
version_added: '1.0'
author: Rafael Campos (@racampos)
options:
  timestamp:
    description:
    - Epoch time(in milliseconds) when the Network health data is required.
    type: int

requirements:
- dnacentersdk
seealso:
# Reference by module name
- module: cisco.dnac.plugins.module_utils.definitions.network_health
# Reference by Internet resource
- name: NetworkHealth reference
  description: Complete reference of the NetworkHealth object model.
  link: https://developer.cisco.com/docs/dna-center/api/1-3-3-x
# Reference by Internet resource
- name: NetworkHealth reference
  description: SDK reference.
  link: https://dnacentersdk.readthedocs.io/en/latest/api/api.html#v2-1-1-summary
"""

EXAMPLES = r"""
- name: get_overall_network_health
  cisco.dnac.network_health:
    state: query  # required
    timestamp: 1  #  integer
  register: query_result
  
"""

RETURN = """
get_overall_network_health:
    description: Returns Overall Network Health information by Device category (Access, Distribution, Core, Router, Wireless) for any given point of time.
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
        time:
          description: It is the network health's time.
          returned: always
          type: str
          sample: '<time>'
        healthScore:
          description: It is the network health's healthScore.
          returned: always
          type: int
          sample: 0
        totalCount:
          description: It is the network health's totalCount.
          returned: always
          type: int
          sample: 0
        goodCount:
          description: It is the network health's goodCount.
          returned: always
          type: int
          sample: 0
        unmonCount:
          description: It is the network health's unmonCount.
          returned: always
          type: int
          sample: 0
        fairCount:
          description: It is the network health's fairCount.
          returned: always
          type: int
          sample: 0
        badCount:
          description: It is the network health's badCount.
          returned: always
          type: int
          sample: 0
        entity:
          description: It is the network health's entity.
          returned: always
          type: dict
        timeinMillis:
          description: It is the network health's timeinMillis.
          returned: always
          type: int
          sample: 0

    measuredBy:
      description: Measured By, property of the response body.
      returned: always
      type: str
      sample: '<measuredby>'
    latestMeasuredByEntity:
      description: Latest Measured By Entity, property of the response body.
      returned: always
      type: dict
    latestHealthScore:
      description: LatestHealthScore, property of the response body.
      returned: always
      type: int
      sample: 0
    monitoredDevices:
      description: MonitoredDevices, property of the response body.
      returned: always
      type: int
      sample: 0
    monitoredHealthyDevices:
      description: MonitoredHealthyDevices, property of the response body.
      returned: always
      type: int
      sample: 0
    monitoredUnHealthyDevices:
      description: MonitoredUnHealthyDevices, property of the response body.
      returned: always
      type: int
      sample: 0
    unMonitoredDevices:
      description: UnMonitoredDevices, property of the response body.
      returned: always
      type: int
      sample: 0
    healthDistirubution:
      description: Health Distirubution, property of the response body (list of objects).
      returned: always
      type: list
      contains:
        category:
          description: It is the network health's category.
          returned: always
          type: str
          sample: '<category>'
        totalCount:
          description: It is the network health's totalCount.
          returned: always
          type: int
          sample: 0
        healthScore:
          description: It is the network health's healthScore.
          returned: always
          type: int
          sample: 0
        goodPercentage:
          description: It is the network health's goodPercentage.
          returned: always
          type: int
          sample: 0
        badPercentage:
          description: It is the network health's badPercentage.
          returned: always
          type: int
          sample: 0
        fairPercentage:
          description: It is the network health's fairPercentage.
          returned: always
          type: int
          sample: 0
        unmonPercentage:
          description: It is the network health's unmonPercentage.
          returned: always
          type: int
          sample: 0
        goodCount:
          description: It is the network health's goodCount.
          returned: always
          type: int
          sample: 0
        badCount:
          description: It is the network health's badCount.
          returned: always
          type: int
          sample: 0
        fairCount:
          description: It is the network health's fairCount.
          returned: always
          type: int
          sample: 0
        unmonCount:
          description: It is the network health's unmonCount.
          returned: always
          type: int
          sample: 0
        kpiMetrics:
          description: It is the network health's kpiMetrics.
          returned: always
          type: list


"""
