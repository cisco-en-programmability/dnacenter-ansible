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
  Comprehensive fabric device information gathering module for Cisco Catalyst Center with advanced filtering and output capabilities.

description:
  - Retrieves comprehensive fabric device information from Cisco Catalyst Center using flexible, user-defined filtering criteria.
  - Supports device identification through multiple filter types including management IP addresses, hostnames, serial numbers, device roles, device types, and
    site hierarchy locations.
  - Enables selective information retrieval across six categories are fabric configuration details, Layer 2/3 handoff configurations, device onboarding status,
    connected neighbor devices, health metrics, and active issues.
  - Implements robust data collection with configurable retry mechanisms, timeout handling, and polling intervals for reliable operation in enterprise
    environments.
  - Provides flexible file output capabilities using the C(output_file_info) parameter with support for JSON and YAML formats, configurable
    file modes (overwrite or append), and optional timestamp inclusion.
  - When C(output_file_info) is specified, results are written to the designated file. otherwise, results are returned
    in the standard Ansible module output.
  - Returns structured data for each requested information category, or an empty result set when no devices match
    the specified filter criteria after exhausting all retry attempts.
  - Operates as a read-only facts/info module ensuring safe execution in check mode without modifying device configurations.

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
    description: List of dictionaries specifying fabric device query parameters.
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
              - List of management IP addresses to identify fabric devices.
              - Each IP address must be unique within the configuration.
              - Devices matching these IPs will have their fabric information retrieved if they are fabric-enabled.
            type: list
            elements: str
          hostname:
            description:
              - List of device hostnames to identify fabric devices.
              - Each hostname must be unique within the configuration.
              - Devices matching these hostnames will have their fabric information retrieved if they are fabric-enabled.
            type: list
            elements: str
          serial_number:
            description:
              - List of device serial numbers to identify fabric devices.
              - Each serial number must be unique within the configuration.
              - Devices matching these serial numbers will have their fabric information retrieved if they are fabric-enabled.
            type: list
            elements: str
          device_role:
            description:
              - List of device roles to filter fabric devices by their assigned roles.
              - Only devices with matching roles will have their fabric information retrieved.
              - Multiple roles can be specified for broader filtering.
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
              - List of device types to filter fabric devices by their hardware models.
              - Only devices matching these types will have their fabric information retrieved.
              - Device types must match exactly as they appear in Cisco Catalyst Center inventory.
              - Multiple device types can be specified for broader filtering across different hardware models.
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
              - List of site hierarchy paths to filter fabric devices by their site locations.
              - Site paths must follow the full hierarchical structure (e.g., "Global/Region/Building/Floor").
              - Only devices within the specified site hierarchies will have their fabric information retrieved.
              - For large deployments with more than 1000 fabric devices, combining site hierarchy with device roles enables optimized
                filtering for better performance.
              - When both site hierarchy and device roles are specified, filtering behavior depends
                on the total fabric device count for performance optimization.
              - Site hierarchy paths must match exactly as configured in Cisco Catalyst Center's site management structure.
            type: list
            elements: str
          timeout:
            description:
              - Maximum time in seconds to wait for device information retrieval operations to complete.
              - Applied to each individual device lookup operation during the filtering process.
              - If device information retrieval fails within this timeout period, the operation will retry based on the 'retries' parameter.
              - Longer timeouts may be needed for environments with slower network connectivity or larger device inventories.
            type: int
            default: 60
          retries:
            description:
              - Number of retry attempts for device information retrieval operations when initial attempts fail.
              - Applied to each individual device lookup and fabric device filtering operation.
              - Higher retry counts improve reliability in environments with intermittent connectivity or high API load.
              - Total operation time is affected by retries combined with timeout and interval settings.
            type: int
            default: 3
          interval:
            description:
              - Time in seconds to wait between retry attempts for device information retrieval operations.
              - Applied as a delay between failed attempts during device lookup and fabric filtering processes.
              - Longer intervals help reduce API load on Cisco Catalyst Center during retry operations.
              - Should be balanced with timeout settings to avoid excessively long operation times.
            type: int
            default: 10
          requested_info:
            description:
              - List of fabric device information types to retrieve.
              - If set to ['all'], it retrieves all available information.
              - If specific info types are listed, only those will be retrieved.
              - If this parameter is omitted or empty, all information will be retrieved by default.
            type: list
            elements: str
            default: [all]
            choices:
              - all                     # Retrieve all available information categories
              - fabric_info             # Fabric configuration details and device roles
              - handoff_info            # Layer 2/3 handoff configurations (Border and Control Plane nodes only)
              - onboarding_info         # Device provisioning status, port assignments, and SSID details
              - connected_devices_info  # Neighbor device information via CDP/LLDP
              - device_health_info      # Health metrics including CPU, memory, and temperature
              - device_issues_info      # Active alerts and issues detected on the device
          output_file_info:
            description:
              - Controls file output generation for fabric device information retrieval results.
              - When provided, saves retrieved device information to the specified file instead of returning in Ansible output.
              - Supports flexible file formatting, writing modes, and optional timestamp inclusion for audit purposes.
              - Enables automated reporting and data archival workflows for fabric device monitoring operations.
            type: dict
            suboptions:
              file_path:
                description:
                  - Absolute path to the output file without file extension.
                  - File extension is automatically appended based on the selected file format (.json or .yaml).
                type: str
                required: true
              file_format:
                description:
                  - Output data format for the generated file.
                  - Determines file structure and extension applied to the file path.
                  - YAML format provides better readability while JSON offers programmatic parsing advantages.
                type: str
                default: yaml
                choices:
                  - json
                  - yaml
              file_mode:
                description:
                  - File writing mode determining how data is written to the target file.
                  - Use 'w' to overwrite existing file content or 'a' to append new data to existing content.
                  - Append mode enables incremental data collection across multiple playbook runs.
                type: str
                default: w
                choices:
                  - w
                  - a
              timestamp:
                description:
                  - Controls inclusion of retrieval timestamp in the output file content.
                  - When enabled, adds the data collection timestamp as the first entry for audit trail purposes.
                  - Useful for tracking when fabric device information was collected in automated workflows.
                type: bool
                default: false

requirements:
- dnacentersdk >= 2.9.3
- python >= 3.9.19

notes:
- This is a facts/info module that only retrieves information and does not modify any device configurations or network state.
- Writing to a local file is for reporting, archival, and audit purposes only and does not affect the state of any managed devices.
- Module is safe to use in check mode as it performs read-only operations against Cisco Catalyst Center APIs.
- Fabric device filtering automatically identifies SDA fabric-enabled devices from the broader network device inventory.
- For deployments with more than 1000 fabric devices, specifying both site hierarchy and device roles enables
  performance optimization through targeted filtering.
- Device identification supports multiple criteria including IP addresses, hostnames, serial numbers, device roles,
  device types, and site hierarchy locations.
- Information retrieval is optimized based on device capabilities - SSID details are only retrieved for
  wireless controllers, handoff information is role-specific.
- Retry mechanisms with configurable timeout, retry count, and polling intervals ensure reliable
  data collection in enterprise-scale deployments.
- Requires Cisco Catalyst Center version 2.3.7.9 or later for fabric device information retrieval functionality.
- File output supports both JSON and YAML formats with flexible writing modes (overwrite/append) and
  optional timestamp inclusion for audit trails.
- Module handles mixed wired and wireless fabric environments automatically, applying appropriate API calls based on device type detection.

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

# Case 1: Retrieves all information for devices that are part of the fabric, from Cisco Catalyst Center.
- name: Get Fabric device information from Cisco Catalyst Center
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

# Case 2: Retrieves specific information for devices that are part of the fabric, from Cisco Catalyst Center.
- name: Get Fabric device information from Cisco Catalyst Center
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

# Case 3: Retrieves all information for devices that are part of the fabric, from Cisco Catalyst Center.
- name: Get Fabric device information from Cisco Catalyst Center
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

# Case 1: Successfully retrieved fabric information for devices that are part of the fabric, from Cisco Catalyst Center
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

# Case 2: Successfully retrieved handoff info for devices that are part of the fabric, from Cisco Catalyst Center
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

# Case 3: Successfully retrieved issues for devices that are part of the fabric, from Cisco Catalyst Center
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

# Case 4: Successfully retrieved health info for devices that are part of the fabric, from Cisco Catalyst Center
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

# Case 5: Successfully retrieved connected device info for devices that are part of the fabric, from Cisco Catalyst Center
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

# Case 6: Successfully retrieved onboarding info for devices that are part of the fabric, from Cisco Catalyst Center
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

