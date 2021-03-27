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
module: network_device
short_description: Manage NetworkDevice objects of Devices
description:
- Returns list of network devices based on filter criteria such as management IP address, mac address, hostname, location name and a wide variety of additional criteria. You can also use the asterisk in any value to conduct a wildcard search. For example, to find all hostnames beginning with myhost in the IP address range 192.25.18.n, issue the following request: GET fqdnoripofdnacenterplatform/dna/intent/api/v1/network-device? hostname=myhost* & managementIpAddress=192.25.18.* For a complete list of parameter names that you can use for filtering this request, see the DNA Center API Reference documentation. Note: If id parameter is provided, it will return the list of network-devices for the given ids and ignores the other request parameters.
- Adds the device with given credential.
- Sync the devices provided as input.
- Deletes the network device for the given Id.
- Returns the network device details for the given device ID.
- Returns brief summary of device info such as hostname, management IP address for the given device Id.
- Returns the list of network devices for the given pagination range.
- Returns the count of network devices based on the filter criteria by management IP address, mac address, hostname and location name.
- Returns the network device by specified IP address.
- Returns the network device with given serial number.
version_added: '1.0.0'
author: Rafael Campos (@racampos)
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
  error_description:
    description:
    - ErrorDescription query parameter.
    type: str
  family:
    description:
    - Family query parameter.
    type: str
  hostname:
    description:
    - Hostname query parameter.
    type: str
  id:
    description:
    - Accepts comma separated id's and return list of network-devices for the given id's. If invalid or not-found id's are provided, null entry will be returned in the list.
    - Device ID.
    - Required for states delete and query.
    type: str
  license_name:
    description:
    - License.name query parameter.
    type: str
  license_status:
    description:
    - License.status query parameter.
    type: str
  license_type:
    description:
    - License.type query parameter.
    type: str
  location:
    description:
    - Location query parameter.
    type: str
  location_name:
    description:
    - LocationName query parameter.
    type: str
  mac_address:
    description:
    - MacAddress query parameter.
    type: str
  management_ip_address:
    description:
    - ManagementIpAddress query parameter.
    type: str
  module_equpimenttype:
    description:
    - Module+equpimenttype query parameter.
    type: str
  module_name:
    description:
    - Module+name query parameter.
    type: str
  module_operationstatecode:
    description:
    - Module+operationstatecode query parameter.
    type: str
  module_partnumber:
    description:
    - Module+partnumber query parameter.
    type: str
  module_servicestate:
    description:
    - Module+servicestate query parameter.
    type: str
  module_vendorequipmenttype:
    description:
    - Module+vendorequipmenttype query parameter.
    type: str
  not_synced_for_minutes:
    description:
    - NotSyncedForMinutes query parameter.
    type: str
  platform_id:
    description:
    - PlatformId query parameter.
    type: str
  reachability_status:
    description:
    - ReachabilityStatus query parameter.
    type: str
  role:
    description:
    - Role query parameter.
    type: str
  serial_number:
    description:
    - SerialNumber query parameter.
    - Device serial number.
    - Required for state query.
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
    - InventoryDeviceInfo's type.
    type: str
  up_time:
    description:
    - UpTime query parameter.
    type: str
  cliTransport:
    description:
    - InventoryDeviceInfo's cliTransport.
    type: str
    required: True
  computeDevice:
    description:
    - InventoryDeviceInfo's computeDevice.
    type: bool
  enablePassword:
    description:
    - InventoryDeviceInfo's enablePassword.
    type: str
    required: True
  extendedDiscoveryInfo:
    description:
    - InventoryDeviceInfo's extendedDiscoveryInfo.
    type: str
  httpPassword:
    description:
    - InventoryDeviceInfo's httpPassword.
    type: str
  httpPort:
    description:
    - InventoryDeviceInfo's httpPort.
    type: str
  httpSecure:
    description:
    - InventoryDeviceInfo's httpSecure.
    type: bool
  httpUserName:
    description:
    - InventoryDeviceInfo's httpUserName.
    type: str
  ipAddress:
    description:
    - InventoryDeviceInfo's ipAddress (list of strings).
    type: list
    required: True
  merakiOrgId:
    description:
    - InventoryDeviceInfo's merakiOrgId (list of strings).
    type: list
  netconfPort:
    description:
    - InventoryDeviceInfo's netconfPort.
    type: str
  password:
    description:
    - InventoryDeviceInfo's password.
    type: str
    required: True
  serialNumber:
    description:
    - InventoryDeviceInfo's serialNumber.
    type: str
  snmpAuthPassphrase:
    description:
    - InventoryDeviceInfo's snmpAuthPassphrase.
    type: str
    required: True
  snmpAuthProtocol:
    description:
    - InventoryDeviceInfo's snmpAuthProtocol.
    type: str
    required: True
  snmpMode:
    description:
    - InventoryDeviceInfo's snmpMode.
    type: str
    required: True
  snmpPrivPassphrase:
    description:
    - InventoryDeviceInfo's snmpPrivPassphrase.
    type: str
    required: True
  snmpPrivProtocol:
    description:
    - InventoryDeviceInfo's snmpPrivProtocol.
    type: str
    required: True
  snmpROCommunity:
    description:
    - InventoryDeviceInfo's snmpROCommunity.
    type: str
    required: True
  snmpRWCommunity:
    description:
    - InventoryDeviceInfo's snmpRWCommunity.
    type: str
    required: True
  snmpRetry:
    description:
    - InventoryDeviceInfo's snmpRetry.
    type: int
    required: True
  snmpTimeout:
    description:
    - InventoryDeviceInfo's snmpTimeout.
    type: int
    required: True
  snmpUserName:
    description:
    - InventoryDeviceInfo's snmpUserName.
    type: str
    required: True
  snmpVersion:
    description:
    - InventoryDeviceInfo's snmpVersion.
    type: str
  updateMgmtIPaddressList:
    description:
    - InventoryDeviceInfo's updateMgmtIPaddressList (list of objects).
    type: list
    elements: dict
    suboptions:
      existMgmtIpAddress:
        description:
        - It is the network device's existMgmtIpAddress.
        type: str
      newMgmtIpAddress:
        description:
        - It is the network device's newMgmtIpAddress.
        type: str

  userName:
    description:
    - InventoryDeviceInfo's userName.
    type: str
    required: True
  is_force_delete:
    description:
    - IsForceDelete query parameter.
    type: bool
  summary:
    description:
    - If true gets the summary.
    - Required for state query.
    type: bool
  records_to_return:
    description:
    - Number of records to return.
    - Required for state query.
    type: int
  start_index:
    description:
    - Start index.
    - Required for state query.
    type: int
  count:
    description:
    - If true gets the number of objects.
    - Required for state query.
    type: bool
  ip_address:
    description:
    - Device IP address.
    - Required for state query.
    type: str

