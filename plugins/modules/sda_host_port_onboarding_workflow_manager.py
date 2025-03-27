#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright (c) 2024, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)
"""Ansible module to manage SD-Access Host Onboarding operations in Cisco Catalyst Center."""
from __future__ import absolute_import, division, print_function
__metaclass__ = type
__author__ = ("Rugvedi Kapse, Madhan Sankaranarayanan")
DOCUMENTATION = r"""
---
module: sda_host_port_onboarding_workflow_manager
short_description: Manage host port onboarding in SD-Access Fabric in Cisco Catalyst
  Center.
description:
  - Manage host onboarding operations, including the addition, update, and deletion
    of port assignments, port channels, or wireless SSID mappings to VLANs within
    the SD-Access Fabric.
  - API to create port assignment(s) for Network Devices in SD-Access Fabric roles
    in Cisco Catalyst Center.
  - API to Update port assignment(s) for Network Devices in SD-Access Fabric roles
    in Cisco Catalyst Center.
  - API to delete port assignment(s) for Network Devices in SD-Access Fabric roles
    in Cisco Catalyst Center.
  - API to create port channel(s) for Network Devices in SD-Access Fabric roles in
    Cisco Catalyst Center.
  - API to update port channel(s) for Network Devices in SD-Access Fabric roles in
    Cisco Catalyst Center.
  - API to delete port channel(s) for Network Devices in SD-Access Fabric roles in
    Cisco Catalyst Center.
  - API to add SSID mapping(s) to VLAN(s) in SD-Access Fabric in Catalyst Center.
  - API to update SSID mapping(s) to VLAN(s) in SD-Access Fabric in Catalyst Center.
  - API to remove SSID mapping(s) to VLAN(s) in SD-Access Fabric in Catalyst Center.
version_added: '6.17.0'
extends_documentation_fragment:
  - cisco.dnac.workflow_manager_params
author: Rugvedi Kapse (@rukapse) Madhan Sankaranarayanan (@madhansansel)
options:
  config_verify:
    description: Set to True to verify the Cisco Catalyst Center configuration after
      applying the playbook configuration.
    type: bool
    default: false
  state:
    description: The desired state of Cisco Catalyst Center after the module execution.
    type: str
    choices: [merged, deleted]
    default: merged
  config:
    description:
      - A list containing detailed configurations for Adding/Updating/Deleting Port
        assignment(s) or Port channel(s) for Network Devices in SDA Fabric roles or
        Adding/Updating/Deleting Wireless SSID(s) mapped to a VLAN in SDA Fabric in
        Cisco Catalyst Center.
    type: list
    elements: dict
    required: true
    suboptions:
      ip_address:
        description:
          - IP address of the target device in the SD-Access Fabric on which access
            device ports need to be configured.
          - Either "hostname" or "ip_address" of the network device, along with "fabric_site_name_hierarchy,"
            is required for performing port assignment or port channel operations.
          - It is not required to provide "ip_address" for Adding/Updating/Deleting
            Wireless SSID(s) mappings to VLAN(s).
          - Only "fabric_site_name_hierarchy" is required for performing Wireless
            SSID(s) operations.
          - The specified IP address must match the management IP displayed in the
            inventory section of Cisco Catalyst Center.
          - For example - "204.1.2.2"
          - Note - If ONLY the "ip_address" or "hostname" along with "fabric_site_name_hierarchy"
            is provided in the "deleted" state, all port assignment(s) or port channel(s)
            configured for the specified fabric device and wireless SSID(s) mappings
            in the fabric site will be deleted.
        type: str
      hostname:
        description:
          - Hostname of the target device in the SD-Access Fabric on which access
            device ports need to be configured.
          - Either "hostname" or "ip_address" of the network device, along with "fabric_site_name_hierarchy,"
            is required for performing port assignment or port channel operations.
          - It is not required to provide "hostname" for Adding/Updating/Deleting
            Wireless SSID(s) mappings to VLAN(s).
          - Only "fabric_site_name_hierarchy" is required for performing Wireless
            SSID(s) operations.
          - The specified hostname must be identical to the hostname displayed in
            the inventory section of Cisco Catalyst Center.
          - For example - "DC-T-9300.cisco.local"
          - Note - If ONLY the "ip_address" or "hostname" along with "fabric_site_name_hierarchy"
            is provided in the "deleted" state, all port assignment(s) or port channel(s)
            configured for the specified fabric device and wireless SSID(s) mappings
            in the fabric site will be deleted.
        type: str
      fabric_site_name_hierarchy:
        description:
          - Specifies the SD-Access Fabric Site within which host onboarding needs
            to be performed.
          - Providing "fabric_site_name_hierarchy" is required for performing all
            host onboarding operations.
          - Fabric site should be represented as a string value that indicates the
            complete hierarchical path of the site.
          - When creating or updating port channels, port assignments, and wireless
            SSIDs simultaneously, ensure that the operation is performed within the
            same fabric site.
          - Example - "Global/USA/San Jose/BLDG23"
          - If only the "fabric_site_name_hierarchy" is provided in the "merged" state,
            only Wireless SSID(s) will be added or updated for the specified fabric
            site.
          - If only the "fabric_site_name_hierarchy" is provided in the "deleted"
            state, all the Wireless SSID(s) configured for the specific fabric site
            will be deleted.
        type: str
        required: true
      port_assignments:
        description:
          - A list containing configuration details for adding, updating, or deleting
            port assignment(s) in Cisco Catalyst Center.
          - The "interface_name" and "connected_device_type" fields are required for
            add and update port assignment(s) operations.
          - For the update port channel(s) operation, the parameters that can be updated
            include "data_vlan_name", "voice_vlan_name", "authentication_template_name"
            and "interface_description".
          - For delete port assignment(s) operation, the valid parameters are "interface_name,"
            "data_vlan_name," and "voice_vlan_name". If all three parameters are provided,
            only port assignments that match all specified criteria are deleted (i.e.,
            AND filtering is applied).
        type: list
        elements: dict
        suboptions:
          interface_name:
            description:
              - Specifies the name of the port or interface on the fabric device where
                port assignment operations need to be performed.
              - This parameter is required for adding or updating port assignments.
              - For example - "GigabitEthernet2/1/1"
            type: str
          connected_device_type:
            description:
              - Specifies the type of access device that needs to be onboarded on
                the specified interface.
              - Valid options for Connected Device Types are - "USER_DEVICE", "ACCESS_POINT",
                and "TRUNKING_DEVICE".
              - TRUNKING_DEVICE - Configures the interface as a trunk port. No additional
                parameters are required for this Connected Device Type. If the "authentication_template_name"
                is provided, it must be set to 'No Authentication' when configuring
                a "TRUNKING_DEVICE".
              - ACCESS_POINT - Configures the port for connecting an access point.
                The "data_vlan_name" parameter is required when configuring "ACCESS_POINT"
                devices in port assignments. Optionally, the "authentication_template_name"
                and "interface_description" can also be specified.
              - USER_DEVICE - Configures the port to connect to a host device, such
                as an IP phone, computer, or laptop. At least one VLAN ("data_vlan_name"
                or "voice_vlan_name") is required when configuring a "USER_DEVICE".
                Optional parameters include "security_group_name", "authentication_template_name",
                and "interface_description".
              - Note - The "connected_device_type" cannot be updated from "TRUNK"
                to "EXTENDED_NODE" unless the protocol configured is PAGP.
            type: str
            choices: ["TRUNKING_DEVICE", "ACCESS_POINT", "USER_DEVICE"]
          data_vlan_name:
            description:
              - Specifies the Data VLAN name or IP address pool to be assigned to
                the port.
              - This parameter is required when the connected_device_type is set to
                ACCESS_POINT.
              - At least one VLAN ("data_vlan_name" or "voice_vlan_name") is required
                when configuring a "USER_DEVICE".
            type: str
          voice_vlan_name:
            description:
              - Specifies the Voice VLAN name or IP address pool to be assigned to
                the port.
              - At least one VLAN ("data_vlan_name" or "voice_vlan_name") is required
                when configuring a "USER_DEVICE".
            type: str
          security_group_name:
            description:
              - Specifies the security or scalable group name for the port assignment.
              - Security/scalable groups are only supported with the "No Authentication"
                profile.
            type: str
          authentication_template_name:
            description:
              - Specifies the authentication template applied to the port during the
                port assignment operation.
              - The available options are "No Authentication", "Open Authentication",
                "Closed Authentication", and "Low Impact".
              - The default "authentication_template_name" for all device types is
                "No Authentication".
              - For Connected Device Type "TRUNKING_DEVICE", the "authentication_template_name"
                must be set to "No Authentication".
              - Security/scalable groups are only supported with the "No Authentication"
                profile.
            type: str
            required: true
            choices: ["No Authentication", "Open Authentication", "Closed Authentication",
              "Low Impact"]
          interface_description:
            description:
              - A description of the port assignment interface.
            type: str
      port_channels:
        description:
          - A list containing configuration details for adding, updating, or deleting
            port channel(s) between a fabric edge and its remotely connected devices
            in Cisco Catalyst Center.
          - The "interface_names" and "connected_device_type" fields are required
            for add and update port channel(s) operations.
          - Only "interface_names" fieled is required for delete  port channel(s)
            operations.
          - For the update port channel(s) operation, the parameters that can be updated
            include "connected_device_type" and "port_channel_description".
          - For delete port channel(s) operation, the valid parameters are "port_channel_name"
            and "connected_device_type". If both parameters are provided, only port
            channels that match the specified criteria are deleted (i.e., AND filtering
            is applied).
        type: list
        elements: dict
        suboptions:
          interface_names:
            description:
              - A list of ports/interfaces of the target device in the SD-Access Fabric
                on which port channel needs to be configured.
              - A maximum of 8 ports are supported in interface_names for "PAGP" and
                "ON" protocols.
              - A maximum of 16 ports are supported in interface_names for the "LACP"
                protocol.
              - In the "merged" state, the specified interfaces will be updated in
                the port channel - If all given interfaces are not already part of
                the port channel, they will be added. - If a subset of interfaces
                is provided, any missing interfaces will be removed to match the given
                list. - For example - interface_names ["TenGigabitEthernet1/0/43",
                "TenGigabitEthernet1/0/44", "TenGigabitEthernet1/0/40"]` ensures all
                three interfaces are part of the port channel. - Running interface_names
                ["TenGigabitEthernet1/0/43", "TenGigabitEthernet1/0/44"]` will remove
                "TenGigabitEthernet1/0/40" from the port channel. - Running interface_names
                ["TenGigabitEthernet1/0/43", "TenGigabitEthernet1/0/44", "TenGigabitEthernet1/0/40"]`
                again will add "TenGigabitEthernet1/0/40" back to the port channel.
            type: list
            elements: str
          connected_device_type:
            description:
              - Specifies the type of device connected to the port channel. Valid
                options are "TRUNK" or "EXTENDED_NODE".
              - To create a port channel between a fabric edge node and an extended
                node, or between two extended nodes, select "EXTENDED_NODE".
              - To create a port channel with a fabric edge node or extended node
                on one side, and a third-party device or server port on the other
                side, choose "TRUNK".
            type: str
            choices: ["TRUNK", "EXTENDED_NODE"]
          protocol:
            description:
              - Specifies the appropriate protocol for the specific Connected Device
                Type to be configured on the port channel.
              - Valid options are "ON", "LACP", and "PAGP".
              - By default, the protocol is "ON" for "connected_device_type" - "EXTENDED_NODE".
              - By default, the protocol is "LACP" for "connected_device_type" - "TRUNK".
              - Protocol field cannot be updated after the initial configuration.
              - The "connected_device_type" cannot be updated from "TRUNK" to "EXTENDED_NODE"
                unless the protocol configured is PAGP.
            type: str
            choices: ["ON", "LACP", "PAGP"]
          port_channel_description:
            description:
              - A description of the port channel.
            type: str
      wireless_ssids:
        description:
          - A list containing configuration details for adding, updating or removing,
            Guest or Enterprise Wireless SSID(s) mapping to Fabric Enabled VLAN(s)
            in the Cisco Catalyst Center.
          - For wireless SSIDs operations, only fabric_site_name_hierarchy is required,
            ip_address and hostname are not needed.
          - Note - For the delete operation, all SSIDs mapped to a VLAN can be removed
            by providing the vlan_name. Alternatively, specific wireless SSIDs mapped
            to a VLAN can be deleted by specifying a list of ssid_names that need
            to be removed. The'security_group_name' must not be provided.
        type: list
        elements: dict
        suboptions:
          vlan_name:
            description:
              - Specifies the name of the VLAN or IP pool reserved for the Wireless
                SSID.
              - It must be a 'Fabric Wireless Enabled' VLAN and should be part of
                the Fabric Site representing 'fabric_site_name_hierarchy'.
              - For the delete operation, all SSIDs mapped to a VLAN can be removed
                by providing the vlan_name.
            type: str
          ssid_details:
            description:
              - A list of Wireless SSID(s) details to be added, updated, or removed
                for the specified VLAN or IP Address pool.
            type: list
            elements: dict
            suboptions:
              ssid_name:
                description:
                  - The name of the Wireless SSID(s) to be mapped to the VLAN. Ensure
                    that specified Wireless SSID is a Fabric SSID.
                  - For the delete operation, specific wireless SSIDs mapped to a
                    VLAN can be deleted by specifying a list of ssid_names that need
                    to be removed.
                type: str
              security_group_name:
                description:
                  - Represents the name of the Security Group or Security Group Tag
                    to be assigned to the Wireless SSID.
                  - Example - Auditors, BYOD, Developers, Guests, etc.
                type: str
requirements:
  - dnacentersdk >= 2.9.2
  - python >= 3.9
notes:
  - SDK Methods used are - devices.Devices.get_device_list - sda.SDA.get_device_info
    - site_design.SiteDesigns.get_sites - sda.SDA.get_fabric_sites - sda.SDA.get_port_assignments
    - sda.SDA.get_port_channels - sda.SDA.add_port_assignments - sda.SDA.update_port_assignments
    - sda.SDA.delete_port_assignments - sda.SDA.add_port_channels - sda.SDA.update_port_channels
    - sda.SDA.update_port_channels - sda.SDA.add_update_or_remove_ssid_mapping_to_a_vlan
    - sda.SDA.retrieve_the_vlans_and_ssids_mapped_to_the_vlan_within_a_fabric_site
  - Paths used are - GET /dna/intent/api/v1/network-device - GET /dna/intent/api/v1/business/sda/device
    - GET /dna/intent/api/v1/sites - GET /dna/intent/api/v1/sda/fabricSites - GET
    /dna/intent/api/v1/sda/portAssignments - GET /dna/intent/api/v1/sda/portChannels
    - POST /dna/intent/api/v1/sda/portAssignments - PUT /dna/intent/api/v1/sda/portAssignments
    - DELETE /dna/intent/api/v1/sda/portAssignments - POST /dna/intent/api/v1/sda/portChannels
    - PUT /dna/intent/api/v1/sda/portChannels - DELETE /dna/intent/api/v1/sda/portChannels
    - PUT /dna/intent/api/v1/sda/fabrics/${fabricId}/vlanToSsids - GET /dna/intent/api/v1/sda/fabrics/${fabricId}/vlanToSsids
"""
EXAMPLES = r"""
- name: Add port assignments, port channels and wireless ssids for a specific fabric
    site
  cisco.dnac.sda_host_port_onboarding_workflow_manager:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    dnac_log: true
    dnac_log_level: "{{dnac_log_level}}"
    state: merged
    config:
      - ip_address: "204.1.2.2"
        fabric_site_name_hierarchy: "Global/USA/San Jose/BLDG23"
        port_assignments:
          # Create TRUNKING DEVICE
          - interface_name: "FortyGigabitEthernet1/1/1"
            connected_device_type: "TRUNKING_DEVICE"
          - interface_name: "FortyGigabitEthernet1/1/2"
            connected_device_type: "TRUNKING_DEVICE"
            authentication_template_name: "No Authentication"
            interface_description: "Trunk Port"
          # Create Access Points
          - interface_name: "FortyGigabitEthernet2/1/1"
            connected_device_type: "ACCESS_POINT"
            data_vlan_name: "AG_VLAN_23"
          - interface_name: "FortyGigabitEthernet2/1/2"
            connected_device_type: "ACCESS_POINT"
            data_vlan_name: "AG_VLAN_23"
            authentication_template_name: "No Authentication"
            interface_description: "Access Point Port"
          # Create User Devices
          - interface_name: "GigabitEthernet1/1/4"
            connected_device_type: "USER_DEVICE"
            data_vlan_name: "AG_VLAN_23"
          - interface_name: "GigabitEthernet2/1/1"
            connected_device_type: "USER_DEVICE"
            voice_vlan_name: "VOICE_VLAN_23"
          - interface_name: "GigabitEthernet2/1/2"
            connected_device_type: "USER_DEVICE"
            data_vlan_name: "AG_VLAN_23"
            voice_vlan_name: "VOICE_VLAN_23"
        port_channels:
          # Default protocol is ON for TRUNK
          - interface_names: ["TenGigabitEthernet1/0/37", "TenGigabitEthernet1/0/38", "TenGigabitEthernet1/0/39"]
            connected_device_type: "TRUNK"
          - interface_names: ["TenGigabitEthernet1/0/43", "TenGigabitEthernet1/0/44"]
            connected_device_type: "TRUNK"
            protocol: "ON"
          - interface_names: ["TenGigabitEthernet1/0/45", "TenGigabitEthernet1/0/46", "TenGigabitEthernet1/0/47", "TenGigabitEthernet1/0/48"]
            connected_device_type: "TRUNK"
            protocol: "LACP"
          - interface_names: ["TenGigabitEthernet1/1/2", "TenGigabitEthernet1/1/3", "TenGigabitEthernet1/1/4"]
            connected_device_type: "TRUNK"
            protocol: "PAGP"
            port_channel_description: "Trunk port channel"
          # Default protocol for EXTENDED_NODE is PAGP
          - interface_names: ["TenGigabitEthernet1/1/5", "TenGigabitEthernet1/1/6"]
            connected_device_type: "EXTENDED_NODE"
          - interface_names: ["TenGigabitEthernet1/1/7", "TenGigabitEthernet1/1/8"]
            connected_device_type: "EXTENDED_NODE"
            protocol: "PAGP"
            port_channel_description: "extended node port channel"
        wireless_ssids:
          - vlan_name: "IAC-VLAN-1"
            ssid_details:
              - ssid_name: "open1-iac"
          - vlan_name: "IAC-VLAN-3"
            ssid_details:
              - ssid_name: "ent_ssid_1_wpa3"
                security_group_name: "Developers"
- name: Update port assignments, port channels and wireless ssids for a specific
    fabric site
  cisco.dnac.sda_host_port_onboarding_workflow_manager:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    dnac_log: true
    dnac_log_level: "{{dnac_log_level}}"
    state: merged
    config:
      - hostname: "DC-T-9300.cisco.local"
        fabric_site_name_hierarchy: "Global/USA/San Jose/BLDG23"
        port_assignments:
          # update - add interface_description
          - interface_name: "FortyGigabitEthernet1/1/1"
            connected_device_type: "TRUNKING_DEVICE"
            interface_description: "Trunk Port at interface 111"
          # update - update the interface_description
          - interface_name: "FortyGigabitEthernet2/1/2"
            connected_device_type: "ACCESS_POINT"
            data_vlan_name: "AG_VLAN_23"
            authentication_template_name: "No Authentication"
            interface_description: "Access Point Port at 212"
          # update - change data vlan
          - interface_name: "GigabitEthernet1/1/4"
            connected_device_type: "USER_DEVICE"
            data_vlan_name: "AG_VLAN_23"
          # update - change voice to data vlan
          - interface_name: "GigabitEthernet2/1/1"
            connected_device_type: "USER_DEVICE"
            data_vlan_name: "AG_VLAN_23"
          # update - remove data vlan
          - interface_name: "GigabitEthernet2/1/2"
            connected_device_type: "USER_DEVICE"
            voice_vlan_name: "VOICE_VLAN_23"
        port_channels:
          # update - add interfaces in the port channel
          - interface_names: ["TenGigabitEthernet1/0/43", "TenGigabitEthernet1/0/44", "TenGigabitEthernet1/0/40"]
            connected_device_type: "TRUNK"
            protocol: "ON"
          # update - add interface and description
          - interface_names: ["TenGigabitEthernet1/0/37", "TenGigabitEthernet1/0/38", "TenGigabitEthernet1/0/39", "TenGigabitEthernet1/0/41"]
            connected_device_type: "TRUNK"
            port_channel_description: "Trunk port channel"
          # update - remove interface from the port channel
          - interface_names: ["TenGigabitEthernet1/0/45", "TenGigabitEthernet1/0/46", "TenGigabitEthernet1/0/47"]
            connected_device_type: "TRUNK"
            protocol: "LACP"
          # update - change device type from extended_node to trunk
          - interface_names: ["TenGigabitEthernet1/1/5", "TenGigabitEthernet1/1/6"]
            connected_device_type: "TRUNK"
          # update - change device type from trunk to extended node when protocol is pagp
          - interface_names: ["TenGigabitEthernet1/1/2", "TenGigabitEthernet1/1/3", "TenGigabitEthernet1/1/4"]
            connected_device_type: "EXTENDED_NODE"
            protocol: "PAGP"
            port_channel_description: "Trunk port channel"
        wireless_ssids:
          # update - add security_group_name
          - vlan_name: "IAC-VLAN-1"
            ssid_details:
              - ssid_name: "open1-iac"
                security_group_name: "Guests"
          # update - remove security_group_name
          - vlan_name: "IAC-VLAN-3"
            ssid_details:
              - ssid_name: "ent_ssid_1_wpa3"
- name: Add or Update just wireless ssid mappings for a specific fabric site (IP/Hostname
    not required)
  cisco.dnac.sda_host_port_onboarding_workflow_manager:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    dnac_log: true
    dnac_log_level: "{{dnac_log_level}}"
    state: merged
    config:
      - fabric_site_name_hierarchy: "Global/USA/San Jose/BLDG23"
        wireless_ssids:
          - vlan_name: "IAC-VLAN-1"
            ssid_details:
              - ssid_name: "ent_ssid_1_wpa3"
                security_group_name: "Developers"
          - vlan_name: "IAC-VLAN-3"
            ssid_details:
              - ssid_name: "guest_ssid_1"
                security_group_name: "Guests"
- name: Delete ALL port assignments, port channels and wireless SSID mappings from
    a fabric site
  cisco.dnac.sda_host_port_onboarding_workflow_manager:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    dnac_log: true
    dnac_log_level: "{{dnac_log_level}}"
    state: deleted
    config:
      - hostname: "DC-T-9300.cisco.local"
        fabric_site_name_hierarchy: "Global/USA/San Jose/BLDG23"
- name: Delete ALL port assignments, port channels and wireless SSID mappings from
    a fabric site
  cisco.dnac.sda_host_port_onboarding_workflow_manager:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    dnac_log: true
    dnac_log_level: "{{dnac_log_level}}"
    state: deleted
    config:
      - ip_address: "204.1.2.2"
        fabric_site_name_hierarchy: "Global/USA/San Jose/BLDG23"
- name: Delete just ALL wireless SSIDs mappings from a fabric site
  cisco.dnac.sda_host_port_onboarding_workflow_manager:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    dnac_log: true
    dnac_log_level: "{{dnac_log_level}}"
    state: deleted
    config:
      - fabric_site_name_hierarchy: "Global/USA/San Jose/BLDG23"
- name: Delete specific port assignments, port channels and wireless SSID mappings
  cisco.dnac.sda_host_port_onboarding_workflow_manager:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    dnac_log: true
    dnac_log_level: "{{dnac_log_level}}"
    state: deleted
    config:
      - ip_address: "204.1.2.2"
        fabric_site_name_hierarchy: "Global/USA/San Jose/BLDG23"
        port_assignments:
          - interface_name: "FortyGigabitEthernet2/1/2"
            connected_device_type: "ACCESS_POINT"
            data_vlan_name: "AG_VLAN_23"
            authentication_template_name: "No Authentication"
            interface_description: "Access Point Port at 212"
        port_channels:
          - interface_names: ["TenGigabitEthernet1/0/37", "TenGigabitEthernet1/0/38", "TenGigabitEthernet1/0/39"]
            connected_device_type: "TRUNK"
          - interface_names: ["TenGigabitEthernet1/0/43", "TenGigabitEthernet1/0/44"]
            connected_device_type: "TRUNK"
            protocol: "ON"
        wireless_ssids:
          - vlan_name: "IAC-VLAN-1"
            ssid_details:
              - ssid_name: "open1-iac"
                security_group_name: "Guests"
- name: Delete specific port assignments, port channels and wireless SSID mappings
  cisco.dnac.sda_host_port_onboarding_workflow_manager:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    dnac_log: true
    dnac_log_level: "{{dnac_log_level}}"
    state: deleted
    config:
      - ip_address: "204.1.2.2"
        fabric_site_name_hierarchy: "Global/USA/San Jose/BLDG23"
        port_assignments:
          - interface_name: "FortyGigabitEthernet1/1/1"
          - interface_name: "FortyGigabitEthernet1/1/2"
          - interface_name: "GigabitEthernet2/1/1"
          - interface_name: "TenGigabitEthernet1/0/37"
          - interface_name: "TenGigabitEthernet1/0/38"
          - interface_name: "TenGigabitEthernet1/0/39"
        port_channels:
          - interface_names: ["TenGigabitEthernet1/0/45", "TenGigabitEthernet1/0/46", "TenGigabitEthernet1/0/47", "TenGigabitEthernet1/0/48"]
          - interface_names: ["TenGigabitEthernet1/1/2", "TenGigabitEthernet1/1/3", "TenGigabitEthernet1/1/4"]
        wireless_ssids:
          - vlan_name: "IAC-VLAN-1"
          - vlan_name: "IAC-VLAN-3"
            ssid_details:
              - ssid_name: "ent_ssid_1_wpa3"
- name: Delete all wireless SSIDs mapped to specific VLANs
  cisco.dnac.sda_host_port_onboarding_workflow_manager:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    dnac_log: true
    dnac_log_level: "{{dnac_log_level}}"
    state: deleted
    config:
      - ip_address: "204.1.2.2"
        fabric_site_name_hierarchy: "Global/USA/San Jose/BLDG23"
        wireless_ssids:
          - vlan_name: "IAC-VLAN-1"
          - vlan_name: "IAC-VLAN-3"
- name: Delete specific wireless SSIDs mapped to a VLAN
  cisco.dnac.sda_host_port_onboarding_workflow_manager:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    dnac_log: true
    dnac_log_level: "{{dnac_log_level}}"
    state: deleted
    config:
      - ip_address: "204.1.2.2"
        fabric_site_name_hierarchy: "Global/USA/San Jose/BLDG23"
        wireless_ssids:
          - vlan_name: "IAC-VLAN-1"
            ssid_details:
              - ssid_name: "ent-ssid-2-wpa2"
          - vlan_name: "IAC-VLAN-3"
            ssid_details:
              - ssid_name: "guest_ssid_1"
              - ssid_name: "ent-ssid-2-wpa2"
"""
RETURN = r"""
# Case_1: Success Scenario
response_1:
  description: A dictionary with  with the response returned by the Cisco Catalyst Center Python SDK
  returned: always
  type: dict
  sample: >
    {
      "response":
        {
          "response": String,
          "version": String
        },
      "msg": String
    }
# Case_2: Error Scenario
response_2:
  description: A string with the response returned by the Cisco Catalyst Center Python SDK
  returned: always
  type: list
  sample: >
    {
      "response": [],
      "msg": String
    }
"""


