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
    - Required for states query and delete.
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
  cisco.dnac.network_device
    dnac_host: dnac
    dnac_username: admin
    dnac_password: SomeSecretPassword
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
  delegate_to: localhost
  register: query_result
  
- name: add_device
  cisco.dnac.network_device
    dnac_host: dnac
    dnac_username: admin
    dnac_password: SomeSecretPassword
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
  delegate_to: localhost
  
- name: sync_devices
  cisco.dnac.network_device
    dnac_host: dnac
    dnac_username: admin
    dnac_password: SomeSecretPassword
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
  delegate_to: localhost
  
- name: delete_device_by_id
  cisco.dnac.network_device
    dnac_host: dnac
    dnac_username: admin
    dnac_password: SomeSecretPassword
    state: delete  # required
    id: SomeValue  # string, required
    is_force_delete: True  # boolean
  delegate_to: localhost
  
- name: get_device_by_id
  cisco.dnac.network_device
    dnac_host: dnac
    dnac_username: admin
    dnac_password: SomeSecretPassword
    state: query  # required
    id: SomeValue  # string, required
  delegate_to: localhost
  register: query_result
  
- name: get_device_summary
  cisco.dnac.network_device
    dnac_host: dnac
    dnac_username: admin
    dnac_password: SomeSecretPassword
    state: query  # required
    id: SomeValue  # string, required
    summary: True  # boolean, required
  delegate_to: localhost
  register: query_result
  
- name: get_network_device_by_pagination_range
  cisco.dnac.network_device
    dnac_host: dnac
    dnac_username: admin
    dnac_password: SomeSecretPassword
    state: query  # required
    records_to_return: 1  #  integer, required
    start_index: 1  #  integer, required
  delegate_to: localhost
  register: query_result
  
- name: get_device_count
  cisco.dnac.network_device
    dnac_host: dnac
    dnac_username: admin
    dnac_password: SomeSecretPassword
    state: query  # required
    count: True  # boolean, required
  delegate_to: localhost
  register: query_result
  
- name: get_network_device_by_ip
  cisco.dnac.network_device
    dnac_host: dnac
    dnac_username: admin
    dnac_password: SomeSecretPassword
    state: query  # required
    ip_address: SomeValue  # string, required
  delegate_to: localhost
  register: query_result
  
- name: get_device_by_serial_number
  cisco.dnac.network_device
    dnac_host: dnac
    dnac_username: admin
    dnac_password: SomeSecretPassword
    state: query  # required
    serial_number: SomeValue  # string, required
  delegate_to: localhost
  register: query_result
  
