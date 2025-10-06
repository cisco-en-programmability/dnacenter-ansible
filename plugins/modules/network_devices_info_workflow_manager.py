# !/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright (c) 2025, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import absolute_import, division, print_function

__metaclass__ = type
__author__ = ("Karthick S N", "Madhan Sankaranarayanan")

DOCUMENTATION = r"""
---
module: network_devices_info_workflow_manager
short_description: Gather facts about network devices from Cisco Catalyst Center (facts/info module) using flexible filters.

description:
  - Gathers detailed facts (information) about network devices managed by Cisco Catalyst Center using flexible user-defined filters.
  - Supports filtering by management IP, MAC address, hostname, serial number, software type,
    software version, role, device type, family, and site hierarchy.
  - Allows selection of specific device information types, such as device details, interfaces,
    VLANs, line cards, supervisor cards, POE, module count, connected devices, configuration,
    summary, polling interval, stack, and link mismatch details.
  - Handles query retries, timeouts, and polling intervals for robust data collection.
  - Supports output to a file using the C(output_file_info) option. Output can be JSON or YAML,
    with user-defined file path, file mode (overwrite or append), and optional timestamp.
  - If C(output_file_info) is provided, results are written to the file; otherwise, results are
    returned in the Ansible output.
  - Returns structured results for each requested information type, or an empty list if
    no devices match the filters after all retries.
  - This module is tagged as a facts/info module and is safe to use in check mode.

version_added: "6.31.0"
extends_documentation_fragment:
  - cisco.dnac.workflow_manager_params
author:
  - Karthick S N (@karthick-s-n)
  - Madhan Sankaranarayanan (@madhansansel)

options:
  config_verify:
    description: Set to True to verify the Cisco Catalyst Center after applying the playbook config.
    type: bool
    default: False
  state:
    description: The desired state of the configuration after module execution.
    type: str
    choices: ["queried"]
    default: queried
  config:
    description:
      - List of dictionaries specifying network device query parameters.
      - Each dictionary must contain a C(network_devices) list with at least one unique identifier
        (such as management IP, MAC address, hostname, or serial number) per device.
    type: list
    elements: dict
    required: true
    suboptions:
      network_devices:
        description:
            - Contains filters to retrieve network devices.
            - Requires at least one unique identifier such as management IP, MAC address, hostname, or serial number per device.
        type: list
        elements: dict
        suboptions:
            management_ip_address:
                description:
                    - List of management IP addresses to identify devices.
                    - Each IP address must be unique.
                type: list
                elements: str
            mac_address:
                description:
                    - List of MAC addresses to identify devices.
                    - Each MAC address must be unique.
                type: list
                elements: str
            hostname:
                description:
                    - List of hostnames to identify devices.
                    - Each hostname must be unique.
                type: list
                elements: str
            serial_number:
                description:
                    - List of serial numbers to identify devices.
                    - Each serial number must be unique.
                type: list
                elements: str
            os_type:
                description:
                    - List of software types to filter devices.
                type: list
                elements: str
                choices:
                  - IOS-XE
                  - IOS
                  - IOS-XR
                  - NX-OS
                  - ASA
                  - FTD
                  - IOS-XE SD-WAN # Additional options may be found in the API documentation.
            software_version:
                description:
                    - List of software versions to filter devices(e.g., 17.12.4).
                type: list
                elements: str
            role:
                description:
                    - List of device roles to filter devices.
                type: list
                elements: str
                choices:
                  - ACCESS
                  - DISTRIBUTION
                  - CORE
                  - WAN
                  - WLC
                  - DATA_CENTER # Additional options may be found in the API documentation.
            device_type:
                description:
                    - List of device types to filter devices (For example, Cisco Catalyst 9300 Switch).
                type: list
                elements: str
                choices:
                  - Cisco Catalyst 9300 Switch
                  - Cisco Catalyst 9400 Switch
                  - Cisco Catalyst 9500 Switch
                  - Cisco Catalyst C9500-48Y4C Switch
                  - Cisco 3800E Unified Access Point
                  - Cisco Catalyst 9130AXI Unified Access Point
                  - Cisco Catalyst 9800-L-C Wireless Controller
                  - Cisco Catalyst 9115AXI Unified Access Point
                  - Cisco Catalyst Wireless 9164I Unified Access Point
                  - Cisco Wireless 9176D1 Access Point # Additional options may be found in the API documentation.
            family:
                description:
                    - List of device families to filter devices.
                type: list
                elements: str
                choices:
                  - Switches and Hubs
                  - Routers
                  - Wireless Controller
                  - Unified AP
                  - Sensors # Additional options may be found in the API documentation.
            site_hierarchy:
                description:
                    - List of site hierarchies to filter devices by site.
                type: list
                elements: str
            timeout:
                description:
                    - Time in seconds to wait for devices to be found.
                    - Default is 60 seconds.
                type: int
                default: 60
            retries:
                description:
                    - Number of times to retry the query if the devices are not found.
                    - Default value is 3 retries.
                type: int
                default: 3
            interval:
                description:
                    - Time in seconds to wait between retries.
                    - Default is 10 seconds.
                type: int
                default: 10
            requested_info:
                description:
                    - List of device information types to retrieve.
                    - If set to ['all'], it retrieves all available information.
                    - If specific info types are listed, only those will be retrieved.
                    - If this parameter is omitted or empty, all information will be retrieved by default.
                type: list
                elements: str
                default: ['all']
                choices:
                    - all # Retrieves all available information of all choices below
                    - device_interfaces_by_range_info #Retrieves interface details by specified range
                    - device_info #Retrieves basic device details of hostname, model, serial number, OS version
                    - interface_info #Retrieves interface details such as status, speed, duplex, and MAC address
                    - interface_vlan_info #Retrieves VLAN information for each interface
                    - line_card_info #Retrieves line card details for modular devices
                    - supervisor_card_info #Retrieves supervisor card details for modular devices
                    - poe_info #Retrieves Power over Ethernet (PoE) information for interfaces
                    - module_count_info #Retrieves the count of installed modules
                    - connected_device_info #Retrieves information about devices connected to the specified device
                    - device_config_info #Retrieves the running configuration of the specified device
                    - device_summary_info #Retrieves a summary of the specified device's information
                    - device_polling_interval_info #Retrieves the polling interval configuration for the specified device
                    - device_stack_info #Retrieves stack information for stackable devices
                    - device_link_mismatch_info #Retrieves details of link mismatches speed/duplex/VLAN issues
            output_file_info:
              description:
                - Controls output file generation for device information.
                - If provided, results are saved to the specified file; otherwise, results are
                  returned in the Ansible output.
                - Use to define file path, format, mode, and timestamp handling.
              type: dict
              suboptions:
                file_path:
                  description:
                    - Absolute path to the output file, without extension.
                    - File extension (.json or .yaml) is added automatically based on C(file_format).
                  type: str
                  required: true
                file_format:
                  description:
                    - Format of the output file.
                    - Supported formats are json and yaml.
                    - Default is yaml if not specified.
                  type: str
                  choices:
                    - json
                    - yaml
                  default: yaml
                file_mode:
                  description:
                    - Writing mode for the output file.
                    - Use 'w' to overwrite or 'a' to append to the existing file content.
                  type: str
                  default: w
                  choices:
                    - w
                    - a
                timestamp:
                  description:
                    - Indicates whether to include a timestamp within the output content.
                    - If set to true, the download time will be added as the first entry in the output.
                  type: bool
                  default: false
requirements:
    - dnacentersdk >= 2.9.3
    - python >= 3.9.19
notes:
    - This is a facts/info module, it only retrieves information and does not modify any device or configuration.
    - Writing to a local file is for reporting/archival purposes only and does not affect the state of any managed device.
    - Safe to use in check mode.
    - SDK Methods used are
        - devices.Devices.get_device_list
        - devices.Devices.get_device_interface_vlans
        - devices.Devices.get_device_interfaces_by_specified_range
        - devices.Devices.get_linecard_details
        - devices.Devices.inventory_insight_device_link_mismatch
        - devices.Devices.get_stack_details_for_device
        - devices.Devices.get_device_config_by_id
        - devices.Devices.get_polling_interval_by_id
        - devices.Devices.get_supervisor_card_detail
        - devices.Devices.poe_details
        - devices.Devices.get_connected_device_detail
        - devices.Devices.get_interface_info_by_id
        - devices.Devices.get_module_count
        - devices.Devices.get_network_device_by_ip
        - devices.Devices.get_device_summary

    - Paths used are
        - GET/dna/intent/api/v1/network-device
        - GET/dna/intent/api/v1/network-device/{id}/vlan
        - GET/dna/intent/api/v1/interface/network-device/{deviceId}/{startIndex}/{recordsToReturn}
        - GET/dna/intent/api/v1/network-device/{deviceUuid}/line-card
        - GET/dna/intent/api/v1/network-device/insight/{siteId}/device-link
        - GET/dna/intent/api/v1/network-device/{deviceId}/stack
        - GET/dna/intent/api/v1/network-device/{networkDeviceId}/config
        - GET/dna/intent/api/v1/network-device/{id}/collection-schedule
        - GET/dna/intent/api/v1/network-device/{id}/brief
        - GET/dna/intent/api/v1/network-device/{deviceUuid}/supervisor-card
        - GET/dna/intent/api/v1/network-device/{deviceUuid}/poe
        - GET/dna/intent/api/v1/network-device/{deviceUuid}/interface/{interfaceUuid}/neighbor
        - GET/dna/intent/api/v1/interface/network-device/{deviceId}
        - GET/dna/intent/api/v1/network-device/module/count
        - GET/dna/intent/api/v1/network-device/ip-address/{ipAddress}
"""

EXAMPLES = r"""
# 1 Example Playbook to gather specific network device information from Cisco Catalyst Center
---
- name: Get Specific Network devices information on Cisco Catalyst Center
  hosts: localhost
  connection: local
  vars_files:
    - "credentials.yml"
  tasks:
    - name: Gather detailed facts for specific network devices
      cisco.dnac.network_devices_info_workflow_manager:
        dnac_host: "{{ dnac_host }}"
        dnac_username: "{{ dnac_username }}"
        dnac_password: "{{ dnac_password }}"
        dnac_verify: "{{ dnac_verify }}"
        dnac_port: "{{ dnac_port }}"
        dnac_version: "{{ dnac_version }}"
        dnac_debug: "{{ dnac_debug }}"
        dnac_log: true
        dnac_log_level: DEBUG
        config_verify: false
        dnac_api_task_timeout: 1000
        dnac_task_poll_interval: 1
        state: queried
        config:
          - network_devices:
              - management_ip_address: ["204.1.1.26"]
                mac_address: ["d4:ad:bd:c1:67:00"]
                hostname: ["DC-FR-9300"]
                serial_number: ["FJC2327U0S2"]
                os_type: ["IOS-XE"]
                software_version: ["17.12.4"]
                role: ["ACCESS"]
                device_type: ["Cisco Catalyst 9300 Switch"]
                family: ["Switches and Hubs"]
                site_hierarchy: [Global/USA]
                timeout: 60
                retries: 3
                interval: 10
                requested_info:
                  - device_info
                  - interface_info
                  - interface_vlan_info
                  - line_card_info
                  - supervisor_card_info
                  - poe_info
                  - module_count_info
                  - connected_device_info
                  - device_interfaces_by_range_info
                  - device_config_info
                  - device_summary_info
                  - device_polling_interval_info
                  - device_stack_info
                  - device_link_mismatch_info
                output_file_info:
                  file_path: /Users/karthick/Downloads/info
                  file_format: json
                  file_mode: w
                  timestamp: true

# 2 Example Playbook to gather all network device information from Cisco Catalyst Center
- name: Get All Network devices information on Cisco Catalyst Center
  hosts: localhost
  connection: local
  vars_files:
    - "credentials.yml"
  tasks:
    - name: Gather detailed facts for all network devices
      cisco.dnac.network_devices_info_workflow_manager:
        dnac_host: "{{ dnac_host }}"
        dnac_username: "{{ dnac_username }}"
        dnac_password: "{{ dnac_password }}"
        dnac_verify: "{{ dnac_verify }}"
        dnac_port: "{{ dnac_port }}"
        dnac_version: "{{ dnac_version }}"
        dnac_debug: "{{ dnac_debug }}"
        dnac_log: true
        dnac_log_level: DEBUG
        config_verify: false
        dnac_api_task_timeout: 1000
        dnac_task_poll_interval: 1
        state: queried
        config:
          - network_devices:
              - management_ip_address: ["204.1.1.26"]
                mac_address: ["d4:ad:bd:c1:67:00"]
                hostname: ["DC-FR-9300"]
                serial_number: ["FJC2327U0S2"]
                os_type: ["IOS-XE"]
                software_version: ["17.12.4"]
                role: ["ACCESS"]
                device_type: ["Cisco Catalyst 9300 Switch"]
                family: ["Switches and Hubs"]
                site_hierarchy: [Global/USA]
                timeout: 60
                retries: 3
                interval: 10
                requested_info:
                  - all
                output_file_info:
                  file_path: /Users/karthick/Downloads/info
                  file_format: json
                  file_mode: w
                  timestamp: true
"""

