#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright (c) 2024, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

"""Ansible module to generate YAML playbook for User and Role Management in Cisco Catalyst Center."""
from __future__ import absolute_import, division, print_function

__metaclass__ = type
__author__ = "Priyadharshini B, Madhan Sankaranarayanan"

DOCUMENTATION = r"""
---
module: brownfield_user_role_playbook_generator
short_description: Generate YAML playbook for 'user_role_workflow_manager' module.
description:
- Generates YAML configurations compatible with the `user_role_workflow_manager`
  module, reducing the effort required to manually create Ansible playbooks and
  enabling programmatic modifications.
- The YAML configurations generated represent the users and roles configured on
  the Cisco Catalyst Center.
version_added: 6.31.0
extends_documentation_fragment:
- cisco.dnac.workflow_manager_params
author:
- Priyadharshini B (@pbalaku2)
- Madhan Sankaranarayanan (@madhansansel)
options:
  config_verify:
    description: Set to True to verify the Cisco Catalyst
      Center after applying the playbook config.
    type: bool
    default: false
  state:
    description: The desired state of Cisco Catalyst Center after module execution.
    type: str
    choices: [merged]
    default: merged
  config:
    description:
      - A list of filters for generating YAML playbook compatible with the `user_role_workflow_manager`
        module.
      - Filters specify which components to include in the YAML configuration file.
      - If "components_list" is specified, only those components are included, regardless of the filters.
    type: list
    elements: dict
    required: true
    suboptions:
      file_path:
        description:
          - Path where the YAML configuration file will be saved.
          - If not provided, the file will be saved in the current working directory with
            a default file name  "<module_name>_playbook_<DD_Mon_YYYY_HH_MM_SS_MS>.yml".
          - For example, "user_role_workflow_manager_playbook_22_Apr_2025_21_43_26_379.yml".
        type: str
      component_specific_filters:
        description:
          - Filters to specify which components to include in the YAML configuration
            file.
          - If "components_list" is specified, only those components are included,
            regardless of other filters.
        type: dict
        suboptions:
          components_list:
            description:
              - List of components to include in the YAML configuration file.
              - Valid values are
                - User Details "user_details"
                - Role Details "role_details"
              - If not specified, all components are included.
              - For example, ["user_details", "role_details"].
            type: list
            elements: str
          user_details:
            description:
              - User details to filter users by username, email, or role.
            type: list
            elements: dict
            suboptions:
              username:
                description:
                  - Username to filter users by username.
                type: str
              email:
                description:
                  - Email to filter users by email address.
                type: str
              role_name:
                description:
                  - Role name to filter users by assigned role.
                type: str
          role_details:
            description:
              - Role details to filter roles by role name.
            type: list
            elements: dict
            suboptions:
              role_name:
                description:
                  - Role name to filter roles by role name.
                type: str
requirements:
- dnacentersdk >= 2.7.2
- python >= 3.9
notes:
- SDK Methods used are
    - user_and_roles.UserandRoles.get_users_api
    - user_and_roles.UserandRoles.get_roles_api
- Paths used are
    - GET /dna/system/api/v1/user
    - GET /dna/system/api/v1/role
"""

EXAMPLES = r"""
- name: Generate YAML Configuration with File Path specified
  cisco.dnac.brownfield_user_role_playbook_generator:
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
      - file_path: "/tmp/catc_user_role_config.yaml"

- name: Generate YAML Configuration with specific user components only
  cisco.dnac.brownfield_user_role_playbook_generator:
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
      - file_path: "/tmp/catc_user_role_config.yaml"
        component_specific_filters:
          components_list: ["user_details"]

- name: Generate YAML Configuration with specific role components only
  cisco.dnac.brownfield_user_role_playbook_generator:
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
      - file_path: "/tmp/catc_user_role_config.yaml"
        component_specific_filters:
          components_list: ["role_details"]

- name: Generate YAML Configuration for users with username filter
  cisco.dnac.brownfield_user_role_playbook_generator:
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
      - file_path: "/tmp/catc_user_role_config.yaml"
        component_specific_filters:
          components_list: ["user_details"]
          user_details:
            - username: "testuser1"
            - username: "testuser2"

- name: Generate YAML Configuration for roles with role name filter
  cisco.dnac.brownfield_user_role_playbook_generator:
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
      - file_path: "/tmp/catc_user_role_config.yaml"
        component_specific_filters:
          components_list: ["role_details"]
          role_details:
            - role_name: "Custom-Admin-Role"
            - role_name: "Network-Operator-Role"

- name: Generate YAML Configuration for all components with no filters
  cisco.dnac.brownfield_user_role_playbook_generator:
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
      - file_path: "/tmp/catc_user_role_config.yaml"
        component_specific_filters:
          components_list: ["user_details", "role_details"]
"""