"""

RETURN = """
get_device_list:
    description: Returns list of network devices based on filter criteria such as management IP address, mac address, hostname, location name and a wide variety of additional criteria. You can also use the asterisk in any value to conduct a wildcard search. For example, to find all hostnames beginning with myhost in the IP address range 192.25.18.n, issue the following request: GET fqdnoripofdnacenterplatform/dna/intent/api/v1/network-device? hostname=myhost* & managementIpAddress=192.25.18.* For a complete list of parameter names that you can use for filtering this request, see the DNA Center API Reference documentation. Note: If id parameter is provided, it will return the list of network-devices for the given ids and ignores the other request parameters.
    returned: always
    type: dict
    contains:
    response:
      description: Response, property of the response body (list of objects).
      returned: always
      type: list
      contains:
        apManagerInterfaceIp:
          description: It is the network device's apManagerInterfaceIp.
          returned: always
          type: str
          sample: '<apmanagerinterfaceip>'
        associatedWlcIp:
          description: It is the network device's associatedWlcIp.
          returned: always
          type: str
          sample: '<associatedwlcip>'
        bootDateTime:
          description: It is the network device's bootDateTime.
          returned: always
          type: str
          sample: '<bootdatetime>'
        collectionInterval:
          description: It is the network device's collectionInterval.
          returned: always
          type: str
          sample: '<collectioninterval>'
        collectionStatus:
          description: It is the network device's collectionStatus.
          returned: always
          type: str
          sample: '<collectionstatus>'
        errorCode:
          description: It is the network device's errorCode.
          returned: always
          type: str
          sample: '<errorcode>'
        errorDescription:
          description: It is the network device's errorDescription.
          returned: always
          type: str
          sample: '<errordescription>'
        family:
          description: It is the network device's family.
          returned: always
          type: str
          sample: '<family>'
        hostname:
          description: It is the network device's hostname.
          returned: always
          type: str
          sample: '<hostname>'
        id:
          description: It is the network device's id.
          returned: always
          type: str
          sample: '478012'
        instanceTenantId:
          description: It is the network device's instanceTenantId.
          returned: always
          type: str
          sample: '<instancetenantid>'
        instanceUuid:
          description: It is the network device's instanceUuid.
          returned: always
          type: str
          sample: '<instanceuuid>'
        interfaceCount:
          description: It is the network device's interfaceCount.
          returned: always
          type: str
          sample: '<interfacecount>'
        inventoryStatusDetail:
          description: It is the network device's inventoryStatusDetail.
          returned: always
          type: str
          sample: '<inventorystatusdetail>'
        lastUpdateTime:
          description: It is the network device's lastUpdateTime.
          returned: always
          type: str
          sample: '<lastupdatetime>'
        lastUpdated:
          description: It is the network device's lastUpdated.
          returned: always
          type: str
          sample: '<lastupdated>'
        lineCardCount:
          description: It is the network device's lineCardCount.
          returned: always
          type: str
          sample: '<linecardcount>'
        lineCardId:
          description: It is the network device's lineCardId.
          returned: always
          type: str
          sample: '<linecardid>'
        location:
          description: It is the network device's location.
          returned: always
          type: str
          sample: '<location>'
        locationName:
          description: It is the network device's locationName.
          returned: always
          type: str
          sample: '<locationname>'
        macAddress:
          description: It is the network device's macAddress.
          returned: always
          type: str
          sample: '<macaddress>'
        managementIpAddress:
          description: It is the network device's managementIpAddress.
          returned: always
          type: str
          sample: '<managementipaddress>'
        memorySize:
          description: It is the network device's memorySize.
          returned: always
          type: str
          sample: '<memorysize>'
        platformId:
          description: It is the network device's platformId.
          returned: always
          type: str
          sample: '<platformid>'
        reachabilityFailureReason:
          description: It is the network device's reachabilityFailureReason.
          returned: always
          type: str
          sample: '<reachabilityfailurereason>'
        reachabilityStatus:
          description: It is the network device's reachabilityStatus.
          returned: always
          type: str
          sample: '<reachabilitystatus>'
        role:
          description: It is the network device's role.
          returned: always
          type: str
          sample: '<role>'
        roleSource:
          description: It is the network device's roleSource.
          returned: always
          type: str
          sample: '<rolesource>'
        serialNumber:
          description: It is the network device's serialNumber.
          returned: always
          type: str
          sample: '<serialnumber>'
        series:
          description: It is the network device's series.
          returned: always
          type: str
          sample: '<series>'
        snmpContact:
          description: It is the network device's snmpContact.
          returned: always
          type: str
          sample: '<snmpcontact>'
        snmpLocation:
          description: It is the network device's snmpLocation.
          returned: always
          type: str
          sample: '<snmplocation>'
        softwareType:
          description: It is the network device's softwareType.
          returned: always
          type: str
          sample: '<softwaretype>'
        softwareVersion:
          description: It is the network device's softwareVersion.
          returned: always
          type: str
          sample: '<softwareversion>'
        tagCount:
          description: It is the network device's tagCount.
          returned: always
          type: str
          sample: '<tagcount>'
        tunnelUdpPort:
          description: It is the network device's tunnelUdpPort.
          returned: always
          type: str
          sample: '<tunneludpport>'
        type:
          description: It is the network device's type.
          returned: always
          type: str
          sample: '<type>'
        upTime:
          description: It is the network device's upTime.
          returned: always
          type: str
          sample: '<uptime>'
        waasDeviceMode:
          description: It is the network device's waasDeviceMode.
          returned: always
          type: str
          sample: '<waasdevicemode>'

    version:
      description: Version, property of the response body.
      returned: always
      type: str
      sample: '1.0'

