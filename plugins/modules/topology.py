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
module: topology
short_description: Manage Topology objects of Topology
description:
- Returns Layer 2 network Topology by specified VLAN ID.
- Returns the Layer 3 network Topology by routing protocol.
- Returns the raw physical Topology by specified criteria of nodeType.
- Returns site Topology.
- Returns the list of VLAN names.
version_added: '1.0'
author: Rafael Campos (@racampos)
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
- name: get_topology_details
  cisco.dnac.topology:
    state: query  # required
    vlan_id: SomeValue  # string, required
    layer2: True  # boolean, required
  register: query_result
  
- name: get_l3_topology_details
  cisco.dnac.topology:
    state: query  # required
    topology_type: SomeValue  # string, required
    layer3: True  # boolean, required
  register: query_result
  
- name: get_physical_topology
  cisco.dnac.topology:
    state: query  # required
    physical: True  # boolean, required
    node_type: SomeValue  # string
  register: query_result
  
- name: get_site_topology
  cisco.dnac.topology:
    state: query  # required
    site: True  # boolean, required
  register: query_result
  
- name: get_vlan_details
  cisco.dnac.topology:
    state: query  # required
    vlan: True  # boolean, required
  register: query_result
  
"""

RETURN = """
get_topology_details:
    description: Returns Layer 2 network Topology by specified VLAN ID.
    returned: always
    type: dict
    contains:
    response:
      description: Response, property of the response body.
      returned: always
      type: dict
      contains:
        id:
          description: It is the Topology's id.
          returned: always
          type: str
          sample: '478012'
        links:
          description: It is the Topology's links.
          returned: always
          type: list
          contains:
            additionalInfo:
              description: It is the Topology's additionalInfo.
              returned: always
              type: dict
            endPortID:
              description: It is the Topology's endPortID.
              returned: always
              type: str
              sample: '<endportid>'
            endPortIpv4Address:
              description: It is the Topology's endPortIpv4Address.
              returned: always
              type: str
              sample: '<endportipv4address>'
            endPortIpv4Mask:
              description: It is the Topology's endPortIpv4Mask.
              returned: always
              type: str
              sample: '<endportipv4mask>'
            endPortName:
              description: It is the Topology's endPortName.
              returned: always
              type: str
              sample: '<endportname>'
            endPortSpeed:
              description: It is the Topology's endPortSpeed.
              returned: always
              type: str
              sample: '<endportspeed>'
            greyOut:
              description: It is the Topology's greyOut.
              returned: always
              type: bool
              sample: false
            id:
              description: It is the Topology's id.
              returned: always
              type: str
              sample: '478012'
            linkStatus:
              description: It is the Topology's linkStatus.
              returned: always
              type: str
              sample: '<linkstatus>'
            source:
              description: It is the Topology's source.
              returned: always
              type: str
              sample: '<source>'
            startPortID:
              description: It is the Topology's startPortID.
              returned: always
              type: str
              sample: '<startportid>'
            startPortIpv4Address:
              description: It is the Topology's startPortIpv4Address.
              returned: always
              type: str
              sample: '<startportipv4address>'
            startPortIpv4Mask:
              description: It is the Topology's startPortIpv4Mask.
              returned: always
              type: str
              sample: '<startportipv4mask>'
            startPortName:
              description: It is the Topology's startPortName.
              returned: always
              type: str
              sample: '<startportname>'
            startPortSpeed:
              description: It is the Topology's startPortSpeed.
              returned: always
              type: str
              sample: '<startportspeed>'
            tag:
              description: It is the Topology's tag.
              returned: always
              type: str
              sample: '<tag>'
            target:
              description: It is the Topology's target.
              returned: always
              type: str
              sample: '<target>'

        nodes:
          description: It is the Topology's nodes.
          returned: always
          type: list
          contains:
            aclApplied:
              description: It is the Topology's aclApplied.
              returned: always
              type: bool
              sample: false
            additionalInfo:
              description: It is the Topology's additionalInfo.
              returned: always
              type: dict
            customParam:
              description: It is the Topology's customParam.
              returned: always
              type: dict
              contains:
                id:
                  description: It is the Topology's id.
                  returned: always
                  type: str
                  sample: '478012'
                label:
                  description: It is the Topology's label.
                  returned: always
                  type: str
                  sample: '<label>'
                parentNodeId:
                  description: It is the Topology's parentNodeId.
                  returned: always
                  type: str
                  sample: '<parentnodeid>'
                x:
                  description: It is the Topology's x.
                  returned: always
                  type: int
                  sample: 0
                y:
                  description: It is the Topology's y.
                  returned: always
                  type: int
                  sample: 0

            dataPathId:
              description: It is the Topology's dataPathId.
              returned: always
              type: str
              sample: '<datapathid>'
            deviceType:
              description: It is the Topology's deviceType.
              returned: always
              type: str
              sample: '<devicetype>'
            family:
              description: It is the Topology's family.
              returned: always
              type: str
              sample: '<family>'
            fixed:
              description: It is the Topology's fixed.
              returned: always
              type: bool
              sample: false
            greyOut:
              description: It is the Topology's greyOut.
              returned: always
              type: bool
              sample: false
            id:
              description: It is the Topology's id.
              returned: always
              type: str
              sample: '478012'
            ip:
              description: It is the Topology's ip.
              returned: always
              type: str
              sample: '1.1.1.17'
            label:
              description: It is the Topology's label.
              returned: always
              type: str
              sample: '<label>'
            networkType:
              description: It is the Topology's networkType.
              returned: always
              type: str
              sample: '<networktype>'
            nodeType:
              description: It is the Topology's nodeType.
              returned: always
              type: str
              sample: '<nodetype>'
            order:
              description: It is the Topology's order.
              returned: always
              type: int
              sample: 0
            osType:
              description: It is the Topology's osType.
              returned: always
              type: str
              sample: '<ostype>'
            platformId:
              description: It is the Topology's platformId.
              returned: always
              type: str
              sample: '<platformid>'
            role:
              description: It is the Topology's role.
              returned: always
              type: str
              sample: '<role>'
            roleSource:
              description: It is the Topology's roleSource.
              returned: always
              type: str
              sample: '<rolesource>'
            softwareVersion:
              description: It is the Topology's softwareVersion.
              returned: always
              type: str
              sample: '<softwareversion>'
            tags:
              description: It is the Topology's tags.
              returned: always
              type: list
            upperNode:
              description: It is the Topology's upperNode.
              returned: always
              type: str
              sample: '<uppernode>'
            userId:
              description: It is the Topology's userId.
              returned: always
              type: str
              sample: '<userid>'
            vlanId:
              description: It is the Topology's vlanId.
              returned: always
              type: str
              sample: '<vlanid>'
            x:
              description: It is the Topology's x.
              returned: always
              type: int
              sample: 0
            y:
              description: It is the Topology's y.
              returned: always
              type: int
              sample: 0


    version:
      description: Version, property of the response body.
      returned: always
      type: str
      sample: '1.0'

