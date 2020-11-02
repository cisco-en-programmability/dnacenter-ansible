#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright: (c) 2020, first last <email>
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

ANSIBLE_METADATA = {
    'metadata_version': '0.0.1',
    'status': ['preview'],
    'supported_by': 'community'
}

DOCUMENTATION = r'''
---
module: interface
short_description: Manage Interface objects of Devices
description:
- Returns all available Interfaces. This endpoint can return a maximum of 500 Interfaces.
- Returns the Interface for the given Interface ID.
- Returns the count of Interfaces for all devices.
- Returns list of Interfaces by specified IP address.
- Returns list of Interfaces by specified device.
- Returns the list of Interfaces for the device for the specified range.
- Returns the Interface count for the given device.
- Returns Interface by specified device Id and Interface name.
- Returns the Interfaces that has ISIS enabled.
- Returns the Interfaces that has OSPF enabled.
version_added: '1.0'
author: first last (@GitHubID)
options:
    limit:
        description:
        - Limit query parameter.
        type: int
    offset:
        description:
        - Offset query parameter.
        type: int
    id:
        description:
        - Interface ID.
        type: str
        required: True
    count:
        description:
        - If true gets the number of objects.
        type: bool
        required: True
    ip_address:
        description:
        - IP address of the Interface.
        type: str
        required: True
    device_id:
        description:
        - Device ID.
        type: str
        required: True
    device_id:
        description:
        - Device ID.
        type: str
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
    device_id:
        description:
        - Device ID.
        type: str
        required: True
    count:
        description:
        - If true gets the number of objects.
        type: bool
        required: True
    device_id:
        description:
        - Device ID.
        type: str
        required: True
    name:
        description:
        - Interface name.
        type: str
    isis:
        description:
        - Specifies that the Interface is isis.
        type: bool
        required: True
    ospf:
        description:
        - Specifies that the Interface is ospf.
        type: bool
        required: True

requirements:
- dnacentersdk
seealso:
# Reference by module name
- module: cisco.dnac.plugins.module_utils.definitions.interface
# Reference by Internet resource
- name: Interface reference
  description: Complete reference of the Interface object model.
  link: https://developer.cisco.com/docs/dna-center/api/1-3-3-x
# Reference by Internet resource
- name: Interface reference
  description: SDK reference.
  link: https://dnacentersdk.readthedocs.io/en/latest/api/api.html#v2-1-1-summary
'''

EXAMPLES = r'''
'''