add_device:
    description: Adds the device with given credential.
    returned: success
    type: dict
    contains:
    response:
      description: InventoryDeviceInfo's response.
      returned: success
      type: dict
      contains:
        taskId:
          description: It is the network device's taskId.
          returned: success
          type: dict
        url:
          description: It is the network device's url.
          returned: success
          type: str
          sample: '<url>'

    version:
      description: InventoryDeviceInfo's version.
      returned: success
      type: str
      sample: '1.0'

sync_devices:
    description: Sync the devices provided as input.
    returned: changed
    type: dict
    contains:
    response:
      description: InventoryDeviceInfo's response.
      returned: changed
      type: dict
      contains:
        taskId:
          description: It is the network device's taskId.
          returned: changed
          type: dict
        url:
          description: It is the network device's url.
          returned: changed
          type: str
          sample: '<url>'

    version:
      description: InventoryDeviceInfo's version.
      returned: changed
      type: str
      sample: '1.0'

delete_device_by_id:
    description: Deletes the network device for the given Id.
    returned: success
    type: dict
    contains:
    response:
      description: Response, property of the response body.
      returned: success
      type: dict
      contains:
        taskId:
          description: It is the network device's taskId.
          returned: success
          type: dict
        url:
          description: It is the network device's url.
          returned: success
          type: str
          sample: '<url>'

    version:
      description: Version, property of the response body.
      returned: success
      type: str
      sample: '1.0'

