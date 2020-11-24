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
module: network_device_autocomplete
short_description: Manage NetworkDeviceAutocomplete objects of Devices
description:
- Gets the list of first 500 network devices sorted lexicographically based on host name. It can be filtered using management IP address, mac address, hostname and location name. If id param is provided, it will be returning the list of network-devices for the given id's and other request params will be ignored. In case of autocomplete request, returns the list of specified attributes.
version_added: '1.0'
author: first last (@GitHubID)
options:
  associated_wlc_ip:
    description:
    - AssociatedWlcIp query parameter.
    type: str
  collection_interval:
    description:
    - CollectionInterval query parameter.
    type: str
  collection_status:
    description:
    - CollectionStatus query parameter.
    type: str
  error_code:
    description:
    - ErrorCode query parameter.
    type: str
  family:
    description:
    - Family query parameter.
    type: str
  hostname:
    description:
    - Hostname query parameter.
    type: str
  limit:
    description:
    - Limit query parameter.
    type: str
  mac_address:
    description:
    - MacAddress query parameter.
    type: str
  management_ip_address:
    description:
    - ManagementIpAddress query parameter.
    type: str
  offset:
    description:
    - Offset query parameter.
    type: str
  platform_id:
    description:
    - PlatformId query parameter.
    type: str
  reachability_failure_reason:
    description:
    - ReachabilityFailureReason query parameter.
    type: str
  reachability_status:
    description:
    - ReachabilityStatus query parameter.
    type: str
  role:
    description:
    - Role query parameter.
    type: str
  role_source:
    description:
    - RoleSource query parameter.
    type: str
  serial_number:
    description:
    - SerialNumber query parameter.
    type: str
  series:
    description:
    - Series query parameter.
    type: str
  software_type:
    description:
    - SoftwareType query parameter.
    type: str
  software_version:
    description:
    - SoftwareVersion query parameter.
    type: str
  type:
    description:
    - Type query parameter.
    type: str
  up_time:
    description:
    - UpTime query parameter.
    type: str
  vrf_name:
    description:
    - VrfName query parameter.
    type: str

requirements:
- dnacentersdk
seealso:
# Reference by module name
- module: cisco.dnac.plugins.module_utils.definitions.network_device_autocomplete
# Reference by Internet resource
- name: NetworkDeviceAutocomplete reference
  description: Complete reference of the NetworkDeviceAutocomplete object model.
  link: https://developer.cisco.com/docs/dna-center/api/1-3-3-x
# Reference by Internet resource
- name: NetworkDeviceAutocomplete reference
  description: SDK reference.
  link: https://dnacentersdk.readthedocs.io/en/latest/api/api.html#v2-1-1-summary
"""

EXAMPLES = r"""
- name: retrieves_all_network_devices
  cisco.dnac.network_device_autocomplete
    dnac_host: dnac
    dnac_username: admin
    dnac_password: SomeSecretPassword
    state: query  # required
    associated_wlc_ip: SomeValue  # string
    collection_interval: SomeValue  # string
    collection_status: SomeValue  # string
    error_code: SomeValue  # string
    family: SomeValue  # string
    hostname: SomeValue  # string
    limit: SomeValue  # string
    mac_address: SomeValue  # string
    management_ip_address: SomeValue  # string
    offset: SomeValue  # string
    platform_id: SomeValue  # string
    reachability_failure_reason: SomeValue  # string
    reachability_status: SomeValue  # string
    role: SomeValue  # string
    role_source: SomeValue  # string
    serial_number: SomeValue  # string
    series: SomeValue  # string
    software_type: SomeValue  # string
    software_version: SomeValue  # string
    type: SomeValue  # string
    up_time: SomeValue  # string
    vrf_name: SomeValue  # string
  delegate_to: localhost
  register: query_result
  
"""

RETURN = """
retrieves_all_network_devices:
    description: Gets the list of first 500 network devices sorted lexicographically based on host name. It can be filtered using management IP address, mac address, hostname and location name. If id param is provided, it will be returning the list of network-devices for the given id's and other request params will be ignored. In case of autocomplete request, returns the list of specified attributes.
    returned: always
    type: dict
    contains:

"""
