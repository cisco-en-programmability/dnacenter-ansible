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
        - Required for state delete.
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
        type: bool
        required: True
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
    ip_address:
        description:
        - Device IP address.
        type: str
        required: True

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
"""

RETURN = r"""
data_0:
    description: Returns list of network devices based on filter criteria such as management IP address, mac address, hostname, location name and a wide variety of additional criteria. You can also use the asterisk in any value to conduct a wildcard search. For example, to find all hostnames beginning with myhost in the IP address range 192.25.18.n, issue the following request: GET fqdnoripofdnacenterplatform/dna/intent/api/v1/network-device? hostname=myhost* & managementIpAddress=192.25.18.* For a complete list of parameter names that you can use for filtering this request, see the DNA Center API Reference documentation. Note: If id parameter is provided, it will return the list of network-devices for the given ids and ignores the other request parameters.
    returned: success,changed,always
    type: dict
    contains:
        response:
            description: Response, property of the response body (list of objects).
            returned: success,changed,always
            type: list
            contains:
                apManagerInterfaceIp:
                    description: It is the network device's apManagerInterfaceIp.
                    returned: success,changed,always
                    type: str
                    sample: '<apmanagerinterfaceip>'
                associatedWlcIp:
                    description: It is the network device's associatedWlcIp.
                    returned: success,changed,always
                    type: str
                    sample: '<associatedwlcip>'
                bootDateTime:
                    description: It is the network device's bootDateTime.
                    returned: success,changed,always
                    type: str
                    sample: '<bootdatetime>'
                collectionInterval:
                    description: It is the network device's collectionInterval.
                    returned: success,changed,always
                    type: str
                    sample: '<collectioninterval>'
                collectionStatus:
                    description: It is the network device's collectionStatus.
                    returned: success,changed,always
                    type: str
                    sample: '<collectionstatus>'
                errorCode:
                    description: It is the network device's errorCode.
                    returned: success,changed,always
                    type: str
                    sample: '<errorcode>'
                errorDescription:
                    description: It is the network device's errorDescription.
                    returned: success,changed,always
                    type: str
                    sample: '<errordescription>'
                family:
                    description: It is the network device's family.
                    returned: success,changed,always
                    type: str
                    sample: '<family>'
                hostname:
                    description: It is the network device's hostname.
                    returned: success,changed,always
                    type: str
                    sample: '<hostname>'
                id:
                    description: It is the network device's id.
                    returned: success,changed,always
                    type: str
                    sample: '478012'
                instanceTenantId:
                    description: It is the network device's instanceTenantId.
                    returned: success,changed,always
                    type: str
                    sample: '<instancetenantid>'
                instanceUuid:
                    description: It is the network device's instanceUuid.
                    returned: success,changed,always
                    type: str
                    sample: '<instanceuuid>'
                interfaceCount:
                    description: It is the network device's interfaceCount.
                    returned: success,changed,always
                    type: str
                    sample: '<interfacecount>'
                inventoryStatusDetail:
                    description: It is the network device's inventoryStatusDetail.
                    returned: success,changed,always
                    type: str
                    sample: '<inventorystatusdetail>'
                lastUpdateTime:
                    description: It is the network device's lastUpdateTime.
                    returned: success,changed,always
                    type: str
                    sample: '<lastupdatetime>'
                lastUpdated:
                    description: It is the network device's lastUpdated.
                    returned: success,changed,always
                    type: str
                    sample: '<lastupdated>'
                lineCardCount:
                    description: It is the network device's lineCardCount.
                    returned: success,changed,always
                    type: str
                    sample: '<linecardcount>'
                lineCardId:
                    description: It is the network device's lineCardId.
                    returned: success,changed,always
                    type: str
                    sample: '<linecardid>'
                location:
                    description: It is the network device's location.
                    returned: success,changed,always
                    type: str
                    sample: '<location>'
                locationName:
                    description: It is the network device's locationName.
                    returned: success,changed,always
                    type: str
                    sample: '<locationname>'
                macAddress:
                    description: It is the network device's macAddress.
                    returned: success,changed,always
                    type: str
                    sample: '<macaddress>'
                managementIpAddress:
                    description: It is the network device's managementIpAddress.
                    returned: success,changed,always
                    type: str
                    sample: '<managementipaddress>'
                memorySize:
                    description: It is the network device's memorySize.
                    returned: success,changed,always
                    type: str
                    sample: '<memorysize>'
                platformId:
                    description: It is the network device's platformId.
                    returned: success,changed,always
                    type: str
                    sample: '<platformid>'
                reachabilityFailureReason:
                    description: It is the network device's reachabilityFailureReason.
                    returned: success,changed,always
                    type: str
                    sample: '<reachabilityfailurereason>'
                reachabilityStatus:
                    description: It is the network device's reachabilityStatus.
                    returned: success,changed,always
                    type: str
                    sample: '<reachabilitystatus>'
                role:
                    description: It is the network device's role.
                    returned: success,changed,always
                    type: str
                    sample: '<role>'
                roleSource:
                    description: It is the network device's roleSource.
                    returned: success,changed,always
                    type: str
                    sample: '<rolesource>'
                serialNumber:
                    description: It is the network device's serialNumber.
                    returned: success,changed,always
                    type: str
                    sample: '<serialnumber>'
                series:
                    description: It is the network device's series.
                    returned: success,changed,always
                    type: str
                    sample: '<series>'
                snmpContact:
                    description: It is the network device's snmpContact.
                    returned: success,changed,always
                    type: str
                    sample: '<snmpcontact>'
                snmpLocation:
                    description: It is the network device's snmpLocation.
                    returned: success,changed,always
                    type: str
                    sample: '<snmplocation>'
                softwareType:
                    description: It is the network device's softwareType.
                    returned: success,changed,always
                    type: str
                    sample: '<softwaretype>'
                softwareVersion:
                    description: It is the network device's softwareVersion.
                    returned: success,changed,always
                    type: str
                    sample: '<softwareversion>'
                tagCount:
                    description: It is the network device's tagCount.
                    returned: success,changed,always
                    type: str
                    sample: '<tagcount>'
                tunnelUdpPort:
                    description: It is the network device's tunnelUdpPort.
                    returned: success,changed,always
                    type: str
                    sample: '<tunneludpport>'
                type:
                    description: It is the network device's type.
                    returned: success,changed,always
                    type: str
                    sample: '<type>'
                upTime:
                    description: It is the network device's upTime.
                    returned: success,changed,always
                    type: str
                    sample: '<uptime>'
                waasDeviceMode:
                    description: It is the network device's waasDeviceMode.
                    returned: success,changed,always
                    type: str
                    sample: '<waasdevicemode>'

        version:
            description: Version, property of the response body.
            returned: success,changed,always
            type: str
            sample: '1.0'

