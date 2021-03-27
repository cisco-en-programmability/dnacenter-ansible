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
module: discovery_network_device
short_description: Manage DiscoveryNetworkDevice objects of Discovery
description:
- Returns the network devices discovered for the given Discovery ID. Discovery ID can be obtained using the "Get Discoveries by range" API.
- Returns the network devices discovered for the given discovery and for the given range. The maximum number of records that can be retrieved is 500. Discovery ID can be obtained using the "Get Discoveries by range" API.
- Returns the count of network devices discovered in the given discovery. Discovery ID can be obtained using the "Get Discoveries by range" API.
- Returns the network devices from a discovery job based on given filters. Discovery ID can be obtained using the "Get Discoveries by range" API.
version_added: '1.0.0'
author: Rafael Campos (@racampos)
options:
  id:
    description:
    - Discovery ID.
    type: str
    required: True
  task_id:
    description:
    - TaskId query parameter.
    type: str
  records_to_return:
    description:
    - Number of records to return.
    type: int
    required: True
  start_index:
    description:
    - Start index.
    type: int
    required: True
  count:
    description:
    - If true gets the number of objects.
    type: bool
    required: True
  cli_status:
    description:
    - CliStatus query parameter.
    type: str
  http_status:
    description:
    - HttpStatus query parameter.
    type: str
  ip_address:
    description:
    - IpAddress query parameter.
    type: str
  netconf_status:
    description:
    - NetconfStatus query parameter.
    type: str
  ping_status:
    description:
    - PingStatus query parameter.
    type: str
  snmp_status:
    description:
    - SnmpStatus query parameter.
    type: str
  sort_by:
    description:
    - SortBy query parameter.
    type: str
  sort_order:
    description:
    - SortOrder query parameter.
    type: str
  summary:
    description:
    - If true gets the summary.
    type: bool
    required: True

requirements:
- dnacentersdk
seealso:
# Reference by module name
- module: cisco.dnac.plugins.module_utils.definitions.discovery_network_device
# Reference by Internet resource
- name: DiscoveryNetworkDevice reference
  description: Complete reference of the DiscoveryNetworkDevice object model.
  link: https://developer.cisco.com/docs/dna-center/api/1-3-3-x
# Reference by Internet resource
- name: DiscoveryNetworkDevice reference
  description: SDK reference.
  link: https://dnacentersdk.readthedocs.io/en/latest/api/api.html#v2-1-1-summary
"""

EXAMPLES = r"""
- name: get_discovered_network_devices_by_discovery_id
  cisco.dnac.discovery_network_device:
    state: query  # required
    id: SomeValue  # string, required
    task_id: SomeValue  # string
  register: query_result
  
- name: get_discovered_devices_by_range
  cisco.dnac.discovery_network_device:
    state: query  # required
    id: SomeValue  # string, required
    records_to_return: 1  #  integer, required
    start_index: 1  #  integer, required
    task_id: SomeValue  # string
  register: query_result
  
- name: get_devices_discovered_by_id
  cisco.dnac.discovery_network_device:
    state: query  # required
    id: SomeValue  # string, required
    count: True  # boolean, required
    task_id: SomeValue  # string
  register: query_result
  
- name: get_network_devices_from_discovery
  cisco.dnac.discovery_network_device:
    state: query  # required
    id: SomeValue  # string, required
    summary: True  # boolean, required
    cli_status: SomeValue  # string
    http_status: SomeValue  # string
    ip_address: SomeValue  # string
    netconf_status: SomeValue  # string
    ping_status: SomeValue  # string
    snmp_status: SomeValue  # string
    sort_by: SomeValue  # string
    sort_order: SomeValue  # string
    task_id: SomeValue  # string
  register: query_result
  
"""

RETURN = """
"""
