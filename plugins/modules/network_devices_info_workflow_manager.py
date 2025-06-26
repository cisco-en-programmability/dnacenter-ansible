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
short_description: >
  The Module will let user specify the filters to be used to query the devices, and it will return the information
  about the devices that match the filters from Cisco Catalyst Center.

description:
  - Queries Cisco Catalyst Center to retrieve information about network devices.
  - Returns device details found within the specified timeout and retry intervals.
  - Returns an empty list if no devices are found after exhausting retries.

version_added: "6.31.0"
extends_documentation_fragment:
  - cisco.dnac.workflow_manager_params
author:
  - Madhan Sankaranarayanan (@madhansansel)

options:
  config_verify:
    description: Set to True to verify the Cisco Catalyst Center after applying the playbook config.
    type: bool
    default: True
  state:
    description: The desired state of the configuration after module execution.
    type: str
    choices: ["queried"]
    default: queried
  config:
    description: A list of dictionaries containing network device details.
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
                    - List of management IP addresses of the devices.
                    - Each IP address must be unique to identify the device.
                type: list
                elements: str
            mac_address:
                description:
                    - List of MAC addresses of the devices.
                    - Each MAC address must be unique to identify the device.
                type: list
                elements: str
            hostname:
                description:
                    - List of hostnames of the devices.
                    - Each hostname must be unique to identify the device.
                type: list
                elements: str
            serial_number:
                description:
                    - List of serial numbers of the devices.
                    - Each serial number must be unique to identify the device.
                type: list
                elements: str
            software_type:
                description:
                    - List of software types for which the devices have to be retrieved (e.g., IOS-XE).
                type: list
                elements: str
            software_version:
                description:
                    - List of software versions for which the devices have to be retrieved.
                type: list
                elements: str
            role:
                description:
                    - List containing roles of the devices to retrieve devices matching the specified roles (e.g., ACCESS, CORE).
                type: list
                elements: str
            device_type:
                description:
                    - List specifying device types to retrieve devices matching the specified types (e.g., Cisco Catalyst 9300 Switch).
                type: list
                elements: str
            family:
                description:
                    - List specifying device families to retrieve devices belonging to the specified families (e.g., Switches and Hubs).
                type: list
                elements: str
            site_hierarchy:
                description:
                    - List specifying site hierarchies to retrieve devices associated with the specified sites.
                type: list
                elements: str
            timeout:
                description:
                    - Time to wait for the devices to be found (in sec).
                    - Default value is 60 seconds if not specified.
                type: int
                default: 60
            retries:
                description:
                    - Number of times to retry the query if the devices are not found.
                    - Default value is 3 retries if not specified.
                type: int
                default: 3
            interval:
                description:
                    - The time to wait between retries, in seconds.
                    - Default value is 10 seconds if not specified.
                type: int
                default: 10
            output_file_path:
                description:
                    - The full file path where the output data will be saved. (e.g.,/Users/Karthick/Downloads/Info)
                    - The file format is inferred from the file extension (e.g., .json, .xlsx, .pdf).
                    - Default file format is JSON if no other extension is specified.
                    - Ensure the directory exists and the process has write permissions to this path.
                    - Recommended formats depend on usage; JSON for raw data, Excel (.xlsx) for tabular reports, PDF for formatted documents.
                type: str
                required: false
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
                    - all
                    - device_info
                    - interface_info
                    - interface_vlan_info
                    - line_card_info
                    - supervisor_card_info
                    - poe_info
                    - module_count_info
                    - connected_device_info
                    - device_config_info
                    - device_summary_info
                    - device_polling_interval_info
                    - device_stack_info
                    - device_link_mismatch_info

requirements:
    - dnacentersdk >= 2.9.3
    - python >= 3.9.19
notes:
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
---
- name: Get Network devices information on Cisco Catalyst Center
  hosts: localhost
  connection: local
  vars_files:
    - "credentials.yml"
  tasks:
    - name: Get Network devices information on Cisco Catalyst Center
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
        config_verify: true
        dnac_api_task_timeout: 1000
        dnac_task_poll_interval: 1
        state: queried
        config:
          - network_devices:
              - management_ip_address: ["204.1.1.26"] # - list of string
                mac_address: ["d4:ad:bd:c1:67:00"] # - list of string
                hostname: ["DC-FR-9300"] # - list of string
                serial_number: ["FJC2327U0S2"] # - list of string
                software_type: ["IOS-XE"] # - list of string
                software_version: ["17.12.4"] # - list of string
                role: ["ACCESS"] # - list of string
                device_type: ["Cisco Catalyst 9300 Switch" ]
                family: ["Switches and Hubs"] # - list of string
                site_hierarchy: [Global/USA]# - list of string
                timeout: 60    #default: 60sec
                retries: 3    #default: 3
                interval: 10   #default: 10sec
                output_file_path: /Users/karthick/Downloads/info #Default json format
                requested_info:
                  - all
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
"""

RETURN = r"""