data_1:
    description: Adds the device with given credential.
    returned: success,changed,always
    type: dict
    contains:
        response:
            description: InventoryDeviceInfo's response.
            returned: success,changed,always
            type: dict
            contains:
                taskId:
                    description: It is the network device's taskId.
                    returned: success,changed,always
                    type: dict
                url:
                    description: It is the network device's url.
                    returned: success,changed,always
                    type: str
                    sample: '<url>'

        version:
            description: InventoryDeviceInfo's version.
            returned: success,changed,always
            type: str
            sample: '1.0'

data_2:
    description: Sync the devices provided as input.
    returned: success,changed,always
    type: dict
    contains:
        response:
            description: InventoryDeviceInfo's response.
            returned: success,changed,always
            type: dict
            contains:
                taskId:
                    description: It is the network device's taskId.
                    returned: success,changed,always
                    type: dict
                url:
                    description: It is the network device's url.
                    returned: success,changed,always
                    type: str
                    sample: '<url>'

        version:
            description: InventoryDeviceInfo's version.
            returned: success,changed,always
            type: str
            sample: '1.0'

data_3:
    description: Deletes the network device for the given Id.
    returned: success,changed,always
    type: dict
    contains:
        response:
            description: Response, property of the response body.
            returned: success,changed,always
            type: dict
            contains:
                taskId:
                    description: It is the network device's taskId.
                    returned: success,changed,always
                    type: dict
                url:
                    description: It is the network device's url.
                    returned: success,changed,always
                    type: str
                    sample: '<url>'

        version:
            description: Version, property of the response body.
            returned: success,changed,always
            type: str
            sample: '1.0'

