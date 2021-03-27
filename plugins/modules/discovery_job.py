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
module: discovery_job
short_description: Manage DiscoveryJob objects of Discovery
description:
- Returns the list of discovery jobs for the given Discovery ID. The results can be optionally filtered based on IP. Discovery ID can be obtained using the "Get Discoveries by range" API.
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
  register: query_result
  
- name: get_discovery_jobs_by_ip
  cisco.dnac.discovery_job:
    state: query  # required
    ip_address: SomeValue  # string, required
    limit: 1  #  integer
    name: SomeValue  # string
    offset: 1  #  integer
  register: query_result
  
"""

RETURN = """
get_list_of_discoveries_by_discovery_id:
    description: Returns the list of discovery jobs for the given Discovery ID. The results can be optionally filtered based on IP. Discovery ID can be obtained using the "Get Discoveries by range" API.
    returned: always
    type: dict
    contains:
      response:
      description: Response, property of the response body (list of objects).
      returned: always
      type: list
      contains:
        attributeInfo:
          description: It is the discovery job's attributeInfo.
          returned: always
          type: dict
        cliStatus:
          description: It is the discovery job's cliStatus.
          returned: always
          type: str
          sample: '<clistatus>'
        discoveryStatus:
          description: It is the discovery job's discoveryStatus.
          returned: always
          type: str
          sample: '<discoverystatus>'
        endTime:
          description: It is the discovery job's endTime.
          returned: always
          type: str
          sample: '<endtime>'
        httpStatus:
          description: It is the discovery job's httpStatus.
          returned: always
          type: str
          sample: '<httpstatus>'
        id:
          description: It is the discovery job's id.
          returned: always
          type: str
          sample: '478012'
        inventoryCollectionStatus:
          description: It is the discovery job's inventoryCollectionStatus.
          returned: always
          type: str
          sample: '<inventorycollectionstatus>'
        inventoryReachabilityStatus:
          description: It is the discovery job's inventoryReachabilityStatus.
          returned: always
          type: str
          sample: '<inventoryreachabilitystatus>'
        ipAddress:
          description: It is the discovery job's ipAddress.
          returned: always
          type: str
          sample: '<ipaddress>'
        jobStatus:
          description: It is the discovery job's jobStatus.
          returned: always
          type: str
          sample: '<jobstatus>'
        name:
          description: It is the discovery job's name.
          returned: always
          type: str
          sample: '<name>'
        netconfStatus:
          description: It is the discovery job's netconfStatus.
          returned: always
          type: str
          sample: '<netconfstatus>'
        pingStatus:
          description: It is the discovery job's pingStatus.
          returned: always
          type: str
          sample: '<pingstatus>'
        snmpStatus:
          description: It is the discovery job's snmpStatus.
          returned: always
          type: str
          sample: '<snmpstatus>'
        startTime:
          description: It is the discovery job's startTime.
          returned: always
          type: str
          sample: '<starttime>'
        taskId:
          description: It is the discovery job's taskId.
          returned: always
          type: str
          sample: 'aeed229047801200e0ef563dbb9a71c2'

    version:
      description: Version, property of the response body.
      returned: always
      type: str
      sample: '1.0'

get_discovery_jobs_by_ip:
    description: Returns the list of discovery jobs for the given IP.
    returned: always
    type: dict
    contains:
      response:
      description: Response, property of the response body (list of objects).
      returned: always
      type: list
      contains:
        attributeInfo:
          description: It is the discovery job's attributeInfo.
          returned: always
          type: dict
        cliStatus:
          description: It is the discovery job's cliStatus.
          returned: always
          type: str
          sample: '<clistatus>'
        discoveryStatus:
          description: It is the discovery job's discoveryStatus.
          returned: always
          type: str
          sample: '<discoverystatus>'
        endTime:
          description: It is the discovery job's endTime.
          returned: always
          type: str
          sample: '<endtime>'
        httpStatus:
          description: It is the discovery job's httpStatus.
          returned: always
          type: str
          sample: '<httpstatus>'
        id:
          description: It is the discovery job's id.
          returned: always
          type: str
          sample: '478012'
        inventoryCollectionStatus:
          description: It is the discovery job's inventoryCollectionStatus.
          returned: always
          type: str
          sample: '<inventorycollectionstatus>'
        inventoryReachabilityStatus:
          description: It is the discovery job's inventoryReachabilityStatus.
          returned: always
          type: str
          sample: '<inventoryreachabilitystatus>'
        ipAddress:
          description: It is the discovery job's ipAddress.
          returned: always
          type: str
          sample: '<ipaddress>'
        jobStatus:
          description: It is the discovery job's jobStatus.
          returned: always
          type: str
          sample: '<jobstatus>'
        name:
          description: It is the discovery job's name.
          returned: always
          type: str
          sample: '<name>'
        netconfStatus:
          description: It is the discovery job's netconfStatus.
          returned: always
          type: str
          sample: '<netconfstatus>'
        pingStatus:
          description: It is the discovery job's pingStatus.
          returned: always
          type: str
          sample: '<pingstatus>'
        snmpStatus:
          description: It is the discovery job's snmpStatus.
          returned: always
          type: str
          sample: '<snmpstatus>'
        startTime:
          description: It is the discovery job's startTime.
          returned: always
          type: str
          sample: '<starttime>'
        taskId:
          description: It is the discovery job's taskId.
          returned: always
          type: str
          sample: 'aeed229047801200e0ef563dbb9a71c2'

    version:
      description: Version, property of the response body.
      returned: always
      type: str
      sample: '1.0'

"""
