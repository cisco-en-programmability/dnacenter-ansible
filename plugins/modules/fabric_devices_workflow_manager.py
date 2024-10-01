#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright (c) 2024, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

"""Ansible module to perform operations on SDA fabric devices in Cisco Catalyst Center."""
from __future__ import absolute_import, division, print_function

__metaclass__ = type
__author__ = ['Muthu Rakesh, Madhan Sankaranarayanan']
DOCUMENTATION = r"""
---
module: fabric_devices_workflow_manager
short_description: Resource module for SDA fabric devices
description:
- Manage operations on SDA fabric devices.
- API to add the fabric devices.
- API to update the fabric devices.
- API to delete the fabric devices.
- API to add fabric devices L2 Handoff.
- API to delete fabric devices L2 Handoff.
- API to add fabric devices L3 Handoff with IP transit.
- API to update fabric devices L3 Handoff with IP transit.
- API to delete fabric devices L3 Handoff with IP transit.
- API to add fabric devices L3 Handoff with SDA transit.
- API to update fabric devices L3 Handoff with SDA transit.
- API to delete fabric devices L3 Handoff with SDA transit.
version_added: '6.20.0'
extends_documentation_fragment:
  - cisco.dnac.workflow_manager_params
author: Muthu Rakesh (@MUTHU-RAKESH-27)
        Madhan Sankaranarayanan (@madhansansel)
options:
  config_verify:
    description: Set to True to verify the Cisco Catalyst Center after applying the playbook config.
    type: bool
    default: False
  state:
    description: The state of Cisco Catalyst Center after module completion.
    type: str
    choices: [ merged, deleted ]
    default: merged
  config:
    description:
    - A list of SDA fabric devices configurations.
    - Each entry in the list represents a fabric devices associated with a fabric site configurations.
    type: list
    elements: dict
    required: true
    suboptions:
      fabric_devices:
        description: SDA fabric devices associated with a fabric site configurations.
        type: dict
        suboptions:
          fabric_name:
            description:
            - Name of the SDA fabric site.
            - Mandatory parameter for all operations under fabric_devices.
            - Creation of the fabric site is a prerequisites.
            - A Fabric Site is composed of networking devices operating in SD-Access Fabric roles.
            - A Fabric Site must have a Border Node and a Control Plane Node, it will also have Edge Nodes.
            - A Fabric Site may also have Fabric Wireless LAN Controllers and Fabric Wireless Access Points.
            type: str
          device_config:
            description: Contains the list of devices and their border settings, L2 Handoff,
                         L3 Handoff with SDA transit, L3 Handoff with IP transit.
            type: list
            elements: dict
            suboptions:
              device_ip:
                description:
                - IP address of the device to be added in the fabric site.
                - Mandatory parameter for all operations under fabric_devices.
                - Device should be provisioned to the site is a prerequisites.
                type: str
              delete_fabric_device:
                description:
                - Effective only when the state is deleted.
                - Set it to True to delete the device from the fabric site.
                - Set it to False to not to delete the device from the fabric site.
                type: bool
              device_roles:
                description:
                - Role of the device in the fabric site.
                - Mandatory parameter for adding the device to the fabric site.
                - device_roles cannot be updated.
                - Atleast one device should be CONTROL_PLANE_NODE to assign other to other devices.
                - CONTROL_PLANE_NODE - Manages the mapping of endpoint IP addresses
                                       to their location within the network. Uses
                                       LISP to handle the mobility.
                  EDGE_NODE - Device that connects endpoints to the SDA network.
                              Handles policy enforcement, segmentation, and
                              communication with the control plane.
                  BORDER_NODE - Serves as the gateway between the fabric and external networks.
                                It manages traffic entering or exiting the SDA environment.
                  WIRELESS_CONTROLLER_NODE - Manages and controls wireless access points and
                                             devices within the network.
                choices: [CONTROL_PLANE_NODE, EDGE_NODE, BORDER_NODE, WIRELESS_CONTROLLER_NODE]
                type: list
                elements: str
              borders_settings:
                description:
                - Effective only when the device_roles contains BORDER_NODE.
                - Mandatory parameter for adding the device to fabric site, when the device_roles contains BORDER_NODE.
                - borders_settings can be updated.
                - Border type can be Layer2 or Layer3.
                - Border type is identified by check the presence of L2 Handoff, L3 Handoff with IP or SDA transit.
                type: dict
                suboptions:
                  layer3_settings:
                    description: Manages a device with the border type as Layer3.
                    type: list
                    elements: dict
                    suboptions:
                      local_autonomous_system_number:
                        description:
                        - Used to identify the local autonomous system in BGP routing.
                        - Mandatory parameter to add the a device with role as BORDER_ROLE.
                        - local_autonomous_system_number cannot be updated.
                        - local_autonomous_system_number can be from 1 to 4,294,967,295.
                        - Dot notation is also allowed. Varies from 1.0 to 65535.65535. For example, 65534.65535
                        type: str
                      is_default_exit:
                        description:
                        - Default gateway used for routing traffic from the fabric to external networks.
                        - Provides a path for traffic to exit the virtual network via the Border Node.
                        - Default value is True.
                        - is_default_exit can be updated.
                        type: bool
                      import_external_routes:
                        description:
                        - Prevents the import of routes learned from external networks into the fabric.
                        - Ensures that only internal routes within the SDA fabric are used, enhances security.
                        - Default value is True.
                        - import_external_routes can be updated.
                        type: bool
                      border_priority:
                        description:
                        - Determines the preference level for a Border Node when multiple border nodes are available.
                        - A higher-priority border node is preferred for routing traffic to external networks.
                        - border_priority should be between 1 to 9.
                        - If border_priority is not set, the default value is 10.
                        - border_priority can be updated.
                        type: int
                      prepend_autonomous_system_count:
                        description:
                        - Artificially increase the AS path length when advertising routes via BGP.
                        - Makes a route appear less favorable to external peers.
                        - prepend_autonomous_system_count should be between 1 to 10.
                        - If prepend_autonomous_system_count is not set, the default value is 0.
                        - prepend_autonomous_system_count can be updated.
                        type: int
                  layer3_handoff_ip_transit:
                    description:
                    - Adds layer 3 handoffs with ip transit in fabric devices.
                    - Configured when IP traffic is routed from the SDA fabric to external networks.
                    - If layer3_handoff_ip_transit is set, border type will be considered as Layer3.
                    type: list
                    elements: dict
                    suboptions:
                      transit_network_name:
                        description:
                        - Network that connects multiple SDA fabrics or networks.
                        - Mandatory parameter for all operations in L3 Handoff with IP transit.
                        - transit_network_name cannot be updated.
                        type: str
                      interface_name:
                        description:
                        - Refers to the specific network interface in the border device.
                        - Mandatory parameter for all operations in L3 Handoff with IP transit.
                        - interface_name cannot be updated.
                        type: str
                      external_connectivity_ip_pool_name:
                        description:
                        - IP address range allocated for communication between the SDA fabric and external networks.
                        - Mandatory parameter for adding the L3 Handoff with IP transit.
                        - This IP pool should be reserved in the fabric site.
                        - If external_connectivity_ip_pool_name is set, then no need to set the local and remote addresses.
                        - Setting external_connectivity_ip_pool_name will automatically set the local and remote adresses.
                        - If both are set, external_connectivity_ip_pool_name will be given higher priority.
                        - Updating the IP addresses are not permitted.
                        type: str
                      virtual_network_name:
                        description:
                        - Refers to the logical segmentation of the network, grouping devices into isolated virtual networks.
                        - Either virtual_network_name or vlan_id is mandatory for all operations in L3 Handoff with IP transit.
                        type: str
                      vlan_id:
                        description:
                        - Unique identifier assigned to a Virtual Local Area Network
                        - Should be unique across the entire fabric site settings.
                        - vlan_id can be from 1 to 4094. Except 1, 1002-1005, 2046, 4094.
                        - Either virtual_network_name or vlan_id is mandatory for all operations in L3 Handoff with IP transit.
                        - vlan_id cannot be updated.
                        type: int
                      tcp_mss_adjustment:
                        description:
                        - Allows the modification of the Maximum Segment Size in TCP packets.
                        - tcp_mss_adjustment can be from 500 to 1440.
                        - tcp_mss_adjustment can be updated.
                        type: int
                      local_ip_address:
                        description:
                        - IP address assigned to a devices interface within the fabric.
                        - local_ip_address is for IPv4.
                        - local_ip_address and remote_ip_address should fall in same subnet.
                        - Either local and remote addresses or external_connectivity_ip_pool_name are mandatory.
                        - If both are set, external_connectivity_ip_pool_name will be given higher priority.
                        type: str
                      remote_ip_address:
                        description:
                        - IP address of a device located outside the fabric network, often used for BGP peering.
                        - remote_ip_address is for IPv4.
                        - local_ip_address and remote_ip_address should fall in same subnet.
                        - Either local and remote addresses or external_connectivity_ip_pool_name are mandatory.
                        - If both are set, external_connectivity_ip_pool_name will be given higher priority.
                        type: str
                      local_ipv6_address:
                        description:
                        - IP address of a device located outside the fabric network, often used for BGP peering.
                        - local_ipv6_address is for IPv6.
                        - local_ipv6_address and remote_ipv6_address should fall in same subnet.
                        - If remote_ipv6_address is provided, then local_ipv6_address is mandatory.
                        - If both are set, external_connectivity_ip_pool_name will be given higher priority.
                        type: str
                      remote_ipv6_address:
                        description:
                        - IP address of a device located outside the fabric network, often used for BGP peering.
                        - remote_ipv6_address is for IPv6.
                        - local_ipv6_address and remote_ipv6_address should fall in same subnet.
                        - If local_ipv6_address is provided, then local_ipv6_address is mandatory.
                        - If both are set, external_connectivity_ip_pool_name will be given higher priority.
                        type: str
                  layer3_handoff_sda_transit:
                    description:
                    - Adds layer 3 handoffs with SDA transit in fabric devices.
                    - Configured when routing traffic is routed from the SDA fabric to external networks.
                    - If layer3_handoff_sda_transit is set, border type will be considered as Layer3.
                    type: dict
                    suboptions:
                      transit_network_name:
                        description:
                        - Network that connects multiple SDA fabrics or networks.
                        - Mandatory parameter for all operations in L3 Handoff with SDA transit.
                        - transit_network_name cannot be updated.
                        type: str
                      affinity_id_prime:
                        description:
                        - It supersedes the border priority to determine border node preference.
                        - The lower the relative value of affinity id prime, the higher the preference.
                        - Resources with the same affinity ID are treated similarly and affinity_id_decider decides the priority.
                        - affinity_id_prime ranges from 0 to 2147483647.
                        - affinity_id_prime can be updated.
                        type: int
                      affinity_id_decider:
                        description:
                        - If affinity id prime value is the same, the affinity id decider value is used as a tiebreaker.
                        - The lower the relative value of affinity id prime, the higher the preference.
                        - affinity_id_decider ranges from 0 to 2147483647.
                        - affinity_id_decider can be updated.
                        type: int
                      connected_to_internet:
                        description:
                        - Set this true to allow associated site to provide internet access to other sites through SDA.
                        - Default value is False.
                        - connected_to_internet can be updated.
                        type: bool
                      is_multicast_over_transit_enabled:
                        description:
                        - Set this true to configure native multicast over multiple sites that are connected to an SDA transit.
                        - Default value is False.
                        - is_multicast_over_transit_enabled can be updated.
                        type: bool
                  layer2_handoff:
                    description:
                    - Adds layer 2 handoffs in fabric devices.
                    - L2 Handoff cannot be updated.
                    - Configured while transferring a devices data traffic at Layer 2 (Data Link layer).
                    - If layer2_handoff is set, border type will be considered as Layer2.
                    type: list
                    elements: dict
                    suboptions:
                      interface_name:
                        description:
                        - Refers to the specific network interface in the border device.
                        - Mandatory parameter for all operations in L2 Handoff.
                        - interface_name cannot be updated.
                        type: str
                      internal_vlan_id:
                        description:
                        - Represents the VLAN identifier used within the fabric for traffic segmentation among devices.
                        - Should be unique across the entire fabric site settings.
                        - Mandatory for all operations in layer2_handoff.
                        - internal_vlan_id can be from 1 to 4094. Except 1, 1002-1005, 2046, 4094.
                        type: int
                      external_vlan_id:
                        description:
                        - Represents to the VLAN identifier used for traffic that exits the fabric to external networks.
                        - Should be unique across the entire fabric site settings.
                        - Mandatory for all operations in layer2_handoff.
                        - external_vlan_id can be from 1 to 4094. Except 1, 1002-1005, 2046, 4094.
                        type: int

requirements:
- dnacentersdk >= 2.9.2
- python >= 3.9
notes:
  - SDK Method used are
    site_design.SiteDesign.get_sites,
    network_settings.NetworkSettings.get_reserve_ip_subpool,
    devices.Devices.get_device_list,
    sda.Sda.get_transit_networks,
    sda.Sda.get_layer3_virtual_networks,
    sda.Sda.get_fabric_sites,
    sda.Sda.get_provisioned_devices,
    sda.Sda.get_fabric_devices_layer2_handoffs,
    sda.Sda.get_fabric_devices_layer3_handoffs_with_sda_transit,
    sda.Sda.get_fabric_devices_layer3_handoffs_with_ip_transit,
    sda.Sda.get_fabric_devices,
    sda.Sda.add_fabric_devices,
    sda.Sda.add_fabric_devices_layer2_handoffs,
    sda.Sda.add_fabric_devices_layer3_handoffs_with_sda_transit,
    sda.Sda.add_fabric_devices_layer3_handoffs_with_ip_transit,
    sda.Sda.update_fabric_devices,
    sda.Sda.update_fabric_devices_layer3_handoffs_with_sda_transit,
    sda.Sda.update_fabric_devices_layer3_handoffs_with_ip_transit,
    sda.Sda.delete_fabric_device_layer2_handoff_by_id,
    sda.Sda.delete_fabric_device_by_id,
    sda.Sda.delete_fabric_device_layer3_handoffs_with_sda_transit,
    sda.Sda.delete_fabric_device_layer3_handoff_with_ip_transit_by_id,
    task.Task.get_tasks_by_id,
    task.Task.get_task_details_by_id,

  - Paths used are
    get /dna/intent/api/v1/sites
    get /dna/intent/api/v1/reserve-ip-subpool
    get /dna/intent/api/v1/network-device
    get /dna/intent/api/v1/sda/transitNetworks
    get /dna/intent/api/v1/sda/layer3VirtualNetworks
    get /dna/intent/api/v1/sda/fabricSites
    get /dna/intent/api/v1/sda/provisionDevices
    get /dna/intent/api/v1/sda/fabricDevices/layer2Handoffs
    get /dna/intent/api/v1/sda/fabricDevices/layer3Handoffs/sdaTransits
    get /dna/intent/api/v1/sda/fabricDevices/layer3Handoffs/ipTransits
    get /dna/intent/api/v1/sda/fabricDevices
    post /dna/intent/api/v1/sda/fabricDevices
    post /dna/intent/api/v1/sda/fabricDevices/layer2Handoffs
    post /dna/intent/api/v1/sda/fabricDevices/layer3Handoffs/sdaTransits
    post /dna/intent/api/v1/sda/fabricDevices/layer3Handoffs/ipTransits
    put /dna/intent/api/v1/sda/fabricDevices
    put /dna/intent/api/v1/sda/fabricDevices/layer3Handoffs/sdaTransits
    put /dna/intent/api/v1/sda/fabricDevices/layer3Handoffs/ipTransits
    delete /dna/intent/api/v1/sda/fabricDevices/${id}
    delete /dna/intent/api/v1/sda/fabricDevices/layer2Handoffs/${id}
    delete /dna/intent/api/v1/sda/fabricDevices/layer3Handoffs/sdaTransits
    delete /dna/intent/api/v1/sda/fabricDevices/layer3Handoffs/ipTransits/${id}
    get /dna/intent/api/v1/tasks/${id}
    get /dna/intent/api/v1/tasks/${id}/detail

"""