data_4:
    description: Returns the network device details for the given device ID.
    returned: success,changed,always
    type: dict
    contains:
        response:
            description: Response, property of the response body.
            returned: success,changed,always
            type: dict
            contains:
                apManagerInterfaceIp:
                    description: It is the network device's apManagerInterfaceIp.
                    returned: success,changed,always
                    type: str
                    sample: '<apmanagerinterfaceip>'
                associatedWlcIp:
                    description: It is the network device's associatedWlcIp.
                    returned: success,changed,always
                    type: str
                    sample: '<associatedwlcip>'
                bootDateTime:
                    description: It is the network device's bootDateTime.
                    returned: success,changed,always
                    type: str
                    sample: '<bootdatetime>'
                collectionInterval:
                    description: It is the network device's collectionInterval.
                    returned: success,changed,always
                    type: str
                    sample: '<collectioninterval>'
                collectionStatus:
                    description: It is the network device's collectionStatus.
                    returned: success,changed,always
                    type: str
                    sample: '<collectionstatus>'
                errorCode:
                    description: It is the network device's errorCode.
                    returned: success,changed,always
                    type: str
                    sample: '<errorcode>'
                errorDescription:
                    description: It is the network device's errorDescription.
                    returned: success,changed,always
                    type: str
                    sample: '<errordescription>'
                family:
                    description: It is the network device's family.
                    returned: success,changed,always
                    type: str
                    sample: '<family>'
                hostname:
                    description: It is the network device's hostname.
                    returned: success,changed,always
                    type: str
                    sample: '<hostname>'
                id:
                    description: It is the network device's id.
                    returned: success,changed,always
                    type: str
                    sample: '478012'
                instanceTenantId:
                    description: It is the network device's instanceTenantId.
                    returned: success,changed,always
                    type: str
                    sample: '<instancetenantid>'
                instanceUuid:
                    description: It is the network device's instanceUuid.
                    returned: success,changed,always
                    type: str
                    sample: '<instanceuuid>'
                interfaceCount:
                    description: It is the network device's interfaceCount.
                    returned: success,changed,always
                    type: str
                    sample: '<interfacecount>'
                inventoryStatusDetail:
                    description: It is the network device's inventoryStatusDetail.
                    returned: success,changed,always
                    type: str
                    sample: '<inventorystatusdetail>'
                lastUpdateTime:
                    description: It is the network device's lastUpdateTime.
                    returned: success,changed,always
                    type: str
                    sample: '<lastupdatetime>'
                lastUpdated:
                    description: It is the network device's lastUpdated.
                    returned: success,changed,always
                    type: str
                    sample: '<lastupdated>'
                lineCardCount:
                    description: It is the network device's lineCardCount.
                    returned: success,changed,always
                    type: str
                    sample: '<linecardcount>'
                lineCardId:
                    description: It is the network device's lineCardId.
                    returned: success,changed,always
                    type: str
                    sample: '<linecardid>'
                location:
                    description: It is the network device's location.
                    returned: success,changed,always
                    type: str
                    sample: '<location>'
                locationName:
                    description: It is the network device's locationName.
                    returned: success,changed,always
                    type: str
                    sample: '<locationname>'
                macAddress:
                    description: It is the network device's macAddress.
                    returned: success,changed,always
                    type: str
                    sample: '<macaddress>'
                managementIpAddress:
                    description: It is the network device's managementIpAddress.
                    returned: success,changed,always
                    type: str
                    sample: '<managementipaddress>'
                memorySize:
                    description: It is the network device's memorySize.
                    returned: success,changed,always
                    type: str
                    sample: '<memorysize>'
                platformId:
                    description: It is the network device's platformId.
                    returned: success,changed,always
                    type: str
                    sample: '<platformid>'
                reachabilityFailureReason:
                    description: It is the network device's reachabilityFailureReason.
                    returned: success,changed,always
                    type: str
                    sample: '<reachabilityfailurereason>'
                reachabilityStatus:
                    description: It is the network device's reachabilityStatus.
                    returned: success,changed,always
                    type: str
                    sample: '<reachabilitystatus>'
                role:
                    description: It is the network device's role.
                    returned: success,changed,always
                    type: str
                    sample: '<role>'
                roleSource:
                    description: It is the network device's roleSource.
                    returned: success,changed,always
                    type: str
                    sample: '<rolesource>'
                serialNumber:
                    description: It is the network device's serialNumber.
                    returned: success,changed,always
                    type: str
                    sample: '<serialnumber>'
                series:
                    description: It is the network device's series.
                    returned: success,changed,always
                    type: str
                    sample: '<series>'
                snmpContact:
                    description: It is the network device's snmpContact.
                    returned: success,changed,always
                    type: str
                    sample: '<snmpcontact>'
                snmpLocation:
                    description: It is the network device's snmpLocation.
                    returned: success,changed,always
                    type: str
                    sample: '<snmplocation>'
                softwareType:
                    description: It is the network device's softwareType.
                    returned: success,changed,always
                    type: str
                    sample: '<softwaretype>'
                softwareVersion:
                    description: It is the network device's softwareVersion.
                    returned: success,changed,always
                    type: str
                    sample: '<softwareversion>'
                tagCount:
                    description: It is the network device's tagCount.
                    returned: success,changed,always
                    type: str
                    sample: '<tagcount>'
                tunnelUdpPort:
                    description: It is the network device's tunnelUdpPort.
                    returned: success,changed,always
                    type: str
                    sample: '<tunneludpport>'
                type:
                    description: It is the network device's type.
                    returned: success,changed,always
                    type: str
                    sample: '<type>'
                upTime:
                    description: It is the network device's upTime.
                    returned: success,changed,always
                    type: str
                    sample: '<uptime>'
                waasDeviceMode:
                    description: It is the network device's waasDeviceMode.
                    returned: success,changed,always
                    type: str
                    sample: '<waasdevicemode>'

        version:
            description: Version, property of the response body.
            returned: success,changed,always
            type: str
            sample: '1.0'

