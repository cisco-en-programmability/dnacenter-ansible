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
  - Accepts a list of network devices with attributes like IP, hostname, serial number,
    site hierarchy, device type, device role.
  - Filters fabric devices from the list of network devices.
  - Retrieves detailed fabric-specific information for the matched devices from Cisco Catalyst Center.
  - Handles retries, timeouts, and polling intervals for robust data collection.
  - Supports output to a file using the C(file_info) option. Output can be JSON or YAML,
    with user-defined file path, file mode (overwrite or append), and optional timestamp.
  - If C(file_info) is provided, results are written to the file; otherwise, results are
    returned in the Ansible output.
  - This module is tagged as a facts/info module and is safe to use in check mode

version_added: "6.32.0"
extends_documentation_fragment:
  - cisco.dnac.workflow_manager_params

author:
  - Priyadharshini B (@pbalaku2)
  - Madhan Sankaranarayanan (@madhansansel)

options:
  config_verify:
    description: Set to true to verify the Cisco Catalyst Center after applying the playbook config.
    type: bool
    default: false
  state:
    description: The desired state of the configuration after module execution.
    type: str
    choices: ["merged"]
    default: merged
  config:
    description: List of dictionaries containing filters to retrieve the fabric device details.
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
              - Each IP address must be unique.
            type: list
            elements: str
          hostname:
            description:
              - List of hostnames of the devices to check if they are part of the fabric.
              - If fabric, retrieves the corresponding fabric information.
              - Each hostname must be unique.
            type: list
            elements: str
          serial_number:
            description:
              - List of serial numbers of the devices to check if they are part of the fabric.
              - If fabric, retrieves the corresponding fabric information.
              - Each serial number must be unique.
            type: list
            elements: str
          device_role:
            description:
              - List of roles of the devices to check if they are part of the fabric (For example, ACCESS, CORE).
              - If fabric, retrieves the corresponding fabric information.
            type: list
            elements: str
            choices:
              - ACCESS
              - DISTRIBUTION
              - CORE
              - WAN
              - WLC
              - DATA_CENTER
              # Additional options may be found in the API documentation.
          device_type:
            description:
              - List of types of the devices to check if they are part of the fabric.
                (For example, Cisco Catalyst 9300 Switch", "Cisco Catalyst 9130AXE Unified Access Point).
              - If fabric, retrieves the corresponding fabric information.
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
              - Cisco Wireless 9176D1 Access Point
              # Additional options may be found in the API documentation.
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
              - Time in seconds to wait for devices to be found.
            type: int
            default: 60
          retries:
            description:
              - Number of retry attempts in case of failures.
            type: int
            default: 3
          interval:
            description:
              - Time in seconds to wait between retries.
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
              - all  # Retrieve all available information categories for each device.
              - fabric_info  # Retrieve details including fabric ID, device roles.
              - handoff_info  # Retrieve handoff info for only fabric devices with Border Node and Control Plane Node roles, not supported on Edge Nodes.
              - onboarding_info  # Retrieve device onboarding details like provision state, SSID, and port information.
              - connected_devices_info  # Retrieve directly connected neighbor devices details.
              - device_health_info  # Retrieve the device's overall health, including CPU and memory usage.
              - device_issues_info  # Retrieve any issues detected on the device.
          output_file_info:
            description:
              - Optional settings to control output file generation for fabric device information.
              - If provided, the content will be saved to the output file. Else, it will be displayed in the terminal.
              - Use this block to define the file path, format, mode, and timestamp handling.
            type: dict
            suboptions:
              file_path:
                description:
                  - Absolute path to the output file, without extension.
                  - The file extension (.json or .yaml) is added automatically based on C(file_format).
                type: str
                required: true
              file_format:
                description:
                  - Format to save the output data.
                  - Supported formats are json and yaml.
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
- This is a facts/info module, it only retrieves information and does not modify any device or configuration.
- Writing to a local file is for reporting/archival purposes only and does not affect the state of any managed device.

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

# case 1: Retrieves all information for devices that are part of the fabric, from cisco catalyst center.

- name: Get Fabric devices info from Cisco Catalyst Center
  hosts: localhost
  connection: local
  vars_files:
    - "credentials.yml"
  tasks:
    - name: Gather detailed facts for specific fabric devices
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
                output_file_info:
                  file_path: /Users/priyadharshini/Downloads/fabric_device_info
                  file_format: yaml
                  file_mode: a
                  timestamp: true

# case 2: Retrieves specific information for devices that are part of the fabric, from cisco catalyst center.

- name: Get Fabric devices info from Cisco Catalyst Center
  hosts: localhost
  connection: local
  vars_files:
    - "credentials.yml"
  tasks:
    - name: Gather detailed facts for specific fabric devices
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
                output_file_info:
                  file_path: /Users/priyadharshini/Downloads/fabric_device_info
                  file_format: yaml
                  file_mode: a
                  timestamp: true

# case 3: Retrieves all information for devices that are part of the fabric, from cisco catalyst center.

- name: Get Fabric devices info from Cisco Catalyst Center
  hosts: localhost
  connection: local
  vars_files:
    - "credentials.yml"
  tasks:
    - name: Gather detailed facts for specific fabric devices
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
                output_file_info:
                  file_path: /Users/priyadharshini/Downloads/fabric_device_info
                  file_format: yaml
                  file_mode: a
                  timestamp: true
"""

RETURN = r"""

# Case 1: Successfully retrieved fabric information for devices that are part of the fabric, from cisco catalyst center

