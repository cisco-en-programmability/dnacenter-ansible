#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright (c) 2026, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

"""Ansible module to generate YAML playbook for User and Role Management in Cisco Catalyst Center."""
from __future__ import absolute_import, division, print_function

__metaclass__ = type
__author__ = "Priyadharshini B, Madhan Sankaranarayanan"

DOCUMENTATION = r"""
---
module: brownfield_user_role_playbook_generator
short_description: Generate YAML playbook for user and role management.
description:
- Generates YAML configurations compatible with the
  C(user_role_workflow_manager) module from existing Catalyst Center
  user and role configurations.
- Automates brownfield discovery by extracting current user accounts
  and custom role definitions into playbook format.
- Reduces manual effort in creating Ansible playbooks for user and
  role management operations.
- Supports selective extraction using filters for usernames, emails,
  and role names.
- Generated YAML can be directly used with C(user_role_workflow_manager)
  for configuration management and disaster recovery scenarios.
version_added: 6.44.0
extends_documentation_fragment:
- cisco.dnac.workflow_manager_params
author:
- Priyadharshini B (@pbalaku2)
- Madhan Sankaranarayanan (@madhansansel)
options:
  state:
    description:
    - The desired state for the module operation.
    - Only C(gathered) state is supported for extracting existing
      configurations from Catalyst Center.
    - The C(gathered) state retrieves user and role data via API
      and transforms it into YAML playbook format.
    type: str
    choices: [gathered]
    default: gathered
  config:
    description:
    - A list of configuration dictionaries specifying filters and
      output parameters for YAML playbook generation.
    - Each configuration item controls which components to extract
      and how to filter the data.
    - Supports filtering by username, email, role name, or component
      type to generate selective configurations.
    type: list
    elements: dict
    required: true
    suboptions:
      generate_all_configurations:
        description:
        - When set to C(true), automatically generates YAML
          configurations for all users and custom roles without
          requiring explicit filters.
        - Discovers all users and custom roles in Catalyst Center
          and extracts complete configurations.
        - System roles (SUPER-ADMIN, NETWORK-ADMIN, OBSERVER) and
          default roles are automatically excluded.
        - If enabled, the C(component_specific_filters) parameter
          becomes optional and defaults to all components.
        - A default filename is generated automatically if
          C(file_path) is not specified using pattern
          C(<module_name>_playbook_<YYYY-MM-DD_HH-MM-SS>.yml).
        - Useful for complete brownfield discovery, documentation,
          and disaster recovery planning.
        type: bool
        default: false
      file_path:
        description:
        - Absolute or relative path where the YAML configuration
          file will be saved.
        - If not provided, the file is saved in the current working
          directory with auto-generated filename.
        - Default filename pattern is
          C(<module_name>_playbook_<YYYY-MM-DD_HH-MM-SS>.yml).
        - For example,
          C(user_role_workflow_manager_playbook_2025-04-22_21-43-26.yml).
        - The directory path must exist and be writable.
        - Supports absolute paths (e.g., C(/tmp/config.yml)) and
          relative paths (e.g., C(./configs/users.yml)).
        type: str
      component_specific_filters:
        description:
        - Filters to specify which components to include in the
          YAML configuration file and criteria for filtering data.
        - If C(components_list) is specified, only those components
          are included in the output file.
        - If C(components_list) is not specified, all supported
          components (user_details and role_details) are included.
        - Each component can have specific filters to select subset
          of configurations based on attributes.
        type: dict
        suboptions:
          components_list:
            description:
            - List of component names to include in the YAML output.
            - Supported components are C(user_details) and
              C(role_details).
            - If not specified, all components are included by
              default.
            - Order in the list does not affect output structure.
            - Invalid component names will cause module to fail with
              error message listing allowed components.
            type: list
            elements: str
            choices: ["user_details", "role_details"]
          user_details:
            description:
            - List of filter parameter dictionaries to select
              specific users for inclusion in YAML output.
            - Multiple filter parameter sets use OR logic (any match
              includes the user).
            - Within a single filter parameter set, all criteria
              must match (AND logic).
            - If not specified, all users are included (subject to
              C(components_list) setting).
            - All filter values are case-insensitive.
            type: list
            elements: dict
            suboptions:
              username:
                description:
                - List of usernames to filter users by exact username
                  match.
                - Matching is case-insensitive.
                - Users with usernames in this list will be included
                  in output.
                - Example C(['testuser1', 'testuser2']) includes only
                  these two users.
                type: list
                elements: str
              email:
                description:
                - List of email addresses to filter users by exact
                  email match.
                - Matching is case-insensitive.
                - Users with email addresses in this list will be
                  included in output.
                - Example C(['user1@example.com', 'user2@example.com'])
                  filters by email.
                type: list
                elements: str
              role_name:
                description:
                - List of role names to filter users by assigned
                  role.
                - Matching is case-insensitive.
                - Users having any of the specified roles will be
                  included in output.
                - Role names should match exactly as defined in
                  Catalyst Center.
                - Example C(['SUPER-ADMIN-ROLE', 'Custom-Admin-Role'])
                  includes users with these roles.
                type: list
                elements: str
          role_details:
            description:
            - List of filter parameter dictionaries to select
              specific roles for inclusion in YAML output.
            - Multiple filter parameter sets use OR logic (any match
              includes the role).
            - If not specified, all custom roles are included
              (system roles are always excluded).
            - System roles (SUPER-ADMIN, NETWORK-ADMIN, OBSERVER)
              and roles with type 'default' or 'system' are
              automatically excluded.
            type: list
            elements: dict
            suboptions:
              role_name:
                description:
                - List of role names to filter roles by exact name
                  match.
                - Matching is case-sensitive for role names.
                - Only custom roles matching these names will be
                  included in output.
                - System and default roles are excluded regardless
                  of filter.
                - Example C(['Custom-Admin-Role',
                  'Network-Operator-Role']) includes only these
                  custom roles.
                type: list
                elements: str
requirements:
- dnacentersdk >= 2.7.2
- python >= 3.9
notes:
- Minimum supported Catalyst Center version is 2.3.5.3 which
  introduced user and role retrieval APIs.
- System roles (SUPER-ADMIN, NETWORK-ADMIN, OBSERVER) are
  automatically excluded from role_details output.
- Roles with type 'default' or 'system' are automatically excluded
  from output.
- Generated YAML file structure matches the input format expected by
  C(user_role_workflow_manager) module.
- Role permissions are transformed from API resourceTypes format to
  hierarchical permission structure with 9 categories.
- User role assignments are transformed from role IDs to role names
  for readability.
- Empty permission categories are represented as C([{}]) in output
  to maintain consistent YAML structure.
- All filter values are expected as lists of strings, even for
  single values.
- Check mode is supported but does not generate files (dry-run).

- SDK Methods used are
    - user_and_roles.UserandRoles.get_users_api
    - user_and_roles.UserandRoles.get_roles_api
- Paths used are
    - GET /dna/system/api/v1/user
    - GET /dna/system/api/v1/role

seealso:
- module: cisco.dnac.user_role_workflow_manager
  description: Module to manage users and roles using generated YAML.
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
    state: gathered
    config:
      - generate_all_configurations: true
        file_path: "/tmp/catc_user_role_config.yaml"

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
    state: gathered
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
    state: gathered
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
    state: gathered
    config:
      - file_path: "/tmp/catc_user_role_config.yaml"
        component_specific_filters:
          components_list: ["user_details"]
          user_details:
            - username: ["testuser1", "testuser2"]

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
    state: gathered
    config:
      - file_path: "/tmp/catc_user_role_config.yaml"
        component_specific_filters:
          components_list: ["role_details"]
          role_details:
            - role_name: ["Custom-Admin-Role", "Network-Operator-Role"]

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
    state: gathered
    config:
      - file_path: "/tmp/catc_user_role_config.yaml"
        component_specific_filters:
          components_list: ["user_details", "role_details"]

- name: Generate YAML for users with specific email addresses
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
    state: gathered
    config:
      - file_path: "/tmp/catc_users_by_email.yaml"
        component_specific_filters:
          components_list: ["user_details"]
          user_details:
            - email: ["admin@example.com", "operator@example.com"]

- name: Generate YAML for users with specific role assignments
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
    state: gathered
    config:
      - file_path: "/tmp/catc_admin_users.yaml"
        component_specific_filters:
          components_list: ["user_details"]
          user_details:
            - role_name: ["SUPER-ADMIN-ROLE", "Custom-Admin-Role"]

- name: Generate YAML with multiple filter criteria (OR logic)
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
    state: gathered
    config:
      - file_path: "/tmp/catc_filtered_users.yaml"
        component_specific_filters:
          components_list: ["user_details"]
          user_details:
            - username: ["testuser1"]
            - email: ["admin@example.com"]
"""

