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
  - Accepts a list of network devices with attributes like IP, hostname, serial number,site hierarchy,device type and device role.
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
    description: Set to True to verify the Cisco Catalyst Center after applying the playbook config.
    type: bool
    default: True
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
              - List containing roles of the devices to identify fabric roles (e.g., ACCESS, CORE).
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
          output_file_path:
            description:
              - Specifies the file path where the output should be written.
              - This is a required field.
              - The module writes the final result to the given path in JSON format.
            type: str
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
                site_hierarchy: ["Global/USA/New York/NY_BLD1", "Global/USA/New York/NY_BLD1/FLOOR1"]
                timeout: 60
                retries: 1
                interval: 10
                output_file_path: Users/Priya/Downloads/INFO

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
                site_hierarchy: ["Global/USA/New York/NY_BLD1", "Global/USA/New York/NY_BLD1/FLOOR1"]
                timeout: 30
                retries: 2
                interval: 10
                output_file_path: Users/Priya/Downloads/INFO
                requested_info:
                  - fabric_info
                  - handoff_info
                  - onboarding_info
                  - connected_devices_info
                  - device_health_info
                  - device_issues_info

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
                site_hierarchy: ["Global/USA/New York/NY_BLD1", "Global/USA/New York/NY_BLD1/FLOOR1"]
                timeout: 30
                retries: 3
                interval: 10
                output_file_path: Users/Priya/Downloads/INFO
                requested_info: [all]
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
  returned: None
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
                'output_file_path': {'type': 'str'},
                'requested_info': {
                    'type': 'list',
                    'elements': 'str',
                    'default': [
                        "fabric_info",
                        "handoff_info",
                        "connected_devices_info",
                        "onboarding_info",
                        "device_health_info",
                        "device_issues_info"
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
            if not isinstance(fabric_devices, list):
                self.msg = "'fabric_devices' must be a list"
                self.set_operation_result("failed", False, self.msg, "ERROR")
                return self

            for device in fabric_devices:
                if not isinstance(device, dict):
                    self.msg = "Each fabric device must be a dictionary"
                    self.set_operation_result("failed", False, self.msg, "ERROR")
                    return self

                req_fields = [
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

                for field in req_fields:
                    value = device.get(field, [])
                    if value:
                        if not isinstance(value, list) or not all(isinstance(v, str) for v in value):
                            self.msg = "'{0}' must be a list of strings".format(field)
                            self.set_operation_result("failed", False, self.msg, "ERROR")
                            return self
                if not any(device.get(key) for key in req_fields):
                    self.msg = (
                        "Each fabric device must contain at least one of: {0}."
                        .format(", ".join(req_fields))
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

                for path in device.get("output_file_path", []):
                    if not isinstance(path, str):
                        self.msg = "'output_file_path' must be a string"
                        self.set_operation_result("failed", False, self.msg, "ERROR")
                        return self

                requested_info = device.get("requested_info", [])
                if not isinstance(requested_info, list):
                    self.msg = "'requested_info' must be a list of strings"
                    self.set_operation_result("failed", False, self.msg, "ERROR")
                    return self

                for value_name in requested_info:
                    if not isinstance(value_name, str):
                        self.msg = "Each item in 'requested_info' must be a string"
                        self.set_operation_result("failed", False, self.msg, "ERROR")
                        return self

            validated_config.append(config)

        self.validated_config = validated_config
        self.msg = "Configuration validated successfully"
        self.set_operation_result("success", False, self.msg, "INFO")
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

        if "fabric_devices" not in config or not config["fabric_devices"]:
            self.msg = "Parameter 'fabric_devices' is mandatory and cannot be empty."
            self.set_operation_result("failed", False, self.msg, "ERROR").check_return_status()

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

            if not fabric_site_ids:
                self.msg = "No fabric sites were retrieved from the Catalyst Center."
                self.set_operation_result("failed", False, self.msg, "ERROR").check_return_status()

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

            # if onboarding_info:
            #     onboarding_info_result = self.get_onboarding_info(ip_uuid_map)
            #     self.total_response.append(onboarding_info_result)
            #     combined_fabric_data["onboarding_info"] = onboarding_info_result

            if connected_devices_info:
                connected_devices_result = self.get_connected_device_details_from_interfaces(ip_uuid_map, fabric_devices)
                self.total_response.append(connected_devices_result)
                combined_fabric_data["connected_devices_info"] = connected_devices_result

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
                    self.msg = "No devices found for {0} = {1}. Data retrieval failed after maximum retries.".format(field_name, value)
                    self.total_response.append(self.msg)

                all_results.append(response)

        site_paths = filtered_config.get("site_hierarchy", [])

        if isinstance(site_paths, list) and site_paths:
            for site_path in site_paths:
                success, site_id = self.get_site_id(site_path)
                if not success:
                    self.log("Site '{0}' not found – skipping".format(site_path), "WARNING")
                    continue

                response, site_device_ids = self.get_device_ids_from_site(
                    site_name=None, site_id=site_id
                )
                self.log("Devices from site {0}: {1}".format(site_id, site_device_ids))

                for device in response.get("response", []):
                    uuid = device.get("instanceUuid")
                    ip = device.get("managementIpAddress")
                    if uuid and ip:
                        ip_uuid_map[ip] = uuid

        self.log("Collected IP to UUID mapping: {0}".format(ip_uuid_map))
        return ip_uuid_map

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
                self.log("Received API response from 'get_fabric_sites_v1': {0}".format(response), "DEBUG")

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

        elif total_fabric_count <= 1000 and site_hierarchy and device_roles_filter:
            self.log("Less than 1000 fabric devices and both site/role provided – broad filtering", "INFO")

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

                if is_in_site or has_matching_role:
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

                        if fabric_data:
                            self.log(
                                "Received API response from 'get_fabric_devices_v1' for device {0}: {1}".format(
                                    ip_address, fabric_data
                                ),
                                "DEBUG"
                            )

                            if isinstance(fabric_data, list):
                                all_fabric_info.append({
                                    "device_ip": ip_address,
                                    "fabric_details": fabric_data
                                })
                            else:
                                all_fabric_info.append({
                                    "device_ip": ip_address,
                                    "fabric_details": [fabric_data]
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

                    if issue_data:
                        self.log(
                            "Received device‑issues for IP {0}: {1}".format(ip_address, issue_data),
                            "DEBUG"
                        )

                        if isinstance(issue_data, list):
                            all_issue_info.append({
                                "device_ip": ip_address,
                                "issue_details": issue_data
                            })
                        else:
                            all_issue_info.append({
                                "device_ip": ip_address,
                                "issue_details": [issue_data]
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
                        "health_details": [device_data]
                    })
                elif device_ip in fabric_devices and device_ip not in seen_ips:
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

                        if layer3_sda_handoff_data:
                            self.log(
                                "Received API resoonse for 'get_fabric_devices_layer3_handoffs_with_sda_transit_v1' for IP {0}: {1}".format(
                                    ip_address, layer3_sda_handoff_data
                                ),
                                "DEBUG"
                            )
                            if isinstance(layer3_sda_handoff_data, list):
                                all_handoff_layer3_sda_info.append({
                                    "device_ip": ip_address,
                                    "handoff_info": layer3_sda_handoff_data
                                })
                            else:
                                all_handoff_layer3_sda_info.append({
                                    "device_ip": ip_address,
                                    "handoff_info": [layer3_sda_handoff_data]
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

                        if layer3_ip_handoff_data:
                            self.log(
                                "Received API resoonse for 'get_fabric_devices_layer3_handoffs_with_ip_transit_v1' for IP {0}: {1}".format(
                                    ip_address, layer3_ip_handoff_data
                                ),
                                "DEBUG"
                            )
                            if isinstance(layer3_ip_handoff_data, list):
                                all_handoff_layer3_ip_info.append({
                                    "device_ip": ip_address,
                                    "handoff_info": layer3_ip_handoff_data
                                })
                            else:
                                all_handoff_layer3_ip_info.append({
                                    "device_ip": ip_address,
                                    "handoff_info": [layer3_ip_handoff_data]
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

                        if layer2_handoff_data:
                            self.log(
                                "Received API respnse for 'get_fabric_devices_layer2_handoffs_v1' for IP {0}: {1}".format(
                                    ip_address, layer2_handoff_data
                                ),
                                "DEBUG"
                            )
                            if isinstance(layer2_handoff_data, list):
                                all_handoff_layer2_info.append({
                                    "device_ip": ip_address,
                                    "handoff_info": layer2_handoff_data
                                })
                            else:
                                all_handoff_layer2_info.append({
                                    "device_ip": ip_address,
                                    "handoff_info": [layer2_handoff_data]
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

    def get_connected_device_details_from_interfaces(self, ip_uuid_map, fabric_devices):
        """
        Retrieves and aggregates connected device details for each fabric device based on interface information.

        Args:
            self (object): The class instance interacting with Catalyst Center.
            ip_uuid_map (dict): Mapping of device IP addresses to instance UUIDs.
            fabric_devices (list): List of IP addresses identified as fabric devices.

        Returns:
            list: A list containing a dictionary of connected device details per fabric device.

        Description:
            This method performs the following for each device:
            1. Retrieves interface details using the device UUID.
            2. Extracts unique interface UUIDs from the interface list.
            3. For each interface UUID, fetches connected device information.
            4. Logs and aggregates all connected device data per device.
            5. Returns the results in a structured format under the key 'connected_device_info'.

            The method structures the data into a list of dictionaries, where each dictionary contains:
                - 'device_ip': The IP address of the device.
                - 'connected_device_details': A list of connected device entries retrieved from the device interfaces.
        """
        self.log("Starting to fetch connected device info for devices: {0}".format(fabric_devices), "INFO")

        all_connected_info = []

        for ip_address, device_id in ip_uuid_map.items():
            if ip_address in fabric_devices:
                try:
                    self.log("Fetching interfaces for device: {}".format(ip_address), "DEBUG")
                    response = self.dnac._exec(
                        family="devices",
                        function="get_interface_info_by_id",
                        params={"device_id": device_id}
                    )
                    interfaces = response.get("response", [])
                    self.log("Found interfaces {0} for device: {1}".format(interfaces, ip_address), "DEBUG")

                    unique_interface_uuids = set()
                    for interface in interfaces:
                        interface_id = interface.get("id")
                        if interface_id:
                            unique_interface_uuids.add(interface_id)
                        else:
                            self.log("Skipping interface (no instanceUuid found)", "WARNING")

                    connected_device_details = []

                    for interface_id in unique_interface_uuids:
                        try:
                            connected_response = self.dnac._exec(
                                family="devices",
                                function="get_connected_device_detail",
                                params={
                                    "device_uuid": device_id,
                                    "interface_uuid": interface_id
                                }
                            )
                            connected_data = connected_response.get("response", {})
                            if connected_data:
                                self.log("Received API response for 'get_connected_device_detail' for IP {0}: {1}".format(ip_address, connected_data), "DEBUG")
                                if isinstance(connected_data, list):
                                    connected_device_details.extend(connected_data)
                                else:
                                    connected_device_details.append(connected_data)

                        except Exception as api_err:
                            self.log("Failed to fetch connected device detail for interface id {0}: {1}".format(interface_id, str(api_err)), "ERROR")

                    if connected_device_details:
                        all_connected_info.append({
                            "device_ip": ip_address,
                            "connected_device_details": connected_device_details
                        })

                except Exception as e:
                    self.log("Failed to retrieve interfaces for device {0}: {1}".format(ip_address, str(e)), "ERROR")

        result = [{"connected_device_info": all_connected_info}]
        self.log("Aggregated connected device info: {0}".format(result), "DEBUG")
        return result


def main():
    """ main entry point for module execution
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