get_device_by_id:
    description: Returns the network device details for the given device ID.
    returned: always
    type: dict
    contains:
    response:
      description: Response, property of the response body.
      returned: always
      type: dict
      contains:
        apManagerInterfaceIp:
          description: It is the network device's apManagerInterfaceIp.
          returned: always
          type: str
          sample: '<apmanagerinterfaceip>'
        associatedWlcIp:
          description: It is the network device's associatedWlcIp.
          returned: always
          type: str
          sample: '<associatedwlcip>'
        bootDateTime:
          description: It is the network device's bootDateTime.
          returned: always
          type: str
          sample: '<bootdatetime>'
        collectionInterval:
          description: It is the network device's collectionInterval.
          returned: always
          type: str
          sample: '<collectioninterval>'
        collectionStatus:
          description: It is the network device's collectionStatus.
          returned: always
          type: str
          sample: '<collectionstatus>'
        errorCode:
          description: It is the network device's errorCode.
          returned: always
          type: str
          sample: '<errorcode>'
        errorDescription:
          description: It is the network device's errorDescription.
          returned: always
          type: str
          sample: '<errordescription>'
        family:
          description: It is the network device's family.
          returned: always
          type: str
          sample: '<family>'
        hostname:
          description: It is the network device's hostname.
          returned: always
          type: str
          sample: '<hostname>'
        id:
          description: It is the network device's id.
          returned: always
          type: str
          sample: '478012'
        instanceTenantId:
          description: It is the network device's instanceTenantId.
          returned: always
          type: str
          sample: '<instancetenantid>'
        instanceUuid:
          description: It is the network device's instanceUuid.
          returned: always
          type: str
          sample: '<instanceuuid>'
        interfaceCount:
          description: It is the network device's interfaceCount.
          returned: always
          type: str
          sample: '<interfacecount>'
        inventoryStatusDetail:
          description: It is the network device's inventoryStatusDetail.
          returned: always
          type: str
          sample: '<inventorystatusdetail>'
        lastUpdateTime:
          description: It is the network device's lastUpdateTime.
          returned: always
          type: str
          sample: '<lastupdatetime>'
        lastUpdated:
          description: It is the network device's lastUpdated.
          returned: always
          type: str
          sample: '<lastupdated>'
        lineCardCount:
          description: It is the network device's lineCardCount.
          returned: always
          type: str
          sample: '<linecardcount>'
        lineCardId:
          description: It is the network device's lineCardId.
          returned: always
          type: str
          sample: '<linecardid>'
        location:
          description: It is the network device's location.
          returned: always
          type: str
          sample: '<location>'
        locationName:
          description: It is the network device's locationName.
          returned: always
          type: str
          sample: '<locationname>'
        macAddress:
          description: It is the network device's macAddress.
          returned: always
          type: str
          sample: '<macaddress>'
        managementIpAddress:
          description: It is the network device's managementIpAddress.
          returned: always
          type: str
          sample: '<managementipaddress>'
        memorySize:
          description: It is the network device's memorySize.
          returned: always
          type: str
          sample: '<memorysize>'
        platformId:
          description: It is the network device's platformId.
          returned: always
          type: str
          sample: '<platformid>'
        reachabilityFailureReason:
          description: It is the network device's reachabilityFailureReason.
          returned: always
          type: str
          sample: '<reachabilityfailurereason>'
        reachabilityStatus:
          description: It is the network device's reachabilityStatus.
          returned: always
          type: str
          sample: '<reachabilitystatus>'
        role:
          description: It is the network device's role.
          returned: always
          type: str
          sample: '<role>'
        roleSource:
          description: It is the network device's roleSource.
          returned: always
          type: str
          sample: '<rolesource>'
        serialNumber:
          description: It is the network device's serialNumber.
          returned: always
          type: str
          sample: '<serialnumber>'
        series:
          description: It is the network device's series.
          returned: always
          type: str
          sample: '<series>'
        snmpContact:
          description: It is the network device's snmpContact.
          returned: always
          type: str
          sample: '<snmpcontact>'
        snmpLocation:
          description: It is the network device's snmpLocation.
          returned: always
          type: str
          sample: '<snmplocation>'
        softwareType:
          description: It is the network device's softwareType.
          returned: always
          type: str
          sample: '<softwaretype>'
        softwareVersion:
          description: It is the network device's softwareVersion.
          returned: always
          type: str
          sample: '<softwareversion>'
        tagCount:
          description: It is the network device's tagCount.
          returned: always
          type: str
          sample: '<tagcount>'
        tunnelUdpPort:
          description: It is the network device's tunnelUdpPort.
          returned: always
          type: str
          sample: '<tunneludpport>'
        type:
          description: It is the network device's type.
          returned: always
          type: str
          sample: '<type>'
        upTime:
          description: It is the network device's upTime.
          returned: always
          type: str
          sample: '<uptime>'
        waasDeviceMode:
          description: It is the network device's waasDeviceMode.
          returned: always
          type: str
          sample: '<waasdevicemode>'

    version:
      description: Version, property of the response body.
      returned: always
      type: str
      sample: '1.0'

get_device_summary:
    description: Returns brief summary of device info such as hostname, management IP address for the given device Id.
    returned: always
    type: dict
    contains:
    response:
      description: Response, property of the response body.
      returned: always
      type: dict
      contains:
        id:
          description: It is the network device's id.
          returned: always
          type: str
          sample: '478012'
        role:
          description: It is the network device's role.
          returned: always
          type: str
          sample: '<role>'
        roleSource:
          description: It is the network device's roleSource.
          returned: always
          type: str
          sample: '<rolesource>'

    version:
      description: Version, property of the response body.
      returned: always
      type: str
      sample: '1.0'

