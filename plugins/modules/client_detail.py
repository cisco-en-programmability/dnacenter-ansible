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
module: client_detail
short_description: Manage ClientDetail objects of Clients
description:
- Returns detailed Client information retrieved by Mac Address for any given point of time.
version_added: '1.0.0'
author: Rafael Campos (@racampos)
options:
  mac_address:
    description:
    - MAC Address of the client.
    type: str
    required: True
  timestamp:
    description:
    - Epoch time(in milliseconds) when the Client health data is required.
    type: int

requirements:
- dnacentersdk
seealso:
# Reference by module name
- module: cisco.dnac.plugins.module_utils.definitions.client_detail
# Reference by Internet resource
- name: ClientDetail reference
  description: Complete reference of the ClientDetail object model.
  link: https://developer.cisco.com/docs/dna-center/api/1-3-3-x
# Reference by Internet resource
- name: ClientDetail reference
  description: SDK reference.
  link: https://dnacentersdk.readthedocs.io/en/latest/api/api.html#v2-1-1-summary
"""

EXAMPLES = r"""
- name: get_client_detail
  cisco.dnac.client_detail:
    state: query  # required
    mac_address: SomeValue  # string, required
    timestamp: 1  #  integer
  register: query_result
  
"""

RETURN = """
get_client_detail:
    description: Returns detailed Client information retrieved by Mac Address for any given point of time.
    returned: always
    type: dict
    contains:
      detail:
      description: Detail, property of the response body.
      returned: always
      type: dict
      contains:
        id:
          description: It is the client detail's id.
          returned: always
          type: str
          sample: '478012'
        connectionStatus:
          description: It is the client detail's connectionStatus.
          returned: always
          type: str
          sample: '<connectionstatus>'
        hostType:
          description: It is the client detail's hostType.
          returned: always
          type: str
          sample: '<hosttype>'
        userId:
          description: It is the client detail's userId.
          returned: always
          type: dict
        hostName:
          description: It is the client detail's hostName.
          returned: always
          type: str
          sample: '<hostname>'
        hostOs:
          description: It is the client detail's hostOs.
          returned: always
          type: dict
        hostVersion:
          description: It is the client detail's hostVersion.
          returned: always
          type: dict
        subType:
          description: It is the client detail's subType.
          returned: always
          type: str
          sample: '<subtype>'
        lastUpdated:
          description: It is the client detail's lastUpdated.
          returned: always
          type: int
          sample: 0
        healthScore:
          description: It is the client detail's healthScore.
          returned: always
          type: list
          contains:
            healthType:
              description: It is the client detail's healthType.
              returned: always
              type: str
              sample: '<healthtype>'
            reason:
              description: It is the client detail's reason.
              returned: always
              type: str
              sample: '<reason>'
            score:
              description: It is the client detail's score.
              returned: always
              type: int
              sample: 0

        hostMac:
          description: It is the client detail's hostMac.
          returned: always
          type: str
          sample: '<hostmac>'
        hostIpV4:
          description: It is the client detail's hostIpV4.
          returned: always
          type: str
          sample: '<hostipv4>'
        hostIpV6:
          description: It is the client detail's hostIpV6.
          returned: always
          type: list
        authType:
          description: It is the client detail's authType.
          returned: always
          type: str
          sample: '<authtype>'
        vlanId:
          description: It is the client detail's vlanId.
          returned: always
          type: str
          sample: '<vlanid>'
        vnid:
          description: It is the client detail's vnid.
          returned: always
          type: str
          sample: '<vnid>'
        ssid:
          description: It is the client detail's ssid.
          returned: always
          type: str
          sample: '<ssid>'
        frequency:
          description: It is the client detail's frequency.
          returned: always
          type: str
          sample: '<frequency>'
        channel:
          description: It is the client detail's channel.
          returned: always
          type: str
          sample: '<channel>'
        apGroup:
          description: It is the client detail's apGroup.
          returned: always
          type: dict
        location:
          description: It is the client detail's location.
          returned: always
          type: dict
        clientConnection:
          description: It is the client detail's clientConnection.
          returned: always
          type: str
          sample: '<clientconnection>'
        connectedDevice:
          description: It is the client detail's connectedDevice.
          returned: always
          type: list
        issueCount:
          description: It is the client detail's issueCount.
          returned: always
          type: int
          sample: 0
        rssi:
          description: It is the client detail's rssi.
          returned: always
          type: str
          sample: '<rssi>'
        avgRssi:
          description: It is the client detail's avgRssi.
          returned: always
          type: dict
        snr:
          description: It is the client detail's snr.
          returned: always
          type: str
          sample: '<snr>'
        avgSnr:
          description: It is the client detail's avgSnr.
          returned: always
          type: dict
        dataRate:
          description: It is the client detail's dataRate.
          returned: always
          type: str
          sample: '<datarate>'
        txBytes:
          description: It is the client detail's txBytes.
          returned: always
          type: str
          sample: '<txbytes>'
        rxBytes:
          description: It is the client detail's rxBytes.
          returned: always
          type: str
          sample: '<rxbytes>'
        dnsSuccess:
          description: It is the client detail's dnsSuccess.
          returned: always
          type: dict
        dnsFailure:
          description: It is the client detail's dnsFailure.
          returned: always
          type: dict
        onboarding:
          description: It is the client detail's onboarding.
          returned: always
          type: dict
          contains:
            averageRunDuration:
              description: It is the client detail's averageRunDuration.
              returned: always
              type: dict
            maxRunDuration:
              description: It is the client detail's maxRunDuration.
              returned: always
              type: dict
            averageAssocDuration:
              description: It is the client detail's averageAssocDuration.
              returned: always
              type: dict
            maxAssocDuration:
              description: It is the client detail's maxAssocDuration.
              returned: always
              type: dict
            averageAuthDuration:
              description: It is the client detail's averageAuthDuration.
              returned: always
              type: dict
            maxAuthDuration:
              description: It is the client detail's maxAuthDuration.
              returned: always
              type: dict
            averageDhcpDuration:
              description: It is the client detail's averageDhcpDuration.
              returned: always
              type: dict
            maxDhcpDuration:
              description: It is the client detail's maxDhcpDuration.
              returned: always
              type: dict
            aaaServerIp:
              description: It is the client detail's aaaServerIp.
              returned: always
              type: str
              sample: '<aaaserverip>'
            dhcpServerIp:
              description: It is the client detail's dhcpServerIp.
              returned: always
              type: dict
            authDoneTime:
              description: It is the client detail's authDoneTime.
              returned: always
              type: dict
            assocDoneTime:
              description: It is the client detail's assocDoneTime.
              returned: always
              type: dict
            dhcpDoneTime:
              description: It is the client detail's dhcpDoneTime.
              returned: always
              type: dict
            assocRootcauseList:
              description: It is the client detail's assocRootcauseList.
              returned: always
              type: list
            aaaRootcauseList:
              description: It is the client detail's aaaRootcauseList.
              returned: always
              type: list
            dhcpRootcauseList:
              description: It is the client detail's dhcpRootcauseList.
              returned: always
              type: list
            otherRootcauseList:
              description: It is the client detail's otherRootcauseList.
              returned: always
              type: list

        clientType:
          description: It is the client detail's clientType.
          returned: always
          type: str
          sample: '<clienttype>'
        onboardingTime:
          description: It is the client detail's onboardingTime.
          returned: always
          type: dict
        port:
          description: It is the client detail's port.
          returned: always
          type: dict
        iosCapable:
          description: It is the client detail's iosCapable.
          returned: always
          type: bool
          sample: false

    connectionInfo:
      description: Connection Info, property of the response body.
      returned: always
      type: dict
      contains:
        hostType:
          description: It is the client detail's hostType.
          returned: always
          type: str
          sample: '<hosttype>'
        nwDeviceName:
          description: It is the client detail's nwDeviceName.
          returned: always
          type: str
          sample: '<nwdevicename>'
        nwDeviceMac:
          description: It is the client detail's nwDeviceMac.
          returned: always
          type: str
          sample: '<nwdevicemac>'
        protocol:
          description: It is the client detail's protocol.
          returned: always
          type: str
          sample: '<protocol>'
        band:
          description: It is the client detail's band.
          returned: always
          type: str
          sample: '<band>'
        spatialStream:
          description: It is the client detail's spatialStream.
          returned: always
          type: str
          sample: '<spatialstream>'
        channel:
          description: It is the client detail's channel.
          returned: always
          type: str
          sample: '<channel>'
        channelWidth:
          description: It is the client detail's channelWidth.
          returned: always
          type: str
          sample: '<channelwidth>'
        wmm:
          description: It is the client detail's wmm.
          returned: always
          type: str
          sample: '<wmm>'
        uapsd:
          description: It is the client detail's uapsd.
          returned: always
          type: str
          sample: '<uapsd>'
        timestamp:
          description: It is the client detail's timestamp.
          returned: always
          type: int
          sample: 0

    topology:
      description: Topology, property of the response body.
      returned: always
      type: dict
      contains:
        nodes:
          description: It is the client detail's nodes.
          returned: always
          type: list
          contains:
            role:
              description: It is the client detail's role.
              returned: always
              type: str
              sample: '<role>'
            name:
              description: It is the client detail's name.
              returned: always
              type: str
              sample: '<name>'
            id:
              description: It is the client detail's id.
              returned: always
              type: str
              sample: '478012'
            description:
              description: It is the client detail's description.
              returned: always
              type: str
              sample: '<description>'
            deviceType:
              description: It is the client detail's deviceType.
              returned: always
              type: str
              sample: '<devicetype>'
            platformId:
              description: It is the client detail's platformId.
              returned: always
              type: dict
            family:
              description: It is the client detail's family.
              returned: always
              type: dict
            ip:
              description: It is the client detail's ip.
              returned: always
              type: str
              sample: '1.1.1.17'
            softwareVersion:
              description: It is the client detail's softwareVersion.
              returned: always
              type: dict
            userId:
              description: It is the client detail's userId.
              returned: always
              type: dict
            nodeType:
              description: It is the client detail's nodeType.
              returned: always
              type: str
              sample: '<nodetype>'
            radioFrequency:
              description: It is the client detail's radioFrequency.
              returned: always
              type: dict
            clients:
              description: It is the client detail's clients.
              returned: always
              type: dict
            count:
              description: It is the client detail's count.
              returned: always
              type: dict
            healthScore:
              description: It is the client detail's healthScore.
              returned: always
              type: int
              sample: 0
            level:
              description: It is the client detail's level.
              returned: always
              type: int
              sample: 0
            fabricGroup:
              description: It is the client detail's fabricGroup.
              returned: always
              type: dict
            connectedDevice:
              description: It is the client detail's connectedDevice.
              returned: always
              type: dict

        links:
          description: It is the client detail's links.
          returned: always
          type: list
          contains:
            source:
              description: It is the client detail's source.
              returned: always
              type: str
              sample: '<source>'
            linkStatus:
              description: It is the client detail's linkStatus.
              returned: always
              type: str
              sample: '<linkstatus>'
            label:
              description: It is the client detail's label.
              returned: always
              type: list
            target:
              description: It is the client detail's target.
              returned: always
              type: str
              sample: '<target>'
            id:
              description: It is the client detail's id.
              returned: always
              type: dict
            portUtilization:
              description: It is the client detail's portUtilization.
              returned: always
              type: dict



"""
