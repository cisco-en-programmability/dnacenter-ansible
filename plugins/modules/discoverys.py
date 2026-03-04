#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: discoverys
short_description: Resource module for Discoverys
description:
  - Manage operations create, update and delete of the resource Discoverys. - > This API creates a discovery. The response
    includes a task url that provides access to the task's details. By accessing this URL, users will receive a response containing
    a resultLocation attribute, which provides details of the discovery settings that was created, including the discovery
    id.
  - API to delete discovery by the given discovery id. - > API to edit the discovery details of the given discovery id. Updating
    the discovery details while the discovery is in progress is not allowed.
version_added: '6.46.0'
extends_documentation_fragment:
  - cisco.dnac.module
author: Rafael Campos (@racampos)
options:
  credentials:
    description: Discoverys's credentials.
    suboptions:
      cli:
        description: Discoverys's cli.
        suboptions:
          description:
            description: Description for CLI credential.
            type: str
          globalCredentialIdList:
            description: List of global credential ids.
            elements: str
            type: list
          protocolOrder:
            description: Connection protocol for the device. Default value is SSH.
            type: str
          username:
            description: CLI username to login to the device.
            type: str
        type: dict
      httpRead:
        description: Discoverys's httpRead.
        suboptions:
          description:
            description: Description for HTTP(S) read credentials.
            type: str
          globalCredentialIdList:
            description: List of global credential ids.
            elements: str
            type: list
          port:
            description: Number of the TCP/UDP port that is used for HTTPS traffic. The default is port number 443 (the well-known
              port for HTTPS).
            type: int
          protocol:
            description: Protocol for HTTP credentials.
            type: str
          username:
            description: Name that is used to authenticate the HTTPS connection. Username cannot contain spaces or angle brackets
              (< >).
            type: str
        type: dict
      httpWrite:
        description: Discoverys's httpWrite.
        suboptions:
          description:
            description: Description for HTTP(S) write credentials.
            type: str
          globalCredentialIdList:
            description: List of global credential ids.
            elements: str
            type: list
          port:
            description: Number of the TCP/UDP port that is used for HTTPS traffic. The default is port number 443 (the well-known
              port for HTTPS).
            type: int
          protocol:
            description: Protocol for HTTP credentials.
            type: str
          username:
            description: Name that is used to authenticate the HTTPS connection. Username cannot contain spaces or angle brackets
              (< >).
            type: str
        type: dict
      netconf:
        description: Discoverys's netconf.
        suboptions:
          description:
            description: Description for NETCONF credential.
            type: str
          globalCredentialIdList:
            description: List of global credential ids.
            elements: str
            type: list
          port:
            description: Netconf Port of the device. Recommended port number is 830.
            type: int
        type: dict
      snmp:
        description: Discoverys's snmp.
        suboptions:
          retries:
            description: The number of times to repeat the failed SNMP polling request after a timeout. Max value supported
              is 3. Default is Global SNMP retry (if exists) or 3.
            type: int
          snmpV2Read:
            description: Discoverys's snmpV2Read.
            suboptions:
              description:
                description: Description for SNMP read-only community.
                type: str
              globalCredentialIdList:
                description: List of global credential ids.
                elements: str
                type: list
            type: dict
          snmpV2Write:
            description: Discoverys's snmpV2Write.
            suboptions:
              description:
                description: Description for SNMP read-write community.
                type: str
              globalCredentialIdList:
                description: List of global credential ids.
                elements: str
                type: list
            type: dict
          snmpV3:
            description: Discoverys's snmpV3.
            suboptions:
              authType:
                description: SNMP authentication type. Required if the SNMP security mode is AUTHPRIV or AUTHNOPRIV.
                type: str
              description:
                description: Description for SNMP V3 credential.
                type: str
              globalCredentialIdList:
                description: List of global credential ids.
                elements: str
                type: list
              mode:
                description: Security level that an SNMP message requires.
                type: str
              privacyType:
                description: SNMP privacy type. Required if the SNMP mode is AUTHPRIV.
                type: str
              username:
                description: Username associated with the SNMPv3 settings. The username can only contain letters, numbers
                  and -_.@ characters.
                type: str
            type: dict
          timeout:
            description: The interval (in seconds) after which SNMP failure to respond to the polling request generates a
              timeout. Max value supported is 300. Default is Global SNMP timeout (if exists) or 5.
            type: int
        type: dict
    type: dict
  discoveryTypeDetails:
    description: Discoverys's discoveryTypeDetails.
    suboptions:
      cidrAddress:
        description: Discoverys's cidrAddress.
        suboptions:
          cidrPrefix:
            description: CIDR prefix for the IP address.
            type: str
          cidrSuffix:
            description: The CIDR suffix length indicates the number of bits for host addresses, following the prefix. For
              IPv4, supported lengths range from 20 to 30, where default is 30. For IPv6, they range from 116 to 126, where
              default is 126.
            type: int
        type: dict
      hopCount:
        description: This field defines the CDP level, indicating the number of hops from the seed device to scan. Acceptable
          values range from 1 to 16, with a default of 16. For instance, a CDP level of 3 means scanning will include up to
          three hops from the seed device.
        type: int
      ipAddress:
        description: IPv4 or IPv6 address of the device.
        type: str
      range:
        description: Discoverys's range.
        elements: dict
        suboptions:
          ipAddressEnd:
            description: End IP address of devices to be discovered.
            type: str
          ipAddressStart:
            description: Start IP address of the devices to be discovered.
            type: str
        type: list
      subnetFilter:
        description: Discoverys's subnetFilter.
        suboptions:
          cidrAddress:
            description: Discoverys's cidrAddress.
            suboptions:
              cidrPrefix:
                description: CIDR prefix for the IP address.
                type: str
              cidrSuffix:
                description: The CIDR suffix length indicates the number of bits for host addresses, following the prefix.
                  For IPv4, supported lengths range from 20 to 30, where default is 30. For IPv6, they range from 116 to 126,
                  where default is 126.
                type: int
            type: dict
          ipAddress:
            description: IPv4 or IPv6 address of the device.
            type: str
        type: dict
      type:
        description: Type of the discovery.
        type: str
    type: dict
  id:
    description: Id path parameter. The id of the discovery.
    type: str
  managementIpSelectionMethod:
    description: When Catalyst Center discovers a device, it uses one of the device's IP addresses as the preferred management
      IP address for the device. The IP address can be that of a built-in management interface of the device, another physical
      interface, or a logical interface like Loopback0. You can configure Catalyst Center to log the device's loopback IP
      address as the preferred management IP address, provided the IP address is reachable from Catalyst Center.
    type: str
  name:
    description: The name of the discovery job being created. This will be a unique name.
    type: str
  onlyNewDevice:
    description: This flag indicates to discover only new devices that are not in inventory. If set to true, only devices
      that are not in the inventory will be discovered. If set to false, devices that already exist in the inventory will
      not be listed in the discovered devices list.
    type: bool
  updateManagementIp:
    description: This flag indicates if the management IP address of existing devices to be updated as part of this discovery.
      If set false devices get discovered with the existing management IP address. If set true it overwrites the management
      IP address with the new IP address used in discovery.
    type: bool
