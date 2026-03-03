#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright (c) 2026, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

"""Ansible module to generate YAML configurations for Network Profile Switching Module."""
from __future__ import absolute_import, division, print_function

__metaclass__ = type
__author__ = ("A Mohamed Rafeek, Madhan Sankaranarayanan")
DOCUMENTATION = r"""
---
module: network_profile_switching_playbook_config_generator
short_description: >-
  Generate YAML configurations playbook for
  'network_profile_switching_workflow_manager' module.
description:
  - Generates YAML configurations compatible with the
    'network_profile_switching_workflow_manager' module, reducing
    the effort required to manually create Ansible playbooks and
    enabling programmatic modifications.
  - Supports complete infrastructure discovery by
    collecting all switch profiles from Cisco Catalyst Center.
  - Enables targeted extraction using filters (profile names,
    Day-N templates, or site hierarchies).
  - Auto-generates timestamped YAML filenames when file path not
    specified.
version_added: 6.45.0
extends_documentation_fragment:
  - cisco.dnac.workflow_manager_params
author:
  - A Mohamed Rafeek (@mabdulk2)
  - Madhan Sankaranarayanan (@madhansansel)
options:
  state:
    description: The desired state of Cisco Catalyst Center after module execution.
    type: str
    choices: [gathered]
    default: gathered
  config:
    description:
      - A list of filters for generating YAML playbook compatible
        with the 'network_profile_switching_playbook_config_generator'
        module.
      - Filters specify which components to include in the YAML
        configuration file.
      - Either 'generate_all_configurations' or 'global_filters'
        must be specified to identify target switch profiles.
    type: list
    elements: dict
    required: true
    suboptions:
      generate_all_configurations:
        description:
          - When set to True, automatically generates YAML
            configurations for all switch profiles and all
            supported features.
          - This mode discovers all managed devices in Cisco
            Catalyst Center and extracts all supported
            configurations.
          - When enabled, the config parameter becomes optional
            and will use default values if not provided.
          - A default filename will be generated automatically
            if file_path is not specified.
          - This is useful for complete network profile switching
            and documentation.
          - Any provided global_filters will be IGNORED in this
            mode.
        type: bool
        required: false
        default: false
      file_path:
        description:
          - Path where the YAML configuration file will be saved.
          - If not provided, the file will be saved in the current
            working directory with a default file name
            C(<module_name>playbook_config_<YYYY-MM-DD_HH-MM-SS>.yml).
          - For example,
            'network_profile_switching_playbook_config_2025-11-12_21-43-26.yml'.
          - Supports both absolute and relative file paths.
        type: str
      global_filters:
        description:
          - Global filters to apply when generating the YAML
            configuration file.
          - These filters apply to all components unless overridden
            by component-specific filters.
          - At least one filter type must be specified to identify
            target devices.
          - If multiple filter types are provided, the module will filter
            them in the following order of profile_name_list, day_n_template_list, site_list
          - All profiles matching any of the provided filters will be retrieved.
        type: dict
        required: false
        suboptions:
          profile_name_list:
            description:
              - List of switch profile names to extract
                configurations from.
              - Switch Profile names must match those registered
                in Catalyst Center.
              - Case-sensitive and must be exact matches.
              - Example ["Campus_Switch_Profile",
                "Enterprise_Switch_Profile"]
              - Module will fail if any specified profile does not
                exist in Catalyst Center.
            type: list
            elements: str
            required: false
          day_n_template_list:
            description:
              - List of Day-N templates to filter switch profiles.
              - Retrieves all switch profiles containing any of
                the specified templates.
              - Case-sensitive and must be exact matches.
              - Example ["Periodic_Config_Audit",
                "Security_Compliance_Check"]
              - Requires retrieving all profiles first, then
                filtering based on template assignments.
            type: list
            elements: str
            required: false
          site_list:
            description:
              - List of site hierarchies to filter switch profiles.
              - Retrieves all switch profiles assigned to any of
                the specified sites.
              - Case-sensitive and must be exact matches.
              - Example ["Global/India/Chennai/Main_Office",
                "Global/USA/San_Francisco/Regional_HQ"]
              - Requires retrieving all profiles first, then
                filtering based on site assignments.
            type: list
            elements: str
            required: false
requirements:
  - dnacentersdk >= 2.10.10
  - python >= 3.9
notes:
  - This module utilizes the following SDK methods
    site_design.retrieves_the_list_of_sites_that_the_given_network_profile_for_sites_is_assigned_to_v1
    site_design.retrieves_the_list_of_network_profiles_for_sites_v1
    configuration_templates.gets_the_templates_available_v1
    network_settings.retrieve_cli_templates_attached_to_a_network_profile_v1
  - The following API paths are used
    GET /dna/intent/api/v1/networkProfilesForSites
    GET /dna/intent/api/v1/template-programmer/template
    GET /dna/intent/api/v1/networkProfilesForSites/{profileId}/templates
  - Minimum Cisco Catalyst Center version required is 2.3.7.9 for
    YAML playbook generation support.
  - Filter priority hierarchy ensures only one filter type is
    processed per execution.
  - Module creates YAML file compatible with
    'network_profile_switching_workflow_manager' module for
    automation workflows.
"""

EXAMPLES = r"""
---
- name: Auto-generate YAML Configuration for all Switch Profiles
  cisco.dnac.network_profile_switching_playbook_config_generator:
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

- name: Auto-generate YAML Configuration with custom file path
  cisco.dnac.network_profile_switching_playbook_config_generator:
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
      - file_path: "/tmp/complete_switch_profile_config.yml"
        generate_all_configurations: true

- name: Generate YAML Configuration with default file path for given switch profiles
  cisco.dnac.network_profile_switching_playbook_config_generator:
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
      - global_filters:
          profile_name_list: ["Campus_Switch_Profile", "Enterprise_Switch_Profile"]

- name: Generate YAML Configuration with default file path based on Day-N templates filters
  cisco.dnac.network_profile_switching_playbook_config_generator:
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
      - global_filters:
          day_n_template_list: ["Periodic_Config_Audit", "Security_Compliance_Check"]

- name: Generate YAML Configuration with default file path based on site list filters
  cisco.dnac.network_profile_switching_playbook_config_generator:
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
      - global_filters:
          site_list: ["Global/India/Chennai/Main_Office", "Global/USA/San_Francisco/Regional_HQ"]

- name: Generate YAML Configuration with default file path based on site and Day-N templates list filters
  cisco.dnac.network_profile_switching_playbook_config_generator:
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
      - global_filters:
          site_list: ["Global/India/Chennai/Main_Office", "Global/USA/San_Francisco/Regional_HQ"]
          day_n_template_list: ["Periodic_Config_Audit", "Security_Compliance_Check"]
"""

RETURN = r"""
# Case_1: Success Scenario
response_1:
  description: >-
    A dictionary with the response returned by the Cisco Catalyst
    Center Python SDK
  returned: always
  type: dict
  sample: >
    {
      "response": {
        "YAML config generation Task succeeded for module
         'network_profile_switching_workflow_manager'.": {
            "file_path":
             "tmp/network_profile_switching_workflow_playbook_templatebase.yml"
          }
        },
      "msg": {
        "YAML config generation Task succeeded for module
         'network_profile_switching_workflow_manager'.": {
            "file_path":
             "tmp/network_profile_switching_workflow_playbook_templatebase.yml"
          }
        }
    }

# Case_2: Error Scenario
response_2:
  description: >-
    A string with the response returned by the Cisco Catalyst
    Center Python SDK
  returned: always
  type: dict
  sample: >
    {
      "response": "No configurations or components to process for
                   module 'network_profile_switching_workflow_manager'.
                   Verify input filters or configuration.",
      "msg": "No configurations or components to process for module
              'network_profile_switching_workflow_manager'.
              Verify input filters or configuration."
    }
"""

from ansible.module_utils.basic import AnsibleModule
from ansible_collections.cisco.dnac.plugins.module_utils.brownfield_helper import (
    BrownFieldHelper,
)
from ansible_collections.cisco.dnac.plugins.module_utils.dnac import (
    validate_list_of_dicts,
)
from ansible_collections.cisco.dnac.plugins.module_utils.network_profiles import (
    NetworkProfileFunctions,
)
import time
from collections import OrderedDict

try:
    import yaml
    HAS_YAML = True

    # Only define OrderedDumper if yaml is available
    class OrderedDumper(yaml.Dumper):
        def represent_dict(self, data):
            return self.represent_mapping("tag:yaml.org,2002:map", data.items())

    OrderedDumper.add_representer(OrderedDict, OrderedDumper.represent_dict)
except ImportError:
    HAS_YAML = False
    yaml = None
    OrderedDumper = None


