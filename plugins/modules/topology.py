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
module: topology
short_description: Manage Topology objects of Topology
description:
- Returns Layer 2 network Topology by specified VLAN ID.
- Returns the Layer 3 network Topology by routing protocol.
- Returns the raw physical Topology by specified criteria of nodeType.
- Returns site Topology.
- Returns the list of VLAN names.
version_added: '1.0'
author: first last (@GitHubID)
options:
    vlan_id:
        description:
        - Vlan Name for e.g Vlan1, Vlan23 etc.
        type: str
        required: True
    layer2:
        description:
        - If true retrieves the layer 2 Topology.
        type: bool
        required: True
    topology_type:
        description:
        - Type of Topology(OSPF,ISIS,etc).
        type: str
        required: True
    layer3:
        description:
        - If true retrieves the layer 3 Topology.
        type: bool
        required: True
    node_type:
        description:
        - NodeType query parameter.
        type: str
    physical:
        description:
        - If true retrieves the physical Topology.
        type: bool
        required: True
    site:
        description:
        - If true retrieves the site Topology.
        type: bool
        required: True
    vlan:
        description:
        - If true retrieves the vlan Topology.
        type: bool
        required: True

requirements:
- dnacentersdk
seealso:
# Reference by module name
- module: cisco.dnac.plugins.module_utils.definitions.topology
# Reference by Internet resource
- name: Topology reference
  description: Complete reference of the Topology object model.
  link: https://developer.cisco.com/docs/dna-center/api/1-3-3-x
# Reference by Internet resource
- name: Topology reference
  description: SDK reference.
  link: https://dnacentersdk.readthedocs.io/en/latest/api/api.html#v2-1-1-summary
