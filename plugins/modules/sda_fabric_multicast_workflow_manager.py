#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright (c) 2025, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

"""Ansible module to perform operations on SDA fabric multicast in Cisco Catalyst Center."""
from __future__ import absolute_import, division, print_function

__metaclass__ = type
__author__ = ["Muthu Rakesh, Madhan Sankaranarayanan, Archit Soni"]
DOCUMENTATION = r"""
---
module: sda_fabric_multicast_workflow_manager
short_description: Manage SDA fabric multicast in Cisco
  Catalyst Center.
description:
  - Perform operations on SDA fabric multicast configurations
    and the replication mode.
  - Manages the multicast configurations like Source
    Specific Multicast (SSM) and Any Source Multicast(ASM).
  - Manages the replication mode of the multicast configuration
    associated with the L3 Virtual Network.
version_added: '6.31.0'
extends_documentation_fragment:
  - cisco.dnac.workflow_manager_params
author: Muthu Rakesh (@MUTHU-RAKESH-27) Madhan Sankaranarayanan
  (@madhansansel) Archit Soni (@koderchit)
options:
  config_verify:
    description: Set to True to verify the Cisco Catalyst
      Center after applying the playbook config.
    type: bool
    default: false
  state:
    description: The state of Cisco Catalyst Center
      after module completion.
    type: str
    choices: [merged, deleted]
    default: merged
  config:
    description:
      - A list of SDA fabric multicast configurations
        associated with fabric sites.
      - Each entry in the list represents multicast
        settings for a specific fabric site.
    type: list
    elements: dict
    required: true
    suboptions:
      fabric_multicast:
        description: Configuration details for SDA fabric
          multicast configurations associated with a
          fabric site.
        type: list
        elements: dict
        suboptions:
          fabric_name:
            description:
              - Name of the SDA fabric site.
              - Mandatory parameter for all operations
                under fabric_multicast.
              - The fabric site must already exist before
                configuring multicast settings.
              - A Fabric Site is composed of networking
                devices operating in SD-Access Fabric
                roles.
              - A fabric site consists of networking
                devices operating in SD-Access Fabric
                roles, including Border Nodes, Control
                Plane Nodes, Edge Nodes, Fabric Wireless
                LAN Controllers, and Fabric Wireless
                Access Points.
              - A Fabric sites may also include Fabric
                Wireless LAN Controllers and Fabric
                Wireless Access Points.
              - Updating this field is not allowed.
              - To delete the entire multicast configuration,
                provide only the 'fabric_name' and 'layer3_virtual_network'.
              - To delete only SSM or ASM configurations,
                provide the corresponding 'ssm' and/or
                'asm' fields.
            type: str
            required: true
          layer3_virtual_network:
            description:
              - Name of the Layer 3 Virtual Network
                (L3VN) associated with the multicast
                configuration.
              - A L3VN is a logically isolated network
                that enables IP routing between different
                subnets while maintaining separation
                from other virtual networks.
              - Mandatory parameter for all operations
                under fabric_multicast.
              - The Layer 3 Virtual Network must be
                created and associated with the fabric
                site and its fabric zones before configuring
                multicast.
              - The created L3 Virtual Network should
                be associated with the fabric site and
                its fabric zones.
              - Updating this field is not allowed after
                creation.
              - To delete the entire multicast configuration,
                provide only the 'fabric_name' and 'layer3_virtual_network'.
              - To delete only the SSM or ASM configurations,
                provide the corresponding 'ssm' and/or
                'asm' fields.
            type: str
            required: true
          replication_mode:
            description: >
              Specifies how multicast traffic is replicated
              within the fabric site. Two replication
              modes are supported: Native Multicast
              and Headend Replication. Native Multicast
              forwards multicast traffic using traditional
              multicast routing protocols such as PIM,
                building
              distribution trees to efficiently deliver
              traffic to multiple receivers. Headend
              Replication replicates multicast packets
              at the source node without using multicast
              routing protocols. Mandatory parameter
              while adding the multicast configuration
              to the fabric site.
            type: str
            choices: [NATIVE_MULTICAST, HEADEND_REPLICATION]
          ip_pool_name:
            description:
              - Name of the IP address pool allocated
                for communication between the SDA fabric
                and external networks.
              - Denotes the IP address range allocated
                for communication between the SDA fabric
                and external networks.
              - Mandatory parameter while adding the
                multicast configuration to the fabric
                site.
              - When multicast is enabled in the fabric
                site, each device operating as a Border
                Node or Edge Node is provisioned with
                an IP address per Virtual Network, used
                for multicast signaling.
              - The IP pool must be reserved in the
                fabric site before multicast configuration.
              - Updating this field is not allowed.
            type: str
          ssm:
            description:
              - PIM Source-Specific Multicast (PIM-SSM)
                configures the multicast tree with the
                source as the root.
              - Either SSM or ASM is mandatory when
                adding multicast configurations to the
                fabric site.
              - When the state is set to 'deleted' and
                SSM is provided, only the SSM ranges
                will be removed.
              - When removing SSM ranges, ASM configurations
                must be present.
              - To delete the entire multicast configuration,
                provide only the 'fabric_name' and 'layer3_virtual_network'.
              - To delete only the SSM or ASM configurations,
                provide the respective 'ssm' or 'asm'
                parameter.
            type: str
            suboptions:
              ipv4_ssm_ranges:
                description:
                  - The IPv4 range for Source-Specific
                    Multicast (SSM), where receivers
                    specify both the multicast group
                    (G) and the source (S) for receiving
                    traffic, enhancing security and
                    efficiency.
                  - Mandatory parameter when the ssm
                    is provided.
                type: list
                elements: str
                required: true
          asm:
            description:
              - PIM Any-Source Multicast (PIM-ASM) allows
                receivers to join a multicast group
                without specifying a particular source.
              - The root of the multicast tree is the
                Rendezvous Point (RP), which forwards
                multicast traffic to receivers.
              - Either SSM or ASM must be provided when
                configuring multicast for the fabric
                site.
              - When the state is 'deleted' and if the
                asm is provided, only the asm ranges
                will be removed.
              - If removing ASM ranges, ensure that
                SSM configurations are also present.
              - To delete the entire multicast configuration,
                provide only the 'fabric_name' and 'layer3_virtual_network'.
              - To delete only the SSM or ASM configurations,
                provide the respective 'ssm' or 'asm'
                parameter.
            type: str
            suboptions:
              rp_device_location:
                description:
                  - Specifies the location of the Rendezvous
                    Point (RP) in the multicast network.
                  - Mandatory parameter when configuring
                    ASM.
                  - When the location is 'FABRIC', the
                    RP is within the SD-Access fabric
                    (typically on a Border, Control
                    Plane, or Edge node).
                  - When the location is 'EXTERNAL',
                    the RP is outside the SD-Access
                    fabric, requiring interconnectivity
                    between the fabric and external
                    multicast networks.
                type: str
                choices: [EXTERNAL, FABRIC]
                required: true
              network_device_ips:
                description:
                  - Specifies the IP addresses of devices
                    within the SD-Access fabric to be
                    used as the RP.
                  - A maximum of two device IPs can
                    be provided.
                  - All the device IPs provided should
                    be provisioned to the fabric site.
                  - For Edge node RPs, only one device
                    should be provided.
                  - If using a Single Stack reserved
                    pool, only one device should be
                    provided.
                type: list
                elements: str
              ex_rp_ipv4_address:
                description:
                  - The IPv4 address of the external
                    RP when the RP device location is
                    set to 'EXTERNAL'.
                  - Either 'ex_rp_ipv4_address' or 'ex_rp_ipv6_address'
                    is required when adding the multicast
                    configuration.
                  - If both 'ex_rp_ipv4_address' and
                    'ex_rp_ipv6_address' are provided,
                    'ex_rp_ipv4_address' takes priority.
                    The second address can be provided
                    as the next element in the list
                    if needed.
                type: str
              is_default_v4_rp:
                description:
                  - A flag that indicates whether the
                    IPv4 RP is the default RP for the
                    multicast domain.
                  - If set to 'true', this RP is used
                    for all multicast groups that do
                    not have a specific RP assigned.
                  - Either 'is_default_v4_rp' or 'ipv4_asm_ranges'
                    must be provided when 'ex_rp_ipv4_address'
                    is used.
                  - The 'ipv4_asm_ranges' will take
                    priority over 'is_default_v4_rp'
                    if both are specified.
                type: bool
              ipv4_asm_ranges:
                description:
                  - A range used exclusively for Any-Source
                    Multicast (ASM), where receivers
                    specify both the source (S) and
                    the group (G) for receiving multicast
                    traffic.
                  - Either 'is_default_v4_rp' or 'ipv4_asm_ranges'
                    must be provided when 'ex_rp_ipv4_address'
                    is used.
                  - The 'ipv4_asm_ranges' takes priority
                    over 'is_default_v4_rp' if both
                    are provided.
                  - The ranges provided for 'ipv4_asm_ranges'
                    should not overlap with the ranges
                    provided for 'ipv4_ssm_ranges' or
                    any other external IP ranges.
                type: list
                elements: str
              ex_rp_ipv6_address:
                description:
                  - This refers to the IPv6 address
                    of the External RP when the RP Device
                    Location is set to EXTERNAL.
                  - Either 'ex_rp_ipv4_address' or 'ex_rp_ipv6_address'
                    is mandatory while adding the multicast
                    configurations to the fabric site.
                  - If both the 'ex_rp_ipv4_address'
                    and 'ex_rp_ipv6_address' is passed,
                    'ex_rp_ipv4_address' will given
                    priority. Provide either one in
                    an element and carry over the other
                    to the next element of the list.
                type: str
              is_default_v6_rp:
                description:
                  - A flag that indicates whether the
                    IPv6 RP is the default RP for the
                    multicast domain.
                  - If set to 'true', this RP is used
                    for all multicast groups that do
                    not have a specific RP assigned.
                  - Either 'is_default_v6_rp' or 'ipv6_asm_ranges'
                    must be provided when 'ex_rp_ipv6_address'
                    is used.
                  - The 'ipv6_asm_ranges' will take
                    priority over 'is_default_v6_rp'
                    if both are specified.
                type: bool
              ipv6_asm_ranges:
                description:
                  - A range used exclusively for Any-Source
                    Multicast (ASM), where receivers
                    specify both the source (S) and
                    the group (G) for receiving multicast
                    traffic.
                  - Either 'is_default_v6_rp' or 'ipv6_asm_ranges'
                    must be provided when 'ex_rp_ipv6_address'
                    is used.
                  - The 'ipv6_asm_ranges' takes priority
                    over 'is_default_v6_rp' if both
                    are provided.
                type: list
                elements: str
requirements:
  - dnacentersdk >= 2.10.2
  - python >= 3.9
notes:
  - SDK Method used are
    site_design.SiteDesign.get_sites,
    network_settings.NetworkSettings.get_reserve_ip_subpool,
    devices.Devices.get_device_list,
    sda.Sda.get_layer3_virtual_networks,
    sda.Sda.get_fabric_sites,
    sda.Sda.get_fabric_zones,
    sda.Sda.get_provisioned_devices,
    sda.Sda.get_multicast_virtual_networks_v1,
    sda.Sda.get_multicast_v1,
    sda.Sda.add_multicast_virtual_networks_v1,
    sda.Sda.update_multicast_v1,
    sda.Sda.update_multicast_virtual_networks_v1,
    sda.Sda.delete_multicast_virtual_network_by_id_v1,
    task.Task.get_tasks_by_id,
    task.Task.get_task_details_by_id,
  - Paths used are
    get /dna/intent/api/v1/sites get
    /dna/intent/api/v1/reserve-ip-subpool get /dna/intent/api/v1/network-device
    get /dna/intent/api/v1/sda/layer3VirtualNetworks
    get /dna/intent/api/v1/sda/fabricSites get /dna/intent/api/v1/sda/fabricZones
    get /dna/intent/api/v1/sda/provisionDevices get
    /dna/intent/api/v1/sda/multicast/virtualNetworks
    get /dna/intent/api/v1/sda/multicast post /dna/intent/api/v1/sda/multicast/virtualNetworks
    put /dna/intent/api/v1/sda/multicast put /dna/intent/api/v1/sda/multicast/virtualNetworks
    delete /dna/intent/api/v1/sda/multicast/virtualNetworks/${id}
    get /dna/intent/api/v1/tasks/${id} get /dna/intent/api/v1/tasks/${id}/detail
"""

EXAMPLES = r"""
---
- name: Configure the SDA multicast on a L3 virtual
    network under a fabric site
  cisco.dnac.sda_fabric_multicast_workflow_manager:
    dnac_host: "{{ dnac_host }}"
    dnac_username: "{{ dnac_username }}"
    dnac_password: "{{ dnac_password }}"
    dnac_verify: "{{ dnac_verify }}"
    dnac_port: "{{ dnac_port }}"
    dnac_version: "{{ dnac_version }}"
    dnac_debug: "{{ dnac_debug }}"
    dnac_log: true
    dnac_log_level: "{{ dnac_log_level }}"
    state: merged
    config_verify: true
    config:
      - fabric_multicast:
          - fabric_name: "Global/USA/SAN JOSE"
            layer3_virtual_network: "L3_VN_MUL_1"
            replication_mode: NATIVE_MULTICAST
            ip_pool_name: ip_pool_dual_mul
            ssm:
              ipv4_ssm_ranges:
                - "225.0.0.0/8"
                - "226.0.0.0/8"
            asm:
              - rp_device_location: "FABRIC"
                network_device_ips:
                  - "204.1.2.3"
                is_default_v4_rp: true
- name: Update the ssm configuration on a L3 virtual
    network under a fabric site
  cisco.dnac.sda_fabric_multicast_workflow_manager:
    dnac_host: "{{ dnac_host }}"
    dnac_username: "{{ dnac_username }}"
    dnac_password: "{{ dnac_password }}"
    dnac_verify: "{{ dnac_verify }}"
    dnac_port: "{{ dnac_port }}"
    dnac_version: "{{ dnac_version }}"
    dnac_debug: "{{ dnac_debug }}"
    dnac_log: true
    dnac_log_level: "{{ dnac_log_level }}"
    state: merged
    config_verify: true
    config:
      - fabric_multicast:
          - fabric_name: "Global/USA/SAN JOSE"
            layer3_virtual_network: "L3_VN_MUL_1"
            ssm:
              ipv4_ssm_ranges:
                - "227.0.0.0/8"
- name: Update the asm configuration on a L3 virtual
    network under a fabric site
  cisco.dnac.sda_fabric_multicast_workflow_manager:
    dnac_host: "{{ dnac_host }}"
    dnac_username: "{{ dnac_username }}"
    dnac_password: "{{ dnac_password }}"
    dnac_verify: "{{ dnac_verify }}"
    dnac_port: "{{ dnac_port }}"
    dnac_version: "{{ dnac_version }}"
    dnac_debug: "{{ dnac_debug }}"
    dnac_log: true
    dnac_log_level: "{{ dnac_log_level }}"
    state: merged
    config_verify: true
    config:
      - fabric_multicast:
          - fabric_name: "Global/USA/SAN JOSE"
            layer3_virtual_network: "L3_VN_MUL_1"
            asm:
              - rp_device_location: "EXTERNAL"
                ex_rp_ipv4_address: "10.0.0.1"
                ipv4_asm_ranges:
                  - "232.0.0.0/8"
                  - "233.0.0.0/8"
                ex_rp_ipv6_address: "2001::1"
                ipv6_asm_ranges:
                  - "FF01::/64"
                  - "FF02::/64"
              - rp_device_location: "EXTERNAL"
                ex_rp_ipv4_address: "10.0.0.2"
                ipv4_asm_ranges:
                  - "234.0.0.0/8"
                  - "235.0.0.0/8"
                ex_rp_ipv6_address: "2001::2"
                ipv6_asm_ranges:
                  - "FF02::/64"
                  - "FF04::/64"
- name: Update the replication mode of the SDA multicast
    configurations under a fabric site
  cisco.dnac.sda_fabric_multicast_workflow_manager:
    dnac_host: "{{ dnac_host }}"
    dnac_username: "{{ dnac_username }}"
    dnac_password: "{{ dnac_password }}"
    dnac_verify: "{{ dnac_verify }}"
    dnac_port: "{{ dnac_port }}"
    dnac_version: "{{ dnac_version }}"
    dnac_debug: "{{ dnac_debug }}"
    dnac_log: true
    dnac_log_level: "{{ dnac_log_level }}"
    state: merged
    config_verify: true
    config:
      - fabric_multicast:
          - fabric_name: "Global/USA/SAN JOSE"
            layer3_virtual_network: "L3_VN_MUL_1"
            replication_mode: "HEADEND_REPLICATION"
- name: Delete the source '226.0.0.0/8' from the ssm
    multicast configuration
  cisco.dnac.sda_fabric_multicast_workflow_manager:
    dnac_host: "{{ dnac_host }}"
    dnac_username: "{{ dnac_username }}"
    dnac_password: "{{ dnac_password }}"
    dnac_verify: "{{ dnac_verify }}"
    dnac_port: "{{ dnac_port }}"
    dnac_version: "{{ dnac_version }}"
    dnac_debug: "{{ dnac_debug }}"
    dnac_log: true
    dnac_log_level: "{{ dnac_log_level }}"
    state: deleted
    config_verify: true
    config:
      - fabric_multicast:
          - fabric_name: "Global/USA/SAN JOSE"
            layer3_virtual_network: "L3_VN_MUL_1"
            ssm:
              ipv4_ssm_ranges:
                - "226.0.0.0/8"
- name: Delete the RP '10.0.0.1' from the asm multicast
    configuration
  cisco.dnac.sda_fabric_multicast_workflow_manager:
    dnac_host: "{{ dnac_host }}"
    dnac_username: "{{ dnac_username }}"
    dnac_password: "{{ dnac_password }}"
    dnac_verify: "{{ dnac_verify }}"
    dnac_port: "{{ dnac_port }}"
    dnac_version: "{{ dnac_version }}"
    dnac_debug: "{{ dnac_debug }}"
    dnac_log: true
    dnac_log_level: "{{ dnac_log_level }}"
    state: deleted
    config_verify: true
    config:
      - fabric_multicast:
          - fabric_name: "Global/USA/SAN JOSE"
            layer3_virtual_network: "L3_VN_MUL_1"
            asm:
              - rp_device_location: "EXTERNAL"
                ex_rp_ipv4_address: "10.0.0.1"
- name: Delete the SDA multicast configurations of the
    L3 virtual network from the fabric site.
  cisco.dnac.sda_fabric_multicast_workflow_manager:
    dnac_host: "{{ dnac_host }}"
    dnac_username: "{{ dnac_username }}"
    dnac_password: "{{ dnac_password }}"
    dnac_verify: "{{ dnac_verify }}"
    dnac_port: "{{ dnac_port }}"
    dnac_version: "{{ dnac_version }}"
    dnac_debug: "{{ dnac_debug }}"
    dnac_log: true
    dnac_log_level: "{{ dnac_log_level }}"
    state: deleted
    config_verify: true
    config:
      - fabric_multicast:
          - fabric_name: "Global/USA/SAN JOSE"
            layer3_virtual_network: "L3_VN_MUL_1"
"""