requirements:
  - dnacentersdk >= 2.11.0
  - python >= 3.12
seealso:
  - name: Cisco DNA Center documentation for Devices CreatesDiscovery
    description: Complete reference of the CreatesDiscovery API.
    link: https://developer.cisco.com/docs/dna-center/#!creates-discovery
  - name: Cisco DNA Center documentation for Devices DeletesDiscoveryById
    description: Complete reference of the DeletesDiscoveryById API.
    link: https://developer.cisco.com/docs/dna-center/#!deletes-discovery-by-id
  - name: Cisco DNA Center documentation for Devices EditsDiscovery
    description: Complete reference of the EditsDiscovery API.
    link: https://developer.cisco.com/docs/dna-center/#!edits-discovery
notes:
  - SDK Method used are
    devices.Devices.creates_discovery,
    devices.Devices.deletes_discovery_by_id,
    devices.Devices.edits_discovery,
  - Paths used are
    post /dna/intent/api/v1/discoverys,
    delete /dna/intent/api/v1/discoverys/{id},
    put /dna/intent/api/v1/discoverys/{id},
"""

EXAMPLES = r"""
---
- name: Create
  cisco.dnac.discoverys:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    state: present
    credentials:
      cli:
        description: string
        globalCredentialIdList:
          - string
        protocolOrder: string
        username: string
      httpRead:
        description: string
        globalCredentialIdList:
          - string
        port: 0
        protocol: string
        username: string
      httpWrite:
        description: string
        globalCredentialIdList:
          - string
        port: 0
        protocol: string
        username: string
      netconf:
        description: string
        globalCredentialIdList:
          - string
        port: 0
      snmp:
        retries: 0
        snmpV2Read:
          description: string
          globalCredentialIdList:
            - string
        snmpV2Write:
          description: string
          globalCredentialIdList:
            - string
        snmpV3:
          authType: string
          description: string
          globalCredentialIdList:
            - string
          mode: string
          privacyType: string
          username: string
        timeout: 0
    discoveryTypeDetails:
      cidrAddress:
        cidrPrefix: string
        cidrSuffix: 0
      hopCount: 0
      ipAddress: string
      range:
        - ipAddressEnd: string
          ipAddressStart: string
      subnetFilter:
        cidrAddress:
          cidrPrefix: string
          cidrSuffix: 0
        ipAddress: string
      type: string
    managementIpSelectionMethod: string
    name: string
    onlyNewDevice: true
    updateManagementIp: true
- name: Delete by id
  cisco.dnac.discoverys:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    state: absent
    id: string
- name: Update by id
  cisco.dnac.discoverys:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    state: present
    credentials:
      cli:
        description: string
        globalCredentialIdList:
          - string
        protocolOrder: string
        username: string
      httpRead:
        description: string
        globalCredentialIdList:
          - string
        port: 0
        protocol: string
        username: string
      httpWrite:
        description: string
        globalCredentialIdList:
          - string
        port: 0
        protocol: string
        username: string
      netconf:
        description: string
        globalCredentialIdList:
          - string
        port: 0
      snmp:
        retries: 0
        snmpV2Read:
          description: string
          globalCredentialIdList:
            - string
        snmpV2Write:
          description: string
          globalCredentialIdList:
            - string
        snmpV3:
          authType: string
          description: string
          globalCredentialIdList:
            - string
          mode: string
          privacyType: string
          username: string
        timeout: 0
    discoveryTypeDetails:
      cidrAddress:
        cidrPrefix: string
        cidrSuffix: 0
      hopCount: 0
      ipAddress: string
      range:
        - ipAddressEnd: string
          ipAddressStart: string
      subnetFilter:
        cidrAddress:
          cidrPrefix: string
          cidrSuffix: 0
        ipAddress: string
      type: string
    id: string
    managementIpSelectionMethod: string
    onlyNewDevice: true
    updateManagementIp: true
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