"""

EXAMPLES = r"""
"""

RETURN = r"""
data_0:
    description: Returns Layer 2 network Topology by specified VLAN ID.
    returned: success,changed,always
    type: dict
    contains:
        response:
            description: Response, property of the response body.
            returned: success,changed,always
            type: dict
            contains:
                id:
                    description: It is the Topology's id.
                    returned: success,changed,always
                    type: str
                    sample: '478012'
                links:
                    description: It is the Topology's links.
                    returned: success,changed,always
                    type: list
                    contains:
                        additionalInfo:
                            description: It is the Topology's additionalInfo.
                            returned: success,changed,always
                            type: dict
                        endPortID:
                            description: It is the Topology's endPortID.
                            returned: success,changed,always
                            type: str
                            sample: '<endportid>'
                        endPortIpv4Address:
                            description: It is the Topology's endPortIpv4Address.
                            returned: success,changed,always
                            type: str
                            sample: '<endportipv4address>'
                        endPortIpv4Mask:
                            description: It is the Topology's endPortIpv4Mask.
                            returned: success,changed,always
                            type: str
                            sample: '<endportipv4mask>'
                        endPortName:
                            description: It is the Topology's endPortName.
                            returned: success,changed,always
                            type: str
                            sample: '<endportname>'
                        endPortSpeed:
                            description: It is the Topology's endPortSpeed.
                            returned: success,changed,always
                            type: str
                            sample: '<endportspeed>'
                        greyOut:
                            description: It is the Topology's greyOut.
                            returned: success,changed,always
                            type: bool
                            sample: false
                        id:
                            description: It is the Topology's id.
                            returned: success,changed,always
                            type: str
                            sample: '478012'
                        linkStatus:
                            description: It is the Topology's linkStatus.
                            returned: success,changed,always
                            type: str
                            sample: '<linkstatus>'
                        source:
                            description: It is the Topology's source.
                            returned: success,changed,always
                            type: str
                            sample: '<source>'
                        startPortID:
                            description: It is the Topology's startPortID.
                            returned: success,changed,always
                            type: str
                            sample: '<startportid>'
                        startPortIpv4Address:
                            description: It is the Topology's startPortIpv4Address.
                            returned: success,changed,always
                            type: str
                            sample: '<startportipv4address>'
                        startPortIpv4Mask:
                            description: It is the Topology's startPortIpv4Mask.
                            returned: success,changed,always
                            type: str
                            sample: '<startportipv4mask>'
                        startPortName:
                            description: It is the Topology's startPortName.
                            returned: success,changed,always
                            type: str
                            sample: '<startportname>'
                        startPortSpeed:
                            description: It is the Topology's startPortSpeed.
                            returned: success,changed,always
                            type: str
                            sample: '<startportspeed>'
                        tag:
                            description: It is the Topology's tag.
                            returned: success,changed,always
                            type: str
                            sample: '<tag>'
                        target:
                            description: It is the Topology's target.
                            returned: success,changed,always
                            type: str
                            sample: '<target>'

                nodes:
                    description: It is the Topology's nodes.
                    returned: success,changed,always
                    type: list
                    contains:
                        aclApplied:
                            description: It is the Topology's aclApplied.
                            returned: success,changed,always
                            type: bool
                            sample: false
                        additionalInfo:
                            description: It is the Topology's additionalInfo.
                            returned: success,changed,always
                            type: dict
                        customParam:
                            description: It is the Topology's customParam.
                            returned: success,changed,always
                            type: dict
                            contains:
                                id:
                                    description: It is the Topology's id.
                                    returned: success,changed,always
                                    type: str
                                    sample: '478012'
                                label:
                                    description: It is the Topology's label.
                                    returned: success,changed,always
                                    type: str
                                    sample: '<label>'
                                parentNodeId:
                                    description: It is the Topology's parentNodeId.
                                    returned: success,changed,always
                                    type: str
                                    sample: '<parentnodeid>'
                                x:
                                    description: It is the Topology's x.
                                    returned: success,changed,always
                                    type: int
                                    sample: 0
                                y:
                                    description: It is the Topology's y.
                                    returned: success,changed,always
                                    type: int
                                    sample: 0

                        dataPathId:
                            description: It is the Topology's dataPathId.
                            returned: success,changed,always
                            type: str
                            sample: '<datapathid>'
                        deviceType:
                            description: It is the Topology's deviceType.
                            returned: success,changed,always
                            type: str
                            sample: '<devicetype>'
                        family:
                            description: It is the Topology's family.
                            returned: success,changed,always
                            type: str
                            sample: '<family>'
                        fixed:
                            description: It is the Topology's fixed.
                            returned: success,changed,always
                            type: bool
                            sample: false
                        greyOut:
                            description: It is the Topology's greyOut.
                            returned: success,changed,always
                            type: bool
                            sample: false
                        id:
                            description: It is the Topology's id.
                            returned: success,changed,always
                            type: str
                            sample: '478012'
                        ip:
                            description: It is the Topology's ip.
                            returned: success,changed,always
                            type: str
                            sample: '1.1.1.17'
                        label:
                            description: It is the Topology's label.
                            returned: success,changed,always
                            type: str
                            sample: '<label>'
                        networkType:
                            description: It is the Topology's networkType.
                            returned: success,changed,always
                            type: str
                            sample: '<networktype>'
                        nodeType:
                            description: It is the Topology's nodeType.
                            returned: success,changed,always
                            type: str
                            sample: '<nodetype>'
                        order:
                            description: It is the Topology's order.
                            returned: success,changed,always
                            type: int
                            sample: 0
                        osType:
                            description: It is the Topology's osType.
                            returned: success,changed,always
                            type: str
                            sample: '<ostype>'
                        platformId:
                            description: It is the Topology's platformId.
                            returned: success,changed,always
                            type: str
                            sample: '<platformid>'
                        role:
                            description: It is the Topology's role.
                            returned: success,changed,always
                            type: str
                            sample: '<role>'
                        roleSource:
                            description: It is the Topology's roleSource.
                            returned: success,changed,always
                            type: str
                            sample: '<rolesource>'
                        softwareVersion:
                            description: It is the Topology's softwareVersion.
                            returned: success,changed,always
                            type: str
                            sample: '<softwareversion>'
                        tags:
                            description: It is the Topology's tags.
                            returned: success,changed,always
                            type: list
                        upperNode:
                            description: It is the Topology's upperNode.
                            returned: success,changed,always
                            type: str
                            sample: '<uppernode>'
                        userId:
                            description: It is the Topology's userId.
                            returned: success,changed,always
                            type: str
                            sample: '<userid>'
                        vlanId:
                            description: It is the Topology's vlanId.
                            returned: success,changed,always
                            type: str
                            sample: '<vlanid>'
                        x:
                            description: It is the Topology's x.
                            returned: success,changed,always
                            type: int
                            sample: 0
                        y:
                            description: It is the Topology's y.
                            returned: success,changed,always
                            type: int
                            sample: 0


        version:
            description: Version, property of the response body.
            returned: success,changed,always
            type: str
            sample: '1.0'