RETURN = r'''
data_0:
    description: Returns all available Interfaces. This endpoint can return a maximum of 500 Interfaces.
    returned: success,changed,always
    type: dict
    contains:
        response:
            description: Response, property of the response body (list of objects).
            returned: success,changed,always
            type: list
            contains:
                adminStatus:
                    description: It is the Interface's adminStatus.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                className:
                    description: It is the Interface's className.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                description:
                    description: It is the Interface's description.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                deviceId:
                    description: It is the Interface's deviceId.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                duplex:
                    description: It is the Interface's duplex.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                id:
                    description: It is the Interface's id.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                ifIndex:
                    description: It is the Interface's ifIndex.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                instanceTenantId:
                    description: It is the Interface's instanceTenantId.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                instanceUuid:
                    description: It is the Interface's instanceUuid.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                interfaceType:
                    description: It is the Interface's InterfaceType.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                ipv4Address:
                    description: It is the Interface's ipv4Address.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                ipv4Mask:
                    description: It is the Interface's ipv4Mask.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                isisSupport:
                    description: It is the Interface's isisSupport.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                lastUpdated:
                    description: It is the Interface's lastUpdated.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                macAddress:
                    description: It is the Interface's macAddress.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                mappedPhysicalInterfaceId:
                    description: It is the Interface's mappedPhysicalInterfaceId.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                mappedPhysicalInterfaceName:
                    description: It is the Interface's mappedPhysicalInterfaceName.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                mediaType:
                    description: It is the Interface's mediaType.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                nativeVlanId:
                    description: It is the Interface's nativeVlanId.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                ospfSupport:
                    description: It is the Interface's ospfSupport.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                pid:
                    description: It is the Interface's pid.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                portMode:
                    description: It is the Interface's portMode.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                portName:
                    description: It is the Interface's portName.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                portType:
                    description: It is the Interface's portType.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                serialNo:
                    description: It is the Interface's serialNo.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                series:
                    description: It is the Interface's series.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                speed:
                    description: It is the Interface's speed.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                status:
                    description: It is the Interface's status.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                vlanId:
                    description: It is the Interface's vlanId.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                voiceVlan:
                    description: It is the Interface's voiceVlan.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'

        version:
            description: Version, property of the response body.
            returned: success,changed,always
            type: str
            sample: 'sample_string'

data_1:
    description: Returns the Interface for the given Interface ID.
    returned: success,changed,always
    type: dict
    contains:
        response:
            description: Response, property of the response body.
            returned: success,changed,always
            type: dict
            contains:
                adminStatus:
                    description: It is the Interface's adminStatus.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                className:
                    description: It is the Interface's className.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                description:
                    description: It is the Interface's description.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                deviceId:
                    description: It is the Interface's deviceId.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                duplex:
                    description: It is the Interface's duplex.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                id:
                    description: It is the Interface's id.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                ifIndex:
                    description: It is the Interface's ifIndex.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                instanceTenantId:
                    description: It is the Interface's instanceTenantId.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                instanceUuid:
                    description: It is the Interface's instanceUuid.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                interfaceType:
                    description: It is the Interface's InterfaceType.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                ipv4Address:
                    description: It is the Interface's ipv4Address.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                ipv4Mask:
                    description: It is the Interface's ipv4Mask.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                isisSupport:
                    description: It is the Interface's isisSupport.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                lastUpdated:
                    description: It is the Interface's lastUpdated.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                macAddress:
                    description: It is the Interface's macAddress.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                mappedPhysicalInterfaceId:
                    description: It is the Interface's mappedPhysicalInterfaceId.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                mappedPhysicalInterfaceName:
                    description: It is the Interface's mappedPhysicalInterfaceName.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                mediaType:
                    description: It is the Interface's mediaType.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                nativeVlanId:
                    description: It is the Interface's nativeVlanId.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                ospfSupport:
                    description: It is the Interface's ospfSupport.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                pid:
                    description: It is the Interface's pid.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                portMode:
                    description: It is the Interface's portMode.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                portName:
                    description: It is the Interface's portName.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                portType:
                    description: It is the Interface's portType.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                serialNo:
                    description: It is the Interface's serialNo.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                series:
                    description: It is the Interface's series.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                speed:
                    description: It is the Interface's speed.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                status:
                    description: It is the Interface's status.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                vlanId:
                    description: It is the Interface's vlanId.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                voiceVlan:
                    description: It is the Interface's voiceVlan.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'

        version:
            description: Version, property of the response body.
            returned: success,changed,always
            type: str
            sample: 'sample_string'

data_2:
    description: Returns the count of Interfaces for all devices.
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
            sample: 'sample_string'

data_3:
    description: Returns list of Interfaces by specified IP address.
    returned: success,changed,always
    type: dict
    contains:
        response:
            description: Response, property of the response body (list of objects).
            returned: success,changed,always
            type: list
            contains:
                adminStatus:
                    description: It is the Interface's adminStatus.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                className:
                    description: It is the Interface's className.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                description:
                    description: It is the Interface's description.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                deviceId:
                    description: It is the Interface's deviceId.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                duplex:
                    description: It is the Interface's duplex.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                id:
                    description: It is the Interface's id.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                ifIndex:
                    description: It is the Interface's ifIndex.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                instanceTenantId:
                    description: It is the Interface's instanceTenantId.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                instanceUuid:
                    description: It is the Interface's instanceUuid.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                interfaceType:
                    description: It is the Interface's InterfaceType.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                ipv4Address:
                    description: It is the Interface's ipv4Address.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                ipv4Mask:
                    description: It is the Interface's ipv4Mask.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                isisSupport:
                    description: It is the Interface's isisSupport.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                lastUpdated:
                    description: It is the Interface's lastUpdated.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                macAddress:
                    description: It is the Interface's macAddress.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                mappedPhysicalInterfaceId:
                    description: It is the Interface's mappedPhysicalInterfaceId.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                mappedPhysicalInterfaceName:
                    description: It is the Interface's mappedPhysicalInterfaceName.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                mediaType:
                    description: It is the Interface's mediaType.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                nativeVlanId:
                    description: It is the Interface's nativeVlanId.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                ospfSupport:
                    description: It is the Interface's ospfSupport.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                pid:
                    description: It is the Interface's pid.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                portMode:
                    description: It is the Interface's portMode.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                portName:
                    description: It is the Interface's portName.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                portType:
                    description: It is the Interface's portType.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                serialNo:
                    description: It is the Interface's serialNo.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                series:
                    description: It is the Interface's series.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                speed:
                    description: It is the Interface's speed.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                status:
                    description: It is the Interface's status.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                vlanId:
                    description: It is the Interface's vlanId.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                voiceVlan:
                    description: It is the Interface's voiceVlan.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'

        version:
            description: Version, property of the response body.
            returned: success,changed,always
            type: str
            sample: 'sample_string'

data_4:
    description: Returns list of Interfaces by specified device.
    returned: success,changed,always
    type: dict
    contains:
        response:
            description: Response, property of the response body (list of objects).
            returned: success,changed,always
            type: list
            contains:
                adminStatus:
                    description: It is the Interface's adminStatus.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                className:
                    description: It is the Interface's className.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                description:
                    description: It is the Interface's description.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                deviceId:
                    description: It is the Interface's deviceId.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                duplex:
                    description: It is the Interface's duplex.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                id:
                    description: It is the Interface's id.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                ifIndex:
                    description: It is the Interface's ifIndex.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                instanceTenantId:
                    description: It is the Interface's instanceTenantId.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                instanceUuid:
                    description: It is the Interface's instanceUuid.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                interfaceType:
                    description: It is the Interface's InterfaceType.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                ipv4Address:
                    description: It is the Interface's ipv4Address.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                ipv4Mask:
                    description: It is the Interface's ipv4Mask.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                isisSupport:
                    description: It is the Interface's isisSupport.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                lastUpdated:
                    description: It is the Interface's lastUpdated.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                macAddress:
                    description: It is the Interface's macAddress.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                mappedPhysicalInterfaceId:
                    description: It is the Interface's mappedPhysicalInterfaceId.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                mappedPhysicalInterfaceName:
                    description: It is the Interface's mappedPhysicalInterfaceName.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                mediaType:
                    description: It is the Interface's mediaType.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                nativeVlanId:
                    description: It is the Interface's nativeVlanId.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                ospfSupport:
                    description: It is the Interface's ospfSupport.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                pid:
                    description: It is the Interface's pid.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                portMode:
                    description: It is the Interface's portMode.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                portName:
                    description: It is the Interface's portName.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                portType:
                    description: It is the Interface's portType.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                serialNo:
                    description: It is the Interface's serialNo.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                series:
                    description: It is the Interface's series.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                speed:
                    description: It is the Interface's speed.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                status:
                    description: It is the Interface's status.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                vlanId:
                    description: It is the Interface's vlanId.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                voiceVlan:
                    description: It is the Interface's voiceVlan.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'

        version:
            description: Version, property of the response body.
            returned: success,changed,always
            type: str
            sample: 'sample_string'

data_5:
    description: Returns the list of Interfaces for the device for the specified range.
    returned: success,changed,always
    type: dict
    contains:
        response:
            description: Response, property of the response body (list of objects).
            returned: success,changed,always
            type: list
            contains:
                adminStatus:
                    description: It is the Interface's adminStatus.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                className:
                    description: It is the Interface's className.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                description:
                    description: It is the Interface's description.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                deviceId:
                    description: It is the Interface's deviceId.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                duplex:
                    description: It is the Interface's duplex.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                id:
                    description: It is the Interface's id.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                ifIndex:
                    description: It is the Interface's ifIndex.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                instanceTenantId:
                    description: It is the Interface's instanceTenantId.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                instanceUuid:
                    description: It is the Interface's instanceUuid.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                interfaceType:
                    description: It is the Interface's InterfaceType.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                ipv4Address:
                    description: It is the Interface's ipv4Address.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                ipv4Mask:
                    description: It is the Interface's ipv4Mask.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                isisSupport:
                    description: It is the Interface's isisSupport.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                lastUpdated:
                    description: It is the Interface's lastUpdated.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                macAddress:
                    description: It is the Interface's macAddress.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                mappedPhysicalInterfaceId:
                    description: It is the Interface's mappedPhysicalInterfaceId.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                mappedPhysicalInterfaceName:
                    description: It is the Interface's mappedPhysicalInterfaceName.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                mediaType:
                    description: It is the Interface's mediaType.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                nativeVlanId:
                    description: It is the Interface's nativeVlanId.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                ospfSupport:
                    description: It is the Interface's ospfSupport.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                pid:
                    description: It is the Interface's pid.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                portMode:
                    description: It is the Interface's portMode.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                portName:
                    description: It is the Interface's portName.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                portType:
                    description: It is the Interface's portType.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                serialNo:
                    description: It is the Interface's serialNo.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                series:
                    description: It is the Interface's series.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                speed:
                    description: It is the Interface's speed.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                status:
                    description: It is the Interface's status.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                vlanId:
                    description: It is the Interface's vlanId.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                voiceVlan:
                    description: It is the Interface's voiceVlan.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'

        version:
            description: Version, property of the response body.
            returned: success,changed,always
            type: str
            sample: 'sample_string'

data_6:
    description: Returns the Interface count for the given device.
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
            sample: 'sample_string'

data_7:
    description: Returns Interface by specified device Id and Interface name.
    returned: success,changed,always
    type: dict
    contains:
        response:
            description: Response, property of the response body.
            returned: success,changed,always
            type: dict
            contains:
                adminStatus:
                    description: It is the Interface's adminStatus.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                className:
                    description: It is the Interface's className.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                description:
                    description: It is the Interface's description.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                deviceId:
                    description: It is the Interface's deviceId.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                duplex:
                    description: It is the Interface's duplex.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                id:
                    description: It is the Interface's id.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                ifIndex:
                    description: It is the Interface's ifIndex.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                instanceTenantId:
                    description: It is the Interface's instanceTenantId.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                instanceUuid:
                    description: It is the Interface's instanceUuid.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                interfaceType:
                    description: It is the Interface's InterfaceType.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                ipv4Address:
                    description: It is the Interface's ipv4Address.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                ipv4Mask:
                    description: It is the Interface's ipv4Mask.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                isisSupport:
                    description: It is the Interface's isisSupport.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                lastUpdated:
                    description: It is the Interface's lastUpdated.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                macAddress:
                    description: It is the Interface's macAddress.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                mappedPhysicalInterfaceId:
                    description: It is the Interface's mappedPhysicalInterfaceId.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                mappedPhysicalInterfaceName:
                    description: It is the Interface's mappedPhysicalInterfaceName.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                mediaType:
                    description: It is the Interface's mediaType.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                nativeVlanId:
                    description: It is the Interface's nativeVlanId.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                ospfSupport:
                    description: It is the Interface's ospfSupport.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                pid:
                    description: It is the Interface's pid.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                portMode:
                    description: It is the Interface's portMode.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                portName:
                    description: It is the Interface's portName.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                portType:
                    description: It is the Interface's portType.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                serialNo:
                    description: It is the Interface's serialNo.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                series:
                    description: It is the Interface's series.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                speed:
                    description: It is the Interface's speed.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                status:
                    description: It is the Interface's status.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                vlanId:
                    description: It is the Interface's vlanId.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                voiceVlan:
                    description: It is the Interface's voiceVlan.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'

        version:
            description: Version, property of the response body.
            returned: success,changed,always
            type: str
            sample: 'sample_string'

data_8:
    description: Returns the Interfaces that has ISIS enabled.
    returned: success,changed,always
    type: dict
    contains:
        response:
            description: Response, property of the response body (list of objects).
            returned: success,changed,always
            type: list
            contains:
                adminStatus:
                    description: It is the Interface's adminStatus.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                className:
                    description: It is the Interface's className.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                description:
                    description: It is the Interface's description.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                deviceId:
                    description: It is the Interface's deviceId.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                duplex:
                    description: It is the Interface's duplex.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                id:
                    description: It is the Interface's id.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                ifIndex:
                    description: It is the Interface's ifIndex.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                instanceTenantId:
                    description: It is the Interface's instanceTenantId.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                instanceUuid:
                    description: It is the Interface's instanceUuid.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                interfaceType:
                    description: It is the Interface's InterfaceType.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                ipv4Address:
                    description: It is the Interface's ipv4Address.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                ipv4Mask:
                    description: It is the Interface's ipv4Mask.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                isisSupport:
                    description: It is the Interface's isisSupport.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                lastUpdated:
                    description: It is the Interface's lastUpdated.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                macAddress:
                    description: It is the Interface's macAddress.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                mappedPhysicalInterfaceId:
                    description: It is the Interface's mappedPhysicalInterfaceId.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                mappedPhysicalInterfaceName:
                    description: It is the Interface's mappedPhysicalInterfaceName.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                mediaType:
                    description: It is the Interface's mediaType.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                nativeVlanId:
                    description: It is the Interface's nativeVlanId.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                ospfSupport:
                    description: It is the Interface's ospfSupport.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                pid:
                    description: It is the Interface's pid.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                portMode:
                    description: It is the Interface's portMode.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                portName:
                    description: It is the Interface's portName.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                portType:
                    description: It is the Interface's portType.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                serialNo:
                    description: It is the Interface's serialNo.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                series:
                    description: It is the Interface's series.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                speed:
                    description: It is the Interface's speed.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                status:
                    description: It is the Interface's status.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                vlanId:
                    description: It is the Interface's vlanId.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                voiceVlan:
                    description: It is the Interface's voiceVlan.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'

        version:
            description: Version, property of the response body.
            returned: success,changed,always
            type: str
            sample: 'sample_string'

data_9:
    description: Returns the Interfaces that has OSPF enabled.
    returned: success,changed,always
    type: dict
    contains:
        response:
            description: Response, property of the response body (list of objects).
            returned: success,changed,always
            type: list
            contains:
                adminStatus:
                    description: It is the Interface's adminStatus.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                className:
                    description: It is the Interface's className.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                description:
                    description: It is the Interface's description.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                deviceId:
                    description: It is the Interface's deviceId.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                duplex:
                    description: It is the Interface's duplex.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                id:
                    description: It is the Interface's id.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                ifIndex:
                    description: It is the Interface's ifIndex.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                instanceTenantId:
                    description: It is the Interface's instanceTenantId.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                instanceUuid:
                    description: It is the Interface's instanceUuid.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                interfaceType:
                    description: It is the Interface's InterfaceType.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                ipv4Address:
                    description: It is the Interface's ipv4Address.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                ipv4Mask:
                    description: It is the Interface's ipv4Mask.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                isisSupport:
                    description: It is the Interface's isisSupport.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                lastUpdated:
                    description: It is the Interface's lastUpdated.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                macAddress:
                    description: It is the Interface's macAddress.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                mappedPhysicalInterfaceId:
                    description: It is the Interface's mappedPhysicalInterfaceId.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                mappedPhysicalInterfaceName:
                    description: It is the Interface's mappedPhysicalInterfaceName.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                mediaType:
                    description: It is the Interface's mediaType.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                nativeVlanId:
                    description: It is the Interface's nativeVlanId.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                ospfSupport:
                    description: It is the Interface's ospfSupport.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                pid:
                    description: It is the Interface's pid.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                portMode:
                    description: It is the Interface's portMode.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                portName:
                    description: It is the Interface's portName.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                portType:
                    description: It is the Interface's portType.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                serialNo:
                    description: It is the Interface's serialNo.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                series:
                    description: It is the Interface's series.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                speed:
                    description: It is the Interface's speed.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                status:
                    description: It is the Interface's status.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                vlanId:
                    description: It is the Interface's vlanId.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                voiceVlan:
                    description: It is the Interface's voiceVlan.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'

        version:
            description: Version, property of the response body.
            returned: success,changed,always
            type: str
            sample: 'sample_string'

'''

from ansible.module_utils.basic import AnsibleModule
from ansible_collections.cisco.dnac.plugins.module_utils.dnac import ModuleDefinition, DNACModule, dnac_argument_spec
from ansible_collections.cisco.dnac.plugins.module_utils.definitions.interface import module_definition


def main():

    moddef = ModuleDefinition(module_definition)

    argument_spec = dnac_argument_spec()
    argument_spec.update(moddef.get_argument_spec_dict())

    required_if = moddef.get_required_if_list()
    
    module = AnsibleModule(
        argument_spec=argument_spec,
        supports_check_mode=False,
        required_if=required_if
    )

    dnac = DNACModule(module, moddef)

    state = module.params.get("state")

    if state == "query":
        dnac.exec("get")

    dnac.exit_json()


if __name__ == "__main__":
    main()