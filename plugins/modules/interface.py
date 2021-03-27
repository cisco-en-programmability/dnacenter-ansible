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
version_added: '1.0.0'
author: Rafael Campos (@racampos)
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
  name:
    description:
    - Interface name.
    type: str
    required: True
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
"""

EXAMPLES = r"""
- name: get_all_interfaces
  cisco.dnac.interface:
    state: query  # required
    limit: 1  #  number
    offset: 1  #  number
  register: query_result
  
- name: get_interface_by_id
  cisco.dnac.interface:
    state: query  # required
    id: SomeValue  # string, required
  register: query_result
  
- name: get_device_interface_count
  cisco.dnac.interface:
    state: query  # required
    count: True  # boolean, required
  register: query_result
  
- name: get_interface_by_ip
  cisco.dnac.interface:
    state: query  # required
    ip_address: SomeValue  # string, required
  register: query_result
  
- name: get_interface_info_by_id
  cisco.dnac.interface:
    state: query  # required
    device_id: SomeValue  # string, required
  register: query_result
  
- name: get_device_interfaces_by_specified_range
  cisco.dnac.interface:
    state: query  # required
    device_id: SomeValue  # string, required
    records_to_return: 1  #  integer, required
    start_index: 1  #  integer, required
  register: query_result
  
- name: get_device_interface_count_by_id
  cisco.dnac.interface:
    state: query  # required
    device_id: SomeValue  # string, required
    count: True  # boolean, required
  register: query_result
  
- name: get_interface_details
  cisco.dnac.interface:
    state: query  # required
    device_id: SomeValue  # string, required
    name: SomeValue  # string, required
  register: query_result
  
- name: get_isis_interfaces
  cisco.dnac.interface:
    state: query  # required
    isis: True  # boolean, required
  register: query_result
  
- name: get_ospf_interfaces
  cisco.dnac.interface:
    state: query  # required
    ospf: True  # boolean, required
  register: query_result
  
"""

RETURN = """
get_all_interfaces:
    description: Returns all available Interfaces. This endpoint can return a maximum of 500 Interfaces.
    returned: always
    type: dict
    contains:
    response:
      description: Response, property of the response body (list of objects).
      returned: always
      type: list
      contains:
        adminStatus:
          description: It is the Interface's adminStatus.
          returned: always
          type: str
          sample: '<adminstatus>'
        className:
          description: It is the Interface's className.
          returned: always
          type: str
          sample: '<classname>'
        description:
          description: It is the Interface's description.
          returned: always
          type: str
          sample: '<description>'
        deviceId:
          description: It is the Interface's deviceId.
          returned: always
          type: str
          sample: '<deviceid>'
        duplex:
          description: It is the Interface's duplex.
          returned: always
          type: str
          sample: '<duplex>'
        id:
          description: It is the Interface's id.
          returned: always
          type: str
          sample: '478012'
        ifIndex:
          description: It is the Interface's ifIndex.
          returned: always
          type: str
          sample: '<ifindex>'
        instanceTenantId:
          description: It is the Interface's instanceTenantId.
          returned: always
          type: str
          sample: '<instancetenantid>'
        instanceUuid:
          description: It is the Interface's instanceUuid.
          returned: always
          type: str
          sample: '<instanceuuid>'
        interfaceType:
          description: It is the Interface's InterfaceType.
          returned: always
          type: str
          sample: '<interfacetype>'
        ipv4Address:
          description: It is the Interface's ipv4Address.
          returned: always
          type: str
          sample: '<ipv4address>'
        ipv4Mask:
          description: It is the Interface's ipv4Mask.
          returned: always
          type: str
          sample: '<ipv4mask>'
        isisSupport:
          description: It is the Interface's isisSupport.
          returned: always
          type: str
          sample: '<isissupport>'
        lastUpdated:
          description: It is the Interface's lastUpdated.
          returned: always
          type: str
          sample: '<lastupdated>'
        macAddress:
          description: It is the Interface's macAddress.
          returned: always
          type: str
          sample: '<macaddress>'
        mappedPhysicalInterfaceId:
          description: It is the Interface's mappedPhysicalInterfaceId.
          returned: always
          type: str
          sample: '<mappedphysicalinterfaceid>'
        mappedPhysicalInterfaceName:
          description: It is the Interface's mappedPhysicalInterfaceName.
          returned: always
          type: str
          sample: '<mappedphysicalinterfacename>'
        mediaType:
          description: It is the Interface's mediaType.
          returned: always
          type: str
          sample: '<mediatype>'
        nativeVlanId:
          description: It is the Interface's nativeVlanId.
          returned: always
          type: str
          sample: '<nativevlanid>'
        ospfSupport:
          description: It is the Interface's ospfSupport.
          returned: always
          type: str
          sample: '<ospfsupport>'
        pid:
          description: It is the Interface's pid.
          returned: always
          type: str
          sample: '<pid>'
        portMode:
          description: It is the Interface's portMode.
          returned: always
          type: str
          sample: '<portmode>'
        portName:
          description: It is the Interface's portName.
          returned: always
          type: str
          sample: '<portname>'
        portType:
          description: It is the Interface's portType.
          returned: always
          type: str
          sample: '<porttype>'
        serialNo:
          description: It is the Interface's serialNo.
          returned: always
          type: str
          sample: '<serialno>'
        series:
          description: It is the Interface's series.
          returned: always
          type: str
          sample: '<series>'
        speed:
          description: It is the Interface's speed.
          returned: always
          type: str
          sample: '<speed>'
        status:
          description: It is the Interface's status.
          returned: always
          type: str
          sample: '<status>'
        vlanId:
          description: It is the Interface's vlanId.
          returned: always
          type: str
          sample: '<vlanid>'
        voiceVlan:
          description: It is the Interface's voiceVlan.
          returned: always
          type: str
          sample: '<voicevlan>'

    version:
      description: Version, property of the response body.
      returned: always
      type: str
      sample: '1.0'