#Case 1: Successful Retrieval of Device Info
response_device_info:
    description: Details of the response containing device information for Cisco Catalyst 9300 switches.
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
        config_spec = {
            'network_devices': {
                'type': 'list',
                'elements': 'dict',
                'management_ip_address': {'type': 'list', 'elements': 'str'},
                'mac_address': {'type': 'list', 'elements': 'str'},
                'hostname': {'type': 'list', 'elements': 'str'},
                'serial_number': {'type': 'list', 'elements': 'str'},
                'role': {'type': 'list', 'elements': 'str'},
                'software_type': {'type': 'list', 'elements': 'str'},
                'software_version': {'type': 'list', 'elements': 'str'},
                'site_hierarchy': {'type': 'list', 'elements': 'str'},
                'device_type': {'type': 'list', 'elements': 'str'},
                'family': {'type': 'list', 'elements': 'str'},
                'timeout': {'type': 'int', 'default': 60},
                'retries': {'type': 'int', 'default': 3},
                'interval': {'type': 'int', 'default': 10},
                'output_file_path': {'type': 'str'},
                'requested_info': {
                    'type': 'list',
                    'elements': 'str',
                    'default': [
                        "device_info", "interface_info", "interface_vlan_info",
                        "line_card_info", "supervisor_card_info", "poe_info",
                        "module_count_info", "connected_device_info",
                        "device_interfaces_by_range_info", "device_config_info",
                        "device_summary_info", "device_polling_interval_info",
                        "device_stack_info", "device_link_mismatch_info"
                    ]
                }
            }
        }

        if not self.config:
            self.msg = "Configuration is not available in the playbook for validation"
            self.set_operation_result("failed", False, self.msg, "ERROR")
            return self

        if not isinstance(self.config, list):
            self.msg = "Config should be a list"
            self.set_operation_result("failed", False, self.msg, "ERROR")
            return self

        valid_config, invalid_params = validate_list_of_dicts(
            self.config, config_spec
        )

        if invalid_params:
            self.msg = "Invalid parameters in playbook: {0}".format(invalid_params)
            self.set_operation_result("failed", False, self.msg, "ERROR")
            return self

        if not valid_config:
            self.log("Configuration validation failed: {0}".format(valid_config), "ERROR")
            return self

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
                        "software_type", or "software_version"
                    And:
                        - "requested_info" (dict): Non-empty dictionary specifying which details to retrieve.

        Returns:
            self: The current instance of the class with updated 'want' attribute containing
                the validated and extracted network device configuration.
        """
        DEFAULT_REQUESTED_INFO = [
            "device_info", "interface_info", "interface_vlan_info",
            "line_card_info", "supervisor_card_info", "poe_info",
            "module_count_info", "connected_device_info",
            "device_interfaces_by_range_info", "device_config_info",
            "device_summary_info", "device_polling_interval_info",
            "device_stack_info", "device_link_mismatch_info"
        ]

        want = {}
        want["network_devices"] = config.get("network_devices")
        self.log(config, "DEBUG")
        required_params = ['network_devices']

        if 'network_devices' not in config or not config['network_devices']:
            msg = "Parameter 'network_devices' is mandatory and cannot be empty."
            self.msg = msg
            self.set_operation_result("failed", False, self.msg, "ERROR").check_return_status()

        else:
            required_device_keys = ['management_ip_address', 'mac_address', 'hostname', 'serial_number',
                                    'role', 'software_type', 'software_version', 'site_hierarchy', 'device_type']
            valid_info_options = ["all"] + DEFAULT_REQUESTED_INFO

            device_check_passed = True
            requested_info_check_passed = True

            for device in config['network_devices']:
                if "all" in device.get("requested_info", []):
                    device["requested_info"] = [
                        "device_info", "interface_info", "interface_vlan_info",
                        "line_card_info", "supervisor_card_info", "poe_info",
                        "module_count_info", "connected_device_info",
                        "device_interfaces_by_range_info", "device_config_info",
                        "device_summary_info", "device_polling_interval_info",
                        "device_stack_info", "device_link_mismatch_info"
                    ]

            for device in config['network_devices']:
                if 'requested_info' not in device or not device['requested_info'] or device['requested_info'] == ["all"] or "all" in device['requested_info']:
                    device["requested_info"] = DEFAULT_REQUESTED_INFO.copy()

            for device in config['network_devices']:
                if not any(device.get(key) for key in required_device_keys):
                    device_check_passed = False
                    break

                if 'requested_info' not in device or not isinstance(device['requested_info'], list) or not device['requested_info']:
                    requested_info_check_passed = False
                    break

                # Validate each entry in requested_info
                for info in device['requested_info']:
                    if info not in valid_info_options:
                        self.msg = "'{}' is not a valid option in 'requested_info'.".format(info)
                        self.set_operation_result("failed", False, self.msg, "ERROR").check_return_status()

            if not device_check_passed:
                self.msg = "At least one of the following parameters must be specified inside each network device: {}.".format(", ".join(required_device_keys))
                self.set_operation_result("failed", False, self.msg, "ERROR").check_return_status()
            elif not requested_info_check_passed:
                self.msg = "Parameter 'requested_info' is mandatory and must be a non-empty list inside each network device."
                self.set_operation_result("failed", False, self.msg, "ERROR").check_return_status()

        self.want = want
        self.log("Desired State (want): {0}".format(str(self.want)), "INFO")
        return self

    def get_diff_queried(self, config):
        """
        Process and retrieve requested information for network devices from the provided configuration.

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
        self.log("Starting get_diff_queried with provided config", "INFO")
        network_device_details = config.get("network_devices")

        for config in network_device_details:
            filtered_config = {}
            for key, value in config.items():
                if key != "requested_info":
                    filtered_config[key] = value
            self.log("Filtered config (excluding requested_info): {}".format(filtered_config))

            DEFAULT_REQUESTED_INFO = [
                "device_info", "interface_info", "interface_vlan_info",
                "line_card_info", "supervisor_card_info", "poe_info",
                "module_count_info", "connected_device_info",
                "device_interfaces_by_range_info", "device_config_info",
                "device_summary_info", "device_polling_interval_info",
                "device_stack_info", "device_link_mismatch_info"
            ]

            requested_info = config.get("requested_info", [])
            if not requested_info or requested_info == ["all"] or "all" in requested_info:
                requested_info = DEFAULT_REQUESTED_INFO.copy()

            device_ids = self.get_device_id(filtered_config)
            output_path = config.get("output_file_path")
            combined_data = {}

            if "device_info" in requested_info:
                result = self.get_device_info(device_ids)
                self.total_response.append(result)
                combined_data["device_info"] = result
            if "interface_info" in requested_info:
                result = self.get_interface_info(device_ids)
                self.total_response.append(result)
                combined_data["interface_info"] = result
            if "interface_vlan_info" in requested_info:
                result = self.get_device_interface_vlans(device_ids)
                self.total_response.append(result)
                combined_data["interface_vlan_info"] = result
            if "line_card_info" in requested_info:
                result = self.get_linecard_details(device_ids)
                self.total_response.append(result)
                combined_data["line_card_info"] = result
            if "supervisor_card_info" in requested_info:
                result = self.get_supervisor_card_detail(device_ids)
                self.total_response.append(result)
                combined_data["supervisor_card_info"] = result
            if "poe_info" in requested_info:
                result = self.get_poe_details(device_ids)
                self.total_response.append(result)
                combined_data["poe_info"] = result
            if "module_count_info" in requested_info:
                result = self.get_module_count(device_ids)
                self.total_response.append(result)
                combined_data["module_count_info"] = result
            if "connected_device_info" in requested_info:
                result = self.get_connected_device_details_from_interfaces(device_ids)
                self.total_response.append(result)
                combined_data["connected_device_info"] = result
            if "device_interfaces_by_range_info" in requested_info:
                result = self.get_interfaces_by_specified_range(device_ids)
                self.total_response.append(result)
                combined_data["device_interfaces_by_range_info"] = result
            if "device_config_info" in requested_info:
                result = self.get_device_config(device_ids)
                self.total_response.append(result)
                combined_data["device_config_info"] = result
            if "device_summary_info" in requested_info:
                result = self.get_device_summary(device_ids)
                self.total_response.append(result)
                combined_data["device_summary_info"] = result
            if "device_polling_interval_info" in requested_info:
                result = self.get_polling_interval(device_ids)
                self.total_response.append(result)
                combined_data["device_polling_interval_info"] = result
            if "device_stack_info" in requested_info:
                result = self.get_stack_details(device_ids)
                self.total_response.append(result)
                combined_data["device_stack_info"] = result
            if "device_link_mismatch_info" in requested_info:
                result = self.get_device_link_mismatch_by_sites(device_ids)
                self.total_response.append(result)
                combined_data["device_link_mismatch_info"] = result

            # Save to file if output_file_path is given
            if output_path:
                result = save_device_response_to_file(output_path, combined_data, self.log)
                if result["status"] == "failed":
                    self.log("Failed to save response to {}: {}".format(output_path, result["error"]), "ERROR")

        if self.total_response:
            self.msg = self.total_response
            self.set_operation_result("success", False, self.msg, "INFO")

        return self

    def get_device_info(self, device_ids):
        """
        Fetch detailed information for a list of network devices from Cisco Catalyst Center.

        Executes API calls for each device ID and aggregates the retrieved data into a structured list.

        Parameters:
            device_ids (list): List of device UUIDs whose information needs to be fetched.

        Returns:
            list: A list containing a single dictionary with key "device_info" and a list of device data as value.
                Returns None if an exception occurs during the API call.
        """

        self.log("Fetching device data for: {0}".format(device_ids), "INFO")

        all_devices = []

        for device_id in device_ids:
            try:
                response = self.dnac._exec(
                    family="devices",
                    function="get_device_list",
                    params={'id': device_id}
                )
                devices = response.get("response", [])
                if isinstance(devices, list):
                    all_devices.extend(devices)
                else:
                    all_devices.append(devices)

            except Exception as e:
                self.msg = "Exception occurred while getting device list: {0}".format(e)
                self.log(self.msg, "ERROR")
                self.set_operation_result("failed", False, self.msg, "ERROR")
                return None

        result = [{"device_info": all_devices}]

        self.log("Retrieved {0} device records".format(result), "DEBUG")
        return result

    def get_device_interface_vlans(self, device_ids):
        """
        Fetch VLAN interface details for a list of devices from Cisco Catalyst Center.

        Queries the VLAN interface configuration for each device ID and aggregates the results.

        Parameters:
            device_ids (list): List of device UUIDs for which VLAN interface data needs to be fetched.

        Returns:
            list: A list containing a single dictionary with key "interface_vlan_info" and the aggregated VLAN data as value.
                Returns None if an exception occurs during the API call.
        """

        self.log("Fetching VLAN interface data for devices: {0}".format(device_ids), "INFO")

        all_vlans = []

        for device_id in device_ids:
            try:
                response = self.dnac._exec(
                    family="devices",
                    function="get_device_interface_vlans",
                    params={'id': device_id}
                )
                vlan_data = response.get("response", [])
                if isinstance(vlan_data, list):
                    all_vlans.extend(vlan_data)
                else:
                    all_vlans.append(vlan_data)

            except Exception as e:
                self.msg = "Exception occurred while getting VLAN interface data: {0}".format(e)
                self.log(self.msg, "ERROR")
                self.set_operation_result("failed", False, self.msg, "ERROR")
                return None

        result = [{"interface_vlan_info": all_vlans}]

        self.log("Retrieved {0} VLAN records".format(all_vlans), "DEBUG")
        return result

    def get_linecard_details(self, device_ids):
        """
        Fetch line card details for a list of devices from Cisco Catalyst Center.

        Queries and aggregates line card information for each provided device ID.

        Parameters:
            device_ids (list): List of device UUIDs for which line card details are to be retrieved.

        Returns:
            list: A list containing a single dictionary with the key "line_card_info" and the collected line card data as its value.
                Returns None if an exception occurs during the API call.
        """

        self.log("Fetching line card details for devices: {0}".format(device_ids), "INFO")

        all_linecards = []

        for device_id in device_ids:
            try:
                response = self.dnac._exec(
                    family="devices",
                    function="get_linecard_details",
                    params={'device_uuid': device_id}
                )
                linecard_data = response.get("response", [])
                if isinstance(linecard_data, list):
                    all_linecards.extend(linecard_data)
                else:
                    all_linecards.append(linecard_data)

            except Exception as e:
                self.msg = "Exception occurred while getting line card details: {0}".format(e)
                self.log(self.msg, "ERROR")
                self.set_operation_result("failed", False, self.msg, "ERROR")
                return None

        result = [{"line_card_info": all_linecards}]

        self.log("Retrieved {0} line card records".format(all_linecards), "DEBUG")
        return result

    def get_stack_details(self, device_ids):
        """
        Fetch stack details for a list of devices from Cisco Catalyst Center.

        Retrieves stack member information for each given device ID and compiles the results.

        Parameters:
            device_ids (list): List of device IDs for which stack details are to be retrieved.

        Returns:
            list: A list containing a single dictionary with the key "device_stack_info" and the collected stack details as its value.
                Returns None if an exception occurs during the API call.
        """

        self.log("Fetching stack details for devices: {0}".format(device_ids), "INFO")

        all_stack_details = []

        for device_id in device_ids:
            try:
                response = self.dnac._exec(
                    family="devices",
                    function="get_stack_details_for_device",
                    params={'device_id': device_id}
                )
                stack_info = response.get("response", [])
                if isinstance(stack_info, list):
                    all_stack_details.extend(stack_info)
                else:
                    all_stack_details.append(stack_info)

            except Exception as e:
                self.msg = "Exception occurred while getting stack details: {0}".format(e)
                self.log(self.msg, "ERROR")
                self.set_operation_result("failed", False, self.msg, "ERROR")
                return None

        result = [{"device_stack_info": all_stack_details}]

        self.log("Retrieved {0} stack detail records".format(all_stack_details), "DEBUG")
        return result

    def get_device_config(self, device_ids):
        """
        Fetch configuration data for a list of devices from Cisco Catalyst Center.

        Retrieves the full configuration details for each specified device ID and aggregates the results.

        Parameters:
            device_ids (list): List of device IDs for which configuration details need to be fetched.

        Returns:
            list: A list containing a single dictionary with the key "device_config_info" and the collected configuration data as its value.
                Returns None if an error occurs during the API call.
        """

        self.log("Fetching device configuration for: {0}".format(device_ids), "INFO")

        all_configs = []

        for device_id in device_ids:
            try:
                response = self.dnac._exec(
                    family="devices",
                    function="get_device_config_by_id",
                    params={'network_device_id': device_id}
                )
                configs = response.get("response", [])
                if isinstance(configs, list):
                    all_configs.extend(configs)
                else:
                    all_configs.append(configs)

            except Exception as e:
                self.msg = "Exception occurred while getting device config: {0}".format(e)
                self.log(self.msg, "ERROR")
                self.set_operation_result("failed", False, self.msg, "ERROR")
                return None

        result = [{"device_config_info": all_configs}]

        self.log("Retrieved {0} device config records".format(result), "DEBUG")
        return result

    def get_polling_interval(self, device_ids):
        """
        Fetch polling interval information for a list of devices from Cisco Catalyst Center.

        Retrieves the polling interval configuration for each specified device ID and compiles the results.

        Parameters:
            device_ids (list): List of device IDs for which polling interval details need to be retrieved.

        Returns:
            list: A list containing a single dictionary with the key "device_polling_interval_info" and the collected polling interval data.
                Returns None if an error occurs during the API call.
        """

        self.log("Fetching polling interval for devices: {0}".format(device_ids), "INFO")

        all_polling_intervals = []

        for device_id in device_ids:
            try:
                response = self.dnac._exec(
                    family="devices",
                    function="get_polling_interval_by_id",
                    params={'id': device_id}
                )
                intervals = response.get("response", [])
                if isinstance(intervals, list):
                    all_polling_intervals.extend(intervals)
                else:
                    all_polling_intervals.append(intervals)

            except Exception as e:
                self.msg = "Exception occurred while getting polling interval: {0}".format(e)
                self.log(self.msg, "ERROR")
                self.set_operation_result("failed", False, self.msg, "ERROR")
                return None

        result = [{"device_polling_interval_info": all_polling_intervals}]

        self.log("Retrieved {0} polling interval records".format(result), "DEBUG")
        return result

    def get_device_summary(self, device_ids):
        """
        Fetch summary information of devices for a list of devices from Cisco Catalyst Center.

        Retrieves key summary details for each device ID provided and aggregates the results.

        Parameters:
            device_ids (list): List of device IDs for which summary information needs to be retrieved.

        Returns:
            list: A list containing a single dictionary with the key "device_summary_info" and the collected summary data.
                Returns None if an error occurs during the API call.
        """

        self.log("Fetching device summary for devices: {0}".format(device_ids), "INFO")

        all_summaries = []

        for device_id in device_ids:
            try:
                response = self.dnac._exec(
                    family="devices",
                    function="get_device_summary",
                    params={'id': device_id}
                )
                summary_data = response.get("response", [])

                if isinstance(summary_data, list):
                    all_summaries.extend(summary_data)
                else:
                    all_summaries.append(summary_data)

            except Exception as e:
                self.msg = "Exception occurred while getting device summary: {0}".format(e)
                self.log(self.msg, "ERROR")
                self.set_operation_result("failed", False, self.msg, "ERROR")
                return None

        result = [{"device_summary_info": all_summaries}]
        self.log("Retrieved {0} device summary records".format(all_summaries), "DEBUG")
        return result

    def get_supervisor_card_detail(self, device_ids):
        """
        Fetch supervisor card details for a list of devices from Cisco Catalyst Center.

        Retrieves detailed supervisor card information for each provided device ID.

        Parameters:
            device_ids (list): List of device IDs to query for supervisor card details.

        Returns:
            list: A list containing a dictionary with key "supervisor_card_info" holding the retrieved data.
                Returns None if an error occurs during data retrieval.
        """

        self.log("Fetching supervisor card details for devices: {0}".format(device_ids), "INFO")

        all_supervisor_cards = []

        for device_id in device_ids:
            try:
                response = self.dnac._exec(
                    family="devices",
                    function="get_supervisor_card_detail",
                    params={'device_uuid': device_id}
                )
                supervisor_cards = response.get("response", [])
                if isinstance(supervisor_cards, list):
                    all_supervisor_cards.extend(supervisor_cards)
                else:
                    all_supervisor_cards.append(supervisor_cards)

            except Exception as e:
                self.msg = "Exception occurred while getting supervisor card details: {0}".format(e)
                self.log(self.msg, "ERROR")
                self.set_operation_result("failed", False, self.msg, "ERROR")
                return None

        result = [{"supervisor_card_info": all_supervisor_cards}]

        self.log("Retrieved {0} supervisor card records".format(result), "DEBUG")
        return result

    def get_poe_details(self, device_ids):
        """
        Fetch Power over Ethernet (PoE) details for specified devices from Cisco Catalyst Center.

        Retrieves PoE information for each device ID provided.

        Parameters:
            device_ids (list): List of device IDs to query for PoE details.

        Returns:
            list: A list containing a dictionary with key "poe_info" holding the retrieved PoE data.
                Returns None if an error occurs during retrieval.
        """

        self.log("Fetching PoE details for devices: {0}".format(device_ids), "INFO")

        all_poe_details = []

        for device_id in device_ids:
            try:
                response = self.dnac._exec(
                    family="devices",
                    function="poe_details",
                    params={'device_uuid': device_id}
                )
                poe_data = response.get("response", [])
                if isinstance(poe_data, list):
                    all_poe_details.extend(poe_data)
                else:
                    all_poe_details.append(poe_data)

            except Exception as e:
                self.msg = "Exception occurred while getting PoE details: {0}".format(e)
                self.log(self.msg, "ERROR")
                self.set_operation_result("failed", False, self.msg, "ERROR")
                return None

        result = [{"poe_info": all_poe_details}]

        self.log("Retrieved {0} PoE detail records".format(result), "DEBUG")
        return result

    def get_interface_info(self, device_ids):
        """
        Fetch interface information for specified devices from Cisco Catalyst Center.

        Retrieves detailed interface data for each device ID provided.

        Parameters:
            device_ids (list): List of device IDs to retrieve interface info for.

        Returns:
            list: A list containing a dictionary with key "interface_info" holding the retrieved interface data.
                Returns None if an error occurs during retrieval.
        """

        self.log("Fetching interface info for devices: {0}".format(device_ids), "INFO")

        all_interface_info = []

        for device_id in device_ids:
            try:
                response = self.dnac._exec(
                    family="devices",
                    function="get_interface_info_by_id",
                    params={'device_id': device_id}
                )
                interface_data = response.get("response", [])
                if isinstance(interface_data, list):
                    all_interface_info.extend(interface_data)
                else:
                    all_interface_info.append(interface_data)

            except Exception as e:
                self.msg = "Exception occurred while getting interface info: {0}".format(e)
                self.log(self.msg, "ERROR")
                self.set_operation_result("failed", False, self.msg, "ERROR")
                return None

        result = [{"interface_info": all_interface_info}]

        self.log("Retrieved {0} interface records".format(result), "DEBUG")
        return result

    def get_module_count(self, device_ids):
        """
        Fetch module count details for specified devices from Cisco Catalyst Center.

        Retrieves module count information for each device ID provided.

        Parameters:
            device_ids (list): List of device IDs to retrieve module count data for.

        Returns:
            list: A list containing a dictionary with key "module_count_info" holding the retrieved module count data.
                Returns None if an error occurs during retrieval.
        """

        self.log("Fetching module count for devices: {0}".format(device_ids), "INFO")

        all_module_counts = []

        for device_id in device_ids:
            try:
                response = self.dnac._exec(
                    family="devices",
                    function="get_module_count",
                    params={'device_id': device_id}
                )
                module_count_data = response.get("response", [])
                if isinstance(module_count_data, list):
                    all_module_counts.extend(module_count_data)
                else:
                    all_module_counts.append(module_count_data)

            except Exception as e:
                self.msg = "Exception occurred while getting module count: {0}".format(e)
                self.log(self.msg, "ERROR")
                self.set_operation_result("failed", False, self.msg, "ERROR")
                return None

        result = [{"module_count_info": all_module_counts}]

        self.log("Retrieved {0} module count records".format(result), "DEBUG")
        return result

    def get_connected_device_details_from_interfaces(self, device_ids):
        """
        Fetches and logs connected device details for each network device using their interface UUIDs.

        This method performs the following steps for each device ID:
        1. Retrieves interface information using the 'get_interface_info_by_id' API.
        2. Extracts unique 'instanceUuid' values from the interfaces.
        3. For each interface UUID, invokes the 'get_connected_device_detail' API using the device ID and interface UUID.
        4. Logs each API response, and collects the results.
        5. Appends all connected device details to the 'total_response' list under the key 'connected_device_info'.

        Parameters:
            device_ids (list): A list of device UUIDs (strings) for which to fetch connected device information.

        Returns:
            None: The results are stored in 'self.total_response'. Logging is used extensively for debugging and tracking.
        """
        self.log("Starting connected device detail collection", "INFO")

        all_connected_info = []

        for device_id in device_ids:
            try:
                self.log("Fetching interfaces for device_id: {}".format(device_id), "DEBUG")
                response = self.dnac._exec(
                    family="devices",
                    function="get_interface_info_by_id",
                    params={"device_id": device_id}
                )
                interfaces = response.get("response", [])
                self.log("Found interfaces {} for device_id: {}".format(interfaces, device_id), "DEBUG")

                unique_interface_uuids = set()
                for interface in interfaces:
                    interface_uuid = interface.get("instanceUuid")
                    if interface_uuid:
                        unique_interface_uuids.add(interface_uuid)
                    else:
                        self.log("Skipping interface (no instanceUuid)", "WARNING")

                for interface_uuid in unique_interface_uuids:
                    try:
                        connected_response = self.dnac._exec(
                            family="devices",
                            function="get_connected_device_detail",
                            params={
                                "device_uuid": device_id,
                                "interface_uuid": interface_uuid
                            }
                        )
                        detail = connected_response.get("response", {})
                        if detail:
                            self.log("API response for device {} and interface {}: {}".format(device_id, interface_uuid, detail), "DEBUG")
                            all_connected_info.append(detail)

                    except Exception as e:
                        self.log("Failed to fetch connected device detail for interface id {}: {}".format(interface_uuid, str(e)), "ERROR")

            except Exception as outer_e:
                self.log("Failed to retrieve interfaces for device_id {}: {}".format(device_id, str(outer_e)), "ERROR")

        result = [{"connected_device_info": all_connected_info}]
        self.log("Retrieved {} connected device records".format(result), "DEBUG")
        return result

    def get_interfaces_by_specified_range(self, device_ids):
        """
        Retrieves interface details for a list of device UUIDs using the
        'Get Device Interfaces by Specified Range' API with default values.
        The API is called with a default range of start_index = 1 and
        records_to_return = 500 for each device.

        Parameters:
            device_ids (list): List of device instance UUIDs for which interface
                               details need to be fetched.

        Returns:
            None. The retrieved results are appended to self.total_response under
            the key 'device_interfaces_by_range_info'.
        """

        self.log("Starting interface range fetch", "INFO")

        all_interface_results = []

        for device_id in device_ids:
            start_index = 1
            records_to_return = 500
            interface_data = []

            while True:
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

                    self.log("Received API response from 'get_device_interfaces_by_specified_range' for device_id {0} start_index {1}: {2}".format(
                        device_id, start_index, response), "DEBUG"
                    )

                    if not response or 'response' not in response:
                        self.log("Empty or invalid response received for device_id: {}".format(device_id), "WARNING")
                        break

                    data_chunk = response['response']
                    if not data_chunk:
                        self.log("No more interfaces found for device_id: {}".format(device_id), "DEBUG")
                        break

                    interface_data.extend(data_chunk)

                    if len(data_chunk) < records_to_return:
                        break

                    start_index += records_to_return

                except Exception as api_err:
                    self.log("Exception while calling get_device_interfaces_by_specified_range for device_id {0} due to {1}".format(device_id, api_err)
                             , "ERROR")
                    break

            all_interface_results.append({
                "device_id": device_id,
                "interface_info": interface_data
            })

        result = [{"device_interfaces_by_range_info": all_interface_results}]
        self.log("Retrieved interface info for range query: {}".format(result), "DEBUG")
        return result

    def get_device_link_mismatch_by_sites(self, site_ids):
        """
        Fetch Inventory Insight Device Link Mismatch data for a list of site IDs.

        Retrieves mismatch data for both 'vlan' and 'speed-duplex' categories for each site.
        Aggregates all results and returns them in a structured list.

        Parameters:
            site_ids (list): List of site IDs to fetch device link mismatch information.

        Returns:
            list: A list containing dictionaries for each site with keys 'site_id', 'vlan', and 'speed-duplex'.
                Returns None if an exception occurs.
        """

        self.log("Fetching device link mismatch for sites: {0}".format(site_ids), "INFO")

        all_mismatches = []

        for site_id in site_ids:
            if not site_id:
                self.msg = "Invalid or missing site ID in site_ids list."
                self.log(self.msg, "ERROR")
                self.set_operation_result("failed", False, self.msg, "ERROR")
                return None

            site_result = {
                "device_id": site_id,
                "vlan": [],
                "speed-duplex": []
            }

            for category in ['vlan', 'speed-duplex']:
                try:
                    response = self.dnac._exec(
                        family="devices",
                        function="inventory_insight_device_link_mismatch",
                        params={
                            'site_id': site_id,
                            'category': category
                        }
                    )
                    mismatch_data = response.get("response", [])
                    if isinstance(mismatch_data, list):
                        site_result[category].extend(mismatch_data)
                    else:
                        site_result[category].append(mismatch_data)

                    if category == 'vlan':
                        self.log("VLAN Category Link Mismatch Response for site {0}: {1}".format(site_id, response), "INFO")
                    else:
                        self.log("Speed-Duplex Category Link Mismatch Response for site {0}: {1}".format(site_id, response), "INFO")

                except Exception as e:
                    self.msg = "Exception occurred while getting {0} link mismatch data for site {1}: {2}".format(category, site_id, e)
                    self.log(self.msg, "ERROR")
                    self.set_operation_result("failed", False, self.msg, "ERROR").check_return_status

            all_mismatches.append(site_result)

        result = [{"device_link_mismatch_info": all_mismatches}]
        self.log("Retrieved link mismatch data for: {0}".format(result), "DEBUG")
        return result

    def get_device_id(self, filtered_config):
        """
        Retrieve unique device instance UUIDs based on the given filtered configuration.

        This method queries the Cisco Catalyst Center for devices matching criteria specified
        in the filtered configuration dictionary. It supports lookups by various device attributes
        such as management IP address, MAC address, hostname, serial number, software type and version,
        role, device type, family, and site hierarchy names.

        The method performs API calls with retries and timeout handling for each filter value,
        collects device instance UUIDs from the responses, and aggregates unique device IDs.
        It also supports site-based device lookups by resolving site IDs and retrieving devices per site.

        Parameters:
            filtered_config (dict): Dictionary containing device filtering parameters.
                Keys include:
                - 'management_ip_address' (list of str)
                - 'mac_address' (list of str)
                - 'hostname' (list of str)
                - 'serial_number' (list of str)
                - 'software_type' (list of str)
                - 'software_version' (list of str)
                - 'role' (list of str)
                - 'device_type' (list of str)
                - 'family' (list of str)
                - 'site_hierarchy' (list of str)
                - 'timeout' (int): API call timeout in seconds
                - 'retries' (int): Number of retry attempts
                - 'interval' (int): Wait interval between retries in seconds

        Returns:
            list: A list of unique device instance UUIDs (strings) that match the filter criteria.
                Returns None if an exception occurs during processing.
        """
        param_keys = [
            'management_ip_address', 'mac_address', 'hostname', 'serial_number',
            'software_type', 'software_version', 'role', 'device_type', 'family'
        ]

        param_key_map = {
            'management_ip_address': 'managementIpAddress',
            'mac_address': 'macAddress',
            'hostname': 'hostname',
            'serial_number': 'serialNumber',
            'software_type': 'softwareType',
            'software_version': 'softwareVersion',
            'role': 'role',
            'device_type': 'type',
            'family': 'family',
        }

        all_results = []
        device_ids = []

        try:
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
                    params = {param_key_map[key]: val}
                    start_time = time.time()
                    attempt = 0
                    self.log("Calling API with params: {0}".format(params))

                    while attempt < retries and (time.time() - start_time) < timeout:
                        params = {param_key_map[key]: val}
                        self.log("Attempt {0} - Calling API with params: {1}".format(attempt + 1, params))

                        response = self.dnac._exec(
                            family="devices",
                            function="get_device_list",
                            params=params
                        )
                        self.log("Response for {0}={1}: {2}".format(key, val, response))

                        devices = response.get('response', [])
                        self.log(devices)
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

                    all_results.append(response)

            # Site-based
            site_names = filtered_config.get("site_hierarchy")
            site_ids = []

            if site_names:
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

        except Exception as e:
            self.log("Exception in get_device_id: {0}".format(e), "ERROR")
            self.set_operation_result("failed", False, str(e), "ERROR")
            return None