data_1:
    description: Returns the Layer 3 network Topology by routing protocol.
    returned: success,changed,always
    type: dict
    contains:
        response:
            description: Response, property of the response body.
            returned: success,changed,always
            type: dict
            contains:
                id:
                    description: It is the Topology's id.
                    returned: success,changed,always
                    type: str
                    sample: '478012'
                links:
                    description: It is the Topology's links.
                    returned: success,changed,always
                    type: list
                    contains:
                        additionalInfo:
                            description: It is the Topology's additionalInfo.
                            returned: success,changed,always
                            type: dict
                        endPortID:
                            description: It is the Topology's endPortID.
                            returned: success,changed,always
                            type: str
                            sample: '<endportid>'
                        endPortIpv4Address:
                            description: It is the Topology's endPortIpv4Address.
                            returned: success,changed,always
                            type: str
                            sample: '<endportipv4address>'
                        endPortIpv4Mask:
                            description: It is the Topology's endPortIpv4Mask.
                            returned: success,changed,always
                            type: str
                            sample: '<endportipv4mask>'
                        endPortName:
                            description: It is the Topology's endPortName.
                            returned: success,changed,always
                            type: str
                            sample: '<endportname>'
                        endPortSpeed:
                            description: It is the Topology's endPortSpeed.
                            returned: success,changed,always
                            type: str
                            sample: '<endportspeed>'
                        greyOut:
                            description: It is the Topology's greyOut.
                            returned: success,changed,always
                            type: bool
                            sample: false
                        id:
                            description: It is the Topology's id.
                            returned: success,changed,always
                            type: str
                            sample: '478012'
                        linkStatus:
                            description: It is the Topology's linkStatus.
                            returned: success,changed,always
                            type: str
                            sample: '<linkstatus>'
                        source:
                            description: It is the Topology's source.
                            returned: success,changed,always
                            type: str
                            sample: '<source>'
                        startPortID:
                            description: It is the Topology's startPortID.
                            returned: success,changed,always
                            type: str
                            sample: '<startportid>'
                        startPortIpv4Address:
                            description: It is the Topology's startPortIpv4Address.
                            returned: success,changed,always
                            type: str
                            sample: '<startportipv4address>'
                        startPortIpv4Mask:
                            description: It is the Topology's startPortIpv4Mask.
                            returned: success,changed,always
                            type: str
                            sample: '<startportipv4mask>'
                        startPortName:
                            description: It is the Topology's startPortName.
                            returned: success,changed,always
                            type: str
                            sample: '<startportname>'
                        startPortSpeed:
                            description: It is the Topology's startPortSpeed.
                            returned: success,changed,always
                            type: str
                            sample: '<startportspeed>'
                        tag:
                            description: It is the Topology's tag.
                            returned: success,changed,always
                            type: str
                            sample: '<tag>'
                        target:
                            description: It is the Topology's target.
                            returned: success,changed,always
                            type: str
                            sample: '<target>'

                nodes:
                    description: It is the Topology's nodes.
                    returned: success,changed,always
                    type: list
                    contains:
                        aclApplied:
                            description: It is the Topology's aclApplied.
                            returned: success,changed,always
                            type: bool
                            sample: false
                        additionalInfo:
                            description: It is the Topology's additionalInfo.
                            returned: success,changed,always
                            type: dict
                        customParam:
                            description: It is the Topology's customParam.
                            returned: success,changed,always
                            type: dict
                            contains:
                                id:
                                    description: It is the Topology's id.
                                    returned: success,changed,always
                                    type: str
                                    sample: '478012'
                                label:
                                    description: It is the Topology's label.
                                    returned: success,changed,always
                                    type: str
                                    sample: '<label>'
                                parentNodeId:
                                    description: It is the Topology's parentNodeId.
                                    returned: success,changed,always
                                    type: str
                                    sample: '<parentnodeid>'
                                x:
                                    description: It is the Topology's x.
                                    returned: success,changed,always
                                    type: int
                                    sample: 0
                                y:
                                    description: It is the Topology's y.
                                    returned: success,changed,always
                                    type: int
                                    sample: 0

                        dataPathId:
                            description: It is the Topology's dataPathId.
                            returned: success,changed,always
                            type: str
                            sample: '<datapathid>'
                        deviceType:
                            description: It is the Topology's deviceType.
                            returned: success,changed,always
                            type: str
                            sample: '<devicetype>'
                        family:
                            description: It is the Topology's family.
                            returned: success,changed,always
                            type: str
                            sample: '<family>'
                        fixed:
                            description: It is the Topology's fixed.
                            returned: success,changed,always
                            type: bool
                            sample: false
                        greyOut:
                            description: It is the Topology's greyOut.
                            returned: success,changed,always
                            type: bool
                            sample: false
                        id:
                            description: It is the Topology's id.
                            returned: success,changed,always
                            type: str
                            sample: '478012'
                        ip:
                            description: It is the Topology's ip.
                            returned: success,changed,always
                            type: str
                            sample: '1.1.1.17'
                        label:
                            description: It is the Topology's label.
                            returned: success,changed,always
                            type: str
                            sample: '<label>'
                        networkType:
                            description: It is the Topology's networkType.
                            returned: success,changed,always
                            type: str
                            sample: '<networktype>'
                        nodeType:
                            description: It is the Topology's nodeType.
                            returned: success,changed,always
                            type: str
                            sample: '<nodetype>'
                        order:
                            description: It is the Topology's order.
                            returned: success,changed,always
                            type: int
                            sample: 0
                        osType:
                            description: It is the Topology's osType.
                            returned: success,changed,always
                            type: str
                            sample: '<ostype>'
                        platformId:
                            description: It is the Topology's platformId.
                            returned: success,changed,always
                            type: str
                            sample: '<platformid>'
                        role:
                            description: It is the Topology's role.
                            returned: success,changed,always
                            type: str
                            sample: '<role>'
                        roleSource:
                            description: It is the Topology's roleSource.
                            returned: success,changed,always
                            type: str
                            sample: '<rolesource>'
                        softwareVersion:
                            description: It is the Topology's softwareVersion.
                            returned: success,changed,always
                            type: str
                            sample: '<softwareversion>'
                        tags:
                            description: It is the Topology's tags.
                            returned: success,changed,always
                            type: list
                        upperNode:
                            description: It is the Topology's upperNode.
                            returned: success,changed,always
                            type: str
                            sample: '<uppernode>'
                        userId:
                            description: It is the Topology's userId.
                            returned: success,changed,always
                            type: str
                            sample: '<userid>'
                        vlanId:
                            description: It is the Topology's vlanId.
                            returned: success,changed,always
                            type: str
                            sample: '<vlanid>'
                        x:
                            description: It is the Topology's x.
                            returned: success,changed,always
                            type: int
                            sample: 0
                        y:
                            description: It is the Topology's y.
                            returned: success,changed,always
                            type: int
                            sample: 0


        version:
            description: Version, property of the response body.
            returned: success,changed,always
            type: str
            sample: '1.0'

