#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright: (c) 2020, Rafael Campos <rcampos@altus.cr>
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

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
    - Required for states update and create.
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
  register: nm_get_network

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

RETURN = r"""
dnac_response:
  description: A dictionary with the response returned by the DNA Center Python SDK
  returned: always
  type: dict
  sample: {"response": 29, "version": "1.0"}
sdk_function:
  description: The DNA Center SDK function used to execute the task
  returned: always
  type: str
  sample: network_settings.create_network
missing_params:
  description: Provided arguments do not comply with the schema of the DNA Center Python SDK function
  returned: when the function request schema is not satisfied
  type: list
  sample:
"""