RETURN = r"""
# Case_1: Success Scenario
response_1:
  description: A dictionary with the response returned by the Cisco Catalyst Center
  returned: always
  type: dict
  sample: >
    {
      "msg": {
        "YAML config generation Task succeeded for module 'user_role_workflow_manager'.": {
            "file_path": "/Users/priyadharshini/Downloads/specific_userrole_details_info"
        }
    },
    "response": {
        "YAML config generation Task succeeded for module 'user_role_workflow_manager'.": {
            "file_path": "/Users/priyadharshini/Downloads/specific_userrole_details_info"
        }
    }
# Case_2: Error Scenario
response_2:
  description: A string with the response returned by the Cisco Catalyst Center
  returned: always
  type: list
  sample: >
    "msg": {
        "YAML config generation Task failed for module 'user_role_workflow_manager'.": {
            "file_path": "/Users/priyadharshini/Downloads/specific_userrole_details_info"
        }
    },
    "response": {
        "YAML config generation Task failed for module 'user_role_workflow_manager'.": {
            "file_path": "/Users/priyadharshini/Downloads/specific_userrole_details_info"
        }
    }
"""

from ansible.module_utils.basic import AnsibleModule
from ansible_collections.cisco.dnac.plugins.module_utils.brownfield_helper import (
    BrownFieldHelper,
)
from ansible_collections.cisco.dnac.plugins.module_utils.dnac import (
    DnacBase,
    validate_list_of_dicts,
)
import time
try:
    import yaml
    HAS_YAML = True
except ImportError:
    HAS_YAML = False
    yaml = None
from collections import OrderedDict


if HAS_YAML:
    class OrderedDumper(yaml.Dumper):
        def represent_dict(self, data):
            return self.represent_mapping("tag:yaml.org,2002:map", data.items())

    OrderedDumper.add_representer(OrderedDict, OrderedDumper.represent_dict)
else:
    OrderedDumper = None