RETURN = r"""
# Case_1: Success Scenario
response_1:
  description: A dictionary with the response returned by the Cisco Catalyst Center
  returned: always
  type: dict
  sample: >
    {
      "msg": "YAML configuration file generated successfully for module 'user_role_workflow_manager'",
        "response": {
            "components_processed": 2,
            "components_skipped": 0,
            "configurations_count": 15,
            "file_path": "user_role_details/user_info",
            "message": "YAML configuration file generated successfully for module 'user_role_workflow_manager'",
            "status": "success"
        },
        "status": "success"
    }
# Case_2: Idempotency Scenario
response_2:
  description: A dictionary with the response returned by the Cisco Catalyst Center
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
        self.supported_states = ["gathered"]
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
            self.log(self.msg, "INFO")
            return self

        # Expected schema for configuration parameters
        temp_spec = {
            "file_path": {"type": "str", "required": False},
            "generate_all_configurations": {"type": "bool", "required": False, "default": False},
            "component_specific_filters": {"type": "dict", "required": False},
            "global_filters": {"type": "dict", "required": False},
        }

        allowed_keys = set(temp_spec.keys())

        self.log(
            "Expected parameter schema defined with {0} allowed parameter(s): {1}".format(
                len(allowed_keys), sorted(list(allowed_keys))
            ),
            "DEBUG"
        )

        # Validate that only allowed keys are present in the configuration
        for config_index, config_item in enumerate(self.config, start=1):
            self.log(
                "Validating configuration item {0}/{1} structure and parameters".format(
                    config_index, len(self.config)
                ),
                "DEBUG"
            )
            if not isinstance(config_item, dict):
                self.msg = "Configuration item must be a dictionary, got: {0}".format(type(config_item).__name__)
                self.set_operation_result("failed", False, self.msg, "ERROR")
                return self

            self.log(
                "Configuration item {0}/{1} is a valid dict with {2} parameter(s): {3}".format(
                    config_index, len(self.config), len(config_item), list(config_item.keys())
                ),
                "DEBUG"
            )

            # Check for invalid keys
            config_keys = set(config_item.keys())
            invalid_keys = config_keys - allowed_keys

            if invalid_keys:
                self.msg = (
                    "Invalid parameters found in playbook configuration: {0}. "
                    "Only the following parameters are allowed: {1}. "
                    "Please remove the invalid parameters and try again.".format(
                        list(invalid_keys), list(allowed_keys)
                    )
                )
                self.set_operation_result("failed", False, self.msg, "ERROR")
                return self

            self.log(
                "Configuration item {0}/{1} parameter key validation passed - all {2} "
                "parameter(s) are valid".format(
                    config_index, len(self.config), len(config_keys)
                ),
                "INFO"
            )

        self.validate_minimum_requirements(self.config)

        self.log(
            "Configuration structure and key validation completed successfully for all "
            "{0} configuration item(s)".format(len(self.config)),
            "INFO"
        )

        self.log("Validating configuration parameters against the expected schema: {0}".format(temp_spec), "DEBUG")

        # Validate params
        valid_temp, invalid_params = validate_list_of_dicts(self.config, temp_spec)

        if invalid_params:
            self.msg = "Invalid parameters in playbook: {0}".format(invalid_params)
            self.set_operation_result("failed", False, self.msg, "ERROR")
            return self

        self.log(
            "Schema validation passed - all {0} configuration item(s) conform to expected "
            "parameter types and structure".format(len(valid_temp)),
            "INFO"
        )

        # Set the validated configuration and update the result with success status
        self.validated_config = valid_temp
        self.msg = "Successfully validated playbook configuration parameters using 'validated_input': {0}".format(
            str(valid_temp)
        )
        for config_index, config_item in enumerate(self.validated_config, start=1):
            config_summary = {
                "has_file_path": "file_path" in config_item,
                "generate_all_configurations": config_item.get("generate_all_configurations", False),
                "has_component_specific_filters": "component_specific_filters" in config_item,
                "has_global_filters": "global_filters" in config_item,
            }
            self.log(
                "Validated configuration item {0}/{1} summary: {2}".format(
                    config_index, len(self.validated_config), config_summary
                ),
                "DEBUG"
            )

        # Success message
        success_msg = (
            "Successfully validated {0} playbook configuration item(s) using schema "
            "validation. All parameters conform to expected types and structure. "
            "Configuration is ready for processing.".format(len(self.validated_config))
        )

        self.set_operation_result("success", False, success_msg, "INFO")

        self.log(
            "Input parameter validation completed successfully. Validated {0} configuration "
            "item(s) across 5 validation steps (availability, structure, keys, minimum "
            "requirements, schema). Configuration is ready for user and role retrieval workflow.".format(
                len(self.validated_config)
            ),
            "INFO"
        )
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
        self.log("Constructing user and role workflow manager mapping.", "DEBUG")

        return {
            "network_elements": {
                "user_details": {
                    "filters": {
                        "username": {"type": "list", "required": False},
                        "email": {"type": "list", "required": False},
                        "role_name": {"type": "list", "required": False},
                    },
                    "reverse_mapping_function": self.user_details_reverse_mapping_function,
                    "api_function": "get_users_api",
                    "api_family": "user_and_roles",
                    "get_function_name": self.get_users,
                },
                "role_details": {
                    "filters": {
                        "role_name": {"type": "list", "required": False},
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

        if not user_details:
            self.log(
                "Transformation aborted - user_details parameter is empty or None. "
                "Cannot extract role information from empty user data.",
                "WARNING"
            )
            return []

        if not isinstance(user_details, dict):
            self.log(
                "Transformation aborted - user_details parameter has invalid type. "
                "Expected dict, got {0}. Cannot extract roleList from non-dictionary.".format(
                    type(user_details).__name__
                ),
                "ERROR"
            )
            return []

        username = user_details.get("username", "unknown")
        self.log(
            "User details validated successfully for user '{0}' - extracting roleList".format(
                username
            ),
            "DEBUG"
        )

        role_ids = user_details.get("roleList", [])
        if not isinstance(role_ids, list):
            self.log(
                "User '{0}' has invalid roleList type in user_details. Expected list, "
                "got {1}. Returning empty role list.".format(
                    username, type(role_ids).__name__
                ),
                "ERROR"
            )
            return []

        if not role_ids:
            self.log(
                "User '{0}' has empty roleList - no roles assigned to this user. "
                "Returning empty role name list.".format(username),
                "INFO"
            )
            return []

        self.log(
            "User '{0}' has {1} role ID(s) to transform: {2}".format(
                username, len(role_ids), role_ids
            ),
            "DEBUG"
        )

        role_names = []

        # Track transformation statistics
        successful_lookups = 0
        failed_lookups = 0
        cache_hits = 0
        cache_misses = 0

        # Check if role cache is available
        if hasattr(self, '_role_cache') and self._role_cache:
            cache_hits = len([rid for rid in role_ids if rid in self._role_cache])
            cache_misses = len(role_ids) - cache_hits

            self.log(
                "Role cache available for user '{0}' transformation - cache contains "
                "{1} role(s). Expected cache hits: {2}, cache misses: {3}".format(
                    username, len(self._role_cache), cache_hits, cache_misses
                ),
                "DEBUG"
            )
        else:
            self.log(
                "Role cache not yet initialized for user '{0}' transformation - will "
                "trigger cache population on first role lookup".format(username),
                "DEBUG"
            )

        # Transform each role ID to role name
        self.log(
            "Beginning role ID to role name transformation for user '{0}' - processing "
            "{1} role ID(s)".format(username, len(role_ids)),
            "DEBUG"
        )

        for role_index, role_id in enumerate(role_ids, start=1):
            self.log(
                "Processing role {0}/{1} for user '{2}': role_id='{3}'".format(
                    role_index, len(role_ids), username, role_id
                ),
                "DEBUG"
            )

            # Validate role ID format
            if not role_id:
                self.log(
                    "Role {0}/{1} for user '{2}' has empty role_id - skipping this role".format(
                        role_index, len(role_ids), username
                    ),
                    "WARNING"
                )
                failed_lookups += 1
                continue

            if not isinstance(role_id, str):
                self.log(
                    "Role {0}/{1} for user '{2}' has invalid role_id type. Expected str, "
                    "got {3}. Skipping this role.".format(
                        role_index, len(role_ids), username, type(role_id).__name__
                    ),
                    "WARNING"
                )
                failed_lookups += 1
                continue

            # Lookup role name using cached mapping
            self.log(
                "Looking up role name for role_id '{0}' (role {1}/{2} for user '{3}')".format(
                    role_id, role_index, len(role_ids), username
                ),
                "DEBUG"
            )

            role_name = self.get_role_name_by_id(role_id)

            if not role_name:
                self.log(
                    "Role name lookup failed for role_id '{0}' (role {1}/{2} for user "
                    "'{3}') - get_role_name_by_id returned empty value. Skipping this role.".format(
                        role_id, role_index, len(role_ids), username
                    ),
                    "WARNING"
                )
                failed_lookups += 1
                continue

            # Check if lookup returned role_id as fallback (not found in cache)
            if role_name == role_id:
                self.log(
                    "Role name lookup returned role_id as fallback for role_id '{0}' "
                    "(role {1}/{2} for user '{3}') - role not found in cache. "
                    "This may indicate a deleted or invalid role.".format(
                        role_id, role_index, len(role_ids), username
                    ),
                    "WARNING"
                )
                # Still count as successful since we have a value
                successful_lookups += 1
            else:
                self.log(
                    "Successfully resolved role_id '{0}' to role name '{1}' for role "
                    "{2}/{3} for user '{4}'".format(
                        role_id, role_name, role_index, len(role_ids), username
                    ),
                    "DEBUG"
                )
                successful_lookups += 1

            # Add role name to list
            role_names.append(role_name)
            self.log(
                "Added role name '{0}' to role list for user '{1}' (role {2}/{3})".format(
                    role_name, username, role_index, len(role_ids)
                ),
                "DEBUG"
            )

        if role_names:
            self.log(
                "Transformed role IDs {0} to role names {1} for user '{2}'".format(
                    role_ids, role_names, username
                ),
                "INFO"
            )
        else:
            self.log(
                "No valid role names resolved for user '{0}' after transformation. "
                "Original role IDs: {1}. This may indicate data inconsistency or "
                "deleted roles.".format(username, role_ids),
                "WARNING"
            )

        self.log(
            "Transformation completed for user '{0}' - returning {1} role name(s): {2}".format(
                username, len(role_names), role_names
            ),
            "DEBUG"
        )

        return role_names

    def get_role_name_by_id(self, role_id):
        """
        Retrieves the role name corresponding to a given role ID using an efficient
        caching mechanism.

        This method provides fast role ID-to-name lookups by maintaining an in-memory
        cache of all roles. On first invocation, it fetches all roles from Catalyst
        Center via API and caches the mapping. Subsequent lookups use the cached data,
        eliminating redundant API calls and improving performance.

        Args:
            role_id (str): The role ID to lookup.

        Returns:
            str: The role name corresponding to the role ID.
        """
        self.log(
            "Starting role name lookup for role_id '{0}' using cached role mapping".format(
                role_id
            ),
            "DEBUG"
        )

        if not role_id:
            self.log(
                "Role ID lookup received empty or None role_id parameter. Returning "
                "empty value as fallback.",
                "WARNING"
            )
            return role_id

        if not isinstance(role_id, str):
            self.log(
                "Role ID lookup received invalid type for role_id parameter. Expected "
                "str, got {0}. Returning original value as fallback.".format(
                    type(role_id).__name__
                ),
                "WARNING"
            )
            return role_id

        self.log(
            "Role ID parameter validated successfully: role_id='{0}' (type=str)".format(
                role_id
            ),
            "DEBUG"
        )

        try:
            cache_exists = hasattr(self, '_role_cache')
            if not cache_exists:
                self.log(
                    "Role cache not initialized - triggering cache population via API "
                    "call to retrieve all roles from Catalyst Center",
                    "INFO"
                )
            if not hasattr(self, '_role_cache'):
                self._role_cache = {}
                roles_response = self.dnac._exec(
                    family="user_and_roles",
                    function="get_roles_api",
                    op_modifies=False,
                )
                roles = roles_response.get("response", {}).get("roles", [])
                if not roles:
                    self.log(
                        "API response contains no roles - received empty roles list. "
                        "Cache will be empty. This may indicate no roles exist in "
                        "Catalyst Center or API access issues.",
                        "WARNING"
                    )
                else:
                    self.log(
                        "Received API response for {0} role(s) - "
                        "building role ID to name cache mapping".format(len(roles)),
                        "INFO"
                    )

                roles_cached = 0
                roles_skipped = 0

                for role_index, role in enumerate(roles, start=1):
                    role_id_key = role.get("roleId")
                    role_name_value = role.get("name")

                    # Validate role data
                    if not role_id_key:
                        self.log(
                            "Role {0}/{1} is missing roleId field - skipping cache entry. "
                            "Role data: {2}".format(role_index, len(roles), role),
                            "WARNING"
                        )
                        roles_skipped += 1
                        continue

                    if not role_name_value:
                        self.log(
                            "Role {0}/{1} with roleId '{2}' is missing name field - "
                            "skipping cache entry".format(
                                role_index, len(roles), role_id_key
                            ),
                            "WARNING"
                        )
                        roles_skipped += 1
                        continue

                    # Add to cache
                    self._role_cache[role_id_key] = role_name_value
                    roles_cached += 1

                    self.log(
                        "Cached role {0}/{1}: roleId='{2}' → name='{3}'".format(
                            role_index, len(roles), role_id_key, role_name_value
                        ),
                        "DEBUG"
                    )
            self.log(
                "Role name lookup completed with cache miss for role_id '{0}' - "
                "returning original role_id as fallback".format(role_id),
                "DEBUG"
            )
            return self._role_cache.get(role_id)

        except Exception as e:
            self.log("Error getting role name for ID {0}: {1}".format(role_id, str(e)), "ERROR")
            return role_id

    def transform_role_resource_types(self, role_details):
        """
        Transforms Catalyst Center role resource types into Ansible playbook-compatible
        permission structure.

        This transformation function converts the complex nested API response structure
        for role permissions into a hierarchical, human-readable format suitable for
        YAML playbook generation. It processes resource types, maps API operations to
        permission levels, and organizes permissions by category and subcategory.

        Args:
            role_details (dict): Role details containing resourceTypes.

        Returns:
            dict: Transformed role permissions structure.
        """
        self.log(
            "Starting transformation of role resource types to playbook-compatible "
            "permission structure for role '{0}'".format(
                role_details.get("name", "unknown")
            ),
            "DEBUG"
        )

        if not role_details:
            self.log(
                "Transformation aborted - role_details parameter is empty or None. "
                "Cannot extract resource types from empty role data.",
                "WARNING"
            )
            return {}

        if not isinstance(role_details, dict):
            self.log(
                "Transformation aborted - role_details parameter has invalid type. "
                "Expected dict, got {0}. Cannot extract resourceTypes from "
                "non-dictionary.".format(type(role_details).__name__),
                "ERROR"
            )
            return {}

        role_name = role_details.get("name", "unknown")

        self.log(
            "Role details validated successfully for role '{0}' - extracting "
            "resourceTypes".format(role_name),
            "DEBUG"
        )

        resource_types = role_details.get("resourceTypes", [])
        if resource_types is None:
            self.log(
                "Role '{0}' has resourceTypes=None in role_details. Treating as empty "
                "resource types - role has no permissions configured.".format(role_name),
                "WARNING"
            )
            resource_types = []

        if not isinstance(resource_types, list):
            self.log(
                "Role '{0}' has invalid resourceTypes type in role_details. Expected "
                "list, got {1}. Returning empty permissions structure.".format(
                    role_name, type(resource_types).__name__
                ),
                "ERROR"
            )
            return {}

        if not resource_types:
            self.log(
                "Role '{0}' has empty resourceTypes - no permissions configured for "
                "this role. Returning structure with all empty categories.".format(
                    role_name
                ),
                "INFO"
            )
        else:
            self.log(
                "Role '{0}' has {1} resource type(s) to transform".format(
                    role_name, len(resource_types)
                ),
                "DEBUG"
            )

        self.log(
            "Initializing permission structure with 9 standard categories for role "
            "'{0}'".format(role_name),
            "DEBUG"
        )

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

        self.log(
            "Initialized empty permission structure for categories: {0}".format(
                list(transformed_permissions.keys())
            ),
            "DEBUG"
        )

        # Track transformation statistics
        total_resources = len(resource_types)
        resources_processed = 0
        resources_skipped = 0
        system_basic_skipped = 0
        invalid_resources = 0

        # Process each resource type
        self.log(
            "Beginning resource type transformation for role '{0}' - processing {1} "
            "resource(s)".format(role_name, total_resources),
            "DEBUG"
        )

        for resource_index, resource in enumerate(resource_types, start=1):
            self.log(
                "Processing resource {0}/{1} for role '{2}'".format(
                    resource_index, total_resources, role_name
                ),
                "DEBUG"
            )

            if not isinstance(resource, dict):
                self.log(
                    "Resource {0}/{1} for role '{2}' has invalid type - expected dict, "
                    "got {3}. Skipping this resource.".format(
                        resource_index, total_resources, role_name,
                        type(resource).__name__
                    ),
                    "WARNING"
                )
                invalid_resources += 1
                resources_skipped += 1
                continue

            resource_type = resource.get("type", "")
            operations = resource.get("operations", [])

            self.log(
                "Resource {0}/{1} details: type='{2}', operations={3}".format(
                    resource_index, total_resources, resource_type, operations
                ),
                "DEBUG"
            )

            if resource_type == "System.Basic":
                self.log(
                    "Skipping System.Basic resource (resource {0}/{1}) from playbook "
                    "generation for role '{2}' - system basic permissions are not "
                    "configurable".format(resource_index, total_resources, role_name),
                    "DEBUG"
                )
                system_basic_skipped += 1
                resources_skipped += 1
                continue

            # Map operations to permission level
            if not operations:
                permission = "deny"
                self.log(
                    "Resource {0}/{1} ('{2}') has empty operations - mapped to "
                    "permission='deny'".format(
                        resource_index, total_resources, resource_type
                    ),
                    "DEBUG"
                )
            elif len(operations) == 1 and "gRead" in operations:
                permission = "read"
                self.log(
                    "Resource {0}/{1} ('{2}') has read-only operation ['gRead'] - "
                    "mapped to permission='read'".format(
                        resource_index, total_resources, resource_type
                    ),
                    "DEBUG"
                )
            else:
                permission = "write"
                self.log(
                    "Resource {0}/{1} ('{2}') has operations {3} - mapped to "
                    "permission='write'".format(
                        resource_index, total_resources, resource_type, operations
                    ),
                    "DEBUG"
                )

            # Parse resource type and create nested structure
            parts = resource_type.split(".")
            parts_count = len(parts)

            self.log(
                "Resource {0}/{1} ('{2}') parsed into {3} level(s): {4}".format(
                    resource_index, total_resources, resource_type, parts_count, parts
                ),
                "DEBUG"
            )

            # Handle different hierarchy levels
            if parts_count == 1:
                # Top-level category (e.g., "Assurance")
                category = self.normalize_category_name(parts[0])

                self.log(
                    "Resource {0}/{1}: Level 1 (category-only) - normalized '{2}' to "
                    "'{3}'".format(
                        resource_index, total_resources, parts[0], category
                    ),
                    "DEBUG"
                )

                if category in transformed_permissions:
                    # Don't override if we already have subcategories
                    if not transformed_permissions[category]:
                        transformed_permissions[category]["overall"] = permission
                        self.log(
                            "Set category '{0}' overall permission to '{1}' for "
                            "resource {2}/{3}".format(
                                category, permission, resource_index, total_resources
                            ),
                            "DEBUG"
                        )
                    else:
                        self.log(
                            "Category '{0}' already has subcategories - skipping "
                            "overall permission for resource {1}/{2}".format(
                                category, resource_index, total_resources
                            ),
                            "DEBUG"
                        )
                else:
                    self.log(
                        "Unknown category '{0}' encountered in resource {1}/{2} - "
                        "not in predefined category list".format(
                            category, resource_index, total_resources
                        ),
                        "WARNING"
                    )
                    resources_skipped += 1
                    continue

            elif parts_count == 2:
                # Category with subcategory (e.g., "Network Design.Advanced Settings")
                category = self.normalize_category_name(parts[0])
                subcategory = self.normalize_subcategory_name(parts[1])

                self.log(
                    "Resource {0}/{1}: Level 2 (category.subcategory) - normalized "
                    "'{2}.{3}' to '{4}.{5}'".format(
                        resource_index, total_resources, parts[0], parts[1],
                        category, subcategory
                    ),
                    "DEBUG"
                )

                if category in transformed_permissions:
                    transformed_permissions[category][subcategory] = permission
                    self.log(
                        "Set permission '{0}.{1}' = '{2}' for resource {3}/{4}".format(
                            category, subcategory, permission, resource_index,
                            total_resources
                        ),
                        "DEBUG"
                    )
                else:
                    self.log(
                        "Unknown category '{0}' encountered in resource {1}/{2}".format(
                            category, resource_index, total_resources
                        ),
                        "WARNING"
                    )
                    resources_skipped += 1
                    continue

            elif parts_count == 3:
                # Nested subcategory (e.g., "Network Provision.Inventory Mgmt.Device Config")
                category = self.normalize_category_name(parts[0])
                parent_subcategory = self.normalize_subcategory_name(parts[1])
                nested_subcategory = self.normalize_subcategory_name(parts[2])

                self.log(
                    "Resource {0}/{1}: Level 3 (category.parent.nested) - normalized "
                    "'{2}.{3}.{4}' to '{5}.{6}.{7}'".format(
                        resource_index, total_resources, parts[0], parts[1], parts[2],
                        category, parent_subcategory, nested_subcategory
                    ),
                    "DEBUG"
                )

                if category in transformed_permissions:
                    # Create nested structure
                    if parent_subcategory not in transformed_permissions[category]:
                        transformed_permissions[category][parent_subcategory] = {}
                        self.log(
                            "Created nested structure for '{0}.{1}' (resource {2}/{3})".format(
                                category, parent_subcategory, resource_index,
                                total_resources
                            ),
                            "DEBUG"
                        )
                    elif not isinstance(
                        transformed_permissions[category][parent_subcategory], dict
                    ):
                        # If it was a simple permission, convert to dict
                        old_value = transformed_permissions[category][parent_subcategory]
                        transformed_permissions[category][parent_subcategory] = {}
                        self.log(
                            "Converted '{0}.{1}' from simple permission '{2}' to "
                            "nested structure for resource {3}/{4}".format(
                                category, parent_subcategory, old_value,
                                resource_index, total_resources
                            ),
                            "DEBUG"
                        )

                    transformed_permissions[category][parent_subcategory][
                        nested_subcategory
                    ] = permission

                    self.log(
                        "Set nested permission '{0}.{1}.{2}' = '{3}' for resource "
                        "{4}/{5}".format(
                            category, parent_subcategory, nested_subcategory,
                            permission, resource_index, total_resources
                        ),
                        "DEBUG"
                    )
                else:
                    self.log(
                        "Unknown category '{0}' encountered in resource {1}/{2}".format(
                            category, resource_index, total_resources
                        ),
                        "WARNING"
                    )
                    resources_skipped += 1
                    continue
            else:
                self.log(
                    "Resource {0}/{1} has unexpected hierarchy depth ({2} levels): "
                    "'{3}'. Skipping this resource.".format(
                        resource_index, total_resources, parts_count, resource_type
                    ),
                    "WARNING"
                )
                invalid_resources += 1
                resources_skipped += 1
                continue

            # Successfully processed resource
            resources_processed += 1

        # Convert to the expected list format for YAML generation
        self.log(
            "Resource type transformation statistics for role '{0}': total={1}, "
            "processed={2}, skipped={3} (system_basic={4}, invalid={5})".format(
                role_name, total_resources, resources_processed, resources_skipped,
                system_basic_skipped, invalid_resources
            ),
            "INFO"
        )

        # Convert to the expected list format for YAML generation
        self.log(
            "Converting transformed permissions to list format for YAML compatibility "
            "for role '{0}'".format(role_name),
            "DEBUG"
        )

        final_structure = {}
        categories_with_permissions = 0
        empty_categories = 0

        for category, permissions in transformed_permissions.items():
            if permissions:
                if category == "platform" and not permissions:
                    # Handle empty platform case
                    final_structure[category] = [{}]
                    empty_categories += 1
                    self.log(
                        "Category '{0}' is empty - using [{{}}] format".format(category),
                        "DEBUG"
                    )
                else:
                    # Handle nested inventory_management structure
                    if category == "network_provision" and "inventory_management" in permissions:
                        inventory_mgmt = permissions["inventory_management"]
                        if isinstance(inventory_mgmt, dict):
                            # Convert inventory_management to list format
                            permissions["inventory_management"] = [inventory_mgmt]
                            self.log(
                                "Converted '{0}.inventory_management' to list format "
                                "for YAML compatibility".format(category),
                                "DEBUG"
                            )

                    final_structure[category] = [permissions]
                    categories_with_permissions += 1

                    if isinstance(permissions, dict):
                        permission_count = len(permissions)
                        self.log(
                            "Category '{0}' has {1} permission(s) configured".format(
                                category, permission_count
                            ),
                            "DEBUG"
                        )
            else:
                # Empty category
                final_structure[category] = [{}]
                empty_categories += 1
                self.log(
                    "Category '{0}' has no permissions - using [{{}}] format".format(
                        category
                    ),
                    "DEBUG"
                )
        self.log(
            "List format conversion completed for role '{0}': categories_with_permissions={1}, "
            "empty_categories={2}, total_categories={3}".format(
                role_name, categories_with_permissions, empty_categories,
                len(final_structure)
            ),
            "INFO"
        )

        self.log(
            "Transformation completed for role '{0}' - returning permission structure "
            "with {1} categories ({2} with permissions, {3} empty)".format(
                role_name, len(final_structure), categories_with_permissions,
                empty_categories
            ),
            "DEBUG"
        )

        return final_structure

    def normalize_category_name(self, category):
        """
        Normalizes Catalyst Center API category names to playbook-compatible snake_case format.

        This normalization function converts category names from the Catalyst Center API response
        format (Title Case with spaces) into standardized snake_case identifiers used in Ansible
        playbooks and YAML configurations.

        Args:
            category (str): Original category name from Catalyst Center API resourceTypes.
                Expected format: Title Case with spaces (e.g., "Network Design")
                Source: resourceTypes[].type field (first part before '.')

        Returns:
            str: Normalized category name in snake_case format.
                - If in mapping: Returns predefined snake_case name
                - If not in mapping: Returns lowercase with spaces→underscores
                Example: "Network Design" → "network_design"
        """
        self.log("Normalizing category name: {0}".format(category), "DEBUG")
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
        self.log("Normalizing subcategory name: {0}".format(subcategory), "DEBUG")
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
        self.log(
            "Temporary specification generation completed for role details. Specification "
            "ready for use in modify_parameters() to transform API response data into "
            "YAML playbook format. Total fields defined: {0}".format(len(role_details)),
            "DEBUG"
        )
        return role_details

    def user_details_temp_spec(self):
        """
        Constructs temporary specification for user details transformation to YAML format.

        Defines the structure and types of user attributes that will be extracted from
        Catalyst Center API responses and formatted for YAML playbook generation. This
        specification serves as a blueprint for the modify_parameters() function to
        transform raw API data into playbook-compatible structures.

        Returns:
            OrderedDict: An ordered dictionary defining the structure of user detail attributes.
        """
        self.log(
            "Starting generation of temporary specification for user details "
            "transformation to define structure and field mappings for YAML "
            "playbook generation",
            "DEBUG"
        )
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
        self.log(
            "Temporary specification generation completed for user details. "
            "Specification ready for use in modify_parameters() to transform API "
            "response data into YAML playbook format. Total fields defined: {0}".format(
                len(user_details)
            ),
            "DEBUG"
        )
        return user_details

    def get_users(self, network_element, filters):
        """
        Retrieves and transforms user details from Catalyst Center based on filters.

        Fetches user data via API, applies component-specific filters, and transforms
        the data into playbook-compatible format using user_details_temp_spec.

        Args:
            network_element (dict): API configuration containing:
                - api_family: SDK family name ("user_and_roles")
                - api_function: SDK method name ("get_users_api")

            filters (dict): Filter configuration containing:
                - component_specific_filters: User-specific filters
                    - user_details: List of filter parameter dicts
                        - username: List of usernames
                        - email: List of emails
                        - role_name: List of role names

        Returns:
            dict: Transformed user details ready for YAML generation.
            Structure:
            {
                "user_details": [
                    {
                        "username": "testuser1",
                        "first_name": "Test",
                        "last_name": "User",
                        "email": "test@example.com",
                        "role_list": ["SUPER-ADMIN-ROLE"]
                    },
                    ...
                ]
            }
        """
        self.log(
            "Starting to retrieve users with network element: {0} and filters: {1}".format(
                network_element, filters
            ),
            "DEBUG",
        )

        component_specific_filters = filters.get("component_specific_filters", {})
        user_filters = component_specific_filters.get("user_details", [])

        self.log(
            "Extracted component-specific filters for user_details: {0} filter "
            "parameter(s) defined".format(len(user_filters)),
            "DEBUG"
        )

        if user_filters:
            self.log(
                "User filters configuration: {0}".format(user_filters),
                "DEBUG"
            )
        else:
            self.log(
                "No user-specific filters provided - will retrieve all users from "
                "Catalyst Center",
                "INFO"
            )

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
            self.log(
                "Received API response for users retrieval - extracting users array "
                "from response",
                "DEBUG"
            )
            users = response.get("response", {}).get("users", [])

            self.log(
                "Successfully retrieved {0} total user(s) from Catalyst Center API".format(
                    len(users)
                ),
                "INFO"
            )

            if not users:
                self.log(
                    "API returned empty users list - no users exist in Catalyst Center "
                    "or API access restricted",
                    "WARNING"
                )

            if user_filters:
                self.log(
                    "Applying user-specific filters to {0} retrieved user(s) - "
                    "processing {1} filter parameter set(s)".format(
                        len(users), len(user_filters)
                    ),
                    "INFO"
                )
                filtered_users = []
                total_matches = 0

                for filter_index, filter_param in enumerate(user_filters, start=1):
                    self.log(
                        "Processing filter parameter set {0}/{1}: {2}".format(
                            filter_index, len(user_filters), filter_param
                        ),
                        "DEBUG"
                    )

                    filter_matches = 0

                    for user_index, user in enumerate(users, start=1):
                        match = True
                        username = user.get("username", "unknown")
                        self.log(
                            "Evaluating user {0}/{1} (username='{2}') against "
                            "filter set {3}/{4}".format(
                                user_index, len(users), username, filter_index,
                                len(user_filters)
                            ),
                            "DEBUG"
                        )
                        for key, value in filter_param.items():
                            if not isinstance(value, list):
                                self.msg = (
                                    "Invalid format for '{0}' in user_details filter. "
                                    "Expected list of strings, got {1}. All filter "
                                    "parameters must be provided as lists.".format(
                                        key, type(value).__name__
                                    )
                                )
                                self.set_operation_result(
                                    "failed", False, self.msg, "ERROR"
                                ).check_return_status()

                            value_list = [
                                v.lower() if isinstance(v, str) else str(v).lower()
                                for v in value
                            ]

                            self.log(
                                "Filter criterion '{0}' with {1} value(s) (normalized "
                                "to lowercase): {2}".format(key, len(value_list), value_list),
                                "DEBUG"
                            )

                            if key == "username":
                                user_username = user.get("username", "").lower()

                                if user_username not in value_list:
                                    self.log(
                                        "User '{0}' username '{1}' does not match filter "
                                        "values {2} - marking as non-match".format(
                                            username, user_username, value_list
                                        ),
                                        "DEBUG"
                                    )
                                    match = False
                                    break
                                else:
                                    self.log(
                                        "User '{0}' username matches filter - criterion "
                                        "satisfied".format(username),
                                        "DEBUG"
                                    )
                            elif key == "email":
                                user_email = user.get("email", "").lower()

                                if user_email not in value_list:
                                    self.log(
                                        "User '{0}' email '{1}' does not match filter "
                                        "values {2} - marking as non-match".format(
                                            username, user_email, value_list
                                        ),
                                        "DEBUG"
                                    )
                                    match = False
                                    break
                                else:
                                    self.log(
                                        "User '{0}' email matches filter - criterion "
                                        "satisfied".format(username),
                                        "DEBUG"
                                    )

                            elif key == "role_name":
                                self.log(
                                    "Transforming role IDs to role names for user '{0}' "
                                    "to check role_name filter".format(username),
                                    "DEBUG"
                                )

                                user_role_names = self.transform_user_role_list(user)
                                user_role_names_lower = [
                                    role.lower() for role in user_role_names
                                ]

                                self.log(
                                    "User '{0}' has roles: {1} (normalized: {2})".format(
                                        username, user_role_names, user_role_names_lower
                                    ),
                                    "DEBUG"
                                )
                                if not any(
                                    filter_role in user_role_names_lower
                                    for filter_role in value_list
                                ):
                                    self.log(
                                        "User '{0}' roles {1} do not match any filter "
                                        "values {2} - marking as non-match".format(
                                            username, user_role_names_lower, value_list
                                        ),
                                        "DEBUG"
                                    )
                                    match = False
                                    break
                                else:
                                    self.log(
                                        "User '{0}' has at least one matching role - "
                                        "criterion satisfied".format(username),
                                        "DEBUG"
                                    )

                        if match:
                            if user not in filtered_users:
                                filtered_users.append(user)
                                filter_matches += 1
                                total_matches += 1

                                self.log(
                                    "User '{0}' matched all criteria in filter set "
                                    "{1}/{2} - added to filtered list (total matches: {3})".format(
                                        username, filter_index, len(user_filters),
                                        total_matches
                                    ),
                                    "DEBUG"
                                )
                            else:
                                self.log(
                                    "User '{0}' already in filtered list - skipping "
                                    "duplicate".format(username),
                                    "DEBUG"
                                )

                    self.log(
                        "Filter set {0}/{1} resulted in {2} matching user(s)".format(
                            filter_index, len(user_filters), filter_matches
                        ),
                        "INFO"
                    )

                final_users = filtered_users

                self.log(
                    "User filtering completed - {0} user(s) matched out of {1} "
                    "total users retrieved (filtered out: {2})".format(
                        len(final_users), len(users), len(users) - len(final_users)
                    ),
                    "INFO"
                )
            else:
                final_users = users

                self.log(
                    "No filters applied - using all {0} retrieved user(s)".format(
                        len(final_users)
                    ),
                    "INFO"
                )

        except Exception as e:
            error_msg = (
                "Error retrieving users from Catalyst Center API. Exception type: {0}, "
                "Exception message: {1}. API call failed using family '{2}' and "
                "function '{3}'.".format(
                    type(e).__name__, str(e), api_family, api_function
                )
            )
            self.log(error_msg, "ERROR")
            self.fail_and_exit(
                "Failed to retrieve users from Catalyst Center. Please verify API "
                "connectivity and permissions."
            )

        # Modify user details using temp_spec
        user_details_temp_spec = self.user_details_temp_spec()
        self.log(
            "Transforming {0} user record(s) using modify_parameters() with "
            "user_details_temp_spec to generate playbook-compatible structure".format(
                len(final_users)
            ),
            "INFO"
        )
        user_details = self.modify_parameters(user_details_temp_spec, final_users)
        self.log(
            "Successfully transformed {0} user(s) into playbook format with fields: "
            "{1}".format(
                len(user_details), list(user_details_temp_spec.keys()) if user_details else []
            ),
            "INFO"
        )

        modified_user_details = {"user_details": user_details}
        self.log(
            "User retrieval and transformation completed successfully - returning "
            "{0} user detail(s) for YAML generation".format(len(user_details)),
            "INFO"
        )

        return modified_user_details

    def get_roles(self, network_element, filters):
        """
        Retrieves and transforms custom role details from Catalyst Center based on filters.

        Fetches role data via API, excludes system/default roles, applies filters, and
        transforms the data into playbook-compatible format using role_details_temp_spec.

        Args:
            network_element (dict): API configuration containing:
                - api_family: SDK family name ("user_and_roles")
                - api_function: SDK method name ("get_roles_api")

            filters (dict): Filter configuration containing:
                - component_specific_filters: Role-specific filters
                    - role_details: List of filter parameter dicts
                        - role_name: List of role names

        Returns:
            dict: Transformed role details ready for YAML generation.
            Structure:
            {
                "role_details": [
                    {
                        "role_name": "Custom-Admin-Role",
                        "description": "Custom administrator role",
                        "assurance": [{"overall": "write"}],
                        "network_design": [{"network_hierarchy": "read"}],
                        ...all 9 permission categories...
                    },
                    ...
                ]
            }
        """
        self.log(
            "Starting to retrieve roles with network element: {0} and filters: {1}".format(
                network_element, filters
            ),
            "DEBUG",
        )

        component_specific_filters = filters.get("component_specific_filters", {})
        role_filters = component_specific_filters.get("role_details", [])

        self.log(
            "Extracted component-specific filters for role_details: {0} filter "
            "parameter(s) defined".format(len(role_filters)),
            "DEBUG"
        )

        if role_filters:
            self.log(
                "Role filters configuration: {0}".format(role_filters),
                "DEBUG"
            )
        else:
            self.log(
                "No role-specific filters provided - will retrieve all custom roles "
                "from Catalyst Center (excluding system/default roles)",
                "INFO"
            )

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
            self.log(
                "Received API response for roles retrieval - extracting roles array "
                "from response",
                "DEBUG"
            )
            roles = response.get("response", {}).get("roles", [])

            self.log(
                "Successfully retrieved {0} total role(s) from Catalyst Center API "
                "(includes system and custom roles)".format(len(roles)),
                "INFO"
            )

            if not roles:
                self.log(
                    "API returned empty roles list - no roles exist in Catalyst Center "
                    "or API access restricted",
                    "WARNING"
                )

            if role_filters:
                self.log(
                    "Applying role-specific filters to {0} retrieved role(s) - "
                    "processing {1} filter parameter set(s). System/default roles "
                    "will be excluded automatically.".format(len(roles), len(role_filters)),
                    "INFO"
                )

                filtered_roles = []
                total_matches = 0
                system_roles_skipped = 0
                filtered_roles = []

                for filter_index, filter_param in enumerate(role_filters, start=1):
                    self.log(
                        "Processing filter parameter set {0}/{1}: {2}".format(
                            filter_index, len(role_filters), filter_param
                        ),
                        "DEBUG"
                    )
                    filter_matches = 0
                    for role_index, role in enumerate(roles, start=1):
                        role_name = role.get("name", "unknown")
                        role_type = role.get("type", "").lower()

                        self.log(
                            "Evaluating role {0}/{1} (name='{2}', type='{3}') against "
                            "filter set {4}/{5}".format(
                                role_index, len(roles), role_name, role_type,
                                filter_index, len(role_filters)
                            ),
                            "DEBUG"
                        )
                        if role_type in ["default", "system"]:
                            self.log(
                                "Skipping {0} role '{1}' - system and default roles are "
                                "excluded from playbook generation".format(
                                    role_type, role_name
                                ),
                                "DEBUG"
                            )
                            system_roles_skipped += 1
                            continue

                        if (
                            role_name.startswith("SUPER-ADMIN") or
                            role_name.startswith("NETWORK-ADMIN") or
                            role_name.startswith("OBSERVER")
                        ):
                            self.log(
                                "Skipping system default role by name prefix: '{0}' - "
                                "system roles are excluded from playbook generation".format(
                                    role_name
                                ),
                                "DEBUG"
                            )
                            system_roles_skipped += 1
                            continue
                        match = True

                        for key, value in filter_param.items():
                            if not isinstance(value, list):
                                self.msg = (
                                    "Invalid format for 'role_name' in role_details filter. "
                                    "Expected list of strings, got {0}. All filter "
                                    "parameters must be provided as lists.".format(
                                        type(value).__name__
                                    )
                                )
                                self.set_operation_result(
                                    "failed", False, self.msg, "ERROR"
                                ).check_return_status()

                            self.log(
                                "Filter criterion '{0}' with {1} value(s): {2}".format(
                                    key, len(value), value
                                ),
                                "DEBUG"
                            )

                            if key == "role_name":
                                if role_name not in value:
                                    self.log(
                                        "Role '{0}' does not match filter values {1} - "
                                        "marking as non-match".format(role_name, value),
                                        "DEBUG"
                                    )
                                    match = False
                                    break
                                else:
                                    self.log(
                                        "Role '{0}' matches filter - criterion satisfied".format(
                                            role_name
                                        ),
                                        "DEBUG"
                                    )
                        if match:
                            if role not in filtered_roles:
                                filtered_roles.append(role)
                                filter_matches += 1
                                total_matches += 1

                                self.log(
                                    "Role '{0}' matched all criteria in filter set {1}/{2} - "
                                    "added to filtered list (total matches: {3})".format(
                                        role_name, filter_index, len(role_filters),
                                        total_matches
                                    ),
                                    "DEBUG"
                                )
                            else:
                                self.log(
                                    "Role '{0}' already in filtered list - skipping "
                                    "duplicate".format(role_name),
                                    "DEBUG"
                                )

                    self.log(
                        "Filter set {0}/{1} resulted in {2} matching role(s)".format(
                            filter_index, len(role_filters), filter_matches
                        ),
                        "INFO"
                    )

                final_roles = filtered_roles

                self.log(
                    "Role filtering completed - {0} custom role(s) matched out of {1} "
                    "total roles retrieved (system/default roles skipped: {2}, filtered "
                    "out: {3})".format(
                        len(final_roles), len(roles), system_roles_skipped,
                        len(roles) - len(final_roles) - system_roles_skipped
                    ),
                    "INFO"
                )

            else:
                self.log(
                    "No user filters applied - excluding system/default roles and "
                    "including all custom roles from {0} total roles".format(len(roles)),
                    "INFO"
                )

                system_roles_skipped = 0
                final_roles = []
                for role_index, role in enumerate(roles, start=1):
                    role_name = role.get("name", "")
                    role_type = role.get("type", "").lower()

                    self.log(
                        "Processing role {0}/{1}: name='{2}', type='{3}'".format(
                            role_index, len(roles), role_name, role_type
                        ),
                        "DEBUG"
                    )

                    if (
                        role_name.startswith("SUPER-ADMIN") or
                        role_name.startswith("NETWORK-ADMIN") or
                        role_name.startswith("OBSERVER")
                    ):
                        self.log(
                            "Skipping system default role by name prefix: '{0}'".format(
                                role_name
                            ),
                            "DEBUG"
                        )
                        system_roles_skipped += 1
                        continue

                    if role_type in ["default", "system"]:
                        self.log(
                            "Skipping {0} role: '{1}'".format(role_type, role_name),
                            "DEBUG"
                        )
                        system_roles_skipped += 1
                        continue

                    final_roles.append(role)

                    self.log(
                        "Added custom role '{0}' to final list (total custom roles: {1})".format(
                            role_name, len(final_roles)
                        ),
                        "DEBUG"
                    )

                self.log(
                    "System/default role exclusion completed - {0} custom role(s) "
                    "included, {1} system/default role(s) excluded".format(
                        len(final_roles), system_roles_skipped
                    ),
                    "INFO"
                )

        except Exception as e:
            error_msg = (
                "Error retrieving roles from Catalyst Center API. Exception type: {0}, "
                "Exception message: {1}. API call failed using family '{2}' and "
                "function '{3}'.".format(
                    type(e).__name__, str(e), api_family, api_function
                )
            )
            self.log(error_msg, "ERROR")
            self.fail_and_exit(
                "Failed to retrieve roles from Catalyst Center. Please verify API "
                "connectivity and permissions."
            )

        # Modify role details using temp_spec
        self.log(
            "Retrieving temporary specification for role details transformation using "
            "role_details_temp_spec()",
            "DEBUG"
        )

        role_details_temp_spec = self.role_details_temp_spec()

        self.log(
            "Transforming {0} role record(s) using modify_parameters() with "
            "role_details_temp_spec to generate playbook-compatible structure with "
            "all 9 permission categories".format(len(final_roles)),
            "INFO"
        )

        role_details = self.modify_parameters(role_details_temp_spec, final_roles)

        self.log(
            "Successfully transformed {0} role(s) into playbook format with fields: "
            "{1}".format(
                len(role_details), list(role_details_temp_spec.keys()) if role_details else []
            ),
            "INFO"
        )

        modified_role_details = {"role_details": role_details}

        self.log(
            "Role retrieval and transformation completed successfully - returning {0} "
            "role detail(s) for YAML generation (all custom roles only)".format(
                len(role_details)
            ),
            "INFO"
        )

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
            self.log(
                "No file_path provided in input parameters - generating default "
                "filename using pattern '{module_name}_playbook_{timestamp}.yml'",
                "INFO"
            )
            file_path = self.generate_filename()
            self.log(
                "Auto-generated file path: {0}".format(file_path),
                "INFO"
            )

        self.log("YAML configuration file path determined: {0}".format(file_path), "DEBUG")

        self.log("File path determined: {0}".format(file_path), "DEBUG")

        component_specific_filters = (
            yaml_config_generator.get("component_specific_filters") or {}
        )
        self.log(
            "Extracted component-specific filters from input: {0}".format(
                component_specific_filters
            ),
            "DEBUG"
        )

        # Retrieve the supported network elements for the module
        module_supported_network_elements = self.module_schema.get("network_elements", {})
        self.log(
            "Module schema contains {0} supported network element type(s): {1}".format(
                len(module_supported_network_elements),
                list(module_supported_network_elements.keys())
            ),
            "DEBUG"
        )
        components_list = component_specific_filters.get(
            "components_list", list(module_supported_network_elements.keys())
        )
        if component_specific_filters.get("components_list"):
            self.log(
                "Using user-specified components_list from filters: {0}".format(
                    components_list
                ),
                "INFO"
            )
        else:
            self.log(
                "No components_list specified in filters - defaulting to all "
                "supported components: {0}".format(components_list),
                "INFO"
            )

        self.log(
            "Components to process in YAML generation: {0} component(s) - {1}".format(
                len(components_list), components_list
            ),
            "INFO"
        )
        # NEW: Initialize tracking variables
        components_processed = 0
        components_skipped = 0
        total_configurations = 0

        self.log(
            "Initialized statistics tracking: components_processed={0}, "
            "components_skipped={1}, total_configurations={2}".format(
                components_processed, components_skipped, total_configurations
            ),
            "DEBUG"
        )
        config_dict = {}
        self.log(
            "Beginning component processing loop - iterating over {0} component(s)".format(
                len(components_list)
            ),
            "DEBUG"
        )

        for component_index, component in enumerate(components_list, start=1):
            self.log(
                "Processing component {0}/{1}: '{2}'".format(
                    component_index, len(components_list), component
                ),
                "DEBUG"
            )

            # Validate component is supported
            network_element = module_supported_network_elements.get(component)

            if not network_element:
                self.log(
                    "Component '{0}' (component {1}/{2}) is not supported by module "
                    "'{3}'. Skipping this component. Supported components: {4}".format(
                        component, component_index, len(components_list),
                        self.module_name, list(module_supported_network_elements.keys())
                    ),
                    "WARNING"
                )
                components_skipped += 1
                self.log(
                    "Incremented components_skipped counter to {0} due to unsupported "
                    "component '{1}'".format(components_skipped, component),
                    "DEBUG"
                )
                continue

            self.log(
                "Component '{0}' validated successfully - network element configuration "
                "found in module schema".format(component),
                "DEBUG"
            )

            # Construct filter parameters
            self.log(
                "Constructing filter parameters for component '{0}' with global_filters "
                "and component_specific_filters".format(component),
                "DEBUG"
            )

            filters = {
                "global_filters": yaml_config_generator.get("global_filters", {}),
                "component_specific_filters": component_specific_filters
            }

            self.log(
                "Filter parameters constructed for component '{0}': global_filters={1}, "
                "component_specific_filters={2}".format(
                    component, filters["global_filters"],
                    filters["component_specific_filters"]
                ),
                "DEBUG"
            )

            operation_func = network_element.get("get_function_name")
            self.log(
                "Retrieved operation function for component '{0}': {1}".format(
                    component, operation_func.__name__ if callable(operation_func)
                    else "None"
                ),
                "DEBUG"
            )
            if not callable(operation_func):
                self.log(
                    "No operation function found for component '{0}' (component {1}/{2}). "
                    "Network element configuration is missing 'get_function_name' or "
                    "function is not callable. Skipping component.".format(
                        component, component_index, len(components_list)
                    ),
                    "WARNING"
                )
                components_skipped += 1
                self.log(
                    "Incremented components_skipped counter to {0} due to missing "
                    "operation function for '{1}'".format(components_skipped, component),
                    "DEBUG"
                )
                continue

            # Execute component retrieval function
            self.log(
                "Calling operation function '{0}' for component '{1}' with network "
                "element config and filters".format(
                    operation_func.__name__, component
                ),
                "INFO"
            )

            try:
                details = operation_func(network_element, filters)

                self.log(
                    "Successfully executed operation function for component '{0}' - "
                    "received details response".format(component),
                    "DEBUG"
                )

                self.log(
                    "Details retrieved for component '{0}': keys={1}, data_type={2}".format(
                        component, list(details.keys()) if isinstance(details, dict) else "N/A",
                        type(details).__name__
                    ),
                    "DEBUG"
                )

                # Validate and extract component data
                if component in details and details[component]:
                    component_data = details[component]

                    self.log(
                        "Component '{0}' has data in response - extracting configurations".format(
                            component
                        ),
                        "DEBUG"
                    )

                    config_dict[component] = component_data

                    # Calculate configuration count
                    if isinstance(component_data, list):
                        config_count = len(component_data)
                    elif isinstance(component_data, dict):
                        config_count = 1
                    else:
                        config_count = 1

                    total_configurations += config_count
                    components_processed += 1

                    self.log(
                        "Successfully processed component '{0}' (component {1}/{2}): "
                        "added {3} configuration(s) to output. Updated statistics: "
                        "components_processed={4}, total_configurations={5}".format(
                            component, component_index, len(components_list),
                            config_count, components_processed, total_configurations
                        ),
                        "INFO"
                    )

                    self.log(
                        "Component '{0}' data added to config_dict".format(
                            component
                        ),
                        "DEBUG"
                    )
                else:
                    self.log(
                        "Component '{0}' (component {1}/{2}) returned no data or empty "
                        "data. Response keys: {3}. Skipping component.".format(
                            component, component_index, len(components_list),
                            list(details.keys()) if isinstance(details, dict) else "N/A"
                        ),
                        "WARNING"
                    )
                    components_skipped += 1
                    self.log(
                        "Incremented components_skipped counter to {0} due to no data "
                        "for component '{1}'".format(components_skipped, component),
                        "DEBUG"
                    )
            except Exception as e:
                self.log(
                    "Error occurred while processing component '{0}' (component {1}/{2}). "
                    "Exception type: {3}, Exception message: {4}. Skipping component and "
                    "continuing with next component.".format(
                        component, component_index, len(components_list),
                        type(e).__name__, str(e)
                    ),
                    "ERROR"
                )
                components_skipped += 1
                self.log(
                    "Incremented components_skipped counter to {0} due to exception "
                    "during processing of component '{1}'".format(
                        components_skipped, component
                    ),
                    "DEBUG"
                )
                continue
            self.log(
                "Component processing loop completed. Final statistics: "
                "components_processed={0}, components_skipped={1}, "
                "total_configurations={2}, total_components_attempted={3}".format(
                    components_processed, components_skipped, total_configurations,
                    len(components_list)
                ),
                "INFO"
            )

        if not config_dict:
            self.log(
                "No configuration data collected from any component - config_dict is "
                "empty. This may indicate no matching users/roles found or all "
                "components were skipped.",
                "WARNING"
            )

            no_config_message = (
                "No users or roles found to process for module '{0}'. Verify input "
                "filters or configuration. Components processed: {1}, Components "
                "skipped: {2}".format(
                    self.module_name, components_processed, components_skipped
                )
            )

            self.log(
                "Generating response for no-data scenario: {0}".format(
                    no_config_message
                ),
                "INFO"
            )

            response_data = {
                "components_processed": components_processed,
                "components_skipped": components_skipped,
                "configurations_count": 0,
                "message": no_config_message,
                "status": "success"
            }
            self.log(
                "Response data for no-data scenario: {0}".format(response_data),
                "DEBUG"
            )

            # Set both msg and response to the same structure
            self.msg = response_data
            self.result["response"] = response_data
            self.log(
                "Operation completed successfully with no data - returning success "
                "status with informational message",
                "INFO"
            )
            self.set_operation_result("success", False, no_config_message, "INFO")
            return self

        final_dict = {"config": config_dict}
        # Create final dictionary structure for YAML
        self.log(
            "Creating final dictionary structure for YAML generation with 'config' "
            "root key and {0} component(s)".format(len(config_dict)),
            "DEBUG"
        )

        final_dict = {"config": config_dict}
        self.log(
            "Final dictionary structure created: root_keys={0}, component_keys={1}".format(
                list(final_dict.keys()), list(config_dict.keys())
            ),
            "DEBUG"
        )

        # Write YAML to file
        self.log(
            "Calling write_dict_to_yaml to write {0} component(s) with {1} total "
            "configuration(s) to file: {2}".format(
                len(config_dict), total_configurations, file_path
            ),
            "INFO"
        )

        write_success = self.write_dict_to_yaml(final_dict, file_path)
        if not write_success:
            self.log(
                "YAML file write operation failed - write_dict_to_yaml returned False "
                "for file path: {0}".format(file_path),
                "ERROR"
            )

            error_message = (
                "Failed to write YAML configuration to file: {0}. Check file "
                "permissions, disk space, and path validity.".format(file_path)
            )

            response_data = {
                "message": error_message,
                "status": "failed"
            }

            self.log(
                "Error response data prepared: {0}".format(response_data),
                "DEBUG"
            )

            self.log(
                "Setting operation result to failed with changed=False - no file created",
                "DEBUG"
            )
            self.set_operation_result("failed", False, error_message, "ERROR")
            self.msg = response_data
            self.result["response"] = response_data

            self.log(
                "YAML configuration generation workflow failed during file write operation",
                "ERROR"
            )

            return self
        self.log(
            "YAML file write operation completed successfully - file created at: "
            "{0}".format(file_path),
            "INFO"
        )

        success_message = (
            "YAML configuration file generated successfully for module '{0}'".format(
                self.module_name
            )
        )

        response_data = {
            "components_processed": components_processed,
            "components_skipped": components_skipped,
            "configurations_count": total_configurations,
            "file_path": file_path,
            "message": success_message,
            "status": "success"
        }

        self.log(
            "Success response data prepared: {0}".format(response_data),
            "DEBUG"
        )

        self.log(
            "Setting operation result to success with changed=True to indicate "
            "file was created",
            "DEBUG"
        )

        self.set_operation_result("success", True, success_message, "INFO")

        self.msg = response_data
        self.result["response"] = response_data

        self.log(
            "YAML configuration generation workflow completed successfully. "
            "Summary: {0} component(s) processed, {1} component(s) skipped, "
            "{2} total configuration(s) written to {3}".format(
                components_processed, components_skipped, total_configurations,
                file_path
            ),
            "INFO"
        )

        return self

    def get_want(self, config, state):
        """
        Creates parameters for API calls based on the specified state.

        Args:
            config (dict): The configuration data for the user/role elements.
            state (str): The desired state ('gathered').
        """
        self.log(
            "Starting parameter preparation for API operations with state '{0}' and "
            "configuration provided".format(state),
            "DEBUG"
        )

        self.log(
            "Input configuration for get_want: generate_all={0}, file_path={1}, "
            "component_filters={2}".format(
                config.get("generate_all_configurations"),
                config.get("file_path"),
                config.get("component_specific_filters")
            ),
            "DEBUG"
        )

        self.validate_params(config)
        self.log(
            "Calling validate_params to validate configuration structure and values",
            "DEBUG"
        )

        self.validate_params(config)

        self.log(
            "Configuration parameters validated successfully - proceeding with parameter "
            "preparation",
            "DEBUG"
        )

        generate_all = config.get("generate_all_configurations", False)
        self.log("Generate all configurations mode: {0}".format(generate_all), "INFO")

        if generate_all:
            self.log("Generate all configurations is enabled - will retrieve all users and custom roles", "INFO")
            if not config.get("component_specific_filters"):
                self.log(
                    "No component_specific_filters provided in generate_all mode - setting "
                    "default component filters to include all components (user_details and "
                    "role_details)",
                    "INFO"
                )

                config["component_specific_filters"] = {
                    "components_list": ["user_details", "role_details"]
                }

                self.log(
                    "Default component_specific_filters set: {0}".format(
                        config["component_specific_filters"]
                    ),
                    "DEBUG"
                )
            else:
                self.log(
                    "Generate all configurations mode is disabled - using explicit component "
                    "filters from configuration",
                    "DEBUG"
                )
        component_specific_filters = config.get("component_specific_filters", {})
        components_list = component_specific_filters.get("components_list", [])

        self.log(
            "Extracted component_specific_filters from configuration: {0}".format(
                component_specific_filters
            ),
            "DEBUG"
        )

        self.log(
            "Extracted components_list for validation: {0} component(s) specified - {1}".format(
                len(components_list), components_list if components_list else "empty (will default to all)"
            ),
            "DEBUG"
        )

        if components_list:
            self.log(
                "Components_list provided - validating {0} component(s) against allowed "
                "component list".format(len(components_list)),
                "INFO"
            )
            allowed_components = ["user_details", "role_details"]
            self.log(
                "Allowed components for this module: {0}".format(allowed_components),
                "DEBUG"
            )
            invalid_components = []
            self.log(
                "Starting validation of each component in components_list",
                "DEBUG"
            )

            # Check each component in the list
            for component_index, component in enumerate(components_list, start=1):
                self.log(
                    "Validating component {0}/{1}: '{2}' against allowed list".format(
                        component_index, len(components_list), component
                    ),
                    "DEBUG"
                )

                if component not in allowed_components:
                    invalid_components.append(component)

                    self.log(
                        "Component '{0}' (component {1}/{2}) is INVALID - not in allowed "
                        "components list {3}. Adding to invalid components list.".format(
                            component, component_index, len(components_list),
                            allowed_components
                        ),
                        "WARNING"
                    )
                else:
                    self.log(
                        "Component '{0}' (component {1}/{2}) is VALID - found in allowed "
                        "components list".format(
                            component, component_index, len(components_list)
                        ),
                        "DEBUG"
                    )

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
            else:
                self.log(
                    "Component validation PASSED - all {0} component(s) are valid: {1}".format(
                        len(components_list), components_list
                    ),
                    "INFO"
                )
        else:
            self.log(
                "No components_list specified - will default to all supported components "
                "during YAML generation: {0}".format(["user_details", "role_details"]),
                "INFO"
            )

        # Build want dictionary
        self.log(
            "Building want dictionary with yaml_config_generator parameters",
            "DEBUG"
        )

        want = {}
        want["yaml_config_generator"] = config

        self.log(
            "Want dictionary constructed successfully with yaml_config_generator key. "
            "Config keys: {0}".format(list(config.keys())),
            "DEBUG"
        )

        self.log(
            "yaml_config_generator parameters added to want: generate_all={0}, "
            "file_path={1}, components_count={2}".format(
                config.get("generate_all_configurations"),
                config.get("file_path", "auto-generated"),
                len(components_list) if components_list else "all"
            ),
            "INFO"
        )

        self.want = want
        self.log("Desired State (want): {0}".format(str(self.want)), "INFO")
        self.msg = "Successfully collected all parameters from the playbook for User Role operations."
        self.status = "success"
        self.log(
            "Parameter preparation completed successfully for state '{0}'. Ready for "
            "diff operations.".format(state),
            "INFO"
        )
        return self

    def get_diff_gathered(self):
        """
        Executes YAML configuration file generation for user and role configurations.

        This function serves as the orchestration layer for the 'gathered' state operation,
        coordinating the execution of YAML configuration file generation based on parameters
        prepared in get_want(). It iterates through defined operations, validates parameters,
        and invokes the appropriate generation functions.
        """
        self.log(
            "Starting diff gathered operation for state 'gathered' to generate YAML "
            "configuration file for user and role management",
            "DEBUG"
        )

        start_time = time.time()

        self.log(
            "Operation start time recorded: {0} (epoch timestamp for performance tracking)".format(
                start_time
            ),
            "DEBUG"
        )

        # Define operations to be processed
        self.log(
            "Defining operations list for processing - currently supports 1 operation: "
            "YAML Config Generator",
            "DEBUG"
        )
        # Define workflow operations
        workflow_operations = [
            (
                "yaml_config_generator",
                "YAML Config Generator",
                self.yaml_config_generator,
            )
        ]
        operations_executed = 0
        operations_skipped = 0

        # Iterate over operations and process them
        self.log(
            "Beginning sequential iteration over {0} defined operation(s) for processing".format(
                len(workflow_operations)
            ),
            "DEBUG"
        )
        for index, (param_key, operation_name, operation_func) in enumerate(
            workflow_operations, start=1
        ):
            self.log(
                "Processing operation {0}/{1}: '{2}' with parameter key '{3}' to check "
                "if parameters exist in want dictionary".format(
                    index, len(workflow_operations), operation_name, param_key
                ),
                "DEBUG"
            )
            params = self.want.get(param_key)
            if params:
                self.log(
                    "Iteration {0}: Parameters found for {1}. Starting processing.".format(
                        index, operation_name
                    ),
                    "INFO",
                )

                try:
                    operation_func(params)
                    self.log(
                        "Operation {0}/{1} ('{2}') executed successfully and passed return "
                        "status validation".format(index, len(workflow_operations), operation_name),
                        "INFO"
                    )
                    operations_executed += 1
                    self.log(
                        "{0} operation completed successfully".format(operation_name),
                        "DEBUG"
                    )
                except Exception as e:
                    self.log(
                        "{0} operation failed with error: {1}".format(operation_name, str(e)),
                        "ERROR"
                    )
                    self.set_operation_result(
                        "failed", True,
                        "{0} operation failed: {1}".format(operation_name, str(e)),
                        "ERROR"
                    ).check_return_status()

            else:
                operations_skipped += 1
                self.log(
                    "No parameters found in want dictionary for operation {0}/{1} ('{2}') "
                    "with parameter key '{3}'. Skipping this operation and continuing with "
                    "next operation.".format(
                        index, len(workflow_operations), operation_name, param_key
                    ),
                    "WARNING"
                )

                self.log(
                    "Want dictionary contents for debugging: keys={0}".format(
                        list(self.want.keys()) if isinstance(self.want, dict) else "non-dict"
                    ),
                    "DEBUG"
                )

        end_time = time.time()
        elapsed_time = end_time - start_time

        self.log(
            "Operation end time recorded: {0} (epoch timestamp)".format(end_time),
            "DEBUG"
        )

        self.log(
            "All operations processed successfully. Total execution time: {0:.2f} seconds. "
            "Operations completed: {1}/{2}".format(
                elapsed_time, len(workflow_operations), len(workflow_operations)
            ),
            "INFO"
        )

        self.log(
            "Diff gathered operation completed successfully for state 'gathered'. "
            "Returning self instance for method chaining.",
            "DEBUG"
        )

        return self


def main():
    """
    Main entry point for the Cisco Catalyst Center brownfield user and role playbook generator module.

    This function serves as the primary execution entry point for the Ansible module,
    orchestrating the complete workflow from parameter collection to YAML playbook
    generation for brownfield user and role management extraction.

    Purpose:
        Initializes and executes the brownfield user and role playbook generator
        workflow to extract existing user accounts and custom role configurations
        from Cisco Catalyst Center and generate Ansible-compatible YAML playbook files.

    Workflow Steps:
        1. Define module argument specification with required parameters
        2. Initialize Ansible module with argument validation
        3. Create UserRolePlaybookGenerator instance
        4. Validate Catalyst Center version compatibility (>= 2.3.5.3)
        5. Validate and sanitize state parameter
        6. Execute input parameter validation
        7. Process each configuration item in the playbook
        8. Execute state-specific operations (gathered workflow)
        9. Return results via module.exit_json()

    Module Arguments:
        Connection Parameters:
            - dnac_host (str, required): Catalyst Center hostname/IP
            - dnac_port (str, default="443"): HTTPS port
            - dnac_username (str, default="admin"): Authentication username
            - dnac_password (str, required, no_log): Authentication password
            - dnac_verify (bool, default=True): SSL certificate verification

        API Configuration:
            - dnac_version (str, default="2.2.3.3"): Catalyst Center version
            - dnac_api_task_timeout (int, default=1200): API timeout (seconds)
            - dnac_task_poll_interval (int, default=2): Poll interval (seconds)
            - validate_response_schema (bool, default=True): Schema validation

        Logging Configuration:
            - dnac_debug (bool, default=False): Debug mode
            - dnac_log (bool, default=False): Enable file logging
            - dnac_log_level (str, default="WARNING"): Log level
            - dnac_log_file_path (str, default="dnac.log"): Log file path
            - dnac_log_append (bool, default=True): Append to log file

        Playbook Configuration:
            - config (list[dict], required): Configuration parameters list
            - state (str, default="gathered", choices=["gathered"]): Workflow state

    Version Requirements:
        - Minimum Catalyst Center version: 2.3.5.3
        - Introduced APIs for user and role retrieval:
            * User Management (get_users_api)
            * Role Management (get_roles_api)

    Supported States:
        - gathered: Extract existing users and roles and generate YAML playbook
        - Future: merged, deleted, replaced (reserved for future use)

    Error Handling:
        - Version compatibility failures: Module exits with error
        - Invalid state parameter: Module exits with error
        - Input validation failures: Module exits with error
        - Configuration processing errors: Module exits with error
        - All errors are logged and returned via module.fail_json()

    Return Format:
        Success: module.exit_json() with result containing:
            - changed (bool): Whether changes were made
            - msg (str/dict): Operation result message or structured response
            - response (dict): Detailed operation results with statistics
            - status (str): Operation status ("success")

        Failure: module.fail_json() with error details:
            - failed (bool): True
            - msg (str): Error message
            - error (str): Detailed error information
    """
    # Record module initialization start time for performance tracking
    module_start_time = time.time()

    # Define the specification for the module's arguments
    # This structure defines all parameters accepted by the module with their types,
    # defaults, and validation rules
    element_spec = {
        # ============================================
        # Catalyst Center Connection Parameters
        # ============================================
        "dnac_host": {
            "required": True,
            "type": "str"
        },
        "dnac_port": {
            "type": "str",
            "default": "443"
        },
        "dnac_username": {
            "type": "str",
            "default": "admin",
            "aliases": ["user"]
        },
        "dnac_password": {
            "type": "str",
            "no_log": True  # Prevent password from appearing in logs
        },
        "dnac_verify": {
            "type": "bool",
            "default": True
        },

        # ============================================
        # API Configuration Parameters
        # ============================================
        "dnac_version": {
            "type": "str",
            "default": "2.2.3.3"
        },
        "dnac_api_task_timeout": {
            "type": "int",
            "default": 1200
        },
        "dnac_task_poll_interval": {
            "type": "int",
            "default": 2
        },
        "validate_response_schema": {
            "type": "bool",
            "default": True
        },

        # ============================================
        # Logging Configuration Parameters
        # ============================================
        "dnac_debug": {
            "type": "bool",
            "default": False
        },
        "dnac_log_level": {
            "type": "str",
            "default": "WARNING"
        },
        "dnac_log_file_path": {
            "type": "str",
            "default": "dnac.log"
        },
        "dnac_log_append": {
            "type": "bool",
            "default": True
        },
        "dnac_log": {
            "type": "bool",
            "default": False
        },

        # ============================================
        # Playbook Configuration Parameters
        # ============================================
        "config": {
            "required": True,
            "type": "list",
            "elements": "dict"
        },
        "state": {
            "default": "gathered",
            "choices": ["gathered"]
        },
    }

    # Initialize the Ansible module with argument specification
    # supports_check_mode=True allows module to run in check mode (dry-run)
    module = AnsibleModule(
        argument_spec=element_spec,
        supports_check_mode=True
    )

    # Create initial log entry with module initialization timestamp
    # Note: Logging is not yet available since object isn't created
    initialization_timestamp = time.strftime(
        "%Y-%m-%d %H:%M:%S",
        time.localtime(module_start_time)
    )

    # Initialize the UserRolePlaybookGenerator object
    # This creates the main orchestrator for brownfield user and role extraction
    ccc_user_role_playbook_generator = UserRolePlaybookGenerator(module)

    # Log module initialization after object creation (now logging is available)
    ccc_user_role_playbook_generator.log(
        "Starting Ansible module execution for brownfield user and role playbook "
        "generator at timestamp {0}".format(initialization_timestamp),
        "INFO"
    )

    ccc_user_role_playbook_generator.log(
        "Module initialized with parameters: dnac_host={0}, dnac_port={1}, "
        "dnac_username={2}, dnac_verify={3}, dnac_version={4}, state={5}, "
        "config_items={6}".format(
            module.params.get("dnac_host"),
            module.params.get("dnac_port"),
            module.params.get("dnac_username"),
            module.params.get("dnac_verify"),
            module.params.get("dnac_version"),
            module.params.get("state"),
            len(module.params.get("config", []))
        ),
        "DEBUG"
    )

    # ============================================
    # Version Compatibility Check
    # ============================================
    ccc_user_role_playbook_generator.log(
        "Validating Catalyst Center version compatibility - checking if version {0} "
        "meets minimum requirement of 2.3.5.3 for user and role management APIs".format(
            ccc_user_role_playbook_generator.get_ccc_version()
        ),
        "INFO"
    )

    if (ccc_user_role_playbook_generator.compare_dnac_versions(
            ccc_user_role_playbook_generator.get_ccc_version(), "2.3.5.3") < 0):

        error_msg = (
            "The specified Catalyst Center version '{0}' does not support the YAML "
            "playbook generation for User Role Management Module. Supported versions "
            "start from '2.3.5.3' onwards. Version '2.3.5.3' introduces APIs for "
            "retrieving user and role settings from the Catalyst Center including "
            "user management (get_users_api) and role management (get_roles_api) "
            "functionalities.".format(
                ccc_user_role_playbook_generator.get_ccc_version()
            )
        )

        ccc_user_role_playbook_generator.log(
            "Version compatibility check failed: {0}".format(error_msg),
            "ERROR"
        )

        ccc_user_role_playbook_generator.msg = error_msg
        ccc_user_role_playbook_generator.set_operation_result(
            "failed", False, ccc_user_role_playbook_generator.msg, "ERROR"
        ).check_return_status()

    ccc_user_role_playbook_generator.log(
        "Version compatibility check passed - Catalyst Center version {0} supports "
        "all required user and role management APIs".format(
            ccc_user_role_playbook_generator.get_ccc_version()
        ),
        "INFO"
    )

    # ============================================
    # State Parameter Validation
    # ============================================
    state = ccc_user_role_playbook_generator.params.get("state")

    ccc_user_role_playbook_generator.log(
        "Validating requested state parameter: '{0}' against supported states: {1}".format(
            state, ccc_user_role_playbook_generator.supported_states
        ),
        "DEBUG"
    )

    if state not in ccc_user_role_playbook_generator.supported_states:
        error_msg = (
            "State '{0}' is invalid for this module. Supported states are: {1}. "
            "Please update your playbook to use one of the supported states.".format(
                state, ccc_user_role_playbook_generator.supported_states
            )
        )

        ccc_user_role_playbook_generator.log(
            "State validation failed: {0}".format(error_msg),
            "ERROR"
        )

        ccc_user_role_playbook_generator.status = "invalid"
        ccc_user_role_playbook_generator.msg = error_msg
        ccc_user_role_playbook_generator.check_return_status()

    ccc_user_role_playbook_generator.log(
        "State validation passed - using state '{0}' for user and role workflow execution".format(
            state
        ),
        "INFO"
    )

    # ============================================
    # Input Parameter Validation
    # ============================================
    ccc_user_role_playbook_generator.log(
        "Starting comprehensive input parameter validation for user and role playbook configuration",
        "INFO"
    )

    ccc_user_role_playbook_generator.validate_input().check_return_status()

    ccc_user_role_playbook_generator.log(
        "Input parameter validation completed successfully - all configuration "
        "parameters meet user and role module requirements",
        "INFO"
    )

    # ============================================
    # Configuration Processing and Default Handling
    # ============================================
    config_list = ccc_user_role_playbook_generator.validated_config

    ccc_user_role_playbook_generator.log(
        "Starting configuration processing loop - will process {0} configuration "
        "item(s) from playbook".format(len(config_list)),
        "INFO"
    )

    # Handle special configuration logic for user and role module
    if len(config_list) == 1:
        config_item = config_list[0]

        ccc_user_role_playbook_generator.log(
            "Single configuration item detected - checking for generate_all_configurations mode",
            "DEBUG"
        )

        # Check if generate_all_configurations is enabled
        if config_item.get("generate_all_configurations", False):
            ccc_user_role_playbook_generator.log(
                "Generate all configurations mode enabled - setting default components "
                "to include both user_details and role_details",
                "INFO"
            )

            if not config_item.get("component_specific_filters"):
                config_item["component_specific_filters"] = {
                    "components_list": ["user_details", "role_details"]
                }

                ccc_user_role_playbook_generator.log(
                    "Default component_specific_filters set for generate_all mode: {0}".format(
                        config_item["component_specific_filters"]
                    ),
                    "DEBUG"
                )
            else:
                ccc_user_role_playbook_generator.log(
                    "Component_specific_filters already provided in generate_all mode - "
                    "using existing filters: {0}".format(
                        config_item.get("component_specific_filters")
                    ),
                    "DEBUG"
                )

        elif not config_item.get("component_specific_filters"):
            # Default behavior for normal mode when no filters specified
            ccc_user_role_playbook_generator.log(
                "No component_specific_filters provided in normal mode - applying "
                "default configuration to retrieve all user and role components",
                "INFO"
            )

            ccc_user_role_playbook_generator.msg = (
                "No valid configurations found in the provided parameters. "
                "Applying default configuration to retrieve all user and role details."
            )

            ccc_user_role_playbook_generator.validated_config = [
                {
                    'component_specific_filters': {
                        'components_list': ["user_details", "role_details"]
                    }
                }
            ]

            ccc_user_role_playbook_generator.log(
                "Default configuration applied: {0}".format(
                    ccc_user_role_playbook_generator.validated_config[0]
                ),
                "DEBUG"
            )

    # ============================================
    # Configuration Processing Loop
    # ============================================
    final_config_list = ccc_user_role_playbook_generator.validated_config

    ccc_user_role_playbook_generator.log(
        "Configuration preprocessing completed - will process {0} final "
        "configuration item(s)".format(len(final_config_list)),
        "INFO"
    )

    for config_index, config in enumerate(final_config_list, start=1):
        ccc_user_role_playbook_generator.log(
            "Processing configuration item {0}/{1} for state '{2}' with components: {3}".format(
                config_index, len(final_config_list), state,
                config.get("component_specific_filters", {}).get("components_list", "all")
            ),
            "INFO"
        )

        # Reset values for clean state between configurations
        ccc_user_role_playbook_generator.log(
            "Resetting module state variables for clean configuration processing",
            "DEBUG"
        )
        ccc_user_role_playbook_generator.reset_values()

        # Collect desired state (want) from configuration
        ccc_user_role_playbook_generator.log(
            "Collecting desired state parameters from configuration item {0} - "
            "building want dictionary for user and role operations".format(
                config_index
            ),
            "DEBUG"
        )
        ccc_user_role_playbook_generator.get_want(
            config, state
        ).check_return_status()

        # Execute state-specific operation (gathered workflow)
        ccc_user_role_playbook_generator.log(
            "Executing state-specific operation for '{0}' workflow on "
            "configuration item {1} - will retrieve users and roles from "
            "Catalyst Center".format(state, config_index),
            "INFO"
        )
        ccc_user_role_playbook_generator.get_diff_state_apply[state]().check_return_status()

        ccc_user_role_playbook_generator.log(
            "Successfully completed processing for configuration item {0}/{1} - "
            "user and role data extraction and YAML generation completed".format(
                config_index, len(final_config_list)
            ),
            "INFO"
        )

    # ============================================
    # Module Completion and Exit
    # ============================================
    module_end_time = time.time()
    module_duration = module_end_time - module_start_time

    completion_timestamp = time.strftime(
        "%Y-%m-%d %H:%M:%S",
        time.localtime(module_end_time)
    )

    ccc_user_role_playbook_generator.log(
        "User and role playbook generator module execution completed successfully "
        "at timestamp {0}. Total execution time: {1:.2f} seconds. Processed {2} "
        "configuration item(s) with final status: {3}".format(
            completion_timestamp,
            module_duration,
            len(final_config_list),
            ccc_user_role_playbook_generator.status
        ),
        "INFO"
    )

    ccc_user_role_playbook_generator.log(
        "Final module result summary: changed={0}, msg_type={1}, response_available={2}".format(
            ccc_user_role_playbook_generator.result.get("changed", False),
            type(ccc_user_role_playbook_generator.result.get("msg")).__name__,
            "response" in ccc_user_role_playbook_generator.result
        ),
        "DEBUG"
    )

    # Exit module with results
    # This is a terminal operation - function does not return after this
    ccc_user_role_playbook_generator.log(
        "Exiting Ansible module with result containing user and role extraction results",
        "DEBUG"
    )

    module.exit_json(**ccc_user_role_playbook_generator.result)


if __name__ == "__main__":
    main()
