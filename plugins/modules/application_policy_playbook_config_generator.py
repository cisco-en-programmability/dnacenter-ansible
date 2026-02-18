#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright (c) 2026, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

"""Ansible module to generate YAML configurations for Application Policy Module."""
from __future__ import absolute_import, division, print_function

__metaclass__ = type
__author__ = "Syed Khadeer Ahmed, Madhan Sankaranarayanan"

DOCUMENTATION = r"""
---
module: application_policy_playbook_config_generator
short_description: Generate YAML configurations playbook for 'application_policy_workflow_manager' module.
description:
- Generates YAML configurations compatible with the 'application_policy_workflow_manager'
  module, reducing the effort required to manually create Ansible playbooks.
- The YAML configurations generated represent the application policies and queuing
  profiles deployed in the Cisco Catalyst Center.
- Supports extraction of Queuing Profiles and Application Policies.
version_added: 6.44.0
extends_documentation_fragment:
- cisco.dnac.workflow_manager_params
author:
- Syed Khadeer Ahmed (@syed-khadeerahmed)
- Madhan Sankaranarayanan (@madhansansel)
options:
  state:
    description: The desired state of Cisco Catalyst Center after module execution.
    type: str
    choices: [gathered]
    default: gathered
  config:
    description:
      - A list of filters for generating YAML playbook compatible with the 'application_policy_workflow_manager'
        module.
      - Filters specify which components to include in the YAML configuration file.
    type: list
    elements: dict
    required: true
    suboptions:
      generate_all_configurations:
        description:
          - When set to True, automatically generates YAML configurations for all application policies and queuing profiles.
          - This mode discovers all configured policies and profiles in Cisco Catalyst Center.
          - When enabled, the config parameter becomes optional and will use default values if not specified.
          - A default filename will be generated automatically if file_path is not specified.
        type: bool
        required: false
        default: false
      file_path:
        description:
          - Path where the YAML configuration file will be saved.
          - If not provided, the file will be saved in the current working directory with
            a default file name "application_policy_workflow_manager_playbook_<DD_Mon_YYYY_HH_MM_SS_MS>.yml".
        type: str
        required: false
      component_specific_filters:
        description:
          - Filters to specify which application policy components to include in the YAML configuration file.
          - Allows granular selection of specific components and their parameters.
        type: dict
        required: false
        suboptions:
          components_list:
            description:
              - List of components to include in the YAML configuration file.
              - Valid values are ["queuing_profile", "application_policy"]
              - If not specified, all supported components are included.
            type: list
            elements: str
            required: false
            choices: ["queuing_profile", "application_policy"]
          queuing_profile:
            description:
              - Specific queuing profile filtering options.
              - Allows extraction of only specific queuing profiles by name.
            type: dict
            required: false
            suboptions:
              profile_names_list:
                description:
                  - List of specific queuing profile names to extract.
                  - Only profiles in this list will be included in the generated configuration.
                  - Example ["Enterprise-QoS-Profile", "Wireless-QoS-Profile"]
                type: list
                elements: str
                required: false
          application_policy:
            description:
              - Specific application policy filtering options.
              - Allows extraction of only specific policies by name.
            type: dict
            required: false
            suboptions:
              policy_names_list:
                description:
                  - List of specific application policy names to extract.
                  - Only policies in this list will be included in the generated configuration.
                  - Example ["wired_traffic_policy", "wireless_traffic_policy"]
                type: list
                elements: str
                required: false
requirements:
- dnacentersdk >= 2.9.3
- python >= 3.9
notes:
- SDK Methods used are
  - application_policy.ApplicationPolicy.get_application_policy
  - application_policy.ApplicationPolicy.get_application_policy_queuing_profile
- Paths used are
  - GET /dna/intent/api/v1/app-policy
  - GET /dna/intent/api/v1/app-policy-queuing-profile
"""

EXAMPLES = r"""
- name: Generate all application policy configurations
  cisco.dnac.application_policy_playbook_config_generator:
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

- name: Generate configurations with custom file path
  cisco.dnac.application_policy_playbook_config_generator:
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
      - file_path: "/tmp/app_policy_config.yml"

- name: Generate specific queuing profiles
  cisco.dnac.application_policy_playbook_config_generator:
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
      - file_path: "/tmp/queuing_profiles.yml"
        component_specific_filters:
          components_list: ["queuing_profile"]
          queuing_profile:
            profile_names_list: ["Enterprise-QoS-Profile", "Wireless-QoS"]

- name: Generate specific application policies
  cisco.dnac.application_policy_playbook_config_generator:
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
      - file_path: "/tmp/app_policies.yml"
        component_specific_filters:
          components_list: ["application_policy"]
          application_policy:
            policy_names_list: ["wired_traffic_policy"]

- name: Generate both queuing profiles and policies with filters
  cisco.dnac.application_policy_playbook_config_generator:
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
      - file_path: "/tmp/complete_app_policy_config.yml"
        component_specific_filters:
          components_list: ["queuing_profile", "application_policy"]
          queuing_profile:
            profile_names_list: ["Enterprise-QoS-Profile"]
          application_policy:
            policy_names_list: ["wired_traffic_policy", "wireless_traffic_policy"]
"""

