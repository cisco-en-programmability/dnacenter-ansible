# !/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright (c) 2025, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import absolute_import, division, print_function

__metaclass__ = type
__author__ = ("Priyadharshini B", "Madhan Sankaranarayanan")

DOCUMENTATION = r"""
---
module: fabric_devices_info_workflow_manager
short_description: >
  This module filters and retrieves fabric device details from Cisco Catalyst Center based on the input device list.

description:
  - Accepts a list of network devices with attributes like IP, hostname, serial number, site hierarchy,device type, device role.
  - Filters fabric devices from the list of network devices.
  - Retrieves detailed fabric-specific information for the matched devices from Cisco Catalyst Center.
  - Supports timeout, retry, and interval configuration to find devices from Cisco Catalyst Center.

version_added: "6.32.0"
extends_documentation_fragment:
  - cisco.dnac.workflow_manager_params

author:
  - Madhan Sankaranarayanan (@madhansansel)
  - Priyadharshini B (@pbalaku2)

options:
  config_verify:
    description: Set to true to verify the Cisco Catalyst Center after applying the playbook config.
    type: bool
    default: true
  state:
    description: The desired state of the configuration after module execution.
    type: str
    choices: ["merged"]
    default: merged
  config:
    description: A list of dictionaries containing filters to retrieve the device details.
    type: list
    elements: dict
    required: true
    suboptions:
      fabric_devices:
        description:
          - Defines filters to retrieve network devices, from which fabric devices will be identified.
          - Each device entry must include at least one unique attribute such as IP address,
            device role, hostname, site hierarchy, or serial number.
        type: list
        elements: dict
        suboptions:
          ip_address:
            description:
              - List of IP addresses of the devices to check if they are part of the fabric.
              - If fabric, retrieves the corresponding fabric information.
            type: list
            elements: str
          hostname:
            description:
              - List of hostnames of the devices to check if they are part of the fabric.
              - If fabric, retrieves the corresponding fabric information.
            type: list
            elements: str
          serial_number:
            description:
              - List of serial numbers of the devices to check if they are part of the fabric.
              - If fabric, retrieves the corresponding fabric information.
            type: list
            elements: str
          device_role:
            description:
              - List containing roles of the devices to check if they are part of the fabric (e.g., ACCESS, CORE).
              - If matched, retrieves the corresponding fabric information.
            type: list
            elements: str
          device_type:
            description:
              - List containing types of the devices to check if they are part of the fabric.
                (e.g., Cisco Catalyst 9300 Switch", "Cisco Catalyst 9130AXE Unified Access Point).
              - If matched, retrieves the corresponding fabric information.
            type: list
            elements: str
          site_hierarchy:
            description:
              - List of site hierarchies to retrieve devices associated with the specified sites.
              - If the device is part of the fabric, retrieves the corresponding fabric information.
              - If more than 1000 fabric devices are present, both site and role are specified in the input,
                the workflow will filter and return only the devices matching the specified role within the given site.
              - If less than 1000 fabric devices are present and both site and role are specified,
                the workflow will retrieve all devices within the specified site and all devices matching the specified role across all sites.
            type: list
            elements: str
          timeout:
            description:
              - Time in seconds to wait for a response from the Catalyst Center.
            type: int
            default: 60
          retries:
            description:
              - Number of retry attempts in case of failures.
            type: int
            default: 3
          interval:
            description:
              - Delay in seconds between each retry.
            type: int
            default: 10
          requested_info:
            description:
              - Select which information categories to gather for each matched fabric device.
              - Use all to retrieve every available category, or specify a subset.
            type: list
            elements: str
            default: [all]
            choices:
              - all
              - fabric_info
              - handoff_info
              - onboarding_info
              - connected_devices_info
              - device_health_info
              - device_issues_info
          file_info:
            description:
              - Optional settings to control output file generation for fabric device information.
              - If provided, the content will be saved to the output file. Else, it will be displayed in the terminal.
              - Use this block to define the file path, format, mode, and timestamp handling.
            type: dict
            suboptions:
              file_path:
                description:
                  - Absolute path to the output file without extension.
                  - The file extension (.json or .yaml) is added automatically based on file_format.
                type: str
                required: true
              file_format:
                description:
                  - Format to save the output data.
                type: str
                default: yaml
                choices:
                  - json
                  - yaml
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
- SDK Methods used are
  - devices.Devices.get_device_list
  - sda.Sda.get_fabric_devices
  - sda.Sda.get_fabric_sites
  - sda.Sda.get_fabric_devices_layer3_handoffs_with_sda_transit
  - sda.Sda.get_fabric_devices_layer3_handoffs_with_ip_transit
  - sda.Sda.get_fabric_devices_layer2_handoffs
  - devices.Devices.get_interface_info_by_id
  - devices.Devices.get_connected_device_detail
  - devices.Devices.devices
  - issues.Issues.issues
  - sda.Sda.get_provisioned_wired_device

- Paths used are
  - GET/dna/intent/api/v1/network-device
  - GET/dna/intent/api/v1/sda/fabricDevices
  - GET/dna/intent/api/v1/sda/fabricSites
  - GET/dna/intent/api/v1/sda/fabricDevices/layer3Handoffs/sdaTransits
  - GET/dna/intent/api/v1/sda/fabricDevices/layer3Handoffs/ipTransits
  - GET/dna/intent/api/v1/sda/fabricDevices/layer2Handoffs
  - GET/dna/intent/api/v1/interface/network-device/{deviceId}
  - GET/dna/intent/api/v1/network-device/{deviceUuid}/interface/{interfaceUuid}/neighbor
  - GET/dna/intent/api/v1/device-health
  - GET/dna/intent/api/v1/issues
  - GET/dna/intent/api/v1/business/sda/provision-device
"""

EXAMPLES = r"""

- name: Get Fabric devices info from Cisco Catalyst Center
  hosts: localhost
  connection: local
  vars_files:
    - "credentials.yml"
  tasks:
    - name: Fabric devices info
      cisco.dnac.fabric_devices_info_workflow_manager:
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
        state: merged
        config:
          - fabric_devices:
              - ip_address: ["204.1.2.3"]
                hostname: ["TB1-DM-Transit.solutionsanity.com"]
                serial_number: ["FJC2335S09F"]
                device_role: ["ACCESS"]
                device_type: ["Cisco Catalyst 9130AXE Unified Access Point"]
                site_hierarchy: ["Global/USA/New York/NY_BLD1", "Global/USA/New York/NY_BLD1/FLOOR1"]
                timeout: 60
                retries: 1
                interval: 10
                file_info:
                  file_path: /Users/priyadharshini/Downloads/fabric_device_info
                  file_format: yaml
                  file_mode: a
                  timestamp: true


- name: Get Fabric devices info from Cisco Catalyst Center
  hosts: localhost
  connection: local
  vars_files:
    - "credentials.yml"
  tasks:
    - name: Fabric devices info
      cisco.dnac.fabric_devices_info_workflow_manager:
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
        state: merged
        config:
          - fabric_devices:
              - ip_address: ["204.1.2.3"]
                hostname: ["TB1-DM-Transit.solutionsanity.com"]
                serial_number: ["FJC2335S09F"]
                device_role: ["ACCESS"]
                device_type: ["Cisco Catalyst 9130AXE Unified Access Point"]
                site_hierarchy: ["Global/USA/New York/NY_BLD1", "Global/USA/New York/NY_BLD1/FLOOR1"]
                timeout: 30
                retries: 2
                interval: 10
                requested_info:
                  - fabric_info
                  - handoff_info
                  - onboarding_info
                  - connected_devices_info
                  - device_health_info
                  - device_issues_info
                file_info:
                  file_path: /Users/priyadharshini/Downloads/fabric_device_info
                  file_format: yaml
                  file_mode: a
                  timestamp: true

- name: Get Fabric devices info from Cisco Catalyst Center
  hosts: localhost
  connection: local
  vars_files:
    - "credentials.yml"
  tasks:
    - name: Fabric devices info
      cisco.dnac.fabric_devices_info_workflow_manager:
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
        state: merged
        config:
          - fabric_devices:
              - ip_address: ["204.1.2.3"]
                hostname: ["TB1-DM-Transit.solutionsanity.com"]
                serial_number: ["FJC2335S09F"]
                device_role: ["ACCESS"]
                device_type: ["Cisco Catalyst 9130AXE Unified Access Point"]
                site_hierarchy: ["Global/USA/New York/NY_BLD1", "Global/USA/New York/NY_BLD1/FLOOR1"]
                timeout: 30
                retries: 3
                interval: 10
                requested_info: [all]
                file_info:
                  file_path: /Users/priyadharshini/Downloads/fabric_device_info
                  file_format: yaml
                  file_mode: a
                  timestamp: true
"""