response_fabric_info:

  description:
    - Fabric information for filtered fabric devices
    - Returned for each fabric device matching the filters.
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

    description:
      - Handoff information for filtered fabric devices.
      - Returned for each fabric device matching the filters.
    returned: always
    type: list

    "sample": {
      "response": [
        "The fabric devices filtered from the network devices are: ['91.1.1.2']",
        [
          {
            "fabric_devices_layer3_handoffs_sda_info": [
              {
                "device_ip": "91.1.1.2",
                "handoff_info": [
                  {
                    "connectedToInternet": true,
                    "fabricId": "6ea62e10-cc4b-4f67-8251-d0939fdd4ad8",
                    "isMulticastOverTransitEnabled": false,
                    "networkDeviceId": "36680b59-39b2-446b-8ceb-5a1e157b5799",
                    "transitNetworkId": "02f92f56-e9c8-4534-b7f1-e06635061de9"
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
                "device_ip": "91.1.1.2",
                "handoff_info": [
                  {
                    "externalConnectivityIpPoolName": "BorderHandOff_sub",
                    "fabricId": "6ea62e10-cc4b-4f67-8251-d0939fdd4ad8",
                    "id": "f10250af-bd72-4175-ad9b-ea2831e74a15",
                    "interfaceName": "TenGigabitEthernet1/0/2",
                    "localIpAddress": "204.1.16.69/30",
                    "localIpv6Address": "2004:1:16::1:0:45/126",
                    "networkDeviceId": "36680b59-39b2-446b-8ceb-5a1e157b5799",
                    "remoteIpAddress": "204.1.16.70/30",
                    "remoteIpv6Address": "2004:1:16::1:0:46/126",
                    "tcpMssAdjustment": 0,
                    "transitNetworkId": "bbf16d41-031b-4061-b9b6-ae75768ae196",
                    "virtualNetworkName": "DEFAULT_VN",
                    "vlanId": 3000
                  },
                  {
                    "externalConnectivityIpPoolName": "BorderHandOff_sub",
                    "fabricId": "6ea62e10-cc4b-4f67-8251-d0939fdd4ad8",
                    "id": "3cd81271-4621-40fd-aac7-8b8499127c0c",
                    "interfaceName": "TenGigabitEthernet1/0/2",
                    "localIpAddress": "204.1.16.73/30",
                    "localIpv6Address": "2004:1:16::1:0:49/126",
                    "networkDeviceId": "36680b59-39b2-446b-8ceb-5a1e157b5799",
                    "remoteIpAddress": "204.1.16.74/30",
                    "remoteIpv6Address": "2004:1:16::1:0:4a/126",
                    "tcpMssAdjustment": 0,
                    "transitNetworkId": "bbf16d41-031b-4061-b9b6-ae75768ae196",
                    "virtualNetworkName": "Fabric_VN",
                    "vlanId": 3001
                  },
                  {
                    "externalConnectivityIpPoolName": "BorderHandOff_sub",
                    "fabricId": "6ea62e10-cc4b-4f67-8251-d0939fdd4ad8",
                    "id": "cdad28e7-8df2-432d-8550-666a9fcfc21c",
                    "interfaceName": "TenGigabitEthernet1/0/2",
                    "localIpAddress": "204.1.16.77/30",
                    "localIpv6Address": "2004:1:16::1:0:4d/126",
                    "networkDeviceId": "36680b59-39b2-446b-8ceb-5a1e157b5799",
                    "remoteIpAddress": "204.1.16.78/30",
                    "remoteIpv6Address": "2004:1:16::1:0:4e/126",
                    "tcpMssAdjustment": 0,
                    "transitNetworkId": "bbf16d41-031b-4061-b9b6-ae75768ae196",
                    "virtualNetworkName": "INFRA_VN",
                    "vlanId": 3002
                  },
                  {
                    "externalConnectivityIpPoolName": "BorderHandOff_sub",
                    "fabricId": "6ea62e10-cc4b-4f67-8251-d0939fdd4ad8",
                    "id": "8711bdb5-7a92-4ab0-a7d7-b4053e1db84c",
                    "interfaceName": "TenGigabitEthernet1/0/2",
                    "localIpAddress": "204.1.16.81/30",
                    "localIpv6Address": "2004:1:16::1:0:51/126",
                    "networkDeviceId": "36680b59-39b2-446b-8ceb-5a1e157b5799",
                    "remoteIpAddress": "204.1.16.82/30",
                    "remoteIpv6Address": "2004:1:16::1:0:52/126",
                    "tcpMssAdjustment": 0,
                    "transitNetworkId": "bbf16d41-031b-4061-b9b6-ae75768ae196",
                    "virtualNetworkName": "IntraSubnet_VN",
                    "vlanId": 3003
                  },
                  {
                    "externalConnectivityIpPoolName": "BorderHandOff_sub",
                    "fabricId": "6ea62e10-cc4b-4f67-8251-d0939fdd4ad8",
                    "id": "66b48881-e72f-44cc-aedb-6819af25bd27",
                    "interfaceName": "TenGigabitEthernet1/0/2",
                    "localIpAddress": "204.1.16.85/30",
                    "localIpv6Address": "2004:1:16::1:0:55/126",
                    "networkDeviceId": "36680b59-39b2-446b-8ceb-5a1e157b5799",
                    "remoteIpAddress": "204.1.16.86/30",
                    "remoteIpv6Address": "2004:1:16::1:0:56/126",
                    "tcpMssAdjustment": 0,
                    "transitNetworkId": "bbf16d41-031b-4061-b9b6-ae75768ae196",
                    "virtualNetworkName": "SGT_Port_test",
                    "vlanId": 3004
                  },
                  {
                    "externalConnectivityIpPoolName": "BorderHandOff_sub",
                    "fabricId": "6ea62e10-cc4b-4f67-8251-d0939fdd4ad8",
                    "id": "6dd7d005-74aa-4762-a59e-1c280a975425",
                    "interfaceName": "TenGigabitEthernet1/0/2",
                    "localIpAddress": "204.1.16.89/30",
                    "localIpv6Address": "2004:1:16::1:0:59/126",
                    "networkDeviceId": "36680b59-39b2-446b-8ceb-5a1e157b5799",
                    "remoteIpAddress": "204.1.16.90/30",
                    "remoteIpv6Address": "2004:1:16::1:0:5a/126",
                    "tcpMssAdjustment": 0,
                    "transitNetworkId": "bbf16d41-031b-4061-b9b6-ae75768ae196",
                    "virtualNetworkName": "VN1",
                    "vlanId": 3005
                  },
                  {
                    "externalConnectivityIpPoolName": "BorderHandOff_sub",
                    "fabricId": "6ea62e10-cc4b-4f67-8251-d0939fdd4ad8",
                    "id": "a13167ae-d900-4048-92a6-0d41bd1bd531",
                    "interfaceName": "TenGigabitEthernet1/0/2",
                    "localIpAddress": "204.1.16.93/30",
                    "localIpv6Address": "2004:1:16::1:0:5d/126",
                    "networkDeviceId": "36680b59-39b2-446b-8ceb-5a1e157b5799",
                    "remoteIpAddress": "204.1.16.94/30",
                    "remoteIpv6Address": "2004:1:16::1:0:5e/126",
                    "tcpMssAdjustment": 0,
                    "transitNetworkId": "bbf16d41-031b-4061-b9b6-ae75768ae196",
                    "virtualNetworkName": "VN2",
                    "vlanId": 3006
                  },
                  {
                    "externalConnectivityIpPoolName": "BorderHandOff_sub",
                    "fabricId": "6ea62e10-cc4b-4f67-8251-d0939fdd4ad8",
                    "id": "932cd9d7-9067-4224-ab1d-922a7cd79b5b",
                    "interfaceName": "TenGigabitEthernet1/0/2",
                    "localIpAddress": "204.1.16.97/30",
                    "localIpv6Address": "2004:1:16::1:0:61/126",
                    "networkDeviceId": "36680b59-39b2-446b-8ceb-5a1e157b5799",
                    "remoteIpAddress": "204.1.16.98/30",
                    "remoteIpv6Address": "2004:1:16::1:0:62/126",
                    "tcpMssAdjustment": 0,
                    "transitNetworkId": "bbf16d41-031b-4061-b9b6-ae75768ae196",
                    "virtualNetworkName": "VN3",
                    "vlanId": 3007
                  },
                  {
                    "externalConnectivityIpPoolName": "BorderHandOff_sub",
                    "fabricId": "6ea62e10-cc4b-4f67-8251-d0939fdd4ad8",
                    "id": "9c09c4a8-5a7f-4b06-ac28-4d895293cfe7",
                    "interfaceName": "TenGigabitEthernet1/0/2",
                    "localIpAddress": "204.1.16.101/30",
                    "localIpv6Address": "2004:1:16::1:0:65/126",
                    "networkDeviceId": "36680b59-39b2-446b-8ceb-5a1e157b5799",
                    "remoteIpAddress": "204.1.16.102/30",
                    "remoteIpv6Address": "2004:1:16::1:0:66/126",
                    "tcpMssAdjustment": 0,
                    "transitNetworkId": "bbf16d41-031b-4061-b9b6-ae75768ae196",
                    "virtualNetworkName": "VN4",
                    "vlanId": 3008
                  },
                  {
                    "externalConnectivityIpPoolName": "BorderHandOff_sub",
                    "fabricId": "6ea62e10-cc4b-4f67-8251-d0939fdd4ad8",
                    "id": "df69abf3-266a-4678-84d2-ca8d9340b4c2",
                    "interfaceName": "TenGigabitEthernet1/0/2",
                    "localIpAddress": "204.1.16.105/30",
                    "localIpv6Address": "2004:1:16::1:0:69/126",
                    "networkDeviceId": "36680b59-39b2-446b-8ceb-5a1e157b5799",
                    "remoteIpAddress": "204.1.16.106/30",
                    "remoteIpv6Address": "2004:1:16::1:0:6a/126",
                    "tcpMssAdjustment": 0,
                    "transitNetworkId": "bbf16d41-031b-4061-b9b6-ae75768ae196",
                    "virtualNetworkName": "VN5",
                    "vlanId": 3009
                  },
                  {
                    "externalConnectivityIpPoolName": "BorderHandOff_sub",
                    "fabricId": "6ea62e10-cc4b-4f67-8251-d0939fdd4ad8",
                    "id": "d95e8a82-7a71-4f4a-a31a-85385c1e1ef8",
                    "interfaceName": "TenGigabitEthernet1/0/2",
                    "localIpAddress": "204.1.16.109/30",
                    "localIpv6Address": "2004:1:16::1:0:6d/126",
                    "networkDeviceId": "36680b59-39b2-446b-8ceb-5a1e157b5799",
                    "remoteIpAddress": "204.1.16.110/30",
                    "remoteIpv6Address": "2004:1:16::1:0:6e/126",
                    "tcpMssAdjustment": 0,
                    "transitNetworkId": "bbf16d41-031b-4061-b9b6-ae75768ae196",
                    "virtualNetworkName": "VN6",
                    "vlanId": 3010
                  },
                  {
                    "externalConnectivityIpPoolName": "BorderHandOff_sub",
                    "fabricId": "6ea62e10-cc4b-4f67-8251-d0939fdd4ad8",
                    "id": "27171568-3f08-4f13-8991-a8904bc7e2a6",
                    "interfaceName": "TenGigabitEthernet1/0/2",
                    "localIpAddress": "204.1.16.113/30",
                    "localIpv6Address": "2004:1:16::1:0:71/126",
                    "networkDeviceId": "36680b59-39b2-446b-8ceb-5a1e157b5799",
                    "remoteIpAddress": "204.1.16.114/30",
                    "remoteIpv6Address": "2004:1:16::1:0:72/126",
                    "tcpMssAdjustment": 0,
                    "transitNetworkId": "bbf16d41-031b-4061-b9b6-ae75768ae196",
                    "virtualNetworkName": "VN7",
                    "vlanId": 3011
                  },
                  {
                    "externalConnectivityIpPoolName": "BorderHandOff_sub",
                    "fabricId": "6ea62e10-cc4b-4f67-8251-d0939fdd4ad8",
                    "id": "bb704a7d-8988-4d8c-80e5-4c02bb9ab042",
                    "interfaceName": "TenGigabitEthernet1/0/2",
                    "localIpAddress": "204.1.16.117/30",
                    "localIpv6Address": "2004:1:16::1:0:75/126",
                    "networkDeviceId": "36680b59-39b2-446b-8ceb-5a1e157b5799",
                    "remoteIpAddress": "204.1.16.118/30",
                    "remoteIpv6Address": "2004:1:16::1:0:76/126",
                    "tcpMssAdjustment": 0,
                    "transitNetworkId": "bbf16d41-031b-4061-b9b6-ae75768ae196",
                    "virtualNetworkName": "WiredVNFB1",
                    "vlanId": 3012
                  },
                  {
                    "externalConnectivityIpPoolName": "BorderHandOff_sub",
                    "fabricId": "6ea62e10-cc4b-4f67-8251-d0939fdd4ad8",
                    "id": "8d814e72-25af-490d-8f69-dec10af9e790",
                    "interfaceName": "TenGigabitEthernet1/0/2",
                    "localIpAddress": "204.1.16.121/30",
                    "localIpv6Address": "2004:1:16::1:0:79/126",
                    "networkDeviceId": "36680b59-39b2-446b-8ceb-5a1e157b5799",
                    "remoteIpAddress": "204.1.16.122/30",
                    "remoteIpv6Address": "2004:1:16::1:0:7a/126",
                    "tcpMssAdjustment": 0,
                    "transitNetworkId": "bbf16d41-031b-4061-b9b6-ae75768ae196",
                    "virtualNetworkName": "WiredVNFBLayer2",
                    "vlanId": 3013
                  },
                  {
                    "externalConnectivityIpPoolName": "BorderHandOff_sub",
                    "fabricId": "6ea62e10-cc4b-4f67-8251-d0939fdd4ad8",
                    "id": "b01aa3a2-61c8-4179-a568-6dcdbafe993f",
                    "interfaceName": "TenGigabitEthernet1/0/2",
                    "localIpAddress": "204.1.16.125/30",
                    "localIpv6Address": "2004:1:16::1:0:7d/126",
                    "networkDeviceId": "36680b59-39b2-446b-8ceb-5a1e157b5799",
                    "remoteIpAddress": "204.1.16.126/30",
                    "remoteIpv6Address": "2004:1:16::1:0:7e/126",
                    "tcpMssAdjustment": 0,
                    "transitNetworkId": "bbf16d41-031b-4061-b9b6-ae75768ae196",
                    "virtualNetworkName": "WiredVNStatic",
                    "vlanId": 3014
                  },
                  {
                    "externalConnectivityIpPoolName": "BorderHandOff_sub",
                    "fabricId": "6ea62e10-cc4b-4f67-8251-d0939fdd4ad8",
                    "id": "a4f61e60-b75c-4bcd-b7c4-e3bd68ec324d",
                    "interfaceName": "TenGigabitEthernet1/0/2",
                    "localIpAddress": "204.1.16.129/30",
                    "localIpv6Address": "2004:1:16::1:0:81/126",
                    "networkDeviceId": "36680b59-39b2-446b-8ceb-5a1e157b5799",
                    "remoteIpAddress": "204.1.16.130/30",
                    "remoteIpv6Address": "2004:1:16::1:0:82/126",
                    "tcpMssAdjustment": 0,
                    "transitNetworkId": "bbf16d41-031b-4061-b9b6-ae75768ae196",
                    "virtualNetworkName": "WirelessVNFB",
                    "vlanId": 3015
                  },
                  {
                    "externalConnectivityIpPoolName": "BorderHandOff_sub",
                    "fabricId": "6ea62e10-cc4b-4f67-8251-d0939fdd4ad8",
                    "id": "43761af5-509f-4d07-9d2c-8b09f6ba2114",
                    "interfaceName": "TenGigabitEthernet1/0/2",
                    "localIpAddress": "204.1.16.133/30",
                    "localIpv6Address": "2004:1:16::1:0:85/126",
                    "networkDeviceId": "36680b59-39b2-446b-8ceb-5a1e157b5799",
                    "remoteIpAddress": "204.1.16.134/30",
                    "remoteIpv6Address": "2004:1:16::1:0:86/126",
                    "tcpMssAdjustment": 0,
                    "transitNetworkId": "bbf16d41-031b-4061-b9b6-ae75768ae196",
                    "virtualNetworkName": "WirelessVNFGuest",
                    "vlanId": 3016
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
                "device_ip": "91.1.1.2",
                "handoff_info": []
              }
            ]
          }
        ]
      ],
      "status": "success"
      }

# Case 3: Successfully retrieved issues for devices that are part of the fabric, from cisco catalyst center

response_device_issues_info:

  description:
    - Issue information for filtered fabric devices.
    - Returned for each fabric device matching the filters.
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
  description:
    - Health information for filtered fabric devices.
    - Returned for each fabric device matching the filters.
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

  description:
    - Connected device information for filtered fabric devices.
    - Returned for each fabric device matching the filters.
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

# Case 6: Successfully retrieved onboarding info for devices that are part of the fabric, from cisco catalyst center

response_onboarding_info:

  description:
    - Onboarding information for filtered fabric devices.
    - Returned for each fabric device matching the filters.
  returned: always
  type: list
  sample: {
    "response": [
      "The fabric devices filtered from the network devices are: ['204.192.5.2']",
      [
        {
          "device_onboarding_info": [
            {
              "device_ip": "204.192.5.2",
              "port_details": []
            }
          ]
        }
      ],
      [
        {
          "ssid_info": [
            {
              "device_ip": "204.192.5.2",
              "ssid_details": [
                {
                  "adminStatus": true,
                  "l2Security": "open",
                  "l3Security": "web_auth",
                  "managed": true,
                  "radioPolicy": "2.4GHz + 5GHz",
                  "ssidName": "ARUBA_SSIDtb17",
                  "wlanId": 28,
                  "wlanProfileName": "ARUBA_SSID_profile"
                },
                {
                  "adminStatus": true,
                  "l2Security": "wpa2_enterprise",
                  "l3Security": "open",
                  "managed": true,
                  "radioPolicy": "2.4GHz + 5GHz + 6GHz",
                  "ssidName": "CiscoSensorProvisioning",
                  "wlanId": 1,
                  "wlanProfileName": "CiscoSensorProvisioning"
                },
                {
                  "adminStatus": true,
                  "l2Security": "open",
                  "l3Security": "open",
                  "managed": true,
                  "radioPolicy": "2.4GHz + 5GHz",
                  "ssidName": "GUEST2tb17",
                  "wlanId": 26,
                  "wlanProfileName": "GUEST2_profile"
                },
                {
                  "adminStatus": true,
                  "l2Security": "open",
                  "l3Security": "web_auth",
                  "managed": true,
                  "radioPolicy": "2.4GHz + 5GHz",
                  "ssidName": "Guest_passthrough_inttb17",
                  "wlanId": 18,
                  "wlanProfileName": "Guest_passthrough_int_profile"
                },
                {
                  "adminStatus": true,
                  "l2Security": "open",
                  "l3Security": "open",
                  "managed": true,
                  "radioPolicy": "2.4GHz",
                  "ssidName": "GUESTtb17",
                  "wlanId": 20,
                  "wlanProfileName": "GUEST_profile"
                },
                {
                  "adminStatus": true,
                  "l2Security": "wpa2_enterprise",
                  "l3Security": "web_auth",
                  "managed": true,
                  "radioPolicy": "2.4GHz + 5GHz",
                  "ssidName": "Guest_webauthinternaltb17",
                  "wlanId": 22,
                  "wlanProfileName": "Guest_webauthinternal_profile"
                },
                {
                  "adminStatus": true,
                  "l2Security": "open",
                  "l3Security": "web_auth",
                  "managed": true,
                  "radioPolicy": "2.4GHz + 5GHz",
                  "ssidName": "Guest_webpassthroughtb17",
                  "wlanId": 19,
                  "wlanProfileName": "Guest_webpassthrough_profile"
                },
                {
                  "adminStatus": true,
                  "l2Security": "open",
                  "l3Security": "open",
                  "managed": true,
                  "radioPolicy": "2.4GHz + 5GHz",
                  "ssidName": "OPENtb17",
                  "wlanId": 23,
                  "wlanProfileName": "OPEN_profile"
                },
                {
                  "adminStatus": true,
                  "l2Security": "wpa2_enterprise",
                  "l3Security": "open",
                  "managed": true,
                  "radioPolicy": "2.4GHz + 5GHz",
                  "ssidName": "posturetb17",
                  "wlanId": 21,
                  "wlanProfileName": "posture_profile"
                },
                {
                  "adminStatus": true,
                  "l2Security": "wpa2_enterprise",
                  "l3Security": "open",
                  "managed": true,
                  "radioPolicy": "2.4GHz + 5GHz",
                  "ssidName": "Radius_ssidtb17",
                  "wlanId": 17,
                  "wlanProfileName": "Radius_ssid_profile"
                },
                {
                  "adminStatus": true,
                  "l2Security": "wpa2_enterprise",
                  "l3Security": "open",
                  "managed": true,
                  "radioPolicy": "2.4GHz + 5GHz",
                  "ssidName": "Random_mactb17",
                  "wlanId": 29,
                  "wlanProfileName": "Random_mac_profile"
                },
                {
                  "adminStatus": true,
                  "l2Security": "wpa2_personal",
                  "l3Security": "open",
                  "managed": true,
                  "radioPolicy": "2.4GHz + 5GHz",
                  "ssidName": "Single5KBandtb17",
                  "wlanId": 27,
                  "wlanProfileName": "Single5KBand_profile"
                },
                {
                  "adminStatus": true,
                  "l2Security": "wpa2_enterprise",
                  "l3Security": "open",
                  "managed": true,
                  "radioPolicy": "2.4GHz + 5GHz",
                  "ssidName": "SSIDDot1XIndiatb17",
                  "wlanId": 30,
                  "wlanProfileName": "SSIDDot1XIndia_profile"
                },
                {
                  "adminStatus": true,
                  "l2Security": "wpa2_enterprise",
                  "l3Security": "open",
                  "managed": true,
                  "radioPolicy": "2.4GHz + 5GHz",
                  "ssidName": "SSIDDUAL BANDtb17",
                  "wlanId": 25,
                  "wlanProfileName": "SSIDDUAL BAND_profile"
                },
                {
                  "adminStatus": false,
                  "l2Security": "wpa2_enterprise",
                  "l3Security": "open",
                  "managed": true,
                  "radioPolicy": "2.4GHz + 5GHz",
                  "ssidName": "SSIDSchedulertb17",
                  "wlanId": 24,
                  "wlanProfileName": "SSIDScheduler_profile"
                }
              ]
            }
          ]
        }
      ],
      [
        {
          "provision_status_info": [
            {
              "device_ip": "204.192.5.2",
              "provision_status": {
                "description": "Wired Provisioned device detail retrieved successfully.",
                "deviceManagementIpAddress": "204.192.5.2",
                "siteNameHierarchy": "Global/USA/SAN JOSE/BLD23",
                "status": "success"
              }
            }
          ]
        }
      ]
    ],
    "status": "success"
    }

# Case 7: Successfully retrieved all info for devices that are part of the fabric, from cisco catalyst center

response_all_info:

  description:
    - All fabric related information for filtered fabric devices.
    - Returned for each fabric device matching the filters.
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
              "handoff_info": []
            }
          ]
        }
      ],
      [
        {
          "fabric_devices_layer3_handoffs_ip_info": [
            {
              "device_ip": "204.1.2.2",
              "handoff_info": []
            }
          ]
        }
      ],
      [
        {
          "fabric_devices_layer2_handoffs_info": [
            {
              "device_ip": "204.1.2.2",
              "handoff_info": []
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

# Case 8: If no fabric devices is found

response_info:

  description:
    - Returned when no fabric devices match the provided filters.
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

try:
    import yaml
except ImportError:
    yaml = None
import time
import os
import json
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
        self.log("Starting playbook configuration validation.", "INFO")

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
                'output_file_info': {
                    'type': 'dict',
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
        self.log("Validating config against config_spec schema.", "DEBUG")
        valid_config, invalid_params = validate_list_of_dicts(
            self.config, config_spec)

        validated_config = []
        dup_ips, dup_hostnames, dup_serials = set(), set(), set()

        if invalid_params:
            self.msg = "Invalid parameters in playbook: {0}".format(invalid_params)
            self.set_operation_result("failed", False, self.msg, "ERROR").check_return_status()

        if not valid_config:
            self.log("Configuration validation failed: {0}".format(valid_config), "ERROR")
            self.set_operation_result("failed", False, self.msg, "ERROR").check_return_status()

        self.log("Configuration validated successfully: {0}".format(valid_config), "INFO")

        for config in self.config:
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

                output_file_info = device.get("output_file_info")

                if output_file_info:
                    if not isinstance(output_file_info, dict):
                        self.msg = "'output_file_info' must be a dictionary. Type found: {0}".format(type(output_file_info))
                        self.set_operation_result("failed", False, self.msg, "ERROR").check_return_status()

                    if "file_path" in output_file_info and not isinstance(output_file_info["file_path"], str):
                        self.msg = "'file_path' in output_file_info must be a string. Type found: {0}".format(type(output_file_info["file_path"]))
                        self.set_operation_result("failed", False, self.msg, "ERROR").check_return_status()

                    if "file_format" in output_file_info and not isinstance(output_file_info["file_format"], str):
                        self.msg = "'file_format' in output_file_info must be a string. Type found: {0}".format(type(output_file_info["file_format"]))
                        self.set_operation_result("failed", False, self.msg, "ERROR").check_return_status()
                        return self

                    if "file_mode" in output_file_info and not isinstance(output_file_info["file_mode"], str):
                        self.msg = "'file_mode' in output_file_info must be a string. Type found: {0}".format(type(output_file_info["file_mode"]))
                        self.set_operation_result("failed", False, self.msg, "ERROR").check_return_status()

                    if "timestamp" in output_file_info and not isinstance(output_file_info["timestamp"], bool):
                        self.msg = "'timestamp' in output_file_info must be a boolean. Type found: {0}".format(type(output_file_info["timestamp"]))
                        self.set_operation_result("failed", False, self.msg, "ERROR").check_return_status()

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
        self.log("Starting desired state preparation with input config: {0}".format(config), "DEBUG")

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

        allowed_output_file_info_keys = {"file_path", "file_format", "file_mode", "timestamp"}
        allowed_file_formats = {"json", "yaml"}
        allowed_file_modes = {"a", "w"}

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

            if "output_file_info" in device:
                output_file_info = device["output_file_info"]
                if output_file_info is None:
                    continue

                for key in output_file_info:
                    if key not in allowed_output_file_info_keys:
                        self.msg = "'{0}' is not a valid key in 'output_file_info'. Allowed keys are: {1}".format(
                            key, sorted(allowed_output_file_info_keys)
                        )
                        self.set_operation_result("failed", False, self.msg, "ERROR").check_return_status()

                    if output_file_info["file_format"] not in allowed_file_formats:
                        self.msg = "'file_format' must be one of: {0}".format(", ".join(sorted(allowed_file_formats)))
                        self.set_operation_result("failed", False, self.msg, "ERROR").check_return_status()

                    if output_file_info["file_mode"] not in allowed_file_modes:
                        self.msg = "'file_mode' must be one of: {0}".format(", ".join(sorted(allowed_file_modes)))
                        self.set_operation_result("failed", False, self.msg, "ERROR").check_return_status()

        self.want = want
        self.log("Desired State (want): {0}".format(self.want), "INFO")
        return self

    def get_diff_merged(self, config):
        """
        Processes the device configuration and retrieves requested information for each fabric device.

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
        self.log("Starting device info retrieval for all device entries", "INFO")

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
            fabric_info:            {0}
            handoff_info:           {1}
            onboarding_info:        {2}
            connected_devices_info: {3}
            device_health_info:     {4}
            device_issues_info:     {5}
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
            fabric_ip_map = self.fabric_id_ip_map(fabric_site_ids, ip_uuid_map, fabric_devices)

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
                self.log("Checking if 'fabric_info' is requested.", "DEBUG")
                self.log("Fetching fabric_info for devices: {0}".format(fabric_devices), "DEBUG")
                fabric_info_result = self.get_fabric_info(ip_uuid_map, fabric_devices)
                self.total_response.append(fabric_info_result)
                combined_fabric_data["fabric_info"] = fabric_info_result

            if device_issues_info:
                self.log("Checking if 'device_issues_info' is requested.", "DEBUG")
                self.log("Fetching device_issues_info for devices: {0}".format(fabric_devices), "DEBUG")
                device_issues_result = self.get_device_issues_info(ip_uuid_map, fabric_devices)
                self.total_response.append(device_issues_result)
                combined_fabric_data["device_issues_info"] = device_issues_result

            if device_health_info:
                self.log("Checking if 'device_health_info' is requested.", "DEBUG")
                self.log("Fetching device_health_info for devices: {0}".format(fabric_devices), "DEBUG")
                device_health_result = self.get_device_health_info(fabric_devices)
                self.total_response.append(device_health_result)
                combined_fabric_data["device_health_info"] = device_health_result

            if handoff_info:
                self.log("Checking if 'handoff_info' is requested.", "DEBUG")
                self.log("Fetching handoff_info for devices: {0}".format(fabric_devices), "DEBUG")
                handoff_layer3_sda_result = self.get_handoff_layer3_sda_info(ip_uuid_map, fabric_ip_map)
                self.total_response.append(handoff_layer3_sda_result)
                combined_fabric_data["handoff_layer3_sda_info"] = handoff_layer3_sda_result

                handoff_layer3_ip_result = self.get_handoff_layer3_ip_info(ip_uuid_map, fabric_ip_map)
                self.total_response.append(handoff_layer3_ip_result)
                combined_fabric_data["handoff_layer3_ip_info"] = handoff_layer3_ip_result

                handoff_layer2_result = self.get_handoff_layer2_info(ip_uuid_map, fabric_ip_map)
                self.total_response.append(handoff_layer2_result)
                combined_fabric_data["handoff_layer2_info"] = handoff_layer2_result

            if onboarding_info:
                self.log("Checking if 'onboarding_info' is requested.", "DEBUG")
                self.log("Fetching onboarding_info for devices: {0}".format(fabric_devices), "DEBUG")
                onboarding_info_result = self.get_onboarding_info(ip_uuid_map, fabric_ip_map)
                self.total_response.append(onboarding_info_result)
                combined_fabric_data["onboarding_info"] = onboarding_info_result

                ssid_info_result = self.get_ssid_details(fabric_devices, ip_uuid_map)
                self.total_response.append(ssid_info_result)
                combined_fabric_data["ssid_info"] = ssid_info_result

                provision_status_result = self.get_provision_status(ip_uuid_map, fabric_devices)
                self.total_response.append(provision_status_result)
                combined_fabric_data["provision_status_info"] = provision_status_result

            if connected_devices_info:
                self.log("Checking if 'connected_devices_info' is requested.", "DEBUG")
                self.log("Fetching connected_devices_info for devices: {0}".format(fabric_devices), "DEBUG")
                connected_devices_result = self.get_connected_device_details_from_interfaces(ip_uuid_map, fabric_devices)
                self.total_response.append(connected_devices_result)
                combined_fabric_data["connected_devices_info"] = connected_devices_result

        if config.get("fabric_devices"):
            output_file_info = config["fabric_devices"][0].get("output_file_info")

        if output_file_info:
            self.log("Writing combined_data to file using file_info: {0}".format(output_file_info), "INFO")
            self.write_device_info_to_file({"output_file_info": output_file_info})

        if self.total_response:
            self.msg = self.total_response
            self.set_operation_result("success", False, self.msg, "INFO")

        return self

    def get_device_id(self, filtered_config):
        """
        Retrieves device UUIDs from Cisco Catalyst Center based on filtered configuration parameters.

        Description:
            This method processes multiple identifying fields from the provided configuration:
            - ip_address
            - hostname
            - serial_number
            - device_role
            - device_type
            - site_hierarchy

            For each field and its values, it calls the Catalyst Center 'get_device_list' API to retrieve device details
            and builds a mapping of management IP addresses to instance UUIDs.

            If 'site_hierarchy' is specified, the method also queries devices under those sites using
            'get_site_id' and 'get_device_ids_from_site', appending any additional devices to the result.

            The resulting 'ip_uuid_map' is used later to fetch fabric, health, or inventory-related information.

        Args:
            self (object): The class instance interacting with Catalyst Center.
            filtered_config (dict): A dictionary containing filter criteria such as IPs, hostnames, serial numbers, roles, and types.

        Returns:
            dict: A mapping of device management IP addresses to their corresponding instance UUIDs.
        """
        self.log("Starting to get device IDs from Cisco Catalyst Center", "DEBUG")

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

        Description:
            This method queries Cisco Catalyst Center for the device details based on its unique identifier (ID).
            It uses the 'get_device_list' function in the 'devices' family, extracts the management IP address
            from the response, and returns it. If any error occurs during the process, an exception is raised
            with an appropriate error message logged.

        Parameters:
            self (object): An instance of a class used for interacting with Cisco Catalyst Center.
            device_id (str): The unique identifier of the device in Cisco Catalyst Center.

        Returns:
            str: The management IP address of the specified device.

        Raises:
            Exception: If there is an error while retrieving the response from Cisco Catalyst Center.
        """

        self.log("Starting to get device IP for device ID: {0}".format(device_id), "DEBUG")

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

    def get_fabric_site_id(self):
        """
        Retrieves a mapping of device IP addresses to UUIDs from Cisco Catalyst Center.

        Description:
            Queries Catalyst Center using available identifiers (IP, hostname, serial, etc.) and site hierarchy,
            then builds an IP-to-UUID map for all matched devices.

        Args:
            self (object): The class instance interacting with Catalyst Center.
            filtered_config (dict): Filtered device configuration with keys like IP, hostname, serial number, role, type, and site.

        Returns:
            dict: Mapping of management IP addresses to their instance UUIDs.
        """

        self.log("Starting to fetch fabric site IDs", "INFO")

        try:
            limit = 500
            offset = 1
            all_sites = []

            while True:
                response = self.dnac._exec(
                    family="sda",
                    function="get_fabric_sites",
                    params={'offset': offset, 'limit': limit}
                )
                self.log("Received API response from 'get_fabric_sites': {0}".format(response), "DEBUG")

                if not response:
                    self.msg = "No response received from get_fabric_sites"
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
            self.log("Exception while calling get_fabric_sites due to {0}".format(api_err), "ERROR")
            self.set_operation_result("failed", False, self.msg, "ERROR").check_return_status()
        return fabric_ids

    def filter_fabric_device(self, ip_uuid_map, filtered_config):
        """
        Identifies fabric devices from a given IP-to-UUID map by querying Cisco Catalyst Center.

        Description:
            For each device UUID, this method queries Catalyst Center's SDA fabric API to check
            if the device belongs to any fabric site. Matches are added to the fabric device list.

        Args:
            self (object): The class instance interacting with Catalyst Center.
            ip_uuid_map (dict): Mapping of device IP addresses to their instance UUIDs.

        Returns:
            list: A list of IP addresses identified as part of a fabric.
        """

        self.log("Starting fabric device filtering with site-role logic", "INFO")

        fabric_site_ids = self.get_fabric_site_id()

        fabric_devices_info_list = []

        for fabric_id in fabric_site_ids:
            for ip_address, device_uuid in ip_uuid_map.items():
                try:
                    response = self.dnac._exec(
                        family="sda",
                        function="get_fabric_devices",
                        params={"fabric_id": fabric_id, "network_device_id": device_uuid}
                    )
                    self.log("Received API response from 'get_fabric_devices': {0}".format(response), "DEBUG")

                    if response.get("response"):
                        fabric_devices_info_list.append({
                            "ip": ip_address,
                            "uuid": device_uuid,
                            "fabric_id": fabric_id,
                            "device_roles": response["response"][0].get("deviceRoles", [])
                        })

                except Exception as api_err:
                    self.log("Error checking fabric membership for device {0}: {1}".format(ip_address, api_err), "ERROR")

        total_fabric_count = len(fabric_devices_info_list)
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

            for device in fabric_devices_info_list:
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

            for device in fabric_devices_info_list:
                device_ip = device.get("ip")
                result_ips.append(device_ip)

        unique_result_ip = list(set(result_ips))
        self.log("Filtered fabric devices: {0}".format(unique_result_ip), "INFO")
        return unique_result_ip

    def fabric_id_ip_map(self, fabric_site_ids, ip_uuid_map, fabric_devices):
        """
        Retrieves the fabric ID for a list of fabric devices.

        Args:
            self (object): The class instance interacting with Catalyst Center.
            fabric_devices (list): List of IP addresses identified as fabric devices.

        Returns:
            list: A list of fabric IDs corresponding to the provided fabric devices.
        """

        self.log("Starting to get fabric IDs for fabric devices: {0}".format(fabric_devices), "DEBUG")
        fabric_ip_map = {}

        for fabric_id in fabric_site_ids:
            for ip_address, device_uuid in ip_uuid_map.items():
                if ip_address in fabric_devices:
                    try:
                        response = self.dnac._exec(
                            family="sda",
                            function="get_fabric_devices",
                            params={"fabric_id": fabric_id, "network_device_id": device_uuid}
                        )
                        self.log(
                            "Received API response from 'get_fabric_devices': {0}".format(response),
                            "DEBUG"
                        )

                        fabric_data = response.get("response", [])
                        if fabric_data:
                            fabric_id_value = fabric_data[0].get("fabricId")
                            if fabric_id_value:
                                fabric_ip_map[ip_address] = fabric_id_value
                                self.log(
                                    "{0} → {1}".format(ip_address, fabric_id_value),
                                    "INFO"
                                )
                        else:
                            self.log(
                                "No response data for IP {0}".format(ip_address),
                                "WARNING"
                            )

                    except Exception as e:
                        self.log(
                            "Error processing IP {0}: {1}".format(ip_address, e),
                            "ERROR"
                        )

        return fabric_ip_map

    def get_fabric_info(self, ip_uuid_map, fabric_devices):
        """
        Retrieves detailed fabric information for the given list of fabric devices from Cisco Catalyst Center.

        Description:
            This method iterates through each fabric site ID and checks which of the provided
            devices (based on IP–UUID mapping) belong to a fabric. For each valid match,
            it calls the Catalyst Center API to retrieve detailed fabric-related attributes.

            The results are aggregated and returned as a structured list of dictionaries.

        Args:
            self (object): The class instance interacting with Catalyst Center.
            ip_uuid_map (dict): Mapping of device IP addresses to instance UUIDs.
            fabric_devices (list): List of IP addresses identified as fabric devices.

        Returns:
            list: A list with a single dictionary:
                [
                    {
                        "fabric_device_info": [
                            {
                                "device_ip": <str>,
                                "fabric_details": <list of fabric-specific metadata or error string>
                            },
                        ]
                    }
                ]
            Returns None if an error occurs during retrieval.
        """
        self.log("Fetching fabric info for {0} devices: {1}".format(len(ip_uuid_map), fabric_devices), "INFO")

        if not fabric_devices:
            self.log("No fabric device IDs provided for fabric info retrieval", "WARNING")
            return [{"fabric_info": []}]

        fabric_site_ids = self.get_fabric_site_id()
        fabric_info_list = []

        for fabric_id in fabric_site_ids:
            for ip_address, device_uuid in ip_uuid_map.items():
                if ip_address in fabric_devices:
                    try:
                        response = self.dnac._exec(
                            family="sda",
                            function="get_fabric_devices",
                            params={"fabric_id": fabric_id, "network_device_id": device_uuid}
                        )
                        fabric_data = response.get("response", [])
                        self.log(
                            "Received API response from 'get_fabric_devices' for device {0}: {1}".format(
                                ip_address, response
                            ),
                            "DEBUG"
                        )

                        if fabric_data:
                            self.log("Fabric details found for device_ip: {0}.".format(ip_address), "INFO")
                            fabric_info_list.append({
                                "device_ip": ip_address,
                                "fabric_details": fabric_data
                            })

                    except Exception as api_err:
                        self.msg = "Exception occurred while getting fabric info for device {0}: {1}".format(ip_address, api_err)
                        self.set_operation_result("failed", False, self.msg, "ERROR")
                        return None

        result = [{"fabric_info": fabric_info_list}]

        self.log("Completed fabric info retrieval for filtered fabric devices. Total devices processed: {0}".format(len(fabric_info_list)), "INFO")
        self.log("Fabric info result: {0}".format(result), "DEBUG")

        return result

    def get_device_issues_info(self, ip_uuid_map, fabric_devices):
        """
        Retrieves current issue or alert information for fabric devices from Cisco Catalyst Center.

        Args:
            self (object): The class instance interacting with Catalyst Center.
            ip_uuid_map (dict): Mapping of device IP addresses to instance UUIDs.
            fabric_devices (list): List of IP addresses identified as fabric devices.

        Description:
            This method loops through the IP-to-UUID mappings and checks if each IP belongs to
            a fabric device. For each match, it queries the Catalyst Center Issues API using
            the device UUID to retrieve current issues or alerts associated with the device.

            The results are structured into a consistent list of dictionaries, each including:
                - 'device_ip': The IP address of the device.
                - 'issue_details': A list of issue records, or a message if no issues are found.

       Returns:
            list: A list with a single dictionary:
                [
                    {
                        "device_issues_info": [
                            {
                                "device_ip": <str>,
                                "issue_details": <list of issue details or error string>
                            },
                            ...
                        ]
                    }
                ]
            Returns None if an exception occurs during any API call.
        """
        self.log("Fetching issue related information for fabric devices: {0}".format(fabric_devices), "INFO")

        if not fabric_devices:
            self.log("No fabric device IDs provided for device issue info retrieval", "WARNING")
            return [{"device_issues_info": []}]

        issue_info_list = []

        for ip_address, device_uuid in ip_uuid_map.items():
            if ip_address in fabric_devices:
                try:
                    response = self.dnac._exec(
                        family="issues",
                        function="issues",
                        params={"device_id": device_uuid}
                    )
                    issue_data = response.get("response", [])
                    self.log(
                        "Received API response from 'issues' for device {0}: {1}".format(
                            ip_address, response
                        ),
                        "DEBUG"
                    )

                    if issue_data:
                        self.log("Issue details found for device_ip: {0}".format(ip_address), "INFO")
                        issue_info_list.append({
                            "device_ip": ip_address,
                            "issue_details": issue_data
                        })

                    else:
                        self.log("No issue data found for device IP: {0}".format(ip_address), "DEBUG")
                        issue_info_list.append({
                            "device_ip": ip_address,
                            "issue_details": []
                        })
                        continue

                except Exception as api_err:
                    self.msg = "Exception occurred while getting device issues for device {0}: {1}".format(ip_address, api_err)
                    self.set_operation_result("failed", False, self.msg, "ERROR")
                    return None

        result = [{"device_issues_info": issue_info_list}]

        self.log("Completed device info retrieval. Total devices processed: {0}".format(len(issue_info_list)), "INFO")
        self.log("Aggregated device‑issues info: {0}".format(result), "DEBUG")

        return result

    def get_device_health_info(self, fabric_devices):
        """
        Fetches health metrics for each device in the provided list of fabric device IPs from Cisco Catalyst Center.

        For each fabric device IP:
        - Retrieves overall health and status metrics such as CPU, memory, device score, etc.
        - Filters and maps the data based on the IPs provided in the fabric_devices list.

        Args:
            self (object): Class instance interacting with Catalyst Center.
            fabric_devices (list): List of IP addresses for fabric devices.

        Description:
            - Makes an API call to fetch all network device health data.
            - Filters the returned data to match the list of input fabric device IPs.
            - If health data is found, it's included in the results.
            - If not, adds a fallback message indicating no health info found for that device.
            - Logs responses and handles any exceptions gracefully.

        Returns:
            list: A list with a single dictionary:
                [
                    {
                        "device_health_info": [
                            {
                                "device_ip": <str>,
                                "health_details": <list of health metrics or error string>
                            },
                        ]
                    }
                ]
            Returns None if an error occurs during retrieval.
        """
        self.log("Fetching fabric device health information for fabric devices: {0}".format(fabric_devices), "INFO")

        if not fabric_devices:
            self.log("No fabric device IDs provided for device health info retrieval", "WARNING")
            return [{"device_health_info": []}]

        health_info_list = []
        seen_ips = set()
        health_data_list = []

        try:
            limit = 500
            offset = 1

            while True:
                response = self.dnac._exec(
                    family="devices",
                    function="devices",
                    params={'offset': offset, 'limit': limit}
                )
                self.log("Received API response from 'devices' for device: {0}".format(response), "DEBUG")

                page_data = response.get("response", [])
                health_data_list.extend(page_data)

                if len(page_data) < limit:
                    break

                offset += limit

            if health_data_list:
                for device_data in health_data_list:
                    device_ip = device_data.get("ipAddress")
                    if device_ip in fabric_devices and device_ip not in seen_ips:
                        seen_ips.add(device_ip)
                        self.log(
                            "Processing health data for device {0}: {1}".format(device_ip, device_data),
                            "DEBUG"
                        )
                        health_info_list.append({
                            "device_ip": device_ip,
                            "health_details": device_data
                        })
            else:
                seen_ips.add(device_ip)
                self.log("No health info found for device: {0}".format(device_ip), "DEBUG")
                health_info_list.append({
                    "device_ip": device_ip,
                    "health_details": {}
                })

        except Exception as api_err:
            self.msg = "Exception occurred while getting health info for device {0}: {1}".format(device_ip, api_err)
            self.set_operation_result("failed", False, self.msg, "ERROR")
            return None

        result = [{"device_health_info": health_info_list}]

        self.log("Completed health info retrieval. Total devices processed: {0}".format(len(health_info_list)), "INFO")
        self.log("Aggregated device-health info: {0}".format(result), "DEBUG")

        return result

    def get_handoff_layer3_sda_info(self, ip_uuid_map, fabric_ip_map):
        """
        Retrieves Layer 3 SDA handoff information for the given fabric devices from Cisco Catalyst Center.

        For each fabric device:
        - Fetches Layer 3 handoff information with SDA transit using the SDA API.
        - Each device handoff details may include routed transit configurations, VLAN, IP, interface mappings, etc.

        Args:
            self (object): The class instance interacting with Catalyst Center.
            ip_uuid_map (dict): Mapping of device IP addresses to instance UUIDs.
            fabric_devices (list): List of IP addresses identified as fabric devices.

        Returns:
            list: A list with a single dictionary:
                [
                    {
                        "fabric_devices_layer3_handoffs_sda_info": [
                            {
                                "device_ip": <str>,
                                "handoff_info": <list of Layer 3 SDA handoff details or error string>
                            },
                        ]
                    }
                ]
            Returns None if an error occurs during retrieval.

        Description:
            - Iterates through fabric-enabled site IDs and retrieves associated device UUIDs.
            - For each device, makes an API call to fetch Layer 3 SDA handoff information.
            - If data is available, adds it under the respective device IP.
            - If no data is found, a message is logged and a default string is added.
            - Aggregates and returns all results in a consistent, structured format.
        """

        self.log("Fetching Layer 3 SDA handoff details for fabric devices", "INFO")

        all_handoff_layer3_sda_list = []
        seen_ips = set()

        for ip_address, device_uuid in ip_uuid_map.items():
            for device_ip, fabric_id in fabric_ip_map.items():
                if ip_address == device_ip and ip_address not in seen_ips:
                    seen_ips.add(ip_address)
                    try:
                        response = self.dnac._exec(
                            family="sda",
                            function="get_fabric_devices_layer3_handoffs_with_sda_transit",
                            params={"fabric_id": fabric_id, "network_device_id": device_uuid}
                        )
                        layer3_sda_handoff_data = response.get("response", [])
                        self.log(layer3_sda_handoff_data)
                        self.log(
                            "Received API response for 'get_fabric_devices_layer3_handoffs_with_sda_transit' for IP {0}: {1}".format(
                                ip_address, response
                            ),
                            "DEBUG"
                        )
                        if layer3_sda_handoff_data:
                            self.log("layer3_sda_handoff_data details found for device_ip: {0}".format(ip_address), "INFO")
                            all_handoff_layer3_sda_list.append({
                                "device_ip": ip_address,
                                "handoff_info": layer3_sda_handoff_data
                            })

                        else:
                            self.log("No Layer 3 SDA handoff data found for device IP: {0}".format(ip_address), "DEBUG")
                            all_handoff_layer3_sda_list.append({
                                "device_ip": ip_address,
                                "handoff_info": []
                            })

                    except Exception as api_err:
                        self.msg = "Exception occurred while getting L3 SDA hand-off info for device {0}: {1}".format(ip_address, api_err)
                        self.set_operation_result("failed", False, self.msg, "ERROR")
                        return None

        result = [{"fabric_devices_layer3_handoffs_sda_info": all_handoff_layer3_sda_list}]

        self.log("Completed L3 SDA hand-off info retrieval. Total devices processed: {0}".format(len(all_handoff_layer3_sda_list)), "INFO")
        self.log("Aggregated L3 SDA hand-off info: {0}".format(result), "DEBUG")

        return result

    def get_handoff_layer3_ip_info(self, ip_uuid_map, fabric_ip_map):
        """
        Retrieves Layer 3 IP handoff information for the given fabric devices from Cisco Catalyst Center.

        For each fabric device:
        - Fetches Layer 3 handoff information with IP transit using the SDA API.
        - Each device handoff details may include VLAN, next-hop IP, interface, VRF, etc.

        Args:
            self (object): The class instance interacting with Catalyst Center.
            ip_uuid_map (dict): Mapping of device IP addresses to instance UUIDs.
            fabric_devices (list): List of IP addresses identified as fabric devices.

        Description:
            - Iterates through fabric-enabled site IDs and their corresponding devices.
            - Calls Catalyst Center SDA API to fetch Layer 3 IP handoff details per device.
            - If data is available, it is added under that device's IP.
            - If not, a string stating [] is returned for that device.
            - Aggregates and returns all results in a consistent structured format.

        Returns:
            list: A list with a single dictionary:
                [
                    {
                        "fabric_devices_layer3_handoffs_ip_info": [
                            {
                                "device_ip": <str>,
                                "handoff_info": <list of Layer 3 IP handoff details or error string>
                            },
                        ]
                    }
                ]
            Returns None if an error occurs during retrieval.
        """

        self.log("Fetching Layer 3 IP handoff details for fabric devices", "INFO")

        all_handoff_layer3_ip_info_list = []
        seen_ips = set()

        for ip_address, device_uuid in ip_uuid_map.items():
            for device_ip, fabric_id in fabric_ip_map.items():
                if ip_address == device_ip and ip_address not in seen_ips:
                    seen_ips.add(ip_address)
                    try:
                        response = self.dnac._exec(
                            family="sda",
                            function="get_fabric_devices_layer3_handoffs_with_ip_transit",
                            params={"fabric_id": fabric_id, "network_device_id": device_uuid}
                        )
                        layer3_ip_handoff_data = response.get("response", [])
                        self.log(
                            "Received API response for 'get_fabric_devices_layer3_handoffs_with_ip_transit' for IP {0}: {1}".format(
                                ip_address, response
                            ),
                            "DEBUG"
                        )
                        if layer3_ip_handoff_data:
                            self.log("Layer 3 IP handoff data found for device IP: {0}".format(ip_address), "INFO")
                            all_handoff_layer3_ip_info_list.append({
                                "device_ip": ip_address,
                                "handoff_info": layer3_ip_handoff_data
                            })

                        else:
                            self.log("No Layer 3 IP handoff data found for device IP: {0}".format(ip_address), "DEBUG")
                            all_handoff_layer3_ip_info_list.append({
                                "device_ip": ip_address,
                                "handoff_info": []
                            })
                    except Exception as api_err:
                        self.msg = "Exception occurred while getting L3 IP hand-off info for device {0}: {1}".format(ip_address, api_err)
                        self.set_operation_result("failed", False, self.msg, "ERROR")
                        return None

        result = [{"fabric_devices_layer3_handoffs_ip_info": all_handoff_layer3_ip_info_list}]

        self.log("Completed L3 IP hand-off info retrieval. Total devices processed: {0}".format(len(all_handoff_layer3_ip_info_list)), "INFO")
        self.log("Aggregated L3 IP hand-off info: {0}".format(result), "DEBUG")

        return result

    def get_handoff_layer2_info(self, ip_uuid_map, fabric_ip_map):
        """
        Retrieves Layer 2 handoff information for the given fabric devices from Cisco Catalyst Center.

        For each fabric device:
        - Fetches Layer 2 handoff information using the Catalyst Center SDA API.
        - Each device's handoff details include handoff type, VLAN, interface, and destination.

        Args:
            self (object): The class instance interacting with Catalyst Center.
            ip_uuid_map (dict): Mapping of device IP addresses to instance UUIDs.
            fabric_devices (list): List of IP addresses identified as fabric devices.

        Description:
            - Iterates over each fabric site ID and its devices.
            - Calls the API to fetch Layer 2 handoff data for devices.
            - If handoff data is found, it is structured and returned per device.
            - If no data is found, a string stating [] is added.
            - The results are aggregated and returned in a standardized format.

        Returns:
            list: A list with a single dictionary:
                [
                    {
                        "fabric_devices_layer2_handoffs_info": [
                            {
                                "device_ip": <str>,
                                "handoff_info": <list of Layer 2 handoff details or error string>
                            },
                        ]
                    }
                ]
            Returns None if an error occurs during retrieval.
        """

        self.log("Fetching Layer 2 handoff details for fabric devices", "INFO")

        all_handoff_layer2_info_list = []
        seen_ips = set()

        for ip_address, device_uuid in ip_uuid_map.items():
            for device_ip, fabric_id in fabric_ip_map.items():
                if ip_address == device_ip and ip_address not in seen_ips:
                    seen_ips.add(ip_address)
                    try:
                        response = self.dnac._exec(
                            family="sda",
                            function="get_fabric_devices_layer2_handoffs",
                            params={"fabric_id": fabric_id, "network_device_id": device_uuid}
                        )
                        layer2_handoff_data = response.get("response", [])
                        self.log(
                            "Received API response for 'get_fabric_devices_layer2_handoffs' for IP {0}: {1}".format(
                                ip_address, response
                            ),
                            "DEBUG"
                        )
                        if layer2_handoff_data:
                            self.log("Layer 2 handoff data found for device IP: {0}".format(ip_address), "INFO")
                            all_handoff_layer2_info_list.append({
                                "device_ip": ip_address,
                                "handoff_info": layer2_handoff_data
                            })

                        else:
                            self.log("No Layer 2 handoff data found for device IP: {0}".format(ip_address), "DEBUG")
                            all_handoff_layer2_info_list.append({
                                "device_ip": ip_address,
                                "handoff_info": []
                            })

                    except Exception as api_err:
                        self.msg = "Exception occurred while getting L2 hand-off info for device {0}: {1}".format(ip_address, api_err)
                        self.set_operation_result("failed", False, self.msg, "ERROR")
                        return None

        result = [{"fabric_devices_layer2_handoffs_info": all_handoff_layer2_info_list}]

        self.log("Completed L2 hand-off info retrieval. Total devices processed: {0}".format(len(all_handoff_layer2_info_list)), "INFO")
        self.log("Aggregated L2 hand-off info: {0}".format(result), "DEBUG")

        return result

    def get_interface_ids_per_device(self, ip_uuid_map, fabric_devices):
        """
        Retrieves interface UUIDs for each fabric device from Cisco Catalyst Center.

        This method uses the IP-to-UUID mapping to request a list of interface identifiers (UUIDs)
        for each fabric device. The data is structured as a dictionary mapping device IP addresses
        to sets of interface UUIDs.

        Args:
            ip_uuid_map (dict): A mapping of device IP addresses to their corresponding instance UUIDs.
            fabric_devices (list): A list of IP addresses representing fabric-enabled network devices.

        Returns:
            dict: A dictionary where each key is a device IP address and each value is a set of interface UUIDs
                  associated with that device. Devices with no interfaces or on exception are skipped or logged.

        Description:
            For each fabric device:
            - Looks up its UUID using the `ip_uuid_map`.
            - Fetches interface data from Catalyst Center using the device UUID.
            - Extracts the interface UUIDs and maps them to the corresponding device IP.
            - Logs and skips interfaces without IDs or in case of API failures.
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
        Retrieve connected device details for each interface of fabric devices.

        This method fetches and aggregates data about devices connected to the interfaces
        of each fabric device. It leverages the device IP-to-UUID mapping to call the appropriate
        API endpoints in Cisco Catalyst Center.

        Args:
            ip_uuid_map (dict): A dictionary mapping device IP addresses to their unique UUIDs.
            fabric_devices (list): List of IP addresses representing fabric-enabled network devices.

        Returns:
            list: A structured list containing dictionaries, each with:
                - 'device_ip': The IP address of the fabric device.
                - 'connected_device_details': A list of connected device information, or a message
                                              indicating no data was found for that device.

        Description:
            For each fabric device in the input list:
            - Retrieves the UUID using the provided IP-to-UUID mapping.
            - Queries Catalyst Center for connected device information on all interfaces.
            - Organizes and returns the results in a consistent format per device.
        """

        self.log("Fetching connected device information for fabric devices: {0}".format(fabric_devices), "INFO")

        if not fabric_devices:
            self.log("No fabric device IDs provided for connected device information retrieval", "WARNING")
            return [{"connected_device_info": []}]

        all_connected_info_list = []
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
                        self.log("Connected device details found for device IP: {0}".format(ip_address), "INFO")
                        if isinstance(connected_data, list):
                            connected_device_details.extend(connected_data)
                        else:
                            connected_device_details.append(connected_data)
                except Exception as e:
                    self.log("Failed to fetch connected device info for {0}: due to {2}".format(ip_address, str(e)), "ERROR")

            if connected_device_details:
                self.log("Connected device details found for device IP: {0}".format(ip_address), "INFO")
                all_connected_info_list.append({
                    "device_ip": ip_address,
                    "connected_device_details": connected_device_details
                })

        result = [{"connected_device_info": all_connected_info_list}]

        self.log("Completed connected device info retrieval. Total devices processed: {0}".format(len(all_connected_info_list)), "INFO")
        self.log("Final aggregated connected device info: {0}".format(result), "DEBUG")

        return result

    def get_dev_type(self, ip_address):
        """
        Fetch the device type (wired or wireless) based on validated device input.

        This method analyzes the device configuration to determine its type.
        It typically checks fields such as role, interface types, or software characteristics
        to infer whether the device is a wired or wireless node.

        Parameters:
            self (object): The instance of the class containing the 'config' or device attributes.

        Returns:
            str: The type of the device:
                - 'wired' for traditional switches, routers, etc.
                - 'wireless' for access points, WLCs, or similar wireless infrastructure.
                Returns None if the device type cannot be determined or if an error occurs.

        Example:
            After validating the input configuration, this method can be used to identify
            whether the device is wired or wireless for appropriate downstream logic.
        """

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

    def get_onboarding_info(self, ip_uuid_map, fabric_ip_map):
        """
        Fetch onboarding details for devices associated with fabric-enabled sites from Cisco Catalyst Center.

        For each fabric site ID, this method retrieves onboarding information for devices in that site.
        It then maps the onboarding details to corresponding device UUIDs using the provided IP-to-UUID mapping.

        Each entry in the returned list contains the device's IP and its onboarding information.

        The retrieved onboarding information may include fields such as:
            - deviceUuid
            - onboardingState (e.g., provisioned, inProgress, failed)
            - role (e.g., Edge, Border)
            - siteHierarchy
            - provisioningStatus
            - errorMessages

        Parameters:
            ip_uuid_map (dict): Mapping of device IP addresses to their instance UUIDs.
            fabric_site_ids (list): List of site IDs that represent fabric-enabled sites.

        Returns:
            list: A list with a single dictionary:
                [
                    {
                        "onboarding_info": [
                            {
                                "device_ip": <str>,
                                "onboarding_details": <list of onboarding records or error string>
                            },
                        ]
                    }
                ]
            Returns None if an error occurs during retrieval.
        """
        self.log("Fetching onboarding records for fabric devices", "INFO")

        all_onboarding_info_list = []

        for device_ip, fabric_id in fabric_ip_map.items():
            for ip_address, device_uuid in ip_uuid_map.items():
                try:
                    response = self.dnac._exec(
                        family="sda",
                        function="get_port_assignments",
                        params={"fabric_id": fabric_id, "network_device_id": device_uuid}
                    )
                    onboarding_data = response.get("response", [])
                    self.log(
                        "Received API response from 'get_port_assignments' for device {0}: {1}".format(
                            ip_address, response
                        ),
                        "DEBUG"
                    )
                    if onboarding_data:
                        self.log("Onboarding data found for device IP: {0}".format(ip_address), "INFO")
                        all_onboarding_info_list.append({
                            "device_ip": ip_address,
                            "port_details": onboarding_data
                        })

                    else:
                        self.log("No onboarding data found for device IP: {0}".format(ip_address), "DEBUG")
                        all_onboarding_info_list.append({
                            "device_ip": ip_address,
                            "port_details": []
                        })
                        continue

                except Exception as api_err:
                    self.msg = "Exception occurred while getting port assignment details for device {0}: {1}".format(ip_address, api_err)
                    self.set_operation_result("failed", False, self.msg, "ERROR")
                    return None

            result = [{"device_onboarding_info": all_onboarding_info_list}]

            self.log("Completed onboarding info retrieval. Total devices processed: {0}".format(len(all_onboarding_info_list)), "INFO")
            self.log("Aggregated device‑onboarding info: {0}".format(result), "DEBUG")

            return result

    def get_provision_status(self, ip_uuid_map, fabric_devices):
        """
        Fetch provisioning status details for fabric-enabled devices from Cisco Catalyst Center.

        For each device identified as a fabric device, this method uses its IP-to-UUID mapping
        to retrieve provisioning status information via Catalyst Center APIs.

        Each entry in the returned list contains the device's IP and its provisioning status, if available.

        The retrieved provisioning status may include key fields such as:
            - deviceRole (e.g., Border Node, Edge Node)
            - provisioningState (e.g., provisioned, failed, in-progress)
            - fabricStatus (e.g., enabled, disabled)
            - siteHierarchy
            - fabricDomain

        Parameters:
            ip_uuid_map (dict): Mapping of device IP addresses to their unique instance UUIDs.
            fabric_devices (list): List of IP addresses identified as fabric-enabled devices.

        Returns:
            list: A list with a single dictionary:
                [
                    {
                        "provisioning_status_info": [
                            {
                                "device_ip": <str>,
                                "provisioning_status_details": <list of provisioning status records or error string>
                            },
                        ]
                    }
                ]
            Returns None if an error occurs during retrieval.
        """

        self.log("Fetching provision status for devices: {0}".format(fabric_devices), "INFO")

        if not fabric_devices:
            self.log("No fabric device IDs provided for provision status information retrieval", "WARNING")
            return [{"provision_status_info": []}]

        all_provision_status_info_list = []

        for ip_address, device_id in ip_uuid_map.items():
            if ip_address in fabric_devices:
                try:
                    self.log("Fetching provision status for device: {0}".format(ip_address), "DEBUG")
                    self.log(ip_address)
                    response = self.dnac._exec(
                        family="sda",
                        function="get_provisioned_wired_device",
                        params={"device_management_ip_address": ip_address}
                    )
                    provision_data = response
                    self.log("Received API response for device {0}: {1}".format(ip_address, response), "DEBUG")

                    if provision_data:
                        all_provision_status_info_list.append({
                            "device_ip": ip_address,
                            "provision_status": provision_data
                        })

                    else:
                        self.log("No provisioning status found for device IP: {0}".format(ip_address), "DEBUG")
                        all_provision_status_info_list.append({
                            "device_ip": ip_address,
                            "provision_status": {}
                        })

                except Exception as api_err:
                    self.msg = "Exception occurred while fetching provisioning status: {0}".format(api_err)
                    self.set_operation_result("failed", False, self.msg, "ERROR")
                    return None

        result = [{"provision_status_info": all_provision_status_info_list}]
        self.log("Aggregated provision status info: {0}".format(result), "DEBUG")
        return result

    def get_ssid_details(self, fabric_devices, ip_uuid_map):
        """
        Fetch SSID details for fabric-enabled wireless devices from Cisco Catalyst Center.

        For each fabric device identified by IP, this method retrieves SSID (wireless network) configuration
        information if the device is a wireless WLC. It uses the provided IP-to-UUID mapping to query Catalyst Center.

        Each entry in the returned list contains the device's IP and its SSID details, if available.

        The retrieved SSID details include key fields such as:
            - ssid_name (e.g., "Corporate_WiFi")
            - wlan_profile_name
            - security_type
            - interface_mappings
            - authentication method
            - VLAN, etc. (depends on the API structure)

        Parameters:
            fabric_devices (list): List of IP addresses identified as fabric-enabled wireless devices.
            ip_uuid_map (dict): Mapping of device IP addresses to their unique instance UUIDs in Catalyst Center.

        Returns:
            list: A list with a single dictionary:
                [
                    {
                        "ssid_info": [
                            {
                                "device_ip": <str>,
                                "ssid_details": <list of SSID details or error string>
                            },
                        ]
                    }
                ]
            Returns None if an error occurs during retrieval.
        """
        self.log("Fetching ssid details for fabric devices: {0}".format(fabric_devices), "INFO")

        if not fabric_devices:
            self.log("No fabric device IDs provided for ssid details information retrieval", "WARNING")
            return [{"ssid_info": []}]

        all_ssid_info_list = []

        for ip_address, device_id in ip_uuid_map.items():
            if ip_address in fabric_devices:
                device_type = self.get_dev_type(ip_address)
                self.log("Device {0} is identified as '{1}'".format(ip_address, device_type), "DEBUG")

                if device_type != "wireless":
                    self.log("Skipping {0} as it is not a wireless device.".format(ip_address), "DEBUG")
                    all_ssid_info_list.append({
                        "device_ip": ip_address,
                        "ssid_details": "The device is not wireless; therefore, SSID information retrieval is not applicable."
                    })
                    continue

                try:
                    response = self.dnac._exec(
                        family="wireless",
                        function="get_ssid_details_for_specific_wireless_controller",
                        params={"network_device_id": device_id}
                    )
                    ssid_data = response.get("response", [])
                    self.log(
                        "Received API response from 'get_ssid_details_for_specific_wireless_controller' "
                        "for device {0}: {1}".format(ip_address, response),
                        "DEBUG"
                    )
                    all_ssid_info_list.append({
                        "device_ip": ip_address,
                        "ssid_details": ssid_data if ssid_data else "No SSID info found"
                    })

                except Exception as api_err:
                    self.msg = "Exception occurred while getting SSID details for device {0}: {1}".format(
                        ip_address, api_err
                    )
                    self.set_operation_result("failed", False, self.msg, "ERROR")
                    return None

        result = [{"ssid_info": all_ssid_info_list}]

        self.log("Completed SSID info retrieval. Total devices processed: {0}".format(len(all_ssid_info_list)), "INFO")
        self.log("Final aggregated SSID info: {0}".format(result), "DEBUG")

        return result

    def write_device_info_to_file(self, config):
        """
        Write collected fabric device information to a specified file with comprehensive format support and error handling.

        This method provides robust file output capabilities for fabric device data with support for multiple
        formats (JSON/YAML), file modes (overwrite/append), automatic directory creation, timestamp insertion,
        and comprehensive error handling with detailed logging for operational traceability.

        Parameters:
            export_configuration (dict): Configuration dictionary containing file output specifications.
                Required structure:
                {
                    "output_output_file_info": {
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
        self.log("Starting Device Information File Export Operation", "INFO")

        output_file_info = config.get("output_file_info", {})
        self.log("File info received: {0}".format(output_file_info), "DEBUG")

        target_file_path = output_file_info.get("file_path")
        output_file_format = output_file_info.get("file_format", "yaml").lower().strip()
        file_write_mode = output_file_info.get("file_mode", "w").lower().strip()
        include_timestamp_flag = output_file_info.get("timestamp", False)

        if not target_file_path:
            self.log("No file_path specified in output_file_info", "ERROR")
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
                timestamp_entry = {"Downloaded_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S")}
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
                    self.log("Failed to read existing file.", "WARNING")
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
                    'config_verify': {'type': 'bool', "default": False},
                    'dnac_api_task_timeout': {'type': 'int', "default": 1200},
                    'dnac_task_poll_interval': {'type': 'int', "default": 2},
                    'config': {'required': True, 'type': 'list', 'elements': 'dict'},
                    'state': {'default': 'merged', 'choices': ['merged']}
                    }

    module = AnsibleModule(argument_spec=element_spec, supports_check_mode=True)
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