get_l3_topology_details:
    description: Returns the Layer 3 network Topology by routing protocol.
    returned: always
    type: dict
    contains:
    response:
      description: Response, property of the response body.
      returned: always
      type: dict
      contains:
        id:
          description: It is the Topology's id.
          returned: always
          type: str
          sample: '478012'
        links:
          description: It is the Topology's links.
          returned: always
          type: list
          contains:
            additionalInfo:
              description: It is the Topology's additionalInfo.
              returned: always
              type: dict
            endPortID:
              description: It is the Topology's endPortID.
              returned: always
              type: str
              sample: '<endportid>'
            endPortIpv4Address:
              description: It is the Topology's endPortIpv4Address.
              returned: always
              type: str
              sample: '<endportipv4address>'
            endPortIpv4Mask:
              description: It is the Topology's endPortIpv4Mask.
              returned: always
              type: str
              sample: '<endportipv4mask>'
            endPortName:
              description: It is the Topology's endPortName.
              returned: always
              type: str
              sample: '<endportname>'
            endPortSpeed:
              description: It is the Topology's endPortSpeed.
              returned: always
              type: str
              sample: '<endportspeed>'
            greyOut:
              description: It is the Topology's greyOut.
              returned: always
              type: bool
              sample: false
            id:
              description: It is the Topology's id.
              returned: always
              type: str
              sample: '478012'
            linkStatus:
              description: It is the Topology's linkStatus.
              returned: always
              type: str
              sample: '<linkstatus>'
            source:
              description: It is the Topology's source.
              returned: always
              type: str
              sample: '<source>'
            startPortID:
              description: It is the Topology's startPortID.
              returned: always
              type: str
              sample: '<startportid>'
            startPortIpv4Address:
              description: It is the Topology's startPortIpv4Address.
              returned: always
              type: str
              sample: '<startportipv4address>'
            startPortIpv4Mask:
              description: It is the Topology's startPortIpv4Mask.
              returned: always
              type: str
              sample: '<startportipv4mask>'
            startPortName:
              description: It is the Topology's startPortName.
              returned: always
              type: str
              sample: '<startportname>'
            startPortSpeed:
              description: It is the Topology's startPortSpeed.
              returned: always
              type: str
              sample: '<startportspeed>'
            tag:
              description: It is the Topology's tag.
              returned: always
              type: str
              sample: '<tag>'
            target:
              description: It is the Topology's target.
              returned: always
              type: str
              sample: '<target>'

        nodes:
          description: It is the Topology's nodes.
          returned: always
          type: list
          contains:
            aclApplied:
              description: It is the Topology's aclApplied.
              returned: always
              type: bool
              sample: false
            additionalInfo:
              description: It is the Topology's additionalInfo.
              returned: always
              type: dict
            customParam:
              description: It is the Topology's customParam.
              returned: always
              type: dict
              contains:
                id:
                  description: It is the Topology's id.
                  returned: always
                  type: str
                  sample: '478012'
                label:
                  description: It is the Topology's label.
                  returned: always
                  type: str
                  sample: '<label>'
                parentNodeId:
                  description: It is the Topology's parentNodeId.
                  returned: always
                  type: str
                  sample: '<parentnodeid>'
                x:
                  description: It is the Topology's x.
                  returned: always
                  type: int
                  sample: 0
                y:
                  description: It is the Topology's y.
                  returned: always
                  type: int
                  sample: 0

            dataPathId:
              description: It is the Topology's dataPathId.
              returned: always
              type: str
              sample: '<datapathid>'
            deviceType:
              description: It is the Topology's deviceType.
              returned: always
              type: str
              sample: '<devicetype>'
            family:
              description: It is the Topology's family.
              returned: always
              type: str
              sample: '<family>'
            fixed:
              description: It is the Topology's fixed.
              returned: always
              type: bool
              sample: false
            greyOut:
              description: It is the Topology's greyOut.
              returned: always
              type: bool
              sample: false
            id:
              description: It is the Topology's id.
              returned: always
              type: str
              sample: '478012'
            ip:
              description: It is the Topology's ip.
              returned: always
              type: str
              sample: '1.1.1.17'
            label:
              description: It is the Topology's label.
              returned: always
              type: str
              sample: '<label>'
            networkType:
              description: It is the Topology's networkType.
              returned: always
              type: str
              sample: '<networktype>'
            nodeType:
              description: It is the Topology's nodeType.
              returned: always
              type: str
              sample: '<nodetype>'
            order:
              description: It is the Topology's order.
              returned: always
              type: int
              sample: 0
            osType:
              description: It is the Topology's osType.
              returned: always
              type: str
              sample: '<ostype>'
            platformId:
              description: It is the Topology's platformId.
              returned: always
              type: str
              sample: '<platformid>'
            role:
              description: It is the Topology's role.
              returned: always
              type: str
              sample: '<role>'
            roleSource:
              description: It is the Topology's roleSource.
              returned: always
              type: str
              sample: '<rolesource>'
            softwareVersion:
              description: It is the Topology's softwareVersion.
              returned: always
              type: str
              sample: '<softwareversion>'
            tags:
              description: It is the Topology's tags.
              returned: always
              type: list
            upperNode:
              description: It is the Topology's upperNode.
              returned: always
              type: str
              sample: '<uppernode>'
            userId:
              description: It is the Topology's userId.
              returned: always
              type: str
              sample: '<userid>'
            vlanId:
              description: It is the Topology's vlanId.
              returned: always
              type: str
              sample: '<vlanid>'
            x:
              description: It is the Topology's x.
              returned: always
              type: int
              sample: 0
            y:
              description: It is the Topology's y.
              returned: always
              type: int
              sample: 0


    version:
      description: Version, property of the response body.
      returned: always
      type: str
      sample: '1.0'