data_5:
    description: Returns brief summary of device info such as hostname, management IP address for the given device Id.
    returned: success,changed,always
    type: dict
    contains:
        response:
            description: Response, property of the response body.
            returned: success,changed,always
            type: dict
            contains:
                id:
                    description: It is the network device's id.
                    returned: success,changed,always
                    type: str
                    sample: '478012'
                role:
                    description: It is the network device's role.
                    returned: success,changed,always
                    type: str
                    sample: '<role>'
                roleSource:
                    description: It is the network device's roleSource.
                    returned: success,changed,always
                    type: str
                    sample: '<rolesource>'

        version:
            description: Version, property of the response body.
            returned: success,changed,always
            type: str
            sample: '1.0'

data_6:
    description: Returns the list of network devices for the given pagination range.
    returned: success,changed,always
    type: dict
    contains:
        response:
            description: Response, property of the response body (list of objects).
            returned: success,changed,always
            type: list
            contains:
                apManagerInterfaceIp:
                    description: It is the network device's apManagerInterfaceIp.
                    returned: success,changed,always
                    type: str
                    sample: '<apmanagerinterfaceip>'
                associatedWlcIp:
                    description: It is the network device's associatedWlcIp.
                    returned: success,changed,always
                    type: str
                    sample: '<associatedwlcip>'
                bootDateTime:
                    description: It is the network device's bootDateTime.
                    returned: success,changed,always
                    type: str
                    sample: '<bootdatetime>'
                collectionInterval:
                    description: It is the network device's collectionInterval.
                    returned: success,changed,always
                    type: str
                    sample: '<collectioninterval>'
                collectionStatus:
                    description: It is the network device's collectionStatus.
                    returned: success,changed,always
                    type: str
                    sample: '<collectionstatus>'
                errorCode:
                    description: It is the network device's errorCode.
                    returned: success,changed,always
                    type: str
                    sample: '<errorcode>'
                errorDescription:
                    description: It is the network device's errorDescription.
                    returned: success,changed,always
                    type: str
                    sample: '<errordescription>'
                family:
                    description: It is the network device's family.
                    returned: success,changed,always
                    type: str
                    sample: '<family>'
                hostname:
                    description: It is the network device's hostname.
                    returned: success,changed,always
                    type: str
                    sample: '<hostname>'
                id:
                    description: It is the network device's id.
                    returned: success,changed,always
                    type: str
                    sample: '478012'
                instanceTenantId:
                    description: It is the network device's instanceTenantId.
                    returned: success,changed,always
                    type: str
                    sample: '<instancetenantid>'
                instanceUuid:
                    description: It is the network device's instanceUuid.
                    returned: success,changed,always
                    type: str
                    sample: '<instanceuuid>'
                interfaceCount:
                    description: It is the network device's interfaceCount.
                    returned: success,changed,always
                    type: str
                    sample: '<interfacecount>'
                inventoryStatusDetail:
                    description: It is the network device's inventoryStatusDetail.
                    returned: success,changed,always
                    type: str
                    sample: '<inventorystatusdetail>'
                lastUpdateTime:
                    description: It is the network device's lastUpdateTime.
                    returned: success,changed,always
                    type: str
                    sample: '<lastupdatetime>'
                lastUpdated:
                    description: It is the network device's lastUpdated.
                    returned: success,changed,always
                    type: str
                    sample: '<lastupdated>'
                lineCardCount:
                    description: It is the network device's lineCardCount.
                    returned: success,changed,always
                    type: str
                    sample: '<linecardcount>'
                lineCardId:
                    description: It is the network device's lineCardId.
                    returned: success,changed,always
                    type: str
                    sample: '<linecardid>'
                location:
                    description: It is the network device's location.
                    returned: success,changed,always
                    type: str
                    sample: '<location>'
                locationName:
                    description: It is the network device's locationName.
                    returned: success,changed,always
                    type: str
                    sample: '<locationname>'
                macAddress:
                    description: It is the network device's macAddress.
                    returned: success,changed,always
                    type: str
                    sample: '<macaddress>'
                managementIpAddress:
                    description: It is the network device's managementIpAddress.
                    returned: success,changed,always
                    type: str
                    sample: '<managementipaddress>'
                memorySize:
                    description: It is the network device's memorySize.
                    returned: success,changed,always
                    type: str
                    sample: '<memorysize>'
                platformId:
                    description: It is the network device's platformId.
                    returned: success,changed,always
                    type: str
                    sample: '<platformid>'
                reachabilityFailureReason:
                    description: It is the network device's reachabilityFailureReason.
                    returned: success,changed,always
                    type: str
                    sample: '<reachabilityfailurereason>'
                reachabilityStatus:
                    description: It is the network device's reachabilityStatus.
                    returned: success,changed,always
                    type: str
                    sample: '<reachabilitystatus>'
                role:
                    description: It is the network device's role.
                    returned: success,changed,always
                    type: str
                    sample: '<role>'
                roleSource:
                    description: It is the network device's roleSource.
                    returned: success,changed,always
                    type: str
                    sample: '<rolesource>'
                serialNumber:
                    description: It is the network device's serialNumber.
                    returned: success,changed,always
                    type: str
                    sample: '<serialnumber>'
                series:
                    description: It is the network device's series.
                    returned: success,changed,always
                    type: str
                    sample: '<series>'
                snmpContact:
                    description: It is the network device's snmpContact.
                    returned: success,changed,always
                    type: str
                    sample: '<snmpcontact>'
                snmpLocation:
                    description: It is the network device's snmpLocation.
                    returned: success,changed,always
                    type: str
                    sample: '<snmplocation>'
                softwareType:
                    description: It is the network device's softwareType.
                    returned: success,changed,always
                    type: str
                    sample: '<softwaretype>'
                softwareVersion:
                    description: It is the network device's softwareVersion.
                    returned: success,changed,always
                    type: str
                    sample: '<softwareversion>'
                tagCount:
                    description: It is the network device's tagCount.
                    returned: success,changed,always
                    type: str
                    sample: '<tagcount>'
                tunnelUdpPort:
                    description: It is the network device's tunnelUdpPort.
                    returned: success,changed,always
                    type: str
                    sample: '<tunneludpport>'
                type:
                    description: It is the network device's type.
                    returned: success,changed,always
                    type: str
                    sample: '<type>'
                upTime:
                    description: It is the network device's upTime.
                    returned: success,changed,always
                    type: str
                    sample: '<uptime>'
                waasDeviceMode:
                    description: It is the network device's waasDeviceMode.
                    returned: success,changed,always
                    type: str
                    sample: '<waasdevicemode>'

        version:
            description: Version, property of the response body.
            returned: success,changed,always
            type: str
            sample: '1.0'