RETURN = r"""

#Case 1: Successful Retrieval of Device Info
response_device_info:
    description:
      - Device information for network devices, including family, type, software version, serial number, and more.
      - Returned for each device matching the query.
    returned: always
    type: dict
    sample: {
    "response": [{
        "family": "Switches and Hubs",
        "type": "Cisco Catalyst 9300 Switch",
        "lastUpdateTime": 1750896739913,
        "macAddress": "0c:75:bd:42:db:80",
        "deviceSupportLevel": "Supported",
        "softwareType": "IOS-XE",
        "softwareVersion": "17.2.1",
        "serialNumber": "FJC2335S09F",
        "inventoryStatusDetail": "<status><general code=\"SUCCESS\"/></status>",
        "collectionInterval": "Global Default",
        "dnsResolvedManagementAddress": "204.1.2.3",
        "lastManagedResyncReasons": "Periodic",
        "managementState": "Managed",
        "pendingSyncRequestsCount": "0",
        "reasonsForDeviceResync": "Periodic",
        "reasonsForPendingSyncRequests": "",
        "syncRequestedByApp": "",
        "upTime": "63 days, 19:36:43.08",
        "roleSource": "MANUAL",
        "lastUpdated": "2025-06-26 00:12:19",
        "interfaceCount": "0",
        "apManagerInterfaceIp": "",
        "bootDateTime": "2025-04-23 04:36:19",
        "collectionStatus": "Managed",
        "hostname": "test123",
        "locationName": null,
        "managementIpAddress": "204.1.2.3",
        "platformId": "C9300-48UXM",
        "reachabilityFailureReason": "",
        "reachabilityStatus": "Reachable",
        "series": "Cisco Catalyst 9300 Series Switches",
        "snmpContact": "",
        "snmpLocation": "",
        "associatedWlcIp": "",
        "apEthernetMacAddress": null,
        "errorCode": null,
        "errorDescription": null,
        "lastDeviceResyncStartTime": "2025-06-26 00:11:45",
        "lineCardCount": "0",
        "lineCardId": "",
        "managedAtleastOnce": false,
        "memorySize": "NA",
        "tagCount": "0",
        "tunnelUdpPort": null,
        "uptimeSeconds": 5528803,
        "vendor": "Cisco",
        "waasDeviceMode": null,
        "description": "Cisco IOS Software [Amsterdam], Catalyst L3 Switch Software (CAT9K_IOSXE),
          Version 17.2.1, RELEASE SOFTWARE (fc4) Technical Support: http://www.cisco.com/techsupport
          Copyright (c) 1986-2020 by Cisco Systems, Inc. Compiled Thu 26-Mar-20 03:29 by mcpre netconf enabled",
        "location": null,
        "role": "ACCESS",
        "instanceUuid": "e62e6405-13e4-4f1b-ae1c-580a28a96a88",
        "instanceTenantId": "66e48af26fe687300375675e",
        "id": "e62e6405-13e4-4f1b-ae1c-580a28a96a88"
    }],
    "version": "string"
    }

#Case 2: Successful Retrieval of Device Interface VLAN info
response_device_interface_vlan_info:
  description: Details of the response containing VLAN information for device interfaces.
  returned: always
  type: dict
  sample: {
    "response": [
      {
        "interfaceName": "GigabitEthernet0/1",
        "ipAddress": "192.168.10.25",
        "mask": 24,
        "networkAddress": "192.168.10.0",
        "numberOfIPs": 254,
        "prefix": "192.168.10.0/24",
        "vlanNumber": 10,
        "vlanType": "Data"
      }
    ],
    "version": "string"
  }

#Case 3: Successful Retrieval of Device Interfaces by Specified Range
response_device_interfaces_range:
  description: Details of the response containing device interface information retrieved by a specified range.
  returned: always
  type: dict
  sample: {
    "response": [
      {
        "addresses": [],
        "adminStatus": "UP",
        "className": null,
        "deviceId": "e62e6405-13e4-4f1b-ae1c-580a28a96a88",
        "duplex": "FullDuplex",
        "ifIndex": "73",
        "interfaceType": "Physical",
        "ipv4Address": null,
        "ipv4Mask": null,
        "isisSupport": "false",
        "lastIncomingPacketTime": null,
        "lastOutgoingPacketTime": 1750896368000,
        "lastUpdated": null,
        "macAddress": "0c:75:bd:42:db:c1",
        "mappedPhysicalInterfaceId": null,
        "mappedPhysicalInterfaceName": null,
        "mediaType": null,
        "mtu": "9100",
        "nativeVlanId": "1",
        "ospfSupport": "false",
        "pid": "C9300-48UXM",
        "portMode": "access",
        "portName": "AppGigabitEthernet1/0/1",
        "portType": "Ethernet Port",
        "serialNo": "FJC2335S09F",
        "series": "Cisco Catalyst 9300 Series Switches",
        "speed": "1000000",
        "status": "up",
        "vlanId": "1",
        "voiceVlan": "",
        "description": "",
        "name": null,
        "instanceUuid": "c9c638b6-4627-4a2e-be25-05f6e487bfcf",
        "instanceTenantId": "66e48af26fe687300375675e",
        "id": "c9c638b6-4627-4a2e-be25-05f6e487bfcf"
      }
    ],
    "version": "string"
  }

#Case 4: Successful Retrieval of Linecard Details
response_linecard_details:
  description: Details of the response containing linecard information for the device.
  returned: always
  type: dict
  sample: {
    "response": [
      {
        "serialno": "SN123456789",
        "partno": "PN987654321",
        "switchno": "SW-001-A1",
        "slotno": "Slot-04"
      }
    ],
    "version": "string"
  }

#Case 5: Successful Retrieval of Inventory Insight Device Link Mismatch API
response_inventory_insight_link_mismatch:
  description: Details of the response containing device link mismatch information from Inventory Insight API.
  returned: always
  type: dict
  sample: {
    "response": [
      {
        "endPortAllowedVlanIds": "10,20,30",
        "endPortNativeVlanId": "10",
        "startPortAllowedVlanIds": "10,20,30",
        "startPortNativeVlanId": "10",
        "linkStatus": "up",
        "endDeviceHostName": "switch-nyc-01",
        "endDeviceId": "device-1001",
        "endDeviceIpAddress": "192.168.1.10",
        "endPortAddress": "GigabitEthernet1/0/24",
        "endPortDuplex": "full",
        "endPortId": "endport-1001",
        "endPortMask": "255.255.255.0",
        "endPortName": "Gi1/0/24",
        "endPortPepId": "pep-ep-1001",
        "endPortSpeed": "1000Mbps",
        "startDeviceHostName": "router-dc-01",
        "startDeviceId": "device-2001",
        "startDeviceIpAddress": "192.168.1.1",
        "startPortAddress": "GigabitEthernet0/1",
        "startPortDuplex": "full",
        "startPortId": "startport-2001",
        "startPortMask": "255.255.255.0",
        "startPortName": "Gi0/1",
        "startPortPepId": "pep-sp-2001",
        "startPortSpeed": "1000Mbps",
        "lastUpdated": "2025-06-26T10:15:00Z",
        "numUpdates": 15,
        "avgUpdateFrequency": 4.0,
        "type": "ethernet-link",
        "instanceUuid": "123e4567-e89b-12d3-a456-426614174000",
        "instanceTenantId": "tenant-xyz123"
      }
    ],
    "version": "string"
  }

#Case 6: Successful Retrieval of Stack Details for Device
response_stack_details:
  description: Details of the response containing stack information for the device.
  returned: always
  type: dict
  sample: {
    "response": {
        "device_stack_info": [
        {
            "deviceId": "e62e6405-13e4-4f1b-ae1c-580a28a96a88",
            "stackSwitchInfo": [
                {
                    "hwPriority": 0,
                    "macAddress": "0c:75:bd:42:db:80",
                    "numNextReload": 1,
                    "role": "ACTIVE",
                    "softwareImage": "17.02.01",
                    "stackMemberNumber": 1,
                    "state": "READY",
                    "switchPriority": 1,
                    "entPhysicalIndex": "1000",
                    "serialNumber": "FJC2335S09F",
                    "platformId": "C9300-48UXM"
                }
            ],
            "stackPortInfo": [
                {
                    "isSynchOk": "Yes",
                    "name": "StackSub-St1-1",
                    "switchPort": "1/1",
                    "neighborPort": "NONE",
                    "nrLinkOkChanges": 0,
                    "stackCableLengthInfo": "NO_CABLE",
                    "stackPortOperStatusInfo": "DOWN",
                    "linkActive": false,
                    "linkOk": false
                },
                {
                    "isSynchOk": "Yes",
                    "name": "StackSub-St1-2",
                    "switchPort": "1/2",
                    "neighborPort": "NONE",
                    "nrLinkOkChanges": 0,
                    "stackCableLengthInfo": "NO_CABLE",
                    "stackPortOperStatusInfo": "DOWN",
                    "linkActive": false,
                    "linkOk": false
                }
            ],
            "svlSwitchInfo": null
        }
    ]
        },
    "version": "string"
  }

#Case 7: Successful Retrieval of Device Config
response_device_config:
  description: Details of the response containing the device configuration as a string.
  returned: always
  type: dict
  sample: {
    "response": "Building Configuration Operation Successful",
    "version": "string"
  }

#Case 8: Successful Retrieval of Polling Interval
response_polling_interval:
  description: Details of the response containing the polling interval value.
  returned: always
  type: dict
  sample: {
    "device_polling_interval_info": [
                86400
            ],
    "version": "string"
  }

#Case 9: Successful Retrieval of Device Summary
response_device_summary:
  description: Details of the response containing a summary of the device.
  returned: always
  type: dict
  sample: {
    "response": {
        "id": "e62e6405-13e4-4f1b-ae1c-580a28a96a88",
        "role": "ACCESS",
        "roleSource": "MANUAL"
    },
    "version": "string"
  }

#Case 10: Successful Retrieval of Supervisor Card Detail
response_supervisor_card_detail:
  description: Details of the response containing supervisor card information for the device.
  returned: always
  type: dict
  sample: {
    "response": [
      {
        "serialno": "SN1234567890",
        "partno": "PN9876543210",
        "switchno": "SW-01",
        "slotno": "3"
      }
    ],
    "version": "string"
  }

#Case 11: Successful Retrieval of POE Details
response_poe_details:
  description: Details of the response containing Power over Ethernet (POE) statistics.
  returned: always
  type: dict
  sample: {
    "response": {
        "powerAllocated": "525",
        "powerConsumed": "0",
        "powerRemaining": "525"
    },
    "version": "string"
  }

#Case 12: Successful Retrieval of Connected Device Detail
response_connected_device_detail:
  description: Details of the response containing information about a connected neighbor device.
  returned: always
  type: dict
  sample: {
    "response": {
        "neighborDevice": "DC-T-9300",
        "neighborPort": "TenGigabitEthernet1/1/8",
        "capabilities": [
            "IGMP_CONDITIONAL_FILTERING",
            "ROUTER",
            "SWITCH"
        ]
    },
    "version": "string"
  }

#Case 13: Successful Retrieval of Interface Info
response_interface_info:
  description: Details of the response containing interface information for a device.
  returned: always
  type: dict
  sample: {
    "response": [
      {
        "addresses": [],
        "adminStatus": "UP",
        "className": null,
        "deviceId": "e62e6405-13e4-4f1b-ae1c-580a28a96a88",
        "duplex": "FullDuplex",
        "ifIndex": "73",
        "interfaceType": "Physical",
        "ipv4Address": null,
        "ipv4Mask": null,
        "isisSupport": "false",
        "lastIncomingPacketTime": null,
        "lastOutgoingPacketTime": 1750896368000,
        "lastUpdated": null,
        "macAddress": "0c:75:bd:42:db:c1",
        "mappedPhysicalInterfaceId": null,
        "mappedPhysicalInterfaceName": null,
        "mediaType": null,
        "mtu": "9100",
        "nativeVlanId": "1",
        "ospfSupport": "false",
        "pid": "C9300-48UXM",
        "portMode": "access",
        "portName": "AppGigabitEthernet1/0/1",
        "portType": "Ethernet Port",
        "serialNo": "FJC2335S09F",
        "series": "Cisco Catalyst 9300 Series Switches",
        "speed": "1000000",
        "status": "up",
        "vlanId": "1",
        "voiceVlan": "",
        "description": "",
        "name": null,
        "instanceUuid": "c9c638b6-4627-4a2e-be25-05f6e487bfcf",
        "instanceTenantId": "66e48af26fe687300375675e",
        "id": "c9c638b6-4627-4a2e-be25-05f6e487bfcf"
      }
    ],
    "version": "string"
  }

#Case 14: Successful Retrieval of Module Count
response_module_count:
  description: Details of the response containing the count of modules.
  returned: always
  type: dict
  sample: {
    "module_count_info": [
                3
            ],
    "version": "string"
  }

#Case 15: Successful Retrieval of Network Device by IP
response_network_device_by_ip:
  description: Details of the response containing network device information retrieved by IP address.
  returned: always
  type: dict
  sample: {
    "response": {
        "apManagerInterfaceIp": "10.10.10.15",
        "associatedWlcIp": "10.10.10.1",
        "bootDateTime": "2025-06-20T09:30:00Z",
        "collectionInterval": "300",
        "collectionStatus": "success",
        "errorCode": "0",
        "errorDescription": "",
        "family": "Cisco Aironet",
        "hostname": "AP-Office-23",
        "id": "ap-12345",
        "instanceTenantId": "tenant-001",
        "instanceUuid": "a1b2c3d4-e5f6-7890-1234-56789abcdef0",
        "interfaceCount": "6",
        "inventoryStatusDetail": "Active",
        "lastUpdateTime": 1687700000,
        "lastUpdated": "2025-06-25T10:00:00Z",
        "lineCardCount": "1",
        "lineCardId": "lc-001",
        "location": "Building 1, Floor 2",
        "locationName": "HQ Floor 2",
        "macAddress": "00:1A:2B:3C:4D:5E",
        "managementIpAddress": "10.10.10.15",
        "memorySize": "2048MB",
        "platformId": "AIR-AP2800",
        "reachabilityFailureReason": "",
        "reachabilityStatus": "reachable",
        "role": "Access Point",
        "roleSource": "auto-discovery",
        "serialNumber": "FTX12345678",
        "series": "2800",
        "snmpContact": "admin@example.com",
        "snmpLocation": "Data Center Rack 5",
        "softwareType": "IOS-XE",
        "softwareVersion": "17.6.1",
        "tagCount": "4",
        "tunnelUdpPort": "4500",
        "type": "wireless-ap",
        "upTime": "3 days, 5 hours",
        "waasDeviceMode": "N/A",
        "dnsResolvedManagementAddress": "ap-office23.example.com",
        "apEthernetMacAddress": "00:1A:2B:3C:4D:5E",
        "vendor": "Cisco",
        "reasonsForPendingSyncRequests": "",
        "pendingSyncRequestsCount": "0",
        "reasonsForDeviceResync": "",
        "lastDeviceResyncStartTime": "2025-06-24T08:00:00Z",
        "uptimeSeconds": 277200,
        "managedAtleastOnce": true,
        "deviceSupportLevel": "Gold",
        "managementState": "Managed",
        "description": "Office wireless access point on Floor 2"
    },
    "version": "string"
  }
"""