get_interface_by_id:
    description: Returns the Interface for the given Interface ID.
    returned: always
    type: dict
    contains:
    response:
      description: Response, property of the response body.
      returned: always
      type: dict
      contains:
        adminStatus:
          description: It is the Interface's adminStatus.
          returned: always
          type: str
          sample: '<adminstatus>'
        className:
          description: It is the Interface's className.
          returned: always
          type: str
          sample: '<classname>'
        description:
          description: It is the Interface's description.
          returned: always
          type: str
          sample: '<description>'
        deviceId:
          description: It is the Interface's deviceId.
          returned: always
          type: str
          sample: '<deviceid>'
        duplex:
          description: It is the Interface's duplex.
          returned: always
          type: str
          sample: '<duplex>'
        id:
          description: It is the Interface's id.
          returned: always
          type: str
          sample: '478012'
        ifIndex:
          description: It is the Interface's ifIndex.
          returned: always
          type: str
          sample: '<ifindex>'
        instanceTenantId:
          description: It is the Interface's instanceTenantId.
          returned: always
          type: str
          sample: '<instancetenantid>'
        instanceUuid:
          description: It is the Interface's instanceUuid.
          returned: always
          type: str
          sample: '<instanceuuid>'
        interfaceType:
          description: It is the Interface's InterfaceType.
          returned: always
          type: str
          sample: '<interfacetype>'
        ipv4Address:
          description: It is the Interface's ipv4Address.
          returned: always
          type: str
          sample: '<ipv4address>'
        ipv4Mask:
          description: It is the Interface's ipv4Mask.
          returned: always
          type: str
          sample: '<ipv4mask>'
        isisSupport:
          description: It is the Interface's isisSupport.
          returned: always
          type: str
          sample: '<isissupport>'
        lastUpdated:
          description: It is the Interface's lastUpdated.
          returned: always
          type: str
          sample: '<lastupdated>'
        macAddress:
          description: It is the Interface's macAddress.
          returned: always
          type: str
          sample: '<macaddress>'
        mappedPhysicalInterfaceId:
          description: It is the Interface's mappedPhysicalInterfaceId.
          returned: always
          type: str
          sample: '<mappedphysicalinterfaceid>'
        mappedPhysicalInterfaceName:
          description: It is the Interface's mappedPhysicalInterfaceName.
          returned: always
          type: str
          sample: '<mappedphysicalinterfacename>'
        mediaType:
          description: It is the Interface's mediaType.
          returned: always
          type: str
          sample: '<mediatype>'
        nativeVlanId:
          description: It is the Interface's nativeVlanId.
          returned: always
          type: str
          sample: '<nativevlanid>'
        ospfSupport:
          description: It is the Interface's ospfSupport.
          returned: always
          type: str
          sample: '<ospfsupport>'
        pid:
          description: It is the Interface's pid.
          returned: always
          type: str
          sample: '<pid>'
        portMode:
          description: It is the Interface's portMode.
          returned: always
          type: str
          sample: '<portmode>'
        portName:
          description: It is the Interface's portName.
          returned: always
          type: str
          sample: '<portname>'
        portType:
          description: It is the Interface's portType.
          returned: always
          type: str
          sample: '<porttype>'
        serialNo:
          description: It is the Interface's serialNo.
          returned: always
          type: str
          sample: '<serialno>'
        series:
          description: It is the Interface's series.
          returned: always
          type: str
          sample: '<series>'
        speed:
          description: It is the Interface's speed.
          returned: always
          type: str
          sample: '<speed>'
        status:
          description: It is the Interface's status.
          returned: always
          type: str
          sample: '<status>'
        vlanId:
          description: It is the Interface's vlanId.
          returned: always
          type: str
          sample: '<vlanid>'
        voiceVlan:
          description: It is the Interface's voiceVlan.
          returned: always
          type: str
          sample: '<voicevlan>'

    version:
      description: Version, property of the response body.
      returned: always
      type: str
      sample: '1.0'