RETURN = r"""

# Case 1: Successfully retrieved fabric information for devices that are part of the fabric, from cisco catalyst center

response_fabric_info:
  description: A list with details of fabric info.
  returned: always
  type: list
  sample:
    {
      "response": [
        "The fabric devices filtered from the network devices are: ['204.1.2.2']",
        {
          "fabric_info": [
            {
              "device_ip": "204.1.2.2",
              "fabric_details": [
                {
                  "borderDeviceSettings": {
                    "borderTypes": [
                      "LAYER_3"
                    ],
                    "layer3Settings": {
                      "borderPriority": 10,
                      "importExternalRoutes": false,
                      "isDefaultExit": true,
                      "localAutonomousSystemNumber": "5",
                      "prependAutonomousSystemCount": 0
                    }
                  },
                  "deviceRoles": [
                    "BORDER_NODE",
                    "CONTROL_PLANE_NODE",
                    "EDGE_NODE"
                  ],
                  "fabricId": "c9fda934-a212-4a1b-be5f-f391d2ff8863",
                  "id": "9294625f-52d4-485f-9d36-5abcfa4f863f",
                  "networkDeviceId": "e5cc9398-afbf-40a2-a8b1-e9cf0635c28a"
                }
              ]
            }
          ]
        }
      ],
      "status": "success"
    }

# Case 2: Successfully retrieved handoff info for devices that are part of the fabric, from cisco catalyst center

response_fabric_devices_layer3_handoffs_sda_info:
    description: A list with details of handoff info of both layer 2 and 3.
    returned: always
    type: list
    "sample": {
      "response": [
        "The fabric devices filtered from the network devices are: ['204.1.2.2']",
        [
          {
            "fabric_devices_layer3_handoffs_sda_info": [
              {
                "device_ip": "204.1.2.2",
                "handoff_info": [
                  {
                    "networkDeviceId": "string",
                    "fabricId": "string",
                    "transitNetworkId": "string",
                    "affinityIdPrime": "integer",
                    "affinityIdDecider": "integer",
                    "connectedToInternet": "boolean",
                    "isMulticastOverTransitEnabled": "boolean"
                  }
                ]
              }
            ]
          }
        ],
        [
          {
            "fabric_devices_layer3_handoffs_ip_info": [
              {
                "device_ip": "204.1.2.2",
                "handoff_info": [
                  {
                    "id": "string",
                    "networkDeviceId": "string",
                    "fabricId": "string",
                    "transitNetworkId": "string",
                    "interfaceName": "string",
                    "externalConnectivityIpPoolName": "string",
                    "virtualNetworkName": "string",
                    "vlanId": "integer",
                    "tcpMssAdjustment": "integer",
                    "localIpAddress": "string",
                    "remoteIpAddress": "string",
                    "localIpv6Address": "string",
                    "remoteIpv6Address": "string"
                  }
                ]
              }
            ]
          }
        ],
        [
          {
            "fabric_devices_layer2_handoffs_info": [
              {
                "device_ip": "204.1.2.2",
                "handoff_info": [
                  {
                    "id": "string",
                    "networkDeviceId": "string",
                    "fabricId": "string",
                    "interfaceName": "string",
                    "internalVlanId": "integer",
                    "externalVlanId": "integer"
                  }
                ]
              }
            ]
          }
        ]
      ],
      "status": "success"
    }

# Case 3: Successfully retrieved issues for devices that are part of the fabric, from cisco catalyst center

response_device_issues_info:
  description: A list with details of issues info.
  returned: always
  type: list
  sample: {
    "response": [
      "The fabric devices filtered from the network devices are: ['204.1.2.2']",
      [
        {
          "device_issues_info": [
            {
              "device_ip": "204.1.2.2",
              "issue_details": [
                {
                  "aiDriven": "No",
                  "category": "Connected",
                  "clientMac": null,
                  "deviceId": "e5cc9398-afbf-40a2-a8b1-e9cf0635c28a",
                  "deviceRole": "",
                  "issueId": "4eec8a72-65ff-45ae-89be-f0437eae778e",
                  "issue_occurence_count": 1703,
                  "last_occurence_time": 1750856863468,
                  "name": "AAA Server '172.23.241.245' state on Edge device 'abhitest' is DEAD.",
                  "priority": "P1",
                  "siteId": "",
                  "status": "active"
                },
                {
                  "aiDriven": "No",
                  "category": "User Defined",
                  "clientMac": null,
                  "deviceId": "e5cc9398-afbf-40a2-a8b1-e9cf0635c28a",
                  "deviceRole": "",
                  "issueId": "80ba94eb-15d3-48c2-a3f4-20bf99551217",
                  "issue_occurence_count": 5,
                  "last_occurence_time": 1750789583288,
                  "name": "NON_AUTHORITATIVE_CLOCK",
                  "priority": "P2",
                  "siteId": "",
                  "status": "active"
                }
              ]
            }
          ]
        }
      ]
    ],
    "status": "success"
  }



# Case 4: Successfully retrieved health info for devices that are part of the fabric, from cisco catalyst center

response_device_health_info:
  description: A list with details of health info.
  returned: always
  type: list
  sample: {
    "response": [
      "The fabric devices filtered from the network devices are: ['204.1.2.2']",
      [
        {
          "device_health_info": [
            {
              "device_ip": "204.1.2.2",
              "health_details": [
                {
                  "airQualityHealth": {},
                  "avgTemperature": 4350.0,
                  "band": {},
                  "clientCount": {},
                  "cpuHealth": 10,
                  "cpuUlitilization": 2.75,
                  "cpuUtilization": 2.75,
                  "deviceFamily": "SWITCHES_AND_HUBS",
                  "deviceType": "Cisco Catalyst 9300 Switch",
                  "freeMemoryBufferHealth": -1,
                  "freeTimerScore": -1,
                  "interDeviceLinkAvailFabric": 10,
                  "interDeviceLinkAvailHealth": 100,
                  "interfaceLinkErrHealth": 10,
                  "interferenceHealth": {},
                  "ipAddress": "204.1.2.2",
                  "issueCount": 2,
                  "location": "Global/USA/New York/NY_BLD1",
                  "macAddress": "90:88:55:07:59:00",
                  "maxTemperature": 5700.0,
                  "memoryUtilization": 50,
                  "memoryUtilizationHealth": 10.0,
                  "model": "Cisco Catalyst 9300 Switch",
                  "name": "abhitest",
                  "noiseHealth": {},
                  "osVersion": "17.12.4",
                  "overallHealth": 1,
                  "packetPoolHealth": -1,
                  "reachabilityHealth": "REACHABLE",
                  "utilizationHealth": {},
                  "uuid": "e5cc9398-afbf-40a2-a8b1-e9cf0635c28a",
                  "wanLinkUtilization": -1.0,
                  "wqePoolsHealth": -1
                }
              ]
            }
          ]
        }
      ]
    ],
    "status": "success"
  }

# Case 5: Successfully retrieved connected device info for devices that are part of the fabric, from cisco catalyst center

response_connected_device_info:

  description: A list with details of connected device info.
  returned: always
  type: list
  sample: {
    "response": [
      "The fabric devices filtered from the network devices are: ['204.1.2.2']",
      [
        {
          "connected_device_info": [
            {
              "connected_device_details": [
                {
                  "capabilities": [
                    "ROUTER",
                    "TB_BRIDGE"
                  ],
                  "neighborDevice": "AP345D.A80E.20B4",
                  "neighborPort": "GigabitEthernet0"
                },
                {
                  "capabilities": [
                    "IGMP_CONDITIONAL_FILTERING",
                    "ROUTER",
                    "SWITCH"
                  ],
                  "neighborDevice": "NY-BN-9300",
                  "neighborPort": "TenGigabitEthernet1/1/2"
                },
                {
                  "capabilities": [
                    "ROUTER",
                    "TB_BRIDGE"
                  ],
                  "neighborDevice": "AP6849.9275.0FD0",
                  "neighborPort": "GigabitEthernet0"
                },
                {
                  "capabilities": [
                    "ROUTER",
                    "TB_BRIDGE"
                  ],
                  "neighborDevice": "AP6CD6.E369.49B4",
                  "neighborPort": "GigabitEthernet0"
                },
                {
                  "capabilities": [
                    "ROUTER",
                    "TB_BRIDGE"
                  ],
                  "neighborDevice": "AP34B8.8315.7C6C",
                  "neighborPort": "GigabitEthernet0"
                },
                {
                  "capabilities": [
                    "HOST"
                  ],
                  "neighborDevice": "IAC-TSIM",
                  "neighborPort": "TenGigabitEthernet0/0/2"
                },
                {
                  "capabilities": [
                    "IGMP_CONDITIONAL_FILTERING",
                    "ROUTER",
                    "SWITCH"
                  ],
                  "neighborDevice": "NY-BN-9300",
                  "neighborPort": "TenGigabitEthernet2/1/2"
                }
              ],
              "device_ip": "204.1.2.2"
            }
          ]
        }
      ]
    ],
    "status": "success"
    }

# Case 5: Successfully retrieved all info for devices that are part of the fabric, from cisco catalyst center

response_all_info:
  description: A list with details of connected device info.
  returned: always
  type: list
  sample: {
    "response": [
      "The fabric devices filtered from the network devices are: ['204.1.2.2', '204.192.6.200']",
      [
        {
          "fabric_info": [
            {
              "device_ip": "204.1.2.2",
              "fabric_details": [
                {
                  "borderDeviceSettings": {
                    "borderTypes": ["LAYER_3"],
                    "layer3Settings": {
                      "borderPriority": 10,
                      "importExternalRoutes": false,
                      "isDefaultExit": true,
                      "localAutonomousSystemNumber": "5",
                      "prependAutonomousSystemCount": 0
                    }
                  },
                  "deviceRoles": [
                    "BORDER_NODE",
                    "CONTROL_PLANE_NODE",
                    "EDGE_NODE"
                  ],
                  "fabricId": "c9fda934-a212-4a1b-be5f-f391d2ff8863",
                  "id": "9294625f-52d4-485f-9d36-5abcfa4f863f",
                  "networkDeviceId": "e5cc9398-afbf-40a2-a8b1-e9cf0635c28a"
                }
              ]
            }
          ]
        }
      ],
      [
        {
          "device_issues_info": [
            {
              "device_ip": "204.1.2.2",
              "issue_details": [
                {
                  "aiDriven": "No",
                  "category": "Connected",
                  "clientMac": null,
                  "deviceId": "e5cc9398-afbf-40a2-a8b1-e9cf0635c28a",
                  "deviceRole": "",
                  "issueId": "4eec8a72-65ff-45ae-89be-f0437eae778e",
                  "issue_occurence_count": 1703,
                  "last_occurence_time": 1750856863468,
                  "name": "AAA Server '172.23.241.245' state on Edge device 'abhitest' is DEAD.",
                  "priority": "P1",
                  "siteId": "",
                  "status": "active"
                },
                {
                  "aiDriven": "No",
                  "category": "User Defined",
                  "clientMac": null,
                  "deviceId": "e5cc9398-afbf-40a2-a8b1-e9cf0635c28a",
                  "deviceRole": "",
                  "issueId": "80ba94eb-15d3-48c2-a3f4-20bf99551217",
                  "issue_occurence_count": 5,
                  "last_occurence_time": 1750789583288,
                  "name": "NON_AUTHORITATIVE_CLOCK",
                  "priority": "P2",
                  "siteId": "",
                  "status": "active"
                }
              ]
            }
          ]
        }
      ],
      [
        {
          "device_health_info": [
            {
              "device_ip": "204.1.2.2",
              "health_details": [
                {
                  "airQualityHealth": {},
                  "avgTemperature": 4350.0,
                  "band": {},
                  "clientCount": {},
                  "cpuHealth": 10,
                  "cpuUlitilization": 2.75,
                  "cpuUtilization": 2.75,
                  "deviceFamily": "SWITCHES_AND_HUBS",
                  "deviceType": "Cisco Catalyst 9300 Switch",
                  "freeMemoryBufferHealth": -1,
                  "freeTimerScore": -1,
                  "interDeviceLinkAvailFabric": 10,
                  "interDeviceLinkAvailHealth": 100,
                  "interfaceLinkErrHealth": 10,
                  "interferenceHealth": {},
                  "ipAddress": "204.1.2.2",
                  "issueCount": 2,
                  "location": "Global/USA/New York/NY_BLD1",
                  "macAddress": "90:88:55:07:59:00",
                  "maxTemperature": 5700.0,
                  "memoryUtilization": 50,
                  "memoryUtilizationHealth": 10.0,
                  "model": "Cisco Catalyst 9300 Switch",
                  "name": "abhitest",
                  "noiseHealth": {},
                  "osVersion": "17.12.4",
                  "overallHealth": 1,
                  "packetPoolHealth": -1,
                  "reachabilityHealth": "REACHABLE",
                  "utilizationHealth": {},
                  "uuid": "e5cc9398-afbf-40a2-a8b1-e9cf0635c28a",
                  "wanLinkUtilization": -1.0,
                  "wqePoolsHealth": -1
                }
              ]
            }
          ]
        }
      ],
      [
        {
          "fabric_devices_layer3_handoffs_sda_info": [
            {
              "device_ip": "204.1.2.2",
              "handoff_info": "No handoff info found"
            }
          ]
        }
      ],
      [
        {
          "fabric_devices_layer3_handoffs_ip_info": [
            {
              "device_ip": "204.1.2.2",
              "handoff_info": "No handoff info found"
            }
          ]
        }
      ],
      [
        {
          "fabric_devices_layer2_handoffs_info": [
            {
              "device_ip": "204.1.2.2",
              "handoff_info": "No handoff info found"
            }
          ]
        }
      ],
      [
        {
          "connected_device_info": [
            {
              "connected_device_details": [
                {
                  "capabilities": [
                    "IGMP_CONDITIONAL_FILTERING",
                    "ROUTER",
                    "SWITCH"
                  ],
                  "neighborDevice": "NY-BN-9300",
                  "neighborPort": "TenGigabitEthernet2/1/2"
                },
                {
                  "capabilities": [
                    "IGMP_CONDITIONAL_FILTERING",
                    "ROUTER",
                    "SWITCH"
                  ],
                  "neighborDevice": "NY-BN-9300",
                  "neighborPort": "TenGigabitEthernet1/1/2"
                },
                {
                  "capabilities": [
                    "ROUTER",
                    "TB_BRIDGE"
                  ],
                  "neighborDevice": "AP6849.9275.0FD0",
                  "neighborPort": "GigabitEthernet0"
                },
                {
                  "capabilities": [
                    "ROUTER",
                    "TB_BRIDGE"
                  ],
                  "neighborDevice": "AP6CD6.E369.49B4",
                  "neighborPort": "GigabitEthernet0"
                },
                {
                  "capabilities": [
                    "ROUTER",
                    "TB_BRIDGE"
                  ],
                  "neighborDevice": "AP34B8.8315.7C6C",
                  "neighborPort": "GigabitEthernet0"
                },
                {
                  "capabilities": ["HOST"],
                  "neighborDevice": "IAC-TSIM",
                  "neighborPort": "TenGigabitEthernet0/0/2"
                },
                {
                  "capabilities": [
                    "ROUTER",
                    "TB_BRIDGE"
                  ],
                  "neighborDevice": "AP345D.A80E.20B4",
                  "neighborPort": "GigabitEthernet0"
                }
              ],
              "device_ip": "204.1.2.2"
            }
          ]
        }
      ]
    ],
    "status": "success"
    }

# Case 6: If no fabric devices is found

response_info:
  description: A list with details of connected device info.
  returned: always
  type: list
  sample: {
    "response":[
      "No fabric devices found for the given filters."
    ]
  }
"""