from ansible.module_utils.basic import AnsibleModule
from ansible_collections.cisco.dnac.plugins.module_utils.dnac import (
    DnacBase,
    validate_list_of_dicts
)


class SDAHostPortOnboarding(DnacBase):
    """
    A class for managing Extranet Policies within the Cisco DNA Center using the SDA API.
    """
    def __init__(self, module):
        """
        Initialize an instance of the class.
        Args:
          - module: The module associated with the class instance.
        Returns:
          The method does not return a value.
        """
        super().__init__(module)

    def validate_input(self):
        """
        Validates the input configuration parameters for the playbook.
        Returns:
            object: An instance of the class with updated attributes:
                - self.msg: A message describing the validation result.
                - self.status: The status of the validation (either "success" or "failed").
                - self.validated_config: If successful, a validated version of the "config" parameter.

        Description:
            This method validates the fields provided in the playbook against a predefined specification.
            It checks if the required fields are present and if their data types match the expected types.
            If any parameter is found to be invalid, it logs an error message and sets the validation status to "failed".
            If the validation is successful, it logs a success message and returns an instance of the class
            with the validated configuration.
        """
        # Check if configuration is available
        if not self.config:
            self.status = "success"
            self.msg = "Configuration is not available in the playbook for validation"
            self.log(self.msg, "ERROR")
            return self

        # Expected schema for configuration parameters
        temp_spec = {
            "ip_address": {"type": "str", "required": False},
            "hostname": {"type": "str", "required": False},
            "fabric_site_name_hierarchy": {"type": "str", "required": False},
            "port_assignments": {
                "type": "list",
                "elements": "dict",
                "required": False,
                "options": {
                    "interface_name": {"type": "str"},
                    "connected_device_type": {"type": "str"},
                    "data_vlan_name": {"type": "str"},
                    "voice_vlan_name": {"type": "str"},
                    "security_group_name": {"type": "str"},
                    "authentication_template_name": {"type": "str"},
                    "interface_description": {"type": "str"}
                }
            },
            "port_channels": {
                "type": "list",
                "elements": "dict",
                "required": False,
                "options": {
                    "interface_names": {"type": "list", "elements": "str"},
                    "connected_device_type": {"type": "str"},
                    "protocol": {"type": "str"},
                    "port_channel_description": {"type": "str"},
                    "port_channel_name": {"type": "str"}
                }
            },
            "wireless_ssids": {
                "type": "list",
                "elements": "dict",
                "required": False,
                "options": {
                    "vlan_name": {"type": "str"},
                    "ssid_details": {
                        "type": "list",
                        "elements": "dict",
                        "required": False,
                        "options": {
                            "ssid_name": {"type": "str"},
                            "security_group_name": {"type": "str"}
                        }
                    }
                }
            }
        }

        # Validate params
        valid_temp, invalid_params = validate_list_of_dicts(
            self.config, temp_spec
        )

        if invalid_params:
            self.msg = "Invalid parameters in playbook: {0}".format(invalid_params)
            self.set_operation_result("failed", False, self.msg, "ERROR")
            return self

        # Set the validated configuration and update the result with success status
        self.validated_config = valid_temp
        self.msg = "Successfully validated playbook configuration parameters using 'validated_input': {0}".format(str(valid_temp))
        self.set_operation_result("success", False, self.msg, "INFO")
        return self

    def validate_device_exists_and_reachable(self, ip_address, hostname):
        """
        Validates whether a device is present in the Catalyst Center and has an acceptable status.
        Args:
            ip_address (str): The IP address of the device to be validated.
            hostname (str): The hostname of the device to be validated.
        Returns:
            bool: True if the device is reachable and has an acceptable collection status, False otherwise.
        """
        device_identifier = ip_address or hostname
        self.log("Initiating validation for device: '{0}'.".format(device_identifier), "INFO")

        if ip_address:
            get_device_list_params = {"management_ip_address": ip_address}
        elif hostname:
            get_device_list_params = {"hostname": hostname}

        self.log("Executing 'get_device_list' API call with parameters: {0}".format(get_device_list_params), "DEBUG")

        response = self.execute_get_request("devices", "get_device_list", get_device_list_params)

        if not response or not response.get("response"):
            self.msg = (
                "Failed to retrieve details for the specified device: {0}. "
                "Please verify that the device exists in the Catalyst Center."
            ).format(device_identifier)
            self.fail_and_exit(self.msg)

        device_info = response["response"][0]
        reachability_status = device_info.get("reachabilityStatus")
        collection_status = device_info.get("collectionStatus")

        if reachability_status == "Reachable" and collection_status in ["In Progress", "Managed"]:
            self.log("Device: {0} is reachable and has an acceptable collection status.".format(device_identifier), "INFO")
            return True

        self.msg = (
            "Cannot perform port onboarding operation on device {0}: "
            "reachabilityStatus is '{1}', collectionStatus is '{2}'.".format(
                device_identifier, reachability_status, collection_status
            )
        )
        return False

    def validate_ip_and_hostname(self, ip_address, hostname):
        """
        Validates the provided IP address and hostname.
        Args:
            ip_address (str): The IP address to be validated.
            hostname (str): The hostname to be validated.
        Returns:
            None: This method does not return a value. It updates the instance attributes:
                - self.msg: A message describing the validation result.
                - self.status: The status of the validation (either "success" or "failed").
        Description:
            This method checks if either an IP address or a hostname is provided. If neither is provided,
            it logs an error message and sets the validation status to "failed". Additionally, it verifies
            if the provided IP address is a valid IPv4 address. If the IP address is invalid, it logs an error
            message and sets the validation status to "failed".
        """
        self.log("Validating IP address: '{0}' and hostname: '{1}'".format(ip_address, hostname), "DEBUG")

        # Check if both IP address and hostname are not provided
        if not ip_address and not hostname:
            self.msg = "Provided IP address: {0}, hostname: {1}. Either an IP address or a hostname is required.".format(ip_address, hostname)
            self.fail_and_exit(self.msg)

        # Check if an IP address is provided but it is not valid
        if ip_address and not self.is_valid_ipv4(ip_address):
            self.msg = "IP address: {0} is not a valid IP Address.".format(ip_address)
            self.fail_and_exit(self.msg)

        # Check if device exists and is reachable in Catalyst Center
        if not self.validate_device_exists_and_reachable(ip_address, hostname):
            self.fail_and_exit(self.msg)

        self.log("Validation successful: Provided IP address or hostname are valid")

    def validate_port_assignment_params(self, interface_name, connected_device_type):
        """
        Validates the required parameters for port assignment operations.
        Args:
            interface_name (str): The name of the interface to be validated.
            connected_device_type (str): The type of the connected device to be validated.
        Returns:
            None: This method does not return a value. It updates the instance attributes:
                - self.msg: A message describing the validation result.
                - self.status: The status of the validation (either "success" or "failed").
        Description:
            This method checks if both `interface_name` and `connected_device_type` are provided.
            If either parameter is missing, it logs an error message and sets the validation status to "failed".
            These parameters are essential for Add/Update Port Assignment operations.
        """
        # Check if either interface_name or connected_device_type is not provided
        self.log("Validating if required parameters 'interface_name' and 'connected_device_type' are provided", "DEBUG")

        if not interface_name or not connected_device_type:
            self.msg = (
                "Both 'interface_name' and ;connected_device_type' are required parameters for Add/Update "
                "Port Assignment operations. Provided 'interface_name': {0}, 'connected_device_type': {1}."
            ).format(interface_name, connected_device_type)
            self.fail_and_exit(self.msg)

        self.log("Validation successful: Provided required parameters 'interface_name' and 'connected_device_type'.", "DEBUG")

    def validate_port_assignment_connected_device_type(self, interface_name, connected_device_type):
        """
        Validates the connected device type for a given interface.
        Args:
            interface_name (str): The name of the interface to be validated.
            connected_device_type (str): The type of the connected device to be validated.
        Returns:
            None: This method does not return a value. It updates the instance attributes:
                - self.msg: A message describing the validation result.
                - self.status: The status of the validation (either "success" or "failed").
        Description:
            This method checks if the provided `connected_device_type` is among the valid device types
            for port assignments. If the type is invalid, it logs an error message and sets the validation
            status to "failed". If the type is valid, it logs a success message.
        """
        self.log("Validating connected device type: '{0}' for interface: '{1}'".format(connected_device_type, interface_name), "DEBUG")

        # List of valid connected device types
        valid_device_types = ["USER_DEVICE", "ACCESS_POINT", "TRUNKING_DEVICE"]

        # Check if the connected device type is valid
        if connected_device_type and connected_device_type.upper() not in valid_device_types:
            valid_device_types_str = ", ".join(valid_device_types)
            self.msg = (
                "Interface {0}: Connected device type: {1} is not valid. "
                "Valid device types are: {2}"
            ).format(interface_name, connected_device_type, valid_device_types_str)
            self.fail_and_exit(self.msg)

        # Log a success message indicating the connected device type is valid
        self.log("Interface {0}: Successfully validated the connected device type: {1}".format(interface_name, connected_device_type), "DEBUG")

    def validate_interface_authentication_template(self, interface_name, authentication_template_name):
        """
        Validates the authentication template name for a given interface.
        Args:
            interface_name (str): The name of the interface to be validated.
            authentication_template_name (str): The authentication template name to be validated.
        Returns:
            None: This method does not return a value. It updates the instance attributes:
                - self.msg: A message describing the validation result.
                - self.status: The status of the validation (either "success" or "failed").
        Description:
            This method checks if the provided `authentication_template_name` is among the valid authentication
            templates for the interface. If the template name is invalid, it logs an error message and sets the
            validation status to "failed". If the template name is valid, it logs a success message.
        """
        self.log("Validating authentication template: '{0}' for interface: '{1}'".format(authentication_template_name, interface_name), "DEBUG")

        # List of valid authentication template names
        valid_template_names = ["No Authentication", "Open Authentication", "Closed Authentication", "Low Impact"]

        # Check if the authentication template name is valid
        if authentication_template_name not in valid_template_names:
            valid_names_str = ", ".join(valid_template_names)
            self.msg = ("Interface {0}: Authentication template '{1}' is not valid. "
                        "Valid authentication templates are: {2}").format(interface_name, authentication_template_name, valid_names_str)
            self.fail_and_exit(self.msg)

        # Log a success message indicating the authentication template name is valid
        self.log("Interface {0}: Successfully validated the authentication template: {1}".format(interface_name, authentication_template_name), "DEBUG")

    def validate_trunking_device_assignment_params(self, port_assignment):
        """
        Validates the parameters for a trunking device in a port assignment.
        Args:
            port_assignment (dict): The port assignment details containing parameters to be validated.
        Returns:
            None: This method does not return a value. It updates the instance attributes:
                - self.msg: A message describing the validation result.
                - self.status: The status of the validation (either "success" or "failed").
        Description:
            This method validates the parameters for a device of type 'TRUNKING_DEVICE' in a port assignment.
            It ensures that the 'authentication_template_name' is set to 'No Authentication' and that no
            invalid parameters are provided. If any parameter is invalid, it logs an error message and sets the
            validation status to "failed". If all parameters are valid, it logs a success message.
        """
        # Retrieve specific parameters from the port_assignment dictionary

        interface_name = port_assignment.get("interface_name")
        connected_device_type = port_assignment.get("connected_device_type")
        authentication_template_name = port_assignment.get("authentication_template_name")

        self.log("Interface {0}: Starting validation for device type 'TRUNKING_DEVICE'.".format(interface_name), "DEBUG")

        # Check if authentication_template_name is set and not equal to 'No Authentication
        if authentication_template_name and authentication_template_name != "No Authentication":
            self.msg = (
                "Interface {0}: Authentication Template: {1} for Device Type - {2} is invalid. "
                "authentication_template_name must be 'No Authentication' for 'TRUNKING_DEVICE'."
            ).format(interface_name, authentication_template_name, connected_device_type)
            self.fail_and_exit(self.msg)

        # Check if any parameters provided in the port_assignment dictionary are not from the valid parameters
        valid_params = {"interface_name", "connected_device_type", "authentication_template_name", "interface_description"}
        provided_params = set(port_assignment.keys())
        invalid_params = provided_params - valid_params

        if invalid_params:
            invalid_params_str = ", ".join(invalid_params)
            self.msg = (
                "Interface {0}: Invalid parameter(s) provided for Device Type - TRUNKING_DEVICE: {1}. "
                "Parameters supported for TRUNKING_DEVICE are 'authentication_template_name' and 'interface_description'."
            ).format(interface_name, invalid_params_str)
            self.fail_and_exit(self.msg)

        self.log("Interface {0}: All provided parameters for 'TRUNKING_DEVICE' are valid".format(interface_name), "DEBUG")

    def validate_user_device_params(self, port_assignment):
        """
        Validates the parameters for a user device in a port assignment.
        Args:
            port_assignment (dict): The port assignment details containing parameters to be validated.
        Returns:
            None: This method does not return a value. It updates the instance attributes:
                - self.msg: A message describing the validation result.
                - self.status: The status of the validation (either "success" or "failed").
        Description:
            This method validates the parameters for a device of type 'USER_DEVICE' in a port assignment.
            It ensures that the appropriate VLANs are provided based on the authentication template name
            and that the security group name is used correctly. If any parameter is invalid, it logs an error
            message and sets the validation status to "failed". If all parameters are valid, it logs a success message.
        """
        # Retrieve specific parameters from the port_assignment dictionary
        interface_name = port_assignment.get("interface_name")
        authentication_template_name = port_assignment.get("authentication_template_name")
        connected_device_type = port_assignment.get("connected_device_type")
        security_group_name = port_assignment.get("security_group_name")
        data_vlan_name = port_assignment.get("data_vlan_name")
        voice_vlan_name = port_assignment.get("voice_vlan_name")

        self.log("Interface {0}: Starting validation for device type 'USER_DEVICE'.".format(interface_name), "DEBUG")

        valid_params = {
            "interface_name",
            "connected_device_type",
            "authentication_template_name",
            "data_vlan_name",
            "voice_vlan_name",
            "security_group_name",
            "interface_description"
        }
        provided_params = set(port_assignment.keys())
        invalid_params = provided_params - valid_params

        if invalid_params:
            invalid_params_str = ", ".join(invalid_params)
            self.msg = (
                "Interface {0}: Invalid parameter(s) provided for Device Type - USER_DEVICE: {1}. "
                "Parameters supported for USER_DEVICE are {2}."
            ).format(interface_name, invalid_params_str, valid_params)
            self.fail_and_exit(self.msg)

        # Check if the authentication_template_name is not "Closed Authentication"
        if authentication_template_name != "Closed Authentication":
            if not data_vlan_name and not voice_vlan_name:
                self.msg = (
                    "Interface {0}: Required parameter for Device Type - {1} is missing. "
                    "At least one VLAN: {2} is required for onboarding device type {1} for Authentication Template other than "
                    "Closed Authentication. Provided data_vlan_name: {3}, voice_vlan_name: {4}."
                ).format(interface_name, connected_device_type, "data_vlan_name OR voice_vlan_name", data_vlan_name, voice_vlan_name)
                self.fail_and_exit(self.msg)
            self.log("Interface {0}: VLAN validation for 'USER_DEVICE' passed.".format(interface_name), "DEBUG")

        # Check if security_group_name is provided and authentication_template_name is not "No Authentication"
        if security_group_name and authentication_template_name and authentication_template_name != "No Authentication":
            self.msg = ("Interface {0}: For Device Type  - {1}, if security_group_name is provided, "
                        "the authentication_template_name must be 'No Authentication'.".format(interface_name, connected_device_type))
            self.fail_and_exit(self.msg)
        self.log("Interface {0}: Security group name validation for 'USER_DEVICE' passed.".format(interface_name), "DEBUG")

        self.log("Interface {0}: All provided parameters for 'USER_DEVICE' are valid".format(interface_name), "DEBUG")

    def validate_access_point_params(self, port_assignment):
        """
        Validates the parameters for an access point in a port assignment.
        Args:
            port_assignment (dict): The port assignment details containing parameters to be validated.
        Returns:
            None: This method does not return a value. It updates the instance attributes:
                - self.msg: A message describing the validation result.
                - self.status: The status of the validation (either "success" or "failed").
        Description:
            This method validates the parameters for a device of type 'ACCESS_POINT' in a port assignment.
            It ensures that the required parameter 'data_vlan_name' is provided and that no invalid parameters
            are included. If any parameter is invalid, it logs an error message and sets the validation status
            to "failed". If all parameters are valid, it logs a success message.
        """
        # Retrieve specific parameters from the port_assignment dictionary
        interface_name = port_assignment.get("interface_name")
        connected_device_type = port_assignment.get("connected_device_type")
        required_param = "data_vlan_name"

        self.log("Interface {0}: Starting validation for device type 'ACCESS_POINT'.".format(interface_name), "DEBUG")

        # Check if the required parameter is present in port_assignment dictionary for a ACCESS_POINT
        if required_param not in port_assignment:
            self.msg = ("Interface {0}: Required parameter '{1}' for Device Type: {2} is missing. "
                        "Parameter required for onboarding device type {2} is '{1}'").format(
                            interface_name, required_param, connected_device_type)
            self.fail_and_exit(self.msg)
        self.log("Interface {0}: Required parameter '{1}' is present.".format(interface_name, required_param), "DEBUG")

        # Check if any parameters provided in the port_assignment dictionary are not from the valid parameters
        valid_params = {"interface_name", "connected_device_type", "authentication_template_name", "data_vlan_name", "interface_description"}
        provided_params = set(port_assignment.keys())
        invalid_params = provided_params - valid_params

        if invalid_params:
            invalid_params_str = ", ".join(invalid_params)
            self.msg = (
                "Interface {0}: Invalid parameter(s) provided for Device Type - ACCESS_POINT: {1}. "
                "Parameters supported for ACCESS_POINT are {2}."
            ).format(interface_name, invalid_params_str, valid_params)
            self.fail_and_exit(self.msg)

        self.log("Interface {0}: All provided parameters for 'ACCESS_POINT' are valid".format(interface_name), "DEBUG")

    def validate_device_specific_params(self, port_assignment):
        """
        Validates device-specific parameters in a port assignment.
        Args:
            port_assignment (dict): The port assignment details containing parameters to be validated.
        Returns:
            None: This method does not return a value. It updates the instance attributes:
                - self.msg: A message describing the validation result.
                - self.status: The status of the validation (either "success" or "failed").
        Description:
            This method validates the device-specific parameters for different types of connected devices in a port assignment.
            It first validates the 'authentication_template_name' if provided. Then, based on the 'connected_device_type',
            it calls the appropriate validation method for 'TRUNKING_DEVICE', 'USER_DEVICE', or 'ACCESS_POINT'.
            If any parameter is invalid, it logs an error message and sets the validation status to "failed".
            If all parameters are valid, it logs a success message.
        """
        # Retrieve required parameters from the port_assignment dictionary
        authentication_template_name = port_assignment.get("authentication_template_name")
        connected_device_type = port_assignment.get("connected_device_type")
        connected_device_type_upper = connected_device_type.upper()

        # Validate authentication_template_name if it is provided
        if authentication_template_name:
            self.log("Validating authentication template: '{0}' for interface.".format(authentication_template_name), "DEBUG")
            self.validate_interface_authentication_template(port_assignment.get("interface_name"), authentication_template_name)

        # Call the validation method for trunking device parameters
        if connected_device_type_upper == "TRUNKING_DEVICE":
            self.log("Calling trunking device parameter validation.", "DEBUG")
            self.validate_trunking_device_assignment_params(port_assignment)

        # Call the validation method for user device parameters
        elif connected_device_type_upper == "USER_DEVICE":
            self.log("Calling user device parameter validation.", "DEBUG")
            self.validate_user_device_params(port_assignment)

        # Call the validation method for access point parameters
        elif connected_device_type_upper == "ACCESS_POINT":
            self.log("Calling access point parameter validation.", "DEBUG")
            self.validate_access_point_params(port_assignment)

        self.log("Finished validation for device type '{0}'.".format(connected_device_type), "DEBUG")

    def validate_port_channel_params(self, port_channel):
        """
        Validates the required parameters for port channel operations.
        Args:
            port_channel (dict): The port channel details containing parameters to be validated.
        Returns:
            None: This method does not return a value. It updates the instance attributes:
                - self.msg: A message describing the validation result.
                - self.status: The status of the validation (either "success" or "failed").
        Description:
            This method checks if the required parameters 'interface_names' and 'connected_device_type' are present
            in the port channel details. If any required parameter is missing, it logs an error message and sets the
            validation status to "failed". If all required parameters are present, the method proceeds without logging
            an error message.
        """
        # Check for missing parameters by comparing required_params with the keys in port_channel
        self.log("Starting validation for port channel parameters.", "DEBUG")

        required_params = ["interface_names", "connected_device_type"]
        missing_params = [param for param in required_params if param not in port_channel.keys()]

        if missing_params:
            self.msg = ("The following required parameters for add/update port channel operations are missing: {0}. "
                        "Provided parameters: {1}").format(", ".join(missing_params), port_channel)
            self.fail_and_exit(self.msg)

        self.log("Port channel parameters validated successfully.", "DEBUG")

    def validate_port_channel_connected_device_type(self, port_channel):
        """
        Validates the connected device type for a port channel.
        Args:
            port_channel (dict): The port channel details containing parameters to be validated.
        Returns:
            None: This method does not return a value. It updates the instance attributes:
                - self.msg: A message describing the validation result.
                - self.status: The status of the validation (either "success" or "failed").
        Description:
            This method checks if the 'connected_device_type' in the port channel details is among the valid types
            'TRUNK' and 'EXTENDED_NODE'. If the device type is invalid, it logs an error message and sets the
            validation status to "failed". If the device type is valid, the method proceeds without logging an error message.
        """
        # Check if the connected_device_type is provided and not in the list of valid types
        valid_connected_device_types = ["TRUNK", "EXTENDED_NODE"]
        connected_device_type = port_channel.get("connected_device_type")

        self.log("Validating connected device type for port channel.", "DEBUG")

        if connected_device_type and connected_device_type.upper() not in valid_connected_device_types:
            valid_connected_device_types_str = ", ".join(valid_connected_device_types)
            self.msg = (
                "Provided connected_device_type: '{0}' is not valid for Port Channel operation: {1}. "
                "Valid connected_device_types for Port Channel operations are: {2}"
            ).format(connected_device_type, port_channel, valid_connected_device_types_str)
            self.fail_and_exit(self.msg)

        self.log("Port channel connected device type validated successfully.", "DEBUG")

    def validate_port_channel_protocol(self, port_channel):
        """
        Validates the protocol for a port channel based on the connected device type.
        Args:
            port_channel (dict): The port channel details containing parameters to be validated.
        Returns:
            None: This method does not return a value. It updates the instance attributes:
                - self.msg: A message describing the validation result.
                - self.status: The status of the validation (either "success" or "failed").
        Description:
            This method checks if the 'protocol' in the port channel details is valid for the specified 'connected_device_type'.
            It ensures that the protocol is among the valid protocols defined for the device type. If the protocol is invalid,
            it logs an error message and sets the validation status to "failed". If the protocol is valid, the method proceeds
            without logging an error message.
        """
        # Valid protocols for each connected device type
        valid_protocols = {
            "TRUNK": ["ON", "LACP", "PAGP"],
            "EXTENDED_NODE": ["PAGP"]
        }

        protocol = port_channel.get("protocol")
        connected_device_type = port_channel.get("connected_device_type")

        self.log("Starting protocol validation for port channel.", "DEBUG")

        # Check if the protocol is present and is not a boolean
        if protocol and not isinstance(protocol, bool):
            protocol_upper = protocol.upper()
            self.log("Validating protocol: {0} and connected_device_type: {1}".format(protocol_upper, connected_device_type), "DEBUG")

            # Check if protocol is valid for the connected device type
            device_valid_protocols = valid_protocols[connected_device_type]
            if protocol_upper not in device_valid_protocols:
                valid_protocols_str = ", ".join(device_valid_protocols)
                self.msg = (
                    "Invalid protocol: '{0}' provided for connected device type '{1}' in port channel operation. "
                    "Valid protocols for '{1}' are: {3}. Port channel details: {2}"
                ).format(protocol, connected_device_type, port_channel, valid_protocols_str)
                self.fail_and_exit(self.msg)

            self.log("Port channel protocol validated successfully for connected_device_type: {0}".format(connected_device_type), "DEBUG")

    def validate_port_channel_interfaces(self, port_channel):
        """
        Validates the interface names list for a given port channel configuration.
        Args:
            port_channel (dict): Dictionary containing port channel configuration details including
                                 'interface_names', 'protocol', and 'connected_device_type'.
        Returns:
            None: This method does not return a value. It updates the instance attributes:
                - self.msg: A message describing the validation result.
                - self.status: The status of the validation (either "success" or "failed").
        Description:
            This method checks if the number of interfaces in 'interface_names' does not exceed the protocol-specific
            limits for the given 'protocol'. If the protocol is 'PAGP' or 'ON', the maximum allowed interfaces are 8. If the
            protocol is 'LACP', the maximum allowed interfaces are 16. If the limits are exceeded, it logs an error message
            and sets the validation status to "failed".
        """
        interface_names_list = port_channel.get("interface_names")
        protocol = port_channel.get("protocol")
        connected_device_type = port_channel.get("connected_device_type")

        protocol = self.update_protocol(protocol, connected_device_type)

        self.log("Validating 'interface_names' list for protocol: {0} in port channel.".format(protocol), "DEBUG")

        # Define protocol-specific interface limits
        protocol_limits = {
            "PAGP": 8,
            "ON": 8,
            "LACP": 16
        }

        # Check if the protocol has a defined interface limit
        if protocol in protocol_limits:
            max_interfaces = protocol_limits[protocol]

            # Check if the number of interfaces exceeds the protocol-specific limit
            if len(interface_names_list) > max_interfaces:
                self.msg = (
                    "The number of interfaces provided: {0} exceeds the limit for protocol: {1} in port channel operation. "
                    "Maximum allowed interfaces for '{1}' protocol: {2}. Port channel details: {3}"
                ).format(len(interface_names_list), protocol, max_interfaces, port_channel)
                self.fail_and_exit(self.msg)

        self.log("Port channel 'interfaces_names' size validated successfully for protocol: {0}".format(protocol), "DEBUG")

    def validate_port_assignment_deletion_params(self, interface):
        """
        Validates the presence of the required parameter 'interface_name' in the interface dictionary
        for a delete port assignment operation.
        Args:
            interface (dict): Dictionary containing the interface parameters to be validated.
        Returns:
            None: This method does not return a value. It updates the instance attributes:
                - self.msg: A message describing the validation result.
                - self.status: The status of the validation (either "success" or "failed").
        Description:
            This method checks if the required parameter 'interface_name' is present in the provided
            interface dictionary. If the required parameter is missing, it logs an error message and
            sets the validation status to "failed". If the required parameter is present, the method
            logs a success message.
        """
        self.log("Starting validation for delete port assignments parameters: {0}".format(interface), "INFO")

        # Define the required parameter
        required_param = "interface_name"

        # Check if the required parameter is in the provided interface dictionary
        if required_param not in interface:
            self.msg = (
                "Missing required parameter '{0}' for port_assignment deletion operation. "
                "Provided params: {1}"
            ).format(required_param, interface)
            self.fail_and_exit(self.msg)

        # If the required parameter is present, log a success message
        self.log("The required parameter '{0}' is present in the provided parameters.".format(required_param), "INFO")

    def validate_port_channel_deletion_params(self, port_channel):
        """
        Validates the presence of the required parameter 'interface_names' in the port channel dictionary
        for a delete port channel operation.
        Args:
            port_channel (dict): Dictionary containing the port channel parameters to be validated.
        Returns:
            None: This method does not return a value. It updates the instance attributes:
                - self.msg: A message describing the validation result.
                - self.status: The status of the validation (either "success" or "failed").
        Description:
            This method checks if the required parameter 'interface_names' is present in the provided
            port channel dictionary. If the required parameter is missing, it logs an error message and
            sets the validation status to "failed". If the required parameter is present, the method
            logs a success message.
        """
        self.log("Starting validation for delete port channels parameters: {0}".format(port_channel), "INFO")

        # Define the required parameter
        required_param = "interface_names"

        # Check if the required parameter is in the provided port channel dictionary
        if required_param not in port_channel:
            self.msg = (
                "Missing required parameter '{0}' in the port_channel. "
                "Provided params: {1}"
            ).format(required_param, port_channel)
            self.fail_and_exit(self.msg)

        # If the required parameter is present, log a success message
        self.log("The required parameter '{0}' is present in the provided parameters.".format(required_param), "INFO")

    def validate_wireless_ssids_params(self, wireless_ssids_details):
        """
        Validates that each VLAN has SSID details and that each SSID has a name.
        Args:
            wireless_ssids_details (list): A list of dictionaries representing VLANs and their SSID details.
        Returns:
            None: This method does not return a value. It updates the instance attributes:
                - self.msg: A message describing the validation result.
        Description:
            This method iterates over each VLAN to check for the presence of SSID details and ensures
            that each SSID has a name. If any VLAN lacks SSID details or if any SSID lacks a name,
            it logs an error message and exits the process.
        """
        self.log("Starting validation of VLANs and SSID details mapped to VLANs.", "INFO")

        for vlan_info in wireless_ssids_details:
            self.log(vlan_info)
            vlan_name = vlan_info.get("vlan_name")
            self.log(vlan_name)
            ssid_details = vlan_info.get("ssid_details", [])
            self.log(ssid_details)

            # Check if SSID details exist
            if not ssid_details:
                self.msg = "Validation failed: SSID Details not provided for the VLAN: '{0}'.".format(vlan_name)
                self.fail_and_exit(self.msg)

            # Check if each SSID has a name
            for ssid in ssid_details:
                ssid_name = ssid.get("ssid_name")
                if not ssid_name:
                    self.msg = "Validation failed: SSID in VLAN '{0}' does not have a 'ssid_name'.".format(vlan_name)
                    self.log(self.msg, "ERROR")
                    self.fail_and_exit(self.msg)

        self.log("Successfully validated all VLANs and SSIDs.", "INFO")

    def validate_params(self, config, state):
        """
        Validates the configuration parameters based on the specified state.
        Args:
            config (dict): Dictionary containing the configuration details, including 'ip_address', 'hostname',
                           'port_assignment_details', and 'port_channel_details'.
            state (str): The state of the configuration, either 'merged' or 'deleted'.
        Returns:
            None: This method does not return a value. It updates the instance attributes:
                - self.msg: A message describing the validation result.
                - self.status: The status of the validation (either "success" or "failed").
        Description:
            This method performs validation on the configuration parameters. For the 'merged' state, it validates required
            port assignment and port channel parameters, connected device types, device-specific parameters, protocols, and
            interface names list. For the 'deleted' state, it validates the parameters for deletion in port assignments and
            port channels. If any validation fails, it logs an error message and sets the validation status to "failed".
        """
        ip_address = config.get("ip_address")
        hostname = config.get("hostname")
        fabric_site_name_hierarchy = config.get("fabric_site_name_hierarchy")
        port_assignment_details = config.get("port_assignments")
        port_channel_details = config.get("port_channels")
        wireless_ssids_details = config.get("wireless_ssids")

        if not fabric_site_name_hierarchy:
            self.msg = (
                "Required parameter 'fabric_site_name_hierarchy' not provided. Provide the "
                "SD-Access Fabric Site in which Host Onboarding operations need to be performed."
            )
            self.fail_and_exit(self.msg)

        if port_assignment_details or port_channel_details:
            self.log("Port assignment/Port Channel operation requested hence validating IP and Hostname.", "DEBUG")
            self.validate_ip_and_hostname(ip_address, hostname)

        if state == "merged":

            # Validate parameters for add/update in port assignments
            if port_assignment_details:
                for interface in port_assignment_details:
                    interface_name = interface.get("interface_name")
                    connected_device_type = interface.get("connected_device_type")
                    self.log("Validating port assignment params for interface: {0}, device type: {1}".format(interface_name, connected_device_type), "INFO")
                    self.validate_port_assignment_params(interface_name, connected_device_type)
                    self.validate_port_assignment_connected_device_type(interface_name, connected_device_type)
                    self.validate_device_specific_params(interface)

            # Validate parameters for add/update in port channels
            if port_channel_details:
                for port_channel in port_channel_details:
                    self.log("Validating port channel params for port_channel: {0}".format(port_channel), "INFO")
                    self.validate_port_channel_params(port_channel)
                    self.validate_port_channel_connected_device_type(port_channel)
                    self.validate_port_channel_protocol(port_channel)
                    self.validate_port_channel_interfaces(port_channel)

            if wireless_ssids_details:
                self.log("Validating Wireless SSIDs Details.", "INFO")
                self.validate_wireless_ssids_params(wireless_ssids_details)

        elif state == "deleted":
            # Validate parameters for deletion in port assignments
            if port_assignment_details:
                for interface in port_assignment_details:
                    self.log("Validating deletion of port assignment params for interface: {0}".format(interface), "INFO")
                    self.validate_port_assignment_deletion_params(interface)

            # Validate parameters for deletion in port channels
            if port_channel_details:
                for port_channel in port_channel_details:
                    self.log("Validating deletion of port channel details for port_channel: {0}".format(port_channel), "INFO")
                    self.validate_port_channel_deletion_params(port_channel)

        self.log("Validation completed for configuration: {0} with state: {1}.".format(config, state), "INFO")

    def get_device_list_params(self, ip_address, hostname):
        """
        Generates a dictionary of device list parameters based on the provided IP address or hostname.
        Args:
            ip_address (str): The management IP address of the device.
            hostname (str): The hostname of the device.
        Returns:
            dict: A dictionary containing the device list parameters with either 'management_ip_address' or 'hostname'.
        Description:
            This method creates a dictionary with either the 'management_ip_address' or 'hostname' based on the provided
            arguments. If both IP address and hostname are provided, the IP address takes precedence. If neither is provided,
            it returns an empty dictionary.
        """
        # Return a dictionary with 'management_ip_address' if ip_address is provided
        if ip_address:
            return {"management_ip_address": ip_address}
        # Return a dictionary with 'hostname' if hostname is provided

        if hostname:
            return {"hostname": hostname}
        # Return an empty dictionary if neither is provided

        return {}

    def get_device_ids_by_params(self, get_device_list_params):
        """
        Fetches device IDs from Cisco Catalyst Center based on provided parameters.
        Args:
            get_device_list_params (dict): Parameters for querying the device list, such as IP address or hostname.
        Returns:
            dict: A dictionary mapping management IP addresses to device instance IDs.
        Description:
            This method queries Cisco Catalyst Center using the provided parameters to retrieve device information.
            It checks if the device is reachable, managed, and not a Unified AP. If valid, it maps the management IP
            address to the device instance ID. If any error occurs or no valid device is found, it logs an error message
            and sets the validation status to "failed".
        """
        # Initialize the dictionary to map management IP to instance ID
        mgmt_ip_to_instance_id_map = {}
        self.log("Parameters for 'get_device_list API call: {0}".format(get_device_list_params), "DEBUG")
        try:
            # Query Cisco Catalyst Center for device information using the parameters
            response = self.dnac._exec(
                family="devices",
                function="get_device_list",
                op_modifies=False,
                params=get_device_list_params
            )
            self.log("Response received from 'get_device_list' API call: {0}".format(str(response)), "DEBUG")

            response = response.get("response")
            # Check if a valid response is received
            if not response:
                self.log("No devices were returned for the given parameters: {0}".format(get_device_list_params), "ERROR")
                return mgmt_ip_to_instance_id_map

            # Get the device information from the response
            device_info = response[0]
            device_ip = device_info.get("managementIpAddress")

            # Check if the device is reachable, not a Unified AP, and in a managed state
            if (device_info.get("reachabilityStatus") == "Reachable" and
                    device_info.get("collectionStatus") in ["Managed", "In Progress"] and
                    device_info.get("family") != "Unified AP"):
                device_id = device_info["id"]
                mgmt_ip_to_instance_id_map[device_ip] = device_id
                self.log("Device {0} is valid and added to the map.".format(device_ip), "INFO")
            else:
                self.log("Device {0} is not valid (either unreachable, not managed, or a Unified AP).".format(device_ip), "ERROR")

        except Exception as e:
            # Log an error message if any exception occurs during the process
            self.log(
                "Error while fetching device ID from Cisco Catalyst Center using API 'get_device_list' for Device: {0}. "
                "Error: {1}".format(get_device_list_params, str(e)),
                "ERROR"
            )
        # Log an error if no valid device is found
        if not mgmt_ip_to_instance_id_map:
            self.msg = (
                "Unable to retrieve details for the Device: {0}."
            ).format(
                get_device_list_params.get("management_ip_address") or get_device_list_params.get("hostname")
            )
            self.fail_and_exit(self.msg)

        return mgmt_ip_to_instance_id_map

    def get_device_info_from_sda_fabric(self, ip_address):
        """
        Retrieves site information for a device from the SDA fabric using its IP address.
        Args:
            ip_address (str): The management IP address of the device.
        Returns:
            str: The site name hierarchy where the device is located.
        Description:
            This method attempts to retrieve the site information from Cisco Catalyst Center for a given device
            using its IP address. It calls the SDA 'get_device_info' API and processes the response to extract
            the site name hierarchy. If an error occurs or no site name is found, it logs an error message and
            sets the validation status to "failed".
        """
        # Attempt to retrieve site information from Catalyst Center
        site_name = None
        try:
            response = self.dnac._exec(
                family="sda",
                function="get_device_info",
                op_modifies=False,
                params={"device_management_ip_address": ip_address},
            )
            self.log("Response received post SDA - 'get_device_info' API call: {0}".format(str(response)), "DEBUG")

            # Process the response if available
            if response:
                site_name = response["siteNameHierarchy"]
            else:
                self.log("No response received from the SDA - 'get_device_info' API call.", "WARNING")

        except Exception as e:
            # Log an error message and fail if an exception occurs
            self.log(
                "An error occurred while retrieving device details for Device '{0}' using SDA - 'get_device_info' API call: {1}".format(
                    ip_address, str(e)
                ),
                "ERROR"
            )

        if not site_name:
            self.msg = "Failed to retrieve site information for Device: '{0}'. Please verify that the device exists.".format(ip_address)
            self.fail_and_exit(self.msg)

        return site_name

    def get_fabric_sites(self, site_name, site_id):
        """
        Retrieve the fabric ID for a given site using the SDA 'get_fabric_sites' API call.
        Args:
            - site_name (str): The name of the site.
            - site_id (str): The unique identifier of the site.
        Returns:
            str: The fabric ID if found, otherwise None.
        Description:
            This method calls the SDA 'get_fabric_sites' API to retrieve the fabric ID for a specified site. It logs the response,
            processes the response to extract the fabric ID, and handles any exceptions that occur during the API call.
        """
        try:
            # Call the SDA 'get_fabric_sites' API with the provided site ID
            response = self.dnac._exec(
                family="sda",
                function="get_fabric_sites",
                op_modifies=False,
                params={"siteId": site_id},
            )
            self.log("Response received post SDA - 'get_fabric_sites' API call: {0}".format(str(response)), "DEBUG")

            response = response.get("response")
            if not response:
                self.log("No response received from the SDA - 'get_fabric_sites' API call.", "WARNING")
                return None

            fabric_id = response[0]["id"]
            return fabric_id

        except Exception as e:
            # Log an error message and fail if an exception occurs
            self.msg = (
                "An error occurred while retrieving 'fabric ID' for Site: '{0}' using SDA - "
                "'get_fabric_sites' API call: {1}".format(site_name, str(e))
            )
            self.fail_and_exit(self.msg)

    def get_network_device_id(self, ip_address, hostname):
        """
        Retrieves the network device ID for a given IP address or hostname.
        Args:
            ip_address (str): The IP address of the device to be queried.
            hostname (str): The hostname of the device to be queried.
        Returns:
            dict: A dictionary mapping management IP addresses to device IDs.
                  Returns an empty dictionary if no devices are found.
        """
        # Get Device IP Address and Id (networkDeviceId required)
        self.log("Starting device ID retrieval for IP: '{0}' or Hostname: '{1}'.".format(ip_address, hostname), "DEBUG")
        get_device_list_params = self.get_device_list_params(ip_address, hostname)
        self.log("get_device_list_params constructed: {0}".format(get_device_list_params), "DEBUG")
        mgmt_ip_to_instance_id_map = self.get_device_ids_by_params(get_device_list_params)
        self.log("Collected mgmt_ip_to_instance_id_map: {0}".format(mgmt_ip_to_instance_id_map), "DEBUG")

        return mgmt_ip_to_instance_id_map

    def get_fabric_id(self, fabric_site_name_hierarchy):
        """
        Retrieves the fabric ID for a given site within the network fabric.
        Args:
            fabric_site_name_hierarchy (str): The hierarchical name of the site within the fabric.
        Returns:
            str: The fabric ID of the specified site.
        """
        # Get siteId of the Site the device is part of
        self.log("Starting fabric ID retrieval for site: '{}'.".format(fabric_site_name_hierarchy), "INFO")

        self.log("Checking if site: {0} exists and retrieving site ID.".format(fabric_site_name_hierarchy), "DEBUG")
        site_exists, site_id = self.get_site_id(fabric_site_name_hierarchy)
        if not site_exists:
            self.msg = "Site ID not found for Site: {0}".format(fabric_site_name_hierarchy)
            self.fail_and_exit(self.msg)

        self.log("Retrieving fabric ID for site ID: '{0}'.".format(site_id), "DEBUG")
        # Get fabricId of the site
        fabric_id = self.get_fabric_sites(fabric_site_name_hierarchy, site_id)
        if not fabric_id:
            self.msg = "Fabric ID not found for Site: {0} with Site ID: {1}".format(
                fabric_site_name_hierarchy, site_id)
            self.fail_and_exit(self.msg)

        self.log("Successfully retrieved fabric ID: '{}' for site: '{}'.".format(fabric_id, fabric_site_name_hierarchy), "INFO")
        return fabric_id

    def validate_device_in_fabric(self, ip_address):
        """
        Validates whether a device with the given IP address is provisioned in a Fabric site.
        Args:
            ip_address (str): The management IP address of the device to be validated.
        """
        self.log("Constructing parameters for 'get_device_info' API call.", "DEBUG")
        get_device_info_from_fabric_params = {
            "device_management_ip_address": ip_address,
        }

        self.log("Executing 'get_device_info' API call with parameters: {}".format(get_device_info_from_fabric_params), "DEBUG")
        response = self.execute_get_request("sda", "get_device_info", get_device_info_from_fabric_params)
        if response.get("status") != "success" and "Fabric device info successfully retrieved from sda fabric" not in response.get("description"):
            self.msg = "Device: '{0}' is not provisioned in a Fabric site.".format(ip_address)
            self.fail_and_exit(self.msg)

    def get_port_assignments_params(self, network_device_id, fabric_id):
        """
        Generates parameters for retrieving port assignments based on network device ID and fabric ID.
        Args:
            network_device_id (str): The ID of the network device.
            fabric_id (str): The ID of the fabric.
        Returns:
            dict: A dictionary containing the parameters 'fabric_id' and 'network_device_id'.
        Description:
            This method creates a dictionary with 'fabric_id' and 'network_device_id' parameters required
            for retrieving port assignments. It logs the generated parameters for debugging purposes and
            returns the dictionary.
        """
        # Create dictionary with required parameters
        get_port_assignment_params = {
            "fabric_id": fabric_id,
            "network_device_id": network_device_id,
        }

        self.log("Generated get_port_assignments_params: {0}".format(get_port_assignment_params), "DEBUG")

        return get_port_assignment_params

    def get_port_assignments(self, get_port_assignments_params):
        """
        Retrieves port assignments from Cisco Catalyst Center using the given parameters.
        Args:
            get_port_assignments_params (dict): Parameters for querying port assignments, including fabric ID and network device ID.
        Returns:
            list: A list of port assignments retrieved from the API.
        Description:
            This method retrieves port assignments from Cisco Catalyst Center by executing the 'get_port_assignments' API call.
            It uses pagination with offset and limit to handle large datasets. The method logs relevant information and returns
            the list of port assignments. If an error occurs during the API call, it logs an error message and sets the validation
            status to "failed".
        """
        try:
            offset = 1
            limit = 500
            port_assignments = []

            while True:
                try:
                    # Update offset and limit in the parameters
                    get_port_assignments_params.update({
                        "offset": offset,
                        "limit": limit
                    })

                    self.log("Updated 'get_port_assignments_params' with offset and limit: {0} ".format(get_port_assignments_params), "INFO")

                    # Execute the API call to get port assignments
                    response = self.dnac._exec(
                        family="sda",
                        function="get_port_assignments",
                        op_modifies=False,
                        params=get_port_assignments_params,
                    )

                    # Process the response if available
                    response = response.get("response")
                    if not response:
                        self.log(
                            "Exiting the loop because no port assignments were returned after increasing the offset. "
                            "Current offset: {0}".format(offset),
                            "INFO"
                        )
                        break

                    port_assignments.extend(response)
                    offset += limit

                except Exception as e:
                    self.msg = (
                        "An error occurred during iteration while retrieving Port Assignment Details: '{0}' using SDA - "
                        "'get_port_assignments' API call: {1}".format(get_port_assignments_params, str(e))
                    )
                    self.fail_and_exit(self.msg)

            if port_assignments:
                self.log("Port Assignment Details: {0}".format(port_assignments), "DEBUG")
            else:
                self.log("No port assignments found.", "DEBUG")

            return port_assignments

        except Exception as e:
            # Log an error message and fail if an exception occurs
            self.msg = (
                "An error occurred while retrieving Port Assignment Details: '{0}' using SDA - "
                "'get_port_assignments' API call: {1}".format(get_port_assignments_params, str(e))
            )
            self.fail_and_exit(self.msg)

    def check_differences(self, existing_port, requested_port):
        """
        Checks for differences between existing and requested port assignments.
        Args:
            existing_port (dict): The existing port assignment details.
            requested_port (dict): The requested port assignment details.
        Returns:
            bool: True if there are differences, False otherwise.
        """
        comparison_fields = [
            ("interfaceName", "interface_name"),
            ("connectedDeviceType", "connected_device_type"),
            ("authenticateTemplateName", "authentication_template_name"),
            ("dataVlanName", "data_vlan_name"),
            ("voiceVlanName", "voice_vlan_name"),
            ("interfaceDescription", "interface_description"),
            ("securityGroupName", "security_group_name")
        ]

        for existing_field, requested_field in comparison_fields:
            if existing_field == "authenticateTemplateName":
                if existing_port.get("authenticateTemplateName") == "No Authentication" and not requested_port.get("authentication_template_name"):
                    continue
                if not existing_port.get("authenticateTemplateName") and requested_port.get("authentication_template_name") == "No Authentication":
                    continue

            if existing_field == "interfaceDescription":
                if existing_port.get("interfaceDescription") == "" and not requested_port.get("interface_description"):
                    continue
                if not existing_port.get("interfaceDescription") and requested_port.get("interface_description") == "":
                    continue
                if existing_port.get("interfaceDescription") and not requested_port.get("interface_description"):
                    continue

            if existing_field in existing_port or requested_field in requested_port:
                if existing_field in existing_port and requested_field in requested_port:
                    if existing_port[existing_field] != requested_port[requested_field]:
                        return True
                else:
                    return True

        return False

    def compare_port_assignments(self, get_port_assignments_params, requested_port_assignment_details):
        """
        Compares existing port assignments with requested port assignments to determine required actions.
        Args:
            get_port_assignments_params (dict): Parameters for querying existing port assignments.
            requested_port_assignment_details (list): List of requested port assignment details.
        Returns:
            tuple: A tuple containing three lists:
                - create_port_assignments (list): List of port assignments to be created.
                - update_port_assignments (list): List of port assignments to be updated.
                - no_update_port_assignments (list): List of port assignments that do not need updates.
        Description:
            This method compares existing port assignments retrieved from Cisco Catalyst Center with the requested
            port assignment details. It categorizes the port assignments into those that need to be created, updated,
            or do not require any updates. The method logs relevant information and returns the categorized lists.
        """
        existing_port_assignment_details = self.get_port_assignments(get_port_assignments_params)

        self.log("Existing Port assignments: {0}".format(existing_port_assignment_details), "DEBUG")
        self.log("Requested Port assignments: {0}".format(requested_port_assignment_details), "DEBUG")

        create_port_assignments = []
        update_port_assignments = []
        no_update_port_assignments = []

        # Convert the requested_port_assignment_details to a dictionary for quick lookup
        requested_ports_dict = {port['interface_name']: port for port in requested_port_assignment_details}

        if not existing_port_assignment_details:
            self.log("Port assignments that need to be CREATED: {0} - {1}".format(len(create_port_assignments), create_port_assignments), "DEBUG")
            create_port_assignments.extend(requested_ports_dict.values())
            return create_port_assignments, update_port_assignments, no_update_port_assignments

        # Iterate over existing ports to find matches and differences
        for existing_port in existing_port_assignment_details:
            interface_name = existing_port['interfaceName']
            # If the interface exists in both, compare fields

            if interface_name in requested_ports_dict:
                requested_port = requested_ports_dict[interface_name]

                # Check for differences using the new function
                has_diff = self.check_differences(existing_port, requested_port)

                if has_diff:
                    # Add the requested port with the id and relevant metadata from the existing port
                    updated_port = requested_port.copy()
                    # Copy the ID from existing port
                    updated_port["id"] = existing_port.get("id")
                    update_port_assignments.append(updated_port)
                else:
                    # If there's no difference, add to no_update_port_assignments
                    no_update_port_assignments.append(existing_port)

                # Remove the requested port from the dictionary so we know it's processed
                del requested_ports_dict[interface_name]

        # Remaining items in requested_ports_dict are new ports to be created
        create_port_assignments.extend(requested_ports_dict.values())

        # Log details of port assignments to be created, update, not updated
        self.log("Port assignments that need to be CREATED: {0} - {1}".format(len(create_port_assignments), create_port_assignments), "DEBUG")
        self.log("Port assignments that need to be UPDATED: {0} - {1}".format(len(update_port_assignments), update_port_assignments), "DEBUG")
        self.log("Port assignments that DON'T NEED UPDATES: {0} - {1}".format(len(no_update_port_assignments), no_update_port_assignments), "DEBUG")

        # Calculate total ports processed and check against requested port assignments
        total_ports_processed = len(create_port_assignments) + len(update_port_assignments) + len(no_update_port_assignments)

        if total_ports_processed == len(requested_port_assignment_details):
            self.log("Match in total counts: Processed={0}, Requested={1}.".format(total_ports_processed, len(requested_port_assignment_details)), "DEBUG")
        else:
            self.log("Mismatch in total counts: Processed={0}, Requested={1}.".format(total_ports_processed, len(requested_port_assignment_details)), "ERROR")

        # Return the categorized port assignments
        return create_port_assignments, update_port_assignments, no_update_port_assignments

    def get_port_channels_params(self, network_device_id, fabric_id):
        """
        Generates parameters for retrieving port channels based on network device ID and fabric ID.
        Args:
            network_device_id (str): The ID of the network device.
            fabric_id (str): The ID of the fabric.
        Returns:
            dict: A dictionary containing the parameters 'fabric_id' and 'network_device_id'.
        Description:
            This method creates a dictionary with 'fabric_id' and 'network_device_id' parameters required
            for retrieving port channels. It logs the generated parameters for debugging purposes and
            returns the dictionary.
        """
        # Create a dictionary with the required parameters
        get_port_channels_params = {
            "fabric_id": fabric_id,
            "network_device_id": network_device_id,
        }

        self.log("get_port_channels_params: {0}".format(get_port_channels_params), "DEBUG")
        return get_port_channels_params

    def get_port_channels(self, get_port_channels_params):
        """
        Retrieves port channels from Cisco Catalyst Center using the given parameters.
        Args:
            get_port_channels_params (dict): Parameters for querying port channels, including fabric ID and network device ID.
        Returns:
            list: A list of port channels retrieved from the API.
        Description:
            This method retrieves port channels from Cisco Catalyst Center by executing the 'get_port_channels' API call.
            It uses pagination with offset and limit to handle large datasets. The method logs relevant information and returns
            the list of port channels. If an error occurs during the API call, it logs an error message and sets the validation
            status to "failed".
        """
        try:
            offset = 1
            limit = 500
            port_channels = []

            while True:
                try:
                    # Update offset and limit in the parameters
                    get_port_channels_params.update({
                        "offset": offset,
                        "limit": limit
                    })

                    # Execute the API call to get port channels
                    response = self.dnac._exec(
                        family="sda",
                        function="get_port_channels",
                        op_modifies=False,
                        params=get_port_channels_params,
                    )

                    # Process the response if available
                    response = response.get("response")
                    if not response:
                        self.log(
                            "Exiting the loop because no port channels were returned after increasing the offset. "
                            "Current offset: {0}".format(offset),
                            "INFO"
                        )
                        break

                    port_channels.extend(response)
                    offset += limit

                except Exception as e:
                    self.msg = (
                        "An error occurred during iteration while retrieving Port Channel Details: '{0}' using "
                        "SDA - 'get_port_channels' API call: {1}".format(get_port_channels_params, str(e))
                    )
                    self.fail_and_exit(self.msg)

            if port_channels:
                self.log("Port Channel Details: {0}".format(port_channels), "DEBUG")
            else:
                self.log("No port channels found.", "DEBUG")

            return port_channels

        except Exception as e:
            # Log an error message and fail if an exception occurs
            self.msg = (
                "An error occurred while retrieving Port Channel Details: '{0}' using SDA - "
                "'get_port_channels' API call: {1}".format(get_port_channels_params, str(e))
            )
            self.fail_and_exit(self.msg)

    def get_add_port_assignments_params(self):
        """
        Generates parameters for adding port assignments based on the current configuration.
        Returns:
            dict: A dictionary containing the payload for adding port assignments.
        Description:
            This method creates the parameters required for adding port assignments by iterating over the list of
            interfaces to be created. It maps the relevant fields from the configuration and constructs the payload
            for the API call. The method logs the generated parameters for debugging purposes and returns the dictionary.
        """
        self.log("Starting to generate parameters for add port assignments.", "DEBUG")

        create_port_assignments = self.have.get("create_port_assignments")
        parameter_mapping = {
            "dataVlanName": "data_vlan_name",
            "voiceVlanName": "voice_vlan_name",
            "authenticateTemplateName": "authentication_template_name",
            "securityGroupName": "security_group_name",
            "interfaceDescription": "interface_description",
        }

        interface_params_list = []
        for interface in create_port_assignments:
            interface_params = {
                "fabricId": self.have.get("fabric_id"),
                "networkDeviceId": self.have.get("network_device_id"),
                "interfaceName": interface.get("interface_name"),
                "connectedDeviceType": interface.get("connected_device_type").upper(),
            }

            self.log("Basic parameters for interface {0}: {1}".format(interface.get("interface_name"), interface_params), "DEBUG")

            # Iterate over the parameters and add them to the result dictionary if present in the config
            for parameter, parameter_name in parameter_mapping.items():
                if interface.get(parameter_name):
                    interface_params[parameter] = interface.get(parameter_name)

            # if interface.get("connected_device_type") == "TRUNKING_DEVICE" and not interface.get("authentication_template_name"):
            if not interface.get("authentication_template_name"):
                interface_params["authenticateTemplateName"] = "No Authentication"
            interface_params_list.append(interface_params)
            self.log("Generated parameters for interface: {0}".format(interface_params), "DEBUG")

        add_port_assignments_params = {"payload": interface_params_list}
        self.log("Final add_port_assignments_params: {0}".format(add_port_assignments_params), "DEBUG")
        return add_port_assignments_params

    def get_update_port_assignments_params(self):
        """
        Generates parameters for updating port assignments based on the current configuration.
        Returns:
            dict: A dictionary containing the payload for updating port assignments.
        Description:
            This method creates the parameters required for updating port assignments by iterating over the list of
            interfaces to be updated. It maps the relevant fields from the configuration and constructs the payload
            for the API call. The method logs the generated parameters for debugging purposes and returns the dictionary.
        """
        self.log("Starting to generate parameters for updating port assignments.", "DEBUG")

        update_port_assignments = self.have.get("update_port_assignments")
        parameters_mapping = {
            "dataVlanName": "data_vlan_name",
            "voiceVlanName": "voice_vlan_name",
            "authenticateTemplateName": "authentication_template_name",
            "securityGroupName": "security_group_name",
            "interfaceDescription": "interface_description"
        }

        interface_params_list = []
        for interface in update_port_assignments:
            interface_params = {
                "id": interface.get("id"),
                "fabricId": self.have.get("fabric_id"),
                "networkDeviceId": self.have.get("network_device_id"),
                "interfaceName": interface.get("interface_name"),
                "connectedDeviceType": interface.get("connected_device_type").upper()
            }

            self.log("Basic parameters for interface {0}: {1}".format(interface.get("interface_name"), interface_params), "DEBUG")

            # Iterate over the parameters and add them to the result dictionary if present in the config
            for parameter, parameter_name in parameters_mapping.items():
                if interface.get(parameter_name):
                    interface_params[parameter] = interface.get(parameter_name)

            self.log("Updated parameters with VLAN and security info for interface {0}: {1}".format(interface.get("interface_name"), interface_params), "DEBUG")

            if interface.get("connected_device_type") == "TRUNKING_DEVICE":
                interface_params["authenticateTemplateName"] = "No Authentication"
                self.log("TRUNKING_DEVICE detected for interface: {0}. Setting 'No Authentication'.".format(interface.get("interface_name")), "DEBUG")
            interface_params_list.append(interface_params)
            self.log("Generated parameters for interface: {0}".format(interface_params), "DEBUG")

        update_port_assignments_params = {"payload": interface_params_list}
        self.log("Final update_port_assignments_params: {0}".format(update_port_assignments_params), "DEBUG")
        return update_port_assignments_params

    def get_delete_port_assignments_params(self, port_assignment_details, network_device_id, fabric_id):
        """
        Generates parameters for deleting port assignments based on the given details.
        Args:
            port_assignment_details (list): List of port assignment details to be deleted.
            network_device_id (str): The ID of the network device.
            fabric_id (str): The ID of the fabric.
        Returns:
            list: A list of dictionaries containing the parameters for deleting port assignments.
        Description:
            This method creates the parameters required for deleting port assignments by iterating over the list of
            port assignment details. It constructs the necessary parameters, including 'fabric_id', 'network_device_id',
            'interface_name', 'data_vlan_name', and 'voice_vlan_name'. The method logs the generated parameters for
            debugging purposes and returns the list of dictionaries.
        """
        self.log("Generating parameters for deleting port assignments. Details: {0}".format(port_assignment_details), "DEBUG")
        delete_port_assignments_params_list = []

        if not port_assignment_details:
            self.log("No port_assignment_details provided. delete_port_assignments_params_list: {0}"
                     .format(delete_port_assignments_params_list), "INFO")
            return delete_port_assignments_params_list

        for delete_param in port_assignment_details:
            delete_port_assignments_params = {
                "fabric_id": fabric_id,
                "network_device_id": network_device_id,
            }

            # Directly iterate over the keys of delete_param
            for parameter in ["interface_name", "data_vlan_name", "voice_vlan_name"]:
                if delete_param.get(parameter):
                    delete_port_assignments_params[parameter] = delete_param.get(parameter)

            delete_port_assignments_params_list.append(delete_port_assignments_params)

        self.log("Generated delete_port_assignments_params_list: {0}".format(delete_port_assignments_params_list), "DEBUG")
        return delete_port_assignments_params_list

    def compare_port_channels(self, get_port_channels_params, requested_port_channels_details):
        """
        Compares existing port channels with requested port channels to determine required actions.
        Args:
            get_port_channels_params (dict): Parameters for querying existing port channels.
            requested_port_channels_details (list): List of requested port channel details.
        Returns:
            tuple: A tuple containing three lists:
                - create_port_channels (list): List of port channels to be created.
                - update_port_channels (list): List of port channels to be updated.
                - no_update_port_channels (list): List of port channels that do not need updates.
        Description:
            This method compares existing port channels retrieved from Cisco Catalyst Center with the requested
            port channel details. It categorizes the port channels into those that need to be created, updated,
            or do not require any updates. The method logs relevant information and returns the categorized lists.
        """
        self.log("Fetching existing port channels using params: {0}".format(get_port_channels_params), "INFO")
        existing_port_channel_details = self.get_port_channels(get_port_channels_params)

        self.log("Existing Port Channels: {0}".format(existing_port_channel_details), "DEBUG")
        self.log("Requested Port Channels: {0}".format(requested_port_channels_details), "DEBUG")

        create_port_channels = []
        update_port_channels = []
        no_update_port_channels = []

        # Handle the case where there are no existing port channels
        if not existing_port_channel_details:
            create_port_channels = requested_port_channels_details
            self.log("No existing port channels found. All requested port channels will be created.", "INFO")
            self.log("Port channels that need to be CREATED: {0} - {1}".format(len(create_port_channels), create_port_channels), "DEBUG")
            return create_port_channels, update_port_channels, no_update_port_channels

        # Define the comparison fields within the function
        comparison_fields = [
            ("connectedDeviceType", "connected_device_type"),
            ("protocol", "protocol"),
            ("description", "port_channel_description")
        ]

        value_options = ["", "None", None]

        for requested_channel in requested_port_channels_details:
            self.log("Processing requested port channel: {0}".format(requested_channel), "DEBUG")
            matched = False
            update_needed = False
            updated_channel = {}

            for existing_channel in existing_port_channel_details:
                self.log("Comparing with existing port channel: {0}".format(existing_channel), "DEBUG")

                requested_interfaces = set(requested_channel["interface_names"])
                existing_interfaces = set(existing_channel["interfaceNames"])
                intersection = requested_interfaces & existing_interfaces

                # Compare sets of interface names
                if intersection:
                    self.log("Match found based on interface names: {0}".format(intersection), "DEBUG")

                    matched = True
                    updated_channel = {
                        "id": existing_channel["id"],
                        "port_channel_name": existing_channel["portChannelName"]
                    }

                    if requested_interfaces != existing_interfaces:  # Partial match
                        update_needed = True
                        self.log(
                            "Interface mismatch: Requested={0}, Existing={1}".format(
                                requested_interfaces, existing_interfaces
                            ),
                            "DEBUG",
                        )

                    for existing_field, req_field in comparison_fields:
                        req_value = requested_channel.get(req_field)
                        existing_value = existing_channel.get(existing_field)

                        self.log("Requested Field: {0}".format(req_field))
                        self.log("Existing Field: {0}".format(existing_field))
                        self.log("Comparing field '{0}': Requested={1}, Existing={2}".format(req_field, req_value, existing_value), "DEBUG")

                        # Handle protocol conditions
                        if req_field == "protocol":
                            if req_value is True:
                                req_value = "ON"
                            elif req_value is None:
                                req_value = existing_value
                            update_protocol = req_value.upper()

                            # Raise an error if protocol is being changed
                            if update_protocol != existing_value:
                                self.log(
                                    "Protocol update not allowed. Attempted to update from {0} to {1}. Exiting.".format(
                                        existing_value, update_protocol
                                    ),
                                    "ERROR",
                                )
                                self.msg = (
                                    "Port Channel: {0} Protocol update is not allowed. "
                                    "Requested: {1}, Existing: {2}"
                                ).format(
                                    existing_channel["portChannelName"], req_value, existing_value
                                )
                                self.fail_and_exit(self.msg)

                        # Handle connected device type conditions
                        if req_field == "connected_device_type":
                            if existing_value == "TRUNK" and req_value == "EXTENDED_NODE" and existing_channel.get("protocol") != "PAGP":
                                self.log("Connected device type change from TRUNK to EXTENDED_NODE not allowed unless protocol is PAGP. Exiting.", "ERROR")
                                self.msg = (
                                    "Port Channel: {0} Cannot change connected_device_type from TRUNK to EXTENDED_NODE unless protocol is PAGP. "
                                    "Requested: {1}, Existing: {2}, Protocol: {3}"
                                ).format(
                                    existing_channel["portChannelName"], req_value, existing_value, existing_channel.get("protocol")
                                )
                                self.fail_and_exit(self.msg)

                        # Handle description specific conditions
                        if req_value in value_options and existing_value in value_options:
                            self.log("Skipping update check for field '{0}' as both values are empty or None".format(req_field), "DEBUG")
                            continue

                        if req_value != existing_value:
                            self.log("Update needed for {0} - Requested: {1}, Existing: {2}".format(req_field, req_value, existing_value), "DEBUG")
                            updated_channel[existing_field] = req_value
                            update_needed = True

                    if update_needed:
                        # Ensure all necessary fields are included in the updated_channel dictionary
                        updated_channel.update({
                            "interface_names": requested_channel.get("interface_names"),
                            "connected_device_type": requested_channel.get("connected_device_type"),
                            "protocol": update_protocol,
                            "port_channel_description": requested_channel.get("port_channel_description")
                        })
                        self.log("Port channel marked for UPDATE: {0}".format(updated_channel), "INFO")
                        update_port_channels.append(updated_channel)
                    else:
                        self.log("No update needed for port channel: {0}".format(existing_channel), "INFO")
                        no_update_port_channels.append(existing_channel)
                    break

            if not matched:
                self.log("Port channel marked for CREATION: {0}".format(requested_channel), "DEBUG")
                create_port_channels.append(requested_channel)

        # Add logging for created, updated, and no-update port channels
        self.log("Port channels that need to be CREATED: {0} - {1}".format(len(create_port_channels), create_port_channels), "DEBUG")
        self.log("Port channels that need to be UPDATED: {0} - {1}".format(len(update_port_channels), update_port_channels), "DEBUG")
        self.log("Port channels that DON'T NEED UPDATES: {0} - {1}".format(len(no_update_port_channels), no_update_port_channels), "DEBUG")

        # Check total ports processed
        total_ports_processed = len(create_port_channels) + len(update_port_channels) + len(no_update_port_channels)
        if total_ports_processed == len(requested_port_channels_details):
            self.log("Match in total counts: Processed={0}, Requested={1}.".format(total_ports_processed, len(requested_port_channels_details)), "DEBUG")
        else:
            self.log("Mismatch in total counts: Processed={0}, Requested={1}.".format(total_ports_processed, len(requested_port_channels_details)), "ERROR")

        # return the categorized port channels
        return create_port_channels, update_port_channels, no_update_port_channels

    def update_protocol(self, protocol, connected_device_type):
        """
        Updates the protocol based on the connected device type.
        Args:
            protocol (str or bool): The protocol to be validated and updated.
            connected_device_type (str): The type of the connected device.
        Returns:
            str: The updated protocol value in uppercase.
        Description:
            This method updates the protocol based on the connected device type. If the protocol is True,
            it sets it to "ON". If no protocol is provided, it defaults to "ON" for TRUNK and "PAGP" for
            EXTENDED_NODE. The method returns the protocol in uppercase.
        """
        connected_device_type = connected_device_type.upper()
        if protocol:
            if protocol is True:
                protocol = "ON"
                self.log("Protocol is set to True, updating 'protocol' to 'ON'.", "INFO")

        else:
            self.log("Protocol not provided, hence using default protocol values based on the 'connected_device_type'.", "INFO")
            self.log("The default protocol for each 'connected_device_type': 'TRUNK' -> 'ON', 'EXTENDED_NODE' -> 'PAGP'", "INFO")
            # Default protocol for TRUNK -> "ON"
            if connected_device_type == "TRUNK":
                protocol = "ON"
                self.log("Connected device type is 'TRUNK', setting protocol to 'ON'.", "INFO")
            # Default protocol for EXTENDED_NODE -> "PAGP"
            elif connected_device_type == "EXTENDED_NODE":
                protocol = "PAGP"
                self.log("Connected device type is 'EXTENDED_NODE', setting protocol to 'PAGP'.", "INFO")

        updated_protocol = protocol.upper()
        self.log("Updated 'protocol' is: {0}".format(updated_protocol), "INFO")
        return updated_protocol

    def get_add_port_channels_params(self):
        """
        Generates parameters for adding port channels based on the current configuration.
        Returns:
            dict: A dictionary containing the payload for adding port channels.
        Description:
            This method creates the parameters required for adding port channels by iterating over the list of
            port channels to be created. It maps the relevant fields from the configuration and constructs the
            payload for the API call. The method logs the generated parameters for debugging purposes and returns
            the dictionary.
        """
        # Retrieve the list of port channels to be created from the current configuration
        create_port_channels = self.have.get("create_port_channels")

        port_channels_params_list = []
        for port_channel in create_port_channels:
            protocol = port_channel.get("protocol")
            connected_device_type = port_channel.get("connected_device_type")
            port_channel_description = port_channel.get("port_channel_description")

            # Construct the parameters for each port channel
            port_channel_params = {
                "fabricId": self.have.get("fabric_id"),
                "networkDeviceId": self.have.get("network_device_id"),
                "interfaceNames": port_channel.get("interface_names"),
                "connectedDeviceType": connected_device_type.upper(),
                "protocol": self.update_protocol(protocol, connected_device_type)
            }

            # Add description if available
            if port_channel_description:
                port_channel_params["description"] = port_channel_description

            port_channels_params_list.append(port_channel_params)
            self.log("Constructed parameters for port channel: {0}".format(port_channel_params), "DEBUG")

        # Create the final payload for adding port channels
        add_port_channels_params = {"payload": port_channels_params_list}
        self.log("Final add_port_channels_params: {0}".format(add_port_channels_params), "DEBUG")
        return add_port_channels_params

    def get_update_port_channels_params(self):
        """
        Generates parameters for updating port channels based on the current configuration.
        Returns:
            dict: A dictionary containing the payload for updating port channels.
        Description:
            This method creates the parameters required for updating port channels by iterating over the list of
            port channels to be updated. It maps the relevant fields from the configuration and constructs the
            payload for the API call. The method logs the generated parameters for debugging purposes and returns
            the dictionary.
        """
        update_port_channels = self.have.get("update_port_channels")

        port_channels_params_list = []
        for port_channel in update_port_channels:
            protocol = port_channel.get("protocol")
            connected_device_type = port_channel.get("connected_device_type")
            port_channel_description = port_channel.get("port_channel_description")

            # Construct the parameters for each port channel
            port_channel_params = {
                "fabricId": self.have.get("fabric_id"),
                "networkDeviceId": self.have.get("network_device_id"),
                "id": port_channel.get("id"),
                "portChannelName": port_channel.get("port_channel_name"),
                "interfaceNames": port_channel.get("interface_names"),
                "connectedDeviceType": connected_device_type,
                "protocol": self.update_protocol(protocol, connected_device_type)
            }

            # Add description if available
            if port_channel_description:
                port_channel_params["description"] = port_channel_description

            port_channels_params_list.append(port_channel_params)
            self.log("Constructed parameters for updating port channel: {0}".format(port_channel_params), "DEBUG")

        # Create the final payload for updating port channels
        update_port_channels_params = {"payload": port_channels_params_list}
        self.log("Final update_port_channels_params: {0}".format(update_port_channels_params), "DEBUG")
        return update_port_channels_params

    def get_delete_port_channels_params(self, port_channel_details, get_port_channels_params):
        """
        Generates parameters for deleting port channels based on the given details.
        Args:
            port_channel_details (list): List of port channel details to be deleted.
            get_port_channels_params (dict): Parameters to retrieve existing port channels.
        Returns:
            dict: A dictionary containing the parameters for deleting port channels indexed by input list index.
        Description:
            This method creates the parameters required for deleting port channels by iterating over the list of
            port channel details. It constructs the necessary parameters, including 'fabric_id', 'network_device_id',
            and 'port_channel_name'. The method logs the generated parameters for debugging purposes and returns
            the dictionary of results.
        """
        results = {}

        existing_port_channel_details = self.get_port_channels(get_port_channels_params)
        self.log("Existing Port Channels: {0}".format(existing_port_channel_details), "DEBUG")

        # Check if existing port channels is None
        if not existing_port_channel_details:
            self.log("No existing port channels found. Delete operation is not required.", "INFO")
            return results

        # If no port_channel_details are provided, prepare to delete all existing port channels
        if not port_channel_details:
            self.log("No 'port_channel_details' provided. Checking for all existing port assignments.", "INFO")

            port_channels_list = [port_channel.get("portChannelName") for port_channel in existing_port_channel_details]
            self.log("No specific port channel details provided. Preparing params to delete all existing port channels.", "INFO")
            self.log("List of port channels to be deleted: {}".format(port_channels_list), "DEBUG")
            self.log("Deleting all port assignments with psarams: {}".format(get_port_channels_params), "INFO")
            results[0] = {
                "delete_port_channel_params": get_port_channels_params,
                "port_channels_list": port_channels_list
            }
            return results

        for index, requested_channel in enumerate(port_channel_details):
            self.log("Processing requested channel at index {0}: {1}".format(index, requested_channel), "DEBUG")

            requested_interfaces = set(requested_channel.get("interface_names", []))
            self.log("Requested interfaces at index {0}: {1}".format(index, requested_interfaces), "DEBUG")

            # delete_required = False
            port_channels_list = []

            for existing_channel in existing_port_channel_details:
                self.log("Comparing with existing channel: {0}".format(existing_channel), "DEBUG")

                existing_interfaces = set(existing_channel.get("interfaceNames", []))
                self.log("Existing interfaces: {0}".format(existing_interfaces), "DEBUG")

                # Compare sets of interface names
                if requested_interfaces == existing_interfaces:
                    port_channel_name = existing_channel["portChannelName"]
                    self.log("Match found for requested channel at index {0} with existing channel: {1}".format(index, port_channel_name), "DEBUG")

                    delete_port_channel_params = {
                        "fabric_id": get_port_channels_params.get("fabric_id"),
                        "network_device_id": get_port_channels_params.get("network_device_id"),
                        "port_channel_name": port_channel_name
                    }
                    # delete_required = True
                    port_channels_list.append(port_channel_name)

                    results[index] = {
                        # "delete_required": delete_required,
                        "delete_port_channel_params": delete_port_channel_params,
                        "port_channels_list": port_channels_list
                    }

                    # Stop after finding the first match
                    break
                else:
                    self.log("Port channel: {0} not found in the Cisco Catalyst Center and hence delete not required.", "INFO")

        self.log("Result generated post verifying if delete port channels is required: {0}".format(results), "DEBUG")
        return results

    def get_vlans_and_ssids_mapped_to_vlans(self, fabric_id):
        """
        Retrieves and returns the VLANs and SSIDs mapped to VLANs within a specified fabric site.
        Args:
            fabric_id (str): The identifier of the fabric site for which VLAN and SSID mappings are to be retrieved.
        Returns:
            list: A list of dictionaries containing details of VLANs and SSIDs mapped to VLANs within the specified fabric site.
        Description:
            This method interacts with the DNA Center API to fetch information about VLANs and SSIDs mapped to VLANs within a given fabric site.
            It uses pagination to handle large datasets by iteratively updating the offset and limit parameters for the API call.
            If the response indicates that no more data is available, the loop exits.
            Logs detailed information about the process and handles any exceptions that may occur, ensuring that errors are logged and the process
            is terminated gracefully if necessary.
        """
        api_family = "fabric_wireless"
        api_function = "retrieve_the_vlans_and_ssids_mapped_to_the_vlan_within_a_fabric_site"
        get_vlans_and_ssids_mapped_to_vlans_params = {"fabric_id": fabric_id}
        try:
            offset = 1
            limit = 500
            vlans_and_ssids_mapped_to_vlans = []

            while True:
                try:
                    # Update offset and limit in the parameters
                    get_vlans_and_ssids_mapped_to_vlans_params.update({
                        "offset": offset,
                        "limit": limit
                    })

                    self.log(
                        "Updated 'get_vlans_and_ssids_mapped_to_vlans_params' with offset and limit: {}".format(
                            get_vlans_and_ssids_mapped_to_vlans_params
                        ),
                        "INFO"
                    )

                    # Execute the API call to get vlans and ssids mapped to the vlan
                    response = self.dnac._exec(
                        family=api_family,
                        function=api_function,
                        fabric_id=fabric_id,
                        op_modifies=False,
                        params=get_vlans_and_ssids_mapped_to_vlans_params,
                    )

                    # Process the response if available
                    response = response.get("response")
                    if not response:
                        self.log(
                            "Exiting the loop because no VLANs and SSIDs mapped to VLANs were returned after increasing the offset. "
                            "Current offset: {0}".format(offset),
                            "INFO"
                        )
                        break

                    vlans_and_ssids_mapped_to_vlans.extend(response)
                    offset += limit

                except Exception as e:
                    self.msg = (
                        "An error occurred during iteration while retrieving VLANs and SSIDs "
                        "mapped to VLANs. Details: '{0}' using SDA - "
                        "'retrieve_the_vlans_and_ssids_mapped_to_the_vlan_within_a_fabric_site' "
                        "API call: {1}".format(get_vlans_and_ssids_mapped_to_vlans_params, str(e))
                    )
                    self.fail_and_exit(self.msg)

            if vlans_and_ssids_mapped_to_vlans:
                self.log("VLANs and SSIDs mapped to VLANs Details: {0}".format(vlans_and_ssids_mapped_to_vlans), "DEBUG")
            else:
                self.log("No VLANs and SSIDs mapped to VLANs found.", "DEBUG")

            return vlans_and_ssids_mapped_to_vlans

        except Exception as e:
            # Log an error message and fail if an exception occurs
            self.msg = (
                "An error occurred while retrieving VLANs and SSIDs mapped to VLANs "
                "Details using SDA - 'retrieve_the_vlans_and_ssids_mapped_to_the_vlan_within_a_fabric_site' "
                "API call: {0} for Fabric ID: {1}. Error: {2}".format(
                    get_vlans_and_ssids_mapped_to_vlans_params, fabric_id, str(e)
                )
            )
            self.fail_and_exit(self.msg)

    def compare_vlans_and_ssids_mapped_to_vlans(self, fabric_name, fabric_id, wireless_ssids_details):
        """
        Compares existing VLANs and SSIDs mapped to VLANs with the provided details,
        identifies which ones need to be created or updated, and which ones dont need updates.
        Args:
            fabric_id (str): The ID of the fabric site.
            wireless_ssids_details (list): A list of dictionaries containing the SSID details provided by the user.
        Returns:
            tuple: Three dictionaries - one for VLANs/SSIDs that need to be created, one for those that need to be updated, and one for
            those that dont need updates.
        """
        # Initialize dictionaries for VLANs/SSIDs that need to be created, updated or dont need updates.
        self.log("Starting VLAN and SSID comparison for fabric: {0} fabric_id: {1}".format(fabric_name, fabric_id), "DEBUG")

        create_vlans_and_ssids_mapped_to_vlans = {}
        update_vlans_and_ssids_mapped_to_vlans = {}
        no_update_vlans_and_ssids_mapped_to_vlans = {}

        # Retrieve existing VLANs and SSIDs mapped to VLANs from the fabric site.
        existing_vlans_and_ssids_mapped_to_vlans = self.get_vlans_and_ssids_mapped_to_vlans(fabric_id)

        # Create a copy of the existing details to be modified.
        updated_vlans_and_ssids = [vlan.copy() for vlan in existing_vlans_and_ssids_mapped_to_vlans]

        # Create a dictionary for quick lookup of existing VLANs and their SSIDs.
        existing_vlans_dict = {vlan['vlanName']: vlan for vlan in existing_vlans_and_ssids_mapped_to_vlans}

        # Iterate through the provided SSID details.
        for ssid_detail in wireless_ssids_details:
            vlan_name = ssid_detail['vlan_name']
            ssid_details = ssid_detail['ssid_details']

            self.log("Processing VLAN: {0}, with SSID details: {1}".format(vlan_name, ssid_details), "DEBUG")
            # Check if the VLAN exists in the existing details.
            if vlan_name in existing_vlans_dict:
                self.log("VLAN '{}' exists. Checking associated SSIDs.".format(vlan_name), "DEBUG")

                existing_ssids = existing_vlans_dict[vlan_name]['ssidDetails']
                self.log("Existing SSIDs for VLAN '{0}': {1}".format(vlan_name, existing_ssids), "DEBUG")

                existing_ssids_dict = {ssid['name']: ssid for ssid in existing_ssids}

                for ssid in ssid_details:
                    ssid_name = ssid['ssid_name']
                    security_group_name = ssid.get('security_group_name')

                    if ssid_name in existing_ssids_dict:
                        self.log("SSID '{0}' exists under VLAN '{1}'. Checking for updates.".format(ssid_name, vlan_name), "DEBUG")
                        # Check if the SSID details need to be updated.
                        existing_ssid = existing_ssids_dict[ssid_name]
                        if existing_ssid.get('securityGroupTag') != security_group_name:
                            # Update needed
                            self.log("Update required for SSID '{0}'. Updating securityGroupTag to '{1}'.".format(ssid_name, security_group_name), "DEBUG")
                            existing_ssid['securityGroupTag'] = security_group_name
                            if vlan_name not in update_vlans_and_ssids_mapped_to_vlans:
                                update_vlans_and_ssids_mapped_to_vlans[vlan_name] = []
                            update_vlans_and_ssids_mapped_to_vlans[vlan_name].append(ssid)
                        else:
                            # No update needed
                            self.log("No update required for SSID '{}'.".format(ssid_name), "DEBUG")
                            if vlan_name not in no_update_vlans_and_ssids_mapped_to_vlans:
                                no_update_vlans_and_ssids_mapped_to_vlans[vlan_name] = []
                            no_update_vlans_and_ssids_mapped_to_vlans[vlan_name].append(ssid)
                    else:
                        # New SSID needs to be added
                        existing_ssids.append({'name': ssid_name, 'securityGroupTag': security_group_name})
                        if vlan_name not in create_vlans_and_ssids_mapped_to_vlans:
                            create_vlans_and_ssids_mapped_to_vlans[vlan_name] = []
                        create_vlans_and_ssids_mapped_to_vlans[vlan_name].append(ssid)
            else:
                # If the VLAN does not exist, add it to the copy.
                self.log("VLAN '{0}' does not exist. Adding new VLAN and its SSIDs.".format(vlan_name), "DEBUG")
                new_vlan_entry = {
                    'vlanName': vlan_name,
                    'ssidDetails': [{'name': ssid['ssid_name'], 'securityGroupTag': ssid.get('security_group_name')} for ssid in ssid_details]
                }
                updated_vlans_and_ssids.append(new_vlan_entry)
                if vlan_name not in create_vlans_and_ssids_mapped_to_vlans:
                    create_vlans_and_ssids_mapped_to_vlans[vlan_name] = []
                create_vlans_and_ssids_mapped_to_vlans[vlan_name].extend(ssid_details)

        self.log("Completed processing. Generated VLANs and SSID mappings.", "DEBUG")
        self.log("create_vlans_and_ssids_mapped_to_vlans: {0}".format(create_vlans_and_ssids_mapped_to_vlans), "DEBUG")
        self.log("update_vlans_and_ssids_mapped_to_vlans: {0}".format(update_vlans_and_ssids_mapped_to_vlans), "DEBUG")
        self.log("no_update_vlans_and_ssids_mapped_to_vlans: {0}".format(no_update_vlans_and_ssids_mapped_to_vlans), "DEBUG")

        # Log the updated VLANs and SSIDs details.
        self.log("Requested Details: {0}".format(updated_vlans_and_ssids))

        return (
            create_vlans_and_ssids_mapped_to_vlans,
            update_vlans_and_ssids_mapped_to_vlans,
            no_update_vlans_and_ssids_mapped_to_vlans,
            updated_vlans_and_ssids
        )

    def get_create_update_remove_vlans_and_ssids_mapped_to_vlans_params(self, create_update_remove_vlans_and_ssids_mapped_to_vlans):
        """
        Constructs and returns parameters for creating, updating, or removing VLANs and SSIDs mappings within a fabric site.
        Parameters:
            create_update_remove_vlans_and_ssids_mapped_to_vlans (list): A list containing the mappings of VLANs and SSIDs to be created, updated, or removed.
                Each item should be a dictionary with details about the VLANs and associated SSIDs.
        Returns:
            dict: A dictionary containing the parameters required for the API call to manage VLANs and SSIDs mappings within a fabric site.
                Includes the fabric ID and a payload with the desired mappings.
        Description:
            This method prepares the parameters needed for API calls that handle the creation, update, or removal of VLANs and SSIDs mappings in a
            given fabric site.
            It includes the fabric ID retrieved from the current state (`self.have`) and a payload which is either provided or set to a default structure.
            The default payload structure consists of an empty VLAN name and an empty list of SSID details if no specific mappings are provided.
        """
        self.log("Preparing parameters for create/update/remove operation on VLANs and SSIDs.", "DEBUG")

        fabric_id = self.have.get("fabric_id")
        create_update_vlans_and_ssids_mapped_to_vlans_params = {
            "fabric_id": fabric_id,
        }
        self.log("Initialized parameters with fabric_id: {0}".format(create_update_vlans_and_ssids_mapped_to_vlans_params), "DEBUG")

        if create_update_remove_vlans_and_ssids_mapped_to_vlans:
            self.log("Using provided VLAN and SSID details for payload.", "DEBUG")
            create_update_vlans_and_ssids_mapped_to_vlans_params.update(
                {"payload": create_update_remove_vlans_and_ssids_mapped_to_vlans}
            )
        else:
            self.log("No VLAN and SSID details provided. Using default empty payload.", "DEBUG")
            existing_vlans_and_ssids_mapped_to_vlans = self.get_vlans_and_ssids_mapped_to_vlans(fabric_id)

            self.log("Retrieved existing VLANs and SSIDs: {0}".format(existing_vlans_and_ssids_mapped_to_vlans), "DEBUG")

            if not existing_vlans_and_ssids_mapped_to_vlans:
                self.log("No Existing VLANs and SSIDs mapped to VLANs found. Hence delete VLANs and SSIDs operation not required")
                return {}

            # Prepare payload with existing VLANs and empty SSID details
            payload = [{"vlanName": vlan["vlanName"], "ssidDetails": []} for vlan in existing_vlans_and_ssids_mapped_to_vlans]

            create_update_vlans_and_ssids_mapped_to_vlans_params.update(
                {"payload": payload}
            )

        self.log("Final parameters prepared: {0}".format(create_update_vlans_and_ssids_mapped_to_vlans_params), "DEBUG")
        return create_update_vlans_and_ssids_mapped_to_vlans_params

    def create_update_remove_vlans_and_ssids_mapped_to_vlans(self, create_update_remove_vlans_and_ssids_mapped_to_vlans_params):
        """
        Initiates the process to add, update, or remove VLANs and SSIDs mappings within a fabric site using the provided parameters.
        Args:
            create_update_remove_vlans_and_ssids_mapped_to_vlans_params (dict): A dictionary containing the parameters required for the API call.
                This includes the fabric ID and the payload detailing the VLANs and SSIDs mappings to be modified.
        Returns:
            dict: The task ID of the API call for tracking the operation's progress and status.
        Description:
            This method logs the initiation of the operation to add, update, or delete VLAN and SSID mappings within a fabric site.
            It calls an internal method to execute a POST API call to the DNA Center's 'fabric_wireless' family, specifically targeting the
            'add_update_or_remove_ssid_mapping_to_a_vlan' function. The method is designed to handle modifications to VLAN and SSID mappings
            based on the given parameters, facilitating network configuration changes within the fabric.
        """
        self.log(
            "Initiating Add/Update/Delete of VLANs and SSIDs mapped to VLANs with parameters: {0}".format(
                create_update_remove_vlans_and_ssids_mapped_to_vlans_params
            ),
            "INFO"
        )

        return self.get_taskid_post_api_call(
            "fabric_wireless",
            "add_update_or_remove_ssid_mapping_to_a_vlan",
            create_update_remove_vlans_and_ssids_mapped_to_vlans_params
        )

    def get_create_update_vlans_and_ssids_mapped_to_vlans_task_status(self, task_id):
        """
        Retrieves the status of a task related to creating or updating VLANs and SSIDs mappings within a fabric site.
        Parameters:
            task_id (str): The identifier of the task whose status is to be retrieved.
        Returns:
            dict: A dictionary containing the status of the task, including details of VLANs and SSIDs involved in the operation.
        Description:
            This method constructs a message detailing the VLANs and SSIDs that were part of create or update operations, if any.
            It retrieves these details from the current state (`self.have`) and organizes them under specific task names.
            The method then calls an internal utility to fetch the task status using the provided task ID, along with the constructed message.
            This facilitates monitoring and logging of the operation's success or failure.
        """
        self.log("Retrieving task status for Task ID: {0}".format(task_id), "DEBUG")
        task_name = "Create/Update VLANs and SSIDs Mapped to VLANs Task"
        create_task_name = "Create VLANs and SSIDs Mapped to VLANs Task Succeeded for following VLAN(s) and SSID(s)"
        update_task_name = "Update VLANs and SSIDs Mapped to VLANs Task Succeeded for following VLAN(s) and SSID(s)"
        msg = {}

        # Retrieve the parameters for create/update vlans and ssids mapped to vlans
        create_vlans_and_ssids_mapped_to_vlans = self.have.get("create_vlans_and_ssids_mapped_to_vlans")
        update_vlans_and_ssids_mapped_to_vlans = self.have.get("update_vlans_and_ssids_mapped_to_vlans")

        self.log("Processing create VLANs and SSIDs mapped to VLANs.", "DEBUG")
        if create_vlans_and_ssids_mapped_to_vlans:
            self.log("Generating msg for CREATE - VLANs and SSIDs mapped to VLANs.", "DEBUG")
            msg[create_task_name] = {
                vlan: [ssid['ssid_name'] for ssid in ssids]
                for vlan, ssids in create_vlans_and_ssids_mapped_to_vlans.items()
            }

        if update_vlans_and_ssids_mapped_to_vlans:
            self.log("Generating msg for UPDATE - VLANs and SSIDs mapped to VLANs.", "DEBUG")
            msg[update_task_name] = {
                vlan: [ssid['ssid_name'] for ssid in ssids]
                for vlan, ssids in update_vlans_and_ssids_mapped_to_vlans.items()
            }
        self.log("Created task message: {}".format(msg), "DEBUG")

        # Retrieve and return the task status using the provided task ID
        return self.get_task_status_from_tasks_by_id(task_id, task_name, msg)

    def add_port_assignments(self, add_port_assignments_params):
        """
        Initiates the task to add port assignments.
        Args:
            add_port_assignments_params (dict): Parameters for adding port assignments.
        Returns:
            dict: The task ID from the API call.
        Description:
            This method initiates the task to add port assignments using the provided parameters and returns the task ID.
        """
        self.log("Initiating addition of port assignments with parameters: {0}".format(add_port_assignments_params), "INFO")
        return self.get_taskid_post_api_call("sda", "add_port_assignments", add_port_assignments_params)

    def update_port_assignments(self, update_port_assignments_params):
        """
        Initiates the task to update port assignments.
        Args:
            update_port_assignments_params (dict): Parameters for updating port assignments.
        Returns:
            dict: The task ID from the API call.
        Description:
            This method initiates the task to update port assignments using the provided parameters and returns the task ID.
        """
        self.log("Initiating update of port assignments with parameters: {0}".format(update_port_assignments_params), "INFO")
        return self.get_taskid_post_api_call("sda", "update_port_assignments", update_port_assignments_params)

    def verify_delete_port_assignments_requirement(self, delete_port_assignments_params_list, get_port_assignments_params):
        """
        Verifies the requirement for deleting port assignments.
        Args:
            delete_port_assignments_params_list (list): List of parameters for deleting port assignments.
        Returns:
            dict: A dictionary indicating whether deletion is required for each port assignment.
        Description:
            This method verifies if deletion is required for each port assignment by checking if the port assignments exist.
            It logs the parameters and returns a dictionary with the verification results.
        """
        self.log(
            "Starting verification for port assignments deletions for "
            "delete_port_assignments_params_list: {0}".format(delete_port_assignments_params_list),
            "DEBUG"
        )
        results = {}

        # Check if existing port channels is None
        if not delete_port_assignments_params_list:
            self.log("No 'delete_port_assignments_params_list' provided. Checking for all existing port assignments.", "INFO")
            existing_port_assignments = self.get_port_assignments(get_port_assignments_params)
            self.log("Retrieved existing port assignments: {}".format(existing_port_assignments), "DEBUG")

            if not existing_port_assignments:
                self.log("No existing port assignments found. Delete operation not required.", "INFO")
                return results

            interfaces_list = [port.get("interfaceName") for port in existing_port_assignments]
            self.log("List of interfaces to be deleted: {}".format(interfaces_list), "DEBUG")
            self.log("Deleting all port assignments with params: {}".format(get_port_assignments_params), "INFO")
            delete_port_assignments_params_list = [get_port_assignments_params]
            results[0] = {
                "delete_port_assignment_params": get_port_assignments_params,
                "interfaces_list": interfaces_list
            }
            return results

        for index, delete_port_assignment_param in enumerate(delete_port_assignments_params_list):
            self.log("Verifying parameters at index {0}: {1}".format(index, delete_port_assignment_param), "DEBUG")

            # Check if port assignments exist for the given parameters
            get_port_assignments_params = delete_port_assignment_param.copy()
            port_assignments = self.get_port_assignments(get_port_assignments_params)
            self.log("Existing Port assignments: {0}".format(port_assignments), "DEBUG")

            # Determine if deletion is required based on the existence of port assignments
            if port_assignments:
                interfaces_list = [port.get("interfaceName") for port in port_assignments] if port_assignments else []
                results[index] = {
                    "delete_port_assignment_params": delete_port_assignment_param,
                    "interfaces_list": interfaces_list
                }
            else:
                self.log(
                    "No matching port assignment found at index {0}: {1}. Delete not required."
                    .format(index, delete_port_assignment_param), "INFO"
                )
        self.log("Final delete verification results: {0}".format(results), "DEBUG")

        return results

    def delete_port_assignments(self, delete_port_assignments_params):
        """
        Initiates the task to delete port assignments.
        Args:
            delete_port_assignments_params (dict): Parameters for deleting port assignments.
        Returns:
            dict: The task ID from the API call.
        Description:
            This method initiates the task to delete port assignments using the provided parameters and returns the task ID.
        """
        self.log("Initiating deletion of port assignments with parameters: {0}".format(delete_port_assignments_params), "INFO")
        return self.get_taskid_post_api_call("sda", "delete_port_assignments", delete_port_assignments_params)

    def add_port_channels(self, add_port_channels_params):
        """
        Initiates the task to add port channels.
        Args:
            add_port_channels_params (dict): Parameters for adding port channels.
        Returns:
            dict: The task ID from the API call.
        Description:
            This method initiates the task to add port channels using the provided parameters and returns the task ID.
        """
        self.log("Initiating addition of port channels with parameters: {0}".format(add_port_channels_params), "INFO")
        return self.get_taskid_post_api_call("sda", "add_port_channels", add_port_channels_params)

    def update_port_channels(self, update_port_channels_params):
        """
        Initiates the task to update port channels.
        Args:
            update_port_channels_params (dict): Parameters for updating port channels.
        Returns:
            dict: The task ID from the API call.
        Description:
            This method initiates the task to update port channels using the provided parameters and returns the task ID.
        """
        self.log("Initiating update of port channels with parameters: {0}".format(update_port_channels_params), "INFO")
        return self.get_taskid_post_api_call("sda", "update_port_channels", update_port_channels_params)

    def delete_port_channels(self, delete_port_channel_param):
        """
        Initiates the task to delete port channels.
        Args:
            delete_port_channel_param (dict): Parameters for deleting port channels.
        Returns:
            dict: The task ID from the API call.
        Description:
            This method initiates the task to delete port channels using the provided parameters and returns the task ID.
        """
        self.log("Initiating deletion of port channels with parameters: {0}".format(delete_port_channel_param), "DEBUG")
        return self.get_taskid_post_api_call("sda", "delete_port_channels", delete_port_channel_param)

    def get_add_port_assignments_task_status(self, task_id):
        """
        Retrieves the task status for adding port assignments.
        Args:
            task_id (str): The ID of the task to check.
        Returns:
            dict: The status of the task retrieved using the task ID.
        Description:
            This method constructs a message indicating the successful completion of the add port assignments
            operation. It then retrieves the task status using the provided task ID and logs the relevant information.
        """
        task_name = "Add Port Assignment(s) Task"
        msg = {}

        # Retrieve the parameters for adding port assignments
        add_port_assignments_params = self.want["add_port_assignments_params"]
        interface_list = [port.get("interfaceName") for port in add_port_assignments_params["payload"]]
        msg["{0} Succeeded for following interface(s)".format(task_name)] = {"success_count": len(interface_list), "success_interfaces": interface_list}

        # Retrieve and return the task status using the provided task ID
        return self.get_task_status_from_tasks_by_id(task_id, task_name, msg)

    def get_update_port_assignments_task_status(self, task_id):
        """
        Retrieves the task status for updating port assignments.
        Args:
            task_id (str): The ID of the task to check.
        Returns:
            dict: The status of the task retrieved using the task ID.
        Description:
            This method constructs a message indicating the successful completion of the update port assignments
            operation. It then retrieves the task status using the provided task ID and logs the relevant information.
        """
        task_name = "Update Port Assignment(s) Task"
        msg = {}

        # Retrieve the parameters for update port assignments
        update_port_assignments_params = self.want["update_port_assignments_params"]
        interface_list = [port.get("interfaceName") for port in update_port_assignments_params["payload"]]
        msg["{0} Succeeded for following interface(s)".format(task_name)] = {"success_count": len(interface_list), "success_interfaces": interface_list}

        # Retrieve and return the task status using the provided task ID
        return self.get_task_status_from_tasks_by_id(task_id, task_name, msg)

    def get_delete_port_assignments_task_status(self, task_id, task_name, interface_list):
        """
        Retrieves the task status for deleting port assignments.
        Args:
            task_id (str): The ID of the task to check.
            task_name (str): The name of the task being performed.
            delete_port_assignment_params (dict): Parameters for the delete port assignment operation.
            interface_list (list): List of interfaces involved in the delete operation.
        Returns:
            dict: The status of the task retrieved using the task ID.
        Description:
            This method constructs a message indicating the successful completion of the delete port assignments
            operation. It then retrieves the task status using the provided task ID and logs the relevant information.
        """
        msg = "{0} operation has completed successfully for {1} interfaces: {2}.".format(task_name, len(interface_list), ", ".join(interface_list))

        # Retrieve and return the task status using the provided task ID
        self.get_task_status_from_tasks_by_id(task_id, task_name, msg).check_return_status()
        return self.status

    def process_delete_port_assignments(self, delete_port_assignments_params_list):
        """
        Processes the deletion of port assignments based on the provided parameters.
        Args:
            delete_port_assignments_params_list (dict): A dictionary containing parameters for deleting port assignments.
        Returns:
            self: Returns the instance with the updated operation result and message.
        Description:
            This method processes the deletion of port assignments by iterating over the provided parameters. It checks
            if deletion is required for each port assignment and performs the deletion if necessary. It logs the task ID,
            status, and interfaces for which the deletion was successful, failed, or skipped. The method sets the final
            message and operation result based on the status of the deletion tasks.
        """
        task_name = "Delete Port Assignment(s) Task"
        failed_interfaces = []
        success_interfaces = []
        skipped_interfaces = []
        msg = {}

        for index, delete_port_assignment_param in delete_port_assignments_params_list.items():
            interface_list = delete_port_assignment_param.get("interfaces_list")
            self.log("Processing - index: {0}, delete_port_assignment_param: {1}".format(index, delete_port_assignment_param), "DEBUG")

            task_id = self.delete_port_assignments(delete_port_assignment_param.get("delete_port_assignment_params"))
            self.log("Task ID: {0}".format(task_id), "DEBUG")
            status = self.get_delete_port_assignments_task_status(task_id, task_name, interface_list)

            if status == "success":
                success_interfaces.extend(interface_list)
            else:
                failed_interfaces.extend(interface_list)

        # Set the final message
        if success_interfaces:
            self.log("{0} Succeeded for following interface(s): {1} ".format(task_name, success_interfaces))
            msg["{0} Succeeded for following interface(s)".format(task_name)] = {
                "success_count": len(success_interfaces),
                "success_interfaces": success_interfaces
            }

        if failed_interfaces:
            self.log("{0} Failed for following interface(s): {1} ".format(task_name, failed_interfaces))
            msg["{0} Failed for following interface(s)".format(task_name)] = {"failed_count": len(failed_interfaces), "failed_interfaces": failed_interfaces}

        self.msg = msg
        # Check if no operations were performed
        if success_interfaces and failed_interfaces:
            self.set_operation_result("failed", True, self.msg, "ERROR")
        elif success_interfaces:
            self.set_operation_result("success", True, self.msg, "INFO")
        elif failed_interfaces:
            self.set_operation_result("failed", True, self.msg, "ERROR")
        else:
            self.set_operation_result("ok", False, self.msg, "INFO")

        return self

    def get_add_port_channels_task_status(self, task_id):
        """
        Retrieves the task status for adding port channels and updates the message accordingly.
        Args:
            task_id (str): The ID of the task to check.
        Returns:
            self: Returns the instance with the updated operation result and message.
        Description:
            This method constructs a message indicating the successful completion of the add port channels
            operation. It then retrieves the task status using the provided task ID. If the operation is
            successful, it fetches existing port channels and updates the message with the names of the
            newly created port channels.
        """
        task_name = "Add Port Channel(s) Task"
        add_port_channels_params = self.want["add_port_channels_params"]
        msg = "{0} has completed successfully for params: {1}.".format(task_name, add_port_channels_params["payload"])

        # Execute the task and get the status
        self.get_task_status_from_tasks_by_id(task_id, task_name, msg)

        # Check if the operation status matches self.status
        if self.status == "success":
            # Fetch existing port channels
            existing_port_channels = self.get_port_channels(self.have.get("get_port_channels_params"))

            # Log the fetched port channels
            self.log("Existing Port Channels after task completion: {0}".format(existing_port_channels), "DEBUG")

            # Compare interface names and collect created port channel names
            port_channels_names = []
            for port_channel in existing_port_channels:
                for payload_channel in add_port_channels_params["payload"]:
                    if set(payload_channel["interfaceNames"]) == set(port_channel["interfaceNames"]):
                        port_channels_names.append(port_channel["portChannelName"])
                        break

            self.log("Names of port_channels that were successfully created: {0}".format(port_channels_names), "DEBUG")

            updated_msg = {}

            # Update the message
            updated_msg["{0} Succeeded for following port channel(s)".format(task_name)] = {
                "success_count": len(port_channels_names),
                "success_port_channels": port_channels_names
            }
            self.msg = updated_msg

        return self

    def get_update_port_channels_task_status(self, task_id):
        """
        Retrieves the task status for updating port channels.
        Args:
            task_id (str): The ID of the task to check.
        Returns:
            dict: The status of the task retrieved using the task ID.
        Description:
            This method constructs a message indicating the successful completion of the update port channels
            operation. It then retrieves the task status using the provided task ID and logs the relevant information.
        """
        task_name = "Update Port Channel(s) Task"
        msg = {}

        # Retrieve the parameters for updating port channels
        update_port_channels_params = self.want.get("update_port_channels_params")
        port_channels_list = [port.get("portChannelName") for port in update_port_channels_params["payload"]]
        msg["{0} Succeeded for following port channel(s)".format(task_name)] = {
            "success_count": len(port_channels_list),
            "success_port_channels": port_channels_list
        }

        # Retrieve and return the task status using the provided task ID
        return self.get_task_status_from_tasks_by_id(task_id, task_name, msg)

    def get_delete_port_channels_task_status(self, task_id, task_name, port_channels_list):
        """
        Retrieves the task status for deleting port channels.
        Args:
            task_id (str): The ID of the task to check.
            task_name (str): The name of the task being performed.
            delete_port_channel_params (dict): Parameters for the delete port channel operation.
            port_channels_list (list): List of port channels involved in the delete operation.
        Returns:
            dict: The status of the task retrieved using the task ID.
        Description:
            This method constructs a message indicating the successful completion of the delete port channels
            operation. It then retrieves the task status using the provided task ID and logs the relevant information.
        """
        msg = "{0} operation has completed successfully for {1} port channels: {2}.".format(task_name, len(port_channels_list), ", ".join(port_channels_list))

        # Retrieve the task status using the provided task ID and check the return status
        self.get_task_status_from_tasks_by_id(task_id, task_name, msg).check_return_status()
        return self.status

    def process_delete_port_channels(self, delete_port_channels_params_list):
        """
        Processes the deletion of port channels based on the provided parameters.
        Args:
            delete_port_channels_params_list (dict): A dictionary containing parameters for deleting port channels.
        Returns:
            self: Returns the instance with the updated operation result and message.
        Description:
            This method processes the deletion of port channels by iterating over the provided parameters. It checks
            if deletion is required for each port channel and performs the deletion if necessary. It logs the task ID,
            status, and channels for which the deletion was successful, failed, or skipped. The method sets the final
            message and operation result based on the status of the deletion tasks.
        """
        task_name = "Delete Port Channel(s) Task"
        failed_channels = []
        success_channels = []
        skipped_channels = []
        msg = {}

        for index, delete_port_channel_param in delete_port_channels_params_list.items():
            channel_list = delete_port_channel_param.get("port_channels_list")
            self.log("Processing - index: {0}, delete_port_channel_param: {1}".format(index, delete_port_channel_param), "DEBUG")

            task_id = self.delete_port_channels(delete_port_channel_param.get("delete_port_channel_params"))
            self.log("Task ID: {0}".format(task_id), "DEBUG")
            status = self.get_delete_port_channels_task_status(task_id, task_name, channel_list)

            if status == "success":
                success_channels.extend(channel_list)
            else:
                failed_channels.extend(channel_list)

        if success_channels:
            self.log("{0} Succeeded for following port channel(s): {1} ".format(task_name, success_channels))
            msg["{0} Succeeded for following port channel(s)".format(task_name)] = {
                "success_count": len(success_channels),
                "success_port_channels": success_channels
            }

        if failed_channels:
            self.log("{0} Failed for following channel(s): {1} ".format(task_name, failed_channels))
            msg["{0} Failed for following port channel(s)".format(task_name)] = {"failed_count": len(failed_channels), "failed_port_channels": failed_channels}

        self.msg = msg
        if success_channels and failed_channels:
            self.set_operation_result("failed", True, self.msg, "ERROR")
        elif success_channels:
            self.set_operation_result("success", True, self.msg, "INFO")
        elif failed_channels:
            self.set_operation_result("failed", True, self.msg, "ERROR")
        else:
            self.set_operation_result("ok", False, self.msg, "INFO")

        return self

    def process_delete_vlans_and_ssids_mapped_to_vlans(self, delete_vlans_and_ssids_mapped_to_vlans_params):
        """
        Processes the deletion of VLANs and their mapped SSIDs.
        Args:
            delete_vlans_and_ssids_mapped_to_vlans_params (dict): Parameters for deleting VLANs and mapped SSIDs.
        Returns:
            dict: The status of the deletion task.
        Description:
            This method handles the task of deleting specified VLANs and the SSIDs mapped to them. It constructs
            a message indicating which VLANs and SSIDs have been successfully processed. It then initiates the
            deletion task and retrieves the task's status.
        """
        self.log("Processing DELETE - VLANs and SSIDs operation with parameters: {0}".format(delete_vlans_and_ssids_mapped_to_vlans_params), "DEBUG")

        msg = {}
        task_name = "Delete VLAN(s) and SSID(s) Mapped to VLAN(s) Task"

        delete_vlans_and_ssids_mapped_to_vlans = self.have.get("delete_vlans_and_ssids_mapped_to_vlans")

        if delete_vlans_and_ssids_mapped_to_vlans:
            self.log("Generated msg for DELETE operation for VLANs and SSIDs.", "DEBUG")
            msg["{0} Succeeded for following VLAN(s) and SSID(s)".format(task_name)] = {
                vlan: [ssid['name'] for ssid in ssids['ssidDetails']]
                for vlan, ssids in delete_vlans_and_ssids_mapped_to_vlans.items()
            }
            self.log("Constructed deletion success message: {}".format(msg), "DEBUG")

        task_id = self.create_update_remove_vlans_and_ssids_mapped_to_vlans(delete_vlans_and_ssids_mapped_to_vlans_params)
        return self.get_task_status_from_tasks_by_id(task_id, task_name, msg)

    def verify_delete_vlans_and_ssids_mapped_to_vlans_requirement(self, fabric_name, fabric_id, wireless_ssids_details):
        """
        Verifies which VLANs and SSIDs should be deleted based on user input.
        Args:
            fabric_id: The identifier for the fabric from which VLANs and SSIDs are retrieved.
            wireless_ssids_details: A list of dictionaries indicating which VLANs and SSIDs should be deleted.
        Returns:
            A tuple containing:
            - A dictionary of VLANs and SSIDs to be deleted.
            - An updated list of VLANs and their SSID details after deletions.
        """
        self.log("Starting verification for VLAN and SSID deletions for fabric: {0} fabric_id: {1}".format(fabric_name, fabric_id), "DEBUG")
        # Retrieve existing VLANs and SSIDs mapped to VLANs from the fabric site.
        existing_vlans_and_ssids_mapped_to_vlans = self.get_vlans_and_ssids_mapped_to_vlans(fabric_id)
        self.log("Retrieved existing VLANs and SSIDs: {0}".format(existing_vlans_and_ssids_mapped_to_vlans), "DEBUG")

        if not existing_vlans_and_ssids_mapped_to_vlans:
            self.log("No existing VLANs and SSIDs mapped to VLANs found. Hence delete operation is not required.", "INFO")
            return {}, []

        # Create a copy of the existing details to be modified.
        updated_vlans_and_ssids = [vlan.copy() for vlan in existing_vlans_and_ssids_mapped_to_vlans]
        self.log("Initial copy of existing VLANs and SSIDs to be modified: {0}".format(updated_vlans_and_ssids), "DEBUG")

        # Initialize dictionary for VLANs/SSIDs that need to be deleted.
        delete_vlans_ssids_mapped_to_vlans = {}

        # If no wireless_ssids_details are provided, mark all for deletion
        if not wireless_ssids_details:
            self.log("No specific wireless SSID details provided. Preparing to delete all existing VLANs and SSIDs.", "INFO")
            for vlan in existing_vlans_and_ssids_mapped_to_vlans:
                vlan_name = vlan['vlanName']
                delete_vlans_ssids_mapped_to_vlans[vlan_name] = vlan

            updated_vlans_and_ssids = []
            self.log("All existing VLANs and SSIDs are marked for deletion: {0}".format(delete_vlans_ssids_mapped_to_vlans), "DEBUG")
            return delete_vlans_ssids_mapped_to_vlans, updated_vlans_and_ssids

        # Create a dictionary for quick lookup of existing VLANs and their SSIDs.
        existing_vlans_dict = {vlan['vlanName']: vlan for vlan in existing_vlans_and_ssids_mapped_to_vlans}
        self.log("Existing VLANs dictionary for lookup: {0}".format(existing_vlans_dict), "DEBUG")

        # Iterate through the provided SSID details to identify deletions.
        for ssid_detail in wireless_ssids_details:
            vlan_name = ssid_detail['vlan_name']
            ssid_details = ssid_detail.get('ssid_details', [])

            if vlan_name in existing_vlans_dict:
                if not ssid_details:
                    # No specific SSID details provided, remove the entire VLAN
                    self.log("Marked VLAN for deletion: {0}".format(vlan_name), "INFO")
                    delete_vlans_ssids_mapped_to_vlans[vlan_name] = existing_vlans_dict[vlan_name]
                    updated_vlans_and_ssids = [vlan for vlan in updated_vlans_and_ssids if vlan['vlanName'] != vlan_name]
                else:
                    existing_ssids = existing_vlans_dict[vlan_name]['ssidDetails']
                    existing_ssids_dict = {ssid['name']: ssid for ssid in existing_ssids}
                    self.log("Existing SSIDs for VLAN {0}: {1}".format(vlan_name, existing_ssids_dict), "DEBUG")

                    for ssid in ssid_details:
                        ssid_name = ssid['ssid_name']

                        if ssid_name in existing_ssids_dict:
                            # SSID exists and needs to be deleted
                            if vlan_name not in delete_vlans_ssids_mapped_to_vlans:
                                delete_vlans_ssids_mapped_to_vlans[vlan_name] = {'vlanName': vlan_name, 'ssidDetails': []}
                            delete_vlans_ssids_mapped_to_vlans[vlan_name]['ssidDetails'].append({'name': ssid_name})
                            self.log("Marked SSID for deletion: {0} under VLAN: {1}".format(ssid_name, vlan_name), "INFO")

                            # Remove SSID from the updated existing details
                            updated_vlans_and_ssids = [
                                {
                                    'vlanName': vlan['vlanName'],
                                    'ssidDetails': [s for s in vlan['ssidDetails'] if s['name'] != ssid_name]
                                } if vlan['vlanName'] == vlan_name else vlan
                                for vlan in updated_vlans_and_ssids
                            ]

        self.log("delete_vlans_ssids_mapped_to_vlans: {0}".format(delete_vlans_ssids_mapped_to_vlans), "INFO")
        self.log("updated_vlans_and_ssids: {0}".format(updated_vlans_and_ssids), "INFO")

        return delete_vlans_ssids_mapped_to_vlans, updated_vlans_and_ssids

    def process_final_result(self, final_status_list):
        """
        Processes a list of final statuses and returns a tuple indicating the result and a boolean flag.
        Args:
            final_status_list (list): List of status strings to process.
        Returns:
            tuple: A tuple containing a status string ("ok" or "success") and a boolean flag (False if all statuses are "ok", True otherwise).
        """
        status_set = set(final_status_list)

        if status_set == {"ok"}:
            return "ok", False
        else:
            return "success", True

    def verify_port_assignments_add_operation(self, add_port_assignments_params):
        """
        Verifies the success of ADD Port Assignments operation.
        Args:
            add_port_assignments_params (dict): The parameters for the add port assignments operation.
        """
        get_port_assignments_params = self.have.get("get_port_assignments_params")
        port_assignments = self.get_port_assignments(get_port_assignments_params)

        self.log("Desired State: {0}".format(str(add_port_assignments_params)), "INFO")
        self.log("State after performing ADD Port Assignments operation: {0}".format(str(port_assignments)), "INFO")

        current_interface_names = [port.get("interfaceName") for port in port_assignments]
        add_interface_names = [
            param.get("interfaceName") for param in add_port_assignments_params["payload"]
        ]

        # Check if all add_interface_names are in current_interface_names
        if all(interface in current_interface_names for interface in add_interface_names):
            self.log(
                "Verified the success of ADD Port Assignments operation for interfaceName(s) {0}.".format(
                    ", ".join(add_interface_names)
                ), "INFO"
            )
        else:
            self.log(
                "The ADD Port Assignments operation may not have been successful "
                "since the port assignments do not exist in the Cisco Catalyst Center.", "WARNING"
            )

    def verify_port_assignments_update_operation(self, update_port_assignments_params):
        """
        Verifies the success of UPDATE Port Assignments operation.
        Args:
            update_port_assignments_params (dict): The parameters for the update port assignments operation.
        """
        get_port_assignments_params = self.have.get("get_port_assignments_params")
        port_assignments = self.get_port_assignments(get_port_assignments_params)

        self.log("Desired State: {0}".format(str(update_port_assignments_params)), "INFO")
        self.log("State after performing UPDATE Port Assignments operation: {0}".format(str(port_assignments)), "INFO")

        mismatched_interfaces = []

        # Compare the update_port_assignments_params with the current port_assignments
        for update_param in update_port_assignments_params["payload"]:
            interface_id = update_param.get("id")
            matching_port = next((port for port in port_assignments if port.get("id") == interface_id), None)

            if matching_port:
                for key, value in update_param.items():
                    if key not in ["fabricId", "networkDeviceId"] and matching_port.get(key) != value:
                        mismatched_interfaces.append(update_param.get("interfaceName"))
                        break

        # Log the results
        if not mismatched_interfaces:
            self.log(
                "Verified the success of UPDATE Port Assignments operation for interfaceName(s) {0}.".format(
                    ", ".join([param.get("interfaceName") for param in update_port_assignments_params["payload"]])
                ), "INFO"
            )
        else:
            self.log(
                "The UPDATE Port Assignments operation may not have been successful "
                "since the following interface assignments do not match: {0}.".format(", ".join(mismatched_interfaces)),
                "WARNING"
            )

    def verify_port_assignments_delete_operation(self, delete_port_assignments_params):
        """
        Verifies the deletion of port assignments.
        Args:
            delete_port_assignments_params (dict): Parameters for deleting port assignments.
        Returns:
            None
        """
        interfaces_still_exist = []

        for index, delete_port_assignment_data in delete_port_assignments_params.items():
            self.log("Processing parameters at - index {0}: {1}".format(index, delete_port_assignment_data), "DEBUG")
            delete_required = delete_port_assignment_data.get("delete_required")
            delete_port_assignment_params = delete_port_assignment_data.get("delete_port_assignment_params")
            interfaces_list = delete_port_assignment_data.get("interfaces_list", [])

            if delete_required:
                port_assignments = self.get_port_assignments(delete_port_assignment_params)

                if port_assignments:
                    existing_interfaces = [port.get("interfaceName") for port in port_assignments if port.get("interfaceName") in interfaces_list]
                    interfaces_still_exist.extend(existing_interfaces)
                    self.log(
                        "The DELETE Port Assignments operation may not have been successful "
                        "since the following interface assignments still exist: {0}.".format(", ".join(existing_interfaces)),
                        "WARNING"
                    )
                else:
                    self.log(
                        "Verified the success of DELETE Port Assignments operation for interfaceName(s) {0}.".format(
                            ", ".join(interfaces_list)
                        ), "INFO"
                    )

        if interfaces_still_exist:
            self.log(
                "The following interfaceName(s) were not deleted: {0}.".format(", ".join(interfaces_still_exist)),
                "ERROR"
            )
        else:
            self.log(
                "All specified port assignments were successfully deleted.",
                "INFO"
            )

    def verify_port_channels_add_operation(self, add_port_channels_params):
        """
        Verifies the success of ADD Port Channels operation.
        Args:
            add_port_channels_params (dict): The parameters for the add port channels operation.
        """
        get_port_channels_params = self.have.get("get_port_channels_params")
        existing_port_channels = self.get_port_channels(get_port_channels_params)

        # Log the fetched port channels
        self.log("Existing Port Channels after task completion: {0}".format(existing_port_channels), "DEBUG")
        self.log("Desired State: {0}".format(add_port_channels_params), "INFO")

        if existing_port_channels:
            # Compare interface names and collect created port channel names
            port_channels_names = []
            for requested_channel in add_port_channels_params.get("payload"):
                requested_interface_names = requested_channel.get("interfaceNames")
                for existing_channel in existing_port_channels:
                    if set(requested_interface_names) == set(existing_channel.get("interfaceNames")):
                        port_channels_names.append(existing_channel.get("portChannelName"))

            # Log the result of verification
            if port_channels_names:
                self.log(
                    "Verified the success of ADD Port Channels operation for portChannelName(s) {0}.".format(
                        ", ".join(port_channels_names)
                    ), "INFO"
                )
            else:
                self.log(
                    "The ADD Port Channels operation may not have been successful "
                    "since the port channels do not exist in the Cisco Catalyst Center.", "WARNING"
                )
        else:
            self.log(
                "The ADD Port Channels operation may not have been successful "
                "since no port channels were found in the Cisco Catalyst Center.", "WARNING"
            )

    def verify_port_channels_update_operation(self, update_port_channels_params):
        """
        Verifies the success of UPDATE Port Channels operation.
        Args:
            update_port_channels_params (dict): The parameters for the update port channels operation.
        """
        get_port_channels_params = self.have.get("get_port_channels_params")
        port_channels = self.get_port_channels(get_port_channels_params)

        self.log("Desired State: {0}".format(str(update_port_channels_params)), "INFO")
        self.log("State after performing UPDATE Port Channels operation: {0}".format(str(port_channels)), "INFO")

        mismatched_channels = []

        # Compare the update_port_channels_params with the current port_channels
        for update_param in update_port_channels_params["payload"]:
            port_channel_name = update_param.get("portChannelName")
            matching_channel = next((channel for channel in port_channels if channel.get("portChannelName") == port_channel_name), None)

            if matching_channel:
                for key, value in update_param.items():
                    if key not in ["fabricId", "networkDeviceId"] and matching_channel.get(key) != value:
                        mismatched_channels.append(port_channel_name)
                        break

        # Log the results
        if not mismatched_channels:
            self.log(
                "Verified the success of UPDATE Port Channels operation for portChannelName(s) {0}.".format(
                    ", ".join([param.get("portChannelName") for param in update_port_channels_params["payload"]])
                ), "INFO"
            )
        else:
            self.log(
                "The UPDATE Port Channels operation may not have been successful "
                "since the following port channels do not match: {0}.".format(", ".join(mismatched_channels)),
                "WARNING"
            )

    def verify_port_channels_delete_operation(self, delete_port_channels_params):
        """
        Verifies the deletion of port channels.
        Args:
            delete_port_channels_params (dict): Parameters for deleting port channels.
        Returns:
            None
        """
        channels_still_exist = []

        for index, delete_port_channel_data in delete_port_channels_params.items():
            self.log("Processing parameters at - index {0}: {1}".format(index, delete_port_channel_data), "DEBUG")
            delete_required = delete_port_channel_data.get("delete_required")
            delete_port_channel_params = delete_port_channel_data.get("delete_port_channel_params")
            channel_list = delete_port_channel_data.get("channel_list", [])

            if delete_required:
                port_channels = self.get_port_channels(delete_port_channel_params)

                if port_channels:
                    existing_channels = [channel.get("portChannelName") for channel in port_channels if channel.get("portChannelName") in channel_list]
                    channels_still_exist.extend(existing_channels)
                    self.log(
                        "The DELETE Port Channels operation may not have been successful "
                        "since the following port channels still exist: {0}.".format(", ".join(existing_channels)),
                        "WARNING"
                    )
                else:
                    self.log(
                        "Verified the success of DELETE Port Channels operation for portChannelName(s) {0}.".format(
                            ", ".join(channel_list)
                        ), "INFO"
                    )

        if channels_still_exist:
            self.log(
                "The following portChannelName(s) were not deleted: {0}.".format(", ".join(channels_still_exist)),
                "ERROR"
            )
        else:
            self.log(
                "All specified port channels were successfully deleted.",
                "INFO"
            )

    def verify_vlans_and_ssids_mapped_to_vlans_create_update_operation(self):
        """
        Verifies the success of creating and updating VLANs and SSIDs mapped to VLANs.
        This method checks the current state of VLANs and SSIDs against the expected create and update
        operations to ensure they have been performed successfully.
        """
        # Retrieve expected create and update mappings

        create_vlans_and_ssids_mapped_to_vlans = self.have.get("create_vlans_and_ssids_mapped_to_vlans", {})
        update_vlans_and_ssids_mapped_to_vlans = self.have.get("update_vlans_and_ssids_mapped_to_vlans", {})

        # Get the current state of VLANs and SSIDs
        fabric_name = self.have.get("fabric_site_name_hierarchy")
        fabric_id = self.have.get("fabric_id")
        current_vlans_and_ssids_mapped_to_vlans = self.get_vlans_and_ssids_mapped_to_vlans(fabric_id)
        self.log("Verifying operations for fabric: {0} fabric_id: {1}".format(fabric_name, fabric_id), "INFO")

        self.log("Desired Create State: {}".format(create_vlans_and_ssids_mapped_to_vlans), "INFO")
        self.log("Desired Update State: {}".format(update_vlans_and_ssids_mapped_to_vlans), "INFO")
        self.log("Current State after operations: {}".format(current_vlans_and_ssids_mapped_to_vlans), "INFO")

        mismatched_vlans_create = {}
        mismatched_vlans_update = {}

        # Verify creations
        if create_vlans_and_ssids_mapped_to_vlans:
            for vlan, expected_ssids in create_vlans_and_ssids_mapped_to_vlans.items():
                actual_vlan = next((item for item in current_vlans_and_ssids_mapped_to_vlans if item['vlanName'] == vlan), None)
                if not actual_vlan:
                    mismatched_vlans_create[vlan] = {'ssid_details': expected_ssids}
                else:
                    actual_ssid_names = {s['name']: s for s in actual_vlan['ssidDetails']}
                    for ssid in expected_ssids:
                        if ssid['ssid_name'] not in actual_ssid_names:
                            mismatched_vlans_create.setdefault(vlan, {'ssid_details': []})['ssid_details'].append(
                                {'name': ssid['ssid_name'], 'securityGroupTag': ssid.get('security_group_name')}
                            )
            # Log the results
            if not mismatched_vlans_create:
                self.log(
                    "Successfully verified the creation of VLANs and SSIDs mapped to VLANs operation: {0}".format(
                        create_vlans_and_ssids_mapped_to_vlans
                    ),
                    "INFO"
                )
            else:
                self.log(
                    "The ADD VLANs and SSIDs mapped to VLANs operation may not have been successful "
                    "since the following mismatches were found: {0}".format(mismatched_vlans_create),
                    "WARNING"
                )

        # Verify updates
        if update_vlans_and_ssids_mapped_to_vlans:
            for vlan, expected_ssids in update_vlans_and_ssids_mapped_to_vlans.items():
                actual_vlan = next((item for item in current_vlans_and_ssids_mapped_to_vlans if item['vlanName'] == vlan), None)
                if not actual_vlan:
                    mismatched_vlans_update[vlan] = {'ssid_details': expected_ssids}
                else:
                    actual_ssid_names = {s['name']: s for s in actual_vlan['ssidDetails']}
                    for ssid in expected_ssids:
                        if ssid['ssid_name'] not in actual_ssid_names:
                            mismatched_vlans_update.setdefault(vlan, {'ssid_details': []})['ssid_details'].append(
                                {'name': ssid['ssid_name'], 'securityGroupTag': ssid.get('security_group_name')}
                            )

            if not mismatched_vlans_update:
                self.log(
                    "Successfully verified the update of VLANs and SSIDs mapped to VLANs operation: {0}".format(
                        update_vlans_and_ssids_mapped_to_vlans
                    ),
                    "INFO"
                )
            else:
                self.log(
                    "The UPDATE VLANs and SSIDs mapped to VLANs operation may not have been successful "
                    "since the following mismatches were found: {0}".format(mismatched_vlans_update),
                    "WARNING"
                )

    def verify_vlans_and_ssids_mapped_to_vlans_delete_operation(self):
        """
        Verifies the deletion of VLANs and SSIDs mapped to VLANs.
        This method checks that the specified VLANs and their associated SSIDs have been deleted
        from the system. It logs the results of the verification process.
        """
        # Retrieve expected deletions
        delete_vlans_and_ssids_mapped_to_vlans = self.have.get("delete_vlans_and_ssids_mapped_to_vlans", {})

        # Get the current state of VLANs and SSIDs
        fabric_id = self.have.get('fabric_id')
        current_vlans_and_ssids_mapped_to_vlans = self.get_vlans_and_ssids_mapped_to_vlans(fabric_id)

        self.log("Expected Deletions: {}".format(delete_vlans_and_ssids_mapped_to_vlans), "INFO")
        self.log("Current State after deletions: {}".format(current_vlans_and_ssids_mapped_to_vlans), "INFO")

        mismatched_vlans_delete = {}

        # Verify deletions
        for vlan, expected_ssid_info in delete_vlans_and_ssids_mapped_to_vlans.items():
            actual_vlan = next((item for item in current_vlans_and_ssids_mapped_to_vlans if item['vlanName'] == vlan), None)

            if actual_vlan:
                # VLAN still exists, so check SSIDs
                actual_ssid_names = {s['name']: s for s in actual_vlan['ssidDetails']}
                for ssid in expected_ssid_info['ssidDetails']:
                    if ssid['name'] in actual_ssid_names:
                        mismatched_vlans_delete.setdefault(vlan, {'ssid_details': []})['ssid_details'].append(
                            {'name': ssid['name'], 'securityGroupTag': ssid.get('securityGroupTag')}
                        )

        # Log the results
        if not mismatched_vlans_delete:
            self.log("Successfully verified the deletion of VLANs and SSIDs mapped to VLANs operation.", "INFO")
        else:
            self.log(
                "The DELETE VLANs and SSIDs mapped to VLANs operation may not have been successful "
                "since the following mismatches were found: {}".format(mismatched_vlans_delete),
                "WARNING"
            )

    def get_have(self, config, state):
        """
        Gathers the current state of the network device and fabric based on the provided configuration and state.
        Args:
            config (dict): The configuration details containing IP address, hostname, port assignments, and port channels.
            state (str): The desired state of the configuration (e.g., "merged", "deleted").
        Returns:
            self: Returns the instance with the updated "have" attribute containing the current state.
        Description:
            This method validates the parameters and retrieves the network fabric ID and device instance ID map.
            It constructs the current state ("have") based on the provided configuration and desired state.
            For the "merged" state, it compares existing and requested port assignments and channels to determine
            which ones need to be created, updated, or no updates are needed. For the "deleted" state, it verifies
            the requirements for deleting port assignments and channels. The method logs the current state and
            returns the instance.
        """
        # Validate the provided configuration parameters
        self.validate_params(config, state)

        port_assignment_details = config.get("port_assignments")
        port_channel_details = config.get("port_channels")
        wireless_ssids_details = config.get("wireless_ssids")
        fabric_site_name_hierarchy = config.get("fabric_site_name_hierarchy")
        ip_address = [config.get("ip_address")]
        hostname = config.get("hostname")

        fabric_id = self.get_fabric_id(fabric_site_name_hierarchy)
        have = {"fabric_id": fabric_id, "fabric_site_name_hierarchy": fabric_site_name_hierarchy}

        def update_network_details():
            # nonlocal ip_address
            mgmt_ip_to_instance_id_map = self.get_network_device_id(ip_address[0], hostname)
            network_device_id = list(mgmt_ip_to_instance_id_map.values())[0]
            ip_address[0] = list(mgmt_ip_to_instance_id_map.keys())[0]
            self.validate_device_in_fabric(ip_address[0])
            have.update({
                "mgmt_ip_to_instance_id_map": mgmt_ip_to_instance_id_map,
                "ip_address": ip_address[0],
                "network_device_id": network_device_id,
                "get_port_assignments_params": self.get_port_assignments_params(network_device_id, fabric_id),
                "get_port_channels_params": self.get_port_channels_params(network_device_id, fabric_id)
            })

        if port_assignment_details or port_channel_details:
            update_network_details()

        if state == "merged":
            if port_assignment_details:
                # Compare and categorize port assignments
                create_port_assignments, update_port_assignments, no_update_port_assignments = self.compare_port_assignments(
                    have["get_port_assignments_params"], port_assignment_details
                )
                have["create_port_assignments"] = create_port_assignments
                have["update_port_assignments"] = update_port_assignments
                have["no_update_port_assignments"] = no_update_port_assignments

            if port_channel_details:
                # Compare and categorize port channels
                (create_port_channels, update_port_channels, no_update_port_channels) = (
                    self.compare_port_channels(have["get_port_channels_params"], port_channel_details)
                )
                have["create_port_channels"] = create_port_channels
                have["update_port_channels"] = update_port_channels
                have["no_update_port_channels"] = no_update_port_channels

            if wireless_ssids_details:
                (create_vlans_and_ssids_mapped_to_vlans, update_vlans_and_ssids_mapped_to_vlans,
                 no_update_vlans_and_ssids_mapped_to_vlans, updated_vlans_and_ssids) = (
                    self.compare_vlans_and_ssids_mapped_to_vlans(fabric_site_name_hierarchy, fabric_id, wireless_ssids_details)
                )
                if create_vlans_and_ssids_mapped_to_vlans or update_vlans_and_ssids_mapped_to_vlans:
                    have["create_update_vlans_and_ssids_mapped_to_vlans"] = updated_vlans_and_ssids
                    have["create_vlans_and_ssids_mapped_to_vlans"] = create_vlans_and_ssids_mapped_to_vlans
                    have["update_vlans_and_ssids_mapped_to_vlans"] = update_vlans_and_ssids_mapped_to_vlans
                    have["no_update_vlans_and_ssids_mapped_to_vlans"] = no_update_vlans_and_ssids_mapped_to_vlans

        elif state == "deleted":
            if port_assignment_details:
                # Generate and verify parameters for deleting port assignments
                delete_port_assignments_params_list = self.get_delete_port_assignments_params(port_assignment_details, have["network_device_id"], fabric_id)
                have["delete_port_assignments_details"] = self.verify_delete_port_assignments_requirement(
                    delete_port_assignments_params_list, have["get_port_assignments_params"])

            if port_channel_details:
                # Generate and verify parameters for deleting port channels
                have["delete_port_channels_details"] = self.get_delete_port_channels_params(port_channel_details, have["get_port_channels_params"])

            if wireless_ssids_details:
                # Generate and verify parameters for deleting
                delete_vlans_and_ssids_mapped_to_vlans, updated_delete_vlans_ssids_mapped_to_vlans = (
                    self.verify_delete_vlans_and_ssids_mapped_to_vlans_requirement(fabric_site_name_hierarchy, fabric_id, wireless_ssids_details)
                )
                have["delete_vlans_and_ssids_mapped_to_vlans"] = delete_vlans_and_ssids_mapped_to_vlans
                have["updated_delete_vlans_ssids_mapped_to_vlans"] = updated_delete_vlans_ssids_mapped_to_vlans

            if not port_assignment_details and not port_channel_details and not wireless_ssids_details:
                if ip_address or hostname:
                    update_network_details()
                    # Handle case where no specific port assignments details are not provided
                    delete_port_assignments_params_list = self.get_delete_port_assignments_params(port_assignment_details, have["network_device_id"], fabric_id)
                    have["delete_port_assignments_details"] = self.verify_delete_port_assignments_requirement(
                        delete_port_assignments_params_list, have["get_port_assignments_params"]
                    )
                    # Handle case where no specific port channels details are not provided
                    have["delete_port_channels_details"] = self.get_delete_port_channels_params(port_assignment_details, have["get_port_channels_params"])

                have["delete_all_vlans_ssids_mapped_to_vlans"] = True
                delete_vlans_and_ssids_mapped_to_vlans, updated_delete_vlans_ssids_mapped_to_vlans = (
                    self.verify_delete_vlans_and_ssids_mapped_to_vlans_requirement(fabric_site_name_hierarchy, fabric_id, wireless_ssids_details)
                )
                have["delete_vlans_and_ssids_mapped_to_vlans"] = delete_vlans_and_ssids_mapped_to_vlans
                have["updated_delete_vlans_ssids_mapped_to_vlans"] = updated_delete_vlans_ssids_mapped_to_vlans

        # Store the constructed current state in the instance attribute
        self.have = have
        self.log("Current State (have): {0}".format(str(self.have)), "INFO")

        return self

    def get_want(self, config, state):
        """
        Creates the desired state parameters for API calls based on the provided configuration and state.
        Args:
            state (str): The desired state of the configuration (e.g., "merged", "deleted").
        Returns:
            self: Returns the instance with the updated "want" attribute containing the desired state.
        Description:
            This method constructs the desired state ("want") based on the provided configuration and desired state.
            For the "merged" state, it prepares parameters for adding or updating port assignments and port channels.
            For the "deleted" state, it prepares parameters for deleting port assignments and port channels. The method
            logs the desired state and returns the instance.
        """
        self.log("Creating Parameters for API Calls with state: {0}".format(state))

        want = {}

        if state == "merged":
            if self.have.get("create_port_assignments"):
                # Set parameters for adding port assignments
                want["add_port_assignments_params"] = self.get_add_port_assignments_params()
                self.log(
                    "State is merged and Port Assignments need to be created in the Cisco Catalyst Center, "
                    "therefore setting 'add_port_assignments_params' - {0}.".format(want.get("add_port_assignments_params")),
                    "DEBUG"
                )

            if self.have.get("update_port_assignments"):
                # Set parameters for updating port assignments
                want["update_port_assignments_params"] = self.get_update_port_assignments_params()
                self.log(
                    "State is merged and Existing Port Assignments in the Cisco Catalyst Center need to be UPDATED."
                    "therefore setting 'update_port_assignments_params' - {0}.".format(want.get("update_port_assignments_params")),
                    "DEBUG"
                )

            if self.have.get("create_port_channels"):
                # Set parameters for adding port channels
                want["add_port_channels_params"] = self.get_add_port_channels_params()
                self.log(
                    "State is merged and Port Channels need to be created in the Cisco Catalyst Center, "
                    "therefore setting 'add_port_channel_params' - {0}.".format(want.get("add_port_channels_params")),
                    "DEBUG"
                )

            if self.have.get("update_port_channels"):
                # Set parameters for updating port channels
                want["update_port_channels_params"] = self.get_update_port_channels_params()
                self.log(
                    "State is merged and Existing Port Channels in the Cisco Catalyst Center need to be UPDATED, "
                    "therefore setting 'update_port_channel_params' - {0}.".format(want.get("update_port_channels_params")),
                    "DEBUG"
                )

            create_update_vlans_and_ssids_mapped_to_vlans = self.have.get("create_update_vlans_and_ssids_mapped_to_vlans")
            if create_update_vlans_and_ssids_mapped_to_vlans:
                want["create_update_vlans_and_ssids_mapped_to_vlans_params"] = (
                    self.get_create_update_remove_vlans_and_ssids_mapped_to_vlans_params(
                        create_update_vlans_and_ssids_mapped_to_vlans
                    )
                )
                self.log(
                    "State is merged and Existing VLANs and wireless SSIDs mapped to VLANs in the Cisco Catalyst Center need to be MODIFIED, "
                    "therefore setting 'create_update_vlans_and_ssids_mapped_to_vlans_params' - {0}".format(
                        want.get("create_update_vlans_and_ssids_mapped_to_vlans_params")
                    )
                )

        elif state == "deleted":
            delete_port_assignments_details = self.have.get("delete_port_assignments_details")
            if delete_port_assignments_details:
                # Set parameters for deleting port assignments
                want["delete_port_assignments_params"] = delete_port_assignments_details
                self.log(
                    "State is deleted and Port Assignments need to be deleted in the Cisco Catalyst Center, "
                    "therefore setting 'delete_port_assignments_params' - {0}.".format(want.get("delete_port_assignments_params")),
                    "DEBUG"
                )

            delete_port_channels_details = self.have.get("delete_port_channels_details")
            if delete_port_channels_details:
                # Set parameters for deleting port channels
                want["delete_port_channels_params"] = delete_port_channels_details
                self.log(
                    "State is deleted and Port Channels need to be deleted in the Cisco Catalyst Center, "
                    "therefore setting 'delete_port_channels_params' - {0}.".format(want.get("delete_port_channels_params")),
                    "DEBUG"
                )

            updated_delete_vlans_ssids_mapped_to_vlans = self.have.get("updated_delete_vlans_ssids_mapped_to_vlans")
            delete_vlans_and_ssids_mapped_to_vlans = self.have.get("delete_vlans_and_ssids_mapped_to_vlans")
            if updated_delete_vlans_ssids_mapped_to_vlans:
                want["delete_vlans_and_ssids_mapped_to_vlans_params"] = (
                    self.get_create_update_remove_vlans_and_ssids_mapped_to_vlans_params(
                        updated_delete_vlans_ssids_mapped_to_vlans
                    )
                )

                self.log(
                    "State is deleted and VLANs and wireless SSIDs mapped to VLANs need to be "
                    "deleted in the Cisco Catalyst Center, therefore setting "
                    "'delete_vlans_and_ssids_mapped_to_vlans_params' - {0}.".format(
                        want.get("delete_vlans_and_ssids_mapped_to_vlans_params")
                    ),
                    "DEBUG"
                )
            # DELETE ALL condition
            elif (
                (config.get("wireless_ssids") and not updated_delete_vlans_ssids_mapped_to_vlans) or
                (self.have.get("delete_all_vlans_ssids_mapped_to_vlans") and delete_vlans_and_ssids_mapped_to_vlans)
            ):
                want["delete_vlans_and_ssids_mapped_to_vlans_params"] = (
                    self.get_create_update_remove_vlans_and_ssids_mapped_to_vlans_params(
                        updated_delete_vlans_ssids_mapped_to_vlans
                    )
                )
                self.log(
                    "State is deleted and ALL VLANs and wireless SSIDs mapped to VLANs need to be deleted in the Cisco Catalyst Center, "
                    "therefore setting 'delete_vlans_and_ssids_mapped_to_vlans_params' - []."
                )

        self.want = want
        self.log("Desired State (want): {0}".format(str(self.want)), "INFO")
        self.msg = "Successfully collected all parameters from the playbook for host onboarding operations."
        self.status = "success"
        return self

    def get_diff_merged(self):
        """
        Executes the necessary actions for add/update port assignments and channels based on the merged state.
        Returns:
            self: Returns the instance with the updated operation result and message.
        Description:
            This method determines the required actions for adding or updating port assignments and channels
            based on the desired state ("merged"). It executes the corresponding action functions and checks
            their statuses. If no actions are required, it sets the operation result to "ok" with an appropriate
            message. The method logs relevant information and updates the final message and status based on the
            execution of the actions.
        """
        self.log("Starting 'get_diff_merged' operation.", "INFO")
        result_details = {}

        action_map = {
            "add_port_assignments_params": (self.add_port_assignments, self.get_add_port_assignments_task_status),
            "update_port_assignments_params": (self.update_port_assignments, self.get_update_port_assignments_task_status),
            "add_port_channels_params": (self.add_port_channels, self.get_add_port_channels_task_status),
            "update_port_channels_params": (self.update_port_channels, self.get_update_port_channels_task_status),
            "create_update_vlans_and_ssids_mapped_to_vlans_params": (
                self.create_update_remove_vlans_and_ssids_mapped_to_vlans,
                self.get_create_update_vlans_and_ssids_mapped_to_vlans_task_status
            )
        }

        # Check if all action_map keys are missing in self.want
        if not any(action_param in self.want for action_param in action_map.keys()):
            self.msg = "Host Onboarding(Add/Update) operation(s) are not required for the provided input parameters in the Cisco Catalyst Center."
            self.set_operation_result("ok", False, self.msg, "INFO")
            return self

        final_status_list = []
        result_details = {}

        for action_param, (action_func, status_func) in action_map.items():
            # Execute the action and check its status
            req_action_param = self.want.get(action_param)
            if req_action_param:
                self.log("Executing action function: {0} with params: {1}".format(action_func.__name__, req_action_param), "INFO")
                result_task_id = action_func(req_action_param)
                self.log("Task Id: {0} returned from the action function: {1}".format(result_task_id, action_func.__name__), "DEBUG")
                status_func(result_task_id).check_return_status()
                self.log("Checked return status for Task Id: {0} using status function: {1}".format(result_task_id, status_func.__name__), "INFO")
                result = self.msg
                result_details.update(result)
                final_status_list.append(self.status)

        final_status, is_changed = self.process_final_result(final_status_list)
        self.msg = result_details
        self.log("Completed 'get_diff_merged' operation with final status: {0}, is_changed: {1}".format(final_status, is_changed), "INFO")
        self.set_operation_result(final_status, is_changed, self.msg, "INFO")
        return self

    def get_diff_deleted(self):
        """
        Executes the necessary actions for deleting port assignments and channels based on the desired state.
        Returns:
            self: Returns the instance with the updated operation result and message.
        Description:
            This method determines the required actions for deleting port assignments and channels
            based on the desired state ("deleted"). It processes the deletion of port assignments and channels,
            updates the final message based on the execution of the actions, and logs the relevant information.
        """
        self.log("Starting 'get_diff_deleted' operation.", "INFO")

        final_status_list = []
        result_details = {}

        # Process deletion of port assignments if required
        delete_port_assignments_params = self.want.get("delete_port_assignments_params")
        if delete_port_assignments_params:
            self.log("Processing deletion of port assignments.", "INFO")
            self.process_delete_port_assignments(delete_port_assignments_params).check_return_status()
            self.log("Processing deletion of port assignments completed.", "INFO")
            result = self.msg
            result_details.update(result)
            final_status_list.append(self.status)

        # Process deletion of port channels if required
        delete_port_channels_params_list = self.want.get("delete_port_channels_params")
        if delete_port_channels_params_list:
            self.log("Processing deletion of port channels.", "INFO")
            self.process_delete_port_channels(delete_port_channels_params_list).check_return_status()
            self.log("Processing deletion of port channels completed.", "INFO")
            result = self.msg
            result_details.update(result)
            final_status_list.append(self.status)

        # Process deletion go vlans and ssids mapped to vlans
        delete_vlans_and_ssids_mapped_to_vlans_params = self.want.get("delete_vlans_and_ssids_mapped_to_vlans_params")
        if delete_vlans_and_ssids_mapped_to_vlans_params:
            self.log("Processing deletion of vlans and ssids mapped to vlan.", "INFO")
            self.process_delete_vlans_and_ssids_mapped_to_vlans(delete_vlans_and_ssids_mapped_to_vlans_params).check_return_status()
            self.log("Processing deletion of vlans and ssids mapped to vlan completed.", "INFO")
            result = self.msg
            result_details.update(result)
            final_status_list.append(self.status)

        self.log("Final Statuses = {0}".format(final_status_list), "DEBUG")

        # Handle the case where no deletions are required
        if not final_status_list:
            self.msg = "No deletions were required for the provided parameters in the Cisco Catalyst Center."
            self.set_operation_result("ok", False, self.msg, "INFO")
            return self

        final_status, is_changed = self.process_final_result(final_status_list)
        self.msg = result_details
        self.log("Completed 'get_diff_deleted' operation with final status: {0}, is_changed: {1}".format(final_status, is_changed), "INFO")
        self.set_operation_result(final_status, is_changed, self.msg, "INFO")
        return self

    def verify_diff_merged(self):
        """
        Verifies the success of merged operations for port assignments, port channels and wireless SSIDs
        by comparing the current state with the desired state.
        Args:
            None
        Returns:
            self: Returns the instance after performing verification on port assignments and
            port channels.
        """
        self.log("Starting 'verify_diff_merged' operation.", "INFO")

        # Retrieve parameters for add and update operations from the desired state (self.want)
        add_port_assignments_params = self.want.get("add_port_assignments_params")
        update_port_assignments_params = self.want.get("update_port_assignments_params")
        add_port_channels_params = self.want.get("add_port_channels_params")
        update_port_channels_params = self.want.get("update_port_channels_params")
        create_update_vlans_and_ssids_mapped_to_vlans_params = self.want.get("create_update_vlans_and_ssids_mapped_to_vlans_params")

        # Verifying ADD Port Assignments operation
        if add_port_assignments_params:
            self.log("Starting verification of ADD Port Assignments operation.", "INFO")
            self.verify_port_assignments_add_operation(add_port_assignments_params)
            self.log("Completed verification of ADD Port Assignments operation.", "INFO")

        # Verifying UPDATE Port Assignments operation
        if update_port_assignments_params:
            self.log("Starting verification of UPDATE Port Assignments operation.", "INFO")
            self.verify_port_assignments_update_operation(update_port_assignments_params)
            self.log("Completed verification of UPDATE Port Assignments operation.", "INFO")

        # Verifying ADD Port Channels operation
        if add_port_channels_params:
            self.log("Starting verification of ADD Port Channels operation.", "INFO")
            self.verify_port_channels_add_operation(add_port_channels_params)
            self.log("Completed verification of ADD Port Channels operation.", "INFO")

        # Verifying UPDATE Port Channels operation
        if update_port_channels_params:
            self.log("Starting verification of UPDATE Port Channels operation.", "INFO")
            self.verify_port_channels_update_operation(update_port_channels_params)
            self.log("Completed verification of UPDATE Port Channels operation.", "INFO")

        # Verifying ADD/UPDATE VLANs and SSIDs mapped to VLANs operation
        if create_update_vlans_and_ssids_mapped_to_vlans_params:
            self.log("Starting verification of ADD/UPDATE VLANs and SSIDs mapped to VLANs operation.", "INFO")
            self.verify_vlans_and_ssids_mapped_to_vlans_create_update_operation()
            self.log("Completed verification of ADD/UPDATE VLANs and SSIDs mapped to VLANs operation.", "INFO")

        self.log("Completed 'verify_diff_merged' operation.", "INFO")
        return self

    def verify_diff_deleted(self):
        """
        Verifies the deletion operations for network configurations.
        Returns:
            self: Returns the instance of the object, allowing for method chaining.
        Description:
            This method checks and verifies deletion operations for port assignments, port channels,
            and VLANs with their mapped SSIDs based on parameters provided in the 'want' attribute.
            It logs the initiation and completion of each verification process, ensuring that all
            necessary deletions are confirmed.
        """
        self.log("Starting 'verify_diff_deleted' operation.", "INFO")

        delete_port_assignments_params = self.want.get("delete_port_assignments_params")
        delete_port_channels_params = self.want.get("delete_port_channels_params")
        delete_vlans_and_ssids_mapped_to_vlans_params = self.want.get("delete_vlans_and_ssids_mapped_to_vlans_params")

        # Verifying DELETE Port Assignments operation
        if delete_port_assignments_params:
            self.log("Starting verification of DELETE Port Assignments operation.", "INFO")
            self.verify_port_assignments_delete_operation(delete_port_assignments_params)
            self.log("Completed verification of DELETE Port Assignments operation.", "INFO")

        # Verifying DELETE Port Channels operation
        if delete_port_channels_params:
            self.log("Starting verification of DELETE Port Channels operation.", "INFO")
            self.verify_port_channels_delete_operation(delete_port_channels_params)
            self.log("Completed verification of DELETE Port Channels operation.", "INFO")

        # Verifying DELETE VLANs and SSIDs mapped to VLANs operation
        if delete_vlans_and_ssids_mapped_to_vlans_params:
            self.log("Starting verification of DELETE VLANs and SSIDs mapped to VLANs operation.", "INFO")
            self.verify_vlans_and_ssids_mapped_to_vlans_delete_operation()
            self.log("Completed verification of DELETE VLANs and SSIDs mapped to VLANs operation.", "INFO")

        self.log("Completed 'verify_diff_deleted' operation.", "INFO")
        return self