get_device_interface_count:
    description: Returns the count of Interfaces for all devices.
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

get_interface_by_ip:
    description: Returns list of Interfaces by specified IP address.
    returned: always
    type: dict
    contains:
    response:
      description: Response, property of the response body (list of objects).
      returned: always
      type: list
      contains:
        adminStatus:
          description: It is the Interface's adminStatus.
          returned: always
          type: str
          sample: '<adminstatus>'
        className:
          description: It is the Interface's className.
          returned: always
          type: str
          sample: '<classname>'
        description:
          description: It is the Interface's description.
          returned: always
          type: str
          sample: '<description>'
        deviceId:
          description: It is the Interface's deviceId.
          returned: always
          type: str
          sample: '<deviceid>'
        duplex:
          description: It is the Interface's duplex.
          returned: always
          type: str
          sample: '<duplex>'
        id:
          description: It is the Interface's id.
          returned: always
          type: str
          sample: '478012'
        ifIndex:
          description: It is the Interface's ifIndex.
          returned: always
          type: str
          sample: '<ifindex>'
        instanceTenantId:
          description: It is the Interface's instanceTenantId.
          returned: always
          type: str
          sample: '<instancetenantid>'
        instanceUuid:
          description: It is the Interface's instanceUuid.
          returned: always
          type: str
          sample: '<instanceuuid>'
        interfaceType:
          description: It is the Interface's InterfaceType.
          returned: always
          type: str
          sample: '<interfacetype>'
        ipv4Address:
          description: It is the Interface's ipv4Address.
          returned: always
          type: str
          sample: '<ipv4address>'
        ipv4Mask:
          description: It is the Interface's ipv4Mask.
          returned: always
          type: str
          sample: '<ipv4mask>'
        isisSupport:
          description: It is the Interface's isisSupport.
          returned: always
          type: str
          sample: '<isissupport>'
        lastUpdated:
          description: It is the Interface's lastUpdated.
          returned: always
          type: str
          sample: '<lastupdated>'
        macAddress:
          description: It is the Interface's macAddress.
          returned: always
          type: str
          sample: '<macaddress>'
        mappedPhysicalInterfaceId:
          description: It is the Interface's mappedPhysicalInterfaceId.
          returned: always
          type: str
          sample: '<mappedphysicalinterfaceid>'
        mappedPhysicalInterfaceName:
          description: It is the Interface's mappedPhysicalInterfaceName.
          returned: always
          type: str
          sample: '<mappedphysicalinterfacename>'
        mediaType:
          description: It is the Interface's mediaType.
          returned: always
          type: str
          sample: '<mediatype>'
        nativeVlanId:
          description: It is the Interface's nativeVlanId.
          returned: always
          type: str
          sample: '<nativevlanid>'
        ospfSupport:
          description: It is the Interface's ospfSupport.
          returned: always
          type: str
          sample: '<ospfsupport>'
        pid:
          description: It is the Interface's pid.
          returned: always
          type: str
          sample: '<pid>'
        portMode:
          description: It is the Interface's portMode.
          returned: always
          type: str
          sample: '<portmode>'
        portName:
          description: It is the Interface's portName.
          returned: always
          type: str
          sample: '<portname>'
        portType:
          description: It is the Interface's portType.
          returned: always
          type: str
          sample: '<porttype>'
        serialNo:
          description: It is the Interface's serialNo.
          returned: always
          type: str
          sample: '<serialno>'
        series:
          description: It is the Interface's series.
          returned: always
          type: str
          sample: '<series>'
        speed:
          description: It is the Interface's speed.
          returned: always
          type: str
          sample: '<speed>'
        status:
          description: It is the Interface's status.
          returned: always
          type: str
          sample: '<status>'
        vlanId:
          description: It is the Interface's vlanId.
          returned: always
          type: str
          sample: '<vlanid>'
        voiceVlan:
          description: It is the Interface's voiceVlan.
          returned: always
          type: str
          sample: '<voicevlan>'

    version:
      description: Version, property of the response body.
      returned: always
      type: str
      sample: '1.0'