class NetworkProfileSwitchingPlaybookGenerator(NetworkProfileFunctions, BrownFieldHelper):
    """
    A class for generator playbook files for infrastructure deployed within the Cisco Catalyst Center
    using the GET APIs.
    """

    values_to_nullify = ["NOT CONFIGURED"]

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
        self.module_name = "network_profile_switching"
        self.module_schema = self.get_workflow_elements_schema()
        self.log("Initialized NetworkProfileSwitchingPlaybookGenerator class instance.", "DEBUG")
        self.log(self.pprint(self.module_schema), "DEBUG")

        # Initialize generate_all_configurations as class-level parameter
        self.generate_all_configurations = False

    def validate_input(self):
        """
        Validates input configuration parameters for network profile switching playbook generation.

        This function performs comprehensive validation of playbook configuration parameters,
        ensuring that all required fields are present, types are correct, and values conform
        to expected formats before proceeding with YAML generation workflow.

        Args:
            None (uses self.config from class instance)

        Returns:
            object: Self instance with updated attributes:
                - self.validated_config: List of validated configuration dictionaries
                - self.msg: Success or failure message
                - self.status: Validation status ("success" or "failed")
                - Operation result set via set_operation_result()
        """
        self.log(
            "Starting validation of input configuration parameters for network profile "
            "switching playbook generation.",
            "INFO"
        )

        if not self.config:
            self.msg = (
                "Configuration is not available in the playbook for validation. This is "
                "valid for certain workflows that don't require configuration parameters."
            )
            self.log(self.msg, "INFO")
            self.status = "success"
            return self

        if not isinstance(self.config, list):
            self.msg = (
                "Configuration must be a list of dictionaries, got: {0}. Please provide "
                "configuration as a list.".format(type(self.config).__name__)
            )
            self.log(self.msg, "ERROR")
            self.set_operation_result("failed", False, self.msg, "ERROR")
            return self

        self.log(
            "Configuration list provided with {0} item(s) to validate. Starting "
            "per-item validation.".format(len(self.config)),
            "DEBUG"
        )

        # Check if configuration is available
        if not self.config:
            self.status = "success"
            self.msg = "Configuration is not available in the playbook for validation"
            self.log(self.msg, "INFO")
            return self

        # Expected schema for configuration parameters
        # Define expected schema for configuration parameters
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
            "global_filters": {
                "type": "dict",
                "required": False
            },
        }

        allowed_keys = set(temp_spec.keys())
        self.log(
            "Defined validation schema with {0} allowed parameter(s): {1}".format(
                len(allowed_keys), list(allowed_keys)
            ),
            "DEBUG"
        )

        # Validate that only allowed keys are present in each configuration item
        self.log(
            "Starting per-item key validation to check for invalid/unknown parameters.",
            "DEBUG"
        )

        # Validate that only allowed keys are present in the configuration
        for config_index, config_item in enumerate(self.config, start=1):
            self.log(
                "Validating configuration item {0}/{1} for type and allowed keys.".format(
                    config_index, len(self.config)
                ),
                "DEBUG"
            )
            if not isinstance(config_item, dict):
                self.msg = (
                    "Configuration item {0}/{1} must be a dictionary, got: {2}. Each "
                    "configuration entry must be a dictionary with valid parameters.".format(
                        config_index, len(self.config), type(config_item).__name__
                    )
                )
                self.set_operation_result("failed", False, self.msg, "ERROR")
                return self

            self.log(
                "Configuration item {0}/{1} passed key validation. All keys are valid.".format(
                    config_index, len(self.config)
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
            "Completed per-item key validation. All {0} configuration item(s) have valid "
            "parameter keys.".format(len(self.config)),
            "INFO"
        )

        # Validate minimum requirements (generate_all or global_filters)
        self.log(
            "Validating minimum requirements to ensure either generate_all_configurations "
            "or global_filters is provided.",
            "DEBUG"
        )

        try:
            self.validate_minimum_requirement_for_global_filters(self.config)
            self.log(
                "Minimum requirements validation passed. Configuration has either "
                "generate_all_configurations or valid global_filters.",
                "INFO"
            )
        except Exception as e:
            self.msg = (
                "Minimum requirements validation failed: {0}. Please ensure either "
                "generate_all_configurations is true or global_filters is provided with "
                "at least one filter list.".format(str(e))
            )
            self.log(self.msg, "ERROR")
            self.set_operation_result("failed", False, self.msg, "ERROR")
            return self

        # Perform schema-based validation using validate_list_of_dicts
        self.log(
            "Starting schema-based validation using validate_list_of_dicts(). Validating "
            "parameter types, defaults, and required fields against schema: {0}".format(temp_spec),
            "DEBUG"
        )

        # # Import validate_list_of_dicts function here to avoid circular imports
        # from ansible_collections.cisco.dnac.plugins.module_utils.dnac import validate_list_of_dicts

        # Validate params
        valid_temp, invalid_params = validate_list_of_dicts(self.config, temp_spec)
        self.log(
            "Schema validation completed. Valid configurations: {0}, Invalid parameters: {1}".format(
                len(valid_temp) if valid_temp else 0,
                bool(invalid_params)
            ),
            "DEBUG"
        )

        if invalid_params:
            self.msg = (
                "Invalid parameters found during schema validation: {0}. Please check "
                "parameter types and values. Expected types: generate_all_configurations "
                "(bool), file_path (str), global_filters (dict).".format(invalid_params)
            )
            self.set_operation_result("failed", False, self.msg, "ERROR")
            return self

        # Validate global_filters structure if provided
        self.log(
            "Validating global_filters structure for configuration items that include filters.",
            "DEBUG"
        )
        for config_index, config_item in enumerate(valid_temp, start=1):
            global_filters = config_item.get("global_filters")

            if global_filters:
                self.log(
                    "Configuration item {0}/{1} has global_filters. Validating filter structure.".format(
                        config_index, len(valid_temp)
                    ),
                    "DEBUG"
                )

                if not isinstance(global_filters, dict):
                    self.msg = (
                        "global_filters in configuration item {0}/{1} must be a dictionary, "
                        "got: {2}. Please provide global_filters as a dictionary with filter lists.".format(
                            config_index, len(valid_temp), type(global_filters).__name__
                        )
                    )
                    self.log(self.msg, "ERROR")
                    self.set_operation_result("failed", False, self.msg, "ERROR")
                    return self

                # Check that at least one filter list is provided and has values
                valid_filter_keys = ["profile_name_list", "day_n_template_list", "site_list"]
                provided_filters = {
                    key: global_filters.get(key)
                    for key in valid_filter_keys
                    if global_filters.get(key)
                }

                if not provided_filters:
                    self.msg = (
                        "global_filters in configuration item {0}/{1} provided but no valid "
                        "filter lists have values. At least one of the following must be provided: "
                        "{2}. Please add at least one filter list with values.".format(
                            config_index, len(valid_temp), valid_filter_keys
                        )
                    )
                    self.log(self.msg, "ERROR")
                    self.set_operation_result("failed", False, self.msg, "ERROR")
                    return self

                # Validate that filter values are lists
                for filter_key, filter_value in provided_filters.items():
                    if not isinstance(filter_value, list):
                        self.msg = (
                            "global_filters.{0} in configuration item {1}/{2} must be a list, "
                            "got: {3}. Please provide filter as a list of strings.".format(
                                filter_key, config_index, len(valid_temp), type(filter_value).__name__
                            )
                        )
                        self.log(self.msg, "ERROR")
                        self.set_operation_result("failed", False, self.msg, "ERROR")
                        return self

                self.log(
                    "Configuration item {0}/{1} global_filters structure validated successfully. "
                    "Provided filters: {2}".format(
                        config_index, len(valid_temp), list(provided_filters.keys())
                    ),
                    "INFO"
                )
            else:
                self.log(
                    "Configuration item {0}/{1} does not have global_filters. Assuming "
                    "generate_all_configurations mode.".format(config_index, len(valid_temp)),
                    "DEBUG"
                )

        # Set validated configuration and return success
        self.validated_config = valid_temp

        self.msg = (
            "Successfully validated {0} configuration item(s) for network profile switching "
            "playbook generation. Validated configuration: {1}".format(
                len(valid_temp), str(valid_temp)
            )
        )

        self.log(
            "Input validation completed successfully. Total items validated: {0}, "
            "Items with generate_all: {1}, Items with global_filters: {2}".format(
                len(valid_temp),
                sum(1 for item in valid_temp if item.get("generate_all_configurations")),
                sum(1 for item in valid_temp if item.get("global_filters"))
            ),
            "INFO"
        )

        self.set_operation_result("success", False, self.msg, "INFO")
        return self

    def get_workflow_elements_schema(self):
        """
        Retrieves the schema configuration for network profile switching workflow manager components.

        This function defines the complete validation schema for global filters used in network
        profile switching playbook generation, specifying allowed filter types, data structures,
        and validation rules for profile name, day-N template, and site-based filtering.

        Args:
            None (uses self context for potential future expansion)

        Returns:
            dict: Schema configuration dictionary with global_filters structure containing
                validation rules for profile_name_list, day_n_template_list, and site_list
                filter types. All filters optional with list[str] type requirement.
        """
        self.log(
            "Defining validation schema for network profile switching workflow manager. "
            "Schema includes global_filters structure with three filter types: profile_name_list, "
            "day_n_template_list, and site_list.",
            "DEBUG"
        )

        schema = {
            "global_filters": {
                "profile_name_list": {
                    "type": "list",
                    "required": False,
                    "elements": "str"
                },
                "day_n_template_list": {
                    "type": "list",
                    "required": False,
                    "elements": "str"
                },
                "site_list": {
                    "type": "list",
                    "required": False,
                    "elements": "str"
                }
            }
        }

        return schema

    def collect_all_switch_profile_list(self, profile_names=None):
        """
        Collects network switch profile information from Cisco Catalyst Center with
        optional client-side filtering.

        This function retrieves all switching network profiles from Catalyst Center using
        paginated API calls, applies optional name-based filtering to validate profile
        existence, and populates self.have with both profile names and complete profile
        data for downstream processing.

        Args:
            profile_names (list, optional): List of specific switch profile names to filter
                                        and validate. If None or empty, retrieves all
                                        profiles without filtering. Profile names are
                                        case-sensitive and must exactly match Catalyst
                                        Center profile names.
                                        Example: ["Campus_Switch_Profile", "Enterprise"]

        Returns:
            object: Self instance with updated self.have attributes:
                - self.have["switch_profile_names"]: List of profile names (filtered or all)
                - self.have["switch_profile_list"]: List of complete profile dicts from API
        """
        self.log(
            "Starting collection of switch profile information from Cisco Catalyst "
            "Center. Filter parameters - profile_names: {0} (count: {1}, mode: {2}). "
            "This operation will retrieve switching network profiles via paginated "
            "API calls to build complete profile catalog for downstream processing.".format(
                profile_names if profile_names else "None (retrieve all)",
                len(profile_names) if profile_names else 0,
                "filtered" if profile_names else "unfiltered"
            ),
            "INFO"
        )
        self.have["switch_profile_names"], self.have["switch_profile_list"] = [], []
        offset = 1
        limit = 500

        resync_retry_count = int(self.payload.get("dnac_api_task_timeout"))
        resync_retry_interval = int(self.payload.get("dnac_task_poll_interval"))
        self.log(
            "Starting pagination loop for switch profile retrieval from Catalyst Center "
            "API. Loop will continue until all profiles retrieved or timeout exhausted "
            "({0} seconds total). Each iteration retrieves up to {1} profiles and sleeps "
            "{2} seconds to prevent API throttling.".format(
                resync_retry_count, limit, resync_retry_interval
            ),
            "INFO"
        )

        page_number = 1
        total_profiles_collected = 0

        while resync_retry_count > 0:
            self.log(
                "Requesting switch profiles page {0} from Catalyst Center API. "
                "API call parameters - profile_type: 'Switching', offset: {1} "
                "(starting index), limit: {2} (max profiles per page), remaining "
                "timeout: {3} seconds. This request targets switching network profiles "
                "for playbook config generation.".format(
                    page_number, offset, limit, resync_retry_count
                ),
                "DEBUG"
            )
            profiles = self.get_network_profile("Switching", offset, limit)
            if not profiles:
                self.log(
                    "No profile data received from Catalyst Center API for page {0} "
                    "(offset={1}). API returned None or empty list. This indicates either "
                    "end of available data or potential API connectivity issue. Exiting "
                    "pagination loop to prevent unnecessary API calls.".format(
                        page_number, offset
                    ),
                    "DEBUG"
                )
                break

            # Calculate and log page statistics
            page_profile_count = len(profiles)
            total_profiles_collected += page_profile_count

            self.log(
                "Successfully retrieved {0} switch profile(s) from Catalyst Center API "
                "for page {1} (offset={2}). Cumulative profiles collected across all "
                "pages: {3}. API response contains valid profile data with IDs, names, "
                "and metadata required for filtering and configuration generation.".format(
                    page_profile_count, page_number, offset, total_profiles_collected
                ),
                "DEBUG"
            )
            self.have["switch_profile_list"].extend(profiles)
            self.log(
                "Appended {0} profile(s) to switch_profile_list collection. Current "
                "total profiles in collection: {1}. Profiles include complete metadata "
                "(id, name, description, templates, sites) for downstream processing "
                "by template and site collection functions.".format(
                    page_profile_count, len(self.have["switch_profile_list"])
                ),
                "DEBUG"
            )

            # Check for last page by comparing received count to limit
            if page_profile_count < limit:
                self.log(
                    "Received profile count ({0}) is less than configured page size limit "
                    "({1}). This indicates the last page of switch profile results has "
                    "been retrieved. No additional profiles available in Catalyst Center. "
                    "Exiting pagination loop to complete collection operation.".format(
                        page_profile_count, limit
                    ),
                    "DEBUG"
                )
                break

            offset += limit  # Increment offset for pagination
            page_number += 1

            self.log(
                "Incrementing pagination offset to {0} for next API request (page {1}). "
                "Next API call will retrieve profiles starting from index {0}, continuing "
                "sequential collection of switch profile catalog from Catalyst Center.".format(
                    offset, page_number
                ),
                "DEBUG"
            )

            # Rate limiting sleep to prevent API throttling
            self.log(
                "Pausing execution for {0} second(s) before next API request to prevent "
                "API rate limiting and throttling by Catalyst Center. This delay ensures "
                "stable API performance and prevents HTTP 429 (Too Many Requests) errors "
                "during large profile catalog retrieval.".format(resync_retry_interval),
                "INFO"
            )
            time.sleep(resync_retry_interval)
            resync_retry_count = resync_retry_count - resync_retry_interval
            self.log(
                "Decremented retry timeout counter after sleep interval. Remaining "
                "timeout: {0} seconds, next timeout check in: {1} seconds. Pagination "
                "loop will exit if timeout exhausted before all profiles retrieved.".format(
                    resync_retry_count, resync_retry_interval
                ),
                "DEBUG"
            )

        if not self.have["switch_profile_list"]:
            self.log(
                "No switch profile(s) found in Cisco Catalyst Center after pagination "
                "loop completion. The switch_profile_list collection is empty. This "
                "indicates either no switching network profiles are configured in "
                "Catalyst Center, or API permissions may be insufficient to retrieve "
                "profiles. Verify switching profiles exist in Catalyst Center before "
                "running playbook generation.",
                "WARNING"
            )
            self.log(
                "Completed switch profile collection operation with empty results. "
                "Final statistics - Profile names count: 0, Full profile list count: 0, "
                "Mode: {0}. No profiles available for filtering or configuration "
                "generation.".format("filtered" if profile_names else "unfiltered"),
                "INFO"
            )
            return self

        self.log(
            "Profile collection from Catalyst Center API completed successfully. "
            "Total switch profiles retrieved: {0} across {1} page(s) of API responses. "
            "Profile list contains complete metadata (id, name, description, templates, "
            "sites) for all switching network profiles configured in Catalyst Center.".format(
                len(self.have["switch_profile_list"]), page_number
            ),
            "INFO"
        )

        self.log(
            "Complete switch profile list structure retrieved from API: {0}".format(
                self.pprint(self.have["switch_profile_list"])
            ),
            "DEBUG"
        )

        if not profile_names:
            # No filtering requested - use all retrieved profile names
            self.have["switch_profile_names"] = [
                profile["name"] for profile in self.have["switch_profile_list"]
            ]

            self.log(
                "No profile name filtering specified in request parameters. Using all "
                "{0} retrieved switch profile(s) from Catalyst Center for downstream "
                "processing. Profile names extracted from complete profile catalog: {1}. "
                "All profiles will be processed for template and site detail collection.".format(
                    len(self.have["switch_profile_names"]),
                    self.have["switch_profile_names"]
                ),
                "INFO"
            )
            return self

        # Filter profiles based on provided profile names
        self.log(
            "Applying client-side filtering to collected switch profiles based on "
            "provided profile_names parameter. Filter contains {0} profile name(s): "
            "{1}. Validation will check that all requested profiles exist in "
            "Catalyst Center profile catalog (exact case-sensitive match required).".format(
                len(profile_names), profile_names), "INFO")

        filtered_profiles = []
        non_existing_profiles = []
        # Iterate through requested profile names with progress tracking
        for profile_index, profile in enumerate(profile_names, start=1):
            self.log(
                "Validating requested profile {0}/{1}: '{2}'. Checking existence in "
                "retrieved profile catalog from Catalyst Center (total {3} profiles "
                "available). Using exact case-sensitive name matching for validation.".format(
                    profile_index, len(profile_names), profile,
                    len(self.have["switch_profile_list"])
                ),
                "DEBUG"
            )

            if self.value_exists(self.have["switch_profile_list"], "name", profile):
                filtered_profiles.append(profile)
                self.log(
                    "Requested profile {0}/{1} '{2}' found in Catalyst Center profile "
                    "catalog. Added to filtered profile list for downstream processing. "
                    "Filtered profile count: {3}/{4} requested profiles validated.".format(
                        profile_index, len(profile_names), profile,
                        len(filtered_profiles), len(profile_names)
                    ),
                    "DEBUG"
                )
            else:
                non_existing_profiles.append(profile)
                self.log(
                    "Requested profile {0}/{1} '{2}' NOT found in Catalyst Center "
                    "profile catalog. This profile either does not exist or profile "
                    "name is incorrect (case-sensitive match required). Added to "
                    "missing profile list for error reporting.".format(
                        profile_index, len(profile_names), profile
                    ),
                    "WARNING"
                )

        if non_existing_profiles:
            self.log(
                "Profile validation failed. The following {0} switch profile(s) do "
                "not exist in Cisco Catalyst Center catalog: {1}. All requested "
                "profiles must exist for operation to proceed. Please verify profile "
                "names are spelled correctly (case-sensitive) and profiles are "
                "properly configured in Catalyst Center before retrying playbook "
                "generation.".format(
                    len(non_existing_profiles), non_existing_profiles
                ),
                "ERROR"
            )
            not_exist_profile = ", ".join(non_existing_profiles)
            self.msg = (
                "Switch profile(s) '{0}' do not exist in Cisco Catalyst Center. "
                "Total missing profiles: {1}/{2} requested. Please verify profile "
                "names are spelled correctly (case-sensitive exact match required) "
                "and profiles are properly configured in Catalyst Center Network "
                "Profiles section before retrying playbook generation.".format(
                    not_exist_profile,
                    len(non_existing_profiles),
                    len(profile_names)
                )
            )

        if filtered_profiles:
            self.log(
                f"Filtered existing switch profile(s): {filtered_profiles}.",
                "DEBUG",
            )
            self.have["switch_profile_names"] = filtered_profiles
            self.log(
                "Client-side filtering completed successfully. Filtered {0} existing "
                "switch profile(s) from {1} total profiles retrieved from Catalyst "
                "Center. Filtered profile names: {2}. All requested profiles "
                "validated and confirmed to exist in Catalyst Center catalog.".format(
                    len(filtered_profiles),
                    len(self.have["switch_profile_list"]),
                    filtered_profiles
                ),
                "INFO"
            )

        self.log(
            "Completed switch profile collection operation successfully. Final results - "
            "Profile names count: {0}, Full profile list count: {1}, Processing mode: "
            "{2}. Profile data populated in self.have for downstream template and site "
            "collection operations.".format(
                len(self.have.get("switch_profile_names", [])),
                len(self.have.get("switch_profile_list", [])),
                "filtered" if profile_names else "unfiltered"
            ),
            "INFO"
        )

        return self

    def collect_site_and_template_details(self, profile_names):
        """
        Collects Day-N template and site assignment details for specified switch profiles.

        This function retrieves comprehensive metadata for each switch profile including
        associated CLI templates (Day-N templates) and assigned site hierarchies from
        Cisco Catalyst Center, populating self.have with complete profile configuration
        details required for YAML playbook generation.

        Args:
            profile_names (list): List of switch profile names to collect details for.
                                Must be profile names that exist in Catalyst Center
                                (validated by collect_all_switch_profile_list).
                                Case-sensitive exact matches required.
                                Example: ["Campus_Switch_Profile", "Enterprise_Profile"]

        Returns:
            object: Self instance with updated self.have attributes:
                - self.have["switch_profile_templates"]: Dict mapping profile_id -> template_names
                - self.have["switch_profile_sites"]: Dict mapping profile_id -> site_mapping
        """
        self.log(
            "Collecting Day-N template and site assignment details for switch profiles "
            "from Cisco Catalyst Center. Profile names provided: {0} (count: {1}). This "
            "operation will retrieve CLI templates and assigned site hierarchies for each "
            "profile to populate complete configuration metadata for YAML generation.".format(
                profile_names, len(profile_names) if profile_names else 0
            ),
            "INFO"
        )

        if not profile_names or not isinstance(profile_names, list):
            self.log(
                "No valid profile names provided for template and site collection. "
                "profile_names is None or not a list. Skipping collection operation.",
                "WARNING"
            )
            return self

        # Initialize counters for statistics
        profiles_processed = 0
        profiles_skipped = 0
        total_templates_collected = 0
        total_sites_collected = 0

        # Iterate through each profile name with progress tracking
        for profile_index, each_profile in enumerate(profile_names, start=1):
            self.log(
                "Processing switch profile {0}/{1}: '{2}'. Retrieving profile UUID from "
                "previously collected profile catalog (switch_profile_list) to enable "
                "template and site API queries.".format(
                    profile_index, len(profile_names), each_profile
                ),
                "DEBUG"
            )
            profile_id = self.get_value_by_key(
                self.have["switch_profile_list"],
                "name",
                each_profile,
                "id",
            )
            if not profile_id:
                self.log(
                    "Profile UUID not found for switch profile {0}/{1}: '{2}'. This profile "
                    "exists in the filter list but has no ID mapping in the retrieved profile "
                    "catalog from Catalyst Center. This may indicate profile was deleted or "
                    "renamed after initial catalog retrieval. Skipping template and site "
                    "detail collection for this profile.".format(
                        profile_index, len(profile_names), each_profile
                    ),
                    "WARNING"
                )
                profiles_skipped += 1
                continue

            self.log(
                "Successfully retrieved profile UUID '{0}' for profile {1}/{2}: '{3}'. "
                "Proceeding with template and site metadata collection.".format(
                    profile_id, profile_index, len(profile_names), each_profile
                ),
                "DEBUG"
            )

            # Retrieve Day-N CLI templates for the profile
            self.log(
                "Retrieving Day-N CLI templates for switch profile {0}/{1}: '{2}' "
                "(UUID: {3}). Querying Catalyst Center API for CLI templates assigned "
                "to this network profile for Day-N configuration automation.".format(
                    profile_index, len(profile_names), each_profile, profile_id
                ),
                "DEBUG"
            )

            templates = self.get_templates_for_profile(profile_id)
            if templates and isinstance(templates, list):
                template_names = [template.get("name") for template in templates if template.get("name")]

                if template_names:
                    self.have.setdefault("switch_profile_templates", {})[profile_id] = template_names
                    total_templates_collected += len(template_names)

                    self.log(
                        "Successfully retrieved {0} Day-N CLI template(s) for switch profile "
                        "{1}/{2}: '{3}'. Template names: {4}. Templates stored in "
                        "switch_profile_templates mapping for YAML generation.".format(
                            len(template_names), profile_index, len(profile_names),
                            each_profile, template_names
                        ),
                        "DEBUG"
                    )
                else:
                    self.log(
                        "Day-N template API returned data for profile {0}/{1}: '{2}', but no "
                        "valid template names found after extraction. Template dicts may be "
                        "missing 'name' field. No templates stored for this profile.".format(
                            profile_index, len(profile_names), each_profile
                        ),
                        "WARNING"
                    )
            else:
                self.log(
                    "No Day-N CLI templates found for switch profile {0}/{1}: '{2}'. The "
                    "profile has no associated CLI templates configured in Catalyst Center "
                    "for Day-N automation. This is not an error - profiles without templates "
                    "are valid and will be processed without template assignments.".format(
                        profile_index, len(profile_names), each_profile
                    ),
                    "WARNING"
                )

            # Retrieve assigned site list for the profile
            self.log(
                "Retrieving assigned site hierarchies for switch profile {0}/{1}: '{2}' "
                "(UUID: {3}). Querying Catalyst Center API for sites where this network "
                "profile is currently assigned for device provisioning.".format(
                    profile_index, len(profile_names), each_profile, profile_id
                ),
                "DEBUG"
            )
            site_list = self.get_site_lists_for_profile(
                each_profile, profile_id)
            # Process site data if available
            if site_list and isinstance(site_list, list):
                self.log(
                    "Received {0} assigned site(s) from Catalyst Center API for switch "
                    "profile {1}/{2}: '{3}'. Processing site IDs to convert to hierarchical "
                    "site names (Global/Region/Building format) for human-readable YAML.".format(
                        len(site_list), profile_index, len(profile_names), each_profile
                    ),
                    "DEBUG"
                )

                # Extract site IDs from site dictionaries
                site_id_list = [site.get("id") for site in site_list if site.get("id")]

                if site_id_list:
                    # Convert site IDs to hierarchical site names
                    site_id_name_mapping = self.get_site_id_name_mapping(site_id_list)

                    if site_id_name_mapping and isinstance(site_id_name_mapping, dict):
                        self.have.setdefault("switch_profile_sites", {})[profile_id] = site_id_name_mapping
                        total_sites_collected += len(site_id_name_mapping)

                        self.log(
                            "Successfully converted {0} site UUID(s) to hierarchical site names "
                            "for switch profile {1}/{2}: '{3}'. Site name mapping: {4}. Site "
                            "data stored in switch_profile_sites for YAML generation.".format(
                                len(site_id_name_mapping), profile_index, len(profile_names),
                                each_profile, site_id_name_mapping
                            ),
                            "DEBUG"
                        )
                    else:
                        self.log(
                            "Site ID to name mapping conversion failed or returned empty result "
                            "for profile {0}/{1}: '{2}'. get_site_id_name_mapping() returned "
                            "invalid data. No site names stored for this profile.".format(
                                profile_index, len(profile_names), each_profile
                            ),
                            "WARNING"
                        )
                else:
                    self.log(
                        "Site list API returned data for profile {0}/{1}: '{2}', but no valid "
                        "site IDs found after extraction. Site dicts may be missing 'id' field. "
                        "No sites stored for this profile.".format(
                            profile_index, len(profile_names), each_profile
                        ),
                        "WARNING"
                    )
            else:
                self.log(
                    "No assigned sites found for switch profile {0}/{1}: '{2}'. The profile "
                    "is not currently associated with any sites in Catalyst Center site "
                    "hierarchy. This is not an error - profiles can exist without site "
                    "assignments and will be processed without site associations.".format(
                        profile_index, len(profile_names), each_profile
                    ),
                    "WARNING"
                )

            # Increment processed counter
            profiles_processed += 1

        self.log(
            "Completed Day-N template and site assignment detail collection for switch "
            "profiles. Operation statistics - Total profiles requested: {0}, Profiles "
            "processed successfully: {1}, Profiles skipped (no UUID): {2}, Total templates "
            "collected: {3}, Total sites collected: {4}. Metadata populated in self.have "
            "for downstream YAML generation and filtering operations.".format(
                len(profile_names), profiles_processed, profiles_skipped,
                total_templates_collected, total_sites_collected
            ),
            "INFO"
        )

        return self

    def process_global_filters(self, global_filters):
        """
        Processes global filters to extract and organize switch profile configurations.

        This function applies hierarchical filtering logic to switch profiles based on
        profile names, Day-N templates, or site assignments, extracting complete profile
        metadata including CLI templates and site hierarchies for YAML playbook generation.

        Args:
            global_filters (dict): Dictionary containing filter parameters with keys:
                                - profile_name_list: List of profile names (optional)
                                - day_n_template_list: List of template names (optional)
                                - site_list: List of site hierarchical paths (optional)
                                At least one filter type should be provided.
                                Example: {
                                    "profile_name_list": ["Campus_Profile"],
                                    "day_n_template_list": ["Config_Template"],
                                    "site_list": ["Global/USA/San_Jose"]
                                }

        Returns:
            list or None: List of profile configuration dictionaries if matches found.
                        Each dict contains profile_name, day_n_templates (optional),
                        and site_names (optional).
                        Returns None if no profiles match the provided filters.
        """
        self.log(
            "Processing global filters to extract and organize switch profile configurations "
            "for YAML generation. Filters provided: {0}. Filter processing follows hierarchical "
            "priority: profile_name_list (highest) > day_n_template_list > site_list (lowest). "
            "Only one filter type will be processed based on priority order.".format(
                global_filters
            ),
            "INFO"
        )

        if not global_filters or not isinstance(global_filters, dict):
            self.log(
                "No valid global filters provided for profile processing. global_filters is "
                "None or not a dictionary. Cannot process profiles without filter criteria. "
                "Please provide at least one filter type (profile_name_list, day_n_template_list, "
                "or site_list) to extract profile configurations.",
                "WARNING"
            )
            return None

        profile_names = global_filters.get("profile_name_list")
        day_n_templates = global_filters.get("day_n_template_list")
        site_list = global_filters.get("site_list")
        final_list = []

        self.log(
            "Extracted filter parameters from global_filters. profile_name_list: {0} "
            "(type: {1}), day_n_template_list: {2} (type: {3}), site_list: {4} (type: {5}). "
            "Validating filter types and determining processing priority.".format(
                profile_names, type(profile_names).__name__,
                day_n_templates, type(day_n_templates).__name__,
                site_list, type(site_list).__name__
            ),
            "DEBUG"
        )

        if profile_names and isinstance(profile_names, list):
            self.log(
                "Filtering switch profiles based on profile_name_list (HIGHEST PRIORITY). "
                "Requested profile names: {0} (count: {1}). Processing each profile from "
                "validated switch_profile_names list to extract CLI templates and site "
                "assignments.".format(profile_names, len(profile_names)),
                "INFO"
            )

            profile_count = 0
            profiles_with_templates = 0
            profiles_with_sites = 0

            for profile_index, profile in enumerate(self.have.get("switch_profile_names", []), start=1):
                self.log(
                    "Processing switch profile {0}/{1}: '{2}' from profile_name_list filter. "
                    "Retrieving profile UUID to lookup templates and sites from collected "
                    "metadata.".format(
                        profile_index, len(self.have.get("switch_profile_names", [])), profile
                    ),
                    "DEBUG"
                )
                each_profile_config = {}
                each_profile_config["profile_name"] = profile

                if profile not in profile_names:
                    self.log(
                        "Profile {0}/{1}: '{2}' is in switch_profile_names but not in "
                        "requested profile_name_list filter. This should not happen as "
                        "validation should have filtered only requested profiles. Skipping "
                        "this profile due to mismatch.".format(
                            profile_index, len(self.have.get("switch_profile_names", [])), profile
                        ),
                        "WARNING"
                    )
                    continue

                profile_id = self.get_value_by_key(
                    self.have["switch_profile_list"],
                    "name",
                    profile,
                    "id",
                )

                if not profile_id:
                    self.log(
                        "Profile UUID not found for switch profile {0}/{1}: '{2}'. Profile exists "
                        "in validated names list but has no ID mapping in profile catalog. "
                        "Skipping template and site extraction for this profile.".format(
                            profile_index, len(self.have.get("switch_profile_names", [])), profile
                        ),
                        "WARNING"
                    )
                    continue

                self.log(
                    "Retrieved profile UUID '{0}' for profile {1}/{2}: '{3}'. Extracting "
                    "CLI templates and site assignments from collected metadata.".format(
                        profile_id, profile_index,
                        len(self.have.get("switch_profile_names", [])), profile
                    ),
                    "DEBUG"
                )

                cli_template_details = self.have.get(
                    "switch_profile_templates", {}).get(profile_id)
                if cli_template_details and isinstance(cli_template_details, list):
                    each_profile_config["day_n_templates"] = cli_template_details
                    profiles_with_templates += 1
                    self.log(
                        "Extracted {0} CLI template(s) for profile {1}/{2}: '{3}'. Template "
                        "names: {4}. Added to day_n_templates field.".format(
                            len(cli_template_details), profile_index,
                            len(self.have.get("switch_profile_names", [])), profile,
                            cli_template_details
                        ),
                        "DEBUG"
                    )
                else:
                    self.log(
                        "No CLI templates found for profile {0}/{1}: '{2}'. Profile has no "
                        "template assignments or templates data is invalid. Omitting "
                        "day_n_templates field from configuration.".format(
                            profile_index, len(self.have.get("switch_profile_names", [])), profile
                        ),
                        "DEBUG"
                    )

                site_details = self.have.get(
                    "switch_profile_sites", {}).get(profile_id)
                if site_details and isinstance(site_details, dict):
                    each_profile_config["site_names"] = list(site_details.values())
                    profiles_with_sites += 1
                    self.log(
                        "Extracted {0} site assignment(s) for profile {1}/{2}: '{3}'. "
                        "Hierarchical site names: {4}. Added to site_names field.".format(
                            len(site_details), profile_index,
                            len(self.have.get("switch_profile_names", [])), profile,
                            list(site_details.values())
                        ),
                        "DEBUG"
                    )
                else:
                    self.log(
                        "No site assignments found for profile {0}/{1}: '{2}'. Profile has "
                        "no site associations or sites data is invalid. Omitting site_names "
                        "field from configuration.".format(
                            profile_index, len(self.have.get("switch_profile_names", [])), profile
                        ),
                        "DEBUG"
                    )

                final_list.append(each_profile_config)
                profile_count += 1

            self.log(
                "Completed profile_name_list filtering. Profile configurations collected: {0}. "
                "Statistics - Total profiles processed: {1}, Profiles with templates: {2}, "
                "Profiles with sites: {3}. Configuration structure: {4}".format(
                    len(final_list), profile_count, profiles_with_templates,
                    profiles_with_sites, final_list
                ),
                "INFO"
            )

        if day_n_templates and isinstance(day_n_templates, list):
            self.log(
                "Filtering switch profiles based on day_n_template_list (MEDIUM PRIORITY, "
                "profile_name_list not provided). Requested template names: {0} (count: {1}). "
                "Matching profiles that contain ANY of the specified CLI templates.".format(
                    day_n_templates, len(day_n_templates)
                ),
                "INFO"
            )

            total_templates_checked = 0
            matched_templates = 0
            unmatched_templates = []

            for template_index, template in enumerate(day_n_templates, start=1):
                self.log(
                    "Processing requested template {0}/{1}: '{2}' for profile matching. "
                    "Iterating through profiles to find matches based on template assignments.".format(
                        template_index, len(day_n_templates), template
                    ),
                    "DEBUG"
                )
                total_templates_checked += 1
                matched_profiles = 0

                for profile_index, (profile_id, templates) in enumerate(
                    self.have.get("switch_profile_templates", {}).items(), start=1
                ):
                    self.log(
                        "Checking profile {0}/{1} (UUID: {2}) for template matches. Profile has "
                        "{3} template(s): {4}. Matching against requested templates: {5}".format(
                            profile_index, len(self.have.get("switch_profile_templates", {})),
                            profile_id, len(templates), templates, day_n_templates
                        ),
                        "DEBUG"
                    )
                    if template not in templates:
                        self.log(
                            "Profile {0}/{1} (UUID: {2}) did NOT match. None of the requested "
                            "templates found in profile's template list. Skipping profile.".format(
                                profile_index, len(self.have.get("switch_profile_templates", {})),
                                profile_id
                            ),
                            "DEBUG"
                        )
                        continue

                    self.log(
                        "Template {0}/{1} (Template: {2}) matched! Found. "
                        "Extracting complete profile metadata.".format(
                            template_index, len(day_n_templates), template
                        ),
                        "DEBUG"
                    )
                    profile_name = self.get_value_by_key(
                        self.have["switch_profile_list"],
                        "id",
                        profile_id,
                        "name",
                    )
                    if not profile_name:
                        self.log(
                            "Profile name not found for matched profile UUID: {0}. Skipping "
                            "this profile due to missing name mapping.".format(profile_id),
                            "WARNING"
                        )
                        continue

                    matched_profiles += 1
                    each_profile_config = {}
                    each_profile_config["profile_name"] = profile_name
                    each_profile_config["day_n_templates"] = templates
                    self.log(
                        "Retrieved profile name '{0}' for matched profile. Included {1} "
                        "template(s): {2}. Extracting site assignments.".format(
                            profile_name, len(templates), templates
                        ),
                        "DEBUG"
                    )

                    site_details = self.have.get(
                        "switch_profile_sites", {}).get(profile_id)
                    if site_details and isinstance(site_details, dict):
                        each_profile_config["site_names"] = list(site_details.values())
                        self.log(
                            "Extracted {0} site(s) for profile '{1}': {2}".format(
                                len(site_details), profile_name, list(site_details.values())
                            ),
                            "DEBUG"
                        )
                    else:
                        each_profile_config["site_names"] = []
                        self.log(
                            "No site assignments found for profile '{0}'. Setting site_names "
                            "to empty list.".format(profile_name),
                            "DEBUG"
                        )
                    final_list.append(each_profile_config)

                if matched_profiles == 0:
                    self.msg = (
                        f"No profiles matched the requested template {template_index}/"
                        f"{len(day_n_templates)}: '{template}'. "
                        "No profiles contain this template assignment.")
                    self.log(self.msg, "WARNING")
                    unmatched_templates.append(template)
                else:
                    self.log(
                        f"Template {template_index}/{len(day_n_templates)}: '{template}' matched "
                        f"with {matched_profiles} profile(s).",
                        "INFO")
                    matched_templates += 1

            if unmatched_templates:
                self.msg = (
                    f"The following {len(unmatched_templates)} requested template(s) did not match "
                    f"any profiles: {unmatched_templates}. Please verify that these templates are "
                    "correctly assigned to profiles in Catalyst Center or adjust filter criteria."
                )
                self.log(self.msg, "WARNING")

            unique_data = {d["profile_name"]: d for d in final_list}.values()
            final_list = list(unique_data)

            self.log(
                "Completed day_n_template_list filtering. Profile configurations collected: {0}. "
                "Statistics - Total profiles checked: {1}, Profiles matched: {2}. "
                "Configuration structure: {3}".format(
                    len(final_list), total_templates_checked, matched_templates, final_list
                ),
                "INFO"
            )

        if site_list and isinstance(site_list, list):
            self.log(
                "Filtering switch profiles based on site_list (LOWEST PRIORITY, neither "
                "profile_name_list nor day_n_template_list provided). Requested site paths: {0} "
                "(count: {1}). Matching profiles assigned to ANY of the specified sites.".format(
                    site_list, len(site_list)
                ),
                "INFO"
            )

            total_sites_checked = 0
            matched_sites = 0
            unmatched_sites = []

            for site_index, site in enumerate(site_list, start=1):
                self.log(
                    "Processing requested site {0}/{1}: '{2}' for profile matching. Iterating "
                    "through profiles to find matches based on site assignments.".format(
                        site_index, len(site_list), site
                    ),
                    "DEBUG"
                )
                total_sites_checked += 1
                matched_profiles = 0

                for profile_index, (profile_id, sites) in enumerate(
                    self.have.get("switch_profile_sites", {}).items(), start=1
                ):
                    self.log(
                        "Checking profile {0}/{1} (UUID: {2}) for site matches. Profile has {3} "
                        "site(s): {4}. Matching against requested sites: {5}".format(
                            profile_index, len(self.have.get("switch_profile_sites", {})),
                            profile_id, len(sites), list(sites.values()), site_list
                        ),
                        "DEBUG"
                    )

                    if site not in sites.values():
                        self.log(
                            "Profile {0}/{1} (Site Name: {2}) did NOT match. None of the requested sites "
                            "found in profile's site assignment list. Skipping profile.".format(
                                profile_index, len(self.have.get("switch_profile_sites", {})),
                                site
                            ),
                            "DEBUG"
                        )
                        continue

                    self.log(
                        f"Site {site_index}/{len(site_list)} (Site Name: {site}) matched! Found "
                        "site assignment. Extracting complete profile metadata.".format(
                            site_index, len(site_list), site
                        ),
                        "DEBUG"
                    )
                    profile_name = self.get_value_by_key(
                        self.have["switch_profile_list"],
                        "id",
                        profile_id,
                        "name",
                    )
                    if not profile_name:
                        self.log(
                            "Profile name not found for matched profile UUID: {0}. Skipping "
                            "this profile due to missing name mapping.".format(profile_id),
                            "WARNING"
                        )
                        continue

                    matched_profiles += 1
                    each_profile_config = {}
                    each_profile_config["profile_name"] = profile_name
                    self.log(
                        "Retrieved profile name '{0}' for matched profile. Included {1} "
                        "site(s): {2}. Extracting CLI templates.".format(
                            profile_name, len(sites), list(sites.values())
                        ),
                        "DEBUG"
                    )

                    cli_template_details = self.have.get(
                        "switch_profile_templates", {}).get(profile_id)
                    if cli_template_details and isinstance(cli_template_details, list):
                        each_profile_config["day_n_templates"] = cli_template_details
                        self.log(
                            "Extracted {0} CLI template(s) for profile '{1}': {2}".format(
                                len(cli_template_details), profile_name, cli_template_details
                            ),
                            "DEBUG"
                        )
                    else:
                        each_profile_config["day_n_templates"] = []
                        self.log(
                            "No CLI templates found for profile '{0}'. Setting day_n_templates "
                            "to empty list.".format(profile_name),
                            "DEBUG"
                        )

                    each_profile_config["site_names"] = list(sites.values())
                    final_list.append(each_profile_config)

                if matched_profiles == 0:
                    self.msg = (
                        f"No profiles matched the requested site {site_index}/"
                        f"{len(site_list)}: '{site}'. "
                        "No profiles contain this site assignment.")
                    self.log(self.msg, "WARNING")
                    unmatched_sites.append(site)
                else:
                    matched_sites += 1
                    self.log(
                        f"Site {site_index}/{len(site_list)}: '{site}' matched "
                        f"with {matched_profiles} profile(s).",
                        "INFO")

            if unmatched_sites:
                self.msg = (
                    f"The following {len(unmatched_sites)} requested site(s) did not match "
                    f"any profiles: {unmatched_sites}. Please verify that these sites are "
                    "correctly assigned to profiles in Catalyst Center or adjust filter criteria."
                )
                self.log(self.msg, "WARNING")

            unique_data = {d["profile_name"]: d for d in final_list}.values()
            final_list = list(unique_data)

            self.log(
                "Completed site_list filtering. Profile configurations collected: {0}. "
                "Statistics - Total profiles checked: {1}, Sites matched: {2}. "
                "Configuration structure: {3}".format(
                    len(final_list), total_sites_checked, matched_sites, final_list
                ),
                "INFO"
            )
        else:
            self.log(
                "No valid global filters provided for profile processing. None of the filter "
                "types (profile_name_list, day_n_template_list, site_list) are valid lists. "
                "Filter values - profile_name_list: {0}, day_n_template_list: {1}, site_list: {2}. "
                "Cannot extract profile configurations without valid filter criteria.".format(
                    profile_names, day_n_templates, site_list
                ),
                "WARNING"
            )

        if not final_list:
            self.log(
                "No switch profiles matched the provided global filters after processing. "
                "Filter criteria may be too restrictive or no profiles exist with the "
                "specified attributes. Final result is empty. Returning None to indicate "
                "no matching configurations found.",
                "WARNING"
            )
            return None

        self.log(
            "Global filter processing completed successfully. Total profile configurations "
            "extracted: {0}. Each configuration contains profile_name with optional "
            "day_n_templates and site_names fields. Result ready for YAML generation workflow.".format(
                len(final_list)
            ),
            "INFO"
        )

        return final_list

    def yaml_config_generator(self, yaml_config_generator):
        """
        Generates YAML configuration file for network switch profiles with applied filters.

        This function processes switch profile configurations from Cisco Catalyst Center,
        applies global filtering criteria, and exports the structured data to a YAML file
        compatible with the network_profile_switching_workflow_manager module for automation.

        Args:
            yaml_config_generator (dict): Configuration parameters containing:
                                        - file_path: Output file path (optional, str)
                                        - generate_all_configurations: Mode flag (optional, bool)
                                        - global_filters: Filter criteria (optional, dict)
                                        Example: {
                                        "file_path": "/tmp/config.yml",
                                        "generate_all_configurations": False,
                                        "global_filters": {
                                            "profile_name_list": ["Campus_Profile"]
                                        }
                                        }

        Returns:
            object: Self instance with updated attributes:
                - self.msg: Operation result message with file_path
                - self.status: Operation status ("success" or "failed")
                - self.result: Complete operation result dictionary
        """

        self.log(
            "Starting YAML configuration file generation for network switch profiles. "
            "Input parameters: {0}. This operation will process switch profile configurations "
            "from Catalyst Center, apply filtering criteria, and export structured data to "
            "YAML file compatible with network_profile_switching_workflow_manager module.".format(
                yaml_config_generator
            ),
            "INFO"
        )

        # Check if generate_all_configurations mode is enabled
        generate_all = yaml_config_generator.get("generate_all_configurations", False)
        if generate_all:
            self.log(
                "Operational mode: GENERATE ALL CONFIGURATIONS enabled (generate_all_configurations=True). "
                "This mode will retrieve complete switch profile catalog from Catalyst Center "
                "including all CLI templates and site assignments, ignoring any provided filters. "
                "Use this mode for comprehensive network switch profile generation.",
                "INFO"
            )
        else:
            self.log(
                "Operational mode: FILTERED CONFIGURATION generation (generate_all_configurations=False). "
                "This mode will apply global_filters to extract specific switch profile subset "
                "based on profile_name_list, day_n_template_list, or site_list criteria.",
                "INFO"
            )

        self.log("Determining output file path for YAML configuration", "DEBUG")
        file_path = yaml_config_generator.get("file_path")
        if not file_path:
            self.log(
                "No custom file_path provided by user in yaml_config_generator parameters. "
                "Initiating automatic filename generation with timestamp format. Default "
                "filename pattern: network_profile_switching_workflow_manager_playbook_YYYY-MM-DD_HH-MM-SS.yml",
                "DEBUG"
            )
            file_path = self.generate_filename()
            self.log(
                "Auto-generated default filename for YAML output: {0}. File will be created "
                "in current working directory with timestamped name for uniqueness.".format(file_path),
                "INFO"
            )
        else:
            self.log(
                "Using user-provided custom file_path for YAML output: {0}. File will be "
                "created at specified path (absolute or relative path supported).".format(file_path),
                "INFO"
            )

        self.log("YAML configuration file path determined: {0}".format(file_path), "DEBUG")

        self.log("Initializing filter dictionaries", "DEBUG")
        # Set empty filters to retrieve everything
        global_filters = {}
        final_list = []
        if generate_all:
            self.log(
                "Processing in GENERATE ALL CONFIGURATIONS mode. Preparing to collect complete "
                "switch profile catalog from Catalyst Center without applying any filters. "
                "This will include all profiles discovered during get_have() operation.",
                "INFO"
            )

            # Warn if filters provided in generate_all mode
            if yaml_config_generator.get("global_filters"):
                self.log(
                    "Warning: global_filters parameter provided in yaml_config_generator but will "
                    "be IGNORED due to generate_all_configurations=True. In generate_all mode, ALL "
                    "switch profiles are processed regardless of filter criteria. Remove global_filters "
                    "or set generate_all_configurations=False to apply filtering.",
                    "WARNING"
                )

            profile_count = 0
            profiles_with_templates = 0
            profiles_with_sites = 0

            for profile_index, each_profile_name in enumerate(
                self.have.get("switch_profile_names", []), start=1
            ):
                self.log(
                    "Processing switch profile {0}/{1}: '{2}' in generate_all mode. Extracting "
                    "complete CLI template and site assignment metadata from collected data.".format(
                        profile_index, len(self.have.get("switch_profile_names", [])),
                        each_profile_name
                    ),
                    "DEBUG"
                )
                each_profile_config = {}
                each_profile_config["profile_name"] = each_profile_name

                profile_id = self.get_value_by_key(
                    self.have["switch_profile_list"],
                    "name",
                    each_profile_name,
                    "id",
                )
                if not profile_id:
                    self.log(
                        "Profile UUID not found for switch profile {0}/{1}: '{2}'. Profile exists "
                        "in validated names list but has no ID mapping in profile catalog. Skipping "
                        "template and site extraction for this profile.".format(
                            profile_index, len(self.have.get("switch_profile_names", [])),
                            each_profile_name
                        ),
                        "WARNING"
                    )
                    continue

                self.log(
                    "Retrieved profile UUID '{0}' for profile {1}/{2}: '{3}'. Extracting CLI "
                    "templates and site assignments from collected metadata.".format(
                        profile_id, profile_index,
                        len(self.have.get("switch_profile_names", [])), each_profile_name
                    ),
                    "DEBUG"
                )

                cli_template_details = self.have.get("switch_profile_templates", {}).get(profile_id)
                if cli_template_details and isinstance(cli_template_details, list):
                    each_profile_config["day_n_templates"] = cli_template_details
                    profiles_with_templates += 1
                    self.log(
                        "Extracted {0} CLI template(s) for profile {1}/{2}: '{3}'. Template "
                        "names: {4}. Added to day_n_templates field in YAML configuration.".format(
                            len(cli_template_details), profile_index,
                            len(self.have.get("switch_profile_names", [])), each_profile_name,
                            cli_template_details
                        ),
                        "DEBUG"
                    )
                else:
                    self.log(
                        "No CLI templates found for profile {0}/{1}: '{2}'. Profile has no "
                        "template assignments or templates data is invalid. Omitting day_n_templates "
                        "field from YAML configuration (optional field).".format(
                            profile_index, len(self.have.get("switch_profile_names", [])),
                            each_profile_name
                        ),
                        "DEBUG"
                    )

                # Extract site assignment details
                site_details = self.have.get("switch_profile_sites", {}).get(profile_id)
                if site_details and isinstance(site_details, dict):
                    each_profile_config["site_names"] = list(site_details.values())
                    profiles_with_sites += 1
                    self.log(
                        "Extracted {0} site assignment(s) for profile {1}/{2}: '{3}'. "
                        "Hierarchical site names: {4}. Added to site_names field in YAML configuration.".format(
                            len(site_details), profile_index,
                            len(self.have.get("switch_profile_names", [])), each_profile_name,
                            list(site_details.values())
                        ),
                        "DEBUG"
                    )
                else:
                    self.log(
                        "No site assignments found for profile {0}/{1}: '{2}'. Profile has no "
                        "site associations or sites data is invalid. Omitting site_names field "
                        "from YAML configuration (optional field).".format(
                            profile_index, len(self.have.get("switch_profile_names", [])),
                            each_profile_name
                        ),
                        "DEBUG"
                    )

                final_list.append(each_profile_config)
                profile_count += 1

            self.log(
                "Completed generate_all_configurations mode processing. Total configurations "
                "collected: {0}. Statistics - Profiles processed: {1}, Profiles with templates: {2}, "
                "Profiles with sites: {3}. Configuration structure ready for YAML export: {4}".format(
                    len(final_list), profile_count, profiles_with_templates, profiles_with_sites,
                    final_list
                ),
                "INFO"
            )
        else:
            # we get ALL configurations
            self.log(
                "Processing in FILTERED CONFIGURATION mode. Extracting global_filters parameter "
                "to apply hierarchical filtering (profile_name_list > day_n_template_list > site_list). "
                "Only matching switch profiles will be included in YAML export.",
                "INFO"
            )
            if yaml_config_generator.get("global_filters"):
                self.log("Warning: global_filters provided but will be ignored due to generate_all_configurations=True", "WARNING")

            # Use provided filters or default to empty
            global_filters = yaml_config_generator.get("global_filters") or {}

            self.log(
                "Extracted global_filters from yaml_config_generator parameter: {0} (type: {1}). "
                "Validating filter structure and preparing for profile matching operation.".format(
                    global_filters, type(global_filters).__name__
                ),
                "DEBUG"
            )

            if global_filters:
                self.log(
                    "Global filters detected. Calling process_global_filters() to apply filter "
                    "criteria and extract matching switch profile configurations. Filter priority: "
                    "profile_name_list (highest) > day_n_template_list > site_list (lowest).",
                    "INFO"
                )
                final_list = self.process_global_filters(global_filters)

                if final_list:
                    self.log(
                        "Global filter processing completed successfully. Matched {0} switch "
                        "profile(s) against provided filter criteria. Configurations ready for "
                        "YAML export: {1}".format(len(final_list), final_list),
                        "INFO"
                    )
                else:
                    self.log(
                        "Global filter processing returned no matching profiles. Filter criteria "
                        "may be too restrictive or no profiles exist with specified attributes. "
                        "final_list is empty after filter application.",
                        "WARNING"
                    )
            else:
                self.log(
                    "No global_filters provided in yaml_config_generator parameter. Cannot extract "
                    "profile configurations without filter criteria in filtered mode. Set "
                    "generate_all_configurations=True to retrieve all profiles, or provide "
                    "global_filters with profile_name_list, day_n_template_list, or site_list.",
                    "WARNING"
                )

        if not final_list:
            self.log(
                "No switch profile configurations collected after processing. final_list is empty "
                "indicating either no profiles matched filter criteria, or no profiles exist in "
                "Catalyst Center. Possible causes: (1) restrictive global_filters, (2) no profiles "
                "configured, (3) insufficient API permissions. YAML file will NOT be created.",
                "WARNING"
            )
            self.msg = (
                "No configurations or components to process for module '{0}'. Verify input "
                "filters (global_filters) or configuration (generate_all_configurations). "
                "Check that switch profiles exist in Catalyst Center and match filter criteria.".format(
                    self.module_name
                )
            )
            self.set_operation_result("success", False, self.msg, "INFO")
            return self

        final_dict = {"config": final_list}
        self.log(
            "Assembling final YAML configuration structure. Creating root 'config' key with "
            "{0} profile configuration(s). Structure follows network_profile_switching_workflow_manager "
            "module format for Ansible playbook compatibility.".format(len(final_list)),
            "DEBUG"
        )

        final_dict = {"config": final_list}

        self.log(
            "Final YAML dictionary structure created successfully. Complete configuration: {0}. "
            "Structure contains {1} profile(s) with profile_name (required), day_n_templates "
            "(optional), and site_names (optional) fields per profile.".format(
                final_dict, len(final_list)
            ),
            "DEBUG"
        )

        # Write YAML configuration to file
        self.log(
            "Initiating YAML file write operation. Target file path: {0}. Calling "
            "write_dict_to_yaml() to serialize configuration dictionary and create file.".format(
                file_path
            ),
            "INFO"
        )

        if self.write_dict_to_yaml(final_dict, file_path):
            self.log(
                "YAML configuration file created successfully at path: {0}. File contains {1} "
                "switch profile configuration(s) in network_profile_switching_workflow_manager "
                "compatible format. File ready for Ansible playbook execution.".format(
                    file_path, len(final_list)
                ),
                "INFO"
            )
            self.msg = {
                "YAML config generation Task succeeded for module '{0}'.".format(
                    self.module_name
                ): {"file_path": file_path}
            }
            self.set_operation_result("success", True, self.msg, "INFO")
        else:
            self.log(
                "YAML configuration file write FAILED for path: {0}. write_dict_to_yaml() returned "
                "False indicating file creation or serialization error. Verify file path permissions, "
                "directory existence, and disk space availability.".format(file_path),
                "ERROR"
            )
            self.msg = {
                "YAML config generation Task failed for module '{0}'.".format(
                    self.module_name
                ): {"file_path": file_path}
            }
            self.set_operation_result("failed", True, self.msg, "ERROR")

        self.log(
            "Completed yaml_config_generator operation. Operation status: {0}, Changed: {1}, "
            "File path: {2}. Returning control to calling function.".format(
                self.status, self.result.get("changed"), file_path
            ),
            "INFO"
        )

        return self

    def get_want(self, config, state):
        """
        Prepares desired configuration parameters for API operations based on playbook state.

        This function validates input configuration, extracts YAML generation parameters,
        and populates the self.want dictionary with structured data required for network
        switch profile YAML playbook generation workflow in Cisco Catalyst Center.

        Args:
            config (dict): Configuration parameters from Ansible playbook containing:
                  - generate_all_configurations: Mode flag (optional, bool)
                  - file_path: Output file path (optional, str)
                  - global_filters: Filter criteria (optional, dict)
                  Example: {
                    "generate_all_configurations": False,
                    "file_path": "/tmp/config.yml",
                    "global_filters": {
                      "profile_name_list": ["Campus_Profile"]
                    }
                  }
            state (str): Desired state for operation (must be 'gathered').
                        Other states not supported for YAML generation.

        Returns:
            object: Self instance with updated attributes:
                - self.want: Dict containing validated YAML generation parameters
                - self.msg: Success message describing parameter collection
                - self.status: Operation status ("success")
        """

        self.log(
            "Preparing desired configuration parameters for API operations based on playbook "
            "configuration. State parameter: '{0}'. This operation validates input parameters, "
            "extracts YAML generation settings, and populates the want dictionary for downstream "
            "processing by get_have() and yaml_config_generator() functions.".format(state),
            "INFO"
        )

        self.log(
            "Initiating comprehensive input parameter validation using validate_params(). "
            "This validates parameter types, required fields, and schema compliance for "
            "YAML generation workflow.",
            "INFO"
        )

        self.validate_params(config)
        self.log(
            "Input parameter validation completed successfully. All configuration parameters "
            "conform to expected schema and type requirements. Proceeding with want dictionary "
            "population.",
            "DEBUG"
        )

        want = {}

        # Add yaml_config_generator to want
        want["yaml_config_generator"] = config
        self.log(
            "Successfully extracted yaml_config_generator parameters from playbook. Complete "
            "parameter structure: {0}. These parameters will control YAML generation mode "
            "(generate_all vs filtered), output file location, and profile filtering criteria.".format(
                want["yaml_config_generator"]
            ),
            "INFO"
        )

        self.want = want
        self.log("Desired State (want): {0}".format(str(self.want)), "INFO")
        self.msg = "Successfully collected all parameters from the playbook for Network Profile Switching operations."
        self.status = "success"
        return self

    def get_have(self, config):
        """
        Retrieves current network switch profile state from Cisco Catalyst Center.

        This function collects complete switch profile configurations including CLI templates
        (Day-N templates) and site assignments from Catalyst Center based on configuration
        mode (generate_all or filtered) for YAML playbook generation workflow.

        Args:
            config (dict): Configuration parameters containing:
                        - generate_all_configurations: Mode flag (optional, bool)
                        - global_filters: Filter criteria (optional, dict)
                        Example: {
                            "generate_all_configurations": False,
                            "global_filters": {
                            "profile_name_list": ["Campus_Profile"]
                            }
                        }

        Returns:
            object: Self instance with updated attributes:
                - self.have: Dict containing current switch profile state
                - self.msg: Success message describing retrieval result
                - self.status: Operation status (implicit, always success)
        """
        self.log(
            "Retrieving current state of network switch profiles from Cisco Catalyst Center. "
            "This operation collects switch profile configurations including CLI templates "
            "(Day-N templates) and site assignments based on configuration mode (generate_all "
            "or filtered). Data will be used for YAML playbook generation workflow.",
            "INFO"
        )

        if not config or not isinstance(config, dict):
            self.log(
                "Invalid config parameter provided to get_have(). Config is None or not a "
                "dictionary type. Cannot retrieve switch profile data without valid configuration. "
                "Skipping data collection. Config type: {0}".format(type(config).__name__),
                "WARNING"
            )
            self.msg = "Invalid configuration provided. Skipping switch profile data retrieval."
            return self

        self.log(
            "Configuration parameter validated successfully. Config type: dict. Proceeding with "
            "operational mode detection and data collection workflow.",
            "DEBUG"
        )

        if config.get("generate_all_configurations", False):
            self.log("Generate all configurations mode ENABLED (generate_all_configurations=True). "
                     "Initiating complete switch profile catalog collection from Cisco Catalyst Center "
                     "without applying any filters. This mode retrieves ALL switch profiles including "
                     "complete CLI template and site assignment metadata for comprehensive "
                     "network profile switching and documentation.", "INFO")

            self.log(
                "Calling collect_all_switch_profile_list() without profile name filters to "
                "retrieve complete switch profile catalog from Catalyst Center. This will fetch "
                "all network profiles of type 'Switching' using paginated API calls.",
                "INFO"
            )
            self.collect_all_switch_profile_list()
            if not self.have.get("switch_profile_names"):
                self.msg = (
                    "No existing switch profiles found in Cisco Catalyst Center. Please verify "
                    "that switch profiles are configured in the system and API credentials have "
                    "sufficient permissions to retrieve network profile data."
                )
                self.status = "success"
                return self

            self.log(
                "Successfully retrieved {0} switch profile(s) from Catalyst Center in generate_all "
                "mode. Profile names: {1}. Proceeding with CLI template and site assignment "
                "collection for all discovered profiles.".format(
                    len(self.have.get("switch_profile_names", [])),
                    self.have.get("switch_profile_names", [])
                ),
                "INFO"
            )

            self.log(
                "Calling collect_site_and_template_details() for all {0} switch profile(s) to "
                "enrich profile data with CLI template assignments and site hierarchy mappings. "
                "This will make approximately {1} API calls (2 per profile for templates and sites).".format(
                    len(self.have.get("switch_profile_names", [])),
                    len(self.have.get("switch_profile_names", [])) * 2
                ),
                "INFO"
            )
            self.collect_site_and_template_details(self.have.get("switch_profile_names", []))
        else:
            self.log(
                "Filtered configuration mode detected (generate_all_configurations=False or not "
                "specified). Extracting global_filters parameter to determine data collection "
                "strategy. Filter priority: profile_name_list (HIGHEST) > day_n_template_list > "
                "site_list (LOWEST). Only highest priority filter with valid data will be processed.",
                "INFO"
            )

            global_filters = config.get("global_filters")

            if not global_filters or not isinstance(global_filters, dict):
                self.log(
                    "No valid global_filters provided in filtered mode. global_filters is None or "
                    "not a dictionary. Cannot determine which switch profiles to collect. Skipping "
                    "data collection. To retrieve profiles, either enable generate_all_configurations "
                    "or provide global_filters with at least one filter type (profile_name_list, "
                    "day_n_template_list, or site_list).",
                    "WARNING"
                )
                self.msg = (
                    "No global_filters provided in filtered mode. Cannot collect switch profile "
                    "data without filter criteria."
                )
                return self

            self.log(
                "Global filters parameter validated successfully. Extracting individual filter "
                "components: profile_name_list, day_n_template_list, site_list. Filter structure: {0}".format(
                    global_filters
                ),
                "DEBUG"
            )

            # Extract individual filter components
            profile_name_list = global_filters.get("profile_name_list", [])
            day_n_template_list = global_filters.get("day_n_template_list", [])
            site_list = global_filters.get("site_list", [])

            self.log(
                "Extracted filter components from global_filters. profile_name_list: {0} (type: {1}, "
                "count: {2}), day_n_template_list: {3} (type: {4}, count: {5}), site_list: {6} "
                "(type: {7}, count: {8})".format(
                    profile_name_list, type(profile_name_list).__name__, len(profile_name_list) if isinstance(profile_name_list, list) else 0,
                    day_n_template_list, type(day_n_template_list).__name__, len(day_n_template_list) if isinstance(day_n_template_list, list) else 0,
                    site_list, type(site_list).__name__, len(site_list) if isinstance(site_list, list) else 0
                ),
                "DEBUG"
            )

            # Process profile_name_list (HIGHEST PRIORITY)
            if profile_name_list and isinstance(profile_name_list, list):
                self.log(
                    "Profile name list filter detected (HIGHEST PRIORITY). Requested profile names: {0} "
                    "(count: {1}). This filter will be used for targeted switch profile collection. "
                    "Other filters (day_n_template_list, site_list) will be IGNORED due to priority "
                    "hierarchy.".format(profile_name_list, len(profile_name_list)),
                    "INFO"
                )

                self.log(
                    "Calling collect_all_switch_profile_list() with profile_name_list filter to "
                    "retrieve and validate specified switch profiles exist in Catalyst Center. "
                    "Function will fail if any requested profile is not found.",
                    "INFO"
                )

                self.collect_all_switch_profile_list(profile_name_list)

                self.log(
                    "Successfully validated {0} switch profile(s) exist in Catalyst Center. Validated "
                    "profile names: {1}. Proceeding with CLI template and site assignment collection.".format(
                        len(self.have.get("switch_profile_names", [])),
                        self.have.get("switch_profile_names", [])
                    ),
                    "INFO"
                )

                self.collect_site_and_template_details(self.have.get("switch_profile_names", []))

            if day_n_template_list and isinstance(day_n_template_list, list):
                self.log(
                    "Day-N template list filter detected (MEDIUM PRIORITY, profile_name_list not "
                    "provided). Requested template names: {0} (count: {1}). This filter requires "
                    "collecting ALL switch profiles first, then filtering based on template assignments. "
                    "Actual template matching will be performed in process_global_filters().".format(
                        day_n_template_list, len(day_n_template_list)
                    ),
                    "INFO"
                )

                self.log(
                    "Calling collect_all_switch_profile_list() WITHOUT filters to retrieve complete "
                    "switch profile catalog. All profiles needed to identify which contain requested "
                    "CLI templates: {0}".format(day_n_template_list),
                    "INFO"
                )

                self.collect_all_switch_profile_list()

                if not self.have.get("switch_profile_names"):
                    self.log(
                        "No switch profiles found in Catalyst Center for template-based filtering. "
                        "Cannot match templates without existing profiles.",
                        "WARNING"
                    )
                    self.msg = "No switch profiles found for template-based filtering."
                    return self

                self.log(
                    "Retrieved {0} switch profile(s) for template-based filtering. Calling "
                    "collect_site_and_template_details() to collect CLI template assignments for "
                    "all profiles. Template matching against {1} will occur during filter processing.".format(
                        len(self.have.get("switch_profile_names", [])),
                        day_n_template_list
                    ),
                    "INFO"
                )

                self.collect_site_and_template_details(self.have.get("switch_profile_names", []))

            if site_list and isinstance(site_list, list):
                self.log(
                    "Site list filter detected (LOWEST PRIORITY, neither profile_name_list nor "
                    "day_n_template_list provided). Requested site paths: {0} (count: {1}). This "
                    "filter requires collecting ALL switch profiles first, then filtering based on "
                    "site assignments. Actual site matching will be performed in process_global_filters().".format(
                        site_list, len(site_list)
                    ),
                    "INFO"
                )

                self.log(
                    "Calling collect_all_switch_profile_list() WITHOUT filters to retrieve complete "
                    "switch profile catalog. All profiles needed to identify which are assigned to "
                    "requested sites: {0}".format(site_list),
                    "INFO"
                )

                self.collect_all_switch_profile_list()

                if not self.have.get("switch_profile_names"):
                    self.log(
                        "No switch profiles found in Catalyst Center for site-based filtering. "
                        "Cannot match sites without existing profiles.",
                        "WARNING"
                    )
                    self.msg = "No switch profiles found for site-based filtering."
                    return self

                self.log(
                    "Retrieved {0} switch profile(s) for site-based filtering. Calling "
                    "collect_site_and_template_details() to collect site assignments for all "
                    "profiles. Site matching against {1} will occur during filter processing.".format(
                        len(self.have.get("switch_profile_names", [])),
                        site_list
                    ),
                    "INFO"
                )

                self.collect_site_and_template_details(self.have.get("switch_profile_names", []))

        # Log complete self.have structure
        self.log(
            "Switch profile data collection completed successfully. Current state (self.have) "
            "structure populated with switch profile metadata: {0}. Data ready for YAML generation "
            "workflow processing.".format(self.pprint(self.have)),
            "INFO"
        )
        profile_count = len(self.have.get("switch_profile_names", []))
        template_count = len(self.have.get("switch_profile_templates", {}))
        site_count = len(self.have.get("switch_profile_sites", {}))

        self.log(
            "Data collection statistics - Total switch profiles: {0}, Profiles with templates: {1}, "
            "Profiles with sites: {2}. Self.have keys populated: {3}".format(
                profile_count, template_count, site_count, list(self.have.keys())
            ),
            "DEBUG"
        )

        self.msg = (
            "Successfully retrieved network switch profile details from Cisco Catalyst Center. "
            "Collected {0} switch profile(s) with complete CLI template and site assignment "
            "metadata. Data ready for YAML configuration generation.".format(profile_count)
        )

        self.log(
            "Completed get_have() operation successfully. Operation result: {0}. Returning self "
            "instance for method chaining and downstream processing.".format(self.msg),
            "INFO"
        )

        return self

    def get_diff_gathered(self):
        """
        Executes the merge operations for various network configurations in the Cisco Catalyst Center.
        This method processes additions and updates for SSIDs, interfaces, power profiles, access point profiles,
        radio frequency profiles, and anchor groups. It logs detailed information about each operation,
        updates the result status, and returns a consolidated result.

        Args:
            None: Function operates on instance attributes (self.want)

        Returns:
            object: Self instance with updated attributes:
                - self.result: Contains operation results from yaml_config_generator
                - self.msg: Operation completion message
                - self.status: Operation status ("success" or "failed")
        """

        start_time = time.time()
        self.log(
            "Starting YAML configuration generation workflow orchestration (get_diff_gathered). "
            "This operation coordinates the complete YAML playbook generation process by extracting "
            "parameters from validated want dictionary, calling yaml_config_generator function, "
            "and checking operation status. Workflow supports extensible operation pattern for "
            "future enhancements.",
            "DEBUG"
        )
        operations = [
            (
                "yaml_config_generator",
                "YAML Config Generator",
                self.yaml_config_generator,
            )
        ]

        # Iterate over operations and process them
        self.log(
            "Operations configuration defined successfully. Total operations: {0}. Operation "
            "details: {1}. Each operation will be processed sequentially with parameter "
            "validation and status checking.".format(
                len(operations),
                [(op[0], op[1]) for op in operations]  # Log param_key and name only
            ),
            "DEBUG"
        )
        for index, (param_key, operation_name, operation_func) in enumerate(
            operations, start=1
        ):
            self.log(
                "Iteration {0}/{1}: Processing '{2}' operation. Checking for parameters in "
                "self.want using param_key '{3}'. If parameters exist, operation function will "
                "be called with extracted parameters and return status validated.".format(
                    index, len(operations), operation_name, param_key
                ),
                "DEBUG"
            )
            params = self.want.get(param_key)
            if params:
                self.log(
                    "Iteration {0}/{1}: Parameters successfully extracted for '{2}' operation. "
                    "Parameter structure: {3} (type: {4}). Initiating operation execution by "
                    "calling operation function with extracted parameters.".format(
                        index, len(operations), operation_name,
                        param_key, type(params).__name__
                    ),
                    "INFO"
                )

                self.log(
                    "Iteration {0}/{1}:"
                    "Calling operation function '{2}' with extracted parameters. Function will "
                    "process parameters, execute YAML generation workflow, and return self instance "
                    "with updated result status. check_return_status() will validate operation "
                    "success after completion.".format(
                        index, len(operations), operation_name
                    ),
                    "DEBUG"
                )
                operation_func(params).check_return_status()
                self.log(
                    "Iteration {0}/{1}: '{2}' operation completed successfully. check_return_status() "
                    "validated operation success. Result status: {3}, Changed: {4}. Continuing to "
                    "next operation if available.".format(
                        index, len(operations), operation_name,
                        self.status, self.result.get("changed")
                    ),
                    "INFO"
                )
            else:
                self.log(
                    "Iteration {0}/{1}: No parameters found in self.want for '{2}' operation using "
                    "param_key '{3}'. Parameters are None or missing, indicating operation should "
                    "be skipped. This is expected if operation is optional or disabled. Continuing "
                    "to next operation without execution.".format(
                        index, len(operations), operation_name, param_key
                    ),
                    "WARNING"
                )

        end_time = time.time()
        duration = end_time - start_time

        self.log(
            "Completed YAML configuration generation workflow orchestration (get_diff_gathered) "
            "successfully. Total execution time: {0:.2f} seconds. All defined operations processed "
            "sequentially with status validation. Returning self instance for method chaining and "
            "module exit_json() execution.".format(duration),
            "DEBUG"
        )

        return self


def main():
    """
    Main entry point for the Cisco Catalyst Center network profile switching playbook configgenerator module.

    This function serves as the primary execution entry point for the Ansible module,
    orchestrating the complete workflow from parameter collection to YAML playbook
    generation for network profile switching playbook config generator.

    Purpose:
        Initializes and executes the network profile switching playbook config generator
        workflow to extract existing network configurations from Cisco Catalyst Center
        and generate Ansible-compatible YAML playbook files.

    Workflow Steps:
        1. Define module argument specification with required parameters
        2. Initialize Ansible module with argument validation
        3. Create NetworkProfileSwitchingPlaybookGenerator instance
        4. Validate Catalyst Center version compatibility (>= 2.3.7.9)
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
        - Minimum Catalyst Center version: 2.3.7.9
        - Introduced APIs for network profile switching retrieval:
            * Network Switch Profile list (retrieves_the_list_of_network_profiles_for_sites_v1)
            * Profile assigned to sites (retrieves_the_list_of_sites_that_the_given_network_profile_for_sites_is_assigned_to_v1)
            * All available CLI templates (gets_the_templates_available_v1)
            * CLI Templates attached to the profiles (retrieve_cli_templates_attached_to_a_network_profile_v1)

    Supported States:
        - gathered: Extract existing network profile switching and generate YAML playbook
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
            - operation_summary (dict): Execution statistics

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

    # Initialize the NetworkProfileSwitchingPlaybookGenerator object
    # This creates the main orchestrator for network profile switching extraction
    ccc_network_profile_switching_playbook_generator = NetworkProfileSwitchingPlaybookGenerator(module)

    # Log module initialization after object creation (now logging is available)
    ccc_network_profile_switching_playbook_generator.log(
        "Starting Ansible module execution for network profile switching playbook config "
        "generator at timestamp {0}".format(initialization_timestamp),
        "INFO"
    )

    ccc_network_profile_switching_playbook_generator.log(
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
    ccc_network_profile_switching_playbook_generator.log(
        "Validating Catalyst Center version compatibility - checking if version {0} "
        "meets minimum requirement of 2.3.7.9 for network settings APIs".format(
            ccc_network_profile_switching_playbook_generator.get_ccc_version()
        ),
        "INFO"
    )

    if (ccc_network_profile_switching_playbook_generator.compare_dnac_versions(
            ccc_network_profile_switching_playbook_generator.get_ccc_version(), "2.3.7.9") < 0):

        error_msg = (
            "The specified Catalyst Center version '{0}' does not support the YAML "
            "playbook generation for Network profile switching module. Supported versions start "
            "from '2.3.7.9' onwards. Version '2.3.7.9' introduces APIs for retrieving "
            "network profile switching or the following global filters: profile_name_list, "
            "day_n_template_list, and site_list from the Catalyst Center.".format(
                ccc_network_profile_switching_playbook_generator.get_ccc_version()
            )
        )

        ccc_network_profile_switching_playbook_generator.log(
            "Version compatibility check failed: {0}".format(error_msg),
            "ERROR"
        )

        ccc_network_profile_switching_playbook_generator.msg = error_msg
        ccc_network_profile_switching_playbook_generator.set_operation_result(
            "failed", False, ccc_network_profile_switching_playbook_generator.msg, "ERROR"
        ).check_return_status()

    ccc_network_profile_switching_playbook_generator.log(
        "Version compatibility check passed - Catalyst Center version {0} supports "
        "all required network profile switching APIs".format(
            ccc_network_profile_switching_playbook_generator.get_ccc_version()
        ),
        "INFO"
    )

    # ============================================
    # State Parameter Validation
    # ============================================
    state = ccc_network_profile_switching_playbook_generator.params.get("state")

    ccc_network_profile_switching_playbook_generator.log(
        "Validating requested state parameter: '{0}' against supported states: {1}".format(
            state, ccc_network_profile_switching_playbook_generator.supported_states
        ),
        "DEBUG"
    )

    if state not in ccc_network_profile_switching_playbook_generator.supported_states:
        error_msg = (
            "State '{0}' is invalid for this module. Supported states are: {1}. "
            "Please update your playbook to use one of the supported states.".format(
                state, ccc_network_profile_switching_playbook_generator.supported_states
            )
        )

        ccc_network_profile_switching_playbook_generator.log(
            "State validation failed: {0}".format(error_msg),
            "ERROR"
        )

        ccc_network_profile_switching_playbook_generator.status = "invalid"
        ccc_network_profile_switching_playbook_generator.msg = error_msg
        ccc_network_profile_switching_playbook_generator.check_return_status()

    ccc_network_profile_switching_playbook_generator.log(
        "State validation passed - using state '{0}' for workflow execution".format(
            state
        ),
        "INFO"
    )

    # ============================================
    # Input Parameter Validation
    # ============================================
    ccc_network_profile_switching_playbook_generator.log(
        "Starting comprehensive input parameter validation for playbook configuration",
        "INFO"
    )

    ccc_network_profile_switching_playbook_generator.validate_input().check_return_status()

    ccc_network_profile_switching_playbook_generator.log(
        "Input parameter validation completed successfully - all configuration "
        "parameters meet module requirements",
        "INFO"
    )

    # ============================================
    # Configuration Processing Loop
    # ============================================
    config_list = ccc_network_profile_switching_playbook_generator.validated_config

    ccc_network_profile_switching_playbook_generator.log(
        "Starting configuration processing loop - will process {0} configuration "
        "item(s) from playbook".format(len(config_list)),
        "INFO"
    )

    for config_index, config in enumerate(config_list, start=1):
        ccc_network_profile_switching_playbook_generator.log(
            "Processing configuration item {0}/{1} for state '{2}'".format(
                config_index, len(config_list), state
            ),
            "INFO"
        )

        # Reset values for clean state between configurations
        ccc_network_profile_switching_playbook_generator.log(
            "Resetting module state variables for clean configuration processing",
            "DEBUG"
        )
        ccc_network_profile_switching_playbook_generator.reset_values()
        # Collect desired state (want) from configuration
        ccc_network_profile_switching_playbook_generator.log(
            "Collecting desired state parameters from configuration item {0}".format(
                config_index
            ),
            "DEBUG"
        )
        ccc_network_profile_switching_playbook_generator.get_want(
            config, state
        ).check_return_status()

        ccc_network_profile_switching_playbook_generator.get_have(
            config).check_return_status()

        # Execute state-specific operation (gathered workflow)
        ccc_network_profile_switching_playbook_generator.log(
            "Executing state-specific operation for '{0}' workflow on "
            "configuration item {1}".format(state, config_index),
            "INFO"
        )
        ccc_network_profile_switching_playbook_generator.get_diff_state_apply[state]().check_return_status()

        ccc_network_profile_switching_playbook_generator.log(
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

    ccc_network_profile_switching_playbook_generator.log(
        "Module execution completed successfully at timestamp {0}. Total execution "
        "time: {1:.2f} seconds. Processed {2} configuration item(s) with final "
        "status: {3}".format(
            completion_timestamp,
            module_duration,
            len(config_list),
            ccc_network_profile_switching_playbook_generator.status
        ),
        "INFO"
    )

    # Exit module with results
    # This is a terminal operation - function does not return after this
    ccc_network_profile_switching_playbook_generator.log(
        "Exiting Ansible module with result: {0}".format(
            ccc_network_profile_switching_playbook_generator.result
        ),
        "DEBUG"
    )

    module.exit_json(**ccc_network_profile_switching_playbook_generator.result)


if __name__ == "__main__":
    main()