data_2:
    description: Returns the raw physical Topology by specified criteria of nodeType.
    returned: success,changed,always
    type: dict
    contains:
        response:
            description: Response, property of the response body.
            returned: success,changed,always
            type: dict
            contains:
                id:
                    description: It is the Topology's id.
                    returned: success,changed,always
                    type: str
                    sample: '478012'
                links:
                    description: It is the Topology's links.
                    returned: success,changed,always
                    type: list
                    contains:
                        additionalInfo:
                            description: It is the Topology's additionalInfo.
                            returned: success,changed,always
                            type: dict
                        endPortID:
                            description: It is the Topology's endPortID.
                            returned: success,changed,always
                            type: str
                            sample: '<endportid>'
                        endPortIpv4Address:
                            description: It is the Topology's endPortIpv4Address.
                            returned: success,changed,always
                            type: str
                            sample: '<endportipv4address>'
                        endPortIpv4Mask:
                            description: It is the Topology's endPortIpv4Mask.
                            returned: success,changed,always
                            type: str
                            sample: '<endportipv4mask>'
                        endPortName:
                            description: It is the Topology's endPortName.
                            returned: success,changed,always
                            type: str
                            sample: '<endportname>'
                        endPortSpeed:
                            description: It is the Topology's endPortSpeed.
                            returned: success,changed,always
                            type: str
                            sample: '<endportspeed>'
                        greyOut:
                            description: It is the Topology's greyOut.
                            returned: success,changed,always
                            type: bool
                            sample: false
                        id:
                            description: It is the Topology's id.
                            returned: success,changed,always
                            type: str
                            sample: '478012'
                        linkStatus:
                            description: It is the Topology's linkStatus.
                            returned: success,changed,always
                            type: str
                            sample: '<linkstatus>'
                        source:
                            description: It is the Topology's source.
                            returned: success,changed,always
                            type: str
                            sample: '<source>'
                        startPortID:
                            description: It is the Topology's startPortID.
                            returned: success,changed,always
                            type: str
                            sample: '<startportid>'
                        startPortIpv4Address:
                            description: It is the Topology's startPortIpv4Address.
                            returned: success,changed,always
                            type: str
                            sample: '<startportipv4address>'
                        startPortIpv4Mask:
                            description: It is the Topology's startPortIpv4Mask.
                            returned: success,changed,always
                            type: str
                            sample: '<startportipv4mask>'
                        startPortName:
                            description: It is the Topology's startPortName.
                            returned: success,changed,always
                            type: str
                            sample: '<startportname>'
                        startPortSpeed:
                            description: It is the Topology's startPortSpeed.
                            returned: success,changed,always
                            type: str
                            sample: '<startportspeed>'
                        tag:
                            description: It is the Topology's tag.
                            returned: success,changed,always
                            type: str
                            sample: '<tag>'
                        target:
                            description: It is the Topology's target.
                            returned: success,changed,always
                            type: str
                            sample: '<target>'

                nodes:
                    description: It is the Topology's nodes.
                    returned: success,changed,always
                    type: list
                    contains:
                        aclApplied:
                            description: It is the Topology's aclApplied.
                            returned: success,changed,always
                            type: bool
                            sample: false
                        additionalInfo:
                            description: It is the Topology's additionalInfo.
                            returned: success,changed,always
                            type: dict
                        customParam:
                            description: It is the Topology's customParam.
                            returned: success,changed,always
                            type: dict
                            contains:
                                id:
                                    description: It is the Topology's id.
                                    returned: success,changed,always
                                    type: str
                                    sample: '478012'
                                label:
                                    description: It is the Topology's label.
                                    returned: success,changed,always
                                    type: str
                                    sample: '<label>'
                                parentNodeId:
                                    description: It is the Topology's parentNodeId.
                                    returned: success,changed,always
                                    type: str
                                    sample: '<parentnodeid>'
                                x:
                                    description: It is the Topology's x.
                                    returned: success,changed,always
                                    type: int
                                    sample: 0
                                y:
                                    description: It is the Topology's y.
                                    returned: success,changed,always
                                    type: int
                                    sample: 0

                        dataPathId:
                            description: It is the Topology's dataPathId.
                            returned: success,changed,always
                            type: str
                            sample: '<datapathid>'
                        deviceType:
                            description: It is the Topology's deviceType.
                            returned: success,changed,always
                            type: str
                            sample: '<devicetype>'
                        family:
                            description: It is the Topology's family.
                            returned: success,changed,always
                            type: str
                            sample: '<family>'
                        fixed:
                            description: It is the Topology's fixed.
                            returned: success,changed,always
                            type: bool
                            sample: false
                        greyOut:
                            description: It is the Topology's greyOut.
                            returned: success,changed,always
                            type: bool
                            sample: false
                        id:
                            description: It is the Topology's id.
                            returned: success,changed,always
                            type: str
                            sample: '478012'
                        ip:
                            description: It is the Topology's ip.
                            returned: success,changed,always
                            type: str
                            sample: '1.1.1.17'
                        label:
                            description: It is the Topology's label.
                            returned: success,changed,always
                            type: str
                            sample: '<label>'
                        networkType:
                            description: It is the Topology's networkType.
                            returned: success,changed,always
                            type: str
                            sample: '<networktype>'
                        nodeType:
                            description: It is the Topology's nodeType.
                            returned: success,changed,always
                            type: str
                            sample: '<nodetype>'
                        order:
                            description: It is the Topology's order.
                            returned: success,changed,always
                            type: int
                            sample: 0
                        osType:
                            description: It is the Topology's osType.
                            returned: success,changed,always
                            type: str
                            sample: '<ostype>'
                        platformId:
                            description: It is the Topology's platformId.
                            returned: success,changed,always
                            type: str
                            sample: '<platformid>'
                        role:
                            description: It is the Topology's role.
                            returned: success,changed,always
                            type: str
                            sample: '<role>'
                        roleSource:
                            description: It is the Topology's roleSource.
                            returned: success,changed,always
                            type: str
                            sample: '<rolesource>'
                        softwareVersion:
                            description: It is the Topology's softwareVersion.
                            returned: success,changed,always
                            type: str
                            sample: '<softwareversion>'
                        tags:
                            description: It is the Topology's tags.
                            returned: success,changed,always
                            type: list
                        upperNode:
                            description: It is the Topology's upperNode.
                            returned: success,changed,always
                            type: str
                            sample: '<uppernode>'
                        userId:
                            description: It is the Topology's userId.
                            returned: success,changed,always
                            type: str
                            sample: '<userid>'
                        vlanId:
                            description: It is the Topology's vlanId.
                            returned: success,changed,always
                            type: str
                            sample: '<vlanid>'
                        x:
                            description: It is the Topology's x.
                            returned: success,changed,always
                            type: int
                            sample: 0
                        y:
                            description: It is the Topology's y.
                            returned: success,changed,always
                            type: int
                            sample: 0


        version:
            description: Version, property of the response body.
            returned: success,changed,always
            type: str
            sample: '1.0'