get_interface_info_by_id:
    description: Returns list of Interfaces by specified device.
    returned: always
    type: dict
    contains:
    response:
      description: Response, property of the response body (list of objects).
      returned: always
      type: list
      contains:
        adminStatus:
          description: It is the Interface's adminStatus.
          returned: always
          type: str
          sample: '<adminstatus>'
        className:
          description: It is the Interface's className.
          returned: always
          type: str
          sample: '<classname>'
        description:
          description: It is the Interface's description.
          returned: always
          type: str
          sample: '<description>'
        deviceId:
          description: It is the Interface's deviceId.
          returned: always
          type: str
          sample: '<deviceid>'
        duplex:
          description: It is the Interface's duplex.
          returned: always
          type: str
          sample: '<duplex>'
        id:
          description: It is the Interface's id.
          returned: always
          type: str
          sample: '478012'
        ifIndex:
          description: It is the Interface's ifIndex.
          returned: always
          type: str
          sample: '<ifindex>'
        instanceTenantId:
          description: It is the Interface's instanceTenantId.
          returned: always
          type: str
          sample: '<instancetenantid>'
        instanceUuid:
          description: It is the Interface's instanceUuid.
          returned: always
          type: str
          sample: '<instanceuuid>'
        interfaceType:
          description: It is the Interface's InterfaceType.
          returned: always
          type: str
          sample: '<interfacetype>'
        ipv4Address:
          description: It is the Interface's ipv4Address.
          returned: always
          type: str
          sample: '<ipv4address>'
        ipv4Mask:
          description: It is the Interface's ipv4Mask.
          returned: always
          type: str
          sample: '<ipv4mask>'
        isisSupport:
          description: It is the Interface's isisSupport.
          returned: always
          type: str
          sample: '<isissupport>'
        lastUpdated:
          description: It is the Interface's lastUpdated.
          returned: always
          type: str
          sample: '<lastupdated>'
        macAddress:
          description: It is the Interface's macAddress.
          returned: always
          type: str
          sample: '<macaddress>'
        mappedPhysicalInterfaceId:
          description: It is the Interface's mappedPhysicalInterfaceId.
          returned: always
          type: str
          sample: '<mappedphysicalinterfaceid>'
        mappedPhysicalInterfaceName:
          description: It is the Interface's mappedPhysicalInterfaceName.
          returned: always
          type: str
          sample: '<mappedphysicalinterfacename>'
        mediaType:
          description: It is the Interface's mediaType.
          returned: always
          type: str
          sample: '<mediatype>'
        nativeVlanId:
          description: It is the Interface's nativeVlanId.
          returned: always
          type: str
          sample: '<nativevlanid>'
        ospfSupport:
          description: It is the Interface's ospfSupport.
          returned: always
          type: str
          sample: '<ospfsupport>'
        pid:
          description: It is the Interface's pid.
          returned: always
          type: str
          sample: '<pid>'
        portMode:
          description: It is the Interface's portMode.
          returned: always
          type: str
          sample: '<portmode>'
        portName:
          description: It is the Interface's portName.
          returned: always
          type: str
          sample: '<portname>'
        portType:
          description: It is the Interface's portType.
          returned: always
          type: str
          sample: '<porttype>'
        serialNo:
          description: It is the Interface's serialNo.
          returned: always
          type: str
          sample: '<serialno>'
        series:
          description: It is the Interface's series.
          returned: always
          type: str
          sample: '<series>'
        speed:
          description: It is the Interface's speed.
          returned: always
          type: str
          sample: '<speed>'
        status:
          description: It is the Interface's status.
          returned: always
          type: str
          sample: '<status>'
        vlanId:
          description: It is the Interface's vlanId.
          returned: always
          type: str
          sample: '<vlanid>'
        voiceVlan:
          description: It is the Interface's voiceVlan.
          returned: always
          type: str
          sample: '<voicevlan>'

    version:
      description: Version, property of the response body.
      returned: always
      type: str
      sample: '1.0'

