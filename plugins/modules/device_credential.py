#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: device_credential
short_description: Resource module for Device Credential
description:
  - Manage operations create, update and delete of the resource Device Credential.
  - API to create device credentials.
  - Delete device credential.
  - API to update device credentials.
version_added: '3.1.0'
extends_documentation_fragment:
  - cisco.dnac.module
author: Rafael Campos (@racampos)
options:
  id:
    description: Id path parameter. Global credential id.
    type: str
  settings:
    description: Device Credential's settings.
    suboptions:
      clientAndEndpoint_aaa:
        description: Device Credential's clientAndEndpoint_aaa.
        suboptions:
          ipAddress:
            description: IP address for ISE serve (eg 1.1.1.4).
            type: str
          network:
            description: IP address for AAA or ISE server (eg 2.2.2.1).
            type: str
          protocol:
            description: Protocol for AAA or ISE serve (eg RADIUS).
            type: str
          servers:
            description: Server type AAA or ISE server (eg AAA).
            type: str
          sharedSecret:
            description: Shared secret for ISE server.
            type: str
        type: dict
      dhcpServer:
        description: DHCP Server IP (eg 1.1.1.1).
        elements: str
        type: list
      dnsServer:
        description: Device Credential's dnsServer.
        suboptions:
          domainName:
            description: Domain Name of DHCP (eg; cisco).
            type: str
          primaryIpAddress:
            description: Primary IP Address for DHCP (eg 2.2.2.2).
            type: str
          secondaryIpAddress:
            description: Secondary IP Address for DHCP (eg 3.3.3.3).
            type: str
        type: dict
      messageOfTheday:
        description: Device Credential's messageOfTheday.
        suboptions:
          bannerMessage:
            description: Massage for Banner message (eg; Good day).
            type: str
          retainExistingBanner:
            description: Retain existing Banner Message (eg "true" or "false").
            type: str
        type: dict
      netflowcollector:
        description: Device Credential's netflowcollector.
        suboptions:
          ipAddress:
            description: IP Address for NetFlow collector (eg 3.3.3.1).
            type: str
          port:
            description: Port for NetFlow Collector (eg; 443).
            type: float
        type: dict
      network_aaa:
        description: Device Credential's network_aaa.
        suboptions:
          ipAddress:
            description: IP address for AAA and ISE server (eg 1.1.1.1).
            type: str
          network:
            description: IP Address for AAA or ISE server (eg 2.2.2.2).
            type: str
          protocol:
            description: Protocol for AAA or ISE serve (eg RADIUS).
            type: str
          servers:
            description: Server type for AAA Network (eg AAA).
            type: str
          sharedSecret:
            description: Shared secret for ISE Server.
            type: str
        type: dict
      ntpServer:
        description: IP address for NTP server (eg 1.1.1.2).
        elements: str
        type: list
      snmpServer:
        description: Device Credential's snmpServer.
        suboptions:
          configureDnacIP:
            description: Configuration DNAC IP for SNMP Server (eg true).
            type: bool
          ipAddresses:
            description: IP Address for SNMP Server (eg 4.4.4.1).
            elements: str
            type: list
        type: dict
      syslogServer:
        description: Device Credential's syslogServer.
        suboptions:
          configureDnacIP:
            description: Configuration DNAC IP for syslog server (eg true).
            type: bool
          ipAddresses:
            description: IP Address for syslog server (eg 4.4.4.4).
            elements: str
            type: list
        type: dict
      timezone:
        description: Input for time zone (eg Africa/Abidjan).
        type: str
    type: dict
requirements:
  - dnacentersdk >= 2.11.0
  - python >= 3.12
seealso:
  - name: Cisco DNA Center documentation for Network Settings CreateDeviceCredentials
    description: Complete reference of the CreateDeviceCredentials API.
    link: https://developer.cisco.com/docs/dna-center/#!create-device-credentials
  - name: Cisco DNA Center documentation for Network Settings DeleteDeviceCredential
    description: Complete reference of the DeleteDeviceCredential API.
    link: https://developer.cisco.com/docs/dna-center/#!delete-device-credential
  - name: Cisco DNA Center documentation for Network Settings UpdateDeviceCredentials
    description: Complete reference of the UpdateDeviceCredentials API.
    link: https://developer.cisco.com/docs/dna-center/#!update-device-credentials
notes:
  - SDK Method used are
    network_settings.NetworkSettings.create_device_credentials,
    network_settings.NetworkSettings.delete_device_credential,
    network_settings.NetworkSettings.update_device_credentials,
  - Paths used are
    post /dna/intent/api/v1/device-credential,
    delete /dna/intent/api/v1/device-credential/{id},
    put /dna/intent/api/v1/device-credential,
"""

EXAMPLES = r"""
---
- name: Create
  cisco.dnac.device_credential:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    state: present
    settings:
      clientAndEndpoint_aaa:
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
        retainExistingBanner: string
      netflowcollector:
        ipAddress: string
        port: 0
      network_aaa:
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
- name: Update all
  cisco.dnac.device_credential:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    state: present
    settings:
      cliCredential:
        description: string
        enablePassword: string
        id: string
        password: string
        username: string
      httpsRead:
        id: string
        name: string
        password: string
        port: string
        username: string
      httpsWrite:
        id: string
        name: string
        password: string
        port: string
        username: string
      snmpV2cRead:
        description: string
        id: string
        readCommunity: string
      snmpV2cWrite:
        description: string
        id: string
        writeCommunity: string
      snmpV3:
        authPassword: string
        authType: string
        description: string
        id: string
        privacyPassword: string
        privacyType: string
        snmpMode: string
        username: string
- name: Delete by id
  cisco.dnac.device_credential:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    state: absent
    id: string
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