RETURN = r"""
# Case_1: Successful configuration of SDA fabric multicast on a L3 VN under a site
response_1:
  description: A dictionary or list with the response returned by the Cisco Catalyst Center Python SDK
  returned: always
  type: dict
  sample: >
    {
      "response": {
        "taskId": "str",
        "url": "str"
      },
      "version": "str"
    }
# Case_2: Successful configuration update of SDA fabric multicast on a L3 VN under a site
response_2:
  description: A dictionary or list with the response returned by the Cisco Catalyst Center Python SDK
  returned: always
  type: dict
  sample: >
    {
      "response": {
        "taskId": "str",
        "url": "str"
      },
      "version": "str"
    }
# Case_3: Successful updation of the replication mode
response_3:
  description: A dictionary or list with the response returned by the Cisco Catalyst Center Python SDK
  returned: always
  type: dict
  sample: >
    {
      "response": {
        "taskId": "str",
        "url": "str"
      },
      "version": "str"
    }
# Case_4: Successful deletion of SDA fabric multicast configuration on a L3 VN under a site
response_4:
  description: A dictionary or list with the response returned by the Cisco Catalyst Center Python SDK
  returned: always
  type: dict
  sample: >
    {
      "response": {
        "taskId": "str",
        "url": "str"
      },
      "version": "str"
    }
"""

import time
import copy
from ansible.module_utils.basic import AnsibleModule
from ansible_collections.cisco.dnac.plugins.module_utils.dnac import (
    DnacBase,
    validate_list_of_dicts,
    get_dict_result,
)