get_device_interfaces_by_specified_range:
    description: Returns the list of Interfaces for the device for the specified range.
    returned: always
    type: dict
    contains:
    response:
      description: Response, property of the response body (list of objects).
      returned: always
      type: list
      contains:
        adminStatus:
          description: It is the Interface's adminStatus.
          returned: always
          type: str
          sample: '<adminstatus>'
        className:
          description: It is the Interface's className.
          returned: always
          type: str
          sample: '<classname>'
        description:
          description: It is the Interface's description.
          returned: always
          type: str
          sample: '<description>'
        deviceId:
          description: It is the Interface's deviceId.
          returned: always
          type: str
          sample: '<deviceid>'
        duplex:
          description: It is the Interface's duplex.
          returned: always
          type: str
          sample: '<duplex>'
        id:
          description: It is the Interface's id.
          returned: always
          type: str
          sample: '478012'
        ifIndex:
          description: It is the Interface's ifIndex.
          returned: always
          type: str
          sample: '<ifindex>'
        instanceTenantId:
          description: It is the Interface's instanceTenantId.
          returned: always
          type: str
          sample: '<instancetenantid>'
        instanceUuid:
          description: It is the Interface's instanceUuid.
          returned: always
          type: str
          sample: '<instanceuuid>'
        interfaceType:
          description: It is the Interface's InterfaceType.
          returned: always
          type: str
          sample: '<interfacetype>'
        ipv4Address:
          description: It is the Interface's ipv4Address.
          returned: always
          type: str
          sample: '<ipv4address>'
        ipv4Mask:
          description: It is the Interface's ipv4Mask.
          returned: always
          type: str
          sample: '<ipv4mask>'
        isisSupport:
          description: It is the Interface's isisSupport.
          returned: always
          type: str
          sample: '<isissupport>'
        lastUpdated:
          description: It is the Interface's lastUpdated.
          returned: always
          type: str
          sample: '<lastupdated>'
        macAddress:
          description: It is the Interface's macAddress.
          returned: always
          type: str
          sample: '<macaddress>'
        mappedPhysicalInterfaceId:
          description: It is the Interface's mappedPhysicalInterfaceId.
          returned: always
          type: str
          sample: '<mappedphysicalinterfaceid>'
        mappedPhysicalInterfaceName:
          description: It is the Interface's mappedPhysicalInterfaceName.
          returned: always
          type: str
          sample: '<mappedphysicalinterfacename>'
        mediaType:
          description: It is the Interface's mediaType.
          returned: always
          type: str
          sample: '<mediatype>'
        nativeVlanId:
          description: It is the Interface's nativeVlanId.
          returned: always
          type: str
          sample: '<nativevlanid>'
        ospfSupport:
          description: It is the Interface's ospfSupport.
          returned: always
          type: str
          sample: '<ospfsupport>'
        pid:
          description: It is the Interface's pid.
          returned: always
          type: str
          sample: '<pid>'
        portMode:
          description: It is the Interface's portMode.
          returned: always
          type: str
          sample: '<portmode>'
        portName:
          description: It is the Interface's portName.
          returned: always
          type: str
          sample: '<portname>'
        portType:
          description: It is the Interface's portType.
          returned: always
          type: str
          sample: '<porttype>'
        serialNo:
          description: It is the Interface's serialNo.
          returned: always
          type: str
          sample: '<serialno>'
        series:
          description: It is the Interface's series.
          returned: always
          type: str
          sample: '<series>'
        speed:
          description: It is the Interface's speed.
          returned: always
          type: str
          sample: '<speed>'
        status:
          description: It is the Interface's status.
          returned: always
          type: str
          sample: '<status>'
        vlanId:
          description: It is the Interface's vlanId.
          returned: always
          type: str
          sample: '<vlanid>'
        voiceVlan:
          description: It is the Interface's voiceVlan.
          returned: always
          type: str
          sample: '<voicevlan>'

    version:
      description: Version, property of the response body.
      returned: always
      type: str
      sample: '1.0'

