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
module: network
short_description: Manage Network objects of NetworkSettings
description:
- API to get DHCP and DNS center server details.
- API to create a Network for DHCP and DNS center server settings.
- API to update Network for DHCP and DNS center server settings.
version_added: '1.0.0'
author: Rafael Campos (@racampos)
options:
  site_id:
    description:
    - Site id to get the Network settings associated with the site.
    - Site id to which site details to associate with the Network settings.
    - Site id to update the Network settings which is associated with the site.
    - Required for states create and update.
    type: str
  settings:
    description:
    - Settings, property of the request body.
    type: dict
    required: True
    suboptions:
      clientAndEndpoint_aaa:
        description:
        - It is the Network's clientAndEndpoint_aaa.
        type: dict
        suboptions:
          ipAddress:
            description:
            - It is the Network's ipAddress.
            type: str
          network:
            description:
            - It is the Network's Network.
            type: str
          protocol:
            description:
            - It is the Network's protocol.
            type: str
          servers:
            description:
            - It is the Network's servers.
            type: str
          sharedSecret:
            description:
            - It is the Network's sharedSecret.
            type: str

      dhcpServer:
        description:
        - It is the Network's dhcpServer.
        type: list
      dnsServer:
        description:
        - It is the Network's dnsServer.
        type: dict
        suboptions:
          domainName:
            description:
            - It is the Network's domainName.
            type: str
          primaryIpAddress:
            description:
            - It is the Network's primaryIpAddress.
            type: str
          secondaryIpAddress:
            description:
            - It is the Network's secondaryIpAddress.
            type: str

      messageOfTheday:
        description:
        - It is the Network's messageOfTheday.
        type: dict
        suboptions:
          bannerMessage:
            description:
            - It is the Network's bannerMessage.
            type: str
          retainExistingBanner:
            description:
            - It is the Network's retainExistingBanner.
            type: bool

      netflowcollector:
        description:
        - It is the Network's netflowcollector.
        type: dict
        suboptions:
          ipAddress:
            description:
            - It is the Network's ipAddress.
            type: str
          port:
            description:
            - It is the Network's port.
            type: int

      network_aaa:
        description:
        - It is the Network's Network_aaa.
        type: dict
        suboptions:
          ipAddress:
            description:
            - It is the Network's ipAddress.
            type: str
          network:
            description:
            - It is the Network's Network.
            type: str
          protocol:
            description:
            - It is the Network's protocol.
            type: str
          servers:
            description:
            - It is the Network's servers.
            type: str
          sharedSecret:
            description:
            - It is the Network's sharedSecret.
            type: str

      ntpServer:
        description:
        - It is the Network's ntpServer.
        type: list
      snmpServer:
        description:
        - It is the Network's snmpServer.
        type: dict
        suboptions:
          configureDnacIP:
            description:
            - It is the Network's configureDnacIP.
            type: bool
          ipAddresses:
            description:
            - It is the Network's ipAddresses.
            type: list

      syslogServer:
        description:
        - It is the Network's syslogServer.
        type: dict
        suboptions:
          configureDnacIP:
            description:
            - It is the Network's configureDnacIP.
            type: bool
          ipAddresses:
            description:
            - It is the Network's ipAddresses.
            type: list

      timezone:
        description:
        - It is the Network's timezone.
        type: str


requirements:
- dnacentersdk
seealso:
# Reference by module name
- module: cisco.dnac.plugins.module_utils.definitions.network
# Reference by Internet resource
- name: Network reference
  description: Complete reference of the Network object model.
  link: https://developer.cisco.com/docs/dna-center/api/1-3-3-x
# Reference by Internet resource
- name: Network reference
  description: SDK reference.
  link: https://dnacentersdk.readthedocs.io/en/latest/api/api.html#v2-1-1-summary
"""

EXAMPLES = r"""
- name: get_network
  cisco.dnac.network:
    state: query  # required
    site_id: SomeValue  # string
  register: query_result
  