EXAMPLES = r"""
- name: Create SDA fabric device with device role as CONTROL_PLANE_NODE
  cisco.dnac.fabric_devices_workflow_manager:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    dnac_log: True
    dnac_log_level: "{{ dnac_log_level }}"
    state: merged
    config_verify: True
    config:
    - fabric_devices:
        fabric_name: Global/USA/SAN-JOSE
        device_config:
        - device_ip: 10.0.0.1
          device_roles: [CONTROL_PLANE_NODE]

- name: Update the SDA fabric device with the device roles with BORDER_NODE and add L2 Handoff
  cisco.dnac.fabric_devices_workflow_manager:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    dnac_log: True
    dnac_log_level: "{{ dnac_log_level }}"
    state: merged
    config_verify: True
    config:
    - fabric_devices:
        fabric_name: Global/USA/SAN-JOSE
        device_config:
        - device_ip: 10.0.0.1
          device_roles: [CONTROL_PLANE_NODE, BORDER_NODE]
          borders_settings:
            layer3_settings:
              local_autonomous_system_number: 1234
              is_default_exit: true
              import_external_routes: true
              border_priority: 2
              prepend_autonomous_system_count: 2
            layer2_handoff:
            - interface_name: FortyGigabitEthernet1/1/1
              internal_vlan_id: 550
              external_vlan_id: 551


- name: Add the L3 Handoff with SDA Transit to the SDA fabric device
  cisco.dnac.fabric_devices_workflow_manager:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    dnac_log: True
    dnac_log_level: "{{ dnac_log_level }}"
    state: merged
    config_verify: True
    config:
    - fabric_devices:
        fabric_name: Global/USA/SAN-JOSE
        device_config:
        - device_ip: 10.0.0.1
          device_roles: [CONTROL_PLANE_NODE, BORDER_NODE]
          borders_settings:
            layer3_handoff_sda_transit:
              transit_network_name: SDA_PUB_SUB_TRANSIT
              affinity_id_prime: 1
              affinity_id_decider: 1
              connected_to_internet: true
              is_multicast_over_transit_enabled: false

- name: Add L3 Handoff with IP Transit to the SDA fabric device with external_connectivity_ip_pool_name
  cisco.dnac.fabric_devices_workflow_manager:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    dnac_log: True
    dnac_log_level: "{{ dnac_log_level }}"
    state: merged
    config_verify: True
    config:
    - fabric_devices:
        fabric_name: Global/USA/SAN-JOSE
        device_config:
        - device_ip: 10.0.0.1
          device_roles: [CONTROL_PLANE_NODE, BORDER_NODE]
          borders_settings:
            layer3_handoff_ip_transit:
            - transit_network_name: IP_TRANSIT_1
              interface_name: FortyGigabitEthernet1/1/1
              external_connectivity_ip_pool_name: Reserved_sda_test_1
              virtual_network_name: L3VN1
              vlan_id: 440
              tcp_mss_adjustment: 2

- name: Add L3 Handoff with IP Transit to the SDA fabric device with local and remote network
  cisco.dnac.fabric_devices_workflow_manager:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    dnac_log: True
    dnac_log_level: "{{ dnac_log_level }}"
    state: merged
    config_verify: True
    config:
    - fabric_devices:
        fabric_name: Global/USA/SAN-JOSE
        device_config:
        - device_ip: 10.0.0.1
          device_roles: [CONTROL_PLANE_NODE, BORDER_NODE]
          borders_settings:
            layer3_handoff_ip_transit:
            - transit_network_name: IP_TRANSIT_1
              interface_name: FortyGigabitEthernet1/1/1
              virtual_network_name: L3VN1
              vlan_id: 440
              tcp_mss_adjustment: 510
              local_ip_address: 10.0.0.1/24
              remote_ip_address: 10.0.0.2/24
              local_ipv6_address: 2009:db8::1/64
              remote_ipv6_address: 2009:db8::2/64

- name: Update the border settings of the SDA Devices
  cisco.dnac.fabric_devices_workflow_manager:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    dnac_log: True
    dnac_log_level: "{{ dnac_log_level }}"
    state: merged
    config_verify: True
    config:
    - fabric_devices:
        fabric_name: Global/USA/SAN-JOSE
        device_config:
        - device_ip: 10.0.0.1
          device_roles: [CONTROL_PLANE_NODE, BORDER_NODE]
          borders_settings:
            layer3_settings:
              local_autonomous_system_number: 1234
              is_default_exit: false
              import_external_routes: false
              border_priority: 1
              prepend_autonomous_system_count: 3

- name: Update the L3 Handoffs with SDA Transit and IP Transit.
  cisco.dnac.fabric_devices_workflow_manager:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    dnac_log: True
    dnac_log_level: "{{ dnac_log_level }}"
    state: merged
    config_verify: True
    config:
    - fabric_devices:
        fabric_name: Global/USA/SAN-JOSE
        device_config:
        - device_ip: 10.0.0.1
          device_roles: [CONTROL_PLANE_NODE, BORDER_NODE]
          borders_settings:
            layer3_handoff_sda_transit:
              transit_network_name: SDA_PUB_SUB_TRANSIT
              affinity_id_prime: 2
              affinity_id_decider: 2
              connected_to_internet: false
              is_multicast_over_transit_enabled: true

            layer3_handoff_ip_transit:
            - transit_network_name: IP_TRANSIT_1
              interface_name: FortyGigabitEthernet1/1/1
              virtual_network_name: L3VN1
              vlan_id: 440
              tcp_mss_adjustment: 511
              local_ip_address: 10.0.0.1/24
              remote_ip_address: 10.0.0.2/24
              local_ipv6_address: 2009:db8::1/64
              remote_ipv6_address: 2009:db8::2/64

- name: Delete the L2 Handoff
  cisco.dnac.fabric_devices_workflow_manager:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    dnac_log: True
    dnac_log_level: "{{ dnac_log_level }}"
    state: deleted
    config_verify: True
    config:
    - fabric_devices:
        fabric_name: Global/USA/SAN-JOSE
        device_config:
        - device_ip: 10.0.0.1
          borders_settings:
            layer2_handoff:
            - interface_name: FortyGigabitEthernet1/1/1
              internal_vlan_id: 550

- name: Delete the L3 Handoff with SDA Transit
  cisco.dnac.fabric_devices_workflow_manager:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    dnac_log: True
    dnac_log_level: "{{ dnac_log_level }}"
    state: deleted
    config_verify: True
    config:
    - fabric_devices:
        fabric_name: Global/USA/SAN-JOSE
        device_config:
        - device_ip: 10.0.0.1
          borders_settings:
            layer3_handoff_sda_transit:
              transit_network_name: SDA_PUB_SUB_TRANSIT

- name: Delete the L3 Handoff with IP Transit
  cisco.dnac.fabric_devices_workflow_manager:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    dnac_log: True
    dnac_log_level: "{{ dnac_log_level }}"
    state: deleted
    config_verify: True
    config:
    - fabric_devices:
        fabric_name: Global/USA/SAN-JOSE
        device_config:
        - device_ip: 10.0.0.1
          borders_settings:
            layer3_handoff_ip_transit:
            - transit_network_name: IP_TRANSIT_1
              interface_name: FortyGigabitEthernet1/1/1
              virtual_network_name: L3VN1

- name: Delete the device along with L2 Handoff and L3 Handoff
  cisco.dnac.fabric_devices_workflow_manager:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    dnac_log: True
    dnac_log_level: "{{ dnac_log_level }}"
    state: deleted
    config_verify: True
    config:
    - fabric_devices:
        fabric_name: Global/USA/SAN-JOSE
        device_config:
        - device_ip: 10.0.0.1
          delete_fabric_device: true
          borders_settings:
            layer3_handoff_ip_transit:
            - transit_network_name: IP_TRANSIT_1
              interface_name: FortyGigabitEthernet1/1/1
              virtual_network_name: L3VN1

            layer3_handoff_sda_transit:
              transit_network_name: SDA_PUB_SUB_TRANSIT

            layer2_handoff:
            - interface_name: FortyGigabitEthernet1/1/1
              internal_vlan_id: 550
"""