get_device_interface_count_by_id:
    description: Returns the Interface count for the given device.
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

get_interface_details:
    description: Returns Interface by specified device Id and Interface name.
    returned: always
    type: dict
    contains:
    response:
      description: Response, property of the response body.
      returned: always
      type: dict
      contains:
        adminStatus:
          description: It is the Interface's adminStatus.
          returned: always
          type: str
          sample: '<adminstatus>'
        className:
          description: It is the Interface's className.
          returned: always
          type: str
          sample: '<classname>'
        description:
          description: It is the Interface's description.
          returned: always
          type: str
          sample: '<description>'
        deviceId:
          description: It is the Interface's deviceId.
          returned: always
          type: str
          sample: '<deviceid>'
        duplex:
          description: It is the Interface's duplex.
          returned: always
          type: str
          sample: '<duplex>'
        id:
          description: It is the Interface's id.
          returned: always
          type: str
          sample: '478012'
        ifIndex:
          description: It is the Interface's ifIndex.
          returned: always
          type: str
          sample: '<ifindex>'
        instanceTenantId:
          description: It is the Interface's instanceTenantId.
          returned: always
          type: str
          sample: '<instancetenantid>'
        instanceUuid:
          description: It is the Interface's instanceUuid.
          returned: always
          type: str
          sample: '<instanceuuid>'
        interfaceType:
          description: It is the Interface's InterfaceType.
          returned: always
          type: str
          sample: '<interfacetype>'
        ipv4Address:
          description: It is the Interface's ipv4Address.
          returned: always
          type: str
          sample: '<ipv4address>'
        ipv4Mask:
          description: It is the Interface's ipv4Mask.
          returned: always
          type: str
          sample: '<ipv4mask>'
        isisSupport:
          description: It is the Interface's isisSupport.
          returned: always
          type: str
          sample: '<isissupport>'
        lastUpdated:
          description: It is the Interface's lastUpdated.
          returned: always
          type: str
          sample: '<lastupdated>'
        macAddress:
          description: It is the Interface's macAddress.
          returned: always
          type: str
          sample: '<macaddress>'
        mappedPhysicalInterfaceId:
          description: It is the Interface's mappedPhysicalInterfaceId.
          returned: always
          type: str
          sample: '<mappedphysicalinterfaceid>'
        mappedPhysicalInterfaceName:
          description: It is the Interface's mappedPhysicalInterfaceName.
          returned: always
          type: str
          sample: '<mappedphysicalinterfacename>'
        mediaType:
          description: It is the Interface's mediaType.
          returned: always
          type: str
          sample: '<mediatype>'
        nativeVlanId:
          description: It is the Interface's nativeVlanId.
          returned: always
          type: str
          sample: '<nativevlanid>'
        ospfSupport:
          description: It is the Interface's ospfSupport.
          returned: always
          type: str
          sample: '<ospfsupport>'
        pid:
          description: It is the Interface's pid.
          returned: always
          type: str
          sample: '<pid>'
        portMode:
          description: It is the Interface's portMode.
          returned: always
          type: str
          sample: '<portmode>'
        portName:
          description: It is the Interface's portName.
          returned: always
          type: str
          sample: '<portname>'
        portType:
          description: It is the Interface's portType.
          returned: always
          type: str
          sample: '<porttype>'
        serialNo:
          description: It is the Interface's serialNo.
          returned: always
          type: str
          sample: '<serialno>'
        series:
          description: It is the Interface's series.
          returned: always
          type: str
          sample: '<series>'
        speed:
          description: It is the Interface's speed.
          returned: always
          type: str
          sample: '<speed>'
        status:
          description: It is the Interface's status.
          returned: always
          type: str
          sample: '<status>'
        vlanId:
          description: It is the Interface's vlanId.
          returned: always
          type: str
          sample: '<vlanid>'
        voiceVlan:
          description: It is the Interface's voiceVlan.
          returned: always
          type: str
          sample: '<voicevlan>'

    version:
      description: Version, property of the response body.
      returned: always
      type: str
      sample: '1.0'