get_network_device_by_pagination_range:
    description: Returns the list of network devices for the given pagination range.
    returned: always
    type: dict
    contains:
    response:
      description: Response, property of the response body (list of objects).
      returned: always
      type: list
      contains:
        apManagerInterfaceIp:
          description: It is the network device's apManagerInterfaceIp.
          returned: always
          type: str
          sample: '<apmanagerinterfaceip>'
        associatedWlcIp:
          description: It is the network device's associatedWlcIp.
          returned: always
          type: str
          sample: '<associatedwlcip>'
        bootDateTime:
          description: It is the network device's bootDateTime.
          returned: always
          type: str
          sample: '<bootdatetime>'
        collectionInterval:
          description: It is the network device's collectionInterval.
          returned: always
          type: str
          sample: '<collectioninterval>'
        collectionStatus:
          description: It is the network device's collectionStatus.
          returned: always
          type: str
          sample: '<collectionstatus>'
        errorCode:
          description: It is the network device's errorCode.
          returned: always
          type: str
          sample: '<errorcode>'
        errorDescription:
          description: It is the network device's errorDescription.
          returned: always
          type: str
          sample: '<errordescription>'
        family:
          description: It is the network device's family.
          returned: always
          type: str
          sample: '<family>'
        hostname:
          description: It is the network device's hostname.
          returned: always
          type: str
          sample: '<hostname>'
        id:
          description: It is the network device's id.
          returned: always
          type: str
          sample: '478012'
        instanceTenantId:
          description: It is the network device's instanceTenantId.
          returned: always
          type: str
          sample: '<instancetenantid>'
        instanceUuid:
          description: It is the network device's instanceUuid.
          returned: always
          type: str
          sample: '<instanceuuid>'
        interfaceCount:
          description: It is the network device's interfaceCount.
          returned: always
          type: str
          sample: '<interfacecount>'
        inventoryStatusDetail:
          description: It is the network device's inventoryStatusDetail.
          returned: always
          type: str
          sample: '<inventorystatusdetail>'
        lastUpdateTime:
          description: It is the network device's lastUpdateTime.
          returned: always
          type: str
          sample: '<lastupdatetime>'
        lastUpdated:
          description: It is the network device's lastUpdated.
          returned: always
          type: str
          sample: '<lastupdated>'
        lineCardCount:
          description: It is the network device's lineCardCount.
          returned: always
          type: str
          sample: '<linecardcount>'
        lineCardId:
          description: It is the network device's lineCardId.
          returned: always
          type: str
          sample: '<linecardid>'
        location:
          description: It is the network device's location.
          returned: always
          type: str
          sample: '<location>'
        locationName:
          description: It is the network device's locationName.
          returned: always
          type: str
          sample: '<locationname>'
        macAddress:
          description: It is the network device's macAddress.
          returned: always
          type: str
          sample: '<macaddress>'
        managementIpAddress:
          description: It is the network device's managementIpAddress.
          returned: always
          type: str
          sample: '<managementipaddress>'
        memorySize:
          description: It is the network device's memorySize.
          returned: always
          type: str
          sample: '<memorysize>'
        platformId:
          description: It is the network device's platformId.
          returned: always
          type: str
          sample: '<platformid>'
        reachabilityFailureReason:
          description: It is the network device's reachabilityFailureReason.
          returned: always
          type: str
          sample: '<reachabilityfailurereason>'
        reachabilityStatus:
          description: It is the network device's reachabilityStatus.
          returned: always
          type: str
          sample: '<reachabilitystatus>'
        role:
          description: It is the network device's role.
          returned: always
          type: str
          sample: '<role>'
        roleSource:
          description: It is the network device's roleSource.
          returned: always
          type: str
          sample: '<rolesource>'
        serialNumber:
          description: It is the network device's serialNumber.
          returned: always
          type: str
          sample: '<serialnumber>'
        series:
          description: It is the network device's series.
          returned: always
          type: str
          sample: '<series>'
        snmpContact:
          description: It is the network device's snmpContact.
          returned: always
          type: str
          sample: '<snmpcontact>'
        snmpLocation:
          description: It is the network device's snmpLocation.
          returned: always
          type: str
          sample: '<snmplocation>'
        softwareType:
          description: It is the network device's softwareType.
          returned: always
          type: str
          sample: '<softwaretype>'
        softwareVersion:
          description: It is the network device's softwareVersion.
          returned: always
          type: str
          sample: '<softwareversion>'
        tagCount:
          description: It is the network device's tagCount.
          returned: always
          type: str
          sample: '<tagcount>'
        tunnelUdpPort:
          description: It is the network device's tunnelUdpPort.
          returned: always
          type: str
          sample: '<tunneludpport>'
        type:
          description: It is the network device's type.
          returned: always
          type: str
          sample: '<type>'
        upTime:
          description: It is the network device's upTime.
          returned: always
          type: str
          sample: '<uptime>'
        waasDeviceMode:
          description: It is the network device's waasDeviceMode.
          returned: always
          type: str
          sample: '<waasdevicemode>'

    version:
      description: Version, property of the response body.
      returned: always
      type: str
      sample: '1.0'