class FabricMulticast(DnacBase):
    """Class containing member attributes for sda_fabric_multicast_workflow_manager module"""

    def __init__(self, module):
        super().__init__(module)
        self.response = []
        self.multicast_vn_obj_params = self.get_obj_params("multicast_vn")
        self.replication_mode_obj_params = self.get_obj_params("replication_mode")
        self.max_timeout = self.params.get("dnac_api_task_timeout")

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
            "fabric_multicast": {
                "type": "list",
                "elements": "dict",
                "fabric_name": {"type": "str", "required": True},
                "replication_mode": {
                    "type": "str",
                    "choices": ["NATIVE_MULTICAST", "HEADEND_REPLICATION"],
                    "default": "NATIVE_MULTICAST",
                },
                "layer3_virtual_network": {"type": "str"},
                "ip_pool_name": {"type": "str"},
                "ssm": {
                    "type": "dict",
                    "ip_pool_name": {"type": "list", "elements": "str"},
                },
                "asm": {
                    "type": "list",
                    "elements": "dict",
                    "rp_device_location": {
                        "type": "str",
                        "choices": ["FABRIC", "EXTERNAL"],
                        "default": "FABRIC",
                    },
                    "network_device_ips": {
                        "type": "list",
                        "elements": "str",
                    },
                    "ex_rp_ipv4_address": {"type": "str"},
                    "is_default_v4_rp": {"type": "bool"},
                    "ipv4_asm_ranges": {"type": "list", "elements": "str"},
                    "ex_rp_ipv6_address": {"type": "str"},
                    "is_default_v6_rp": {"type": "bool"},
                    "ipv6_asm_ranges": {"type": "list", "elements": "str"},
                },
            }
        }

        # Validate playbook params against the specification (temp_spec)
        valid_temp, invalid_params = validate_list_of_dicts(self.config, temp_spec)
        if invalid_params:
            self.msg = "Invalid parameters in playbook: {invalid_params}".format(
                invalid_params="\n".join(invalid_params)
            )
            self.set_operation_result(
                "failed", False, self.msg, "ERROR"
            ).check_return_status()

        self.validated_config = valid_temp
        self.log(
            "Successfully validated playbook config params: {valid_temp}".format(
                valid_temp=valid_temp
            ),
            "INFO",
        )
        self.msg = "Successfully validated input from the playbook."
        self.status = "success"
        return self

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

        if get_object == "multicast_vn":
            obj_params = [
                ("fabricId", "fabricId"),
                ("virtualNetworkName", "virtualNetworkName"),
                ("ipPoolName", "ipPoolName"),
                ("ipv4SsmRanges", "ipv4SsmRanges"),
                ("multicastRPs", "multicastRPs"),
            ]
        elif get_object == "replication_mode":
            obj_params = [("replicationMode", "replicationMode")]
        else:
            raise ValueError(
                "Received an unexpected value for 'get_object': {object_name}".format(
                    object_name=get_object
                )
            )

        return obj_params

    def check_valid_virtual_network_name(self, virtual_network_name):
        """
        Check if the given L3 virtual network name exists.

        Parameters:
            virtual_network_name (str): The name of the L3 virtual network.
        Returns:
            True or False (bool): True if the L3 virtual network exists. Else, return False.
        Description:
            Calls the 'get_layer3_virtual_networks' API with the given virtual network name.
            If a matching virtual network is found, returns True.
            If no matching network is found, or if there is an error, returns False.
        """

        self.log(
            "Starting to check if virtual network exists: '{name}'.".format(
                name=virtual_network_name
            ),
            "DEBUG",
        )
        try:
            virtual_network_details = self.dnac._exec(
                family="sda",
                function="get_layer3_virtual_networks",
                params={
                    "virtual_network_name": virtual_network_name,
                },
            )
            self.log(
                "Response received from 'get_layer3_virtual_networks': {response}".format(
                    response=virtual_network_details
                ),
                "DEBUG",
            )

            if not isinstance(virtual_network_details, dict):
                self.msg = "Error in getting virtual network details - Response is not a dictionary"
                self.log(self.msg, "CRITICAL")
                self.set_operation_result(
                    "failed", False, self.msg, "ERROR"
                ).check_return_status()

            # if the SDK returns no response, then the virtual network does not exist
            virtual_network_details = virtual_network_details.get("response")
            if not virtual_network_details:
                self.log(
                    "There is no L3 virtual network with the name '{name}'.".format(
                        name=virtual_network_name
                    ),
                    "DEBUG",
                )
                return False

            self.log(
                "L3 virtual network '{name}' exists.".format(name=virtual_network_name),
                "DEBUG",
            )

        except Exception as e:
            self.msg = "Exception occurred while running the API 'get_layer3_virtual_networks': {error_msg}".format(
                error_msg=str(e)
            )
            self.log(self.msg, "CRITICAL")
            self.set_operation_result(
                "failed", False, self.msg, "ERROR"
            ).check_return_status()

        return True

    def check_valid_reserved_pool(self, reserved_pool_name, fabric_name):
        """
        Check if a reserved IP pool exists within a given fabric site.

        Parameters:
            reserved_pool_name (str): The name of the reserved pool.
            fabric_name (str): The name of the fabric site.
        Returns:
            True or False (bool): True if the reserved pool exists. Else, return False.
        Description:
            Call the API 'get_reserve_ip_subpool' by setting the 'site_id' and 'offset' field.
            Iterates through paginated results to find a reserved pool with the given name.
            If found, returns True. If not found or an error occurs, returns False.
        """

        self.log(
            "Starting to check for reserved pool '{pool_name}' in fabric '{fabric_name}'.".format(
                pool_name=reserved_pool_name, fabric_name=fabric_name
            ),
            "DEBUG",
        )
        try:
            (site_exists, site_id) = self.get_site_id(fabric_name)
            self.log(
                "The site with the name '{site_name} exists in Cisco Catalyst Center is '{site_exists}'".format(
                    site_name=fabric_name, site_exists=site_exists
                ),
                "DEBUG",
            )
            if not site_id:
                self.msg = (
                    "The site with the hierarchy name '{site_name}' is invalid.".format(
                        site_name=fabric_name
                    )
                )
                self.set_operation_result(
                    "failed", False, self.msg, "ERROR"
                ).check_return_status()

            offset = 1
            start_time = time.time()

            self.log(
                "Calling API 'get_reserve_ip_subpool' with site_id '{site_id}' and offset '{offset}'.".format(
                    site_id=site_id, offset=offset
                ),
                "DEBUG",
            )
            while True:
                all_reserved_pool_details = self.dnac._exec(
                    family="network_settings",
                    function="get_reserve_ip_subpool",
                    params={"site_id": site_id, "offset": offset},
                )
                self.log(
                    "Response received from 'get_reserve_ip_subpool': {response}".format(
                        response=all_reserved_pool_details
                    ),
                    "DEBUG",
                )

                if not isinstance(all_reserved_pool_details, dict):
                    self.msg = (
                        "Error in getting reserve pool - Response is not a dictionary"
                    )
                    self.log(self.msg, "CRITICAL")
                    self.set_operation_result(
                        "failed", False, self.msg, "ERROR"
                    ).check_return_status()

                offset += 25
                all_reserved_pool_details = all_reserved_pool_details.get("response")
                if not all_reserved_pool_details:
                    self.log(
                        "There is no reserved subpool in the site '{site_name}'.".format(
                            site_name=fabric_name
                        ),
                        "DEBUG",
                    )
                    return False

                # Check for maximum timeout, default value is 1200 seconds
                if (time.time() - start_time) >= self.max_timeout:
                    self.msg = "Max timeout of {0} sec has reached for the API 'get_reserved_ip_subpool' status.".format(
                        self.max_timeout
                    )
                    self.log(self.msg, "CRITICAL")
                    self.status = "failed"
                    return True

                # Find the reserved pool with the given name in the list of reserved pools
                reserved_pool_details = get_dict_result(
                    all_reserved_pool_details, "groupName", reserved_pool_name
                )
                if reserved_pool_details:
                    self.log(
                        "The reserved pool '{reserved_pool}' found in the site '{site_name}'.".format(
                            reserved_pool=reserved_pool_name, site_name=fabric_name
                        ),
                        "DEBUG",
                    )
                    return True

                self.log(
                    "No matching reserved pool found for '{pool}' in site '{site_name}' at offset '{offset}'."
                    "Continuing to next offset.".format(
                        pool=reserved_pool_name, site_name=fabric_name, offset=offset
                    ),
                    "DEBUG",
                )
        except Exception as e:
            self.msg = "Exception occurred while running the API 'get_reserve_ip_subpool': {error_msg}".format(
                error_msg=e
            )
            self.log(self.msg, "CRITICAL")
            self.set_operation_result(
                "failed", False, self.msg, "ERROR"
            ).check_return_status()

        return True

    def get_fabric_site_id_from_name(self, site_name, site_id):
        """
        Get the fabric ID from the given site hierarchy name.

        Parameters:
            site_name (str): The name of the site.
            site_id (str): The ID of the site.
        Returns:
            fabric_site_id (str): The ID of the fabric site, or None if not found or invalid.
        Description:
            Calls the API 'get_fabric_sites' by setting the 'site_id' field.
            If an error occurs or the site is not a fabric site, returns None.
        """

        self.log(
            "Attempting to retrieve fabric site details for site ID '{site_id}' and site name '{site_name}'.".format(
                site_id=site_id, site_name=site_name
            ),
            "DEBUG",
        )
        fabric_site_id = None
        try:
            fabric_site_exists = self.dnac._exec(
                family="sda",
                function="get_fabric_sites",
                params={"site_id": site_id},
            )
            self.log(
                "Response received from 'get_fabric_sites': {response}".format(
                    response=fabric_site_exists
                ),
                "DEBUG",
            )

            # If the status is 'failed', then the site is not a fabric
            if not isinstance(fabric_site_exists, dict):
                self.msg = "Error in getting fabric site details - Response is not a dictionary"
                self.log(self.msg, "CRITICAL")
                self.set_operation_result(
                    "failed", False, self.msg, "ERROR"
                ).check_return_status()

            # if the SDK returns no response, then the virtual network does not exist
            fabric_site_exists = fabric_site_exists.get("response")
            if not fabric_site_exists:
                self.log(
                    "The site hierarchy 'fabric_site' {site_name} is not a valid one or it is not a 'Fabric' site.".format(
                        site_name=site_name
                    ),
                    "ERROR",
                )
                return fabric_site_id

            self.log(
                "The site hierarchy 'fabric_site' {fabric_name} is a valid fabric site.".format(
                    fabric_name=site_name
                ),
                "DEBUG",
            )
            if not isinstance(fabric_site_exists, list):
                self.msg = (
                    "Error in getting fabric site details - Response is not a list."
                )
                self.log(self.msg, "CRITICAL")
                self.set_operation_result(
                    "failed", False, self.msg, "ERROR"
                ).check_return_status()

            fabric_site_id = fabric_site_exists[0].get("id")
            self.log(
                "Fabric site ID retrieved successfully: {fabric_site_id}".format(
                    fabric_site_id=fabric_site_id
                ),
                "DEBUG",
            )
        except Exception as e:
            self.msg = "Exception occurred while running the API 'get_fabric_sites': {error_msg}".format(
                error_msg=e
            )
            self.log(self.msg, "CRITICAL")
            self.set_operation_result(
                "failed", False, self.msg, "ERROR"
            ).check_return_status()

        return fabric_site_id

    def get_fabric_zone_id_from_name(self, site_name, site_id):
        """
        Get the fabric zone ID from the given site hierarchy name.

        Parameters:
            site_name (str): The name of the site.
            site_id (str): The ID of the zone.
        Returns:
            fabric_zone_id (str): The ID of the fabric zone, or None if not found.
        Description:
            Call the API 'get_fabric_zones' by setting the 'site_name_hierarchy' field with the
            given site name.
            If no valid fabric zone is found, returns None. Else, return the fabric site ID.
        """

        self.log(
            "Attempting to retrieve fabric site details for site ID '{site_id}' and site name '{site_name}'.".format(
                site_id=site_id, site_name=site_name
            ),
            "DEBUG",
        )
        fabric_zone_id = None
        try:
            fabric_zone = self.dnac._exec(
                family="sda",
                function="get_fabric_zones",
                params={"site_id": site_id},
            )
            self.log(
                "Response received from 'get_fabric_zones': {response}".format(
                    response=fabric_zone
                ),
                "DEBUG",
            )

            # If the status is 'failed', then the zone is not a fabric
            if not isinstance(fabric_zone, dict):
                self.msg = "Error in getting fabric zone details - Response is not a dictionary"
                self.log(self.msg, "CRITICAL")
                self.set_operation_result(
                    "failed", False, self.msg, "ERROR"
                ).check_return_status()

            # if the SDK returns no response, then the virtual network does not exist
            fabric_zone = fabric_zone.get("response")
            if not fabric_zone:
                self.log(
                    "No fabric zone found for site '{site_name}'.".format(
                        site_name=site_name
                    ),
                    "ERROR",
                )
                return fabric_zone_id

            self.log(
                "Fabric zone found for site '{site_name}'.".format(site_name=site_name),
                "DEBUG",
            )
            fabric_zone_id = fabric_zone[0].get("id")
            self.log(
                "Fabric zone ID retrieved successfully: {fabric_zone_id}".format(
                    fabric_zone_id=fabric_zone_id
                ),
                "DEBUG",
            )
        except Exception as e:
            self.msg = "Exception occurred while running the API 'get_fabric_zones': {error_msg}".format(
                error_msg=e
            )
            self.log(self.msg, "CRITICAL")
            self.set_operation_result(
                "failed", False, self.msg, "ERROR"
            ).check_return_status()

        return fabric_zone_id

    def check_device_is_provisioned(
        self, fabric_device_ip, device_id, site_id, site_name
    ):
        """
        Check if the device with the given IP is provisioned to the site or not.

        Parameters:
            fabric_device_ip (str): The IP address of the network device.
            device_id (str): The ID of the network device.
            site_id (str): The ID of the fabric site.
            site_name (str): The name of the fabric site.
        Returns:
            self: The current object with updated desired Fabric Devices information.
        Description:
            Call the API 'get_provisioned_devices' by setting the 'network_device_id'
            and 'site_id' fields with the device ID and the site ID.
            If the response is empty, return self by setting the self.msg and
            self.status as 'failed'.
        """

        self.log(
            "Checking provision status for device ID '{device_id}' with IP '{device_ip}' at site '{site_name}'.".format(
                device_id=device_id, device_ip=fabric_device_ip, site_name=site_name
            ),
            "DEBUG",
        )
        try:
            provisioned_device_details = self.dnac._exec(
                family="sda",
                function="get_provisioned_devices",
                params={"network_device_id": device_id, "site_id": site_id},
            )
            self.log(
                "Response received from 'get_provisioned_devices': {response}".format(
                    response=provisioned_device_details
                ),
                "DEBUG",
            )

            # If the response returned from the SDK is None, then the device is not provisioned to the site.
            provisioned_device_details = provisioned_device_details.get("response")
            if not provisioned_device_details:
                self.msg = "The network device with the IP address '{device_ip}' is not provisioned to the site '{site_name}'.".format(
                    device_ip=fabric_device_ip, site_name=site_name
                )
                self.log(self.msg, "ERROR")
                self.set_operation_result(
                    "failed", False, self.msg, "ERROR"
                ).check_return_status()

        except Exception as e:
            self.msg = "Exception occurred while running the API 'get_provisioned_devices': {error_msg}".format(
                error_msg=e
            )
            self.log(self.msg, "CRITICAL")
            self.status = "failed"

        if self.status != "failed":
            self.log(
                "The network device with the IP address '{device_ip}' is provisioned to the site '{site_name}'.".format(
                    device_ip=fabric_device_ip, site_name=site_name
                ),
                "DEBUG",
            )

        return self

    def format_fabric_multicast_params(
        self, fabric_name, l3_vn, fabric_multicast_details
    ):
        """
        Process the multicast configuration parameters retrieved from the Cisco Catalyst Center.

        Parameters:
            fabric_name (str): The name of the fabric site.
            l3_vn (str): The name of the Layer 3 Virtual Network.
            fabric_multicast_details (dict): The multicast configuration details from the Cisco Catalyst Center.
        Returns:
            fabric_multicast_info (dict): Processed multicast configuration data in a format
            suitable for Cisco Catalyst Center API payload.
        Description:
            Form a dict with the params which is in accordance with the API payload structure.
        """

        fabric_multicast_info = {}
        multicast_data = fabric_multicast_details[0]
        fabric_multicast_info.update(
            {
                "fabricId": multicast_data.get("fabricId"),
                "virtualNetworkName": multicast_data.get("virtualNetworkName"),
                "ipPoolName": multicast_data.get("ipPoolName"),
                "ipv4SsmRanges": multicast_data.get("ipv4SsmRanges"),
                "multicastRPs": multicast_data.get("multicastRPs"),
            }
        )

        # Formatted payload for the SDK 'Add multicast virtual networks', 'Update multicast virtual networks'
        self.log(
            "The multicast configuration details of the fabric site '{fabric_name}' for the '{l3_vn}' are '{multicast_info}'".format(
                fabric_name=fabric_name,
                l3_vn=l3_vn,
                multicast_info=fabric_multicast_info,
            ),
            "DEBUG",
        )
        return fabric_multicast_info

    def format_replication_mode_params(self, fabric_name, replication_mode_details):
        """
        Process the multicast configuration parameters retrieved from the Cisco Catalyst Center.

        Parameters:
            fabric_name (str): The name of the fabric site.
            replication_mode_details (dict): The replication mode multicast configuration details from the Cisco Catalyst Center.
        Returns:
            replication_mode_info (dict): Processed replication mode multicast configuration data in a format
            suitable for Cisco Catalyst Center API payload.
        Description:
            Form a dict with the params which is in accordance with the API payload structure.
        """

        replication_mode_info = {}
        replication_data = replication_mode_details[0]
        replication_mode_info.update(
            {
                "fabricId": replication_data.get("fabricId"),
                "replicationMode": replication_data.get("replicationMode"),
            }
        )

        # Formatted payload for the SDK 'Update multicast'
        self.log(
            "The replication mode of the multicast configuration in the fabric site '{fabric_name}' are '{replication_mode_info}'".format(
                fabric_name=fabric_name, replication_mode_info=replication_mode_info
            ),
            "DEBUG",
        )
        return replication_mode_info

    def get_fabric_multicast_details(self, fabric_name, multicast_get_params):
        """
        Get the multicast configuration for the given fabric name from the Cisco Catalyst Center.

        Parameters:
            fabric_name (str): The name of the fabric site.
            multicast_get_params (dict): The payload for the 'get_multicast_virtual_networks_v1' API which contains the fabric_id
                                         and the layer 3 virtual network.
        Returns:
            fabric_multicast_details (dict or None): The fabric multicast details of the fabric site with the given layer 3 virtual network.
        Description:
            Call the API 'get_multicast_virtual_networks_v1' with 'fabric_id' and 'virtual_network_name'
            as the filter parameters. Catch the exception, if the API throws any.
        """

        self.log(
            "Checking if the multicast configuration is present under the fabric '{fabric_name}' with the payload {payload}.".format(
                fabric_name=fabric_name, payload=multicast_get_params
            ),
            "DEBUG",
        )
        fabric_multicast_details = None
        try:
            fabric_multicast_details = self.dnac._exec(
                family="sda",
                function="get_multicast_virtual_networks",
                params=multicast_get_params,
            )
            self.log(
                "Response received from 'get_multicast_virtual_networks_v1': {response}".format(
                    response=fabric_multicast_details
                ),
                "DEBUG",
            )
            if not isinstance(fabric_multicast_details, dict):
                self.msg = "Error in getting fabric multicast details - Response is not a dictionary"
                self.log(self.msg, "ERROR")
                self.set_operation_result(
                    "failed", False, self.msg, "ERROR"
                ).check_return_status()

        except Exception as e:
            self.msg = (
                "Exception occurred while running the API 'get_multicast_virtual_networks_v1' "
                "with parameters {params}: {error_msg}".format(
                    params=multicast_get_params, error_msg=e
                )
            )
            self.log(self.msg, "CRITICAL")
            self.set_operation_result(
                "failed", False, self.msg, "ERROR"
            ).check_return_status()

        return fabric_multicast_details

    def get_multicast_replication_mode_details(self, fabric_name, fabric_id):
        """
        Get the multicast replication mode configuration for a given fabric site from Cisco Catalyst Center.

        Parameters:
            fabric_name (str): The name of the fabric site.
            fabric_id (str): The ID of the fabric site.
        Returns:
            replication_mode_details (dict): The multicast replication mode details of the fabric site.
        Description:
            Calls the 'get_multicast_v1' API with the 'fabric_id' as the filter parameter to retrieve
            the multicast replication mode details.
            If the response is not in the expected dictionary format, an error message is logged and
            the operation result is marked as failed.
            If an exception occurs while calling the API, it is caught and logged.
        """

        self.log(
            "Checking replication mode of the multicast configuration under fabric '{fabric_name}' "
            "with fabric_id: {fabric_id}.".format(
                fabric_name=fabric_name, fabric_id=fabric_id
            ),
            "DEBUG",
        )
        replication_mode_details = None
        try:
            replication_mode_details = self.dnac._exec(
                family="sda", function="get_multicast", params={"fabric_id": fabric_id}
            )
            self.log(
                "Response received from 'get_multicast_v1': {response}".format(
                    response=replication_mode_details
                ),
                "DEBUG",
            )
            if not isinstance(replication_mode_details, dict):
                self.msg = "Error in getting replication mode of the multicast configuration details - Response is not a dictionary"
                self.log(self.msg, "ERROR")
                self.set_operation_result(
                    "failed", False, self.msg, "ERROR"
                ).check_return_status()

        except Exception as e:
            self.msg = (
                "Exception occurred while calling the 'get_multicast_v1' API with fabric name "
                "{fabric_name} fabric_id {fabric_id}: {error_msg}".format(
                    fabric_name=fabric_name, fabric_id=fabric_id, error_msg=e
                )
            )
            self.log(self.msg, "CRITICAL")
            self.status = "failed"

        return replication_mode_details

    def fabric_multicast_exists(self, fabric_id, fabric_name, l3_virtual_network):
        """
        Check if the SDA fabric multicast with the given fabric ID and
        the Layer 3 virtual network exists or not.

        Parameters:
            fabric_id (str): The Id of the fabric site to check for existence.
            fabric_name (str): The name of the fabric site to check for existence.
            l3_virtual_network (str): The name of the layer 3 virtual network to check for existence.
        Returns:
            dict - A dictionary containing information about the
                   SDA fabric device's existence:
                - 'exists' (bool): True if the fabric multicast configuration exists, False otherwise.
                - 'id' (str or None): The ID of the fabric multicast configuration if it exists or None if it doesn't.
                - 'multicast_details' (dict or None): Details of the fabric multicast configuration if it exists else None.
                - 'replication_mode_details' (str or None): Details of replication mode of the fabric site's multicast configuration.
        Description:
            Initializes the 'exists', 'multicast_details', 'replication_mode_details', 'fabric_id', and 'id' fields
            in the multicast_info dictionary with default values (None or False).
            Calls the function 'get_fabric_multicast_details' to retrieve the multicast configuration details for the
            given fabric from the Cisco Catalyst Center.
            If no multicast configuration details are found (i.e., the response is empty), it returns the multicast_info
            dictionary with 'exists' set to False.
            Otherwise, it formats the multicast and replication mode details and updates the 'multicast_info' dictionary
            with the relevant data, then returns it.
        """

        self.log(
            "Starting the check for the multicast configuration fabric site {fabric_name} with ID '{fabric_id}'.".format(
                fabric_name=fabric_name, fabric_id=fabric_id
            ),
            "DEBUG",
        )
        multicast_info = {
            "exists": False,
            "multicast_details": None,
            "replication_mode_details": None,
            "id": None,
            "fabric_id": fabric_id,
        }
        multicast_get_params = {"fabric_id": fabric_id}
        if l3_virtual_network:
            multicast_get_params.update({"virtual_network_name": l3_virtual_network})

        fabric_multicast_details = self.get_fabric_multicast_details(
            fabric_name, multicast_get_params
        )
        self.log(
            "Successfully retrieved multicast details of the fabric site {fabric_name} with ID '{fabric_id}'.".format(
                fabric_name=fabric_name, fabric_id=fabric_id
            ),
            "DEBUG",
        )

        # If the SDK return an empty response, then the fabric multicast details is not available
        fabric_multicast_details = fabric_multicast_details.get("response")
        if not fabric_multicast_details:
            self.log(
                "There is no multicast configuration available for the fabric site '{fabric_name}'".format(
                    fabric_name=fabric_name
                ),
                "DEBUG",
            )
            return multicast_info

        self.log(
            "The multicast configuration for the fabric site '{fabric_name}' is found: {details}".format(
                fabric_name=fabric_name, details=fabric_multicast_details
            ),
            "INFO",
        )

        replication_mode_details = self.get_multicast_replication_mode_details(
            fabric_name, fabric_id
        )
        replication_mode_details = replication_mode_details.get("response")
        if not replication_mode_details:
            self.msg = "Unable to retrieve the 'replication mode' details of the fabric site '{fabric_name}'.".format(
                fabric_name=fabric_name
            )
            self.log(str(self.msg, "ERROR"))
            self.set_operation_result(
                "failed", False, self.msg, "ERROR"
            ).check_return_status()

        # Update the existence, details and the id of the fabric mutlticast configuration
        self.log(
            "Formatting the multicast and replication mode details of the fabric '{fabric_name}.".format(
                fabric_name=fabric_name
            ),
            "DEBUG",
        )
        multicast_info.update(
            {
                "exists": True,
                "id": fabric_multicast_details[0].get("id"),
                "multicast_details": self.format_fabric_multicast_params(
                    fabric_name, l3_virtual_network, fabric_multicast_details
                ),
                "replication_mode_details": self.format_replication_mode_params(
                    fabric_name, replication_mode_details
                ),
            }
        )

        self.log(
            "SDA fabric multicast details successfully formatted for fabric site '{fabric_name}' "
            "with virtual network name '{vn_name}'.".format(
                fabric_name=fabric_name, vn_name=l3_virtual_network
            ),
            "DEBUG",
        )
        self.log(
            "SDA fabric multicast details: {multicast_details}".format(
                multicast_details=multicast_info.get("multicast_details")
            ),
            "DEBUG",
        )
        self.log(
            "SDA fabric multicast replication mode details: {replication_mode_details}".format(
                replication_mode_details=multicast_info.get("replication_mode_details")
            ),
            "DEBUG",
        )
        self.log(
            "SDA fabric multicast id: {id}".format(id=multicast_info.get("id")), "DEBUG"
        )

        return multicast_info

    def get_have_fabric_multicast(self, fabric_multicast):
        """
        Get the SDA fabric multicast related information from Cisco
        Catalyst Center based on the provided playbook details.

        Parameters:
            fabric_devices (dict): Playbook details containing fabric multicast details.
        Returns:
            self: The current object with updated current Fabric Multicast information.
        Description:
            Fetch keys required to identify the multicast configurations associated to the
            Layer 3 virtual network (fabric_name, layer3_virtual_network).
            If the keys are not present, return an Error stating the which key is not present.
            The fabric_id should be fetched from the fabric name and it should not be a fabric zone.
            Call the function 'fabric_multicast_exists' to get the details from the
            Cisco Catalyst Center.
        """

        self.log(
            "Starting the process to retrieve SDA fabric multicast information.", "INFO"
        )
        fabric_multicast_details = []
        for item in fabric_multicast:
            fabric_name = item.get("fabric_name")

            # Fabric name is mandatory for this workflow
            if not fabric_name:
                self.msg = "The required parameter 'fabric_name' in 'fabric_multicast' is missing."
                self.log(self.msg, "ERROR")
                self.status = "failed"
                return self

            self.log(
                "Initiating site ID retrieval for fabric '{fabric_name}'.".format(
                    fabric_name=fabric_name
                ),
                "INFO",
            )
            (site_exists, site_id) = self.get_site_id(fabric_name)
            self.log(
                "Retrieved site ID: {site_id}. Site exists: {site_exists}.".format(
                    site_id=site_id, site_exists=site_exists
                ),
                "DEBUG",
            )
            self.log(
                "The site with the name '{site_name} exists in Cisco Catalyst Center is '{site_exists}'".format(
                    site_name=fabric_name, site_exists=site_exists
                ),
                "DEBUG",
            )
            if not site_id:
                self.msg = "Invalid site hierarchy name '{site_name}'.".format(
                    site_name=fabric_name
                )
                self.set_operation_result(
                    "failed", False, self.msg, "ERROR"
                ).check_return_status()

            self.log(
                "Fetching fabric site ID for site '{site_id}'.".format(site_id=site_id),
                "INFO",
            )
            fabric_site_id = self.get_fabric_site_id_from_name(fabric_name, site_id)
            if not fabric_site_id:
                fabric_site_id = self.get_fabric_zone_id_from_name(fabric_name, site_id)
                if not fabric_site_id:
                    self.msg = "The provided 'fabric_name' '{fabric_name}' is not a valid fabric site.".format(
                        fabric_name=fabric_name
                    )
                    if self.params.get("state") == "deleted":
                        self.log(self.msg, "INFO")
                        self.result.get("response").append({"msg": self.msg})
                        self.status = "exited"
                        return self

                    self.log(self.msg, "ERROR")
                    self.set_operation_result(
                        "failed", False, self.msg, "ERROR"
                    ).check_return_status()

                self.msg = "The Multicast should only be associated with fabric sites, not fabric zones."
                self.log(self.msg, "ERROR")
                self.set_operation_result(
                    "failed", False, self.msg, "ERROR"
                ).check_return_status()

            else:
                self.log(
                    "Fabric site ID obtained: {fabric_site_id}.".format(
                        fabric_site_id=fabric_site_id
                    ),
                    "DEBUG",
                )

            layer3_virtual_network = item.get("layer3_virtual_network")
            if not layer3_virtual_network:
                self.msg = "The required parameter 'layer3_virtual_network' in 'fabric_multicast' is missing."
                self.log(str(self.msg), "ERROR")
                self.set_operation_result(
                    "failed", False, self.msg, "ERROR"
                ).check_return_status()

            self.log(
                "The Layer 3 virtual network provided in the playbook is '{l3_vn}'.".format(
                    l3_vn=layer3_virtual_network
                ),
                "INFO",
            )

            multicast_info = self.fabric_multicast_exists(
                fabric_site_id, fabric_name, layer3_virtual_network
            )
            self.log(
                "SDA fabric multicast exists for '{fabric_name}': {exists}".format(
                    fabric_name=fabric_name, exists=multicast_info.get("exists")
                ),
                "DEBUG",
            )
            self.log(
                "SDA fabric multicast details for '{fabric_name}': {multicast_details}".format(
                    fabric_name=fabric_name,
                    multicast_details=multicast_info.get("multicast_details"),
                ),
                "DEBUG",
            )
            self.log(
                "SDA fabric multicast ID for '{fabric_name}': {id}".format(
                    fabric_name=fabric_name, id=multicast_info.get("id")
                ),
                "DEBUG",
            )

            fabric_multicast_details.append(multicast_info)

        self.log(
            "All multicast details of the fabric sites are collected: {details}".format(
                details=fabric_multicast_details
            ),
            "INFO",
        )
        self.have.update({"fabric_multicast": fabric_multicast_details})
        self.msg = (
            "Collecting the SDA multicast details from the Cisco Catalyst Center."
        )
        self.status = "success"
        return self

    def get_have(self, config):
        """
        Get the SDA fabric multicast related information from Cisco Catalyst Center.

        Parameters:
            config (dict): Playbook details containing fabric multicast details.
        Returns:
            self: The current object with updated fabric multicast details.
        Description:
            Check if the 'fabric_multicast' is present in the config or not. If yes,
            Call the function 'get_have_fabric_multicast' and collect the mutlicast configurations
            from the Cisco Catalyst Center.
        """

        self.log("Starting to retrieve SDA fabric multicast information.", "INFO")
        fabric_multicast = config.get("fabric_multicast")
        if not fabric_multicast:
            self.msg = "The parameter 'fabric_multicast' is missing under the 'config'."
            self.set_operation_result(
                "failed", False, self.msg, "ERROR"
            ).check_return_status()

        self.log(
            "Fabric multicast found in config. Proceeding with retrieval.", "DEBUG"
        )
        self.get_have_fabric_multicast(fabric_multicast).check_return_status()
        self.log(
            "Fabric multicast information retrieval was successful. Details: {details}".format(
                details=self.have
            ),
            "DEBUG",
        )
        self.log(
            "Current State (have): {current_state}".format(current_state=self.have),
            "INFO",
        )
        self.msg = "Successfully retrieved the SDA fabric multicast details from the Cisco Catalyst Center."
        self.status = "success"
        return self

    def get_device_details_from_ip(self, device_ip):
        """
        Get the network device details from the network device IP.

        Parameters:
            device_ip (str): The IP address of the network device.
        Returns:
            device_details (dict or None): The details of the network device, or None if the device does not exist.
        Description:
            Call the API 'get_device_list' by setting the 'management_ip_address' field with the
            given IP address.
            If the API response contains device details, they are returned. If no device exists or the response
            is empty, None is returned
        """

        self.log(
            "Starting to get device details for device IP: '{ip}'.".format(
                ip=device_ip
            ),
            "DEBUG",
        )
        device_details = None
        try:
            self.log(
                "Calling 'get_device_list' API with 'management_ip_address': '{ip}'.".format(
                    ip=device_ip
                ),
                "DEBUG",
            )
            device_details = self.dnac._exec(
                family="devices",
                function="get_device_list",
                params={"management_ip_address": device_ip},
            )
            self.log(
                "Response received from 'get_device_list': {response}".format(
                    response=device_details
                ),
                "DEBUG",
            )

            # If the SDK returns no response, then the device does not exist
            device_details = device_details.get("response")
            if not device_details:
                self.log(
                    "No device found with the IP address '{ip_address}'.".format(
                        ip_address=device_ip
                    ),
                    "DEBUG",
                )
                return device_details

        except Exception as e:
            self.msg = "An exception occurred while calling the 'get_device_list' API for IP '{ip}': {error_msg}".format(
                ip=device_ip, error_msg=str(e)
            )
            self.log(self.msg, "CRITICAL")
            self.set_operation_result(
                "failed", False, self.msg, "ERROR"
            ).check_return_status()

        self.log(
            "Successfully retrieved device details for IP '{ip}': {details}".format(
                ip=device_ip, details=device_details
            ),
            "DEBUG",
        )
        return device_details

    def get_the_device_ids(self, fabric_name, device_ips):
        """
        Retrieve network device IDs for the layer 3 virtual network under the specified fabric.

        Parameters:
            fabric_name (str): The name of the fabric site.
            device_ips (list of str): The list of IP address of the network devices.
        Returns:
            network_device_ids (list of str): A list of IDs of the network devices under the fabric.
        Description:
            For each device IP in the provided list, this method:
            1. Calls 'get_device_details_from_ip' to retrieve device details.
            2. Calls 'get_site_id' to retrieve the site ID for the given fabric name.
            3. Validates whether the device is provisioned under the site.
            If any device is not valid or not provisioned, an error is logged, and the process exits.
        """

        self.log(
            "Starting to retrieve network device IDs for fabric '{fabric}' and device IPs: {ips}.".format(
                fabric=fabric_name, ips=device_ips
            ),
            "INFO",
        )
        network_device_ids = []
        if not device_ips or not isinstance(device_ips, list):
            self.msg = "The 'device_ips' parameter must be a non-empty list."
            self.log(self.msg, "ERROR")
            self.set_operation_result(
                "failed", False, self.msg, "ERROR"
            ).check_return_status()

        for device_ip in device_ips:
            self.log("Processing device IP: {ip}".format(ip=device_ip), "DEBUG")
            network_device_details = self.get_device_details_from_ip(device_ip)
            if not network_device_details:
                self.msg = "The device IP '{ip}' is not valid or does not exist under the fabric '{fabric_name}'.".format(
                    ip=device_ip, fabric_name=fabric_name
                )
                self.log(self.msg, "ERROR")
                self.set_operation_result(
                    "failed", False, self.msg, "ERROR"
                ).check_return_status()

            self.log(
                "The device with IP '{ip}' is valid. Details: {details}".format(
                    ip=device_ip, details=network_device_details
                ),
                "DEBUG",
            )
            network_device_id = network_device_details[0].get("id")
            self.log(
                "Retrieved network device ID for IP '{ip}': {device_id}".format(
                    ip=device_ip, device_id=network_device_id
                ),
                "DEBUG",
            )
            self.log(
                "Retrieving site ID for fabric '{fabric_name}'.".format(
                    fabric_name=fabric_name
                ),
                "DEBUG",
            )
            (site_exists, site_id) = self.get_site_id(fabric_name)
            self.log(
                "The site with the name '{site_name} exists in Cisco Catalyst Center is '{site_exists}'".format(
                    site_name=fabric_name, site_exists=site_exists
                ),
                "DEBUG",
            )
            if not site_id:
                self.msg = "The site with the name '{site_name}' does not exist or is invalid.".format(
                    site_name=fabric_name
                )
                self.set_operation_result(
                    "failed", False, self.msg, "ERROR"
                ).check_return_status()

            self.log(
                "Site ID for fabric '{fabric}' retrieved successfully: {site_id}".format(
                    fabric=fabric_name, site_id=site_id
                ),
                "DEBUG",
            )
            self.log(
                "Checking if the device with IP '{ip}' is provisioned under site '{site_name}'.".format(
                    ip=device_ip, site_name=fabric_name
                ),
                "DEBUG",
            )
            self.check_device_is_provisioned(
                device_ip, network_device_id, site_id, fabric_name
            ).check_return_status()
            self.log(
                "The device '{device_id}' with IP '{device_ip}' is provisioned in the site '{fabric_name}'.".format(
                    device_id=network_device_id,
                    device_ip=device_ip,
                    fabric_name=fabric_name,
                ),
                "INFO",
            )
            self.log(
                "The device(s) '{device_ips}' are provisioned to the site '{fabric_name}'.".format(
                    device_ips=device_ips, fabric_name=fabric_name
                ),
                "INFO",
            )
            network_device_ids.append(network_device_id)

        self.log(
            "Successfully retrieved device IDs for the provided IPs. Device IDs: {ids}".format(
                ids=network_device_ids
            ),
            "INFO",
        )
        return network_device_ids

    def determine_rp_device_location(
        self, network_device_ips, ex_rp_ipv4_address, ex_rp_ipv6_address
    ):
        """
        Determine the RP device location ('FABRIC' or 'EXTERNAL') based on input parameters.
        Parameters:
            network_device_ips (list): The list of network device ips.
            ex_rp_ipv4_address (str): The IPv4 address of the RP location at the EXTERNAL location.
            ex_rp_ipv6_address (str): The IPv6 address of the RP location at the EXTERNAL location.
        """

        if network_device_ips:
            return "FABRIC"

        if ex_rp_ipv4_address or ex_rp_ipv6_address:
            return "EXTERNAL"

        return None

    def validate_rp_device_location(
        self,
        rp_device_location,
        network_device_ips,
        ex_rp_ipv4_address,
        ex_rp_ipv6_address,
        fabric_name,
    ):
        """
        Validate the RP device location and its related parameters.

        Parameters:
            rp_device_location (str): The location of the RP.
            network_device_ips (list): The list of network device ips.
            ex_rp_ipv4_address (str): The IPv4 address of the RP location at the EXTERNAL location.
            ex_rp_ipv6_address (str): The IPv6 address of the RP location at the EXTERNAL location.
        Description:
            Check if the location of the RP is valid or not.
            If the RP location is "FABRIC" and if the network device IPs are not present, fail the module.
            If the RP location is "EXTERNAL' and if either the 'ex_rp_ipv4_address' or 'ex_rp_ipv4_address'
            is not present, fail the module.
        """

        valid_locations = ["FABRIC", "EXTERNAL"]
        if rp_device_location not in valid_locations:
            self.msg = "Invalid 'rp_device_location'. Must be one of: {valid_locations}.".format(
                valid_locations=valid_locations
            )
            self.log(self.msg, "ERROR")
            self.set_operation_result(
                "failed", False, self.msg, "ERROR"
            ).check_return_status()

        if rp_device_location == "FABRIC" and not network_device_ips:
            self.msg = (
                "The parameter 'network_device_ips' is mandatory when 'rp_device_location' is 'FABRIC' "
                "in fabric '{fabric_name}'.".format(fabric_name=fabric_name)
            )
            self.log(self.msg, "ERROR")
            self.set_operation_result(
                "failed", False, self.msg, "ERROR"
            ).check_return_status()

        if rp_device_location == "EXTERNAL" and not (
            ex_rp_ipv4_address or ex_rp_ipv6_address
        ):
            self.msg = (
                "The parameters 'ex_rp_ipv4_address' or 'ex_rp_ipv6_address' are mandatory when "
                "'rp_device_location' is 'EXTERNAL' in fabric '{fabric_name}'.".format(
                    fabric_name=fabric_name
                )
            )
            self.log(self.msg, "ERROR")
            self.set_operation_result(
                "failed", False, self.msg, "ERROR"
            ).check_return_status()

    def process_fabric_rp(
        self, item, fabric_name, layer3_virtual_network, network_device_ips
    ):
        """
        Process FABRIC RP details.

        Parameters:
            item (dict): The details of the Any-source multicast.
            fabric_name (str): The name of the fabric site.
            layer3_virtual_network (str): The name of the Layer 3 virtual network.
            network_device_ips (list of str): The IPs of the network devices.
        Returns:
            rendezvous_point (dict): The IDs of the RP network devices.
        Description:
            Check if there are more than two network device IDs. If so, fail the module.
            Collect the network device IDs using the network device IPs.
            Return the network device IDs.

        """

        self.log(
            "Processing FABRIC RP details for fabric '{fabric_name}'.".format(
                fabric_name=fabric_name
            ),
            "DEBUG",
        )

        # Validate network device IPs
        if not isinstance(network_device_ips, list):
            self.msg = "The parameter 'network_device_ips' must be a list for L3 VN '{l3_vn}' under fabric '{fabric_name}'.".format(
                l3_vn=layer3_virtual_network, fabric_name=fabric_name
            )
            self.log(self.msg, "ERROR")
            self.set_operation_result(
                "failed", False, self.msg, "ERROR"
            ).check_return_status()

        if len(network_device_ips) > 2:
            self.msg = "Maximum of two 'network_device_ips' are allowed for fabric '{fabric_name}'.".format(
                fabric_name=fabric_name
            )
            self.log(self.msg, "ERROR")
            self.set_operation_result(
                "failed", False, self.msg, "ERROR"
            ).check_return_status()

        # Get device IDs
        network_device_ids = self.get_the_device_ids(fabric_name, network_device_ips)

        # Build RP details
        rendezvous_point = {
            "networkDeviceIds": network_device_ids,
        }

        # Process IPv4 and IPv6 ASM ranges
        self.process_asm_ranges(item, rendezvous_point)

        return rendezvous_point

    def process_external_rp(self, item, fabric_name):
        """
        Process EXTERNAL RP details.
        Parameters:
            item (dict): The details of the Any-source multicast.
            fabric_name (str): The name of the fabric site.
        Returns:
            rendezvous_point (dict): The EXTERNAL IPv4 or IPv6 address.
        Description:
            If 'ex_rp_ipv4_address' is provided, store the address in the 'ipv4Address'.
            If 'ex_rp_ipv6_address' is provided, store the address in the 'ipv6Address'.
        """

        self.log(
            "Processing EXTERNAL RP details for fabric '{fabric_name}'.".format(
                fabric_name=fabric_name
            ),
            "DEBUG",
        )

        rendezvous_point = {}

        # Add external IPv4 and IPv6 addresses
        if item.get("ex_rp_ipv4_address"):
            rendezvous_point["ipv4Address"] = item["ex_rp_ipv4_address"]
        if item.get("ex_rp_ipv6_address"):
            rendezvous_point["ipv6Address"] = item["ex_rp_ipv6_address"]

        # Process IPv4 and IPv6 ASM ranges
        self.process_asm_ranges(item, rendezvous_point)

        return rendezvous_point

    def process_asm_ranges(self, item, rendezvous_point):
        """
        Process IPv4 and IPv6 ASM ranges for a rendezvous point.

        Parameters:
            item (dict): The details of the Any-source multicast.
            fabric_name (str): The name of the fabric site.
        """

        if item.get("ipv4_asm_ranges"):
            rendezvous_point["ipv4AsmRanges"] = item["ipv4_asm_ranges"]
        elif item.get("is_default_v4_rp"):
            rendezvous_point["isDefaultV4RP"] = item["is_default_v4_rp"]

        if item.get("ipv6_asm_ranges"):
            rendezvous_point["ipv6AsmRanges"] = item["ipv6_asm_ranges"]
        elif item.get("is_default_v6_rp"):
            rendezvous_point["isDefaultV6RP"] = item["is_default_v6_rp"]

    def process_any_source_multicast_details(
        self,
        fabric_name,
        layer3_virtual_network,
        any_source_multicast,
        have_multicast_details,
    ):
        """
        Process the any-source multicast (ASM) details provided in the playbook.

        Parameters:
            fabric_name (dict): The name of the fabric site.
            layer3_virtual_network (str): The layer 3 virtual name of the multicast configuration in the fabric site.
            any_source_multicast (dict): The any source multicast details of the fabric site.
            have_multicast_details (dict): Multicast configuration details of the fabric site, if exists. Else None.
        Returns:
            multicast_rps (list of dict): A list of rendezvous point (RP) details for the given fabric.
        Description:
            For every element in the 'asm', we have to fetch the 'network_device_ips', 'ex_rp_ipv4_address'
            and 'ex_rp_ipv6_address'.
            If the 'network_device_ips' is provided then the RP device location is 'FABRIC'.
            Else, 'EXTERNAL'.
            For the structure which is suitable for the API payload according to the device RP location.
        """

        self.log(
            "Processing any-source multicast (ASM) details for fabric '{fabric_name}', L3 VN '{l3_vn}'.".format(
                fabric_name=fabric_name, l3_vn=layer3_virtual_network
            ),
            "INFO",
        )

        # Validate input
        if not any_source_multicast or not isinstance(any_source_multicast, list):
            self.msg = "Invalid or missing 'any_source_multicast' parameter. Must be a non-empty list."
            self.log(self.msg, "ERROR")
            self.set_operation_result(
                "failed", False, self.msg, "ERROR"
            ).check_return_status()

        multicast_rps = []
        for item in any_source_multicast:
            rendezvous_point = {}
            network_device_ips = item.get("network_device_ips")
            ex_rp_ipv4_address = item.get("ex_rp_ipv4_address")
            ex_rp_ipv6_address = item.get("ex_rp_ipv6_address")

            # Determine RP device location
            rp_device_location = self.determine_rp_device_location(
                network_device_ips, ex_rp_ipv4_address, ex_rp_ipv6_address
            )
            self.validate_rp_device_location(
                rp_device_location,
                network_device_ips,
                ex_rp_ipv4_address,
                ex_rp_ipv6_address,
                fabric_name,
            )

            # Process based on RP device location
            if rp_device_location == "FABRIC":
                rendezvous_point = self.process_fabric_rp(
                    item, fabric_name, layer3_virtual_network, network_device_ips
                )
            elif rp_device_location == "EXTERNAL":
                rendezvous_point = self.process_external_rp(item, fabric_name)

            # Add RP device location
            rendezvous_point["rpDeviceLocation"] = rp_device_location

            # Append the processed RP to the list
            multicast_rps.append(rendezvous_point)

        # Log the final RP details
        self.log(
            "Processed rendezvous points for fabric '{fabric_name}': {multicast_rps}".format(
                fabric_name=fabric_name, multicast_rps=multicast_rps
            ),
            "DEBUG",
        )

        return multicast_rps

    def get_want_fabric_multicast(self, fabric_multicast):
        """
        Get all the SDA fabric multicast information from playbook.
        Set the status and the msg before returning from the API
        Check the return value of the API with check_return_status()

        Parameters:
            fabric_multicast (dict): Playbook details containing fabric multicast information.
        Returns:
            self: The current object with updated desired fabric multicast information.
        Description:
            For all the config under the fabric_multicast, set the 'multicast_details' and
            'replication_mode_details' as None.
            Do all the validation for the parameter provided in the playbook.
            Check for the mandatory parameter like fabric_name and the layer3_virtual_network.
            Do the validation for the 'replication_mode' like whether the provided value is in the
            valid replication mode list or not.
            Get the 'ip_pool_name'. Check whether it is a valid one or not and check if it is
            reserved to the fabric site.
            Fetch and validate the 'ssm' and the 'asm' configurations from the playbook.
        """

        self.log(
            "Starting to process fabric multicast configurations from the playbook.",
            "INFO",
        )
        fabric_multicast_details = []
        fabric_multicast_index = -1
        for item in fabric_multicast:
            fabric_devices_info = {
                "multicast_details": None,
                "replication_mode_details": None,
            }
            fabric_multicast_index += 1
            fabric_name = item.get("fabric_name")
            self.log(
                "Starting to gather fabric multicast details for fabric: {fabric_name}".format(
                    fabric_name=fabric_name
                ),
                "DEBUG",
            )
            have_multicast_details = self.have.get("fabric_multicast")[
                fabric_multicast_index
            ]
            fabric_id = have_multicast_details.get("fabric_id")
            if not fabric_id:
                self.msg = "The fabric ID of the fabric site '{fabric_name}' is not found in the Cisco Catalyst Center.".format(
                    fabric_name=fabric_name
                )
                self.set_operation_result(
                    "failed", False, self.msg, "ERROR"
                ).check_return_status()

            replication_mode = item.get("replication_mode")
            valid_replication_mode_list = ["NATIVE_MULTICAST", "HEADEND_REPLICATION"]
            have_fabric_multicast_exists = have_multicast_details.get("exists")
            self.log(
                "Processing replication mode configuration at position: {index}".format(
                    index=fabric_multicast_index + 1
                ),
                "DEBUG",
            )

            if not replication_mode:
                if have_fabric_multicast_exists:
                    replication_mode = have_multicast_details.get(
                        "replication_mode_details"
                    ).get("replicationMode")
                else:
                    replication_mode = "HEADEND_REPLICATION"
                    self.msg = (
                        "The parameter 'replication_mode' is missing for the fabric with name '{fabric_name}'."
                        "Setting it to its default value of '{replication_mode}'".format(
                            fabric_name=fabric_name, replication_mode=replication_mode
                        )
                    )

            if replication_mode not in valid_replication_mode_list:
                self.msg = "The 'replication_mode' should must be in the following list '{valid_list}'.".format(
                    valid_list=valid_replication_mode_list
                )
                self.set_operation_result(
                    "failed", False, self.msg, "ERROR"
                ).check_return_status()

            fabric_devices_info.update(
                {
                    "replication_mode_details": {
                        "fabricId": fabric_id,
                        "replicationMode": replication_mode,
                    }
                }
            )

            layer3_virtual_network = item.get("layer3_virtual_network")
            if not layer3_virtual_network:
                self.msg = "The parameter 'layer3_virtual_network' is missing for the fabric with name '{fabric_name}'.".format(
                    fabric_name=fabric_name
                )
                self.set_operation_result(
                    "failed", False, self.msg, "ERROR"
                ).check_return_status()

            self.log(
                "Checking if the Layer 3 virtual network '{l3_vn}' is valid or not".format(
                    l3_vn=layer3_virtual_network
                ),
                "DEBUG",
            )
            is_valid_virtual_network = self.check_valid_virtual_network_name(
                layer3_virtual_network
            )

            # If the response returned from the SDK is None, then the Layer 3 VN is not present in the Cisco Catalyst Center.
            if not is_valid_virtual_network:
                self.msg = (
                    "The virtual network with the name '{virtual_nw_name}' is not valid for the fabric "
                    "with name '{fabric_name}'.".format(
                        virtual_nw_name=layer3_virtual_network, fabric_name=fabric_name
                    )
                )
                self.set_operation_result(
                    "failed", False, self.msg, "ERROR"
                ).check_return_status()

            self.log(
                "The provided Layer 3 virtual network '{l3_vn}' is valid in the fabric site '{fabric_name}'.".format(
                    l3_vn=layer3_virtual_network, fabric_name=fabric_name
                ),
                "INFO",
            )

            self.log(
                "Check to verify the Layer 3 virtual network '{l3_vn}' is in the "
                "fabric zone(s) under the fabric site '{fabric_name}' is done by the API.".format(
                    l3_vn=layer3_virtual_network, fabric_name=fabric_name
                ),
                "DEBUG",
            )

            ip_pool_name = item.get("ip_pool_name")
            have_multicast_details = have_multicast_details.get("multicast_details")
            if not ip_pool_name:
                if have_fabric_multicast_exists:
                    ip_pool_name = have_multicast_details.get("ipPoolName")
                else:
                    self.msg = "The parameter 'ip_pool_name' is missing for the fabric with name '{fabric_name}'.".format(
                        fabric_name=fabric_name
                    )
                    self.set_operation_result(
                        "failed", False, self.msg, "ERROR"
                    ).check_return_status()

            is_valid_reserved_pool = self.check_valid_reserved_pool(
                ip_pool_name, fabric_name
            )
            if not is_valid_reserved_pool:
                self.msg = (
                    "The 'ip_pool_name' is not a valid reserved pool under the "
                    "fabric with name '{fabric_name}'.".format(fabric_name=fabric_name)
                )
                self.set_operation_result(
                    "failed", False, self.msg, "ERROR"
                ).check_return_status()

            multicast_details = {
                "fabricId": fabric_id,
                "virtualNetworkName": layer3_virtual_network,
                "ipPoolName": ip_pool_name,
            }
            source_specific_multicast = item.get("ssm")
            if source_specific_multicast:
                ipv4_ssm_ranges = source_specific_multicast.get("ipv4_ssm_ranges")
                if not ipv4_ssm_ranges:
                    self.msg = (
                        "The 'ipv4_ssm_ranges' parameter should not be empty under 'ssm' "
                        "for the fabric site '{fabric_name}'".format(
                            fabric_name=fabric_name
                        )
                    )
                    self.set_operation_result(
                        "failed", False, self.msg, "ERROR"
                    ).check_return_status()

                if not isinstance(ipv4_ssm_ranges, list):
                    self.msg = (
                        "The 'ipv4_ssm_ranges' parameter should be a 'list' datatype "
                        "under 'ssm' for the fabric site '{fabric_name}'".format(
                            fabric_name=fabric_name
                        )
                    )
                    self.set_operation_result(
                        "failed", False, self.msg, "ERROR"
                    ).check_return_status()
                else:
                    multicast_details.update({"ipv4SsmRanges": ipv4_ssm_ranges})

            else:
                if have_fabric_multicast_exists:
                    have_ssm = have_multicast_details.get("ipv4SsmRanges")
                    self.log(
                        "The 'ssm' details for the fabric site '{fabric_name}' is present in the CC: {details}".format(
                            fabric_name=fabric_name, details=have_ssm
                        ),
                        "INFO",
                    )
                    if have_ssm:
                        multicast_details.update({"ipv4SsmRanges": have_ssm})

            any_source_multicast = item.get("asm")
            have_multicast_rps = None
            if have_fabric_multicast_exists:
                have_multicast_rps = have_multicast_details.get("multicastRPs")

            if any_source_multicast:
                multicast_details.update(
                    {
                        "multicastRPs": self.process_any_source_multicast_details(
                            fabric_name,
                            layer3_virtual_network,
                            any_source_multicast,
                            have_multicast_rps,
                        )
                    }
                )
            else:
                if have_multicast_rps:
                    multicast_details.update({"multicastRPs": have_multicast_rps})

            if self.params.get("state") != "deleted" and not self.have.get(
                "fabric_multicast"
            )[fabric_multicast_index].get("exists"):
                if not multicast_details.get(
                    "ipv4SsmRanges"
                ) and not multicast_details.get("multicastRPs"):
                    self.msg = "Either the parameter 'ssm' or 'asm' should be provided for the fabric site '{fabric_name}'.".format(
                        fabric_name=fabric_name
                    )
                    self.set_operation_result(
                        "failed", False, self.msg, "ERROR"
                    ).check_return_status()

            self.log(
                "The any source multicast details for the fabric site  '{fabric_name}': {details}".format(
                    fabric_name=fabric_name, details=any_source_multicast
                ),
                "INFO",
            )
            fabric_devices_info.update({"multicast_details": multicast_details})
            self.log(
                "Collected multicast details for the fabric site '{fabric_name}': {details}".format(
                    fabric_name=fabric_name, details=fabric_devices_info
                ),
                "DEBUG",
            )
            fabric_multicast_details.append(fabric_devices_info)

        self.log(
            "All fabric multicast details are processed. Compiled details: {requested_state}".format(
                requested_state=fabric_multicast_details
            ),
            "DEBUG",
        )
        self.want.update({"fabric_multicast": fabric_multicast_details})
        self.msg = "Collecting the SDA fabric multicast details from the playbook."
        self.status = "success"
        self.log(
            "Fabric multicast details successfully gathered. Status: {status}".format(
                status=self.status
            ),
            "DEBUG",
        )
        return self

    def get_want(self, config):
        """
        Get the SDA fabric multicast related information from the playbook.

        Parameters:
            config (dict): Playbook details containing fabric multicast details.
        Returns:
            self: The current object with updated fabric multicast details.
        Description:
            Check if 'fabric_multicast' exists in the provided playbook configuration.
            If it exists, process the multicast details using 'get_want_fabric_multicast'.
        """

        self.log(
            "Starting to retrieve fabric multicast information from the provided configuration.",
            "DEBUG",
        )
        fabric_multicast = config.get("fabric_multicast")
        if not fabric_multicast:
            self.msg = "The parameter 'fabric_multicast' is missing under the 'config'."
            self.set_operation_result(
                "failed", False, self.msg, "ERROR"
            ).check_return_status()

        self.log(
            "The 'fabric_multicast' parameter exists in the configuration with {count} entries.".format(
                count=len(fabric_multicast)
            ),
            "DEBUG",
        )
        self.get_want_fabric_multicast(fabric_multicast).check_return_status()
        self.log("Fabric multicast details successfully processed.", "INFO")

        self.log(
            "Desired State (want): {requested_state}".format(requested_state=self.want),
            "INFO",
        )
        self.msg = "Successfully retrieved details from the playbook."
        self.status = "success"
        return self

    def retain_multicast_cc_values(self, want_multicast_params, have_multicast_params):
        """
        Retain and merge multicast configurations from the playbook with existing configurations.

        Parameters:
            want_multicast_params (dict): The multicast configurations provided in the playbook.
            have_multicast_params (dict): The multicast configurations available in the Cisco Catalyst Center.
        Returns:
            updated_multicast_params (dict): The retained multicast configurations combined with
                                             the multicast configuration provided in the playbook.
        Description:
            This function maintains the merged state in the Cisco Catalyst Center.
            We have to preserve the config which is present in the Cisco Catalyst Center
            along with the new config provided in the playbook.
            If 'ssm' is provided in the config. Add the new ipv4_ssm_ranges to the existing ones.
            If 'asm' is provided in the config. Store all the rp configuration. If the rp is
            available in the playbook and in the multicast configuration of the fabric site.
            Remove the config and add the config which is provided in the playbook.
        """

        self.log(
            "Started retaining the multicast configuration along with the provided configuration...",
            "DEBUG",
        )
        updated_multicast_params = {}
        want_ipv4_ssm_ranges = want_multicast_params.get("ipv4SsmRanges")
        have_ipv4_ssm_ranges = have_multicast_params.get("ipv4SsmRanges")
        updated_multicast_params.update(
            {
                "fabricId": want_multicast_params.get("fabricId"),
                "virtualNetworkName": want_multicast_params.get("virtualNetworkName"),
                "ipPoolName": want_multicast_params.get("ipPoolName"),
            }
        )
        updated_ipv4_ssm_range = []
        self.log(
            "The IPv4 ssm ranges present in the Cisco Catalyst Center '{ssm_ranges}".format(
                ssm_ranges=have_ipv4_ssm_ranges
            ),
            "DEBUG",
        )
        self.log(
            "The IPv4 ssm ranges provided in the playbook '{ssm_ranges}".format(
                ssm_ranges=want_ipv4_ssm_ranges
            ),
            "DEBUG",
        )
        if want_ipv4_ssm_ranges and have_ipv4_ssm_ranges:
            if set(want_ipv4_ssm_ranges).issubset(have_ipv4_ssm_ranges):
                self.log(
                    "The 'ipv4_ssm_ranges' provided in the playbook is already available in the "
                    "Cisco Catalyst Center.",
                    "DEBUG",
                )
                updated_ipv4_ssm_range = have_ipv4_ssm_ranges
            else:
                self.log(
                    "The configuration which is provided in the playbook is not available in "
                    "Cisco Catalyst Center. Retaining the the playbook config along with the config "
                    "present in the Cisco Catalyst Center.",
                    "DEBUG",
                )
                updated_ipv4_ssm_range = list(
                    set(want_ipv4_ssm_ranges + have_ipv4_ssm_ranges)
                )
        else:
            if not want_ipv4_ssm_ranges and have_ipv4_ssm_ranges:
                self.log(
                    "The ipv4 ssm ranges are not provided in the payload and it is available "
                    "in the Cisco Catalyst Center.",
                    "DEBUG",
                )
                updated_ipv4_ssm_range = have_ipv4_ssm_ranges
            elif not have_ipv4_ssm_ranges and want_ipv4_ssm_ranges:
                self.log(
                    "The ipv4 ssm ranges are provided in the playbook and it is not present in the "
                    "Cisco Catalyst Center.",
                    "DEBUG",
                )
                updated_ipv4_ssm_range = want_ipv4_ssm_ranges
            else:
                self.log(
                    "The ipv4 ssm ranges are not provided in the playbook and it is not present in the "
                    "Cisco Catalyst Center.",
                    "DEBUG",
                )

        updated_multicast_params.update({"ipv4SsmRanges": updated_ipv4_ssm_range})
        have_asm_config = have_multicast_params.get("multicastRPs")
        want_asm_config = want_multicast_params.get("multicastRPs")
        updated_asm_config = copy.deepcopy(have_asm_config)
        if want_asm_config:
            for item in want_asm_config:
                asm_config_in_cc = {}
                rp_device_location = item.get("rpDeviceLocation")
                ipv4_address = item.get("ipv4Address")
                ipv6_address = item.get("ipv6Address")
                fabric_rp_ipv4_address = None
                fabric_rp_ipv6_address = None
                if rp_device_location == "FABRIC":
                    asm_config_in_cc = get_dict_result(
                        have_asm_config, "rpDeviceLocation", "FABRIC"
                    )
                    self.log(
                        "The asm config for the RP with location 'FABRIC' is '{asm_config}'.".format(
                            asm_config=asm_config_in_cc
                        ),
                        "DEBUG",
                    )
                    if asm_config_in_cc:
                        fabric_rp_ipv4_address = asm_config_in_cc.get("ipv4Address")
                        fabric_rp_ipv6_address = asm_config_in_cc.get("ipv6Address")
                        self.log(
                            "The multicast configuration with the RP as 'FABRIC' is available "
                            "in the Cisco Catalyst Center.",
                            "DEBUG",
                        )
                    else:
                        self.log(
                            "The multicast configuration with the RP as 'FABRIC' is not available "
                            "in the Cisco Catalyst Center.",
                            "DEBUG",
                        )

                    self.log(
                        "The IPv4 address of the 'FABRIC' RP is '{ipv4}'.".format(
                            ipv4=fabric_rp_ipv4_address
                        ),
                        "DEBUG",
                    )
                    self.log(
                        "The IPv6 address of the 'FABRIC' RP is '{ipv6}'.".format(
                            ipv6=fabric_rp_ipv6_address
                        ),
                        "DEBUG",
                    )
                elif ipv4_address:
                    asm_config_in_cc = get_dict_result(
                        have_asm_config, "ipv4Address", ipv4_address
                    )
                    if len(have_asm_config) == 1:
                        if (
                            have_asm_config[0].get("ipv4Address") is None
                            or have_asm_config[0].get("ipv4Address") == ipv4_address
                        ):
                            asm_config_in_cc = None

                    self.log(
                        "The asm config for the IPv4 RP '{ip}' with location 'EXTERNAL' is '{asm_config}'.".format(
                            ip=ipv4_address, asm_config=asm_config_in_cc
                        ),
                        "INFO",
                    )
                elif ipv6_address:
                    asm_config_in_cc = get_dict_result(
                        have_asm_config, "ipv6Address", ipv6_address
                    )
                    if len(have_asm_config) == 1:
                        if (
                            have_asm_config[0].get("ipv6Address") is None
                            or have_asm_config[0].get("ipv6Address") == ipv6_address
                        ):
                            asm_config_in_cc = None

                    self.log(
                        "The asm config for the IPv6 RP '{ip}' with location 'EXTERNAL' is '{asm_config}'.".format(
                            ip=ipv6_address, asm_config=asm_config_in_cc
                        ),
                        "INFO",
                    )

                self.log(
                    "Before updating the asm config: {updated_asm_config}".format(
                        updated_asm_config=updated_asm_config
                    ),
                    "DEBUG",
                )
                if asm_config_in_cc:
                    updated_asm_config.remove(asm_config_in_cc)
                    if fabric_rp_ipv4_address:
                        item.update({"ipv4Address": fabric_rp_ipv4_address})

                    if fabric_rp_ipv6_address:
                        item.update({"ipv6Address": fabric_rp_ipv6_address})

                updated_asm_config.append(item)
                self.log(
                    "After updating the asm config: {updated_asm_config}".format(
                        updated_asm_config=updated_asm_config
                    ),
                    "DEBUG",
                )

        updated_multicast_params.update({"multicastRPs": updated_asm_config})
        self.log(
            "Final updated asm config: {updated_asm_config}".format(
                updated_asm_config=updated_asm_config
            ),
            "INFO",
        )
        return updated_multicast_params

    def bulk_add_multicast_config(self, add_multicast_config):
        """
        Configure SDA multicast configurations in bulk using the provided payload.

        Parameters:
            add_multicast_config (list): The payload for adding the fabric devices in bulk.
        Returns:
            self (object): The current object with adding SDA multicast configurations.
        Description:
            Process the payload in batches of 20 and send it to the SDA API 'add_multicast_virtual_networks_v1'.
            Validate the API response, check for the 'task_id', and ensure the task completes successfully.
            Log an error if the task fails.
        """

        self.log("Starting to configure multicast configurations in bulk.", "INFO")

        # Validate input
        if not isinstance(add_multicast_config, list) or not add_multicast_config:
            self.msg = (
                "Invalid payload: 'add_multicast_config' must be a non-empty list."
            )
            self.log(self.msg, "ERROR")
            self.set_operation_result(
                "failed", False, self.msg, "ERROR"
            ).check_return_status()

        BATCH_SIZE = 20
        try:
            config_length = len(add_multicast_config)

            for index in range(0, config_length, BATCH_SIZE):
                payload = {"payload": add_multicast_config[index : index + BATCH_SIZE]}
                self.log(
                    "Processing batch {start}-{end} of {total} multicast configurations.".format(
                        start=index + 1,
                        end=min(index + BATCH_SIZE, config_length),
                        total=config_length,
                    ),
                    "DEBUG",
                )
                task_name = "add_multicast_virtual_networks_v1"
                task_id = self.get_taskid_post_api_call("sda", task_name, payload)
                if not task_id:
                    self.msg = "Failed to retrieve task_id for task '{task_name}' with payload: {batch_payload}.".format(
                        task_name=task_name, batch_payload=payload
                    )
                    self.set_operation_result(
                        "failed", False, self.msg, "ERROR"
                    ).check_return_status()

                success_msg = "Successfully configured the multicast configuration with details '{config_details}'.".format(
                    config_details=add_multicast_config[index : index + BATCH_SIZE]
                )
                self.get_task_status_from_tasks_by_id(
                    task_id, task_name, success_msg
                ).check_return_status()

            self.msg = (
                "Successfully added the multicast configurations with the "
                "payload to the Cisco Catalyst Center: {payload}".format(
                    payload=add_multicast_config
                )
            )
            self.log(self.msg, "INFO")
            self.status = "success"

        except Exception as e:
            self.msg = (
                "Exception occurred while configuring the multicast "
                "configurations with the payload '{payload}': {error_msg}".format(
                    payload=add_multicast_config, error_msg=e
                )
            )
            self.set_operation_result(
                "failed", False, self.msg, "ERROR"
            ).check_return_status()

        return self

    def bulk_update_replication_mode(self, update_replication_mode):
        """
        Updates the SDA multicast replication mode in bulk using the provided payload.

        Parameters:
            update_replication_mode (list): The payload for updating the replication mode in bulk.
        Returns:
            self (object): The current object with updated replication mode information.
        Description:
            Processes the payload in batches of 20 entries and sends them to the SDA API
            'update_multicast_v1'. Validates the API response, checks for the 'task_id',
            and ensures the task completes successfully. Logs an error and stops the module
            if a task fails.
        """

        self.log("Starting to update replication modes in bulk.", "INFO")

        if not isinstance(update_replication_mode, list) or not update_replication_mode:
            self.msg = (
                "Invalid input: 'update_replication_mode' must be a non-empty list."
            )
            self.log(self.msg, "ERROR")
            self.set_operation_result(
                "failed", False, self.msg, "ERROR"
            ).check_return_status()

        BATCH_SIZE = 20
        try:
            config_length = len(update_replication_mode)

            for index in range(0, config_length, BATCH_SIZE):
                payload = {
                    "payload": update_replication_mode[index : index + BATCH_SIZE]
                }
                self.log(
                    "Processing batch {start}-{end} of {total} replication mode updates.".format(
                        start=index + 1,
                        end=min(index + BATCH_SIZE, config_length),
                        total=config_length,
                    ),
                    "DEBUG",
                )

                # Prepare API payload and task details
                task_name = "update_multicast_v1"
                task_id = self.get_taskid_post_api_call("sda", task_name, payload)
                if not task_id:
                    self.msg = "Failed to retrieve task_id for task '{task_name}' with payload: {batch_payload}.".format(
                        task_name=task_name, batch_payload=payload
                    )
                    self.set_operation_result(
                        "failed", False, self.msg, "ERROR"
                    ).check_return_status()

                success_msg = "Successfully updated replication mode for batch {start}-{end}.".format(
                    start=index + 1, end=min(index + BATCH_SIZE, config_length)
                )
                self.get_task_status_from_tasks_by_id(
                    task_id, task_name, success_msg
                ).check_return_status()

            self.msg = (
                "Successfully updated the replication mode with the "
                "payload to the Cisco Catalyst Center: {payload}".format(
                    payload=update_replication_mode
                )
            )
            self.log(self.msg, "INFO")
            self.status = "success"

        except Exception as e:
            self.msg = "An exception occurred while updating replication modes: {error_msg}. Payload: {payload}".format(
                error_msg=str(e), payload=update_replication_mode
            )
            self.set_operation_result(
                "failed", False, self.msg, "ERROR"
            ).check_return_status()

        return self

    def bulk_update_multicast_config(self, update_multicast_config):
        """
        Updates SDA multicast configurations in bulk using the provided payload.

        Parameters:
            update_multicast_config (list): The payload for updating the fabric devices in bulk.
        Returns:
            self (object): The current object with updated SDA multicast configurations.
        Description:
            Processes the payload in batches of 20 entries and sends them to the SDA API
            'update_multicast_virtual_networks_v1'. Validates the API response, checks for the 'task_id',
            and ensures the task completes successfully. Logs an error and stops the module if a task fails.
        """

        self.log("Starting to update multicast configurations in bulk.", "INFO")

        # Validate input payload
        if not isinstance(update_multicast_config, list) or not update_multicast_config:
            self.msg = (
                "Invalid input: 'update_multicast_config' must be a non-empty list."
            )
            self.log(self.msg, "ERROR")
            self.set_operation_result(
                "failed", False, self.msg, "ERROR"
            ).check_return_status()

        BATCH_SIZE = 20
        try:
            self.log(
                "Starting to update the multicast configurations in batches.", "INFO"
            )
            config_length = len(update_multicast_config)

            for index in range(0, config_length, BATCH_SIZE):

                # Prepare API payload
                payload = {
                    "payload": update_multicast_config[index : index + BATCH_SIZE]
                }
                self.log(
                    "Processing batch {start}-{end} of {total} multicast configurations.".format(
                        start=index + 1,
                        end=min(index + BATCH_SIZE, config_length),
                        total=config_length,
                    ),
                    "DEBUG",
                )
                task_name = "update_multicast_virtual_networks_v1"
                task_id = self.get_taskid_post_api_call("sda", task_name, payload)
                if not task_id:
                    self.msg = "Failed to retrieve task_id for task '{task_name}' with payload: {batch_payload}.".format(
                        task_name="update_multicast_virtual_networks_v1",
                        batch_payload=payload,
                    )
                    self.set_operation_result(
                        "failed", False, self.msg, "ERROR"
                    ).check_return_status()

                success_msg = "Successfully updated multicast configurations for batch {start}-{end}.".format(
                    start=index + 1, end=min(index + BATCH_SIZE, config_length)
                )
                self.get_task_status_from_tasks_by_id(
                    task_id, task_name, success_msg
                ).check_return_status()

            self.msg = (
                "Successfully updated the multicast configurations with the "
                "payload to the Cisco Catalyst Center: {payload}".format(
                    payload=update_multicast_config
                )
            )
            self.log(self.msg, "INFO")
            self.status = "success"

        except Exception as e:
            self.msg = (
                "Exception occurred while updating the multicast "
                "configurations with the payload '{payload}': {error_msg}".format(
                    payload=update_multicast_config, error_msg=e
                )
            )
            self.set_operation_result(
                "failed", False, self.msg, "ERROR"
            ).check_return_status()

        return self

    def update_fabric_multicast(self, fabric_multicast):
        """
        Add or Update the SDA multicast configurations along with the source specific and
        any source configurations under the layer 3 virtual network of a fabric site
        in Cisco Catalyst Center based on the playbook details.

        Parameters:
            fabric_multicast (dict): SDA fabric multicast configuration(s) from the playbook details.
        Returns:
            self (object): The current object with updated desired fabric multicast information.
        Description:
            Check if the multicast configuration associated with the Layer 3 virtual network is
            present in the Cisco Catalyst Center or not.
            If it does not exist, use the API 'add_multicast_virtual_networks_v1'
            to add the multicast configuration.
            If it does exist, check whether the multicast configuration requires an update
            or not. If it requires, use the API 'update_multicast_virtual_networks_v1'
            to update the multicast configuration.
            Check if the replication mode requires any update or not. If it does,
            use the API 'update_multicast_v1' to update the replication mode configurations.
        """

        self.log(
            "Input values for update_fabric_multicast: {input}".format(
                input=fabric_multicast
            ),
            "DEBUG",
        )
        fabric_multicast_index = -1
        to_create_multicast = []
        to_update_replication_mode = []
        to_update = []

        # Validate input
        if not fabric_multicast:
            self.log("Error: 'fabric_multicast' is empty or not provided.", "ERROR")
            self.set_operation_result(
                "failed", False, "Input fabric_multicast is required.", "ERROR"
            )
            return self

        # Process each multicast configuration
        for multicast_config in fabric_multicast:
            fabric_multicast_index += 1
            fabric_name = multicast_config.get("fabric_name")
            if not fabric_name:
                self.log("Error: 'fabric_name' is missing from input.", "ERROR")
                self.set_operation_result(
                    "failed", False, "Fabric name is required.", "ERROR"
                )
                return self

            self.log(
                "Fabric name: '{fabric_name}".format(fabric_name=fabric_name), "DEBUG"
            )
            self.response.append({"response": {}, "msg": {}})
            self.response[0].get("response").update({fabric_name: {}})
            self.response[0].get("msg").update({fabric_name: {}})
            layer3_virtual_network = multicast_config.get("layer3_virtual_network")
            if not layer3_virtual_network:
                self.log(
                    "Error: 'layer3_virtual_network' is missing from input.", "ERROR"
                )
                self.set_operation_result(
                    "failed",
                    False,
                    "Layer 3 virtual network name is required.",
                    "ERROR",
                )
                return self

            self.log(
                "Layer 3 virtual network name: '{l3_vn}".format(
                    l3_vn=layer3_virtual_network
                ),
                "DEBUG",
            )
            self.response[0].get("response").get(fabric_name).update(
                {layer3_virtual_network: {}}
            )
            self.response[0].get("msg").get(fabric_name).update(
                {layer3_virtual_network: {}}
            )
            result_fabric_multicast_msg = (
                self.response[0].get("msg").get(fabric_name).get(layer3_virtual_network)
            )
            result_fabric_multicast_response = (
                self.response[0]
                .get("response")
                .get(fabric_name)
                .get(layer3_virtual_network)
            )
            multicast_details_exists = self.have.get("fabric_multicast")[
                fabric_multicast_index
            ].get("exists")
            self.log(
                "Check if the multicast configuration is present in the Cisco Catalyst Center or not.",
                "DEBUG",
            )
            if not multicast_details_exists:
                self.log(
                    "The multicast configurations for the VN '{l3_vn}' under the '{fabric_name}' is not present "
                    "in the Cisco Catalyst Center.".format(
                        l3_vn=layer3_virtual_network, fabric_name=fabric_name
                    ),
                    "DEBUG",
                )
                multicast_params = self.want.get("fabric_multicast")[
                    fabric_multicast_index
                ].get("multicast_details")
                replication_params = self.want.get("fabric_multicast")[
                    fabric_multicast_index
                ].get("replication_mode_details")
                to_create_multicast.append(multicast_params)
                result_fabric_multicast_response.update(
                    {"multicast_details": multicast_params}
                )
                result_fabric_multicast_msg.update(
                    {
                        "multicast_details": "SDA fabric multicast configurations added successfully."
                    }
                )
                to_update_replication_mode.append(replication_params)
                result_fabric_multicast_response.update(
                    {"replication_mode": replication_params}
                )
                result_fabric_multicast_msg.update(
                    {
                        "replication_mode": "SDA fabric replication mode updated successfully."
                    }
                )
            else:
                self.log(
                    "The multicast configurations for the VN '{l3_vn}' under the '{fabric_name}' is available "
                    "in the Cisco Catalyst Center.".format(
                        l3_vn=layer3_virtual_network, fabric_name=fabric_name
                    ),
                    "DEBUG",
                )
                want_multicast_params = self.want.get("fabric_multicast")[
                    fabric_multicast_index
                ].get("multicast_details")
                want_replication_params = self.want.get("fabric_multicast")[
                    fabric_multicast_index
                ].get("replication_mode_details")
                have_multicast_params = self.have.get("fabric_multicast")[
                    fabric_multicast_index
                ].get("multicast_details")
                have_replication_params = self.have.get("fabric_multicast")[
                    fabric_multicast_index
                ].get("replication_mode_details")
                updated_multicast_params = self.retain_multicast_cc_values(
                    want_multicast_params, have_multicast_params
                )
                self.log(
                    "The updated playbook details after retaining the Cisco Catalyst Center details "
                    "to the playbook details: {updated_multicast_params}".format(
                        updated_multicast_params=updated_multicast_params
                    )
                )

                if not self.requires_update(
                    have_multicast_params,
                    updated_multicast_params,
                    self.multicast_vn_obj_params,
                ):
                    self.log(
                        "SDA fabric multicast configuration for the layer 3 VN '{l3_vn}' under the fabric "
                        "'{fabric_name}' doesn't require an update.".format(
                            l3_vn=layer3_virtual_network, fabric_name=fabric_name
                        ),
                        "INFO",
                    )
                    result_fabric_multicast_msg.update(
                        {
                            "multicast_details": "SDA fabric multicast configurations doesn't require an update."
                        }
                    )
                else:

                    # Multicast configuration needs an update
                    self.log(
                        "Updating multicast configuration for VN '{l3_vn}' under fabric '{fabric_name}'.".format(
                            l3_vn=layer3_virtual_network, fabric_name=fabric_name
                        ),
                        "INFO",
                    )
                    self.log(
                        "Desired SDA multicast configuration for '{l3_vn}' under the fabric '{fabric_name} "
                        "in Cisco Catalyst Center: {desired_state}".format(
                            l3_vn=layer3_virtual_network,
                            fabric_name=fabric_name,
                            desired_state=updated_multicast_params,
                        ),
                        "DEBUG",
                    )
                    updated_multicast_params.update(
                        {
                            "id": self.have.get("fabric_multicast")[
                                fabric_multicast_index
                            ].get("id")
                        }
                    )
                    to_update.append(updated_multicast_params)
                    result_fabric_multicast_response.update(
                        {"multicast_details": want_multicast_params}
                    )
                    result_fabric_multicast_msg.update(
                        {
                            "multicast_details": "SDA fabric multicast configurations updated successfully."
                        }
                    )

                if not self.requires_update(
                    have_replication_params,
                    want_replication_params,
                    self.replication_mode_obj_params,
                ):
                    self.log(
                        "No updates required for replication mode for VN '{l3_vn}' under fabric '{fabric_name}'.".format(
                            l3_vn=layer3_virtual_network, fabric_name=fabric_name
                        ),
                        "INFO",
                    )
                    if "updated successfully" not in result_fabric_multicast_msg.get(
                        "multicast_details"
                    ):
                        result_fabric_multicast_msg.update(
                            {
                                "multicast_details": "SDA fabric replication mode doesn't require an update."
                            }
                        )
                else:

                    # Replication mode needs an update
                    self.log(
                        "Current SDA fabric replication mode for '{l3_vn}' under the fabric '{fabric_name} "
                        "in Cisco Catalyst Center: {current_state}".format(
                            l3_vn=layer3_virtual_network,
                            fabric_name=fabric_name,
                            current_state=have_replication_params,
                        ),
                        "DEBUG",
                    )
                    self.log(
                        "Desired SDA fabric replication mode for '{l3_vn}' under the fabric '{fabric_name} "
                        "in Cisco Catalyst Center: {desired_state}".format(
                            l3_vn=layer3_virtual_network,
                            fabric_name=fabric_name,
                            desired_state=want_replication_params,
                        ),
                        "DEBUG",
                    )
                    to_update_replication_mode.append(want_replication_params)
                    result_fabric_multicast_response.update(
                        {"multicast_details": want_replication_params}
                    )
                    result_fabric_multicast_msg.update(
                        {
                            "multicast_details": "SDA fabric replication mode updated successfully."
                        }
                    )

        if to_create_multicast:
            self.log(
                "Attempting to configure {count} multicast configuration(s).".format(
                    count=len(to_create_multicast)
                ),
                "INFO",
            )
            self.bulk_add_multicast_config(to_create_multicast).check_return_status()

        if to_update_replication_mode:
            self.log(
                "Attempting to update {count} replication mode(s).".format(
                    count=len(to_update_replication_mode)
                ),
                "INFO",
            )
            self.bulk_update_replication_mode(
                to_update_replication_mode
            ).check_return_status()

        if to_update:
            self.log(
                "Attempting to update {count} multicast configuration(s).".format(
                    count=len(to_update)
                ),
                "INFO",
            )
            self.bulk_update_multicast_config(to_update).check_return_status()

        self.result.update({"response": self.response})
        self.log("SDA fabric multicast updates completed successfully.", "INFO")
        self.msg = "The operations on fabric device is successful."
        self.status = "success"
        return self

    def get_diff_merged(self, config):
        """
        Add or Update the SDA multicast configurations along with the source specific and
        any source configurations under the layer 3 virtual network of a fabric site
        in Cisco Catalyst Center based on the playbook details.

        Parameters:
            config (list of dict): Playbook details containing SDA fabric multicast information.
        Returns:
            self (object): The current object with updated desired fabric multicast information.
        Description:
            If the 'fabric_multicast' is available in the playbook, call the function
            'update_fabric_multicast'. Else return self.
        """

        fabric_multicast = config.get("fabric_multicast")
        if fabric_multicast is not None:
            self.log(
                "Updating fabric multicast config: {multicast_config}".format(
                    multicast_config=fabric_multicast
                ),
                "DEBUG",
            )
            try:
                self.update_fabric_multicast(fabric_multicast).check_return_status()
                self.log(
                    "Successfully updated {count} fabric multicast configuration(s).".format(
                        count=len(fabric_multicast)
                    ),
                    "INFO",
                )
            except Exception as e:
                self.log(
                    "Error while updating fabric multicast: {error}".format(
                        error=str(e)
                    ),
                    "ERROR",
                )
                self.set_operation_result(
                    "failed",
                    False,
                    "Failed to update fabric multicast configuration(s).",
                    "ERROR",
                )
                return self
        else:
            self.log(
                "No 'fabric_multicast' found in configuration. Skipping update.",
                "WARNING",
            )

        self.msg = "Successfully merged the SDA fabric multicast configurations."
        self.status = "success"
        return self

    def delete_fabric_multicast(self, fabric_multicast):
        """
        Delete fabric multicast configurations associated with the virtual network
        in Cisco Catalyst Center with fields provided in playbook.

        Parameters:
            fabric_multicast (dict): SDA fabric multicast associated with the L3 virtual network
                                     under a fabric site playbook details.
        Returns:
            self (object): The current object with updated desired Fabric Multicast information.
        Description:
            Check if the multicast configuration associated with the Layer 3 virtual network
            exists or not.
            If it does, check for the ssm and asm configuration in the playbook.
            If one of the exists, remove that configuration or remove the entire multicast
            configuration of the layer 3 virtual network.
            If there is no multicast configuration associated with the layer 3 virtual
            network, exit the function after adding required messages to the response.
        """

        self.log(
            "Starting the process of deleting the multicast configuration associated to the virtual network...",
            "DEBUG",
        )

        self.response.append({"response": {}, "msg": {}})
        result_fabric_multicast_response = self.response[0].get("response")
        result_fabric_multicast_msg = self.response[0].get("msg")
        fabric_multicast_index = -1
        for item in fabric_multicast:
            fabric_multicast_index += 1
            fabric_name = item.get("fabric_name")
            if not fabric_name:
                self.log("Error: 'fabric_name' is missing from input.", "ERROR")
                self.set_operation_result(
                    "failed", False, "Fabric name is required.", "ERROR"
                )
                return self

            layer3_virtual_network = item.get("layer3_virtual_network")
            if not layer3_virtual_network:
                self.log(
                    "Error: 'layer3_virtual_network' is missing from input.", "ERROR"
                )
                self.set_operation_result(
                    "failed", False, "Layer 3 virtual network is required.", "ERROR"
                )
                return self

            if result_fabric_multicast_response.get(fabric_name) is None:
                result_fabric_multicast_response.update({fabric_name: {}})

            result_fabric_multicast_response.get(fabric_name).update(
                {layer3_virtual_network: {}}
            )

            if result_fabric_multicast_msg.get(fabric_name) is None:
                result_fabric_multicast_msg.update({fabric_name: {}})

            result_fabric_multicast_msg.get(fabric_name).update(
                {layer3_virtual_network: {}}
            )
            result_response_fabric_name = result_fabric_multicast_response.get(
                fabric_name
            )
            result_msg_fabric_name = result_fabric_multicast_msg.get(fabric_name)

            self.log(
                "Starting deletion of fabric multicast configuration under fabric '{fabric_name}' "
                "for the Layer 3 virtual network {layer3_virtual_network}.".format(
                    fabric_name=fabric_name,
                    layer3_virtual_network=layer3_virtual_network,
                ),
                "DEBUG",
            )

            have_fabric_multicast_config = self.have.get("fabric_multicast")[
                fabric_multicast_index
            ]
            multicast_config_exists = have_fabric_multicast_config.get("exists")

            self.log(
                "The multicast configuration exists '{exists}' with the layer 3 virtual network "
                "'{layer3_vn}' for the fabric site '{fabric_name}'.".format(
                    exists=multicast_config_exists,
                    layer3_vn=layer3_virtual_network,
                    fabric_name=fabric_name,
                ),
                "INFO",
            )
            if not multicast_config_exists:
                self.log(
                    "Multicast conigurations for the layer 3 virtual network '{l3_vn}' under the "
                    "fabric site '{fabric_name}' is not found in Cisco Catalyst Center.".format(
                        l3_vn=layer3_virtual_network, fabric_name=fabric_name
                    ),
                    "INFO",
                )
                result_msg_fabric_name.get(layer3_virtual_network).update(
                    {
                        "multicast_details": "SDA multicast configs are not found for the layer 3 virtual network."
                    }
                )
                result_response_fabric_name.get(layer3_virtual_network).update(
                    {
                        "multicast_details": "SDA multicast configs are not found for the layer 3 virtual network."
                    }
                )
                continue

            # Retrieve details
            self.log(
                "Deleting specific SSM or ASM configurations for Layer 3 VN '{l3_vn}' in fabric '{fabric_name}'.".format(
                    l3_vn=layer3_virtual_network, fabric_name=fabric_name
                ),
                "DEBUG",
            )
            ssm_details = item.get("ssm")
            asm_details = item.get("asm")
            id = have_fabric_multicast_config.get("id")
            if not (ssm_details or asm_details):
                self.log(
                    "Deleting fabric multicast configuration for the layer 3 virtual network '{l3_vn}' "
                    "under the fabric site '{fabric_name}' with ID '{id}'".format(
                        l3_vn=layer3_virtual_network, fabric_name=fabric_name, id=id
                    ),
                    "DEBUG",
                )
                try:
                    payload = {"id": id}
                    task_name = "delete_multicast_virtual_network_by_id_v1"
                    task_id = self.get_taskid_post_api_call("sda", task_name, payload)
                    if not task_id:
                        self.msg = "Unable to retrive the task_id for the task '{task_name}'.".format(
                            task_name=task_name
                        )
                        self.set_operation_result(
                            "failed", False, self.msg, "ERROR"
                        ).check_return_status()

                    success_msg = (
                        "Successfully deleted the SDA fabric multicast configurations."
                    )
                    self.get_task_status_from_tasks_by_id(
                        task_id, task_name, success_msg
                    ).check_return_status()
                    result_msg_fabric_name.get(layer3_virtual_network).update(
                        {
                            "multicast_details": "SDA device successfully removed for the layer 3 virtual network."
                        }
                    )
                    result_response_fabric_name.get(layer3_virtual_network).update(
                        {"multicast_details": id}
                    )

                except Exception as e:
                    self.msg = (
                        "Exception occurred while deleting the multicast configurations "
                        "for the layer 3 virtual network '{l3_vn}' for the fabric site '{fabric_name}': {error_msg}".format(
                            l3_vn=layer3_virtual_network,
                            fabric_name=fabric_name,
                            error_msg=e,
                        )
                    )
                    self.log(self.msg, "ERROR")
                    self.set_operation_result(
                        "failed", False, self.msg, "ERROR"
                    ).check_return_status()
            else:
                self.log(
                    "Deleting specific SSM or ASM configurations for Layer 3 VN '{l3_vn}' in fabric '{fabric_name}'.".format(
                        l3_vn=layer3_virtual_network, fabric_name=fabric_name
                    ),
                    "DEBUG",
                )
                to_update = []
                have_multicast_params = self.have.get("fabric_multicast")[
                    fabric_multicast_index
                ].get("multicast_details")
                want_multicast_params = self.want.get("fabric_multicast")[
                    fabric_multicast_index
                ].get("multicast_details")
                want_ssm = want_multicast_params.get("ipv4SsmRanges")
                have_ssm = have_multicast_params.get("ipv4SsmRanges")
                is_ssm_empty = False
                is_need_update = False
                if not have_ssm:
                    if not want_ssm:
                        is_ssm_empty = True

                    self.log(
                        "SDA fabric multicast ssm configurations are not present in the "
                        "layer 3 VN '{l3_vn}' under the fabric '{fabric_name}'.".format(
                            l3_vn=layer3_virtual_network, fabric_name=fabric_name
                        ),
                        "INFO",
                    )
                else:
                    if want_ssm:
                        want_multicast_params.update({"ipv4SsmRanges": have_ssm})
                        for item in want_ssm:
                            if item in have_ssm:

                                # Multicast configuration needs an update
                                is_need_update = True
                                self.log(
                                    "The ssm config '{item}' is still present in the Cisco Catalyst Center.".format(
                                        item=item
                                    ),
                                    "INFO",
                                )
                                want_multicast_params.get("ipv4SsmRanges").remove(item)
                                if want_multicast_params.get("ipv4SsmRanges") == []:
                                    self.log(
                                        "The entire ssm config is going to be removed from the L3 virtual network "
                                        "'{l3_vn}' under the fabric site '{fabric_name}'".format(
                                            l3_vn=layer3_virtual_network,
                                            fabric_name=fabric_name,
                                        ),
                                        "INFO",
                                    )
                                    is_ssm_empty = True
                    else:
                        is_ssm_empty = True

                have_asm = (
                    self.have.get("fabric_multicast")[fabric_multicast_index]
                    .get("multicast_details")
                    .get("multicastRPs")
                )
                want_asm = want_multicast_params.get("multicastRPs")
                is_asm_empty = False

                if not have_asm:
                    if not want_asm:
                        is_asm_empty = True

                    self.log(
                        "SDA fabric multicast asm configurations are not present in the "
                        "layer 3 VN '{l3_vn}' under the fabric '{fabric_name}'.".format(
                            l3_vn=layer3_virtual_network, fabric_name=fabric_name
                        ),
                        "INFO",
                    )
                else:
                    if want_asm:
                        want_multicast_params.update({"multicastRPs": have_asm})
                        for item in want_asm:
                            rp_device_location = item.get("rpDeviceLocation")
                            self.log(
                                "The 'rp_device_location' is {rp_device_location}".format(
                                    rp_device_location=rp_device_location
                                ),
                                "DEBUG",
                            )
                            if rp_device_location == "FABRIC":
                                want_nw_device_ids = item.get("networkDeviceIds")
                                want_nw_device_ids = set(want_nw_device_ids)
                                self.log(
                                    "The network device ID of the 'FABRIC' is '{device_ids}'.".format(
                                        device_ids=want_nw_device_ids
                                    ),
                                    "DEBUG",
                                )
                                have_nw_device = get_dict_result(
                                    have_asm, "rpDeviceLocation", "FABRIC"
                                )
                                self.log(
                                    "The RP device details: {have_nw_device}".format(
                                        have_nw_device=have_nw_device
                                    ),
                                    "DEBUG",
                                )
                                if have_nw_device:
                                    have_nw_device_ids = have_nw_device.get(
                                        "networkDeviceIds"
                                    )
                                    common_elem = [
                                        id
                                        for id in have_nw_device_ids
                                        if id not in want_nw_device_ids
                                    ]
                                    self.log(
                                        "The common elements found in the playbook and Cisco Catalyst Center "
                                        "are '{common_elem}".format(
                                            common_elem=common_elem
                                        ),
                                        "DEBUG",
                                    )
                                    if common_elem:
                                        item.update({"networkDeviceIds": common_elem})
                                    else:
                                        multicast_rps = (
                                            self.want.get("fabric_multicast")[
                                                fabric_multicast_index
                                            ]
                                            .get("multicast_details")
                                            .get("multicastRPs")
                                        )
                                        for value in multicast_rps:
                                            if (
                                                value.get("rpDeviceLocation")
                                                == "FABRIC"
                                            ):
                                                multicast_rps.remove(value)

                                    is_need_update = True
                            else:
                                ex_rp_ipv4_address = item.get("ipv4Address")
                                ex_rp_ipv6_address = item.get("ipv6Address")
                                multicast_rps = (
                                    self.want.get("fabric_multicast")[
                                        fabric_multicast_index
                                    ]
                                    .get("multicast_details")
                                    .get("multicastRPs")
                                )
                                if ex_rp_ipv4_address:
                                    ex_ipv4_details = get_dict_result(
                                        have_asm, "ipv4Address", ex_rp_ipv4_address
                                    )
                                    if ex_ipv4_details:
                                        for value in multicast_rps:
                                            if (
                                                value.get("ipv4Address")
                                                == ex_rp_ipv4_address
                                            ):
                                                want_multicast_params.get(
                                                    "multicastRPs"
                                                ).remove(value)

                                        is_need_update = True

                                elif ex_rp_ipv6_address:
                                    ex_ipv6_details = get_dict_result(
                                        have_asm, "ipv6Address", ex_rp_ipv6_address
                                    )
                                    if ex_ipv6_details:
                                        for value in multicast_rps:
                                            if (
                                                value.get("ipv6Address")
                                                == ex_rp_ipv6_address
                                            ):
                                                want_multicast_params.get(
                                                    "multicastRPs"
                                                ).remove(value)

                                        is_need_update = True

                            if not want_multicast_params.get("multicastRPs"):
                                self.log(
                                    "The entire asm config is going to be removed from the L3 virtual network "
                                    "'{l3_vn}' under the fabric site '{fabric_name}'".format(
                                        l3_vn=layer3_virtual_network,
                                        fabric_name=fabric_name,
                                    ),
                                    "INFO",
                                )
                                is_asm_empty = True
                    else:
                        is_asm_empty = True

                if is_asm_empty and is_ssm_empty:
                    self.log(
                        "Error: The multicast configurations should have either ssm or asm config "
                        "for the layer 3 virtual network '{l3_vn}' under the fabric site '{fabric_name}'.".format(
                            l3_vn=layer3_virtual_network, fabric_name=fabric_name
                        ),
                        "ERROR",
                    )
                    self.msg = (
                        "The multicast configurations should have either ssm or asm config "
                        "for the layer 3 virtual network '{l3_vn}' under the fabric site '{fabric_name}'.".format(
                            l3_vn=layer3_virtual_network, fabric_name=fabric_name
                        )
                    )
                    self.set_operation_result(
                        "failed", False, self.msg, "ERROR"
                    ).check_return_status()

                if is_need_update:
                    want_multicast_params.update(
                        {
                            "id": self.have.get("fabric_multicast")[
                                fabric_multicast_index
                            ].get("id")
                        }
                    )
                    to_update.append(want_multicast_params)

                if to_update:
                    result_response_fabric_name.get(layer3_virtual_network).update(
                        {"multicast_details": want_multicast_params}
                    )
                    result_msg_fabric_name.get(layer3_virtual_network).update(
                        {
                            "multicast_details": "SDA fabric multicast configurations updated successfully."
                        }
                    )
                    self.log(
                        "Attempting to update {count} multicast configuration(s).".format(
                            count=len(to_update)
                        ),
                        "INFO",
                    )
                    self.bulk_update_multicast_config(to_update).check_return_status()
                else:
                    self.log(
                        "SDA fabric multicast configuration for the layer 3 VN '{l3_vn}' under the fabric "
                        "'{fabric_name}' doesn't require an update.".format(
                            l3_vn=layer3_virtual_network, fabric_name=fabric_name
                        ),
                        "INFO",
                    )
                    result_msg_fabric_name.get(layer3_virtual_network).update(
                        {
                            "multicast_details": "SDA fabric multicast configurations doesn't require an update."
                        }
                    )

        self.result.update({"response": self.response})
        self.msg = "The deletion of devices L2 Handoff, L3 Handoff with IP and SDA transit is successful."
        self.log(str(self.msg), "DEBUG")
        self.status = "success"
        return self

    def get_diff_deleted(self, config):
        """
        Delete the SDA multicast configurations associated with the virtual network in
        the fabric site in Cisco Catalyst Center based on the playbook details.

        Parameters:
            config (list of dict): Playbook details containing SDA fabric multicast information.
        Returns:
            self (object): The current object with updated desired Fabric Multicast information.
        Description:
            If the 'fabric_multicast' is available in the playbook, call the function 'delete_fabric_multicast'.
            Else return self.
        """

        fabric_multicast = config.get("fabric_multicast")
        if fabric_multicast is not None:
            self.log(
                "Fabric multicast found in the configuration. Initiating deletion process.",
                "INFO",
            )
            self.delete_fabric_multicast(fabric_multicast)
        else:
            self.log(
                "No fabric multicast configurations found in the configuration."
                "No deletion actions performed.",
                "INFO",
            )

        self.msg = "Successfully deleted the SDA fabric multicast configurations."
        self.status = "success"
        return self

    def verify_diff_merged(self, config):
        """
        Validating the Cisco Catalyst Center configuration with the playbook details
        when state is merged (Create/Update).

        Parameters:
            config (dict): Playbook details containing fabric multicast configurations.
        Returns:
            self (object): The current object with updated fabric multicast configurations.
        Description:
            Call the get_have function to collected the updated information from the Cisco Catalyst Center.
            Check the difference between the information provided by the user and the information collected
            from the Cisco Catalyst Center. If there is any difference, then the config is not applied to
            the Cisco Catalyst Center.
        """

        self.get_have(config)
        self.log(
            "Current State (have): {current_state}".format(current_state=self.have),
            "INFO",
        )
        self.log(
            "Desired State (want): {requested_state}".format(requested_state=self.want),
            "INFO",
        )
        fabric_multicast = config.get("fabric_multicast")

        # Retrieve fabric multicast details from the config
        fabric_multicast = config.get("fabric_multicast")
        if fabric_multicast is None:
            self.log(
                "No fabric multicast configurations found in the playbook. Nothing to validate.",
                "INFO",
            )
            self.msg = "No fabric multicast configurations to validate."
            self.status = "success"
            return self

        fabric_multicast_index = -1
        for item in fabric_multicast:
            fabric_name = item.get("fabric_name")
            fabric_multicast_index += 1
            layer3_virtual_network = item.get("layer3_virtual_network")
            have_details = self.have.get("fabric_multicast")[fabric_multicast_index]
            want_details = self.want.get("fabric_multicast")[fabric_multicast_index]

            # Verifying whether the multicast configuration of the L3 VN on a fabric site is applied or not
            if have_details:
                have_details = have_details.get("multicast_details")

            if want_details:
                want_details = want_details.get("multicast_details")

            if self.requires_update(
                have_details, want_details, self.multicast_vn_obj_params
            ):
                self.msg = (
                    "The SDA multicast configuration of the layer 3 virtual network '{l3_vn}' "
                    "under the fabric site '{fabric_name}' is not applied to the Cisco Catalyst Center.".format(
                        l3_vn=layer3_virtual_network, fabric_name=fabric_name
                    )
                )
                self.set_operation_result(
                    "failed", False, self.msg, "ERROR"
                ).check_return_status()

            self.log(
                "Successfully validated the presence of the multicast configs of "
                "layer 3 virtual network '{l3_vn}' under the fabric site '{fabric_name}.".format(
                    l3_vn=layer3_virtual_network, fabric_name=fabric_name
                ),
                "INFO",
            )

            have_replication_details = self.have.get("replication_mode_details")
            want_replication_details = self.want.get("replication_mode_details")

            # Verifying whether the replication mode of the fabric site is applied or not
            if (
                have_replication_details
                and want_replication_details
                and self.requires_update(
                    have_replication_details,
                    want_replication_details,
                    self.replication_mode_obj_params,
                )
            ):
                self.msg = (
                    "The replication mode of the fabric site '{fabric_name}' provided "
                    "in the playbook is not applied to the Cisco Catalyst Center.".format(
                        fabric_name=fabric_name
                    )
                )
                self.set_operation_result(
                    "failed", False, self.msg, "ERROR"
                ).check_return_status()

            self.log(
                "Successfully validated the presence of the replication mode config "
                "under the fabric site '{fabric_name}.".format(fabric_name=fabric_name),
                "INFO",
            )

            self.response[0].get("msg").get(fabric_name).update(
                {"Validation": "Success"}
            )

        self.result.update({"response": self.response})
        self.msg = "Successfully validated the SDA fabric configurations."
        self.status = "success"
        return self

    def verify_ssm_asm(self, want_ssm, want_asm, fabric_multicast_index, fabric_name):
        """
        Validating the Cisco Catalyst Center configuration with the playbook details
        for the state is deleted when the ssm and the asm configuration are provided.

        Parameters:
            want_ssm (dict): The Source specific multicast configurations provided in the playbook.
            want_asm (list of dict): The Any source multicast configurations provided in the playbook.
            fabric_multicast_index (int): The index which points to the which item in the config.
            fabric_name (str): The name of the fabric site.
        Returns:
            self (object): The current object with updated desired fabric multicast configurations.
        Description:
        """

        have_ssm = self.have.get("fabric_multicast")[fabric_multicast_index].get(
            "multicast_details"
        )
        if have_ssm:
            have_ssm = have_ssm.get("ipv4SsmRanges")

        self.msg = (
            "The SDA fabric multicast configurations are not applied to the Cisco Catalyst Center"
            "for the config at position '{idx}' under the fabric site '{fabric_name}'.".format(
                idx=fabric_multicast_index + 1, fabric_name=fabric_name
            )
        )
        self.log(
            "The ssm configurations present in the Cisco Catalyst Center: {ssm}".format(
                ssm=have_ssm
            ),
            "INFO",
        )
        self.log(
            "The ssm configurations provided in the playbook: {ssm}".format(
                ssm=want_asm
            ),
            "INFO",
        )
        if want_ssm:
            want_ssm = want_ssm.get("ipv4_ssm_ranges")

        if not want_ssm:
            self.log(
                "No SSM configurations provided in the playbook. Skipping SSM validation for fabric '{fabric_name}'.".format(
                    fabric_name=fabric_name
                ),
                "DEBUG",
            )
        else:
            self.log(
                "Validating SSM configurations for fabric '{fabric_name}'.".format(
                    fabric_name=fabric_name
                ),
                "INFO",
            )
            for item in want_ssm:
                if have_ssm and item in have_ssm:
                    self.log(
                        "The ssm config '{item}' is still present in the Cisco Catalyst Center "
                        "for the fabric site '{fabric_name}'.".format(
                            item=item, fabric_name=fabric_name
                        ),
                        "INFO",
                    )
                    self.set_operation_result(
                        "failed", False, self.msg, "ERROR"
                    ).check_return_status()

        have_asm = self.have.get("fabric_multicast")[fabric_multicast_index].get(
            "multicast_details"
        )
        if have_asm:
            have_asm = have_asm.get("multicastRPs")

        if not want_asm:
            self.log(
                "No ASM configurations provided in the playbook. Skipping ASM validation for fabric '{fabric_name}'.".format(
                    fabric_name=fabric_name
                ),
                "DEBUG",
            )
        else:
            for item in want_asm:
                rp_device_location = item.get("rp_device_location")
                if rp_device_location == "FABRIC":
                    have_rp_details = get_dict_result(
                        have_asm, "rpDeviceLocation", "FABRIC"
                    )
                    if not have_rp_details:
                        self.log(
                            "RP details not found in Cisco Catalyst Center for 'FABRIC' devices "
                            "in fabric '{fabric_name}'.".format(
                                fabric_name=fabric_name
                            ),
                            "DEBUG",
                        )
                        continue

                    want_nw_device_ips = item.get("networkDeviceIds")
                    want_nw_device_ips = set(want_nw_device_ips)
                    want_nw_device_ids = []
                    for ip in want_nw_device_ips:
                        network_device_details = self.get_device_details_from_ip(ip)
                        self.log(
                            "The device with the IP {ip} is a valid network device IP.".format(
                                ip=item
                            ),
                            "DEBUG",
                        )
                        network_device_id = network_device_details[0].get("id")
                        want_nw_device_ids.append(network_device_id)

                    have_nw_device_ids = have_rp_details.get("networkDeviceIds")
                    common_elem = [
                        id for id in have_nw_device_ids if id not in want_nw_device_ids
                    ]
                    if common_elem:
                        self.log(
                            "Validation failed: ASM configuration '{item}' for 'FABRIC' devices is still present "
                            "in Cisco Catalyst Center for fabric '{fabric_name}'. Expected it to be absent.".format(
                                item=item, fabric_name=fabric_name
                            ),
                            "ERROR",
                        )
                        self.set_operation_result(
                            "failed", False, self.msg, "ERROR"
                        ).check_return_status()

                else:
                    ex_rp_ipv4_address = item.get("ex_rp_ipv4_address")
                    ex_rp_ipv6_address = item.get("ex_rp_ipv6_address")
                    if ex_rp_ipv4_address:
                        ex_ipv4_details = get_dict_result(
                            have_asm, "ipv4Address", ex_rp_ipv4_address
                        )
                        if ex_ipv4_details:
                            self.log(
                                "Validation failed: ASM configuration '{item}' for EXTERNAL IPv4 address "
                                "'{ex_rp_ipv4_address}' is still present in Cisco Catalyst Center for "
                                "fabric '{fabric_name}'. Expected it to be absent.".format(
                                    item=item,
                                    ex_rp_ipv4_address=ex_rp_ipv4_address,
                                    fabric_name=fabric_name,
                                ),
                                "ERROR",
                            )
                            self.set_operation_result(
                                "failed", False, self.msg, "ERROR"
                            ).check_return_status()
                    else:
                        ex_ipv6_details = get_dict_result(
                            have_asm, "ipv6Address", ex_rp_ipv6_address
                        )
                        if ex_ipv6_details:
                            self.log(
                                "Validation failed: ASM configuration '{item}' for EXTERNAL IPv6 address "
                                "'{ex_rp_ipv6_address}' is still present in Cisco Catalyst Center for "
                                "fabric '{fabric_name}'. Expected it to be absent.".format(
                                    item=item,
                                    ex_rp_ipv6_address=ex_rp_ipv6_address,
                                    fabric_name=fabric_name,
                                ),
                                "ERROR",
                            )
                            self.set_operation_result(
                                "failed", False, self.msg, "ERROR"
                            ).check_return_status()

        self.msg = "Successfully validated the absence of ssm and asm config in the Cisco Catalyst Center."
        self.status = "success"
        return self

    def verify_diff_deleted(self, config):
        """
        Validating the Cisco Catalyst Center configuration with the playbook details
        when state is deleted (delete).

        Parameters:
            config (dict): Playbook details containing fabric multicast configurations.
        Returns:
            self (object): The current object with updated desired fabric multicast configurations.
        Description:
            Call the get_have function to collected the updated information from the Cisco Catalyst Center.
            Check if the config provided by the user is present in the Cisco Catalyst Center or not
            If the config is available in the Cisco Catalyst Center then the config is not applied to
            the Cisco Catalyst Center.
        """

        self.get_have(config)
        self.log(
            "Current State (have): {current_state}".format(current_state=self.have),
            "INFO",
        )
        fabric_multicast = config.get("fabric_multicast")

        # Retrieve fabric multicast configurations from the playbook
        fabric_multicast = config.get("fabric_multicast")
        if fabric_multicast is None:
            self.log(
                "No fabric multicast configurations provided in the playbook. Skipping validation.",
                "INFO",
            )
            self.msg = "No fabric multicast configurations to validate."
            self.status = "success"
            return self

        # Iterate over each fabric multicast configuration
        fabric_multicast_index = -1
        for item in fabric_multicast:
            fabric_multicast_index += 1
            fabric_name = item.get("fabric_name")
            layer3_virtual_network = item.get("layer3_virtual_network")
            want_details = config.get("fabric_multicast")[fabric_multicast_index]
            ssm = None
            asm = None
            self.log(
                "Validating deletion for fabric '{fabric_name}' and Layer 3 virtual network '{l3_vn}'.".format(
                    fabric_name=fabric_name, l3_vn=layer3_virtual_network
                ),
                "INFO",
            )
            if want_details:
                ssm = want_details.get("ssm")
                asm = want_details.get("asm")

            if ssm or asm:
                self.log(
                    "SSM or ASM configurations found in the playbook. Validating "
                    "their absence in Cisco Catalyst Center.",
                    "INFO",
                )
                self.verify_ssm_asm(ssm, asm, fabric_multicast_index, fabric_name)
            else:
                fabric_multicast_details = self.have.get("fabric_multicast")[
                    fabric_multicast_index
                ]
                fabric_multicast_exists = fabric_multicast_details.get("exists")

                # Verifying the absence of the SDA multicast configurations for a L3 VN under a fabric site
                if fabric_multicast_exists:
                    self.msg = (
                        "Validation failed: The SDA fabric multicast configurations for Layer 3 virtual network '{l3_vn}' "
                        "under fabric '{fabric_name}' are still present in Cisco Catalyst Center. Expected them to be deleted.".format(
                            l3_vn=layer3_virtual_network, fabric_name=fabric_name
                        )
                    )
                    self.set_operation_result(
                        "failed", False, self.msg, "ERROR"
                    ).check_return_status()

                self.log(
                    "Successfully validated absence of SDA multicast configurations for the "
                    "Layer 3 virtual network '{l3_vn}' under the fabric site '{fabric_name}'.".format(
                        l3_vn=layer3_virtual_network, fabric_name=fabric_name
                    ),
                    "INFO",
                )

            self.response[0].get("msg").get(fabric_name).update(
                {"Validation": "Success"}
            )

        self.result.update({"response": self.response})
        self.msg = (
            "Successfully validated the absence of SDA fabric multicast configurations."
        )
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
    """Main entry ..."""

    # Define the specification for module arguments
    element_spec = {
        "dnac_host": {"type": "str", "required": True},
        "dnac_port": {"type": "str", "default": "443"},
        "dnac_username": {"type": "str", "default": "admin", "aliases": ["user"]},
        "dnac_password": {"type": "str", "no_log": True},
        "dnac_verify": {"type": "bool", "default": True},
        "dnac_version": {"type": "str", "default": "2.2.3.3"},
        "dnac_debug": {"type": "bool", "default": False},
        "dnac_log": {"type": "bool", "default": False},
        "dnac_log_level": {"type": "str", "default": "WARNING"},
        "dnac_log_file_path": {"type": "str", "default": "dnac.log"},
        "dnac_log_append": {"type": "bool", "default": True},
        "config_verify": {"type": "bool", "default": False},
        "dnac_api_task_timeout": {"type": "int", "default": 1200},
        "dnac_task_poll_interval": {"type": "int", "default": 2},
        "config": {"type": "list", "required": True, "elements": "dict"},
        "state": {"default": "merged", "choices": ["merged", "deleted"]},
        "validate_response_schema": {"type": "bool", "default": True},
    }

    # Create an AnsibleModule object with argument specifications
    module = AnsibleModule(argument_spec=element_spec, supports_check_mode=False)
    ccc_sda_multicast = FabricMulticast(module)
    ccc_version = ccc_sda_multicast.get_ccc_version()
    minimum_supported_version = "2.3.7.6"
    if (
        ccc_sda_multicast.compare_dnac_versions(ccc_version, minimum_supported_version)
        < 0
    ):
        ccc_sda_multicast.msg = (
            "The specified Catalyst Center version '{0}' does not support the SDA fabric multicast feature. "
            "Supported versions start from '{1}'. Version '{1}' introduces APIs for managing multicast configurations.".format(
                ccc_version, minimum_supported_version
            )
        )
        ccc_sda_multicast.status = "failed"
        ccc_sda_multicast.check_return_status()

    state = ccc_sda_multicast.params.get("state")
    config_verify = ccc_sda_multicast.params.get("config_verify")
    if state not in ccc_sda_multicast.supported_states:
        ccc_sda_multicast.status = "invalid"
        ccc_sda_multicast.msg = "State '{state}' is invalid".format(state=state)
        ccc_sda_multicast.check_return_status()

    ccc_sda_multicast.validate_input().check_return_status()

    for config in ccc_sda_multicast.config:
        ccc_sda_multicast.reset_values()
        ccc_sda_multicast.get_have(config).check_return_status()
        ccc_sda_multicast.get_want(config).check_return_status()
        ccc_sda_multicast.get_diff_state_apply[state](config).check_return_status()
        if config_verify:
            ccc_sda_multicast.verify_diff_state_apply[state](
                config
            ).check_return_status()

    module.exit_json(**ccc_sda_multicast.result)


if __name__ == "__main__":
    main()
