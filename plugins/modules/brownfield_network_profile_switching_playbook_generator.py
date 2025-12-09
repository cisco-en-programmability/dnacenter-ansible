#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright (c) 2024, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

"""Ansible module to generate YAML configurations for Network Profile Switching Module."""
from __future__ import absolute_import, division, print_function

__metaclass__ = type
__author__ = ("A Mohamed Rafeek, Madhan Sankaranarayanan")
DOCUMENTATION = r"""
---
module: brownfield_network_profile_switching_playbook_generator
short_description: Generate YAML configurations playbook for 'brownfield_network_profile_switching_playbook_generator' module.
description:
  - Generates YAML configurations compatible with the 'brownfield_network_profile_switching_playbook_generator'
    module, reducing the effort required to manually create Ansible playbooks and
    enabling programmatic modifications.
version_added: 6.43.0
extends_documentation_fragment:
  - cisco.dnac.workflow_manager_params
author:
  - A Mohamed Rafeek (@mabdulk2)
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
    choices: [gathered]
    default: gathered
  config:
    description:
      - A list of filters for generating YAML playbook compatible with the `brownfield_network_profile_switching_playbook_generator`
        module.
      - Filters specify which components to include in the YAML configuration file.
      - If "components_list" is specified, only those components are included, regardless of the filters.
    type: list
    elements: dict
    required: true
    suboptions:
      generate_all_configurations:
        description:
          - When set to True, automatically generates YAML configurations for all switch profile and all supported features.
          - This mode discovers all managed devices in Cisco Catalyst Center and extracts all supported configurations.
          - When enabled, the config parameter becomes optional and will use default values if not provided.
          - A default filename will be generated automatically if file_path is not specified.
          - This is useful for complete brownfield infrastructure discovery and documentation.
        type: bool
        required: false
        default: false
      file_path:
        description:
        - Path where the YAML configuration file will be saved.
        - If not provided, the file will be saved in the current working directory with
          a default file name  "network_profile_switching_workflow_manager_playbook_<DD_Mon_YYYY_HH_MM_SS_MS>.yml".
        - For example, "network_profile_switching_workflow_manager_playbook_12_Nov_2025_21_43_26_379.yml".
        type: str
      global_filters:
        description:
          - Global filters to apply when generating the YAML configuration file.
          - These filters apply to all components unless overridden by component-specific filters.
          - At least one filter type must be specified to identify target devices.
        type: dict
        required: false
        suboptions:
          profile_name_list:
            description:
              - List of switch profile names to extract configurations from.
              - LOWEST PRIORITY - Only used if neither day_n_templates nor site_names are provided.
              - Switch Profile names must match those registered in Catalyst Center.
              - Case-sensitive and must be exact matches.
              - Example ["Campus_Switch_Profile", "Enterprise_Switch_Profile"]
            type: list
            elements: str
            required: false
          day_n_template_list:
            description:
              - List of day_n_templates assigned to the profile.
              - LOWEST PRIORITY - Only used if neither profile_name_list nor site_list are provided.
              - Case-sensitive and must be exact matches.
              - Example ["Periodic_Config_Audit", "Security_Compliance_Check"]
            type: list
            elements: str
            required: false
          site_list:
            description:
              - List of sites assigned to the profile.
              - LOWEST PRIORITY - Only used if neither profile_name_list nor day_n_template_list are provided.
              - Case-sensitive and must be exact matches.
              - Example ["Global/India/Chennai/Main_Office", "Global/USA/San_Francisco/Regional_HQ"]
            type: list
            elements: str
            required: false
      component_specific_filters:
        description:
        - Filters to specify which components to include in the YAML configuration file.
        - If "components_list" is specified, only those components are included,
          regardless of other filters.
        type: dict
        suboptions:
          components_list:
            description:
            - List of components to include in the YAML configuration file.
            - Valid values are
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
"""