get_physical_topology:
    description: Returns the raw physical Topology by specified criteria of nodeType.
    returned: always
    type: dict
    contains:
    response:
      description: Response, property of the response body.
      returned: always
      type: dict
      contains:
        id:
          description: It is the Topology's id.
          returned: always
          type: str
          sample: '478012'
        links:
          description: It is the Topology's links.
          returned: always
          type: list
          contains:
            additionalInfo:
              description: It is the Topology's additionalInfo.
              returned: always
              type: dict
            endPortID:
              description: It is the Topology's endPortID.
              returned: always
              type: str
              sample: '<endportid>'
            endPortIpv4Address:
              description: It is the Topology's endPortIpv4Address.
              returned: always
              type: str
              sample: '<endportipv4address>'
            endPortIpv4Mask:
              description: It is the Topology's endPortIpv4Mask.
              returned: always
              type: str
              sample: '<endportipv4mask>'
            endPortName:
              description: It is the Topology's endPortName.
              returned: always
              type: str
              sample: '<endportname>'
            endPortSpeed:
              description: It is the Topology's endPortSpeed.
              returned: always
              type: str
              sample: '<endportspeed>'
            greyOut:
              description: It is the Topology's greyOut.
              returned: always
              type: bool
              sample: false
            id:
              description: It is the Topology's id.
              returned: always
              type: str
              sample: '478012'
            linkStatus:
              description: It is the Topology's linkStatus.
              returned: always
              type: str
              sample: '<linkstatus>'
            source:
              description: It is the Topology's source.
              returned: always
              type: str
              sample: '<source>'
            startPortID:
              description: It is the Topology's startPortID.
              returned: always
              type: str
              sample: '<startportid>'
            startPortIpv4Address:
              description: It is the Topology's startPortIpv4Address.
              returned: always
              type: str
              sample: '<startportipv4address>'
            startPortIpv4Mask:
              description: It is the Topology's startPortIpv4Mask.
              returned: always
              type: str
              sample: '<startportipv4mask>'
            startPortName:
              description: It is the Topology's startPortName.
              returned: always
              type: str
              sample: '<startportname>'
            startPortSpeed:
              description: It is the Topology's startPortSpeed.
              returned: always
              type: str
              sample: '<startportspeed>'
            tag:
              description: It is the Topology's tag.
              returned: always
              type: str
              sample: '<tag>'
            target:
              description: It is the Topology's target.
              returned: always
              type: str
              sample: '<target>'

        nodes:
          description: It is the Topology's nodes.
          returned: always
          type: list
          contains:
            aclApplied:
              description: It is the Topology's aclApplied.
              returned: always
              type: bool
              sample: false
            additionalInfo:
              description: It is the Topology's additionalInfo.
              returned: always
              type: dict
            customParam:
              description: It is the Topology's customParam.
              returned: always
              type: dict
              contains:
                id:
                  description: It is the Topology's id.
                  returned: always
                  type: str
                  sample: '478012'
                label:
                  description: It is the Topology's label.
                  returned: always
                  type: str
                  sample: '<label>'
                parentNodeId:
                  description: It is the Topology's parentNodeId.
                  returned: always
                  type: str
                  sample: '<parentnodeid>'
                x:
                  description: It is the Topology's x.
                  returned: always
                  type: int
                  sample: 0
                y:
                  description: It is the Topology's y.
                  returned: always
                  type: int
                  sample: 0

            dataPathId:
              description: It is the Topology's dataPathId.
              returned: always
              type: str
              sample: '<datapathid>'
            deviceType:
              description: It is the Topology's deviceType.
              returned: always
              type: str
              sample: '<devicetype>'
            family:
              description: It is the Topology's family.
              returned: always
              type: str
              sample: '<family>'
            fixed:
              description: It is the Topology's fixed.
              returned: always
              type: bool
              sample: false
            greyOut:
              description: It is the Topology's greyOut.
              returned: always
              type: bool
              sample: false
            id:
              description: It is the Topology's id.
              returned: always
              type: str
              sample: '478012'
            ip:
              description: It is the Topology's ip.
              returned: always
              type: str
              sample: '1.1.1.17'
            label:
              description: It is the Topology's label.
              returned: always
              type: str
              sample: '<label>'
            networkType:
              description: It is the Topology's networkType.
              returned: always
              type: str
              sample: '<networktype>'
            nodeType:
              description: It is the Topology's nodeType.
              returned: always
              type: str
              sample: '<nodetype>'
            order:
              description: It is the Topology's order.
              returned: always
              type: int
              sample: 0
            osType:
              description: It is the Topology's osType.
              returned: always
              type: str
              sample: '<ostype>'
            platformId:
              description: It is the Topology's platformId.
              returned: always
              type: str
              sample: '<platformid>'
            role:
              description: It is the Topology's role.
              returned: always
              type: str
              sample: '<role>'
            roleSource:
              description: It is the Topology's roleSource.
              returned: always
              type: str
              sample: '<rolesource>'
            softwareVersion:
              description: It is the Topology's softwareVersion.
              returned: always
              type: str
              sample: '<softwareversion>'
            tags:
              description: It is the Topology's tags.
              returned: always
              type: list
            upperNode:
              description: It is the Topology's upperNode.
              returned: always
              type: str
              sample: '<uppernode>'
            userId:
              description: It is the Topology's userId.
              returned: always
              type: str
              sample: '<userid>'
            vlanId:
              description: It is the Topology's vlanId.
              returned: always
              type: str
              sample: '<vlanid>'
            x:
              description: It is the Topology's x.
              returned: always
              type: int
              sample: 0
            y:
              description: It is the Topology's y.
              returned: always
              type: int
              sample: 0


    version:
      description: Version, property of the response body.
      returned: always
      type: str
      sample: '1.0'