data_7:
    description: Returns the count of network devices based on the filter criteria by management IP address, mac address, hostname and location name.
    returned: success,changed,always
    type: dict
    contains:
        response:
            description: Response, property of the response body.
            returned: success,changed,always
            type: int
            sample: 0
        version:
            description: Version, property of the response body.
            returned: success,changed,always
            type: str
            sample: '1.0'

data_8:
    description: Returns the network device by specified IP address.
    returned: success,changed,always
    type: dict
    contains:
        response:
            description: Response, property of the response body.
            returned: success,changed,always
            type: dict
            contains:
                apManagerInterfaceIp:
                    description: It is the network device's apManagerInterfaceIp.
                    returned: success,changed,always
                    type: str
                    sample: '<apmanagerinterfaceip>'
                associatedWlcIp:
                    description: It is the network device's associatedWlcIp.
                    returned: success,changed,always
                    type: str
                    sample: '<associatedwlcip>'
                bootDateTime:
                    description: It is the network device's bootDateTime.
                    returned: success,changed,always
                    type: str
                    sample: '<bootdatetime>'
                collectionInterval:
                    description: It is the network device's collectionInterval.
                    returned: success,changed,always
                    type: str
                    sample: '<collectioninterval>'
                collectionStatus:
                    description: It is the network device's collectionStatus.
                    returned: success,changed,always
                    type: str
                    sample: '<collectionstatus>'
                errorCode:
                    description: It is the network device's errorCode.
                    returned: success,changed,always
                    type: str
                    sample: '<errorcode>'
                errorDescription:
                    description: It is the network device's errorDescription.
                    returned: success,changed,always
                    type: str
                    sample: '<errordescription>'
                family:
                    description: It is the network device's family.
                    returned: success,changed,always
                    type: str
                    sample: '<family>'
                hostname:
                    description: It is the network device's hostname.
                    returned: success,changed,always
                    type: str
                    sample: '<hostname>'
                id:
                    description: It is the network device's id.
                    returned: success,changed,always
                    type: str
                    sample: '478012'
                instanceTenantId:
                    description: It is the network device's instanceTenantId.
                    returned: success,changed,always
                    type: str
                    sample: '<instancetenantid>'
                instanceUuid:
                    description: It is the network device's instanceUuid.
                    returned: success,changed,always
                    type: str
                    sample: '<instanceuuid>'
                interfaceCount:
                    description: It is the network device's interfaceCount.
                    returned: success,changed,always
                    type: str
                    sample: '<interfacecount>'
                inventoryStatusDetail:
                    description: It is the network device's inventoryStatusDetail.
                    returned: success,changed,always
                    type: str
                    sample: '<inventorystatusdetail>'
                lastUpdateTime:
                    description: It is the network device's lastUpdateTime.
                    returned: success,changed,always
                    type: str
                    sample: '<lastupdatetime>'
                lastUpdated:
                    description: It is the network device's lastUpdated.
                    returned: success,changed,always
                    type: str
                    sample: '<lastupdated>'
                lineCardCount:
                    description: It is the network device's lineCardCount.
                    returned: success,changed,always
                    type: str
                    sample: '<linecardcount>'
                lineCardId:
                    description: It is the network device's lineCardId.
                    returned: success,changed,always
                    type: str
                    sample: '<linecardid>'
                location:
                    description: It is the network device's location.
                    returned: success,changed,always
                    type: str
                    sample: '<location>'
                locationName:
                    description: It is the network device's locationName.
                    returned: success,changed,always
                    type: str
                    sample: '<locationname>'
                macAddress:
                    description: It is the network device's macAddress.
                    returned: success,changed,always
                    type: str
                    sample: '<macaddress>'
                managementIpAddress:
                    description: It is the network device's managementIpAddress.
                    returned: success,changed,always
                    type: str
                    sample: '<managementipaddress>'
                memorySize:
                    description: It is the network device's memorySize.
                    returned: success,changed,always
                    type: str
                    sample: '<memorysize>'
                platformId:
                    description: It is the network device's platformId.
                    returned: success,changed,always
                    type: str
                    sample: '<platformid>'
                reachabilityFailureReason:
                    description: It is the network device's reachabilityFailureReason.
                    returned: success,changed,always
                    type: str
                    sample: '<reachabilityfailurereason>'
                reachabilityStatus:
                    description: It is the network device's reachabilityStatus.
                    returned: success,changed,always
                    type: str
                    sample: '<reachabilitystatus>'
                role:
                    description: It is the network device's role.
                    returned: success,changed,always
                    type: str
                    sample: '<role>'
                roleSource:
                    description: It is the network device's roleSource.
                    returned: success,changed,always
                    type: str
                    sample: '<rolesource>'
                serialNumber:
                    description: It is the network device's serialNumber.
                    returned: success,changed,always
                    type: str
                    sample: '<serialnumber>'
                series:
                    description: It is the network device's series.
                    returned: success,changed,always
                    type: str
                    sample: '<series>'
                snmpContact:
                    description: It is the network device's snmpContact.
                    returned: success,changed,always
                    type: str
                    sample: '<snmpcontact>'
                snmpLocation:
                    description: It is the network device's snmpLocation.
                    returned: success,changed,always
                    type: str
                    sample: '<snmplocation>'
                softwareType:
                    description: It is the network device's softwareType.
                    returned: success,changed,always
                    type: str
                    sample: '<softwaretype>'
                softwareVersion:
                    description: It is the network device's softwareVersion.
                    returned: success,changed,always
                    type: str
                    sample: '<softwareversion>'
                tagCount:
                    description: It is the network device's tagCount.
                    returned: success,changed,always
                    type: str
                    sample: '<tagcount>'
                tunnelUdpPort:
                    description: It is the network device's tunnelUdpPort.
                    returned: success,changed,always
                    type: str
                    sample: '<tunneludpport>'
                type:
                    description: It is the network device's type.
                    returned: success,changed,always
                    type: str
                    sample: '<type>'
                upTime:
                    description: It is the network device's upTime.
                    returned: success,changed,always
                    type: str
                    sample: '<uptime>'
                waasDeviceMode:
                    description: It is the network device's waasDeviceMode.
                    returned: success,changed,always
                    type: str
                    sample: '<waasdevicemode>'

        version:
            description: Version, property of the response body.
            returned: success,changed,always
            type: str
            sample: '1.0'