EXAMPLES = r"""
---
- name: Auto-generate YAML Configuration for all Switch Profiles
  cisco.dnac.brownfield_network_profile_switching_playbook_generator:
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
  cisco.dnac.brownfield_network_profile_switching_playbook_generator:
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
  cisco.dnac.brownfield_network_profile_switching_playbook_generator:
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
  cisco.dnac.brownfield_network_profile_switching_playbook_generator:
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
  cisco.dnac.brownfield_network_profile_switching_playbook_generator:
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
  cisco.dnac.brownfield_network_profile_switching_playbook_generator:
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


class NetworkProfileSwitchingGenerator(NetworkProfileFunctions, BrownFieldHelper):
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
        self.module_name = "network_profile_switching_workflow_manager"
        self.module_schema = self.get_workflow_elements_schema()
        self.log("Initialized NetworkProfileSwitchingGenerator class instance.", "DEBUG")
        self.log(self.module_schema, "DEBUG")

        # Initialize generate_all_configurations as class-level parameter
        self.generate_all_configurations = False

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
            "generate_all_configurations": {"type": "bool", "required": False, "default": False},
            "file_path": {"type": "str", "required": False},
            "component_specific_filters": {"type": "dict", "required": False},
            "global_filters": {"type": "dict", "elements": "dict", "required": False},
        }

        # # Import validate_list_of_dicts function here to avoid circular imports
        # from ansible_collections.cisco.dnac.plugins.module_utils.dnac import validate_list_of_dicts

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

    def get_workflow_elements_schema(self):
        """
        Returns the mapping configuration for network switch profile workflow manager.
        Returns:
            dict: A dictionary containing network elements and global filters configuration with validation rules.
        """
        return {
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

    def collect_all_switch_profile_list(self, profile_names=None):
        """
        Get required details for the given profile config from Cisco Catalyst Center

        Parameters:
            profile_names (list) - List of network switch profile names

        Returns:
            self - The current object with Filtered or all profile list
        """
        self.log(
            f"Collecting template and switch profile related information for: {profile_names}",
            "INFO",
        )
        self.have["switch_profile_names"], self.have["switch_profile_list"] = [], []
        offset = 1
        limit = 500

        resync_retry_count = int(self.payload.get("dnac_api_task_timeout"))
        resync_retry_interval = int(self.payload.get("dnac_task_poll_interval"))
        while resync_retry_count > 0:
            profiles = self.get_network_profile("Switching", offset, limit)
            if not profiles:
                self.log(
                    "No data received from API (Offset={0}). Exiting pagination.".format(
                        offset
                    ),
                    "DEBUG",
                )
                break

            self.log(
                "Received {0} profile(s) from API (Offset={1}).".format(
                    len(profiles), offset
                ),
                "DEBUG",
            )
            self.have["switch_profile_list"].extend(profiles)

            if len(profiles) < limit:
                self.log(
                    "Received less than limit ({0}) results, assuming last page. Exiting pagination.".format(
                        limit
                    ),
                    "DEBUG",
                )
                break

            offset += limit  # Increment offset for pagination
            self.log(
                "Incrementing offset to {0} for next API request.".format(offset),
                "DEBUG",
            )

            self.log(
                "Pauses execution for {0} seconds.".format(resync_retry_interval),
                "INFO",
            )
            time.sleep(resync_retry_interval)
            resync_retry_count = resync_retry_count - resync_retry_interval

        if self.have["switch_profile_list"]:
            self.log(
                "Total {0} profile(s) retrieved for 'switch': {1}.".format(
                    len(self.have["switch_profile_list"]),
                    self.pprint(self.have["switch_profile_list"]),
                ),
                "DEBUG",
            )

            # Filter profiles based on provided profile names
            if profile_names:
                filtered_profiles = []
                non_existing_profiles = []
                for profile in profile_names:
                    if self.value_exists(self.have["switch_profile_list"], "name", profile):
                        filtered_profiles.append(profile)
                        self.log(f"Found existing switch profile: {profile}", "DEBUG")
                    else:
                        non_existing_profiles.append(profile)
                        self.log(f"Switch profile not found: {profile}", "WARNING")

                if non_existing_profiles:
                    self.log(
                        f"The following switch profile(s) do not exist in Cisco Catalyst Center: {non_existing_profiles}.",
                        "ERROR",
                    )
                    not_exist_profile = ", ".join(non_existing_profiles)
                    self.fail_and_exit(
                        self.fail_and_exit(f"Switch profile(s) '{not_exist_profile}' does not exist in Cisco Catalyst Center.")
                    )

                if filtered_profiles:
                    self.log(
                        f"Filtered existing switch profile(s): {filtered_profiles}.",
                        "DEBUG",
                    )
                    self.have["switch_profile_names"] = filtered_profiles
            else:
                self.have["switch_profile_names"] = [
                    profile["name"] for profile in self.have["switch_profile_list"]
                ]
                self.log(
                    "No specific profile names provided. Using all retrieved switch profiles: {0}.".format(
                        self.have["switch_profile_names"]
                    ),
                    "DEBUG",
                )
        else:
            self.log("No existing switch profile(s) found.", "WARNING")

        return self

    def collect_site_and_template_details(self, profile_names):
        """
        Get template details based on the profile names from Cisco Catalyst Center

        Parameters:
            profile_names (list) - List of network switch profile names

        Returns:
            self - The current object with templates and site details
            information collection for profile create and update.
        """
        self.log(f"Collecting template name based on the switch profile: {profile_names}", "INFO")

        for each_profile in profile_names:
            profile_id = self.get_value_by_key(
                self.have["switch_profile_list"],
                "name",
                each_profile,
                "id",
            )
            if not profile_id:
                self.log(
                    f"Profile ID not found for switch profile: {each_profile}. Skipping template retrieval.",
                    "WARNING",
                )
                continue

            templates = self.get_templates_for_profile(profile_id)
            if templates:
                template_names = [
                    template.get("name") for template in templates
                ]
                self.have.setdefault("switch_profile_templates", {})[
                    profile_id
                ] = template_names
                self.log(
                    f"Retrieved templates for switch profile '{each_profile}': {template_names}",
                    "DEBUG",
                )
            else:
                self.log(
                    f"No templates found for switch profile: {each_profile}.",
                    "WARNING",
                )

            site_list = self.get_site_lists_for_profile(
                each_profile, profile_id)
            if site_list:
                self.log(
                    "Received Site List: {0} for config: {1}.".format(
                        site_list, each_profile
                    ),
                    "INFO",
                )
                site_id_list = [site.get("id") for site in site_list]
                site_id_name_mapping = self.get_site_id_name_mapping(site_id_list)
                self.log(f"Site ID to Name Mapping: {self.pprint(site_id_name_mapping)} for profile: {each_profile}",
                         "DEBUG")
                self.have.setdefault("switch_profile_sites", {})[
                    profile_id
                ] = site_id_name_mapping
                log_msg = f"Retrieved site list for switch profile '{each_profile}': {site_id_name_mapping}"
                self.log(log_msg, "DEBUG")
            else:
                self.log(
                    f"No sites found for switch profile: {each_profile}.",
                    "WARNING",
                )

        return self

    def process_global_filters(self, global_filters):
        """
        Process global filters for network profile switching.

        Args:
            global_filters (dict): A dictionary containing global filter
            parameters.

        Returns:
            dict: A dictionary containing processed global filter parameters.
        """
        self.log("Processing global filters: {0}".format(global_filters), "DEBUG")
        profile_names = global_filters.get("profile_name_list")
        day_n_templates = global_filters.get("day_n_template_list")
        site_list = global_filters.get("site_list")
        final_list = []

        if profile_names and isinstance(profile_names, list):
            self.log("Filtering switch profiles based on profile_name_list: {0}".format(
                global_filters.get("profile_name_list")), "DEBUG")
            for profile in self.have["switch_profile_names"]:
                each_porfile_config = {}
                each_porfile_config["profile_name"] = profile
                each_porfile_config["day_n_templates"] = []
                each_porfile_config["sites"] = []

                profile_id = self.get_value_by_key(
                    self.have["switch_profile_list"],
                    "name",
                    profile,
                    "id",
                )
                if profile_id:
                    cli_template_details = self.have.get(
                        "switch_profile_templates", {}).get(profile_id)
                    if cli_template_details and isinstance(cli_template_details, list):
                        each_porfile_config["day_n_templates"] = cli_template_details

                    site_details = self.have.get(
                        "switch_profile_sites", {}).get(profile_id)
                    if site_details and isinstance(site_details, dict):
                        each_porfile_config["sites"] = list(site_details.values())

                    final_list.append(each_porfile_config)
                    self.log("Profile configurations collected for switch profile list: {0}".format(
                        final_list), "DEBUG")
        elif day_n_templates and isinstance(day_n_templates, list):
            self.log("Filtering switch profiles based on day_n_template_list: {0}".format(
                global_filters.get("day_n_template_list")), "DEBUG")
            for profile_id, templates in self.have.get("switch_profile_templates", {}).items():
                if any(template in templates for template in day_n_templates):
                    profile_name = self.get_value_by_key(
                        self.have["switch_profile_list"],
                        "id",
                        profile_id,
                        "name",
                    )
                    each_porfile_config = {}
                    each_porfile_config["profile_name"] = profile_name
                    each_porfile_config["day_n_templates"] = templates
                    site_details = self.have.get(
                        "switch_profile_sites", {}).get(profile_id)
                    if site_details and isinstance(site_details, dict):
                        each_porfile_config["sites"] = list(site_details.values())
                    else:
                        each_porfile_config["sites"] = []
                    final_list.append(each_porfile_config)
            self.log("Profile configurations collected for day-n template list: {0}".format(
                final_list), "DEBUG")
        elif site_list and isinstance(site_list, list):
            self.log("Filtering switch profiles based on site_list: {0}".format(
                global_filters.get("site_list")), "DEBUG")
            for profile_id, sites in self.have.get("switch_profile_sites", {}).items():
                if any(site in sites.values() for site in site_list):
                    profile_name = self.get_value_by_key(
                        self.have["switch_profile_list"],
                        "id",
                        profile_id,
                        "name",
                    )
                    each_porfile_config = {}
                    each_porfile_config["profile_name"] = profile_name
                    cli_template_details = self.have.get(
                        "switch_profile_templates", {}).get(profile_id)
                    if cli_template_details and isinstance(cli_template_details, list):
                        each_porfile_config["day_n_templates"] = cli_template_details
                    else:
                        each_porfile_config["day_n_templates"] = []
                    each_porfile_config["sites"] = list(sites.values())
                    final_list.append(each_porfile_config)
            self.log("Profile configurations collected for site list: {0}".format(
                final_list), "DEBUG")
        else:
            self.log("No specific global filters provided, processing all profiles", "DEBUG")

        if not final_list:
            self.log("No profiles matched the provided global filters", "WARNING")
            return None

        return final_list

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
            self.log("Generate all switch profile configurations from Catalyst Center", "INFO")

        self.log("Determining output file path for YAML configuration", "DEBUG")
        file_path = yaml_config_generator.get("file_path")
        if not file_path:
            self.log("No file_path provided by user, generating default filename", "DEBUG")
            file_path = self.generate_filename()
        else:
            self.log("Using user-provided file_path: {0}".format(file_path), "DEBUG")

        self.log("YAML configuration file path determined: {0}".format(file_path), "DEBUG")

        self.log("Initializing filter dictionaries", "DEBUG")
        # Set empty filters to retrieve everything
        global_filters = {}
        final_list = []
        if generate_all:
            self.log("Preparing to collect all configurations for switch profile.",
                     "DEBUG")
            for each_profile_name in self.have.get("switch_profile_names", []):
                each_porfile_config = {}
                each_porfile_config["profile_name"] = each_profile_name
                each_porfile_config["day_n_templates"] = []
                each_porfile_config["sites"] = []

                profile_id = self.get_value_by_key(
                    self.have["switch_profile_list"],
                    "name",
                    each_profile_name,
                    "id",
                )
                if profile_id:
                    cli_template_details = self.have.get(
                        "switch_profile_templates", {}).get(profile_id)
                    if cli_template_details and isinstance(cli_template_details, list):
                        each_porfile_config["day_n_templates"] = cli_template_details

                    site_details = self.have.get(
                        "switch_profile_sites", {}).get(profile_id)
                    if site_details and isinstance(site_details, dict):
                        each_porfile_config["sites"] = list(site_details.values())

                    final_list.append(each_porfile_config)
            self.log("All configurations collected for generate_all_configurations mode: {0}".format(
                final_list), "DEBUG")
        else:
            # we get ALL configurations
            self.log("Overriding any provided filters to retrieve based on global filters", "INFO")
            if yaml_config_generator.get("global_filters"):
                self.log("Warning: global_filters provided but will be ignored due to generate_all_configurations=True", "WARNING")

            # Use provided filters or default to empty
            global_filters = yaml_config_generator.get("global_filters") or {}
            if global_filters:
                final_list = self.process_global_filters(global_filters)

        if not final_list:
            self.msg = "No configurations or components to process for module '{0}'. Verify input filters or configuration.".format(
                self.module_name
            )
            self.set_operation_result("ok", False, self.msg, "INFO")
            return self

        final_dict = {"config": final_list}
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
        This method prepares the parameters required for retrieving and managing
        switch profile configurations such as Day n template and sites list in the Cisco Catalyst Center
        based on the desired state. It logs detailed information for each operation.

        Args:
            config (dict): The configuration data for the network elements.
            state (str): The desired state of the network elements ('gathered').
        """

        self.log(
            "Creating Parameters for API Calls with state: {0}".format(state), "INFO"
        )

        self.validate_params(config)

        want = {}

        # Add yaml_config_generator to want
        want["yaml_config_generator"] = config
        self.log(
            "yaml_config_generator added to want: {0}".format(
                want["yaml_config_generator"]
            ),
            "INFO",
        )

        self.want = want
        self.log("Desired State (want): {0}".format(str(self.want)), "INFO")
        self.msg = "Successfully collected all parameters from the playbook for Network Profile Switching operations."
        self.status = "success"
        return self

    def get_have(self, config):
        """
        Retrieves the current state of network switch profile from the Cisco Catalyst Center.
        This method fetches the existing configurations for switch profiles
        such as Day n template and sites list

        Args:
            config (dict): The configuration data for the network elements.

        Returns:
            object: An instance of the class with updated attributes:
                self.have: A dictionary containing the current state of network switch profiles.
                self.msg: A message describing the retrieval result.
                self.status: The status of the retrieval (either "success" or "failed").
        """
        self.log(
            "Retrieving current state of network switch profiles from Cisco Catalyst Center.",
            "INFO",
        )

        if config and isinstance(config, dict):
            if config.get("generate_all_configurations", False):
                self.log("Collecting all switch profile details", "INFO")
                self.collect_all_switch_profile_list()
                if not self.have.get("switch_profile_names"):
                    self.msg = "No existing switch profiles found in Cisco Catalyst Center."
                    self.status = "success"
                    return self

                self.collect_site_and_template_details(self.have.get("switch_profile_names", []))

            global_filters = config.get("global_filters")
            if global_filters:
                profile_name_list = global_filters.get("profile_name_list", [])
                day_n_template_list = global_filters.get("day_n_template_list", [])
                site_list = global_filters.get("site_list", [])

                if profile_name_list and isinstance(profile_name_list, list):
                    self.log(f"Collecting given switch profile details for {profile_name_list}", "INFO")
                    self.collect_all_switch_profile_list(profile_name_list)
                    self.collect_site_and_template_details(self.have.get("switch_profile_names", []))

                if day_n_template_list and isinstance(day_n_template_list, list):
                    self.log(f"Collecting Template details based on profile: {profile_name_list}", "INFO")
                    self.collect_all_switch_profile_list()
                    self.collect_site_and_template_details(self.have.get("switch_profile_names", []))

                if site_list and isinstance(site_list, list):
                    self.log(f"Collecting Site details based on profile: {profile_name_list}", "INFO")
                    self.collect_all_switch_profile_list()
                    self.collect_site_and_template_details(self.have.get("switch_profile_names", []))

        self.log("Current State (have): {0}".format(self.pprint(self.have)), "INFO")
        self.msg = "Successfully retrieved the details from the system"
        return self

    def get_diff_merged(self):
        """
        Executes the merge operations for various network configurations in the Cisco Catalyst Center.
        This method processes additions and updates for SSIDs, interfaces, power profiles, access point profiles,
        radio frequency profiles, and anchor groups. It logs detailed information about each operation,
        updates the result status, and returns a consolidated result.
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
    # Define the specification for the module"s arguments
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
        "state": {"default": "gathered", "choices": ["gathered"]},
    }

    # Initialize the Ansible module with the provided argument specifications
    module = AnsibleModule(argument_spec=element_spec, supports_check_mode=True)
    # Initialize the NetworkCompliance object with the module
    ccc_network_profile_switching_playbook_generator = NetworkProfileSwitchingGenerator(module)
    if (
        ccc_network_profile_switching_playbook_generator.compare_dnac_versions(
            ccc_network_profile_switching_playbook_generator.get_ccc_version(), "2.3.7.9"
        )
        < 0
    ):
        ccc_network_profile_switching_playbook_generator.msg = (
            "The specified version '{0}' does not support the YAML Playbook generation "
            "for <module_name_caps> Module. Supported versions start from '2.3.7.9' onwards. ".format(
                ccc_network_profile_switching_playbook_generator.get_ccc_version()
            )
        )
        ccc_network_profile_switching_playbook_generator.set_operation_result(
            "failed", False, ccc_network_profile_switching_playbook_generator.msg, "ERROR"
        ).check_return_status()

    # Get the state parameter from the provided parameters
    state = ccc_network_profile_switching_playbook_generator.params.get("state")
    # Check if the state is valid
    if state not in ccc_network_profile_switching_playbook_generator.supported_states:
        ccc_network_profile_switching_playbook_generator.status = "invalid"
        ccc_network_profile_switching_playbook_generator.msg = "State {0} is invalid".format(
            state
        )
        ccc_network_profile_switching_playbook_generator.check_return_status()

    # Validate the input parameters and check the return statusk
    ccc_network_profile_switching_playbook_generator.validate_input().check_return_status()

    # Iterate over the validated configuration parameters
    for config in ccc_network_profile_switching_playbook_generator.validated_config:
        ccc_network_profile_switching_playbook_generator.reset_values()
        ccc_network_profile_switching_playbook_generator.get_want(
            config, state).check_return_status()
        ccc_network_profile_switching_playbook_generator.get_have(
            config).check_return_status()
        ccc_network_profile_switching_playbook_generator.get_diff_state_apply[
            state
        ]().check_return_status()

    module.exit_json(**ccc_network_profile_switching_playbook_generator.result)


if __name__ == "__main__":
    main()