get_isis_interfaces:
    description: Returns the Interfaces that has ISIS enabled.
    returned: always
    type: dict
    contains:
    response:
      description: Response, property of the response body (list of objects).
      returned: always
      type: list
      contains:
        adminStatus:
          description: It is the Interface's adminStatus.
          returned: always
          type: str
          sample: '<adminstatus>'
        className:
          description: It is the Interface's className.
          returned: always
          type: str
          sample: '<classname>'
        description:
          description: It is the Interface's description.
          returned: always
          type: str
          sample: '<description>'
        deviceId:
          description: It is the Interface's deviceId.
          returned: always
          type: str
          sample: '<deviceid>'
        duplex:
          description: It is the Interface's duplex.
          returned: always
          type: str
          sample: '<duplex>'
        id:
          description: It is the Interface's id.
          returned: always
          type: str
          sample: '478012'
        ifIndex:
          description: It is the Interface's ifIndex.
          returned: always
          type: str
          sample: '<ifindex>'
        instanceTenantId:
          description: It is the Interface's instanceTenantId.
          returned: always
          type: str
          sample: '<instancetenantid>'
        instanceUuid:
          description: It is the Interface's instanceUuid.
          returned: always
          type: str
          sample: '<instanceuuid>'
        interfaceType:
          description: It is the Interface's InterfaceType.
          returned: always
          type: str
          sample: '<interfacetype>'
        ipv4Address:
          description: It is the Interface's ipv4Address.
          returned: always
          type: str
          sample: '<ipv4address>'
        ipv4Mask:
          description: It is the Interface's ipv4Mask.
          returned: always
          type: str
          sample: '<ipv4mask>'
        isisSupport:
          description: It is the Interface's isisSupport.
          returned: always
          type: str
          sample: '<isissupport>'
        lastUpdated:
          description: It is the Interface's lastUpdated.
          returned: always
          type: str
          sample: '<lastupdated>'
        macAddress:
          description: It is the Interface's macAddress.
          returned: always
          type: str
          sample: '<macaddress>'
        mappedPhysicalInterfaceId:
          description: It is the Interface's mappedPhysicalInterfaceId.
          returned: always
          type: str
          sample: '<mappedphysicalinterfaceid>'
        mappedPhysicalInterfaceName:
          description: It is the Interface's mappedPhysicalInterfaceName.
          returned: always
          type: str
          sample: '<mappedphysicalinterfacename>'
        mediaType:
          description: It is the Interface's mediaType.
          returned: always
          type: str
          sample: '<mediatype>'
        nativeVlanId:
          description: It is the Interface's nativeVlanId.
          returned: always
          type: str
          sample: '<nativevlanid>'
        ospfSupport:
          description: It is the Interface's ospfSupport.
          returned: always
          type: str
          sample: '<ospfsupport>'
        pid:
          description: It is the Interface's pid.
          returned: always
          type: str
          sample: '<pid>'
        portMode:
          description: It is the Interface's portMode.
          returned: always
          type: str
          sample: '<portmode>'
        portName:
          description: It is the Interface's portName.
          returned: always
          type: str
          sample: '<portname>'
        portType:
          description: It is the Interface's portType.
          returned: always
          type: str
          sample: '<porttype>'
        serialNo:
          description: It is the Interface's serialNo.
          returned: always
          type: str
          sample: '<serialno>'
        series:
          description: It is the Interface's series.
          returned: always
          type: str
          sample: '<series>'
        speed:
          description: It is the Interface's speed.
          returned: always
          type: str
          sample: '<speed>'
        status:
          description: It is the Interface's status.
          returned: always
          type: str
          sample: '<status>'
        vlanId:
          description: It is the Interface's vlanId.
          returned: always
          type: str
          sample: '<vlanid>'
        voiceVlan:
          description: It is the Interface's voiceVlan.
          returned: always
          type: str
          sample: '<voicevlan>'

    version:
      description: Version, property of the response body.
      returned: always
      type: str
      sample: '1.0'