RETURN = r"""
# Case_1: Successful addition of SDA fabric devices
response_1:
  description: A dictionary or list with the response returned by the Cisco Catalyst Center Python SDK
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

# Case_2: Successful updation of SDA fabric devices
response_2:
  description: A dictionary or list with the response returned by the Cisco Catalyst Center Python SDK
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

# Case_3: Successful deletion of SDA fabric devices
response_3:
  description: A dictionary or list with the response returned by the Cisco Catalyst Center Python SDK
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

# Case_4: Successful creation L2 Handoff in fabric device
response_4:
  description: A dictionary or list with the response returned by the Cisco Catalyst Center Python SDK
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


# Case_5: Successful deletion L2 Handoff in fabric device
response_5:
  description: A dictionary or list with the response returned by the Cisco Catalyst Center Python SDK
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


# Case_6: Successful creation L3 Handoff with SDA transit in fabric device
response_6:
  description: A dictionary or list with the response returned by the Cisco Catalyst Center Python SDK
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

# Case_7: Successful updation L3 Handoff with SDA transit in fabric device
response_7:
  description: A dictionary or list with the response returned by the Cisco Catalyst Center Python SDK
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

# Case_8: Successful updation L3 Handoff with SDA transit in fabric device
response_8:
  description: A dictionary or list with the response returned by the Cisco Catalyst Center Python SDK
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

# Case_9: Successful deletion L3 Handoff with SDA transit in fabric device
response_9:
  description: A dictionary or list with the response returned by the Cisco Catalyst Center Python SDK
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

# Case_10: Successful creation L3 Handoff with IP transit in fabric device
response_10:
  description: A dictionary or list with the response returned by the Cisco Catalyst Center Python SDK
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

# Case_11: Successful updation L3 Handoff with IP transit in fabric device
response_11:
  description: A dictionary or list with the response returned by the Cisco Catalyst Center Python SDK
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

# Case_12: Successful deletion L3 Handoff with IP transit in fabric device
response_12:
  description: A dictionary or list with the response returned by the Cisco Catalyst Center Python SDK
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

import time
from ansible.module_utils.basic import AnsibleModule
from ansible_collections.cisco.dnac.plugins.module_utils.dnac import (
    DnacBase,
    validate_list_of_dicts,
    get_dict_result,
    dnac_compare_equality,
)


class FabricDevices(DnacBase):
    """Class containing member attributes for fabric_devices_workflow_manager module"""

    def __init__(self, module):
        super().__init__(module)
        self.result["response"] = []
        self.fabric_devices_obj_params = self.get_obj_params("fabricDevices")
        self.fabric_l3_handoff_sda_obj_params = self.get_obj_params("fabricSdaL3Handoff")
        self.fabric_l3_handoff_ip_obj_params = self.get_obj_params("fabricIpL3Handoff")
        self.max_timeout = self.params.get('dnac_api_task_timeout')

    def validate_input(self):
        """
        Checks if the configuration parameters provided in the playbook
        meet the expected structure and data types,
        as defined in the 'temp_spec' dictionary.

        Parameters:
            self (object): The current object details.
        Returns:
            self (object): The current object with updated desired Fabric Devices information.
        Example:
            If the validation succeeds, 'self.status' will be 'success' and
            'self.validated_config' will contain the validated configuration.
            If it fails, 'self.status' will be 'failed', and
            'self.msg' will describe the validation issues.
        """

        if not self.config:
            self.msg = "config not available in playbook for validation."
            self.status = "success"
            return self

        # temp_spec is the specification for the expected structure of configuration parameters
        temp_spec = {
            "fabric_devices": {
                "type": 'list',
                "elements": 'dict',
                "fabric_name": {"type": 'string'},
                "device_config": {
                    "type": 'list',
                    "elements": 'dict',
                    "device_ip": {"type": 'string'},
                    "delete_fabric_device": {"type": 'bool'},
                    "device_roles": {
                        "type": 'list',
                        "elements": 'str',
                    },
                    "borders_settings": {
                        "type": 'list',
                        "elements": 'dict',
                        "layer3_settings": {
                            "type": 'dict',
                            "local_autonomous_system_number": {"type": 'string'},
                            "is_default_exit": {"type": 'bool'},
                            "import_external_routes": {"type": 'bool'},
                            "border_priority": {"type": 'integer'},
                            "prepend_autonomous_system_count": {"type": 'integer'}
                        },
                        "layer3_handoff_ip_transit": {
                            "type": 'list',
                            "elements": 'dict',
                            "transit_network_name": {"type": 'string'},
                            "interface_name": {"type": 'string'},
                            "external_connectivity_ip_pool_name": {"type": 'string'},
                            "virtual_network_name": {"type": 'string'},
                            "vlan_id": {"type": 'integer'},
                            "tcp_mss_adjustment": {"type": 'integer'},
                            "local_ip_address": {"type": 'string'},
                            "remote_ip_address": {"type": 'string'},
                            "local_ipv6_address": {"type": 'string'},
                            "remote_ipv6_address": {"type": 'string'},
                        },
                        "layer3_handoff_sda_transit": {
                            "type": 'list',
                            "elements": 'dict',
                            "transit_network_name": {"type": 'string'},
                            "affinity_id_prime": {"type": 'integer'},
                            "affinity_id_decider": {"type": 'integer'},
                            "connected_to_internet": {"type": 'bool'},
                            "is_multicast_over_transit_enabled": {"type": 'bool'}
                        },
                        "layer2_handoff": {
                            "type": 'list',
                            "elements": 'dict',
                            "interface_name": {"type": 'string'},
                            "internal_vlan_id": {"type": 'integer'},
                            "external_vlan_id": {"type": 'integer'}
                        }
                    }
                }
            }
        }

        # Validate playbook params against the specification (temp_spec)
        valid_temp, invalid_params = validate_list_of_dicts(self.config, temp_spec)
        if invalid_params:
            self.msg = (
                "Invalid parameters in playbook: {invalid_params}"
                .format(invalid_params="\n".join(invalid_params))
            )
            self.status = "failed"
            return self

        self.validated_config = valid_temp
        self.log("Successfully validated playbook config params: {valid_temp}"
                 .format(valid_temp=valid_temp), "INFO")
        self.msg = "Successfully validated input from the playbook."
        self.status = "success"
        return self

    def requires_update(self, have, want, obj_params):
        """
        Check if the config given requires update by comparing
        current information with the requested information.

        This method compares the current fabric devices information from
        Cisco Catalyst Center with the user-provided details from the playbook,
        using a specified schema for comparison.

        Parameters:
            have (dict): Current information from the Cisco Catalyst Center
                          of SDA fabric devices.
            want (dict): Users provided information from the playbook
            obj_params (list of tuples) - A list of parameter mappings specifying which
                                          Cisco Catalyst Center parameters (dnac_param) correspond to
                                          the user-provided parameters (ansible_param).
        Returns:
            bool - True if any parameter specified in obj_params differs between
            current_obj and requested_obj, indicating that an update is required.
            False if all specified parameters are equal.
        Description:
            This function checks both the information provided by the user and
            the information available in the Cisco Catalyst Center.
            Based on the object_params the comparison will be taken place.
            If there is a difference in those information, it will return True.
            Else False.
        """

        current_obj = have
        requested_obj = want
        self.log("Current State (have): {current_obj}".format(current_obj=current_obj), "DEBUG")
        self.log("Desired State (want): {requested_obj}".format(requested_obj=requested_obj), "DEBUG")

        return any(not dnac_compare_equality(current_obj.get(dnac_param),
                                             requested_obj.get(ansible_param))
                   for (dnac_param, ansible_param) in obj_params)

    def get_obj_params(self, get_object):
        """
        Get the required comparison obj_params value

        Parameters:
            get_object (str): identifier for the required obj_params
        Returns:
            obj_params (list): obj_params value for comparison.
        Description:
            This function gets the object for the requires_update function.
            The obj_params will have the pattern to be compared.
        """

        try:
            if get_object == "fabricDevices":
                obj_params = [
                    ("borderTypes", "borderTypes"),
                    ("layer3Settings", "layer3Settings"),
                ]
            elif get_object == "fabricSdaL3Handoff":
                obj_params = [
                    ("affinityIdPrime", "affinityIdPrime"),
                    ("affinityIdDecider", "affinityIdDecider"),
                    ("connectedToInternet", "connectedToInternet"),
                    ("isMulticastOverTransitEnabled", "isMulticastOverTransitEnabled"),
                ]
            elif get_object == "fabricIpL3Handoff":
                obj_params = [
                    ("tcpMssAdjustment", "tcpMssAdjustment"),
                ]
            else:
                raise ValueError("Received an unexpected value for 'get_object': {object_name}"
                                 .format(object_name=get_object))
        except Exception as msg:
            self.log("Received exception: {msg}".format(msg=msg), "CRITICAL")

        return obj_params

    def get_transit_id_from_name(self, transit_name):
        """
        Get the transit ID from the transit name.

        Parameters:
            transit_name (str): The name of the transit network.
        Returns:
            transit_id (str or None): The ID of the transit network. None, if transit doesnot exist.
        Description:
            Call the API 'get_transit_networks' by setting the 'name' field with the
            given transit name.
            If the response is not empty, fetch the Id and return. Else, return None.
        """

        transit_id = None
        try:
            transit_details = self.dnac._exec(
                family="sda",
                function="get_transit_networks",
                op_modifies=True,
                params={"name": transit_name},
            )

            # If the SDK returns no response, then the transit doesnot exist
            transit_details = transit_details.get("response")
            if not transit_details:
                self.log(
                    "There is no transit network with the name '{name}'."
                    .format(name=transit_name)
                )
                return transit_id

            transit_id = transit_details[0].get("id")
        except Exception as msg:
            self.msg = (
                "Exception occured while running the API 'get_transit_networks': {msg}"
                .format(msg=msg)
            )
            self.log(self.msg, "CRITICAL")
            self.status = "failed"
            return self

        return transit_id

    def get_device_id_from_ip(self, device_ip):
        """
        Get the network device ID from the network device IP.

        Parameters:
            device_ip (str): The IP address of the network device.
        Returns:
            device_id (str or None): The ID of the network device. None, if the device doesnot exist.
        Description:
            Call the API 'get_device_list' by setting the 'management_ip_address' field with the
            given IP address.
            If the response is not empty, fetch the Id and return. Else, return None.
        """

        device_id = None
        try:
            device_details = self.dnac._exec(
                family="devices",
                function="get_device_list",
                op_modifies=True,
                params={"management_ip_address": device_ip},
            )

            # If the SDK returns no response, then the device doesnot exist
            device_details = device_details.get("response")
            if not device_details:
                self.log(
                    "There is no device with the IP address '{ip_address}'."
                    .format(ip_address=device_ip)
                )
                return device_id

            device_id = device_details[0].get("id")
        except Exception as msg:
            self.msg = (
                "Exception occured while running the API 'get_device_list': {msg}"
                .format(msg=msg)
            )
            self.log(self.msg, "CRITICAL")
            self.status = "failed"
            return self

        return device_id

    def check_valid_virtual_network_name(self, virtual_network_name):
        """
        Get the fabric ID from the given site hierarchy name.

        Parameters:
            virtual_network_name (str): The name of the L3 virtual network.
        Returns:
            True or False (bool): True if the L3 virtual network exists. Else, return False.
        Description:
            Call the API 'get_layer3_virtual_networks' by setting the 'virtual_network_name'
            and 'offset' field.
            Call the API till we reach empty response or we find the L3 virtual network with the
            given name.
            If the status is set to failed, return None. Else, return the fabric site ID.
        """

        try:
            virtual_network_details = self.dnac._exec(
                family="sda",
                function="get_layer3_virtual_networks",
                op_modifies=True,
                params={
                    "virtual_network_name": virtual_network_name,
                },
            )
            if not isinstance(virtual_network_details, dict):
                self.msg = "Error in getting virtual network details - Response is not a dictionary"
                self.log(self.msg, "CRITICAL")
                self.status = "failed"
                return self.check_return_status()

            # if the SDK returns no response, then the virtual network doesnot exist
            virtual_network_details = virtual_network_details.get("response")
            if not virtual_network_details:
                self.log(
                    "There is no L3 virtual network with the name '{name}."
                    .format(name=virtual_network_name)
                )
                return False

        except Exception as msg:
            self.msg = (
                "Exception occured while running the API 'get_layer3_virtual_networks': {msg}"
                .format(msg=msg)
            )
            self.log(self.msg, "CRITICAL")
            self.status = "failed"
            return self.check_return_status()

        return True

    def check_valid_reserved_pool(self, reserved_pool_name, fabric_name):
        """
        Get the fabric ID from the given site hierarchy name.

        Parameters:
            reserved_pool_name (str): The name of the reserved pool.
            fabric_name (str): The name of the fabric site to check for existence.
        Returns:
            True or False (bool): True if the reserved pool exists. Else, return False.
        Description:
            Call the API 'get_reserve_ip_subpool' by setting the 'site_id' and 'offset' field.
            Call the API till we reach empty response or we find the reserved subpool with the
            given subpool name.
            If the status is set to failed, return None. Else, return the fabric site ID.
        """

        try:
            (site_exists, site_id) = self.get_site_id(fabric_name)
            self.log(
                "The site with the name '{site_name} exists in Cisco Catalyst Center is '{site_exists}'"
                .format(site_name=fabric_name, site_exists=site_exists)
            )
            if not site_id:
                self.msg = (
                    "The site with the hierarchy name '{site_name}' is invalid."
                    .format(site_name=fabric_name)
                )
                self.status = "failed"
                return self.check_return_status()

            offset = 1
            start_time = time.time()

            # Calling the SDK with incremental offset till we find the reserved pool or empty response
            while True:
                all_reserved_pool_details = self.dnac._exec(
                    family="network_settings",
                    function="get_reserve_ip_subpool",
                    op_modifies=True,
                    params={
                        "site_id": site_id,
                        "offset": offset
                    },
                )
                if not isinstance(all_reserved_pool_details, dict):
                    self.msg = "Error in getting reserve pool - Response is not a dictionary"
                    self.log(self.msg, "CRITICAL")
                    self.status = "failed"
                    return self.check_return_status()

                offset += 25
                all_reserved_pool_details = all_reserved_pool_details.get("response")
                if not all_reserved_pool_details:
                    self.log(
                        "There is no reserved subpool in the site '{site_name}'."
                        .format(site_name=fabric_name)
                    )
                    return False

                # Check for maximum timeout, default value is 1200 seconds
                if (time.time() - start_time) >= self.max_timeout:
                    self.msg = (
                        "Max timeout of {0} sec has reached for the API 'get_reserved_ip_subpool' status."
                        .format(self.max_timeout)
                    )
                    self.status = "failed"
                    break

                # Find the reserved pool with the given name in the list of reserved pools
                reserved_pool_details = get_dict_result(all_reserved_pool_details, "groupName", reserved_pool_name)
                if reserved_pool_details:
                    self.log(
                        "The reserved pool found with the name '{reserved_pool}' in the site '{site_name}'."
                        .format(reserved_pool=reserved_pool_name, site_name=fabric_name)
                    )
                    return True

                self.log(
                    "The site hierarchy 'fabric_site' {fabric_name} is a valid fabric site."
                    .format(fabric_name=fabric_name)
                )
        except Exception as msg:
            self.msg = (
                "Exception occured while running the API 'get_reserve_ip_subpool': {msg}"
                .format(msg=msg)
            )
            self.log(self.msg, "CRITICAL")
            self.status = "failed"
            return self.check_return_status()

        return True

    def get_fabric_site_id_from_name(self, fabric_name):
        """
        Get the fabric ID from the given site hierarchy name.

        Parameters:
            fabric_name (str): The name of the fabric site to check for existence.
        Returns:
            fabric_site_id (str): The ID of the fabric site.
        Description:
            Call the API 'get_site' by setting the 'site_name_hierarchy' field with the
            given site name.
            If the status is set to failed, return None. Else, return the fabric site ID.
        """

        fabric_site_id = None
        try:
            (site_exists, site_id) = self.get_site_id(fabric_name)
            self.log(
                "The site with the name '{site_name} exists in Cisco Catalyst Center is '{site_exists}'"
                .format(site_name=fabric_name, site_exists=site_exists)
            )
            if not site_id:
                self.msg = (
                    "The site with the hierarchy name '{site_name}' is invalid."
                    .format(site_name=fabric_name)
                )
                self.status = "failed"
                return self.check_return_status()

            fabric_site_exists = self.dnac._exec(
                family="sda",
                function="get_fabric_sites",
                op_modifies=True,
                params={"site_id": site_id},
            )

            # If the status is 'failed', then the site is not a fabric
            status = fabric_site_exists.get("status")
            if status == "failed":
                self.log(
                    "The site hierarchy 'fabric_site' {fabric_name} is not a valid one or it not a 'Fabric' site."
                    .format(fabric_name=fabric_name), "ERROR"
                )
                return fabric_site_id

            self.log(
                "The site hierarchy 'fabric_site' {fabric_name} is a valid fabric site."
                .format(fabric_name=fabric_name)
            )
        except Exception as msg:
            self.msg = (
                "Exception occured while running the API 'get_fabric_sites': {msg}"
                .format(msg=msg)
            )
            self.log(self.msg, "CRITICAL")
            self.status = "failed"
            return self.check_return_status()

        return fabric_site_id

    def check_device_is_provisioned(self, fabric_device_ip, device_id):
        """
        Check if the device with the given IP is provisioned to the site or not.

        Parameters:
            fabric_device_ip (str): The IP address of the network device.
            device_id (str): The ID of the network device.
        Returns:
            self: The current object with updated desired Fabric Devices information.
        Description:
            Call the API 'get_provisioned_devices' by setting the 'network_device_id'
            field with the device ID.
            If the response is empty, return self by setting the self.msg and
            self.status as 'failed'.
        """

        try:
            provisioned_device_details = self.dnac._exec(
                family="sda",
                function="get_provisioned_devices",
                op_modifies=True,
                params={"network_device_id": device_id},
            )

            # If the response returned from the SDK is None, then the device is not provisioned to the site.
            provisioned_device_details = provisioned_device_details.get("response")
            if not provisioned_device_details:
                self.msg = (
                    "The network device with the IP address '{device_ip}' is not provisioned."
                    .format(device_ip=fabric_device_ip)
                )
                self.log(self.msg, "ERROR")
                self.status = "failed"

        except Exception as msg:
            self.msg = (
                "Exception occured while running the API 'get_provisioned_devices': {msg}"
                .format(msg=msg)
            )
            self.log(self.msg, "CRITICAL")
            self.status = "failed"

        return self

    def format_fabric_device_params(self, fabric_device_details):
        """
        Process the fabric device parameters retrieved from the Cisco Catalyst Center.

        Parameters:
            fabric_device_details (str): The fabric device details from the Cisco Catalyst Center.
        Returns:
            fabric_device_info (dict): Processed fabric device data in a format
            suitable for Cisco Catalyst Center configuration.
        Description:
            Form a dict with the params which is in accordance with the API payload structure.
        """

        fabric_device_info = {
            "id": fabric_device_details.get("id"),
            "fabricId": fabric_device_details.get("fabricId"),
            "networkDeviceId": fabric_device_details.get("networkDeviceId"),
            "deviceRoles": fabric_device_details.get("deviceRoles"),
            "borderDeviceSettings": fabric_device_details.get("borderDeviceSettings")
        }

        # Formatted payload for the SDK 'Add fabric devices', 'Update fabric devices'
        self.log(
            "The fabric device details are '{fabric_device_info}'"
            .format(fabric_device_info=fabric_device_info)
        )
        return fabric_device_info

    def l2_handoff_exists(self, fabric_id, device_id, internal_vlan_id, interface_name):
        """
        Check the availability of the L2 Handoff for the 'fabric_id', 'network_device_id',
        'internal_vlan_id' and return the ID of the Layer 2 Handoff.

        Parameters:
            fabric_id (str): The Id of the fabric site to check for existence.
            device_id (str): The Id of the provisioned device to check for existence.
            internal_vlan_id (str): The VLAN ID for the internal network.
            interface_name (str): The interface name of the network device.
        Returns:
            l2_handoff_id (dict or None) - L2 Handoff ID from the Cisco Catalyst Center.
        Description:
            Call the API 'get_fabric_devices_layer2_handoffs'. If the response is empty return None.
            Else, return the id of the l2 handoff.
        """

        l2_handoff_id = None
        offset = 1
        start_time = time.time()

        # Call the SDK with incremental offset till we find the L2 Handoff with given
        # interface name and internal vlan id
        while True:
            try:
                all_l2_handoff_details = self.dnac._exec(
                    family="sda",
                    function="get_fabric_devices_layer2_handoffs",
                    op_modifies=True,
                    params={
                        "fabric_id": fabric_id,
                        "network_device_id": device_id,
                        "offset": offset
                    }
                )
            except Exception as msg:
                self.msg = (
                    "Exception occured while running the API 'get_fabric_devices_layer2_handoffs': {msg}"
                    .format(msg=msg)
                )
                self.log(self.msg, "CRITICAL")
                self.status = "failed"
                return self.check_return_status()

            offset += 500
            if not isinstance(all_l2_handoff_details, dict):
                self.msg = "Failed to retrieve the L2 Handoff details - Response is not a dictionary"
                self.log(self.msg, "CRITICAL")
                self.status = "failed"
                return self.check_return_status()

            all_l2_handoff_details = all_l2_handoff_details.get("response")
            if not all_l2_handoff_details:
                self.log(
                    "There is no L2 Handoffs are available associated with the device with ID '{id}' in the Cisco Catalyst Center."
                    .format(id=device_id), "INFO"
                )
                break

            l2_handoff_details = next(item for item in all_l2_handoff_details
                                      if item.get("internalVlanId") == internal_vlan_id and
                                      item.get("interfaceName") == interface_name)
            l2_handoff_details = get_dict_result(all_l2_handoff_details, "internalVlanId", internal_vlan_id)
            if l2_handoff_details:
                self.log(
                    "The L2 handoff details with the internal VLAN Id: {details}"
                    .format(details=internal_vlan_id)
                )
                l2_handoff_id = l2_handoff_details.get("id")
                break

            end_time = time.time()
            if (end_time - start_time) >= self.max_timeout:
                self.msg = (
                    "Max timeout of {max_time} sec has reached for the API 'l2_handoff_exists' status."
                    .format(max_time=self.max_timeout)
                )
                self.status = "failed"
                return self.check_return_status()

        return l2_handoff_id

    def sda_l3_handoff_exists(self, fabric_id, device_id, transit_name):
        """
        Check the availability of the L2 Handoff for the 'fabric_id', 'network_device_id',
        'internal_vlan_id'.

        Parameters:
            fabric_id (str): The Id of the fabric site to check for existence.
            device_id (str): The Id of the provisioned device to check for existence.
            transit_name (str): The IP address of the the provisioned device.
        Returns:
            sda_l3_handoff_details (dict or None): The details of the L3 Handoff with SDA transit with
            the given transit name. None if the there is no L3 Handoff with SDA transit.
        Description:
            Call the API 'get_fabric_devices_layer3_handoffs_with_sda_transit'. If the response is
            empty return None. Else, return the details of the l3 handoff with SDA transit.
        """

        sda_l3_handoff_details = None
        transit_id = self.get_transit_id_from_name(transit_name)
        if not transit_id:
            self.msg = (
                "The SDA transit with the name '{name}' is not available in the Cisco Catalyst Center."
                .format(name=transit_name)
            )
            self.status = "failed"
            return self.check_return_status()

        start_time = time.time()
        offset = 1

        # Call the SDK with incremental offset till to find the SDA L3 Handoff
        while True:
            try:
                all_sda_l3_handoff_details = self.dnac._exec(
                    family="sda",
                    function="get_fabric_devices_layer3_handoffs_with_sda_transit",
                    op_modifies=True,
                    params={
                        "fabric_id": fabric_id,
                        "network_device_id": device_id,
                        "offset": offset
                    }
                )
            except Exception as msg:
                self.msg = (
                    "Exception occurred while getting the details of Layer3 Handoffs with SDA transit "
                    "with the transit name '{name}': {msg}".format(name=transit_name, msg=msg)
                )
                self.log(self.msg, "CRITICAL")
                self.status = "failed"
                return self.check_return_status()

            offset += 500
            if not isinstance(all_sda_l3_handoff_details, dict):
                self.msg = "Failed to retrieve the L2 Handoff details - Response is not a dictionary"
                self.log(self.msg, "CRITICAL")
                self.status = "failed"
                return self.check_return_status()

            all_sda_l3_handoff_details = all_sda_l3_handoff_details.get("response")
            if not all_sda_l3_handoff_details:
                self.log(
                    "There is no L3 Handoffs with SDA transit associated with the device with ID '{id}' in the Cisco Catalyst Center."
                    .format(id=device_id), "INFO"
                )
                break

            sda_l3_handoff_details = get_dict_result(all_sda_l3_handoff_details, "transitNetworkId", transit_id)
            if sda_l3_handoff_details:
                self.log(
                    "The L3 Handoff with SDA transit details with the transit name '{name}': '{details}"
                    .format(name=transit_name, details=sda_l3_handoff_details)
                )
                break

            end_time = time.time()
            if (end_time - start_time) >= self.max_timeout:
                self.msg = (
                    "Max timeout of {max_time} sec has reached for the API 'sda_l3_handoff_exists' status."
                    .format(max_time=self.max_timeout)
                )
                self.status = "failed"
                return self.check_return_status()

        return sda_l3_handoff_details

    def ip_l3_handoff_exists(self, fabric_id, device_id, transit_name,
                             virtual_network_name, vlan_id):
        """
        Check if the SDA fabric devices with the given fabric ID and
        the provisioned device ID exists or not.

        Parameters:
            fabric_id (str): The Id of the fabric site to check for existence.
            device_id (str): The Id of the provisioned device to check for existence.
            transit_name (str): The IP address of the the provisioned device.
            virtual_network_name (str): The Layer 3 virtual network name.
            vlan_id (str): The VLAN ID associated with the L3 Handoff IP transit.
        Returns:
            ip_l3_handoff_details (dict or None): The details of the L3 Handoff with IP transit with
            the given transit name, virtual network name or VLAN ID.
            None if the there is no L3 Handoff with Ip transit.
        Description:
            Call the API 'get_fabric_devices_layer3_handoffs_with_ip_transit'. If the response is
            empty return None. Else, return the details of the l3 handoff with SDA transit which matches
            the given transit name and virtual network name or vlan id from the fabric device.
        """

        ip_l3_handoff_details = None

        # Check if the transit name is valid or not
        # If yes, return the transit ID. Else, return a failure message.
        transit_id = self.get_transit_id_from_name(transit_name)
        if not transit_id:
            self.msg = (
                "The IP transit with the name '{name}' is not available in the Cisco Catalyst Center."
                .format(name=transit_name)
            )
            self.status = "failed"
            return self.check_return_status()

        start_time = time.time()
        offset = 1

        # Call the SDK with incremental offset till we find the IP L3 Handoff with given virtual network name
        while True:
            try:
                all_ip_l3_handoff_details = self.dnac._exec(
                    family="sda",
                    function="get_fabric_devices_layer3_handoffs_with_ip_transit",
                    op_modifies=True,
                    params={
                        "fabric_id": fabric_id,
                        "network_device_id": device_id,
                        "offset": offset
                    }
                )
            except Exception as msg:
                self.msg = (
                    "Exception occurred while getting the details of Layer3 Handoffs with IP transit "
                    "with the transit name '{name}': {msg}".format(name=transit_name, msg=msg)
                )
                self.log(self.msg, "CRITICAL")
                self.status = "failed"
                return self.check_return_status()

            offset += 500
            if not isinstance(all_ip_l3_handoff_details, dict):
                self.msg = "Failed to retrieve the L2 Handoff details - Response is not a dictionary"
                self.log(self.msg, "CRITICAL")
                self.status = "failed"
                return self.check_return_status()

            all_ip_l3_handoff_details = all_ip_l3_handoff_details.get("response")
            if not all_ip_l3_handoff_details:
                self.log(
                    "There is no L3 Handoffs with IP transit associated with the device with ID '{id}' in the Cisco Catalyst Center."
                    .format(id=device_id), "INFO"
                )
                break

            virtual_network = virtual_network_name
            check_string = "virtualNetworkName"
            if not virtual_network:
                virtual_network = vlan_id
                check_string = "vlanId"

            ip_l3_handoff_details = next(item for item in all_ip_l3_handoff_details
                                         if item.get("transitNetworkId") == transit_id and
                                         item.get(check_string) == virtual_network)
            if ip_l3_handoff_details:
                self.log(
                    "The L3 Handoff with IP transit details with the transit name '{name}': '{details}"
                    .format(name=transit_name, details=ip_l3_handoff_details)
                )
                break

            end_time = time.time()
            if (end_time - start_time) >= self.max_timeout:
                self.msg = (
                    "Max timeout of {max_time} sec has reached for the API 'ip_l3_handoff_exists' status."
                    .format(max_time=self.max_timeout)
                )
                self.status = "failed"
                return self.check_return_status()

        return ip_l3_handoff_details

    def fabric_device_exists(self, fabric_id, device_id, device_ip):
        """
        Check if the SDA fabric devices with the given fabric ID and
        the provisioned device ID exists or not.

        Parameters:
            fabric_id (str): The Id of the fabric site to check for existence.
            device_id (str): The Id of the provisioned device to check for existence.
            device_ip (str): The IP address of the the provisioned device.
        Returns:
            dict - A dictionary containing information about the
                   SDA fabric device's existence:
                - 'exists' (bool): True if the fabric device exists, False otherwise.
                - 'id' (str or None): The ID of the fabric device if it exists or None if it doesn't.
                - 'device_details' (dict or None): Details of the fabric device if it exists else None.
        Description:
            Sets the existance, details and the id of the fabric device as None.
            Calls the API 'get_fabric_devices' by settings the fields 'fabric_id'
            and 'network_device_id'.
            If the response is empty return the device_info, Else, format the given
            details and return the device_info.
        """

        device_info = {
            "exists": False,
            "device_details": None,
            "id": None,
        }
        fabric_device_details = self.dnac._exec(
            family="sda",
            function="get_fabric_devices",
            op_modifies=True,
            params={
                "fabric_id": fabric_id,
                "network_device_id": device_id,
            }
        )
        if not isinstance(fabric_device_details, dict):
            self.msg = "Error in getting fabric devices - Response is not a dictionary"
            self.log(self.msg, "ERROR")
            self.status = "failed"
            return self.check_return_status()

        # If the SDK return an empty response, then the fabric device is not available
        fabric_device_details = fabric_device_details.get("response")
        if not fabric_device_details:
            self.log("Fabric device with IP {ip} does not exist.".format(ip=device_ip), "DEBUG")
            return device_info

        self.log(
            "Fabric device with the IP address '{ip}' is found: {details}"
            .format(ip=device_ip, details=fabric_device_details), "INFO"
        )

        # Update the existence, details and the id of the fabric device
        device_info.update({
            "exists": True,
            "id": fabric_device_details[0].get("id"),
            "device_details": self.format_fabric_device_params(fabric_device_details[0])
        })

        self.log("SDA fabric device details: {details}".format(details=device_info.get("details")), "DEBUG")
        self.log("SDA fabric device id: {id}".format(id=device_info.get("id")), "DEBUG")
        return device_info

    def get_have_fabric_devices(self, fabric_devices):
        """
        Get the SDA fabric devices related information from Cisco
        Catalyst Center based on the provided playbook details.

        Parameters:
            fabric_devices (dict): Playbook details containing fabric devices details.
        Returns:
            self: The current object with updated current Fabric Devices information.
        Description:
            Set the structure for 'fabric_devices_info'. Get the fabric name and get the fabric ID.
            Get the network device IP and get the device ID. Check for the provisioning status.
            Check the existence of the fabric device. If exists, retrieve the device details.
            Check the availability of L2 Handoff, L3 Handoff with SDA Transit, L3 Handoff with IP Transit.
            Store it in 'fabric_devices_info' and return it.
        """

        fabric_devices_details = []
        fabric_name = fabric_devices.get("fabric_name")

        # Fabric name is mandatory for this workflow
        if not fabric_name:
            self.msg = "The required parameter 'fabric_name' in 'fabric_devices' is missing."
            self.log(self.msg, "ERROR")
            self.status = "failed"
            return self

        # Check if the fabric exists or not
        # If yes, return the id of the fabric site
        fabric_site_id = self.get_fabric_site_id_from_name(fabric_name).check_return_status()
        if not fabric_site_id:
            self.msg = (
                "The provided 'fabric_name' '{fabric_name}' is not a fabric site."
                .format(fabric_name=fabric_name)
            )
            self.log(self.msg, "ERROR")
            self.status = "failed"
            return self

        # device_config contains the list of devices on which the operations should be performed
        device_config = fabric_devices.get("device_config")
        if not device_config:
            self.msg = (
                "The parameter 'device_config' is mandatory under 'fabric_devices'."
            )
            self.status = "failed"
            return self

        for item in device_config:
            fabric_devices_info = {
                "exists": False,
                "device_details": None,
                "l2_handoff_ids": [],
                "sda_l3_handoff_details": None,
                "ip_l3_handoff_details": [],
                "id": None,
                "fabric_site_id": None,
                "network_device_id": None,
                "delete_fabric_device": False,
            }

            # Fabric device IP is mandatory for this workflow
            fabric_device_ip = item.get("device_ip")
            if not fabric_device_ip:
                self.msg = "The required parameter 'device_ip' in 'device_config' is missing."
                self.log(self.msg, "ERROR")
                self.status = "failed"
                return self

            network_device_id = self.get_device_id_from_ip(fabric_device_ip).check_return_status()

            # The device should be provisioned to the site
            self.check_device_is_provisioned(fabric_device_ip, network_device_id)
            delete_fabric_device = fabric_devices.get("delete_fabric_device")
            if not delete_fabric_device:
                delete_fabric_device = False

            fabric_devices_info.update({
                "fabric_site_id": fabric_site_id,
                "network_device_id": network_device_id,
                "delete_fabric_device": delete_fabric_device,
            })
            device_info = self.fabric_device_exists(fabric_site_id, network_device_id, fabric_device_ip)
            fabric_devices_info.update({
                "exists": device_info.get("exists"),
                "id": device_info.get("id"),
                "device_details": device_info.get("device_details")
            })
            device_exists = fabric_devices_info.get("exists")
            if not device_exists:
                self.log(
                    "The device with IP '{ip} need to added to the fabric site '{site}': {device_info}."
                    .format(ip=fabric_device_ip, site=fabric_name, device_info=fabric_devices_info)
                )
                fabric_devices_details.append(fabric_devices_info)
                continue

            device_roles = device_info.get("device_details").get("deviceRoles")
            is_border_device = False
            if "BORDER_NODE" in device_roles:
                is_border_device = True

            # The border settings is active on when the device has a role of the border node
            borders_settings = item.get("borders_settings")
            if is_border_device and borders_settings:
                layer2_handoff = borders_settings.get("layer2_handoff")

                # If L2 handoff is set, then the border type should atleast be Layer2
                if layer2_handoff:
                    for value in layer2_handoff:
                        internal_vlan_id = value.get("internal_vlan_id")
                        if not internal_vlan_id:
                            self.msg = (
                                "The required parameter 'internal_vlan_id' in 'l2_handoffs' is missing "
                                "for the device ip '{ip}'.".format(ip=fabric_device_ip)
                            )
                            self.status = "failed"
                            return self

                        interface_name = value.get("interface_name")
                        if not interface_name:
                            self.msg = (
                                "The required parameter 'interface_name' in 'l2_handoffs' is missing "
                                "for the device ip '{ip}'.".format(ip=fabric_device_ip)
                            )
                            self.status = "failed"
                            return self

                        l2_handoff_id = self.l2_handoff_exists(fabric_site_id,
                                                               network_device_id,
                                                               internal_vlan_id,
                                                               interface_name)
                        fabric_devices_info.get("l2_handoff_ids").append(l2_handoff_id)

                layer3_handoff_sda_transit = borders_settings.get("layer3_handoff_sda_transit")
                # If the SDA L3 Handoff is set, then the border type is atleast set to Layer3
                if layer3_handoff_sda_transit:

                    # Transit network name is mandatory
                    transit_network_name = layer3_handoff_sda_transit.get("transit_network_name")
                    if not transit_network_name:
                        self.msg = (
                            "The required parameter 'transit_network_name' in 'layer3_handoff_sda_transit' is missing."
                        )
                        self.status = "failed"
                        return self

                    sda_l3_handoff_details = self.sda_l3_handoff_exists(fabric_site_id,
                                                                        network_device_id,
                                                                        transit_network_name)
                    fabric_devices_info.update({
                        "sda_l3_handoff_details": sda_l3_handoff_details
                    })

                layer3_handoff_ip_transit = borders_settings.get("layer3_handoff_ip_transit")

                # If the IP L3 Handoff is set, then the border type is set to Layer2 and Layer3
                if layer3_handoff_ip_transit:
                    for value in layer3_handoff_ip_transit:

                        # Transit name, interface name and virtual network name are mandatory
                        transit_network_name = layer3_handoff_ip_transit.get("transit_network_name")
                        if not transit_network_name:
                            self.msg = (
                                "The required parameter 'transit_network_name' in 'layer3_handoff_ip_transit' is missing."
                            )
                            self.status = "failed"
                            return self

                        interface_name = layer3_handoff_ip_transit.get(interface_name)
                        if not interface_name:
                            self.msg = (
                                "The required parameter 'interface_name' in 'layer3_handoff_ip_transit' is missing."
                            )
                            self.status = "failed"
                            return self

                        virtual_network_name = layer3_handoff_ip_transit.get(virtual_network_name)
                        vlan_id = layer3_handoff_ip_transit.get(vlan_id)
                        if not (virtual_network_name and vlan_id):
                            self.msg = (
                                "Either the 'virtual_network_name' or 'vlan_id' is mandatory for updating and deleting the "
                                "layer3_handoff_ip_transit or both of them is mandatory for creating a layer3_handoff_ip_transit."
                            )
                            self.status = "failed"
                            return self

                        ip_l3_handoff_detail = self.ip_l3_handoff_exists(fabric_site_id, network_device_id,
                                                                         transit_network_name, virtual_network_name,
                                                                         vlan_id)
                        fabric_devices_info.get("ip_l3_handoff_details").append(ip_l3_handoff_detail)

            self.log("SDA fabric device exists for '{ip}': {exists}"
                     .format(ip=fabric_device_ip, exists=fabric_devices_info.get("exists")), "DEBUG")
            self.log("SDA fabric device details for '{ip}': {device_details}"
                     .format(ip=fabric_device_ip, device_details=fabric_devices_info.get("device_details")), "DEBUG")
            self.log("SDA fabric device ID for '{ip}': {id}"
                     .format(ip=fabric_device_ip, id=fabric_devices_info.get("id")), "DEBUG")
            self.log("L2 handoff details for '{ip}': '{l2_handoff_details}'"
                     .format(ip=fabric_device_ip,
                             l2_handoff_details=fabric_devices_info.get("l2_handoff_details")), "DEBUG")
            self.log("L3 SDA handoff details for '{ip}': '{sda_l3_handoff_details}'"
                     .format(ip=fabric_device_ip,
                             sda_l3_handoff_details=fabric_devices_info.get("sda_l3_handoff_details")), "DEBUG")
            self.log("L3 IP handoff details for '{ip}': '{ip_l3_handoff_details}'"
                     .format(ip=fabric_device_ip,
                             ip_l3_handoff_details=fabric_devices_info.get("ip_l3_handoff_details")), "DEBUG")
            fabric_devices_details.append(fabric_devices_info)

        self.log("SDA fabric devices Cisco Catalyst Center details: {current_state}"
                 .format(current_state=fabric_devices_details), "INFO")
        self.have.update({"fabric_devices": fabric_devices_details})
        self.msg = "Collecting the SDA fabric devices details from the Cisco Catalyst Center."
        self.status = "success"
        return self

    def get_have(self, config):
        """
        Get the SDA fabric devices related information from Cisco Catalyst Center.

        Parameters:
            config (dict): Playbook details containing fabric devices details.
        Returns:
            self: The current object with updated fabric devices details.
        Description:
            Check the fabric_devices. If it is not available, return with a msg by setting the
            self.status as 'failed' and return self.
            Call the 'get_have_fabric_devices' function to collect the information
            about the fabric devices in the Cisco Catalyst Center.
        """

        fabric_devices = config.get("fabric_devices")
        if not fabric_devices:
            self.msg = "The parameter 'fabric_devices' is missing under the 'config'."
            self.status = "failed"
            return self

        self.get_have_fabric_devices(fabric_devices).check_return_status()

        self.log("Current State (have): {current_state}".format(current_state=self.have), "INFO")
        self.msg = "Successfully retrieved the SDA fabric devices details from the Cisco Catalyst Center."
        self.status = "success"
        return self

    def get_device_params(self, fabric_id, network_id, device_details, config_index):
        """
        Get the SDA fabric devices detail along with the border
        settings information from playbook.
        Set the status and the msg before returning from the API
        Check the return value of the API with check_return_status()

        Parameters:
            fabric_id (str): The Id of the fabric site.
            network_id (str): The Id of the network device.
            device_details (dict): Playbook details containing fabric devices details along
            with the Border Settings, L2 Handoff, L3 SDA Handoff, L3 IP Handoff information.
            config_index (int) - Pointer to the device_config elements in the playbook.
        Returns:
            device_info (dict): The processed device details from the user playbook.
        Description:
            Get the device details from the playbook and do the basic validation and
            do the checks which is done by the GUI.
            Return the device details.
        """

        device_ip = device_details.get("device_ip")
        device_info = {
            "networkDeviceId": network_id,
            "fabricId": fabric_id,
        }

        # If the user didnot provide the mandatory information and if it can be
        # retrieved from the Cisco Catalyst Center, we will use it
        have_device_details = self.have.get("fabric_devices")[config_index].get("device_details")
        have_device_exists = self.have.get("fabric_devices")[config_index] \
                                      .get("device_details").get("exists")

        # Device IP and the Fabric name is mandatory and cannot be fetched from the Cisco Catalyst Center
        device_roles = device_details.get("device_roles")
        if not device_roles:
            if not have_device_exists:
                self.msg = (
                    "The parameter 'device_roles is mandatory under 'device_config' "
                    "for the device with IP '{ip}'.".format(ip=device_ip)
                )
                self.status = "failed"
                return self.check_return_status()

            device_roles = have_device_details.get("deviceRoles")

        else:
            device_roles_list = ["CONTROL_PLANE_NODE", "EDGE_NODE",
                                 "BORDER_NODE", "WIRELESS_CONTROLLER_NODE"]
            for item in device_roles:
                if item not in device_roles_list:
                    self.msg = (
                        "The value '{item}' in 'device_roles' for the IP '{ip}' should be in the list '{roles_list}'."
                        .format(item=item, ip=device_ip, roles_list=device_roles_list)
                    )
                    self.status = "failed"
                    return self.check_return_status()

            # The role of the device cannot be updated
            if have_device_exists and device_roles != have_device_details.get("deviceRoles"):
                self.msg = (
                    "The parameter 'device_roles' cannot be updated in the device with IP '{ip}'."
                    .format(ip=device_ip)
                )
                self.status = "failed"
                return self.check_return_status()

        device_info.update({
            "deviceRoles": device_roles
        })
        if "BORDER_NODE" not in device_roles:
            return device_info

        borders_settings = device_details.get("borders_settings")
        have_border_settings = None

        # Get the border settings details from the Cisco Catalyst Center, if available
        if not borders_settings:
            have_border_settings = have_device_details.get("borderDeviceSettings")
            if not have_border_settings:
                self.msg = (
                    "The parameter 'border_settings' is mandatory when the 'device_roles' has 'BORDER_NODE' "
                    "for the device {ip}.".format(ip=device_ip)
                )
                self.status = "failed"
                return self.check_return_status()

            device_info.update({
                "borderDeviceSettings": have_border_settings
            })
            return device_info

        else:
            border_device_settings = {}
            border_types = []
            layer3_settings = borders_settings.get("layer3_settings")
            if layer3_settings:
                border_types.append("LAYER_3")

            l2_handoff = borders_settings.get("layer2_handoff")
            if l2_handoff:
                border_types.append("LAYER_2")

            if have_border_settings:
                border_types = have_border_settings.get("borderTypes")

            if not border_types:
                self.msg = (
                    "Either L3 or L2 Handoff should be set. Please provide the 'layer3_settings' or "
                    "'layer2_handoff' for the device with IP '{ip}'".format(ip=device_ip)
                )
                self.status = "failed"
                return self.check_return_status()

            border_device_settings.update({
                "borderTypes": border_types
            })

            # Get the border settings from the Cisco Catalyst Center
            have_layer3_settings = None
            if have_border_settings:
                have_layer3_settings = have_border_settings.get("layer3Settings")

            if "LAYER_3" in border_types:
                local_autonomous_system_number = layer3_settings.get("local_autonomous_system_number")
                if not local_autonomous_system_number:
                    if have_layer3_settings:
                        have_local_autonomous_system_number = have_layer3_settings.get("localAutonomousSystemNumber")
                        local_autonomous_system_number = have_local_autonomous_system_number
                    else:
                        self.msg = (
                            "The parameter 'local_autonomous_system_number' is mandatory for the 'layer3_settings' "
                            "for the device with IP '{ip}'.".format(ip=device_ip)
                        )
                        self.status = "failed"
                        return self.check_return_status()

                is_default_exit = layer3_settings.get("layer3_settings")
                if not is_default_exit:
                    if have_layer3_settings:
                        have_is_default_exit = have_layer3_settings.get("isDefaultExit")
                        is_default_exit = have_is_default_exit
                    else:
                        is_default_exit = True

                import_external_routes = layer3_settings.get("import_external_routes")
                if not import_external_routes:
                    if have_layer3_settings:
                        have_import_external_routes = have_layer3_settings.get("importExternalRoutes")
                        import_external_routes = have_import_external_routes
                    else:
                        import_external_routes = True

                border_priority = layer3_settings.get("border_priority")
                # Default value of border priority is 10
                # we can se the border priority from 0 to 9
                if not border_priority:
                    if have_layer3_settings:
                        have_border_priority = have_layer3_settings.get("borderPriority")
                        if have_border_priority:
                            border_priority = have_border_priority
                        else:
                            border_priority = 10
                    else:
                        border_priority = 10
                else:
                    try:
                        border_priority = int(border_priority)
                        if not 1 <= border_priority <= 9:
                            self.msg = "The 'border_priority' should be from 1 to 9."
                            self.status = "failed"
                            return self.check_return_status()

                    except ValueError:
                        self.msg = "The 'border_priority' should contain only digits 0-9."
                        self.status = "failed"
                        return self.check_return_status()

                prepend_autonomous_system_count = layer3_settings.get("prepend_autonomous_system_count")
                # Default value of prepend autonomous system count is 0
                # we can se the prepend autonomous system count from 1 to 10
                if not prepend_autonomous_system_count:
                    if have_layer3_settings:
                        have_prepend_autonomous_system_count = have_layer3_settings.get("prependAutonomousSystemCount")
                        if have_prepend_autonomous_system_count:
                            prepend_autonomous_system_count = have_prepend_autonomous_system_count
                        else:
                            prepend_autonomous_system_count = 0
                    else:
                        prepend_autonomous_system_count = 0
                else:
                    try:
                        prepend_autonomous_system_count = int(prepend_autonomous_system_count)
                        if not 1 <= prepend_autonomous_system_count <= 10:
                            self.msg = "The 'prepend_autonomous_system_count' should be from 1 to 10."
                            self.status = "failed"
                            return self.check_return_status()

                    except ValueError:
                        self.msg = "The 'prepend_autonomous_system_count' should contain only digits 0-9."
                        self.status = "failed"
                        return self.check_return_status()

                border_device_settings.update({
                    "layer3Settings": {
                        "localAutonomousSystemNumber": local_autonomous_system_number,
                        "isDefaultExit": is_default_exit,
                        "importExternalRoutes": import_external_routes,
                        "borderPriority": border_priority,
                        "prependAutonomousSystemCount": prepend_autonomous_system_count,
                    }
                })

            device_info.update({
                "borderDeviceSettings" : border_device_settings
            })

        return device_info

    def get_l2_handoff_params(self, fabric_id, network_id, device_details, device_config_index):
        """
        Get the L2 Handoff of the SDA fabric devices information from playbook.
        Set the status and the msg before returning from the API
        Check the return value of the API with check_return_status()

        Parameters:
            fabric_id (str): The Id of the fabric site.
            network_id (str): The Id of the network device.
            device_details (dict): Playbook details containing fabric devices details along
            with the Border Settings, L2 Handoff, L3 SDA Handoff, L3 IP Handoff information.
            device_config_index (int): The index of the device details in the device_config.
        Returns:
            l2_handoff_info (list): The processed L2 Handoff details from the user playbook.
        Description:

        """

        l2_handoff_info = []
        layer2_handoff = device_details.get("layer2_handoff")
        if not layer2_handoff:
            return l2_handoff_info

        device_ip = device_details.get("device_ip")
        l2_handoff_index = -1
        for item in layer2_handoff:
            l2_handoff_index += 1
            l2_handoff = {
                "networkDeviceId": network_id,
                "fabricId": fabric_id,
            }
            if self.have.get("fabric_devices")[device_config_index] \
                   .get("l2_handoff_details")[l2_handoff_index]:
                continue

            interface_name = item.get("interface_name")
            if not interface_name:
                self.msg = (
                    "The 'interface_name' is mandatory under 'layer2_handoff' for "
                    "the device with IP '{ip}'".format(ip=device_ip)
                )
                self.status = "failed"
                return self.check_return_status()

            internal_vlan_id = item.get("internal_vlan_id")
            if not internal_vlan_id:
                self.msg = (
                    "The 'internal_vlan_id' is mandatory under 'layer2_handoff' for "
                    "the device with IP '{ip}'".format(ip=device_ip)
                )
                self.status = "failed"
                return self.check_return_status()

            # Internal vlan id can be from 2 to 4094
            # Except 1002, 1003, 1004, 1005, 2046, 4094
            try:
                internal_vlan_id = int(internal_vlan_id)
                reserved_vlans = [1, 1002, 1003, 1004, 1005, 2046, 4094]
                if not (1 <= internal_vlan_id <= 4094) or (internal_vlan_id not in reserved_vlans):
                    self.msg = (
                        "The 'internal_vlan_id' should be from 2 to 4094 and it should not be a "
                        "reserved VLAN '{reserved_vlan}'".format(reserved_vlan=reserved_vlans)
                    )
                    self.status = "failed"
                    return self.check_return_status()

            except ValueError:
                self.msg = "The 'internal_vlan_id' should contain only digits 0-9."
                self.status = "failed"
                return self.check_return_status()

            external_vlan_id = item.get("external_vlan_id")
            if not external_vlan_id:
                self.msg = (
                    "The 'external_vlan_id' is mandatory under 'layer2_handoff' for "
                    "the device with IP '{ip}'".format(ip=device_ip)
                )
                self.status = "failed"
                return self.check_return_status()

            # External vlan id can be from 2 to 4094
            # Except 1002, 1003, 1004, 1005, 2046, 4094
            try:
                external_vlan_id = int(external_vlan_id)
                reserved_vlans = [1, 1002, 1003, 1004, 1005, 2046, 4094]
                if not (1 <= external_vlan_id <= 4094) or (external_vlan_id not in reserved_vlans):
                    self.msg = (
                        "The 'external_vlan_id' should be from 2 to 4094 and it should not be a "
                        "reserved VLAN '{reserved_vlan}'".format(reserved_vlan=reserved_vlans)
                    )
                    self.status = "failed"
                    return self.check_return_status()

            except ValueError:
                self.msg = "The 'external_vlan_id' should contain only digits 0-9."
                self.status = "failed"
                return self.check_return_status()

            l2_handoff.update({
                "interfaceName": interface_name,
                "internalVlanId": internal_vlan_id,
                "externalVlanId": external_vlan_id,
            })

            l2_handoff_info.append(l2_handoff)

        return l2_handoff_info

    def get_sda_l3_handoff_params(self, fabric_id, network_id, device_details, device_config_index):
        """
        Get the L3 SDA Handoff of the SDA fabric devices information from playbook.
        Set the status and the msg before returning from the API
        Check the return value of the API with check_return_status()

        Parameters:
            fabric_id (str): The Id of the fabric site.
            network_id (str): The Id of the network device.
            device_details (dict): Playbook details containing fabric devices details along
            with the Border Settings, L2 Handoff, L3 SDA Handoff, L3 IP Handoff information.
            device_config_index (int): The index of the device details in the device_config.
        Returns:
            sda_l3_handoff_info (dict): The processed L3 Handoff with SDA transit details from the user playbook.
        Description:

        """

        sda_l3_handoff_info = {}
        layer3_handoff_sda_transit = device_details.get("layer3_handoff_sda_transit")
        if not layer3_handoff_sda_transit:
            return sda_l3_handoff_info

        device_ip = device_details.get("device_ip")
        sda_l3_handoff_info = {
            "networkDeviceId": network_id,
            "fabricId": fabric_id,
        }

        is_sda_l3_handoff_exists = False
        have_sda_l3_handoff = self.have.get("fabric_devices")[device_config_index] \
                                       .get("sda_l3_handoff_details")
        if have_sda_l3_handoff:
            is_sda_l3_handoff_exists = True

        transit_name = layer3_handoff_sda_transit.get("transit_network_name")
        if not transit_name:
            self.msg = (
                "The parameter 'transit_name' is mandatory under 'layer3_handoff_sda_transit'."
            )
            self.status = "failed"
            return self.check_return_status()

        transit_id = self.get_transit_id_from_name(transit_name)
        if not transit_id:
            self.msg = (
                "The SDA transit with the name '{name}' is not available in the Cisco Catalyst Center."
                .format(name=transit_name)
            )
            self.status = "failed"
            return self.check_return_status()

        connected_to_internet = layer3_handoff_sda_transit.get("connected_to_internet")
        if not connected_to_internet:
            if is_sda_l3_handoff_exists:
                connected_to_internet = have_sda_l3_handoff.get("connectedToInternet")
            else:
                connected_to_internet = False

        is_multicast_over_transit_enabled = layer3_handoff_sda_transit.get("is_multicast_over_transit_enabled")
        if not is_multicast_over_transit_enabled:
            if is_sda_l3_handoff_exists:
                is_multicast_over_transit_enabled = have_sda_l3_handoff.get("isMulticastOverTransitEnabled")
            else:
                is_multicast_over_transit_enabled = False

        affinity_id_prime = layer3_handoff_sda_transit.get("affinity_id_prime")
        if not affinity_id_prime:
            have_affinity_id_prime = have_sda_l3_handoff.get("affinityIdPrime")
            if is_sda_l3_handoff_exists and not have_affinity_id_prime:
                affinity_id_prime = have_affinity_id_prime

        else:

            # Affinity id prime value should be from 0 to 2147483647
            try:
                affinity_id_prime = int(affinity_id_prime)
                if not (0 <= affinity_id_prime <= 2147483647):
                    self.msg = (
                        "The 'affinity_id_prime' should be from 0 to 2147483647 for the "
                        "device '{device_ip}'".format(device_ip=device_ip)
                    )
                    self.status = "failed"
                    return self.check_return_status()

            except ValueError:
                self.msg = "The 'affinity_id_prime' should contain only digits 0-9."
                self.status = "failed"
                return self.check_return_status()

        affinity_id_decider = layer3_handoff_sda_transit.get("affinity_id_decider")
        if not affinity_id_decider:
            have_affinity_id_decider = have_sda_l3_handoff.get("affinityIdDecider")
            if is_sda_l3_handoff_exists and not have_affinity_id_decider:
                affinity_id_decider = have_affinity_id_decider

        else:

            # Affinity id decider value should be from 0 to 2147483647
            try:
                affinity_id_decider = int(affinity_id_decider)
                if not (0 <= affinity_id_decider <= 2147483647):
                    self.msg = (
                        "The 'affinity_id_decider' should be from 0 to 2147483647 for the "
                        "device '{device_ip}'".format(device_ip=device_ip)
                    )
                    self.status = "failed"
                    return self.check_return_status()

            except ValueError:
                self.msg = "The 'affinity_id_decider' should contain only digits 0-9."
                self.status = "failed"
                return self.check_return_status()

        if affinity_id_prime ^ affinity_id_decider:
            self.msg = (
                "Either 'affinity_id_prime' or 'affinity_id_decider' is not accepted. If you wish "
                "to add the affinity, pass both the 'affinity_id_prime' or 'affinity_id_decider' "
                "for the device with IP '{ip}".format(ip=device_ip)
            )
            self.status = "failed"
            return self.check_return_status()

        sda_l3_handoff_info.update({
            "interfaceName": transit_id,
            "affinityIdPrime": affinity_id_prime,
            "affinityIdDecider": affinity_id_decider,
            "connectedToInternet": connected_to_internet,
            "isMulticastOverTransitEnabled": is_multicast_over_transit_enabled,
        })

        return sda_l3_handoff_info

    def get_ip_l3_handoff_params(self, fabric_id, network_id, device_details, device_config_index, fabric_name):
        """
        Get the L3 IP Handoff of the SDA fabric devices information from playbook.
        Set the status and the msg before returning from the API
        Check the return value of the API with check_return_status()

        Parameters:
            fabric_id (str): The Id of the fabric site.
            network_id (str): The Id of the network device.
            device_details (dict): Playbook details containing fabric devices details along
            with the Border Settings, L2 Handoff, L3 SDA Handoff, L3 IP Handoff information.
            device_config_index (int): The index of the device details in the device_config.
            fabric_name (str): The name of the fabric site.
        Returns:
            ip_l3_handoff_info (list): The processed L3 Handoff with IP transit details from the user playbook.
        Description:

        """

        ip_l3_handoff_info = []
        layer3_handoff_ip_transit = device_details.get("layer3_handoff_ip_transit")
        if not layer3_handoff_ip_transit:
            return ip_l3_handoff_info

        device_ip = device_details.get("device_ip")
        l3_ip_handoff_index = -1
        for item in layer3_handoff_ip_transit:
            l3_ip_handoff_index += 1
            l3_ip_handoff = {
                "networkDeviceId": network_id,
                "fabricId": fabric_id,
            }
            is_ip_l3_handoff_exists = False
            have_ip_l3_handoff = self.have.get("fabric_devices")[device_config_index] \
                                          .get("ip_l3_handoff_details")[l3_ip_handoff_index]
            if have_ip_l3_handoff:
                is_ip_l3_handoff_exists = True

            transit_name = item.get("transit_network_name")
            if not transit_name:
                self.msg = (
                    "The parameter 'transit_name' is mandatory under 'layer3_handoff_sda_transit'."
                )
                self.status = "failed"
                return self.check_return_status()

            transit_id = self.get_transit_id_from_name(transit_name)
            if not transit_id:
                self.msg = (
                    "The SDA transit with the name '{name}' is not available in the Cisco Catalyst Center."
                    .format(name=transit_name)
                )
                self.status = "failed"
                return self.check_return_status()

            interface_name = item.get("interface_name")
            if not interface_name:
                self.msg = (
                    "The 'interface_name' is mandatory under 'layer3_handoff_ip_transit' for "
                    "the device with IP '{ip}'".format(ip=device_ip)
                )
                self.status = "failed"
                return self.check_return_status()

            virtual_network_name = item.get("virtual_network_name")
            if virtual_network_name:
                is_valid_virtual_network = self.check_valid_virtual_network_name(virtual_network_name)
                if not is_valid_virtual_network:
                    self.msg = (
                        "The virtual network with the name '{virtual_nw_name}' is not valid."
                        .format(virtual_nw_name=virtual_network_name)
                    )
                    self.status = "failed"
                    return self.check_return_status()

            vlan_id = item.get("vlan_id")
            if vlan_id:

                # vlan id can be from 2 to 4094
                # Except 1002, 1003, 1004, 1005, 2046, 4094
                try:
                    vlan_id = int(vlan_id)
                    reserved_vlans = [1, 1002, 1003, 1004, 1005, 2046, 4094]
                    if not (1 <= vlan_id <= 4094) or (vlan_id not in reserved_vlans):
                        self.msg = (
                            "The 'vlan_id' should be from 2 to 4094 and it should not be a "
                            "reserved VLAN '{reserved_vlan}' in 'layer3_handoff_ip_transit'."
                            .format(reserved_vlan=reserved_vlans)
                        )
                        self.status = "failed"
                        return self.check_return_status()

                except ValueError:
                    self.msg = "The 'vlan_id' should contain only digits 0-9."
                    self.status = "failed"
                    return self.check_return_status()

            if is_ip_l3_handoff_exists:
                if not (virtual_network_name and vlan_id):
                    self.msg = (
                        "The 'virtual_network_name' or 'vlan_id' is mandatory under 'layer3_handoff_ip_transit' "
                        "for updating the Layer 3 Handoff with IP transit in the device with IP '{ip}'"
                        .format(ip=device_ip)
                    )
                    self.status = "failed"
                    return self.check_return_status()
                elif virtual_network_name and (not vlan_id):
                    vlan_id = have_ip_l3_handoff.get("vlanId")
                elif vlan_id and (not virtual_network_name):
                    virtual_network_name = have_ip_l3_handoff.get("virtualNetworkName")
            else:
                self.msg = (
                    "The 'virtual_network_name' and  'vlan_id' are mandatory under 'layer3_handoff_ip_transit' for "
                    "adding the Layer 3 Handoff with IP transit in the device with IP '{ip}'"
                    .format(ip=device_ip)
                )
                self.status = "failed"
                return self.check_return_status()

            l3_ip_handoff.update({
                "transitNetworkId": transit_id,
                "interfaceName": interface_name,
                "virtualNetworkName": virtual_network_name,
                "vlanId": vlan_id,
            })
            tcp_mss_adjustment = item.get("tcp_mss_adjustment")
            if not tcp_mss_adjustment:
                if is_ip_l3_handoff_exists:
                    have_tcp_mss_adjustment = have_ip_l3_handoff.get("tcpMssAdjustment")
                    if have_tcp_mss_adjustment:
                        tcp_mss_adjustment = have_tcp_mss_adjustment
                else:
                    tcp_mss_adjustment = 0
            else:

                # TCP mss adjustment should be from 500 to 1440
                try:
                    tcp_mss_adjustment = int(tcp_mss_adjustment)
                    if not (500 <= tcp_mss_adjustment <= 1440):
                        self.msg = (
                            "The 'tcp_mss_adjustment' should be from 500 to 1440 in 'layer3_handoff_ip_transit'."
                        )
                        self.status = "failed"
                        return self.check_return_status()

                except ValueError:
                    self.msg = "The 'tcp_mss_adjustment' should contain only digits 0-9."
                    self.status = "failed"
                    return self.check_return_status()

            if tcp_mss_adjustment:
                l3_ip_handoff.update({
                    "tcpMssAdjustment": tcp_mss_adjustment,
                })

            # If the fabric device is avaiable, then fetch the local and remote IP addresses
            if is_ip_l3_handoff_exists:
                local_ip_address = have_ip_l3_handoff.get("localIpAddress")
                remote_ip_address = have_ip_l3_handoff.get("remoteIpAddress")
                local_ipv6_address = have_ip_l3_handoff.get("localIpv6Address")
                remote_ipv6_address = have_ip_l3_handoff.get("remoteIpv6Address")
                l3_ip_handoff.update({
                    "localIpAddress": local_ip_address,
                    "remoteIpAddress": remote_ip_address,
                    "localIpv6Address": local_ipv6_address,
                    "remoteIpv6Address": remote_ipv6_address,
                })
            else:

                # If external_connectivity_ip_pool_name is given local and remote address will be ignored
                # If external_connectivity_ip_pool_name is not given, then local and remote is mandatory
                external_connectivity_ip_pool_name = item.get("external_connectivity_ip_pool_name")
                if external_connectivity_ip_pool_name:

                    # Check if the reserved pool is available in the Cisco Catalyst Center or not
                    is_valid_reserved_pool = self.check_valid_reserved_pool(external_connectivity_ip_pool_name,
                                                                            fabric_name)
                    if not is_valid_reserved_pool:
                        self.msg = (
                            "The 'external_connectivity_ip_pool_name' is not a valid reserved pool for the "
                            "device with IP '{ip}'.".format(ip=device_ip)
                        )
                        self.status = "failed"
                        return self.check_return_status()

                    l3_ip_handoff.update({
                        "externalConnectivityIpPoolName": external_connectivity_ip_pool_name
                    })
                else:
                    local_ip_address = item.get("local_ip_address")
                    remote_ip_address = item.get("remote_ip_address")
                    local_ipv6_address = item.get("local_ipv6_address")
                    remote_ipv6_address = item.get("remote_ipv6_address")
                    if not (local_ip_address and remote_ip_address):
                        self.msg = (
                            "The parameters 'local_ip_address' and 'remote_ip_address' is mandatory for "
                            "creating L3 Handoff with IP Transit."
                        )
                        self.msg = "failed"
                        return self.check_return_status()

                    l3_ip_handoff.update({
                        "localIpAddress": local_ip_address,
                        "remoteIpAddress": remote_ip_address
                    })
                    if local_ipv6_address and remote_ipv6_address:
                        l3_ip_handoff.update({
                            "localIpv6Address": local_ipv6_address,
                            "remoteIpv6Address": remote_ipv6_address
                        })

            ip_l3_handoff_info.append(l3_ip_handoff)

        return ip_l3_handoff_info

    def get_want_fabric_devices(self, fabric_devices):
        """
        Get all the SDA fabric devices along with the Border settings, L2 Handoff,
        L3 SDA Handoff, L3 IP Handoff information from playbook.
        Set the status and the msg before returning from the API
        Check the return value of the API with check_return_status()

        Parameters:
            fabric_devices (dict): Playbook details containing fabric devices details along
            with the Border Settings, L2 Handoff, L3 SDA Handoff, L3 IP Handoff information.
        Returns:
            self: The current object with updated desired fabric devices information.
        Description:
            Do all the validation which is done in the GUI and format the payload
            in such a way that we can pass it to the API.
            Call the respective functions for gathering the device details,
            L2 Handoff, L3 IP Handoff, L3 SDA Handoff provided by the user.
        """

        fabric_devices_details = []
        fabric_name = fabric_devices.get("fabric_name")
        fabric_site_id = self.have.get("fabric_devices").get("fabric_site_id")
        device_config = fabric_devices.get("device_config")
        device_config_index = -1
        for item in device_config:
            device_config_index += 1
            device_ip = fabric_devices.get("device_ip")
            fabric_devices_info = {
                "device_details": None,
                "l2_handoff_details": [],
                "sda_l3_handoff_details": None,
                "ip_l3_handoff_details": [],
            }
            network_device_id = self.have.get("fabric_devices").get("network_device_id")
            fabric_devices_info.update({
                "device_details": self.get_device_params(fabric_site_id, network_device_id, item),
                "l2_handoff_details": self.get_l2_handoff_params(fabric_site_id, network_device_id, item, device_config_index),
                "sda_l3_handoff_details": self.get_sda_l3_handoff_params(fabric_site_id, network_device_id, item, device_config_index),
                "ip_l3_handoff_details": self.get_ip_l3_handoff_params(fabric_site_id, network_device_id, item,
                                                                       device_config_index, fabric_name),
            })
            self.log(
                "The fabric device with IP '{ip}' details under the site '{site}': {details}"
                .format(ip=device_ip, site=fabric_name, details=fabric_devices_info)
            )
            fabric_devices_details.append(fabric_devices_info)

        self.log("SDA fabric devices playbook details: {requested_state}"
                 .format(requested_state=fabric_devices_details), "DEBUG")
        self.want.update({"fabric_devices": fabric_devices_details})
        self.msg = "Collecting the SDA fabric transits details from the playbook."
        self.status = "success"
        return self

    def get_want(self, config):
        """
        Get the SDA fabric devices related information from playbook.

        Parameters:
            config (list of dict): Playbook details contains the details of fabric devices.
        Returns:
            self: The current object with updated fabric devices details.
        Description:

        """

        fabric_devices = config.get("fabric_devices")
        if not fabric_devices:
            self.msg = "The parameter 'fabric_devices' is missing under the 'config'."
            self.status = "failed"
            return self

        self.get_want_fabric_devices(fabric_devices).check_return_status()

        self.log("Desired State (want): {requested_state}".format(requested_state=self.want), "INFO")
        self.msg = "Successfully retrieved details from the playbook."
        self.status = "success"
        return self

    def update_l2_handoff(self, have_l2_handoff, want_l2_handoff,
                          device_ip, result_fabric_device_response,
                          result_fabric_device_msg):
        """
        Create L2 Handoff in a fabric device with fields provided in playbook.

        Parameters:
            have_l2_handoff (list): L2 Handoff details from the Cisco Catalyst Center.
            want_l2_handoff (dict): L2 Handoff details from the user playbook.
            device_ip (str): The IP of the fabric device.
            result_fabric_device_response (dict): The response status of the fabric device.
            result_fabric_device_msg (dict): The message status of the fabric device.

        Returns:
            self (object): The current object with added L2 Handoff information.
        Description:

        """

        create_l2_handoff = []
        l2_handoff_index = -1

        # The L2 Handoffs doesnot support updation
        # So find which L2 handoffs need to be created and which needs to be ignored
        for item in want_l2_handoff:
            l2_handoff_index += 1
            if not have_l2_handoff[l2_handoff_index]:
                create_l2_handoff.append(item)

        try:
            payload = {"payload": create_l2_handoff}
            task_name = "add_fabric_devices_layer2_handoffs"
            task_id = self.get_taskid_post_api_call("sda", task_name, payload)
            if not task_id:
                self.msg = (
                    "Unable to retrive the task_id for the task '{task_name}'."
                    .format(task_name=task_name)
                )
                self.set_operation_result("failed", False, self.msg, "ERROR")
                return self

            success_msg = (
                "L2 Handoff(s) '{l2_handoff}' added successfully in the device with IP '{ip}."
                .format(l2_handoff=create_l2_handoff, ip=device_ip)
            )
            self.get_task_status_from_tasks_by_id(task_id, task_name, success_msg).check_return_status()
        except Exception as msg:
            self.msg = (
                "Exception occured while creating the L2 Handoff(s) in the device '{ip}': {msg}"
                .format(ip=device_ip, msg=msg)
            )
            self.status = "failed"
            return self

        result_fabric_device_response.update({
            "l2_handoff_details": create_l2_handoff
        })
        result_fabric_device_msg.update({
            "l2_handoff_details": "L2 Handoffs added successfully."
        })

        self.msg = "Successfully added the L2 Handoffs."
        self.status = "success"
        return self

    def update_sda_l3_handoff(self, have_sda_l3_handoff, want_sda_l3_handoff,
                              device_ip, result_fabric_device_response,
                              result_fabric_device_msg):
        """
        Create SDA L3 Handoff in a fabric device with fields provided in playbook.

        Parameters:
            have_sda_l3_handoff (list): SDA L3 Handoff details from the Cisco Catalyst Center.
            want_sda_l3_handoff (dict): SDA L3 Handoff details from the user playbook.
            device_ip (str): The IP of the fabric device.
            result_fabric_device_response (dict): The response status of the fabric device.
            result_fabric_device_msg (dict): The message status of the fabric device.

        Returns:
            self (object): The current object with added SDA L3 Handoff information.
        Description:

        """

        # Check is SDA L3 Handoff exists or not
        if not have_sda_l3_handoff:
            self.log(
                "Desired SDA L3 Handoff details for the device '{ip}' (want): {requested_state}"
                .format(ip=device_ip, requested_state=want_sda_l3_handoff), "DEBUG"
            )
            try:
                payload = {"payload": [want_sda_l3_handoff]}
                task_name = "add_fabric_devices_layer3_handoffs_with_sda_transit"
                task_id = self.get_taskid_post_api_call("sda", task_name, payload)
                if not task_id:
                    self.msg = (
                        "Unable to retrive the task_id for the task '{task_name}'."
                        .format(task_name=task_name)
                    )
                    self.set_operation_result("failed", False, self.msg, "ERROR")
                    return self

                success_msg = (
                    "L3 Handoff(s) with SDA Transit '{sda_l2_handoff}' added successfully in the device with IP '{ip}."
                    .format(sda_l2_handoff=want_sda_l3_handoff, ip=device_ip)
                )
                self.get_task_status_from_tasks_by_id(task_id, task_name, success_msg).check_return_status()
            except Exception as msg:
                self.msg = (
                    "Exception occured while adding the SDA L3 Handoff for the device '{ip}': {msg}"
                    .format(ip=device_ip, msg=msg)
                )
                self.status = "failed"
                return self

            result_fabric_device_response.update({
                "sda_l3_handoff_details": want_sda_l3_handoff
            })
            result_fabric_device_msg.update({
                "sda_l3_handoff_details": "SDA L3 handoff added successfully"
            })
            self.msg = "Successfully added the L3 Handoff with SDA Transit."
            self.status = "success"
            return self

        self.log(
            "Current SDA L3 Handoff details for the device '{ip}' in Catalyst Center: {current_details}"
            .format(ip=device_ip, current_details=have_sda_l3_handoff), "DEBUG"
        )
        self.log(
            "Desired SDA L3 Handoff details for the device '{ip}' for Catalyst Center: {requested_details}"
            .format(ip=device_ip, requested_details=want_sda_l3_handoff), "DEBUG"
        )

        # SDA L3 Handoff Exists
        # Check if the SDA L3 Handoff required an update or not
        if not self.requires_update(have_sda_l3_handoff,
                                    want_sda_l3_handoff,
                                    self.fabric_l3_handoff_sda_obj_params):
            self.log(
                "SDA L3 Handoff for the device '{ip}' doesn't require an update."
                .format(ip=device_ip), "INFO"
            )
            result_fabric_device_msg.update({
                "sda_l3_handoff_details": "SDA L3 Handoff doesn't require an update."
            })
            self.msg = "L3 Handoff with SDA Transit doesnot require an update."
            self.status = "success"
            return self

        self.log("Updating SDA L3 Handoff for the device '{ip}'.".format(ip=device_ip), "DEBUG")

        # SDA L3 Handoff requires an update or not
        try:
            payload = {"payload": [want_sda_l3_handoff]}
            task_name = "update_fabric_devices_layer3_handoffs_with_sda_transit"
            task_id = self.get_taskid_post_api_call("sda", task_name, payload)
            if not task_id:
                self.msg = (
                    "Unable to retrive the task_id for the task '{task_name}'."
                    .format(task_name=task_name)
                )
                self.set_operation_result("failed", False, self.msg, "ERROR")
                return self

            success_msg = (
                "L3 Handoff(s) with SDA Transit '{sda_l3_handoff}' updated successfully in the device with IP '{ip}."
                .format(sda_l3_handoff=want_sda_l3_handoff, ip=device_ip)
            )
            self.get_task_status_from_tasks_by_id(task_id, task_name, success_msg).check_return_status()
        except Exception as msg:
            self.msg = (
                "Exception occured while updating the SDA L3 Handoff for the device '{ip}': {msg}"
                .format(ip=device_ip, msg=msg)
            )
            self.status = "failed"
            return self

        self.log(
            "Successfully updated the SDA L3 Handoff to the device '{ip}'."
            .format(ip=device_ip), "INFO"
        )
        result_fabric_device_response.update({
            "sda_l3_handoff_details": want_sda_l3_handoff
        })
        result_fabric_device_msg.update({
            "sda_l3_handoff_details": "SDA L3 Handoff updated successfully."
        })

        self.msg = "Successfully updated the L3 Handoff with SDA Transit."
        self.status = "success"
        return self

    def update_ip_l3_handoff(self, have_ip_l3_handoff, want_ip_l3_handoff,
                             device_ip, result_fabric_device_response,
                             result_fabric_device_msg):
        """
        Create IP L3 Handoff in a fabric device with fields provided in playbook.

        Parameters:
            have_ip_l3_handoff (list): IP L3 Handoff details from the Cisco Catalyst Center.
            want_ip_l3_handoff (dict): IP L3 Handoff details from the user playbook.
            device_ip (str): The IP of the fabric device.
            result_fabric_device_response (dict): The response status of the fabric device.
            result_fabric_device_msg (dict): The message status of the fabric device.

        Returns:
            self (object): The current object with added SDA L3 Handoff information.
        Description:

        """

        create_ip_l3_handoff = []
        update_ip_l3_handoff = []
        ip_l3_handoff_index = -1
        for item in want_ip_l3_handoff:
            ip_l3_handoff_index += 1

            # Check for the IP L3 Handoff existence
            if not have_ip_l3_handoff[ip_l3_handoff_index]:
                create_ip_l3_handoff.append(item)
            else:
                if self.requires_update(have_ip_l3_handoff[ip_l3_handoff_index],
                                        item,
                                        self.fabric_l3_handoff_ip_obj_params):
                    update_ip_l3_handoff.append(item)

        # If both the list are empty, then not update is required
        if not (create_ip_l3_handoff or update_ip_l3_handoff):
            self.log(
                "IP L3 Handoff for the device '{ip}' doesn't require an update."
                .format(ip=device_ip), "INFO"
            )
            result_fabric_device_msg.update({
                "ip_l3_handoff_details": "IP L3 Handoff doesn't require an update."
            })

            return self

        # L3 IP Handoffs to be created
        result_fabric_device_response.update({
            "ip_l3_handoff_details": {}
        })
        result_fabric_device_msg.update({
            "ip_l3_handoff_details": {}
        })
        if create_ip_l3_handoff:
            self.log(
                "IP L3 Handoff details to be created for the device '{ip}' (want): {requested_state}"
                .format(ip=device_ip, requested_state=create_ip_l3_handoff), "DEBUG"
            )
            try:
                payload = {"payload": create_ip_l3_handoff}
                task_name = "add_fabric_devices_layer3_handoffs_with_ip_transit"
                task_id = self.get_taskid_post_api_call("sda", task_name, payload)
                if not task_id:
                    self.msg = (
                        "Unable to retrive the task_id for the task '{task_name}'."
                        .format(task_name=task_name)
                    )
                    self.set_operation_result("failed", False, self.msg, "ERROR")
                    return self

                success_msg = (
                    "L3 Handoff(s) with IP Transit '{ip_l3_handoff}' added successfully in the device with IP '{ip}."
                    .format(ip_l3_handoff=create_ip_l3_handoff, ip=device_ip)
                )
                self.get_task_status_from_tasks_by_id(task_id, task_name, success_msg).check_return_status()
            except Exception as msg:
                self.msg = (
                    "Exception occured while adding the L3 Handoff with IP Transit to the device '{ip}': {msg}"
                    .format(ip=device_ip, msg=msg)
                )
                self.log(self.msg, "ERROR")
                self.status = "failed"
                return self

            result_fabric_device_response.get("ip_l3_handoff_details").update({
                "creation": create_ip_l3_handoff
            })
            result_fabric_device_msg.get("ip_l3_handoff_details").update({
                "creation": "IP L3 Handoffs creation is successful."
            })

        # L3 IP Handoffs to be updated
        if update_ip_l3_handoff:
            self.log(
                "Desired L3 Handoff details with IP Transit for the device '{ip}' for Catalyst Center: {requested_details}"
                .format(ip=device_ip, requested_details=update_ip_l3_handoff), "DEBUG"
            )
            try:
                payload = {"payload": update_ip_l3_handoff}
                task_name = "update_fabric_devices_layer3_handoffs_with_ip_transit"
                task_id = self.get_taskid_post_api_call("sda", task_name, payload)
                if not task_id:
                    self.msg = (
                        "Unable to retrive the task_id for the task '{task_name}'."
                        .format(task_name=task_name)
                    )
                    self.set_operation_result("failed", False, self.msg, "ERROR")
                    return self

                success_msg = (
                    "L3 Handoff(s) with IP Transit '{ip_l3_handoff}' updated successfully in the device with IP '{ip}."
                    .format(ip_l3_handoff=update_ip_l3_handoff, ip=device_ip)
                )
                self.get_task_status_from_tasks_by_id(task_id, task_name, success_msg).check_return_status()
            except Exception as msg:
                self.msg = (
                    "Exception occured while updating the L3 Handoff with IP Transit to the device '{ip}': {msg}"
                    .format(ip=device_ip, msg=msg)
                )
                self.log(self.msg, "ERROR")
                self.status = "failed"
                return self

            self.log(
                "Successfully updated the L3 Handoff with IP Transit for the device '{ip}'."
                .format(ip=device_ip), "INFO"
            )
            result_fabric_device_response.get("ip_l3_handoff_details").update({
                "updation": update_ip_l3_handoff
            })
            result_fabric_device_msg.get("ip_l3_handoff_details").update({
                "updation": "IP L3 Handoffs updation is successful."
            })

        self.msg = "L3 Handoff(s) with IP Transit operations are successful."
        self.status = "success"
        return self

    def update_fabric_devices(self, fabric_devices):
        """
        Create/Update fabric devices, Border Settings, L2 Handoffs, L3 Handoff with SDA Transit,
        L3 Handoff with IP Transit in Cisco Catalyst Center with fields provided in playbook.

        Parameters:
            fabric_devices (dict): SDA fabric devices under a fabric site playbook details.
        Returns:
            self (object): The current object with updated desired Fabric Devices information.
        Description:

        """

        fabric_name = fabric_devices.get("fabric_name")
        fabric_device_index = -1
        device_config = fabric_devices.get("device_config")
        self.result.get("response").append({"response": {}, "msg": {}})
        self.result.get("response")[0].get("response").update({fabric_name: {}})
        self.result.get("response")[0].get("msg").update({fabric_name: {}})
        for item in device_config:
            fabric_device_index += 1
            device_ip = item.get("device_ip")
            self.result.get("response")[0].get("response").get(fabric_name).update({
                device_ip: {
                    "device_details": None,
                    "l2_handoff": [],
                    "l3_sda_handoff": None,
                    "l3_ip_handoff": []
                }
            })
            self.result.get("response")[0].get("msg").get(fabric_name).update({
                device_ip: {}
            })
            result_fabric_device_response = self.result.get("response")[0].get("response") \
                                                       .get(fabric_name).get(device_ip)
            result_fabric_device_msg = self.result.get("response")[0].get("msg") \
                                                  .get(fabric_name).get(device_ip)
            have_fabric_device = self.have.get("fabric_devices")[fabric_device_index]
            want_fabric_device = self.want.get("fabric_devices")[fabric_device_index]
            have_device_details = have_fabric_device.get("device_details")
            want_device_details = want_fabric_device.get("device_details")

            # Check fabric device exists, if not add it
            if not have_fabric_device:
                self.log("Desired fabric device '{ip}' details (want): {requested_state}"
                         .format(ip=device_ip, requested_state=want_device_details), "DEBUG")
                try:
                    payload = {"payload": [want_device_details]}
                    task_name = "add_fabric_devices"
                    task_id = self.get_taskid_post_api_call("sda", task_name, payload)
                    if not task_id:
                        self.msg = (
                            "Unable to retrive the task_id for the task '{task_name}'."
                            .format(task_name=task_name)
                        )
                        self.set_operation_result("failed", False, self.msg, "ERROR")
                        return self

                    success_msg = (
                        "Successfully added the fabric device with details '{device_details}'."
                        .format(device_details=want_device_details)
                    )
                    self.get_task_status_from_tasks_by_id(task_id, task_name, success_msg).check_return_status()
                except Exception as msg:
                    self.msg = (
                        "Exception occured while adding the device '{ip}' to the fabric site '{site}: {msg}"
                        .format(ip=device_ip, site=fabric_name, msg=msg)
                    )
                    self.status = "failed"
                    return self

                self.log(
                    "Successfully added the device with IP '{ip}' to the fabric site '{fabric_site}'."
                    .format(fabric_site=fabric_name, ip=device_ip), "INFO"
                )
                result_fabric_device_response.update({
                    "device_details": want_device_details
                })
                result_fabric_device_msg.update({
                    "device_details": "SDA fabric device details added successfully."
                })
            else:
                self.log(
                    "Current SDA fabric device '{ip}' details in Catalyst Center: {current_details}"
                    .format(ip=device_ip, current_details=have_device_details), "DEBUG"
                )
                self.log(
                    "Desired SDA fabric transit '{ip}' details for Catalyst Center: {requested_details}"
                    .format(ip=device_ip, requested_details=want_device_details), "DEBUG"
                )

                # Check if the update is required or not
                if not self.requires_update(have_device_details,
                                            want_device_details,
                                            self.fabric_devices_obj_params):
                    self.log(
                        "SDA fabric device '{ip}' device doesn't require an update."
                        .format(ip=device_ip), "INFO"
                    )
                    result_fabric_device_msg.update({
                        "device_details": "SDA fabric device details doesn't require an update."
                    })
                else:
                    self.log("Updating SDA fabric device '{ip}'.".format(ip=device_ip), "DEBUG")

                    # Device Details Exists
                    self.log(
                        "Current SDA fabric device '{ip}' details in Catalyst Center: {current_state}"
                        .format(ip=device_ip, current_state=have_device_details), "DEBUG"
                    )
                    self.log(
                        "Desired SDA fabric device '{ip}' details: {requested_state}"
                        .format(ip=device_ip, requested_state=want_device_details), "DEBUG"
                    )
                    want_device_details.update({"id": self.have.get("fabric_devices")[fabric_device_index].get("id")})
                    try:
                        payload = {"payload": [want_device_details]}
                        task_name = "update_fabric_devices"
                        task_id = self.get_taskid_post_api_call("sda", task_name, payload)
                        if not task_id:
                            self.msg = (
                                "Unable to retrive the task_id for the task '{task_name}'."
                                .format(task_name=task_name)
                            )
                            self.set_operation_result("failed", False, self.msg, "ERROR")
                            return self

                        success_msg = (
                            "Successfully updated the fabric device with details '{device_details}'."
                            .format(device_details=want_device_details)
                        )
                        self.get_task_status_from_tasks_by_id(task_id, task_name, success_msg).check_return_status()
                    except Exception as msg:
                        self.msg = (
                            "Exception occured while updating the fabric device with IP '{ip}': {msg}"
                            .format(ip=device_ip, msg=msg)
                        )
                        self.log(self.msg, "ERROR")
                        self.status = "failed"
                        return self

                    self.log(
                        "Successfully updated the device with IP '{ip}' to the fabric site '{fabric_site}'."
                        .format(fabric_site=fabric_name, ip=device_ip), "INFO"
                    )
                    result_fabric_device_response.update({
                        "device_details": want_device_details
                    })
                    result_fabric_device_msg.update({
                        "device_details": "SDA fabric device details updated successfully."
                    })

            have_l2_handoff = have_fabric_device.get("l2_handoff_details")
            want_l2_handoff = want_fabric_device.get("l2_handoff_details")
            if want_l2_handoff:
                self.update_l2_handoff(have_l2_handoff, want_l2_handoff, device_ip,
                                       result_fabric_device_response,
                                       result_fabric_device_msg)

            have_sda_l3_handoff = have_fabric_device.get("sda_l3_handoff_details")
            want_sda_l3_handoff = want_fabric_device.get("sda_l3_handoff_details")
            if want_sda_l3_handoff:
                self.update_sda_l3_handoff(have_sda_l3_handoff, want_sda_l3_handoff, device_ip,
                                           result_fabric_device_response,
                                           result_fabric_device_msg)

            have_ip_l3_handoff = have_fabric_device.get("ip_l3_handoff_details")
            want_ip_l3_handoff = want_fabric_device.get("ip_l3_handoff_details")
            if want_ip_l3_handoff:
                self.update_ip_l3_handoff(have_ip_l3_handoff, want_ip_l3_handoff, device_ip,
                                          result_fabric_device_response,
                                          result_fabric_device_msg)

        self.log("Updated the SDA fabric transits successfully", "INFO")
        self.msg = "The operations on fabric device is successful."
        self.status = "success"
        return self

    def get_diff_merged(self, config):
        """
        Add or Update the SDA devices transits, Border Settings, L2 Handoff, L3 SDA Handoff,
        L3 IP Handoff in Cisco Catalyst Center based on the playbook details.

        Parameters:
            config (list of dict): Playbook details containing SDA fabric devices information.
        Returns:
            self (object): The current object with updated desired Fabric Devices information.
        Description:
            If the 'fabric_devices' is available in the playbook, call the function 'update_fabric_devices'.
            Else return self.
        """

        fabric_devices = config.get("fabric_devices")
        if fabric_devices is not None:
            self.update_fabric_devices(fabric_devices)

        return self

    def delete_l2_handoff(self, have_l2_handoff, device_ip,
                          result_fabric_device_response,
                          result_fabric_device_msg):
        """
        Delete L2 Handoffs in Cisco Catalyst Center with fields provided in playbook.

        Parameters:
            have_l2_handoff (list): L2 Handoff details from the Cisco Catalyst Center.
            device_ip (str): The IP of the fabric device.
            result_fabric_device_response (dict): The response status of the fabric device.
            result_fabric_device_msg (dict): The message status of the fabric device.
        Returns:
            self (object): The current object with deleted L2 Handoffs information.
        Description:

        """

        result_fabric_device_response.update({
            "l2_handoff_details": {}
        })
        delete_l2_handoff = []
        non_existing_l2_handoff = []

        # Check if the L2 Handoff exists or not
        for item in have_l2_handoff:
            if not item:
                non_existing_l2_handoff.append(item)
            else:
                delete_l2_handoff.append(item)

        for item in delete_l2_handoff:
            id = item.get("id")
            try:
                payload = {"id": id}
                task_name = "delete_fabric_device_layer2_handoff_by_id"
                task_id = self.get_taskid_post_api_call("sda", task_name, payload)
                if not task_id:
                    self.msg = (
                        "Unable to retrive the task_id for the task '{task_name}'."
                        .format(task_name=task_name)
                    )
                    self.set_operation_result("failed", False, self.msg, "ERROR")
                    return self

                success_msg = (
                    "Successfully deleted the fabric device L2 Handoff with id '{id}'."
                    .format(id=id)
                )
                self.get_task_status_from_tasks_by_id(task_id, task_name, success_msg).check_return_status()
            except Exception as msg:
                self.msg = (
                    "Exception occured while deleting the L2 Handoff in the fabric device with IP '{ip}': {msg}"
                    .format(ip=device_ip, msg=msg)
                )
                self.log(self.msg, "ERROR")
                self.status = "failed"
                return self

        result_fabric_device_response.get("l2_handoff_details").update({
            "Deleted L2 Handoff": delete_l2_handoff,
            "Non existing L2 Handoff": non_existing_l2_handoff
        })
        if delete_l2_handoff:
            result_fabric_device_msg.update({
                "l2_handoff_details": "L2 Handoffs deleted successfully."
            })
        else:
            result_fabric_device_msg.update({
                "l2_handoff_details": "L2 Handoffs are not found in the Cisco Catalyst Center."
            })

        self.msg = "Successfully deleted the L2 Handoffs."
        self.status = "success"
        return self

    def delete_sda_l3_handoff(self, have_sda_l3_handoff, device_ip,
                              result_fabric_device_response,
                              result_fabric_device_msg):
        """
        Delete L3 Handoff with SDA Transit in Cisco Catalyst Center with fields provided in playbook.

        Parameters:
            have_l2_handoff (list): SDA L3 Handoff details from the Cisco Catalyst Center.
            device_ip (str): The IP of the fabric device.
            result_fabric_device_response (dict): The response status of the fabric device.
            result_fabric_device_msg (dict): The message status of the fabric device.
        Returns:
            self (object): The current object with deleted SDA L3 Handoffs information.
        Description:

        """

        if not have_sda_l3_handoff:

            # SDA L3 Handoff doesnot exist
            result_fabric_device_msg.update({
                "sda_l3_handoff_details": "SDA L3 Handoff is not found in the Cisco Catalyst Center."
            })
        else:

            # SDA L3 Handoff does exist
            fabric_id = have_sda_l3_handoff.get("fabricId")
            network_device_id = have_sda_l3_handoff.get("networkDeviceId")
            try:
                payload = {
                    "fabric_id": fabric_id,
                    "network_device_id": network_device_id,
                }
                task_name = "delete_fabric_device_layer3_handoffs_with_sda_transit"
                task_id = self.get_taskid_post_api_call("sda", task_name, payload)
                if not task_id:
                    self.msg = (
                        "Unable to retrive the task_id for the task '{task_name}'."
                        .format(task_name=task_name)
                    )
                    self.set_operation_result("failed", False, self.msg, "ERROR")
                    return self

                success_msg = (
                    "Successfully deleted the fabric device SDA Transit L3 Handoff with id '{id}'."
                    .format(id=id)
                )
                self.get_task_status_from_tasks_by_id(task_id, task_name, success_msg).check_return_status()
            except Exception as msg:
                self.msg = (
                    "Exception occured while deleting the SDA L3 Handoff in the fabric device with IP '{ip}': {msg}"
                    .format(ip=device_ip, msg=msg)
                )
                self.log(self.msg, "ERROR")
                self.status = "failed"
                return self

            result_fabric_device_response.update({
                "sda_l3_handoff_details": have_sda_l3_handoff
            })
            result_fabric_device_msg.update({
                "sda_l3_handoff_details": "SDA L3 Handoff is deleted successfully."
            })

        self.msg = "Successfully deleted the SDA L3 Handoffs."
        self.status = "success"
        return self

    def delete_ip_l3_handoff(self, have_ip_l3_handoff, device_ip,
                             result_fabric_device_response,
                             result_fabric_device_msg):
        """
        Delete L3 Handoff with IP Transit in Cisco Catalyst Center with fields provided in playbook.

        Parameters:
            have_ip_l3_handoff (list): IP L3 Handoff details from the Cisco Catalyst Center.
            device_ip (str): The IP of the fabric device.
            result_fabric_device_response (dict): The response status of the fabric device.
            result_fabric_device_msg (dict): The message status of the fabric device.
        Returns:
            self (object): The current object with deleted IP L3 Handoffs information.
        Description:

        """

        result_fabric_device_response.update({
            "ip_l3_handoff_details": {}
        })
        delete_ip_l3_handoff = []
        non_existing_ip_l3_handoff = []

        # Check which IP L3 Handoff exists and which doesnot
        for item in have_ip_l3_handoff:
            if not item:
                non_existing_ip_l3_handoff.append(item)
            else:
                delete_ip_l3_handoff.append(item)

        for item in delete_ip_l3_handoff:
            id = item.get("id")
            try:
                payload = {"id": id}
                task_name = "delete_fabric_device_layer3_handoff_with_ip_transit_by_id"
                task_id = self.get_taskid_post_api_call("sda", task_name, payload)
                if not task_id:
                    self.msg = (
                        "Unable to retrive the task_id for the task '{task_name}'."
                        .format(task_name=task_name)
                    )
                    self.set_operation_result("failed", False, self.msg, "ERROR")
                    return self

                success_msg = (
                    "Successfully deleted the fabric device IP Transit L3 Handoff with id '{id}'."
                    .format(id=id)
                )
                self.get_task_status_from_tasks_by_id(task_id, task_name, success_msg).check_return_status()
            except Exception as msg:
                self.msg = (
                    "Exception occured while deleting the IP L3 Handoff in the fabric device with IP '{ip}': {msg}"
                    .format(ip=device_ip, msg=msg)
                )
                self.log(self.msg, "ERROR")
                self.status = "failed"
                return self

        result_fabric_device_response.get("ip_l3_handoff_details").update({
            "Deleted L2 Handoff": delete_ip_l3_handoff,
            "Non existing L2 Handoff": non_existing_ip_l3_handoff
        })
        if delete_ip_l3_handoff:
            result_fabric_device_msg.update({
                "ip_l3_handoff_details": "IP L3 Handoffs deleted successfully."
            })
        else:
            result_fabric_device_msg.update({
                "ip_l3_handoff_details": "IP L3 Handoffs are not found in the Cisco Catalyst Center."
            })

        self.msg = "Successfully deleted the IP L3 Handoffs."
        self.status = "success"
        return self

    def delete_fabric_devices(self, fabric_devices):
        """
        Delete fabric devices, Border Settings, L2 Handoffs, L3 Handoff with SDA Transit,
        L3 Handoff with IP Transit in Cisco Catalyst Center with fields provided in playbook.

        Parameters:
            fabric_devices (dict): SDA fabric devices under a fabric site playbook details.
        Returns:
            self (object): The current object with updated desired Fabric Devices information.
        Description:

        """

        fabric_name = fabric_devices.get("fabric_name")
        fabric_device_index = -1
        device_config = fabric_devices.get("device_config")
        self.result.get("response").append({"response": {}, "msg": {}})
        self.result.get("response")[0].get("response").update({fabric_name: {}})
        self.result.get("response")[0].get("msg").update({fabric_name: {}})
        for item in device_config:
            fabric_device_index += 1
            device_ip = item.get("device_ip")
            self.result.get("response")[0].get("response").get(fabric_name).update({
                device_ip: {
                    "device_details": None,
                    "l2_handoff": [],
                    "l3_sda_handoff": None,
                    "l3_ip_handoff": []
                }
            })
            self.result.get("response")[0].get("msg").get(fabric_name).update({
                device_ip: {}
            })
            result_fabric_device_response = self.result.get("response")[0].get("response") \
                                                       .get(fabric_name).get(device_ip)
            result_fabric_device_msg = self.result.get("response")[0].get("msg") \
                                                  .get(fabric_name).get(device_ip)
            have_fabric_device = self.have.get("fabric_devices")[fabric_device_index]
            want_fabric_device = self.want.get("fabric_devices")[fabric_device_index]
            have_l2_handoff = have_fabric_device.get("l2_handoff_details")
            if item.get("l2_handoff_details"):
                self.delete_l2_handoff(have_l2_handoff, device_ip,
                                       result_fabric_device_response,
                                       result_fabric_device_msg).check_return_status()

            have_sda_l3_handoff = have_fabric_device.get("sda_l3_handoff_details")
            if item.get("sda_l3_handoff_details"):
                self.delete_sda_l3_handoff(have_sda_l3_handoff, device_ip,
                                           result_fabric_device_response,
                                           result_fabric_device_msg).check_return_status()

            have_ip_l3_handoff = have_fabric_device.get("ip_l3_handoff_details")
            if item.get("ip_l3_handoff_details"):
                self.delete_ip_l3_handoff(have_ip_l3_handoff, device_ip,
                                          result_fabric_device_response,
                                          result_fabric_device_msg).check_return_status()
            delete_fabric_device = have_fabric_device.get("delete_fabric_device")

            # If the delete_fabric_device is set to True
            # We need to delete the device as well along with the settings
            if delete_fabric_device:
                id = have_fabric_device.get("id")
                try:
                    payload = {"id": id}
                    task_name = "delete_fabric_device_by_id"
                    task_id = self.get_taskid_post_api_call("sda", task_name, payload)
                    if not task_id:
                        self.msg = (
                            "Unable to retrive the task_id for the task '{task_name}'."
                            .format(task_name=task_name)
                        )
                        self.set_operation_result("failed", False, self.msg, "ERROR")
                        return self

                    success_msg = (
                        "Successfully deleted the SDA fabric device with id '{id}'."
                        .format(id=id)
                    )
                    self.get_task_status_from_tasks_by_id(task_id, task_name, success_msg).check_return_status()
                except Exception as msg:
                    self.msg = (
                        "Exception occured while deleting the fabric device with IP '{ip}': {msg}"
                        .format(ip=device_ip, msg=msg)
                    )
                    self.log(self.msg, "ERROR")
                    self.status = "failed"
                    return self

        self.msg = "The deletion of devices L2 Handoff, L3 Handoff with IP and SDA transit is successful."
        self.status = "failed"
        return self

    def get_diff_deleted(self, config):
        """
        Delete the SDA devices transits, Border Settings, L2 Handoff, L3 SDA Handoff,
        L3 IP Handoff in Cisco Catalyst Center based on the playbook details.

        Parameters:
            config (list of dict): Playbook details containing SDA fabric devices information.
        Returns:
            self (object): The current object with updated desired Fabric Devices information.
        Description:
            If the 'fabric_devices' is available in the playbook, call the function 'delete_fabric_devices'.
            Else return self.
        """

        fabric_devices = config.get("fabric_devices")
        if fabric_devices is not None:
            self.delete_fabric_devices(fabric_devices)

        return self

    def verify_ip_l3_handoff(self, device_ip, have_l3_ip, want_l3_ip):
        """
        Validating the Cisco Catalyst Center configuration with the playbook details
        when state is merged (Create/Update).

        Parameters:
            device_ip (str): The IP of the fabric device.
            have_l3_ip (dict): L3 handoff with IP transit details in the Cisco Catalyst Center.
            want_l3_ip (dict): L3 handoff with IP transit details provided in the playbook.
        Returns:
            self (object): The current object with updated verification information of L3 IP Handoff.
        Description:

        """

        ip_l3_handoff_index = -1
        for item in want_l3_ip:
            ip_l3_handoff_index += 1
            if self.requires_update(have_l3_ip[ip_l3_handoff_index],
                                    item, self.fabric_l3_handoff_ip_obj_params):
                self.msg = (
                    "The L3 Handoff for IP transit config for the device '{ip}' is still not "
                    "applied to the Cisco Catalyst Center.".format(ip=device_ip)
                )
                self.status = "failed"
                return self

        self.msg = "Successfully validated the L3 Handoff with IP Transit."
        self.status = "success"
        return self

    def verify_l2_handoff(self, device_ip, have_l2, want_l2):
        """
        Validating the Cisco Catalyst Center configuration with the playbook details
        when state is merged (Create/Update).

        Parameters:
            device_ip (str): The IP of the fabric device.
            have_l2 (dict): L2 handoff details in the Cisco Catalyst Center.
            want_l2 (dict): L2 handoff details provided in the playbook.
        Returns:
            self (object): The current object with updated verification information of L2 Handoff.
        Description:

        """

        l2_handoff_index = -1
        for item in want_l2:
            l2_handoff_index += 1
            if not have_l2[l2_handoff_index]:
                self.msg = (
                    "The L2 Handoff for config '{config}' for the device '{ip}' is still not "
                    "applied to the Cisco Catalyst Center.".format(config=item, ip=device_ip)
                )
                self.status = "failed"
                return self

        self.msg = "Successfully validated the L2 Handoff."
        self.status = "success"
        return self

    def verify_sda_l3_handoff(self, device_ip, have_l3_sda, want_l3_sda):
        """
        Validating the Cisco Catalyst Center configuration with the playbook details
        when state is merged (Create/Update).

        Parameters:
            device_ip (str): The IP of the fabric device.
            have_l3_sda (dict): L3 handoff with SDA transit details in the Cisco Catalyst Center.
            want_l3_sda (dict): L3 handoff with SDA transit details provided in the playbook.
        Returns:
            self (object): The current object with updated verification information of L3 SDA Handoff.
        Description:

        """

        if self.requires_update(have_l3_sda, want_l3_sda, self.fabric_l3_handoff_ip_obj_params):
            self.msg = (
                "The L3 Handoff for SDA transit for the device '{ip}' is still not "
                "applied to the Cisco Catalyst Center.".format(ip=device_ip)
            )
            self.status = "failed"
            return self

        self.msg = "Successfully validated the L3 Handoff with SDA Transit."
        self.status = "success"
        return self

    def verify_layer3_settings(self, device_ip, have_device_details, want_device_details):
        """
        Validating the Cisco Catalyst Center configuration with the playbook details
        when state is merged (Create/Update).

        Parameters:
            device_ip (str): The IP of the fabric device.
            have_device_details (dict): SDA fabric device details in the Cisco Catalyst Center.
            want_device_details (dict): SDA fabric device details provided in the playbook.
        Returns:
            self (object): The current object with updated verification information of SDA fabric devices.
        Description:

        """

        if self.requires_update(have_device_details, want_device_details, self.fabric_devices_obj_params):
            self.msg = (
                "The border setting for SDA devce with IP '{ip}' is still not "
                "applied to the Cisco Catalyst Center.".format(ip=device_ip)
            )
            self.status = "failed"
            return self

        self.msg = "Successfully validated SDA fabric device details."
        self.status = "success"
        return self

    def verify_diff_merged(self, config):
        """
        Validating the Cisco Catalyst Center configuration with the playbook details
        when state is merged (Create/Update).

        Parameters:
            config (dict): Playbook details containing fabric devices configuration.
        Returns:
            self (object): The current object with updated desired Fabric Devices information.
        Description:

        """

        self.get_have(config)
        self.log("Current State (have): {current_state}".format(current_state=self.have), "INFO")
        self.log("Desired State (want): {requested_state}".format(requested_state=self.want), "INFO")
        fabric_devices = config.get("fabric_devices")
        if fabric_devices is not None:
            fabric_name = fabric_devices.get("fabric_name")
            device_config = fabric_devices.get("device_config")
            fabric_device_index = -1
            for item in device_config:
                fabric_device_index += 1
                device_ip = item.get("device_ip")
                have_details = self.have.get("fabric_devices")[fabric_device_index]
                want_details = self.want.get("fabric_devices")[fabric_device_index]

                # Verifying whether the IP L3 Handoff is applied to the Cisco Catalyst Center or not
                if item.get("layer3_handoff_ip_transit"):
                    have_l3_ip = have_details.get("ip_l3_handoff_details")
                    want_l3_ip = want_details.get("ip_l3_handoff_details")
                    self.verify_ip_l3_handoff(device_ip, have_l3_ip, want_l3_ip).check_return_status()
                self.log(
                    "Successfully validated the L3 Handoffs for IP Transit in the device '{ip}'."
                    .format(ip=device_ip), "INFO"
                )

                # Verifying whether the SDA L3 Handoff is applied to the Cisco Catalyst Center or not
                if item.get("layer3_handoff_sda_transit"):
                    have_l3_sda = have_details.get("sda_l3_handoff_details")
                    want_l3_sda = want_details.get("sda_l3_handoff_details")
                    self.verify_sda_l3_handoff(device_ip, have_l3_sda, want_l3_sda).check_return_status()

                self.log(
                    "Successfully validated the L3 Handoffs for SDA Transit in the device '{ip}'."
                    .format(ip=device_ip), "INFO"
                )

                # Verifying whether the L2 Handoff is applied to the Cisco Catalyst Center or not
                if item.get("layer2_handoff"):
                    have_l2 = have_details.get("sda_l3_handoff_details")
                    want_l2 = want_details.get("sda_l3_handoff_details")
                    self.verify_l2_handoff(device_ip, have_l2, want_l2).check_return_status()

                self.log(
                    "Successfully validated the L2 Handoffs for in the device '{ip}'."
                    .format(ip=device_ip), "INFO"
                )

                if item.get("layer3_settings"):
                    have_device_details = have_details.get("device_details")
                    want_device_details = want_details.get("device_details")
                    self.verify_layer3_settings(device_ip, have_device_details,
                                                want_device_details).check_return_status()

                self.log(
                    "Successfully validated the border settings for in the device '{ip}'."
                    .format(ip=device_ip), "INFO"
                )
                self.result.get("response")[0].get("msg").get(fabric_name) \
                           .get(device_ip).update({"Validation": "Success"})

        self.msg = "Successfully validated the SDA fabric devices(s)."
        self.status = "success"
        return self

    def verify_diff_deleted(self, config):
        """
        Validating the Cisco Catalyst Center configuration with the playbook details
        when state is deleted (delete).

        Parameters:
            config (dict): Playbook details containing fabric devices configuration.
        Returns:
            self (object): The current object with updated desired Fabric Devices information.
        Description:

        """

        self.get_have(config)
        self.log("Current State (have): {current_state}".format(current_state=self.have), "INFO")
        self.log("Desired State (want): {requested_state}".format(requested_state=self.want), "INFO")
        fabric_devices = config.get("fabric_devices")
        if fabric_devices is not None:
            fabric_device_index = -1
            fabric_name = fabric_devices.get("fabric_name")
            device_config = fabric_devices.get("device_config")
            for item in device_config:
                device_ip = item.get("device_ip")
                fabric_device_details = self.have.get("fabric_devices")[fabric_device_index]
                if item.get("layer3_handoff_ip_transit"):

                    # Verifying the absence of IP L3 Handoff
                    if fabric_device_details.get("ip_l3_handoff_details"):
                        self.msg = (
                            "The L3 Handoff for IP transit for the device '{ip}' is still present in "
                            "the Cisco Catalyst Center.".format(ip=device_ip)
                        )
                        self.status = "failed"
                        return self

                    self.log(
                        "Successfully validated absence of L3 Handoffs for IP Transit in the device '{ip}'."
                        .format(ip=device_ip), "INFO"
                    )

                if item.get("layer3_handoff_sda_transit"):

                    # Verifying the absence of SDA L3 Handoff
                    if fabric_device_details.get("sda_l3_handoff_details"):
                        self.msg = (
                            "The L3 Handoff for SDA transit for the device '{ip}' is still present in "
                            "the Cisco Catalyst Center.".format(ip=device_ip)
                        )
                        self.status = "failed"
                        return self

                    self.log(
                        "Successfully validated absence of L3 Handoffs for SDA Transit in the device '{ip}'."
                        .format(ip=device_ip), "INFO"
                    )

                if item.get("layer2_handoff"):

                    # Verifying the absence of L2 Handoff
                    if fabric_device_details.get("l2_handoff_details"):
                        self.msg = (
                            "The L2 Handoff for the device '{ip}' is still present in "
                            "the Cisco Catalyst Center.".format(ip=device_ip)
                        )
                        self.status = "failed"
                        return self

                    self.log(
                        "Successfully validated absence of L2 Handoffs in the device '{ip}'."
                        .format(ip=device_ip), "INFO"
                    )

                self.result.get("response")[0].get("msg").get(fabric_name) \
                           .get(device_ip).update({"Validation": "Success"})

        self.msg = "Successfully validated the absence of SDA fabric device(s)."
        self.status = "success"
        return self

    def reset_values(self):
        """
        Reset all neccessary attributes to default values

        Parameters:
            self (object): The current object details.
        Returns:
            None
        """

        self.have.clear()
        self.want.clear()
        return


def main():
    """main entry point for module execution"""

    # Define the specification for module arguments
    element_spec = {
        "dnac_host": {"type": 'str', "required": True},
        "dnac_port": {"type": 'str', "default": '443'},
        "dnac_username": {"type": 'str', "default": 'admin', "aliases": ['user']},
        "dnac_password": {"type": 'str', "no_log": True},
        "dnac_verify": {"type": 'bool', "default": 'True'},
        "dnac_version": {"type": 'str', "default": '2.2.3.3'},
        "dnac_debug": {"type": 'bool', "default": False},
        "dnac_log": {"type": 'bool', "default": False},
        "dnac_log_level": {"type": 'str', "default": 'WARNING'},
        "dnac_log_file_path": {"type": 'str', "default": 'dnac.log'},
        "dnac_log_append": {"type": 'bool', "default": True},
        "config_verify": {"type": 'bool', "default": False},
        "dnac_api_task_timeout": {"type": 'int', "default": 1200},
        "dnac_task_poll_interval": {"type": 'int', "default": 2},
        "config": {"type": 'list', "required": True, "elements": 'dict'},
        "state": {"default": 'merged', "choices": ['merged', 'deleted']},
        "validate_response_schema": {"type": 'bool', "default": True},
    }

    # Create an AnsibleModule object with argument specifications
    module = AnsibleModule(argument_spec=element_spec, supports_check_mode=False)
    ccc_sda_transit = FabricDevices(module)
    state = ccc_sda_transit.params.get("state")
    config_verify = ccc_sda_transit.params.get("config_verify")
    if state not in ccc_sda_transit.supported_states:
        ccc_sda_transit.status = "invalid"
        ccc_sda_transit.msg = "State '{state}' is invalid".format(state=state)
        ccc_sda_transit.check_return_status()

    ccc_sda_transit.validate_input().check_return_status()

    for config in ccc_sda_transit.config:
        ccc_sda_transit.reset_values()
        ccc_sda_transit.get_have(config).check_return_status()
        if state != "deleted":
            ccc_sda_transit.get_want(config).check_return_status()
        ccc_sda_transit.get_diff_state_apply[state](config).check_return_status()
        if config_verify:
            ccc_sda_transit.verify_diff_state_apply[state](config).check_return_status()

    module.exit_json(**ccc_sda_transit.result)


if __name__ == "__main__":
    main()
