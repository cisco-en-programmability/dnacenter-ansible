#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import absolute_import, division, print_function
import datetime
import os

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
__metaclass__ = type
from abc import ABCMeta


class BrownFieldHelper:
    """Class contains members which can be reused for all workflow brownfield modules"""

    __metaclass__ = ABCMeta

    def __init__(self):
        pass

    def validate_global_filters(self, global_filters):
        """
        Validates the provided global filters against the valid global filters for the current module.
        Args:
            global_filters (dict): The global filters to be validated.
        Returns:
            bool: True if all filters are valid, False otherwise.
        Raises:
            SystemExit: If validation fails and fail_and_exit is called.
        """
        import re

        self.log(
            "Starting validation of global filters for module: {0}".format(
                self.module_name
            ),
            "INFO",
        )

        # Retrieve the valid global filters from the module mapping
        valid_global_filters = self.module_schema.get("global_filters", {})

        # Check if the module does not support global filters but global filters are provided
        if not valid_global_filters and global_filters:
            self.msg = "Module '{0}' does not support global filters, but 'global_filters' were provided: {1}. Please remove them.".format(
                self.module_name, list(global_filters.keys())
            )
            self.log(self.msg, "ERROR")
            self.fail_and_exit(self.msg)

        # Support legacy format (list of filter names)
        if isinstance(valid_global_filters, list):
            # Legacy validation - keep existing behavior
            invalid_filters = [
                key for key in global_filters.keys() if key not in valid_global_filters
            ]
            if invalid_filters:
                self.msg = "Invalid 'global_filters' found for module '{0}': {1}. Valid 'global_filters' are: {2}".format(
                    self.module_name, invalid_filters, valid_global_filters
                )
                self.log(self.msg, "ERROR")
                self.fail_and_exit(self.msg)
            return True

        # Enhanced validation for new format (dict with rules)
        self.log(
            "Valid global filters for module '{0}': {1}".format(
                self.module_name, list(valid_global_filters.keys())
            ),
            "DEBUG",
        )

        invalid_filters = []

        for filter_name, filter_value in global_filters.items():
            if filter_name not in valid_global_filters:
                invalid_filters.append("Filter '{0}' not supported".format(filter_name))
                continue

            filter_spec = valid_global_filters[filter_name]

            # Validate type
            expected_type = filter_spec.get("type", "str")
            if expected_type == "list" and not isinstance(filter_value, list):
                invalid_filters.append(
                    "Filter '{0}' must be a list, got {1}".format(
                        filter_name, type(filter_value).__name__
                    )
                )
                continue
            elif expected_type == "dict" and not isinstance(filter_value, dict):
                invalid_filters.append(
                    "Filter '{0}' must be a dict, got {1}".format(
                        filter_name, type(filter_value).__name__
                    )
                )
                continue
            elif expected_type == "str" and not isinstance(filter_value, str):
                invalid_filters.append(
                    "Filter '{0}' must be a string, got {1}".format(
                        filter_name, type(filter_value).__name__
                    )
                )
                continue
            elif expected_type == "int" and not isinstance(filter_value, int):
                invalid_filters.append(
                    "Filter '{0}' must be an integer, got {1}".format(
                        filter_name, type(filter_value).__name__
                    )
                )
                continue

            # Validate required
            if filter_spec.get("required", False) and not filter_value:
                invalid_filters.append(
                    "Filter '{0}' is required but empty".format(filter_name)
                )
                continue

            #  ADD: Direct range validation for integers
            if expected_type == "int" and "range" in filter_spec:
                range_values = filter_spec["range"]
                min_val, max_val = range_values[0], range_values[1]
                if not (min_val <= filter_value <= max_val):
                    invalid_filters.append(
                        "Filter '{0}' value {1} is outside valid range [{2}, {3}]".format(
                            filter_name, filter_value, min_val, max_val
                        )
                    )
                    continue

            # Validate list elements
            if expected_type == "list" and filter_value:
                element_type = filter_spec.get("elements", "str")
                validate_ip = filter_spec.get("validate_ip", False)
                pattern = filter_spec.get("pattern")
                range_values = filter_spec.get("range")

                for i, element in enumerate(filter_value):
                    if element_type == "str" and not isinstance(element, str):
                        invalid_filters.append(
                            "Filter '{0}[{1}]' must be a string".format(filter_name, i)
                        )
                        continue
                    elif element_type == "int" and not isinstance(element, int):
                        invalid_filters.append(
                            "Filter '{0}[{1}]' must be an integer".format(
                                filter_name, i
                            )
                        )
                        continue

                    #  ADD: Range validation for list elements
                    if (
                        element_type == "int"
                        and range_values
                        and isinstance(element, int)
                    ):
                        min_val, max_val = range_values[0], range_values[1]
                        if not (min_val <= element <= max_val):
                            invalid_filters.append(
                                "Filter '{0}[{1}]' value {2} is outside valid range [{3}, {4}]".format(
                                    filter_name, i, element, min_val, max_val
                                )
                            )
                            continue

                    # Use existing IP validation functions instead of regex
                    if validate_ip and isinstance(element, str):
                        if not (
                            self.is_valid_ipv4(element) or self.is_valid_ipv6(element)
                        ):
                            invalid_filters.append(
                                "Filter '{0}[{1}]' contains invalid IP address: {2}".format(
                                    filter_name, i, element
                                )
                            )
                    elif (
                        pattern
                        and isinstance(element, str)
                        and not re.match(pattern, element)
                    ):
                        invalid_filters.append(
                            "Filter '{0}[{1}]' does not match required pattern".format(
                                filter_name, i
                            )
                        )

        if invalid_filters:
            self.msg = "Invalid 'global_filters' found for module '{0}': {1}".format(
                self.module_name, invalid_filters
            )
            self.log(self.msg, "ERROR")
            self.fail_and_exit(self.msg)

        self.log(
            "All global filters for module '{0}' are valid.".format(self.module_name),
            "INFO",
        )
        return True

    def validate_component_specific_filters(self, component_specific_filters):
        """
        Validates component-specific filters for the given module.
        Args:
            component_specific_filters (dict): User-provided component-specific filters.
        Returns:
            bool: True if all filters are valid, False otherwise.
        Raises:
            SystemExit: If validation fails and fail_and_exit is called.
        """
        import re

        self.log(
            "Validating 'component_specific_filters' for module: {0}".format(
                self.module_name
            ),
            "INFO",
        )

        # Retrieve network elements for the module
        module_info = self.module_schema
        network_elements = module_info.get("network_elements", {})

        if not network_elements:
            self.msg = "'component_specific_filters' are not supported for module '{0}'.".format(
                self.module_name
            )
            self.fail_and_exit(self.msg)

        # Validate components_list if provided
        components_list = component_specific_filters.get("components_list", [])
        if components_list:
            invalid_components = [
                comp for comp in components_list if comp not in network_elements
            ]
            if invalid_components:
                self.msg = "Invalid network components provided for module '{0}': {1}. Valid components are: {2}".format(
                    self.module_name, invalid_components, list(network_elements.keys())
                )
                self.fail_and_exit(self.msg)

        # Validate each component's filters
        invalid_filters = []

        for component_name, component_filters in component_specific_filters.items():
            if component_name == "components_list":
                continue

            # Check if component exists
            if component_name not in network_elements:
                invalid_filters.append(
                    "Component '{0}' not supported".format(component_name)
                )
                continue

            # Get valid filters for this component
            valid_filters_for_component = network_elements[component_name].get(
                "filters", {}
            )

            # Support legacy format (list of filter names)
            if isinstance(valid_filters_for_component, list):
                if isinstance(component_filters, dict):
                    for filter_name in component_filters.keys():
                        if filter_name not in valid_filters_for_component:
                            invalid_filters.append(
                                "Filter '{0}' not valid for component '{1}'".format(
                                    filter_name, component_name
                                )
                            )
                continue

            # Enhanced validation for new format (dict with rules)
            if isinstance(component_filters, dict):
                for filter_name, filter_value in component_filters.items():
                    if filter_name not in valid_filters_for_component:
                        invalid_filters.append(
                            "Filter '{0}' not valid for component '{1}'".format(
                                filter_name, component_name
                            )
                        )
                        continue

                    filter_spec = valid_filters_for_component[filter_name]

                    # Validate type
                    expected_type = filter_spec.get("type", "str")
                    if expected_type == "list" and not isinstance(filter_value, list):
                        invalid_filters.append(
                            "Component '{0}' filter '{1}' must be a list".format(
                                component_name, filter_name
                            )
                        )
                        continue
                    elif expected_type == "dict" and not isinstance(filter_value, dict):
                        invalid_filters.append(
                            "Component '{0}' filter '{1}' must be a dict".format(
                                component_name, filter_name
                            )
                        )
                        continue
                    elif expected_type == "str" and not isinstance(filter_value, str):
                        invalid_filters.append(
                            "Component '{0}' filter '{1}' must be a string".format(
                                component_name, filter_name
                            )
                        )
                        continue
                    elif expected_type == "int" and not isinstance(filter_value, int):
                        invalid_filters.append(
                            "Component '{0}' filter '{1}' must be an integer".format(
                                component_name, filter_name
                            )
                        )
                        continue

                    #  ADD: Direct range validation for integers
                    if expected_type == "int" and "range" in filter_spec:
                        range_values = filter_spec["range"]
                        min_val, max_val = range_values[0], range_values[1]
                        if not (min_val <= filter_value <= max_val):
                            invalid_filters.append(
                                "Component '{0}' filter '{1}' value {2} is outside valid range [{3}, {4}]".format(
                                    component_name,
                                    filter_name,
                                    filter_value,
                                    min_val,
                                    max_val,
                                )
                            )
                            continue

                    # Validate choices for lists
                    if expected_type == "list" and "choices" in filter_spec:
                        valid_choices = filter_spec["choices"]
                        invalid_choices = [
                            item for item in filter_value if item not in valid_choices
                        ]
                        if invalid_choices:
                            invalid_filters.append(
                                "Component '{0}' filter '{1}' contains invalid choices: {2}. Valid choices: {3}".format(
                                    component_name,
                                    filter_name,
                                    invalid_choices,
                                    valid_choices,
                                )
                            )

                    # Validate choices for strings
                    if expected_type == "str" and "choices" in filter_spec:
                        valid_choices = filter_spec["choices"]
                        if filter_value not in valid_choices:
                            invalid_filters.append(
                                "Component '{0}' filter '{1}' has invalid value: '{2}'. Valid choices: {3}".format(
                                    component_name,
                                    filter_name,
                                    filter_value,
                                    valid_choices,
                                )
                            )

                    # Validate nested dict options and apply dynamic validation
                    if expected_type == "dict" and "options" in filter_spec:
                        nested_options = filter_spec["options"]
                        for nested_key, nested_value in filter_value.items():
                            if nested_key not in nested_options:
                                invalid_filters.append(
                                    "Component '{0}' filter '{1}' contains invalid nested key: '{2}'".format(
                                        component_name, filter_name, nested_key
                                    )
                                )
                                continue

                            nested_spec = nested_options[nested_key]
                            nested_type = nested_spec.get("type", "str")

                            if nested_type == "list" and not isinstance(
                                nested_value, list
                            ):
                                invalid_filters.append(
                                    "Component '{0}' filter '{1}.{2}' must be a list".format(
                                        component_name, filter_name, nested_key
                                    )
                                )
                            elif nested_type == "str" and not isinstance(
                                nested_value, str
                            ):
                                invalid_filters.append(
                                    "Component '{0}' filter '{1}.{2}' must be a string".format(
                                        component_name, filter_name, nested_key
                                    )
                                )
                            elif nested_type == "int" and not isinstance(
                                nested_value, int
                            ):
                                invalid_filters.append(
                                    "Component '{0}' filter '{1}.{2}' must be an integer".format(
                                        component_name, filter_name, nested_key
                                    )
                                )

                            #  ADD: Direct range validation for nested integers
                            if nested_type == "int" and "range" in nested_spec:
                                range_values = nested_spec["range"]
                                min_val, max_val = range_values[0], range_values[1]
                                if not (min_val <= nested_value <= max_val):
                                    invalid_filters.append(
                                        "Component '{0}' filter '{1}.{2}' value {3} is outside valid range [{4}, {5}]".format(
                                            component_name,
                                            filter_name,
                                            nested_key,
                                            nested_value,
                                            min_val,
                                            max_val,
                                        )
                                    )
                                    continue

                            # Validate patterns using regex
                            if "pattern" in nested_spec and isinstance(
                                nested_value, str
                            ):
                                pattern = nested_spec["pattern"]
                                if not re.match(pattern, nested_value):
                                    invalid_filters.append(
                                        "Component '{0}' filter '{1}.{2}' does not match required pattern".format(
                                            component_name, filter_name, nested_key
                                        )
                                    )

        if invalid_filters:
            self.msg = "Invalid filters provided for module '{0}': {1}".format(
                self.module_name, invalid_filters
            )
            self.fail_and_exit(self.msg)

        self.log(
            "All component-specific filters for module '{0}' are valid.".format(
                self.module_name
            ),
            "INFO",
        )
        return True

    def validate_params(self, config):
        """
        Validates the parameters provided for the YAML configuration generator.
        Args:
            config (dict): A dictionary containing the configuration parameters
                for the YAML configuration generator. It may include:
                - "global_filters": A dictionary of global filters to validate.
                - "component_specific_filters": A dictionary of component-specific filters to validate.
            state (str): The state of the operation, e.g., "merged" or "deleted".
        """
        self.log("Starting validation of the input parameters.", "INFO")
        self.log(self.module_schema)

        # Validate global_filters if provided
        global_filters = config.get("global_filters")
        if global_filters:
            self.log(
                "Validating 'global_filters' for module '{0}': {1}.".format(
                    self.module_name, global_filters
                ),
                "INFO",
            )
            self.validate_global_filters(global_filters)
        else:
            self.log(
                "No 'global_filters' provided for module '{0}'; skipping validation.".format(
                    self.module_name
                ),
                "INFO",
            )

        # Validate component_specific_filters if provided
        component_specific_filters = config.get("component_specific_filters")
        if component_specific_filters:
            self.log(
                "Validating 'component_specific_filters' for module '{0}': {1}.".format(
                    self.module_name, component_specific_filters
                ),
                "INFO",
            )
            self.validate_component_specific_filters(component_specific_filters)
        else:
            self.log(
                "No 'component_specific_filters' provided for module '{0}'; skipping validation.".format(
                    self.module_name
                ),
                "INFO",
            )

        self.log("Completed validation of all input parameters.", "INFO")

    def validate_invalid_params(self, config_list, valid_params):
        """
        Validates that all parameters in each configuration entry are valid.

        Args:
            config_list (list): List of configuration dictionaries to validate.
            valid_params (dict_keys): Valid parameter keys for the module.
        """

        self.log(
            "Starting validation of invalid parameters in configuration entries.",
            "DEBUG",
        )

        if not isinstance(config_list, list):
            self.msg = (
                f"Invalid input: Expected a list of configuration entries, "
                f"but got {type(config_list).__name__}."
            )
            self.fail_and_exit(self.msg)

        valid_params_set = set(valid_params)
        if not valid_params_set:
            self.msg = "No valid parameters provided for validation. Please provide valid parameters."
            self.fail_and_exit(self.msg)

        self.log(
            f"Processing validation for {len(config_list)} configuration(s).", "DEBUG"
        )
        for idx, config in enumerate(config_list, start=1):
            self.log(f"Validating configuration entry {idx}: {config}", "DEBUG")

            invalid_params_set = set(config.keys()) - valid_params_set
            if invalid_params_set:
                self.msg = (
                    f"Invalid parameters found in configuration entry {idx}: {list(invalid_params_set)}. "
                    f"Valid parameters are: {list(valid_params_set)}."
                )
                self.fail_and_exit(self.msg)

            self.log(f"Entry {idx}: No invalid parameters found.", "DEBUG")

        self.log(
            "Completed validation of invalid parameters in configuration entries.",
            "DEBUG",
        )

    def validate_minimum_requirements(self, config_list, require_global_filters=False):
        """
        Validate minimum requirements for each configuration entry in a list.

        This function checks each config dictionary in `config_list` to ensure that the
        module can safely proceed with execution. It enforces the following rules:
        - If generate_all_configurations not provided or set to False:
            - component_specific_filters must exist
            - component_specific_filters must contain 'components_list' key (the list can be empty)
        Args:
            config_list : list of config dictionaries to validate.
        """

        self.log(
            "Starting validation of minimum requirements for configuration entries.",
            "DEBUG",
        )

        if not isinstance(config_list, list):
            self.msg = (
                f"Invalid input: Expected a list of configuration entries, "
                f"but got {type(config_list).__name__}."
            )
            self.fail_and_exit(self.msg)

        self.log(
            f"Processing validation for {len(config_list)} configuration(s).", "DEBUG"
        )

        for idx, config in enumerate(config_list, start=1):
            self.log(f"Validating configuration entry {idx}: {config}", "DEBUG")

            has_generate_all_config_flag = "generate_all_configurations" in config
            generate_all_configurations = config.get(
                "generate_all_configurations", False
            )
            component_specific_filters = config.get("component_specific_filters")

            if has_generate_all_config_flag and generate_all_configurations:
                self.log(
                    f"Entry {idx}: generate_all_configurations=True, skipping filters check.",
                    "DEBUG",
                )
                continue  # No further validation needed

            if component_specific_filters is None or "components_list" not in component_specific_filters:
                global_filter_msg = ""
                if require_global_filters:
                    global_filter_msg = "'global filters' or "
            if (
                component_specific_filters is None
                or "components_list" not in component_specific_filters
            ):
                if has_generate_all_config_flag:
                    self.msg = (
                        f"Validation Error in entry {idx}: {global_filter_msg}'component_specific_filters' must be provided "
                        f"with 'components_list' key when 'generate_all_configurations' is set to False."
                    )
                else:
                    self.msg = (
                        f"Validation Error in entry {idx}: 'generate_all_configurations' must be provided as True"
                        f" or {global_filter_msg}'component_specific_filters' must be provided with 'components_list' key."
                    )
                self.fail_and_exit(self.msg)

            self.log(f"Entry {idx}: Passed minimum requirements validation.", "DEBUG")

        self.log(
            "Completed validation of minimum requirements for configuration entries.",
            "DEBUG",
        )

    def validate_minimum_requirement_for_global_filters(self, config_list):
        """
        Validates minimum requirements for configuration entries using global filters.

        This function enforces business logic validation rules for brownfield modules that
        support global_filters-based configuration extraction. It ensures each configuration
        entry provides either generate_all_configurations mode OR valid global_filters,
        preventing invalid configuration states that would result in no-op or ambiguous
        behavior during playbook generation.

        Args:
            config_list (list[dict]): List of configuration dictionaries to validate. Each entry
                                     should contain one or more of:
                - generate_all_configurations (bool, optional): Complete discovery mode flag
                - global_filters (dict, optional): Filter criteria for targeted extraction
                - component_specific_filters (dict, optional): Component-level filters (ignored)

        Returns:
            None (validation passes) or calls fail_and_exit() on validation errors

        Validation Rules:
            Rule 1 (Auto-Discovery Mode):
                - If 'generate_all_configurations' exists AND equals True
                - Skip all filter validation (auto-discovery mode)
                - Continue to next configuration entry

            Rule 2 (Global Filters Mode):
                - If 'global_filters' exists AND is non-empty dict
                - Skip validation (filters provided for targeted extraction)
                - Continue to next configuration entry

            Rule 3 (Invalid Configuration):
                - If neither Rule 1 nor Rule 2 satisfied
                - Configuration is INVALID (missing required parameters)
                - Call fail_and_exit() with detailed error message

        Configuration Modes:
            Auto-Discovery Mode (generate_all_configurations=True):
                - Discovers ALL entities in Catalyst Center
                - Ignores any provided global_filters
                - Suitable for complete brownfield inventory extraction
                - Example: Extract all APs, sites, devices without filtering

            Targeted Extraction Mode (global_filters provided):
                - Filters entities by specific criteria
                - Supports site, hostname, MAC, ID-based filtering
                - Suitable for selective brownfield extraction
                - Example: Extract only APs in specific sites

            Invalid Mode (neither provided):
                - Missing both generate_all and global_filters
                - Cannot determine extraction scope
                - Validation FAILS with error message

        Error Messages:
            Format: "Validation Error in entry {idx}: Either 'generate_all_configurations'
                    must be provided as True or 'global_filters' must be provided"

            Provides clear guidance on required parameters:
                - Option 1: Set generate_all_configurations=True
                - Option 2: Provide valid global_filters dictionary

        Input Validation:
            - config_list must be list type (not dict, str, etc.)
            - Invalid type triggers immediate fail_and_exit()
            - Error message specifies expected type vs. actual type

        Global Filters Validation:
            - Must be dictionary type (not list, str, etc.)
            - Must contain at least one key-value pair (len > 0)
            - Empty dict {} considered invalid (no filter criteria)
            - None or False considered invalid (no filters)

        Integration Points:
            - Called after basic schema validation (validate_list_of_dicts)
            - Called before params validation (validate_params)
            - Ensures configuration is actionable before API calls
            - Prevents ambiguous configuration states

        Notes:
            - This function is for global_filters-based modules only
            - For component_specific_filters modules, use validate_minimum_requirements()
            - generate_all_configurations takes precedence over filters
            - Empty global_filters dict is considered invalid (no criteria)
            - Function name includes "global_filters" to distinguish from component validation
        """
        self.log(
            "Starting minimum requirements validation for configuration entries using "
            "global_filters mode. This validation ensures each configuration provides either "
            "'generate_all_configurations=True' for complete discovery OR 'global_filters' "
            f"dictionary for targeted extraction. Module: '{self.module_name}'",
            "DEBUG"
        )

        # Validate input type
        if not isinstance(config_list, list):
            self.msg = (
                "Invalid input type for validate_minimum_requirement_for_global_filters(): "
                f"Expected list of configuration entries, but got {type(config_list).__name__}. "
                "Configuration must be provided as a list of dictionaries, even if only one "
                f"configuration entry exists. Example: [{{...config...}}]. Module: "
                f"'{self.module_name}'"
            )
            self.log(self.msg, "ERROR")
            self.fail_and_exit(self.msg)

        self.log(
            f"Input type validation passed. Received list with {len(config_list)} configuration "
            "entry/entries to validate. Beginning per-entry validation loop to check minimum "
            "requirements for each configuration.",
            "DEBUG"
        )

        # Validate each configuration entry
        for idx, config in enumerate(config_list, start=1):
            self.log(
                f"Validating configuration entry {idx}/{len(config_list)} for minimum requirements. "
                f"Entry contains {len(config.keys()) if isinstance(config, dict) else 0} parameter(s). "
                f"Configuration: {config}",
                "DEBUG"
            )

            # Extract configuration flags and filters
            has_generate_all_config_flag = "generate_all_configurations" in config
            generate_all_configurations = config.get("generate_all_configurations", False)
            component_specific_filters = config.get("component_specific_filters")
            global_filters = config.get("global_filters", False)

            self.log(
                f"Entry {idx}/{len(config_list)}: Extracted configuration parameters - "
                f"has_generate_all_flag: {has_generate_all_config_flag}, "
                f"generate_all_value: {generate_all_configurations}, "
                f"has_component_filters: {bool(component_specific_filters)}, "
                f"has_global_filters: {bool(global_filters)}, "
                f"global_filters_type: {type(global_filters).__name__}",
                "DEBUG"
            )

            # Rule 1: Check for auto-discovery mode (generate_all_configurations=True)
            if has_generate_all_config_flag and generate_all_configurations:
                self.log(
                    f"Entry {idx}/{len(config_list)}: Auto-discovery mode detected "
                    "(generate_all_configurations=True). This mode will discover ALL entities "
                    "in Cisco Catalyst Center without applying any filter criteria. Skipping "
                    "global_filters validation check as filters are not required in auto-discovery "
                    "mode. Configuration is VALID.",
                    "DEBUG"
                )
                continue  # No further validation needed for auto-discovery mode

            # Rule 2: Check for targeted extraction mode (global_filters provided)
            if global_filters and isinstance(global_filters, dict) and len(global_filters) > 0:
                self.log(
                    f"Entry {idx}/{len(config_list)}: Targeted extraction mode detected "
                    f"(global_filters provided). Found {len(global_filters)} filter type(s): "
                    f"{list(global_filters.keys())}. This mode will apply hierarchical filter "
                    "matching to extract specific entities from Catalyst Center inventory. "
                    "Skipping generate_all_configurations check as valid filters provided. "
                    "Configuration is VALID.",
                    "DEBUG"
                )
                continue  # No further validation needed for targeted extraction mode

            # Rule 3: Invalid configuration - neither auto-discovery nor filters provided
            self.msg = (
                f"Minimum requirements validation FAILED for configuration entry {idx}/{len(config_list)}. "
                "Configuration must provide EITHER 'generate_all_configurations=True' for complete "
                "brownfield discovery OR 'global_filters' dictionary for targeted extraction. "
                f"Current configuration state: generate_all_configurations={generate_all_configurations}, "
                f"global_filters={'empty/invalid' if not global_filters else 'provided but empty dict'}. "
                "Required actions: (1) Set 'generate_all_configurations: true' to extract all entities, "
                f"OR (2) Provide 'global_filters' dictionary with at least one filter type."
            )
            self.log(self.msg, "ERROR")
            self.fail_and_exit(self.msg)

        # All configuration entries passed validation
        self.log(
            f"Completed minimum requirements validation for all {len(config_list)} configuration "
            "entry/entries. All configurations passed validation checks - each provides either "
            "'generate_all_configurations=True' or valid 'global_filters' dictionary. Module can "
            f"proceed with brownfield playbook generation workflow. Module: '{self.module_name}'",
            "DEBUG"
        )

    def yaml_config_generator(self, yaml_config_generator):
        """
        Generates a YAML configuration file based on the provided parameters.
        This function retrieves network element details using global and component-specific filters, processes the data,
        and writes the YAML content to a specified file. It dynamically handles multiple network elements and their respective filters.

        Args:
            yaml_config_generator (dict): Contains file_path, global_filters, and component_specific_filters.

        Returns:
            self: The current instance with the operation result and message updated.
        """

        self.log(
            "Starting YAML config generation with parameters: {0}".format(
                yaml_config_generator
            ),
            "DEBUG",
        )

        # Check if generate_all_configurations mode is enabled
        generate_all = yaml_config_generator.get("generate_all_configurations", False)
        if generate_all:
            self.log(
                "Auto-discovery mode enabled - will process all devices and all features",
                "INFO",
            )

        self.log("Determining output file path for YAML configuration", "DEBUG")
        file_path = yaml_config_generator.get("file_path")
        if not file_path:
            self.log(
                "No file_path provided by user, generating default filename", "DEBUG"
            )
            file_path = self.generate_filename()
        else:
            self.log("Using user-provided file_path: {0}".format(file_path), "DEBUG")

        self.log(
            "YAML configuration file path determined: {0}".format(file_path), "DEBUG"
        )

        self.log("Initializing filter dictionaries", "DEBUG")
        if generate_all:
            # In generate_all_configurations mode, override any provided filters to ensure we get ALL configurations
            self.log(
                "Auto-discovery mode: Overriding any provided filters to retrieve all devices and all features",
                "INFO",
            )
            if yaml_config_generator.get("global_filters"):
                self.log(
                    "Warning: global_filters provided but will be ignored due to generate_all_configurations=True",
                    "WARNING",
                )
            if yaml_config_generator.get("component_specific_filters"):
                self.log(
                    "Warning: component_specific_filters provided but will be ignored due to generate_all_configurations=True",
                    "WARNING",
                )

            # Set empty filters to retrieve everything
            global_filters = {}
            component_specific_filters = {}
        else:
            # Use provided filters or default to empty
            global_filters = yaml_config_generator.get("global_filters") or {}
            component_specific_filters = (
                yaml_config_generator.get("component_specific_filters") or {}
            )

        self.log("Retrieving supported network elements schema for the module", "DEBUG")
        module_supported_network_elements = self.module_schema.get(
            "network_elements", {}
        )

        self.log("Determining components list for processing", "DEBUG")
        components_list = component_specific_filters.get(
            "components_list", list(module_supported_network_elements.keys())
        )

        # If components_list is empty, default to all supported components
        if not components_list:
            self.log(
                "No components specified; processing all supported components.", "DEBUG"
            )
            components_list = list(module_supported_network_elements.keys())

        self.log("Components to process: {0}".format(components_list), "DEBUG")

        self.log(
            "Initializing final configuration list and operation summary tracking",
            "DEBUG",
        )
        final_config_list = []
        processed_count = 0
        skipped_count = 0

        for component in components_list:
            self.log("Processing component: {0}".format(component), "DEBUG")
            network_element = module_supported_network_elements.get(component)
            if not network_element:
                self.log(
                    "Component {0} not supported by module, skipping processing".format(
                        component
                    ),
                    "WARNING",
                )
                skipped_count += 1
                continue

            filters = {
                "global_filters": global_filters,
                "component_specific_filters": component_specific_filters.get(
                    component, []
                ),
            }
            operation_func = network_element.get("get_function_name")
            if not callable(operation_func):
                self.log(
                    "No retrieval function defined for component: {0}".format(
                        component
                    ),
                    "ERROR",
                )
                skipped_count += 1
                continue

            component_data = operation_func(network_element, filters)
            # Validate retrieval success
            if not component_data:
                self.log(
                    "No data retrieved for component: {0}".format(component), "DEBUG"
                )
                continue

            self.log(
                "Details retrieved for {0}: {1}".format(component, component_data),
                "DEBUG",
            )
            processed_count += 1
            final_config_list.append(component_data)

        if not final_config_list:
            self.log(
                "No configurations retrieved. Processed: {0}, Skipped: {1}, Components: {2}".format(
                    processed_count, skipped_count, components_list
                ),
                "WARNING",
            )
            self.msg = {
                "status": "ok",
                "message": (
                    "No configurations found for module '{0}'. Verify filters and component availability. "
                    "Components attempted: {1}".format(
                        self.module_name, components_list
                    )
                ),
                "components_attempted": len(components_list),
                "components_processed": processed_count,
                "components_skipped": skipped_count,
            }
            self.set_operation_result("ok", False, self.msg, "INFO")
            return self

        yaml_config_dict = {"config": final_config_list}
        self.log(
            "Final config dictionary created: {0}".format(
                self.pprint(yaml_config_dict)
            ),
            "DEBUG",
        )

        if self.write_dict_to_yaml(yaml_config_dict, file_path, OrderedDumper):
            self.msg = {
                "status": "success",
                "message": "YAML configuration file generated successfully for module '{0}'".format(
                    self.module_name
                ),
                "file_path": file_path,
                "components_processed": processed_count,
                "components_skipped": skipped_count,
                "configurations_count": len(final_config_list),
            }
            self.set_operation_result("success", True, self.msg, "INFO")

            self.log(
                "YAML configuration generation completed. File: {0}, Components: {1}/{2}, Configs: {3}".format(
                    file_path,
                    processed_count,
                    len(components_list),
                    len(final_config_list),
                ),
                "INFO",
            )
        else:
            self.msg = {
                "YAML config generation Task failed for module '{0}'.".format(
                    self.module_name
                ): {"file_path": file_path}
            }
            self.set_operation_result("failed", True, self.msg, "ERROR")

        return self

    def generate_filename(self):
        """
        Generates a filename for the module with a timestamp and '.yml' extension in the format 'YYYY-MM-DD_HH-MM-SS'.
        Args:
            module_name (str): The name of the module for which the filename is generated.
        Returns:
            str: The generated filename with the format 'module_name_playbook_timestamp.yml'.
        """
        self.log("Starting the filename generation process.", "INFO")

        # Get the current timestamp in the desired format
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        self.log("Timestamp successfully generated: {0}".format(timestamp), "DEBUG")

        # Construct the filename
        self.module_name_prefix = self.module_name.split("_workflow_manager")[0]

        filename = "{0}_playbook_config_{1}.yml".format(
            self.module_name_prefix, timestamp
        )
        self.log("Filename successfully constructed: {0}".format(filename), "DEBUG")

        self.log(
            "Filename generation process completed successfully: {0}".format(filename),
            "INFO",
        )
        return filename

    def ensure_directory_exists(self, file_path):
        """Ensure the directory for the file path exists."""
        self.log(
            "Starting 'ensure_directory_exists' for file path: {0}".format(file_path),
            "INFO",
        )

        # Extract the directory from the file path
        directory = os.path.dirname(file_path)
        self.log("Extracted directory: {0}".format(directory), "DEBUG")

        # Check if the directory exists
        if directory and not os.path.exists(directory):
            self.log(
                "Directory '{0}' does not exist. Creating it.".format(directory), "INFO"
            )
            os.makedirs(directory)
            self.log("Directory '{0}' created successfully.".format(directory), "INFO")
        else:
            self.log(
                "Directory '{0}' already exists. No action needed.".format(directory),
                "INFO",
            )

    def write_dict_to_yaml(self, data_dict, file_path, dumper=OrderedDumper):
        """
        Converts a dictionary to YAML format and writes it to a specified file path.
        Args:
            data_dict (dict): The dictionary to convert to YAML format.
            file_path (str): The path where the YAML file will be written.
            dumper: The YAML dumper class to use for serialization (default is OrderedDumper).
        Returns:
            bool: True if the YAML file was successfully written, False otherwise.
        """

        self.log(
            "Starting to write dictionary to YAML file at: {0}".format(file_path),
            "DEBUG",
        )
        try:
            self.log("Starting conversion of dictionary to YAML format.", "INFO")
            # yaml_content = yaml.dump(
            #     data_dict, Dumper=OrderedDumper, default_flow_style=False
            # )
            yaml_content = yaml.dump(
                data_dict,
                Dumper=dumper,
                default_flow_style=False,
                indent=2,
                allow_unicode=True,
                sort_keys=False,  # Important: Don't sort keys to preserve order
            )
            yaml_content = "---\n" + yaml_content
            self.log("Dictionary successfully converted to YAML format.", "DEBUG")

            # Ensure the directory exists
            self.ensure_directory_exists(file_path)

            self.log(
                "Preparing to write YAML content to file: {0}".format(file_path), "INFO"
            )
            with open(file_path, "w") as yaml_file:
                yaml_file.write(yaml_content)

            self.log(
                "Successfully written YAML content to {0}.".format(file_path), "INFO"
            )
            return True

        except Exception as e:
            self.msg = "An error occurred while writing to {0}: {1}".format(
                file_path, str(e)
            )
            self.fail_and_exit(self.msg)

    # Important Note: This function removes params with  null values
    def modify_parameters(self, temp_spec, details_list):
        """
        Modifies the parameters of the provided details_list based on the temp_spec.
        Args:
            temp_spec (OrderedDict): An ordered dictionary defining the structure and transformation rules for the parameters.
            details_list (list): A list of dictionaries containing the details to be modified.
        Returns:
            list: A list of dictionaries containing the modified details based on the temp_spec.
        """

        self.log("Details list: {0}".format(details_list), "DEBUG")
        modified_details = []
        self.log("Starting modification of parameters based on temp_spec.", "INFO")

        for index, detail in enumerate(details_list):
            mapped_detail = OrderedDict()  # Use OrderedDict to preserve order
            self.log("Processing detail {0}: {1}".format(index, detail), "DEBUG")

            for key, spec in temp_spec.items():
                self.log(
                    "Processing key '{0}' with spec: {1}".format(key, spec), "DEBUG"
                )

                if spec.get("fixed_value") is not None:
                    mapped_detail[key] = spec["fixed_value"]
                    self.log(
                        "Assigned fixed value for key '{0}': {1}".format(
                            key, mapped_detail[key]
                        ),
                        "DEBUG",
                    )
                    continue

                source_key = spec.get("source_key", key)
                value = detail.get(source_key)

                self.log(
                    "Retrieved value for source key '{0}': {1}".format(
                        source_key, value
                    ),
                    "DEBUG",
                )

                transform = spec.get("transform", lambda x: x)
                self.log(
                    "Using transformation function for key '{0}'.".format(key), "DEBUG"
                )

                # Handle different spec types with appropriate None handling
                if spec["type"] == "dict":
                    if spec.get("special_handling"):
                        self.log(
                            "Special handling detected for key '{0}'.".format(key),
                            "DEBUG",
                        )
                        transformed_value = transform(detail)
                        # Skip if transformed value is null/None
                        if transformed_value is not None:
                            mapped_detail[key] = transformed_value
                            self.log(
                                "Mapped detail for key '{0}' using special handling: {1}".format(
                                    key, mapped_detail[key]
                                ),
                                "DEBUG",
                            )
                    else:
                        # Handle nested dictionary mapping - process only if value exists
                        if value is not None:
                            self.log(
                                "Mapping nested dictionary for key '{0}'.".format(key),
                                "DEBUG",
                            )
                            self.log(
                                "Nested dictionary value to be processed: {0}".format(
                                    value
                                ),
                                "DEBUG",
                            )
                            self.log(
                                "Spec options for nested dictionary: {0}".format(
                                    spec.get("options")
                                ),
                                "DEBUG",
                            )
                            nested_result = self.modify_parameters(
                                spec["options"], [value]
                            )
                            if (
                                nested_result and nested_result[0]
                            ):  # Check if nested result is not empty
                                mapped_detail[key] = nested_result[0]
                                self.log(
                                    "Mapped nested dictionary for key '{0}': {1}".format(
                                        key, mapped_detail[key]
                                    ),
                                    "DEBUG",
                                )
                        else:
                            # Handle nested dictionary mapping - process even if value is None
                            self.log(
                                "Mapping nested dictionary for key '{0}'.".format(key),
                                "DEBUG",
                            )
                            nested_result = self.modify_parameters(
                                spec["options"], [detail]
                            )
                            if (
                                nested_result and nested_result[0]
                            ):  # Check if nested result is not empty
                                mapped_detail[key] = nested_result[0]
                                self.log(
                                    "Mapped nested dictionary for key '{0}': {1}".format(
                                        key, mapped_detail[key]
                                    ),
                                    "DEBUG",
                                )

                elif spec["type"] == "list":
                    if spec.get("special_handling"):
                        self.log(
                            "Special handling detected for key '{0}'.".format(key),
                            "DEBUG",
                        )
                        transformed_value = transform(detail)
                        # Skip if transformed value is null/None or empty list
                        if transformed_value is not None and transformed_value != []:
                            mapped_detail[key] = transformed_value
                            self.log(
                                "Mapped detail for key '{0}' using special handling: {1}".format(
                                    key, mapped_detail[key]
                                ),
                                "DEBUG",
                            )
                    else:
                        # For lists, only process if value exists and is not None
                        if value is not None:
                            if (
                                isinstance(value, list) and value
                            ):  # Check if list is not empty
                                processed_list = []
                                for v in value:
                                    if v is not None:  # Skip None items in the list
                                        if isinstance(v, dict):
                                            nested_result = self.modify_parameters(
                                                spec["options"], [v]
                                            )
                                            if nested_result and nested_result[0]:
                                                processed_list.append(nested_result[0])
                                        else:
                                            transformed_item = transform(v)
                                            if transformed_item is not None:
                                                processed_list.append(transformed_item)

                                if (
                                    processed_list
                                ):  # Only add if list is not empty after processing
                                    mapped_detail[key] = processed_list
                            elif (
                                value
                            ):  # Handle non-list values that are not None or empty
                                transformed_value = transform(value)
                                if (
                                    transformed_value is not None
                                    and transformed_value != []
                                ):
                                    mapped_detail[key] = transformed_value

                            if key in mapped_detail:
                                self.log(
                                    "Mapped list for key '{0}' with transformation: {1}".format(
                                        key, mapped_detail[key]
                                    ),
                                    "DEBUG",
                                )
                        else:
                            self.log(
                                "Skipping list key '{0}' because value is null/None".format(
                                    key
                                ),
                                "DEBUG",
                            )

                elif spec["type"] == "str" and spec.get("special_handling"):
                    transformed_value = transform(detail)
                    # Skip if transformed value is null/None or empty string
                    if transformed_value is not None and transformed_value != "":
                        mapped_detail[key] = transformed_value
                        self.log(
                            "Mapped detail for key '{0}' using special handling: {1}".format(
                                key, mapped_detail[key]
                            ),
                            "DEBUG",
                        )
                else:
                    # For str, int, and other simple types - skip if value is None
                    if value is None:
                        self.log(
                            "Skipping key '{0}' because value is null/None".format(key),
                            "DEBUG",
                        )
                        continue

                    transformed_value = transform(value)
                    # Skip if transformed value is null/None
                    if transformed_value is not None:
                        # For strings, also skip empty strings if desired (optional)
                        if spec["type"] == "str" and transformed_value == "":
                            self.log(
                                "Skipping key '{0}' because transformed value is empty string".format(
                                    key
                                ),
                                "DEBUG",
                            )
                            continue

                        mapped_detail[key] = transformed_value
                        self.log(
                            "Mapped '{0}' to '{1}' with transformed value: {2}".format(
                                source_key, key, mapped_detail[key]
                            ),
                            "DEBUG",
                        )

            modified_details.append(mapped_detail)
            self.log(
                "Finished processing detail {0}. Mapped detail: {1}".format(
                    index, mapped_detail
                ),
                "INFO",
            )

        self.log("Completed modification of all details.", "INFO")

        return modified_details

    def get_value_by_key(self, data_list, key_name, key_value, return_key):
        """
        Get value from a list of dictionaries based on a key-value pair.

        Args:
            data_list: List of dictionaries to search
            key_name: Key to match (e.g., "name")
            key_value: Value to match (e.g., "Campus_Switch_Profile")
            return_key: Key whose value to return (e.g., "id")

        Returns:
            Value of return_key if found, None otherwise
        """
        for item in data_list:
            if item.get(key_name) == key_value:
                return item.get(return_key)

        return None

    # Important Note: This function retains params with null values
    # def modify_parameters(self, temp_spec, details_list):
    #     """
    #     Modifies the parameters of the provided details_list based on the temp_spec.
    #     Args:
    #         temp_spec (OrderedDict): An ordered dictionary defining the structure and transformation rules for the parameters.
    #         details_list (list): A list of dictionaries containing the details to be modified.
    #     Returns:
    #         list: A list of dictionaries containing the modified details based on the temp_spec.
    #     """

    #     self.log("Details list: {0}".format(details_list), "DEBUG")
    #     modified_details = []
    #     self.log("Starting modification of parameters based on temp_spec.", "INFO")

    #     for index, detail in enumerate(details_list):
    #         mapped_detail = OrderedDict()  # Use OrderedDict to preserve order
    #         self.log("Processing detail {0}: {1}".format(index, detail), "DEBUG")

    #         for key, spec in temp_spec.items():
    #             self.log(
    #                 "Processing key '{0}' with spec: {1}".format(key, spec), "DEBUG"
    #             )

    #             source_key = spec.get("source_key", key)
    #             value = detail.get(source_key)
    #             self.log(
    #                 "Retrieved value for source key '{0}': {1}".format(
    #                     source_key, value
    #                 ),
    #                 "DEBUG",
    #             )

    #             transform = spec.get("transform", lambda x: x)
    #             self.log(
    #                 "Using transformation function for key '{0}'.".format(key), "DEBUG"
    #             )

    #             if spec["type"] == "dict":
    #                 if spec.get("special_handling"):
    #                     self.log(
    #                         "Special handling detected for key '{0}'.".format(key),
    #                         "DEBUG",
    #                     )
    #                     mapped_detail[key] = transform(detail)
    #                     self.log(
    #                         "Mapped detail for key '{0}' using special handling: {1}".format(
    #                             key, mapped_detail[key]
    #                         ),
    #                         "DEBUG",
    #                     )
    #                 else:
    #                     # Handle nested dictionary mapping
    #                     self.log(
    #                         "Mapping nested dictionary for key '{0}'.".format(key),
    #                         "DEBUG",
    #                     )
    #                     mapped_detail[key] = self.modify_parameters(
    #                         spec["options"], [detail]
    #                     )[0]
    #                     self.log(
    #                         "Mapped nested dictionary for key '{0}': {1}".format(
    #                             key, mapped_detail[key]
    #                         ),
    #                         "DEBUG",
    #                     )
    #             elif spec["type"] == "list":
    #                 if spec.get("special_handling"):
    #                     self.log(
    #                         "Special handling detected for key '{0}'.".format(key),
    #                         "DEBUG",
    #                     )
    #                     mapped_detail[key] = transform(detail)
    #                     self.log(
    #                         "Mapped detail for key '{0}' using special handling: {1}".format(
    #                             key, mapped_detail[key]
    #                         ),
    #                         "DEBUG",
    #                     )
    #                 else:
    #                     if isinstance(value, list):
    #                         mapped_detail[key] = [
    #                             (
    #                                 self.modify_parameters(spec["options"], [v])[0]
    #                                 if isinstance(v, dict)
    #                                 else transform(v)
    #                             )
    #                             for v in value
    #                         ]
    #                     else:
    #                         mapped_detail[key] = transform(value) if value else []
    #                 self.log(
    #                     "Mapped list for key '{0}' with transformation: {1}".format(
    #                         key, mapped_detail[key]
    #                     ),
    #                     "DEBUG",
    #                 )
    #             elif spec["type"] == "str" and spec.get("special_handling"):
    #                 mapped_detail[key] = transform(detail)
    #                 self.log(
    #                     "Mapped detail for key '{0}' using special handling: {1}".format(
    #                         key, mapped_detail[key]
    #                     ),
    #                     "DEBUG",
    #                 )
    #             else:
    #                 mapped_detail[key] = transform(value)
    #                 self.log(
    #                     "Mapped '{0}' to '{1}' with transformed value: {2}".format(
    #                         source_key, key, mapped_detail[key]
    #                     ),
    #                     "DEBUG",
    #                 )

    #         modified_details.append(mapped_detail)
    #         self.log(
    #             "Finished processing detail {0}. Mapped detail: {1}".format(
    #                 index, mapped_detail
    #             ),
    #             "INFO",
    #         )

    #     self.log("Completed modification of all details.", "INFO")

    #     return modified_details

    def get_want(self, config, state):
        """
        Creates parameters for API calls based on the specified state.
        This method prepares the parameters required for adding, updating, or deleting
        network configurations such as SSIDs and interfaces in the Cisco Catalyst Center
        based on the desired state. It logs detailed information for each operation.
        Args:
            config (dict): The configuration data for the network elements.
            state (str): The desired state of the network elements ('merged' or 'deleted').
        Returns:
            self: Current instance with updated attributes:
            - self.want (dict): Desired state containing yaml_config_generator params
            - self.msg (str): Success message for operation
            - self.status (str): Operation status ("success")
        """

        self.log(
            "Creating Parameters for API Calls with state: {0}".format(state), "INFO"
        )

        self.validate_params(config)

        # Add yaml_config_generator to want
        self.want["yaml_config_generator"] = config

        self.log("Desired State (want): {0}".format(self.pprint(self.want)), "INFO")
        self.msg = "Successfully collected all parameters from the playbook for config generation."
        self.status = "success"
        return self

    def execute_get_with_pagination(
        self, api_family, api_function, params, offset=1, limit=500, use_strings=False
    ):
        """
        Executes a paginated GET request using the specified API family, function, and parameters.
        Args:
            api_family (str): The API family to use for the call (For example, 'wireless', 'network', etc.).
            api_function (str): The specific API function to call for retrieving data (For example, 'get_ssid_by_site', 'get_interfaces').
            params (dict): Parameters for filtering the data.
            offset (int, optional): Starting offset for pagination. Defaults to 1.
            limit (int, optional): Maximum number of records to retrieve per page. Defaults to 500.
            use_strings (bool, optional): Whether to use string values for offset and limit. Defaults to False.
        Returns:
            list: A list of dictionaries containing the retrieved data based on the filtering parameters.
        """
        self.log(
            "Starting paginated API execution for family '{0}', function '{1}'".format(
                api_family, api_function
            ),
            "DEBUG",
        )

        def update_params(current_offset, current_limit):
            """Update the params dictionary with pagination info."""
            # Create a copy of params to avoid modifying the original
            updated_params = params.copy()
            updated_params.update(
                {
                    "offset": str(current_offset) if use_strings else current_offset,
                    "limit": str(current_limit) if use_strings else current_limit,
                }
            )
            return updated_params

        try:
            # Initialize results list and keep offset/limit as integers for arithmetic
            if not params:
                self.log(
                    "Starting paginated GET request for family '{0}', function '{1}' with initial params: {2}".format(
                        api_family, api_function, params
                    ),
                    "INFO",
                )
                params = {}

            results = []
            current_offset = offset
            current_limit = limit

            self.log(
                "Pagination settings - offset: {0}, limit: {1}, use_strings: {2}".format(
                    current_offset, current_limit, use_strings
                ),
                "DEBUG",
            )

            # Start the loop for paginated API calls
            while True:
                # Update parameters for pagination
                api_params = update_params(current_offset, current_limit)

                try:
                    # Execute the API call
                    self.log(
                        "Attempting API call with offset {0} and limit {1} for family '{2}', function '{3}': {4}".format(
                            current_offset,
                            current_limit,
                            api_family,
                            api_function,
                            api_params,
                        ),
                        "INFO",
                    )

                    # Execute the API call
                    response = self.dnac._exec(
                        family=api_family,
                        function=api_function,
                        op_modifies=False,
                        params=api_params,
                    )

                except Exception as e:
                    # Handle error during API call
                    self.msg = (
                        "An error occurred while retrieving data using family '{0}', function '{1}'. "
                        "Error: {2}".format(api_family, api_function, str(e))
                    )
                    self.fail_and_exit(self.msg)

                self.log(
                    "Response received from API call for family '{0}', function '{1}': {2}".format(
                        api_family, api_function, response
                    ),
                    "DEBUG",
                )

                # Process the response if available
                response_data = response.get("response")
                if not response_data:
                    self.log(
                        "Exiting the loop because no data was returned after increasing the offset. "
                        "Current offset: {0}".format(current_offset),
                        "INFO",
                    )
                    break

                # Extend the results list with the response data
                results.extend(response_data)

                # Check if the response size is less than the limit
                if len(response_data) < current_limit:
                    self.log(
                        "Received less than limit ({0}) results, assuming last page. Exiting pagination.".format(
                            current_limit
                        ),
                        "DEBUG",
                    )
                    break

                # Increment the offset for the next iteration (always use integer arithmetic)
                current_offset = int(current_offset) + int(current_limit)

            if results:
                self.log(
                    "Data retrieved for family '{0}', function '{1}': Total records: {2}".format(
                        api_family, api_function, len(results)
                    ),
                    "INFO",
                )
            else:
                self.log(
                    "No data found for family '{0}', function '{1}'.".format(
                        api_family, api_function
                    ),
                    "DEBUG",
                )

            # Return the list of retrieved data
            return results

        except Exception as e:
            self.msg = (
                "An error occurred while retrieving data using family '{0}', function '{1}'. "
                "Error: {2}".format(api_family, api_function, str(e))
            )
            self.fail_and_exit(self.msg)

    def get_site_id_from_fabric_site_or_zones(self, fabric_id, fabric_type):
        """
        Retrieves the site ID from fabric sites or zones based on the provided fabric ID and type.
        Args:
            fabric_id (str): The ID of the fabric site or zone.
            fabric_type (str): The type of fabric, either "fabric_site" or "fabric_zone".
        Returns:
            str: The site ID retrieved from the fabric site or zones.
        Raises:
            Exception: If an error occurs while retrieving the site ID.
        """

        site_id = None
        self.log(
            "Retrieving site ID from fabric site or zones for fabric_id: {0}, fabric_type: {1}".format(
                fabric_id, fabric_type
            ),
            "DEBUG",
        )

        if fabric_type == "fabric_site":
            function_name = "get_fabric_sites"
        else:
            function_name = "get_fabric_zones"

        try:
            response = self.dnac._exec(
                family="sda",
                function=function_name,
                op_modifies=False,
                params={"id": fabric_id},
            )
            response = response.get("response")
            self.log(
                "Received API response from '{0}': {1}".format(
                    function_name, str(response)
                ),
                "DEBUG",
            )

            if not response:
                self.msg = "No fabric sites or zones found for fabric_id: {0} with type: {1}".format(
                    fabric_id, fabric_type
                )
                return site_id

            site_id = response[0].get("siteId")
            self.log(
                "Retrieved site ID: {0} from fabric site or zones.".format(site_id),
                "DEBUG",
            )

        except Exception as e:
            self.msg = """Error while getting the details of fabric site or zones with ID '{0}' and type '{1}': {2}""".format(
                fabric_id, fabric_type, str(e)
            )
            self.log(self.msg, "ERROR")
            self.fail_and_exit(self.msg)

        return site_id

    def analyse_fabric_site_or_zone_details(self, fabric_id):
        """
        Analyzes the fabric site or zone details to determine the site ID and fabric type.
        Args:
            fabric_id (str): The ID of the fabric site or zone.
        Returns:
            tuple: A tuple containing the site ID and fabric type.
                - site_id (str): The ID of the fabric site or zone.
                - fabric_type (str): The type of fabric, either "fabric_site" or "fabric_zone".
        """

        self.log(
            "Analyzing fabric site or zone details for fabric_id: {0}".format(
                fabric_id
            ),
            "DEBUG",
        )
        site_id, fabric_type = None, None

        site_id = self.get_site_id_from_fabric_site_or_zones(fabric_id, "fabric_site")
        if not site_id:
            site_id = self.get_site_id_from_fabric_site_or_zones(
                fabric_id, "fabric_zone"
            )
            if not site_id:
                return None, None

            self.log(
                "Fabric zone ID '{0}' retrieved successfully.".format(site_id), "DEBUG"
            )
            return site_id, "fabric_zone"

        self.log(
            "Fabric site ID '{0}' retrieved successfully.".format(site_id), "DEBUG"
        )
        return site_id, "fabric_site"

    def get_site_id(self, site_name):
        """
        Retrieves the site ID for a given site name.
        Args:
            site_name (str): The name of the site for which to retrieve the ID.
        Returns:
            str: The ID of the site.
        Raises:
            Exception: If an error occurs while retrieving the site name hierarchy.
        """

        self.log("Retrieving site name hierarchy for all sites.", "DEBUG")
        self.log("Executing 'get_sites' API call to retrieve all sites.", "DEBUG")
        site_id = None

        api_family, api_function, params = (
            "site_design",
            "get_sites",
            {"nameHierarchy": site_name},
        )
        site_details = self.execute_get_with_pagination(
            api_family, api_function, params
        )

        if site_details:
            site_id = site_details[0].get("id")

        return site_id

    def get_site_name(self, site_id):
        """
        Retrieves the site name hierarchy for a given site ID.
        Args:
            site_id (str): The ID of the site for which to retrieve the name hierarchy.
        Returns:
            str: The name hierarchy of the site.
        Raises:
            Exception: If an error occurs while retrieving the site name hierarchy.
        """

        self.log(
            "Retrieving site name hierarchy for site_id: {0}".format(site_id), "DEBUG"
        )
        api_family, api_function, params = "site_design", "get_sites", {}
        site_details = self.execute_get_with_pagination(
            api_family, api_function, params
        )
        if not site_details:
            self.msg = "No site details found for site_id: {0}".format(site_id)
            self.fail_and_exit(self.msg)

        site_name_hierarchy = None
        for site in site_details:
            if site.get("id") == site_id:
                site_name_hierarchy = site.get("nameHierarchy")
                break

        # If site_name_hierarchy is not found, log an error and exit
        if not site_name_hierarchy:
            self.msg = "Site name hierarchy not found for site_id: {0}".format(site_id)
            self.fail_and_exit(self.msg)

        self.log(
            "Site name hierarchy for site_id '{0}': {1}".format(
                site_id, site_name_hierarchy
            ),
            "INFO",
        )

        return site_name_hierarchy

    def get_site_id_name_mapping(self, site_id_list=None):
        """
        Retrieves the site name hierarchy for all sites.

        Args:
            site_id_list (list): A list of site IDs to retrieve for the name hierarchies.

        Returns:
            dict: A dictionary mapping site IDs to their name hierarchies.

        Raises:
            Exception: If an error occurs while retrieving the site name hierarchies.
        """

        self.log("Retrieving site name hierarchy for all sites.", "DEBUG")
        self.log("Executing 'get_sites' API call to retrieve all sites.", "DEBUG")
        site_id_name_mapping = {}

        api_family, api_function, params = "site_design", "get_sites", {}
        site_details = self.execute_get_with_pagination(
            api_family, api_function, params
        )

        ccc_version = self.get_ccc_version()
        for site in site_details:
            site_id = site.get("id")
            if site_id:
                if (
                    self.compare_dnac_versions(ccc_version, "2.3.7.9") <= 0
                    and site.get("type") == "global"
                ):
                    # For versions <= 2.3.7.9
                    self.log(
                        f"Processing site ID '{site_id}' with type 'global' for CCC version <= 2.3.7.9, using name instead of nameHierarchy",
                        "DEBUG",
                    )
                    site_id_name_mapping[site_id] = site.get("name")
                else:
                    self.log(
                        f"Processing site ID '{site_id}', mapping to nameHierarchy: {site.get('nameHierarchy')}",
                        "DEBUG",
                    )
                    site_id_name_mapping[site_id] = site.get("nameHierarchy")

        if site_id_list:
            filtered_mapping = {
                site_id: site_id_name_mapping[site_id]
                for site_id in site_id_list
                if site_id in site_id_name_mapping
            }
            self.log(
                "Filtered site ID to name hierarchy mapping: {0}".format(
                    filtered_mapping
                ),
                "DEBUG",
            )
            return filtered_mapping

        self.log(
            f"Site ID to name mapping completed. Total sites mapped: {len(site_id_name_mapping)}",
            "INFO",
        )
        return site_id_name_mapping

    def get_deployed_layer2_feature_configuration(self, network_device_id, feature):
        """
        Retrieves the configurations for a deployed layer 2 feature on a wired device.
        Args:
            device_id (str): Network device ID of the wired device.
            feature (str): Name of the layer 2 feature to retrieve (Example, 'vlan', 'cdp', 'stp').
        Returns:
            dict: The configuration details of the deployed layer 2 feature.
        """
        self.log(
            "Retrieving deployed configuration for layer 2 feature '{0}' on device {1}".format(
                feature, network_device_id
            ),
            "INFO",
        )
        # Prepare the API parameters
        api_params = {"id": network_device_id, "feature": feature}
        # Execute the API call to get the deployed layer 2 feature configuration
        return self.execute_get_request(
            "wired",
            "get_configurations_for_a_deployed_layer2_feature_on_a_wired_device",
            api_params,
        )

    def get_device_list_params(
        self, ip_address_list=None, hostname_list=None, serial_number_list=None
    ):
        """
        Generates a dictionary of device list parameters based on the provided IP address, hostname, or serial number.
        Args:
            ip_address (str): The management IP address of the device.
            hostname (str): The hostname of the device.
            serial_number (str, optional): The serial number of the device.
        Returns:
            dict: A dictionary containing the device list parameters with either 'management_ip_address', 'hostname', or 'serialNumber'.
        """
        # Return a dictionary with 'management_ip_address' if ip_address is provided
        if ip_address_list:
            self.log(
                "Using IP addresses '{0}' for device list parameters".format(
                    ip_address_list
                ),
                "DEBUG",
            )
            return {"management_ip_address": ip_address_list}

        # Return a dictionary with 'hostname' if hostname is provided
        if hostname_list:
            self.log(
                "Using hostnames '{0}' for device list parameters".format(
                    hostname_list
                ),
                "DEBUG",
            )
            return {"hostname": hostname_list}

        # Return a dictionary with 'serialNumber' if serial_number is provided
        if serial_number_list:
            self.log(
                "Using serial numbers '{0}' for device list parameters".format(
                    serial_number_list
                ),
                "DEBUG",
            )
            return {"serial_number": serial_number_list}

        # Return an empty dictionary if none is provided
        self.log(
            "No IP addresses, hostnames, or serial numbers provided, returning empty parameters",
            "DEBUG",
        )
        return {}

    def get_device_list(self, get_device_list_params):
        """
        Fetches device IDs from Cisco Catalyst Center based on provided parameters using pagination.
        Args:
            get_device_list_params (dict): Parameters for querying the device list, such as IP address, hostname, or serial number.
        Returns:
            dict: A dictionary mapping management IP addresses to device information including ID, hostname, and serial number.
        Description:
            This method queries Cisco Catalyst Center using the provided parameters to retrieve device information.
            It checks if each device is reachable, managed, and not a Unified AP. If valid, it maps the management IP
            address to a dictionary containing device instance ID, hostname, and serial number.
        """
        # Initialize the dictionary to map management IP to device information
        mgmt_ip_to_device_info_map = {}
        self.log(
            "Parameters for 'get_device_list' API call: {0}".format(
                get_device_list_params
            ),
            "DEBUG",
        )

        try:
            # Use the existing pagination function to get all devices
            self.log(
                "Using execute_get_with_pagination to retrieve device list", "DEBUG"
            )
            device_list = self.execute_get_with_pagination(
                api_family="devices",
                api_function="get_device_list",
                params=get_device_list_params,
            )

            if not device_list:
                self.log(
                    "No devices were returned for the given parameters: {0}".format(
                        get_device_list_params
                    ),
                    "WARNING",
                )
                return mgmt_ip_to_device_info_map

            # Iterate through all devices in the response
            valid_devices_count = 0
            total_devices_count = len(device_list)

            self.log(
                "Processing {0} devices from the API response".format(
                    total_devices_count
                ),
                "INFO",
            )

            for device_info in device_list:
                device_ip = device_info.get("managementIpAddress")
                device_hostname = device_info.get("hostname")
                device_serial = device_info.get("serialNumber")
                device_id = device_info.get("id")
                device_software_version = device_info.get("softwareVersion")
                device_platform = device_info.get("platformId")

                self.log(
                    "Processing device: IP={0}, Hostname={1}, Serial={2}, ID={3}".format(
                        device_ip, device_hostname, device_serial, device_id
                    ),
                    "DEBUG",
                )

                # Check if the device is reachable, not a Unified AP, and in a managed state
                if (
                    device_info.get("reachabilityStatus") == "Reachable"
                    and device_info.get("collectionStatus")
                    in ["Managed", "In Progress"]
                    and device_info.get("family") != "Unified AP"
                ):
                    # Create device information dictionary
                    device_data = {
                        "device_id": device_id,
                        "hostname": device_hostname,
                        "serial_number": device_serial,
                        "software_version": device_software_version,
                        "platform": device_platform,
                    }

                    mgmt_ip_to_device_info_map[device_ip] = device_data
                    valid_devices_count += 1

                    self.log(
                        "Device {0} (hostname: {1}, serial: {2}) is valid and added to the map.".format(
                            device_ip, device_hostname, device_serial
                        ),
                        "INFO",
                    )
                else:
                    self.log(
                        "Device {0} (hostname: {1}, serial: {2}) is not valid - Status: {3}, Collection: {4}, Family: {5}".format(
                            device_ip,
                            device_hostname,
                            device_serial,
                            device_info.get("reachabilityStatus"),
                            device_info.get("collectionStatus"),
                            device_info.get("family"),
                        ),
                        "WARNING",
                    )

            self.log(
                "Device processing complete: {0}/{1} devices are valid and added to mapping".format(
                    valid_devices_count, total_devices_count
                ),
                "INFO",
            )

        except Exception as e:
            # Log an error message if any exception occurs during the process
            self.log(
                "Error while fetching device IDs from Cisco Catalyst Center using API 'get_device_list' for parameters: {0}. "
                "Error: {1}".format(get_device_list_params, str(e)),
                "ERROR",
            )

        # Only fail and exit if no valid devices are found
        if not mgmt_ip_to_device_info_map:
            self.msg = (
                "Unable to retrieve details for any devices matching parameters: {0}. "
                "Please verify the device parameters and ensure devices are reachable and managed."
            ).format(get_device_list_params)
            self.fail_and_exit(self.msg)

        return mgmt_ip_to_device_info_map

    def get_device_id_management_ip_mapping(self, get_device_list_params=None):
        """
        Fetches device IDs from Cisco Catalyst Center based on provided parameters using pagination.
        Args:
            get_device_list_params (dict): Parameters for querying the device list, such as IP address, hostname, or serial number.
        Returns:
            dict: A dictionary mapping management IP addresses to device information including ID, hostname, and serial number.
        Description:
            This method queries Cisco Catalyst Center using the provided parameters to retrieve device information.
            It checks if each device is reachable, managed, and not a Unified AP. If valid, it maps the management IP
            address to a dictionary containing device instance ID, hostname, and serial number.
        """
        # Initialize the dictionary to map management IP to device information
        mgmt_id_to_device_ip_map = {}
        self.log(
            "Parameters for 'get_device_list' API call: {0}".format(
                get_device_list_params
            ),
            "DEBUG",
        )

        try:
            # Use the existing pagination function to get all devices
            self.log(
                "Using execute_get_with_pagination to retrieve device list", "DEBUG"
            )
            device_list = self.execute_get_with_pagination(
                api_family="devices",
                api_function="get_device_list",
                params=get_device_list_params,
            )

            if not device_list:
                self.log(
                    "No devices were returned for the given parameters: {0}".format(
                        get_device_list_params
                    ),
                    "WARNING",
                )
                return mgmt_id_to_device_ip_map

            for device_info in device_list:
                device_ip = device_info.get("managementIpAddress")
                device_id = device_info.get("id")
                self.log(
                    "Processing device: IP={0}, ID={1}".format(device_ip, device_id),
                    "DEBUG",
                )

                mgmt_id_to_device_ip_map[device_id] = device_ip
                self.log(
                    "Device '{0}' is added to the map.".format(device_ip),
                    "INFO",
                )

        except Exception as e:
            # Log an error message if any exception occurs during the process
            self.log(
                "Error while fetching device IDs from Cisco Catalyst Center using API 'get_device_list' for parameters: {0}. "
                "Error: {1}".format(get_device_list_params, str(e)),
                "ERROR",
            )

        # Only fail and exit if no devices are found
        if not mgmt_id_to_device_ip_map:
            self.msg = (
                "Unable to retrieve details for any devices matching parameters: {0}. "
                "Please verify the device parameters and ensure devices are reachable and managed."
            ).format(get_device_list_params)
            self.fail_and_exit(self.msg)

        return mgmt_id_to_device_ip_map

    def get_network_device_details(
        self, ip_addresses=None, hostnames=None, serial_numbers=None
    ):
        """
        Retrieves the network device ID for a given IP address list or hostname list.
        Args:
            ip_address (list): The IP addresses of the devices to be queried.
            hostnames (list): The hostnames of the devices to be queried.
            serial_numbers (list): The serial numbers of the devices to be queried.
        Returns:
            dict: A dictionary mapping management IP addresses to device IDs.
                Returns an empty dictionary if no devices are found.
        """
        # Get Device IP Address and Id (networkDeviceId required)
        self.log(
            "Starting device ID retrieval for IPs: '{0}' or Hostnames: '{1}' or Serial Numbers: '{2}'.".format(
                ip_addresses, hostnames, serial_numbers
            ),
            "DEBUG",
        )
        get_device_list_params = self.get_device_list_params(
            ip_address_list=ip_addresses,
            hostname_list=hostnames,
            serial_number_list=serial_numbers,
        )
        self.log(
            "get_device_list_params constructed: {0}".format(get_device_list_params),
            "DEBUG",
        )
        mgmt_ip_to_instance_id_map = self.get_device_list(get_device_list_params)
        self.log(
            "Collected mgmt_ip_to_instance_id_map: {0}".format(
                mgmt_ip_to_instance_id_map
            ),
            "DEBUG",
        )

        return mgmt_ip_to_instance_id_map

    def modify_network_parameters(self, reverse_mapping_spec, data_list):
        """
        Transform API response data from Catalyst Center format to Ansible playbook format.

        Applies reverse mapping specification to convert raw API responses into clean,
        Ansible-compatible YAML configuration format by mapping fields, converting types,
        and applying custom transformation functions.

        Args:
            reverse_mapping_spec (OrderedDict): Specification dictionary containing:
                - target_key (str): Target field name in Ansible config
                - mapping_rule (dict): Transformation rules including:
                    - source_key (str): Source field path in API response
                    - type (str): Expected data type for validation
                    - transform (callable, optional): Custom transformation function
                    - optional (bool, optional): Whether field is optional
                    - special_handling (bool, optional): Requires special processing

            data_list (list): List of data objects from DNAC API responses to transform.

        Returns:
            list: Transformed data list suitable for Ansible playbook configuration.
                 Each item is transformed according to the mapping specification with:
                 - Field names converted to Ansible-compatible format
                 - Data types properly converted and validated
                 - Optional fields handled appropriately
                 - Custom transformations applied where specified

        Transformation Process:
            1. Iterates through each data item in the input list
            2. Applies each mapping rule from the specification
            3. Extracts nested values using dot-notation source keys
            4. Applies custom transform functions when specified
            5. Validates and sanitizes values based on expected types
            6. Handles optional fields and missing data gracefully
            7. Preserves semantic meaning (e.g., empty lists for server configs)

        Error Handling:
            - Logs warnings for transformation errors
            - Skips invalid data items with detailed logging
            - Handles missing nested fields gracefully
            - Preserves partial transformations when possible

        Examples:
            API Response -> Ansible Config transformation:
            {'siteName': 'Global/USA/NYC'} -> {'site_name': 'Global/USA/NYC'}
        """
        self.log(
            "Starting transformation of {0} API response items using {1} mapping rules to convert "
            "Catalyst Center format to Ansible playbook format".format(
                len(data_list) if data_list else 0,
                len(reverse_mapping_spec) if reverse_mapping_spec else 0,
            ),
            "DEBUG",
        )
        if not reverse_mapping_spec:
            self.log(
                "Reverse mapping specification is empty or None, cannot perform transformation. "
                "Returning empty list.",
                "WARNING",
            )
            return []

        if not isinstance(reverse_mapping_spec, (dict, OrderedDict)):
            self.log(
                "Invalid reverse mapping specification - expected dict or OrderedDict, got {0}. "
                "Returning empty list.".format(type(reverse_mapping_spec).__name__),
                "ERROR",
            )
            return []

        if not data_list:
            self.log(
                "Data list is empty or None, no API response data to transform. "
                "Returning empty list.",
                "DEBUG",
            )
            return []

        if not isinstance(data_list, list):
            self.log(
                "Invalid data_list - expected list, got {0}. Attempting to wrap in list.".format(
                    type(data_list).__name__
                ),
                "WARNING",
            )
            data_list = [data_list]

        self.log(
            "Input validation successful - processing {0} data items with {1} mapping rules".format(
                len(data_list), len(reverse_mapping_spec)
            ),
            "DEBUG",
        )

        transformed_data = []
        items_processed = 0
        items_failed = 0

        for item_index, data_item in enumerate(data_list):
            self.log(
                "Processing data item {0}/{1}".format(item_index + 1, len(data_list)),
                "DEBUG",
            )

            if not isinstance(data_item, dict):
                self.log(
                    "Skipping invalid data item at index {0} - expected dict, got {1}".format(
                        item_index, type(data_item).__name__
                    ),
                    "WARNING",
                )
                items_failed += 1
                continue

            transformed_item = {}
            fields_processed = 0
            fields_failed = 0

            # Apply each mapping rule from the specification
            for target_key, mapping_rule in reverse_mapping_spec.items():
                try:
                    # Validate mapping rule structure
                    if not isinstance(mapping_rule, dict):
                        self.log(
                            "Invalid mapping rule for field '{0}' - expected dict, got {1}. "
                            "Skipping field.".format(
                                target_key, type(mapping_rule).__name__
                            ),
                            "WARNING",
                        )
                        fields_failed += 1
                        continue

                    source_key = mapping_rule.get("source_key")
                    transform_func = mapping_rule.get("transform")
                    is_optional = mapping_rule.get("optional", False)

                    value = None

                    # Case 1: Transform function without source_key (uses entire data_item)
                    if (
                        source_key is None
                        and transform_func
                        and callable(transform_func)
                    ):
                        self.log(
                            "Applying custom transformation for field '{0}' using transform function "
                            "on entire data item".format(target_key),
                            "DEBUG",
                        )

                        try:
                            value = transform_func(data_item)
                            self.log(
                                "Transform function succeeded for field '{0}', result type: {1}".format(
                                    target_key, type(value).__name__
                                ),
                                "DEBUG",
                            )
                        except Exception as transform_error:
                            self.log(
                                "Transform function failed for field '{0}': {1}. "
                                "Setting value to None.".format(
                                    target_key, str(transform_error)
                                ),
                                "WARNING",
                            )
                            value = None
                            fields_failed += 1

                    # Case 2: Extract value from source_key path
                    elif source_key:
                        self.log(
                            "Extracting value for field '{0}' from source path '{1}'".format(
                                target_key, source_key
                            ),
                            "DEBUG",
                        )

                        value = self._extract_nested_value(data_item, source_key)

                        if value is None and not is_optional:
                            self.log(
                                "Required field '{0}' has no value at source path '{1}'".format(
                                    target_key, source_key
                                ),
                                "DEBUG",
                            )

                        # Apply transformation function if specified and value exists
                        if (
                            transform_func
                            and callable(transform_func)
                            and value is not None
                        ):
                            self.log(
                                "Applying custom transformation to extracted value for field '{0}'".format(
                                    target_key
                                ),
                                "DEBUG",
                            )

                            try:
                                original_value = value
                                value = transform_func(value)
                                self.log(
                                    "Transform function succeeded for field '{0}': {1} -> {2}".format(
                                        target_key,
                                        type(original_value).__name__,
                                        type(value).__name__,
                                    ),
                                    "DEBUG",
                                )
                            except Exception as transform_error:
                                self.log(
                                    "Transform function failed for field '{0}': {1}. "
                                    "Using original extracted value.".format(
                                        target_key, str(transform_error)
                                    ),
                                    "WARNING",
                                )
                                fields_failed += 1

                    # Case 3: No source_key and no transform function
                    else:
                        self.log(
                            "Skipping field '{0}' - no source_key or transform function provided "
                            "in mapping rule".format(target_key),
                            "DEBUG",
                        )
                        continue

                    # Sanitize the value based on expected type
                    expected_type = mapping_rule.get("type", "str")
                    try:
                        sanitized_value = self._sanitize_value(value, expected_type)

                        # Only add non-None values or explicitly include None for optional fields
                        if sanitized_value is not None or (
                            is_optional and value is None
                        ):
                            transformed_item[target_key] = sanitized_value
                            fields_processed += 1

                            self.log(
                                "Successfully transformed field '{0}': type={1}, optional={2}".format(
                                    target_key, expected_type, is_optional
                                ),
                                "DEBUG",
                            )

                    except Exception as sanitize_error:
                        self.log(
                            "Value sanitization failed for field '{0}' (expected type: {1}): {2}. "
                            "Skipping field.".format(
                                target_key, expected_type, str(sanitize_error)
                            ),
                            "WARNING",
                        )
                        fields_failed += 1
                        continue

                except Exception as field_error:
                    self.log(
                        "Unexpected error transforming field '{0}': {1}. Skipping field.".format(
                            target_key, str(field_error)
                        ),
                        "WARNING",
                    )
                    fields_failed += 1
                    continue

            # Add transformed item to result list
            if transformed_item:
                transformed_data.append(transformed_item)
                items_processed += 1

                self.log(
                    "Completed transformation of data item {0}/{1}: {2} fields processed, "
                    "{3} fields failed".format(
                        item_index + 1, len(data_list), fields_processed, fields_failed
                    ),
                    "DEBUG",
                )
            else:
                self.log(
                    "Data item {0}/{1} resulted in empty transformation - all fields were skipped "
                    "or failed".format(item_index + 1, len(data_list)),
                    "WARNING",
                )
                items_failed += 1

                # Sanitize the value
                value = self._sanitize_value(value, mapping_rule.get("type", "str"))

                transformed_item[target_key] = value

            transformed_data.append(transformed_item)
            self.log(
                "Completed transformation of API response data to Ansible playbook format: "
                "{0} items successfully transformed, {1} items failed, "
                "total output: {2} configuration objects".format(
                    items_processed, items_failed, len(transformed_data)
                ),
                "INFO",
            )

        return transformed_data

    def _extract_nested_value(self, data_item, key_path):
        """
        Extract a value from nested dictionary structure using dot notation key path.

        Safely navigates nested dictionary structures to extract values at arbitrary
        depth levels using dot-separated key paths. Handles missing keys gracefully
        with comprehensive logging for debugging brownfield configuration extraction.


        Args:
            data_item (dict or None): The source dictionary to extract values from.
                                     Can be None or empty dict.
            key_path (str): Dot-separated path to the target value.
                           Examples: 'settings.dns.servers', 'ipV4AddressSpace.subnet'

        Returns:
            any or None: The value at the specified key path, or None if:
                        - key_path is empty or None
                        - data_item is None or not a dictionary
                        - Any key in the path doesn't exist
                        - Path traversal encounters non-dict value

        """
        self.log(
            "Extracting nested value from dictionary structure using dot-notation "
            "path traversal for brownfield configuration transformation",
            "DEBUG",
        )

        self.log(
            "Extraction parameters - Key path: '{0}', Data type: {1}".format(
                key_path if key_path else "None",
                type(data_item).__name__ if data_item is not None else "None",
            ),
            "DEBUG",
        )

        if not key_path:
            self.log(
                "Key path is empty or None, cannot extract value from nested structure. "
                "Returning None.",
                "DEBUG",
            )
            return None

        if not isinstance(key_path, str):
            self.log(
                "Invalid key_path parameter type - expected str, got {0}. "
                "Cannot perform dot-notation traversal. Returning None.".format(
                    type(key_path).__name__
                ),
                "WARNING",
            )
            return None

        # Validate data_item parameter
        if not data_item:
            self.log(
                "Data item is empty or None for key path '{0}', cannot navigate "
                "nested structure. Returning None.".format(key_path),
                "DEBUG",
            )
            return None

        if not isinstance(data_item, dict):
            self.log(
                "Data item is not a dict (type: {0}) for key path '{1}', cannot "
                "navigate nested structure. Returning None.".format(
                    type(data_item).__name__, key_path
                ),
                "WARNING",
            )
            return None

        keys = key_path.split(".")
        value = data_item

        # Traverse the nested structure
        for index, key in enumerate(keys, start=1):
            # Log current traversal step
            self.log(
                "Traversal step {0}/{1}: Attempting to access key '{2}' in {3}".format(
                    index, len(keys), key, type(value).__name__
                ),
                "DEBUG",
            )

            # Validate current value is a dictionary before accessing key
            if not isinstance(value, dict):
                self.log(
                    "Cannot traverse further at step {0}/{1} - current value at key "
                    "'{2}' is {3}, not dict. Path: '{4}'. Returning None.".format(
                        index,
                        len(keys),
                        keys[index - 2] if index > 1 else "root",
                        type(value).__name__,
                        key_path,
                    ),
                    "DEBUG",
                )
                return None

            # Attempt to access the key
            if key in value:
                value = value[key]

                self.log(
                    "Traversal step {0}/{1}: Successfully accessed key '{2}', "
                    "retrieved value type: {3}".format(
                        index, len(keys), key, type(value).__name__
                    ),
                    "DEBUG",
                )
            else:
                # Key not found - log available keys for debugging
                available_keys = list(value.keys())

                # Limit displayed keys to first 10 for readability
                keys_display = (
                    available_keys[:10] if len(available_keys) > 10 else available_keys
                )
                more_indicator = (
                    " (and {0} more)".format(len(available_keys) - 10)
                    if len(available_keys) > 10
                    else ""
                )

                self.log(
                    "Traversal failed at step {0}/{1} - key '{2}' not found in nested "
                    "structure. Path: '{3}'. Available keys at this level: {4}{5}. "
                    "Returning None.".format(
                        index, len(keys), key, key_path, keys_display, more_indicator
                    ),
                    "DEBUG",
                )
                return None

        self.log(
            "Successfully completed nested value extraction for path '{0}': "
            "traversed {1} level(s), retrieved value type: {2}".format(
                key_path, len(keys), type(value).__name__
            ),
            "DEBUG",
        )

        return value

    def _sanitize_value(self, value, value_type):
        """
        Sanitize and normalize a value based on its expected type for YAML output.

        Performs type validation, conversion, and normalization to ensure values are
        properly formatted for Ansible YAML configurations. Handles type coercion with
        comprehensive logging and provides sensible defaults for missing or invalid values.

        Args:
            value: The raw value to sanitize from API response. Can be any type:
                - None: Represents missing or unconfigured values
                - str: String values (may need boolean/numeric conversion)
                - list: Collections (may need singleton wrapping)
                - dict: Nested configuration objects
                - int/float: Numeric values requiring string conversion
                - bool: Boolean flags requiring lowercase string conversion

            value_type (str): Expected target type for validation and conversion:
                - "str": String type with special handling for booleans/numbers
                - "list": List type with singleton conversion support
                - "dict": Dictionary/object type for nested configurations
                - "int": Integer type for numeric values
                - "bool": Boolean type for flags
                - Other: Pass-through with minimal processing

        Returns:
            Sanitized value of the appropriate type:
            - For None input: Returns appropriate empty value ([], {}, "")
            - For type mismatches: Attempts conversion or wrapping
            - For strings: Handles boolean/numeric conversion
            - For primitives: Converts to target type with validation

        Type Conversion Rules:
            None handling:
                - "list" → [] (empty list)
                - "dict" → {} (empty dict)
                - "int" → 0 (zero)
                - "bool" → False
                - Other → "" (empty string)

            String conversions:
                - bool True → "true" (lowercase)
                - bool False → "false" (lowercase)
                - int/float → string representation
                - Other types → str() conversion

            List handling:
                - Non-list values wrapped in single-element list
                - Empty/None values → []
                - Preserves existing lists unchanged

        Examples:
            # None handling
            _sanitize_value(None, "list") → []
            _sanitize_value(None, "dict") → {}
            _sanitize_value(None, "str") → ""

            # String conversions
            _sanitize_value(True, "str") → "true"
            _sanitize_value(123, "str") → "123"
            _sanitize_value("hello", "str") → "hello"

            # List handling
            _sanitize_value("single", "list") → ["single"]
            _sanitize_value(["a", "b"], "list") → ["a", "b"]
            _sanitize_value(None, "list") → []

            # Type preservation
            _sanitize_value({"key": "val"}, "dict") → {"key": "val"}
            _sanitize_value(42, "int") → 42
        """
        self.log(
            "Sanitizing value for YAML output compatibility: value_type='{0}', "
            "input_type={1}".format(
                value_type, type(value).__name__ if value is not None else "None"
            ),
            "DEBUG",
        )

        # =====================================
        # Handle None/Empty Values
        # =====================================
        if value is None:
            self.log(
                "Input value is None, returning type-appropriate empty value for type '{0}'".format(
                    value_type
                ),
                "DEBUG",
            )

            # Return type-specific default values for None
            if value_type == "list":
                self.log("Returning empty list [] for None value", "DEBUG")
                return []
            elif value_type == "dict":
                self.log("Returning empty dict {{}} for None value", "DEBUG")
                return {}
            elif value_type == "int":
                self.log("Returning zero (0) for None integer value", "DEBUG")
                return 0
            elif value_type == "bool":
                self.log("Returning False for None boolean value", "DEBUG")
                return False
            else:
                self.log("Returning empty string for None value (default)", "DEBUG")
                return ""

        # =====================================
        # List Type Handling
        # =====================================
        if value_type == "list":
            self.log(
                "Processing list type conversion for value type: {0}".format(
                    type(value).__name__
                ),
                "DEBUG",
            )

            # Already a list - return as-is
            if isinstance(value, list):
                self.log(
                    "Value is already a list with {0} element(s), returning unchanged".format(
                        len(value)
                    ),
                    "DEBUG",
                )
                return value

            # Non-list value - wrap in single-element list
            if value:
                self.log(
                    "Wrapping non-list value (type: {0}) into single-element list".format(
                        type(value).__name__
                    ),
                    "DEBUG",
                )
                return [value]
            else:
                # Empty/falsy value
                self.log(
                    "Value is falsy (type: {0}), returning empty list".format(
                        type(value).__name__
                    ),
                    "DEBUG",
                )
                return []

        # =====================================
        # String Type Handling
        # =====================================
        if value_type == "str":
            self.log(
                "Processing string type conversion for value type: {0}".format(
                    type(value).__name__
                ),
                "DEBUG",
            )

            # Boolean to lowercase string conversion
            if isinstance(value, bool):
                result = str(value).lower()
                self.log(
                    "Converted boolean {0} to lowercase string: '{1}'".format(
                        value, result
                    ),
                    "DEBUG",
                )
                return result

            # Numeric to string conversion
            elif isinstance(value, (int, float)):
                result = str(value)
                self.log(
                    "Converted numeric value {0} (type: {1}) to string: '{2}'".format(
                        value, type(value).__name__, result
                    ),
                    "DEBUG",
                )
                return result

            # Already a string
            elif isinstance(value, str):
                self.log(
                    "Value is already a string (length: {0}), returning unchanged".format(
                        len(value)
                    ),
                    "DEBUG",
                )
                return value

            # Other types - attempt str() conversion
            else:
                try:
                    result = str(value)
                    self.log(
                        "Converted value of type {0} to string using str() conversion".format(
                            type(value).__name__
                        ),
                        "DEBUG",
                    )
                    return result
                except Exception as e:
                    self.log(
                        "Failed to convert value of type {0} to string: {1}. "
                        "Returning empty string as fallback.".format(
                            type(value).__name__, str(e)
                        ),
                        "WARNING",
                    )
                    return ""

        # =====================================
        # Integer Type Handling
        # =====================================
        if value_type == "int":
            self.log(
                "Processing integer type conversion for value type: {0}".format(
                    type(value).__name__
                ),
                "DEBUG",
            )

            # Already an integer
            if isinstance(value, int) and not isinstance(value, bool):
                self.log("Value is already an integer: {0}".format(value), "DEBUG")
                return value

            # Try converting to integer
            try:
                result = int(value)
                self.log(
                    "Successfully converted value from type {0} to integer: {1}".format(
                        type(value).__name__, result
                    ),
                    "DEBUG",
                )
                return result
            except (ValueError, TypeError) as e:
                self.log(
                    "Failed to convert value '{0}' (type: {1}) to integer: {2}. "
                    "Returning 0 as fallback.".format(
                        value, type(value).__name__, str(e)
                    ),
                    "WARNING",
                )
                return 0

        # =====================================
        # Boolean Type Handling
        # =====================================
        if value_type == "bool":
            self.log(
                "Processing boolean type conversion for value type: {0}".format(
                    type(value).__name__
                ),
                "DEBUG",
            )

            # Already a boolean
            if isinstance(value, bool):
                self.log("Value is already a boolean: {0}".format(value), "DEBUG")
                return value

            # String to boolean conversion
            if isinstance(value, str):
                value_lower = value.lower().strip()

                # True values
                if value_lower in ("true", "yes", "on", "1", "enabled"):
                    self.log(
                        "Converted string '{0}' to boolean: True".format(value), "DEBUG"
                    )
                    return True

                # False values
                elif value_lower in ("false", "no", "off", "0", "disabled", ""):
                    self.log(
                        "Converted string '{0}' to boolean: False".format(value),
                        "DEBUG",
                    )
                    return False

                # Ambiguous string
                else:
                    self.log(
                        "Ambiguous string value '{0}' for boolean conversion, "
                        "using Python bool() evaluation".format(value),
                        "WARNING",
                    )
                    result = bool(value)
                    return result

            # Numeric to boolean
            elif isinstance(value, (int, float)):
                result = bool(value)
                self.log(
                    "Converted numeric value {0} to boolean: {1}".format(value, result),
                    "DEBUG",
                )
                return result

            # Other types - use Python's truthiness
            else:
                result = bool(value)
                self.log(
                    "Converted value of type {0} to boolean using Python bool(): {1}".format(
                        type(value).__name__, result
                    ),
                    "DEBUG",
                )
                return result

        # =====================================
        # Dictionary Type Handling
        # =====================================
        if value_type == "dict":
            self.log(
                "Processing dictionary type validation for value type: {0}".format(
                    type(value).__name__
                ),
                "DEBUG",
            )

            if isinstance(value, dict):
                self.log(
                    "Value is already a dict with {0} key(s), returning unchanged".format(
                        len(value)
                    ),
                    "DEBUG",
                )
                return value
            else:
                self.log(
                    "Value is not a dict (type: {0}), returning empty dict as fallback".format(
                        type(value).__name__
                    ),
                    "WARNING",
                )
                return {}

        # =====================================
        # Unknown/Unhandled Type - Pass Through
        # =====================================
        self.log(
            "Unknown or unhandled value_type '{0}', returning value unchanged (type: {1})".format(
                value_type, type(value).__name__
            ),
            "DEBUG",
        )

        # Exit log with result summary
        result_preview = str(value)[:100] if value is not None else "None"
        if len(str(value)) > 100:
            result_preview += "... (truncated)"

        self.log(
            "Sanitization completed: target_type='{0}', result_type={1}, "
            "value_preview={2}".format(
                value_type, type(value).__name__, result_preview
            ),
            "DEBUG",
        )

        return value


def main():
    pass


if __name__ == "__main__":
    main()
