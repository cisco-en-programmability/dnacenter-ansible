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

        self.log("Starting validation of invalid parameters in configuration entries.", "DEBUG")

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

        self.log(f"Processing validation for {len(config_list)} configuration(s).", "DEBUG")
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

        self.log("Completed validation of invalid parameters in configuration entries.", "DEBUG")

    def validate_minimum_requirements(self, config_list):
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

        self.log("Starting validation of minimum requirements for configuration entries.", "DEBUG")

        if not isinstance(config_list, list):
            self.msg = (
                f"Invalid input: Expected a list of configuration entries, "
                f"but got {type(config_list).__name__}."
            )
            self.fail_and_exit(self.msg)

        self.log(f"Processing validation for {len(config_list)} configuration(s).", "DEBUG")

        for idx, config in enumerate(config_list, start=1):
            self.log(f"Validating configuration entry {idx}: {config}", "DEBUG")

            has_generate_all_config_flag = "generate_all_configurations" in config
            generate_all_configurations = config.get("generate_all_configurations", False)
            component_specific_filters = config.get("component_specific_filters")

            if has_generate_all_config_flag and generate_all_configurations:
                self.log(f"Entry {idx}: generate_all_configurations=True, skipping filters check.", "DEBUG")
                continue  # No further validation needed

            if component_specific_filters is None or "components_list" not in component_specific_filters:
                if has_generate_all_config_flag:
                    self.msg = (
                        f"Validation Error in entry {idx}: 'component_specific_filters' must be provided "
                        f"with 'components_list' key when 'generate_all_configurations' is set to False."
                    )
                else:
                    self.msg = (
                        f"Validation Error in entry {idx}: Either 'generate_all_configurations' must be provided as True"
                        f" or 'component_specific_filters' must be provided with 'components_list' key."
                    )
                self.fail_and_exit(self.msg)

            self.log(f"Entry {idx}: Passed minimum requirements validation.", "DEBUG")

        self.log("Completed validation of minimum requirements for configuration entries.", "DEBUG")

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
            self.log("Auto-discovery mode enabled - will process all devices and all features", "INFO")

        self.log("Determining output file path for YAML configuration", "DEBUG")
        file_path = yaml_config_generator.get("file_path")
        if not file_path:
            self.log("No file_path provided by user, generating default filename", "DEBUG")
            file_path = self.generate_filename()
        else:
            self.log("Using user-provided file_path: {0}".format(file_path), "DEBUG")

        self.log("YAML configuration file path determined: {0}".format(file_path), "DEBUG")

        self.log("Initializing filter dictionaries", "DEBUG")
        if generate_all:
            # In generate_all_configurations mode, override any provided filters to ensure we get ALL configurations
            self.log("Auto-discovery mode: Overriding any provided filters to retrieve all devices and all features", "INFO")
            if yaml_config_generator.get("global_filters"):
                self.log("Warning: global_filters provided but will be ignored due to generate_all_configurations=True", "WARNING")
            if yaml_config_generator.get("component_specific_filters"):
                self.log("Warning: component_specific_filters provided but will be ignored due to generate_all_configurations=True", "WARNING")

            # Set empty filters to retrieve everything
            global_filters = {}
            component_specific_filters = {}
        else:
            # Use provided filters or default to empty
            global_filters = yaml_config_generator.get("global_filters") or {}
            component_specific_filters = yaml_config_generator.get("component_specific_filters") or {}

        self.log("Retrieving supported network elements schema for the module", "DEBUG")
        module_supported_network_elements = self.module_schema.get("network_elements", {})

        self.log("Determining components list for processing", "DEBUG")
        components_list = component_specific_filters.get(
            "components_list", list(module_supported_network_elements.keys())
        )

        # If components_list is empty, default to all supported components
        if not components_list:
            self.log("No components specified; processing all supported components.", "DEBUG")
            components_list = list(module_supported_network_elements.keys())

        self.log("Components to process: {0}".format(components_list), "DEBUG")

        self.log("Initializing final configuration list and operation summary tracking", "DEBUG")
        final_config_list = []
        processed_count = 0
        skipped_count = 0

        for component in components_list:
            self.log("Processing component: {0}".format(component), "DEBUG")
            network_element = module_supported_network_elements.get(component)
            if not network_element:
                self.log(
                    "Component {0} not supported by module, skipping processing".format(component),
                    "WARNING",
                )
                skipped_count += 1
                continue

            filters = {
                "global_filters": global_filters,
                "component_specific_filters": component_specific_filters.get(component, [])
            }
            operation_func = network_element.get("get_function_name")
            if not callable(operation_func):
                self.log(
                    "No retrieval function defined for component: {0}".format(component),
                    "ERROR"
                )
                skipped_count += 1
                continue

            component_data = operation_func(network_element, filters)
            # Validate retrieval success
            if not component_data:
                self.log(
                    "No data retrieved for component: {0}".format(component),
                    "DEBUG"
                )
                continue

            self.log(
                "Details retrieved for {0}: {1}".format(component, component_data), "DEBUG"
            )
            processed_count += 1
            final_config_list.append(component_data)

        if not final_config_list:
            self.log(
                "No configurations retrieved. Processed: {0}, Skipped: {1}, Components: {2}".format(
                    processed_count, skipped_count, components_list
                ),
                "WARNING"
            )
            self.msg = {
                "status": "ok",
                "message": (
                    "No configurations found for module '{0}'. Verify filters and component availability. "
                    "Components attempted: {1}".format(self.module_name, components_list)
                ),
                "components_attempted": len(components_list),
                "components_processed": processed_count,
                "components_skipped": skipped_count
            }
            self.set_operation_result("ok", False, self.msg, "INFO")
            return self

        yaml_config_dict = {"config": final_config_list}
        self.log(
            "Final config dictionary created: {0}".format(self.pprint(yaml_config_dict)),
            "DEBUG"
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
                "configurations_count": len(final_config_list)
            }
            self.set_operation_result("success", True, self.msg, "INFO")

            self.log(
                "YAML configuration generation completed. File: {0}, Components: {1}/{2}, Configs: {3}".format(
                    file_path, processed_count, len(components_list), len(final_config_list)
                ),
                "INFO"
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
        filename = "{0}_playbook_{1}.yml".format(self.module_name, timestamp)
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

    def get_site_id_name_mapping(self):
        """
        Retrieves the site name hierarchy for all sites.
        Returns:
            dict: A dictionary mapping site IDs to their name hierarchies.
        Raises:
            Exception: If an error occurs while retrieving the site name hierarchy.
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


def main():
    pass


if __name__ == "__main__":
    main()