requirements:
- dnacentersdk
seealso:
# Reference by module name
- module: cisco.dnac.plugins.module_utils.definitions.network_device
# Reference by Internet resource
- name: NetworkDevice reference
  description: Complete reference of the NetworkDevice object model.
  link: https://developer.cisco.com/docs/dna-center/api/1-3-3-x
# Reference by Internet resource
- name: NetworkDevice reference
  description: SDK reference.
  link: https://dnacentersdk.readthedocs.io/en/latest/api/api.html#v2-1-1-summary
"""

EXAMPLES = r"""
- name: get_device_list
  cisco.dnac.network_device:
    state: query  # required
    associated_wlc_ip: SomeValue  # string
    collection_interval: SomeValue  # string
    collection_status: SomeValue  # string
    error_code: SomeValue  # string
    error_description: SomeValue  # string
    family: SomeValue  # string
    hostname: SomeValue  # string
    id: SomeValue  # string
    license_name: SomeValue  # string
    license_status: SomeValue  # string
    license_type: SomeValue  # string
    location: SomeValue  # string
    location_name: SomeValue  # string
    mac_address: SomeValue  # string
    management_ip_address: SomeValue  # string
    module_equpimenttype: SomeValue  # string
    module_name: SomeValue  # string
    module_operationstatecode: SomeValue  # string
    module_partnumber: SomeValue  # string
    module_servicestate: SomeValue  # string
    module_vendorequipmenttype: SomeValue  # string
    not_synced_for_minutes: SomeValue  # string
    platform_id: SomeValue  # string
    reachability_status: SomeValue  # string
    role: SomeValue  # string
    serial_number: SomeValue  # string
    series: SomeValue  # string
    software_type: SomeValue  # string
    software_version: SomeValue  # string
    type: SomeValue  # string
    up_time: SomeValue  # string
  register: query_result