- name: create_network
  cisco.dnac.network:
    state: create  # required
    site_id: SomeValue  # string, required
    settings:  # required
      dhcpServer:
      - SomeValue  # string
      dnsServer:
        domainName: SomeValue  # string
        primaryIpAddress: SomeValue  # string
        secondaryIpAddress: SomeValue  # string
      syslogServer:
        ipAddresses:
        - SomeValue  # string
        configureDnacIP: True  # boolean
      snmpServer:
        ipAddresses:
        - SomeValue  # string
        configureDnacIP: True  # boolean
      netflowcollector:
        ipAddress: SomeValue  # string
        port: 1  #  number
      ntpServer:
      - SomeValue  # string
      timezone: SomeValue  # string
      messageOfTheday:
        bannerMessage: SomeValue  # string
        retainExistingBanner: True  # boolean
      network_aaa:
        servers: SomeValue  # string
        ipAddress: SomeValue  # string
        network: SomeValue  # string
        protocol: SomeValue  # string
        sharedSecret: SomeValue  # string
      clientAndEndpoint_aaa:
        servers: SomeValue  # string
        ipAddress: SomeValue  # string
        network: SomeValue  # string
        protocol: SomeValue  # string
        sharedSecret: SomeValue  # string
  
- name: update_network
  cisco.dnac.network:
    state: update  # required
    site_id: SomeValue  # string, required
    settings:  # required
      dhcpServer:
      - SomeValue  # string
      dnsServer:
        domainName: SomeValue  # string
        primaryIpAddress: SomeValue  # string
        secondaryIpAddress: SomeValue  # string
      syslogServer:
        ipAddresses:
        - SomeValue  # string
        configureDnacIP: True  # boolean
      snmpServer:
        ipAddresses:
        - SomeValue  # string
        configureDnacIP: True  # boolean
      netflowcollector:
        ipAddress: SomeValue  # string
        port: 1  #  number
      ntpServer:
      - SomeValue  # string
      timezone: SomeValue  # string
      messageOfTheday:
        bannerMessage: SomeValue  # string
        retainExistingBanner: True  # boolean
      network_aaa:
        servers: SomeValue  # string
        ipAddress: SomeValue  # string
        network: SomeValue  # string
        protocol: SomeValue  # string
        sharedSecret: SomeValue  # string
      clientAndEndpoint_aaa:
        servers: SomeValue  # string
        ipAddress: SomeValue  # string
        network: SomeValue  # string
        protocol: SomeValue  # string
        sharedSecret: SomeValue  # string
  
"""

RETURN = """
get_network:
    description: API to get DHCP and DNS center server details.
    returned: always
    type: dict
    contains:
      response:
      description: Response, property of the response body (list of objects).
      returned: always
      type: list
      contains:
        instanceType:
          description: It is the Network's instanceType.
          returned: always
          type: str
          sample: '<instancetype>'
        instanceUuid:
          description: It is the Network's instanceUuid.
          returned: always
          type: str
          sample: '<instanceuuid>'
        namespace:
          description: It is the Network's namespace.
          returned: always
          type: str
          sample: '<namespace>'
        type:
          description: It is the Network's type.
          returned: always
          type: str
          sample: '<type>'
        key:
          description: It is the Network's key.
          returned: always
          type: str
          sample: '<key>'
        version:
          description: It is the Network's version.
          returned: always
          type: int
          sample: 0
        value:
          description: It is the Network's value.
          returned: always
          type: list
          contains:
            ipAddresses:
              description: It is the Network's ipAddresses.
              returned: always
              type: list
            configureDnacIP:
              description: It is the Network's configureDnacIP.
              returned: always
              type: bool
              sample: false

        groupUuid:
          description: It is the Network's groupUuid.
          returned: always
          type: str
          sample: '<groupuuid>'
        inheritedGroupUuid:
          description: It is the Network's inheritedGroupUuid.
          returned: always
          type: str
          sample: '<inheritedgroupuuid>'
        inheritedGroupName:
          description: It is the Network's inheritedGroupName.
          returned: always
          type: str
          sample: '<inheritedgroupname>'

    version:
      description: Version, property of the response body.
      returned: always
      type: str
      sample: '1.0'

create_network:
    description: API to create a Network for DHCP and DNS center server settings.
    returned: success
    type: dict
    contains:
      executionId:
      description: Execution Id, property of the response body.
      returned: success
      type: str
      sample: '<executionid>'
    executionStatusUrl:
      description: Execution Status Url, property of the response body.
      returned: success
      type: str
      sample: '<executionstatusurl>'
    message:
      description: Message, property of the response body.
      returned: success
      type: str
      sample: '<message>'

update_network:
    description: API to update Network for DHCP and DNS center server settings.
    returned: changed
    type: dict
    contains:
      executionId:
      description: Execution Id, property of the response body.
      returned: changed
      type: str
      sample: '<executionid>'
    executionStatusUrl:
      description: Execution Status Url, property of the response body.
      returned: changed
      type: str
      sample: '<executionstatusurl>'
    message:
      description: Message, property of the response body.
      returned: changed
      type: str
      sample: '<message>'

"""