class UserRolePlaybookGenerator(DnacBase, BrownFieldHelper):
    """
    A class for generating playbook files for user and role management configured in Cisco Catalyst Center using the GET APIs.
    """

    def __init__(self, module):
        """
        Initialize an instance of the class.
        Args:
            module: The module associated with the class instance.
        Returns:
            The method does not return a value.
        """
        self.supported_states = ["merged"]
        super().__init__(module)
        self.module_schema = self.user_role_workflow_manager_mapping()
        self.module_name = "user_role_workflow_manager"

    def validate_input(self):
        """
        Validates the input configuration parameters for the playbook.
        Returns:
            object: An instance of the class with updated attributes:
                self.msg: A message describing the validation result.
                self.status: The status of the validation (either "success" or "failed").
                self.validated_config: If successful, a validated version of the "config" parameter.
        """
        self.log("Starting validation of input configuration parameters.", "DEBUG")

        # Check if configuration is available
        if not self.config:
            self.status = "success"
            self.msg = "Configuration is not available in the playbook for validation"
            self.log(self.msg, "ERROR")
            return self

        # Expected schema for configuration parameters
        temp_spec = {
            "file_path": {"type": "str", "required": False},
            "component_specific_filters": {"type": "dict", "required": False},
            "global_filters": {"type": "dict", "required": False},
        }

        # Validate params
        valid_temp, invalid_params = validate_list_of_dicts(self.config, temp_spec)

        if invalid_params:
            self.msg = "Invalid parameters in playbook: {0}".format(invalid_params)
            self.set_operation_result("failed", False, self.msg, "ERROR")
            return self

        # Set the validated configuration and update the result with success status
        self.validated_config = valid_temp
        self.msg = "Successfully validated playbook configuration parameters using 'validated_input': {0}".format(
            str(valid_temp)
        )
        self.set_operation_result("success", False, self.msg, "INFO")
        return self

    def user_role_workflow_manager_mapping(self):
        """
        Constructs and returns a structured mapping for managing user and role elements.
        This mapping includes associated filters, temporary specification functions, API details,
        and fetch function references used in the user and role workflow orchestration process.

        Returns:
            dict: A dictionary with the following structure:
                - "network_elements": A nested dictionary where each key represents a component
                (e.g., 'user_details', 'role_details') and maps to:
                    - "filters": List of filter keys relevant to the component.
                    - "reverse_mapping_function": Reference to the function that generates temp specs for the component.
                    - "api_function": Name of the API to be called for the component.
                    - "api_family": API family name (e.g., 'user_and_roles').
                    - "get_function_name": Reference to the internal function used to retrieve the component data.
                - "global_filters": An empty list reserved for global filters applicable across all elements.
        """
        return {
            "network_elements": {
                "user_details": {
                    "filters": {
                        "username": {"type": "str", "required": False},
                        "email": {"type": "str", "required": False},
                        "role_name": {"type": "str", "required": False},
                    },
                    "reverse_mapping_function": self.user_details_reverse_mapping_function,
                    "api_function": "get_users_api",
                    "api_family": "user_and_roles",
                    "get_function_name": self.get_users,
                },
                "role_details": {
                    "filters": {
                        "role_name": {"type": "str", "required": False},
                    },
                    "reverse_mapping_function": self.role_details_reverse_mapping_function,
                    "api_function": "get_roles_api",
                    "api_family": "user_and_roles",
                    "get_function_name": self.get_roles,
                },
            },
            "global_filters": {},
        }

    def user_details_reverse_mapping_function(self, requested_features=None):
        """
        Returns the reverse mapping specification for user details.
        Args:
            requested_features (list, optional): List of specific features to include (not used for users).
        Returns:
            dict: A dictionary containing reverse mapping specifications for user details
        """
        self.log("Generating reverse mapping specification for user details", "DEBUG")
        return self.user_details_temp_spec()

    def role_details_reverse_mapping_function(self, requested_features=None):
        """
        Returns the reverse mapping specification for role details.
        Args:
            requested_features (list, optional): List of specific features to include (not used for roles).
        Returns:
            dict: A dictionary containing reverse mapping specifications for role details
        """
        self.log("Generating reverse mapping specification for role details", "DEBUG")
        return self.role_details_temp_spec()

    def transform_user_role_list(self, user_details):
        """
        Transforms user role list from role IDs to role names.

        Args:
            user_details (dict): User details containing roleList with role IDs.

        Returns:
            list: List of role names corresponding to the role IDs.
        """
        self.log("Transforming user role list for user: {0}".format(user_details.get("username")), "DEBUG")

        role_ids = user_details.get("roleList", [])
        if not role_ids:
            return []

        role_names = []
        for role_id in role_ids:
            # Get role name from role mapping (we need to fetch roles first)
            role_name = self.get_role_name_by_id(role_id)
            if role_name:
                role_names.append(role_name)

        return role_names

    def get_role_name_by_id(self, role_id):
        """
        Gets role name by role ID.

        Args:
            role_id (str): The role ID to lookup.

        Returns:
            str: The role name corresponding to the role ID.
        """
        try:
            # Cache roles if not already cached
            if not hasattr(self, '_role_cache'):
                self._role_cache = {}
                roles_response = self.dnac._exec(
                    family="user_and_roles",
                    function="get_roles_api",
                    op_modifies=False,
                )
                roles = roles_response.get("response", {}).get("roles", [])
                for role in roles:
                    self._role_cache[role.get("roleId")] = role.get("name")

            return self._role_cache.get(role_id, role_id)
        except Exception as e:
            self.log("Error getting role name for ID {0}: {1}".format(role_id, str(e)), "ERROR")
            return role_id

    def transform_role_resource_types(self, role_details):
        """
        Transforms role resource types into a more readable format for the playbook.

        Args:
            role_details (dict): Role details containing resourceTypes.

        Returns:
            dict: Transformed role permissions structure.
        """
        self.log("Transforming role resource types for role: {0}".format(role_details.get("name")), "DEBUG")

        resource_types = role_details.get("resourceTypes", [])
        if not resource_types:
            return {}

        # Initialize the structure for all categories
        transformed_permissions = {
            "assurance": {},
            "network_analytics": {},
            "network_design": {},
            "network_provision": {},
            "network_services": {},
            "platform": {},
            "security": {},
            "system": {},
            "utilities": {}
        }

        for resource in resource_types:
            resource_type = resource.get("type", "")
            operations = resource.get("operations", [])

            if resource_type == "System.Basic":
                self.log("Skipping System.Basic from playbook generation", "DEBUG")
                continue

            # Map operations to permission level
            if not operations:
                permission = "deny"
            elif len(operations) == 1 and "gRead" in operations:
                permission = "read"
            else:
                permission = "write"

            # Parse resource type and create nested structure
            parts = resource_type.split(".")

            if len(parts) == 1:
                # Top-level category (e.g., "Assurance", "Network Design")
                category = self.normalize_category_name(parts[0])
                if category in transformed_permissions:
                    # Don't override if we already have subcategories
                    if not transformed_permissions[category]:
                        transformed_permissions[category]["overall"] = permission

            elif len(parts) == 2:
                # Category with subcategory (e.g., "Network Design.Advanced Network Settings")
                category = self.normalize_category_name(parts[0])
                subcategory = self.normalize_subcategory_name(parts[1])

                if category in transformed_permissions:
                    transformed_permissions[category][subcategory] = permission

            elif len(parts) == 3:
                # Nested subcategory (e.g., "Network Provision.Inventory Management.Device Configuration")
                category = self.normalize_category_name(parts[0])
                parent_subcategory = self.normalize_subcategory_name(parts[1])
                nested_subcategory = self.normalize_subcategory_name(parts[2])

                if category in transformed_permissions:
                    # Create nested structure
                    if parent_subcategory not in transformed_permissions[category]:
                        transformed_permissions[category][parent_subcategory] = {}
                    elif not isinstance(transformed_permissions[category][parent_subcategory], dict):
                        # If it was a simple permission, convert to dict
                        transformed_permissions[category][parent_subcategory] = {}

                    transformed_permissions[category][parent_subcategory][nested_subcategory] = permission

        # Convert to the expected list format for YAML generation
        final_structure = {}
        for category, permissions in transformed_permissions.items():
            if permissions:
                if category == "platform" and not permissions:
                    # Handle empty platform case
                    final_structure[category] = [{}]
                else:
                    # Handle nested inventory_management structure
                    if category == "network_provision" and "inventory_management" in permissions:
                        inventory_mgmt = permissions["inventory_management"]
                        if isinstance(inventory_mgmt, dict):
                            # Convert inventory_management to list format
                            permissions["inventory_management"] = [inventory_mgmt]

                    final_structure[category] = [permissions]
            else:
                # Empty category
                final_structure[category] = [{}]

        return final_structure

    def normalize_category_name(self, category):
        """
        Normalizes category names to match expected format.

        Args:
            category (str): Original category name from API.

        Returns:
            str: Normalized category name.
        """
        category_mapping = {
            "Assurance": "assurance",
            "Network Analytics": "network_analytics",
            "Network Design": "network_design",
            "Network Provision": "network_provision",
            "Network Services": "network_services",
            "Platform": "platform",
            "Security": "security",
            "System": "system",
            "Utilities": "utilities"
        }
        return category_mapping.get(category, category.lower().replace(" ", "_"))

    def normalize_subcategory_name(self, subcategory):
        """
        Normalizes subcategory names to match expected format.

        Args:
            subcategory (str): Original subcategory name from API.

        Returns:
            str: Normalized subcategory name.
        """
        # Handle specific mappings
        name_mapping = {
            "Monitoring and Troubleshooting": "monitoring_and_troubleshooting",
            "Monitoring Settings": "monitoring_settings",
            "Troubleshooting Tools": "troubleshooting_tools",
            "Data Access": "data_access",
            "Advanced Network Settings": "advanced_network_settings",
            "Image Repository": "image_repository",
            "Network Hierarchy": "network_hierarchy",
            "Network Profiles": "network_profiles",
            "Network Settings": "network_settings",
            "Virtual Network": "virtual_network",
            "Compliance": "compliance",
            "Inventory Management": "inventory_management",
            "Device Configuration": "device_configuration",
            "Discovery": "discovery",
            "Network Device": "network_device",
            "Port Management": "port_management",
            "Topology": "topology",
            "Network Telemetry": "network_telemetry",
            "PnP": "pnp",
            "Provision": "provision",
            "App Hosting": "app_hosting",
            "Bonjour": "bonjour",
            "Stealthwatch": "stealthwatch",
            "Umbrella": "umbrella",
            "Group-Based Policy": "group_based_policy",
            "IP Based Access Control": "ip_based_access_control",
            "Security Advisories": "security_advisories",
            "Machine Reasoning": "machine_reasoning",
            "System Management": "system_management",
            "Basic": "basic",
            "Event Viewer": "event_viewer",
            "Network Reasoner": "network_reasoner",
            "Scheduler": "scheduler",
            "Search": "search"
        }

        return name_mapping.get(subcategory, subcategory.lower().replace(" ", "_").replace("-", "_"))

    def role_details_temp_spec(self):
        """
        Constructs a temporary specification for role details, defining the structure and types of attributes
        that will be used in the YAML configuration file.

        Returns:
            OrderedDict: An ordered dictionary defining the structure of role detail attributes.
        """
        self.log("Generating temporary specification for role details.", "DEBUG")
        role_details = OrderedDict({
            "role_name": {"type": "str", "source_key": "name"},
            "description": {"type": "str", "source_key": "description"},
            # Transform resource types into structured permissions
            "assurance": {
                "type": "list",
                "special_handling": True,
                "transform": lambda x: self.transform_role_resource_types(x).get("assurance", [{}]),
            },
            "network_analytics": {
                "type": "list",
                "special_handling": True,
                "transform": lambda x: self.transform_role_resource_types(x).get("network_analytics", [{}]),
            },
            "network_design": {
                "type": "list",
                "special_handling": True,
                "transform": lambda x: self.transform_role_resource_types(x).get("network_design", [{}]),
            },
            "network_provision": {
                "type": "list",
                "special_handling": True,
                "transform": lambda x: self.transform_role_resource_types(x).get("network_provision", [{}]),
            },
            "network_services": {
                "type": "list",
                "special_handling": True,
                "transform": lambda x: self.transform_role_resource_types(x).get("network_services", [{}]),
            },
            "platform": {
                "type": "list",
                "special_handling": True,
                "transform": lambda x: self.transform_role_resource_types(x).get("platform", [{}]),
            },
            "security": {
                "type": "list",
                "special_handling": True,
                "transform": lambda x: self.transform_role_resource_types(x).get("security", [{}]),
            },
            "system": {
                "type": "list",
                "special_handling": True,
                "transform": lambda x: self.transform_role_resource_types(x).get("system", [{}]),
            },
            "utilities": {
                "type": "list",
                "special_handling": True,
                "transform": lambda x: self.transform_role_resource_types(x).get("utilities", [{}]),
            },
        })
        return role_details

    def user_details_temp_spec(self):
        """
        Constructs a temporary specification for user details, defining the structure and types of attributes
        that will be used in the YAML configuration file.

        Returns:
            OrderedDict: An ordered dictionary defining the structure of user detail attributes.
        """
        self.log("Generating temporary specification for user details.", "DEBUG")
        user_details = OrderedDict({
            "username": {"type": "str", "source_key": "username"},
            "first_name": {"type": "str", "source_key": "firstName"},
            "last_name": {"type": "str", "source_key": "lastName"},
            "email": {"type": "str", "source_key": "email"},
            "role_list": {
                "type": "list",
                "special_handling": True,
                "transform": self.transform_user_role_list,
            },
        })
        return user_details

    def role_details_temp_spec(self):
        """
        Constructs a temporary specification for role details, defining the structure and types of attributes
        that will be used in the YAML configuration file.

        Returns:
            OrderedDict: An ordered dictionary defining the structure of role detail attributes.
        """
        self.log("Generating temporary specification for role details.", "DEBUG")
        role_details = OrderedDict({
            "role_name": {"type": "str", "source_key": "name"},
            "description": {"type": "str", "source_key": "description"},
            # Transform resource types into structured permissions
            "assurance": {
                "type": "list",
                "special_handling": True,
                "transform": lambda x: self.transform_role_resource_types(x).get("assurance", [{}]),
            },
            "network_analytics": {
                "type": "list",
                "special_handling": True,
                "transform": lambda x: self.transform_role_resource_types(x).get("network_analytics", [{}]),
            },
            "network_design": {
                "type": "list",
                "special_handling": True,
                "transform": lambda x: self.transform_role_resource_types(x).get("network_design", [{}]),
            },
            "network_provision": {
                "type": "list",
                "special_handling": True,
                "transform": lambda x: self.transform_role_resource_types(x).get("network_provision", [{}]),
            },
            "network_services": {
                "type": "list",
                "special_handling": True,
                "transform": lambda x: self.transform_role_resource_types(x).get("network_services", [{}]),
            },
            "platform": {
                "type": "list",
                "special_handling": True,
                "transform": lambda x: self.transform_role_resource_types(x).get("platform", [{}]),
            },
            "security": {
                "type": "list",
                "special_handling": True,
                "transform": lambda x: self.transform_role_resource_types(x).get("security", [{}]),
            },
            "system": {
                "type": "list",
                "special_handling": True,
                "transform": lambda x: self.transform_role_resource_types(x).get("system", [{}]),
            },
            "utilities": {
                "type": "list",
                "special_handling": True,
                "transform": lambda x: self.transform_role_resource_types(x).get("utilities", [{}]),
            },
        })
        return role_details

    def get_users(self, network_element, filters):
        """
        Retrieves user details based on the provided network element and component-specific filters.

        Args:
            network_element (dict): A dictionary containing the API family and function for retrieving users.
            filters (dict): A dictionary containing global_filters and component_specific_filters.

        Returns:
            dict: A dictionary containing the modified details of users.
        """
        self.log(
            "Starting to retrieve users with network element: {0} and filters: {1}".format(
                network_element, filters
            ),
            "DEBUG",
        )

        component_specific_filters = filters.get("component_specific_filters", {})
        user_filters = component_specific_filters.get("user_details", [])

        final_users = []
        api_family = network_element.get("api_family")
        api_function = network_element.get("api_function")

        self.log(
            "Getting users using family '{0}' and function '{1}'.".format(
                api_family, api_function
            ),
            "INFO",
        )

        try:
            # Get all users first
            response = self.dnac._exec(
                family=api_family,
                function=api_function,
                op_modifies=False,
                params={"invoke_source": "external"},
            )
            users = response.get("response", {}).get("users", [])
            self.log("Retrieved {0} users from Catalyst Center".format(len(users)), "INFO")

            if user_filters:
                filtered_users = []
                for filter_param in user_filters:
                    for user in users:
                        match = True
                        for key, value in filter_param.items():
                            if key == "username" and user.get("username", "").lower() != value.lower():
                                match = False
                                break
                            elif key == "email" and user.get("email", "") != value:
                                match = False
                                break
                            elif key == "role_name":
                                user_role_names = self.transform_user_role_list(user)
                                if value not in user_role_names:
                                    match = False
                                    break

                        if match and user not in filtered_users:
                            filtered_users.append(user)

                final_users = filtered_users
            else:
                final_users = users

        except Exception as e:
            self.log("Error retrieving users: {0}".format(str(e)), "ERROR")
            self.fail_and_exit("Failed to retrieve users from Catalyst Center")

        # Modify user details using temp_spec
        user_details_temp_spec = self.user_details_temp_spec()
        user_details = self.modify_parameters(user_details_temp_spec, final_users)

        modified_user_details = {"user_details": user_details}
        self.log("Modified user details: {0}".format(modified_user_details), "INFO")

        return modified_user_details

    def get_roles(self, network_element, filters):
        """
        Retrieves role details based on the provided network element and component-specific filters.

        Args:
            network_element (dict): A dictionary containing the API family and function for retrieving roles.
            filters (dict): A dictionary containing global_filters and component_specific_filters.

        Returns:
            dict: A dictionary containing the modified details of roles.
        """
        self.log(
            "Starting to retrieve roles with network element: {0} and filters: {1}".format(
                network_element, filters
            ),
            "DEBUG",
        )

        component_specific_filters = filters.get("component_specific_filters", {})
        role_filters = component_specific_filters.get("role_details", [])

        final_roles = []
        api_family = network_element.get("api_family")
        api_function = network_element.get("api_function")

        self.log(
            "Getting roles using family '{0}' and function '{1}'.".format(
                api_family, api_function
            ),
            "INFO",
        )

        try:
            # Get all roles
            response = self.dnac._exec(
                family=api_family,
                function=api_function,
                op_modifies=False,
            )
            roles = response.get("response", {}).get("roles", [])
            self.log("Retrieved {0} roles from Catalyst Center".format(len(roles)), "INFO")

            if role_filters:
                filtered_roles = []
                for filter_param in role_filters:
                    for role in roles:
                        # Skip default and system roles
                        role_type = role.get("type", "").lower()
                        if role_type in ["default", "system"]:
                            self.log("Skipping {0} role: {1}".format(role_type, role.get("name")), "DEBUG")
                            continue

                        match = True
                        for key, value in filter_param.items():
                            if key == "role_name" and role.get("name", "") != value:
                                match = False
                                break

                        if match and role not in filtered_roles:
                            filtered_roles.append(role)

                final_roles = filtered_roles
            else:
                # Exclude system default roles and roles with type "default" or "system"
                final_roles = []
                for role in roles:
                    role_name = role.get("name", "")
                    role_type = role.get("type", "").lower()

                    # Skip system default roles by name
                    if (
                        role_name.startswith("SUPER-ADMIN") or
                        role_name.startswith("NETWORK-ADMIN") or
                        role_name.startswith("OBSERVER")
                    ):
                        self.log("Skipping system default role: {0}".format(role_name), "DEBUG")
                        continue

                    # Skip roles with type "default" or "system"
                    if role_type in ["default", "system"]:
                        self.log("Skipping {0} role: {1}".format(role_type, role_name), "DEBUG")
                        continue

                    final_roles.append(role)

        except Exception as e:
            self.log("Error retrieving roles: {0}".format(str(e)), "ERROR")
            self.fail_and_exit("Failed to retrieve roles from Catalyst Center")

        # Modify role details using temp_spec
        role_details_temp_spec = self.role_details_temp_spec()
        role_details = self.modify_parameters(role_details_temp_spec, final_roles)

        modified_role_details = {"role_details": role_details}
        self.log("Modified role details: {0}".format(modified_role_details), "INFO")

        return modified_role_details

    def yaml_config_generator(self, yaml_config_generator):
        """
        Generates a YAML configuration file based on the provided parameters.
        This function retrieves user and role details using component-specific filters, processes the data,
        and writes the YAML content to a specified file.

        Args:
            yaml_config_generator (dict): Contains file_path and component_specific_filters.

        Returns:
            self: The current instance with the operation result and message updated.
        """
        self.log(
            "Starting YAML config generation with parameters: {0}".format(
                yaml_config_generator
            ),
            "DEBUG",
        )

        file_path = yaml_config_generator.get("file_path")
        if not file_path:
            self.log("No file_path provided by user, generating default filename", "DEBUG")
            file_path = self.generate_filename()
        else:
            self.log("Using user-provided file_path: {0}".format(file_path), "DEBUG")

        self.log("YAML configuration file path determined: {0}".format(file_path), "DEBUG")

        self.log("File path determined: {0}".format(file_path), "DEBUG")

        component_specific_filters = (
            yaml_config_generator.get("component_specific_filters") or {}
        )
        self.log(
            "Component-specific filters: {0}".format(component_specific_filters),
            "DEBUG",
        )

        # Retrieve the supported network elements for the module
        module_supported_network_elements = self.module_schema.get("network_elements", {})
        components_list = component_specific_filters.get(
            "components_list", list(module_supported_network_elements.keys())
        )
        self.log("Components to process: {0}".format(components_list), "DEBUG")

        # Create the structured configuration
        config_dict = {}

        for component in components_list:
            network_element = module_supported_network_elements.get(component)
            if not network_element:
                self.log(
                    "Skipping unsupported network element: {0}".format(component),
                    "WARNING",
                )
                continue

            filters = {
                "global_filters": yaml_config_generator.get("global_filters", {}),
                "component_specific_filters": component_specific_filters
            }

            operation_func = network_element.get("get_function_name")
            if callable(operation_func):
                details = operation_func(network_element, filters)
                self.log(
                    "Details retrieved for {0}: {1}".format(component, details), "DEBUG"
                )

                # Add the component data to the config dictionary
                if component in details and details[component]:
                    config_dict[component] = details[component]

        if not config_dict:
            self.msg = "No users or roles found to process for module '{0}'. Verify input filters or configuration.".format(
                self.module_name
            )
            self.set_operation_result("success", False, self.msg, "INFO")
            return self

        final_dict = {"config": config_dict}
        self.log("Final dictionary created: {0}".format(final_dict), "DEBUG")

        if self.write_dict_to_yaml(final_dict, file_path):
            self.msg = {
                "YAML config generation Task succeeded for module '{0}'.".format(
                    self.module_name
                ): {"file_path": file_path}
            }
            self.set_operation_result("success", True, self.msg, "INFO")
        else:
            self.msg = {
                "YAML config generation Task failed for module '{0}'.".format(
                    self.module_name
                ): {"file_path": file_path}
            }
            self.set_operation_result("failed", True, self.msg, "ERROR")

        return self

    def get_want(self, config, state):
        """
        Creates parameters for API calls based on the specified state.

        Args:
            config (dict): The configuration data for the user/role elements.
            state (str): The desired state ('merged').
        """
        self.log(
            "Creating Parameters for API Calls with state: {0}".format(state), "INFO"
        )

        self.validate_params(config)

        component_specific_filters = config.get("component_specific_filters", {})
        components_list = component_specific_filters.get("components_list", [])

        if components_list:
            # Define allowed components
            allowed_components = ["user_details", "role_details"]
            invalid_components = []

            # Check each component in the list
            for component in components_list:
                if component not in allowed_components:
                    invalid_components.append(component)

            # If invalid components found, return error
            if invalid_components:
                self.msg = (
                    "Invalid components found in components_list: {0}. "
                    "Only the following components are allowed: {1}. "
                    "Please remove the invalid components and try again.".format(
                        invalid_components, allowed_components
                    )
                )
                self.set_operation_result("failed", True, self.msg, "ERROR")

        want = {}
        want["yaml_config_generator"] = config
        self.log(
            "yaml_config_generator added to want: {0}".format(
                want["yaml_config_generator"]
            ),
            "INFO",
        )

        self.want = want
        self.log("Desired State (want): {0}".format(str(self.want)), "INFO")
        self.msg = "Successfully collected all parameters from the playbook for User Role operations."
        self.status = "success"
        return self

    def get_diff_merged(self):
        """
        Executes the merge operations for user and role configurations in the Cisco Catalyst Center.
        """
        start_time = time.time()
        self.log("Starting 'get_diff_merged' operation.", "DEBUG")

        operations = [
            (
                "yaml_config_generator",
                "YAML Config Generator",
                self.yaml_config_generator,
            )
        ]

        # Iterate over operations and process them
        self.log("Beginning iteration over defined operations for processing.", "DEBUG")
        for index, (param_key, operation_name, operation_func) in enumerate(
            operations, start=1
        ):
            self.log(
                "Iteration {0}: Checking parameters for {1} operation with param_key '{2}'.".format(
                    index, operation_name, param_key
                ),
                "DEBUG",
            )
            params = self.want.get(param_key)
            if params:
                self.log(
                    "Iteration {0}: Parameters found for {1}. Starting processing.".format(
                        index, operation_name
                    ),
                    "INFO",
                )
                operation_func(params).check_return_status()
            else:
                self.log(
                    "Iteration {0}: No parameters found for {1}. Skipping operation.".format(
                        index, operation_name
                    ),
                    "WARNING",
                )

        end_time = time.time()
        self.log(
            "Completed 'get_diff_merged' operation in {0:.2f} seconds.".format(
                end_time - start_time
            ),
            "DEBUG",
        )

        return self