get_device_count:
    description: Returns the count of network devices based on the filter criteria by management IP address, mac address, hostname and location name.
    returned: always
    type: dict
    contains:
    response:
      description: Response, property of the response body.
      returned: always
      type: int
      sample: 0
    version:
      description: Version, property of the response body.
      returned: always
      type: str
      sample: '1.0'

get_network_device_by_ip:
    description: Returns the network device by specified IP address.
    returned: always
    type: dict
    contains:
    response:
      description: Response, property of the response body.
      returned: always
      type: dict
      contains:
        apManagerInterfaceIp:
          description: It is the network device's apManagerInterfaceIp.
          returned: always
          type: str
          sample: '<apmanagerinterfaceip>'
        associatedWlcIp:
          description: It is the network device's associatedWlcIp.
          returned: always
          type: str
          sample: '<associatedwlcip>'
        bootDateTime:
          description: It is the network device's bootDateTime.
          returned: always
          type: str
          sample: '<bootdatetime>'
        collectionInterval:
          description: It is the network device's collectionInterval.
          returned: always
          type: str
          sample: '<collectioninterval>'
        collectionStatus:
          description: It is the network device's collectionStatus.
          returned: always
          type: str
          sample: '<collectionstatus>'
        errorCode:
          description: It is the network device's errorCode.
          returned: always
          type: str
          sample: '<errorcode>'
        errorDescription:
          description: It is the network device's errorDescription.
          returned: always
          type: str
          sample: '<errordescription>'
        family:
          description: It is the network device's family.
          returned: always
          type: str
          sample: '<family>'
        hostname:
          description: It is the network device's hostname.
          returned: always
          type: str
          sample: '<hostname>'
        id:
          description: It is the network device's id.
          returned: always
          type: str
          sample: '478012'
        instanceTenantId:
          description: It is the network device's instanceTenantId.
          returned: always
          type: str
          sample: '<instancetenantid>'
        instanceUuid:
          description: It is the network device's instanceUuid.
          returned: always
          type: str
          sample: '<instanceuuid>'
        interfaceCount:
          description: It is the network device's interfaceCount.
          returned: always
          type: str
          sample: '<interfacecount>'
        inventoryStatusDetail:
          description: It is the network device's inventoryStatusDetail.
          returned: always
          type: str
          sample: '<inventorystatusdetail>'
        lastUpdateTime:
          description: It is the network device's lastUpdateTime.
          returned: always
          type: str
          sample: '<lastupdatetime>'
        lastUpdated:
          description: It is the network device's lastUpdated.
          returned: always
          type: str
          sample: '<lastupdated>'
        lineCardCount:
          description: It is the network device's lineCardCount.
          returned: always
          type: str
          sample: '<linecardcount>'
        lineCardId:
          description: It is the network device's lineCardId.
          returned: always
          type: str
          sample: '<linecardid>'
        location:
          description: It is the network device's location.
          returned: always
          type: str
          sample: '<location>'
        locationName:
          description: It is the network device's locationName.
          returned: always
          type: str
          sample: '<locationname>'
        macAddress:
          description: It is the network device's macAddress.
          returned: always
          type: str
          sample: '<macaddress>'
        managementIpAddress:
          description: It is the network device's managementIpAddress.
          returned: always
          type: str
          sample: '<managementipaddress>'
        memorySize:
          description: It is the network device's memorySize.
          returned: always
          type: str
          sample: '<memorysize>'
        platformId:
          description: It is the network device's platformId.
          returned: always
          type: str
          sample: '<platformid>'
        reachabilityFailureReason:
          description: It is the network device's reachabilityFailureReason.
          returned: always
          type: str
          sample: '<reachabilityfailurereason>'
        reachabilityStatus:
          description: It is the network device's reachabilityStatus.
          returned: always
          type: str
          sample: '<reachabilitystatus>'
        role:
          description: It is the network device's role.
          returned: always
          type: str
          sample: '<role>'
        roleSource:
          description: It is the network device's roleSource.
          returned: always
          type: str
          sample: '<rolesource>'
        serialNumber:
          description: It is the network device's serialNumber.
          returned: always
          type: str
          sample: '<serialnumber>'
        series:
          description: It is the network device's series.
          returned: always
          type: str
          sample: '<series>'
        snmpContact:
          description: It is the network device's snmpContact.
          returned: always
          type: str
          sample: '<snmpcontact>'
        snmpLocation:
          description: It is the network device's snmpLocation.
          returned: always
          type: str
          sample: '<snmplocation>'
        softwareType:
          description: It is the network device's softwareType.
          returned: always
          type: str
          sample: '<softwaretype>'
        softwareVersion:
          description: It is the network device's softwareVersion.
          returned: always
          type: str
          sample: '<softwareversion>'
        tagCount:
          description: It is the network device's tagCount.
          returned: always
          type: str
          sample: '<tagcount>'
        tunnelUdpPort:
          description: It is the network device's tunnelUdpPort.
          returned: always
          type: str
          sample: '<tunneludpport>'
        type:
          description: It is the network device's type.
          returned: always
          type: str
          sample: '<type>'
        upTime:
          description: It is the network device's upTime.
          returned: always
          type: str
          sample: '<uptime>'
        waasDeviceMode:
          description: It is the network device's waasDeviceMode.
          returned: always
          type: str
          sample: '<waasdevicemode>'

    version:
      description: Version, property of the response body.
      returned: always
      type: str
      sample: '1.0'