- name: add_device
  cisco.dnac.network_device:
    state: create  # required
    cliTransport: SomeValue  # string, required
    enablePassword: SomeValue  # string, required
    ipAddress:  # required
    - SomeValue  # string
    password: SomeValue  # string, required
    snmpAuthPassphrase: SomeValue  # string, required
    snmpAuthProtocol: SomeValue  # string, required
    snmpMode: SomeValue  # string, required
    snmpPrivPassphrase: SomeValue  # string, required
    snmpPrivProtocol: SomeValue  # string, required
    snmpROCommunity: SomeValue  # string, required
    snmpRWCommunity: SomeValue  # string, required
    snmpRetry: 1  #  integer, required
    snmpTimeout: 1  #  integer, required
    snmpUserName: SomeValue  # string, required
    userName: SomeValue  # string, required
    computeDevice: True  # boolean
    extendedDiscoveryInfo: SomeValue  # string
    httpPassword: SomeValue  # string
    httpPort: SomeValue  # string
    httpSecure: True  # boolean
    httpUserName: SomeValue  # string
    merakiOrgId:
    - SomeValue  # string
    netconfPort: SomeValue  # string
    serialNumber: SomeValue  # string
    snmpVersion: SomeValue  # string
    type: SomeValue  # string, valid values: 'COMPUTE_DEVICE', 'MERAKI_DASHBOARD', 'NETWORK_DEVICE', 'NODATACHANGE'.
    updateMgmtIPaddressList:
    - existMgmtIpAddress: SomeValue  # string
      newMgmtIpAddress: SomeValue  # string

- name: sync_devices
  cisco.dnac.network_device:
    state: update  # required
    cliTransport: SomeValue  # string, required
    enablePassword: SomeValue  # string, required
    ipAddress:  # required
    - SomeValue  # string
    password: SomeValue  # string, required
    snmpAuthPassphrase: SomeValue  # string, required
    snmpAuthProtocol: SomeValue  # string, required
    snmpMode: SomeValue  # string, required
    snmpPrivPassphrase: SomeValue  # string, required
    snmpPrivProtocol: SomeValue  # string, required
    snmpROCommunity: SomeValue  # string, required
    snmpRWCommunity: SomeValue  # string, required
    snmpRetry: 1  #  integer, required
    snmpTimeout: 1  #  integer, required
    snmpUserName: SomeValue  # string, required
    userName: SomeValue  # string, required
    computeDevice: True  # boolean
    extendedDiscoveryInfo: SomeValue  # string
    httpPassword: SomeValue  # string
    httpPort: SomeValue  # string
    httpSecure: True  # boolean
    httpUserName: SomeValue  # string
    merakiOrgId:
    - SomeValue  # string
    netconfPort: SomeValue  # string
    serialNumber: SomeValue  # string
    snmpVersion: SomeValue  # string
    type: SomeValue  # string, valid values: 'COMPUTE_DEVICE', 'MERAKI_DASHBOARD', 'NETWORK_DEVICE', 'NODATACHANGE'.
    updateMgmtIPaddressList:
    - existMgmtIpAddress: SomeValue  # string
      newMgmtIpAddress: SomeValue  # string

- name: delete_device_by_id
  cisco.dnac.network_device:
    state: delete  # required
    id: SomeValue  # string, required
    is_force_delete: True  # boolean

- name: get_device_by_id
  cisco.dnac.network_device:
    state: query  # required
    id: SomeValue  # string, required
  register: query_result

- name: get_device_summary
  cisco.dnac.network_device:
    state: query  # required
    id: SomeValue  # string, required
    summary: True  # boolean, required
  register: query_result

- name: get_network_device_by_pagination_range
  cisco.dnac.network_device:
    state: query  # required
    records_to_return: 1  #  integer, required
    start_index: 1  #  integer, required
  register: query_result

- name: get_device_count
  cisco.dnac.network_device:
    state: query  # required
    count: True  # boolean, required
  register: query_result

- name: get_network_device_by_ip
  cisco.dnac.network_device:
    state: query  # required
    ip_address: SomeValue  # string, required
  register: query_result

- name: get_device_by_serial_number
  cisco.dnac.network_device:
    state: query  # required
    serial_number: SomeValue  # string, required
  register: query_result

"""

RETURN = """
"""