data_3:
    description: Returns site Topology.
    returned: success,changed,always
    type: dict
    contains:
        response:
            description: Response, property of the response body.
            returned: success,changed,always
            type: dict
            contains:
                sites:
                    description: It is the Topology's sites.
                    returned: success,changed,always
                    type: list
                    contains:
                        displayName:
                            description: It is the Topology's displayName.
                            returned: success,changed,always
                            type: str
                            sample: '<displayname>'
                        groupNameHierarchy:
                            description: It is the Topology's groupNameHierarchy.
                            returned: success,changed,always
                            type: str
                            sample: '<groupnamehierarchy>'
                        id:
                            description: It is the Topology's id.
                            returned: success,changed,always
                            type: str
                            sample: '478012'
                        latitude:
                            description: It is the Topology's latitude.
                            returned: success,changed,always
                            type: str
                            sample: '<latitude>'
                        locationAddress:
                            description: It is the Topology's locationAddress.
                            returned: success,changed,always
                            type: str
                            sample: '<locationaddress>'
                        locationCountry:
                            description: It is the Topology's locationCountry.
                            returned: success,changed,always
                            type: str
                            sample: '<locationcountry>'
                        locationType:
                            description: It is the Topology's locationType.
                            returned: success,changed,always
                            type: str
                            sample: '<locationtype>'
                        longitude:
                            description: It is the Topology's longitude.
                            returned: success,changed,always
                            type: str
                            sample: '<longitude>'
                        name:
                            description: It is the Topology's name.
                            returned: success,changed,always
                            type: str
                            sample: '<name>'
                        parentId:
                            description: It is the Topology's parentId.
                            returned: success,changed,always
                            type: str
                            sample: '<parentid>'


        version:
            description: Version, property of the response body.
            returned: success,changed,always
            type: str
            sample: '1.0'

data_4:
    description: Returns the list of VLAN names.
    returned: success,changed,always
    type: dict
    contains:
        response:
            description: Response, property of the response body (list of strings).
            returned: success,changed,always
            type: list
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
from ansible_collections.cisco.dnac.plugins.module_utils.definitions.topology import (
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

    dnac.exit_json()


if __name__ == "__main__":
    main()