data_9:
    description: Returns the network device with given serial number.
    returned: success,changed,always
    type: dict
    contains:
        response:
            description: Response, property of the response body.
            returned: success,changed,always
            type: dict
            contains:
                apManagerInterfaceIp:
                    description: It is the network device's apManagerInterfaceIp.
                    returned: success,changed,always
                    type: str
                    sample: '<apmanagerinterfaceip>'
                associatedWlcIp:
                    description: It is the network device's associatedWlcIp.
                    returned: success,changed,always
                    type: str
                    sample: '<associatedwlcip>'
                bootDateTime:
                    description: It is the network device's bootDateTime.
                    returned: success,changed,always
                    type: str
                    sample: '<bootdatetime>'
                collectionInterval:
                    description: It is the network device's collectionInterval.
                    returned: success,changed,always
                    type: str
                    sample: '<collectioninterval>'
                collectionStatus:
                    description: It is the network device's collectionStatus.
                    returned: success,changed,always
                    type: str
                    sample: '<collectionstatus>'
                errorCode:
                    description: It is the network device's errorCode.
                    returned: success,changed,always
                    type: str
                    sample: '<errorcode>'
                errorDescription:
                    description: It is the network device's errorDescription.
                    returned: success,changed,always
                    type: str
                    sample: '<errordescription>'
                family:
                    description: It is the network device's family.
                    returned: success,changed,always
                    type: str
                    sample: '<family>'
                hostname:
                    description: It is the network device's hostname.
                    returned: success,changed,always
                    type: str
                    sample: '<hostname>'
                id:
                    description: It is the network device's id.
                    returned: success,changed,always
                    type: str
                    sample: '478012'
                instanceTenantId:
                    description: It is the network device's instanceTenantId.
                    returned: success,changed,always
                    type: str
                    sample: '<instancetenantid>'
                instanceUuid:
                    description: It is the network device's instanceUuid.
                    returned: success,changed,always
                    type: str
                    sample: '<instanceuuid>'
                interfaceCount:
                    description: It is the network device's interfaceCount.
                    returned: success,changed,always
                    type: str
                    sample: '<interfacecount>'
                inventoryStatusDetail:
                    description: It is the network device's inventoryStatusDetail.
                    returned: success,changed,always
                    type: str
                    sample: '<inventorystatusdetail>'
                lastUpdateTime:
                    description: It is the network device's lastUpdateTime.
                    returned: success,changed,always
                    type: str
                    sample: '<lastupdatetime>'
                lastUpdated:
                    description: It is the network device's lastUpdated.
                    returned: success,changed,always
                    type: str
                    sample: '<lastupdated>'
                lineCardCount:
                    description: It is the network device's lineCardCount.
                    returned: success,changed,always
                    type: str
                    sample: '<linecardcount>'
                lineCardId:
                    description: It is the network device's lineCardId.
                    returned: success,changed,always
                    type: str
                    sample: '<linecardid>'
                location:
                    description: It is the network device's location.
                    returned: success,changed,always
                    type: str
                    sample: '<location>'
                locationName:
                    description: It is the network device's locationName.
                    returned: success,changed,always
                    type: str
                    sample: '<locationname>'
                macAddress:
                    description: It is the network device's macAddress.
                    returned: success,changed,always
                    type: str
                    sample: '<macaddress>'
                managementIpAddress:
                    description: It is the network device's managementIpAddress.
                    returned: success,changed,always
                    type: str
                    sample: '<managementipaddress>'
                memorySize:
                    description: It is the network device's memorySize.
                    returned: success,changed,always
                    type: str
                    sample: '<memorysize>'
                platformId:
                    description: It is the network device's platformId.
                    returned: success,changed,always
                    type: str
                    sample: '<platformid>'
                reachabilityFailureReason:
                    description: It is the network device's reachabilityFailureReason.
                    returned: success,changed,always
                    type: str
                    sample: '<reachabilityfailurereason>'
                reachabilityStatus:
                    description: It is the network device's reachabilityStatus.
                    returned: success,changed,always
                    type: str
                    sample: '<reachabilitystatus>'
                role:
                    description: It is the network device's role.
                    returned: success,changed,always
                    type: str
                    sample: '<role>'
                roleSource:
                    description: It is the network device's roleSource.
                    returned: success,changed,always
                    type: str
                    sample: '<rolesource>'
                serialNumber:
                    description: It is the network device's serialNumber.
                    returned: success,changed,always
                    type: str
                    sample: '<serialnumber>'
                series:
                    description: It is the network device's series.
                    returned: success,changed,always
                    type: str
                    sample: '<series>'
                snmpContact:
                    description: It is the network device's snmpContact.
                    returned: success,changed,always
                    type: str
                    sample: '<snmpcontact>'
                snmpLocation:
                    description: It is the network device's snmpLocation.
                    returned: success,changed,always
                    type: str
                    sample: '<snmplocation>'
                softwareType:
                    description: It is the network device's softwareType.
                    returned: success,changed,always
                    type: str
                    sample: '<softwaretype>'
                softwareVersion:
                    description: It is the network device's softwareVersion.
                    returned: success,changed,always
                    type: str
                    sample: '<softwareversion>'
                tagCount:
                    description: It is the network device's tagCount.
                    returned: success,changed,always
                    type: str
                    sample: '<tagcount>'
                tunnelUdpPort:
                    description: It is the network device's tunnelUdpPort.
                    returned: success,changed,always
                    type: str
                    sample: '<tunneludpport>'
                type:
                    description: It is the network device's type.
                    returned: success,changed,always
                    type: str
                    sample: '<type>'
                upTime:
                    description: It is the network device's upTime.
                    returned: success,changed,always
                    type: str
                    sample: '<uptime>'
                waasDeviceMode:
                    description: It is the network device's waasDeviceMode.
                    returned: success,changed,always
                    type: str
                    sample: '<waasdevicemode>'

        version:
            description: Version, property of the response body.
            returned: success,changed,always
            type: str
            sample: '1.0'

"""

from ansible.module_utils.basic import AnsibleModule
from ansible_collections.cisco.dnac.plugins.module_utils.dnac import (
    ModuleDefinition,
    DNACModule,
    dnac_argument_spec,
)
from ansible_collections.cisco.dnac.plugins.module_utils.definitions.network_device import (
    module_definition,
)


def main():

    moddef = ModuleDefinition(module_definition)

    argument_spec = dnac_argument_spec()
    argument_spec.update(moddef.get_argument_spec_dict())

    required_if = moddef.get_required_if_list()

    module = AnsibleModule(
        argument_spec=argument_spec, supports_check_mode=False, required_if=required_if
    )

    dnac = DNACModule(module, moddef)

    state = module.params.get("state")

    if state == "query":
        dnac.exec("get")

    elif state == "delete":
        dnac.exec("delete")

    elif state == "create":
        dnac.disable_validation()
        dnac.exec("post")

    elif state == "update":
        dnac.disable_validation()
        dnac.exec("put")

    dnac.exit_json()


if __name__ == "__main__":
    main()