get_device_by_serial_number:
    description: Returns the network device with given serial number.
    returned: always
    type: dict
    contains:
    response:
      description: Response, property of the response body.
      returned: always
      type: dict
      contains:
        apManagerInterfaceIp:
          description: It is the network device's apManagerInterfaceIp.
          returned: always
          type: str
          sample: '<apmanagerinterfaceip>'
        associatedWlcIp:
          description: It is the network device's associatedWlcIp.
          returned: always
          type: str
          sample: '<associatedwlcip>'
        bootDateTime:
          description: It is the network device's bootDateTime.
          returned: always
          type: str
          sample: '<bootdatetime>'
        collectionInterval:
          description: It is the network device's collectionInterval.
          returned: always
          type: str
          sample: '<collectioninterval>'
        collectionStatus:
          description: It is the network device's collectionStatus.
          returned: always
          type: str
          sample: '<collectionstatus>'
        errorCode:
          description: It is the network device's errorCode.
          returned: always
          type: str
          sample: '<errorcode>'
        errorDescription:
          description: It is the network device's errorDescription.
          returned: always
          type: str
          sample: '<errordescription>'
        family:
          description: It is the network device's family.
          returned: always
          type: str
          sample: '<family>'
        hostname:
          description: It is the network device's hostname.
          returned: always
          type: str
          sample: '<hostname>'
        id:
          description: It is the network device's id.
          returned: always
          type: str
          sample: '478012'
        instanceTenantId:
          description: It is the network device's instanceTenantId.
          returned: always
          type: str
          sample: '<instancetenantid>'
        instanceUuid:
          description: It is the network device's instanceUuid.
          returned: always
          type: str
          sample: '<instanceuuid>'
        interfaceCount:
          description: It is the network device's interfaceCount.
          returned: always
          type: str
          sample: '<interfacecount>'
        inventoryStatusDetail:
          description: It is the network device's inventoryStatusDetail.
          returned: always
          type: str
          sample: '<inventorystatusdetail>'
        lastUpdateTime:
          description: It is the network device's lastUpdateTime.
          returned: always
          type: str
          sample: '<lastupdatetime>'
        lastUpdated:
          description: It is the network device's lastUpdated.
          returned: always
          type: str
          sample: '<lastupdated>'
        lineCardCount:
          description: It is the network device's lineCardCount.
          returned: always
          type: str
          sample: '<linecardcount>'
        lineCardId:
          description: It is the network device's lineCardId.
          returned: always
          type: str
          sample: '<linecardid>'
        location:
          description: It is the network device's location.
          returned: always
          type: str
          sample: '<location>'
        locationName:
          description: It is the network device's locationName.
          returned: always
          type: str
          sample: '<locationname>'
        macAddress:
          description: It is the network device's macAddress.
          returned: always
          type: str
          sample: '<macaddress>'
        managementIpAddress:
          description: It is the network device's managementIpAddress.
          returned: always
          type: str
          sample: '<managementipaddress>'
        memorySize:
          description: It is the network device's memorySize.
          returned: always
          type: str
          sample: '<memorysize>'
        platformId:
          description: It is the network device's platformId.
          returned: always
          type: str
          sample: '<platformid>'
        reachabilityFailureReason:
          description: It is the network device's reachabilityFailureReason.
          returned: always
          type: str
          sample: '<reachabilityfailurereason>'
        reachabilityStatus:
          description: It is the network device's reachabilityStatus.
          returned: always
          type: str
          sample: '<reachabilitystatus>'
        role:
          description: It is the network device's role.
          returned: always
          type: str
          sample: '<role>'
        roleSource:
          description: It is the network device's roleSource.
          returned: always
          type: str
          sample: '<rolesource>'
        serialNumber:
          description: It is the network device's serialNumber.
          returned: always
          type: str
          sample: '<serialnumber>'
        series:
          description: It is the network device's series.
          returned: always
          type: str
          sample: '<series>'
        snmpContact:
          description: It is the network device's snmpContact.
          returned: always
          type: str
          sample: '<snmpcontact>'
        snmpLocation:
          description: It is the network device's snmpLocation.
          returned: always
          type: str
          sample: '<snmplocation>'
        softwareType:
          description: It is the network device's softwareType.
          returned: always
          type: str
          sample: '<softwaretype>'
        softwareVersion:
          description: It is the network device's softwareVersion.
          returned: always
          type: str
          sample: '<softwareversion>'
        tagCount:
          description: It is the network device's tagCount.
          returned: always
          type: str
          sample: '<tagcount>'
        tunnelUdpPort:
          description: It is the network device's tunnelUdpPort.
          returned: always
          type: str
          sample: '<tunneludpport>'
        type:
          description: It is the network device's type.
          returned: always
          type: str
          sample: '<type>'
        upTime:
          description: It is the network device's upTime.
          returned: always
          type: str
          sample: '<uptime>'
        waasDeviceMode:
          description: It is the network device's waasDeviceMode.
          returned: always
          type: str
          sample: '<waasdevicemode>'

    version:
      description: Version, property of the response body.
      returned: always
      type: str
      sample: '1.0'

"""