get_ospf_interfaces:
    description: Returns the Interfaces that has OSPF enabled.
    returned: always
    type: dict
    contains:
    response:
      description: Response, property of the response body (list of objects).
      returned: always
      type: list
      contains:
        adminStatus:
          description: It is the Interface's adminStatus.
          returned: always
          type: str
          sample: '<adminstatus>'
        className:
          description: It is the Interface's className.
          returned: always
          type: str
          sample: '<classname>'
        description:
          description: It is the Interface's description.
          returned: always
          type: str
          sample: '<description>'
        deviceId:
          description: It is the Interface's deviceId.
          returned: always
          type: str
          sample: '<deviceid>'
        duplex:
          description: It is the Interface's duplex.
          returned: always
          type: str
          sample: '<duplex>'
        id:
          description: It is the Interface's id.
          returned: always
          type: str
          sample: '478012'
        ifIndex:
          description: It is the Interface's ifIndex.
          returned: always
          type: str
          sample: '<ifindex>'
        instanceTenantId:
          description: It is the Interface's instanceTenantId.
          returned: always
          type: str
          sample: '<instancetenantid>'
        instanceUuid:
          description: It is the Interface's instanceUuid.
          returned: always
          type: str
          sample: '<instanceuuid>'
        interfaceType:
          description: It is the Interface's InterfaceType.
          returned: always
          type: str
          sample: '<interfacetype>'
        ipv4Address:
          description: It is the Interface's ipv4Address.
          returned: always
          type: str
          sample: '<ipv4address>'
        ipv4Mask:
          description: It is the Interface's ipv4Mask.
          returned: always
          type: str
          sample: '<ipv4mask>'
        isisSupport:
          description: It is the Interface's isisSupport.
          returned: always
          type: str
          sample: '<isissupport>'
        lastUpdated:
          description: It is the Interface's lastUpdated.
          returned: always
          type: str
          sample: '<lastupdated>'
        macAddress:
          description: It is the Interface's macAddress.
          returned: always
          type: str
          sample: '<macaddress>'
        mappedPhysicalInterfaceId:
          description: It is the Interface's mappedPhysicalInterfaceId.
          returned: always
          type: str
          sample: '<mappedphysicalinterfaceid>'
        mappedPhysicalInterfaceName:
          description: It is the Interface's mappedPhysicalInterfaceName.
          returned: always
          type: str
          sample: '<mappedphysicalinterfacename>'
        mediaType:
          description: It is the Interface's mediaType.
          returned: always
          type: str
          sample: '<mediatype>'
        nativeVlanId:
          description: It is the Interface's nativeVlanId.
          returned: always
          type: str
          sample: '<nativevlanid>'
        ospfSupport:
          description: It is the Interface's ospfSupport.
          returned: always
          type: str
          sample: '<ospfsupport>'
        pid:
          description: It is the Interface's pid.
          returned: always
          type: str
          sample: '<pid>'
        portMode:
          description: It is the Interface's portMode.
          returned: always
          type: str
          sample: '<portmode>'
        portName:
          description: It is the Interface's portName.
          returned: always
          type: str
          sample: '<portname>'
        portType:
          description: It is the Interface's portType.
          returned: always
          type: str
          sample: '<porttype>'
        serialNo:
          description: It is the Interface's serialNo.
          returned: always
          type: str
          sample: '<serialno>'
        series:
          description: It is the Interface's series.
          returned: always
          type: str
          sample: '<series>'
        speed:
          description: It is the Interface's speed.
          returned: always
          type: str
          sample: '<speed>'
        status:
          description: It is the Interface's status.
          returned: always
          type: str
          sample: '<status>'
        vlanId:
          description: It is the Interface's vlanId.
          returned: always
          type: str
          sample: '<vlanid>'
        voiceVlan:
          description: It is the Interface's voiceVlan.
          returned: always
          type: str
          sample: '<voicevlan>'

    version:
      description: Version, property of the response body.
      returned: always
      type: str
      sample: '1.0'

"""
