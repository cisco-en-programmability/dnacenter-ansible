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
module: client_detail
short_description: Manage ClientDetail objects of Clients
description:
- Returns detailed Client information retrieved by Mac Address for any given point of time.
version_added: '1.0'
author: first last (@GitHubID)
options:
    mac_address:
        description:
        - MAC Address of the client.
        type: str
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
'''

EXAMPLES = r'''
'''

RETURN = r'''
data_0:
    description: Returns detailed Client information retrieved by Mac Address for any given point of time.
    returned: success,changed,always
    type: dict
    contains:
        detail:
            description: Detail, property of the response body.
            returned: success,changed,always
            type: dict
            contains:
                id:
                    description: It is the client detail's id.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                connectionStatus:
                    description: It is the client detail's connectionStatus.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                hostType:
                    description: It is the client detail's hostType.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                userId:
                    description: It is the client detail's userId.
                    returned: success,changed,always
                    type: dict
                hostName:
                    description: It is the client detail's hostName.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                hostOs:
                    description: It is the client detail's hostOs.
                    returned: success,changed,always
                    type: dict
                hostVersion:
                    description: It is the client detail's hostVersion.
                    returned: success,changed,always
                    type: dict
                subType:
                    description: It is the client detail's subType.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                lastUpdated:
                    description: It is the client detail's lastUpdated.
                    returned: success,changed,always
                    type: int
                    sample: 0
                healthScore:
                    description: It is the client detail's healthScore.
                    returned: success,changed,always
                    type: list
                    contains:
                        healthType:
                            description: It is the client detail's healthType.
                            returned: success,changed,always
                            type: str
                            sample: 'sample_string'
                        reason:
                            description: It is the client detail's reason.
                            returned: success,changed,always
                            type: str
                            sample: 'sample_string'
                        score:
                            description: It is the client detail's score.
                            returned: success,changed,always
                            type: int
                            sample: 0

                hostMac:
                    description: It is the client detail's hostMac.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                hostIpV4:
                    description: It is the client detail's hostIpV4.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                hostIpV6:
                    description: It is the client detail's hostIpV6.
                    returned: success,changed,always
                    type: list
                authType:
                    description: It is the client detail's authType.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                vlanId:
                    description: It is the client detail's vlanId.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                vnid:
                    description: It is the client detail's vnid.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                ssid:
                    description: It is the client detail's ssid.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                frequency:
                    description: It is the client detail's frequency.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                channel:
                    description: It is the client detail's channel.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                apGroup:
                    description: It is the client detail's apGroup.
                    returned: success,changed,always
                    type: dict
                location:
                    description: It is the client detail's location.
                    returned: success,changed,always
                    type: dict
                clientConnection:
                    description: It is the client detail's clientConnection.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                connectedDevice:
                    description: It is the client detail's connectedDevice.
                    returned: success,changed,always
                    type: list
                issueCount:
                    description: It is the client detail's issueCount.
                    returned: success,changed,always
                    type: int
                    sample: 0
                rssi:
                    description: It is the client detail's rssi.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                avgRssi:
                    description: It is the client detail's avgRssi.
                    returned: success,changed,always
                    type: dict
                snr:
                    description: It is the client detail's snr.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                avgSnr:
                    description: It is the client detail's avgSnr.
                    returned: success,changed,always
                    type: dict
                dataRate:
                    description: It is the client detail's dataRate.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                txBytes:
                    description: It is the client detail's txBytes.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                rxBytes:
                    description: It is the client detail's rxBytes.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                dnsSuccess:
                    description: It is the client detail's dnsSuccess.
                    returned: success,changed,always
                    type: dict
                dnsFailure:
                    description: It is the client detail's dnsFailure.
                    returned: success,changed,always
                    type: dict
                onboarding:
                    description: It is the client detail's onboarding.
                    returned: success,changed,always
                    type: dict
                    contains:
                        averageRunDuration:
                            description: It is the client detail's averageRunDuration.
                            returned: success,changed,always
                            type: dict
                        maxRunDuration:
                            description: It is the client detail's maxRunDuration.
                            returned: success,changed,always
                            type: dict
                        averageAssocDuration:
                            description: It is the client detail's averageAssocDuration.
                            returned: success,changed,always
                            type: dict
                        maxAssocDuration:
                            description: It is the client detail's maxAssocDuration.
                            returned: success,changed,always
                            type: dict
                        averageAuthDuration:
                            description: It is the client detail's averageAuthDuration.
                            returned: success,changed,always
                            type: dict
                        maxAuthDuration:
                            description: It is the client detail's maxAuthDuration.
                            returned: success,changed,always
                            type: dict
                        averageDhcpDuration:
                            description: It is the client detail's averageDhcpDuration.
                            returned: success,changed,always
                            type: dict
                        maxDhcpDuration:
                            description: It is the client detail's maxDhcpDuration.
                            returned: success,changed,always
                            type: dict
                        aaaServerIp:
                            description: It is the client detail's aaaServerIp.
                            returned: success,changed,always
                            type: str
                            sample: 'sample_string'
                        dhcpServerIp:
                            description: It is the client detail's dhcpServerIp.
                            returned: success,changed,always
                            type: dict
                        authDoneTime:
                            description: It is the client detail's authDoneTime.
                            returned: success,changed,always
                            type: dict
                        assocDoneTime:
                            description: It is the client detail's assocDoneTime.
                            returned: success,changed,always
                            type: dict
                        dhcpDoneTime:
                            description: It is the client detail's dhcpDoneTime.
                            returned: success,changed,always
                            type: dict
                        assocRootcauseList:
                            description: It is the client detail's assocRootcauseList.
                            returned: success,changed,always
                            type: list
                        aaaRootcauseList:
                            description: It is the client detail's aaaRootcauseList.
                            returned: success,changed,always
                            type: list
                        dhcpRootcauseList:
                            description: It is the client detail's dhcpRootcauseList.
                            returned: success,changed,always
                            type: list
                        otherRootcauseList:
                            description: It is the client detail's otherRootcauseList.
                            returned: success,changed,always
                            type: list

                clientType:
                    description: It is the client detail's clientType.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                onboardingTime:
                    description: It is the client detail's onboardingTime.
                    returned: success,changed,always
                    type: dict
                port:
                    description: It is the client detail's port.
                    returned: success,changed,always
                    type: dict
                iosCapable:
                    description: It is the client detail's iosCapable.
                    returned: success,changed,always
                    type: bool
                    sample: false

        connectionInfo:
            description: Connection Info, property of the response body.
            returned: success,changed,always
            type: dict
            contains:
                hostType:
                    description: It is the client detail's hostType.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                nwDeviceName:
                    description: It is the client detail's nwDeviceName.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                nwDeviceMac:
                    description: It is the client detail's nwDeviceMac.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                protocol:
                    description: It is the client detail's protocol.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                band:
                    description: It is the client detail's band.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                spatialStream:
                    description: It is the client detail's spatialStream.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                channel:
                    description: It is the client detail's channel.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                channelWidth:
                    description: It is the client detail's channelWidth.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                wmm:
                    description: It is the client detail's wmm.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                uapsd:
                    description: It is the client detail's uapsd.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                timestamp:
                    description: It is the client detail's timestamp.
                    returned: success,changed,always
                    type: int
                    sample: 0

        topology:
            description: Topology, property of the response body.
            returned: success,changed,always
            type: dict
            contains:
                nodes:
                    description: It is the client detail's nodes.
                    returned: success,changed,always
                    type: list
                    contains:
                        role:
                            description: It is the client detail's role.
                            returned: success,changed,always
                            type: str
                            sample: 'sample_string'
                        name:
                            description: It is the client detail's name.
                            returned: success,changed,always
                            type: str
                            sample: 'sample_string'
                        id:
                            description: It is the client detail's id.
                            returned: success,changed,always
                            type: str
                            sample: 'sample_string'
                        description:
                            description: It is the client detail's description.
                            returned: success,changed,always
                            type: str
                            sample: 'sample_string'
                        deviceType:
                            description: It is the client detail's deviceType.
                            returned: success,changed,always
                            type: str
                            sample: 'sample_string'
                        platformId:
                            description: It is the client detail's platformId.
                            returned: success,changed,always
                            type: dict
                        family:
                            description: It is the client detail's family.
                            returned: success,changed,always
                            type: dict
                        ip:
                            description: It is the client detail's ip.
                            returned: success,changed,always
                            type: str
                            sample: 'sample_string'
                        softwareVersion:
                            description: It is the client detail's softwareVersion.
                            returned: success,changed,always
                            type: dict
                        userId:
                            description: It is the client detail's userId.
                            returned: success,changed,always
                            type: dict
                        nodeType:
                            description: It is the client detail's nodeType.
                            returned: success,changed,always
                            type: str
                            sample: 'sample_string'
                        radioFrequency:
                            description: It is the client detail's radioFrequency.
                            returned: success,changed,always
                            type: dict
                        clients:
                            description: It is the client detail's clients.
                            returned: success,changed,always
                            type: dict
                        count:
                            description: It is the client detail's count.
                            returned: success,changed,always
                            type: dict
                        healthScore:
                            description: It is the client detail's healthScore.
                            returned: success,changed,always
                            type: int
                            sample: 0
                        level:
                            description: It is the client detail's level.
                            returned: success,changed,always
                            type: int
                            sample: 0
                        fabricGroup:
                            description: It is the client detail's fabricGroup.
                            returned: success,changed,always
                            type: dict
                        connectedDevice:
                            description: It is the client detail's connectedDevice.
                            returned: success,changed,always
                            type: dict

                links:
                    description: It is the client detail's links.
                    returned: success,changed,always
                    type: list
                    contains:
                        source:
                            description: It is the client detail's source.
                            returned: success,changed,always
                            type: str
                            sample: 'sample_string'
                        linkStatus:
                            description: It is the client detail's linkStatus.
                            returned: success,changed,always
                            type: str
                            sample: 'sample_string'
                        label:
                            description: It is the client detail's label.
                            returned: success,changed,always
                            type: list
                        target:
                            description: It is the client detail's target.
                            returned: success,changed,always
                            type: str
                            sample: 'sample_string'
                        id:
                            description: It is the client detail's id.
                            returned: success,changed,always
                            type: dict
                        portUtilization:
                            description: It is the client detail's portUtilization.
                            returned: success,changed,always
                            type: dict



'''

from ansible.module_utils.basic import AnsibleModule
from ansible_collections.cisco.dnac.plugins.module_utils.dnac import ModuleDefinition, DNACModule, dnac_argument_spec
from ansible_collections.cisco.dnac.plugins.module_utils.definitions.client_detail import module_definition


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