from ansible_collections.cisco.dnac.plugins.module_utils.dnac import (
    DnacBase,
)
from ansible.module_utils.basic import AnsibleModule
import json
import time
import os
try:
    import yaml
except ImportError:
    yaml = None
from datetime import datetime

from ansible_collections.cisco.dnac.plugins.module_utils.validation import (
    validate_list_of_dicts,)


class NetworkDevicesInfo(DnacBase):
    """Class containing member attributes for network_devices_info_workflow_manager module"""
    def __init__(self, module):
        super().__init__(module)
        self.supported_states = ['queried']
        self.total_response = []

    def validate_input(self):
        """
        Validate the playbook configuration for device information retrieval and data integrity.

        This method performs strict type checks, required field validation, duplicate detection,
        and default value population to ensure the playbook configuration is correctly structured
        and ready for further processing or API interactions.

        It validates that:
        - The configuration exists and is a list.
        - Each item in the list conforms to the expected schema defined in `config_spec`.
        - Default values are applied where necessary.
        - Invalid parameters are detected and reported.

        Parameters:
            self (object): An instance of the class handling Cisco Catalyst Center operations,
                        containing the `config` attribute to validate.

        Returns:
            self: The current instance with updated attributes:
                - self.msg (str): Status message indicating validation success or failure.
                - self.status (str): Either "success" or "failed", based on validation result.
                - self.validated_config (list): A sanitized, validated version of the playbook configuration,
                                                if validation succeeds.
    """
        self.log("Starting playbook configuration validation.", "INFO")

        config_spec = {
            'network_devices': {
                'type': 'list',
                'elements': 'dict',
                'management_ip_address': {'type': 'list', 'elements': 'str'},
                'mac_address': {'type': 'list', 'elements': 'str'},
                'hostname': {'type': 'list', 'elements': 'str'},
                'serial_number': {'type': 'list', 'elements': 'str'},
                'role': {'type': 'list', 'elements': 'str'},
                'os_type': {'type': 'list', 'elements': 'str'},
                'software_version': {'type': 'list', 'elements': 'str'},
                'site_hierarchy': {'type': 'list', 'elements': 'str'},
                'device_type': {'type': 'list', 'elements': 'str'},
                'family': {'type': 'list', 'elements': 'str'},
                'timeout': {'type': 'int', 'default': 60},
                'retries': {'type': 'int', 'default': 3},
                'interval': {'type': 'int', 'default': 10},
                'output_file_path': {'type': 'str'},
                'format_type': {'type': 'str', 'default': 'yaml'},
                'requested_info': {
                    'type': 'list',
                    'elements': 'str',
                    'default': [
                        "device_info",
                        "interface_info",
                        "interface_vlan_info",
                        "line_card_info",
                        "supervisor_card_info",
                        "poe_info",
                        "module_count_info",
                        "connected_device_info",
                        "device_interfaces_by_range_info",
                        "device_config_info",
                        "device_summary_info",
                        "device_polling_interval_info",
                        "device_stack_info",
                        "device_link_mismatch_info"
                    ]
                },
                "output_file_info": {
                    "type": "dict",
                    "elements": "dict",
                    "file_path": {"type": "str"},
                    'file_format': {'type': 'str', 'default': 'yaml'},
                    'file_mode': {'type': 'str', 'default': 'w'},
                    'timestamp': {'type': 'bool', 'default': False}
                }

            }
        }

        if not self.config:
            self.msg = "Configuration is not available in the playbook for validation"
            self.set_operation_result("failed", False, self.msg, "ERROR")
            return self

        valid_config, invalid_params = validate_list_of_dicts(
            self.config, config_spec
        )

        if invalid_params:
            self.msg = "Invalid parameters in playbook: {0}".format(invalid_params)
            self.set_operation_result("failed", False, self.msg, "ERROR").check_return_status()

        if not valid_config:
            self.log("Configuration validation failed. No valid config found: {0}".format(valid_config))
            self.set_operation_result("failed", False, self.msg, "ERROR").check_return_status()

        self.log("Configuration validated successfully: {0}".format(valid_config), "INFO")
        self.validated_config = valid_config
        return self

    def get_want(self, config):
        """
        Retrieve and validate network device configuration from the playbook.

        This method ensures the presence of required device identification fields and 'requested_info'.
        It prepares the desired state ('want') used for further processing or comparisons.

        Parameters:
            config (dict): Dictionary containing the playbook configuration.
                Must include:
                - "network_devices" (list of dict): List of network device entries.
                    Each entry must include at least one of:
                        - "management_ip_address", "mac_address", "hostname", "serial_number", "role",
                        "os_type", or "software_version"
                    And:
                        - "requested_info" (dict): Non-empty dictionary specifying which details to retrieve.

        Returns:
            self: The current instance of the class with updated 'want' attribute containing
                the validated and extracted network device configuration.
        """
        self.log("Starting desired state preparation with input config: {0}".format(config), "DEBUG")

        DEFAULT_REQUESTED_INFO = [
            "device_info", "interface_info", "interface_vlan_info",
            "line_card_info", "supervisor_card_info", "poe_info",
            "module_count_info", "connected_device_info",
            "device_interfaces_by_range_info", "device_config_info",
            "device_summary_info", "device_polling_interval_info",
            "device_stack_info", "device_link_mismatch_info"
        ]

        desired_devices = {}
        desired_devices["network_devices"] = config.get("network_devices")

        required_device_keys = ['management_ip_address', 'mac_address', 'hostname', 'serial_number',
                                'role', 'os_type', 'software_version', 'site_hierarchy', 'device_type', 'family']
        valid_requested_info_options = ["all"] + DEFAULT_REQUESTED_INFO
        allowed_file_info_keys = {"file_path", "file_format", "file_mode", "timestamp"}
        allowed_file_formats = {"json", "yaml"}
        allowed_file_modes = {"a", "w"}

        if 'network_devices' not in config or not config['network_devices']:
            msg = "Parameter 'network_devices' is mandatory and cannot be empty."
            self.msg = msg
            self.set_operation_result("failed", False, self.msg, "ERROR").check_return_status()

        device_check_passed = True
        requested_info_check_passed = True

        for idx, device in enumerate(config['network_devices']):
            if "all" in device.get("requested_info", []):
                self.log("Expanding 'all' in requested_info for device index {0}".format(idx), "DEBUG")
                device["requested_info"] = [
                    "device_info", "interface_info", "interface_vlan_info",
                    "line_card_info", "supervisor_card_info", "poe_info",
                    "module_count_info", "connected_device_info",
                    "device_interfaces_by_range_info", "device_config_info",
                    "device_summary_info", "device_polling_interval_info",
                    "device_stack_info", "device_link_mismatch_info"
                ]

            if 'requested_info' not in device or not device['requested_info'] or device['requested_info'] == ["all"] or "all" in device['requested_info']:
                self.log("Applying default requested_info for device index {0}".format(idx), "DEBUG")
                device["requested_info"] = DEFAULT_REQUESTED_INFO.copy()
            self.log("Device index {0} requested_info: {1}".format(idx, device.get('requested_info')), "DEBUG")

            if ("device_link_mismatch_info" in device.get("requested_info", [])
                    or device.get("requested_info") in ["all"]):

                site_hierarchy = device.get("site_hierarchy")
                if site_hierarchy is None or site_hierarchy == []:
                    self.msg = "For 'device_link_mismatch_info', 'site_hierarchy' must be provided."
                    self.set_operation_result("failed", False, self.msg, "ERROR").check_return_status()

            if not any(device.get(key) for key in required_device_keys):
                self.log("Device index {0} missing required identification keys: {1}".format(idx, required_device_keys))
                device_check_passed = False
                break

            if 'requested_info' not in device or not isinstance(device['requested_info'], list) or not device['requested_info']:
                requested_info_check_passed = False
                break

            # Validate each entry in requested_info
            for info in device['requested_info']:
                if info not in valid_requested_info_options:
                    self.log("Invalid requested_info '{0}' in device index {1}."
                             "Valid options: {2}".format(info, idx, valid_requested_info_options))
                    self.msg = "'{0}' is not a valid option in 'requested_info'.".format(info)
                    self.set_operation_result("failed", False, self.msg, "ERROR").check_return_status()

            if "output_file_info" in device:
                output_file_info = device["output_file_info"]
                if output_file_info is None:
                    continue

                for key in output_file_info:
                    if key not in allowed_file_info_keys:
                        self.msg = "Invalid file_info key '{0}' in device index {1}."\
                            "Allowed keys: {2}".format(key, idx, sorted(allowed_file_info_keys))
                        self.set_operation_result("failed", False, self.msg, "ERROR")

                    if output_file_info["file_format"] not in allowed_file_formats:
                        self.msg = "Invalid file_format '{0}' in device index {1}. "\
                            "Allowed formats: {2}".format(output_file_info.get("file_format"), idx, sorted(allowed_file_formats))
                        self.set_operation_result("failed", False, self.msg, "ERROR")

                    if output_file_info["file_mode"] not in allowed_file_modes:
                        self.msg = "Invalid 'file_mode' '{0}' in device index {1}. "\
                            "Allowed modes: {2}".format(output_file_info.get("file_mode"), idx, ", ".join(sorted(allowed_file_modes)))
                        self.set_operation_result("failed", False, self.msg, "ERROR")

        if not device_check_passed:
            self.msg = "At least one of the following parameters must be specified inside each network device: {0}.".format(", ".join(required_device_keys))
            self.set_operation_result("failed", False, self.msg, "ERROR").check_return_status()
        elif not requested_info_check_passed:
            self.msg = "Parameter 'requested_info' is mandatory and must be a non-empty list inside each network device."
            self.set_operation_result("failed", False, self.msg, "ERROR").check_return_status()

        self.want = desired_devices
        self.log("Completed desired state preparation. Final state: {0}".format(self.want), "INFO")
        return self

    def get_diff_queried(self, config):
        """
        Processes the device configuration and retrieves requested information for each device.

        This method iterates over the network devices listed under the "network_devices" key in the given
        configuration dictionary. For each device entry, it filters out the "requested_info" key, applies
        a default list of requested information if necessary, and calls respective data retrieval methods
        to gather the requested device details. The collected results are aggregated into a combined
        dictionary.

        If an output file path is specified, the combined data is saved to the file, with logging of any
        errors during the save operation. All collected responses are appended to the instance attribute
        `self.total_response`.

        Upon completion, the method sets the operation result status and message indicating success and
        returns the current instance.

        Parameters:
            config (dict): Configuration dictionary expected to contain:
                - "network_devices" (list of dict): Each dictionary includes device parameters such as
                IP, MAC, hostname, and optionally:
                    - "requested_info" (list): Specifies which categories of device info to retrieve.
                    If missing, empty, or containing "all", a default full list is used.
                    - "output_file_path" (str): Optional path to save the combined output.

        Returns:
            self: The current instance with updated internal state reflecting the operation results.
        """
        self.log("Starting device info retrieval for all device entries", "INFO")
        network_device_details = config.get("network_devices")

        if not network_device_details:
            self.msg = "No network_devices found in configuration."
            self.set_operation_result("failed", False, self.msg, "ERROR")
            return self

        DEFAULT_REQUESTED_INFO = [
            "device_info", "interface_info", "interface_vlan_info",
            "line_card_info", "supervisor_card_info", "poe_info",
            "module_count_info", "connected_device_info",
            "device_interfaces_by_range_info", "device_config_info",
            "device_summary_info", "device_polling_interval_info",
            "device_stack_info", "device_link_mismatch_info"
        ]

        for idx, config in enumerate(network_device_details):
            self.log("Processing device entry {0}: {1}".format(idx, config), "DEBUG")
            filtered_config = {}
            for key, value in config.items():
                if key != "requested_info":
                    filtered_config[key] = value
            self.log("Filtered config (excluding requested_info): {0}".format(filtered_config))

            requested_info = config.get("requested_info", [])
            if not requested_info or requested_info == ["all"] or "all" in requested_info:
                self.log("Applying default requested_info for device entry {0}".format(idx), "DEBUG")
                requested_info = DEFAULT_REQUESTED_INFO.copy()

            device_ids = self.get_device_id(filtered_config)
            combined_data = {}
            if not device_ids:
                self.msg = "No network devices found for the given filters."
                self.total_response.append(self.msg)
                break
            else:
                device_ips = []
                for device_id in device_ids:
                    self.log("Processing device ID: {0}".format(device_id), "DEBUG")
                    device_ip = self.get_device_ip_from_id(device_id)
                    if device_ip:
                        device_ips.append(device_ip)
                self.total_response.append("The network devices found: {0}".format(device_ips))

            if "device_info" in requested_info:
                self.log("Checking if 'device_info' is requested.", "DEBUG")
                self.log("Fetching device_info for device_ips: {0}".format(device_ips), "DEBUG")
                result = self.get_device_info(device_ids)
                self.total_response.append(result)
                combined_data["device_info"] = result

            if "interface_info" in requested_info:
                self.log("Checking if 'interface_info' is requested.", "DEBUG")
                self.log("Fetching interface_info for device_ips: {0}".format(device_ips), "DEBUG")
                result = self.get_interface_info(device_ids)
                self.total_response.append(result)
                combined_data["interface_info"] = result

            if "interface_vlan_info" in requested_info:
                self.log("Checking if 'interface_vlan_info' is requested.", "DEBUG")
                self.log("Fetching interface_vlan_info for device_ips: {0}".format(device_ips), "DEBUG")
                result = self.get_device_interface_vlans(device_ids)
                self.total_response.append(result)
                combined_data["interface_vlan_info"] = result

            if "line_card_info" in requested_info:
                self.log("Checking if 'line_card_info' is requested.", "DEBUG")
                self.log("Fetching line_card_info for device_ips: {0}".format(device_ips), "DEBUG")
                result = self.get_linecard_details(device_ids)
                self.total_response.append(result)
                combined_data["line_card_info"] = result

            if "supervisor_card_info" in requested_info:
                self.log("Checking if 'supervisor_card_info' is requested.", "DEBUG")
                self.log("Fetching supervisor_card_info for device_ips: {0}".format(device_ips), "DEBUG")
                result = self.get_supervisor_card_detail(device_ids)
                self.total_response.append(result)
                combined_data["supervisor_card_info"] = result

            if "poe_info" in requested_info:
                self.log("Checking if 'poe_info' is requested.", "DEBUG")
                self.log("Fetching poe_info for device_ips: {0}".format(device_ips), "DEBUG")
                result = self.get_poe_details(device_ids)
                self.total_response.append(result)
                combined_data["poe_info"] = result

            if "module_count_info" in requested_info:
                self.log("Checking if 'module_count_info' is requested.", "DEBUG")
                self.log("Fetching module_count_info for device_ips: {0}".format(device_ips), "DEBUG")
                result = self.get_module_count(device_ids)
                self.total_response.append(result)
                combined_data["module_count_info"] = result

            if "connected_device_info" in requested_info:
                self.log("Checking if 'connected_device_info' is requested.", "DEBUG")
                self.log("Fetching connected_device_info for device_ips: {0}".format(device_ips), "DEBUG")
                result = self.get_connected_device_details_from_interfaces(device_ids)
                self.total_response.append(result)
                combined_data["connected_device_info"] = result

            if "device_interfaces_by_range_info" in requested_info:
                self.log("Checking if 'device_interfaces_by_range_info' is requested.", "DEBUG")
                self.log("Fetching device_interfaces_by_range_info for device_ips: {0}".format(device_ips), "DEBUG")
                result = self.get_interfaces_by_specified_range(device_ids)
                self.total_response.append(result)
                combined_data["device_interfaces_by_range_info"] = result

            if "device_config_info" in requested_info:
                self.log("Checking if 'device_config_info' is requested.", "DEBUG")
                self.log("Fetching device_config_info for device_ips: {0}".format(device_ips), "DEBUG")
                result = self.get_device_config(device_ids)
                self.total_response.append(result)
                combined_data["device_config_info"] = result

            if "device_summary_info" in requested_info:
                self.log("Checking if 'device_summary_info' is requested.", "DEBUG")
                self.log("Fetching device_summary_info for device_ips: {0}".format(device_ips), "DEBUG")
                result = self.get_device_summary(device_ids)
                self.total_response.append(result)
                combined_data["device_summary_info"] = result

            if "device_polling_interval_info" in requested_info:
                self.log("Checking if 'device_polling_interval_info' is requested.", "DEBUG")
                self.log("Fetching device_polling_interval_info for device_ips: {0}".format(device_ips), "DEBUG")
                result = self.get_polling_interval(device_ids)
                self.total_response.append(result)
                combined_data["device_polling_interval_info"] = result

            if "device_stack_info" in requested_info:
                self.log("Checking if 'device_stack_info' is requested.", "DEBUG")
                self.log("Fetching device_stack_info for device_ips: {0}".format(device_ips), "DEBUG")
                result = self.get_stack_details(device_ids)
                self.total_response.append(result)
                combined_data["device_stack_info"] = result

            if "device_link_mismatch_info" in requested_info:
                self.log("Checking if 'device_link_mismatch_info' is requested.", "DEBUG")
                self.log("Fetching device_link_mismatch_info for device_ips: {0}".format(device_ips), "DEBUG")
                site_names = config.get("site_hierarchy", [])
                site_ids = []
                for site_name in site_names:
                    self.log("Fetching site ID for site name: {0}".format(site_name), "DEBUG")
                    site_id_list = self.get_site_id(site_name)
                    self.log(site_id_list, "DEBUG")

                    if site_id_list and isinstance(site_id_list, tuple):
                        site_ids.extend(site_id_list)

                site_ids = [sid for sid in site_ids if isinstance(sid, str)]
                self.log("Site hierarchy for link mismatch: {0}".format(site_ids), "DEBUG")
                result = self.get_device_link_mismatch_by_sites(device_ids=device_ids, site_ids=site_ids)
                self.total_response.append(result)
                combined_data["device_link_mismatch_info"] = result

            file_info = config.get("file_info")
            if file_info:
                self.log("Writing combined_data to file using file_info: {0}".format(file_info), "INFO")
                self.write_device_info_to_file({"file_info": file_info, "data": combined_data})

        if network_device_details:
            output_file_info = network_device_details[0].get("output_file_info")

        if output_file_info:
            self.write_device_info_to_file({"output_file_info": output_file_info})

        if self.total_response:
            self.msg = self.total_response
            self.set_operation_result("success", False, self.msg, "INFO")

        return self

    def get_device_info(self, device_ids):
        """
        Fetch detailed information for a list of network devices from Cisco Catalyst Center.

        For each device ID, this method calls the 'get_device_list' API and aggregates the results.
        Each entry in the returned list contains the device's management IP and its details.

        The retrieved device details include key fields like:
        family, type, lastUpdateTime, macAddress, softwareVersion, serialNumber, managementIpAddress,
        hostname, upTime, role, platformId, reachabilityStatus, description, instanceUuid, id
        and more, providing a comprehensive overview of each device's configuration and status.

        Executes API calls for each device ID and aggregates the retrieved data into a structured list.

        Parameters:
            device_ids (list): List of device UUIDs whose information needs to be fetched.

        Returns:
            list: A list with a single dictionary:
                [
                    {
                        "device_info": [
                            {
                                "device_ip": <str>,
                                "device_details": <list of device details, exception or empty string>
                            },
                        ]
                    }
                ]
        """

        self.log("Starting device info retrieval for device_ids: {0}".format(device_ids), "INFO")
        if not device_ids:
            self.log("No device IDs provided for Device info data retrieval", "WARNING")
            return [{"device_info": []}]

        device_info_list = []

        for device_id in device_ids:
            device_ip = self.get_device_ip_from_id(device_id)
            self.log("Processing device ID: {0} (IP: {1})".format(device_id, device_ip), "DEBUG")
            self.log("Fetching device info for device_id: {0}, device_ip: {1}".format(device_id, device_ip), "DEBUG")

            try:
                response = self.dnac._exec(
                    family="devices",
                    function="get_device_list",
                    params={'id': device_id}
                )
                self.log(
                    "Received API response from 'get_device_info' for device {0} (IP: {1}): {2}".format(
                        device_id, device_ip, response), "DEBUG")

                device_response = response.get("response", [])
                if device_response:
                    self.log("Device details found for device_id: {0}, device_ip: {1}".format(device_id, device_ip), "INFO")
                    device_info_list.append({
                        "device_ip": device_ip,
                        "device_details": [device_response]
                    })
                else:
                    self.log("No device details found for device_id: {0}, device_ip: {1}".format(device_id, device_ip), "WARNING")
                    device_info_list.append({
                        "device_ip": device_ip,
                        "device_details": []
                    })

            except Exception as e:
                self.msg = "Exception occurred while getting device list for device_id {0}, device_ip {1}: {2}".format(device_id, device_ip, e)
                device_info_list.append({
                    "device_ip": device_ip,
                    "device_details": "Error: {0}".format(e)
                })
                continue

        result = [{"device_info": device_info_list}]

        self.log("Completed device info retrieval. Total devices processed: {0}".format(len(device_info_list)), "INFO")
        self.log("Device info result: {0}".format(result), "DEBUG")
        return result

    def get_device_interface_vlans(self, device_ids):
        """
        Fetch VLAN interface details for a list of devices from Cisco Catalyst Center.

        For each device ID, this method calls the 'get_device_list' API and aggregates the results.
        Each entry in the returned list contains the device's management IP and its details.

        Retrieves VLAN interface configuration data for each device ID and aggregates the results
        into a structured format. Each device's VLAN interface details include interface-specific
        VLAN assignments, configurations, and related network information.

        The retrieved VLAN interface details include key fields such as:
        - interfaceName (e.g., "GigabitEthernet0/1")
        - ipAddress (e.g., "192.168.10.25")
        - mask (e.g., 24)
        - networkAddress (e.g., "192.168.10.0")
        - numberOfIPs (e.g., 254)
        - prefix (e.g., "192.168.10.0/24")
        - vlanNumber (e.g., 10)
        - vlanType (e.g., "Data")

        Parameters:
            device_ids (list): List of device UUIDs for which VLAN interface data needs to be fetched.

        Returns:
            list: A list with a single dictionary:
                [
                    {
                        "interface_vlan_info": [
                            {
                                "device_ip": <str>,
                                "interface_vlan_details": <list of VLAN interface details, exception or empty string>
                            },
                        ]
                    }
                ]
        """

        self.log("Fetching VLAN interface data for {0} devices: {1}".format(len(device_ids), device_ids), "INFO")
        if not device_ids:
            self.log("No device IDs provided for VLAN interface data retrieval", "WARNING")
            return [{"interface_vlan_info": []}]

        vlans_info_list = []

        for device_id in device_ids:
            device_ip = self.get_device_ip_from_id(device_id)
            self.log("Processing device ID: {0} (IP: {1})".format(device_id, device_ip), "DEBUG")
            self.log("Fetching device interface vlans info for device_id: {0}, device_ip: {1}".format(device_id, device_ip), "DEBUG")

            try:
                response = self.dnac._exec(
                    family="devices",
                    function="get_device_interface_vlans",
                    params={'id': device_id}
                )
                self.log(
                    "Received API response from 'get_device_interface_vlans' for device {0} (IP: {1}): {2}".format(
                        device_id, device_ip, response), "DEBUG")

                vlan_data = response.get("response", [])
                if vlan_data:
                    self.log("Found {0} VLAN records for device IP: {1}".format(len(vlan_data), device_ip), "DEBUG")
                    vlans_info_list.append({
                        "device_ip": device_ip,
                        "interface_vlan_details": [vlan_data]
                    })
                else:
                    self.log("No VLAN interface data found for device IP: {0}".format(device_ip), "DEBUG")
                    vlans_info_list.append({
                        "device_ip": device_ip,
                        "interface_vlan_details": []
                    })

            except Exception as e:
                self.msg = "Exception occurred while getting VLAN interface data for device {0} (IP: {1}): {2}".format(device_id, device_ip, e)
                vlans_info_list.append({
                    "device_ip": device_ip,
                    "interface_vlan_details": "Error: {0}".format(e)
                })
                continue

        result = [{"interface_vlan_info": vlans_info_list}]

        self.log("Completed Interface Vlan info retrieval. Total devices processed: {0}".format(len(vlans_info_list)), "INFO")
        self.log("Interface Vlan info result: {0}".format(result), "DEBUG")
        return result

    def get_linecard_details(self, device_ids):
        """
        Fetch line card details for a list of devices from Cisco Catalyst Center.

        For each device ID, this method calls the 'get_device_list' API and aggregates the results.
        Each entry in the returned list contains the device's management IP and its details.

        Queries and aggregates line card information for each provided device ID.

        The retrieved line card details include key fields such as:
        - serialno (e.g., "SN123456789")
        - partno (e.g., "PN987654321")
        - switchno (e.g., "SW-001-A1")
        - slotno (e.g., "Slot-04")

        Parameters:
            device_ids (list): List of device UUIDs for which line card details are to be retrieved.

        Returns:
            list: A list with a single dictionary:
                [
                    {
                        "line_card_info": [
                            {
                                "device_ip": <str>,
                                "linecard_details": <list of line card details, exception or empty string>
                            },
                        ]
                    }
                ]
        """

        self.log("Fetching Line card data for {0} devices: {1}".format(len(device_ids), device_ids), "INFO")
        if not device_ids:
            self.log("No device IDs provided for Line Card info retrieval", "WARNING")
            return [{"line_card_info": []}]

        linecards_info_list = []

        for device_id in device_ids:
            device_ip = self.get_device_ip_from_id(device_id)
            self.log("Processing device ID: {0} (IP: {1})".format(device_id, device_ip), "DEBUG")
            self.log("Fetching line card info for device_id: {0}, device_ip: {1}".format(device_id, device_ip), "DEBUG")

            try:
                response = self.dnac._exec(
                    family="devices",
                    function="get_linecard_details",
                    params={'device_uuid': device_id}
                )
                self.log(
                    "Received API response from 'get_linecard_details' for device {0} (IP: {1}): {2}".format(
                        device_id, device_ip, response), "DEBUG")

                linecard_data = response.get("response", [])
                if linecard_data:
                    self.log("Found {0} line card records for device IP: {1}".format(len(linecard_data), device_ip), "DEBUG")
                    linecards_info_list.append({
                        "device_ip": device_ip,
                        "linecard_details": [linecard_data]
                    })
                else:
                    self.log("No line card details found for device IP: {0}".format(device_ip), "DEBUG")
                    linecards_info_list.append({
                        "device_ip": device_ip,
                        "linecard_details": []
                    })

            except Exception as e:
                self.msg = "Exception occurred while getting line card info list for device_id {0}, device_ip {1}: {2}".format(device_id, device_ip, e)
                linecards_info_list.append({
                    "device_ip": device_ip,
                    "linecard_details": "Error: {0}".format(e)
                })
                continue

        result = [{"line_card_info": linecards_info_list}]

        self.log("Completed Line Card info retrieval. Total devices processed: {0}".format(len(linecards_info_list)), "INFO")
        self.log("Line Card info result: {0}".format(result), "DEBUG")
        return result

    def get_stack_details(self, device_ids):
        """
        Fetch stack details for a list of devices from Cisco Catalyst Center.

        For each device ID, this method calls the 'get_device_list' API and aggregates the results.
        Each entry in the returned list contains the device's management IP and its details.

        Retrieves stack member information for each given device ID and compiles the results.

        The stack member info includes key fields such as:
        - stackSwitchInfo: list of dicts with fields including hwPriority, macAddress, role, softwareImage,
        stackMemberNumber, state, switchPriority, serialNumber, platformId, entPhysicalIndex
        - stackPortInfo: list of dicts with fields including isSynchOk, name, switchPort, neighborPort,
        nrLinkOkChanges, stackCableLengthInfo, stackPortOperStatusInfo, linkActive, linkOk
        - svlSwitchInfo: list of dicts with fields including macAddress, role, softwareImage,
        stackMemberNumber, state, switchPriority, serialNumber, platformId, entPhysicalIndex

        Parameters:
            device_ids (list): List of device IDs for which stack details are to be retrieved.

        Returns:
            list: A list with a single dictionary:
                [
                    {
                        "device_stack_info": [
                            {
                                "device_ip": <str>,
                                "stack_details": <list of stack member details, exception or empty string>
                            },
                        ]
                    }
                ]
        """

        self.log("Fetching stack details for {0} devices: {1}".format(len(device_ids), device_ids), "INFO")
        if not device_ids:
            self.log("No device IDs provided for Stack info retrieval", "WARNING")
            return [{"device_stack_info": []}]

        stack_info_list = []

        for device_id in device_ids:
            device_ip = self.get_device_ip_from_id(device_id)
            self.log("Processing device ID: {0} (IP: {1})".format(device_id, device_ip), "DEBUG")
            self.log("Fetching stack info for device_id: {0}, device_ip: {1}".format(device_id, device_ip), "DEBUG")

            try:
                response = self.dnac._exec(
                    family="devices",
                    function="get_stack_details_for_device",
                    params={'device_id': device_id}
                )
                self.log(
                    "Received API response from 'get_stack_details' for device {0} (IP: {1}): {2}".format(
                        device_id, device_ip, response), "DEBUG")

                stack_info = response.get("response", [])
                if stack_info:
                    self.log("Found {0} stack records for device IP: {1}".format(len(stack_info), device_ip), "DEBUG")
                    stack_info_list.append({
                        "device_ip": device_ip,
                        "stack_details": [stack_info]
                    })
                else:
                    self.log("No stack details found for device IP: {0}".format(device_ip), "DEBUG")
                    stack_info_list.append({
                        "device_ip": device_ip,
                        "stack_details": []
                    })

            except Exception as e:
                self.msg = "Exception occurred while getting device stack info list for device_id {0}, device_ip {1}: {2}".format(device_id, device_ip, e)
                stack_info_list.append({
                    "device_ip": device_ip,
                    "stack_details": "Error: {0}".format(e)
                })
                continue

        result = [{"device_stack_info": stack_info_list}]

        self.log("Completed Stack info retrieval. Total devices processed: {0}".format(len(stack_info_list)), "INFO")
        self.log("Stack info result: {0}".format(result), "DEBUG")
        return result

    def get_device_config(self, device_ids):
        """
        Fetch configuration data for a list of devices from Cisco Catalyst Center.

        For each device ID, this method calls the 'get_device_list' API and aggregates the results.
        Each entry in the returned list contains the device's management IP and its details.

        Retrieves the full configuration details for each specified device ID and aggregates the results.

        The configuration details include the device's running configuration, which may consist of
        multiple lines of configuration commands.

        Parameters:
            device_ids (list): List of device IDs for which configuration details need to be fetched.

        Returns:
            list: A list with a single dictionary:
                [
                    {
                        "device_config_info": [
                            {
                                "device_ip": <str>,
                                "device_config_details": <list of configuration lines, exception or empty string>
                            },
                        ]
                    }
                ]
        """

        self.log("Fetching Device config data for {0} devices: {1}".format(len(device_ids), device_ids), "INFO")
        if not device_ids:
            self.log("No device IDs provided for Device Config info retrieval", "WARNING")
            return [{"device_config_info": []}]

        device_config_list = []

        for device_id in device_ids:
            device_ip = self.get_device_ip_from_id(device_id)
            self.log("Processing device ID: {0} (IP: {1})".format(device_id, device_ip), "DEBUG")
            self.log("Fetching device config info for device_id: {0}, device_ip: {1}".format(device_id, device_ip), "DEBUG")

            try:
                response = self.dnac._exec(
                    family="devices",
                    function="get_device_config_by_id",
                    params={'network_device_id': device_id}
                )
                self.log(
                    "Received API response from 'get_device_config' for device {0} (IP: {1}): {2}".format(
                        device_id, device_ip, response), "DEBUG")

                config_data = response.get("response", [])
                if config_data:
                    self.log("Found {0} configuration lines for device IP: {1}".format(len(config_data), device_ip), "DEBUG")
                    device_config_list.append({
                        "device_ip": device_ip,
                        "device_config_details": [config_data]
                    })
                else:
                    self.log("No device config card details found for device IP: {0}".format(device_ip), "DEBUG")
                    device_config_list.append({
                        "device_ip": device_ip,
                        "device_config_details": []
                    })

            except Exception as e:
                self.msg = "Exception occurred while getting device config for device_id {0}, device_ip {1}: {2}".format(device_id, device_ip, e)
                device_config_list.append({
                    "device_ip": device_ip,
                    "device_config_details": "Error: {0}".format(e)
                })
                continue

        result = [{"device_config_info": device_config_list}]

        self.log("Completed Device Config info retrieval. Total devices processed: {0}".format(len(device_config_list)), "INFO")
        self.log("Device Config info result: {0}".format(result), "DEBUG")
        return result

    def get_polling_interval(self, device_ids):
        """
        Fetch polling interval information for a list of devices from Cisco Catalyst Center.

        For each device ID, this method calls the 'get_device_list' API and aggregates the results.
        Each entry in the returned list contains the device's management IP and its details.

        Retrieves the polling interval configuration for each specified device ID and compiles the results.

        The polling interval details include the time intervals at which the device is polled for updates,
        which can be critical for monitoring and management tasks (e.g., 86400 seconds for daily polling).

        Parameters:
            device_ids (list): List of device IDs for which polling interval details need to be retrieved.

        Returns:
            list: A list with a single dictionary:
                [
                    {
                        "device_polling_interval_info": [
                            {
                                "device_ip": <str>,
                                "polling_interval_details": <list of polling interval values, exception or empty string>
                            },
                        ]
                    }
                ]
        """

        self.log("Fetching polling interval data for {0} devices: {1}".format(len(device_ids), device_ids), "INFO")
        if not device_ids:
            self.log("No device IDs provided for Polling Interval info retrieval", "WARNING")
            return [{"device_polling_interval_info": []}]

        polling_intervals_info_list = []

        for device_id in device_ids:
            device_ip = self.get_device_ip_from_id(device_id)
            self.log("Processing device ID: {0} (IP: {1})".format(device_id, device_ip), "DEBUG")
            self.log("Fetching polling intervals info for device_id: {0}, device_ip: {1}".format(device_id, device_ip), "DEBUG")

            try:
                response = self.dnac._exec(
                    family="devices",
                    function="get_polling_interval_by_id",
                    params={'id': device_id}
                )
                self.log(
                    "Received API response from 'get_polling_interval' for device {0} (IP: {1}): {2}".format(
                        device_id, device_ip, response), "DEBUG")

                intervals = response.get("response", [])
                if intervals:
                    self.log("Found {0} polling interval records for device IP: {1}".format((intervals), device_ip), "DEBUG")
                    polling_intervals_info_list.append({
                        "device_ip": device_ip,
                        "polling_interval_details": [intervals]
                    })
                else:
                    self.log("No polling interval details found for device IP: {0}".format(device_ip), "DEBUG")
                    polling_intervals_info_list.append({
                        "device_ip": device_ip,
                        "polling_interval_details": []
                    })

            except Exception as e:
                self.msg = "Exception occurred while getting polling interval info list for device_id {0}, device_ip {1}: {2}".format(device_id, device_ip, e)
                polling_intervals_info_list.append({
                    "device_ip": device_ip,
                    "polling_interval_details": "Error: {0}".format(e)
                })
                continue

        result = [{"device_polling_interval_info": polling_intervals_info_list}]

        self.log("Completed Device Polling Interval info retrieval. Total devices processed: {0}".format(len(polling_intervals_info_list)), "INFO")
        self.log("Device Polling Interval info result: {0}".format(result), "DEBUG")
        return result

    def get_device_summary(self, device_ids):
        """
        Fetch summary information of devices for a list of devices from Cisco Catalyst Center.

        For each device ID, this method calls the 'get_device_list' API and aggregates the results.
        Each entry in the returned list contains the device's management IP and its details.

        Retrieves key summary details for each device ID provided and aggregates the results.

        The retrieved device summary details include key fields such as:
        - id (e.g., "e62e6405-13e4-4f1b-ae1c-580a28a96a88")
        - role (e.g., "ACCESS")
        - roleSource (e.g., "MANUAL")

        Parameters:
            device_ids (list): List of device IDs for which summary information needs to be retrieved.

        Returns:
            list: A list with a single dictionary:
                [
                    {
                        "device_summary_info": [
                            {
                                "device_ip": <str>,
                                "device_summary_details": <list of summary details, exception or empty string>
                            },
                        ]
                    }
                ]
        """

        self.log("Fetching device summary data for {0} devices: {1}".format(len(device_ids), device_ids), "INFO")
        if not device_ids:
            self.log("No device IDs provided for Device Summary info retrieval", "WARNING")
            return [{"device_summary_info": []}]

        device_summary_info_list = []

        for device_id in device_ids:
            device_ip = self.get_device_ip_from_id(device_id)
            self.log("Processing device ID: {0} (IP: {1})".format(device_id, device_ip), "DEBUG")
            self.log("Fetching device summary info for device_id: {0}, device_ip: {1}".format(device_id, device_ip), "DEBUG")

            try:
                response = self.dnac._exec(
                    family="devices",
                    function="get_device_summary",
                    params={'id': device_id}
                )
                self.log(
                    "Received API response from 'get_device_summary' for device {0} (IP: {1}): {2}".format(
                        device_id, device_ip, response), "DEBUG")

                summary_data = response.get("response", [])
                self.log("Summary data: {0}".format(summary_data), "DEBUG")
                if summary_data:
                    self.log("Found {0} summary records for device IP: {1}".format(len(summary_data), device_ip), "DEBUG")
                    device_summary_info_list.append({
                        "device_ip": device_ip,
                        "device_summary_details": [summary_data]
                    })
                else:
                    self.log("No device summary details found for device IP: {0}".format(device_ip), "DEBUG")
                    device_summary_info_list.append({
                        "device_ip": device_ip,
                        "device_summary_details": []
                    })

            except Exception as e:
                self.msg = "Exception occurred while getting device summary list for device_id {0}, device_ip {1}: {2}".format(device_id, device_ip, e)
                device_summary_info_list.append({
                    "device_ip": device_ip,
                    "device_summary_details": "Error: {0}".format(e)
                })
                continue

        result = [{"device_summary_info": device_summary_info_list}]

        self.log("Completed Device Summary info retrieval. Total devices processed: {0}".format(len(device_summary_info_list)), "INFO")
        self.log("Device Summary info result: {0}".format(result), "DEBUG")
        return result

    def get_supervisor_card_detail(self, device_ids):
        """
        Fetch supervisor card details for a list of devices from Cisco Catalyst Center.

        For each device ID, this method calls the 'get_device_list' API and aggregates the results.
        Each entry in the returned list contains the device's management IP and its details.

        Retrieves detailed supervisor card information for each provided device ID.

        The retrieved supervisor card details include key fields such as:
        - serialno (e.g., "SN1234567890")
        - partno (e.g., "PN9876543210")
        - switchno (e.g., "SW-01")
        - slotno (e.g., "3")

        Parameters:
            device_ids (list): List of device IDs to query for supervisor card details.

        Returns:
            list: A list with a single dictionary:
                [
                    {
                        "supervisor_card_info": [
                            {
                                "device_ip": <str>,
                                "supervisor_card_details": <list of supervisor card details, exception or empty string>
                            },
                        ]
                    }
                ]
        """

        self.log("Fetching supervisor card data for {0} devices: {1}".format(len(device_ids), device_ids), "INFO")
        if not device_ids:
            self.log("No device IDs provided for Supervisor Card info retrieval", "WARNING")
            return [{"supervisor_card_info": []}]

        supervisor_cards_info_list = []

        for device_id in device_ids:
            device_ip = self.get_device_ip_from_id(device_id)
            self.log("Processing device ID: {0} (IP: {1})".format(device_id, device_ip), "DEBUG")
            self.log("Fetching supervisor card info for device_id: {0}, device_ip: {1}".format(device_id, device_ip), "DEBUG")

            try:
                response = self.dnac._exec(
                    family="devices",
                    function="get_supervisor_card_detail",
                    params={'device_uuid': device_id}
                )
                self.log(
                    "Received API response from 'get_supervisor_card_details' for device {0} (IP: {1}): {2}".format(
                        device_id, device_ip, response), "DEBUG")

                supervisor_cards = response.get("response", [])
                if supervisor_cards:
                    self.log("Found {0} supervisor card records for device IP: {1}".format(len(supervisor_cards), device_ip), "DEBUG")
                    supervisor_cards_info_list.append({
                        "device_ip": device_ip,
                        "supervisor_card_details": [supervisor_cards]
                    })
                else:
                    self.log("No supervisor card details found for device IP: {0}".format(device_ip), "DEBUG")
                    supervisor_cards_info_list.append({
                        "device_ip": device_ip,
                        "supervisor_card_details": []
                    })

            except Exception as e:
                self.msg = "Exception occurred while getting supervisor card info list for device_id {0}, device_ip {1}: {2}".format(device_id, device_ip, e)
                supervisor_cards_info_list.append({
                    "device_ip": device_ip,
                    "supervisor_card_details": "Error: {0}".format(e)
                })
                continue

        result = [{"supervisor_card_info": supervisor_cards_info_list}]

        self.log("Completed Device Supervisor Card info retrieval. Total devices processed: {0}".format(len(supervisor_cards_info_list)), "INFO")
        self.log("Device Supervisor Card info result: {0}".format(result), "DEBUG")
        return result

    def get_poe_details(self, device_ids):
        """
        Fetch Power over Ethernet (PoE) details for specified devices from Cisco Catalyst Center.

        For each device ID, this method calls the 'get_device_list' API and aggregates the results.
        Each entry in the returned list contains the device's management IP and its details.

        Retrieves PoE information for each device ID provided.

        The retrieved PoE details include key fields such as:
        - powerAllocated (e.g., "525")
        - powerConsumed (e.g., "0")
        - powerRemaining (e.g., "525")

        Parameters:
            device_ids (list): List of device IDs to query for PoE details.

        Returns:
            list: A list with a single dictionary:
                [
                    {
                        "poe_info": [
                            {
                                "device_ip": <str>,
                                "poe_details": <list of PoE details, exception or empty string>
                            },
                        ]
                    }
                ]
        """

        self.log("Fetching PoE data for {0} devices: {1}".format(len(device_ids), device_ids), "INFO")
        if not device_ids:
            self.log("No device IDs provided for PoE info retrieval", "WARNING")
            return [{"poe_info": []}]

        poe_info_list = []

        for device_id in device_ids:
            device_ip = self.get_device_ip_from_id(device_id)
            self.log("Processing device ID: {0} (IP: {1})".format(device_id, device_ip), "DEBUG")
            self.log("Fetching poe info for device_id: {0}, device_ip: {1}".format(device_id, device_ip), "DEBUG")

            try:
                response = self.dnac._exec(
                    family="devices",
                    function="poe_details",
                    params={'device_uuid': device_id}
                )
                self.log(
                    "Received API response from 'poe_details': {0}".format(
                        (response)
                    ),
                    "DEBUG",
                )
                poe_data = response.get("response", [])
                if poe_data:
                    self.log("Found {0} PoE records for device IP: {1}".format(len(poe_data), device_ip), "DEBUG")
                    poe_info_list.append({
                        "device_ip": device_ip,
                        "poe_details": [poe_data]
                    })
                else:
                    self.log("No PoE details found for device IP: {0}".format(device_ip), "DEBUG")
                    poe_info_list.append({
                        "device_ip": device_ip,
                        "poe_details": []
                    })

            except Exception as e:
                self.msg = "Exception occurred while getting PoE Info list for device_id {0}, device_ip {1}: {2}".format(device_id, device_ip, e)
                poe_info_list.append({
                    "device_ip": device_ip,
                    "poe_details": "Error: {0}".format(e)
                })
                continue

        result = [{"poe_info": poe_info_list}]

        self.log("Completed Device PoE info retrieval. Total devices processed: {0}".format(len(poe_info_list)), "INFO")
        self.log("Device PoE info result: {0}".format(result), "DEBUG")
        return result

    def get_interface_info(self, device_ids):
        """
        Fetch interface information on interfaces for specified devices from Cisco Catalyst Center.

        For each device ID, this method calls the 'get_device_list' API and aggregates the results.
        Each entry in the returned list contains the device's management IP and its details.

        Retrieves detailed interface data for each device ID provided.

        The retrieved interface details include key fields such as:
        - adminStatus (e.g., "UP")
        - duplex (e.g., "FullDuplex")
        - ifIndex (e.g., "73")
        - interfaceType (e.g., "Physical")
        - macAddress (e.g., "0c:75:bd:42:db:c1")
        - mtu (e.g., "9100")
        - nativeVlanId (e.g., "1")
        - portMode (e.g., "access")
        - portName (e.g., "AppGigabitEthernet1/0/1")
        - portType (e.g., "Ethernet Port")
        - serialNo (e.g., "FJC2335S09F")
        - speed (e.g., "1000000")
        - status (e.g., "up")
        - vlanId (e.g., "1")
        - voiceVlan (e.g., "")
        - description (e.g., "")
        - instanceUuid
        - instanceTenantId

        Parameters:
            device_ids (list): List of device IDs to retrieve interface info for.

        Returns:
            list: A list with a single dictionary:
                [
                    {
                        "interface_info": [
                            {
                                "device_ip": <str>,
                                "interface_details": <list of interface details, exception or empty string>
                            },
                        ]
                    }
                ]
        """

        self.log("Fetching interface info for {0} devices: {1}".format(len(device_ids), device_ids), "INFO")
        if not device_ids:
            self.log("No device IDs provided for Interface info retrieval", "WARNING")
            return [{"interface_info": []}]

        interface_info_list = []

        for device_id in device_ids:
            device_ip = self.get_device_ip_from_id(device_id)
            self.log("Processing device ID: {0} (IP: {1})".format(device_id, device_ip), "DEBUG")
            self.log("Fetching device interface info for device_id: {0}, device_ip: {1}".format(device_id, device_ip), "DEBUG")

            try:
                response = self.dnac._exec(
                    family="devices",
                    function="get_interface_info_by_id",
                    params={'device_id': device_id}
                )
                self.log(
                    "Received API response from 'get_interface_info' for device {0} (IP: {1}): {2}".format(
                        device_id, device_ip, response), "DEBUG")

                interface_data = response.get("response", [])
                if interface_data:
                    self.log("Found {0} interface records for device IP: {1}".format(len(interface_data), device_ip), "DEBUG")
                    interface_info_list.append({
                        "device_ip": device_ip,
                        "interface_details": [interface_data]
                    })
                else:
                    self.log("No interface details found for device IP: {0}".format(device_ip), "DEBUG")
                    interface_info_list.append({
                        "device_ip": device_ip,
                        "interface_details": []
                    })

            except Exception as e:
                self.msg = "Exception occurred while getting device interface info list for device_id {0}, device_ip {1}: {2}".format(device_id, device_ip, e)
                interface_info_list.append({
                    "device_ip": device_ip,
                    "interface_details": "Error: {0}".format(e)
                })
                continue

        result = [{"interface_info": interface_info_list}]

        self.log("Completed Device Interface info retrieval. Total devices processed: {0}".format(len(interface_info_list)), "INFO")
        self.log("Device Interface info result: {0}".format(result), "DEBUG")
        return result

    def get_module_count(self, device_ids):
        """
        Fetch module count details for specified devices from Cisco Catalyst Center.

        For each device ID, this method calls the 'get_device_list' API and aggregates the results.
        Each entry in the returned list contains the device's management IP and its details.

        Retrieves module count information for each device ID provided.

        The retrieved module count includes the key field:
            - module_count_info (int): Number of modules in the device (e.g., 3)

        Parameters:
            device_ids (list): List of device IDs to retrieve module count data for.

        Returns:
            list: A list with a single dictionary:
                [
                    {
                        "module_count_info": [
                            {
                                "device_ip": <str>,
                                "module_count_details": <list of module count details, exception or empty string>
                            },
                        ]
                    }
                ]
        """

        self.log("Fetching module count data for {0} devices: {1}".format(len(device_ids), device_ids), "INFO")
        if not device_ids:
            self.log("No device IDs provided for Module Count info retrieval", "WARNING")
            return [{"module_count_info": []}]

        module_counts_info_list = []

        for device_id in device_ids:
            device_ip = self.get_device_ip_from_id(device_id)
            self.log("Processing device ID: {0} (IP: {1})".format(device_id, device_ip), "DEBUG")
            self.log("Fetching module count info for device_id: {0}, device_ip: {1}".format(device_id, device_ip), "DEBUG")

            try:
                response = self.dnac._exec(
                    family="devices",
                    function="get_module_count",
                    params={'device_id': device_id}
                )
                self.log(
                    "Received API response from 'get_module_count' for device {0} (IP: {1}): {2}".format(
                        device_id, device_ip, response), "DEBUG")

                module_count_data = response.get("response", [])

                if module_count_data:
                    self.log("Found {0} module count records for device IP: {1}".format(module_count_data, device_ip), "DEBUG")
                    module_counts_info_list.append({
                        "device_ip": device_ip,
                        "module_count_details": [module_count_data]
                    })
                else:
                    self.log("No module count details found for device IP: {0}".format(device_ip), "DEBUG")
                    module_counts_info_list.append({
                        "device_ip": device_ip,
                        "module_count_details": []
                    })

            except Exception as e:
                self.msg = "Exception occurred while getting module count info list for device_id {0}, device_ip {1}: {2}".format(device_id, device_ip, e)
                module_counts_info_list.append({
                    "device_ip": device_ip,
                    "module_count_details": "Error: {0}".format(e)
                })
                continue

        result = [{"module_count_info": module_counts_info_list}]

        self.log("Completed Device Module Count info retrieval. Total devices processed: {0}".format(len(module_counts_info_list)), "INFO")
        self.log("Device Module Count info result: {0}".format(result), "DEBUG")
        return result

    def get_interface_ids_per_device(self, device_ids):
        """
        Fetch interface UUIDs for a list of device IDs.

        Retrieves interface data for each device using the 'get_interface_info_by_id' API,
        extracts 'instanceUuid' values, and maps them to their respective device IDs.

        Parameters:
            device_ids (list): List of device UUIDs to fetch interface information for.

        Returns:
            dict: A dictionary with each device ID as the key and a set of its interface UUIDs as the value.
                Example: { "device_id_1": {"uuid1", "uuid2"}}
                Returns an empty dict if no interfaces are found or on failure.
        """
        self.log("Starting interface ID fetch per device", "INFO")

        device_interfaces_map = {}

        for device_id in device_ids:
            try:
                self.log("Fetching interfaces for device_id: {0}".format(device_id), "DEBUG")

                response = self.dnac._exec(
                    family="devices",
                    function="get_interface_info_by_id",
                    params={"device_id": device_id}
                )
                self.log(
                    "Received API response from 'get_interface_ids_per_device' for device {0}: {1}".format(
                        device_id, response), "DEBUG")

                interfaces = response.get("response", [])
                self.log("Found interfaces {0} for device_id: {1}".format(interfaces, device_id), "DEBUG")

                interface_ids = set()
                for interface in interfaces:
                    interface_uuid = interface.get("instanceUuid")
                    if interface_uuid:
                        interface_ids.add(interface_uuid)
                    else:
                        self.log("Skipping interface with no instanceUuid for device {0}".format(device_id), "WARNING")

                device_interfaces_map[device_id] = interface_ids

            except Exception as e:
                self.log("Failed to retrieve interfaces for device_id {0}: {1}".format(device_id, str(e)), "ERROR")

        return device_interfaces_map

    def get_connected_device_details_from_interfaces(self, device_ids):
        """
        Fetch connected device details for all interfaces of the given device UUIDs.

        For each device, retrieves interface UUIDs, then fetches connected device details
        for each interface. Aggregates and returns all connected device details grouped by device.

        The retrieved connected device details include key fields such as:
        - neighborDevice (str): Name of the neighboring device (e.g., "DC-T-9300")
        - neighborPort (str): Port on the neighboring device (e.g., "TenGigabitEthernet1/1/8")
        - capabilities (list): List of capabilities supported by the neighbor device
        (e.g., ["IGMP_CONDITIONAL_FILTERING", "ROUTER", "SWITCH"])

        Parameters:
            device_ids (list): List of device UUIDs to query connected device details for.

        Returns:
            list: A list with a single dictionary:
                [
                    {
                        "connected_device_info": [
                            {
                                "device_ip": <str>,
                                "connected_device_details": <list of connected device detail dictionaries, exception or empty string>
                            },
                        ]
                    }
                ]
        """

        self.log("Fetching connected device data for {0} devices: {1}".format(len(device_ids), device_ids), "INFO")
        if not device_ids:
            self.log("No device IDs provided for Connected Device info retrieval", "WARNING")
            return [{"connected_device_info": []}]

        connected_info_list = []
        device_interfaces_map = self.get_interface_ids_per_device(device_ids)

        for device_id, interface_ids in device_interfaces_map.items():
            connected_device_details = []
            device_ip = self.get_device_ip_from_id(device_id)
            self.log("Processing device ID: {0} (IP: {1})".format(device_id, device_ip), "DEBUG")
            self.log("Fetching connected device info for device_id: {0}, device_ip: {1}".format(device_id, device_ip), "DEBUG")

            for interface_uuid in interface_ids:
                try:
                    connected_response = self.dnac._exec(
                        family="devices",
                        function="get_connected_device_detail",
                        params={
                            "device_uuid": device_id,
                            "interface_uuid": interface_uuid
                        }
                    )
                    self.log(
                        "Received API response from 'get_connected_device_details_from_interfaces' for device {0} (IP: {1}): {2}".format(
                            device_id, device_ip, connected_response), "DEBUG")

                    detail = connected_response.get("response", {})
                    if detail:
                        self.log("Connected data for device {0} and interface {1}: {2}".format(
                            device_id, interface_uuid, detail
                        ), "DEBUG")

                        if isinstance(detail, list):
                            connected_device_details.extend(detail)
                        else:
                            connected_device_details.append(detail)

                    if connected_device_details:
                        self.log("Found {0} connected device details for device IP: {1}".format(
                            len(connected_device_details), device_ip), "DEBUG")
                        connected_info_list.append({
                            "device_ip": device_ip,
                            "connected_device_details": connected_device_details
                        })
                    else:
                        self.log("No connected device details found for device ip: {0}".format(device_ip), "INFO")
                        connected_info_list.append({
                            "device_ip": device_ip,
                            "connected_device_details": []
                        })

                except Exception as e:
                    self.log("Failed to fetch connected device detail for device_id {0} interface_id {1}: {2}".format(
                        device_id, interface_uuid, str(e)
                    ), "ERROR")
                    connected_device_details.append({
                        "device_ip": device_ip,
                        "connected_device_details": "Error: {0}".format(e)
                    })
                    continue

        result = [{"connected_device_info": connected_info_list}]

        self.log("Completed Connected Device info retrieval. Total devices processed: {0}".format(len(connected_info_list)), "INFO")
        self.log("Connected Device info result: {0}".format(result), "DEBUG")
        return result

    def get_interfaces_by_specified_range(self, device_ids):
        """
        Fetch interfaces by specified range details for specified devices from Cisco Catalyst Center.

        Retrieves interface details for a list of device UUIDs using the
        'Get Device Interfaces by Specified Range' API with default values.
        The API is called with a default range of start_index = 1 and
        records_to_return = 500 for each device.

        The retrieved interface details include key fields such as:
        - addresses (list): List of interface IP addresses (usually empty or detailed IPs)
        - adminStatus (str): Administrative status (e.g., "UP")
        - duplex (str): Duplex mode (e.g., "FullDuplex")
        - ifIndex (str): Interface index identifier (e.g., "73")
        - interfaceType (str): Type of interface (e.g., "Physical")
        - lastOutgoingPacketTime (int): Timestamp of last outgoing packet (epoch ms)
        - macAddress (str): MAC address of the interface (e.g., "0c:75:bd:42:db:c1")
        - mtu (str): Maximum Transmission Unit size (e.g., "9100")
        - nativeVlanId (str): Native VLAN ID (e.g., "1")
        - pid (str): Platform ID (e.g., "C9300-48UXM")
        - portMode (str): Port mode (e.g., "access")
        - portName (str): Name of the port (e.g., "AppGigabitEthernet1/0/1")
        - portType (str): Type of port (e.g., "Ethernet Port")
        - serialNo (str): Serial number of the device (e.g., "FJC2335S09F")
        - series (str): Device series (e.g., "Cisco Catalyst 9300 Series Switches")
        - speed (str): Speed in kbps (e.g., "1000000")
        - status (str): Operational status (e.g., "up")
        - vlanId (str): VLAN ID assigned (e.g., "1")
        - voiceVlan (str): Voice VLAN (usually empty)
        - description (str): Interface description (usually empty)
        - instanceUuid (str): Interface instance UUID
        - instanceTenantId (str): Tenant ID for the instance

        Parameters:
            device_ids (list): List of device instance UUIDs for which interface
                               details need to be fetched.

        Returns:
            list: A list with a single dictionary:
                [
                    {
                        "connected_device_info": [
                            {
                                "device_ip": <str>,
                                "connected_device_details": <list of connected device detail dictionaries, exception or empty string>
                            },
                        ]
                    }
                ]
        """

        self.log("Fetching range interface data for {0} devices: {1}".format(len(device_ids), device_ids), "INFO")
        if not device_ids:
            self.log("No device IDs provided for Interface by Range info retrieval", "WARNING")
            return [{"device_interfaces_by_range_info": []}]

        interface_by_range_info_list = []

        for device_id in device_ids:
            device_ip = self.get_device_ip_from_id(device_id)
            start_index = 1
            records_to_return = 500
            interface_data = []

            while True:
                self.log("Fetching interfaces for device {0} - starting at index {1} (requesting {2} records)".format(
                    device_id, start_index, records_to_return), "DEBUG")
                try:
                    response = self.dnac._exec(
                        family="devices",
                        function="get_device_interfaces_by_specified_range",
                        params={
                            "device_id": device_id,
                            "start_index": start_index,
                            "records_to_return": records_to_return
                        }
                    )

                    self.log("Received API response from 'get_device_interfaces_by_specified_range': {0}".format(
                        response), "DEBUG"
                    )

                    if not response or 'response' not in response:
                        self.log("Empty or invalid response received for device_id: {0}".format(device_id), "WARNING")
                        break

                    data_chunk = response['response']
                    if data_chunk:
                        self.log("Found {0} interface records for device IP: {1}".format(len(data_chunk), device_ip), "DEBUG")
                        interface_data.extend(data_chunk)
                    else:
                        self.log("No interface details found for device IP: {0}".format(device_ip), "DEBUG")
                        break

                    if len(data_chunk) < records_to_return:
                        self.log("Reached end of data - received {0} records (less than requested {1})".format(
                            len(data_chunk), records_to_return), "DEBUG")
                        break

                    start_index += records_to_return

                except Exception as api_err:
                    self.log("Exception while calling get_device_interfaces_by_specified_range for device_id {0} due to {1}".format(device_id, api_err)
                             , "ERROR")
                    interface_data = ["Error: {0}".format(api_err)]
                    break

            self.log("No interface info found for device ip: {0}".format(device_ip), "INFO")
            interface_by_range_info_list.append({
                "device_ip": device_ip,
                "interface_info": [interface_data] if interface_data else []
            })

        result = [{"device_interfaces_by_range_info": interface_by_range_info_list}]

        self.log("Completed Device Interface by Range info retrieval. Total devices processed: {0}".format(len(interface_by_range_info_list)), "INFO")
        self.log("Device Interface by Range info result: {0}".format(result), "DEBUG")

        return result

    def get_device_link_mismatch_by_sites(self, site_ids, device_ids):
        """
        Fetch Inventory Insight Device Link Mismatch data for a list of site IDs.

        Retrieves mismatch data for both 'vlan' and 'speed-duplex' categories for each site.
        Aggregates all results and returns them in a structured list.

        The retrieved device link mismatch data includes key fields such as:
        - endPortAllowedVlanIds (str): Allowed VLAN IDs on the end port (e.g., "10,20,30")
        - endPortNativeVlanId (str): Native VLAN ID on the end port (e.g., "10")
        - startPortAllowedVlanIds (str): Allowed VLAN IDs on the start port (e.g., "10,20,30")
        - startPortNativeVlanId (str): Native VLAN ID on the start port (e.g., "10")
        - linkStatus (str): Current status of the link (e.g., "up")
        - endDeviceHostName (str): Hostname of the device at the end port (e.g., "switch-nyc-01")
        - endDeviceId (str): Unique ID of the device at the end port (e.g., "device-1001")
        - endDeviceIpAddress (str): IP address of the device at the end port (e.g., "192.168.1.10")
        - endPortAddress (str): Interface address of the end port (e.g., "GigabitEthernet1/0/24")
        - endPortDuplex (str): Duplex setting of the end port (e.g., "full")
        - endPortSpeed (str): Speed setting of the end port (e.g., "1000Mbps")
        - startDeviceHostName (str): Hostname of the device at the start port (e.g., "router-dc-01")
        - startDeviceId (str): Unique ID of the device at the start port (e.g., "device-2001")
        - startDeviceIpAddress (str): IP address of the device at the start port (e.g., "192.168.1.1")
        - startPortAddress (str): Interface address of the start port (e.g., "GigabitEthernet0/1")
        - startPortDuplex (str): Duplex setting of the start port (e.g., "full")
        - startPortSpeed (str): Speed setting of the start port (e.g., "1000Mbps")
        - lastUpdated (str): ISO 8601 timestamp of last update (e.g., "2025-06-26T10:15:00Z")
        - numUpdates (int): Number of updates recorded (e.g., 15)
        - avgUpdateFrequency (float): Average frequency of updates (e.g., 4.0)
        - type (str): Type of link (e.g., "ethernet-link")
        - instanceUuid (str): Unique instance UUID

        Parameters:
            site_ids (list): List of site IDs to fetch device link mismatch information.

        Returns:
        list: A list containing a single dictionary with structure:
            [
                {
                    "device_link_mismatch_info": [
                        {
                            "device_ip": "<device_management_ip>",
                            "vlan": [
                                {
                                    "device_ip": "<device_ip>",
                                    "link_mismatch_details": <list_of_vlan_mismatch_data_or_error_message>
                                }
                            ],
                            "speed-duplex": [
                                {
                                    "device_ip": "<device_ip>",
                                    "link_mismatch_details": <list of speed duplex mismatch data, exception or empty string>
                                }
                            ]
                        },
                    ]
                }
            ]
        """

        self.log("Fetching device link mismatch data for {0} devices: {1}".format(len(device_ids), device_ids), "INFO")
        if not site_ids or not device_ids:
            self.log("No site IDs or device IDs provided for Device Link Mismatch info retrieval", "WARNING")
            return [{"device_link_mismatch_info": []}]

        link_mismatch_info = []
        device_ips = []
        self.log(site_ids)
        for site_id in site_ids:
            for device_id in device_ids:
                if not site_id:
                    self.msg = "Invalid or missing site ID in site_ids list."
                    continue
                device_ip = self.get_device_ip_from_id(device_id)
                device_ips.append(device_ip)

                site_result = {
                    "device_ip": device_ip,
                    "vlan": [],
                    "speed-duplex": []
                }

                for category in ['vlan', 'speed-duplex']:
                    self.log("Processing device ID: {0} (IP: {1})".format(device_id, device_ip), "DEBUG")
                    self.log("Fetching device link mismatch info for device_id: {0}, device_ip: {1}".format(device_id, device_ip), "DEBUG")

                    try:
                        response = self.dnac._exec(
                            family="devices",
                            function="inventory_insight_device_link_mismatch",
                            params={
                                'site_id': site_id,
                                'category': category
                            }
                        )
                        self.log(
                            "Received API response from 'inventory_insight_device_link_mismatch': {0}".format(
                                (response)
                            ),
                            "DEBUG",
                        )
                        mismatch_data = response.get("response", [])
                        if mismatch_data:
                            self.log(
                                "Received API response for device {0}: {1}".format(device_ip, mismatch_data),
                                "DEBUG"
                            )
                            if isinstance(mismatch_data, list):
                                site_result[category].append({
                                    "device_ip": device_ip,
                                    "link_mismatch_details": mismatch_data
                                })

                        else:
                            self.log("No link mismatch found for device IP: {0}".format(device_ip), "DEBUG")
                            site_result[category].append({
                                "device_ip": device_ip,
                                "link_mismatch_details": []
                            })

                        if category == 'vlan':
                            self.log("VLAN Category Link Mismatch Response for site {0}: {1}".format(site_id, response), "INFO")
                        else:
                            self.log("Speed-Duplex Category Link Mismatch Response for site {0}: {1}".format(site_id, response), "INFO")

                    except Exception as e:
                        self.msg = "Exception occurred while getting {0} link mismatch data for site {1}: {2}".format(category, site_id, e)
                        site_result[category].append({
                            "device_ip": device_ip,
                            "link_mismatch_details": "Error: {0}".format(e)
                        })
                        continue

                self.log(site_result["vlan"])
                self.log(site_result["speed-duplex"])
                link_mismatch_info.append(site_result)

        result = [{"device_link_mismatch_info": link_mismatch_info}]

        self.log("Completed Device Link Mismatch info retrieval. Total devices processed: {0}".format(len(link_mismatch_info)), "INFO")
        self.log("Device Link Mismatch info result: {0}".format(result), "DEBUG")

        return result

    def get_device_id(self, filtered_config):
        """
        Retrieve and aggregate unique device instance UUIDs based on comprehensive filtering criteria.

        This method performs intelligent device discovery across Cisco Catalyst Center using multiple
        filter strategies including device attributes and site hierarchy lookups. It implements robust
        retry mechanisms, timeout handling, and comprehensive logging to ensure reliable device
        identification even in large-scale network environments.

        The method supports two primary discovery strategies:
        1. Attribute-based filtering: Searches devices by specific attributes like IP, MAC, hostname, etc.
        2. Site-based filtering: Discovers devices associated with specific network sites

        Parameters:
            device_filter_configuration (dict): Comprehensive filtering configuration containing:
                Device Attribute Filters:
                - 'management_ip_address' (list of str): Management IP addresses for device lookup
                - 'mac_address' (list of str): MAC addresses for device identification
                - 'hostname' (list of str): Device hostnames for name-based discovery
                - 'serial_number' (list of str): Serial numbers for hardware-based identification
                - 'software_type' (list of str): Software types (e.g., 'IOS-XE', 'NX-OS')
                - 'software_version' (list of str): Specific software versions for filtering
                - 'role' (list of str): Device roles (e.g., 'ACCESS', 'CORE', 'DISTRIBUTION')
                - 'device_type' (list of str): Device types (e.g., 'Cisco Catalyst 9300 Switch')
                - 'family' (list of str): Device families (e.g., 'Switches and Hubs', 'Routers')
                - 'site_hierarchy' (list of str): Site hierarchy paths for location-based filtering

                Operation Control Parameters:
                - 'timeout' (int, optional): Maximum time in seconds for device discovery operations.
                                        Default: 60 seconds
                - 'retries' (int, optional): Number of retry attempts for failed API calls.
                                        Default: 3 retries
                - 'interval' (int, optional): Wait interval in seconds between retry attempts.
                                            Default: 10 seconds

        Returns:
            list of str: Unique device instance UUIDs matching the specified filter criteria.
                        Each UUID represents a distinct network device in Cisco Catalyst Center.
                        Returns empty list if no devices match the criteria.
                        Returns None if a critical exception prevents processing.

        Raises:
            APIError: When Cisco Catalyst Center API returns error responses
            TimeoutError: When device discovery operations exceed configured timeout
            ValidationError: When invalid filter configuration is provided
        """

        param_keys = [
            'management_ip_address', 'mac_address', 'hostname', 'serial_number',
            'os_type', 'software_version', 'role', 'device_type', 'family'
        ]

        api_parameter_mapping = {
            'management_ip_address': 'managementIpAddress',
            'mac_address': 'macAddress',
            'hostname': 'hostname',
            'serial_number': 'serialNumber',
            'os_type': 'softwareType',
            'software_version': 'softwareVersion',
            'role': 'role',
            'device_type': 'type',
            'family': 'family',
        }

        all_info_results = []
        device_ids = []

        timeout = filtered_config.get("timeout", 60)
        retries = filtered_config.get("retries", 3)
        interval = filtered_config.get("interval", 10)

        for key in param_keys:
            values = filtered_config.get(key, [])
            if not isinstance(values, list) or len(values) == 0:
                self.log("Skipping {0} as it is empty list".format(key), "INFO")
                continue

            self.log("Processing {0} with values: {1}".format(key, values), "INFO")
            for val in values:
                params = {api_parameter_mapping[key]: val}
                start_time = time.time()
                attempt = 0
                self.log("Calling API with params: {0}".format(params))

                while attempt < retries and (time.time() - start_time) < timeout:
                    params = {api_parameter_mapping[key]: val}
                    self.log("Attempt {0} - Calling API with params: {1}".format(attempt + 1, params))

                    response = self.dnac._exec(
                        family="devices",
                        function="get_device_list",
                        params=params
                    )
                    self.log(
                        "Received API response for device_id {0}: {1}".format(device_ids, response), "DEBUG",)

                    devices = response.get('response', [])
                    if devices:
                        for device in devices:
                            uuid = device.get('instanceUuid')
                            if uuid:
                                device_ids.append(uuid)
                        break
                    else:
                        self.log("No device response found, retrying in {0} seconds...".format(interval))
                        attempt += 1
                        time.sleep(interval)

                else:
                    msg = ("Max retries and timeout reached, No information available for {0} - {1}".format(key, val))
                    self.log(msg)
                    self.total_response.append(msg)

                all_info_results.append(response)

        # Site-based
        site_names = filtered_config.get("site_hierarchy")
        site_ids = []

        if site_names:
            if not isinstance(site_names, list):
                site_names = [site_names]
            for site_name in site_names:
                success, site_id = self.get_site_id(site_name)
                site_ids.append((success, site_id, site_name))

            for success, site_id, site_name in site_ids:
                if success and site_id:
                    response, site_device_ids = self.get_device_ids_from_site(site_name=None, site_id=site_id)

                    self.log("Devices from site {0}: {1}".format(site_id, site_device_ids), "INFO")
                    device_ids.extend(site_device_ids)

        unique_device_ids = list(set(device_ids))
        self.log("Collected device instance UUIDs: {0}".format(device_ids), "INFO")
        self.log("Collected unique device instance UUIDs: {0}".format(unique_device_ids), "INFO")
        return unique_device_ids

    def get_device_ip_from_id(self, device_id):
        """
        Retrieve the management IP address of a device from Cisco Catalyst Center using its ID.
        Parameters:
            - self (object): An instance of a class used for interacting with Cisco Catalyst Center.
            - device_id (str): The unique identifier of the device in Cisco Catalyst Center.
        Returns:
            str: The management IP address of the specified device.

        Description:
            This method queries Cisco Catalyst Center for the device details based on its unique identifier (ID).
            It uses the 'get_device_list' function in the 'devices' family, extracts the management IP address
            from the response, and returns it. If any error occurs during the process, an exception is raised
            with an appropriate error message logged.
        Raises:
            Exception: If there is a critical error during API communication with Cisco Catalyst Center,
              invalid device UUID format, or authentication/authorization failures.
        """

        try:
            response = self.dnac._exec(
                family="devices",
                function="get_device_list",
                op_modifies=True,
                params={"id": device_id},
            )
            self.log(
                "Received API response from 'get_device_list': {0}".format(
                    str(response)
                ),
                "DEBUG",
            )
            response = response.get("response")[0]
            device_ip = response.get("managementIpAddress")

            return device_ip
        except Exception as e:
            error_message = "Error occurred while getting the response of device from Cisco Catalyst Center: {0}".format(
                str(e)
            )
            self.set_operation_result("failed", False, error_message, "ERROR").check_return_status()

    def write_device_info_to_file(self, config):
        """
        Write collected network device information to a specified file with comprehensive format support and error handling.

        This method provides robust file output capabilities for network device data with support for multiple
        formats (JSON/YAML), file modes (overwrite/append), automatic directory creation, timestamp insertion,
        and comprehensive error handling with detailed logging for operational traceability.

        Parameters:
            export_configuration (dict): Configuration dictionary containing file output specifications.
                Required structure:
                {
                    "output_file_info": {
                        "file_path": str,   # Absolute path without extension (required)
                        "file_format": str, # "json" or "yaml" (default: "yaml")
                        "file_mode": str,   # "w" (overwrite) or "a" (append) (default: "w")
                        "timestamp": bool   # Include download timestamp (default: False)
                    },
                    "data": dict            # Optional: specific data to write (uses self.total_response if not provided)
                }

        Returns:
            self: The current instance with updated internal state reflecting the file operation results.

        Raises:
            Exception: Critical errors during file operations, directory creation, or data serialization
                  are logged but do not raise exceptions to maintain operational continuity.
        """

        self.log("=== Starting Device Information File Export Operation ===", "INFO")

        output_file_info = config.get("output_file_info", {})
        self.log("File info received: {0}".format(output_file_info), "DEBUG")

        target_file_path = output_file_info.get("file_path")
        output_file_format = output_file_info.get("file_format", "yaml").lower().strip()
        file_write_mode = output_file_info.get("file_mode", "w").lower().strip()
        include_timestamp_flag = output_file_info.get("timestamp", False)

        self.log("Extracted file parameters - Path: {0}, Format: {1}, Mode: {2}, Timestamp: {3}".format(
            target_file_path, output_file_format, file_write_mode, include_timestamp_flag), "INFO")

        if not target_file_path:
            self.log("No file_path specified in output_file_info", "ERROR")
            return self

        if file_write_mode not in {"w", "a"}:
            self.log("Invalid file_mode '{0}'. Use 'w' (overwrite) or 'a' (append).".format(file_write_mode), "ERROR")
            return self

        full_path_with_ext = "{0}.{1}".format(target_file_path, output_file_format)

        try:
            os.makedirs(os.path.dirname(full_path_with_ext), exist_ok=True)
        except Exception as e:
            self.log("Error creating directories for path: {0} — {1}".format(full_path_with_ext, e), "ERROR")
            return self

        try:
            if isinstance(self.total_response, list):
                new_data = self.total_response[:]
            else:
                new_data = [self.total_response]

            if include_timestamp_flag:
                timestamp_entry = {"Downloaded at": datetime.now().strftime("%Y-%m-%d %H:%M:%S")}
                new_data_with_timestamp = [timestamp_entry] + new_data
            else:
                new_data_with_timestamp = new_data

            if file_write_mode == "a" and os.path.exists(full_path_with_ext):
                try:
                    with open(full_path_with_ext, "r") as f:
                        if output_file_format == "json":
                            existing_data = json.load(f)
                        else:
                            existing_data = yaml.safe_load(f)

                        if existing_data is None:
                            existing_data = []
                        elif not isinstance(existing_data, list):
                            existing_data = [existing_data]

                except Exception:
                    self.log("Failed to read existing file. Starting fresh.", "WARNING")
                    existing_data = []

                data_to_write = existing_data + new_data_with_timestamp

            else:
                data_to_write = new_data_with_timestamp

            with open(full_path_with_ext, "w") as f:
                if output_file_format == "json":
                    json.dump(data_to_write, f, indent=2)
                else:
                    yaml.dump(data_to_write, f, default_flow_style=False)

            self.log("Successfully wrote device info to file: {0}".format(full_path_with_ext), "INFO")

        except Exception as e:
            self.log("Failed to write device info to file {0}: {1}".format(full_path_with_ext, e), "ERROR")

        return self