def save_device_response_to_file(path, data, log=None):
    """
    Save the provided device response data to a JSON file at the specified path.

    This function writes the given data dictionary to a file in JSON format. If the provided
    file path does not end with ".json", the extension is automatically appended. The function
    ensures that the target directory exists, creating it if necessary. On successful write,
    it logs an informational message if a logging function is provided.

    Parameters:
        path (str): The full file path where the data should be saved.
        data (dict): The device response data to be serialized and saved as JSON.
        log (callable, optional): A logging function accepting a message and level string,
            e.g., log(message, level). If provided, logs success or failure messages.

    Returns:
        dict: A dictionary indicating the status of the save operation:
            - {"status": "success"} on success.
            - {"status": "failed", "error": <error_message>} if an exception occurs.
    """
    try:
        if not path.lower().endswith(".json"):
            path = path + ".json"

        directory = os.path.dirname(path)
        if directory and not os.path.exists(directory):
            os.makedirs(directory)

        with open(path, 'w') as f:
            json.dump(data, f, indent=4)

        if log:
            log("Successfully wrote device data to {}".format(path), "INFO")

        return {"status": "success"}

    except Exception as e:
        if log:
            log("Failed to write data to file: {}".format(str(e)), "ERROR")
        return {"status": "failed", "error": str(e)}


def main():
    """
    main entry point for module execution
    """
    element_spec = {'dnac_host': {'required': True, 'type': 'str'},
                    'dnac_port': {'type': 'str', 'default': '443'},
                    'dnac_username': {'type': 'str', 'default': 'admin', 'aliases': ['user']},
                    'dnac_password': {'type': 'str', 'no_log': True},
                    'dnac_verify': {'type': 'bool', 'default': 'True'},
                    'dnac_version': {'type': 'str', 'default': '2.2.3.3'},
                    'dnac_debug': {'type': 'bool', 'default': False},
                    'dnac_log_level': {'type': 'str', 'default': 'WARNING'},
                    "dnac_log_file_path": {"type": 'str', "default": 'dnac.log'},
                    "dnac_log_append": {"type": 'bool', "default": True},
                    'dnac_log': {'type': 'bool', 'default': False},
                    'validate_response_schema': {'type': 'bool', 'default': True},
                    'config_verify': {'type': 'bool', "default": True},
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