from ansible_collections.cisco.dnac.plugins.module_utils.dnac import (
    DnacBase,
)
from ansible.module_utils.basic import AnsibleModule
import time
import os
import json
import yaml
from datetime import datetime

from ansible_collections.cisco.dnac.plugins.module_utils.validation import (
    validate_list_of_dicts,)


class FabricDevicesInfo(DnacBase):
    def __init__(self, module):
        super().__init__(module)
        self.supported_states = ['merged']
        self.total_response = []

    def validate_input(self):
        """
        Validate the playbook configuration for fabric device structure and integrity.

        This method ensures that the provided 'config' attribute adheres to the expected format for fabric device
        processing. It validates the presence and types of required fields, checks for duplicates, and ensures
        consistency in user-provided values such as requested information categories.

        Args:
            self: The instance of the class that contains the 'config' attribute to be validated.

        Returns:
            The method returns the current instance with updated attributes:
            - self.msg: A descriptive message indicating the outcome of the validation process.
            - self.status: The result of the validation ('success' or 'failed').
            - self.validated_config: A cleaned and validated configuration if validation succeeds.

        Validations Performed:
            - 'config' must be a list of dictionaries.
            - Each dictionary must contain the key 'fabric_devices' mapped to a list.
            - Each 'fabric_device' must be a dictionary containing at least one of:
                'ip_address', 'hostname', 'serial_number', 'device_role', or 'site_hierarchy'.
            - All values in those fields (if present) must be lists of strings.
            - 'requested_info', if provided, must be a list of allowed strings.
            - Validates 'timeout', 'retries', and 'interval' as non-negative integers if specified.
            - Ensures 'output_file_path' is a string if provided.
            - Detects and prevents duplicate IP addresses, hostnames, or serial numbers across devices.
        """
        config_spec = {
            'fabric_devices': {
                'type': 'list',
                'elements': 'dict',
                'ip_address': {'type': 'list', 'elements': 'str'},
                'hostname': {'type': 'list', 'elements': 'str'},
                'serial_number': {'type': 'list', 'elements': 'str'},
                'device_role': {'type': 'list', 'elements': 'str'},
                'site_hierarchy': {'type': 'list', 'elements': 'str'},
                'device_type': {'type': 'list', 'elements': 'str'},
                'timeout': {'type': 'int', 'default': 60},
                'retries': {'type': 'int', 'default': 3},
                'interval': {'type': 'int', 'default': 10},
                'requested_info': {
                    'type': 'list',
                    'elements': 'str',
                    'default': [
                        'fabric_info',
                        'handoff_info',
                        'connected_devices_info',
                        'onboarding_info',
                        'device_health_info',
                        'device_issues_info'
                    ]
                },
                'file_info': {
                    'type': 'dict',
                    'elements': 'dict',
                    'file_path': {'type': 'str'},
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

        if not isinstance(self.config, list):
            self.msg = "Config should be a list"
            self.set_operation_result("failed", False, self.msg, "ERROR")
            return self

        validated_config, invalid_params = validate_list_of_dicts(
            self.config, config_spec)

        validated_config = []
        dup_ips, dup_hostnames, dup_serials = set(), set(), set()

        if invalid_params:
            self.msg = "Invalid parameters in playbook: {0}".format(invalid_params)
            self.set_operation_result("failed", False, self.msg, "ERROR")
            return self

        for config in self.config:
            if not isinstance(config, dict):
                self.msg = "Each item in config must be a dictionary"
                self.set_operation_result("failed", False, self.msg, "ERROR")
                return self

            if "fabric_devices" not in config:
                self.msg = "'fabric_devices' key is missing in the config block"
                self.set_operation_result("failed", False, self.msg, "ERROR")
                return self

            fabric_devices = config.get("fabric_devices", [])

            for device in fabric_devices:
                for ip in device.get("ip_address", []):
                    if ip in dup_ips:
                        self.msg = "Duplicate ip_address found: {0}".format(ip)
                        self.set_operation_result("failed", False, self.msg, "ERROR")
                        return self
                    dup_ips.add(ip)

                for hostname in device.get("hostname", []):
                    if hostname in dup_hostnames:
                        self.msg = "Duplicate hostname found: {0}".format(hostname)
                        self.set_operation_result("failed", False, self.msg, "ERROR")
                        return self
                    dup_hostnames.add(hostname)

                for serial in device.get("serial_number", []):
                    if serial in dup_serials:
                        self.msg = "Duplicate serial_number found: {0}".format(serial)
                        self.set_operation_result("failed", False, self.msg, "ERROR")
                        return self
                    dup_serials.add(serial)

                for numeric in ("timeout", "retries", "interval"):
                    if numeric in device and device[numeric] not in (None, ""):
                        if not isinstance(device[numeric], int) or device[numeric] < 0:
                            self.msg = "'{0}' must be a non-negative integer".format(numeric)
                            self.set_operation_result("failed", False, self.msg, "ERROR")
                            return self

                file_info = device.get("file_info")

                if file_info:
                    if not isinstance(file_info, dict):
                        self.msg = "'file_info' must be a dictionary"
                        self.set_operation_result("failed", False, self.msg, "ERROR")
                        return self

                    file_info.setdefault("file_format", "yaml")
                    file_info.setdefault("file_mode", "w")
                    file_info.setdefault("timestamp", False)

                    allowed_file_info_keys = {"file_path", "file_format", "file_mode", "timestamp"}

                    for key in file_info:
                        if key not in allowed_file_info_keys:
                            self.msg = "'{0}' is not a valid key in file_info. Allowed keys are: {1}".format(
                                key, sorted(allowed_file_info_keys)
                            )
                            self.set_operation_result("failed", False, self.msg, "ERROR")
                            return self

                    if "file_path" in file_info and not isinstance(file_info["file_path"], str):
                        self.msg = "'file_path' in file_info must be a string"
                        self.set_operation_result("failed", False, self.msg, "ERROR")
                        return self

                    if "file_format" in file_info and not isinstance(file_info["file_format"], str):
                        self.msg = "'file_format' in file_info must be a string"
                        self.set_operation_result("failed", False, self.msg, "ERROR")
                        return self

                    if "file_mode" in file_info and not isinstance(file_info["file_mode"], str):
                        self.msg = "'file_mode' in file_info must be a string"
                        self.set_operation_result("failed", False, self.msg, "ERROR")
                        return self

                    if "timestamp" in file_info and not isinstance(file_info["timestamp"], bool):
                        self.msg = "'timestamp' in file_info must be a boolean"
                        self.set_operation_result("failed", False, self.msg, "ERROR")
                        return self

            validated_config.append(config)

        self.validated_config = validated_config
        return self

    def get_want(self, config):
        """
        Extract the desired state ('want') from a fabric devices playbook block.

        Args:
            self (object): An instance of a class interacting with Cisco Catalyst Center.
            config (dict): A dictionary containing the playbook configuration, expected to include
                        a list of fabric devices under the 'fabric_devices' key.

        Returns:
            self: The current instance of the class with the 'want' attribute populated
                based on the validated fabric device data from the playbook.

        Description:
            This method processes the 'fabric_devices' section of the provided configuration and
            validates its structure and content. Specifically, it performs the following steps:

            - Checks that the 'fabric_devices' key exists and is not empty.
            - Validates that each device entry includes at least one of the following:
            'ip_address', 'hostname', 'serial_number', 'device_role', or 'site_hierarchy'.
            - If 'requested_info' is provided for a device, verifies that all values are among
            the allowed set:
                - all
                - fabric_info
                - handoff_info
                - onboarding_info
                - connected_devices_info
                - device_health_info
                - device_issues_info
            Upon successful validation, the fabric device data is stored in the instance's 'want'
            attribute for use in subsequent processing.
        """

        want = {}
        want["fabric_devices"] = config.get("fabric_devices")

        required_device_keys = [
            "ip_address",
            "hostname",
            "serial_number",
            "device_role",
            "site_hierarchy",
            "device_type"
        ]
        allowed_return_values = {
            "all",
            "fabric_info",
            "handoff_info",
            "onboarding_info",
            "connected_devices_info",
            "device_health_info",
            "device_issues_info",
        }

        allowed_keys = {"file_path", "file_format", "file_mode", "timestamp"}

        for device in config["fabric_devices"]:
            if not any(device.get(key) for key in required_device_keys):
                self.msg = (
                    "Each fabric device must contain at least one of: {0}."
                    .format(", ".join(required_device_keys))
                )
                self.set_operation_result("failed", False, self.msg, "ERROR").check_return_status()

            if "requested_info" in device and device["requested_info"] is not None:
                return_value = device["requested_info"]
                for value_name in return_value:
                    if value_name not in allowed_return_values:
                        self.msg = (
                            "'{0}' is not a valid return value. Allowed values are: {1}"
                            .format(value_name, sorted(allowed_return_values))
                        )
                        self.set_operation_result("failed", False, self.msg, "ERROR").check_return_status()

            if "file_info" in device:
                file_info = device["file_info"]
                if file_info is None:
                    continue

                allowed_formats = {"json", "yaml"}
                allowed_modes = {"a", "w"}

                for key in file_info:
                    if key not in allowed_keys:
                        self.msg = "'{0}' is not a valid key in 'file_info'. Allowed keys are: {1}".format(
                            key, sorted(allowed_keys)
                        )
                        self.set_operation_result("failed", False, self.msg, "ERROR").check_return_status()

                    if file_info["file_format"] not in allowed_formats:
                        self.msg = "'file_format' must be one of: {0}".format(", ".join(sorted(allowed_formats)))
                        self.set_operation_result("failed", False, self.msg, "ERROR").check_return_status()

                    if file_info["file_mode"] not in allowed_modes:
                        self.msg = "'file_mode' must be one of: {0}".format(", ".join(sorted(allowed_modes)))
                        self.set_operation_result("failed", False, self.msg, "ERROR").check_return_status()

        self.want = want
        self.log("Desired State (want): {0}".format(self.want), "INFO")
        return self

    def get_diff_merged(self, config):
        """
        Retrieve and merge fabric-related information from Cisco Catalyst Center based on device configuration input.

        Args:
            self (object): An instance of the class interacting with Cisco Catalyst Center APIs.
            config (dict): A dictionary containing the playbook configuration, including a list of
                        fabric devices and the specific types of information to be retrieved
                        (via the 'requested_info' key).

        Returns:
            self: The current instance with the 'msg' and 'total_response' attributes populated
                based on the API responses for the requested device information.

        Description:
            This method retrieves fabric-related information of fabric devices
            for a list of network devices provided in the playbook. For each device in the
            input, it performs the following:

            - Determines which categories of information are requested, including:
                - fabric_info
                - handoff_info (Layer 2, Layer 3 SDA, Layer 3 IP)
                - onboarding_info
                - connected_devices_info
                - device_health_info
                - device_issues_info
        """

        self.log("Starting get_diff_merged with provided config", "INFO")
        self.log(config)

        fabric_devices = config.get("fabric_devices", [])
        combined_fabric_data = {}

        for device_cfg in fabric_devices:
            filtered_config = {}
            for field_name, field_value in device_cfg.items():
                if field_name != "requested_info":
                    filtered_config[field_name] = field_value

            self.log("Filtered config (excluding requested_info): {0}".format(filtered_config))

            requested_info = device_cfg.get("requested_info", [])
            if not requested_info:
                all_info_requested = True
            else:
                all_info_requested = "all" in requested_info

            fabric_info = all_info_requested or "fabric_info" in requested_info
            handoff_info = all_info_requested or "handoff_info" in requested_info
            onboarding_info = all_info_requested or "onboarding_info" in requested_info
            connected_devices_info = all_info_requested or "connected_devices_info" in requested_info
            device_health_info = all_info_requested or "device_health_info" in requested_info
            device_issues_info = all_info_requested or "device_issues_info" in requested_info

            self.log("""
            Requested:
            fabric_info:            {}
            handoff_info:           {}
            onboarding_info:        {}
            connected_devices_info: {}
            device_health_info:     {}
            device_issues_info:     {}
            """.format(
                fabric_info,
                handoff_info,
                onboarding_info,
                connected_devices_info,
                device_health_info,
                device_issues_info
            ), "DEBUG")

            ip_uuid_map = self.get_device_id(filtered_config)
            fabric_site_ids = self.get_fabric_site_id()
            fabric_devices = self.filter_fabric_device(ip_uuid_map, filtered_config)

            if not ip_uuid_map:
                self.log("No matching network devices were found for the given filter criteria.")
                self.total_response.append(self.msg)

            if not fabric_site_ids:
                self.msg = "No fabric sites were retrieved from the Catalyst Center."
                self.total_response.append(self.msg)

            if not fabric_devices:
                self.msg = "No fabric devices found for the given filters."
                self.total_response.append(self.msg)
                break

            else:
                self.total_response.append("The fabric devices filtered from the network devices are: {0}".format(fabric_devices))

            if fabric_info:
                fabric_info_result = self.get_fabric_info(ip_uuid_map, fabric_devices)
                self.total_response.append(fabric_info_result)
                combined_fabric_data["fabric_info"] = fabric_info_result

            if device_issues_info:
                device_issues_result = self.get_device_issues_info(ip_uuid_map, fabric_devices)
                self.total_response.append(device_issues_result)
                combined_fabric_data["device_issues_info"] = device_issues_result

            if device_health_info:
                device_health_result = self.get_device_health_info(fabric_devices)
                self.total_response.append(device_health_result)
                combined_fabric_data["device_health_info"] = device_health_result

            if handoff_info:
                handoff_layer3_sda_result = self.get_handoff_layer3_sda_info(ip_uuid_map, fabric_devices)
                self.total_response.append(handoff_layer3_sda_result)
                combined_fabric_data["handoff_layer3_sda_info"] = handoff_layer3_sda_result

                handoff_layer3_ip_result = self.get_handoff_layer3_ip_info(ip_uuid_map, fabric_devices)
                self.total_response.append(handoff_layer3_ip_result)
                combined_fabric_data["handoff_layer3_ip_info"] = handoff_layer3_ip_result

                handoff_layer2_result = self.get_handoff_layer2_info(ip_uuid_map, fabric_devices)
                self.total_response.append(handoff_layer2_result)
                combined_fabric_data["handoff_layer2_info"] = handoff_layer2_result

            if onboarding_info:
                onboarding_info_result = self.get_onboarding_info(ip_uuid_map, fabric_devices)
                self.total_response.append(onboarding_info_result)
                combined_fabric_data["onboarding_info"] = onboarding_info_result

                ssid_info_result = self.get_ssid_details(fabric_devices, ip_uuid_map)
                self.total_response.append(ssid_info_result)
                combined_fabric_data["ssid_info"] = ssid_info_result

                provision_status_result = self.get_provision_status(ip_uuid_map, fabric_devices)
                self.total_response.append(provision_status_result)
                combined_fabric_data["provision_status_info"] = provision_status_result

            if connected_devices_info:
                connected_devices_result = self.get_connected_device_details_from_interfaces(ip_uuid_map, fabric_devices)
                self.total_response.append(connected_devices_result)
                combined_fabric_data["connected_devices_info"] = connected_devices_result

        if config.get("fabric_devices"):
            file_info = config["fabric_devices"][0].get("file_info")

        if file_info:
            self.write_device_info_to_file({"file_info": file_info})

        if self.total_response:
            self.msg = self.total_response
            self.set_operation_result("success", False, self.msg, "INFO")

        return self

    def get_device_id(self, filtered_config):
        """
        Retrieves device UUIDs from Cisco Catalyst Center based on filtered configuration parameters.

        Args:
            self (object): The class instance interacting with Catalyst Center.
            filtered_config (dict): A dictionary containing filtered device fields such as IPs, hostnames, serial numbers, roles, and types.

        Returns:
            dict: A mapping of device management IP addresses to their corresponding instance UUIDs.

        Description:
            This method processes multiple identifying fields from the provided configuration:
            - ip_address
            - hostname
            - serial_number
            - device_role
            - device_type
            - site_hierarchy

            For each field and its values, the method calls the Catalyst Center 'get_device_list' API to retrieve device details
            and builds an IP-to-UUID mapping.

            If 'site_hierarchy' is provided, the method also queries devices associated with those sites using
            'get_site_id' and 'get_device_ids_from_site', appending additional devices to the result.

            The resulting 'ip_uuid_map' is used later to fetch fabric-related or health-related details for the devices.
        """
        param_keys = [
            "ip_address", "hostname", "serial_number", "device_role", "device_type"
        ]

        param_key_map = {
            "ip_address": "managementIpAddress",
            "hostname": "hostname",
            "serial_number": "serialNumber",
            "device_role": "role",
            "device_type": "type",
        }

        ip_uuid_map = {}
        all_results = []

        timeout = filtered_config.get("timeout", 60)
        retries = filtered_config.get("retries", 3)
        interval = filtered_config.get("interval", 10)

        for field_name in param_keys:
            values = filtered_config.get(field_name, [])
            if not isinstance(values, list) or len(values) == 0:
                self.log("Skipping {0} as it is an empty list".format(field_name))
                continue

            self.log("Processing {0} with values: {1}".format(field_name, values))

            for value in values:
                params = {param_key_map[field_name]: value}
                attempt = 0
                start_time = time.time()

                while attempt < retries and (time.time() - start_time) < timeout:
                    self.log("Attempt {0} - Calling API with params: {1}".format(attempt + 1, params))

                    response = self.dnac._exec(
                        family="devices",
                        function="get_device_list",
                        params=params
                    )
                    self.log("Received API response for {0}={1}: {2}".format(field_name, value, response))

                    devices = response.get("response", [])
                    if devices:
                        for device in devices:
                            uuid = device.get("instanceUuid")
                            ip = device.get("managementIpAddress")
                            if uuid and ip:
                                ip_uuid_map[ip] = uuid
                        break
                    else:
                        self.log("No response data found, retrying in {0} seconds...".format(interval))
                        attempt += 1
                        time.sleep(interval)
                else:
                    msg = "No devices found for {0} = {1}. Data retrieval failed after maximum retries.".format(field_name, value)
                    self.total_response.append(msg)

                all_results.append(response)

        site_paths = filtered_config.get("site_hierarchy", [])

        if isinstance(site_paths, list) and site_paths:
            for site_path in site_paths:
                success, site_id = self.get_site_id(site_path)
                if not success:
                    self.log("Site '{0}' not found – skipping".format(site_path), "WARNING")
                    continue

                response, site_device_ids = self.get_device_ids_from_site(
                    site_path, site_id
                )
                self.log("Devices from site {0}: {1}".format(site_id, site_device_ids))

                if response is not None and isinstance(response, dict):
                    devices = response.get("response", [])

                else:
                    self.log("Invalid or empty response received in get_device_id", "ERROR")
                    devices = None
                if devices:
                    for device in devices:
                        uuid = device.get("deviceId", None)
                        ip = self.get_device_ip_from_id(uuid)
                        if uuid and ip:
                            ip_uuid_map[ip] = uuid
                else:
                    self.log("No response data found")

        self.log("Collected IP to UUID mapping: {0}".format(ip_uuid_map))
        return ip_uuid_map

    def get_device_ip_from_id(self, device_id):
        """
        Retrieve the management IP address of a device from Cisco Catalyst Center using its ID.
        Parameters:
            - self (object): An instance of a class used for interacting with Cisco Catalyst Center.
            - device_id (str): The unique identifier of the device in Cisco Catalyst Center.
        Returns:
            str: The management IP address of the specified device.
        Raises:
            Exception: If there is an error while retrieving the response from Cisco Catalyst Center.
        Description:
            This method queries Cisco Catalyst Center for the device details based on its unique identifier (ID).
            It uses the 'get_device_list' function in the 'devices' family, extracts the management IP address
            from the response, and returns it. If any error occurs during the process, an exception is raised
            with an appropriate error message logged.
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
            self.log(error_message, "ERROR")
            raise Exception(error_message)

    def get_fabric_site_id(self):
        """
        Retrieves a mapping of device IP addresses to UUIDs from Cisco Catalyst Center.

        Args:
            self (object): The class instance interacting with Catalyst Center.
            filtered_config (dict): Filtered device configuration with keys like IP, hostname, serial number, role, type, and site.

        Returns:
            dict: Mapping of management IP addresses to their instance UUIDs.

        Description:
            Queries Catalyst Center using available identifiers (IP, hostname, serial, etc.) and site hierarchy,
            then builds an IP-to-UUID map for all matched devices.
        """
        self.log("Starting to fetch fabric site IDs", "INFO")

        try:
            limit = 500
            offset = 1
            all_sites = []

            while True:
                response = self.dnac._exec(
                    family="sda",
                    function="get_fabric_sites_v1",
                    params={'offset': offset, 'limit': limit}
                )
                self.log("Received API response from 'get_fabric_sites_v1': {0}".format(response), "error")

                if not response:
                    self.msg = "No response received from get_fabric_sites_v1"
                    self.set_operation_result("failed", False, self.msg, "ERROR")

                all_sites.extend(response['response'])

                if len(response['response']) < limit:
                    break

                offset += limit

            fabric_ids = []
            for site_entry in all_sites:
                fabric_id = site_entry.get("id")
                if fabric_id:
                    fabric_ids.append(fabric_id)

        except Exception as api_err:
            self.log("Exception while calling get_fabric_sites_v1 due to {0}".format(api_err), "ERROR")
            self.set_operation_result("failed", False, self.msg, "ERROR").check_return_status()
        return fabric_ids

    def filter_fabric_device(self, ip_uuid_map, filtered_config):
        """
        Identifies fabric devices from a given IP-to-UUID map by querying Cisco Catalyst Center.

        Args:
            self (object): The class instance interacting with Catalyst Center.
            ip_uuid_map (dict): Mapping of device IP addresses to their instance UUIDs.

        Returns:
            list: A list of IP addresses identified as part of a fabric.

        Description:
            For each device UUID, this method queries Catalyst Center's SDA fabric API to check
            if the device belongs to any fabric site. Matches are added to the fabric device list.
        """
        self.log("Starting fabric device filtering with site-role logic", "INFO")

        fabric_site_ids = self.get_fabric_site_id()

        all_fabric_devices = []

        for fabric_id in fabric_site_ids:
            for ip_address, device_uuid in ip_uuid_map.items():
                try:
                    response = self.dnac._exec(
                        family="sda",
                        function="get_fabric_devices_v1",
                        params={"fabric_id": fabric_id, "network_device_id": device_uuid}
                    )
                    self.log("Received API response from 'get_fabric_devices_v1': {0}".format(response), "DEBUG")

                    if response.get("response"):
                        all_fabric_devices.append({
                            "ip": ip_address,
                            "uuid": device_uuid,
                            "fabric_id": fabric_id,
                            "device_roles": response["response"][0].get("deviceRoles", [])
                        })
                except Exception as api_err:
                    self.log("Error checking fabric membership for device {0}: {1}".format(ip_address, api_err), "ERROR")

        total_fabric_count = len(all_fabric_devices)
        self.log("Total fabric devices found: {0}".format(total_fabric_count), "INFO")

        site_hierarchy = filtered_config.get("site_hierarchy", [])
        device_roles_filter = filtered_config.get("device_role", [])

        result_ips = []

        if total_fabric_count > 1000 and site_hierarchy and device_roles_filter:
            self.log("More than 1000 fabric devices and both site/role provided – strict filtering", "INFO")

            site_ids = []
            for site in site_hierarchy:
                success, site_id = self.get_site_id(site)
                if success:
                    site_ids.append(site_id)

            for device in all_fabric_devices:
                device_fabric_id = device.get("fabric_id")
                device_roles = device.get("device_roles", [])
                device_ip = device.get("ip")

                is_in_site = device_fabric_id in site_ids

                has_matching_role = False
                for role in device_roles_filter:
                    if role in device_roles:
                        has_matching_role = True
                        break

                if is_in_site and has_matching_role:
                    result_ips.append(device_ip)

        else:
            self.log("No special filtering required – returning all fabric devices", "INFO")

            for device in all_fabric_devices:
                device_ip = device.get("ip")
                result_ips.append(device_ip)

        unique_result_ip = list(set(result_ips))
        self.log("Filtered fabric devices: {0}".format(unique_result_ip), "INFO")
        return unique_result_ip

    def get_fabric_info(self, ip_uuid_map, fabric_devices):
        """
        Retrieves detailed fabric information for the given list of fabric devices from Cisco Catalyst Center.

        Args:
            self (object): The class instance interacting with Catalyst Center.
            ip_uuid_map (dict): Mapping of device IP addresses to instance UUIDs.
            fabric_devices (list): List of IP addresses identified as fabric devices.

        Returns:
            list: A list containing a single dictionary with fabric information per device.

        Description:
            This method iterates through each fabric site ID and checks which of the provided
            devices (based on IP–UUID mapping) belong to a fabric. For each valid match,
            it calls the Catalyst Center API to retrieve detailed fabric-related attributes.

            The results are aggregated into a list, where each entry contains:
                - 'device_ip': The device's management IP.
                - 'fabric_details': A list of fabric-specific metadata for that device.

        """
        self.log("Starting to fetch fabric info for devices: {0}".format(fabric_devices), "INFO")

        fabric_site_ids = self.get_fabric_site_id()
        all_fabric_info = []

        for fabric_id in fabric_site_ids:
            for ip_address, device_uuid in ip_uuid_map.items():
                if ip_address in fabric_devices:
                    try:
                        response = self.dnac._exec(
                            family="sda",
                            function="get_fabric_devices_v1",
                            params={"fabric_id": fabric_id, "network_device_id": device_uuid}
                        )
                        fabric_data = response.get("response", [])
                        self.log(
                            "Received API response from 'get_fabric_devices_v1' for device {0}: {1}".format(
                                ip_address, response
                            ),
                            "DEBUG"
                        )
                        if fabric_data:
                            all_fabric_info.append({
                                "device_ip": ip_address,
                                "fabric_details": fabric_data
                            })

                    except Exception as api_err:
                        self.msg = "Exception occurred while getting fabric info: {0}".format(api_err)
                        self.set_operation_result("failed", False, self.msg, "ERROR")
                        return None

        result = [{"fabric_info": all_fabric_info}]
        return result

    def get_device_issues_info(self, ip_uuid_map, fabric_devices):
        """
        Retrieves current issue or alert information for fabric devices from Cisco Catalyst Center.

        Args:
            self (object): The class instance interacting with Catalyst Center.
            ip_uuid_map (dict): Mapping of device IP addresses to instance UUIDs.
            fabric_devices (list): List of IP addresses identified as fabric devices.

        Returns:
            list: A list of dictionaries containing issue details per fabric device.

        Description:
            This method loops through the IP-to-UUID mappings and checks if each IP belongs to
            a fabric device. For each match, it queries the Catalyst Center Issues API using
            the device UUID to retrieve current issues or alerts associated with the device.

            The method structures the data into a list of dictionaries, where each dictionary contains:
                - 'device_ip': The IP address of the device.
                - 'issue_details': A list of issue records, or a string stating "No issues found".

        """
        self.log("Starting to fetch issues info for devices: {0}".format(fabric_devices), "INFO")

        all_issue_info = []

        for ip_address, device_uuid in ip_uuid_map.items():
            if ip_address in fabric_devices:
                try:
                    response = self.dnac._exec(
                        family="issues",
                        function="issues_v1",
                        params={"device_id": device_uuid}
                    )
                    issue_data = response.get("response", [])
                    self.log(
                        "Received API response from 'issues_v1' for device {0}: {1}".format(
                            ip_address, response
                        ),
                        "DEBUG"
                    )
                    if issue_data:
                        all_issue_info.append({
                            "device_ip": ip_address,
                            "issue_details": issue_data
                        })

                    else:
                        self.log("No issue data found for device IP: {0}".format(ip_address), "DEBUG")
                        all_issue_info.append({
                            "device_ip": ip_address,
                            "issue_details": "No issues found"
                        })
                        continue

                except Exception as api_err:
                    self.msg = "Exception occurred while getting device issues: {0}".format(api_err)
                    self.set_operation_result("failed", False, self.msg, "ERROR")
                    return None

        result = [{"device_issues_info": all_issue_info}]
        self.log("Aggregated device‑issues info: {0}".format(result), "DEBUG")
        return result

    def get_device_health_info(self, fabric_devices):
        """
        Fetches health metrics for each device in the provided list of fabric device IPs.

        Args:
            self (object): Class instance interacting with Catalyst Center.
            fabric_devices (list): List of IP addresses for fabric devices.

        Returns:
            list: A list containing one dictionary with health details per device.

        Description:
            Calls the API to retrieve health info and filters results
            based on the input IPs. Handles missing data and API errors gracefully.

            The method structures the data into a list of dictionaries, where each dictionary contains:
                - 'device_ip': The IP address of the device.
                - 'health_details': A list containing the health data per device, or a string stating "No health info found".
        """
        self.log("Starting to fetch health info for devices: {0}".format(fabric_devices), "INFO")

        all_health_info = []
        seen_ips = set()
        health_data = []

        try:
            limit = 500
            offset = 1

            while True:
                response = self.dnac._exec(
                    family="devices",
                    function="devices_v1",
                    params={'offset': offset, 'limit': limit}
                )
                self.log("Received API response from 'devices_v1': {0}".format(response), "DEBUG")

                page_data = response.get("response", [])
                health_data.extend(page_data)

                if len(page_data) < limit:
                    break

                offset += limit
            if health_data:
                for device_data in health_data:
                    device_ip = device_data.get("ipAddress")
                    if device_ip in fabric_devices and device_ip not in seen_ips:
                        seen_ips.add(device_ip)
                        self.log(
                            "Processing health data for device {0}: {1}".format(device_ip, device_data),
                            "DEBUG"
                        )
                        all_health_info.append({
                            "device_ip": device_ip,
                            "health_details": device_data
                        })
            else:
                seen_ips.add(device_ip)
                self.log("No health info found for device IP: {0}".format(device_ip), "DEBUG")
                all_health_info.append({
                    "device_ip": device_ip,
                    "health_details": "No health info found"
                })

        except Exception as api_err:
            self.msg = "Exception occurred while getting health info: {0}".format(api_err)
            self.set_operation_result("failed", False, self.msg, "ERROR")
            return None

        result = [{"device_health_info": all_health_info}]
        self.log("Aggregated device-health info: {0}".format(result), "DEBUG")
        return result

    def get_handoff_layer3_sda_info(self, ip_uuid_map, fabric_devices):
        """
        Retrieves Layer 3 SDA handoff information for the given fabric devices.

        Args:
            self (object): The class instance interacting with Catalyst Center.
            ip_uuid_map (dict): Mapping of device IP addresses to instance UUIDs.
            fabric_devices (list): List of IPs identified as fabric devices.

        Returns:
            list: A list containing a dictionary of Layer 3 SDA handoff information per device.

        Description:
            Gathers Layer 3 handoff data with SDA transit for each fabric device.
            Handles both structured data and cases where no handoff information is found.

            The method structures the data into a list of dictionaries, where each dictionary contains:
                - 'device_ip': The IP address of the device.
                - 'handoff_info': A list of Layer 3 handoff records with SDA transit, or a string stating "No handoff info found".
        """
        self.log("Starting to fetch layer3 SDA handoff info for devices: {0}".format(fabric_devices), "INFO")

        fabric_site_ids = self.get_fabric_site_id()
        all_handoff_layer3_sda_info = []
        seen_ips = set()

        for fabric_id in fabric_site_ids:
            for ip_address, device_uuid in ip_uuid_map.items():
                if ip_address in fabric_devices and ip_address not in seen_ips:
                    seen_ips.add(ip_address)
                    try:
                        response = self.dnac._exec(
                            family="sda",
                            function="get_fabric_devices_layer3_handoffs_with_sda_transit_v1",
                            params={"fabric_id": fabric_id, "network_device_id": device_uuid}
                        )
                        layer3_sda_handoff_data = response.get("response", [])
                        self.log(
                            "Received API response for 'get_fabric_devices_layer3_handoffs_with_sda_transit_v1' for IP {0}: {1}".format(
                                ip_address, response
                            ),
                            "DEBUG"
                        )
                        if layer3_sda_handoff_data:
                            all_handoff_layer3_sda_info.append({
                                "device_ip": ip_address,
                                "handoff_info": layer3_sda_handoff_data
                            })

                        else:
                            self.log("No Layer 3 SDA handoff data found for device IP: {0}".format(ip_address), "DEBUG")
                            all_handoff_layer3_sda_info.append({
                                "device_ip": ip_address,
                                "handoff_info": "No handoff info found"
                            })

                    except Exception as api_err:
                        self.msg = "Exception occurred while getting L3 SDA hand-off info: {0}".format(api_err)
                        self.set_operation_result("failed", False, self.msg, "ERROR")
                        return None

        result = [{"fabric_devices_layer3_handoffs_sda_info": all_handoff_layer3_sda_info}]
        self.log("Aggregated L3 SDA hand-off info: {0}".format(result), "DEBUG")
        return result

    def get_handoff_layer3_ip_info(self, ip_uuid_map, fabric_devices):
        """
        Retrieves Layer 3 IP handoff information for the given fabric devices.

        Args:
            self (object): The class instance interacting with Catalyst Center.
            ip_uuid_map (dict): Mapping of device IP addresses to instance UUIDs.
            fabric_devices (list): List of IPs identified as fabric devices.

        Returns:
            list: A list containing a dictionary of Layer 3 IP handoff information per device.

        Description:
            Gathers Layer 3 handoff data with IP transit for each fabric device.
            Handles both structured data and cases where no handoff information is found.
            The method structures the data into a list of dictionaries, where each dictionary contains:
                - 'device_ip': The IP address of the device.
                - 'handoff_info': A list of Layer 3 handoff records with IP transit, or a string stating "No handoff info found".
        """
        self.log("Starting to fetch layer3 IP handoff for devices: {0}".format(fabric_devices), "INFO")

        fabric_site_ids = self.get_fabric_site_id()
        all_handoff_layer3_ip_info = []
        seen_ips = set()

        for fabric_id in fabric_site_ids:
            for ip_address, device_uuid in ip_uuid_map.items():
                if ip_address in fabric_devices and ip_address not in seen_ips:
                    seen_ips.add(ip_address)
                    try:
                        response = self.dnac._exec(
                            family="sda",
                            function="get_fabric_devices_layer3_handoffs_with_ip_transit_v1",
                            params={"fabric_id": fabric_id, "network_device_id": device_uuid}
                        )
                        layer3_ip_handoff_data = response.get("response", [])
                        self.log(
                            "Received API response for 'get_fabric_devices_layer3_handoffs_with_ip_transit_v1' for IP {0}: {1}".format(
                                ip_address, response
                            ),
                            "DEBUG"
                        )
                        if layer3_ip_handoff_data:
                            all_handoff_layer3_ip_info.append({
                                "device_ip": ip_address,
                                "handoff_info": layer3_ip_handoff_data
                            })

                        else:
                            self.log("No Layer 3 IP handoff data found for device IP: {0}".format(ip_address), "DEBUG")
                            all_handoff_layer3_ip_info.append({
                                "device_ip": ip_address,
                                "handoff_info": "No handoff info found"
                            })
                    except Exception as api_err:
                        self.msg = "Exception occurred while getting L3 IP hand-off info: {0}".format(api_err)
                        self.set_operation_result("failed", False, self.msg, "ERROR")
                        return None

        result = [{"fabric_devices_layer3_handoffs_ip_info": all_handoff_layer3_ip_info}]
        self.log("Aggregated L3 IP hand-off info: {0}".format(result), "DEBUG")
        return result

    def get_handoff_layer2_info(self, ip_uuid_map, fabric_devices):
        """
        Retrieves Layer 2 handoff information for the given fabric devices.

        Args:
            self (object): The class instance interacting with Catalyst Center.
            ip_uuid_map (dict): Mapping of device IP addresses to instance UUIDs.
            fabric_devices (list): List of IPs identified as fabric devices.

        Returns:
            list: A list containing a dictionary of Layer 2 handoff information per device.

        Description:
            Gathers Layer 2 handoff data for each fabric device.
            Handles both cases where handoff information is present or absent.

            The method structures the data into a list of dictionaries, where each dictionary contains:
                - 'device_ip': The IP address of the device.
                - 'handoff_info': A list of Layer 2 handoff records, or a string stating "No handoff info found".
        """
        self.log("Starting to fetch layer2 handoff info for devices: {0}".format(fabric_devices), "INFO")

        fabric_site_ids = self.get_fabric_site_id()
        all_handoff_layer2_info = []
        seen_ips = set()

        for fabric_id in fabric_site_ids:
            for ip_address, device_uuid in ip_uuid_map.items():
                if ip_address in fabric_devices and ip_address not in seen_ips:
                    seen_ips.add(ip_address)
                    try:
                        response = self.dnac._exec(
                            family="sda",
                            function="get_fabric_devices_layer2_handoffs_v1",
                            params={"fabric_id": fabric_id, "network_device_id": device_uuid}
                        )
                        layer2_handoff_data = response.get("response", [])
                        self.log(
                            "Received API response for 'get_fabric_devices_layer2_handoffs_v1' for IP {0}: {1}".format(
                                ip_address, response
                            ),
                            "DEBUG"
                        )
                        if layer2_handoff_data:
                            all_handoff_layer2_info.append({
                                "device_ip": ip_address,
                                "handoff_info": layer2_handoff_data
                            })

                        else:
                            self.log("No Layer 2 handoff data found for device IP: {0}".format(ip_address), "DEBUG")
                            all_handoff_layer2_info.append({
                                "device_ip": ip_address,
                                "handoff_info": "No handoff info found"
                            })

                    except Exception as api_err:
                        self.msg = "Exception occurred while getting L2 hand-off info: {0}".format(api_err)
                        self.set_operation_result("failed", False, self.msg, "ERROR")
                        return None

        result = [{"fabric_devices_layer2_handoffs_info": all_handoff_layer2_info}]
        self.log("Aggregated L2 hand-off info: {0}".format(result), "DEBUG")
        return result

    def get_interface_ids_per_device(self, ip_uuid_map, fabric_devices):
        """
        Retrieves interface UUIDs for each fabric device.

        Args:
            ip_uuid_map (dict): Mapping of device IP addresses to UUIDs.
            fabric_devices (list): List of IP addresses identified as fabric devices.

        Returns:
            dict: A mapping of IP addresses to a set of interface UUIDs.
        """
        self.log("Fetching interface IDs for fabric devices: {0}".format(fabric_devices), "INFO")

        device_interfaces_map = {}

        for ip_address, device_id in ip_uuid_map.items():
            if ip_address in fabric_devices:
                try:
                    self.log("Fetching interfaces for device: {0}".format(ip_address), "DEBUG")

                    response = self.dnac._exec(
                        family="devices",
                        function="get_interface_info_by_id",
                        params={"device_id": device_id}
                    )
                    interfaces = response.get("response", [])
                    self.log("Received API response for 'get_interface_info_by_id' for device {0}: {1}".format(ip_address, response), "DEBUG")

                    interface_ids = set()
                    for interface in interfaces:
                        interface_id = interface.get("id")
                        if interface_id:
                            interface_ids.add(interface_id)
                        else:
                            self.log("Skipping interface (no ID found) for device {0}".format(ip_address), "WARNING")

                    device_interfaces_map[ip_address] = interface_ids

                except Exception as e:
                    self.log("Failed to retrieve interfaces for device {0}: {1}".format(ip_address, str(e)), "ERROR")

        return device_interfaces_map

    def get_connected_device_details_from_interfaces(self, ip_uuid_map, fabric_devices):
        """
        Retrieves connected device details for each interface of fabric devices.

        Args:
            ip_uuid_map (dict): Mapping of device IP addresses to UUIDs.
            fabric_devices (list): List of IP addresses identified as fabric devices.

        Returns:
            list: A list of dictionaries containing connected device details per fabric device.
        """
        self.log("Fetching connected device info for fabric devices", "INFO")

        all_connected_info = []
        device_interfaces_map = self.get_interface_ids_per_device(ip_uuid_map, fabric_devices)

        for ip_address, interface_ids in device_interfaces_map.items():
            device_id = ip_uuid_map[ip_address]
            connected_device_details = []

            for interface_id in interface_ids:
                try:
                    response = self.dnac._exec(
                        family="devices",
                        function="get_connected_device_detail",
                        params={
                            "device_uuid": device_id,
                            "interface_uuid": interface_id
                        }
                    )
                    connected_data = response.get("response", {})
                    self.log("Received API response for IP {0}, interface {1}: {2}".format(ip_address, interface_id, response), "DEBUG")

                    if connected_data:
                        if isinstance(connected_data, list):
                            connected_device_details.extend(connected_data)
                        else:
                            connected_device_details.append(connected_data)
                except Exception as e:
                    self.log("Failed to fetch connected device info for {0}:{1} due to {2}".format(ip_address, interface_id, str(e)), "ERROR")

            if connected_device_details:
                all_connected_info.append({
                    "device_ip": ip_address,
                    "connected_device_details": connected_device_details
                })

        result = [{"connected_device_info": all_connected_info}]
        self.log("Final aggregated connected device info: {0}".format(result), "DEBUG")
        return result

    def get_dev_type(self, ip_address):
        """
        Fetches the type of device (wired/wireless)

        Parameters:
          - self: The instance of the class containing the 'config' attribute
                  to be validated.
        Returns:
          The method returns an instance of the class with updated attributes:
          str: The type of the device ('wired' or 'wireless'), or None if the device is
              unrecognized, not present, or an error occurs.
        Example:
          Post creation of the validated input, we use this method to get the
          type of the device.
        """

        # for ip_address, device_id in ip_uuid_map.items():
        #     if ip_address in fabric_devices:
        try:
            dev_response = self.dnac_apply["exec"](
                family="devices",
                function="get_network_device_by_ip",
                params={"ip_address": ip_address},
            )

            self.log(
                "The device response from 'get_network_device_by_ip' API for IP {0} is {1}".format(
                    ip_address, str(dev_response)
                ),
                "DEBUG",
            )

            dev_dict = dev_response.get("response", {})
            if not dev_dict:
                self.log(
                    "Invalid response received from the API 'get_network_device_by_ip'. 'response' is empty or missing.",
                    "WARNING",
                )
                return None

            device_family = dev_dict.get("family")
            if not device_family:
                self.log("Device family is missing in the response.", "WARNING")
                return None

            if device_family == "Wireless Controller":
                device_type = "wireless"
            elif device_family in ["Switches and Hubs", "Routers"]:
                device_type = "wired"
            else:
                device_type = None

            self.log("The device type is {0}".format(device_type), "INFO")

            return device_type
        except Exception as e:
            self.msg = "The Device - {0} not present in the Cisco Catalyst Center.".format(
                ip_address
            )
            self.set_operation_result("failed", False, self.msg, "ERROR")

            return None

    def get_onboarding_info(self, ip_uuid_map, fabric_devices):
        """
        Retrieves onboarding information for devices associated with fabric sites.

        Args:
            self (object): The class instance interacting with Catalyst Center.
            ip_uuid_map (dict): Mapping of device IP addresses to instance UUIDs.
            fabric_site_ids (list): List of site IDs that represent fabric-enabled sites.

        Returns:
            list: A list containing dictionaries with onboarding information per device.

        Description:
            For each site ID in the fabric site list:
            - Fetches the onboarding details of associated devices from Catalyst Center.
            - Maps the results to the corresponding device UUIDs from the provided mapping.
            - If onboarding info is available, it's included in the result.
            - If not, a message indicating missing onboarding info is added.
            - Aggregates and returns all onboarding results in a consistent format.
        """

        self.log("Fetching onboarding info - port assignment details for fabric devices", "error")

        fabric_site_ids = self.get_fabric_site_id()
        all_onboarding_info = []
        self.log("Fabric site IDs retrieved: {0}".format(fabric_site_ids))
        for fabric_id in fabric_site_ids:
            for ip_address, device_uuid in ip_uuid_map.items():
                if ip_address in fabric_devices:
                    try:
                        response = self.dnac._exec(
                            family="sda",
                            function="get_port_assignments_v1",
                            params={"fabric_id": fabric_id, "network_device_id": device_uuid}
                        )
                        onboarding_data = response.get("response", [])
                        self.log(
                            "Received API response from 'get_port_assignments_v1' for device {0}: {1}".format(
                                ip_address, response
                            ),
                            "DEBUG"
                        )
                        if onboarding_data:
                            all_onboarding_info.append({
                                "device_ip": ip_address,
                                "port_details": onboarding_data
                            })

                        else:
                            self.log("No onboarding data found for device IP: {0}".format(ip_address), "DEBUG")
                            all_onboarding_info.append({
                                "device_ip": ip_address,
                                "port_details": "No port assignment details found"
                            })
                            continue

                    except Exception as api_err:
                        self.msg = "Exception occurred while getting port assignment details: {0}".format(api_err)
                        self.set_operation_result("failed", False, self.msg, "ERROR")
                        return None

            result = [{"device_onboarding_info": all_onboarding_info}]
            self.log("Aggregated device‑onboarding info: {0}".format(result), "DEBUG")
            return result

    def get_provision_status(self, ip_uuid_map, fabric_devices):
        """
        Retrieves provisioning status information for each fabric device.

        Args:
            self (object): The class instance interacting with Catalyst Center.
            ip_uuid_map (dict): Mapping of device IP addresses to instance UUIDs.
            fabric_devices (list): List of IP addresses identified as fabric devices.

        Returns:
            list: A list containing a dictionary of provisioning status per device.

        Description:
            For each fabric device:
            - Retrieves the provisioning status from Catalyst Center using the device's IP address.
            - If provisioning info is found, it is added to the result.
            - If not, a message indicating no provisioning info is stored instead.
            - All results are aggregated and returned in a consistent structure.
        """
        self.log("Fetching provision status info for fabric devices: {0}".format(fabric_devices), "INFO")

        all_provision_status_info = []

        for ip_address, device_id in ip_uuid_map.items():
            if ip_address in fabric_devices:
                try:
                    self.log("Fetching provision status for device: {0}".format(ip_address), "DEBUG")
                    self.log(ip_address)
                    response = self.dnac._exec(
                        family="sda",
                        function="get_provisioned_wired_device_v1",
                        params={"device_management_ip_address": ip_address}
                    )
                    provision_data = response
                    self.log("Received API response for device {0}: {1}".format(ip_address, response), "DEBUG")

                    if provision_data:
                        all_provision_status_info.append({
                            "device_ip": ip_address,
                            "provision_status": provision_data
                        })

                    else:
                        self.log("No provisioning status found for device IP: {0}".format(ip_address), "DEBUG")
                        all_provision_status_info.append({
                            "device_ip": ip_address,
                            "provision_status": "No provisioning info found"
                        })

                except Exception as api_err:
                    self.msg = "Exception occurred while fetching provisioning status: {0}".format(api_err)
                    self.set_operation_result("failed", False, self.msg, "ERROR")
                    return None

        result = [{"provision_status_info": all_provision_status_info}]
        self.log("Aggregated provision status info: {0}".format(result), "DEBUG")
        return result

    def get_ssid_details(self, fabric_devices, ip_uuid_map):
        """
        Retrieves SSID details for the given fabric devices, if fabric device is wireless.

        Args:
            self (object): The class instance interacting with Catalyst Center.
            fabric_devices (list): List of IP addresses identified as fabric devices.
            ip_uuid_map (dict): Mapping of device IP addresses to instance UUIDs.

        Returns:
            list: A list containing a dictionary of SSID details per device.

        Description:
            This method fetches SSID information for each fabric device and structures the data
            into a list of dictionaries, where each dictionary contains:
                - 'device_ip': The IP address of the device.
                - 'ssid_details': A list of SSID records, or a string stating "No SSID info found".
        """
        self.log("Starting to fetch SSID details for devices: {0}".format(fabric_devices), "INFO")

        all_ssid_info = []

        for ip_address, device_id in ip_uuid_map.items():
            if ip_address in fabric_devices:
                device_type = self.get_dev_type(ip_address)
                self.log("Device {0} is identified as '{1}'".format(ip_address, device_type), "DEBUG")

                if device_type != "wireless":
                    self.log("Skipping {0} as it is not a wireless device.".format(ip_address), "DEBUG")
                    all_ssid_info.append({
                        "device_ip": ip_address,
                        "ssid_details": "The device is not wireless; therefore, SSID information retrieval is not applicable."
                    })
                    continue

                try:
                    response = self.dnac._exec(
                        family="wireless",
                        function="get_ssid_details_for_specific_wireless_controller_v1",
                        params={"network_device_id": device_id}
                    )
                    ssid_data = response.get("response", [])
                    self.log(
                        "Received API response from 'get_ssid_details_for_specific_wireless_controller_v1' "
                        "for device {0}: {1}".format(ip_address, response),
                        "DEBUG"
                    )
                    all_ssid_info.append({
                        "device_ip": ip_address,
                        "ssid_details": ssid_data if ssid_data else "No SSID info found"
                    })

                except Exception as api_err:
                    self.msg = "Exception occurred while getting SSID details for {0}: {1}".format(
                        ip_address, api_err
                    )
                    self.set_operation_result("failed", False, self.msg, "ERROR")
                    return None

        result = [{"ssid_info": all_ssid_info}]
        self.log("Final aggregated SSID info: {0}".format(result), "DEBUG")
        return result

    def write_device_info_to_file(self, config):
        """
        Writes the collected device info to a specified file in JSON or YAML format.
        Supports appending or overwriting based on file_mode.

        Args:
            self (object): Class instance with total_response and logging methods.
            config (dict): Configuration dictionary containing 'file_info'.

        Behavior:
            - Writes to the file path specified in config['file_info']['file_path'].
            - File format defaults to YAML but can be set to JSON.
            - File mode defaults to overwrite ('w') but can be append ('a').
            - If timestamp is True, inserts a 'Downloaded_at' timestamp inside the file content.
            - Creates directories in the file path if they do not exist.
        """
        file_info = config.get("file_info", {})
        self.log("File info received: {0}".format(file_info), "DEBUG")

        file_path = file_info.get("file_path")
        file_format = file_info.get("file_format", "yaml").lower()
        file_mode = file_info.get("file_mode", "w").lower()
        timestamp_flag = file_info.get("timestamp", False)

        if not file_path:
            self.log("No file_path specified in file_info", "ERROR")
            return self

        full_path_with_ext = "{0}.{1}".format(file_path, file_format)

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

            if timestamp_flag:
                timestamp_entry = {"Downloaded_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S")}
                new_data_with_timestamp = [timestamp_entry] + new_data
            else:
                new_data_with_timestamp = new_data

            if file_mode == "a" and os.path.exists(full_path_with_ext):
                try:
                    with open(full_path_with_ext, "r") as f:
                        if file_format == "json":
                            existing_data = json.load(f)
                        else:
                            existing_data = yaml.safe_load(f)

                        if existing_data is None:
                            existing_data = []
                        elif not isinstance(existing_data, list):
                            existing_data = [existing_data]

                except Exception:
                    self.log("Failed to read existing file.", "WARNING")
                    existing_data = []

                data_to_write = existing_data + new_data_with_timestamp

            else:
                data_to_write = new_data_with_timestamp

            with open(full_path_with_ext, "w") as f:
                if file_format == "json":
                    json.dump(data_to_write, f, indent=2)
                else:
                    yaml.dump(data_to_write, f, default_flow_style=False)

            self.log("Successfully wrote device info to file: {0}".format(full_path_with_ext), "INFO")

        except Exception as e:
            self.log("Failed to write device info to file {0}: {1}".format(full_path_with_ext, e), "ERROR")

        return self


def main():
    """ main entry point for module execution
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
                    'config_verify': {'type': 'bool', "default": True},
                    'dnac_api_task_timeout': {'type': 'int', "default": 1200},
                    'dnac_task_poll_interval': {'type': 'int', "default": 2},
                    'config': {'required': True, 'type': 'list', 'elements': 'dict'},
                    'state': {'default': 'merged', 'choices': ['merged']}
                    }

    module = AnsibleModule(argument_spec=element_spec, supports_check_mode=False)
    ccc_fabric_device_info = FabricDevicesInfo(module)
    state = ccc_fabric_device_info.params.get("state")

    current_version = ccc_fabric_device_info.get_ccc_version()
    min_supported_version = "2.3.7.9"

    if ccc_fabric_device_info.compare_dnac_versions(current_version, min_supported_version) < 0:
        ccc_fabric_device_info.status = "failed"
        ccc_fabric_device_info.msg = (
            "The specified version '{0}' does not support the 'fabric device info workflow' feature. "
            "Supported version(s) start from '{1}' onwards.".format(current_version, min_supported_version)
        )
        ccc_fabric_device_info.log(ccc_fabric_device_info.msg, "ERROR")
        ccc_fabric_device_info.check_return_status()

    if state not in ccc_fabric_device_info.supported_states:
        ccc_fabric_device_info.status = "invalid"
        ccc_fabric_device_info.msg = "State {0} is invalid".format(state)
        ccc_fabric_device_info.check_return_status()

    ccc_fabric_device_info.validate_input().check_return_status()

    for config in ccc_fabric_device_info.validated_config:
        ccc_fabric_device_info.reset_values()
        ccc_fabric_device_info.get_want(config).check_return_status()
        ccc_fabric_device_info.get_diff_state_apply[state](config)

    module.exit_json(**ccc_fabric_device_info.result)


if __name__ == '__main__':
    main()
