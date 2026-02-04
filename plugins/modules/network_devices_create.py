#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: network_devices_create
short_description: Resource module for Network Devices Create
description:
  - Manage operation create of the resource Network Devices Create. - > Adds the network device to inventory. The API supports
    Network Device, Meraki Dashboard, Compute Device, Firewall Management Center FMC and Third-Party Device. Access points
    associated with added WLC will be automatically added to inventory. For Meraki Dashboard, use the dashboard URL as the
    management address.
version_added: '6.46.0'
extends_documentation_fragment:
  - cisco.dnac.module
author: Rafael Campos (@racampos)
options:
  category:
    description: Category of the device. Used to determine the type of the device being added.
    type: str
  credentials:
    description: Network Devices Create's credentials.
    suboptions:
      cli:
        description: Network Devices Create's cli.
        suboptions:
          enablePassword:
            description: Password that is used to move to a higher privilege level in the CLI. Configure this password only
              if your network devices require it. Passwords cannot contain spaces or angle brackets(<>).
            type: str
          password:
            description: CLI Password. Passwords cannot contain spaces or angle brackets(<>).
            type: str
          protocol:
            description: Protocol used for CLI access. Default is SSH.
            type: str
          username:
            description: CLI username to login to the device.
            type: str
        type: dict
      http:
        description: Network Devices Create's http.
        suboptions:
          password:
            description: HTTP password. The password cannot contain spaces or angle brackets (< >). Note that some Cisco IOS
              XE devices do not allow a question mark (?).
            type: str
          port:
            description: HTTP port. The default port is 443 for protocol= HTTPS and 80 for protocol=HTTP.
            type: int
          protocol:
            description: HTTP protocol. Compute device require HTTPS.
            type: str
          username:
            description: HTTP username. Username cannot contain spaces or angle brackets (< >).
            type: str
        type: dict
      meraki:
        description: Network Devices Create's meraki.
        suboptions:
          apiKey:
            description: Meraki API key.
            type: str
          orgIds:
            description: Meraki organizations for which the devices needs to be imported. Imports devices from all organizations
              if not provided.
            elements: str
            type: list
        type: dict
      netconf:
        description: Network Devices Create's netconf.
        suboptions:
          port:
            description: Netconf port of the device. Default port is 830.
            type: int
        type: dict
      snmp:
        description: Network Devices Create's snmp.
        suboptions:
          authPassword:
            description: SNMPv3 authentication password.
            type: str
          authType:
            description: SNMPv3 authentication type. Required for AUTHPRIV (Authentication and Privacy) and AUTHNOPRIV (Authentication)
              modes. SHA256 The device will be authenticated using SHA256. SHA The device will be authenticated using SHA.
              MD5 The device will be authenticated using MD5.
            type: str
          mode:
            description: Security level that an SNMP message requires. AUTHPRIV provides both authentication and encryption.
              AUTHNOPRIV provides authentication, but does not provide encryption. NOAUTHNOPRIV does not provide authentication
              or encryption.
            type: str
          privacyPassword:
            description: SNMPv3 privacy password.
            type: str
          privacyType:
            description: SNMP privacy type. Required if the SNMP mode is AUTHPRIV. AES128 algorithm used for encryption. AES192
              algorithm used for encryption. AES256 algorithm used for encryption. CISCOAES192 algorithm used for encryption.
              CISCOAES256 algorithm used for encryption.
            type: str
          readCommunity:
            description: Read-only community string password used only to view SNMP information on the device.
            type: str
          username:
            description: Name associated with the SNMPv3 settings.
            type: str
          version:
            description: SNMP version to be used for the device.
            type: str
          writeCommunity:
            description: Write community string used to make changes to the SNMP information on the device.
            type: str
        type: dict
    type: dict
  managementAddress:
    description: Management address of the network device. For meraki dashboard, this is the dashboard URL.
    type: str
requirements:
  - dnacentersdk >= 2.11.0
  - python >= 3.12
seealso:
  - name: Cisco DNA Center documentation for Devices AddsANewNetworkDevice
    description: Complete reference of the AddsANewNetworkDevice API.
    link: https://developer.cisco.com/docs/dna-center/#!adds-a-new-network-device
notes:
  - SDK Method used are
    devices.Devices.adds_a_new_network_device,
  - Paths used are
    post /dna/intent/api/v1/networkDevices,
"""

EXAMPLES = r"""
---
- name: Create
  cisco.dnac.network_devices_create:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    category: string
    credentials:
      cli:
        enablePassword: string
        password: string
        protocol: string
        username: string
      http:
        password: string
        port: 0
        protocol: string
        username: string
      meraki:
        apiKey: string
        orgIds:
          - string
      netconf:
        port: 0
      snmp:
        authPassword: string
        authType: string
        mode: string
        privacyPassword: string
        privacyType: string
        readCommunity: string
        username: string
        version: string
        writeCommunity: string
    managementAddress: string
"""
RETURN = r"""
dnac_response:
  description: A dictionary or list with the response returned by the Cisco DNAC Python SDK
  returned: always
  type: dict
  sample: >
    {
      "response": {
        "taskId": "string",
        "url": "string"
      },
      "version": "string"
    }
"""