def main():
    """main entry point for module execution"""
    # Define the specification for the module's arguments
    element_spec = {
        "dnac_host": {"required": True, "type": "str"},
        "dnac_port": {"type": "str", "default": "443"},
        "dnac_username": {"type": "str", "default": "admin", "aliases": ["user"]},
        "dnac_password": {"type": "str", "no_log": True},
        "dnac_verify": {"type": "bool", "default": True},
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
        "state": {"default": "merged", "choices": ["merged"]},
    }

    # Initialize the Ansible module with the provided argument specifications
    module = AnsibleModule(argument_spec=element_spec, supports_check_mode=True)

    # Initialize the UserRolePlaybookGenerator object with the module
    ccc_user_role_playbook_generator = UserRolePlaybookGenerator(module)

    # Check version compatibility
    if (
        ccc_user_role_playbook_generator.compare_dnac_versions(
            ccc_user_role_playbook_generator.get_ccc_version(), "2.3.5.3"
        )
        < 0
    ):
        ccc_user_role_playbook_generator.msg = (
            "The specified version '{0}' does not support the YAML Playbook generation "
            "for User Role Management Module. Supported versions start from '2.3.5.3' onwards. "
            "Version '2.3.5.3' introduces APIs for retrieving user and role settings from "
            "the Catalyst Center".format(
                ccc_user_role_playbook_generator.get_ccc_version()
            )
        )
        ccc_user_role_playbook_generator.set_operation_result(
            "failed", False, ccc_user_role_playbook_generator.msg, "ERROR"
        ).check_return_status()

    # Get the state parameter from the provided parameters
    state = ccc_user_role_playbook_generator.params.get("state")

    # Check if the state is valid
    if state not in ccc_user_role_playbook_generator.supported_states:
        ccc_user_role_playbook_generator.status = "invalid"
        ccc_user_role_playbook_generator.msg = "State {0} is invalid".format(state)
        ccc_user_role_playbook_generator.check_return_status()

    # Validate the input parameters and check the return status
    ccc_user_role_playbook_generator.validate_input().check_return_status()
    config = ccc_user_role_playbook_generator.validated_config

    if len(config) == 1 and config[0].get("component_specific_filters") is None:
        ccc_user_role_playbook_generator.msg = (
            "No valid configurations found in the provided parameters."
        )
        ccc_user_role_playbook_generator.validated_config = [
            {
                'component_specific_filters': {
                    'components_list': ["user_details", "role_details"]
                }
            }
        ]

    # Iterate over the validated configuration parameters
    for config in ccc_user_role_playbook_generator.validated_config:
        ccc_user_role_playbook_generator.reset_values()
        ccc_user_role_playbook_generator.get_want(config, state).check_return_status()
        ccc_user_role_playbook_generator.get_diff_state_apply[state]().check_return_status()

    module.exit_json(**ccc_user_role_playbook_generator.result)


if __name__ == "__main__":
    main()