def main():
    """ main entry point for module execution
    """
    # Define the specification for the module"s arguments
    element_spec = {
        "dnac_host": {"required": True, "type": "str"},
        "dnac_port": {"type": "str", "default": "443"},
        "dnac_username": {"type": "str", "default": "admin", "aliases": ["user"]},
        "dnac_password": {"type": "str", "no_log": True},
        "dnac_verify": {"type": "bool", "default": "True"},
        "dnac_version": {"type": "str", "default": "2.2.3.3"},
        "dnac_debug": {"type": "bool", "default": False},
        "dnac_log_level": {"type": "str", "default": "WARNING"},
        "dnac_log_file_path": {"type": "str", "default": "dnac.log"},
        "dnac_log_append": {"type": "bool", "default": True},
        "dnac_log": {"type": "bool", "default": False},
        "validate_response_schema": {"type": "bool", "default": True},
        "config_verify": {"type": "bool", "default": False},
        "dnac_api_task_timeout": {"type": "int", "default": 1200},
        "dnac_task_poll_interval": {"type": "int", "default": 2},
        "config": {"required": True, "type": "list", "elements": "dict"},
        "state": {"default": "merged", "choices": ["merged", "deleted"]}
    }

    # Initialize the Ansible module with the provided argument specifications
    module = AnsibleModule(argument_spec=element_spec,
                           supports_check_mode=False)

    # Initialize the NetworkCompliance object with the module
    ccc_sda_host_port_onboarding = SDAHostPortOnboarding(module)

    if ccc_sda_host_port_onboarding.compare_dnac_versions(ccc_sda_host_port_onboarding.get_ccc_version(), "2.3.7.6") < 0:
        ccc_sda_host_port_onboarding.msg = (
            "The specified version '{0}' does not support the SDA Host Port Onboarding feature. Supported versions start "
            "  from '2.3.7.6' onwards. Version '2.3.7.6' introduces APIs for creating, updating and deleting the "
            "Port Assignments, Port Channels and Wireless SSIDs."
            .format(ccc_sda_host_port_onboarding.get_ccc_version())
        )
        ccc_sda_host_port_onboarding.set_operation_result("failed", False, ccc_sda_host_port_onboarding.msg, "ERROR").check_return_status()

    # Get the state parameter from the provided parameters
    state = ccc_sda_host_port_onboarding.params.get("state")

    # Check if the state is valid
    if state not in ccc_sda_host_port_onboarding.supported_states:
        ccc_sda_host_port_onboarding.status = "invalid"
        ccc_sda_host_port_onboarding.msg = "State {0} is invalid".format(state)
        ccc_sda_host_port_onboarding.check_return_status()

    # Validate the input parameters and check the return status
    ccc_sda_host_port_onboarding.validate_input().check_return_status()

    # Get the config_verify parameter from the provided parameters
    config_verify = ccc_sda_host_port_onboarding.params.get("config_verify")

    # Iterate over the validated configuration parameters
    for config in ccc_sda_host_port_onboarding.validated_config:
        ccc_sda_host_port_onboarding.reset_values()
        ccc_sda_host_port_onboarding.get_have(config, state).check_return_status()
        ccc_sda_host_port_onboarding.get_want(config, state).check_return_status()
        ccc_sda_host_port_onboarding.get_diff_state_apply[state]().check_return_status()

        if config_verify:
            ccc_sda_host_port_onboarding.verify_diff_state_apply[state]().check_return_status()

    module.exit_json(**ccc_sda_host_port_onboarding.result)


if __name__ == "__main__":
    main()
