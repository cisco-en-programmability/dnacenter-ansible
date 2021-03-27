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
module: device_detail
short_description: Manage DeviceDetail objects of Devices
description:
- Returns detailed Network Device information retrieved by Mac Address, Device Name or UUID for any given point of time.
version_added: '1.0.0'
author: Rafael Campos (@racampos)
options:
  identifier:
    description:
    - One of keywords : macAddress or uuid or nwDeviceName.
    type: str
    required: True
  search_by:
    description:
    - MAC Address or Device Name value or UUID of the network device.
    type: str
    required: True
  timestamp:
    description:
    - Epoch time(in milliseconds) when the device data is required.
    type: int

requirements:
- dnacentersdk
seealso:
# Reference by module name
- module: cisco.dnac.plugins.module_utils.definitions.device_detail
# Reference by Internet resource
- name: DeviceDetail reference
  description: Complete reference of the DeviceDetail object model.
  link: https://developer.cisco.com/docs/dna-center/api/1-3-3-x
# Reference by Internet resource
- name: DeviceDetail reference
  description: SDK reference.
  link: https://dnacentersdk.readthedocs.io/en/latest/api/api.html#v2-1-1-summary
"""

EXAMPLES = r"""
- name: get_device_detail
  cisco.dnac.device_detail:
    state: query  # required
    identifier: SomeValue  # string, required
    search_by: SomeValue  # string, required
    timestamp: 1  #  integer
  register: query_result
  
"""

RETURN = """
get_device_detail:
    description: Returns detailed Network Device information retrieved by Mac Address, Device Name or UUID for any given point of time.
    returned: always
    type: dict
    contains:
    response:
      description: Response, property of the response body.
      returned: always
      type: dict
      contains:
        HALastResetReason:
          description: It is the device detail's HALastResetReason.
          returned: always
          type: str
          sample: '<halastresetreason>'
        managementIpAddr:
          description: It is the device detail's managementIpAddr.
          returned: always
          type: str
          sample: '<managementipaddr>'
        HAPrimaryPowerStatus:
          description: It is the device detail's HAPrimaryPowerStatus.
          returned: always
          type: str
          sample: '<haprimarypowerstatus>'
        redundancyMode:
          description: It is the device detail's redundancyMode.
          returned: always
          type: str
          sample: '<redundancymode>'
        communicationState:
          description: It is the device detail's communicationState.
          returned: always
          type: str
          sample: '<communicationstate>'
        nwDeviceName:
          description: It is the device detail's nwDeviceName.
          returned: always
          type: str
          sample: '<nwdevicename>'
        redundancyUnit:
          description: It is the device detail's redundancyUnit.
          returned: always
          type: str
          sample: '<redundancyunit>'
        platformId:
          description: It is the device detail's platformId.
          returned: always
          type: str
          sample: '<platformid>'
        redundancyPeerState:
          description: It is the device detail's redundancyPeerState.
          returned: always
          type: str
          sample: '<redundancypeerstate>'
        nwDeviceId:
          description: It is the device detail's nwDeviceId.
          returned: always
          type: str
          sample: '<nwdeviceid>'
        redundancyState:
          description: It is the device detail's redundancyState.
          returned: always
          type: str
          sample: '<redundancystate>'
        nwDeviceRole:
          description: It is the device detail's nwDeviceRole.
          returned: always
          type: str
          sample: '<nwdevicerole>'
        nwDeviceFamily:
          description: It is the device detail's nwDeviceFamily.
          returned: always
          type: str
          sample: '<nwdevicefamily>'
        macAddress:
          description: It is the device detail's macAddress.
          returned: always
          type: str
          sample: '<macaddress>'
        collectionStatus:
          description: It is the device detail's collectionStatus.
          returned: always
          type: str
          sample: '<collectionstatus>'
        deviceSeries:
          description: It is the device detail's deviceSeries.
          returned: always
          type: str
          sample: '<deviceseries>'
        osType:
          description: It is the device detail's osType.
          returned: always
          type: str
          sample: '<ostype>'
        clientCount:
          description: It is the device detail's clientCount.
          returned: always
          type: str
          sample: '<clientcount>'
        HASecondaryPowerStatus:
          description: It is the device detail's HASecondaryPowerStatus.
          returned: always
          type: str
          sample: '<hasecondarypowerstatus>'
        softwareVersion:
          description: It is the device detail's softwareVersion.
          returned: always
          type: str
          sample: '<softwareversion>'
        nwDeviceType:
          description: It is the device detail's nwDeviceType.
          returned: always
          type: str
          sample: '<nwdevicetype>'
        overallHealth:
          description: It is the device detail's overallHealth.
          returned: always
          type: int
          sample: 0
        memoryScore:
          description: It is the device detail's memoryScore.
          returned: always
          type: int
          sample: 0
        cpuScore:
          description: It is the device detail's cpuScore.
          returned: always
          type: int
          sample: 0
        noiseScore:
          description: It is the device detail's noiseScore.
          returned: always
          type: int
          sample: 0
        utilizationScore:
          description: It is the device detail's utilizationScore.
          returned: always
          type: int
          sample: 0
        airQualityScore:
          description: It is the device detail's airQualityScore.
          returned: always
          type: int
          sample: 0
        interferenceScore:
          description: It is the device detail's interferenceScore.
          returned: always
          type: int
          sample: 0
        wqeScore:
          description: It is the device detail's wqeScore.
          returned: always
          type: int
          sample: 0
        freeMbufScore:
          description: It is the device detail's freeMbufScore.
          returned: always
          type: int
          sample: 0
        packetPoolScore:
          description: It is the device detail's packetPoolScore.
          returned: always
          type: int
          sample: 0
        freeTimerScore:
          description: It is the device detail's freeTimerScore.
          returned: always
          type: int
          sample: 0
        memory:
          description: It is the device detail's memory.
          returned: always
          type: str
          sample: '<memory>'
        cpu:
          description: It is the device detail's cpu.
          returned: always
          type: str
          sample: '<cpu>'
        noise:
          description: It is the device detail's noise.
          returned: always
          type: str
          sample: '<noise>'
        utilization:
          description: It is the device detail's utilization.
          returned: always
          type: str
          sample: '<utilization>'
        airQuality:
          description: It is the device detail's airQuality.
          returned: always
          type: str
          sample: '<airquality>'
        interference:
          description: It is the device detail's interference.
          returned: always
          type: str
          sample: '<interference>'
        wqe:
          description: It is the device detail's wqe.
          returned: always
          type: str
          sample: '<wqe>'
        freeMbuf:
          description: It is the device detail's freeMbuf.
          returned: always
          type: str
          sample: '<freembuf>'
        packetPool:
          description: It is the device detail's packetPool.
          returned: always
          type: str
          sample: '<packetpool>'
        freeTimer:
          description: It is the device detail's freeTimer.
          returned: always
          type: str
          sample: '<freetimer>'
        location:
          description: It is the device detail's location.
          returned: always
          type: str
          sample: '<location>'
        timestamp:
          description: It is the device detail's timestamp.
          returned: always
          type: str
          sample: '<timestamp>'


"""
