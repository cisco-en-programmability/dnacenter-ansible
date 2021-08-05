#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: network_update
short_description: Resource module for Network Update
description:
- Manage operation update of the resource Network Update.
version_added: '1.0.0'
author: Rafael Campos (@racampos)
options:
  settings:
    description: Network Update's settings.
    suboptions:
      clientAndEndpoint_aaa:
        description: Network Update's clientAndEndpoint_aaa.
        suboptions:
          additionalIp:
            description: Network Update's additionalIp.
            elements: str
            type: list
          ipAddress:
            description: Mandatory for ISE servers.
            type: str
          network:
            description: Network Update's network.
            type: str
          protocol:
            description: Network Update's protocol.
            type: str
          servers:
            description: Network Update's servers.
            type: str
          sharedSecret:
            description: Supported only by ISE servers.
            type: str
        type: dict
      dhcpServer:
        description: Network Update's dhcpServer.
        elements: str
        type: list
      dnsServer:
        description: Network Update's dnsServer.
        suboptions:
          domainName:
            description: Can only contain alphanumeric characters or hyphen.
            type: str
          primaryIpAddress:
            description: Valid range 1.0.0.0 - 223.255.255.255.
            type: str
          secondaryIpAddress:
            description: Valid range 1.0.0.0 - 223.255.255.255.
            type: str
        type: dict
      messageOfTheday:
        description: Network Update's messageOfTheday.
        suboptions:
          bannerMessage:
            description: Network Update's bannerMessage.
            type: str
          retainExistingBanner:
            description: RetainExistingBanner flag.
            type: bool
        type: dict
      netflowcollector:
        description: Network Update's netflowcollector.
        suboptions:
          ipAddress:
            description: Network Update's ipAddress.
            type: str
          port:
            description: Network Update's port.
            type: int
        type: dict
      network_aaa:
        description: Network Update's network_aaa.
        suboptions:
          additionalIp:
            description: Network Update's additionalIp.
            elements: str
            type: list
          ipAddress:
            description: Mandatory for ISE servers and for AAA consider this as additional
              Ip.
            type: str
          network:
            description: For AAA server consider it as primary IP and For ISE consider
              as Network.
            type: str
          protocol:
            description: Network Update's protocol.
            type: str
          servers:
            description: Server type supported by ISE and AAA.
            type: str
          sharedSecret:
            description: Supported only by ISE servers.
            type: str
        type: dict
      ntpServer:
        description: Network Update's ntpServer.
        elements: str
        type: list
      snmpServer:
        description: Network Update's snmpServer.
        suboptions:
          configureDnacIP:
            description: ConfigureDnacIP flag.
            type: bool
          ipAddresses:
            description: Network Update's ipAddresses.
            elements: str
            type: list
        type: dict
      syslogServer:
        description: Network Update's syslogServer.
        suboptions:
          configureDnacIP:
            description: ConfigureDnacIP flag.
            type: bool
          ipAddresses:
            description: Network Update's ipAddresses.
            elements: str
            type: list
        type: dict
      timezone:
        description: Network Update's timezone.
        type: str
    type: dict
  siteId:
    description: SiteId path parameter. Site id to update the network settings which
      is associated with the site.
    type: str
requirements:
- dnacentersdk
seealso:
# Reference by Internet resource
- name: Network Update reference
  description: Complete reference of the Network Update object model.
  link: https://dnacentersdk.readthedocs.io/en/latest/api/api.html#v3-0-0-summary
"""

EXAMPLES = r"""
- name: Update by id
  cisco.dnac.network_update:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    settings:
      clientAndEndpoint_aaa:
        additionalIp:
        - string
        ipAddress: string
        network: string
        protocol: string
        servers: string
        sharedSecret: string
      dhcpServer:
      - string
      dnsServer:
        domainName: string
        primaryIpAddress: string
        secondaryIpAddress: string
      messageOfTheday:
        bannerMessage: string
        retainExistingBanner: true
      netflowcollector:
        ipAddress: string
        port: 0
      network_aaa:
        additionalIp:
        - string
        ipAddress: string
        network: string
        protocol: string
        servers: string
        sharedSecret: string
      ntpServer:
      - string
      snmpServer:
        configureDnacIP: true
        ipAddresses:
        - string
      syslogServer:
        configureDnacIP: true
        ipAddresses:
        - string
      timezone: string
    siteId: string

- name: Create
  cisco.dnac.network_update:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    settings:
      clientAndEndpoint_aaa:
        additionalIp:
        - string
        ipAddress: string
        network: string
        protocol: string
        servers: string
        sharedSecret: string
      dhcpServer:
      - string
      dnsServer:
        domainName: string
        primaryIpAddress: string
        secondaryIpAddress: string
      messageOfTheday:
        bannerMessage: string
        retainExistingBanner: true
      netflowcollector:
        ipAddress: string
        port: 0
      network_aaa:
        additionalIp:
        - string
        ipAddress: string
        network: string
        protocol: string
        servers: string
        sharedSecret: string
      ntpServer:
      - string
      snmpServer:
        configureDnacIP: true
        ipAddresses:
        - string
      syslogServer:
        configureDnacIP: true
        ipAddresses:
        - string
      timezone: string
    siteId: string

"""

RETURN = r"""
dnac_response:
  description: A dictionary or list with the response returned by the Cisco DNAC Python SDK
  returned: always
  type: dict
  sample: >
    {
      "executionId": "string",
      "executionStatusUrl": "string",
      "message": "string"
    }
"""