get_site_topology:
    description: Returns site Topology.
    returned: always
    type: dict
    contains:
    response:
      description: Response, property of the response body.
      returned: always
      type: dict
      contains:
        sites:
          description: It is the Topology's sites.
          returned: always
          type: list
          contains:
            displayName:
              description: It is the Topology's displayName.
              returned: always
              type: str
              sample: '<displayname>'
            groupNameHierarchy:
              description: It is the Topology's groupNameHierarchy.
              returned: always
              type: str
              sample: '<groupnamehierarchy>'
            id:
              description: It is the Topology's id.
              returned: always
              type: str
              sample: '478012'
            latitude:
              description: It is the Topology's latitude.
              returned: always
              type: str
              sample: '<latitude>'
            locationAddress:
              description: It is the Topology's locationAddress.
              returned: always
              type: str
              sample: '<locationaddress>'
            locationCountry:
              description: It is the Topology's locationCountry.
              returned: always
              type: str
              sample: '<locationcountry>'
            locationType:
              description: It is the Topology's locationType.
              returned: always
              type: str
              sample: '<locationtype>'
            longitude:
              description: It is the Topology's longitude.
              returned: always
              type: str
              sample: '<longitude>'
            name:
              description: It is the Topology's name.
              returned: always
              type: str
              sample: '<name>'
            parentId:
              description: It is the Topology's parentId.
              returned: always
              type: str
              sample: '<parentid>'


    version:
      description: Version, property of the response body.
      returned: always
      type: str
      sample: '1.0'

get_vlan_details:
    description: Returns the list of VLAN names.
    returned: always
    type: dict
    contains:
    response:
      description: Response, property of the response body (list of strings).
      returned: always
      type: list
    version:
      description: Version, property of the response body.
      returned: always
      type: str
      sample: '1.0'

"""
