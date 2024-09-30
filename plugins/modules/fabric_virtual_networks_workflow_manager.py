#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2022, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import absolute_import, division, print_function

__metaclass__ = type
__author__ = ("Abhishek Maheshwari, Madhan Sankaranarayanan")

DOCUMENTATION = r"""
---
module: fabric_virtual_networks_workflow_manager
short_description: Configure the layer2 fabric VLAN(s) and layer3 Virtual Network and configuring the Anycast Gateway(s)
        in the Cisco Catalyst Center Platform.
description:
- Creating the layer2 fabric VLAN(s) for the SDA operaation in Cisco Catalyst Center.
- Updating the layer2 fabric VLAN(s) for the SDA operaation in Cisco Catalyst Center.
- Deleting the layer2 fabric VLAN(s) for the SDA operaation in Cisco Catalyst Center.
- Creating the layer3 Virtual Network(s) for the SDA operaation in Cisco Catalyst Center.
- Updating the layer3 Virtual Network(s) for the SDA operaation in Cisco Catalyst Center.
- Deleting the layer3 Virtual Network(s) for the SDA operaation in Cisco Catalyst Center.
- Creating the Anycast Gateway(s) for the SDA operaation in Cisco Catalyst Center.
- Updating the Anycast Gateway(s) for the SDA operaation in Cisco Catalyst Center.
- Deleting the Anycast Gateway(s) for the SDA operaation in Cisco Catalyst Center.
version_added: '6.18.0'
extends_documentation_fragment:
  - cisco.dnac.workflow_manager_params
author: Abhishek Maheshwari (@abmahesh)
        Madhan Sankaranarayanan (@madhansansel)
options:
  config_verify:
    description: Set to True to verify the Cisco Catalyst Center config after applying the playbook config.
    type: bool
    default: False
  state:
    description: The state of Cisco Catalyst Center after module completion.
    type: str
    choices: [ merged, deleted ]
    default: merged
  config:
    description: A list containing detailed configurations for creating, updating, or deleting fabric sites or zones
        in a Software-Defined Access (SDA) environment. It also includes specifications for updating the authentication
        profile template for these sites. Each element in the list represents a specific operation to be performed on
        the SDA infrastructure, such as the addition, modification, or removal of fabric sites/zones, and modifications
        to authentication profiles.
    type: list
    elements: dict
    required: True
    suboptions:
      fabric_vlan:
        description: A list containing VLAN configurations for fabric sites in an SDA environment. Each VLAN entry
            includes information about its name, ID, traffic type, and wireless capabilities.
        type: list
        elements: dict
        suboptions:
          vlan_name:
            description: Name of the VLAN of the layer2 virtual network. Must contain only alphanumeric characters,
                underscores, and hyphens. And updation of this field is not allowed.
            type: str
            required: True
          vlan_id:
            description:  ID of the VLAN of the layer2 virtual network. Allowed VLAN range is 2-4093 except for
                reserved VLANs 1002-1005, and 2046. If deploying on a fabric zone, this vlanId must match the
                vlanId of the corresponding layer 2 virtual network on the fabric site. And updation of this
                field is not allowed.
            type: str
            required: True
          fabric_site_locations:
            description: A list of fabric site locations where this VLAN is deployed, including site hierarchy and fabric type details.
            type: list
            elements: dict
            suboptions:
              site_name:
                description: This name uniquely identifies the site for operations such as creating/updating/deleting any fabric
                    VLAN. This parameter is mandatory for any fabric Vlan management operation. And updation of this field is not allowed.
                type: str
                required: True
              fabric_type:
                description: Specifies the type of site to be managed within the SDA environment. The acceptable values are 'fabric_site'
                    and 'fabric_zone'. The default value is 'fabric_site', indicating the configuration of a broader network area, whereas
                    'fabric_zone' typically refers to a more specific segment within the site.
                type: str
                required: True
          traffic_type:
            description: The type of traffic handled by the VLAN (e.g., DATA, VOICE). By defaut it is set to "DATA".
            type: str
            required: True
          fabric_enabled_wireless:
            description: Indicates whether the fabric VLAN is enabled for wireless in the fabric environment. By default it is set to False.
            type: bool
          associated_layer3_virtual_network:
            description: Name of the layer3 virtual network associated with the layer2 fabric Vlan. This field is provided to support
                requests related to virtual network anchoring. The layer3 virtual network must have already been added to the fabric
                before association. This field must either be present in all payload elements or none. And updation of this field is
                not allowed.
            type: str
      virtual_networks:
        description: A list of virtual networks (VNs) configured within the SDA fabric. Each virtual network has associated information
            such as the name and anchored site.
        type: list
        elements: dict
        suboptions:
          vn_name:
            description: Name of the layer3 virtual network. The VN name must consist of only letters, numbers, and underscores, and
                must be between 1-16 characters in length. And updation of this field is not allowed.
            type: str
            required: True
          fabric_site_locations:
            description: A list of fabric site locations where this this layer 3 virtual network is to be assigned to, including site
                hierarchy and fabric type details. If this parameter is given make sure to provide the site_name and fabric_type as
                well as the required parameter to extend the virtual networks across given fabric sites.
            type: list
            elements: dict
            suboptions:
              site_name:
                description: This name uniquely identifies the site for operations such as creating/updating/deleting any layer3
                    virtual network.
                type: str
              fabric_type:
                description: Specifies the type of site to be managed within the SDA environment. The acceptable values are 'fabric_site'
                    and 'fabric_zone'. The default value is 'fabric_site', indicating the configuration of a broader network area, whereas
                    'fabric_zone' typically refers to a more specific segment within the site.
                type: str
          anchored_site_name:
            description: The name of the fabric site where the virtual network is anchored. And make sure when we are passing this
                parameter, fabric site location will contain same site_name and the size of fabric_site_locations field is one.
                In case all the parameters are passed, layer3 virtual network gets created and extended to multiple fabric sites
                but the operation gets failed because of anchored site and module will return failure as response.
                When a Virtual Network is anchored at the site, at least one CP and External Border must be present.
            type: str
      anycast_gateways:
        description: A list of anycast gateways in the SDA fabric, each with details about its associated virtual network, IP pool,
            VLAN configuration, and other advanced network settings.
        type: list
        elements: dict
        suboptions:
          vn_name:
            description: Name of the layer 3 virtual network associated with the anycast gateway. the virtual network must have
                already been added to the site before creating an anycast gateway with it.
                And updation of this field is not allowed.
            type: str
            required: True
          fabric_site_locations:
            description: Information about the site location where the anycast gateway is to be assigned to.
                And updation of this field is not allowed.
            type: dict
            required: True
            suboptions:
              site_name:
                description: The hierarchical name of the site where the anycast gateway is deployed.
                type: str
              fabric_type:
                description: Specifies the type of site to be managed within the SDA environment. The acceptable values are 'fabric_site'
                    and 'fabric_zone'. The default value is 'fabric_site', indicating the configuration of a broader network area, whereas
                    'fabric_zone' typically refers to a more specific segment within the site.
                type: str
          ip_pool_name:
            description: Name of the IP pool associated with the anycast gateway. Make sure IP Pool is already exist in the Cisco Catalsyt
                Center and if does not exist then we can create/reserve using the network_settings_workflow_manager module.
                And updation of this field is not allowed.
            type: str
            required: True
          tcp_mss_adjustment:
            description: The value used to adjust the TCP Maximum Segment Size (MSS). The value should be in range (500, 1441).
            type: int
          vlan_name:
            description: Name of the VLAN of the anycast gateway. And it's an optional field if the parameter 'auto_generate_vlan_name'
                is set to True.
                And updation of this field is not allowed.
            type: str
          vlan_id:
            description: ID of the VLAN of the anycast gateway. allowed VLAN range is 2-4093 except for reserved VLANs 1002-1005,
                2046, and 4094. if deploying an anycast gateway on a fabric zone, this vlanId must match the vlanId of the
                corresponding anycast gateway on the fabric site. And it's an optional field if the parameter 'auto_generate_vlan_name'
                is set to True.
                And updation of this field is not allowed.
            type: int
          traffic_type:
            description: The type of traffic handled by the VLAN (e.g., DATA, VOICE). By defaut it is set to "DATA".
                Also unable to update the "traffic_type" in anycast gateway if "is_critical_pool" is set to True.
            type: str
          pool_type:
            description: The pool type of the anycast gateway (required for & applicable only to INFRA_VN). Need to select one
                of either value from (EXTENDED_NODE, FABRIC_AP).
                And updation of this field is not allowed.
          security_group_name:
            description: The name of the security group associated with the anycast gateway. It is not applicable to INFRA_VN.
            type: str
          is_critical_pool:
            description: Specifies whether this pool is marked as critical for the network. if true, 'auto_generate_vlan_name'
                must also be true. By default it is set to False. It is not applicable to INFRA_VN.
                And updation of this field is not allowed.
            type: bool
          layer2_flooding_enabled:
            description: Indicates whether Layer 2 flooding is enabled in the network. By default it is set to False. It is not
                applicable to INFRA_VN.
            type: bool
          fabric_enabled_wireless:
            description: Specifies whether the anycast gateway is enabled for wireless in the fabric.
                 By default it is set to False. It is not applicable to INFRA_VN.
            type: bool
          ip_directed_broadcast:
            description: Indicates whether IP directed broadcasts are allowed. By default it is set to False. It is not
                applicable to INFRA_VN.
            type: bool
          intra_subnet_routing_enabled:
            description: Specifies whether routing is enabled within the subnet. By default it is set to False. It is not
                applicable to INFRA_VN.
                And updation of this field is not allowed.
            type: bool
          multiple_ip_to_mac_addresses:
            description: Indicates whether multiple IPs can be associated with a single MAC address. By default it is set to False.
                It is not applicable to INFRA_VN.
            type: bool
          supplicant_based_extended_node_onboarding:
            description: Specifies whether supplicant-based onboarding for extended nodes is enabled. By default it is set to False.
                It is applicable only to INFRA_VN requests, must not be null when pool_type is EXTENDED_NODE.
            type: bool
          group_policy_enforcement_enabled:
            description: Indicates whether group policy enforcement is enabled in the fabric. By default it is set to False.
            type: bool
          auto_generate_vlan_name:
            description: Specifies whether the VLAN name should be auto-generated. If 'is_critical_pool' is set to True then
                this field must be set to True. And if 'auto_generate_vlan_name' is set to True then vlan_name and vlan_id
                will be autogenerated by Catalyst Center even though if vlan_name or id is provided in the playbook.
            type: bool


requirements:
- dnacentersdk >= 2.9.2
- python >= 3.9

notes:
  - To ensure the module operates correctly for scaled sets, which involve creating/updating/deleting layer2 fabric VLAN and layer3
    virtual network and also for the configuration of anycast gateways, please provide valid input in the playbook. If any failure
    is encountered, the module will halt execution without proceeding to further operations.
  - In order to delete the Fabric Vlan on the fabric site make sure that if there is any fabric zone(s) exist within that site then
    delete the Fabric Vlan from the fabric zone first and once all the Fabric Vlan deleted from fabric zones then only the parent
    fabric site with Vlan is available for the deletion.
  - In order to layer3 Virtual Network make sure that first all the Anycast Gateway(s) having the given virtual network will be
    deleted first then only deletion operation for Virtual Network gets enabled.
  - SDK Method used are
    ccc_virtual_network.sda.get_site
    ccc_virtual_network.sda.get_fabric_sites
    ccc_virtual_network.sda.get_fabric_zones
    ccc_virtual_network.sda.get_layer2_virtual_networks
    ccc_virtual_network.sda.add_layer2_virtual_networks
    ccc_virtual_network.sda.update_layer2_virtual_networks
    ccc_virtual_network.sda.delete_layer2_virtual_network_by_id
    ccc_virtual_network.sda.get_layer3_virtual_networks
    ccc_virtual_network.sda.add_layer3_virtual_networks
    ccc_virtual_network.sda.update_layer3_virtual_networks
    ccc_virtual_network.sda.delete_layer3_virtual_network_by_id
    ccc_virtual_network.sda.get_reserve_ip_subpool
    ccc_virtual_network.sda.get_anycast_gateways
    ccc_virtual_network.sda.add_anycast_gateways
    ccc_virtual_network.sda.update_anycast_gateways
    ccc_virtual_network.sda.delete_anycast_gateway_by_id

"""

EXAMPLES = r"""
- name: Create layer2 fabric Vlan for sda in Cisco Catalyst Center.
  cisco.dnac.fabric_virtual_networks_workflow_manager:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    dnac_log_level: "{{dnac_log_level}}"
    dnac_log: False
    state: merged
    config:
      - fabric_vlan:
        - vlan_name: "vlan_test1"
          fabric_site_locations:
          - site_name_hierarchy: "Global/India"
            fabric_type: "fabric_site"
          - site_name_hierarchy: "Global/India/Chennai"
            fabric_type: "fabric_zone"
          vlan_id: 1333
          traffic_type: "DATA"
          fabric_enabled_wireless: False
        - vlan_name: "vlan_test2"
          fabric_site_locations:
          - site_name_hierarchy: "Global/USA"
            fabric_type: "fabric_site"
          vlan_id: 1334
          traffic_type: "VOICE"
          fabric_enabled_wireless: False

- name: Update layer2 fabric Vlan for sda in Cisco Catalyst Center.
  cisco.dnac.fabric_virtual_networks_workflow_manager:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    dnac_log_level: "{{dnac_log_level}}"
    dnac_log: False
    state: merged
    config:
      - fabric_vlan:
        - vlan_name: "vlan_test1"
          fabric_site_locations:
          - site_name_hierarchy: "Global/India"
            fabric_type: "fabric_site"
          - site_name_hierarchy: "Global/India/Chennai"
            fabric_type: "fabric_zone"
          vlan_id: 1333
          traffic_type: "VOICE"
          fabric_enabled_wireless: True

- name: Deleting layer2 fabric Vlan from the Cisco Catalyst Center.
  cisco.dnac.fabric_virtual_networks_workflow_manager:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    dnac_log_level: "{{dnac_log_level}}"
    dnac_log: False
    state: deleted
    config:
      - fabric_vlan:
        - vlan_name: "vlan_test1"
          fabric_site_locations:
          - site_name_hierarchy: "Global/India/Chennai"
            fabric_type: "fabric_zone"
          vlan_id: 1333

- name: Create layer3 Virtual Network and anchored the site to the VN as well.
  cisco.dnac.fabric_virtual_networks_workflow_manager:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    dnac_log_level: "{{dnac_log_level}}"
    dnac_log: False
    state: merged
    config:
      - virtual_networks:
        - vn_name: "vn_with_anchor"
          fabric_site_locations:
            - site_name_hierarchy: "Global/India"
              fabric_type: "fabric_site"
          anchored_site_name: "Global/India"

- name: Create layer3 Virtual Network and extend it to multiple fabric sites.
  cisco.dnac.fabric_virtual_networks_workflow_manager:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    dnac_log_level: "{{dnac_log_level}}"
    dnac_log: False
    state: merged
    config:
      - virtual_networks:
        - vn_name: "vn_test"
          fabric_site_locations:
            - site_name_hierarchy: "Global/India"
              fabric_type: "fabric_site"
            - site_name_hierarchy: "Global/USA"
              fabric_type: "fabric_site"

- name: Update layer3 Virtual Network in the Cisco Catalyst Center.
  cisco.dnac.fabric_virtual_networks_workflow_manager:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    dnac_log_level: "{{dnac_log_level}}"
    dnac_log: False
    state: merged
    config:
      - virtual_networks:
        - vn_name: "vn_test"
          fabric_site_locations:
            - site_name_hierarchy: "Global/India"
              fabric_type: "fabric_site"
            - site_name_hierarchy: "Global/USA"
              fabric_type: "fabric_site"
            - site_name_hierarchy: "Global/China"
              fabric_type: "fabric_site"

- name: Deleting layer3 Virtual Network from the Cisco Catalyst Center.
  cisco.dnac.fabric_virtual_networks_workflow_manager:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    dnac_log_level: "{{dnac_log_level}}"
    dnac_log: False
    state: deleted
    config:
      - virtual_networks:
          - vn_name: "vlan_test1"

- name: Create the Anycast gateway(s) for SDA in Catalsyt Center.
  cisco.dnac.fabric_virtual_networks_workflow_manager:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    dnac_log_level: "{{dnac_log_level}}"
    dnac_log: False
    state: merged
    config:
      - anycast_gateways:
        - vn_name: "VN_Anycast"
          fabric_site_location:
            site_name_hierarchy: "Global/India"
            fabric_type: "fabric_site"
          ip_pool_name: "IP_Pool_1"
          tcp_mss_adjustment: 580
          traffic_type: "DATA"
          is_critical_pool: False
          auto_generate_vlan_name: True

- name: Update the Anycast gateway(s) for SDA in Catalsyt Center.
  cisco.dnac.fabric_virtual_networks_workflow_manager:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    dnac_log_level: "{{dnac_log_level}}"
    dnac_log: False
    state: merged
    config:
      - anycast_gateways:
        - vn_name: "VN_India"
          fabric_site_location:
            site_name_hierarchy: "Global/India"
            fabric_type: "fabric_site"
          ip_pool_name: "Reserve_Ip_Abhi_pool"
          tcp_mss_adjustment: 590
          traffic_type: "DATA"
          is_critical_pool: False
          layer2_flooding_enabled: False
          multiple_ip_to_mac_addresses: False

- name: Deleting Anycast Gateway from the Cisco Catalyst Center.
  cisco.dnac.fabric_virtual_networks_workflow_manager:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    dnac_log_level: "{{dnac_log_level}}"
    dnac_log: False
    state: deleted
    config:
      - anycast_gateways:
        - vn_name: "vlan_test1"
          fabric_site_location:
            site_name_hierarchy: "Global/India"
            fabric_type: "fabric_site"
          ip_pool_name: "IP_Pool_1"

"""