# Case 7: Successfully retrieved all info for devices that are part of the fabric, from Cisco Catalyst Center
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

        if not self.config:
            self.msg = "Configuration is not available in the playbook for validation"
            self.set_operation_result("failed", False, self.msg, "ERROR").check_return_status()

        self.log("Validating configuration structure against schema specification", "DEBUG")

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

        for config in self.config:
            if "fabric_devices" not in config:
                self.msg = "'fabric_devices' key is missing in the config block"
                self.set_operation_result("failed", False, self.msg, "ERROR").check_return_status()

            fabric_devices = config.get("fabric_devices", [])

            self.log("Processing {0} fabric devices for duplicate detection".format(len(fabric_devices)), "DEBUG")

            for device in fabric_devices:
                for ip in device.get("ip_address", []):
                    if ip in dup_ips:
                        self.log("Duplicate ip_address found: {0}".format(ip), "WARNING")
                    dup_ips.add(ip)

                for hostname in device.get("hostname", []):
                    if hostname in dup_hostnames:
                        self.log("Duplicate hostname found: {0}".format(hostname), "WARNING")
                    dup_hostnames.add(hostname)

                for serial in device.get("serial_number", []):
                    if serial in dup_serials:
                        self.log("Duplicate serial_number found: {0}".format(serial), "WARNING")
                    dup_serials.add(serial)

                for numeric in ("timeout", "retries", "interval"):
                    if numeric in device and device[numeric] not in (None, ""):
                        if not isinstance(device[numeric], int) or device[numeric] < 0:
                            self.msg = "'{0}' must be a non-negative integer".format(numeric)
                            self.set_operation_result("failed", False, self.msg, "ERROR").check_return_status()

            self.log("Duplicate detection completed - unique identifiers validated", "DEBUG")

            for device in fabric_devices:
                for numeric in ("timeout", "retries", "interval"):
                    if numeric in device and device[numeric] not in (None, ""):
                        if not isinstance(device[numeric], int) or device[numeric] < 0:
                            self.msg = "'{0}' must be a non-negative integer".format(numeric)
                            self.set_operation_result("failed", False, self.msg, "ERROR").check_return_status()

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

                    if "file_mode" in output_file_info and not isinstance(output_file_info["file_mode"], str):
                        self.msg = "'file_mode' in output_file_info must be a string. Type found: {0}".format(type(output_file_info["file_mode"]))
                        self.set_operation_result("failed", False, self.msg, "ERROR").check_return_status()

                    if "timestamp" in output_file_info and not isinstance(output_file_info["timestamp"], bool):
                        self.msg = "'timestamp' in output_file_info must be a boolean. Type found: {0}".format(type(output_file_info["timestamp"]))
                        self.set_operation_result("failed", False, self.msg, "ERROR").check_return_status()

            validated_config.append(config)

        self.validated_config = validated_config

        self.log("Completed fabric device configuration validation successfully - {0} configurations validated".format(len(validated_config)), "INFO")

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

        for idx, device in enumerate(config["fabric_devices"]):
            self.log("Processing device entry {0}: {1}".format(idx + 1, device), "DEBUG")
            if not any(device.get(key) for key in required_device_keys):
                self.log("Device index {0} missing required identification keys: {1}".format(idx + 1, required_device_keys), "ERROR")
                self.msg = (
                    "Each fabric device must contain at least one of: {0}."
                    .format(", ".join(required_device_keys))
                )
                self.set_operation_result("failed", False, self.msg, "ERROR").check_return_status()

            if "requested_info" in device and device["requested_info"] is not None:
                self.log("Applying requested_info for device index {0}".format(idx + 1), "DEBUG")
                return_value = device["requested_info"]
                for value_name in return_value:
                    if value_name not in allowed_return_values:
                        self.log(
                            "Invalid requested_info '{0}' in device index {1}."
                            "Valid options: {2}".format(value_name, idx, allowed_return_values), "ERROR"
                        )
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
        self.log("Completed desired state preparation. Final state: {0}".format(self.want), "INFO")
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
        self.log("Processing fabric device information retrieval for {0} device configuration entries".format(len(fabric_devices)), "DEBUG")
        combined_fabric_data = {}

        for device_cfg in fabric_devices:
            self.log("Processing device configuration entry with parameters: {0}".format(list(device_cfg.keys())), "DEBUG")
            filtered_config = {}
            for field_name, field_value in device_cfg.items():
                if field_name != "requested_info":
                    filtered_config[field_name] = field_value

            self.log("Filtered config (excluding requested_info): {0}".format(filtered_config), "DEBUG")
            self.log("Extracted device identification parameters: {0}".format(list(filtered_config.keys())), "DEBUG")
            requested_info = device_cfg.get("requested_info", [])

            if not requested_info:
                all_info_requested = True
                self.log("No specific information types requested - retrieving all available information categories", "DEBUG")
            else:
                all_info_requested = "all" in requested_info
                self.log("Specific information types requested: {0}".format(requested_info), "DEBUG")

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

            self.log("Retrieving device UUID mappings and fabric site associations for device identification", "DEBUG")

            ip_uuid_map = self.get_device_id(filtered_config)
            fabric_site_ids = self.get_fabric_site_id()
            fabric_devices = self.filter_fabric_device(ip_uuid_map, filtered_config)
            fabric_ip_map = self.fabric_id_ip_map(fabric_site_ids, ip_uuid_map, fabric_devices)

            if not ip_uuid_map:
                self.msg = "No matching network devices were found for the given filter criteria."
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
                self.log("Retrieving fabric configuration details and device roles for {0} fabric devices".format(len(fabric_devices)), "DEBUG")
                fabric_info_result = self.get_fabric_info(ip_uuid_map, fabric_devices)
                self.total_response.append(fabric_info_result)
                combined_fabric_data["fabric_info"] = fabric_info_result

            if device_issues_info:
                self.log("Retrieving active device issues and alerts for {0} fabric devices".format(len(fabric_devices)), "DEBUG")
                device_issues_result = self.get_device_issues_info(ip_uuid_map, fabric_devices)
                self.total_response.append(device_issues_result)
                combined_fabric_data["device_issues_info"] = device_issues_result

            if device_health_info:
                self.log("Retrieving health metrics and performance data for {0} fabric devices".format(len(fabric_devices)), "DEBUG")
                device_health_result = self.get_device_health_info(fabric_devices)
                self.total_response.append(device_health_result)
                combined_fabric_data["device_health_info"] = device_health_result

            if handoff_info:
                self.log("Retrieving Layer 2/3 handoff configurations for fabric border and control plane nodes", "DEBUG")
                self.log("Retrieving Layer 3 SDA handoff configurations for fabric devices", "DEBUG")
                handoff_layer3_sda_result = self.get_handoff_layer3_sda_info(ip_uuid_map, fabric_ip_map)
                self.total_response.append(handoff_layer3_sda_result)
                combined_fabric_data["handoff_layer3_sda_info"] = handoff_layer3_sda_result

                self.log("Retrieving Layer 3 IP transit handoff configurations for fabric devices", "DEBUG")
                handoff_layer3_ip_result = self.get_handoff_layer3_ip_info(ip_uuid_map, fabric_ip_map)
                self.total_response.append(handoff_layer3_ip_result)
                combined_fabric_data["handoff_layer3_ip_info"] = handoff_layer3_ip_result

                self.log("Retrieving Layer 2 handoff configurations for fabric devices", "DEBUG")
                handoff_layer2_result = self.get_handoff_layer2_info(ip_uuid_map, fabric_ip_map)
                self.total_response.append(handoff_layer2_result)
                combined_fabric_data["handoff_layer2_info"] = handoff_layer2_result

            if onboarding_info:
                self.log("Retrieving device onboarding status and provisioning details for {0} fabric devices".format(len(fabric_devices)), "DEBUG")
                self.log("Retrieving device onboarding and provisioning status information", "DEBUG")
                onboarding_info_result = self.get_onboarding_info(ip_uuid_map, fabric_ip_map, fabric_devices)
                self.total_response.append(onboarding_info_result)
                combined_fabric_data["onboarding_info"] = onboarding_info_result

                self.log("Retrieving SSID configuration details for wireless fabric devices", "DEBUG")
                ssid_info_result = self.get_ssid_details(fabric_devices, ip_uuid_map)
                self.total_response.append(ssid_info_result)
                combined_fabric_data["ssid_info"] = ssid_info_result

                self.log("Retrieving device provision status and deployment state information", "DEBUG")
                provision_status_result = self.get_provision_status(ip_uuid_map, fabric_devices)
                self.total_response.append(provision_status_result)
                combined_fabric_data["provision_status_info"] = provision_status_result

            if connected_devices_info:
                self.log("Retrieving connected neighbor device information via interface for {0} fabric devices".format(len(fabric_devices)), "DEBUG")
                connected_devices_result = self.get_connected_device_details_from_interfaces(ip_uuid_map, fabric_devices)
                self.total_response.append(connected_devices_result)
                combined_fabric_data["connected_devices_info"] = connected_devices_result

        if config.get("fabric_devices"):
            output_file_info = config["fabric_devices"][0].get("output_file_info")

        if output_file_info:
            self.log("Processing file output configuration for fabric device information export: {0}".format(output_file_info), "INFO")
            self.write_device_info_to_file({"output_file_info": output_file_info})
            self.log("Fabric device information successfully written to output file", "INFO")

        if self.total_response:
            self.log("Fabric device information retrieval workflow completed successfully with {0} response entries".format(len(fabric_devices)), "INFO")
            self.msg = self.total_response
            self.set_operation_result("success", False, self.msg, "INFO")

        return self

    def get_device_id(self, filtered_config):
        """
        Fetch device UUIDs from Cisco Catalyst Center based on filtered configuration parameters.

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
        self.log("Initiating device UUID mapping retrieval using multiple identification criteria", "INFO")
        self.log("Device identification parameters: {0}".format([k for k in filtered_config.keys() if filtered_config.get(k)]), "DEBUG")

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

        self.log("Using retry configuration - timeout: {0}s, retries: {1}, interval: {2}s".format(timeout, retries, interval), "DEBUG")
        self.log("Starting device identification using direct parameter lookup for {0} parameter types".format(len(param_keys)), "DEBUG")

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
                device_found = False

                while attempt < retries and (time.time() - start_time) < timeout:
                    self.log("Attempt {0} - Calling API with params: {1}".format(attempt + 1, params))

                    try:
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
                            self.log("Successfully mapped devices to UUID for {0}={1}".format(field_name, value), "DEBUG")
                            device_found = True
                            break
                        else:
                            self.log("No response data found, retrying in {0} seconds...".format(interval))
                            attempt += 1
                            time.sleep(interval)
                    except Exception as e:
                        self.log("API call failed for {0}={1} on attempt {2}: {3}".format(field_name, value, attempt + 1, str(e)), "WARNING")
                        if attempt < retries - 1:
                            time.sleep(interval)

                if not device_found:
                    failure_msg = (
                        "No devices found for {0} = {1} after {2} retry attempts "
                        "within {3} second timeout"
                    ).format(field_name, value, retries, timeout)
                    self.log(failure_msg, "WARNING")
                    self.total_response.append(failure_msg)

                all_results.append(response)

        site_paths = filtered_config.get("site_hierarchy", [])

        if isinstance(site_paths, list) and site_paths:
            self.log("Starting site hierarchy-based device identification for {0} site paths".format(len(site_paths)), "DEBUG")
            for site_path in site_paths:
                self.log("Processing site hierarchy path: {0}".format(site_path), "DEBUG")
                success, site_id = self.get_site_id(site_path)
                if not success:
                    self.log("Site '{0}' not found – skipping".format(site_path), "WARNING")
                    continue
                self.log("Successfully resolved site path '{0}' to site ID: {1}".format(site_path, site_id), "DEBUG")

                response, site_device_ids = self.get_device_ids_from_site(
                    site_path, site_id
                )
                self.log("Devices from site {0}: {1}".format(site_id, site_device_ids))

                if response is not None and isinstance(response, dict):
                    site_devices = response.get("response", [])
                    self.log("Processing {0} devices from site response for UUID mapping".format(len(site_devices)), "DEBUG")
                else:
                    self.log("Invalid or empty response received in get_device_id", "ERROR")
                    site_devices = None

                if site_devices:
                    for device in site_devices:
                        site_devices_mapped = 0
                        device_uuid = device.get("deviceId", None)
                        if device_uuid:
                            management_ip = self.get_device_ip_from_id(device_uuid)

                            if management_ip:
                                ip_uuid_map[management_ip] = device_uuid
                                site_devices_mapped += 1
                    self.log("Successfully mapped {0} devices from site hierarchy '{1}' to IP-UUID pairs".format(site_devices_mapped, site_path), "DEBUG")

                else:
                    self.log("No devices found in site hierarchy '{0}' for UUID mapping".format(site_path), "DEBUG")

        total_mapped_devices = len(ip_uuid_map)
        self.log("Device UUID mapping retrieval completed - successfully mapped {0} unique devices".format(total_mapped_devices), "INFO")

        if total_mapped_devices > 0:
            self.log("Device IP addresses mapped: {0}".format(list(ip_uuid_map.keys())), "DEBUG")
        else:
            self.log("No devices were successfully mapped using the provided identification criteria", "WARNING")

        self.log("Collected IP to UUID mapping: {0}".format(ip_uuid_map))
        return ip_uuid_map

    def get_device_ip_from_id(self, device_id):
        """
        Fetch management IP address of a device from Cisco Catalyst Center using its ID.

        Description:
            This method queries Cisco Catalyst Center for the device details based on its unique identifier (ID).
            It uses the 'get_device_list' function in the 'devices' family, extracts the management IP address
            from the response, and returns it. If any error occurs during the process, an exception is raised
            with an appropriate error message logged.

        Parameters:
            self (object): An instance of a class used for interacting with Cisco Catalyst Center.
            device_id (str): The unique identifier of the device in Cisco Catalyst Center.

        Returns:
            str: The management IP address of the specified device in dotted decimal notation.
                Returns None if the device exists but has no management IP address configured.

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

            device_list = response.get("response", [])
            if not device_list:
                error_message = "No device found in Catalyst Center with ID: {0}".format(device_id)
                self.log(error_message, "WARNING")
                return None

            if len(device_list) == 0:
                error_message = "Empty device response received from Catalyst Center for device ID: {0}".format(device_id)
                self.log(error_message, "WARNING")
                return None

            self.log(
                "Received API response from 'get_device_list': {0}".format(
                    str(response)
                ),
                "DEBUG",
            )
            device_data = device_list[0]
            self.log("Successfully retrieved device data for device ID: {0}".format(device_id), "DEBUG")

            management_ip = device_data.get("managementIpAddress")

            if management_ip:
                self.log("Successfully extracted management IP address: {0} for device: {1}".format(management_ip, device_id), "DEBUG")
                return management_ip
            else:
                self.log("Device {0} found but no management IP address configured".format(device_id), "WARNING")
                return None

        except Exception as e:
            error_message = "Failed to retrieve device IP address from Catalyst Center for device ID {0}: {1}".format(device_id, str(e))
            self.log(error_message, "ERROR")
            self.set_operation_result("failed", False, error_message, "ERROR").check_return_status()

    def get_fabric_site_id(self):
        """
        Retrieve all fabric site identifiers from Cisco Catalyst Center for fabric device operations.

        This method queries the Catalyst Center SDA API to obtain a comprehensive list of all
        fabric site IDs configured in the deployment. It implements pagination to handle large
        fabric deployments and returns the complete set of fabric site identifiers for use
        in subsequent fabric device filtering and information retrieval operations.

        Args:
            self (object): The class instance interacting with Catalyst Center.
            filtered_config (dict): Filtered device configuration with keys like IP, hostname, serial number, role, type, and site.

        Returns:
            list: List of fabric site identifiers (UUIDs) representing all fabric sites
                configured in the Catalyst Center. Returns empty list if no fabric sites
                are configured or if API call fails.
        """
        self.log("Starting to fetch fabric site IDs", "INFO")
        self.log("Retrieving complete fabric site inventory from Catalyst Center SDA configuration", "INFO")

        try:
            limit = 500
            offset = 1
            fabric_sites_data = []

            self.log("Implementing pagination to retrieve all fabric sites with limit: {0}".format(limit), "DEBUG")

            while True:
                self.log("Retrieving fabric sites page with offset: {0}, limit: {1}".format(offset, limit), "DEBUG")
                response = self.dnac._exec(
                    family="sda",
                    function="get_fabric_sites",
                    params={'offset': offset, 'limit': limit}
                )
                self.log("Received API response from 'get_fabric_sites': {0}".format(response), "DEBUG")

                if 'response' not in response:
                    error_message = "Invalid response structure received from fabric sites API - missing 'response' key"
                    self.log(error_message, "ERROR")
                    self.set_operation_result("failed", False, error_message, "ERROR")

                current_page_sites = response['response']
                current_page_count = len(current_page_sites)

                self.log("Retrieved {0} fabric sites in current page (offset: {1})".format(current_page_count, offset), "DEBUG")

                fabric_sites_data.extend(current_page_sites)

                if current_page_count < limit:
                    self.log("Fabric site pagination complete - received {0} sites (less than limit {1})".format(current_page_count, limit), "DEBUG")
                    break

                offset += limit

            self.log("Extracting fabric site identifiers from {0} total fabric sites".format(len(fabric_sites_data)), "DEBUG")
            fabric_ids = []
            for fabric_site in fabric_sites_data:
                fabric_id = fabric_site.get("id")
                if fabric_id:
                    fabric_ids.append(fabric_id)
                else:
                    self.log("Fabric site entry found without ID field - skipping entry", "WARNING")

            self.log("Fabric site inventory retrieval completed - found {0} total fabric sites with valid IDs".format(len(fabric_ids)), "INFO")
            return fabric_ids

        except Exception as api_err:
            self.log("Exception while calling get_fabric_sites due to {0}".format(api_err), "ERROR")
            self.set_operation_result("failed", False, self.msg, "ERROR").check_return_status()

    def filter_fabric_device(self, ip_uuid_map, filtered_config):
        """
        Identify and filter fabric-enabled devices from device inventory using Catalyst Center SDA API.

        This method queries the Catalyst Center SDA fabric API to determine which devices from the
        provided IP-to-UUID mapping are configured as fabric devices. It implements performance
        optimization logic that applies strict site-role filtering when more than 1000 fabric devices
        are detected, and returns all fabric devices otherwise.

        Args:
            self (object): The class instance interacting with Catalyst Center.
            ip_uuid_map (dict): Mapping of device management IP addresses to their instance UUIDs.
                 Format: {"192.168.1.1": "uuid-string", "192.168.1.2": "uuid-string"}
            filtered_config (dict): Configuration containing filtering criteria including:
                - site_hierarchy: List of site hierarchy paths for site-based filtering
                - device_role: List of device roles for role-based filtering
                Used for performance optimization when fabric device count exceeds 1000

        Returns:
            list: List of unique management IP addresses representing devices that are fabric-enabled.
                Returns empty list if no fabric devices are found or if all API calls fail.
                Format: ["192.168.1.1", "192.168.1.2"]
        """
        self.log("Initiating fabric device identification and filtering from device inventory", "INFO")
        self.log("Processing fabric membership verification for {0} devices across fabric sites".format(len(ip_uuid_map)), "DEBUG")

        fabric_site_ids = self.get_fabric_site_id()

        if not fabric_site_ids:
            self.log("No fabric sites found in Catalyst Center - no fabric devices can be identified", "WARNING")
            return []

        self.log("Checking fabric membership across {0} fabric sites for comprehensive device discovery".format(len(fabric_site_ids)), "DEBUG")

        fabric_devices_info_list = []

        for fabric_id in fabric_site_ids:
            self.log("Checking fabric membership for devices in fabric site: {0}".format(fabric_id), "DEBUG")
            for ip_address, device_uuid in ip_uuid_map.items():
                try:
                    response = self.dnac._exec(
                        family="sda",
                        function="get_fabric_devices",
                        params={"fabric_id": fabric_id, "network_device_id": device_uuid}
                    )
                    self.log("Received API response from 'get_fabric_devices': {0}".format(response), "DEBUG")
                    fabric_response_data = response.get("response")
                    if fabric_response_data:
                        device_roles = fabric_response_data[0].get("deviceRoles", [])
                        fabric_devices_info_list.append({
                            "ip": ip_address,
                            "uuid": device_uuid,
                            "fabric_id": fabric_id,
                            "device_roles": device_roles
                        })
                        self.log("Device {0} confirmed as fabric member in site {1} with roles: {2}".format(ip_address, fabric_id, device_roles), "DEBUG")

                except Exception as api_err:
                    self.log("Fabric membership verification failed for device {0} in site {1}: {2}".format(ip_address, fabric_id, str(api_err)), "WARNING")

        total_fabric_count = len(fabric_devices_info_list)
        self.log("Total fabric devices found: {0}".format(total_fabric_count), "INFO")

        site_hierarchy = filtered_config.get("site_hierarchy", [])
        device_roles_filter = filtered_config.get("device_role", [])

        result_ips = []

        if total_fabric_count > 1000 and site_hierarchy and device_roles_filter:
            self.log(
                "Applying performance optimization - fabric device count ({0}) "
                "exceeds 1000 and both site/role filters provided".format(total_fabric_count),
                "INFO"
            )
            self.log("Implementing strict site-role filtering to optimize fabric device selection", "DEBUG")

            site_ids = []
            for site_path in site_hierarchy:
                site_lookup_success, site_id = self.get_site_id(site_path)
                if site_lookup_success:
                    site_ids.append(site_id)
                    self.log("Successfully resolved site path '{0}' to site ID: {1}".format(site_path, site_id), "DEBUG")
                else:
                    self.log("Failed to resolve site hierarchy path '{0}' - excluding from site filtering".format(site_path), "WARNING")

            self.log("Site-role filtering will use {0} resolved site IDs and {1} device roles".format(len(site_ids), len(device_roles_filter)), "DEBUG")

            filtered_devices_count = 0
            for device in fabric_devices_info_list:
                device_fabric_id = device.get("fabric_id")
                device_roles = device.get("device_roles", [])
                device_ip = device.get("ip")

                is_in_specified_site = device_fabric_id in site_ids

                has_matching_role = False
                for role in device_roles_filter:
                    if role in device_roles:
                        has_matching_role = True
                        break

                if is_in_specified_site and has_matching_role:
                    result_ips.append(device_ip)
                    filtered_devices_count += 1
                self.log(
                    "Strict site-role filtering completed - selected {0} devices from {1} total fabric devices".format(
                        filtered_devices_count, total_fabric_count
                    ),
                    "INFO"
                )
        else:
            self.log("No special filtering required – returning all fabric devices", "INFO")

            for device in fabric_devices_info_list:
                device_ip = device.get("ip")
                result_ips.append(device_ip)

        unique_result_ip = list(set(result_ips))
        self.log("Fabric device filtering completed - returning {0} unique fabric device IP addresses".format(len(unique_result_ip)), "INFO")
        return unique_result_ip

    def fabric_id_ip_map(self, fabric_site_ids, ip_uuid_map, fabric_devices):
        """
        Build a mapping of fabric device IP addresses to their corresponding fabric site identifiers.

        This method creates a comprehensive mapping between fabric device management IP addresses
        and their associated fabric site IDs by querying the Catalyst Center SDA API. The mapping
        is essential for subsequent fabric-specific operations like handoff configuration retrieval,
        onboarding status checks, and fabric device management tasks.

        Args:
            fabric_site_ids (list): List of fabric site identifiers (UUIDs) to query for device membership.
                These represent all configured fabric sites in the Catalyst Center.
            ip_uuid_map (dict): Mapping of device management IP addresses to their instance UUIDs.
                Format: {"192.168.1.1": "device-uuid-1", "192.168.1.2": "device-uuid-2"}
            fabric_devices (list): List of management IP addresses that have been identified as fabric devices.
                Only devices in this list will be processed for fabric ID mapping.
                Format: ["192.168.1.1", "192.168.1.2"]

        Returns:
            dict: A mapping of fabric device IP addresses to their corresponding fabric IDs.
        """
        self.log("Building fabric device IP to fabric site ID mapping for comprehensive fabric operations", "INFO")
        self.log("Processing fabric ID mapping for {0} fabric devices across {1} fabric sites".format(len(fabric_devices), len(fabric_site_ids)), "DEBUG")

        fabric_ip_map = {}
        successful_mappings = 0
        failed_mappings = 0

        for fabric_id in fabric_site_ids:
            self.log("Processing fabric site {0} for device membership verification".format(fabric_id), "DEBUG")
            for ip_address, device_uuid in ip_uuid_map.items():
                if ip_address in fabric_devices:
                    try:
                        self.log("Verifying fabric membership for device {0} in fabric site {1}".format(ip_address, fabric_id), "DEBUG")

                        response = self.dnac._exec(
                            family="sda",
                            function="get_fabric_devices",
                            params={"fabric_id": fabric_id, "network_device_id": device_uuid}
                        )
                        self.log(
                            "Received API response from 'get_fabric_devices': {0}".format(response),
                            "DEBUG"
                        )

                        fabric_response_data = response.get("response", [])
                        if fabric_response_data:
                            fabric_id_value = fabric_response_data[0].get("fabricId")

                            if fabric_id_value:
                                fabric_ip_map[ip_address] = fabric_id_value
                                successful_mappings += 1
                                self.log("Successfully mapped fabric device {0} to fabric site {1}".format(ip_address, fabric_id_value), "DEBUG")
                            else:
                                self.log("Fabric device response for {0} missing fabricId field in site {1}".format(ip_address, fabric_id), "WARNING")
                        else:
                            self.log("Device {0} not found in fabric site {1} - checking additional sites".format(ip_address, fabric_id), "DEBUG")

                    except Exception as e:
                        failed_mappings += 1
                        self.log("Fabric membership verification failed for device {0} in site {1}: {2}".format(ip_address, fabric_id, str(e)), "ERROR")

        total_fabric_devices = len(fabric_devices)
        mapped_devices = len(fabric_ip_map)
        unmapped_devices = total_fabric_devices - mapped_devices

        self.log("Fabric device to site ID mapping completed - mapped {0}/{1} devices successfully".format(mapped_devices, total_fabric_devices), "INFO")

        if unmapped_devices > 0:
            self.log("Warning: {0} fabric devices could not be mapped to fabric sites".format(unmapped_devices), "WARNING")

        if successful_mappings > 0:
            self.log("Fabric device mappings created: {0}".format(list(fabric_ip_map.keys())), "DEBUG")

        return fabric_ip_map

    def get_fabric_info(self, ip_uuid_map, fabric_devices):
        """
        Retrieve comprehensive fabric configuration details for specified fabric devices from Catalyst Center.

        This method queries the Catalyst Center SDA API to collect detailed fabric-specific information
        for each provided fabric device. It iterates through all fabric sites to locate each device's
        fabric membership and retrieves complete fabric configuration metadata including device roles,
        fabric site associations, and SDA-specific attributes.

        Args:
            ip_uuid_map (dict): Mapping of device management IP addresses to their instance UUIDs.
                Format: {"192.168.1.1": "device-uuid-1", "192.168.1.2": "device-uuid-2"}
                Used for device identification in fabric API queries.
            fabric_devices (list): List of management IP addresses that have been confirmed as fabric devices.
                Only devices in this list will be processed for fabric information retrieval.
                Format: ["192.168.1.1", "192.168.1.2"]

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
        """
        self.log("Retrieving comprehensive fabric configuration details for fabric device inventory", "INFO")
        self.log("Processing fabric information for {0} fabric devices from {1} total devices".format(len(fabric_devices), len(ip_uuid_map)), "DEBUG")

        if not fabric_devices:
            self.log("No fabric device IDs provided for fabric info retrieval", "WARNING")
            return [{"fabric_info": []}]

        fabric_site_ids = self.get_fabric_site_id()
        if not fabric_site_ids:
            self.log("No fabric sites found in Catalyst Center - unable to retrieve fabric information", "WARNING")
            return [{"fabric_info": []}]

        fabric_info_list = []
        devices_processed = 0
        devices_with_fabric_info = 0
        devices_with_errors = 0

        self.log("Querying fabric device information across {0} fabric sites".format(len(fabric_site_ids)), "DEBUG")

        for fabric_id in fabric_site_ids:
            self.log("Processing fabric site {0} for device fabric information retrieval".format(fabric_id), "DEBUG")
            for index, (ip_address, device_uuid) in enumerate(ip_uuid_map.items()):
                if ip_address in fabric_devices:
                    devices_processed += 1
                    self.log(
                        "Processing fabric info for device {0}/{1}: "
                        "ID = {2} (IP: {3})".format(index + 1, len(ip_uuid_map), device_uuid, ip_address),
                        "DEBUG"
                    )
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
                            devices_with_fabric_info += 1
                            self.log("Fabric details found for device_ip: {0}.".format(ip_address), "INFO")
                            fabric_info_list.append({
                                "device_ip": ip_address,
                                "fabric_details": fabric_data
                            })
                            self.log("Successfully retrieved fabric configuration for device {0}".format(ip_address), "DEBUG")

                    except Exception as api_err:
                        devices_with_errors += 1
                        error_message = "Failed to retrieve fabric information for device {0}: {1}".format(ip_address, str(api_err))
                        self.log(error_message, "ERROR")
                        fabric_info_list.append({
                            "device_ip": ip_address,
                            "fabric_details": "Error: {0}".format(api_err)
                        })
                        continue

        result = [{"fabric_info": fabric_info_list}]

        self.log("Completed fabric info retrieval for filtered fabric devices. Total devices processed: {0}".format(len(fabric_info_list)), "INFO")
        self.log("Fabric info result: {0}".format(result), "DEBUG")

        total_fabric_devices = len(fabric_devices)
        self.log(
            "Fabric information retrieval completed - processed {0}/{1} fabric devices successfully".format(
                devices_with_fabric_info, total_fabric_devices
            ),
            "INFO"
        )
        if devices_with_errors > 0:
            self.log("Warning: {0} devices encountered errors during fabric information retrieval".format(devices_with_errors), "WARNING")

        if devices_with_fabric_info > 0:
            self.log(
                "Fabric information successfully retrieved for devices: {0}".format(
                    [info["device_ip"] for info in fabric_info_list if not isinstance(info["fabric_details"], str)]
                ),
                "DEBUG"
            )
        return result

    def get_device_issues_info(self, ip_uuid_map, fabric_devices):
        """
        Retrieve current device issues and alerts for specified fabric devices from Catalyst Center.

        This method queries the Catalyst Center Issues API to collect comprehensive issue and alert
        information for each provided fabric device. It processes device UUID mappings to identify
        active issues, warnings, and alerts associated with fabric devices, providing essential
        troubleshooting data for fabric network operations and health monitoring.

        Args:
            ip_uuid_map (dict): Mapping of device management IP addresses to their instance UUIDs.
                Format: {"192.168.1.1": "device-uuid-1", "192.168.1.2": "device-uuid-2"}
                Used for device identification in issues API queries.
            fabric_devices (list): List of management IP addresses that have been confirmed as fabric devices.
                Only devices in this list will be processed for issue information retrieval.
                Format: ["192.168.1.1", "192.168.1.2"]
        Returns:
            list: Structured device issues information results in standardized format:
                [
                    {
                        "device_issues_info": [
                            {
                                "device_ip": "192.168.1.1",
                                "issue_details": [issue_records] or [] or "Error: <error_message>"
                            },
                            {
                                "device_ip": "192.168.1.2",
                                "issue_details": [issue_records] or [] or "Error: <error_message>"
                            }
                        ]
                    }
                ]
                Returns [{"device_issues_info": []}] if no fabric devices provided.
        """
        self.log("Retrieving current device issues and alerts for fabric device troubleshooting", "INFO")
        self.log(
            "Processing device issues information for {0} fabric devices "
            "from {1} total devices".format(
                len(fabric_devices), len(ip_uuid_map)
            ),
            "DEBUG"
        )
        if not fabric_devices:
            self.log("No fabric device IDs provided for device issue info retrieval", "WARNING")
            return [{"device_issues_info": []}]

        issue_info_list = []
        devices_processed = 0
        devices_with_issues = 0
        devices_without_issues = 0
        devices_with_errors = 0

        for index, (ip_address, device_uuid) in enumerate(ip_uuid_map.items()):
            if ip_address in fabric_devices:
                devices_processed += 1
                self.log("Retrieving issue information for fabric device {0} (UUID: {1})".format(ip_address, device_uuid), "DEBUG")
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
                        devices_with_issues += 1
                        self.log("Active issues found for fabric device {0} - retrieved {1} issue records".format(ip_address, len(issue_data)), "INFO")
                        issue_info_list.append({
                            "device_ip": ip_address,
                            "issue_details": issue_data
                        })

                    else:
                        devices_without_issues += 1
                        self.log("No active issues found for fabric device {0} - device status healthy".format(ip_address), "DEBUG")
                        issue_info_list.append({
                            "device_ip": ip_address,
                            "issue_details": []
                        })

                except Exception as api_err:
                    devices_with_errors += 1
                    self.msg = "Failed to retrieve device issues for fabric device {0}: {1}".format(ip_address, str(api_err))
                    issue_info_list.append({
                        "device_ip": ip_address,
                        "issue_details": "Error: {0}".format(str(api_err))
                    })

        result = [{"device_issues_info": issue_info_list}]

        self.log("Completed device info retrieval. Total devices processed: {0}".format(len(issue_info_list)), "INFO")

        total_fabric_devices = len(fabric_devices)
        self.log("Device issues retrieval completed - processed {0}/{1} fabric devices successfully".format(devices_processed, total_fabric_devices), "INFO")

        if devices_with_issues > 0:
            self.log("Fabric devices with active issues: {0}".format(devices_with_issues), "WARNING")

        if devices_without_issues > 0:
            self.log("Fabric devices with healthy status (no issues): {0}".format(devices_without_issues), "INFO")

        if devices_with_errors > 0:
            self.log("Warning: {0} devices encountered errors during issue information retrieval".format(devices_with_errors), "WARNING")

        self.log("Aggregated device‑issues info: {0}".format(result), "DEBUG")

        return result

    def get_device_health_info(self, fabric_devices):
        """
        Retrieve comprehensive health metrics and performance data for specified fabric devices from Catalyst Center.

        This method queries the Catalyst Center device health API to collect detailed health information
        including CPU utilization, memory usage, device scores, and overall health status for each
        provided fabric device. It implements pagination to handle large device inventories and filters
        results to match only the specified fabric devices for targeted health monitoring.

        Args:
            fabric_devices (list): List of management IP addresses for fabric devices requiring health monitoring.
                Format: ["192.168.1.1", "192.168.1.2"]
                Only devices in this list will be included in health information results.
        Description:
            - Makes an API call to fetch all network device health data.
            - Filters the returned data to match the list of input fabric device IPs.
            - If health data is found, it's included in the results.
            - If not, adds a fallback message indicating no health info found for that device.
            - Logs responses and handles any exceptions gracefully.

        Returns:
            list: Structured device health information results in standardized format:
                [
                    {
                        "device_health_info": [
                            {
                                "device_ip": "192.168.1.1",
                                "health_details": {health_metrics_object} or {}
                            },
                            {
                                "device_ip": "192.168.1.2",
                                "health_details": {health_metrics_object} or {}
                            }
                        ]
                    }
                ]
                Returns [{"device_health_info": []}] if no fabric devices provided.
                Returns None if critical API failure prevents health data retrieval.
        """
        self.log("Retrieving comprehensive health metrics and performance data for fabric device monitoring", "INFO")
        self.log("Processing health information for {0} fabric devices from enterprise device inventory".format(len(fabric_devices)), "DEBUG")

        if not fabric_devices:
            self.log("No fabric device IDs provided for device health info retrieval", "WARNING")
            return [{"device_health_info": []}]

        health_info_list = []
        processed_device_ips = set()
        health_data_list = []

        self.log("Implementing pagination to retrieve comprehensive device health inventory with 500 device limit per request", "DEBUG")
        try:
            limit = 500
            offset = 1
            total_pages_processed = 0

            while True:
                total_pages_processed += 1
                self.log("Retrieving device health data page {0} with offset: {1}, limit: {2}".format(total_pages_processed, offset, limit), "DEBUG")
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
            self.log("Successfully retrieved health data for {0} total devices from Catalyst Center".format(len(health_data_list)), "INFO")

            devices_with_health_data = 0
            devices_without_health_data = 0

            if health_data_list:
                self.log("Filtering device health data to match {0} specified fabric devices".format(len(fabric_devices)), "DEBUG")
                for device_data in health_data_list:
                    device_ip = device_data.get("ipAddress")
                    if device_ip in fabric_devices and device_ip not in processed_device_ips:
                        devices_with_health_data += 1
                        processed_device_ips.add(device_ip)
                        self.log("Health metrics found for fabric device {0}".format(device_ip), "DEBUG")
                        health_info_list.append({
                            "device_ip": device_ip,
                            "health_details": device_data
                        })
                for fabric_device_ip in fabric_devices:
                    if fabric_device_ip not in processed_device_ips:
                        devices_without_health_data += 1
                        health_info_list.append({
                            "device_ip": fabric_device_ip,
                            "health_details": {}
                        })
                        self.log("No health information found for fabric device {0}".format(fabric_device_ip), "WARNING")
            else:
                self.log("No device health data retrieved from Catalyst Center - all fabric devices will have empty health details", "WARNING")
                for fabric_device_ip in fabric_devices:
                    devices_without_health_data += 1
                    health_info_list.append({
                        "device_ip": fabric_device_ip,
                        "health_details": {}
                    })

        except Exception as api_err:
            self.msg = "Critical failure during device health information retrieval: {0}".format(str(api_err))
            health_info_list.append({
                "device_ip": fabric_device_ip,
                "health_details": "Error: {0}".format(str(api_err))
            })

        result = [{"device_health_info": health_info_list}]

        self.log("Completed health info retrieval. Total devices processed: {0}".format(len(health_info_list)), "INFO")

        total_fabric_devices = len(fabric_devices)
        self.log(
            "Device health information retrieval completed - processed {0}/{1} "
            "fabric devices successfully".format(
                len(health_info_list), total_fabric_devices
            ),
            "INFO"
        )
        if devices_with_health_data > 0:
            self.log("Fabric devices with health metrics available: {0}".format(devices_with_health_data), "INFO")

        if devices_without_health_data > 0:
            self.log("Fabric devices without health data: {0}".format(devices_without_health_data), "WARNING")

        self.log("Aggregated device-health info: {0}".format(result), "DEBUG")

        return result

    def get_handoff_layer3_sda_info(self, ip_uuid_map, fabric_ip_map):
        """
        Retrieve Layer 3 SDA handoff configuration details for fabric devices from Catalyst Center.

        This method queries the Catalyst Center SDA API to collect comprehensive Layer 3 handoff
        information with SDA transit configurations for fabric devices. It processes fabric device
        mappings to retrieve routed transit configurations, VLAN mappings, IP interface details,
        and SDA-specific handoff parameters essential for inter-fabric connectivity and routing.

        Args:
            ip_uuid_map (dict): Mapping of device management IP addresses to their instance UUIDs.
                Format: {"192.168.1.1": "device-uuid-1", "192.168.1.2": "device-uuid-2"}
                Used for device identification in handoff configuration queries.
            fabric_ip_map (dict): Mapping of fabric device IP addresses to their fabric site identifiers.
                Format: {"192.168.1.1": "fabric-site-uuid-1", "192.168.1.2": "fabric-site-uuid-2"}
                Used to associate devices with their fabric contexts for handoff queries.
        Description:
            - Iterates through fabric-enabled site IDs and retrieves associated device UUIDs.
            - For each device, makes an API call to fetch Layer 3 SDA handoff information.
            - If data is available, adds it under the respective device IP.
            - If no data is found, a message is logged and a default string is added.
            - Aggregates and returns all results in a consistent, structured format.
        Returns:
            list: Structured Layer 3 SDA handoff information results in standardized format:
                [
                    {
                        "fabric_devices_layer3_handoffs_sda_info": [
                            {
                                "device_ip": "192.168.1.1",
                                "handoff_info": [handoff_configuration_records] or [] or "Error: <error_message>"
                            },
                            {
                                "device_ip": "192.168.1.2",
                                "handoff_info": [handoff_configuration_records] or [] or "Error: <error_message>"
                            }
                        ]
                    }
                ]
                Returns [{"fabric_devices_layer3_handoffs_sda_info": []}] if no fabric devices found.
        """
        self.log("Retrieving Layer 3 SDA handoff configurations for fabric inter-site connectivity", "INFO")
        self.log("Processing Layer 3 SDA handoff information for {0} devices across fabric sites".format(len(fabric_ip_map)), "DEBUG")

        if not fabric_ip_map:
            self.log("No fabric device mappings provided for Layer 3 SDA handoff retrieval - returning empty result structure", "WARNING")
            return [{"fabric_devices_layer3_handoffs_sda_info": []}]

        all_handoff_layer3_sda_list = []
        processed_device_ips = set()
        devices_processed = 0
        devices_with_handoffs = 0
        devices_without_handoffs = 0
        devices_with_errors = 0

        for index, (ip_address, device_uuid) in enumerate(ip_uuid_map.items()):
            for device_ip, fabric_id in fabric_ip_map.items():
                if ip_address == device_ip and ip_address not in processed_device_ips:
                    self.log(
                        "Processing layer3 sda handoff info for device {0}/{1}: "
                        "ID = {2} (IP: {3})".format(index + 1, len(ip_uuid_map), device_uuid, ip_address),
                        "DEBUG"
                    )
                    processed_device_ips.add(ip_address)
                    devices_processed += 1

                    self.log("Retrieving Layer 3 SDA handoff configuration for fabric device {0} in fabric site {1}".format(ip_address, fabric_id), "DEBUG")

                    try:
                        response = self.dnac._exec(
                            family="sda",
                            function="get_fabric_devices_layer3_handoffs_with_sda_transit",
                            params={"fabric_id": fabric_id, "network_device_id": device_uuid}
                        )
                        layer3_sda_handoff_data = response.get("response", [])
                        self.log(
                            "Received API response for 'get_fabric_devices_layer3_handoffs_with_sda_transit' for IP {0}: {1}".format(
                                ip_address, response
                            ),
                            "DEBUG"
                        )
                        if layer3_sda_handoff_data:
                            devices_with_handoffs += 1
                            self.log(
                                "Layer 3 SDA handoff configuration found for fabric device {0} - "
                                "retrieved {1} handoff records".format(
                                    ip_address, len(layer3_sda_handoff_data)
                                ),
                                "INFO"
                            )
                            all_handoff_layer3_sda_list.append({
                                "device_ip": ip_address,
                                "handoff_info": layer3_sda_handoff_data
                            })

                        else:
                            devices_without_handoffs += 1
                            self.log(
                                "No Layer 3 SDA handoff configuration found for fabric device {0} - "
                                "device may not be configured for inter-fabric routing".format(
                                    ip_address
                                ),
                                "DEBUG"
                            )
                            all_handoff_layer3_sda_list.append({
                                "device_ip": ip_address,
                                "handoff_info": []
                            })

                    except Exception as api_err:
                        devices_with_errors += 1
                        self.msg = "Exception occurred while getting L3 SDA hand-off info for device {0}: {1}".format(ip_address, api_err)
                        all_handoff_layer3_sda_list.append({
                            "device_ip": ip_address,
                            "handoff_info": "Error: {0}".format(api_err)
                        })

        result = [{"fabric_devices_layer3_handoffs_sda_info": all_handoff_layer3_sda_list}]

        total_fabric_devices = len(fabric_ip_map)
        self.log(
            "Layer 3 SDA handoff configuration retrieval completed - "
            "processed {0}/{1} fabric devices successfully".format(
                devices_processed,
                total_fabric_devices
            ),
            "INFO"
        )
        if devices_with_handoffs > 0:
            self.log("Fabric devices with Layer 3 SDA handoff configurations: {0}".format(devices_with_handoffs), "INFO")

        if devices_without_handoffs > 0:
            self.log("Fabric devices without Layer 3 SDA handoff configurations: {0}".format(devices_without_handoffs), "INFO")

        if devices_with_errors > 0:
            self.log("Warning: {0} devices encountered errors during Layer 3 SDA handoff configuration retrieval".format(devices_with_errors), "WARNING")

        self.log("Completed L3 SDA hand-off info retrieval. Total devices processed: {0}".format(len(all_handoff_layer3_sda_list)), "INFO")
        self.log("Aggregated L3 SDA hand-off info: {0}".format(result), "DEBUG")

        return result

    def get_handoff_layer3_ip_info(self, ip_uuid_map, fabric_ip_map):
        """
        Retrieve Layer 3 IP handoff configuration details for fabric devices from Catalyst Center.

        This method queries the Catalyst Center SDA API to collect comprehensive Layer 3 handoff
        information with IP transit configurations for fabric devices. It processes fabric device
        mappings to retrieve IP transit configurations, VLAN mappings, next-hop IP addresses,
        interface details, VRF assignments, and routing parameters essential for external connectivity
        and traditional IP-based handoffs from fabric networks.

        Args:
            ip_uuid_map (dict): Mapping of device management IP addresses to their instance UUIDs.
                Format: {"192.168.1.1": "device-uuid-1", "192.168.1.2": "device-uuid-2"}
                Used for device identification in handoff configuration queries.
            fabric_ip_map (dict): Mapping of fabric device IP addresses to their fabric site identifiers.
                Format: {"192.168.1.1": "fabric-site-uuid-1", "192.168.1.2": "fabric-site-uuid-2"}
                Used to associate devices with their fabric contexts for handoff queries.

        Returns:
            list: Structured Layer 3 IP handoff information results in standardized format:
                [
                    {
                        "fabric_devices_layer3_handoffs_ip_info": [
                            {
                                "device_ip": "192.168.1.1",
                                "handoff_info": [handoff_configuration_records] or [] or "Error: <error_message>"
                            },
                            {
                                "device_ip": "192.168.1.2",
                                "handoff_info": [handoff_configuration_records] or [] or "Error: <error_message>"
                            }
                        ]
                    }
                ]
                Returns [{"fabric_devices_layer3_handoffs_ip_info": []}] if no fabric devices found.
        Note:
            Layer 3 IP handoffs are typically configured on Border Nodes for external network
            connectivity. These handoffs provide traditional IP routing integration points
            between fabric networks and legacy IP infrastructure.
        """

        self.log("Retrieving Layer 3 IP handoff configurations for fabric external connectivity", "INFO")
        self.log("Processing Layer 3 IP handoff information for {0} devices across fabric sites".format(len(fabric_ip_map)), "DEBUG")

        all_handoff_layer3_ip_info_list = []
        processed_device_ips = set()
        devices_processed = 0
        devices_with_handoffs = 0
        devices_without_handoffs = 0
        devices_with_errors = 0

        for index, (ip_address, device_uuid) in enumerate(ip_uuid_map.items()):
            for device_ip, fabric_id in fabric_ip_map.items():
                if ip_address == device_ip and ip_address not in processed_device_ips:
                    self.log(
                        "Retrieving Layer 3 IP handoff configuration for fabric device {0} "
                        "in fabric site {1}".format(
                            ip_address, fabric_id
                        ),
                        "DEBUG"
                    )
                    processed_device_ips.add(ip_address)
                    devices_processed += 1

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
                            devices_with_handoffs += 1
                            self.log(
                                "Layer 3 IP handoff configuration found for fabric device {0} - "
                                "retrieved {1} handoff records".format(
                                    ip_address, len(layer3_ip_handoff_data)
                                ),
                                "INFO"
                            )
                            all_handoff_layer3_ip_info_list.append({
                                "device_ip": ip_address,
                                "handoff_info": layer3_ip_handoff_data
                            })
                        else:
                            devices_without_handoffs += 1
                            self.log(
                                "No Layer 3 IP handoff configuration found for fabric device {0} - "
                                "device may not be configured for external IP connectivity".format(
                                    ip_address
                                ),
                                "DEBUG"
                            )
                            all_handoff_layer3_ip_info_list.append({
                                "device_ip": ip_address,
                                "handoff_info": []
                            })

                    except Exception as api_err:
                        devices_with_errors += 1
                        self.msg = "Failed to retrieve Layer 3 IP handoff configuration for fabric device {0}: {1}".format(ip_address, str(api_err))
                        all_handoff_layer3_ip_info_list.append({
                            "device_ip": ip_address,
                            "handoff_info": "Error: {0}".format(api_err)
                        })

        result = [{"fabric_devices_layer3_handoffs_ip_info": all_handoff_layer3_ip_info_list}]

        total_fabric_devices = len(fabric_ip_map)
        self.log(
            "Layer 3 IP handoff configuration retrieval completed - "
            "processed {0}/{1} fabric devices successfully".format(
                devices_processed,
                total_fabric_devices
            ),
            "INFO"
        )
        if devices_with_handoffs > 0:
            self.log("Fabric devices with Layer 3 IP handoff configurations: {0}".format(devices_with_handoffs), "INFO")

        if devices_without_handoffs > 0:
            self.log("Fabric devices without Layer 3 IP handoff configurations: {0}".format(devices_without_handoffs), "INFO")

        if devices_with_errors > 0:
            self.log("Warning: {0} devices encountered errors during Layer 3 IP handoff configuration retrieval".format(devices_with_errors), "WARNING")

        self.log("Completed L3 IP hand-off info retrieval. Total devices processed: {0}".format(len(all_handoff_layer3_ip_info_list)), "INFO")
        self.log("Aggregated L3 IP hand-off info: {0}".format(result), "DEBUG")

        return result

    def get_handoff_layer2_info(self, ip_uuid_map, fabric_ip_map):
        """
        Retrieve Layer 2 handoff configuration details for fabric devices from Catalyst Center.

        This method queries the Catalyst Center SDA API to collect comprehensive Layer 2 handoff
        information for fabric devices. It processes fabric device mappings to retrieve Layer 2
        handoff configurations including handoff types, VLAN mappings, interface assignments,
        and destination details essential for fabric edge connectivity and Layer 2 network
        integration points within the SDA fabric architecture.

        Args:
            ip_uuid_map (dict): Mapping of device management IP addresses to their instance UUIDs.
                Format: {"192.168.1.1": "device-uuid-1", "192.168.1.2": "device-uuid-2"}
                Used for device identification in handoff configuration queries.
            fabric_ip_map (dict): Mapping of fabric device IP addresses to their fabric site identifiers.
                Format: {"192.168.1.1": "fabric-site-uuid-1", "192.168.1.2": "fabric-site-uuid-2"}
                Used to associate devices with their fabric contexts for handoff queries.

        Returns:
            list: Structured Layer 2 handoff information results in standardized format:
                [
                    {
                        "fabric_devices_layer2_handoffs_info": [
                            {
                                "device_ip": "192.168.1.1",
                                "handoff_info": [handoff_configuration_records] or [] or "Error: <error_message>"
                            },
                            {
                                "device_ip": "192.168.1.2",
                                "handoff_info": [handoff_configuration_records] or [] or "Error: <error_message>"
                            }
                        ]
                    }
                ]
                Returns [{"fabric_devices_layer2_handoffs_info": []}] if no fabric devices found.
        """
        self.log("Retrieving Layer 2 handoff configurations for fabric edge connectivity", "INFO")
        self.log("Processing Layer 2 handoff information for {0} devices across fabric sites".format(len(fabric_ip_map)), "DEBUG")

        all_handoff_layer2_info_list = []
        processed_device_ips = set()
        devices_processed = 0
        devices_with_handoffs = 0
        devices_without_handoffs = 0
        devices_with_errors = 0

        for index, (ip_address, device_uuid) in enumerate(ip_uuid_map.items()):
            for device_ip, fabric_id in fabric_ip_map.items():
                if ip_address == device_ip and ip_address not in processed_device_ips:
                    self.log(
                        "Retrieving Layer 2 handoff configuration for fabric device {0} "
                        "in fabric site {1}".format(
                            ip_address, fabric_id
                        ),
                        "DEBUG"
                    )
                    devices_processed += 1
                    processed_device_ips.add(ip_address)

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
                            devices_with_handoffs += 1
                            self.log(
                                "Layer 2 handoff configuration found for fabric device {0} - "
                                "retrieved {1} handoff records".format(
                                    ip_address, len(layer2_handoff_data)
                                ),
                                "INFO"
                            )
                            all_handoff_layer2_info_list.append({
                                "device_ip": ip_address,
                                "handoff_info": layer2_handoff_data
                            })

                        else:
                            devices_without_handoffs += 1
                            self.log(
                                "No Layer 2 handoff configuration found for fabric device {0} - "
                                "device may not be configured for Layer 2 edge connectivity".format(
                                    ip_address
                                ),
                                "DEBUG"
                            )
                            all_handoff_layer2_info_list.append({
                                "device_ip": ip_address,
                                "handoff_info": []
                            })

                    except Exception as api_err:
                        devices_with_errors += 1
                        self.msg = "Failed to retrieve Layer 2 handoff configuration for fabric device {0}: {1}".format(ip_address, str(api_err))
                        self.log(self.msg, "ERROR")
                        all_handoff_layer2_info_list.append({
                            "device_ip": ip_address,
                            "handoff_info": "Error: {0}".format(api_err)
                        })
                        continue

        result = [{"fabric_devices_layer2_handoffs_info": all_handoff_layer2_info_list}]

        total_fabric_devices = len(fabric_ip_map)
        self.log(
            "Layer 2 handoff configuration retrieval completed - "
            "processed {0}/{1} fabric devices successfully".format(
                devices_processed,
                total_fabric_devices
            ),
            "INFO"
        )
        if devices_with_handoffs > 0:
            self.log("Fabric devices with Layer 2 handoff configurations: {0}".format(devices_with_handoffs), "INFO")

        if devices_without_handoffs > 0:
            self.log("Fabric devices without Layer 2 handoff configurations: {0}".format(devices_without_handoffs), "INFO")

        if devices_with_errors > 0:
            self.log("Warning: {0} devices encountered errors during Layer 2 handoff configuration retrieval".format(devices_with_errors), "WARNING")

        self.log("Completed L2 hand-off info retrieval. Total devices processed: {0}".format(len(all_handoff_layer2_info_list)), "INFO")
        self.log("Aggregated L2 hand-off info: {0}".format(result), "DEBUG")

        return result

    def get_interface_ids_per_device(self, ip_uuid_map, fabric_devices):
        """
        Retrieves interface UUIDs for each fabric device from Cisco Catalyst Center.

        This method queries the Catalyst Center device interface API to collect comprehensive
        interface UUID mappings for specified fabric devices. It processes fabric device
        IP-to-UUID mappings to retrieve all interface identifiers associated with each device,
        providing essential interface inventory data for fabric interface configuration,
        monitoring, and management operations.

        Args:
            ip_uuid_map (dict): Mapping of device management IP addresses to their instance UUIDs.
                Format: {"192.168.1.1": "device-uuid-1", "192.168.1.2": "device-uuid-2"}
                Used for device identification in interface queries.
            fabric_devices (list): List of management IP addresses for fabric devices requiring interface discovery.
                Only devices in this list will be processed for interface information retrieval.
                Format: ["192.168.1.1", "192.168.1.2"]

        Returns:
            dict: A dictionary where each key is a device IP address and each value is a set of interface UUIDs
                associated with that device. Devices with no interfaces or on exception are skipped or logged.
        """
        self.log("Retrieving interface identifiers for fabric device interface inventory and management", "INFO")
        self.log(
            "Processing interface discovery for {0} fabric devices from {1} total devices".format(
                len(fabric_devices),
                len(ip_uuid_map)
            ),
            "DEBUG"
        )
        if not fabric_devices:
            self.log("No fabric devices provided for interface identifier retrieval - returning empty mapping", "WARNING")
            return {}

        device_interfaces_map = {}
        device_interfaces_map = {}
        devices_processed = 0
        devices_with_interfaces = 0
        devices_without_interfaces = 0
        devices_with_errors = 0
        total_interfaces_discovered = 0

        for index, (ip_address, device_id) in enumerate(ip_uuid_map.items()):
            if ip_address in fabric_devices:
                devices_processed += 1
                self.log("Retrieving interface information for fabric device {0} (UUID: {1})".format(ip_address, device_id), "DEBUG")

                try:
                    self.log("Fetching interfaces for device: {0}".format(ip_address), "DEBUG")

                    response = self.dnac._exec(
                        family="devices",
                        function="get_interface_info_by_id",
                        params={"device_id": device_id}
                    )
                    interface_response_data = response.get("response", [])
                    self.log(
                        "Interface query completed for device {0} - found {1} interface records".format(
                            ip_address,
                            len(interface_response_data)
                        ),
                        "DEBUG"
                    )
                    self.log("Received API response for 'get_interface_info_by_id' for device {0}: {1}".format(ip_address, response), "DEBUG")

                    interface_ids = set()
                    for interface in interface_response_data:
                        interface_id = interface.get("id")
                        if interface_id:
                            interface_ids.add(interface_id)
                        else:
                            interfaces_without_ids += 1
                            self.log(
                                "Interface record missing UUID identifier for device {0} - skipping interface".format(
                                    ip_address
                                ),
                                "WARNING"
                            )
                    device_interfaces_map[ip_address] = interface_ids
                    total_interfaces_discovered += len(interface_ids)

                    if interface_ids:
                        devices_with_interfaces += 1
                        self.log(
                            "Successfully mapped {0} interface identifiers for fabric device {1}".format(
                                len(interface_ids),
                                ip_address
                            ),
                            "DEBUG"
                        )
                    else:
                        devices_without_interfaces += 1
                        self.log(
                            "No interface identifiers found for fabric device {0} - "
                            "device may have no configured interfaces".format(ip_address),
                            "WARNING"
                        )
                    if interfaces_without_ids > 0:
                        self.log(
                            "Warning: {0} interface records for device {1} were missing "
                            "UUID identifiers".format(
                                interfaces_without_ids,
                                ip_address
                            ),
                            "WARNING"
                        )

                except Exception as e:
                    devices_with_errors += 1
                    self.msg = "Failed to retrieve interface information for fabric device {0}: {1}".format(ip_address, str(e))
                    self.log(self.msg, "ERROR")

        total_fabric_devices = len(fabric_devices)
        successful_devices = len(device_interfaces_map)

        self.log(
            "Interface identifier retrieval completed - "
            "processed {0}/{1} fabric devices successfully".format(
                successful_devices,
                total_fabric_devices
            ),
            "INFO"
        )

        if devices_with_interfaces > 0:
            self.log("Fabric devices with interface identifiers: {0}".format(devices_with_interfaces), "INFO")

        if devices_without_interfaces > 0:
            self.log("Fabric devices without interface identifiers: {0}".format(devices_without_interfaces), "INFO")

        if devices_with_errors > 0:
            self.log("Warning: {0} devices encountered errors during interface retrieval".format(devices_with_errors), "WARNING")

        self.log("Total interface identifiers discovered across all fabric devices: {0}".format(total_interfaces_discovered), "INFO")

        return device_interfaces_map

    def get_connected_device_details_from_interfaces(self, ip_uuid_map, fabric_devices):
        """
        Discover connected device topology for fabric devices through comprehensive interface-level analysis.

        This method performs extensive connected device discovery by querying each interface of specified
        fabric devices to identify neighboring devices, endpoints, and network attachments. It processes
        interface-level connectivity data to provide complete visibility into fabric device interconnections,
        attached endpoints, and network topology relationships essential for fabric network management
        and troubleshooting operations.

        Args:
            ip_uuid_map (dict): Mapping of device management IP addresses to their instance UUIDs.
                            Format: {"192.168.1.1": "device-uuid-1", "192.168.1.2": "device-uuid-2"}
                            Used for device identification in connected device queries.
            fabric_devices (list): List of management IP addresses for fabric devices requiring
                                connected device topology discovery.
                                Format: ["192.168.1.1", "192.168.1.2"]

        Returns:
            list: Structured connected device topology information in standardized format:
                [
                    {
                        "connected_device_info": [
                            {
                                "device_ip": "192.168.1.1",
                                "connected_device_details": [connected_device_records] or "Error: <message>"
                            },
                            {
                                "device_ip": "192.168.1.2",
                                "connected_device_details": [connected_device_records] or "Error: <message>"
                            }
                        ]
                    }
                ]
                Returns [{"connected_device_info": []}] if no fabric devices provided.
        """
        self.log("Discovering connected device topology for fabric device interface inventory", "INFO")
        self.log("Processing connected device discovery for {0} fabric devices".format(len(fabric_devices)), "DEBUG")

        if not fabric_devices:
            self.log("No fabric device IDs provided for connected device information retrieval", "WARNING")
            return [{"connected_device_info": []}]

        connected_info_list = []
        devices_with_connections = 0
        devices_without_connections = 0
        devices_with_errors = 0

        self.log("Retrieving interface inventories for fabric devices to enable connected device discovery", "DEBUG")
        device_interfaces_map = self.get_interface_ids_per_device(ip_uuid_map, fabric_devices)

        if not device_interfaces_map:
            self.log("No interface mappings available for fabric devices - unable to perform connected device discovery", "WARNING")
            return [{"connected_device_info": []}]

        self.log("Processing connected device discovery across {0} fabric devices with interface inventories".format(len(device_interfaces_map)), "DEBUG")

        for index, (ip_address, interface_ids) in enumerate(device_interfaces_map.items()):
            interface_count = len(interface_ids)
            device_id = ip_uuid_map[ip_address]
            interfaces_with_connections = 0
            connected_device_details = []

            for interface_id in interface_ids:
                self.log("Querying connected devices for interface {0} on device {1}".format(interface_id, ip_address), "DEBUG")
                try:
                    response = self.dnac._exec(
                        family="devices",
                        function="get_connected_device_detail",
                        params={
                            "device_uuid": device_id,
                            "interface_uuid": interface_id
                        }
                    )
                    interface_connected_data = response.get("response", {})
                    self.log("Received API response for IP {0}, interface {1}: {2}".format(ip_address, interface_id, response), "DEBUG")

                    if interface_connected_data:
                        interfaces_with_connections += 1
                        self.log("Connected device details found for device IP: {0}".format(ip_address), "INFO")

                        if isinstance(interface_connected_data, list):
                            connected_device_details.extend(interface_connected_data)
                        else:
                            connected_device_details.append(interface_connected_data)

                    if connected_device_details:
                        devices_with_connections += 1
                        self.log(
                            "Connected device discovery completed for device {0} - "
                            "found {1} total connections across {2} interfaces".format(
                                ip_address,
                                len(connected_device_details),
                                interfaces_with_connections
                            ),
                            "DEBUG"
                        )
                        connected_info_list.append({
                            "device_ip": ip_address,
                            "connected_device_details": connected_device_details
                        })
                    else:
                        devices_without_connections += 1
                        self.log(
                            "No connected devices discovered for device {0} "
                            "across {1} interfaces".format(
                                ip_address,
                                interface_count
                            ),
                            "DEBUG"
                        )
                except Exception as e:
                    devices_with_errors += 1
                    self.log("Failed to fetch connected device info for {0}: due to {1}".format(ip_address, str(e)), "ERROR")
                    connected_info_list.append({
                        "device_ip": ip_address,
                        "connected_device_details": "Error: {0}".format(e)
                    })

        result = [{"connected_device_info": connected_info_list}]

        total_fabric_devices = len(fabric_devices)
        successful_devices = len(connected_info_list)

        self.log(
            "Connected device topology discovery completed - "
            "processed {0}/{1} fabric devices with {2} total interfaces".format(
                successful_devices,
                total_fabric_devices,
                interface_count
            ),
            "INFO"
        )
        if devices_with_connections > 0:
            self.log("Fabric devices with connected device discoveries: {0}".format(devices_with_connections), "INFO")

        if devices_without_connections > 0:
            self.log("Fabric devices with no connected devices: {0}".format(devices_without_connections), "INFO")

        if devices_with_errors > 0:
            self.log("Warning: {0} devices encountered errors during connected device discovery".format(devices_with_errors), "WARNING")

        self.log("Total connected devices discovered across fabric topology: {0}".format(connected_info_list), "INFO")

        self.log("Completed connected device info retrieval. Total devices processed: {0}".format(len(connected_info_list)), "INFO")
        self.log("Final aggregated connected device info: {0}".format(result), "DEBUG")

        return result

    def get_dev_type(self, ip_address):
        """
        Determine device infrastructure type classification for network device analysis and management.

        This method queries the Catalyst Center device inventory to classify a network device
        as either wired or wireless infrastructure based on its device family attributes.
        The classification is essential for applying appropriate configuration templates,
        monitoring policies, and management workflows specific to device infrastructure types.

        Args:
            ip_address (str): Management IP address of the network device requiring type classification.
                Format: "192.168.1.1"
                Must be a valid, reachable device IP address in Catalyst Center inventory.

        Returns:
            str or None: Device infrastructure type classification:
                - 'wired': Traditional network infrastructure (switches, routers)
                - 'wireless': Wireless infrastructure (controllers, access points)
                - None: Device type cannot be determined, device not found, or API failure
        """
        self.log("Determining device infrastructure type classification for network device management", "INFO")
        self.log("Processing device type determination for IP address: {0}".format(ip_address), "DEBUG")

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
            self.log("Device family identified as '{0}' for infrastructure type classification".format(device_family), "DEBUG")

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

    def get_onboarding_info(self, ip_uuid_map, fabric_ip_map, fabric_devices):
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
            ip_uuid_map (dict): Mapping of device management IP addresses to their instance UUIDs.
                Format: {"192.168.1.1": "device-uuid-1", "192.168.1.2": "device-uuid-2"}
                Used for device identification in onboarding status queries.
            fabric_ip_map (dict): Mapping of fabric device IP addresses to their fabric site identifiers.
                Format: {"192.168.1.1": "fabric-site-uuid-1", "192.168.1.2": "fabric-site-uuid-2"}
                Used to associate devices with their fabric contexts for onboarding queries.
            fabric_devices (list): List of management IP addresses for fabric devices requiring onboarding
                information retrieval. Only devices in this list will be processed.
                Format: ["192.168.1.1", "192.168.1.2"]
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
        """
        self.log("Retrieving fabric device onboarding information for lifecycle management and troubleshooting", "INFO")
        self.log("Processing onboarding status for {0} fabric devices across fabric sites".format(len(fabric_devices)), "DEBUG")

        if not fabric_devices:
            self.log("No fabric devices provided for onboarding information retrieval - returning empty result structure", "WARNING")
            return [{"device_onboarding_info": []}]

        if not fabric_ip_map:
            self.log("No fabric device mappings provided for onboarding information retrieval - returning empty result structure", "WARNING")
            return [{"device_onboarding_info": []}]

        all_onboarding_info_list = []
        devices_processed = 0
        devices_with_onboarding_data = 0
        devices_without_onboarding_data = 0
        devices_with_errors = 0

        for device_ip, fabric_id in fabric_ip_map.items():
            for index, (ip_address, device_uuid) in enumerate(ip_uuid_map.items()):
                if ip_address in fabric_devices:
                    devices_processed += 1
                    self.log(
                        "Processing onboarding device detail for device {0}/{1}: "
                        "ID = {2} (IP: {3})".format(index + 1, len(ip_uuid_map), device_uuid, ip_address),
                        "DEBUG"
                    )
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
                            devices_with_onboarding_data += 1
                            self.log("Onboarding data found for device IP: {0}".format(ip_address), "INFO")
                            all_onboarding_info_list.append({
                                "device_ip": ip_address,
                                "port_details": onboarding_data
                            })
                        else:
                            devices_without_onboarding_data += 1
                            self.log("No onboarding data found for device IP: {0}".format(ip_address), "DEBUG")
                            all_onboarding_info_list.append({
                                "device_ip": ip_address,
                                "port_details": []
                            })
                            continue

                    except Exception as api_err:
                        devices_with_errors += 1
                        self.msg = "Exception occurred while getting port assignment details for device {0}: {1}".format(ip_address, api_err)
                        all_onboarding_info_list.append({
                            "device_ip": device_ip,
                            "port_details": "Error: {0}".format(api_err)
                        })

            result = [{"device_onboarding_info": all_onboarding_info_list}]

            total_fabric_devices = len(fabric_devices)
            self.log(
                "Fabric device onboarding information retrieval completed - "
                "processed {0}/{1} fabric devices successfully".format(
                    devices_processed,
                    total_fabric_devices
                ),
                "INFO"
            )

            if devices_with_onboarding_data > 0:
                self.log("Fabric devices with onboarding data indicating successful fabric integration: {0}".format(devices_with_onboarding_data), "INFO")

            if devices_without_onboarding_data > 0:
                self.log("Fabric devices without onboarding data indicating potential onboarding issues: {0}".format(devices_without_onboarding_data), "INFO")

            if devices_with_errors > 0:
                self.log("Warning: {0} devices encountered errors during onboarding information retrieval".format(devices_with_errors), "WARNING")

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
        Note:
            Provisioning status provides insights into fabric device readiness, role assignments,
            and current state within the SDA fabric infrastructure for operational monitoring.
        """
        self.log("Retrieving fabric device provisioning status for lifecycle management and health monitoring", "INFO")
        self.log("Processing provisioning status for {0} fabric devices".format(len(fabric_devices)), "DEBUG")

        if not fabric_devices:
            self.log("No fabric device IDs provided for provision status information retrieval", "WARNING")
            return [{"provision_status_info": []}]

        all_provision_status_info_list = []
        devices_processed = 0
        devices_with_provisioning_status = 0
        devices_without_provisioning_status = 0
        devices_with_errors = 0

        for index, (ip_address, device_id) in enumerate(ip_uuid_map.items()):
            if ip_address in fabric_devices:
                devices_processed += 1
                self.log(
                    "Processing provision status info for device {0}/{1}: "
                    "ID = {2} (IP: {3})".format(index + 1, len(ip_uuid_map), device_id, ip_address),
                    "DEBUG"
                )
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
                        devices_with_provisioning_status += 1
                        all_provision_status_info_list.append({
                            "device_ip": ip_address,
                            "provision_status": provision_data
                        })
                        self.log("Provisioning status found for fabric device {0} - device is provisioned in fabric".format(ip_address), "INFO")
                    else:
                        devices_without_provisioning_status += 1
                        self.log("No provisioning status found for device IP: {0}".format(ip_address), "DEBUG")
                        all_provision_status_info_list.append({
                            "device_ip": ip_address,
                            "provision_status": {}
                        })
                        self.log("No provisioning status found for fabric device {0} - device may not be provisioned or not found".format(ip_address), "DEBUG")

                except Exception as api_err:
                    devices_with_errors += 1
                    self.msg = "Failed to retrieve provisioning status for fabric device {0}: {1}".format(ip_address, str(api_err))
                    self.log(self.msg, "ERROR")
                    all_provision_status_info_list.append({
                        "device_ip": ip_address,
                        "interface_details": "Error: {0}".format(api_err)
                    })

        result = [{"provision_status_info": all_provision_status_info_list}]

        total_fabric_devices = len(fabric_devices)
        self.log(
            "Fabric device provisioning status retrieval completed - "
            "processed {0}/{1} fabric devices successfully".format(
                devices_processed,
                total_fabric_devices
            ),
            "INFO"
        )
        if devices_with_provisioning_status > 0:
            self.log("Fabric devices with provisioning status indicating successful fabric provisioning: {0}".format(devices_with_provisioning_status), "INFO")

        if devices_without_provisioning_status > 0:
            self.log(
                "Fabric devices without provisioning status indicating potential "
                "provisioning issues: {0}".format(
                    devices_without_provisioning_status
                ),
                "INFO"
            )

        if devices_with_errors > 0:
            self.log("Warning: {0} devices encountered errors during provisioning status retrieval".format(devices_with_errors), "WARNING")

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

            Note:
                SSID details are only applicable to wireless controllers. Non-wireless devices
                are processed but marked as not applicable for SSID configuration retrieval.
        """
        self.log("Retrieving wireless SSID configuration details for fabric wireless infrastructure management", "INFO")
        self.log("Processing SSID configuration for {0} fabric devices requiring wireless network analysis".format(len(fabric_devices)), "DEBUG")

        if not fabric_devices:
            self.log("No fabric device IDs provided for ssid details information retrieval", "WARNING")
            return [{"ssid_info": []}]

        all_ssid_info_list = []
        devices_processed = 0
        wireless_devices_found = 0
        non_wireless_devices_found = 0
        devices_with_ssid_data = 0
        devices_without_ssid_data = 0
        devices_with_errors = 0

        for index, (ip_address, device_id) in enumerate(ip_uuid_map.items()):
            if ip_address in fabric_devices:
                devices_processed += 1
                self.log("Processing SSID configuration analysis for fabric device {0}".format(ip_address), "DEBUG")
                device_type = self.get_dev_type(ip_address)
                self.log("Device {0} is identified as '{1}'".format(ip_address, device_type), "DEBUG")

                if device_type != "wireless":
                    non_wireless_devices_found += 1
                    self.log(
                        "Skipping SSID retrieval for device {0} - "
                        "device type '{1}' does not support SSID configuration".format(
                            ip_address,
                            device_type
                        ),
                        "DEBUG"
                    )
                    all_ssid_info_list.append({
                        "device_ip": ip_address,
                        "ssid_details": "The device is not wireless; therefore, SSID information retrieval is not applicable."
                    })
                    continue
                wireless_devices_found += 1
                self.log("Retrieving SSID configuration for wireless controller {0}".format(ip_address), "DEBUG")

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
                    if ssid_data:
                        devices_with_ssid_data += 1
                        all_ssid_info_list.append({
                            "device_ip": ip_address,
                            "ssid_details": ssid_data
                        })
                        self.log("SSID configuration found for wireless controller {0} - retrieved {1} SSID records".format(ip_address, len(ssid_data)), "INFO")
                    else:
                        devices_without_ssid_data += 1
                        all_ssid_info_list.append({
                            "device_ip": ip_address,
                            "ssid_details": "No SSID info found"
                        })
                        self.log(
                            "No SSID configuration found for wireless controller {0} - "
                            "controller may not have configured SSIDs".format(
                                ip_address
                            ),
                            "DEBUG"
                        )
                except Exception as api_err:
                    devices_with_errors += 1
                    self.msg = "Failed to retrieve SSID configuration for wireless controller {0}: {1}".format(ip_address, str(api_err))
                    self.log(self.msg, "ERROR")

                    all_ssid_info_list.append({
                        "device_ip": ip_address,
                        "ssid_details": "Error: {0}".format(api_err)
                    })

        result = [{"ssid_info": all_ssid_info_list}]

        total_fabric_devices = len(fabric_devices)
        self.log(
            "Wireless SSID configuration retrieval completed - "
            "processed {0}/{1} fabric devices successfully".format(
                devices_processed,
                total_fabric_devices
            ),
            "INFO"
        )
        if wireless_devices_found > 0:
            self.log("Wireless controllers identified for SSID analysis: {0}".format(wireless_devices_found), "INFO")

        if non_wireless_devices_found > 0:
            self.log("Non-wireless devices skipped for SSID analysis: {0}".format(non_wireless_devices_found), "INFO")

        if devices_with_ssid_data > 0:
            self.log("Wireless controllers with SSID configurations: {0}".format(devices_with_ssid_data), "INFO")

        if devices_without_ssid_data > 0:
            self.log("Wireless controllers without SSID configurations: {0}".format(devices_without_ssid_data), "INFO")

        if devices_with_errors > 0:
            self.log("Warning: {0} devices encountered errors during SSID configuration retrieval".format(devices_with_errors), "WARNING")

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