def main():
    """
    main entry point for module execution
    """
    element_spec = {'dnac_host': {'required': True, 'type': 'str'},
                    'dnac_port': {'type': 'str', 'default': '443'},
                    'dnac_username': {'type': 'str', 'default': 'admin', 'aliases': ['user']},
                    'dnac_password': {'type': 'str', 'no_log': True},
                    'dnac_verify': {'type': 'bool', 'default': True},
                    'dnac_version': {'type': 'str', 'default': '2.2.3.3'},
                    'dnac_debug': {'type': 'bool', 'default': False},
                    'dnac_log_level': {'type': 'str', 'default': 'WARNING'},
                    "dnac_log_file_path": {"type": 'str', "default": 'dnac.log'},
                    "dnac_log_append": {"type": 'bool', "default": True},
                    'dnac_log': {'type': 'bool', 'default': False},
                    'validate_response_schema': {'type': 'bool', 'default': True},
                    'config_verify': {'type': 'bool', "default": False},
                    'dnac_api_task_timeout': {'type': 'int', "default": 1200},
                    'dnac_task_poll_interval': {'type': 'int', "default": 2},
                    'config': {'required': True, 'type': 'list', 'elements': 'dict'},
                    'state': {'default': 'queried', 'choices': ['queried']}
                    }

    module = AnsibleModule(argument_spec=element_spec, supports_check_mode=False)
    ccc_device_info = NetworkDevicesInfo(module)
    state = ccc_device_info.params.get("state")

    current_version = ccc_device_info.get_ccc_version()
    min_supported_version = "2.3.7.6"

    if ccc_device_info.compare_dnac_versions(current_version, min_supported_version) < 0:
        ccc_device_info.status = "failed"
        ccc_device_info.msg = (
            "The specified version '{0}' does not support the 'network device info workflow' feature. "
            "Supported version(s) start from '{1}' onwards.".format(current_version, min_supported_version)
        )
        ccc_device_info.log(ccc_device_info.msg, "ERROR")
        ccc_device_info.check_return_status()

    if state not in ccc_device_info.supported_states:
        ccc_device_info.status = "invalid"
        ccc_device_info.msg = "State {0} is invalid".format(state)
        ccc_device_info.check_return_status()

    ccc_device_info.validate_input().check_return_status()

    for config in ccc_device_info.validated_config:
        ccc_device_info.reset_values()
        ccc_device_info.get_want(config).check_return_status()
        ccc_device_info.get_diff_state_apply[state](config).check_return_status()

    module.exit_json(**ccc_device_info.result)


if __name__ == '__main__':
    main()