RETURN = r"""

dnac_response:
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

from ansible.module_utils.basic import AnsibleModule
from ansible_collections.cisco.dnac.plugins.module_utils.dnac import (
    DnacBase,
    validate_list_of_dicts,
)
import copy
import re


class VirtualNetwork(DnacBase):
    """Class containing member attributes for fabric sites and zones workflow manager module"""

    def __init__(self, module):
        super().__init__(module)
        self.supported_states = ["merged", "deleted"]
        self.created_fabric_vlan, self.updated_fabric_vlan, self.no_update_fabric_vlan = [], [], []
        self.created_vn, self.updated_vn, self.no_update_vn = [], [], []
        self.created_anycast, self.updated_anycast, self.no_update_anycast = [], [], []
        self.deleted_fabric_vlan, self.absent_fabric_vlan = [], []
        self.deleted_vn, self.absent_vn = [], []
        self.deleted_anycast, self.absent_anycast = [], []

    def validate_input(self):
        """
        Validate the fields provided in the playbook.
        Checks the configuration provided in the playbook against a predefined specification
        to ensure it adheres to the expected structure and data types.
        Parameters:
            self: The instance of the class containing the 'config' attribute to be validated.
        Returns:
            The method returns an instance of the class with updated attributes:
                - self.msg: A message describing the validation result.
                - self.status: The status of the validation (either 'success' or 'failed').
                - self.validated_config: If successful, a validated version of the 'config' parameter.
        Example:
            To use this method, create an instance of the class and call 'validate_input' on it.
            If the validation succeeds, 'self.status' will be 'success' and 'self.validated_config'
            will contain the validated configuration. If it fails, 'self.status' will be 'failed', and
            'self.msg' will describe the validation issues.
        """

        temp_spec = {
            'fabric_vlan': {
                'type': 'list',
                'elements': 'dict',
                'vlan_name': {'type': 'str'},
                'vlan_id': {'type': 'int'},
                'traffic_type': {'type': 'str'},
                'fabric_enabled_wireless': {'type': 'bool'},
                'associated_layer3_virtual_network': {'type': 'str'},
                'fabric_site_locations': {
                    'type': 'list',
                    'elements': 'dict',
                    'site_name_hierarchy': {'type': 'str'},
                    'fabric_type': {'type': 'str'}
                }
            },
            'virtual_networks': {
                'type': 'list',
                'elements': 'dict',
                'vn_name': {'type': 'str'},
                'anchored_site_name': {'type': 'str'},
                'fabric_site_locations': {
                    'type': 'list',
                    'elements': 'dict',
                    'site_name_hierarchy': {'type': 'str'},
                    'fabric_type': {'type': 'str'}
                }
            },
            'anycast_gateways': {
                'type': 'list',
                'elements': 'dict',
                'vn_name': {'type': 'str'},
                'fabric_site_location': {
                    'site_name_hierarchy': {'type': 'str'},
                    'fabric_type': {'type': 'str'}
                },
                'ip_pool_name': {'type': 'str'},
                'tcp_mss_adjustment': {'type': 'int'},
                'vlan_name': {'type': 'str'},
                'vlan_id': {'type': 'int'},
                'traffic_type': {'type': 'str'},
                'pool_type': {'type': 'str'},
                'security_group_name': {'type': 'str'},
                'is_critical_pool': {'type': 'bool'},
                'layer2_flooding_enabled': {'type': 'bool'},
                'fabric_enabled_wireless': {'type': 'bool'},
                'ip_directed_broadcast': {'type': 'bool'},
                'intra_subnet_routing_enabled': {'type': 'bool'},
                'multiple_ip_to_mac_addresses': {'type': 'bool'},
                'supplicant_based_extended_node_onboarding': {'type': 'bool'},
                'group_policy_enforcement_enabled': {'type': 'bool'},
                'auto_generate_vlan_name': {'type': 'bool'},
            },
        }

        # Validate device params
        valid_temp, invalid_params = validate_list_of_dicts(
            self.config, temp_spec
        )

        if invalid_params:
            self.msg = "The playbook contains invalid parameters: {0}".format(invalid_params)
            self.set_operation_result("failed", False, self.msg, "ERROR").check_return_status()

        self.validated_config = valid_temp
        self.msg = "Successfully validated playbook configuration parameters using 'validate_input': {0}".format(str(valid_temp))
        self.log(self.msg, "INFO")
        self.status = "success"

        return self

    def get_site_id(self, site_name):
        """
        Retrieves the site IDs for a given site name from the Cisco Catalyst Center.
        Args:
            self (object): An instance of a class used for interacting with Cisco Catalyst Center.
            site_name (str): The complete name of site for which the site ID need to be retrieved.
        Returns:
            str: A site ID corresponding to the provided site name.
        Description:
            This function invokes an API to fetch the details of each site from the Cisco Catalyst Center. If the
            site is found, its site ID is extracted and added to the list of site IDs.
            The function logs messages for successful API responses, missing site, and any errors
            encountered during the process. The final site ID is returned.
        """

        try:
            response = self.dnac._exec(
                family="site_design",
                function='get_sites',
                op_modifies=True,
                params={"name_hierarchy": site_name},
            )
            self.log("Received API response from 'get_site': {0}".format(str(response)), "DEBUG")
            response = response.get('response')

            if not response:
                self.msg = "No site with the name '{0}' found in Cisco Catalyst Center.".format(site_name)
                self.set_operation_result("failed", False, self.msg, "ERROR").check_return_status()
            site_id = response[0].get("id")

            if not site_id:
                self.msg = "No site with the name '{0}' found in Cisco Catalyst Center.".format(site_name)
                self.set_operation_result("failed", False, self.msg, "ERROR").check_return_status()

        except Exception as e:
            self.msg = """Error while getting the details of Site with given name '{0}' present in
                    Cisco Catalyst Center: {1}""".format(site_name, str(e))
            self.set_operation_result("failed", False, self.msg, "ERROR").check_return_status()

        return site_id

    def get_fabric_site_id(self, site_name, site_id):
        """
        Retrieves the fabric site ID for a given site in Cisco Catalyst Center.
        Args:
            self (object): An instance of a class used for interacting with Cisco Catalyst Center.
            site_name (str): The name of the site whose fabric ID is being retrieved.
            site_id (str): The unique identifier of the site in Cisco Catalyst Center.
        Returns:
            str or None: The fabric site ID if the site is a fabric site, or `None` if it is not found.
        Description:
            This function interacts with the Cisco Catalyst Center API to check if a site is part of the fabric network.
            It uses the site ID to query the `get_fabric_sites` API, and if the site exists within the fabric, its fabric
            site ID is returned. If the site is not part of the fabric or an error occurs, the function logs an appropriate
            message and returns `None`.
            In case of an exception during the API call, the function logs the error, updates the status to "failed", and
            triggers a check for return status.
        """

        try:
            fabric_site_id = None
            response = self.dnac._exec(
                family="sda",
                function='get_fabric_sites',
                op_modifies=True,
                params={"site_id": site_id},
            )
            response = response.get("response")
            self.log("Received API response from 'get_fabric_sites' for the site '{0}': {1}".format(site_name, str(response)), "DEBUG")

            if not response:
                self.log("Given site '{0}' is not a fabric site in Cisco Catalyst Center.".format(site_name), "INFO")
                return fabric_site_id
            fabric_site_id = response[0].get("id")
        except Exception as e:
            self.msg = """Error while getting the details of Site with given name '{0}' present in
                    Cisco Catalyst Center: {1}""".format(site_name, str(e))
            self.set_operation_result("failed", False, self.msg, "ERROR").check_return_status()

        return fabric_site_id

    def get_fabric_zone_id(self, site_name, site_id):
        """
        Retrieves the fabric zone ID for a given site in Cisco Catalyst Center.
        Args:
            self (object): An instance of a class used for interacting with Cisco Catalyst Center.
            site_name (str): The name of the site whose fabric zone ID is being retrieved.
            site_id (str): The unique identifier of the site in Cisco Catalyst Center.
        Returns:
            str or None: The fabric zone ID if the site is a fabric zone, or `None` if it is not found.
        Description:
            This function queries Cisco Catalyst Center's API to determine whether a site is part of a fabric zone.
            It sends a request to the `get_fabric_zones` API using the provided site ID. If the site is part of a fabric
            zone, the corresponding zone ID is returned. If the site is not a fabric zone or no response is received,
            the function logs an informational message and returns `None`.
            If an error occurs during the API call, the function logs the error, sets the status to "failed", and performs
            error handling through `check_return_status`.
        """

        try:
            fabric_zone_id = None
            response = self.dnac._exec(
                family="sda",
                function='get_fabric_zones',
                op_modifies=True,
                params={"site_id": site_id},
            )
            response = response.get("response")
            self.log("Received API response from 'get_fabric_zones' for the site '{0}': {1}".format(site_name, str(response)), "DEBUG")

            if not response:
                self.log("Given site '{0}' is not a fabric zone in Cisco Catalyst Center.".format(site_name), "INFO")
                return fabric_zone_id

            fabric_zone_id = response[0].get("id")

        except Exception as e:
            self.msg = """Error while getting the details of fabric zone '{0}' present in
                    Cisco Catalyst Center: {1}""".format(site_name, str(e))
            self.set_operation_result("failed", False, self.msg, "ERROR").check_return_status()

        return fabric_zone_id

    def is_valid_vn_name(self, vn_name):
        """
        Validates the format of a layer3 Virtual Network name for SDA (Software-Defined Access) operations.
        Args:
            self (object): An instance of a class used for interacting with Cisco Catalyst Center.
            vn_name (str): The virtual network name to validate.
        Returns:
            self (object): Returns the instance of the class if the VN name is valid. If invalid, updates the instance status
            to "failed", logs a warning message, and adds a failure response to the result dictionary.
        Description:
            This function checks whether the provided virtual network name follows a specific pattern using a regular
            expression. The VN name must consist of only letters, numbers, and underscores, and must be between 1-16
            characters in length. If the VN name is valid, it logs an informational message and returns the instance.
            If invalid, the function sets the status to "failed", logs a warning, and stores the error message in the
            result dictionary.
        """

        # Regex pattern for virtual network name having only letters numbers and underscores with 1-16 character long.
        pattern = r'^[a-zA-Z0-9_]{1,16}$'
        if re.match(pattern, vn_name):
            self.log("Given virtual network name '{0}' is valid for the sda operation.".format(vn_name), "INFO")
            return self

        self.msg = (
            "Given Virtual Network name '{0}' in the input playbook is not valid. VirtualNetworkContext "
            "name should be 1-16 characters long and contains only letters numbers and underscores."
        ).format(vn_name)
        self.set_operation_result("failed", False, self.msg, "WARNING")

        return self

    def is_valid_fabric_vlan_name(self, vlan_name):
        """
        Validates the format of a fabric VLAN name for SDA (Software-Defined Access) operations.
        Args:
            self (object): An instance of a class used for interacting with Cisco Catalyst Center.
            vlan_name (str): The fabric VLAN name to validate.
        Returns:
            self (object): Returns the instance of the class if the VLAN name is valid. If invalid, updates the instance's
            status to "failed", logs a warning message, and adds a failure response to the result dictionary.
        Description:
            This function checks whether the provided fabric VLAN name follows a specific pattern using a regular
            expression. The VLAN name must consist of alphanumeric characters, underscores, and hyphens, and be
            between 1-32 characters in length. If the VLAN name is valid, it logs an informational message and
            returns the instance. If the VLAN name is invalid, the function sets the status to "failed", logs a
            warning, and stores the error message in the result dictionary.
        """

        # Regex pattern for fabric vlan name having alphanumeric characters, underscores and hyphens with 1-32 character long.
        vlan_name_pattern = r'^[a-zA-Z0-9_-]{1,32}$'
        if re.match(vlan_name_pattern, vlan_name):
            self.log("Given fabric vlan name '{0}' is valid for the sda operation.".format(vlan_name), "INFO")
            return self

        self.msg = (
            "Given Fabric Vlan name '{0}' in the input playbook is not valid. FabricVlanNameContext "
            "name should be 1-32 characters long and contains only alphanumeric characters, underscores and hyphens."
        ).format(vlan_name)
        self.set_operation_result("failed", False, self.msg, "WARNING")

        return self

    def validate_fabric_type(self, fabric_type):
        """
        Validates the fabric type provided for SDA (Software-Defined Access) operations.
        Args:
            self (object): An instance of a class used for interacting with Cisco Catalyst Center.
            fabric_type (str): The fabric type to validate. It must be either "fabric_site" or "fabric_zone".
        Returns:
            self (object): Returns the instance of the class. If an invalid fabric type is provided, it updates the status to
            "failed", logs an error message, and adds the failure response to the result dictionary.
        Description:
            This function checks if the given `fabric_type` is one of the allowed values: "fabric_site" or "fabric_zone".
            If the `fabric_type` is valid, the function does nothing and simply returns the class instance. If the
            `fabric_type` is invalid, it sets the status to "failed", logs an error, and updates the result dictionary
            with an appropriate error message.
        """

        if fabric_type not in ["fabric_site", "fabric_zone"]:
            self.msg = (
                "Invalid fabric_type '{0}' parameter given in the playbook. Please provide one of the following "
                "fabric_type ['fabric_site', 'fabric_zone']."
            ).format(fabric_type)
            self.set_operation_result("failed", False, self.msg, "ERROR")

        return self

    def collect_fabric_vlan_ids(self, vlan_name, vlan_id):
        """
        Collects fabric VLAN IDs for a given VLAN in Cisco Catalyst Center.
        Args:
            self (object): An instance of a class used for interacting with Cisco Catalyst Center.
            vlan_name (str): The name of the VLAN whose fabric VLAN IDs are to be collected.
            vlan_id (str): The unique identifier of the VLAN in Cisco Catalyst Center.
        Returns:
            list: A list of VLAN IDs associated with the given VLAN. Returns an empty list if no VLANs are found or if
            an error occurs.
        Description:
            This function interacts with the Cisco Catalyst Center API to retrieve fabric VLAN IDs for a specified VLAN.
            It queries the `get_layer2_virtual_networks` API using the provided VLAN ID. If VLAN data is found, it collects
            the corresponding VLAN IDs into a list and returns them. If the VLAN is not present or an error occurs during
            the API call, the function logs an appropriate message, updates the status to "failed" if necessary, and returns
            an empty list.
        """

        try:
            vlan_ids = []
            response = self.dnac._exec(
                family="sda",
                function='get_layer2_virtual_networks',
                op_modifies=True,
                params={"vlan_id": vlan_id},
            )
            response = response.get("response")
            self.log("Received API response from 'get_layer2_virtual_networks' for the Vlan '{0}': {1}".format(vlan_name, str(response)), "DEBUG")

            if not response:
                self.log("Given layer2 fabric Vlan '{0}' is not present in Cisco Catalyst Center.".format(vlan_name), "INFO")
                return vlan_ids

            for vlan_vn in response:
                vlan_ids.append(vlan_vn.get("id"))

        except Exception as e:
            self.msg = (
                "Error while getting the details for layer2 fabric Vlan '{0}' present in "
                "Cisco Catalyst Center: {1}"
            ).format(vlan_name, str(e))
            self.set_operation_result("failed", False, self.msg, "ERROR").check_return_status()

        return vlan_ids

    def get_fabric_vlan_details(self, vlan_name, vlan_id, fabric_id):
        """
        Retrieves the details of a fabric VLAN from the Cisco Catalyst Center.
        Args:
            self (object): An instance of a class used for interacting with Cisco Catalyst Center.
            vlan_name (str): The name of the VLAN whose details are to be retrieved.
            vlan_id (str): The unique identifier of the VLAN in Cisco Catalyst Center.
            fabric_id (str): The unique identifier of the fabric in which the VLAN resides.
        Returns:
            dict or None: A dictionary containing the details of the VLAN if found. Returns `None` if the VLAN does not
            exist or an error occurs during the API call.
        Description:
            This function queries Cisco Catalyst Center's API to fetch details about a specified fabric VLAN using the
            provided `vlan_id` and `fabric_id`. If the VLAN is not found or an exception occurs, the function logs an
            appropriate message, sets the status to "failed" if needed, and returns `None`.
        """

        try:
            response = self.dnac._exec(
                family="sda",
                function='get_layer2_virtual_networks',
                op_modifies=True,
                params={
                    "vlan_id": vlan_id,
                    "fabric_id": fabric_id
                },
            )
            response = response.get("response")
            self.log("Received API response from 'get_layer2_virtual_networks' for the vlan '{0}': {1}".format(vlan_name, str(response)), "DEBUG")

            if not response:
                self.log("Given layer2 vlan '{0}' is not present in Cisco Catalyst Center.".format(vlan_name), "INFO")
                return None

        except Exception as e:
            self.msg = (
                "Error while getting the details for layer2 vlan '{0}' present in "
                "Cisco Catalyst Center: {1}"
            ).format(vlan_name, str(e))
            self.set_operation_result("failed", False, self.msg, "ERROR").check_return_status()

        return response[0]

    def validate_traffic_type(self, traffic_type):
        """
        Validates the traffic type provided for SDA (Software-Defined Access) operations.
        Args:
            self (object): An instance of a class used for interacting with Cisco Catalyst Center.
            traffic_type (str): The traffic type to validate. Allowed values are "DATA" or "VOICE".
        Returns:
            self (object): Returns the instance of class. If invalid traffic type is provided, function sets the
            status to "failed", logs an error message, and adds the failure response to the result dictionary.
        Description:
            This function checks if the provided `traffic_type` is one of the allowed values: "DATA" or "VOICE".
            If valid, it logs a success message and returns the class instance. If the `traffic_type` is invalid,
            the function sets the status to "failed", logs an error message, and updates the result dictionary
            with the error information.
        """

        if traffic_type not in ["DATA", "VOICE"]:
            self.msg = (
                "Invalid traffic_type '{0}' given in the playbook. Allowed values are (DATA, VOICE)."
            ).format(traffic_type)
            self.set_operation_result("failed", False, self.msg, "ERROR").check_return_status()

        self.log("Parameter traffic_type '{0}' given in the playbook validated successfully.".format(traffic_type), "INFO")

        return self

    def create_payload_for_fabric_vlan(self, vlan, fabric_id_list):
        """
        Creates a list of payloads for configuring fabric VLANs in Cisco Catalyst Center.
        Args:
            self (object): An instance of a class used for interacting with Cisco Catalyst Center.
            vlan (dict): A dictionary containing VLAN details, including:
                - vlan_name (str): The name of the VLAN.
                - vlan_id (int): The identifier of the VLAN.
                - traffic_type (str): The type of traffic, either "DATA" or "VOICE". Defaults to "DATA".
                - fabric_enabled_wireless (bool): Whether fabric-enabled wireless is enabled for the VLAN.
                - associated_layer3_virtual_network (str): The associated Layer 3 virtual network name.
            fabric_id_list (list): A list of fabric IDs where the VLAN configuration will be applied.
        Returns:
            list: A list of dictionaries, each containing the payload required to create or configure the VLAN
            on each fabric in the `fabric_id_list`.
        Description:
            This function generates a payload for configuring a fabric VLAN in Cisco Catalyst Center.
            For each fabric ID in the `fabric_id_list`, it creates a deep copy of the base payload, adds the fabric ID,
            and appends the result to the payload list. The function returns the list of payloads, one for each fabric ID.
        """

        create_vlan_payload_list = []
        traffic_type = vlan.get("traffic_type", "DATA").upper()
        # Validate the given traffic type for Vlan/VN/Anycast configuration.
        self.validate_traffic_type(traffic_type)

        vlan_payload = {
            "vlanName": vlan.get("vlan_name"),
            "vlanId": vlan.get("vlan_id"),
            "trafficType": traffic_type,
            "isFabricEnabledWireless": vlan.get("fabric_enabled_wireless", False),
            "associatedLayer3VirtualNetworkName": vlan.get("associated_layer3_virtual_network")
        }

        for fabric_id in fabric_id_list:
            deep_payload_dict = copy.deepcopy(vlan_payload)
            deep_payload_dict["fabricId"] = fabric_id
            create_vlan_payload_list.append(deep_payload_dict)
            del deep_payload_dict

        return create_vlan_payload_list

    def create_fabric_vlan(self, collect_add_vlan_payload):
        """
        Creates fabric VLAN(s) in Cisco Catalyst Center using the provided payload.
        Args:
            self (object): An instance of a class used for interacting with Cisco Catalyst Center.
            collect_add_vlan_payload (dict): The payload containing the details for the VLAN(s) to be created.
        Returns:
            self (object): Returns the instance of the class. If the creation process fails at any point, the instance's
                status is set to "failed" and the failure response is added to the result dictionary.
        Description:
            This function interacts with the Cisco Catalyst Center API to create one or more fabric VLANs. It sends a
            request to the `add_layer2_virtual_networks` API with the provided payload. If the task completes successfully,
            an message is logged. If the task fails, the function logs the reason for failure, updating the
            class status accordingly.
        """

        try:
            payload = {"payload": collect_add_vlan_payload}
            task_name = "add_layer2_virtual_networks"
            task_id = self.get_taskid_post_api_call("sda", task_name, payload)

            if not task_id:
                self.msg = "Unable to retrive the task_id for the task '{0}'.".format(task_name)
                self.set_operation_result("failed", False, self.msg, "ERROR")
                return self

            success_msg = "Layer2 Fabric VLAN(s) '{0}' created successfully in the Cisco Catalyst Center.".format(self.created_fabric_vlan)
            self.get_task_status_from_tasks_by_id(task_id, task_name, success_msg)

        except Exception as e:
            self.msg = (
                "An exception occured while creating the layer2 VLAN(s) '{0}' in the Cisco Catalyst "
                "Center: {1}"
            ).format(self.created_fabric_vlan, str(e))
            self.set_operation_result("failed", False, self.msg, "ERROR")

        return self

    def fabric_vlan_needs_update(self, vlan, fabric_vlan_in_ccc):
        """
        Determines if a fabric VLAN needs to be updated based on the provided configuration.
        Args:
            self (object): An instance of a class used for interacting with Cisco Catalyst Center.
            vlan (dict): A dictionary containing the desired VLAN configuration, which may include:
                - traffic_type (str): The type of traffic for the VLAN (e.g., "DATA", "VOICE").
                - fabric_enabled_wireless (bool): Indicates whether fabric-enabled wireless is enabled for the VLAN.
            fabric_vlan_in_ccc (dict): A dictionary representing the current VLAN configuration, which includes:
                - trafficType (str): The current type of traffic for the VLAN.
                - isFabricEnabledWireless (bool): The current status of fabric-enabled wireless for the VLAN.
        Returns:
            bool: Returns `True` if the VLAN needs to be updated and `False` otherwise.
        Description:
            This function compares the desired VLAN configuration provided in the `vlan` dictionary with the current
            configuration stored in `fabric_vlan_in_ccc`. If either parameter requires an update, function returns
            `True`. If both parameters match the current configuration, it returns `False`.
        """

        traffic_type = vlan.get("traffic_type")
        enabled_wireless = vlan.get("fabric_enabled_wireless")

        if traffic_type and traffic_type != fabric_vlan_in_ccc.get("trafficType"):
            return True

        if enabled_wireless is not None and enabled_wireless != fabric_vlan_in_ccc.get("isFabricEnabledWireless"):
            return True

        return False

    def update_payload_fabric_vlan(self, vlan, fabric_vlan_in_ccc, fabric_id):
        """
        Constructs an update payload for a fabric VLAN based on the provided configuration.
        Args:
            self (object): An instance of a class used for interacting with Cisco Catalyst Center.
            vlan (dict): A dictionary containing the new VLAN configuration.
            fabric_vlan_in_ccc (dict): A dictionary representing the current VLAN configuration in Cisco Catalyst Center.
            fabric_id (str): The unique identifier of the fabric to which the VLAN belongs.
        Returns:
            dict: A dictionary containing the payload needed to update the fabric VLAN configuration, including the
                relevant identifiers and configuration details.
        Description:
            This function constructs a payload for updating a fabric VLAN in Cisco Catalyst Center. The resulting payload
            is structured to include the VLAN ID, fabric ID, traffic type, wireless enablement status, and associated
            Layer3 virtual network name and used to submit an update request to the Cisco Catalyst Center API.
        """

        traffic_type = vlan.get("traffic_type").upper()
        # Validate the given traffic type for Vlan/VN/Anycast configuration.
        self.validate_traffic_type(traffic_type)

        wireless_enable = vlan.get("fabric_enabled_wireless")
        if wireless_enable is None:
            wireless_enable = fabric_vlan_in_ccc.get("isFabricEnabledWireless")

        vlan_update_payload = {
            "id": fabric_vlan_in_ccc.get("id"),
            "fabricId": fabric_id,
            "vlanName": vlan.get("vlan_name"),
            "vlanId": vlan.get("vlan_id"),
            "trafficType": traffic_type or fabric_vlan_in_ccc.get("trafficType"),
            "isFabricEnabledWireless": wireless_enable,
            "associatedLayer3VirtualNetworkName": fabric_vlan_in_ccc.get("associatedLayer3VirtualNetworkName")
        }

        return vlan_update_payload

    def update_fabric_vlan(self, update_vlan_payload):
        """
        Updates the fabric VLAN(s) in Cisco Catalyst Center using the provided payload.
        Args:
            self (object): An instance of a class used for interacting with Cisco Catalyst Center.
            update_vlan_payload (dict): A dictionary containing the details required to update the fabric VLAN(s).
        Returns:
            self (object): Returns the instance of the class. If the update process fails at any point, the instance's
                status is set to "failed" and the failure response is added to the result dictionary.
        Description:
            This function interacts with the Cisco Catalyst Center API to update one or more fabric VLANs. It sends
            request to the `update_layer2_virtual_networks` API with the provided payload. If the task completes
            successfully, an informational message is logged. If the task fails, the function logs the reason for
            failure, updating the class status accordingly.
            In case of exceptions during the process, the function captures the error, logs an appropriate message,
            and sets the status to "failed".
        """

        try:
            payload = {"payload": update_vlan_payload}
            task_name = "update_layer2_virtual_networks"
            task_id = self.get_taskid_post_api_call("sda", task_name, payload)

            if not task_id:
                self.msg = "Unable to retrive the task_id for the task '{0}'.".format(task_name)
                self.set_operation_result("failed", False, self.msg, "ERROR")
                return self

            success_msg = "Layer2 Fabric VLAN(s) '{0}' updated successfully in the Cisco Catalyst Center.".format(self.updated_fabric_vlan)
            self.get_task_status_from_tasks_by_id(task_id, task_name, success_msg)

        except Exception as e:
            self.msg = (
                "An exception occured while updating the layer2 fabric VLAN(s) '{0}' in the Cisco Catalyst "
                "Center: {1}"
            ).format(self.updated_fabric_vlan, str(e))
            self.set_operation_result("failed", False, self.msg, "ERROR")

        return self

    def delete_layer2_fabric_vlan(self, vlan_name, vlan_vn_id):
        """
        Deletes a Layer2 fabric VLAN in Cisco Catalyst Center based on the provided VLAN ID.
        Args:
            self (object): An instance of a class used for interacting with Cisco Catalyst Center.
            vlan_name (str): The name of the Fabric VLAN to be deleted.
            vlan_vn_id (str): The unique identifier of the Fabric VLAN to be deleted.
        Returns:
            self (object): Returns the instance of the class. If the deletion process fails at any point, the
                instance's status is set to "failed" and the failure response is added to result dictionary.
        Description:
            This function interacts with the Cisco Catalyst Center API to delete a specified Layer 2 fabric VLAN.
            If the task completes successfully, an informational message is logged and VLAN name is appended to
            the list of deleted VLANs. If the task fails, the function logs the reason for failure, updating the
            class status accordingly.
            In case of exceptions during the process, the function captures the error, logs an appropriate message,
            and sets the status to "failed".
        """

        try:
            payload = {"id": vlan_vn_id}
            task_name = "delete_layer2_virtual_network_by_id"
            task_id = self.get_taskid_post_api_call("sda", task_name, payload)

            if not task_id:
                self.msg = "Unable to retrive the task_id for the task '{0}'.".format(task_name)
                self.set_operation_result("failed", False, self.msg, "ERROR")
                return self

            success_msg = "Fabric VLAN '{0}' deleted successfully from the Cisco Catalyst Center.".format(vlan_name)
            self.get_task_status_from_tasks_by_id(task_id, task_name, success_msg)
            self.deleted_fabric_vlan.append(vlan_name)

        except Exception as e:
            self.msg = "Exception occurred while deleting the fabric Vlan '{0}' due to: {1}".format(vlan_name, str(e))
            self.set_operation_result("failed", False, self.msg, "ERROR").check_return_status()

        return self

    def is_virtual_network_exist(self, vn_name):
        """
        Checks if a specified Layer3 Virtual Network exists in the Cisco Catalyst Center.
        Args:
            self (object): An instance of a class used for interacting with Cisco Catalyst Center.
            vn_name (str): The name of the Virtual Network to check for existence.
        Returns:
            bool: Returns True if the virtual network exists, False if it does not.
        Description:
            This function interacts with the Cisco Catalyst Center API to determine the existence of a
            specified Layer3 Virtual Network by querying the `get_layer3_virtual_networks` endpoint.
            If the function successfully retrieves a response, it will return True, indicating the
            virtual network exists.
        """

        try:
            response = self.dnac._exec(
                family="sda",
                function='get_layer3_virtual_networks',
                op_modifies=True,
                params={
                    "virtual_network_name": vn_name,
                },
            )
            response = response.get("response")
            self.log("Received API response from 'get_layer3_virtual_networks' for vn '{0}': {1}".format(vn_name, str(response)), "DEBUG")

            if not response:
                self.log("Given layer3 Virtual Network '{0}' is not present in Cisco Catalyst Center.".format(vn_name), "INFO")
                return False

        except Exception as e:
            self.msg = (
                "Error while getting the details for layer3 virtual network '{0}' present in "
                "Cisco Catalyst Center: {1}"
            ).format(vn_name, str(e))
            self.set_operation_result("failed", False, self.msg, "ERROR").check_return_status()

        return True

    def get_fabric_ids(self, fabric_locations):
        """
        Retrieves a list of fabric IDs based on the specified fabric locations.
        Args:
            self (object): An instance of a class used for interacting with Cisco Catalyst Center.
            fabric_locations (list): A list of dictionaries, each containing information about fabric locations.
                including "site_name_hierarchy" and "fabric_type". The "fabric_type" can either be "fabric_site" or
                "fabric_zone".
        Returns:
            list: A list of fabric IDs corresponding to the specified fabric locations. If a fabric ID cannot
                be retrieved for a location, a warning is logged, and the function continues to the next location.
        Description:
            This function processes a list of fabric locations to extract fabric IDs. For each location, it
            validates the fabric type and retrieves the corresponding site ID. Depending on the fabric type, it
            calls either `get_fabric_site_id` or `get_fabric_zone_id` to obtain the fabric ID.
            If the site is not recognized as a fabric site or zone, a warning message is logged, and that
            location is skipped. The resulting list of fabric IDs is returned.
        """

        fabric_id_list = []

        for fabric in fabric_locations:
            site_name = fabric.get("site_name_hierarchy")
            fabric_type = fabric.get("fabric_type", "fabric_site")
            # Validate the correct fabric_type given in the playbook
            self.validate_fabric_type(fabric_type).check_return_status()
            site_id = self.get_site_id(site_name)

            if fabric_type == "fabric_site":
                fabric_id = self.get_fabric_site_id(site_name, site_id)
            else:
                fabric_id = self.get_fabric_zone_id(site_name, site_id)

            if not fabric_id:
                self.log("Unable to get the Fabric Id as the give site '{0}' is not fabric site/zone".format(site_name), "WARNING")
                continue

            fabric_id_list.append(fabric_id)

        return fabric_id_list

    def create_vn_payload(self, vn_detail):
        """
        Constructs a payload for a Virtual Network based on the provided details.
        Args:
            self (object): An instance of a class used for interacting with Cisco Catalyst Center.
            vn_detail (dict): A dictionary containing the details required to create the virtual network.
        Returns:
            dict: A dictionary representing the virtual network payload. This includes -
                - "virtualNetworkName": The name of the virtual network.
                - "fabricIds" (optional): A list of fabric IDs associated with the fabric locations, if applicable.
                - "anchoredSiteId" (optional): The ID of the anchored site, if it exists.
        Description:
            This function generates a payload necessary for creating a virtual network in the Cisco Catalyst Center.
            Additionally, if an anchored site name is provided, the function attempts to retrieve the associated
            site ID. If the site ID is found, it fetches the corresponding fabric ID for the anchored site.
            The constructed payload, containing the virtual network name and optionally the fabric IDs and anchored
            site ID, is then returned for further use.
        """

        fabric_locations = vn_detail.get("fabric_site_locations")
        vn_name = vn_detail.get("vn_name")
        vn_payload = {
            "virtualNetworkName": vn_name,
        }

        if fabric_locations:
            fabric_ids = self.get_fabric_ids(fabric_locations)

            if fabric_ids:
                vn_payload["fabricIds"] = fabric_ids

        site_name = vn_detail.get("anchored_site_name")
        if site_name:
            site_id = self.get_site_id(site_name)
            if not site_id:
                msg = "Given Anchor site '{0}' not  present in Cisco Catalyst Center.".format(site_name)
                self.log(msg, "ERROR")
                return vn_payload
            try:
                anchor_fabric_id = self.get_fabric_site_id(site_name, site_id)
            except Exception as e:
                anchor_fabric_id = self.get_fabric_zone_id(site_name, site_id)

            if anchor_fabric_id:
                vn_payload["anchoredSiteId"] = anchor_fabric_id

        return vn_payload

    def get_vn_details_from_ccc(self, vn_name):
        """
        Retrieves details of a specified Layer3 Virtual Network from the Cisco Catalyst Center.
        Args:
            self (object): An instance of a class used for interacting with Cisco Catalyst Center.
            vn_name (str): The name of the Layer3 Virtual Network whose details are to be fetched.
        Returns:
            dict or None: A dictionary containing the details of the specified virtual network if found;
                        otherwise, returns None.
        Description:
            This function queries the Cisco Catalyst Center API to obtain information about a Layer3
            Virtual Network identified by the provided name.
            If the response does not contain any data, it logs an informational message indicating that the
            specified virtual network is not present.
            The function returns the details of the virtual network as a dictionary, or None if the network
            does not exist or if an error occurs during the retrieval process.
        """

        try:
            response = self.dnac._exec(
                family="sda",
                function='get_layer3_virtual_networks',
                op_modifies=True,
                params={
                    "virtual_network_name": vn_name,
                },
            )
            response = response.get("response")
            self.log("Received API response from 'get_layer3_virtual_networks' for the vn '{0}': {1}".format(vn_name, str(response)), "DEBUG")

            if not response:
                self.log("Given layer3 virtual network '{0}' is not present in Cisco Catalyst Center.".format(vn_name), "INFO")
                return None

        except Exception as e:
            self.msg = (
                "Error while getting the details for layer3 virtual network '{0}' present in "
                "Cisco Catalyst Center: {1}"
            ).format(vn_name, str(e))
            self.set_operation_result("failed", False, self.msg, "ERROR").check_return_status()

        return response[0]

    def create_virtual_networks(self, collected_add_vn_payload):
        """
        Creates Layer3 Virtual Networks in the Cisco Catalyst Center using the provided payload.
        Args:
            self (object): An instance of a class used for interacting with Cisco Catalyst Center.
            collected_add_vn_payload (dict): A dictionary containing the details required to create
                                            the Layer3 Virtual Networks.
        Returns:
            self (object): The instance of the class with updated status and result attributes reflecting
                        the outcome of the virtual network creation operation.
        Description:
            This function sends a request to the Cisco Catalyst Center API to create Layer3 virtual
            networks based on the information provided in the `collected_add_vn_payload`.
            If successful, it logs an informational message indicating the creation of the virtual networks.
            If the creation fails, it logs the failure reason if available; otherwise it logs generic failure message.
            In the case of any exceptions during the process, it logs the error and updates the status to "failed."
        """

        try:
            payload = {"payload": collected_add_vn_payload}
            task_name = "add_layer3_virtual_networks"
            task_id = self.get_taskid_post_api_call("sda", task_name, payload)

            if not task_id:
                self.msg = "Unable to retrive the task_id for the task '{0}'.".format(task_name)
                self.set_operation_result("failed", False, self.msg, "ERROR")
                return self

            success_msg = "Layer3 Virtual Network(s) '{0}' created successfully in the Cisco Catalyst Center.".format(self.created_vn)
            self.get_task_status_from_tasks_by_id(task_id, task_name, success_msg)

        except Exception as e:
            self.msg = (
                "An exception occured while creating the layer3 Virtual Network(s) '{0}' in the Cisco Catalyst "
                "Center: {1}"
            ).format(self.created_vn, str(e))
            self.set_operation_result("failed", False, self.msg, "ERROR")

        return self

    def is_vn_needs_update(self, vn_details, vn_in_ccc):
        """
        Determines if a Virtual Network requires an update based on its details and current state in
        the Cisco Catalyst Center.
        Args:
            self (object): An instance of a class used for interacting with Cisco Catalyst Center.
            vn_details (dict): A dictionary containing details about the virtual network, including:
                - vn_name (str): The name of the virtual network.
                - fabric_site_locations (list): A list of fabric site locations associated with the virtual network.
                - anchored_site_name (str): The name of the anchored site.
            vn_in_ccc (dict): A dictionary representing the current state of the virtual network in the Cisco
                            Catalyst Center, which includes:
                - fabricIds (list): A list of fabric IDs currently associated with the virtual network.
                - anchoredSiteId (str): The ID of the anchored site currently associated with the virtual network.
        Returns:
            bool: Returns `True` if the virtual network needs an update; otherwise, returns `False`.
        Description:
            This function checks if a virtual network needs to be updated by comparing its provided details
            with the existing configuration in the Cisco Catalyst Center.
            If all checks are passed without indicating an update, the function returns `False`.
        """

        vn_name = vn_details.get("vn_name")
        fabric_ids_in_ccc = vn_in_ccc.get("fabricIds")
        fabric_locations = vn_details.get("fabric_site_locations")

        if fabric_locations is None:
            self.log("There is no fabric site details given in the playbook for the vn '{0}'.".format(vn_name), "INFO")
            return False

        if not fabric_locations and fabric_ids_in_ccc:
            return True

        fabric_site_ids = self.get_fabric_ids(fabric_locations)
        if not fabric_site_ids:
            self.log("Unable to get fabric site ids for the vn '{0}'.".format(vn_name), "INFO")
            return False

        if not fabric_ids_in_ccc:
            self.log("There is no fabric site available in Cisco Catalyst Center for the vn '{0}'.".format(vn_name), "INFO")
            return True

        if len(fabric_site_ids) != len(fabric_ids_in_ccc):
            return True

        for fabric_id in fabric_site_ids:
            if fabric_id not in fabric_ids_in_ccc:
                return True

        anchor_site = vn_details.get("anchored_site_name")
        if anchor_site:
            site_id = self.get_site_id(anchor_site)

            if not site_id:
                msg = "Given Anchor site '{0}' not  present in Cisco Catalyst Center.".format(anchor_site)
                self.log(msg, "ERROR")
                return False
            try:
                anchor_fabric_id = self.get_fabric_site_id(anchor_site, site_id)
            except Exception as e:
                anchor_fabric_id = self.get_fabric_zone_id(anchor_site, site_id)

            if anchor_fabric_id and anchor_fabric_id != vn_in_ccc.get("anchoredSiteId"):
                return True

        return False

    def update_payload_vn(self, vn_details, vn_in_ccc):
        """
        Constructs an update payload for a virtual network based on the provided details and its current
        configuration in the Cisco Catalyst Center.
        Args:
            self (object): An instance of a class used for interacting with Cisco Catalyst Center.
            vn_details (dict): A dictionary containing details about VN to be updated, including:
                - vn_name (str): The name of the virtual network.
                - fabric_site_locations (list): A list of fabric site locations associated with virtual network.
                - anchored_site_name (str): The name of the anchored site.
            vn_in_ccc (dict): A dictionary representing the current state of the virtual network in the
                            Cisco Catalyst Center, which includes:
                - id (str): The identifier of the existing virtual network.
                - anchoredSiteId (str): The ID of anchored site currently associated with the virtual network.
        Returns:
            dict: A dictionary representing the payload for updating the virtual network.
        Description:
            This function constructs a payload for updating a virtual network by gathering relevant details
            from the provided `vn_details` and the current configuration in `vn_in_ccc`.
            The function returns the constructed update payload for the virtual network, which includes all
            necessary identifiers and configurations needed for the update operation.
        """

        vn_name = vn_details.get("vn_name")
        update_vn_payload = {
            "id": vn_in_ccc.get("id"),
            "virtualNetworkName": vn_name
        }
        fabric_locations = vn_details.get("fabric_site_locations")
        fabric_site_ids = []

        if isinstance(fabric_locations, list) and not fabric_locations:
            update_vn_payload["fabricIds"] = []

        if fabric_locations:
            fabric_site_ids = self.get_fabric_ids(fabric_locations)
            update_vn_payload["fabricIds"] = fabric_site_ids

        anchor_site = vn_details.get("anchored_site_name")
        if not anchor_site and vn_in_ccc.get("anchoredSiteId"):
            update_vn_payload["anchoredSiteId"] = vn_in_ccc.get("anchoredSiteId")
            return update_vn_payload

        if not anchor_site:
            self.log("Anchored site is not provided to get associated with the virtual network '{0}'.".format(vn_name), "INFO")
            return update_vn_payload

        site_id = self.get_site_id(anchor_site)
        try:
            anchor_fabric_id = self.get_fabric_site_id(anchor_site, site_id)
        except Exception as e:
            anchor_fabric_id = self.get_fabric_zone_id(anchor_site, site_id)
        update_vn_payload["anchoredSiteId"] = anchor_fabric_id

        return update_vn_payload

    def update_virtual_networks(self, collected_update_vn_payload):
        """
        Updates Layer3 Virtual Networks in the Cisco Catalyst Center using the provided payload.
        Args:
            self (object): An instance of a class used for interacting with Cisco Catalyst Center.
            collected_update_vn_payload (dict): A dictionary containing the payload for updating
                                                Layer3 Virtual Networks.
        Returns:
            self (object): The instance of the class, allowing for method chaining.
        Description:
            This function sends a request to the Cisco Catalyst Center to update Layer3 Virtual
            Networks using the provided payload.
            The function returns the instance of the class, allowing for further method calls on the
            same instance.
        """

        try:
            payload = {"payload": collected_update_vn_payload}
            task_name = "update_layer3_virtual_networks"
            task_id = self.get_taskid_post_api_call("sda", task_name, payload)

            if not task_id:
                self.msg = "Unable to retrive the task_id for the task '{0}'.".format(task_name)
                self.set_operation_result("failed", False, self.msg, "ERROR")
                return self

            success_msg = "Layer3 Virtual Network(s) '{0}' updated successfully in the Cisco Catalyst Center.".format(self.updated_vn)
            self.get_task_status_from_tasks_by_id(task_id, task_name, success_msg)

        except Exception as e:
            self.msg = (
                "An exception occured while updating the layer3 Virtual Network(s) '{0}' in "
                "the Cisco Catalyst Center: {1}"
            ).format(self.updated_vn, str(e))
            self.set_operation_result("failed", False, self.msg, "ERROR")

        return self

    def delete_layer3_virtual_network(self, vn_name, vn_id):
        """
        Deletes a Layer3 Virtual Network from the Cisco Catalyst Center.
        Args:
            self (object): An instance of a class used for interacting with Cisco Catalyst Center.
            vn_name (str): The name of the virtual network to be deleted.
            vn_id (str): The identifier of the virtual network to be deleted.
        Returns:
            self (object): The instance of the class, allowing for method chaining.
        Description:
            This function sends a request to delete a Layer3 Virtual Network specified by the
            given virtual network ID. It executes the API call to the Cisco Catalyst Center
            and logs the response received.
            The function returns the instance of the class, enabling further method calls on the
            same instance.
        """

        try:
            payload = {"id": vn_id}
            task_name = "delete_layer3_virtual_network_by_id"
            task_id = self.get_taskid_post_api_call("sda", task_name, payload)

            if not task_id:
                self.msg = "Unable to retrive the task_id for the task '{0}'.".format(task_name)
                self.set_operation_result("failed", False, self.msg, "ERROR")
                return self

            success_msg = "Layer3 Virtual Network '{0}' deleted successfully from the Cisco Catalyst Center.".format(vn_name)
            self.get_task_status_from_tasks_by_id(task_id, task_name, success_msg)
            self.deleted_vn.append(vn_name)

        except Exception as e:
            self.msg = "Exception occurred while deleting the layer3 Virtual Network '{0}' due to: {1}".format(vn_name, str(e))
            self.set_operation_result("failed", False, self.msg, "ERROR").check_return_status()

        return self

    def is_ip_pool_exist(self, ip_pool_name, site_id):
        """
        Checks if a specified IP pool exists in the Cisco Catalyst Center.
        Args:
            self (object): An instance of a class used for interacting with Cisco Catalyst Center.
            ip_pool_name (str): The name of the IP pool to check for existence.
            site_id (str): The identifier of the site where the IP pool is located.
        Returns:
            bool: True if the IP pool exists, False otherwise.
        Description:
            This function sends a request to the Cisco Catalyst Center to retrieve information
            about a specific reserved IP subpool based on the provided IP pool name and site ID.
            The primary purpose of this function is to facilitate validation of IP pool existence
            for network configurations or management tasks.
        """

        try:
            response = self.dnac._exec(
                family="network_settings",
                function="get_reserve_ip_subpool",
                op_modifies=True,
                params={
                    "site_id": site_id,
                    "group_name": ip_pool_name
                }
            )
            response = response.get("response")
            self.log("Received API response from 'get_reserve_ip_subpool' for the IP Pool '{0}': {1}".format(ip_pool_name, str(response)), "DEBUG")

            if not response:
                self.log("There is no reserve ip pool '{0}' present in the Cisco Catalyst Center system.".format(ip_pool_name), "INFO")
                return False

        except Exception as e:
            self.msg = (
                "Error while getting the details for reserve IP Pool with name '{0}' present in "
                "Cisco Catalyst Center: {1}"
            ).format(ip_pool_name, str(e))
            self.set_operation_result("failed", False, self.msg, "ERROR").check_return_status()

        return True

    def get_anycast_gateway_details(self, vn_name, ip_pool_name, fabric_id):
        """
        Retrieves details of an Anycast Gateway for a specified virtual network and IP pool.
        Args:
            self (object): An instance of a class used for interacting with Cisco Catalyst Center.
            vn_name (str): The name of the virtual network associated with the Anycast Gateway.
            ip_pool_name (str): The name of the IP pool for which the Anycast Gateway details are requested.
            fabric_id (str): The identifier of the fabric within which the IP pool is located.
        Returns:
            dict or None: Returns a dictionary containing the Anycast Gateway details if found,
                        or None if no details are available.
        Description:
            This function sends a request to the Cisco Catalyst Center to fetch the details
            of an Anycast Gateway related to the specified virtual network and IP pool.
            The function primarily serves to facilitate the management and configuration of
            Anycast Gateways in network environments, aiding in tasks related to IP addressing
            and routing.
        """

        try:
            response = self.dnac._exec(
                family="sda",
                function="get_anycast_gateways",
                op_modifies=True,
                params={
                    "fabric_id": fabric_id,
                    "ip_pool_name": ip_pool_name,
                    "virtual_network_name": vn_name
                }
            )
            response = response.get("response")
            self.log("Received API response from 'get_anycast_gateways' for the IP Pool '{0}': {1}".format(ip_pool_name, str(response)), "DEBUG")

            if not response:
                self.log("There is no reserve ip pool '{0}' present in the Cisco Catalyst Center system.".format(ip_pool_name), "INFO")
                return None

        except Exception as e:
            self.msg = (
                "Error while getting the details for reserve IP Pool with name '{0}' for the virtual network '{1}' present in "
                "Cisco Catalyst Center: {2}"
            ).format(ip_pool_name, vn_name, str(e))
            self.set_operation_result("failed", False, self.msg, "ERROR").check_return_status()

        return response[0]

    def validate_gateway_payload(self, anycast):
        """
        Validates the payload parameters for configuring an Anycast Gateway.
        Args:
            self (object): An instance of a class used for interacting with Cisco Catalyst Center.
            anycast (dict): A dictionary containing configuration parameters for the Anycast Gateway.
        Returns:
            self (object): The instance of the class, which allows for method chaining or further handling
                based on the validation outcome.
        Description:
            This function checks the validity of several parameters specified in the provided
            `anycast` dictionary for configuring an Anycast Gateway.
            - It validates the `pool_type` to ensure it is either "EXTENDED_NODE" or "FABRIC_AP".
            If not valid, it logs an error message and sets the status to "failed".
            - The `tcp_mss_adjustment` is validated to be within the range of 500 to 1440.
            - The `traffic_type` is validated through a separate method `validate_traffic_type()`.
            - The `vlan_id` is checked to be within the range of 2 to 4094, excluding the reserved
                VLAN IDs 1002-1005 and 2046. An error message is logged, and the status is set to
                "failed" if the `vlan_id` is invalid.
            If all parameters are valid, a success message is logged indicating successful validation
            of the Anycast Gateway configuration parameters.
        """

        pool_type = anycast.get("pool_type")
        if pool_type and pool_type not in ["EXTENDED_NODE", "FABRIC_AP"]:
            self.msg = (
                "Invalid pool_type '{0}' parameter given in the playbook. Please provide one of the following "
                "pool_type ['EXTENDED_NODE', 'FABRIC_AP']."
            ).format(pool_type)
            self.set_operation_result("failed", False, self.msg, "ERROR").check_return_status()

        tcp_mss_adjustment = anycast.get("tcp_mss_adjustment")
        if tcp_mss_adjustment and tcp_mss_adjustment not in range(500, 1441):
            self.msg = (
                "Invalid tcp_mss_adjustment '{0}' given in the playbook. Allowed tcp_mss_adjustment range is (500,1440)."
            ).format(tcp_mss_adjustment)
            self.set_operation_result("failed", False, self.msg, "ERROR").check_return_status()

        traffic_type = anycast.get("traffic_type")
        if traffic_type:
            # Validate the given traffic type for Vlan/VN/Anycast configuration.
            self.validate_traffic_type(traffic_type.upper())

        vlan_id = anycast.get("vlan_id")
        if vlan_id and vlan_id not in range(2, 4094) or vlan_id in [1002, 1003, 1004, 1005, 2046]:
            self.msg = (
                "Invalid vlan_id '{0}' given in the playbook. Allowed VLAN range is (2,4094) except for "
                "reserved VLANs 1002-1005, and 2046."
            ).format(vlan_id)
            self.set_operation_result("failed", False, self.msg, "ERROR").check_return_status()

        self.log("Given parameter '{0}' for the configuration of anycast gateway validated successfully.".format(str(anycast)), "INFO")

        return self

    def get_anycast_gateway_mapping(self, vn_name):
        """
        Retrieves a mapping of Anycast Gateway configuration parameters from their common names
        to their respective API field names.
        Args:
            self (object): An instance of a class used for interacting with Cisco Catalyst Center.
            vn_name (str): The name of the layer3 Virtual Network to check whether it's INFRA_VN or not
                and seperate the payload for the API for respective VN.
        Returns:
            dict: A dictionary where the keys are common parameter names used in configuration
                and the values are the corresponding field names used in the Anycast Gateway API.
        Description:
            This function creates and returns a mapping of various configuration parameters
            associated with Anycast Gateways. The mapping translates common, user-friendly names
            into the specific field names expected by the API.
        """

        gateway_mapping = {
            "tcp_mss_adjustment": "tcpMssAdjustment",
            "vlan_name": "vlanName",
            "vlan_id": "vlanId",
            "traffic_type": "trafficType",
            "pool_type": "poolType",
            "security_group_name": "securityGroupName",
            "is_critical_pool": "isCriticalPool",
            "layer2_flooding_enabled": "isLayer2FloodingEnabled",
            "fabric_enabled_wireless": "isWirelessPool",
            "ip_directed_broadcast": "isIpDirectedBroadcast",
            "intra_subnet_routing_enabled": "isIntraSubnetRoutingEnabled",
            "multiple_ip_to_mac_addresses": "isMultipleIpToMacAddresses",
            "supplicant_based_extended_node_onboarding": "isSupplicantBasedExtendedNodeOnboarding",
            "group_policy_enforcement_enabled": "isGroupBasedPolicyEnforcementEnabled"
        }

        if vn_name == "INFRA_VN":
            params_to_remove = ["is_critical_pool", "layer2_flooding_enabled", "fabric_enabled_wireless", "security_group_name",
                                "ip_directed_broadcast", "intra_subnet_routing_enabled", "multiple_ip_to_mac_addresses"]
            for item in params_to_remove:
                gateway_mapping.pop(item, None)

        return gateway_mapping

    def create_anycast_payload(self, anycast, fabric_id):
        """
        Constructs the payload for creating an Anycast Gateway configuration.
        Args:
            self (object): An instance of a class used for interacting with Cisco Catalyst Center.
            anycast (dict): A dictionary containing Anycast Gateway configuration details.
            fabric_id (str): The identifier for the fabric associated with the Anycast Gateway.
        Returns:
            dict: A dictionary representing the Anycast Gateway payload, structured with the necessary
                parameters for API submission. This includes:
                - fabricId: The ID of the fabric.
                - virtualNetworkName: The name of the virtual network.
                - ipPoolName: The name of the IP pool.
                - trafficType: The type of traffic.
                - Additional parameters mapped from the Anycast configuration, with defaults set as needed.
        Description:
            This function creates a payload for the Anycast Gateway API based on the provided configuration
            details. It retrieves a mapping of parameters needed for the Anycast configuration and populates
            the payload with values from the `anycast` dictionary.
            This structured payload then be sent to the API to create/update Anycast Gateway configuration.
        """

        vn_name = anycast.get("vn_name")
        anycast_payload = {
            "fabricId": fabric_id,
            "virtualNetworkName": vn_name,
            "ipPoolName": anycast.get("ip_pool_name"),
            "trafficType": anycast.get("traffic_type"),
        }
        anycast_mapping = self.get_anycast_gateway_mapping(vn_name)

        if vn_name == "INFRA_VN":
            infra_enable_list = ["supplicant_based_extended_node_onboarding", "group_policy_enforcement_enabled"]

            for key, value in anycast_mapping.items():
                playbook_param = anycast.get(key)
                if key == "pool_type":
                    anycast_payload[value] = anycast.get(key, "EXTENDED_NODE")
                    continue

                if playbook_param is not None:
                    anycast_payload[value] = playbook_param
                elif playbook_param is None and key in infra_enable_list:
                    anycast_payload[value] = False
        else:
            params_enable_list = ["is_critical_pool", "layer2_flooding_enabled", "fabric_enabled_wireless",
                                  "ip_directed_broadcast", "intra_subnet_routing_enabled", "multiple_ip_to_mac_addresses"]
            for key, value in anycast_mapping.items():
                playbook_param = anycast.get(key)

                if playbook_param is not None:
                    anycast_payload[value] = playbook_param
                elif playbook_param is None and key in params_enable_list:
                    anycast_payload[value] = False

        if anycast.get("auto_generate_vlan_name") is True or anycast_payload.get("isCriticalPool") is True:
            anycast_payload.pop("vlanName", None)
            anycast_payload.pop("vlanId", None)
            anycast_payload["autoGenerateVlanName"] = True

        return anycast_payload

    def is_gateway_needs_update(self, anycast, anycast_details_in_ccc):
        """
        Checks if the Anycast Gateway configuration needs to be updated based on provided parameters.
        Args:
            self (object): An instance of a class used for interacting with Cisco Catalyst Center.
            anycast (dict): A dictionary containing the current configuration parameters for the Anycast Gateway.
            anycast_details_in_ccc (dict): A dictionary containing the current Anycast Gateway configuration details
                                            from the Cisco Catalyst Center (CCC) to compare against.
        Returns:
            bool: True if any of the relevant parameters differ between the provided `anycast` configuration and the
                corresponding parameters in `anycast_details_in_ccc`, indicating that an update is needed.
                Returns False if no differences are found.
        Description:
            This function compares specific configuration parameters of an Anycast Gateway between the provided
            configuration (`anycast`) and the existing configuration in the Cisco Catalyst Center.
            If any differences are detected, it logs an informational message and returns True. If no discrepancies
            are found, the function returns False, indicating that the current configuration is up to date.
        """

        update_param_to_check = ["tcp_mss_adjustment", "traffic_type", "security_group_name", "layer2_flooding_enabled", "fabric_enabled_wireless"
                                 , "ip_directed_broadcast", "multiple_ip_to_mac_addresses", "supplicant_based_extended_node_onboarding"
                                 , "group_policy_enforcement_enabled"]
        vn_name = anycast.get("vn_name")
        anycast_mapping = self.get_anycast_gateway_mapping(vn_name)

        if vn_name == "INFRA_VN":
            params_to_remove = ["security_group_name", "layer2_flooding_enabled", "fabric_enabled_wireless",
                                "ip_directed_broadcast", "multiple_ip_to_mac_addresses"]
            for param in params_to_remove:
                update_param_to_check.remove(param)
        else:
            update_param_to_check.remove("supplicant_based_extended_node_onboarding")
            update_param_to_check.remove("group_policy_enforcement_enabled")

        if anycast.get("traffic_type") and anycast_details_in_ccc.get("isCriticalPool") is True:
            update_param_to_check.remove("traffic_type")

        for param in update_param_to_check:
            if anycast.get(param) is not None:
                key_in_ccc = anycast_mapping.get(param)
                if anycast.get(param) != anycast_details_in_ccc.get(key_in_ccc):
                    msg = (
                        "Given parameter '{0}' for the given anycast doesnot match so gateway needs update."
                    ).format(param)
                    self.log(msg, "INFO")
                    return True

        return False

    def get_anycast_gateway_update_payload(self, anycast, anycast_details_in_ccc):
        """
        Constructs the payload necessary to update the Anycast Gateway configuration in Cisco Catalyst Center.
        Args:
            self (object): An instance of a class used for interacting with Cisco Catalyst Center.
            anycast (dict): A dictionary containing the new configuration parameters for the Anycast Gateway.
            anycast_details_in_ccc (dict): A dictionary containing the current Anycast Gateway configuration details from CCC.
        Returns:
            dict: A dictionary containing the payload needed to update the Anycast Gateway configuration.
        Description:
            This function constructs an update payload for the Anycast Gateway by combining existing values from
            `anycast_details_in_ccc` with any new values specified in the `anycast` dictionary. If a parameter exists in
            `anycast`, it is prioritized over the existing value. If a parameter does not exist in `anycast`, the function
            retains the current value from `anycast_details_in_ccc`.
            The resulting payload can be used for updating the Anycast Gateway configuration in the Cisco Catalyst Center.
        """

        vn_name = anycast_details_in_ccc.get("virtualNetworkName")
        anycast_payload = {
            "id": anycast_details_in_ccc.get("id"),
            "fabricId": anycast_details_in_ccc.get("fabricId"),
            "virtualNetworkName": vn_name,
            "ipPoolName": anycast_details_in_ccc.get("ipPoolName"),
            "vlanName": anycast_details_in_ccc.get("vlanName"),
            "vlanId": anycast_details_in_ccc.get("vlanId"),
            "isCriticalPool": anycast_details_in_ccc.get("isCriticalPool"),
            "poolType": anycast_details_in_ccc.get("poolType"),
            "isIntraSubnetRoutingEnabled": anycast_details_in_ccc.get("isIntraSubnetRoutingEnabled")
        }
        params_in_playbook = ["tcp_mss_adjustment", "traffic_type", "security_group_name", "layer2_flooding_enabled",
                              "fabric_enabled_wireless", "ip_directed_broadcast", "multiple_ip_to_mac_addresses",
                              "supplicant_based_extended_node_onboarding", "group_policy_enforcement_enabled"]

        anycast_mapping = self.get_anycast_gateway_mapping(vn_name)

        if vn_name == "INFRA_VN":
            params_to_remove = ["security_group_name", "layer2_flooding_enabled", "fabric_enabled_wireless",
                                "ip_directed_broadcast", "multiple_ip_to_mac_addresses"]
            for param in params_to_remove:
                params_in_playbook.remove(param)
            anycast_payload.pop("isCriticalPool", None)
            anycast_payload.pop("isIntraSubnetRoutingEnabled", None)
        else:
            params_in_playbook.remove("supplicant_based_extended_node_onboarding")
            params_in_playbook.remove("group_policy_enforcement_enabled")
            anycast_payload.pop("poolType", None)

        if anycast.get("traffic_type") and anycast_details_in_ccc.get("isCriticalPool") is True:
            params_in_playbook.remove("traffic_type")
            anycast_payload["trafficType"] = anycast_details_in_ccc.get("trafficType")

        for param in params_in_playbook:
            key = anycast_mapping.get(param)
            if anycast.get(param) is not None:
                anycast_payload[key] = anycast.get(param)
            else:
                anycast_payload[key] = anycast_details_in_ccc.get(key)

        return anycast_payload

    def add_anycast_gateways_in_system(self, collected_add_anycast_payload):
        """
        Adds Anycast Gateways to the Cisco Catalyst Center using the provided payload.
        Args:
            self (object): An instance of a class used for interacting with Cisco Catalyst Center.
            collected_add_anycast_payload (dict): A dictionary containing the necessary details for
                adding Anycast Gateways.
        Returns:
            self (object): The instance of the class, allowing for method chaining. The status of the operation
                can be checked via the `status` attribute.
        Description:
            This function interacts with the Cisco DNA Center API to add Anycast Gateways. It sends the provided
            payload to the API and processes the response.
            In case of an exception during the API call, the function captures the exception and logs the error.
            The method returns the instance itself, allowing for further interactions with the object.
        """

        try:
            payload = {"payload": collected_add_anycast_payload}
            task_name = "add_anycast_gateways"
            task_id = self.get_taskid_post_api_call("sda", task_name, payload)

            if not task_id:
                self.msg = "Unable to retrive the task_id for the task '{0}'.".format(task_name)
                self.set_operation_result("failed", False, self.msg, "ERROR")
                return self

            success_msg = "Anycast Gateway(s) '{0}' added successfully in the Cisco Catalyst Center.".format(self.created_anycast)
            self.get_task_status_from_tasks_by_id(task_id, task_name, success_msg)

        except Exception as e:
            self.msg = (
                "An exception occured while adding the Anycast Gateway(s) '{0}' in the Cisco Catalyst "
                "Center: {1}"
            ).format(self.created_anycast, str(e))
            self.set_operation_result("failed", False, self.msg, "ERROR")

        return self

    def update_anycast_gateways_in_system(self, collected_update_anycast_payload):
        """
        Updates Anycast Gateways in the Cisco Catalyst Center using the provided payload.
        Args:
            self (object): An instance of a class used for interacting with Cisco Catalyst Center.
            collected_update_anycast_payload (dict): A dictionary containing the necessary details for updating
                Anycast Gateways.
        Returns:
            self (object): The instance of the class, allowing for method chaining. The status of the operation
                can be checked via the `status` attribute.
        Description:
            This function interacts with the Cisco DNA Center API to update Anycast Gateways. It sends the provided
            payload to the API and processes the response.
            In case of an exception during the API call, the function captures the exception and logs the error.
            The method returns the instance itself, allowing for further interactions with the object.
        """

        try:
            payload = {"payload": collected_update_anycast_payload}
            task_name = "update_anycast_gateways"
            task_id = self.get_taskid_post_api_call("sda", task_name, payload)

            if not task_id:
                self.msg = "Unable to retrive the task_id for the task '{0}'.".format(task_name)
                self.set_operation_result("failed", False, self.msg, "ERROR")
                return self

            success_msg = "Anycast Gateway(s) '{0}' updated successfully in the Cisco Catalyst Center.".format(self.updated_anycast)
            self.get_task_status_from_tasks_by_id(task_id, task_name, success_msg)

        except Exception as e:
            self.msg = (
                "An exception occured while updating the Anycast Gateway(s) '{0}' in the Cisco Catalyst "
                "Center: {1}"
            ).format(self.updated_anycast, str(e))
            self.set_operation_result("failed", False, self.msg, "ERROR")

        return self

    def delete_anycast_gateway(self, gateway_id, unique_anycast):
        """
        Deletes an Anycast Gateway in the Cisco Catalyst Center based on the provided gateway ID.
        Args:
            self (object): An instance of a class used for interacting with Cisco Catalyst Center.
            gateway_id (str): The unique identifier of the Anycast Gateway to be deleted.
            unique_anycast (str): A descriptive name or identifier for the Anycast Gateway, used for logging.
        Returns:
            self (object): The instance of the class, allowing for method chaining. The status of the operation
                can be checked via the `status` attribute.
        Description:
            This function sends a request to the Cisco DNA Center API to delete the specified Anycast Gateway
            using its ID. It processes the API response and checks for the presence of a task ID to confirm that
            the deletion request was received.
            If the deletion is successful, it logs a success message and appends the deleted gateway's name to the
            `deleted_anycast` list. If there is an error during the deletion process or an exception occurs, it
            captures the error, logs an appropriate message, and updates the status.
            The method returns the instance itself, allowing for further interactions with the object.
        """

        try:
            payload = {"id": gateway_id}
            task_name = "delete_anycast_gateway_by_id"
            task_id = self.get_taskid_post_api_call("sda", task_name, payload)

            if not task_id:
                self.msg = "Unable to retrive the task_id for the task '{0}'.".format(task_name)
                self.set_operation_result("failed", False, self.msg, "ERROR")
                return self

            success_msg = "Anycast Gateway '{0}' deleted successfully from the Cisco Catalyst Center.".format(unique_anycast)
            self.get_task_status_from_tasks_by_id(task_id, task_name, success_msg)
            self.deleted_anycast.append(unique_anycast)

        except Exception as e:
            self.msg = "Exception occurred while deleting the Anycast Gateway '{0}' due to: {1}".format(unique_anycast, str(e))
            self.set_operation_result("failed", False, self.msg, "ERROR")

        return self

    def get_have(self, config):
        """
        Collects and stores the current state of fabric VLANs, Layer3 virtual networks, and Anycast
        gateway IDs based on the provided configuration.
        Args:
            self (object): An instance of a class used for interacting with Cisco Catalyst Center.
            config (dict): A configuration dictionary containing details about fabric VLANs,
                        virtual networks, and Anycast gateways.
        Returns:
            self (object): The instance of the class with the updated `have` attribute containing the current
                state of fabric Vlan, Virtual Network and Anycast Gateways.
        Description:
            This function processes the given configuration to gather details about:
            - Fabric VLANs: It retrieves VLAN IDs based on the names provided.
            - Layer3 Virtual Networks: It checks for the existence of specified virtual networks.
            - Anycast Gateways: It collects IDs of Anycast gateways based on their associated
            virtual networks and IP pool names.
            For each of these components, the function logs success messages for each
            successfully collected item. The collected data is stored in the `have`
            attribute of the instance.
        """

        have = {
            "fabric_vlan_ids": [],
            "l3_vn_name": [],
            "anycast_gateway_ids": []
        }

        fabric_vlan_details = config.get('fabric_vlan')
        if fabric_vlan_details:
            for vlan in fabric_vlan_details:
                vlan_name = vlan.get("vlan_name")
                vlan_id = vlan.get("vlan_id")

                fabric_vlan_ids = self.collect_fabric_vlan_ids(vlan_name, vlan_id)

                if fabric_vlan_ids:
                    self.log("Successfully collect the vlan details for the vlan '{0}'.".format(vlan_name), "DEBUG")
                    have["fabric_vlan_ids"].extend(fabric_vlan_ids)

        virtual_networks = config.get('virtual_networks')
        if virtual_networks:
            for vn in virtual_networks:
                vn_name = vn.get("vn_name")
                is_vn_exist = self.is_virtual_network_exist(vn_name)

                if is_vn_exist:
                    self.log("Successfully collect the layer3 VN details for the VN '{0}'.".format(vn_name), "DEBUG")
                    have["l3_vn_name"].append(vn_name)

        anycast_gateways = config.get('anycast_gateways')
        if anycast_gateways:
            for anycast in anycast_gateways:
                vn_name = anycast.get("vn_name")
                ip_pool_name = anycast.get("ip_pool_name")
                site_name = anycast.get("fabric_site_location").get("site_name_hierarchy")
                site_id = self.get_site_id(site_name)
                fabric_type = anycast.get("fabric_site_location").get("fabric_type")
                # Validate the fabric_type given in the playbook
                self.validate_fabric_type(fabric_type).check_return_status()

                if fabric_type == "fabric_site":
                    fabric_id = self.get_fabric_site_id(site_name, site_id)
                else:
                    fabric_id = self.get_fabric_zone_id(site_name, site_id)

                # Collect the gateway id with combination of vn_name, ip_pool_name and fabric id
                gateway_details = self.get_anycast_gateway_details(vn_name, ip_pool_name, fabric_id)
                if gateway_details:
                    gateway_id = gateway_details.get("id")
                    self.log("Successfully collect the anycast gateway details for the IP pool '{0}'.".format(ip_pool_name), "DEBUG")
                    have["anycast_gateway_ids"].append(gateway_id)

        self.have = have
        self.log("Current State (have): {0}".format(str(have)), "INFO")

        return self

    def get_want(self, config):
        """
        Collects and validates the desired state of fabric VLANs, virtual networks,
        and Anycast gateways based on the provided configuration.
        Args:
            self (object): An instance of a class used for interacting with Cisco Catalyst Center.
            config (dict): A configuration dictionary containing details about fabric VLANs,
                        virtual networks, and Anycast gateways.
        Returns:
            self (object): The instance of the class with the updated `want` attribute containing the validated desired state
                of fabric Vlan, Virtual Network and Anycast Gateways.
        Description:
            This function processes the given configuration to gather and validate details about:
            - Fabric VLANs: It collects information on VLANs, ensuring required parameters are present
            and that the VLAN IDs are within valid ranges.
            - Virtual Networks: It checks for the existence of specified virtual networks, ensuring
            their names are provided and valid.
            - Anycast Gateways: It collects details about Anycast gateways, checking that necessary
            parameters are present and that referenced virtual networks and IP pools exist.
            If any required parameters are missing or invalid, the function logs an error message
            and updates the status accordingly. On successful collection of all parameters, it logs
            the desired state and sets the status to success.
        """

        want = {}

        fabric_vlan_details = config.get('fabric_vlan')
        if fabric_vlan_details:
            fabric_vlan_info = []

            for vlan in fabric_vlan_details:
                missing_required_param = []
                vlan_name = vlan.get("vlan_name")
                fabric_site_locations = vlan.get("fabric_site_locations")
                vlan_id = vlan.get("vlan_id")
                required_param = ["vlan_name", "vlan_id", "fabric_site_locations"]

                for param in required_param:
                    value = vlan.get(param)
                    if not value:
                        self.log("Adding the missing param '{0}' required for fabric Vlan operations".format(value), "DEBUG")
                        missing_required_param.append(param)

                if vlan_id not in range(2, 4094) or vlan_id in [1002, 1003, 1004, 1005, 2046]:
                    self.msg = (
                        "Invalid vlan_id '{0}' given in the playbook. Allowed VLAN range is (2,4094) except for "
                        "reserved VLANs 1002-1005, and 2046."
                    ).format(vlan_id)
                    self.set_operation_result("failed", False, self.msg, "ERROR").check_return_status()
                    return self

                if missing_required_param:
                    self.msg = (
                        "Required parameter(s) '{0}' are missing and they must be given in the playbook in order to  "
                        "perform any layer2 fabric vlan operation in Cisco Catalyst Center."
                    ).format(missing_required_param)
                    self.set_operation_result("failed", False, self.msg, "ERROR").check_return_status()

                # Validate the Fabric Vlan name against the regex
                self.is_valid_fabric_vlan_name(vlan_name).check_return_status()

                for fabric in fabric_site_locations:
                    site_name = fabric.get("site_name_hierarchy")
                    fabric_type = fabric.get("fabric_type")

                    if not site_name or not fabric_type:
                        self.msg = (
                            "Required parameter 'site_name' and 'fabric_type 'must be given in the playbook in order to "
                            "perform any operation on fabric vlan '{0}'."
                        ).format(vlan_name)
                        self.set_operation_result("failed", False, self.msg, "ERROR").check_return_status()

                    # Validate the correct fabric_type given in the playbook
                    self.validate_fabric_type(fabric_type).check_return_status()
                fabric_vlan_info.append(vlan)

            want["fabric_vlan_info"] = fabric_vlan_info

        vn_details = config.get('virtual_networks')
        if vn_details:
            vn_info = []

            for vn in vn_details:
                vn_name = vn.get("vn_name")

                if not vn_name:
                    # self.status = "failed"
                    self.msg = (
                        "Required parameter 'vn_name' must be given in the playbook in order to perform any virtual "
                        "networks operation including creation/updation/deletion in Cisco Catalyst Center."
                    )
                    self.set_operation_result("failed", False, self.msg, "ERROR").check_return_status()

                # Validate the VN name against the regex
                self.is_valid_vn_name(vn_name).check_return_status()
                vn_info.append(vn)

            want["vn_info"] = vn_info

        anycast_gateway_details = config.get("anycast_gateways")
        if anycast_gateway_details:
            anycast_info = []
            state = self.params.get("state")

            for anycast in anycast_gateway_details:
                required_param = ["vn_name", "fabric_site_location", "ip_pool_name"]
                vn_name = anycast.get("vn_name")
                ip_pool_name = anycast.get("ip_pool_name")
                missing_required_item = []

                for item in required_param:
                    if not anycast.get(item):
                        missing_required_item.append(item)

                if missing_required_item:
                    self.msg = (
                        "Required parameter '{0}' must be given in the playbook in order to perform any anycast "
                        "networks operation including creation/updation/deletion in Cisco Catalyst Center."
                    ).format(missing_required_item)
                    self.set_operation_result("failed", False, self.msg, "ERROR").check_return_status()

                is_vn_exist = self.is_virtual_network_exist(vn_name)

                if not is_vn_exist:
                    self.msg = (
                        "Given layer3 Virtual Network '{0}' does not exist in the Cisco Catalyst Center. "
                        "Please create the L3 Virtual network first in order to configure anycast gateway."
                    ).format(vn_name)
                    if state == "deleted":
                        continue
                    self.set_operation_result("failed", False, self.msg, "ERROR").check_return_status()

                site_name = anycast.get("fabric_site_location").get("site_name_hierarchy")
                if not site_name:
                    self.msg = (
                        "Parameter 'site_name' must be provided in the playbook in order to configure "
                        "anycast gateway in the Catalyst Center."
                    )
                    self.set_operation_result("failed", False, self.msg, "ERROR").check_return_status()

                site_id = self.get_site_id(site_name)
                if not site_id:
                    self.msg = "Given site '{0}' does not exist in the Catalyst Center.".format(site_name)
                    self.set_operation_result("failed", False, self.msg, "ERROR").check_return_status()

                is_pool_exist = self.is_ip_pool_exist(ip_pool_name, site_id)
                if not is_pool_exist:
                    self.msg = (
                        "Given reserve ip pool'{0}' does not exist and reserve to the given site '{1}'. "
                        "Please create and reserve the given IP pool using the network_settings_workflow_manager"
                        " module for the configuration of Anycast gateways in the Catalyst Center."
                    ).format(ip_pool_name, site_name)
                    self.set_operation_result("failed", False, self.msg, "ERROR").check_return_status()

                anycast_info.append(anycast)
            want["anycast_info"] = anycast_info

        self.want = want
        self.msg = (
            "Successfully collected all parameters from the playbook for creation/updation/deletion of fabric vlan "
            "and layer3 virtual networks and for the anycast gateway configuration as well."
        )
        self.log("Desired State (want): {0}".format(str(self.want)), "INFO")

        return self

    def update_fabric_vlan_vn_anycast_gateway_messages(self):
        """
        Updates and logs messages based on the status of fabric VLANs, virtual networks,
        and Anycast gateways.
        Args:
            self (object): An instance of a class used for interacting with Cisco Catalyst Center.
        Returns:
            self (object): Returns the current instance of the class with updated `result`
                        and `msg` attributes.
        Description:
            This method aggregates status messages related to the creation, update, or
            deletion of fabric VLANs, Layer 3 virtual networks, and Anycast gateways.
            The messages include success and failure notifications for:
            - Fabric VLANs: created, updated, or deleted
            - Layer3 Virtual Networks: created, updated, or deleted
            - Anycast Gateways: added, updated, or deleted
            The method also updates the `result["response"]` attribute with the concatenated status messages.
        """

        self.result["changed"] = False
        result_msg_list = []

        if self.created_fabric_vlan:
            create_fabric_vlan = "Layer2 Fabric VLAN(s) '{0}' created successfully in the Cisco Catalyst Center.".format(self.created_fabric_vlan)
            result_msg_list.append(create_fabric_vlan)

        if self.updated_fabric_vlan:
            update_fabric_vlan = "Layer2 Fabric VLAN(s) '{0}' updated successfully in the Cisco Catalyst Center.".format(self.updated_fabric_vlan)
            result_msg_list.append(update_fabric_vlan)

        if self.no_update_fabric_vlan:
            no_update_fabric_vlan = "Given Fabric VLAN(s) '{0}' does not need any update in Cisco Catalyst Center.".format(self.no_update_fabric_vlan)
            result_msg_list.append(no_update_fabric_vlan)

        if self.created_vn:
            create_vn_msg = "Layer3 Virtual Network(s) '{0}' created successfully in the Cisco Catalyst Center.".format(self.created_vn)
            result_msg_list.append(create_vn_msg)

        if self.updated_vn:
            update_vn_msg = "Layer3 Virtual Network(s '{0}' updated successfully in the Cisco Catalyst Center.".format(self.updated_vn)
            result_msg_list.append(update_vn_msg)

        if self.no_update_vn:
            no_update_vn_msg = "Given Virtual Network(s '{0}' does not need any update in Cisco Catalyst Center.".format(self.no_update_vn)
            result_msg_list.append(no_update_vn_msg)

        if self.created_anycast:
            create_anycast_msg = "Anycast Gateway(s) '{0}' added successfully in the Cisco Catalyst Center.".format(self.created_anycast)
            result_msg_list.append(create_anycast_msg)

        if self.updated_anycast:
            update_anycast_msg = "Anycast Gateway(s) '{0}' updated successfully in the Cisco Catalyst Center.".format(self.updated_anycast)
            result_msg_list.append(update_anycast_msg)

        if self.no_update_anycast:
            no_update_anycast_msg = "Given Anycast Gateway(s) '{0}' does not need any update in the Cisco Catalyst Center.".format(self.no_update_anycast)
            result_msg_list.append(no_update_anycast_msg)

        if self.deleted_fabric_vlan:
            delete_fabric_vlan = "Fabric VLAN(s) '{0}' deleted successfully from the Cisco Catalyst Center.".format(self.deleted_fabric_vlan)
            result_msg_list.append(delete_fabric_vlan)

        if self.absent_fabric_vlan:
            absent_vlan_msg = "Unable to delete Fabric VLAN(s) '{0}' as they are not present in Cisco Catalyst Center.".format(self.absent_fabric_vlan)
            result_msg_list.append(absent_vlan_msg)

        if self.deleted_vn:
            delete_vn_msg = "Layer3 Virtual Network(s) '{0}' deleted successfully from the Cisco Catalyst Center.".format(self.deleted_vn)
            result_msg_list.append(delete_vn_msg)

        if self.absent_vn:
            absent_vn_msg = "Unable to delete layer3 Virtual Network(s) '{0}' as they are not present in Cisco Catalyst Center.".format(self.absent_vn)
            result_msg_list.append(absent_vn_msg)

        if self.deleted_anycast:
            delete_anycast_msg = "Anycast Gateway(s) '{0}' deleted successfully from the Cisco Catalyst Center.".format(self.deleted_anycast)
            result_msg_list.append(delete_anycast_msg)

        if self.absent_anycast:
            absent_anycast_msg = "Unable to delete Anycast Gateway(s) '{0}' as they are not present in Cisco Catalyst Center.".format(self.absent_anycast)
            result_msg_list.append(absent_anycast_msg)

        if (
            self.created_fabric_vlan or self.updated_fabric_vlan or self.deleted_fabric_vlan
            or self.created_vn or self.updated_vn or self.deleted_vn
            or self.created_anycast or self.updated_anycast or self.deleted_anycast
        ):
            self.result["changed"] = True

        self.msg = " ".join(result_msg_list)
        self.set_operation_result("success", self.result["changed"], self.msg, "INFO")

        return self

    def get_diff_merged(self, config):
        """
        Creates or updates fabric VLANs, virtual networks, and Anycast gateways in the Cisco Catalyst Center
        based on the provided configuration.
        Args:
            self (object): An instance of a class used for interacting with Cisco Catalyst Center.
            config (dict): A dictionary containing the configuration details for fabric VLANs, virtual networks,
                        and Anycast gateways. The structure includes:
                - 'fabric_vlan': List of dictionaries with details about fabric VLANs.
                - 'virtual_networks': List of dictionaries with details about virtual networks.
                - 'anycast_gateways': List of dictionaries with details about Anycast gateways.
        Returns:
            self (object): Returns the current instance of the class with updated attributes for created,
                        updated, and no-update status of VLANs, virtual networks, and Anycast gateways.
        Description:
            This method processes the configuration to perform the following tasks:
            - Create or update fabric VLANs based on the provided details. It checks for existing VLANs and
            determines if updates are necessary. Newly created VLANs are collected for later processing.
            - Create or update Layer 3 virtual networks. It checks for existing networks and evaluates if
            updates are required, collecting information on both newly created and updated networks.
            - Create or update Anycast gateways. The method checks if Anycast gateways already exist, evaluates
            whether they need updating, and collects payloads for creation or updates as necessary.
        """

        # Create/Update fabric Vlan in Cisco Catalyst Center
        fabric_vlan_details = config.get('fabric_vlan')

        if fabric_vlan_details:
            collected_add_vlan_payload, collected_update_vlan_payload = [], []
            for vlan in fabric_vlan_details:
                vlan_name = vlan.get("vlan_name")
                vlan_id = vlan.get("vlan_id")
                fabric_locations = vlan.get("fabric_site_locations")
                fabric_id_list = []

                for fabric in fabric_locations:
                    site_name = fabric.get("site_name_hierarchy")
                    fabric_type = fabric.get("fabric_type")
                    site_id = self.get_site_id(site_name)

                    if fabric_type == "fabric_site":
                        fabric_id = self.get_fabric_site_id(site_name, site_id)
                    else:
                        fabric_id = self.get_fabric_zone_id(site_name, site_id)

                    if not fabric_id:
                        self.msg = (
                            "Given site '{0}' is not the fabric site/zone. Please make it fabric site/zone "
                            "first to perform any layer2 fabric vlan operation in Cisco Catalyst Center."
                        ).format(site_name)
                        self.set_operation_result("failed", False, self.msg, "ERROR").check_return_status()

                    fabric_vlan_in_ccc = self.get_fabric_vlan_details(vlan_name, vlan_id, fabric_id)
                    if fabric_vlan_in_ccc:
                        if fabric_type == "fabric_site":
                            # Check fabric vlan needs update or not only for fabric site
                            if self.fabric_vlan_needs_update(vlan, fabric_vlan_in_ccc):
                                self.updated_fabric_vlan.append(vlan_name)
                                collected_update_vlan_payload.append(self.update_payload_fabric_vlan(vlan, fabric_vlan_in_ccc, fabric_id))
                            else:
                                self.no_update_fabric_vlan.append(vlan_name)
                                self.msg = "Given L2 Vlan '{0}' does not need any update".format(vlan_name)
                                self.log(self.msg, "INFO")
                                self.result["response"] = self.msg
                    else:
                        fabric_id_list.append(fabric_id)

                if fabric_id_list:
                    self.created_fabric_vlan.append(vlan_name)
                    collected_add_vlan_payload.extend(self.create_payload_for_fabric_vlan(vlan, fabric_id_list))

            if collected_add_vlan_payload:
                self.create_fabric_vlan(collected_add_vlan_payload).check_return_status()

            if collected_update_vlan_payload:
                self.update_fabric_vlan(collected_update_vlan_payload).check_return_status()

        # Create/Update virtual network in Cisco Catalyst Center
        virtual_networks = config.get('virtual_networks')
        if virtual_networks:
            collected_add_vn_payload, collected_update_vn_payload = [], []
            for vn_details in virtual_networks:
                vn_name = vn_details.get("vn_name")
                vn_payload = {"virtualNetworkName": vn_name}

                if self.have.get("l3_vn_name") and vn_name in self.have.get("l3_vn_name"):
                    # Given VN already present in Cisco Catalyst Center, check vn needs update or not.
                    vn_in_ccc = self.get_vn_details_from_ccc(vn_name)
                    vn_needs_update = self.is_vn_needs_update(vn_details, vn_in_ccc)
                    if vn_needs_update:
                        self.updated_vn.append(vn_name)
                        collected_update_vn_payload.append(self.update_payload_vn(vn_details, vn_in_ccc))
                    else:
                        # Given Virtual network doesnot need any update
                        self.no_update_vn.append(vn_name)
                        self.msg = "Given Virtual network '{0}' does not need any update".format(vn_name)
                        self.log(self.msg, "INFO")
                        self.result["response"] = self.msg
                else:
                    self.created_vn.append(vn_name)
                    vn_payload = self.create_vn_payload(vn_details)
                    collected_add_vn_payload.append(vn_payload)

            if collected_add_vn_payload:
                self.create_virtual_networks(collected_add_vn_payload).check_return_status()

            if collected_update_vn_payload:
                self.update_virtual_networks(collected_update_vn_payload).check_return_status()

        # Create/Update Anycast gateway in Cisco Catalyst Center with fabric id, ip pool and vn name
        anycast_gateways = config.get("anycast_gateways")
        if anycast_gateways:
            collected_add_anycast_payload, collected_update_anycast_payload = [], []
            for anycast in anycast_gateways:
                vn_name = anycast.get("vn_name")
                ip_pool_name = anycast.get("ip_pool_name")
                site_name = anycast.get("fabric_site_location").get("site_name_hierarchy")
                site_id = self.get_site_id(site_name)
                fabric_type = anycast.get("fabric_site_location").get("fabric_type")

                if fabric_type == "fabric_site":
                    fabric_id = self.get_fabric_site_id(site_name, site_id)
                else:
                    fabric_id = self.get_fabric_zone_id(site_name, site_id)

                # Collect the gateway id with combination of vn_name, ip_pool_name and fabric id
                unique_anycast = vn_name + "_" + ip_pool_name + "_" + site_name
                anycast_details_in_ccc = self.get_anycast_gateway_details(vn_name, ip_pool_name, fabric_id)
                self.validate_gateway_payload(anycast).check_return_status()

                if anycast_details_in_ccc:
                    # Already present in the Cisco Catalyst Center and check for update needed or not.
                    gateway_needs_update = self.is_gateway_needs_update(anycast, anycast_details_in_ccc)
                    if gateway_needs_update:
                        self.updated_anycast.append(unique_anycast)
                        gateway_update_payload = self.get_anycast_gateway_update_payload(anycast, anycast_details_in_ccc)
                        collected_update_anycast_payload.append(gateway_update_payload)
                    else:
                        self.no_update_anycast.append(unique_anycast)
                        self.msg = "Given Anycast gateway '{0}' does not need any update in the Cisco Catalyst Center".format(unique_anycast)
                        self.log(self.msg, "INFO")
                        self.result["response"] = self.msg
                else:
                    # Given Anycast gateways details not present in the system needs to create it
                    self.created_anycast.append(unique_anycast)
                    gateway_payload = self.create_anycast_payload(anycast, fabric_id)
                    collected_add_anycast_payload.append(gateway_payload)

            if collected_add_anycast_payload:
                self.add_anycast_gateways_in_system(collected_add_anycast_payload).check_return_status()

            if collected_update_anycast_payload:
                self.update_anycast_gateways_in_system(collected_update_anycast_payload).check_return_status()

        return self

    def get_diff_deleted(self, config):
        """
        Deletes specified layer2 fabric VLANs, layer3 virtual networks, and Anycast gateways from the Cisco Catalyst
        Center based on the provided configuration.
        Args:
            self (object): An instance of a class used for interacting with Cisco Catalyst Center.
            config (dict): A dictionary containing configuration details for deleting fabric VLANs, virtual networks,
                        and Anycast gateways. The structure includes:
                - 'fabric_vlan': List of dictionaries with details about fabric VLANs to delete.
                - 'virtual_networks': List of dictionaries with details about virtual networks to delete.
                - 'anycast_gateways': List of dictionaries with details about Anycast gateways to delete.
        Returns:
            self (object): Returns the current instance of the class after attempting to delete the specified items.
        Description:
            This method processes the provided configuration to perform the following deletion tasks:
            - For each specified layer2 fabric VLAN, it checks if the VLAN is associated with the given fabric site or zone.
            If so, it deletes the VLAN from the Cisco Catalyst Center. If the VLAN does not exist, it logs a warning and
            adds the VLAN name to the `absent_fabric_vlan` list.
            - For each specified layer3 virtual network, it checks if the network exists in the Cisco Catalyst Center. If
            present, it deletes the virtual network. If not, it logs an informational message and adds the network name
            to the `absent_vn` list.
            - For each specified Anycast gateway, it retrieves the corresponding gateway ID and deletes the gateway if it exists.
            If the gateway is not found, it logs an informational message and adds the unique identifier of the gateway to
            the `absent_anycast` list.
        """

        # Verify the deletion of layer2 Fabric Vlan from the Cisco Catalyst Center
        fabric_vlan_details = config.get('fabric_vlan')
        if fabric_vlan_details:
            for vlan in fabric_vlan_details:
                vlan_name = vlan.get("vlan_name")
                vlan_id = vlan.get("vlan_id")
                fabric_locations = vlan.get("fabric_site_locations")

                for fabric in fabric_locations:
                    site_name = fabric.get("site_name_hierarchy")
                    fabric_type = fabric.get("fabric_type")
                    site_id = self.get_site_id(site_name)

                    if fabric_type == "fabric_site":
                        fabric_id = self.get_fabric_site_id(site_name, site_id)
                    else:
                        fabric_id = self.get_fabric_zone_id(site_name, site_id)

                    if not fabric_id:
                        msg = (
                            "Given site '{0}' is not associated to given layer2 vlan '{1}' so cannot delete the "
                            "layer2 vlan from Cisco Catalyst Center."
                        ).format(site_name, vlan_name)
                        self.log(msg, "ERROR")
                        self.absent_fabric_vlan.append(vlan_name)
                        continue
                    fabric_vlan_in_ccc = self.get_fabric_vlan_details(vlan_name, vlan_id, fabric_id)
                    if not fabric_vlan_in_ccc:
                        self.log("Given fabric vlan '{0}' is not present in Cisco Catalyst Center.".format(vlan_name), "WARNING")
                        self.absent_fabric_vlan.append(vlan_name)
                        continue

                    fabric_vlan_id = fabric_vlan_in_ccc.get("id")
                    self.delete_layer2_fabric_vlan(vlan_name, fabric_vlan_id).check_return_status()

        # Delete layer3 Virtual network from the Cisco Catalyst Center
        virtual_network_details = config.get('virtual_networks')
        if virtual_network_details:
            for vn in virtual_network_details:
                vn_name = vn.get("vn_name")

                if self.have.get("l3_vn_name") and vn_name in self.have.get("l3_vn_name"):
                    vn_in_ccc = self.get_vn_details_from_ccc(vn_name)
                    vn_id = vn_in_ccc.get("id")
                    self.delete_layer3_virtual_network(vn_name, vn_id).check_return_status()
                else:
                    self.log("Given Virtual network '{0}' is not present in Cisco Catalyst Center.".format(vn_name), "INFO")
                    self.absent_vn.append(vn_name)
                    continue

        # Need ID of the anycast gateway to edelete the anycast gateway
        anycast_gateways = config.get("anycast_gateways")
        if anycast_gateways:
            for anycast in anycast_gateways:
                vn_name = anycast.get("vn_name")
                ip_pool_name = anycast.get("ip_pool_name")
                site_name = anycast.get("fabric_site_location").get("site_name_hierarchy")
                site_id = self.get_site_id(site_name)
                fabric_type = anycast.get("fabric_site_location").get("fabric_type")

                if fabric_type == "fabric_site":
                    fabric_id = self.get_fabric_site_id(site_name, site_id)
                else:
                    fabric_id = self.get_fabric_zone_id(site_name, site_id)

                # Collect the gateway id with combination of vn_name, ip_pool_name and fabric id
                unique_anycast = vn_name + "_" + ip_pool_name + "_" + site_name
                anycast_details_in_ccc = self.get_anycast_gateway_details(vn_name, ip_pool_name, fabric_id)

                if not anycast_details_in_ccc:
                    self.absent_anycast.append(unique_anycast)
                    self.log("Given Anycast gateway '{0}' is not present in Cisco Catalyst Center.".format(unique_anycast), "INFO")
                    continue
                gateway_id = anycast_details_in_ccc.get("id")

                self.delete_anycast_gateway(gateway_id, unique_anycast).check_return_status()

        return self

    def verify_diff_merged(self, config):
        """
        Verify the addition/update status of fabric Vlan, layer3 Virtual Networks and
        Anycast Gateway(s) in teh Cisco Catalyst Center.
        Parameters:
            self (object): An instance of a class used for interacting with Cisco Catalyst Center.
            config (dict): The configuration details to be verified.
        Returns:
            self (object): An instance of a class used for interacting with Cisco Catalyst Center.
        Description:
            This method verifies whether the specified configurations have been successfully added/updated
            in Cisco Catalyst Center as desired.
        """

        self.get_have(config)
        self.log("Current State (have): {0}".format(str(self.have)), "INFO")
        self.log("Desired State (want): {0}".format(str(self.want)), "INFO")

        # Verify the creation/updation of fabric Vlan in the Cisco Catalyst Center
        fabric_vlan_details = config.get('fabric_vlan')
        if fabric_vlan_details:
            verify_vlan_list, missed_vlan_list = [], []
            for vlan in fabric_vlan_details:
                vlan_name = vlan.get("vlan_name")
                vlan_id = vlan.get("vlan_id")
                fabric_locations = vlan.get("fabric_site_locations")
                for fabric in fabric_locations:
                    site_name = fabric.get("site_name_hierarchy")
                    fabric_type = fabric.get("fabric_type")
                    site_id = self.get_site_id(site_name)

                    if fabric_type == "fabric_site":
                        fabric_id = self.get_fabric_site_id(site_name, site_id)
                    else:
                        fabric_id = self.get_fabric_zone_id(site_name, site_id)

                    fabric_vlan_in_ccc = self.get_fabric_vlan_details(vlan_name, vlan_id, fabric_id)
                    if fabric_vlan_in_ccc:
                        verify_vlan_list.append(vlan_name)
                    else:
                        missed_vlan_list.append(vlan_name)

            if not missed_vlan_list:
                msg = (
                    "Requested fabric Vlan(s) '{0}' have been successfully added/updated to the Cisco Catalyst Center "
                    "and their addition/updation has been verified."
                ).format(verify_vlan_list)
                self.log(msg, "INFO")
            else:
                msg = (
                    "Playbook's input does not match with Cisco Catalyst Center, indicating that the fabric Vlan(s) '{0}' "
                    " addition/updation task may not have executed successfully."
                ).format(missed_vlan_list)
                self.log(msg, "INFO")

        # Verify the creation/updation of layer3 Virtual Network in the Cisco Catalyst Center
        virtual_networks = config.get('virtual_networks')
        if virtual_networks:
            verify_vn_list, missed_vn_list = [], []

            for vn_details in virtual_networks:
                vn_name = vn_details.get("vn_name")

                if self.have.get("l3_vn_name") and vn_name in self.have.get("l3_vn_name"):
                    verify_vn_list.append(vn_name)
                else:
                    missed_vn_list.append(vn_name)

            if not missed_vn_list:
                msg = (
                    "Requested layer3 Virtual Network(s) '{0}' have been successfully added/updated to the Cisco Catalyst Center "
                    "and their addition/updation has been verified."
                ).format(verify_vn_list)
                self.log(msg, "INFO")
            else:
                msg = (
                    "Playbook's input does not match with Cisco Catalyst Center, indicating that the fabric Vlan(s) '{0}' "
                    " addition/updation task may not have executed successfully."
                ).format(missed_vn_list)
                self.log(msg, "INFO")

        # Verify the creation/updation of Anycast gateway in the Cisco Catalyst Center with fabric id, ip pool and vn name
        anycast_gateways = config.get("anycast_gateways")
        if anycast_gateways:
            verify_anycast_list, missed_anycast_list = [], []
            for anycast in anycast_gateways:
                vn_name = anycast.get("vn_name")
                ip_pool_name = anycast.get("ip_pool_name")
                site_name = anycast.get("fabric_site_location").get("site_name_hierarchy")
                site_id = self.get_site_id(site_name)
                fabric_type = anycast.get("fabric_site_location").get("fabric_type")

                if fabric_type == "fabric_site":
                    fabric_id = self.get_fabric_site_id(site_name, site_id)
                else:
                    fabric_id = self.get_fabric_zone_id(site_name, site_id)

                # Collect the gateway id with combination of vn_name, ip_pool_name and fabric id
                unique_anycast = vn_name + "_" + ip_pool_name + "_" + site_name
                anycast_details_in_ccc = self.get_anycast_gateway_details(vn_name, ip_pool_name, fabric_id)

                if anycast_details_in_ccc:
                    verify_anycast_list.append(unique_anycast)
                else:
                    missed_anycast_list.append(unique_anycast)

            if not missed_anycast_list:
                msg = (
                    "Requested Anycast Gateway(s) '{0}' have been successfully added/updated to the Cisco Catalyst Center "
                    "and their addition/updation has been verified."
                ).format(verify_anycast_list)
                self.log(msg, "INFO")
            else:
                msg = (
                    "Playbook's input does not match with Cisco Catalyst Center, indicating that the Anycast Gateway(s) '{0}' "
                    " addition/updation task may not have executed successfully."
                ).format(missed_anycast_list)
                self.log(msg, "INFO")

        return self

    def verify_diff_deleted(self, config):
        """
        Verify the deletion status of fabric sites/zones fromt the Cisco Catalyst Center.
        Parameters:
            self (object): An instance of a class used for interacting with Cisco Catalyst Center.
            config (dict): The configuration details to be verified.
        Returns:
            self (object): An instance of a class used for interacting with Cisco Catalyst Center.
        Description:
            This method checks the deletion status of a configuration in Cisco Catalyst Center.
            It validates whether the specified fabric Vlan(s), layer3 Virtual Network(s) or
            Anycast Gateway(s) deleted from Cisco Catalyst Center and verified it.
        """

        self.get_have(config)
        self.log("Current State (have): {0}".format(str(self.have)), "INFO")
        self.log("Desired State (want): {0}".format(str(self.want)), "INFO")

        # Verify the deletion of layer2 Fabric Vlan from the Cisco Catalyst Center
        fabric_vlan_details = config.get('fabric_vlan')
        if fabric_vlan_details:
            verify_vlan_list, missed_vlan_list = [], []
            for vlan in fabric_vlan_details:
                vlan_name = vlan.get("vlan_name")
                vlan_id = vlan.get("vlan_id")
                fabric_locations = vlan.get("fabric_site_locations")

                for fabric in fabric_locations:
                    site_name = fabric.get("site_name_hierarchy")
                    fabric_type = fabric.get("fabric_type")
                    site_id = self.get_site_id(site_name)

                    if fabric_type == "fabric_site":
                        fabric_id = self.get_fabric_site_id(site_name, site_id)
                    else:
                        fabric_id = self.get_fabric_zone_id(site_name, site_id)

                    fabric_vlan_in_ccc = self.get_fabric_vlan_details(vlan_name, vlan_id, fabric_id)
                    if not fabric_vlan_in_ccc:
                        verify_vlan_list.append(vlan_name)
                    else:
                        missed_vlan_list.append(vlan_name)

            if verify_vlan_list:
                self.status = "success"
                msg = (
                    "Requested fabric Vlan(s) '{0}' have been successfully deleted from the Cisco Catalyst "
                    "Center and their deletion has been verified."
                ).format(verify_vlan_list)
                self.log(msg, "INFO")
            else:
                msg = (
                    "Playbook's input does not match with Cisco Catalyst Center, indicating that fabric Vlan(s)"
                    " '{0}' deletion task may not have executed successfully."
                ).format(missed_vlan_list)

        # Verify the deletion of layer3 Virtual Network from the Cisco Catalyst Center
        virtual_network_details = config.get('virtual_networks')
        if virtual_network_details:
            verify_vn_list, missed_vn_list = [], []
            for vn in virtual_network_details:
                vn_name = vn.get("vn_name")

                if self.have.get("l3_vn_name") and vn_name in self.have.get("l3_vn_name"):
                    missed_vn_list.append(vn_name)
                else:
                    verify_vn_list.append(vn_name)

            if verify_vn_list:
                self.status = "success"
                msg = (
                    "Requested layer3 Virtual Network(s) '{0}' have been successfully deleted from the Cisco "
                    "Catalyst Center and their deletion has been verified."
                ).format(verify_vn_list)
                self.log(msg, "INFO")
            else:
                msg = (
                    "Playbook's input does not match with Cisco Catalyst Center, indicating that layer3 Virtual"
                    "  Network(s) '{0}' deletion task may not have executed successfully."
                ).format(missed_vn_list)
                self.log(msg, "INFO")

        # Verify the deletion of Anycast gateway from the Cisco Catalyst Center
        anycast_gateways = config.get("anycast_gateways")
        if anycast_gateways:
            verify_anycast_list, missed_anycast_list = [], []
            for anycast in anycast_gateways:
                vn_name = anycast.get("vn_name")
                ip_pool_name = anycast.get("ip_pool_name")
                site_name = anycast.get("fabric_site_location").get("site_name_hierarchy")
                site_id = self.get_site_id(site_name)
                fabric_type = anycast.get("fabric_site_location").get("fabric_type")

                if fabric_type == "fabric_site":
                    fabric_id = self.get_fabric_site_id(site_name, site_id)
                else:
                    fabric_id = self.get_fabric_zone_id(site_name, site_id)

                # Collect the gateway id with combination of vn_name, ip_pool_name and fabric id
                unique_anycast = vn_name + "_" + ip_pool_name + "_" + site_name
                anycast_details_in_ccc = self.get_anycast_gateway_details(vn_name, ip_pool_name, fabric_id)

                if not anycast_details_in_ccc:
                    verify_anycast_list.append(unique_anycast)
                    continue
                missed_anycast_list.append(unique_anycast)

            if verify_anycast_list:
                self.status = "success"
                msg = (
                    "Requested Anycast Gateway(s) '{0}' have been successfully deleted from the Cisco "
                    "Catalyst Center and their deletion has been verified."
                ).format(verify_anycast_list)
                self.log(msg, "INFO")
            else:
                msg = (
                    "Playbook's input does not match with Cisco Catalyst Center, indicating that Anycast "
                    " Gateway(s) '{0}' deletion task may not have executed successfully."
                ).format(missed_anycast_list)
                self.log(msg, "INFO")

        return self


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
                    'config_verify': {'type': 'bool', "default": False},
                    'dnac_api_task_timeout': {'type': 'int', "default": 1200},
                    'dnac_task_poll_interval': {'type': 'int', "default": 2},
                    'config': {'required': True, 'type': 'list', 'elements': 'dict'},
                    'state': {'default': 'merged', 'choices': ['merged', 'deleted']}
                    }

    module = AnsibleModule(argument_spec=element_spec,
                           supports_check_mode=False)

    ccc_virtual_network = VirtualNetwork(module)
    state = ccc_virtual_network.params.get("state")

    if state not in ccc_virtual_network.supported_states:
        ccc_virtual_network.status = "invalid"
        ccc_virtual_network.msg = "State {0} is invalid".format(state)
        ccc_virtual_network.check_return_status()

    ccc_virtual_network.validate_input().check_return_status()
    config_verify = ccc_virtual_network.params.get("config_verify")

    for config in ccc_virtual_network.validated_config:
        ccc_virtual_network.reset_values()
        ccc_virtual_network.get_want(config).check_return_status()
        ccc_virtual_network.get_have(config).check_return_status()
        ccc_virtual_network.get_diff_state_apply[state](config).check_return_status()
        if config_verify:
            ccc_virtual_network.verify_diff_state_apply[state](config).check_return_status()

    # Invoke the API to check the status and log the output of each fabric vlan(s), virtual network(s)
    # and anycast gateways update on the console.
    ccc_virtual_network.update_fabric_vlan_vn_anycast_gateway_messages().check_return_status()

    module.exit_json(**ccc_virtual_network.result)


if __name__ == '__main__':
    main()