RETURN = r"""
response_1:
  description: Successful YAML configuration generation
  returned: always
  type: dict
  sample: >
    {
        "msg": "YAML config generation succeeded for module 'application_policy_workflow_manager'.",
        "response": {
            "status": "success",
            "message": "YAML config generation succeeded for module 'application_policy_workflow_manager'.",
            "file_path": "application_policy_workflow_manager_playbook_2026-02-03_03-00-59.yml",
            "configurations_count": 15,
            "components_processed": 2,
            "components_skipped": 0
        },
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

try:
    import yaml
    HAS_YAML = True
except ImportError:
    HAS_YAML = False
    yaml = None
import time
from collections import OrderedDict


if HAS_YAML:
    class OrderedDumper(yaml.Dumper):
        def represent_dict(self, data):
            return self.represent_mapping("tag:yaml.org,2002:map", data.items())

    OrderedDumper.add_representer(OrderedDict, OrderedDumper.represent_dict)
else:
    OrderedDumper = None


class ApplicationPolicyPlaybookGenerator(DnacBase, BrownFieldHelper):
    """
    A class for generating playbook files for application policies deployed within the Cisco Catalyst Center.
    """

    def __init__(self, module):
        """
        Initialize an instance of the class.
        Args:
            module: The module associated with the class instance.
        Returns:
            None
        """
        self.supported_states = ["gathered"]
        super().__init__(module)
        self.module_schema = self.get_workflow_elements_schema()
        self.module_name = "application_policy_workflow_manager"

        # Initialize operation tracking
        self.operation_successes = []
        self.operation_failures = []
        self.total_components_processed = 0

        # Initialize generate_all_configurations
        self.generate_all_configurations = False

        self.log("Initialized ApplicationPolicyPlaybookGenerator for module: {0}".format(self.module_name), "INFO")

    def validate_input(self):
        """
        Validates input configuration parameters for application policy playbook generation.

        Performs comprehensive validation of playbook configuration structure, parameters,
        and nested filters to ensure they conform to the expected schema.

        Returns:
            self: Instance with updated attributes:
                - self.validated_config: Validated configuration list
                - self.msg: Validation result message
                - self.status: Operation status (success/failed)
        """
        self.log(
            "Starting validation of input configuration parameters for application "
            "policy playbook generation",
            "DEBUG"
        )

        if not self.config:
            self.msg = "config parameter is required for application_policy_playbook_config_generator module"
            self.set_operation_result("failed", False, self.msg, "ERROR")
            return self

        self.log(
            "Configuration parameter 'config' is present with {0} configuration "
            "item(s) to validate".format(len(self.config)),
            "DEBUG"
        )

        self.log(
            "Defining temporary specification (temp_spec) for allowed top-level "
            "configuration parameters",
            "DEBUG"
        )

        temp_spec = {
            "generate_all_configurations": {
                "type": "bool",
                "required": False,
                "default": False
            },
            "file_path": {
                "type": "str",
                "required": False
            },
            "component_specific_filters": {
                "type": "dict",
                "required": False
            },
        }
        allowed_keys = set(temp_spec.keys())

        self.log(
            "Temporary specification defined with {0} allowed top-level parameters: "
            "{1}".format(len(allowed_keys), list(allowed_keys)),
            "DEBUG"
        )

        # Validate that only allowed keys are present in the configuration
        for config_index, config_item in enumerate(self.config, start=1):
            self.log(
                "Validating configuration item {0}/{1} - checking if item is a "
                "dictionary".format(config_index, len(self.config)),
                "DEBUG"
            )

            if not isinstance(config_item, dict):
                self.log(
                    "Configuration item {0}/{1} failed type validation - expected "
                    "dict but got {2}".format(
                        config_index, len(self.config), type(config_item).__name__
                    ),
                    "ERROR"
                )

                self.msg = (
                    "Configuration item must be a dictionary, got: {0}".format(
                        type(config_item).__name__
                    )
                )

                self.log(
                    "Setting operation result to failed due to invalid configuration "
                    "item type. Error message: {0}".format(self.msg),
                    "ERROR"
                )

                self.set_operation_result("failed", False, self.msg, "ERROR")
                return self

            self.log(
                "Configuration item {0}/{1} passed type validation - is a dictionary "
                "with keys: {2}".format(
                    config_index, len(self.config), list(config_item.keys())
                ),
                "DEBUG"
            )

            # Check for invalid keys at top level
            config_keys = set(config_item.keys())
            invalid_keys = config_keys - allowed_keys

            self.log(
                "Checking configuration item {0}/{1} for invalid top-level keys. "
                "Found keys: {2}, Allowed keys: {3}, Invalid keys: {4}".format(
                    config_index, len(self.config), list(config_keys),
                    list(allowed_keys), list(invalid_keys) if invalid_keys else "none"
                ),
                "DEBUG"
            )

            if invalid_keys:
                self.log(
                    "Configuration item {0}/{1} contains {2} invalid top-level "
                    "parameter(s): {3}. Only these parameters are allowed: {4}".format(
                        config_index, len(self.config), len(invalid_keys),
                        list(invalid_keys), list(allowed_keys)
                    ),
                    "ERROR"
                )

                self.msg = (
                    "Invalid parameters found in playbook configuration: {0}. "
                    "Only the following parameters are allowed: {1}. "
                    "Please remove the invalid parameters and try again.".format(
                        list(invalid_keys), list(allowed_keys)
                    )
                )

                self.log(
                    "Setting operation result to failed due to invalid top-level "
                    "parameters and calling check_return_status to exit. Error "
                    "message: {0}".format(self.msg),
                    "ERROR"
                )

                self.set_operation_result(
                    "failed", False, self.msg, "ERROR"
                ).check_return_status()

            self.log(
                "Configuration item {0}/{1} passed top-level key validation - all "
                "keys are allowed".format(config_index, len(self.config)),
                "DEBUG"
            )

        # Validate component_specific_filters nested parameters
        self.log(
            "Beginning validation of component_specific_filters nested parameters "
            "for all configuration items",
            "DEBUG"
        )

        allowed_component_filter_keys = ["components_list", "queuing_profile", "application_policy"]
        allowed_component_choices = ["queuing_profile", "application_policy"]

        self.log(
            "Allowed component_specific_filters keys: {0}".format(
                allowed_component_filter_keys
            ),
            "DEBUG"
        )

        self.log(
            "Allowed component choices for components_list: {0}".format(
                allowed_component_choices
            ),
            "DEBUG"
        )

        for config_index, config_item in enumerate(self.config, start=1):
            component_filters = config_item.get("component_specific_filters", {})

            if not component_filters:
                self.log(
                    "Configuration item {0}/{1} does not contain "
                    "component_specific_filters - skipping nested validation".format(
                        config_index, len(self.config)
                    ),
                    "DEBUG"
                )
                continue

            self.log(
                "Configuration item {0}/{1} contains component_specific_filters - "
                "validating nested structure with keys: {2}".format(
                    config_index, len(self.config), list(component_filters.keys())
                ),
                "DEBUG"
            )

            # Validate component_specific_filters keys
            filter_keys = set(component_filters.keys())
            invalid_filter_keys = filter_keys - set(allowed_component_filter_keys)

            self.log(
                "Checking component_specific_filters for invalid keys. Found keys: "
                "{0}, Allowed keys: {1}, Invalid keys: {2}".format(
                    list(filter_keys), allowed_component_filter_keys,
                    list(invalid_filter_keys) if invalid_filter_keys else "none"
                ),
                "DEBUG"
            )

            if invalid_filter_keys:
                self.log(
                    "Configuration item {0}/{1} component_specific_filters contains "
                    "{2} invalid key(s): {3}. Allowed keys: {4}".format(
                        config_index, len(self.config), len(invalid_filter_keys),
                        list(invalid_filter_keys), allowed_component_filter_keys
                    ),
                    "ERROR"
                )

                self.msg = (
                    "Invalid keys found in 'component_specific_filters': {0}. "
                    "Only the following keys are allowed: {1}. "
                    "Please correct the parameter names and try again.".format(
                        list(invalid_filter_keys), allowed_component_filter_keys
                    )
                )

                self.log(
                    "Setting operation result to failed due to invalid "
                    "component_specific_filters keys and calling check_return_status "
                    "to exit. Error message: {0}".format(self.msg),
                    "ERROR"
                )

                self.set_operation_result(
                    "failed", False, self.msg, "ERROR"
                ).check_return_status()

            self.log(
                "Configuration item {0}/{1} component_specific_filters passed key "
                "validation".format(config_index, len(self.config)),
                "DEBUG"
            )

            # Validate components_list values
            components_list = component_filters.get("components_list", [])
            if components_list:
                self.log(
                    "Configuration item {0}/{1} contains components_list with {2} "
                    "component(s): {3}".format(
                        config_index, len(self.config), len(components_list),
                        components_list
                    ),
                    "DEBUG"
                )

                if not isinstance(components_list, list):
                    self.msg = "'components_list' must be a list, got: {0}".format(type(components_list).__name__)
                    self.set_operation_result("failed", False, self.msg, "ERROR").check_return_status()

                invalid_components = set(components_list) - set(allowed_component_choices)

                self.log(
                    "Validating component names in components_list. Found "
                    "components: {0}, Allowed: {1}, Invalid: {2}".format(
                        components_list, allowed_component_choices,
                        list(invalid_components) if invalid_components else "none"
                    ),
                    "DEBUG"
                )

                if invalid_components:
                    self.msg = (
                        "Invalid component names found in 'components_list': {0}. "
                        "Only the following components are allowed: {1}. "
                        "Please correct the component names and try again.".format(
                            list(invalid_components), allowed_component_choices
                        )
                    )
                    self.set_operation_result("failed", False, self.msg, "ERROR").check_return_status()

                self.log(
                    "Configuration item {0}/{1} components_list passed validation - "
                    "all component names are valid".format(
                        config_index, len(self.config)
                    ),
                    "DEBUG"
                )

                # Validate queuing_profile nested parameters
                queuing_profile = component_filters.get("queuing_profile", {})
                if queuing_profile:
                    self.log(
                        "Configuration item {0}/{1} contains queuing_profile filters - "
                        "validating nested parameters".format(config_index, len(self.config)),
                        "DEBUG"
                    )

                    if not isinstance(queuing_profile, dict):
                        self.msg = "'queuing_profile' must be a dictionary, got: {0}".format(type(queuing_profile).__name__)
                        self.set_operation_result("failed", False, self.msg, "ERROR").check_return_status()

                    allowed_qp_keys = ["profile_names_list"]
                    qp_keys = set(queuing_profile.keys())
                    invalid_qp_keys = qp_keys - set(allowed_qp_keys)

                    self.log(
                        "Validating queuing_profile keys. Found keys: {0}, Allowed "
                        "keys: {1}, Invalid keys: {2}".format(
                            list(qp_keys), allowed_qp_keys,
                            list(invalid_qp_keys) if invalid_qp_keys else "none"
                        ),
                        "DEBUG"
                    )

                    if invalid_qp_keys:
                        self.msg = (
                            "Invalid keys found in 'queuing_profile': {0}. "
                            "Only the following keys are allowed: {1}. "
                            "Please correct the parameter names and try again.".format(
                                list(invalid_qp_keys), allowed_qp_keys
                            )
                        )
                        self.set_operation_result("failed", False, self.msg, "ERROR").check_return_status()

                    self.log(
                        "Configuration item {0}/{1} queuing_profile passed key "
                        "validation".format(config_index, len(self.config)),
                        "DEBUG"
                    )

                # Validate application_policy nested parameters
                application_policy = component_filters.get("application_policy", {})
                if application_policy:
                    self.log(
                        "Configuration item {0}/{1} contains application_policy filters - "
                        "validating nested parameters".format(config_index, len(self.config)),
                        "DEBUG"
                    )

                    if not isinstance(application_policy, dict):
                        self.msg = "'application_policy' must be a dictionary, got: {0}".format(type(application_policy).__name__)
                        self.set_operation_result("failed", False, self.msg, "ERROR").check_return_status()

                    allowed_ap_keys = ["policy_names_list"]
                    ap_keys = set(application_policy.keys())
                    invalid_ap_keys = ap_keys - set(allowed_ap_keys)

                    self.log(
                        "Validating application_policy keys. Found keys: {0}, Allowed "
                        "keys: {1}, Invalid keys: {2}".format(
                            list(ap_keys), allowed_ap_keys,
                            list(invalid_ap_keys) if invalid_ap_keys else "none"
                        ),
                        "DEBUG"
                    )

                    if invalid_ap_keys:
                        self.log(
                            "Configuration item {0}/{1} application_policy contains {2} "
                            "invalid key(s): {3}. Allowed keys: {4}".format(
                                config_index, len(self.config), len(invalid_ap_keys),
                                list(invalid_ap_keys), allowed_ap_keys
                            ),
                            "ERROR"
                        )

                        self.msg = (
                            "Invalid keys found in 'application_policy': {0}. "
                            "Only the following keys are allowed: {1}. "
                            "Please correct the parameter names and try again.".format(
                                list(invalid_ap_keys), allowed_ap_keys
                            )
                        )

                        self.log(
                            "Setting operation result to failed due to invalid "
                            "application_policy keys and calling check_return_status to "
                            "exit. Error message: {0}".format(self.msg),
                            "ERROR"
                        )

                        self.set_operation_result("failed", False, self.msg, "ERROR").check_return_status()

                    self.log(
                        "Configuration item {0}/{1} application_policy passed key "
                        "validation".format(config_index, len(self.config)),
                        "DEBUG"
                    )
                else:
                    self.log(
                        "Configuration item {0}/{1} does not contain application_policy "
                        "filters - skipping validation".format(
                            config_index, len(self.config)
                        ),
                        "DEBUG"
                    )

        self.log(
            "Completed validation of component_specific_filters for all {0} "
            "configuration item(s)".format(len(self.config)),
            "DEBUG"
        )

        # Run schema validation using validate_list_of_dicts
        self.log(
            "Running schema validation using validate_list_of_dicts with temp_spec "
            "for type checking and default value assignment",
            "DEBUG"
        )

        valid_temp, invalid_params = validate_list_of_dicts(self.config, temp_spec)

        self.log(
            "Schema validation using validate_list_of_dicts completed. Valid items: "
            "{0}, Invalid parameters: {1}".format(
                len(valid_temp) if valid_temp else 0,
                invalid_params if invalid_params else "none"
            ),
            "DEBUG"
        )

        # Validate minimum requirements
        self.log(
            "Running validate_minimum_requirements to check for required fields",
            "DEBUG"
        )

        self.validate_minimum_requirements(valid_temp)

        # Check for invalid parameters from schema validation
        if invalid_params:
            self.log(
                "Schema validation found {0} invalid parameter(s): {1}".format(
                    len(invalid_params), invalid_params
                ),
                "ERROR"
            )

            self.msg = "Invalid parameters in playbook: {0}".format(invalid_params)

            self.log(
                "Setting operation result to failed due to schema validation errors. "
                "Error message: {0}".format(self.msg),
                "ERROR"
            )

            self.set_operation_result("failed", False, self.msg, "ERROR")
            return self

        self.validated_config = valid_temp

        self.log(
            "All validation checks passed successfully. Validated configuration "
            "contains {0} item(s)".format(len(self.validated_config)),
            "INFO"
        )

        self.msg = "Successfully validated playbook configuration parameters"

        self.log(
            "Setting operation result to success. Success message: {0}".format(
                self.msg
            ),
            "INFO"
        )

        self.set_operation_result("success", False, self.msg, "INFO")

        self.log(
            "Input validation completed successfully - configuration is ready for "
            "processing",
            "INFO"
        )

        return self

    def get_workflow_elements_schema(self):
        """
        Constructs and returns the workflow elements schema for application policy components.

        Defines the complete mapping configuration that orchestrates how application policy
        and queuing profile data is retrieved, filtered, transformed, and structured for
        YAML playbook generation. This schema serves as the central configuration registry
        for all supported components in the brownfield discovery process.

        Returns:
            dict: Complete workflow elements schema containing network_elements
                  configuration with all component definitions.
        """
        self.log(
            "Starting construction of workflow elements schema for application "
            "policy brownfield discovery module",
            "DEBUG"
        )

        queuing_profile_config = {
            "filters": {
                "profile_names_list": {
                    "type": "list",
                    "required": False,
                    "elements": "str"
                }
            },
            "reverse_mapping_function": self.queuing_profile_reverse_mapping_spec,
            "api_function": "get_application_policy_queuing_profile",
            "api_family": "application_policy",
            "get_function_name": self.get_queuing_profiles,
        }

        application_policy_config = {
            "filters": {
                "policy_names_list": {
                    "type": "list",
                    "required": False,
                    "elements": "str"
                }
            },
            "reverse_mapping_function": self.application_policy_reverse_mapping_spec,
            "api_function": "get_application_policy",
            "api_family": "application_policy",
            "get_function_name": self.get_application_policies,
        }

        network_elements = {
            "queuing_profile": queuing_profile_config,
            "application_policy": application_policy_config
        }

        schema = {
            "network_elements": network_elements
        }

        self.log(
            "Schema structure ready for use in validation, component iteration, and "
            "API calls throughout brownfield discovery workflow",
            "DEBUG"
        )

        self.log(
            "Component configurations summary: "
            "queuing_profile (filters: {0}, api: {1}), "
            "application_policy (filters: {2}, api: {3})".format(
                list(queuing_profile_config["filters"].keys()),
                queuing_profile_config["api_function"],
                list(application_policy_config["filters"].keys()),
                application_policy_config["api_function"]
            ),
            "DEBUG"
        )

        return schema

    def queuing_profile_reverse_mapping_spec(self):
        """
        Defines reverse mapping specification for transforming queuing profile API data to playbook format.

        This specification serves as the declarative configuration for converting Cisco Catalyst
        Center API response data (queuing profiles) into the structured format expected by the
        application_policy_workflow_manager playbook. It maps API field names to playbook parameter
        names and defines transformation logic for complex nested structures.

        Returns:
            OrderedDict: Reverse mapping specification with field definitions and
                         transformation configurations for queuing profile data.
        """
        self.log(
            "Starting construction of reverse mapping specification for queuing "
            "profile data transformation from API format to playbook format",
            "DEBUG"
        )

        reverse_mapping_spec = OrderedDict({
            "profile_name": {
                "type": "str",
                "source_key": "name"
            },
            "profile_description": {
                "type": "str",
                "source_key": "description"
            },
            "bandwidth_settings": {
                "type": "dict",
                "source_key": "clause",
                "special_handling": True,
                "transform": self.transform_bandwidth_settings
            },
            "dscp_settings": {
                "type": "dict",
                "source_key": "clause",
                "special_handling": True,
                "transform": self.transform_dscp_settings
            }
        })

        self.log(
            "Field mapping summary: profile_name (direct), profile_description (direct), "
            "bandwidth_settings (transform), dscp_settings (transform)",
            "DEBUG"
        )

        self.log(
            "Reverse mapping specification ready for use in queuing profile data "
            "transformation workflow. Specification will ensure consistent field "
            "ordering and proper data type handling.",
            "DEBUG"
        )

        return reverse_mapping_spec

    def application_policy_reverse_mapping_spec(self):
        """
        Defines reverse mapping specification for transforming application policy API data to playbook format.

        This specification serves as the declarative configuration for converting Cisco Catalyst
        Center application policy API response data into the structured format expected by the
        application_policy_workflow_manager playbook. It maps API field names to playbook parameter
        names and defines transformation logic for complex nested structures including site names,
        application sets, and business relevance clauses.

        Returns:
            OrderedDict: Reverse mapping specification with field definitions and
                         transformation configurations for application policy data.
        """
        self.log(
            "Starting construction of reverse mapping specification for application "
            "policy data transformation from API format to playbook format",
            "DEBUG"
        )

        self.log(
            "Initializing reverse mapping with {0} total field mappings including "
            "direct mappings and special transformation functions".format(7),
            "DEBUG"
        )

        reverse_mapping_spec = OrderedDict({
            "name": {"type": "str", "source_key": "policyScope"},
            "policy_status": {
                "type": "str",
                "source_key": "deletePolicyStatus",
                "transform": lambda x: "deployed" if x == "NONE" else x.lower()
            },
            "site_names": {
                "type": "list",
                "elements": "str",
                "source_key": "advancedPolicyScope",
                "special_handling": True,
                "transform": self.transform_site_names
            },
            "device_type": {
                "type": "str",
                "source_key": "advancedPolicyScope",
                "special_handling": True,
                "transform": self.transform_device_type
            },
            "ssid_name": {
                "type": "str",
                "source_key": "advancedPolicyScope",
                "special_handling": True,
                "transform": self.transform_ssid_name
            },
            "application_queuing_profile_name": {
                "type": "str",
                "source_key": "contract",
                "special_handling": True,
                "transform": self.get_queuing_profile_name_from_id
            },
            "clause": {
                "type": "list",
                "elements": "dict",
                "source_key": "consumer",
                "special_handling": True,
                "transform": self.transform_clause
            }
        })

        self.log(
            "Reverse mapping specification constructed successfully with {0} field "
            "definitions. Fields with special handling: {1}. Fields with direct "
            "mapping: {2}. Fields with lambda transforms: {3}".format(
                len(reverse_mapping_spec),
                sum(1 for v in reverse_mapping_spec.values()
                    if v.get("special_handling") and callable(v.get("transform"))),
                sum(1 for v in reverse_mapping_spec.values()
                    if not v.get("special_handling") and not v.get("transform")),
                sum(1 for v in reverse_mapping_spec.values()
                    if v.get("transform") and not v.get("special_handling"))
            ),
            "INFO"
        )

        self.log(
            "Note: Policy consolidation by policyScope happens in "
            "transform_application_policies() before applying this reverse mapping "
            "specification to aggregate multiple sub-policies into single policy entry",
            "DEBUG"
        )

        return reverse_mapping_spec

    def transform_bandwidth_settings(self, clause_data):
        """
        Transforms bandwidth configuration clauses from API response to playbook format.

        This function processes BANDWIDTH and BANDWIDTH_CUSTOM clause types from Cisco Catalyst
        Center queuing profile API responses and converts them into the structured bandwidth
        settings format expected by the application_policy_workflow_manager playbook.

        Args:
            clause_data (list): List of clause dictionaries from queuing profile API response.
                               Expected to contain BANDWIDTH or BANDWIDTH_CUSTOM clause types
                               with nested interfaceSpeedBandwidthClauses structures.

        Returns:
            dict or None: Transformed bandwidth settings dictionary in playbook format.
                         Returns None if:
                         - clause_data is None or empty
                         - clause_data is not a list
                         - No BANDWIDTH/BANDWIDTH_CUSTOM clauses found
                         - No valid interfaceSpeedBandwidthClauses in clauses
        """
        self.log(
            "Starting transformation of bandwidth settings from clause data for queuing "
            "profile configuration",
            "DEBUG"
        )

        if not clause_data or not isinstance(clause_data, list):
            self.log(
                "Bandwidth settings transformation skipped - invalid clause data provided. "
                "Expected list of clause dictionaries, got: {0}".format(
                    type(clause_data).__name__ if clause_data else "None"
                ),
                "DEBUG"
            )
            return None

        self.log(
            "Received {0} clause(s) to process for bandwidth settings extraction. "
            "Searching for BANDWIDTH or BANDWIDTH_CUSTOM clause types.".format(
                len(clause_data)
            ),
            "DEBUG"
        )

        # Traffic class mapping from API format to playbook format
        tc_map = {
            "BROADCAST_VIDEO": "broadcast_video",
            "BULK_DATA": "bulk_data",
            "MULTIMEDIA_CONFERENCING": "multimedia_conferencing",
            "MULTIMEDIA_STREAMING": "multimedia_streaming",
            "NETWORK_CONTROL": "network_control",
            "OPS_ADMIN_MGMT": "ops_admin_mgmt",
            "REAL_TIME_INTERACTIVE": "real_time_interactive",
            "SIGNALING": "signaling",
            "TRANSACTIONAL_DATA": "transactional_data",
            "VOIP_TELEPHONY": "voip_telephony",
            "BEST_EFFORT": "best_effort",
            "SCAVENGER": "scavenger"
        }

        self.log(
            "Traffic class mapping table initialized with {0} traffic class entries for "
            "converting API format (uppercase with underscores) to playbook format "
            "(lowercase with underscores)".format(len(tc_map)),
            "DEBUG"
        )

        bandwidth_settings = None

        # Iterate through clauses to find bandwidth configuration
        for clause_index, clause in enumerate(clause_data, start=1):
            self.log(
                "Processing clause {0}/{1} to check for bandwidth configuration. "
                "Clause type check in progress.".format(clause_index, len(clause_data)),
                "DEBUG"
            )

            if not isinstance(clause, dict):
                self.log(
                    "Clause {0}/{1} is not a dictionary - skipping. Expected dict, got: "
                    "{2}".format(
                        clause_index, len(clause_data), type(clause).__name__
                    ),
                    "WARNING"
                )
                continue

            clause_type = clause.get("type")
            # Process BANDWIDTH or BANDWIDTH_CUSTOM clause types
            if clause_type in ["BANDWIDTH", "BANDWIDTH_CUSTOM"]:
                self.log(
                    "Found bandwidth clause at position {0}/{1} with type '{2}'. "
                    "Extracting bandwidth configuration settings.".format(
                        clause_index, len(clause_data), clause_type
                    ),
                    "INFO"
                )

                is_common = clause.get("isCommonBetweenAllInterfaceSpeeds", False)

                self.log(
                    "Bandwidth configuration mode determined: {0}. Settings are {1} "
                    "across all interface speeds.".format(
                        "common" if is_common else "interface-specific",
                        "common" if is_common else "NOT common"
                    ),
                    "INFO"
                )

                # Extract interface speed bandwidth clauses
                interface_speed_clauses = clause.get("interfaceSpeedBandwidthClauses", [])

                if not interface_speed_clauses:
                    self.log(
                        "No interfaceSpeedBandwidthClauses found in bandwidth clause "
                        "{0}/{1}. This clause will be skipped as it contains no bandwidth "
                        "allocation data. Check if API response structure is valid.".format(
                            clause_index, len(clause_data)
                        ),
                        "WARNING"
                    )
                    continue

                self.log(
                    "Found {0} interface speed bandwidth clause(s) in bandwidth clause "
                    "{1}/{2}. Processing bandwidth allocations for each interface speed.".format(
                        len(interface_speed_clauses), clause_index, len(clause_data)
                    ),
                    "DEBUG"
                )

                if is_common:
                    # Common bandwidth settings across all interface speeds
                    self.log(
                        "Processing common bandwidth settings (applies to ALL interface "
                        "speeds). Building bandwidth_settings structure with "
                        "is_common_between_all_interface_speeds=true and "
                        "interface_speed='ALL'.",
                        "INFO"
                    )

                    bandwidth_settings = OrderedDict([
                        ("is_common_between_all_interface_speeds", True),
                        ("interface_speed", "ALL"),
                        ("bandwidth_percentages", OrderedDict())
                    ])

                    self.log(
                        "Initialized common bandwidth settings structure. Extracting "
                        "traffic class bandwidth percentages from first interface speed "
                        "clause (should be 'ALL' interface speed).",
                        "DEBUG"
                    )
                    if len(interface_speed_clauses) > 0:
                        first_speed_clause = interface_speed_clauses[0]
                        interface_speed_value = first_speed_clause.get("interfaceSpeed", "ALL")

                        self.log(
                            "Processing interface speed clause with speed: '{0}'. Expected "
                            "'ALL' for common bandwidth settings.".format(
                                interface_speed_value
                            ),
                            "DEBUG"
                        )

                        tc_bandwidth_settings = first_speed_clause.get("tcBandwidthSettings", [])

                        self.log(
                            "Found {0} traffic class bandwidth setting(s) in interface "
                            "speed clause. Processing each traffic class allocation.".format(
                                len(tc_bandwidth_settings)
                            ),
                            "INFO"
                        )

                        for tc_index, tc_setting in enumerate(tc_bandwidth_settings, start=1):
                            tc_name = tc_setting.get("trafficClass")
                            bandwidth_percent = tc_setting.get("bandwidthPercentage")

                            self.log(
                                "Processing traffic class {0}/{1}: API name='{2}', "
                                "bandwidth percentage={3}. Checking if traffic class is in "
                                "mapping table.".format(
                                    tc_index, len(tc_bandwidth_settings), tc_name,
                                    bandwidth_percent
                                ),
                                "DEBUG"
                            )

                            if tc_name in tc_map and bandwidth_percent is not None:
                                playbook_tc_name = tc_map[tc_name]
                                bandwidth_settings["bandwidth_percentages"][playbook_tc_name] = str(
                                    bandwidth_percent
                                )

                                self.log(
                                    "Successfully mapped traffic class {0}/{1}: '{2}' → "
                                    "'{3}' with bandwidth allocation {4}%. Added to "
                                    "bandwidth_percentages dictionary.".format(
                                        tc_index, len(tc_bandwidth_settings), tc_name,
                                        playbook_tc_name, bandwidth_percent
                                    ),
                                    "DEBUG"
                                )
                            else:
                                skip_reason = (
                                    "traffic class not in mapping table" if tc_name not in tc_map
                                    else "bandwidth percentage is None"
                                )
                                self.log(
                                    "Skipping traffic class {0}/{1}: '{2}' - {3}. This "
                                    "traffic class will not be included in bandwidth "
                                    "settings.".format(
                                        tc_index, len(tc_bandwidth_settings), tc_name,
                                        skip_reason
                                    ),
                                    "WARNING"
                                )

                        self.log(
                            "Completed processing common bandwidth settings. Total traffic "
                            "classes configured: {0}. Total bandwidth allocated: {1}% "
                            "(should typically sum to 100%).".format(
                                len(bandwidth_settings["bandwidth_percentages"]),
                                sum(int(v) for v in bandwidth_settings["bandwidth_percentages"].values())
                            ),
                            "INFO"
                        )
                    else:
                        self.log(
                            "No interface speed clauses found in common bandwidth settings. "
                            "This is unexpected - bandwidth settings may be incomplete.",
                            "WARNING"
                        )
                else:
                    # Interface-specific bandwidth settings
                    self.log(
                        "Processing interface-specific bandwidth settings (different "
                        "allocations per interface speed). Building bandwidth_settings "
                        "structure with is_common_between_all_interface_speeds=false and "
                        "interface_speed_settings list.",
                        "INFO"
                    )

                    bandwidth_settings = OrderedDict([
                        ("is_common_between_all_interface_speeds", False),
                        ("interface_speed_settings", [])
                    ])

                    self.log(
                        "Initialized interface-specific bandwidth settings structure. "
                        "Processing {0} interface speed clause(s) individually.".format(
                            len(interface_speed_clauses)
                        ),
                        "DEBUG"
                    )

                    for speed_index, speed_clause in enumerate(interface_speed_clauses, start=1):
                        interface_speed = speed_clause.get("interfaceSpeed")

                        self.log(
                            "Processing interface speed clause {0}/{1} for interface speed: "
                            "'{2}'. Extracting traffic class bandwidth allocations specific "
                            "to this interface speed.".format(
                                speed_index, len(interface_speed_clauses), interface_speed
                            ),
                            "INFO"
                        )

                        tc_bandwidth_settings = speed_clause.get("tcBandwidthSettings", [])

                        self.log(
                            "Found {0} traffic class bandwidth setting(s) for interface "
                            "speed '{1}'. Processing allocations.".format(
                                len(tc_bandwidth_settings), interface_speed
                            ),
                            "DEBUG"
                        )
                        speed_setting = OrderedDict([
                            ("interface_speed", interface_speed),
                            ("bandwidth_percentages", OrderedDict())
                        ])

                        for tc_index, tc_setting in enumerate(tc_bandwidth_settings, start=1):
                            tc_name = tc_setting.get("trafficClass")
                            bandwidth_percent = tc_setting.get("bandwidthPercentage")

                            self.log(
                                "Processing traffic class {0}/{1} for interface speed "
                                "'{2}': API name='{3}', bandwidth={4}%. Mapping to playbook "
                                "format.".format(
                                    tc_index, len(tc_bandwidth_settings), interface_speed,
                                    tc_name, bandwidth_percent
                                ),
                                "DEBUG"
                            )

                            if tc_name in tc_map and bandwidth_percent is not None:
                                playbook_tc_name = tc_map[tc_name]
                                speed_setting["bandwidth_percentages"][playbook_tc_name] = str(
                                    bandwidth_percent
                                )

                                self.log(
                                    "Successfully mapped traffic class {0}/{1} for interface "
                                    "speed '{2}': '{3}' → '{4}' with {5}% bandwidth.".format(
                                        tc_index, len(tc_bandwidth_settings), interface_speed,
                                        tc_name, playbook_tc_name, bandwidth_percent
                                    ),
                                    "DEBUG"
                                )
                            else:
                                skip_reason = (
                                    "traffic class not in mapping table" if tc_name not in tc_map
                                    else "bandwidth percentage is None"
                                )
                                self.log(
                                    "Skipping traffic class {0}/{1} for interface speed "
                                    "'{2}': '{3}' - {4}.".format(
                                        tc_index, len(tc_bandwidth_settings), interface_speed,
                                        tc_name, skip_reason
                                    ),
                                    "WARNING"
                                )
                        bandwidth_settings["interface_speed_settings"].append(speed_setting)

                        self.log(
                            "Completed processing interface speed '{0}' ({1}/{2}). Traffic "
                            "classes configured: {3}. Total bandwidth: {4}%.".format(
                                interface_speed, speed_index, len(interface_speed_clauses),
                                len(speed_setting["bandwidth_percentages"]),
                                sum(int(v) for v in speed_setting["bandwidth_percentages"].values())
                            ),
                            "INFO"
                        )

                    self.log(
                        "Completed processing all interface-specific bandwidth settings. "
                        "Total interface speeds configured: {0}.".format(
                            len(bandwidth_settings["interface_speed_settings"])
                        ),
                        "INFO"
                    )

                # Exit after processing first BANDWIDTH/BANDWIDTH_CUSTOM clause
                self.log(
                    "Bandwidth clause processing complete. Found and processed {0} "
                    "bandwidth clause (type: '{1}'). Returning bandwidth settings. "
                    "Subsequent clauses will not be processed.".format(
                        "common" if is_common else "interface-specific", clause_type
                    ),
                    "INFO"
                )
                break
            else:
                self.log(
                    "Clause {0}/{1} with type '{2}' is not a bandwidth clause - skipping. "
                    "Only BANDWIDTH and BANDWIDTH_CUSTOM clause types are processed by "
                    "this function.".format(clause_index, len(clause_data), clause_type),
                    "DEBUG"
                )

        if bandwidth_settings:
            is_common_result = bandwidth_settings.get("is_common_between_all_interface_speeds")
            if is_common_result:
                tc_count = len(bandwidth_settings.get("bandwidth_percentages", {}))
                total_bandwidth = sum(
                    int(v) for v in bandwidth_settings.get("bandwidth_percentages", {}).values()
                )
                self.log(
                    "Bandwidth settings transformation completed successfully. Mode: common "
                    "across all interface speeds. Traffic classes configured: {0}. Total "
                    "bandwidth allocated: {1}%. Returning bandwidth settings dictionary.".format(
                        tc_count, total_bandwidth
                    ),
                    "INFO"
                )
            else:
                speed_count = len(bandwidth_settings.get("interface_speed_settings", []))
                self.log(
                    "Bandwidth settings transformation completed successfully. Mode: "
                    "interface-specific. Interface speeds configured: {0}. Returning "
                    "bandwidth settings dictionary.".format(speed_count),
                    "INFO"
                )
        else:
            self.log(
                "Bandwidth settings transformation completed with no bandwidth configuration "
                "found. No BANDWIDTH or BANDWIDTH_CUSTOM clauses were found in the {0} "
                "clause(s) provided. Returning None.".format(len(clause_data)),
                "WARNING"
            )

        return bandwidth_settings

    def transform_dscp_settings(self, clause_data):
        """
        Transforms DSCP configuration clauses from API response to playbook format.

        This function processes DSCP_CUSTOMIZATION clause types from Cisco Catalyst Center
        queuing profile API responses and converts them into the structured DSCP settings
        format expected by the application_policy_workflow_manager playbook.

        Args:
            clause_data (list): List of clause dictionaries from queuing profile API response.
                               Expected to contain DSCP_CUSTOMIZATION clause type with nested
                               tcDscpSettings array containing traffic class DSCP mappings.

        Returns:
            OrderedDict or None: DSCP settings dictionary in playbook format with traffic class
                                names as keys and DSCP values as string values.
                                Returns None if:
                                - clause_data is None or empty
                                - clause_data is not a list
                                - No DSCP_CUSTOMIZATION clause found
                                - No valid tcDscpSettings in DSCP_CUSTOMIZATION clause
        """
        self.log(
            "Starting transformation of DSCP settings from clause data for queuing "
            "profile QoS packet marking configuration",
            "DEBUG"
        )

        # Validate input clause_data
        if not clause_data or not isinstance(clause_data, list):
            self.log(
                "DSCP settings transformation skipped - invalid clause data provided. "
                "Expected list of clause dictionaries, got: {0}".format(
                    type(clause_data).__name__ if clause_data is not None else "None"
                ),
                "WARNING"
            )
            return None

        self.log(
            "Received {0} clause(s) to process for DSCP settings extraction. Searching "
            "for DSCP_CUSTOMIZATION clause type.".format(len(clause_data)),
            "DEBUG"
        )

        # Traffic class mapping from API format to playbook format
        tc_map = {
            "BROADCAST_VIDEO": "broadcast_video",
            "BULK_DATA": "bulk_data",
            "MULTIMEDIA_CONFERENCING": "multimedia_conferencing",
            "MULTIMEDIA_STREAMING": "multimedia_streaming",
            "NETWORK_CONTROL": "network_control",
            "OPS_ADMIN_MGMT": "ops_admin_mgmt",
            "REAL_TIME_INTERACTIVE": "real_time_interactive",
            "SIGNALING": "signaling",
            "TRANSACTIONAL_DATA": "transactional_data",
            "VOIP_TELEPHONY": "voip_telephony",
            "BEST_EFFORT": "best_effort",
            "SCAVENGER": "scavenger"
        }

        self.log(
            "Traffic class mapping table initialized with {0} traffic class entries for "
            "converting API format (uppercase with underscores) to playbook format "
            "(lowercase with underscores)".format(len(tc_map)),
            "DEBUG"
        )

        dscp_settings = None

        # Iterate through clauses to find DSCP customization
        for clause_index, clause in enumerate(clause_data, start=1):
            self.log(
                "Processing clause {0}/{1} to check for DSCP customization configuration. "
                "Clause type check in progress.".format(clause_index, len(clause_data)),
                "DEBUG"
            )

            if not isinstance(clause, dict):
                self.log(
                    "Clause {0}/{1} is not a dictionary - skipping. Expected dict, got: "
                    "{2}".format(
                        clause_index, len(clause_data), type(clause).__name__
                    ),
                    "WARNING"
                )
                continue

            clause_type = clause.get("type")

            self.log(
                "Clause {0}/{1} has type: '{2}'. Checking if this is a DSCP customization "
                "clause (DSCP_CUSTOMIZATION).".format(
                    clause_index, len(clause_data), clause_type
                ),
                "DEBUG"
            )

            # Process DSCP_CUSTOMIZATION clause type
            if clause_type == "DSCP_CUSTOMIZATION":
                self.log(
                    "Found DSCP customization clause at position {0}/{1}. Extracting "
                    "traffic class DSCP value mappings for QoS packet marking.".format(
                        clause_index, len(clause_data)
                    ),
                    "INFO"
                )

                # Extract DSCP values for each traffic class
                tc_dscp_settings = clause.get("tcDscpSettings", [])

                if not tc_dscp_settings:
                    self.log(
                        "No tcDscpSettings found in DSCP_CUSTOMIZATION clause {0}/{1}. "
                        "This clause will be skipped as it contains no DSCP value mappings. "
                        "Check if API response structure is valid.".format(
                            clause_index, len(clause_data)
                        ),
                        "WARNING"
                    )
                    continue

                self.log(
                    "Found {0} traffic class DSCP setting(s) in DSCP_CUSTOMIZATION clause "
                    "{1}/{2}. Processing DSCP values for each traffic class.".format(
                        len(tc_dscp_settings), clause_index, len(clause_data)
                    ),
                    "INFO"
                )

                # Initialize DSCP settings dictionary
                dscp_settings = OrderedDict()

                self.log(
                    "Initialized DSCP settings OrderedDict for storing traffic class to "
                    "DSCP value mappings in consistent order",
                    "DEBUG"
                )

                # Process each traffic class DSCP setting
                for tc_index, tc_setting in enumerate(tc_dscp_settings, start=1):
                    tc_name = tc_setting.get("trafficClass")
                    dscp_value = tc_setting.get("dscp")

                    self.log(
                        "Processing traffic class {0}/{1}: API name='{2}', DSCP value={3}. "
                        "Checking if traffic class is in mapping table.".format(
                            tc_index, len(tc_dscp_settings), tc_name, dscp_value
                        ),
                        "DEBUG"
                    )

                    if tc_name in tc_map and dscp_value is not None:
                        playbook_tc_name = tc_map[tc_name]
                        dscp_settings[playbook_tc_name] = str(dscp_value)

                        self.log(
                            "Successfully mapped traffic class {0}/{1}: '{2}' → '{3}' with "
                            "DSCP value {4}. Added to DSCP settings dictionary.".format(
                                tc_index, len(tc_dscp_settings), tc_name, playbook_tc_name,
                                dscp_value
                            ),
                            "DEBUG"
                        )
                    else:
                        skip_reason = (
                            "traffic class not in mapping table" if tc_name not in tc_map
                            else "DSCP value is None"
                        )
                        self.log(
                            "Skipping traffic class {0}/{1}: '{2}' - {3}. This traffic "
                            "class will not be included in DSCP settings.".format(
                                tc_index, len(tc_dscp_settings), tc_name, skip_reason
                            ),
                            "WARNING"
                        )
                self.log(
                    "Completed processing DSCP_CUSTOMIZATION clause. Total traffic classes "
                    "configured: {0}. Returning DSCP settings dictionary.".format(
                        len(dscp_settings)
                    ),
                    "INFO"
                )

                # Exit after processing first DSCP_CUSTOMIZATION clause
                self.log(
                    "DSCP customization clause processing complete. Found and processed "
                    "DSCP_CUSTOMIZATION clause at position {0}/{1}. Returning DSCP "
                    "settings. Subsequent clauses will not be processed.".format(
                        clause_index, len(clause_data)
                    ),
                    "INFO"
                )
                break
            else:
                self.log(
                    "Clause {0}/{1} with type '{2}' is not a DSCP customization clause - "
                    "skipping. Only DSCP_CUSTOMIZATION clause type is processed by this "
                    "function.".format(clause_index, len(clause_data), clause_type),
                    "DEBUG"
                )

        if dscp_settings:
            self.log(
                "DSCP settings transformation completed successfully. Total traffic classes "
                "with DSCP values configured: {0}. DSCP value range: {1} to {2}. "
                "Returning DSCP settings dictionary.".format(
                    len(dscp_settings),
                    min(int(v) for v in dscp_settings.values()) if dscp_settings else 0,
                    max(int(v) for v in dscp_settings.values()) if dscp_settings else 0
                ),
                "INFO"
            )
        else:
            self.log(
                "DSCP settings transformation completed with no DSCP configuration found. "
                "No DSCP_CUSTOMIZATION clauses were found in the {0} clause(s) provided. "
                "Returning None.".format(len(clause_data)),
                "WARNING"
            )

        return dscp_settings

    def transform_site_names(self, advanced_policy_scope):
        """
        Transforms site UUIDs from advanced policy scope to human-readable hierarchical site names.

        This function extracts site group IDs (UUIDs) from the advancedPolicyScope structure in
        application policy API responses and resolves them to their full hierarchical site names
        (e.g., "Global/USA/San Jose/Building-1") for playbook compatibility.

        Args:
            advanced_policy_scope (dict): Advanced policy scope dictionary from API response
                                         containing advancedPolicyScopeElement array with
                                         groupId (site UUID) arrays.

        Returns:
            list: List of hierarchical site name strings (e.g., ["Global/USA/San Jose"]).
                  Returns empty list if:
                  - advanced_policy_scope is None or invalid type
                  - advancedPolicyScopeElement is missing or invalid
                  - No valid site UUIDs found
                  - All site UUID resolutions fail
        """
        self.log(
            "Starting transformation of site UUIDs to hierarchical site names from "
            "advanced policy scope data",
            "DEBUG"
        )

        # Validate input advanced_policy_scope
        if not advanced_policy_scope or not isinstance(advanced_policy_scope, dict):
            self.log(
                "Site name transformation skipped - invalid advanced policy scope provided. "
                "Expected dict, got: {0}".format(
                    type(advanced_policy_scope).__name__ if advanced_policy_scope is not None
                    else "None"
                ),
                "WARNING"
            )
            return []

        self.log(
            "Received valid advanced policy scope dictionary. Extracting site group IDs "
            "from advancedPolicyScopeElement array.",
            "DEBUG"
        )

        site_ids = []
        advanced_policy_scope_elements = advanced_policy_scope.get("advancedPolicyScopeElement", [])

        if not isinstance(advanced_policy_scope_elements, list):
            self.log(
                "Site name transformation skipped - advancedPolicyScopeElement is not a list. "
                "Expected list, got: {0}".format(
                    type(advanced_policy_scope_elements).__name__
                ),
                "WARNING"
            )
            return []

        self.log(
            "Found {0} advanced policy scope element(s) to process for site group ID "
            "extraction.".format(len(advanced_policy_scope_elements)),
            "DEBUG"
        )

        # Extract site IDs from all elements
        for element_index, element in enumerate(advanced_policy_scope_elements, start=1):
            self.log(
                "Processing advanced policy scope element {0}/{1} to extract site group "
                "IDs (UUIDs).".format(element_index, len(advanced_policy_scope_elements)),
                "DEBUG"
            )

            if not isinstance(element, dict):
                self.log(
                    "Advanced policy scope element {0}/{1} is not a dictionary - skipping. "
                    "Expected dict, got: {2}".format(
                        element_index, len(advanced_policy_scope_elements),
                        type(element).__name__
                    ),
                    "WARNING"
                )
                continue

            group_ids = element.get("groupId", [])

            if not isinstance(group_ids, list):
                self.log(
                    "groupId in element {0}/{1} is not a list - skipping. Expected list, "
                    "got: {2}".format(
                        element_index, len(advanced_policy_scope_elements),
                        type(group_ids).__name__
                    ),
                    "WARNING"
                )
                continue
            if group_ids:
                self.log(
                    "Found {0} site group ID(s) in element {1}/{2}. Adding to site ID "
                    "collection.".format(
                        len(group_ids), element_index, len(advanced_policy_scope_elements)
                    ),
                    "DEBUG"
                )
                site_ids.extend(group_ids)
            else:
                self.log(
                    "Element {0}/{1} has empty groupId array - no site IDs to extract.".format(
                        element_index, len(advanced_policy_scope_elements)
                    ),
                    "DEBUG"
                )

        self.log(
            "Completed site ID extraction. Total site UUIDs collected: {0}. Starting "
            "site name resolution via get_site_name API calls.".format(len(site_ids)),
            "INFO"
        )

        if not site_ids:
            self.log(
                "No site UUIDs found in advanced policy scope elements. Returning empty "
                "site names list.",
                "WARNING"
            )
            return []

        # Resolve site IDs to hierarchical site names
        site_names = []
        for site_index, site_id in enumerate(site_ids, start=1):
            self.log(
                "Resolving site UUID {0}/{1}: '{2}' to hierarchical site name via "
                "get_site_name API call.".format(site_index, len(site_ids), site_id),
                "DEBUG"
            )

            site_name = self.get_site_name(site_id)

            if site_name:
                site_names.append(site_name)
                self.log(
                    "Successfully resolved site UUID {0}/{1}: '{2}' → '{3}'. Added to "
                    "site names list.".format(site_index, len(site_ids), site_id, site_name),
                    "INFO"
                )
            else:
                self.log(
                    "Failed to resolve site UUID {0}/{1}: '{2}'. Site name not found in "
                    "Catalyst Center or API call failed. Excluding from site names list.".format(
                        site_index, len(site_ids), site_id
                    ),
                    "WARNING"
                )

        self.log(
            "Site name transformation completed. Successfully resolved {0} out of {1} "
            "site UUIDs to hierarchical site names. Site names: {2}".format(
                len(site_names), len(site_ids), site_names
            ),
            "INFO"
        )

        if len(site_names) < len(site_ids):
            failed_count = len(site_ids) - len(site_names)
            self.log(
                "Warning: {0} site UUID(s) failed to resolve to site names. This may "
                "indicate deleted sites or invalid UUIDs in the policy configuration.".format(
                    failed_count
                ),
                "WARNING"
            )

        return site_names

    def transform_device_type(self, advanced_policy_scope):
        """
        Determines device type (wired or wireless) from advanced policy scope configuration.

        This function analyzes the advancedPolicyScope structure from application policy API
        responses to determine whether the policy applies to wired or wireless devices based
        on the presence of SSID configuration.

        Args:
            advanced_policy_scope (dict): Advanced policy scope dictionary from API response
                                         containing advancedPolicyScopeElement array with
                                         optional ssid field.

        Returns:
            str: Device type - "wireless" if SSID present, "wired" otherwise.
                 Always returns a string (never None).
                 Default return value is "wired" for all error/edge cases.
        """
        self.log(
            "Starting device type determination from advanced policy scope configuration",
            "DEBUG"
        )

        if not advanced_policy_scope or not isinstance(advanced_policy_scope, dict):
            self.log(
                "Device type determination defaulting to 'wired' - invalid advanced policy "
                "scope provided. Expected dict, got: {0}".format(
                    type(advanced_policy_scope).__name__ if advanced_policy_scope is not None
                    else "None"
                ),
                "WARNING"
            )
            return "wired"

        self.log(
            "Received valid advanced policy scope dictionary. Extracting "
            "advancedPolicyScopeElement array to check for SSID presence.",
            "DEBUG"
        )

        advanced_policy_scope_elements = advanced_policy_scope.get("advancedPolicyScopeElement", [])

        if not isinstance(advanced_policy_scope_elements, list):
            self.log(
                "Device type determination defaulting to 'wired' - "
                "advancedPolicyScopeElement is not a list. Expected list, got: {0}".format(
                    type(advanced_policy_scope_elements).__name__
                ),
                "WARNING"
            )
            return "wired"

        if not advanced_policy_scope_elements:
            self.log(
                "Device type determination defaulting to 'wired' - "
                "advancedPolicyScopeElement array is empty (no policy scope elements found).",
                "DEBUG"
            )
            return "wired"

        self.log(
            "Found {0} advanced policy scope element(s) to check for SSID presence. "
            "Iterating to detect wireless configuration.".format(
                len(advanced_policy_scope_elements)
            ),
            "DEBUG"
        )

        for element_index, element in enumerate(advanced_policy_scope_elements, start=1):
            self.log(
                "Checking advanced policy scope element {0}/{1} for SSID field to "
                "determine wireless policy.".format(
                    element_index, len(advanced_policy_scope_elements)
                ),
                "DEBUG"
            )

            if not isinstance(element, dict):
                self.log(
                    "Advanced policy scope element {0}/{1} is not a dictionary - skipping. "
                    "Expected dict, got: {2}".format(
                        element_index, len(advanced_policy_scope_elements),
                        type(element).__name__
                    ),
                    "WARNING"
                )
                continue

            ssid = element.get("ssid")

            self.log(
                "Advanced policy scope element {0}/{1} SSID field value: {2} (type: {3})".format(
                    element_index, len(advanced_policy_scope_elements),
                    ssid, type(ssid).__name__ if ssid is not None else "None"
                ),
                "DEBUG"
            )

            if ssid:
                self.log(
                    "SSID detected in advanced policy scope element {0}/{1}. SSID value: {2}. "
                    "Device type determined as 'wireless'. Terminating search.".format(
                        element_index, len(advanced_policy_scope_elements), ssid
                    ),
                    "INFO"
                )
                return "wireless"
            else:
                self.log(
                    "No SSID found in advanced policy scope element {0}/{1} (SSID is None, "
                    "empty, or not present). Continuing to check remaining elements.".format(
                        element_index, len(advanced_policy_scope_elements)
                    ),
                    "DEBUG"
                )

        self.log(
            "Completed checking all {0} advanced policy scope element(s). No SSID found in "
            "any element. Device type determined as 'wired' (default).".format(
                len(advanced_policy_scope_elements)
            ),
            "INFO"
        )

        return "wired"

    def transform_ssid_name(self, advanced_policy_scope):
        """
        Extracts SSID name from advanced policy scope for wireless application policies.

        This function analyzes the advancedPolicyScope structure from application policy API
        responses to extract the SSID (Service Set Identifier) name for wireless policies.
        The SSID name is required for wireless policies and should be None/excluded for wired
        policies.

        Args:
            advanced_policy_scope (dict): Advanced policy scope dictionary from API response
                                         containing advancedPolicyScopeElement array with
                                         optional ssid field.

        Returns:
            str or None: SSID name string if found in wireless policy, None for wired policies
                        or if no SSID is configured. None values are filtered out during YAML
                        generation, so wired policies won't have ssid_name field.
        """
        self.log(
            "Starting SSID name extraction from advanced policy scope for wireless policy "
            "identification",
            "DEBUG"
        )

        if not advanced_policy_scope or not isinstance(advanced_policy_scope, dict):
            self.log(
                "SSID name extraction returning None - invalid advanced policy scope provided. "
                "Expected dict, got: {0}. This indicates a wired policy or invalid data.".format(
                    type(advanced_policy_scope).__name__ if advanced_policy_scope is not None
                    else "None"
                ),
                "DEBUG"
            )
            return None

        self.log(
            "Received valid advanced policy scope dictionary. Extracting "
            "advancedPolicyScopeElement array to check for SSID configuration.",
            "DEBUG"
        )

        advanced_policy_scope_elements = advanced_policy_scope.get("advancedPolicyScopeElement", [])

        if not isinstance(advanced_policy_scope_elements, list):
            self.log(
                "SSID name extraction returning None - advancedPolicyScopeElement is not a "
                "list. Expected list, got: {0}. This indicates invalid policy data.".format(
                    type(advanced_policy_scope_elements).__name__
                ),
                "WARNING"
            )
            return None

        if not advanced_policy_scope_elements:
            self.log(
                "SSID name extraction returning None - advancedPolicyScopeElement array is "
                "empty (no policy scope elements found). This indicates a wired policy or "
                "invalid configuration.",
                "DEBUG"
            )
            return None

        self.log(
            "Found {0} advanced policy scope element(s) to check for SSID configuration. "
            "Iterating to extract SSID name for wireless policy.".format(
                len(advanced_policy_scope_elements)
            ),
            "DEBUG"
        )

        # Check each element for SSID presence
        for element_index, element in enumerate(advanced_policy_scope_elements, start=1):
            self.log(
                "Checking advanced policy scope element {0}/{1} for SSID field to extract "
                "wireless network identifier.".format(
                    element_index, len(advanced_policy_scope_elements)
                ),
                "DEBUG"
            )

            if not isinstance(element, dict):
                self.log(
                    "Advanced policy scope element {0}/{1} is not a dictionary - skipping. "
                    "Expected dict, got: {2}. Continuing to next element.".format(
                        element_index, len(advanced_policy_scope_elements),
                        type(element).__name__
                    ),
                    "WARNING"
                )
                continue

            ssid = element.get("ssid")

            self.log(
                "Advanced policy scope element {0}/{1} SSID field value: {2} (type: {3})".format(
                    element_index, len(advanced_policy_scope_elements),
                    ssid if ssid else "None/null/empty",
                    type(ssid).__name__ if ssid is not None else "NoneType"
                ),
                "DEBUG"
            )

            if ssid:
                # Handle SSID as list (typical format)
                if isinstance(ssid, list) and len(ssid) > 0:
                    ssid_name = ssid[0]
                    self.log(
                        "SSID found as list in element {0}/{1}. Extracting first SSID from "
                        "list: '{2}'. Total SSIDs in list: {3}. Returning SSID name and "
                        "terminating search.".format(
                            element_index, len(advanced_policy_scope_elements), ssid_name,
                            len(ssid)
                        ),
                        "INFO"
                    )
                    return ssid_name
                # Handle SSID as string (legacy format or direct string value)
                elif isinstance(ssid, str):
                    self.log(
                        "SSID found as string in element {0}/{1}. SSID name: '{2}'. "
                        "Returning SSID name and terminating search.".format(
                            element_index, len(advanced_policy_scope_elements), ssid
                        ),
                        "INFO"
                    )
                    return ssid
                else:
                    self.log(
                        "SSID field in element {0}/{1} has unexpected type or is empty. "
                        "Type: {2}, Value: {3}. Continuing to next element.".format(
                            element_index, len(advanced_policy_scope_elements),
                            type(ssid).__name__, ssid
                        ),
                        "DEBUG"
                    )
            else:
                self.log(
                    "No SSID found in advanced policy scope element {0}/{1} (SSID is None, "
                    "null, empty list, or empty string). Continuing to check remaining "
                    "elements.".format(element_index, len(advanced_policy_scope_elements)),
                    "DEBUG"
                )

        self.log(
            "Completed checking all {0} advanced policy scope element(s). No SSID found in "
            "any element. Returning None. This indicates a wired policy or policy without "
            "SSID configuration.".format(len(advanced_policy_scope_elements)),
            "INFO"
        )

        return None

    def get_queuing_profile_name_from_id(self, contract_data):
        """
        Retrieves queuing profile name by resolving profile ID from contract data.

        This function extracts the queuing profile ID reference from application policy
        contract data and queries the Cisco Catalyst Center API to resolve the ID to its
        human-readable profile name for playbook compatibility.

        Args:
            contract_data (dict): Contract dictionary from application policy API response
                                 containing idRef field with queuing profile UUID.

        Returns:
            str or None: Queuing profile name if successfully resolved, None if:
                        - contract_data is None or invalid type
                        - idRef is missing from contract_data
                        - API call fails or returns no data
                        - Profile not found in Catalyst Center
                        - Response structure is invalid
        """
        self.log(
            "Starting queuing profile name resolution from contract data reference",
            "DEBUG"
        )

        if not contract_data or not isinstance(contract_data, dict):
            self.log(
                "Queuing profile name resolution returning None - invalid contract data "
                "provided. Expected dict with idRef field, got: {0}. This indicates the "
                "application policy has no QoS profile assigned.".format(
                    type(contract_data).__name__ if contract_data is not None else "None"
                ),
                "DEBUG"
            )
            return None

        self.log(
            "Received valid contract data dictionary. Extracting queuing profile ID "
            "reference (idRef) for API lookup.",
            "DEBUG"
        )

        profile_id = contract_data.get("idRef")
        if not profile_id:
            self.log(
                "Queuing profile name resolution returning None - no profile ID (idRef) "
                "found in contract data. Contract data keys: {0}. This indicates the "
                "application policy has no QoS profile configured.".format(
                    list(contract_data.keys())
                ),
                "DEBUG"
            )
            return None

        self.log(
            "Extracted queuing profile ID from contract: '{0}'. Initiating API call to "
            "resolve profile UUID to human-readable profile name.".format(profile_id),
            "DEBUG"
        )

        try:
            response = self.dnac._exec(
                family="application_policy",
                function="get_application_policy_queuing_profile",
                op_modifies=False
            )
            self.log(
                "Received API response for queuing profile lookup. Response structure: "
                "{0}".format(
                    {
                        "has_response_key": "response" in response if response else False,
                        "response_type": type(response.get("response")).__name__ if response and "response" in response else "N/A",
                        "response_count": len(response.get("response")) if response and isinstance(response.get("response"), list) else 0
                    } if response else "No response"
                ),
                "DEBUG"
            )

            if not response:
                self.log(
                    "API response is None or empty for profile ID '{0}'. This may indicate "
                    "a network issue, authentication failure, or API unavailability. "
                    "Returning None.".format(profile_id),
                    "WARNING"
                )
                return None

            if "response" not in response:
                self.log(
                    "API response missing 'response' key for profile ID '{0}'. Response "
                    "keys: {1}. This indicates an unexpected API response format. "
                    "Returning None.".format(profile_id, list(response.keys())),
                    "WARNING"
                )
                return None

            profiles = response.get("response")

            if not isinstance(profiles, list):
                self.log(
                    "API response 'response' field is not a list for profile ID '{0}'. "
                    "Got type: {1}. This indicates an unexpected API response format. "
                    "Returning None.".format(profile_id, type(profiles).__name__),
                    "WARNING"
                )
                return None

            if not profiles or len(profiles) == 0:
                self.log(
                    "API response contains empty profile list. No queuing profiles found "
                    "in Catalyst Center. Returning None for profile ID '{0}'.".format(
                        profile_id
                    ),
                    "WARNING"
                )
                return None

            self.log(
                "API response contains {0} total queuing profile(s). Searching for profile "
                "with ID '{1}' in profile list.".format(len(profiles), profile_id),
                "DEBUG"
            )

            # Search for matching profile by ID
            for profile_index, profile in enumerate(profiles, start=1):
                if not isinstance(profile, dict):
                    self.log(
                        "Profile entry {0}/{1} is not a dictionary. Got type: {2}. Skipping "
                        "this profile entry.".format(
                            profile_index, len(profiles), type(profile).__name__
                        ),
                        "DEBUG"
                    )
                    continue

                # Log profile structure for first profile to debug field names
                if profile_index == 1:
                    self.log(
                        "Sample queuing profile structure (first profile): keys={0}, "
                        "name='{1}', id field present: {2}".format(
                            list(profile.keys()),
                            profile.get("name", "N/A"),
                            "id" in profile
                        ),
                        "DEBUG"
                    )

                # Try multiple possible ID field names
                current_profile_id = profile.get("id") or profile.get("profileId") or profile.get("instanceUuid")

                self.log(
                    "Checking profile {0}/{1}: name='{2}', extracted_id='{3}', "
                    "looking_for_id='{4}', match={5}".format(
                        profile_index, len(profiles), profile.get("name", "N/A"),
                        current_profile_id, profile_id, current_profile_id == profile_id
                    ),
                    "DEBUG"
                )

                if current_profile_id == profile_id:
                    profile_name = profile.get("name")

                    if not profile_name:
                        self.log(
                            "Found matching profile at index {0}/{1} for ID '{2}' but profile "
                            "is missing 'name' field. Profile keys: {3}. This indicates incomplete "
                            "profile data from API. Returning None.".format(
                                profile_index, len(profiles), profile_id, list(profile.keys())
                            ),
                            "WARNING"
                        )
                        return None

                    self.log(
                        "Successfully found and resolved queuing profile name for ID '{0}' at "
                        "index {1}/{2}: '{3}'. Profile name will be used in application policy "
                        "playbook configuration.".format(
                            profile_id, profile_index, len(profiles), profile_name
                        ),
                        "INFO"
                    )

                    return profile_name

            # No matching profile found
            self.log(
                "No queuing profile found with ID '{0}' after searching all {1} profile(s). "
                "This indicates the profile has been deleted from Catalyst Center or the "
                "profile ID is invalid. Returning None.".format(profile_id, len(profiles)),
                "WARNING"
            )

            return None

        except Exception as e:
            self.log(
                "Exception occurred while resolving queuing profile name for ID '{0}'. "
                "Error type: {1}, Error message: {2}. This may indicate network issues, "
                "authentication failures, API unavailability, or permission problems. "
                "Returning None to allow policy generation to continue without QoS profile "
                "reference.".format(
                    profile_id, type(e).__name__, str(e)
                ),
                "ERROR"
            )

            return None

    def get_application_set_name_from_id(self, app_set_id):
        """
        Retrieves application set name by resolving application set ID via Catalyst Center API.

        This function queries the Cisco Catalyst Center to resolve an application set UUID to its
        human-readable name for use in application policy configurations. Application sets are
        collections of applications grouped together for policy assignment.

        Args:
            app_set_id (str): Application set UUID to resolve to human-readable name.
                             Expected format: UUID string (e.g., "abc-123-def-456").

        Returns:
            str or None: Application set name if successfully resolved, None if:
                        - app_set_id is None or empty
                        - API call fails or returns no data
                        - Application set not found in Catalyst Center
                        - Response structure is invalid
                        - Matching set has no name field
        """
        self.log(
            "Starting application set name resolution from application set ID reference",
            "DEBUG"
        )

        if not app_set_id:
            self.log(
                "Application set name resolution returning None - no application set ID "
                "provided. app_set_id is None or empty string. This indicates the policy "
                "has no application set reference.",
                "DEBUG"
            )
            return None

        self.log(
            "Received application set ID: '{0}'. Initiating API call to retrieve all "
            "application sets for ID matching and name resolution.".format(app_set_id),
            "INFO"
        )

        try:
            response = self.dnac._exec(
                family="application_policy",
                function="get_application_sets",
                op_modifies=False
            )
            self.log(
                "Received API response for application sets query. Response structure: {0}".format(
                    {
                        "has_response_key": "response" in response if response else False,
                        "response_type": type(response.get("response")).__name__ if response and "response" in response else "N/A",
                        "response_count": len(response.get("response")) if response and isinstance(response.get("response"), list) else 0
                    } if response else "No response"
                ),
                "DEBUG"
            )

            if not response:
                self.log(
                    "API response is None or empty for application sets query. This may "
                    "indicate a network issue, authentication failure, or API unavailability. "
                    "Returning None for app_set_id '{0}'.".format(app_set_id),
                    "WARNING"
                )
                return None

            if "response" not in response:
                self.log(
                    "API response missing 'response' key for application sets query. "
                    "Response keys: {0}. This indicates an unexpected API response format. "
                    "Returning None for app_set_id '{1}'.".format(
                        list(response.keys()), app_set_id
                    ),
                    "WARNING"
                )
                return None

            app_sets = response.get("response")

            if not isinstance(app_sets, list):
                self.log(
                    "API response 'response' field is not a list. Got type: {0}. This "
                    "indicates an unexpected API response format. Returning None for "
                    "app_set_id '{1}'.".format(type(app_sets).__name__, app_set_id),
                    "WARNING"
                )
                return None

            if not app_sets or len(app_sets) == 0:
                self.log(
                    "API response contains empty application set list. No application sets "
                    "are configured in Catalyst Center. Cannot resolve app_set_id '{0}'. "
                    "Returning None.".format(app_set_id),
                    "WARNING"
                )
                return None

            self.log(
                "Retrieved {0} application set(s) from Catalyst Center. Starting linear "
                "search to find matching ID for '{1}'.".format(len(app_sets), app_set_id),
                "INFO"
            )

            # Search for matching application set
            for set_index, app_set in enumerate(app_sets, start=1):
                if not isinstance(app_set, dict):
                    self.log(
                        "Application set {0}/{1} is not a dictionary - skipping. Expected "
                        "dict, got: {2}. Continuing to next application set.".format(
                            set_index, len(app_sets), type(app_set).__name__
                        ),
                        "WARNING"
                    )
                    continue

                current_id = app_set.get("id")

                self.log(
                    "Checking application set {0}/{1}: ID='{2}', target ID='{3}', "
                    "match={4}".format(
                        set_index, len(app_sets), current_id, app_set_id,
                        current_id == app_set_id
                    ),
                    "DEBUG"
                )

                if current_id == app_set_id:
                    # Found matching application set
                    app_set_name = app_set.get("name")

                    if not app_set_name:
                        self.log(
                            "Found matching application set at index {0}/{1} for ID '{2}', "
                            "but 'name' field is missing or empty. Application set keys: {3}. "
                            "Returning None.".format(
                                set_index, len(app_sets), app_set_id, list(app_set.keys())
                            ),
                            "WARNING"
                        )
                        return None

                    self.log(
                        "Successfully resolved application set name for ID '{0}' at index "
                        "{1}/{2}: '{3}'. Name will be used in application policy clause "
                        "configuration.".format(
                            app_set_id, set_index, len(app_sets), app_set_name
                        ),
                        "INFO"
                    )

                    return app_set_name

            # No matching application set found
            self.log(
                "Completed search of all {0} application set(s) - no match found for ID "
                "'{1}'. This indicates the application set has been deleted from Catalyst "
                "Center, the ID is invalid, or the application set is not synchronized. "
                "Returning None.".format(len(app_sets), app_set_id),
                "WARNING"
            )

            return None

        except Exception as e:
            self.log(
                "Exception occurred while resolving application set name for ID '{0}'. "
                "Error type: {1}, Error message: {2}. This may indicate network issues, "
                "authentication failures, API unavailability, or permission problems. "
                "Returning None to allow policy generation to continue without this "
                "application set reference.".format(
                    app_set_id, type(e).__name__, str(e)
                ),
                "ERROR"
            )
            return None

    def transform_clause(self, policy):
        """
        Transforms application policy producer data into playbook-compatible clause format.

        This function extracts application sets from policy producer.scalableGroup references
        and organizes them by business relevance level (BUSINESS_RELEVANT, BUSINESS_IRRELEVANT,
        DEFAULT) to create BUSINESS_RELEVANCE clause configurations for playbook generation.

        Args:
            policy (dict): Complete policy object from get_application_policy API response
                          containing producer, exclusiveContract, policyScope, and name fields.

        Returns:
            list: List containing single clause dictionary with BUSINESS_RELEVANCE structure,
                 or empty list if:
                 - policy is None or invalid type
                 - policy is a special type (queuing_customization, etc.)
                 - No producer data found
                 - No scalableGroup data found
                 - No valid application sets resolved
                 - All application set resolutions failed
        """
        self.log(
            "Starting clause transformation from application policy producer data",
            "DEBUG"
        )

        if not policy or not isinstance(policy, dict):
            self.log(
                "Clause transformation returning empty list - invalid policy data provided. "
                "Expected dict, got: {0}. This indicates invalid API response or data "
                "structure issue.".format(
                    type(policy).__name__ if policy is not None else "None"
                ),
                "WARNING"
            )
            return []

        policy_name = policy.get("policyScope", "unknown")

        self.log(
            "Processing clause transformation for policy: '{0}'. Checking if this is a "
            "special policy type that should not have application clauses.".format(
                policy_name
            ),
            "DEBUG"
        )

        # Check if this is a special policy type that shouldn't have application clauses
        name_lower = policy.get("name", "").lower()

        self.log(
            "Policy internal name (lowercase): '{0}'. Checking for special policy type "
            "patterns (queuing_customization, global_policy_configuration).".format(
                name_lower
            ),
            "DEBUG"
        )

        if any(x in name_lower for x in ["queuing_customization", "global_policy_configuration"]):
            self.log(
                "Skipping clause transformation for special policy type: {0}. Special policies "
                "(queuing_customization, global_policy_configuration) don't require application "
                "clauses.".format(policy_name),
                "DEBUG"
            )
            return []

        self.log(
            "Policy '{0}' is not a special type - proceeding with clause extraction. "
            "Extracting producer data to get application set references.".format(
                policy_name
            ),
            "DEBUG"
        )

        # Extract producer data (contains app set info)
        producer = policy.get("producer")
        if not producer or not isinstance(producer, dict):
            self.log(
                "No valid producer data found in policy '{0}'. Producer is None or not a "
                "dict (got: {1}). Returning empty clause list. This indicates the policy "
                "has no application set assignments.".format(
                    policy_name, type(producer).__name__ if producer is not None else "None"
                ),
                "DEBUG"
            )
            return []

        self.log(
            "Found producer data in policy '{0}'. Producer keys: {1}. Extracting "
            "scalableGroup array to get application set ID references.".format(
                policy_name, list(producer.keys())
            ),
            "DEBUG"
        )

        scalable_groups = producer.get("scalableGroup", [])
        if not scalable_groups or not isinstance(scalable_groups, list):
            self.log(
                "No valid scalableGroup data found in producer for policy '{0}'. "
                "scalableGroup is None, empty, or not a list (got: {1}). Returning empty "
                "clause list. This indicates the policy has no application sets configured.".format(
                    policy_name,
                    type(scalable_groups).__name__ if scalable_groups is not None else "None"
                ),
                "DEBUG"
            )
            return []

        self.log(
            "Found {0} scalable group(s) (application set references) in policy '{1}'. "
            "Starting application set ID extraction and name resolution.".format(
                len(scalable_groups), policy_name
            ),
            "INFO"
        )

        # Get relevance level from exclusiveContract
        relevance_level = "DEFAULT"
        exclusive_contract = policy.get("exclusiveContract")

        self.log(
            "Extracting business relevance level from exclusiveContract for policy '{0}'. "
            "exclusiveContract present: {1}".format(
                policy_name, exclusive_contract is not None
            ),
            "DEBUG"
        )

        if exclusive_contract and isinstance(exclusive_contract, dict):
            clauses = exclusive_contract.get("clause", [])

            self.log(
                "Found {0} clause(s) in exclusiveContract for policy '{1}'. Searching for "
                "BUSINESS_RELEVANCE clause type to determine relevance level.".format(
                    len(clauses) if isinstance(clauses, list) else 0, policy_name
                ),
                "DEBUG"
            )

            if clauses and isinstance(clauses, list) and len(clauses) > 0:
                for clause_index, clause in enumerate(clauses, start=1):
                    if not isinstance(clause, dict):
                        self.log(
                            "Clause {0}/{1} in exclusiveContract is not a dict - skipping. "
                            "Expected dict, got: {2}".format(
                                clause_index, len(clauses), type(clause).__name__
                            ),
                            "WARNING"
                        )
                        continue

                    clause_type = clause.get("type")

                    self.log(
                        "Checking exclusiveContract clause {0}/{1} for policy '{2}': "
                        "type='{3}'".format(
                            clause_index, len(clauses), policy_name, clause_type
                        ),
                        "DEBUG"
                    )

                    if clause_type == "BUSINESS_RELEVANCE":
                        relevance_level = clause.get("relevanceLevel", "DEFAULT")

                        self.log(
                            "Found BUSINESS_RELEVANCE clause in exclusiveContract clause "
                            "{0}/{1} for policy '{2}'. Extracted relevance level: '{3}'. "
                            "This level will apply to all application sets in this policy.".format(
                                clause_index, len(clauses), policy_name, relevance_level
                            ),
                            "INFO"
                        )
                        break
                else:
                    self.log(
                        "No BUSINESS_RELEVANCE clause found in {0} exclusiveContract "
                        "clause(s) for policy '{1}'. Using default relevance level: "
                        "'{2}'.".format(len(clauses), policy_name, relevance_level),
                        "DEBUG"
                    )
            else:
                self.log(
                    "exclusiveContract for policy '{0}' has no clauses or invalid clause "
                    "structure. Using default relevance level: '{1}'.".format(
                        policy_name, relevance_level
                    ),
                    "DEBUG"
                )
        else:
            self.log(
                "No valid exclusiveContract found for policy '{0}'. Using default relevance "
                "level: '{1}'. This is normal for policies without explicit relevance "
                "configuration.".format(policy_name, relevance_level),
                "DEBUG"
            )

        self.log(
            "Business relevance level determined for policy '{0}': '{1}'. All application "
            "sets in this policy will be assigned this relevance level.".format(
                policy_name, relevance_level
            ),
            "INFO"
        )

        # Dictionary to group application sets by relevance level
        relevance_map = {}

        self.log(
            "Initialized relevance map for grouping application sets by relevance level. "
            "Processing {0} scalable group(s) to extract and resolve application set IDs.".format(
                len(scalable_groups)
            ),
            "DEBUG"
        )

        # Process each scalable group (app set)
        for group_index, group in enumerate(scalable_groups, start=1):
            self.log(
                "Processing scalable group {0}/{1} in policy '{2}' to extract application "
                "set ID reference.".format(group_index, len(scalable_groups), policy_name),
                "DEBUG"
            )

            if not isinstance(group, dict):
                self.log(
                    "Scalable group {0}/{1} in policy '{2}' is not a dictionary - skipping. "
                    "Expected dict, got: {3}. Continuing to next scalable group.".format(
                        group_index, len(scalable_groups), policy_name, type(group).__name__
                    ),
                    "WARNING"
                )
                continue

            app_set_id = group.get("idRef")
            if not app_set_id:
                self.log(
                    "Scalable group {0}/{1} in policy '{2}' has no idRef (application set "
                    "UUID). Scalable group keys: {3}. Skipping this group.".format(
                        group_index, len(scalable_groups), policy_name, list(group.keys())
                    ),
                    "WARNING"
                )
                continue

            self.log(
                "Extracted application set ID from scalable group {0}/{1} in policy '{2}': "
                "'{3}'. Initiating API call to resolve UUID to application set name.".format(
                    group_index, len(scalable_groups), policy_name, app_set_id
                ),
                "DEBUG"
            )

            # Get application set name from ID
            app_set_name = self.get_application_set_name_from_id(app_set_id)

            if app_set_name:
                if relevance_level not in relevance_map:
                    relevance_map[relevance_level] = []
                    self.log(
                        "Created new relevance map entry for level '{0}' in policy '{1}'.".format(
                            relevance_level, policy_name
                        ),
                        "DEBUG"
                    )

                relevance_map[relevance_level].append(app_set_name)

                self.log(
                    "Successfully resolved and added application set {0}/{1} for policy "
                    "'{2}': UUID '{3}' → name '{4}'. Added to relevance level '{5}'. "
                    "Total app sets at this level: {6}".format(
                        group_index, len(scalable_groups), policy_name, app_set_id,
                        app_set_name, relevance_level, len(relevance_map[relevance_level])
                    ),
                    "INFO"
                )
            else:
                self.log(
                    "Failed to resolve application set name for scalable group {0}/{1} in "
                    "policy '{2}': UUID '{3}'. Application set may be deleted, UUID invalid, "
                    "or API call failed. This application set will be excluded from the "
                    "clause.".format(
                        group_index, len(scalable_groups), policy_name, app_set_id
                    ),
                    "WARNING"
                )

        self.log(
            "Completed processing all {0} scalable group(s) for policy '{1}'. Relevance "
            "map summary: {2}. Starting clause structure building.".format(
                len(scalable_groups), policy_name,
                {k: len(v) for k, v in relevance_map.items()}
            ),
            "INFO"
        )

        # Build relevance_details list
        relevance_details = []
        for relevance in ["BUSINESS_RELEVANT", "BUSINESS_IRRELEVANT", "DEFAULT"]:
            if relevance in relevance_map and relevance_map[relevance]:
                # Remove duplicates and sort application set names
                app_sets = sorted(list(set(relevance_map[relevance])))

                self.log(
                    "Building relevance details entry for policy '{0}': relevance='{1}', "
                    "app sets count={2} (after deduplication), app sets={3}".format(
                        policy_name, relevance, len(app_sets), app_sets
                    ),
                    "DEBUG"
                )

                relevance_details.append(OrderedDict([
                    ("relevance", relevance),
                    ("application_set_name", app_sets)
                ]))

                self.log(
                    "Added relevance details entry {0} for policy '{1}': '{2}' with {3} "
                    "application set(s)".format(
                        len(relevance_details), policy_name, relevance, len(app_sets)
                    ),
                    "DEBUG"
                )

        if relevance_details:
            clause_structure = [OrderedDict([
                ("clause_type", "BUSINESS_RELEVANCE"),
                ("relevance_details", relevance_details)
            ])]

            self.log(
                "Successfully created BUSINESS_RELEVANCE clause for policy '{0}' with {1} "
                "relevance level(s). Total application sets across all levels: {2}. "
                "Returning clause structure.".format(
                    policy_name, len(relevance_details),
                    sum(len(rd["application_set_name"]) for rd in relevance_details)
                ),
                "INFO"
            )

            return clause_structure

        self.log(
            "No relevance details generated for policy '{0}'. This indicates all "
            "application set ID resolutions failed, or no valid application sets were "
            "configured. Returning empty clause list. Scalable groups processed: {1}, "
            "successful resolutions: 0".format(policy_name, len(scalable_groups)),
            "WARNING"
        )
        return []

    def transform_application_policies(self, policies):
        """
        Transforms application policies from API response to playbook-compatible format.

        This function consolidates multiple API policy entries (base policy, queuing customization,
        relevance-specific policies) into single unified policy configurations for playbook generation.
        Each policyScope represents a logical policy that may have multiple API entries.

        Args:
            policies (list): List of policy dictionaries from get_application_policy API response.
                            May contain multiple entries per logical policy (grouped by policyScope).

        Returns:
            list: List of consolidated policy dictionaries in playbook format, one entry per
                 unique (policyScope, sites) combination. Returns empty list if:
                 - policies is None or empty
                 - No valid policies found
                 - All policies missing required fields (policyScope, site_names)
        """
        if not policies:
            self.log("No policies to transform", "INFO")
            return []

        self.log("Starting transformation of {0} policies".format(len(policies)), "INFO")

        # First, group policies by policyScope to consolidate them
        policy_groups = {}
        for policy in policies:
            if not isinstance(policy, dict):
                continue

            policy_scope = policy.get("policyScope")
            if not policy_scope:
                continue

            if policy_scope not in policy_groups:
                policy_groups[policy_scope] = []
            policy_groups[policy_scope].append(policy)

        self.log("Grouped into {0} unique policy scopes".format(len(policy_groups)), "INFO")

        transformed_policies = []
        seen_policies = set()

        for policy_scope, policy_list in policy_groups.items():
            self.log("Processing policy scope: {0} with {1} entries".format(policy_scope, len(policy_list)), "INFO")

            # Use the first policy as the base (they should all have same scope/site info)
            base_policy = policy_list[0]
            advanced_policy_scope = base_policy.get("advancedPolicyScope")

            # Get site IDs for unique identification
            site_ids = []
            if advanced_policy_scope and isinstance(advanced_policy_scope, dict):
                adv_scope_elements = advanced_policy_scope.get("advancedPolicyScopeElement", [])
                for element in adv_scope_elements:
                    if isinstance(element, dict):
                        group_ids = element.get("groupId", [])
                        if isinstance(group_ids, list):
                            site_ids.extend(group_ids)

            policy_identifier = (policy_scope, tuple(sorted(site_ids)))

            if policy_identifier in seen_policies:
                self.log("Skipping duplicate policy: {0}".format(policy_scope), "DEBUG")
                continue

            seen_policies.add(policy_identifier)

            policy_data = OrderedDict()
            policy_data["name"] = policy_scope

            delete_status = base_policy.get("deletePolicyStatus", "NONE")
            policy_data["policy_status"] = "deployed" if delete_status == "NONE" else delete_status.lower()

            site_names = self.transform_site_names(advanced_policy_scope)
            if site_names:
                policy_data["site_names"] = site_names

            device_type = self.transform_device_type(advanced_policy_scope)
            policy_data["device_type"] = device_type

            if device_type == "wireless":
                ssid_name = self.transform_ssid_name(advanced_policy_scope)
                if ssid_name:
                    policy_data["ssid_name"] = ssid_name

            # Get queuing profile from any policy in the list
            # Check both contract and exclusiveContract fields
            queuing_profile_name = None
            for policy in policy_list:
                # Check contract field first (most common for queuing customization)
                contract = policy.get("contract")
                if contract and isinstance(contract, dict):
                    queuing_profile_name = self.get_queuing_profile_name_from_id(contract)
                    if queuing_profile_name:
                        self.log(
                            "Found queuing profile '{0}' in policy '{1}' contract field".format(
                                queuing_profile_name, policy.get("name", "N/A")
                            ),
                            "DEBUG"
                        )
                        break

                # Also check exclusiveContract field as fallback
                exclusive_contract = policy.get("exclusiveContract")
                if exclusive_contract and isinstance(exclusive_contract, dict):
                    queuing_profile_name = self.get_queuing_profile_name_from_id(exclusive_contract)
                    if queuing_profile_name:
                        self.log(
                            "Found queuing profile '{0}' in policy '{1}' exclusiveContract field".format(
                                queuing_profile_name, policy.get("name", "N/A")
                            ),
                            "DEBUG"
                        )
                        break

            if queuing_profile_name:
                policy_data["application_queuing_profile_name"] = queuing_profile_name
                self.log(
                    "Added queuing profile name '{0}' to policy '{1}' playbook configuration".format(
                        queuing_profile_name, policy_scope
                    ),
                    "INFO"
                )
            else:
                self.log(
                    "No queuing profile found for policy '{0}' - checked {1} sub-policy/policies. "
                    "Policy will be generated without QoS profile configuration.".format(
                        policy_scope, len(policy_list)
                    ),
                    "DEBUG"
                )

            # Collect all application sets across all sub-policies by relevance
            all_relevance_map = {
                "BUSINESS_RELEVANT": set(),
                "BUSINESS_IRRELEVANT": set(),
                "DEFAULT": set()
            }

            for policy in policy_list:
                # Skip special policy types
                name_lower = policy.get("name", "").lower()
                if any(x in name_lower for x in ["queuing_customization", "global_policy_configuration"]):
                    continue

                # Get app sets from this sub-policy
                producer = policy.get("producer")
                if not producer or not isinstance(producer, dict):
                    continue

                scalable_groups = producer.get("scalableGroup", [])
                if not scalable_groups or not isinstance(scalable_groups, list):
                    continue

                # Get relevance level from exclusiveContract
                relevance_level = "DEFAULT"
                exclusive_contract = policy.get("exclusiveContract")
                if exclusive_contract and isinstance(exclusive_contract, dict):
                    clauses = exclusive_contract.get("clause", [])
                    for clause in clauses:
                        if clause.get("type") == "BUSINESS_RELEVANCE":
                            relevance_level = clause.get("relevanceLevel", "DEFAULT")
                            break

                # Add app sets to the relevance map
                for group in scalable_groups:
                    if not isinstance(group, dict):
                        continue

                    app_set_id = group.get("idRef")
                    if app_set_id:
                        app_set_name = self.get_application_set_name_from_id(app_set_id)
                        if app_set_name:
                            all_relevance_map[relevance_level].add(app_set_name)
                            self.log("Added '{0}' to {1} for policy '{2}'".format(
                                app_set_name, relevance_level, policy_scope), "DEBUG")

            # Build clause if we have any application sets
            relevance_details = []
            for relevance in ["BUSINESS_RELEVANT", "BUSINESS_IRRELEVANT", "DEFAULT"]:
                if all_relevance_map[relevance]:
                    app_sets = sorted(list(all_relevance_map[relevance]))
                    relevance_details.append(OrderedDict([
                        ("relevance", relevance),
                        ("application_set_name", app_sets)
                    ]))

            if relevance_details:
                policy_data["clause"] = [OrderedDict([
                    ("clause_type", "BUSINESS_RELEVANCE"),
                    ("relevance_details", relevance_details)
                ])]
                self.log("Successfully added clause to policy '{0}' with {1} relevance levels".format(
                    policy_scope, len(relevance_details)), "INFO")
            else:
                self.log("No clause data found for policy '{0}'".format(policy_scope), "INFO")

            if policy_scope and site_names:
                transformed_policies.append(policy_data)
                self.log("Successfully transformed policy: {0} (has clause: {1})".format(
                    policy_scope, "clause" in policy_data), "INFO")
            else:
                self.log("Skipping policy due to missing required fields: name={0}, sites={1}".format(
                    policy_scope, len(site_names) if site_names else 0), "WARNING")

        self.log("Transformed {0} policies total".format(len(transformed_policies)), "INFO")
        return transformed_policies

    def get_detailed_application_policy(self, policy_name):
        """
        Retrieves detailed application policy data including consumer information by querying
        Cisco Catalyst Center API.

        This function fetches comprehensive policy details for a specific policy by name, including
        consumer relationships, producer settings, contract assignments, and clause configurations.
        The detailed policy data provides complete context for policy transformation and analysis.

        Args:
            policy_name (str): Name of the application policy to retrieve (policyScope value).
                              Example: "wired_traffic_policy", "wireless_guest_policy"

        Returns:
            dict or None: Detailed policy dictionary if found, None if:
                         - policy_name is None or empty
                         - API call fails or raises exception
                         - No policy found with matching policyScope
                         - API response is empty or invalid
                         - Response structure is unexpected
        """
        self.log(
            "Starting detailed application policy retrieval for policy name: '{0}'".format(
                policy_name
            ),
            "INFO"
        )

        if not policy_name:
            self.log(
                "Detailed policy retrieval returning None - no policy name provided. "
                "policy_name is None or empty string. Cannot query API without policy name.",
                "INFO"
            )
            return None

        self.log(
            "Initiating API call to fetch detailed policy data for policyScope: '{0}'. "
            "This will retrieve complete policy configuration including consumer, producer, "
            "contract, and clause details.".format(policy_name),
            "DEBUG"
        )

        try:
            # Try getting with policy scope parameter
            response = self.dnac._exec(
                family="application_policy",
                function="get_application_policy",
                op_modifies=False,
                params={"policyScope": policy_name}
            )
            self.log(
                "Received API response for detailed policy query '{0}'. Response structure: {1}".format(
                    policy_name,
                    {
                        "has_response_key": "response" in response if response else False,
                        "response_type": type(response.get("response")).__name__ if response and "response" in response else "N/A",
                        "response_count": len(response.get("response")) if response and isinstance(response.get("response"), list) else 0
                    } if response else "No response"
                ),
                "DEBUG"
            )

            if not response:
                self.log(
                    "API response is None or empty for policy '{0}'. This may indicate a "
                    "network issue, authentication failure, or API unavailability. Returning "
                    "None.".format(policy_name),
                    "WARNING"
                )
                return None

            if "response" not in response:
                self.log(
                    "API response missing 'response' key for policy '{0}'. Response keys: {1}. "
                    "This indicates an unexpected API response format. Returning None.".format(
                        policy_name, list(response.keys())
                    ),
                    "WARNING"
                )
                return None

            policies = response.get("response")

            if not isinstance(policies, list):
                self.log(
                    "API response 'response' field is not a list for policy '{0}'. Got type: {1}. "
                    "This indicates an unexpected API response format. Returning None.".format(
                        policy_name, type(policies).__name__
                    ),
                    "WARNING"
                )
                return None

            if not policies or len(policies) == 0:
                self.log(
                    "No policy found with policyScope '{0}'. API returned empty policy list. "
                    "This indicates the policy does not exist in Catalyst Center or has been "
                    "deleted. Returning None.".format(policy_name),
                    "WARNING"
                )
                return None

            self.log(
                "API response contains {0} policy/policies for policyScope '{1}'. Extracting "
                "first policy from response list (policyScope should be unique).".format(
                    len(policies), policy_name
                ),
                "DEBUG"
            )

            # Extract first policy (policyScope should be unique)
            detailed_policy = policies[0]

            if not isinstance(detailed_policy, dict):
                self.log(
                    "First policy in response is not a dictionary for policyScope '{0}'. "
                    "Got type: {1}. This indicates an unexpected API response format. "
                    "Returning None.".format(policy_name, type(detailed_policy).__name__),
                    "WARNING"
                )
                return None

            # Log policy structure for debugging
            policy_keys = list(detailed_policy.keys())
            has_consumer = "consumer" in detailed_policy
            has_producer = "producer" in detailed_policy
            has_contract = "contract" in detailed_policy
            has_exclusive_contract = "exclusiveContract" in detailed_policy

            self.log(
                "Successfully retrieved detailed policy data for '{0}'. Policy structure: "
                "keys={1}, has_consumer={2}, has_producer={3}, has_contract={4}, "
                "has_exclusiveContract={5}. Internal policy name: '{6}'".format(
                    policy_name, policy_keys, has_consumer, has_producer, has_contract,
                    has_exclusive_contract, detailed_policy.get("name", "N/A")
                ),
                "INFO"
            )

            # Log consumer data if present for debugging
            if has_consumer:
                consumer = detailed_policy.get("consumer", {})
                consumer_scalable_groups = consumer.get("scalableGroup", []) if isinstance(consumer, dict) else []

                self.log(
                    "Detailed policy '{0}' has consumer data with {1} scalable group(s). "
                    "Consumer structure provides destination traffic classification details.".format(
                        policy_name, len(consumer_scalable_groups) if isinstance(consumer_scalable_groups, list) else 0
                    ),
                    "DEBUG"
                )

            # Log producer data if present
            if has_producer:
                producer = detailed_policy.get("producer", {})
                producer_scalable_groups = producer.get("scalableGroup", []) if isinstance(producer, dict) else []

                self.log(
                    "Detailed policy '{0}' has producer data with {1} scalable group(s). "
                    "Producer structure provides source traffic classification details.".format(
                        policy_name, len(producer_scalable_groups) if isinstance(producer_scalable_groups, list) else 0
                    ),
                    "DEBUG"
                )

            self.log(
                "Detailed policy retrieval completed successfully for '{0}'. Returning "
                "complete policy object with all relationship data.".format(policy_name),
                "INFO"
            )

            return detailed_policy

        except Exception as e:
            self.log(
                "Exception occurred while fetching detailed policy for '{0}'. Error type: {1}, "
                "Error message: {2}. This may indicate network issues, authentication failures, "
                "API unavailability, permission problems, or invalid policy name. Returning None "
                "to allow graceful continuation.".format(
                    policy_name, type(e).__name__, str(e)
                ),
                "ERROR"
            )
            return None

    def get_application_policies(self, network_element, filters):
        """
        Retrieves application policies from Cisco Catalyst Center and transforms them into
        playbook-compatible format.

        This function fetches all application policies from the Catalyst Center API, applies
        optional name-based filtering, and transforms the API response into the structure
        required by the application_policy_workflow_manager module for playbook generation.

        Args:
            network_element (dict): Network element definition from module schema containing
                                   API configuration (family, function, filters).
            filters (dict): Filter dictionary containing component_specific_filters with
                           optional policy_names_list for filtering specific policies.

        Returns:
            dict: Dictionary with 'application_policy' key containing list of transformed
                 policy configurations in playbook format. Returns empty list if:
                 - API call fails or raises exception
                 - No policies found in Catalyst Center
                 - All policies filtered out by policy_names_list
                 - Transformation fails completely
        """
        self.log(
            "Starting application policy retrieval with filters. Component filters: {0}".format(
                bool(filters.get("component_specific_filters"))
            ),
            "INFO"
        )

        component_specific_filters = filters.get("component_specific_filters", {})
        app_policy_filters = component_specific_filters.get("application_policy", {})
        policy_names_list = app_policy_filters.get("policy_names_list", [])

        self.log(
            "Extracted filter parameters. component_specific_filters present: {0}, "
            "application_policy filters present: {1}, policy_names_list count: {2}, "
            "policy names: {3}".format(
                bool(component_specific_filters),
                bool(app_policy_filters),
                len(policy_names_list) if policy_names_list else 0,
                policy_names_list if policy_names_list else "None (retrieve all policies)"
            ),
            "DEBUG"
        )

        if policy_names_list:
            self.log(
                "Filtering application policies by {0} policy name(s): {1}".format(
                    len(policy_names_list), policy_names_list
                ),
                "INFO"
            )
        else:
            self.log(
                "No policy name filter specified - will retrieve all application policies",
                "INFO"
            )

        try:
            # Get all application policies
            response = self.dnac._exec(
                family="application_policy",
                function="get_application_policy",
                op_modifies=False,
            )
            self.log(
                "Received API response for application policy query. Response structure: {0}".format(
                    {
                        "has_response_key": "response" in response if response else False,
                        "response_type": type(response.get("response")).__name__ if response and "response" in response else "N/A",
                        "response_count": len(response.get("response")) if response and isinstance(response.get("response"), list) else 0
                    } if response else "No response"
                ),
                "DEBUG"
            )

            if not response or not response.get("response"):
                self.log(
                    "No application policies found in API response. Response is None or missing "
                    "'response' key. This may indicate no policies configured in Catalyst Center, "
                    "API unavailability, or authentication issues. Returning empty policy list.",
                    "WARNING"
                )
                return {"application_policy": []}

            policies = response.get("response", [])

            if not isinstance(policies, list):
                self.log(
                    "API response 'response' field is not a list. Got type: {0}. This indicates "
                    "an unexpected API response format. Returning empty policy list.".format(
                        type(policies).__name__
                    ),
                    "WARNING"
                )
                return {"application_policy": []}

            if not policies:
                self.log(
                    "API returned empty policy list. No application policies are configured in "
                    "Catalyst Center. Returning empty policy list.",
                    "WARNING"
                )
                return {"application_policy": []}

            self.log(
                "Successfully retrieved {0} total application policy entries from Catalyst Center "
                "API. These entries may include base policies, queuing customizations, and "
                "relevance-specific sub-policies that will be consolidated during transformation.".format(
                    len(policies)
                ),
                "INFO"
            )

            # Apply client-side filtering by policy names if specified
            if policy_names_list:
                original_count = len(policies)
                policies = [p for p in policies if p.get("policyScope") in policy_names_list]

                self.log(
                    "Applied client-side filtering based on policy_names_list. Original policy "
                    "entries: {0}, filtered policy entries: {1}, filter matched: {2}/{3} requested "
                    "policy names, requested names: {4}".format(
                        original_count,
                        len(policies),
                        len(set(p.get("policyScope") for p in policies)),
                        len(policy_names_list),
                        policy_names_list
                    ),
                    "INFO"
                )

                if not policies:
                    self.log(
                        "No policies matched the filter criteria after applying policy_names_list "
                        "filter. Requested policy names: {0}. These policies may not exist in "
                        "Catalyst Center or names may be incorrect. Returning empty policy list.".format(
                            policy_names_list
                        ),
                        "WARNING"
                    )
                    return {"application_policy": []}
            else:
                self.log(
                    "No policy name filtering specified (policy_names_list is empty or not "
                    "provided). Proceeding with all {0} policy entries from API.".format(
                        len(policies)
                    ),
                    "INFO"
                )

            # Log sample policy structure for debugging
            if policies and len(policies) > 0:
                sample_policy = policies[0]
                policy_keys = list(sample_policy.keys())
                has_consumer = "consumer" in sample_policy
                has_producer = "producer" in sample_policy
                has_contract = "contract" in sample_policy
                has_exclusive_contract = "exclusiveContract" in sample_policy
                has_advanced_policy_scope = "advancedPolicyScope" in sample_policy

                self.log(
                    "Sample policy structure analysis (first policy entry): keys={0}, "
                    "policyScope='{1}', internal_name='{2}', has_consumer={3}, has_producer={4}, "
                    "has_contract={5}, has_exclusiveContract={6}, has_advancedPolicyScope={7}".format(
                        policy_keys,
                        sample_policy.get("policyScope", "N/A"),
                        sample_policy.get("name", "N/A"),
                        has_consumer,
                        has_producer,
                        has_contract,
                        has_exclusive_contract,
                        has_advanced_policy_scope
                    ),
                    "DEBUG"
                )

                # Log consumer data presence for debugging (destination traffic classification)
                if has_consumer:
                    consumer = sample_policy.get("consumer", {})
                    consumer_scalable_groups = consumer.get("scalableGroup", []) if isinstance(consumer, dict) else []

                    self.log(
                        "Sample policy has consumer data (destination traffic classification). "
                        "Consumer structure: type={0}, has_scalableGroup={1}, scalableGroup_count={2}. "
                        "Consumer data provides destination group references for policy application.".format(
                            type(consumer).__name__,
                            "scalableGroup" in consumer if isinstance(consumer, dict) else False,
                            len(consumer_scalable_groups) if isinstance(consumer_scalable_groups, list) else 0
                        ),
                        "DEBUG"
                    )

                    # Log sample consumer data structure
                    if consumer_scalable_groups and len(consumer_scalable_groups) > 0:
                        first_consumer_group = consumer_scalable_groups[0]
                        self.log(
                            "Sample consumer scalableGroup entry: type={0}, keys={1}. This "
                            "represents destination group for policy application.".format(
                                type(first_consumer_group).__name__,
                                list(first_consumer_group.keys()) if isinstance(first_consumer_group, dict) else "N/A"
                            ),
                            "DEBUG"
                        )
                else:
                    self.log(
                        "Sample policy does not have consumer data. This is normal for some policy "
                        "types (queuing customization, global configuration).",
                        "DEBUG"
                    )

                # Log producer data presence (source traffic classification)
                if has_producer:
                    producer = sample_policy.get("producer", {})
                    producer_scalable_groups = producer.get("scalableGroup", []) if isinstance(producer, dict) else []

                    self.log(
                        "Sample policy has producer data (source traffic classification). Producer "
                        "scalableGroup count: {0}. This provides application set references for "
                        "traffic classification.".format(
                            len(producer_scalable_groups) if isinstance(producer_scalable_groups, list) else 0
                        ),
                        "DEBUG"
                    )

            # Transform policies using consolidation and transformation logic
            self.log(
                "Initiating policy transformation. Calling transform_application_policies() to "
                "consolidate multiple API entries per policyScope and transform to playbook format. "
                "Input policy entries: {0}".format(len(policies)),
                "INFO"
            )

            transformed_policies = self.transform_application_policies(policies)

            if not isinstance(transformed_policies, list):
                self.log(
                    "Policy transformation returned non-list result. Expected list, got: {0}. "
                    "This indicates a transformation error. Returning empty policy list.".format(
                        type(transformed_policies).__name__
                    ),
                    "ERROR"
                )
                return {"application_policy": []}

            self.log(
                "Successfully transformed {0} application policy entries into {1} consolidated "
                "playbook policy configurations. Average consolidation ratio: {2:.1f} API entries "
                "per playbook policy.".format(
                    len(policies),
                    len(transformed_policies),
                    len(policies) / len(transformed_policies) if transformed_policies else 0
                ),
                "INFO"
            )

            # Log summary of policies with/without clauses
            policies_with_clauses = sum(1 for p in transformed_policies if "clause" in p)
            policies_without_clauses = len(transformed_policies) - policies_with_clauses
            policies_with_qos = sum(1 for p in transformed_policies if "application_queuing_profile_name" in p)
            wireless_policies = sum(1 for p in transformed_policies if p.get("device_type") == "wireless")
            wired_policies = sum(1 for p in transformed_policies if p.get("device_type") == "wired")

            self.log(
                "Policy transformation summary statistics: Total playbook policies: {0}, "
                "Policies with application clauses: {1}, Policies without clauses (QoS-only): {2}, "
                "Policies with QoS profiles: {3}, Wireless policies: {4}, Wired policies: {5}".format(
                    len(transformed_policies),
                    policies_with_clauses,
                    policies_without_clauses,
                    policies_with_qos,
                    wireless_policies,
                    wired_policies
                ),
                "INFO"
            )

            if transformed_policies and len(transformed_policies) > 0:
                sample_transformed = transformed_policies[0]

                self.log(
                    "Sample transformed policy structure: name='{0}', policy_status='{1}', "
                    "device_type='{2}', site_count={3}, has_clause={4}, has_qos_profile={5}, "
                    "has_ssid={6}".format(
                        sample_transformed.get("name", "N/A"),
                        sample_transformed.get("policy_status", "N/A"),
                        sample_transformed.get("device_type", "N/A"),
                        len(sample_transformed.get("site_names", [])),
                        "clause" in sample_transformed,
                        "application_queuing_profile_name" in sample_transformed,
                        "ssid_name" in sample_transformed
                    ),
                    "DEBUG"
                )

                # Log clause details if present
                if "clause" in sample_transformed:
                    clause = sample_transformed.get("clause", [])
                    if clause and len(clause) > 0:
                        first_clause = clause[0]
                        relevance_details = first_clause.get("relevance_details", [])
                        total_app_sets = sum(len(rd.get("application_set_name", [])) for rd in relevance_details)

                        self.log(
                            "Sample policy clause structure: clause_type='{0}', relevance_levels={1}, "
                            "total_application_sets={2}".format(
                                first_clause.get("clause_type", "N/A"),
                                len(relevance_details),
                                total_app_sets
                            ),
                            "DEBUG"
                        )

            self.log(
                "Application policy retrieval and transformation completed successfully. Returning "
                "{0} consolidated policy configurations wrapped in 'application_policy' key for "
                "YAML generation.".format(len(transformed_policies)),
                "INFO"
            )

            return {"application_policy": transformed_policies}

        except Exception as e:
            self.log(
                "Exception occurred during application policy retrieval or transformation. "
                "Error type: {0}, Error message: {1}. This may indicate API unavailability, "
                "authentication failures, network issues, or transformation errors. Returning "
                "empty policy list to allow graceful continuation.".format(
                    type(e).__name__, str(e)
                ),
                "ERROR"
            )

            import traceback
            self.log(
                "Full exception traceback for application policy retrieval: {0}".format(
                    traceback.format_exc()
                ),
                "DEBUG"
            )
            return {"application_policy": []}

    def transform_queuing_profiles(self, profiles):
        """
        Transforms queuing profiles from Cisco Catalyst Center API response to playbook-compatible
        format for application_policy_workflow_manager module.

        This function processes raw queuing profile data from the API, extracting profile metadata,
        bandwidth settings across different interface speeds, and DSCP customizations to create
        playbook configurations that can be used for policy deployment and management.

        Args:
            profiles (list): List of queuing profile dictionaries from get_application_policy_queuing_profile
                            API response. Each profile contains name, description, and clause array.

        Returns:
            list: List of transformed queuing profile dictionaries in playbook format with OrderedDict
                 structures. Returns empty list if:
                 - profiles is None or empty
                 - No valid profiles found (all skipped due to type issues)
                 - All profiles missing required fields
        """
        self.log(
            "Starting transformation of queuing profiles from API response to playbook format",
            "DEBUG"
        )

        if not profiles:
            self.log(
                "No queuing profiles provided for transformation. Returning empty profile list.",
                "INFO"
            )
            return []

        if not isinstance(profiles, list):
            self.log(
                "Profiles parameter is not a list - invalid input. Expected list, got: {0}. "
                "Returning empty profile list.".format(type(profiles).__name__),
                "WARNING"
            )
            return []

        self.log(
            "Received {0} queuing profile(s) from API for transformation. Starting profile "
            "iteration and clause processing.".format(len(profiles)),
            "INFO"
        )

        transformed_profiles = []

        for profile_index, profile in enumerate(profiles, start=1):
            self.log(
                "Processing queuing profile {0}/{1} for transformation".format(
                    profile_index, len(profiles)
                ),
                "DEBUG"
            )

            if not isinstance(profile, dict):
                self.log(
                    "Queuing profile {0}/{1} is not a dictionary - skipping. Expected dict, "
                    "got: {2}. Continuing to next profile.".format(
                        profile_index, len(profiles), type(profile).__name__
                    ),
                    "WARNING"
                )
                continue

            profile_data = OrderedDict()

            # Basic profile information
            profile_name = profile.get("name")
            profile_description = profile.get("description", "")

            self.log(
                "Extracting basic metadata for profile {0}/{1}: name='{2}', "
                "description='{3}' (length={4})".format(
                    profile_index, len(profiles), profile_name,
                    profile_description[:50] + "..." if len(profile_description) > 50 else profile_description,
                    len(profile_description)
                ),
                "DEBUG"
            )

            profile_data["profile_name"] = profile_name
            profile_data["profile_description"] = profile_description

            # Process clauses for bandwidth and DSCP settings
            clauses = profile.get("clause", [])

            self.log(
                "Extracting clause data from profile '{0}' ({1}/{2}). Clause array length: {3}. "
                "Calling extract_settings_from_clauses() to process bandwidth and DSCP settings.".format(
                    profile_name, profile_index, len(profiles), len(clauses) if clauses else 0
                ),
                "DEBUG"
            )

            if clauses:
                bandwidth_settings, dscp_settings = self.extract_settings_from_clauses(clauses)

                self.log(
                    "Clause extraction complete for profile '{0}' ({1}/{2}). Bandwidth settings "
                    "found: {3}, DSCP settings found: {4}".format(
                        profile_name, profile_index, len(profiles),
                        bandwidth_settings is not None, dscp_settings is not None
                    ),
                    "DEBUG"
                )

                if bandwidth_settings:
                    profile_data["bandwidth_settings"] = bandwidth_settings

                    is_common = bandwidth_settings.get("is_common_between_all_interface_speeds", False)

                    self.log(
                        "Added bandwidth settings to profile '{0}' ({1}/{2}). Configuration type: "
                        "{3}, interface speeds: {4}".format(
                            profile_name, profile_index, len(profiles),
                            "common (ALL speeds)" if is_common else "interface-specific",
                            bandwidth_settings.get("interface_speed") if is_common else
                            len(bandwidth_settings.get("interface_speed_settings", []))
                        ),
                        "INFO"
                    )
                else:
                    self.log(
                        "No bandwidth settings extracted for profile '{0}' ({1}/{2}). Bandwidth "
                        "settings field will be omitted from playbook configuration.".format(
                            profile_name, profile_index, len(profiles)
                        ),
                        "DEBUG"
                    )

                if dscp_settings:
                    profile_data["dscp_settings"] = dscp_settings

                    self.log(
                        "Added DSCP settings to profile '{0}' ({1}/{2}). DSCP customizations "
                        "for {3} traffic class(es): {4}".format(
                            profile_name, profile_index, len(profiles),
                            len(dscp_settings),
                            list(dscp_settings.keys())[:5]  # Show first 5 traffic classes
                        ),
                        "INFO"
                    )
                else:
                    self.log(
                        "No DSCP settings extracted for profile '{0}' ({1}/{2}). DSCP settings "
                        "field will be omitted from playbook configuration.".format(
                            profile_name, profile_index, len(profiles)
                        ),
                        "DEBUG"
                    )

            transformed_profiles.append(profile_data)

            self.log(
                "Successfully transformed queuing profile {0}/{1}: '{2}'. Profile structure: "
                "has_bandwidth_settings={3}, has_dscp_settings={4}, total_fields={5}".format(
                    profile_index, len(profiles), profile_name,
                    "bandwidth_settings" in profile_data,
                    "dscp_settings" in profile_data,
                    len(profile_data)
                ),
                "INFO"
            )

        self.log(
            "Completed transformation of all queuing profiles. Successfully transformed {0} out "
            "of {1} profile(s) from API response. Skipped profiles (type errors): {2}".format(
                len(transformed_profiles), len(profiles), len(profiles) - len(transformed_profiles)
            ),
            "INFO"
        )

        # Log summary statistics
        profiles_with_bandwidth = sum(1 for p in transformed_profiles if "bandwidth_settings" in p)
        profiles_with_dscp = sum(1 for p in transformed_profiles if "dscp_settings" in p)
        profiles_with_both = sum(1 for p in transformed_profiles if "bandwidth_settings" in p and "dscp_settings" in p)
        profiles_minimal = sum(1 for p in transformed_profiles if "bandwidth_settings" not in p and "dscp_settings" not in p)

        self.log(
            "Transformation summary statistics: Total profiles: {0}, With bandwidth settings: {1}, "
            "With DSCP settings: {2}, With both settings: {3}, Minimal (no QoS settings): {4}".format(
                len(transformed_profiles), profiles_with_bandwidth, profiles_with_dscp,
                profiles_with_both, profiles_minimal
            ),
            "INFO"
        )

        return transformed_profiles

    def extract_settings_from_clauses(self, clauses):
        """
        Extracts bandwidth and DSCP settings from queuing profile clause arrays.

        This function processes clause data from get_application_policy_queuing_profile API response,
        parsing BANDWIDTH and DSCP_CUSTOMIZATION clause types to extract traffic class configurations
        for both common (ALL speeds) and interface-specific bandwidth settings, plus DSCP value mappings.

        Purpose:
            Processes queuing profile clauses to extract QoS configurations by:
            - Parsing BANDWIDTH clauses for common (ALL speeds) or interface-specific settings
            - Extracting traffic class bandwidth percentage allocations
            - Processing DSCP_CUSTOMIZATION clauses for traffic class DSCP value mappings
            - Converting API traffic class names to playbook-compatible snake_case format
            - Creating OrderedDict structures for consistent YAML field ordering
            - Handling both common and interface-specific bandwidth configurations

        Args:
            clauses (list): List of clause dictionaries from get_application_policy_queuing_profile
                           API response. Each clause contains type field (BANDWIDTH, DSCP_CUSTOMIZATION)
                           and associated configuration data.

        Returns:
            tuple: (bandwidth_settings, dscp_settings) where:
                  - bandwidth_settings: OrderedDict with bandwidth configuration or None
                  - dscp_settings: OrderedDict with DSCP mappings or None
                  Both can be None independently if corresponding clause type not found.
        """
        if not clauses:
            self.log(
                "No clauses provided for settings extraction. Returning (None, None).",
                "INFO"
            )
            return None, None

        if not isinstance(clauses, list):
            self.log(
                "Clauses parameter is not a list - invalid input. Expected list, got: {0}. "
                "Returning (None, None).".format(type(clauses).__name__),
                "WARNING"
            )
            return None, None

        bandwidth_settings = None
        dscp_settings = OrderedDict()

        # Traffic class mapping for bandwidth percentages
        tc_map = {
            "BROADCAST_VIDEO": "broadcast_video",
            "BULK_DATA": "bulk_data",
            "MULTIMEDIA_CONFERENCING": "multimedia_conferencing",
            "MULTIMEDIA_STREAMING": "multimedia_streaming",
            "NETWORK_CONTROL": "network_control",
            "OPS_ADMIN_MGMT": "ops_admin_mgmt",
            "REAL_TIME_INTERACTIVE": "real_time_interactive",
            "SIGNALING": "signaling",
            "TRANSACTIONAL_DATA": "transactional_data",
            "VOIP_TELEPHONY": "voip_telephony",
            "BEST_EFFORT": "best_effort",
            "SCAVENGER": "scavenger"
        }

        self.log(
            "Initialized traffic class mapping dictionary with {0} standard traffic class names. "
            "Starting clause iteration.".format(len(tc_map)),
            "DEBUG"
        )

        for clause_index, clause in enumerate(clauses, start=1):
            self.log(
                "Processing clause {0}/{1} for bandwidth and DSCP settings extraction".format(
                    clause_index, len(clauses)
                ),
                "DEBUG"
            )

            if not isinstance(clause, dict):
                self.log(
                    "Clause {0}/{1} is not a dictionary - skipping. Expected dict, got: {2}. "
                    "Continuing to next clause.".format(
                        clause_index, len(clauses), type(clause).__name__
                    ),
                    "WARNING"
                )
                continue

            clause_type = clause.get("type")

            self.log(
                "Clause {0}/{1} type: '{2}'. Determining processing path based on clause type.".format(
                    clause_index, len(clauses), clause_type
                ),
                "DEBUG"
            )

            # Process bandwidth settings
            if clause_type == "BANDWIDTH":
                is_common = clause.get("isCommonBetweenAllInterfaceSpeeds", False)

                self.log(
                    "Processing BANDWIDTH clause {0}/{1}. Common across all interface speeds: {2}".format(
                        clause_index, len(clauses), is_common
                    ),
                    "INFO"
                )

                interface_speed_clauses = clause.get("interfaceSpeedBandwidthClauses", [])

                if not interface_speed_clauses:
                    self.log(
                        "No interfaceSpeedBandwidthClauses found in BANDWIDTH clause {0}/{1}. "
                        "This clause cannot be processed without interface speed bandwidth data. "
                        "Skipping clause.".format(clause_index, len(clauses)),
                        "WARNING"
                    )
                    continue

                if not isinstance(interface_speed_clauses, list):
                    self.log(
                        "interfaceSpeedBandwidthClauses in clause {0}/{1} is not a list. "
                        "Expected list, got: {2}. Skipping clause.".format(
                            clause_index, len(clauses), type(interface_speed_clauses).__name__
                        ),
                        "WARNING"
                    )
                    continue

                self.log(
                    "Found {0} interface speed bandwidth clause(s) in BANDWIDTH clause {1}/{2}".format(
                        len(interface_speed_clauses), clause_index, len(clauses)
                    ),
                    "DEBUG"
                )

                if is_common:
                    self.log(
                        "Creating common bandwidth settings structure for clause {0}/{1}. "
                        "Interface speed will be set to 'ALL'.".format(clause_index, len(clauses)),
                        "DEBUG"
                    )

                    # Common bandwidth settings across all interface speeds
                    bandwidth_settings = OrderedDict([
                        ("is_common_between_all_interface_speeds", True),
                        ("interface_speed", "ALL"),
                        ("bandwidth_percentages", OrderedDict())
                    ])

                    # Get the first (and should be only) interface speed clause for "ALL"
                    if len(interface_speed_clauses) > 0:
                        first_speed_clause = interface_speed_clauses[0]
                        tc_bandwidth_settings = first_speed_clause.get("tcBandwidthSettings", [])

                        self.log(
                            "Extracting traffic class bandwidth settings from first interface speed "
                            "clause. Traffic class bandwidth settings count: {0}".format(
                                len(tc_bandwidth_settings)
                            ),
                            "DEBUG"
                        )

                        if not isinstance(tc_bandwidth_settings, list):
                            self.log(
                                "tcBandwidthSettings is not a list in interface speed clause. "
                                "Expected list, got: {0}. Using empty list.".format(
                                    type(tc_bandwidth_settings).__name__
                                ),
                                "WARNING"
                            )
                            tc_bandwidth_settings = []

                        for tc_index, tc_setting in enumerate(tc_bandwidth_settings, start=1):
                            if not isinstance(tc_setting, dict):
                                self.log(
                                    "Traffic class setting {0}/{1} is not a dictionary - skipping. "
                                    "Expected dict, got: {2}".format(
                                        tc_index, len(tc_bandwidth_settings), type(tc_setting).__name__
                                    ),
                                    "WARNING"
                                )
                                continue

                            tc_name = tc_setting.get("trafficClass")
                            bandwidth_percent = tc_setting.get("bandwidthPercentage")

                            self.log(
                                "Processing traffic class bandwidth setting {0}/{1}: "
                                "trafficClass='{2}', bandwidthPercentage={3}".format(
                                    tc_index, len(tc_bandwidth_settings), tc_name, bandwidth_percent
                                ),
                                "DEBUG"
                            )

                            if tc_name in tc_map and bandwidth_percent is not None:
                                playbook_tc_name = tc_map[tc_name]
                                bandwidth_settings["bandwidth_percentages"][playbook_tc_name] = str(bandwidth_percent)

                                self.log(
                                    "Added bandwidth allocation for traffic class {0}/{1}: "
                                    "API name '{2}' → playbook name '{3}', bandwidth: {4}%".format(
                                        tc_index, len(tc_bandwidth_settings), tc_name,
                                        playbook_tc_name, bandwidth_percent
                                    ),
                                    "INFO"
                                )
                            else:
                                self.log(
                                    "Skipping traffic class bandwidth setting {0}/{1}. "
                                    "Reason: trafficClass '{2}' not in mapping (in_map={3}) or "
                                    "bandwidthPercentage is None (is_none={4})".format(
                                        tc_index, len(tc_bandwidth_settings), tc_name,
                                        tc_name in tc_map if tc_name else False,
                                        bandwidth_percent is None
                                    ),
                                    "DEBUG"
                                )

                        self.log(
                            "Completed common bandwidth settings extraction for clause {0}/{1}. "
                            "Total traffic classes configured: {2}".format(
                                clause_index, len(clauses),
                                len(bandwidth_settings["bandwidth_percentages"])
                            ),
                            "INFO"
                        )

                else:
                    self.log(
                        "Creating interface-specific bandwidth settings structure for clause {0}/{1}. "
                        "Processing multiple interface speeds.".format(clause_index, len(clauses)),
                        "DEBUG"
                    )

                    # Interface-specific bandwidth settings
                    bandwidth_settings = OrderedDict([
                        ("is_common_between_all_interface_speeds", False),
                        ("interface_speed_settings", [])
                    ])

                    for speed_clause_index, speed_clause in enumerate(interface_speed_clauses, start=1):
                        if not isinstance(speed_clause, dict):
                            self.log(
                                "Interface speed clause {0}/{1} in BANDWIDTH clause {2}/{3} is not "
                                "a dictionary - skipping. Expected dict, got: {4}".format(
                                    speed_clause_index, len(interface_speed_clauses),
                                    clause_index, len(clauses), type(speed_clause).__name__
                                ),
                                "WARNING"
                            )
                            continue

                        interface_speed = speed_clause.get("interfaceSpeed")
                        tc_bandwidth_settings = speed_clause.get("tcBandwidthSettings", [])

                        self.log(
                            "Processing interface speed clause {0}/{1}: interface_speed='{2}', "
                            "traffic class count={3}".format(
                                speed_clause_index, len(interface_speed_clauses),
                                interface_speed, len(tc_bandwidth_settings)
                            ),
                            "DEBUG"
                        )

                        speed_setting = OrderedDict([
                            ("interface_speed", interface_speed),
                            ("bandwidth_percentages", OrderedDict())
                        ])

                        if not isinstance(tc_bandwidth_settings, list):
                            self.log(
                                "tcBandwidthSettings for interface speed '{0}' is not a list. "
                                "Expected list, got: {1}. Using empty list.".format(
                                    interface_speed, type(tc_bandwidth_settings).__name__
                                ),
                                "WARNING"
                            )
                            tc_bandwidth_settings = []

                        for tc_index, tc_setting in enumerate(tc_bandwidth_settings, start=1):
                            if not isinstance(tc_setting, dict):
                                self.log(
                                    "Traffic class setting {0}/{1} for interface speed '{2}' is "
                                    "not a dictionary - skipping. Expected dict, got: {3}".format(
                                        tc_index, len(tc_bandwidth_settings), interface_speed,
                                        type(tc_setting).__name__
                                    ),
                                    "WARNING"
                                )
                                continue

                            tc_name = tc_setting.get("trafficClass")
                            bandwidth_percent = tc_setting.get("bandwidthPercentage")

                            if tc_name in tc_map and bandwidth_percent is not None:
                                playbook_tc_name = tc_map[tc_name]
                                speed_setting["bandwidth_percentages"][playbook_tc_name] = str(bandwidth_percent)

                                self.log(
                                    "Added bandwidth for interface speed '{0}', traffic class "
                                    "{1}/{2}: '{3}' → '{4}', bandwidth: {5}%".format(
                                        interface_speed, tc_index, len(tc_bandwidth_settings),
                                        tc_name, playbook_tc_name, bandwidth_percent
                                    ),
                                    "DEBUG"
                                )
                            else:
                                self.log(
                                    "Skipping traffic class {0}/{1} for interface speed '{2}'. "
                                    "trafficClass '{3}' not in mapping or bandwidthPercentage is None".format(
                                        tc_index, len(tc_bandwidth_settings), interface_speed, tc_name
                                    ),
                                    "DEBUG"
                                )

                        bandwidth_settings["interface_speed_settings"].append(speed_setting)

                        self.log(
                            "Completed interface speed setting {0}/{1}: speed='{2}', "
                            "traffic classes configured={3}".format(
                                speed_clause_index, len(interface_speed_clauses),
                                interface_speed, len(speed_setting["bandwidth_percentages"])
                            ),
                            "INFO"
                        )

                    self.log(
                        "Completed interface-specific bandwidth settings extraction for clause "
                        "{0}/{1}. Total interface speeds configured: {2}".format(
                            clause_index, len(clauses),
                            len(bandwidth_settings["interface_speed_settings"])
                        ),
                        "INFO"
                    )

            # Process DSCP settings
            elif clause_type == "DSCP_CUSTOMIZATION":
                self.log(
                    "Processing DSCP_CUSTOMIZATION clause {0}/{1}. Extracting traffic class "
                    "DSCP value mappings.".format(clause_index, len(clauses)),
                    "INFO"
                )

                tc_dscp_settings = clause.get("tcDscpSettings", [])

                if not isinstance(tc_dscp_settings, list):
                    self.log(
                        "tcDscpSettings in DSCP_CUSTOMIZATION clause {0}/{1} is not a list. "
                        "Expected list, got: {2}. Using empty list.".format(
                            clause_index, len(clauses), type(tc_dscp_settings).__name__
                        ),
                        "WARNING"
                    )
                    tc_dscp_settings = []

                self.log(
                    "Found {0} traffic class DSCP setting(s) in DSCP_CUSTOMIZATION clause {1}/{2}".format(
                        len(tc_dscp_settings), clause_index, len(clauses)
                    ),
                    "DEBUG"
                )

                for tc_index, tc_setting in enumerate(tc_dscp_settings, start=1):
                    if not isinstance(tc_setting, dict):
                        self.log(
                            "Traffic class DSCP setting {0}/{1} is not a dictionary - skipping. "
                            "Expected dict, got: {2}".format(
                                tc_index, len(tc_dscp_settings), type(tc_setting).__name__
                            ),
                            "WARNING"
                        )
                        continue

                    tc_name = tc_setting.get("trafficClass")
                    dscp_value = tc_setting.get("dscp")

                    self.log(
                        "Processing traffic class DSCP setting {0}/{1}: trafficClass='{2}', "
                        "dscp='{3}'".format(tc_index, len(tc_dscp_settings), tc_name, dscp_value),
                        "DEBUG"
                    )

                    if tc_name in tc_map and dscp_value is not None:
                        playbook_tc_name = tc_map[tc_name]
                        dscp_settings[playbook_tc_name] = str(dscp_value)

                        self.log(
                            "Added DSCP mapping for traffic class {0}/{1}: API name '{2}' → "
                            "playbook name '{3}', DSCP value: '{4}'".format(
                                tc_index, len(tc_dscp_settings), tc_name, playbook_tc_name, dscp_value
                            ),
                            "INFO"
                        )
                    else:
                        self.log(
                            "Skipping traffic class DSCP setting {0}/{1}. Reason: trafficClass "
                            "'{2}' not in mapping (in_map={3}) or dscp value is None (is_none={4})".format(
                                tc_index, len(tc_dscp_settings), tc_name,
                                tc_name in tc_map if tc_name else False,
                                dscp_value is None
                            ),
                            "DEBUG"
                        )

                self.log(
                    "Completed DSCP settings extraction for clause {0}/{1}. Total DSCP mappings: {2}".format(
                        clause_index, len(clauses), len(dscp_settings)
                    ),
                    "INFO"
                )

        dscp_result = dscp_settings if dscp_settings else None

        self.log(
            "Completed extraction of settings from all {0} clause(s). Bandwidth settings found: {1}, "
            "DSCP settings found: {2}. Bandwidth type: {3}, DSCP mapping count: {4}".format(
                len(clauses),
                bandwidth_settings is not None,
                dscp_result is not None,
                "common (ALL speeds)" if bandwidth_settings and bandwidth_settings.get("is_common_between_all_interface_speeds")
                else "interface-specific" if bandwidth_settings else "N/A",
                len(dscp_result) if dscp_result else 0
            ),
            "INFO"
        )

        return bandwidth_settings, dscp_result

    def get_queuing_profiles(self, network_element, config):
        """
        Retrieves queuing profiles from Cisco Catalyst Center and transforms them into
        playbook-compatible format.

        This function fetches all queuing profiles from the Catalyst Center API, applies
        optional name-based filtering, and transforms the API response into the structure
        required by the application_policy_workflow_manager module for playbook generation.

        Args:
            network_element (dict): Network element definition from module schema containing
                                   API configuration (family, function, filters).
            config (dict): Configuration dictionary containing component_specific_filters with
                          optional profile_names_list for filtering specific profiles.

        Returns:
            dict: Dictionary with 'queuing_profile' key containing list of transformed
                 profile configurations in playbook format. Returns empty dict if:
                 - API call fails or raises exception
                 - No profiles found in Catalyst Center
                 - All profiles filtered out by profile_names_list
                 - Transformation fails completely
        """
        self.log(
            "Starting queuing profile retrieval with configuration filters. "
            "Has component_specific_filters: {0}".format(
                bool(config.get("component_specific_filters"))
            ),
            "INFO"
        )

        # Extract filters from config
        component_specific_filters = config.get("component_specific_filters", {})
        queuing_profile_filters = component_specific_filters.get("queuing_profile", {})
        profile_names_list = queuing_profile_filters.get("profile_names_list", [])

        self.log(
            "Extracted filter parameters. component_specific_filters present: {0}, "
            "queuing_profile filters present: {1}, profile_names_list count: {2}, "
            "profile names: {3}".format(
                bool(component_specific_filters),
                bool(queuing_profile_filters),
                len(profile_names_list) if profile_names_list else 0,
                profile_names_list if profile_names_list else "None (retrieve all profiles)"
            ),
            "DEBUG"
        )

        if profile_names_list:
            self.log(
                "Filtering queuing profiles by {0} profile name(s): {1}".format(
                    len(profile_names_list), profile_names_list
                ),
                "INFO"
            )
        else:
            self.log(
                "No profile name filter specified - will retrieve all queuing profiles",
                "INFO"
            )

        try:
            # Get queuing profiles
            response = self.dnac._exec(
                family="application_policy",
                function="get_application_policy_queuing_profile",
                op_modifies=False,
            )
            self.log(
                "Received API response for queuing profile query. Response structure: {0}".format(
                    {
                        "has_response_key": "response" in response if response else False,
                        "response_type": type(response.get("response")).__name__ if response and "response" in response else "N/A",
                        "response_count": len(response.get("response")) if response and isinstance(response.get("response"), list) else 0
                    } if response else "No response"
                ),
                "DEBUG"
            )

            if not response or not response.get("response"):
                self.log(
                    "No queuing profiles found in API response. Response is None or missing "
                    "'response' key. This may indicate no profiles configured in Catalyst Center, "
                    "API unavailability, or authentication issues. Returning empty profile dictionary.",
                    "WARNING"
                )
                return {"queuing_profile": []}

            profiles = response.get("response", [])

            if not isinstance(profiles, list):
                self.log(
                    "API response 'response' field is not a list. Got type: {0}. This indicates "
                    "an unexpected API response format. Returning empty profile dictionary.".format(
                        type(profiles).__name__
                    ),
                    "WARNING"
                )
                return {"queuing_profile": []}

            if not profiles:
                self.log(
                    "API returned empty profile list. No queuing profiles are configured in "
                    "Catalyst Center. Returning empty profile dictionary.",
                    "WARNING"
                )
                return {"queuing_profile": []}

            self.log(
                "Successfully retrieved {0} total queuing profile(s) from Catalyst Center API.".format(
                    len(profiles)
                ),
                "INFO"
            )

            # Filter by profile names if specified
            if profile_names_list:
                original_count = len(profiles)
                profiles = [p for p in profiles if p.get("name") in profile_names_list]

                self.log(
                    "Applied client-side filtering based on profile_names_list. Original profiles: "
                    "{0}, filtered profiles: {1}, filter matched: {2}/{3} requested profile names, "
                    "requested names: {4}".format(
                        original_count,
                        len(profiles),
                        len(set(p.get("name") for p in profiles)),
                        len(profile_names_list),
                        profile_names_list
                    ),
                    "INFO"
                )

                if not profiles:
                    self.log(
                        "No queuing profiles matched the filter criteria after applying "
                        "profile_names_list filter. Requested profile names: {0}. These profiles "
                        "may not exist in Catalyst Center or names may be incorrect. Returning "
                        "empty profile dictionary.".format(profile_names_list),
                        "WARNING"
                    )
                    return {"queuing_profile": []}
            else:
                self.log(
                    "No profile name filtering specified (profile_names_list is empty or not "
                    "provided). Proceeding with all {0} profile(s) from API.".format(
                        len(profiles)
                    ),
                    "INFO"
                )

            # Log sample profile structure for debugging
            if profiles and len(profiles) > 0:
                sample_profile = profiles[0]
                profile_keys = list(sample_profile.keys())
                has_clause = "clause" in sample_profile
                clause_count = len(sample_profile.get("clause", [])) if has_clause else 0

                self.log(
                    "Sample profile structure analysis (first profile): keys={0}, "
                    "profile_name='{1}', has_clause={2}, clause_count={3}".format(
                        profile_keys,
                        sample_profile.get("name", "N/A"),
                        has_clause,
                        clause_count
                    ),
                    "DEBUG"
                )

            self.log(
                "Initiating profile transformation. Calling transform_queuing_profiles() to "
                "extract metadata, bandwidth settings, and DSCP settings. Input profile count: {0}".format(
                    len(profiles)
                ),
                "INFO"
            )

            # Transform profiles
            transformed_profiles = self.transform_queuing_profiles(profiles)

            if not isinstance(transformed_profiles, list):
                self.log(
                    "Profile transformation returned non-list result. Expected list, got: {0}. "
                    "This indicates a transformation error. Returning empty profile dictionary.".format(
                        type(transformed_profiles).__name__
                    ),
                    "ERROR"
                )
                return {"queuing_profile": []}

            self.log(
                "Successfully transformed {0} queuing profile(s) from API response.".format(
                    len(transformed_profiles)
                ),
                "INFO"
            )

            # Log summary statistics
            profiles_with_bandwidth = sum(1 for p in transformed_profiles if "bandwidth_settings" in p)
            profiles_with_dscp = sum(1 for p in transformed_profiles if "dscp_settings" in p)
            profiles_with_both = sum(1 for p in transformed_profiles if "bandwidth_settings" in p and "dscp_settings" in p)
            profiles_minimal = sum(1 for p in transformed_profiles if "bandwidth_settings" not in p and "dscp_settings" not in p)

            self.log(
                "Profile transformation summary statistics: Total profiles: {0}, With bandwidth "
                "settings: {1}, With DSCP settings: {2}, With both settings: {3}, Minimal "
                "(no QoS settings): {4}".format(
                    len(transformed_profiles),
                    profiles_with_bandwidth,
                    profiles_with_dscp,
                    profiles_with_both,
                    profiles_minimal
                ),
                "INFO"
            )

            # Log sample transformed profile structure
            if transformed_profiles and len(transformed_profiles) > 0:
                sample_transformed = transformed_profiles[0]

                self.log(
                    "Sample transformed profile structure: profile_name='{0}', "
                    "description_length={1}, has_bandwidth_settings={2}, has_dscp_settings={3}, "
                    "total_fields={4}".format(
                        sample_transformed.get("profile_name", "N/A"),
                        len(sample_transformed.get("profile_description", "")),
                        "bandwidth_settings" in sample_transformed,
                        "dscp_settings" in sample_transformed,
                        len(sample_transformed)
                    ),
                    "DEBUG"
                )

                # Log bandwidth settings structure if present
                if "bandwidth_settings" in sample_transformed:
                    bandwidth_settings = sample_transformed.get("bandwidth_settings", {})
                    is_common = bandwidth_settings.get("is_common_between_all_interface_speeds", False)

                    self.log(
                        "Sample profile bandwidth settings structure: is_common={0}, "
                        "interface_speed='{1}', has_bandwidth_percentages={2}".format(
                            is_common,
                            bandwidth_settings.get("interface_speed") if is_common else "interface-specific",
                            "bandwidth_percentages" in bandwidth_settings
                        ),
                        "DEBUG"
                    )

                # Log DSCP settings structure if present
                if "dscp_settings" in sample_transformed:
                    dscp_settings = sample_transformed.get("dscp_settings", {})

                    self.log(
                        "Sample profile DSCP settings structure: traffic_class_count={0}, "
                        "sample_classes={1}".format(
                            len(dscp_settings),
                            list(dscp_settings.keys())[:3] if len(dscp_settings) > 3 else list(dscp_settings.keys())
                        ),
                        "DEBUG"
                    )

            self.log(
                "Queuing profile retrieval and transformation completed successfully. Returning "
                "{0} profile configuration(s) wrapped in 'queuing_profile' key for YAML generation.".format(
                    len(transformed_profiles)
                ),
                "INFO"
            )

            return {"queuing_profile": transformed_profiles}

        except Exception as e:
            self.log(
                "Exception occurred during queuing profile retrieval or transformation. "
                "Error type: {0}, Error message: {1}. This may indicate API unavailability, "
                "authentication failures, network issues, or transformation errors. Returning "
                "empty profile dictionary to allow graceful continuation.".format(
                    type(e).__name__, str(e)
                ),
                "ERROR"
            )

            # Log full traceback for debugging
            import traceback
            self.log(
                "Full exception traceback for queuing profile retrieval: {0}".format(
                    traceback.format_exc()
                ),
                "DEBUG"
            )

            return {"queuing_profile": []}

    def yaml_config_generator(self, yaml_config_generator):
        """
        Generates YAML configuration file from retrieved application policy and queuing profile data.

        This function orchestrates the complete YAML generation workflow by retrieving component
        configurations from Cisco Catalyst Center, transforming them to playbook format, and
        writing the consolidated output to a YAML file compatible with application_policy_workflow_manager.

        Args:
            yaml_config_generator (dict): Configuration dictionary containing file path and component filters.

        Returns:
            object: Self instance with updated status and result information.
        """
        self.log(
            "Starting YAML configuration file generation workflow for module '{0}'. Processing "
            "configuration and determining output file path.".format(self.module_name),
            "INFO"
        )

        if not isinstance(yaml_config_generator, dict):
            self.msg = (
                "yaml_config_generator parameter must be a dictionary, got: {0}. Cannot "
                "proceed with YAML generation.".format(type(yaml_config_generator).__name__)
            )
            self.set_operation_result("failed", False, self.msg, "ERROR")
            return self

        try:
            # Determine output file path (user-provided or auto-generated)
            file_path = yaml_config_generator.get("file_path")

            if not file_path:
                self.log(
                    "No file_path provided in configuration. Generating default filename using "
                    "timestamp-based naming convention.",
                    "DEBUG"
                )
                file_path = self.generate_filename()

                if not file_path:
                    self.msg = (
                        "Failed to generate default filename for YAML configuration file. "
                        "generate_filename() returned None or empty string."
                    )
                    self.set_operation_result("failed", False, self.msg, "ERROR")
                    return self

                self.log(
                    "Auto-generated default filename for YAML output: '{0}'".format(file_path),
                    "INFO"
                )
            else:
                self.log(
                    "Using user-provided file path for YAML output: '{0}'".format(file_path),
                    "INFO"
                )

            component_specific_filters = yaml_config_generator.get("component_specific_filters", {})
            components_list = component_specific_filters.get("components_list", ["queuing_profile", "application_policy"])

            self.log(
                "Extracted component configuration. component_specific_filters present: {0}, "
                "components_list: {1} (count: {2})".format(
                    bool(component_specific_filters),
                    components_list,
                    len(components_list) if components_list else 0
                ),
                "DEBUG"
            )

            if not components_list:
                self.log(
                    "Components list is empty. No components to process. This will result in "
                    "empty configuration output.",
                    "WARNING"
                )

            # Use list of dicts instead of single list
            final_output = []

            components_processed = 0
            components_skipped = 0
            total_configurations = 0

            self.log(
                "Starting component iteration and retrieval. Processing {0} component(s): {1}".format(
                    len(components_list), components_list
                ),
                "INFO"
            )

            # Process each component in the components list
            for component_index, component_name in enumerate(components_list, start=1):
                self.log(
                    "Processing component {0}/{1}: '{2}'. Checking module schema for component "
                    "definition.".format(component_index, len(components_list), component_name),
                    "DEBUG"
                )

                # Validate component exists in module schema
                if component_name not in self.module_schema["network_elements"]:
                    self.log(
                        "Component '{0}' ({1}/{2}) not found in module schema network_elements. "
                        "Available components: {3}. Skipping this component.".format(
                            component_name,
                            component_index,
                            len(components_list),
                            list(self.module_schema["network_elements"].keys())
                        ),
                        "WARNING"
                    )
                    components_skipped += 1
                    continue

                # Get component definition and retrieval function
                network_element = self.module_schema["network_elements"][component_name]
                get_function = network_element.get("get_function_name")

                if not get_function:
                    self.log(
                        "Component '{0}' ({1}/{2}) has no get_function_name defined in schema. "
                        "Cannot retrieve configurations. Skipping this component.".format(
                            component_name, component_index, len(components_list)
                        ),
                        "ERROR"
                    )
                    components_skipped += 1
                    continue

                self.log(
                    "Initiating retrieval for component '{0}' ({1}/{2}). Calling retrieval "
                    "function to fetch configurations from Cisco Catalyst Center.".format(
                        component_name, component_index, len(components_list)
                    ),
                    "INFO"
                )

                # Call component-specific retrieval function
                component_data = get_function(network_element, yaml_config_generator)

                # Validate component data returned
                if not component_data:
                    self.log(
                        "Component '{0}' ({1}/{2}) retrieval returned None or empty result. "
                        "No configurations retrieved for this component. Skipping.".format(
                            component_name, component_index, len(components_list)
                        ),
                        "WARNING"
                    )
                    components_skipped += 1
                    continue

                if not isinstance(component_data, dict):
                    self.log(
                        "Component '{0}' ({1}/{2}) retrieval returned invalid data type. "
                        "Expected dict, got: {3}. Skipping this component.".format(
                            component_name, component_index, len(components_list),
                            type(component_data).__name__
                        ),
                        "WARNING"
                    )
                    components_skipped += 1
                    continue

                # Check if component data contains the component key with actual configurations
                if component_name not in component_data:
                    self.log(
                        "Component '{0}' ({1}/{2}) data missing expected key '{0}'. "
                        "Data keys: {3}. Skipping this component.".format(
                            component_name, component_index, len(components_list),
                            list(component_data.keys())
                        ),
                        "WARNING"
                    )
                    components_skipped += 1
                    continue

                component_configs = component_data.get(component_name)

                if not component_configs:
                    self.log(
                        "Component '{0}' ({1}/{2}) has no configurations (empty list or None). "
                        "No data to include in YAML output. Skipping this component.".format(
                            component_name, component_index, len(components_list)
                        ),
                        "INFO"
                    )
                    components_skipped += 1
                    continue

                config_count = len(component_configs) if isinstance(component_configs, list) else 1

                self.log(
                    "Successfully retrieved {0} configuration(s) for component '{1}' ({2}/{3}). "
                    "Adding to final output collection.".format(
                        config_count, component_name, component_index, len(components_list)
                    ),
                    "INFO"
                )

                # Add component configurations to final output
                final_output.append({component_name: component_configs})
                components_processed += 1
                total_configurations += config_count

            self.log(
                "Completed component iteration. Components processed successfully: {0}, "
                "Components skipped (not found/no data): {1}, Total configurations collected: {2}".format(
                    components_processed, components_skipped, total_configurations
                ),
                "INFO"
            )

            # Validate that we have configurations to write
            if not final_output:
                self.msg = (
                    "No configurations found to generate YAML file. All components either had "
                    "no data or were skipped. Components requested: {0}, Components skipped: {1}. "
                    "No YAML file will be created.".format(
                        components_list, components_skipped
                    )
                )
                self.log(self.msg, "INFO")
                self.set_operation_result("success", False, self.msg, "INFO")
                return self

            self.log(
                "Initiating YAML file write operation. Target file path: '{0}', "
                "Total configurations to write: {1}, Components included: {2}".format(
                    file_path, total_configurations, components_processed
                ),
                "INFO"
            )

            # Write to YAML file
            success = self.write_dict_to_yaml(final_output, file_path)

            if success:
                self.msg = "YAML config generation succeeded for module '{0}'.".format(
                    self.module_name
                )

                # Build structured response with detailed operation metrics
                structured_response = {
                    "status": "success",
                    "message": self.msg,
                    "file_path": file_path,
                    "configurations_count": total_configurations,
                    "components_processed": components_processed,
                    "components_skipped": components_skipped
                }

                self.log(
                    "YAML configuration file successfully written to: '{0}'. Total configurations "
                    "written: {1}, Components included: {2}, File write operation completed.".format(
                        file_path, total_configurations, components_processed
                    ),
                    "INFO"
                )

                # Pass structured response as additional_info to preserve detailed metrics
                self.set_operation_result("success", True, self.msg, "INFO", structured_response)
            else:
                self.msg = (
                    "Failed to write YAML configuration file to path: '{0}'. File write operation "
                    "returned failure status. Check file path validity, permissions, and disk space.".format(
                        file_path
                    )
                )

                self.log(self.msg, "ERROR")
                self.set_operation_result("failed", False, self.msg, "ERROR")

            return self

        except Exception as e:
            self.msg = (
                "Exception occurred during YAML configuration generation workflow. "
                "Error type: {0}, Error message: {1}. YAML file generation failed.".format(
                    type(e).__name__, str(e)
                )
            )

            self.log(self.msg, "ERROR")

            # Log full traceback for debugging
            import traceback
            self.log(
                "Full exception traceback for YAML generation: {0}".format(
                    traceback.format_exc()
                ),
                "DEBUG"
            )

            self.set_operation_result("failed", False, self.msg, "ERROR")
            return self

    def get_diff_gathered(self):
        """
        Execute the application policy gathering workflow to collect brownfield configurations.

        This method orchestrates the complete brownfield application policy extraction workflow
        by coordinating YAML configuration generation operations based on user-provided
        parameters and filters. It serves as the main execution entry point for the 'gathered'
        state operation.

        Purpose:
            Coordinates the execution of application policy extraction operations to generate
            Ansible-compatible YAML playbook configurations from existing Cisco Catalyst
            Center deployments (brownfield environments).

        Workflow Steps:
            1. Log workflow initiation with timestamp
            2. Validate operation registry and parameters
            3. Iterate through registered operations
            4. Check parameter availability for each operation
            5. Execute operation functions with error handling
            6. Track execution time per operation and total
            7. Aggregate results and operation summaries
            8. Log completion with performance metrics

        Args:
            None

        Returns:
            object: Self instance with updated status after YAML generation.
        """
        self.log(
            "Starting brownfield application policy gathering workflow for state 'gathered' "
            "to extract existing application policies and queuing profiles from Cisco Catalyst "
            "Center and generate Ansible-compatible YAML playbooks",
            "DEBUG"
        )

        # Record workflow start time for performance tracking
        workflow_start_time = time.time()

        self.log(
            "Workflow execution started at timestamp: {0}".format(
                time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(workflow_start_time))
            ),
            "INFO"
        )

        # Define operations registry for this workflow state
        # Each tuple contains: (param_key, operation_name, operation_func)
        operations = [
            ("yaml_config_generator", "YAML Configuration Generator", self.yaml_config_generator)
        ]

        self.log(
            "Registered {0} operation(s) for execution in 'gathered' workflow: {1}".format(
                len(operations),
                [op[1] for op in operations]
            ),
            "DEBUG"
        )

        # Validate operations registry
        if not operations:
            error_msg = (
                "Operations registry is empty for state 'gathered' - no operations to execute"
            )
            self.log(error_msg, "ERROR")
            self.msg = error_msg
            self.status = "failed"
            return self

        # Track operation execution statistics
        operations_attempted = 0
        operations_executed = 0
        operations_skipped = 0
        operations_failed = 0

        # Get configuration from validated_config
        config = self.validated_config[0] if self.validated_config else {}

        self.log(
            "Extracted configuration from validated_config. Config keys: {0}".format(
                list(config.keys()) if config else "None"
            ),
            "DEBUG"
        )

        # Build want dictionary for operation execution
        self.want = {
            "yaml_config_generator": config
        }

        # Execute each operation in sequence
        for operation_index, (param_key, operation_name, operation_func) in enumerate(operations, start=1):
            operations_attempted += 1

            self.log(
                "Processing operation {0}/{1}: '{2}' (checking for parameter key '{3}' "
                "in workflow state)".format(
                    operation_index, len(operations), operation_name, param_key
                ),
                "INFO"
            )

            # Validate operation function is callable
            if not operation_func or not callable(operation_func):
                error_msg = (
                    "Operation {0}/{1} '{2}' has invalid function reference (expected "
                    "callable, got {3}). Skipping operation.".format(
                        operation_index, len(operations), operation_name,
                        type(operation_func).__name__ if operation_func else "None"
                    )
                )
                self.log(error_msg, "ERROR")
                operations_skipped += 1
                continue

            # Check if parameters are available for this operation
            operation_params = self.want.get(param_key)

            if not operation_params:
                self.log(
                    "Operation {0}/{1} '{2}' has no parameters in workflow state "
                    "(parameter key '{3}' not found or empty). Skipping operation.".format(
                        operation_index, len(operations), operation_name, param_key
                    ),
                    "WARNING"
                )
                operations_skipped += 1
                continue

            # Validate operation parameters structure
            if not isinstance(operation_params, dict):
                self.log(
                    "Operation {0}/{1} '{2}' has invalid parameters structure - "
                    "expected dict, got {3}. Skipping operation.".format(
                        operation_index, len(operations), operation_name,
                        type(operation_params).__name__
                    ),
                    "WARNING"
                )
                operations_skipped += 1
                continue

            self.log(
                "Operation {0}/{1} '{2}' parameters found in workflow state with "
                "{3} configuration key(s): {4}. Starting operation execution.".format(
                    operation_index, len(operations), operation_name,
                    len(operation_params), list(operation_params.keys())
                ),
                "INFO"
            )

            # Record operation start time
            operation_start_time = time.time()

            self.log(
                "Executing operation '{0}' with parameters: {1}".format(
                    operation_name, operation_params
                ),
                "DEBUG"
            )

            try:
                # Execute the operation function with parameters
                operation_result = operation_func(operation_params)

                # Validate operation result
                if not operation_result:
                    self.log(
                        "Operation '{0}' completed but returned None result".format(
                            operation_name
                        ),
                        "WARNING"
                    )

                # Check operation status via check_return_status()
                # This will exit module if status is 'failed'
                operation_result.check_return_status()

                # Calculate operation execution time
                operation_end_time = time.time()
                operation_duration = operation_end_time - operation_start_time

                self.log(
                    "Operation {0}/{1} '{2}' completed successfully in {3:.2f} seconds".format(
                        operation_index, len(operations), operation_name, operation_duration
                    ),
                    "INFO"
                )

                operations_executed += 1

            except Exception as e:
                # Calculate operation execution time even on failure
                operation_end_time = time.time()
                operation_duration = operation_end_time - operation_start_time

                error_msg = (
                    "Operation {0}/{1} '{2}' failed after {3:.2f} seconds with error: {4}".format(
                        operation_index, len(operations), operation_name,
                        operation_duration, str(e)
                    )
                )
                self.log(error_msg, "ERROR")

                operations_failed += 1

                # Set failure status and message
                self.msg = (
                    "Workflow execution failed during operation '{0}': {1}".format(
                        operation_name, str(e)
                    )
                )
                self.status = "failed"

                # Exit immediately on operation failure
                # Note: check_return_status() will handle module exit
                return self

        # Calculate total workflow execution time
        workflow_end_time = time.time()
        workflow_duration = workflow_end_time - workflow_start_time

        # Log workflow completion summary
        self.log(
            "Brownfield application policy gathering workflow completed. "
            "Execution summary: attempted={0}, executed={1}, skipped={2}, failed={3}, "
            "total_duration={4:.2f} seconds".format(
                operations_attempted, operations_executed, operations_skipped,
                operations_failed, workflow_duration
            ),
            "INFO"
        )

        # Determine overall workflow success
        if operations_executed == 0:
            self.log(
                "No operations were executed - all operations were skipped or had invalid "
                "configurations. Workflow completed with warnings.",
                "WARNING"
            )
            self.msg = (
                "Workflow completed but no operations were executed. "
                "Verify configuration parameters."
            )
            self.status = "ok"
        elif operations_failed > 0:
            self.log(
                "Workflow completed with {0} operation failure(s)".format(operations_failed),
                "ERROR"
            )
            self.status = "failed"
        else:
            self.log(
                "All {0} operation(s) executed successfully without errors".format(
                    operations_executed
                ),
                "INFO"
            )
            # Note: Individual operation may have already set status to "success"
            # We preserve that status if it was set
            if self.status != "success":
                self.status = "ok"

        self.log(
            "Brownfield application policy gathering workflow execution finished at "
            "timestamp {0}. Total execution time: {1:.2f} seconds. Final status: {2}".format(
                time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(workflow_end_time)),
                workflow_duration,
                self.status
            ),
            "INFO"
        )

        return self


def main():
    """
    Main entry point for the Cisco Catalyst Center brownfield application policy playbook generator module.

    This function serves as the primary execution entry point for the Ansible module,
    orchestrating the complete workflow from parameter collection to YAML playbook
    generation for brownfield application policy extraction.

    Purpose:
        Initializes and executes the brownfield application policy playbook generator
        workflow to extract existing application policy and queuing profile configurations
        from Cisco Catalyst Center and generate Ansible-compatible YAML playbook files.

    Workflow Steps:
        1. Define module argument specification with required parameters
        2. Initialize Ansible module with argument validation
        3. Create ApplicationPolicyPlaybookGenerator instance
        4. Validate Catalyst Center version compatibility (>= 2.3.7.6)
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
        - Minimum Catalyst Center version: 2.3.7.6
        - Introduced APIs for application policy retrieval:
            * Application Policies (get_application_policy)
            * Queuing Profiles (get_application_policy_queuing_profile)

    Supported States:
        - gathered: Extract existing application policies and generate YAML playbook
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
            - msg (str): Operation result message
            - response (dict): Detailed operation results
            - configurations_generated (int): Number of configurations

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

    # Initialize the ApplicationPolicyPlaybookGenerator object
    # This creates the main orchestrator for brownfield application policy extraction
    ccc_app_policy_generator = ApplicationPolicyPlaybookGenerator(module)

    # Log module initialization after object creation (now logging is available)
    ccc_app_policy_generator.log(
        "========== Starting application_policy_playbook_config_generator module ==========",
        "INFO"
    )

    ccc_app_policy_generator.log(
        "Module initialized at timestamp {0} with parameters: dnac_host={1}, "
        "dnac_port={2}, dnac_username={3}, dnac_verify={4}, dnac_version={5}, "
        "state={6}, config_items={7}".format(
            initialization_timestamp,
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
    current_version = ccc_app_policy_generator.get_ccc_version()
    min_supported_version = "2.3.7.6"

    ccc_app_policy_generator.log(
        "Version check: Current Catalyst Center version={0}, Minimum required={1}".format(
            current_version, min_supported_version
        ),
        "INFO"
    )

    if ccc_app_policy_generator.compare_dnac_versions(current_version, min_supported_version) < 0:
        error_msg = (
            "The specified Catalyst Center version '{0}' does not support the YAML "
            "playbook generation for Application Policy module. Supported versions start "
            "from '{1}' onwards. Version '{1}' introduces APIs for retrieving "
            "application policies and queuing profiles from the Catalyst Center.".format(
                current_version, min_supported_version
            )
        )

        ccc_app_policy_generator.log(
            "Version compatibility check failed: {0}".format(error_msg),
            "ERROR"
        )

        ccc_app_policy_generator.msg = error_msg
        ccc_app_policy_generator.set_operation_result(
            "failed", False, ccc_app_policy_generator.msg, "ERROR"
        ).check_return_status()

    ccc_app_policy_generator.log(
        "Version compatibility check passed - Catalyst Center version {0} supports "
        "all required application policy APIs".format(current_version),
        "INFO"
    )

    # ============================================
    # State Parameter Validation
    # ============================================
    state = ccc_app_policy_generator.params.get("state")

    ccc_app_policy_generator.log(
        "Requested state: '{0}'. Validating against supported states: {1}".format(
            state, ccc_app_policy_generator.supported_states
        ),
        "INFO"
    )

    if state not in ccc_app_policy_generator.supported_states:
        error_msg = (
            "State '{0}' is invalid for this module. Supported states are: {1}. "
            "Please update your playbook to use one of the supported states.".format(
                state, ccc_app_policy_generator.supported_states
            )
        )

        ccc_app_policy_generator.log(
            "State validation failed: {0}".format(error_msg),
            "ERROR"
        )

        ccc_app_policy_generator.status = "invalid"
        ccc_app_policy_generator.msg = error_msg
        ccc_app_policy_generator.check_return_status()

    ccc_app_policy_generator.log(
        "State validation passed - using state '{0}' for workflow execution".format(
            state
        ),
        "INFO"
    )

    # ============================================
    # Input Parameter Validation
    # ============================================
    ccc_app_policy_generator.log(
        "Starting input validation for {0} configuration item(s)".format(
            len(ccc_app_policy_generator.config)
        ),
        "INFO"
    )

    ccc_app_policy_generator.validate_input().check_return_status()

    ccc_app_policy_generator.log(
        "Input validation completed successfully for all configuration items",
        "INFO"
    )

    # ============================================
    # Configuration Processing Loop
    # ============================================
    config_list = ccc_app_policy_generator.validated_config

    ccc_app_policy_generator.log(
        "Starting configuration processing for {0} validated configuration item(s)".format(
            len(config_list)
        ),
        "INFO"
    )

    for config_index, config in enumerate(config_list, start=1):
        ccc_app_policy_generator.log(
            "Processing configuration {0}/{1}".format(
                config_index, len(config_list)
            ),
            "INFO"
        )

        # Reset values for clean state between configurations
        ccc_app_policy_generator.log(
            "Resetting module state variables for clean configuration processing",
            "DEBUG"
        )
        ccc_app_policy_generator.reset_values()

        # Collect desired state (want) from configuration
        ccc_app_policy_generator.log(
            "Collecting desired state parameters from configuration item {0}".format(
                config_index
            ),
            "DEBUG"
        )
        ccc_app_policy_generator.get_want(config, state).check_return_status()

        # Execute state-specific operation (gathered workflow)
        ccc_app_policy_generator.log(
            "Executing state-specific operation for '{0}' workflow on "
            "configuration item {1}".format(state, config_index),
            "INFO"
        )
        ccc_app_policy_generator.get_diff_state_apply[state]().check_return_status()

        ccc_app_policy_generator.log(
            "Successfully completed processing for configuration item {0}/{1}".format(
                config_index, len(config_list)
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

    ccc_app_policy_generator.log(
        "========== Module execution completed successfully ==========",
        "INFO"
    )

    ccc_app_policy_generator.log(
        "Module completed at timestamp {0}. Total execution time: {1:.2f} seconds. "
        "Processed {2} configuration item(s) with final status: {3}".format(
            completion_timestamp,
            module_duration,
            len(config_list),
            ccc_app_policy_generator.status
        ),
        "INFO"
    )

    # Exit module with results
    # This is a terminal operation - function does not return after this
    ccc_app_policy_generator.log(
        "Exiting Ansible module with result: {0}".format(
            ccc_app_policy_generator.result
        ),
        "DEBUG"
    )

    module.exit_json(**ccc_app_policy_generator.result)


if __name__ == "__main__":
    main()
