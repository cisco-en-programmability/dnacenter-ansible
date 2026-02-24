#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright (c) 2026, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

"""Ansible module to generate YAML configurations for Tags Workflow Manager Module."""
from __future__ import absolute_import, division, print_function

__metaclass__ = type
__author__ = "Archit Soni, Madhan Sankaranarayanan"

DOCUMENTATION = r"""
---
module: tags_playbook_config_generator
short_description: Generate YAML configurations playbook for 'tags_workflow_manager' module.
description:
- Generates YAML configurations compatible with the
  'tags_workflow_manager' module.
- Reduces manual effort in creating Ansible playbooks.
- Enables programmatic modifications of infrastructure.
version_added: 6.43.0
extends_documentation_fragment:
- cisco.dnac.workflow_manager_params
author:
- Archit Soni (@koderchit)
- Madhan Sankaranarayanan (@madhansansel)
options:
  state:
    description: The desired state of Cisco Catalyst Center after module execution.
    type: str
    choices: ["gathered"]
    default: gathered
  config:
    description:
    - A list of filters for generating YAML playbook compatible with the `tags_workflow_manager`
      module.
    - Filters specify which components to include in the YAML configuration file.
    - If "components_list" is specified, only those components are included, regardless of the filters.
    type: list
    elements: dict
    required: true
    suboptions:
      generate_all_configurations:
        description:
          - When set to True, automatically generates YAML configurations for all devices and all supported features.
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
          a default file name "tags_playbook_config_<YYYY-MM-DD_HH-MM-SS>.yml".
        - For example, "tags_playbook_config_2026-01-24_12-33-20.yml".
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
            - Valid values are tag and tag_memberships.
            - If specified, only the listed components will be included in the generated YAML file.
            - If not specified, all supported components will be included by default.
            type: list
            elements: str
            choices: ["tag" , "tag_memberships"]
          tag:
            description:
            - Filters specific to tag configuration retrieval.
            - Used to narrow down which tags should be included in the generated YAML file.
            - If no filters are provided, all tags from Cisco Catalyst Center will be retrieved.
            type: list
            elements: dict
            suboptions:
              tag_name:
                description:
                - Name of the tag to filter by.
                - Retrieves the tag with the exact matching name from Cisco Catalyst Center.
                - Example Production, Network-Core, Campus-Switches.
                type: str
          tag_memberships:
            description:
            - Filters specific to tag membership configuration retrieval.
            - Used to specify which tag memberships (device and port associations) should be included.
            - If no filters are provided, all tag memberships from Cisco Catalyst Center will be retrieved.
            type: list
            elements: dict
            suboptions:
              tag_name:
                description:
                - Name of the tag whose memberships should be retrieved.
                - Retrieves all network devices and interfaces (ports) associated with this tag.
                - Example Production, Network-Core, Campus-Switches.
                type: str
              device_identifier:
                description:
                - Specifies the device identifier to use when generating the tag membership configuration.
                - This determines how devices and interfaces are identified in the output YAML file.
                - Applies to both network device and interface (port) tag memberships.
                - If not specified, defaults to serial_number.
                - "hostname: Uses the device hostname as the identifier"
                - "serial_number: Uses the device serial number as the identifier (default)"
                - "mac_address: Uses the device MAC address as the identifier"
                - "ip_address: Uses the device IP address as the identifier"
                type: str
                required: false
                default: serial_number
                choices:
                - hostname
                - serial_number
                - mac_address
                - ip_address
requirements:
- dnacentersdk >= 2.4.5
- python >= 3.9
notes:
- Cisco Catalyst Center >= 2.3.7.9
- |-
  SDK Methods used are
  tags.Tag.get_tag
  tags.Tag.get_tag_members_by_id
- |-
  SDK Paths used are
  /dna/intent/api/v1/tag
  /dna/intent/api/v1/tag/${id}/member
seealso:
- module: cisco.dnac.tags_workflow_manager
  description: Module for managing tags and tag memberships.
"""

EXAMPLES = r"""
# Example 1: Generate all configurations for all tags and tag memberships
- name: Generate complete brownfield tag configuration
  hosts: dnac_servers
  vars_files:
    - credentials.yml
  gather_facts: false
  connection: local
  tasks:
    - name: Generate all tag configurations from Cisco Catalyst Center
      cisco.dnac.tags_playbook_config_generator:
        dnac_host: "{{ dnac_host }}"
        dnac_port: "{{ dnac_port }}"
        dnac_username: "{{ dnac_username }}"
        dnac_password: "{{ dnac_password }}"
        dnac_verify: "{{ dnac_verify }}"
        dnac_debug: "{{ dnac_debug }}"
        dnac_version: "{{ dnac_version }}"
        dnac_log: true
        dnac_log_level: DEBUG
        dnac_log_append: false
        dnac_log_file_path: "{{ dnac_log_file_path }}"
        state: gathered
        config:
          - generate_all_configurations: true

# Example 2: Generate all configurations with custom file path
- name: Generate complete brownfield tag configuration with custom filename
  hosts: dnac_servers
  vars_files:
    - credentials.yml
  gather_facts: false
  connection: local
  tasks:
    - name: Generate all tag configurations to a specific file
      cisco.dnac.tags_playbook_config_generator:
        dnac_host: "{{ dnac_host }}"
        dnac_port: "{{ dnac_port }}"
        dnac_username: "{{ dnac_username }}"
        dnac_password: "{{ dnac_password }}"
        dnac_verify: "{{ dnac_verify }}"
        dnac_debug: "{{ dnac_debug }}"
        dnac_version: "{{ dnac_version }}"
        dnac_log: true
        dnac_log_level: DEBUG
        dnac_log_append: false
        dnac_log_file_path: "{{ dnac_log_file_path }}"
        state: gathered
        config:
          - file_path: "/tmp/complete_tags_config.yaml"
            generate_all_configurations: true

# Example 3: Generate only tag configurations without memberships
- name: Generate tag definitions only
  hosts: dnac_servers
  vars_files:
    - credentials.yml
  gather_facts: false
  connection: local
  tasks:
    - name: Export all tag definitions to YAML file
      cisco.dnac.tags_playbook_config_generator:
        dnac_host: "{{ dnac_host }}"
        dnac_port: "{{ dnac_port }}"
        dnac_username: "{{ dnac_username }}"
        dnac_password: "{{ dnac_password }}"
        dnac_verify: "{{ dnac_verify }}"
        dnac_debug: "{{ dnac_debug }}"
        dnac_version: "{{ dnac_version }}"
        dnac_log: true
        dnac_log_level: DEBUG
        dnac_log_append: false
        dnac_log_file_path: "{{ dnac_log_file_path }}"
        state: gathered
        config:
          - file_path: "/tmp/catc_tags.yaml"
            component_specific_filters:
              components_list: ["tag"]

# Example 4: Generate only tag membership configurations
- name: Generate tag memberships only
  hosts: dnac_servers
  vars_files:
    - credentials.yml
  gather_facts: false
  connection: local
  tasks:
    - name: Export all tag memberships to YAML file
      cisco.dnac.tags_playbook_config_generator:
        dnac_host: "{{ dnac_host }}"
        dnac_port: "{{ dnac_port }}"
        dnac_username: "{{ dnac_username }}"
        dnac_password: "{{ dnac_password }}"
        dnac_verify: "{{ dnac_verify }}"
        dnac_debug: "{{ dnac_debug }}"
        dnac_version: "{{ dnac_version }}"
        dnac_log: true
        dnac_log_level: DEBUG
        dnac_log_append: false
        dnac_log_file_path: "{{ dnac_log_file_path }}"
        state: gathered
        config:
          - file_path: "/tmp/catc_tags.yaml"
            component_specific_filters:
              components_list: ["tag_memberships"]

# Example 5: Generate both tags and memberships together
- name: Generate tags and their memberships
  hosts: dnac_servers
  vars_files:
    - credentials.yml
  gather_facts: false
  connection: local
  tasks:
    - name: Export tags and tag memberships to YAML file
      cisco.dnac.tags_playbook_config_generator:
        dnac_host: "{{ dnac_host }}"
        dnac_port: "{{ dnac_port }}"
        dnac_username: "{{ dnac_username }}"
        dnac_password: "{{ dnac_password }}"
        dnac_verify: "{{ dnac_verify }}"
        dnac_debug: "{{ dnac_debug }}"
        dnac_version: "{{ dnac_version }}"
        dnac_log: true
        dnac_log_level: DEBUG
        dnac_log_append: false
        dnac_log_file_path: "{{ dnac_log_file_path }}"
        state: gathered
        config:
          - file_path: "/tmp/catc_tags.yaml"
            component_specific_filters:
              components_list: ["tag", "tag_memberships"]

# Example 6: Filter specific tags by name
- name: Generate configuration for specific tags by name
  hosts: dnac_servers
  vars_files:
    - credentials.yml
  gather_facts: false
  connection: local
  tasks:
    - name: Export specific tags to YAML file
      cisco.dnac.tags_playbook_config_generator:
        dnac_host: "{{ dnac_host }}"
        dnac_port: "{{ dnac_port }}"
        dnac_username: "{{ dnac_username }}"
        dnac_password: "{{ dnac_password }}"
        dnac_verify: "{{ dnac_verify }}"
        dnac_debug: "{{ dnac_debug }}"
        dnac_version: "{{ dnac_version }}"
        dnac_log: true
        dnac_log_level: DEBUG
        dnac_log_append: false
        dnac_log_file_path: "{{ dnac_log_file_path }}"
        state: gathered
        config:
          - file_path: "/tmp/catc_tags.yaml"
            component_specific_filters:
              components_list: ["tag", "tag_memberships"]
              tag:
                - tag_name: Production
                - tag_name: Data-Center

# Example 7: Filter specific tag memberships by tag name
- name: Generate memberships for specific tags
  hosts: dnac_servers
  vars_files:
    - credentials.yml
  gather_facts: false
  connection: local
  tasks:
    - name: Export memberships for specific tags
      cisco.dnac.tags_playbook_config_generator:
        dnac_host: "{{ dnac_host }}"
        dnac_port: "{{ dnac_port }}"
        dnac_username: "{{ dnac_username }}"
        dnac_password: "{{ dnac_password }}"
        dnac_verify: "{{ dnac_verify }}"
        dnac_debug: "{{ dnac_debug }}"
        dnac_version: "{{ dnac_version }}"
        dnac_log: true
        dnac_log_level: DEBUG
        dnac_log_append: false
        dnac_log_file_path: "{{ dnac_log_file_path }}"
        state: gathered
        config:
          - file_path: "/tmp/catc_tags.yaml"
            component_specific_filters:
              components_list: ["tag", "tag_memberships"]
              tag_memberships:
                - tag_name: Campus-Switches
                - tag_name: Core-Routers

# Example 8: Multiple configurations in a single playbook
- name: Generate multiple tag configuration files
  hosts: dnac_servers
  vars_files:
    - credentials.yml
  gather_facts: false
  connection: local
  tasks:
    - name: Generate multiple brownfield tag configurations
      cisco.dnac.tags_playbook_config_generator:
        dnac_host: "{{ dnac_host }}"
        dnac_port: "{{ dnac_port }}"
        dnac_username: "{{ dnac_username }}"
        dnac_password: "{{ dnac_password }}"
        dnac_verify: "{{ dnac_verify }}"
        dnac_debug: "{{ dnac_debug }}"
        dnac_version: "{{ dnac_version }}"
        dnac_log: true
        dnac_log_level: DEBUG
        dnac_log_append: false
        dnac_log_file_path: "{{ dnac_log_file_path }}"
        state: gathered
        config:
          - file_path: "/tmp/all_tags.yaml"
            component_specific_filters:
              components_list: ["tag"]
          - file_path: "/tmp/all_memberships.yaml"
            component_specific_filters:
              components_list: ["tag_memberships"]
          - file_path: "/tmp/specific_tags.yaml"
            component_specific_filters:
              components_list: ["tag", "tag_memberships"]
              tag:
                - tag_name: Branch-Office
                - tag_name: Access-Points

# Example 9: Retrieve all tag memberships with hostname as device identifier
- name: Generate all tag memberships using hostname identifier
  hosts: dnac_servers
  vars_files:
    - credentials.yml
  gather_facts: false
  connection: local
  tasks:
    - name: Export all tag memberships with hostnames
      cisco.dnac.tags_playbook_config_generator:
        dnac_host: "{{ dnac_host }}"
        dnac_port: "{{ dnac_port }}"
        dnac_username: "{{ dnac_username }}"
        dnac_password: "{{ dnac_password }}"
        dnac_verify: "{{ dnac_verify }}"
        dnac_debug: "{{ dnac_debug }}"
        dnac_version: "{{ dnac_version }}"
        dnac_log: true
        dnac_log_level: DEBUG
        dnac_log_append: false
        dnac_log_file_path: "{{ dnac_log_file_path }}"
        state: gathered
        config:
          - file_path: "/tmp/tags_by_hostname.yaml"
            component_specific_filters:
              components_list: ["tag_memberships"]
              tag_memberships:
                - device_identifier: hostname
      # This will retrieve all tags with their members identified by hostname instead of serial_number

# Example 10: Retrieve specific tag membership with IP address as device identifier
- name: Generate specific tag membership using IP address identifier
  hosts: dnac_servers
  vars_files:
    - credentials.yml
  gather_facts: false
  connection: local
  tasks:
    - name: Export specific tag membership with IP addresses
      cisco.dnac.tags_playbook_config_generator:
        dnac_host: "{{ dnac_host }}"
        dnac_port: "{{ dnac_port }}"
        dnac_username: "{{ dnac_username }}"
        dnac_password: "{{ dnac_password }}"
        dnac_verify: "{{ dnac_verify }}"
        dnac_debug: "{{ dnac_debug }}"
        dnac_version: "{{ dnac_version }}"
        dnac_log: true
        dnac_log_level: DEBUG
        dnac_log_append: false
        dnac_log_file_path: "{{ dnac_log_file_path }}"
        state: gathered
        config:
          - file_path: "/tmp/production_tag_by_ip.yaml"
            component_specific_filters:
              components_list: ["tag_memberships"]
              tag_memberships:
                - tag_name: Production
                  device_identifier: ip_address
      # This will retrieve only the 'Production' tag's members with IP addresses

# Example 11: Retrieve tag memberships with MAC address as device identifier
- name: Generate tag memberships using MAC address identifier
  hosts: dnac_servers
  vars_files:
    - credentials.yml
  gather_facts: false
  connection: local
  tasks:
    - name: Export tag memberships with MAC addresses
      cisco.dnac.tags_playbook_config_generator:
        dnac_host: "{{ dnac_host }}"
        dnac_port: "{{ dnac_port }}"
        dnac_username: "{{ dnac_username }}"
        dnac_password: "{{ dnac_password }}"
        dnac_verify: "{{ dnac_verify }}"
        dnac_debug: "{{ dnac_debug }}"
        dnac_version: "{{ dnac_version }}"
        dnac_log: true
        dnac_log_level: DEBUG
        dnac_log_append: false
        dnac_log_file_path: "{{ dnac_log_file_path }}"
        state: gathered
        config:
          - file_path: "/tmp/tags_by_mac.yaml"
            component_specific_filters:
              components_list: ["tag_memberships"]
              tag_memberships:
                - tag_name: Campus-Switches
                  device_identifier: mac_address
                - tag_name: Core-Routers
                  device_identifier: mac_address
      # This will retrieve specific tags' members with MAC addresses

# Example 12: Retrieve tag memberships with default device identifier (serial_number)
- name: Generate tag memberships with default serial number identifier
  hosts: dnac_servers
  vars_files:
    - credentials.yml
  gather_facts: false
  connection: local
  tasks:
    - name: Export tag memberships with serial numbers (default)
      cisco.dnac.tags_playbook_config_generator:
        dnac_host: "{{ dnac_host }}"
        dnac_port: "{{ dnac_port }}"
        dnac_username: "{{ dnac_username }}"
        dnac_password: "{{ dnac_password }}"
        dnac_verify: "{{ dnac_verify }}"
        dnac_debug: "{{ dnac_debug }}"
        dnac_version: "{{ dnac_version }}"
        dnac_log: true
        dnac_log_level: DEBUG
        dnac_log_append: false
        dnac_log_file_path: "{{ dnac_log_file_path }}"
        state: gathered
        config:
          - file_path: "/tmp/tags_by_serial.yaml"
            component_specific_filters:
              components_list: ["tag_memberships"]
              tag_memberships:
                - tag_name: Data-Center
      # When device_identifier is not specified, it defaults to 'serial_number'

# Example 13: Mixed configuration with different device identifiers
- name: Generate tag configurations with mixed device identifiers
  hosts: dnac_servers
  vars_files:
    - credentials.yml
  gather_facts: false
  connection: local
  tasks:
    - name: Export tags with various device identifier formats
      cisco.dnac.tags_playbook_config_generator:
        dnac_host: "{{ dnac_host }}"
        dnac_port: "{{ dnac_port }}"
        dnac_username: "{{ dnac_username }}"
        dnac_password: "{{ dnac_password }}"
        dnac_verify: "{{ dnac_verify }}"
        dnac_debug: "{{ dnac_debug }}"
        dnac_version: "{{ dnac_version }}"
        dnac_log: true
        dnac_log_level: DEBUG
        dnac_log_append: false
        dnac_log_file_path: "{{ dnac_log_file_path }}"
        state: gathered
        config:
          - file_path: "/tmp/mixed_identifiers.yaml"
            component_specific_filters:
              components_list: ["tag_memberships"]
              tag_memberships:
                - tag_name: Production
                  device_identifier: hostname
                - tag_name: Development
                  device_identifier: ip_address
                - tag_name: Testing
                  device_identifier: mac_address
                - tag_name: Staging
      # Different tags can use different device identifiers in the same configuration
"""

RETURN = r"""
# Case_1: Success Scenario
response_1:
  description:
  - Response returned by Cisco Catalyst Center Python SDK.
  returned: always
  type: dict
  sample:
    response:
      response: "YAML configuration successfully generated"
      version: "1.0"
    msg: "YAML config generation Task succeeded for module
      'tags_workflow_manager'"

# Case_2: Error Scenario
response_2:
  description:
  - Error message when generation fails.
  returned: on failure
  type: dict
  sample:
    response: []
    msg: "YAML config generation Task failed for module
      'tags_workflow_manager': Invalid file path"
"""

from ansible.module_utils.basic import AnsibleModule
from ansible_collections.cisco.dnac.plugins.module_utils.brownfield_helper import (
    BrownFieldHelper,
)
from ansible_collections.cisco.dnac.plugins.module_utils.dnac import (
    DnacBase,
)
from ansible_collections.cisco.dnac.plugins.module_utils.validation import (
    validate_list_of_dicts,
)
from collections import defaultdict
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


class TagsPlaybookGenerator(DnacBase, BrownFieldHelper):
    """
    A class for generator playbook files for infrastructure deployed within the Cisco Catalyst Center using the GET APIs.
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
        self.module_schema = self.get_workflow_filters_schema()
        self.site_id_name_dict = self.get_site_id_name_mapping()
        self.module_name = "tags_workflow_manager"
        self.tag_name_to_details_mapping, self.tag_id_to_tag_name_mapping = (
            self.get_tag_name_to_details_mapping()
        )

    def get_tag_name_to_details_mapping(self):
        """
        Generates a mapping of tag names to their complete details and tag IDs to names.

        Returns:
            tuple: (tag_name_to_details, tag_id_to_name)
                - tag_name_to_details (dict): Maps tag names to their full details.
                - tag_id_to_name (dict): Maps tag IDs to tag names.
        """
        self.log(
            "Starting generation of tag name to details mapping and tag ID to name mapping.",
            "DEBUG",
        )

        api_family = "tag"
        api_function = "get_tag"
        params = {}

        self.log(
            f"Executing API call with family='{api_family}', function='{api_function}', params={params}",
            "DEBUG",
        )

        tag_details = self.execute_get_with_pagination(api_family, api_function, params)

        self.log(
            f"Retrieved {len(tag_details) if tag_details else 0} tag(s) from API response.",
            "INFO",
        )

        tag_name_to_details = {}
        tag_id_to_name = {}

        for index, tag in enumerate(tag_details, start=1):
            tag_name = tag.get("name")
            tag_id = tag.get("id")

            self.log(
                f"Processing tag {index}/{len(tag_details)}: name='{tag_name}', id='{tag_id}'",
                "DEBUG",
            )

            if not tag_name or not tag_id:
                self.log(
                    f"Skipping tag at index {index} due to missing name or id. Tag data: {self.pprint(tag)}",
                    "WARNING",
                )
                continue

            tag_name_to_details[tag_name] = tag
            self.log(f"Added tag '{tag_name}' to name-to-details mapping.", "DEBUG")

            tag_id_to_name[tag_id] = tag_name
            self.log(
                f"Added tag ID '{tag_id}' -> name '{tag_name}' to ID-to-name mapping.",
                "DEBUG",
            )

        self.log(
            f"Successfully generated tag mappings: {len(tag_name_to_details)} tag(s) in name-to-details map, "
            f"{len(tag_id_to_name)} tag(s) in ID-to-name map.",
            "INFO",
        )

        return tag_name_to_details, tag_id_to_name

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
            "generate_all_configurations": {
                "type": "bool",
                "required": False,
                "default": False,
            },
            "file_path": {"type": "str", "required": False},
            "component_specific_filters": {"type": "dict", "required": False},
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

    def get_workflow_filters_schema(self):
        """
        Retrieves the workflow filters schema for the tags module.

        This method defines and returns a dictionary schema that contains configuration
        for network elements related to tags and tag memberships. The schema includes
        filters, reverse mapping functions, API functions, API families, and getter
        functions for each network element type.

        Parameters:
            self (object): An instance of the TagsPlaybookGenerator class.

        Returns:
            dict: A dictionary containing the workflow filters schema with the following structure:
                - network_elements (dict): Contains configuration for different network element types
                    - tag (dict): Configuration for tag-related operations
                        - filters (list): List of filter parameters (tag_name, tag_id)
                        - reverse_mapping_function (method): Function to map tag specifications
                        - api_function (str): API function name for retrieving tags
                        - api_family (str): API family identifier
                        - get_function_name (method): Method to get tag configuration
                    - tag_memberships (dict): Configuration for tag membership operations
                        - filters (list): List of filter parameters (tag_name, tag_id)
                        - reverse_mapping_function (method): Function to map tag membership specs
                        - api_function (str): API function name for retrieving tag members
                        - api_family (str): API family identifier
                        - get_function_name (method): Method to get tag membership configuration

        Description:
            The method constructs a schema dictionary that defines how tag and tag membership
            data should be processed. It logs the schema generation process and the number of
            network elements included in the schema.
        """
        self.log("Retrieving workflow filters schema for tags module.", "DEBUG")

        schema = {
            "network_elements": {
                "tag": {
                    "filters": ["tag_name", "tag_id"],
                    "reverse_mapping_function": self.tag_temp_spec,
                    "api_function": "get_tag",
                    "api_family": "tag",
                    "get_function_name": self.get_tag_configuration,
                },
                "tag_memberships": {
                    "filters": ["tag_name", "tag_id", "device_identifier"],
                    "reverse_mapping_function": self.tag_memberships_temp_spec,
                    "api_function": "get_tag_members_by_id",
                    "api_family": "tag",
                    "get_function_name": self.get_tag_membership_configuration,
                },
            },
        }

        network_elements = list(schema["network_elements"].keys())
        self.log(
            f"Workflow filters schema generated successfully with {len(network_elements)} network elements: {network_elements}",
            "INFO",
        )

        return schema

    def fetch_tag_memberships_for_all_tags(
        self, api_family, api_function, device_identifier="serial_number"
    ):
        """
        Fetches tag membership details for all tags in the cached mapping.

        This method iterates through all tags stored in the tag_name_to_details_mapping
        and retrieves both network device and interface members for each tag using the
        specified API family and function.

        Args:
            api_family (str): The API family name (e.g., "tag").
            api_function (str): The API function name (e.g., "get_tag_members_by_id").
            device_identifier (str): The device identifier type (default: "serial_number").
                Used to specify how devices should be identified in the output.

        Returns:
            list: A list of dictionaries containing tag membership details. Each dictionary contains:
                - tag_id (str): The ID of the tag.
                - tag_name (str): The name of the tag.
                - network_device_members (list): List of network device members.
                - interface_members (list): List of interface members.
                - device_identifier (str): The device identifier type used.
                Tags without any members are excluded from the returned list.
        """
        self.log(
            f"Starting to process '{len(self.tag_name_to_details_mapping)}' tags (from cache) to retrieve their tag memberships.",
            "INFO",
        )

        all_tag_memberships_config = []
        # Use cached tag details instead of making an API call
        for tag_index, (tag_name, tag_details) in enumerate(
            self.tag_name_to_details_mapping.items(), start=1
        ):
            self.log(
                f"Processing tag {tag_index}/{len(self.tag_name_to_details_mapping)}: '{tag_name}'",
                "DEBUG",
            )
            tag_id = tag_details.get("id")
            self.log(
                f"Retrieved tag_id: '{tag_id}' for tag: '{tag_name}'",
                "DEBUG",
            )
            params = {"id": tag_id, "member_association_type": "STATIC"}
            self.log(
                f"Setting member_association_type to 'STATIC' for tag: '{tag_name}' (ID: '{tag_id}')",
                "DEBUG",
            )

            # Execute API call to retrieve network device membership details
            self.log(
                f"Preparing to retrieve network device members for tag '{tag_name}' (ID: '{tag_id}')",
                "DEBUG",
            )
            params["member_type"] = "networkdevice"
            self.log(
                f"Executing API call with params: {params}",
                "DEBUG",
            )

            network_device_members = self.execute_get_with_pagination(
                api_family, api_function, params
            )
            self.log(
                f"Network device members retrieved for tag '{tag_name}': {len(network_device_members) if network_device_members else 0} member(s) found",
                "INFO",
            )
            self.log(
                f"Network device members details: {self.pprint(network_device_members)}",
                "DEBUG",
            )

            # Execute API call to retrieve interface membership details
            self.log(
                f"Preparing to retrieve interface members for tag '{tag_name}' (ID: '{tag_id}')",
                "DEBUG",
            )
            params["member_type"] = "interface"
            self.log(
                f"Executing API call with params: {params}",
                "DEBUG",
            )

            interface_members = self.execute_get_with_pagination(
                api_family, api_function, params
            )
            self.log(
                f"Interface members retrieved for tag '{tag_name}': {len(interface_members) if interface_members else 0} member(s) found",
                "INFO",
            )
            self.log(
                f"Interface members details: {self.pprint(interface_members)}",
                "DEBUG",
            )

            # Combine members for this tag
            tag_membership_details = {
                "tag_id": tag_id,
                "tag_name": tag_name,
                "network_device_members": network_device_members,
                "interface_members": interface_members,
                "device_identifier": device_identifier,
            }

            if not network_device_members and not interface_members:
                self.log(
                    f"No members found for tag '{tag_name}'. Skipping addition to final memberships.",
                    "INFO",
                )
                continue

            all_tag_memberships_config.append(tag_membership_details)
            self.log(
                f"Successfully added membership details for tag '{tag_name}'. "
                f"Total members: {len(network_device_members) if network_device_members else 0} device(s), "
                f"{len(interface_members) if interface_members else 0} interface(s)",
                "INFO",
            )

        self.log(
            f"Completed processing all tags. Found {len(all_tag_memberships_config)} tag(s) with memberships out of "
            f"{len(self.tag_name_to_details_mapping)} total tag(s).",
            "INFO",
        )
        return all_tag_memberships_config

    def fetch_tag_memberships_for_single_tag(
        self,
        tag_name,
        tag_id,
        api_family,
        api_function,
        device_identifier="serial_number",
    ):
        """
        Fetches tag membership details for a single tag.

        Args:
            tag_name (str): The name of the tag.
            tag_id (str): The ID of the tag.
            api_family (str): The API family name.
            api_function (str): The API function name.
            device_identifier (str): The device identifier type (default: "serial_number").

        Returns:
            dict or None: Tag membership details if members are found, None otherwise.
        """
        self.log(
            f"Fetching memberships for tag '{tag_name}' (ID: '{tag_id}') with device_identifier '{device_identifier}'",
            "DEBUG",
        )

        params = {"id": tag_id, "member_association_type": "STATIC"}
        self.log(
            f"Setting member_association_type to 'STATIC' for tag: '{tag_name}' (ID: '{tag_id}')",
            "DEBUG",
        )

        # Execute API call to retrieve network device membership details
        self.log(
            f"Preparing to retrieve network device members for tag '{tag_name}' (ID: '{tag_id}')",
            "DEBUG",
        )
        params["member_type"] = "networkdevice"
        self.log(
            f"Executing API call with params: {params}",
            "DEBUG",
        )

        network_device_members = self.execute_get_with_pagination(
            api_family, api_function, params
        )
        self.log(
            f"Network device members retrieved for tag '{tag_name}': {len(network_device_members) if network_device_members else 0} "
            "member(s) found",
            "INFO",
        )
        self.log(
            f"Network device members details: {self.pprint(network_device_members)}",
            "DEBUG",
        )

        # Execute API call to retrieve interface membership details
        self.log(
            f"Preparing to retrieve interface members for tag '{tag_name}' (ID: '{tag_id}')",
            "DEBUG",
        )

        params["member_type"] = "interface"
        self.log(
            f"Executing API call with params: {params}",
            "DEBUG",
        )

        interface_members = self.execute_get_with_pagination(
            api_family, api_function, params
        )

        self.log(
            f"Interface members retrieved for tag '{tag_name}': {len(interface_members) if interface_members else 0} member(s) found",
            "INFO",
        )
        self.log(
            f"Interface members details: {self.pprint(interface_members)}",
            "DEBUG",
        )

        # Combine members for this tag
        tag_membership_details = {
            "tag_id": tag_id,
            "tag_name": tag_name,
            "network_device_members": network_device_members,
            "interface_members": interface_members,
            "device_identifier": device_identifier,
        }

        if not network_device_members and not interface_members:
            self.log(
                f"No members found for tag '{tag_name}'.",
                "INFO",
            )
            return None

        self.log(
            f"Successfully retrieved membership details for tag '{tag_name}'. "
            f"Total members: {len(network_device_members) if network_device_members else 0} device(s), "
            f"{len(interface_members) if interface_members else 0} interface(s)",
            "INFO",
        )
        return tag_membership_details

    def get_tag_membership_configuration(
        self, network_element, component_specific_filters=None
    ):
        """
        Retrieves tag membership configuration from Cisco Catalyst Center.

        This method fetches network device and interface members associated with tags
        based on the provided filters. It processes both component-specific filters
        (tag_name or tag_id) and defaults to retrieving all tags if no filters are provided.

        Args:
            network_element (dict): Dictionary containing API family and function details.
                Expected keys:
                    - "api_family" (str): The API family name (e.g., "tag").
                    - "api_function" (str): The API function name (e.g., "get_tag_members_by_id").
            component_specific_filters (list, optional): List of filter dictionaries to specify
                which tags to query. Each dictionary can contain:
                    - "tag_name" (str): The name of the tag to filter by.
                    - "tag_id" (str): The ID of the tag to filter by.
                If None, all tags from the cached mapping will be processed.

        Returns:
            dict: A dictionary containing modified tag membership details with the following structure:
                {
                    "tag_memberships": [
                        {
                            "tags": [<tag_name>],
                            "device_details": [
                                {
                                    "serial_numbers": [<serial_number>, ...],
                                    "port_names": [<port_name>, ...]  # Optional, only if interface members exist
                                }
                            ]
                        }
                    ]
                }

        Description:
            The method performs the following operations:
            1. Extracts API family and function from the network_element parameter.
            2. Processes component_specific_filters to identify tags by name or ID.
            3. For each identified tag, retrieves both network device and interface members
                using static member association.
            4. If no filters are provided, processes all tags from the cached tag mapping.
            5. Transforms the retrieved data into a playbook-compatible format using
                tag_memberships_temp_spec.
            6. Returns the modified tag membership details.

        Notes:
            - Only STATIC member associations are retrieved.
            - Invalid or non-existent tag names/IDs are logged and skipped.
            - The method uses cached tag mappings (tag_name_to_details_mapping and
                tag_id_to_tag_name_mapping) to avoid redundant API calls.
        """

        self.log(
            f"Starting to retrieve tag membership configuration with network element: {network_element} and "
            f"component-specific filters: {component_specific_filters}",
            "DEBUG",
        )
        # Extract API family and function from network_element
        tag_memberships_config = []
        api_family = network_element.get("api_family")
        api_function = network_element.get("api_function")
        self.log(
            f"Getting tag membership details using API family '{api_family}' and function '{api_function}'",
            "INFO",
        )

        params = {}
        if component_specific_filters:
            self.log(
                f"Processing {len(component_specific_filters)} component-specific filter(s)",
                "DEBUG",
            )
            for filter_index, filter_param in enumerate(
                component_specific_filters, start=1
            ):
                self.log(
                    f"Processing filter {filter_index}/{len(component_specific_filters)}: {filter_param}",
                    "DEBUG",
                )

                device_identifier = "serial_number"  # Default device identifier
                tag_name = None
                tag_id = None

                # Process tag_name
                if "tag_name" in filter_param:
                    value = filter_param["tag_name"]
                    self.log(
                        f"Processing tag_name filter with value: '{value}'",
                        "DEBUG",
                    )
                    if value in self.tag_name_to_details_mapping:
                        tag_id = self.tag_name_to_details_mapping[value].get("id")
                        params["id"] = tag_id
                        tag_name = value
                        self.log(
                            f"Tag name '{value}' found in mapping. Resolved to tag_id: '{tag_id}'",
                            "INFO",
                        )
                    else:
                        self.log(
                            f"Tag with name '{value}' does not exist in Cisco Catalyst Center. Skipping.",
                            "WARNING",
                        )
                        continue

                # Process tag_id
                if "tag_id" in filter_param:
                    value = filter_param["tag_id"]
                    self.log(
                        f"Processing tag_id filter with value: '{value}'",
                        "DEBUG",
                    )
                    if value not in self.tag_id_to_tag_name_mapping:
                        self.log(
                            f"Tag with ID '{value}' does not exist in Cisco Catalyst Center. Skipping.",
                            "WARNING",
                        )
                        continue

                    tag_name = self.tag_id_to_tag_name_mapping[value]
                    params["id"] = value
                    self.log(
                        f"Tag ID '{value}' found in mapping. Resolved to tag_name: '{tag_name}'",
                        "INFO",
                    )

                # Process device_identifier
                if "device_identifier" in filter_param:
                    value = filter_param["device_identifier"]
                    self.log(
                        f"Processing device_identifier filter with value: '{value}'",
                        "DEBUG",
                    )
                    if value not in [
                        "hostname",
                        "serial_number",
                        "mac_address",
                        "ip_address",
                    ]:
                        self.log(
                            f"Invalid device_identifier value: '{value}'. Must be one of 'hostname', 'serial_number', 'mac_address', or 'ip_address'. "
                            f"Skipping this filter.",
                            "WARNING",
                        )
                        continue

                    device_identifier = value
                    self.log(
                        f"Device identifier set to '{value}' for tag membership retrieval.",
                        "INFO",
                    )

                # Check if only device_identifier is provided without specific tag
                if not params.get("id"):
                    # User wants to fetch all tags with the specific device identifier
                    self.log(
                        f"No specific tag ID or name provided. Fetching all tags with device_identifier '{device_identifier}'.",
                        "INFO",
                    )
                    all_memberships = self.fetch_tag_memberships_for_all_tags(
                        api_family, api_function, device_identifier
                    )
                    tag_memberships_config.extend(all_memberships)
                    self.log(
                        f"Added {len(all_memberships)} tag membership(s) to configuration.",
                        "INFO",
                    )
                else:
                    # Fetch membership for a specific tag
                    self.log(
                        f"Fetching membership for specific tag '{tag_name}' (ID: '{tag_id}') with device_identifier '{device_identifier}'.",
                        "INFO",
                    )
                    tag_membership_details = self.fetch_tag_memberships_for_single_tag(
                        tag_name,
                        tag_id,
                        api_family,
                        api_function,
                        device_identifier,
                    )

                    if not tag_membership_details:
                        self.log(
                            f"Skipping tag '{tag_name}' - no memberships found.",
                            "INFO",
                        )
                        continue

                    tag_memberships_config.append(tag_membership_details)
                    self.log(
                        f"Successfully added membership details for tag '{tag_name}' to configuration.",
                        "INFO",
                    )
        else:
            # Use cached tag details instead of making an API call
            self.log(
                "No component-specific filters provided. Processing all tags from cached mapping.",
                "INFO",
            )
            tag_memberships_config = self.fetch_tag_memberships_for_all_tags(
                api_family, api_function
            )

        # Modify Tag Membership details using temp_spec
        tag_memberships_temp_spec = self.tag_memberships_temp_spec()
        tag_memberships_details = self.modify_parameters(
            tag_memberships_temp_spec, tag_memberships_config
        )
        modified_tag_memberships_details = {"tag_memberships": tag_memberships_details}
        self.log(
            f"Modified Tag Membership details: {self.pprint(modified_tag_memberships_details)}",
            "INFO",
        )

        return modified_tag_memberships_details

    def get_tag_configuration(self, network_element, component_specific_filters=None):
        """
        Retrieve and process tag configuration from Cisco Catalyst Center.

        This method fetches tag details either by applying component-specific filters or by retrieving
        all available tags. It uses cached tag mappings to avoid unnecessary API calls and processes
        the tag information according to the tag template specification.

        Args:
            network_element: The network element identifier for which tags are being retrieved.
                            Used primarily for logging purposes.
            component_specific_filters (list of dict, optional): A list of filter dictionaries to
                                                                 narrow down tag selection. Each dictionary
                                                                 can contain:
                                                                 - 'tag_name': Filter by tag name
                                                                 - 'tag_id': Filter by tag ID
                                                                 If None, all cached tags are retrieved.

        Returns:
            dict: A dictionary containing modified tag details with the following structure:
                  {
                      "tag": [list of processed tag detail dictionaries]
                  }
                  Each tag detail is modified according to the tag_temp_spec template.

        Note:
            This method relies on pre-populated instance variables:
            - self.tag_name_to_details_mapping: Maps tag names to their detail dictionaries
            - self.tag_id_to_tag_name_mapping: Maps tag IDs to tag names
            The method uses cached data to minimize API calls to Cisco Catalyst Center.
        """

        self.log(
            "Starting to retrieve tag configuration with network element: {0} and component-specific filters: {1}".format(
                network_element, component_specific_filters
            ),
            "DEBUG",
        )

        final_tags = []

        if component_specific_filters:
            self.log(
                f"Processing {len(component_specific_filters)} component-specific filter(s) for tag configuration.",
                "INFO",
            )

            for filter_index, filter_param in enumerate(
                component_specific_filters, start=1
            ):
                self.log(
                    f"Processing filter {filter_index}/{len(component_specific_filters)}: {filter_param}",
                    "DEBUG",
                )

                for key, value in filter_param.items():
                    self.log(
                        f"Evaluating filter parameter - key: '{key}', value: '{value}'",
                        "DEBUG",
                    )

                    if key == "tag_name":
                        self.log(
                            f"Processing tag_name filter with value: '{value}'",
                            "DEBUG",
                        )

                        if value in self.tag_name_to_details_mapping:
                            tag_details = [self.tag_name_to_details_mapping[value]]
                            self.log(
                                f"Tag name '{value}' found in mapping. Retrieved tag details.",
                                "INFO",
                            )
                        else:
                            self.log(
                                f"Tag with name '{value}' does not exist in Cisco Catalyst Center. Skipping.",
                                "WARNING",
                            )
                            tag_details = []

                    elif key == "tag_id":
                        self.log(
                            f"Processing tag_id filter with value: '{value}'",
                            "DEBUG",
                        )

                        if value in self.tag_id_to_tag_name_mapping:
                            tag_name = self.tag_id_to_tag_name_mapping[value]
                            self.log(
                                f"Tag ID '{value}' found in mapping. Resolved to tag_name: '{tag_name}'",
                                "DEBUG",
                            )

                            if tag_name in self.tag_name_to_details_mapping:
                                tag_details = [
                                    self.tag_name_to_details_mapping[
                                        self.tag_id_to_tag_name_mapping[value]
                                    ]
                                ]
                                self.log(
                                    f"Tag name '{tag_name}' validated in details mapping. Retrieved tag details.",
                                    "INFO",
                                )
                            else:
                                self.log(
                                    f"Tag with ID '{value}', name: '{tag_name}' does not exist in Cisco Catalyst Center. Skipping.",
                                    "WARNING",
                                )
                                tag_details = []
                        else:
                            self.log(
                                f"Tag with ID '{value}' does not exist in Cisco Catalyst Center. Skipping.",
                                "WARNING",
                            )
                            tag_details = []
                    else:
                        self.log(
                            f"Ignoring unsupported filter parameter: {key}",
                            "DEBUG",
                        )
                        tag_details = []

                    if tag_details:
                        self.log(
                            f"Using cached tag details for filter parameter: {key}, value: {value}, details: {self.pprint(tag_details)}",
                            "INFO",
                        )
                        final_tags.extend(tag_details)
                        self.log(
                            f"Extended final_tags list. Current count: {len(final_tags)}",
                            "DEBUG",
                        )
                    else:
                        self.log(
                            f"No tag details to add for filter parameter: {key}, value: {value}",
                            "DEBUG",
                        )
        else:
            # Use cached tag details instead of making an API call
            self.log(
                "No component-specific filters provided. Retrieving all tags from cached mapping.",
                "INFO",
            )
            tag_details = list(self.tag_name_to_details_mapping.values())
            self.log(
                f"Retrieved {len(tag_details)} tag(s) from cached mapping: {self.pprint(tag_details)}",
                "INFO",
            )
            final_tags.extend(tag_details)
            self.log(
                f"Extended final_tags list with all cached tags. Total count: {len(final_tags)}",
                "DEBUG",
            )

        self.log(
            f"Total tags collected for processing: {len(final_tags)}",
            "INFO",
        )

        # Modify tag details using temp_spec
        self.log(
            "Generating tag template specification for parameter modification.",
            "DEBUG",
        )
        tag_temp_spec = self.tag_temp_spec()

        self.log(
            f"Modifying {len(final_tags)} tag(s) using tag_temp_spec.",
            "DEBUG",
        )
        tags_details = self.modify_parameters(tag_temp_spec, final_tags)

        self.log(
            f"Successfully modified {len(tags_details)} tag detail(s).",
            "INFO",
        )

        modified_tags_details = {"tag": tags_details}

        self.log(
            f"Modified Tag details (count: {len(tags_details)}): {self.pprint(modified_tags_details)}",
            "INFO",
        )

        self.log(
            "Completed tag configuration retrieval and processing.",
            "DEBUG",
        )

        return modified_tags_details

    def tag_temp_spec(self):
        """
        Generate a temporary specification dictionary for tag configuration.

        Returns:
            OrderedDict: A structured specification dictionary for tag configurations.
        """
        self.log("Generating temporary specification for tags.", "DEBUG")
        tag = OrderedDict(
            {
                "name": {"type": "str", "source_key": "name"},
                "description": {"type": "str", "source_key": "description"},
                "device_rules": {
                    "type": "dict",
                    "elements": "dict",
                    "special_handling": True,
                    "transform": self.transform_device_rules,
                    "rule_descriptions": {
                        "type": "list",
                        "elements": "dict",
                        "required": True,
                        "rule_name": {"type": "str", "required": True},
                        "search_pattern": {"type": "str", "required": True},
                        "value": {"type": "str", "required": True},
                        "operation": {"type": "str", "default": "ILIKE"},
                    },
                },
                "port_rules": {
                    "type": "dict",
                    "elements": "dict",
                    "special_handling": True,
                    "transform": self.transform_port_rules,
                    "scope_description": {
                        "type": "dict",
                        "elements": "dict",
                        "scope_category": {"type": "str", "required": True},
                        "inherit": {"type": "bool"},
                        "scope_members": {
                            "type": "list",
                            "elements": "str",
                            "required": True,
                        },
                    },
                    "rule_descriptions": {
                        "type": "list",
                        "elements": "dict",
                        "rule_name": {"type": "str", "required": True},
                        "search_pattern": {"type": "str", "required": True},
                        "value": {"type": "str", "required": True},
                        "operation": {"type": "str", "default": "ILIKE"},
                    },
                },
            }
        )
        return tag

    def tag_memberships_temp_spec(self):
        """
        Generate temporary specification for tag memberships configuration.

        Returns:
            OrderedDict: Specification dictionary containing tags and device_details fields
                        with their types, validation rules, and transform functions.
        """
        self.log("Generating temporary specification for tag memberships.", "DEBUG")
        tag_memberships = OrderedDict(
            {
                "tags": {
                    "type": "list",
                    "elements": "str",
                    "required": True,
                    "special_handling": True,
                    "transform": self.transform_tags_details,
                },
                "device_details": {
                    "type": "list",
                    "elements": "dict",
                    "special_handling": True,
                    "transform": self.transform_device_details,
                    "ip_addresses": {"type": "list", "elements": "str"},
                    "hostnames": {"type": "list", "elements": "str"},
                    "mac_addresses": {"type": "list", "elements": "str"},
                    "serial_numbers": {"type": "list", "elements": "str"},
                    "port_names": {"type": "list", "elements": "str"},
                },
            }
        )
        return tag_memberships

    def ungroup_rules_tree_into_list(self, rules):
        """
        Recursively extracts all leaf nodes (base rules) from a nested rule structure.

        Args:
            rules (dict or None): The rule structure, which may contain nested dictionaries.

        Returns:
            list: A list of leaf nodes (base rules).

        Description: Recursively extracts all leaf nodes (base rules) from a nested rule structure.
        """

        if rules is None:
            self.log("Rules input is None. Returning None.", "DEBUG")
            return None

        leaf_nodes = []

        # Check if the current dictionary has 'items' (indicating nested conditions)
        if isinstance(rules, dict) and "items" in rules:
            for item in rules["items"]:
                # Recursively process each item
                leaf_nodes.extend(self.ungroup_rules_tree_into_list(item))
        else:
            # If no 'items', it's a leaf node
            leaf_nodes.append(rules)

        return leaf_nodes

    def format_rule_for_playbook(self, rule):
        """
        Formats a rule from API representation to playbook format by reverse mapping
        selectors and extracting search patterns from the value.

        This method transforms rules retrieved from Cisco Catalyst Center API into a
        playbook-compatible format. It handles reverse mapping of rule names and extracts
        search patterns based on wildcard characters in the value field. Special handling
        is provided for 'speed' rules which include unit conversion (kbps to Mbps).

        Args:
            rule (dict): A dictionary containing API rule details with keys:
            - "operation" (str): The operation to be performed (e.g., "ILIKE").
            - "name" (str): The API name for the rule (e.g., "hostname", "speed", "portName").
            - "value" (str): The value with pattern markers (%, wildcards) indicating search pattern.

        Returns:
            dict: A formatted rule in playbook representation with keys:
            - "rule_name" (str): The playbook-friendly name (e.g., "device_name", "speed", "port_name").
            - "search_pattern" (str): The pattern type - "equals", "contains", "starts_with", or "ends_with".
            - "value" (str): The cleaned value without pattern markers (% symbols removed, speed converted to Mbps).
            - "operation" (str): The operation type from the original rule.

        Description:
            The method performs the following transformations:
            1. Reverse maps API rule names to playbook-friendly names using a predefined mapping
            2. Determines search pattern based on wildcard placement in the value:
               - No wildcards: "equals"
               - Leading and trailing %: "contains"
               - Trailing % only: "starts_with"
               - Leading % only: "ends_with"
            3. Special handling for speed rules:
               - Converts kbps to Mbps by removing "000" suffix
               - Applies pattern detection before unit conversion
            4. Returns a structured dictionary ready for playbook generation

        Example:
            Input: {"name": "hostname", "operation": "ILIKE", "value": "%router%"}
            Output: {"rule_name": "device_name", "search_pattern": "contains",
                "value": "router", "operation": "ILIKE"}
        """

        self.log(
            "Starting reverse rule formatting for rule: {0}".format(self.pprint(rule)),
            "DEBUG",
        )

        operation = rule.get("operation")
        value = rule.get("value")
        name = rule.get("name")

        # Reverse name selector mapping (API names to playbook names)
        reverse_name_selector = {
            # Device rule_names
            "hostname": "device_name",
            "family": "device_family",
            "series": "device_series",
            "managementIpAddress": "ip_address",
            "groupNameHierarchy": "location",
            "softwareVersion": "version",
            # Port rule_names
            "speed": "speed",
            "adminStatus": "admin_status",
            "portName": "port_name",
            "status": "operational_status",
            "description": "description",
        }

        rule_name = reverse_name_selector.get(name, name)

        # Determine search pattern and clean value based on rule_name
        if rule_name == "speed":
            # Speed has special handling with "000" suffix (kbps to Mbps conversion)
            if value.startswith("%") and value.endswith("%000%"):
                search_pattern = "contains"
                cleaned_value = value[1:-5]  # Remove leading % and trailing %000%
            elif value.endswith("%000%"):
                search_pattern = "starts_with"
                cleaned_value = value[:-5]  # Remove trailing %000%
            elif value.startswith("%") and value.endswith("000"):
                search_pattern = "ends_with"
                cleaned_value = value[1:-3]  # Remove leading % and trailing 000
            elif value.endswith("000"):
                search_pattern = "equals"
                cleaned_value = value[:-3]  # Remove trailing 000
            else:
                # Fallback if pattern doesn't match expected format
                search_pattern = "equals"
                cleaned_value = value
        else:
            # Standard pattern handling for non-speed rules
            if value.startswith("%") and value.endswith("%"):
                search_pattern = "contains"
                cleaned_value = value[1:-1]  # Remove leading and trailing %
            elif value.endswith("%"):
                search_pattern = "starts_with"
                cleaned_value = value[:-1]  # Remove trailing %
            elif value.startswith("%"):
                search_pattern = "ends_with"
                cleaned_value = value[1:]  # Remove leading %
            else:
                search_pattern = "equals"
                cleaned_value = value

        formatted_rule = {
            "rule_name": rule_name,
            "search_pattern": search_pattern,
            "value": cleaned_value,
            "operation": operation,
        }

        self.log(
            "Reverse transformed rule: Input={0} → Output={1}".format(
                self.pprint(rule), self.pprint(formatted_rule)
            ),
            "INFO",
        )
        return formatted_rule

    def transform_tags_details(self, tag_membership_details):
        """
        Extract tag name from membership details and return as a list.

        Args:
            tag_membership_details (dict): Dictionary containing tag membership info with 'tag_name' key.

        Returns:
            list: Single-element list containing the tag name.
        """
        return [tag_membership_details.get("tag_name")]

    def transform_device_details(self, tag_membership_details):
        """
        Transforms tag membership details into device details format for playbook generation.

        This method processes network device and interface members from tag membership details
        and organizes them into a structured format suitable for YAML playbook generation.
        Network devices are grouped by serial numbers, and interfaces are mapped to their
        parent devices with associated port names.

        Args:
            tag_membership_details (dict): Dictionary containing tag membership information with keys:
                - "network_device_members" (list): List of network device member dictionaries,
                    each containing "serialNumber" key.
                - "interface_members" (list): List of interface member dictionaries, each containing:
                    - "deviceId" (str): Parent device ID for the interface.
                    - "portName" (str): Name of the port/interface.

        Returns:
            list: A list of device detail dictionaries with the following structure:
                - For network devices without ports:
                    {
                        "serial_numbers": [<serial_number>, ...]
                    }
                - For devices with interfaces:
                    {
                        "serial_numbers": [<serial_number>],
                        "port_names": [<port_name>, ...]
                    }

        Description:
            The method performs the following operations:
            1. Extracts serial numbers from network device members and creates a device entry.
            2. Processes interface members by:
                - Retrieving parent device details using device ID.
                - Building a mapping of device serial numbers to their port names.
                - Creating separate device entries for each device with its associated ports.
            3. Returns an empty list if no members are found.

        Note:
            - If parent device details cannot be retrieved for an interface, the method
            fails immediately with an error message.
            - Network devices without interfaces are listed separately from those with interfaces.
        """
        self.log(
            f"Transforming device details: {self.pprint(tag_membership_details)}",
            "DEBUG",
        )

        # Get device_identifier from tag_membership_details (default to serial_number)
        device_identifier = tag_membership_details.get(
            "device_identifier", "serial_number"
        )
        self.log(
            f"Using device_identifier: '{device_identifier}' for device transformation",
            "INFO",
        )

        # Map device_identifier to API field names and output keys (shared for both device and interface members)
        identifier_mapping = {
            "hostname": {"api_field": "hostname", "output_key": "hostnames"},
            "serial_number": {
                "api_field": "serialNumber",
                "output_key": "serial_numbers",
            },
            "mac_address": {
                "api_field": "macAddress",
                "output_key": "mac_addresses",
            },
            "ip_address": {
                "api_field": "managementIpAddress",
                "output_key": "ip_addresses",
            },
        }

        mapping = identifier_mapping.get(device_identifier)
        if not mapping:
            self.log(
                f"Invalid device_identifier '{device_identifier}'. Defaulting to 'serial_number'.",
                "WARNING",
            )
            mapping = identifier_mapping["serial_number"]

        api_field = mapping["api_field"]
        output_key = mapping["output_key"]

        self.log(
            f"Using API field '{api_field}' to populate output key '{output_key}'",
            "DEBUG",
        )

        device_details = []
        network_device_members = tag_membership_details.get(
            "network_device_members", []
        )
        if not network_device_members:
            self.log(
                "No network device members found in members_details.",
                "DEBUG",
            )
        else:
            self.log(
                f"Network device members found: {self.pprint(network_device_members)}",
                "DEBUG",
            )

            self.log(
                f"Extracting field '{api_field}' from network device members to populate '{output_key}'",
                "DEBUG",
            )

            network_device_identifiers = []

            for index, network_device_member in enumerate(
                network_device_members, start=1
            ):
                identifier_value = network_device_member.get(api_field)
                self.log(
                    f"Processing network device member {index}/{len(network_device_members)}: {api_field}='{identifier_value}'",
                    "DEBUG",
                )
                network_device_identifiers.append(identifier_value)

            self.log(
                f"Collected {len(network_device_identifiers)} network device {output_key}",
                "INFO",
            )
            device_details.append(
                {
                    output_key: network_device_identifiers,
                }
            )

        self.log(self.pprint(device_details), "DEBUG")
        interface_members = tag_membership_details.get("interface_members", [])
        if not interface_members:
            self.log(
                "No interface members found in members_details.",
                "DEBUG",
            )
        else:
            self.log(
                f"Interface members found: {self.pprint(interface_members)}",
                "DEBUG",
            )

            self.log(
                f"Extracting field '{api_field}' from interface members' parent devices to populate '{output_key}'",
                "DEBUG",
            )

            parent_network_device_identifiers = []
            device_to_ports_mapping = defaultdict(list)

            for index, interface_member in enumerate(interface_members, start=1):
                parent_network_device_id = interface_member.get("deviceId")
                port_name = interface_member.get("portName")
                self.log(
                    f"Processing interface member {index}/{len(interface_members)}: device_id='{parent_network_device_id}', port_name='{port_name}'",
                    "DEBUG",
                )

                parent_device_info = self.get_device_details(parent_network_device_id)
                if parent_device_info:
                    parent_identifier_value = parent_device_info.get(api_field)
                    parent_network_device_identifiers.append(parent_identifier_value)
                    self.log(
                        f"Retrieved parent device info for device_id '{parent_network_device_id}': {api_field}='{parent_identifier_value}'",
                        "DEBUG",
                    )
                else:
                    self.msg = f"Unable to retrieve parent device details for device ID: {parent_network_device_id}"
                    self.log(self.msg, "ERROR")
                    self.fail_and_exit(self.msg)

                parent_network_device_identifier = parent_device_info.get(api_field)
                device_to_ports_mapping[parent_network_device_identifier].append(
                    port_name
                )
                self.log(
                    f"Added port '{port_name}' to device '{parent_network_device_identifier}'",
                    "DEBUG",
                )

            self.log(
                f"Built device-to-ports mapping for {len(device_to_ports_mapping)} device(s)",
                "INFO",
            )

            for device_identifier_value, port_names in device_to_ports_mapping.items():
                self.log(
                    f"Creating device entry for {api_field} '{device_identifier_value}' with {len(port_names)} port(s)",
                    "DEBUG",
                )
                device_details.append(
                    {
                        output_key: [device_identifier_value],
                        "port_names": port_names,
                    }
                )

        self.log(
            f"Transformation complete. Generated {len(device_details)} device detail entries",
            "INFO",
        )
        return device_details

    def get_device_details(self, device_id):
        """
        Retrieves device details from Cisco Catalyst Center based on device ID.

        Args:
            device_id (str): The device ID.

        Returns:
            dict or None: Device details if found, otherwise None.
        """
        self.log(
            "Retrieving device details for device_id: {0}".format(device_id), "DEBUG"
        )

        params = {"id": device_id}

        try:
            response = self.dnac._exec(
                family="devices",
                function="get_device_list",
                op_modifies=False,
                params=params,
            )

            self.log(
                "Received API response from 'get_device_list': {0}".format(
                    str(response)
                ),
                "DEBUG",
            )

            device_list = response.get("response")

            if not device_list or not isinstance(device_list, list):
                self.log(
                    "No device found with device_id: '{0}'.".format(device_id),
                    "WARNING",
                )
                return None

            device_details = device_list[0]
            self.log(
                "Successfully retrieved device details: {0}".format(
                    self.pprint(device_details)
                ),
                "INFO",
            )

            return device_details

        except Exception as e:
            self.log(
                "Error retrieving device details for device_id {0}: {1}".format(
                    device_id, str(e)
                ),
                "ERROR",
            )
            return None

    def transform_device_rules(self, tags_details):
        """
        Transforms device-specific dynamic rules from Cisco Catalyst Center format to playbook format.

        This method extracts dynamic rules for network devices from tag details, ungroups nested
        rule structures into individual rules, and formats them for playbook generation. It processes
        only rules with memberType 'networkdevice', ignoring other member types.

        Args:
            tags_details (dict): Dictionary containing tag details from Cisco Catalyst Center with keys:
                - "dynamicRules" (list): List of dynamic rule dictionaries, each containing:
                    - "memberType" (str): Type of member (e.g., "networkdevice", "interface").
                    - "rules" (dict): Nested rule structure with conditions and operations.

        Returns:
            dict or None: A dictionary containing formatted rule descriptions:
                {
                    "rule_descriptions": [
                        {
                            "rule_name": str,        # Playbook-friendly name (e.g., "device_name")
                            "search_pattern": str,   # Pattern type: "equals", "contains", "starts_with", "ends_with"
                            "value": str,            # Cleaned value without pattern markers
                            "operation": str         # Operation type (e.g., "ILIKE")
                        },
                        ...
                    ]
                }
                Returns None if no tags_details, no dynamic rules, or no network device rules found.

        Description:
            The method performs the following operations:
            1. Validates input tags_details and checks for dynamic rules presence.
            2. Iterates through dynamic rules to find network device member types.
            3. Ungroups nested rule structures into flat list of individual rules.
            4. Formats each rule into playbook-compatible format using format_rule_for_playbook.
            5. Returns structured dictionary with all transformed rules or None if no rules found.

        Example:
            Input tags_details with nested rules:
            {
                "dynamicRules": [
                    {
                        "memberType": "networkdevice",
                        "rules": {
                            "items": [
                                {"name": "hostname", "operation": "ILIKE", "value": "%router%"}
                            ]
                        }
                    }
                ]
            }

            Output:
            {
                "rule_descriptions": [
                    {
                        "rule_name": "device_name",
                        "search_pattern": "contains",
                        "value": "router",
                        "operation": "ILIKE"
                    }
                ]
            }
        """
        self.log(
            f"Transforming device rules for tags details: {self.pprint(tags_details)}",
            "DEBUG",
        )

        if not tags_details:
            self.log("tags_details is None or empty. Returning None.", "DEBUG")
            return None

        dynamic_rules_in_ccc = tags_details.get("dynamicRules")
        if not dynamic_rules_in_ccc:
            self.log("No dynamicRules found in tags_details. Returning None.", "DEBUG")
            return None

        self.log(
            f"Found {len(dynamic_rules_in_ccc)} dynamic rule(s) to process.",
            "DEBUG",
        )

        transformed_rule_descriptions = []
        for rule_index, dynamic_rule_in_ccc in enumerate(dynamic_rules_in_ccc, start=1):
            member_type_in_ccc = dynamic_rule_in_ccc.get("memberType")
            self.log(
                f"Processing dynamic rule {rule_index}/{len(dynamic_rules_in_ccc)}: memberType='{member_type_in_ccc}'",
                "DEBUG",
            )

            if member_type_in_ccc == "networkdevice":
                self.log(
                    f"Dynamic rule {rule_index} is for network devices. Processing rules.",
                    "DEBUG",
                )
                rules_in_ccc = dynamic_rule_in_ccc.get("rules")
                ungrouped_rules_in_ccc = self.ungroup_rules_tree_into_list(rules_in_ccc)
                self.log(
                    f"Ungrouped {len(ungrouped_rules_in_ccc) if ungrouped_rules_in_ccc else 0} rule(s) from rule tree.",
                    "DEBUG",
                )

                for ungrouped_rule_index, ungrouped_rule in enumerate(
                    ungrouped_rules_in_ccc, start=1
                ):
                    self.log(
                        f"Processing ungrouped rule {ungrouped_rule_index}/{len(ungrouped_rules_in_ccc)}: {self.pprint(ungrouped_rule)}",
                        "DEBUG",
                    )
                    playbook_format_rule = self.format_rule_for_playbook(ungrouped_rule)
                    transformed_rule_descriptions.append(playbook_format_rule)
                    self.log(
                        f"Added transformed rule to descriptions. Total count: {len(transformed_rule_descriptions)}",
                        "DEBUG",
                    )
            else:
                self.log(
                    f"Skipping dynamic rule {rule_index} with memberType='{member_type_in_ccc}' (not 'networkdevice').",
                    "DEBUG",
                )

        if not transformed_rule_descriptions:
            self.log(
                "No transformed rule descriptions found. Returning None.",
                "INFO",
            )
            return None

        self.log(
            f"Successfully transformed {len(transformed_rule_descriptions)} device rule(s).",
            "INFO",
        )

        return {"rule_descriptions": transformed_rule_descriptions}

    def format_scope_description_for_playbook(self, scope_description):
        """
        Transforms scope description from Cisco Catalyst Center API format to playbook format.

        This method converts scope details from the API representation (with IDs and groupType)
        to a playbook-friendly format (with names and scope_category). It resolves tag IDs to
        tag names and site IDs to site hierarchies, making the configuration human-readable
        and suitable for YAML playbook generation.

        Args:
            scope_description (dict): A dictionary containing scope details from Cisco Catalyst Center API.
                Expected keys:
                    - "groupType" (str): Type of the scope - either "TAG" or "SITE".
                    - "scopeObjectIds" (list): List of scope member IDs (tag IDs or site IDs).
                    - "inherit" (bool, optional): Inheritance flag, primarily used for SITE scopes.

        Returns:
            dict or None: A formatted dictionary containing scope description for playbook with structure:
                {
                    "scope_category": str,      # Either "TAG" or "SITE"
                    "scope_members": list,      # List of resolved names (tag names or site hierarchies)
                    "inherit": bool             # Inheritance flag from input
                }
                Returns None if scope_description is None or empty.

        Description:
            The method performs the following transformations:
            1. Validates input scope_description and returns None if empty.
            2. Extracts groupType, scopeObjectIds, and inherit flag from input.
            3. For TAG scopes:
               - Iterates through each tag ID in scopeObjectIds
               - Resolves tag ID to tag name using cached tag_id_to_tag_name_mapping
               - Fails if any tag ID cannot be resolved
               - Builds list of tag names
            4. For SITE scopes:
               - Iterates through each site ID in scopeObjectIds
               - Looks up site ID in cached site_id_name_dict to get site hierarchy
               - Fails if any site ID cannot be resolved
               - Builds list of site hierarchies
            5. For unsupported groupTypes:
               - Logs a warning and returns empty scope_members list
            6. Constructs formatted dictionary with scope_category, scope_members, and inherit
            7. Returns the formatted scope description for playbook use.

        Example:
            Input scope_description from API:
            {
                "groupType": "TAG",
                "scopeObjectIds": ["tag-uuid-1", "tag-uuid-2"],
                "inherit": False
            }

            Output:
            {
                "scope_category": "TAG",
                "scope_members": ["Production", "Network-Core"],
                "inherit": False
            }
        """

        self.log(
            f"Starting reverse scope description formatting for input: {self.pprint(scope_description)}",
            "DEBUG",
        )
        if not scope_description:
            self.log(
                "scope_description is None or empty. Returning None",
                "INFO",
            )
            return None

        group_type = scope_description.get("groupType")
        scope_object_ids = scope_description.get("scopeObjectIds", [])
        inherit_flag = scope_description.get("inherit")

        self.log(
            f"Extracted scope parameters: groupType='{group_type}', "
            f"scopeObjectIds count={len(scope_object_ids)}, inherit={inherit_flag}",
            "DEBUG",
        )

        scope_members = []

        if group_type == "TAG":
            self.log(
                f"Processing TAG scope with {len(scope_object_ids)} tag ID(s)",
                "INFO",
            )
            for index, tag_id in enumerate(scope_object_ids, start=1):
                self.log(
                    f"Resolving tag {index}/{len(scope_object_ids)}: tag_id='{tag_id}'",
                    "DEBUG",
                )
                tag_name = self.tag_id_to_tag_name_mapping.get(tag_id)
                if tag_name is None:
                    self.msg = (
                        f"Tag ID: {tag_id} could not be resolved to a tag name in Cisco Catalyst Center. "
                        "Please verify the tag exists."
                    )
                    self.log(self.msg, "ERROR")
                    self.fail_and_exit(self.msg)

                scope_members.append(tag_name)
                self.log(
                    f"Successfully resolved tag_id '{tag_id}' to tag_name '{tag_name}'",
                    "DEBUG",
                )

            self.log(
                f"Successfully processed {len(scope_members)} TAG scope member(s)",
                "INFO",
            )
        elif group_type == "SITE":
            self.log(
                f"Processing SITE scope with {len(scope_object_ids)} site ID(s)",
                "INFO",
            )
            for index, site_id in enumerate(scope_object_ids, start=1):
                self.log(
                    f"Resolving site {index}/{len(scope_object_ids)}: site_id='{site_id}'",
                    "DEBUG",
                )
                site_name_hierarchy = self.site_id_name_dict.get(site_id)
                if site_name_hierarchy is None:
                    self.msg = (
                        f"Site ID: {site_id} could not be resolved to a site name in Cisco Catalyst Center. "
                        "Please verify the site exists."
                    )
                    self.log(self.msg, "ERROR")
                    self.fail_and_exit(self.msg)

                scope_members.append(site_name_hierarchy)
                self.log(
                    f"Successfully resolved site_id '{site_id}' to site_name_hierarchy '{site_name_hierarchy}'",
                    "DEBUG",
                )

            self.log(
                f"Successfully processed {len(scope_members)} SITE scope member(s)",
                "INFO",
            )
        else:
            self.log(
                f"Unexpected or unsupported groupType: '{group_type}'. No scope members will be processed.",
                "WARNING",
            )

        formatted_scope_description = {
            "scope_category": group_type,
            "scope_members": scope_members,
            "inherit": inherit_flag,
        }

        self.log(
            f"Reverse formatted Scope Description - Input: {self.pprint(scope_description)} | "
            f"Output: {self.pprint(formatted_scope_description)}",
            "INFO",
        )

        return formatted_scope_description

    def transform_port_rules(self, tags_details):
        """
        Transforms port/interface-specific dynamic rules from Cisco Catalyst Center format to playbook format.

        This method extracts dynamic rules for network interfaces (ports) from tag details, ungroups
        nested rule structures into individual rules, and formats them along with scope descriptions
        for playbook generation. It processes only rules with memberType 'interface', ignoring other
        member types like 'networkdevice'.

        Args:
            tags_details (dict): Dictionary containing tag details from Cisco Catalyst Center with keys:
                - "dynamicRules" (list): List of dynamic rule dictionaries, each containing:
                    - "memberType" (str): Type of member (e.g., "interface", "networkdevice").
                    - "rules" (dict): Nested rule structure with conditions and operations.
                    - "scopeRule" (dict): Scope definition specifying where rules apply.

        Returns:
            dict or None: A dictionary containing formatted rule and scope descriptions:
                {
                    "rule_descriptions": [
                        {
                            "rule_name": str,        # Playbook-friendly name (e.g., "port_name", "speed")
                            "search_pattern": str,   # Pattern type: "equals", "contains", "starts_with", "ends_with"
                            "value": str,            # Cleaned value without pattern markers
                            "operation": str         # Operation type (e.g., "ILIKE")
                        },
                        ...
                    ],
                    "scope_description": {
                        "scope_category": str,       # Either "TAG" or "SITE"
                        "scope_members": list,       # List of resolved scope member names
                        "inherit": bool              # Inheritance flag
                    }
                }
                Returns None if no tags_details, no dynamic rules, no interface rules,
                or if scope description is missing.

        Description:
            The method performs the following operations:
            1. Validates input tags_details and checks for dynamic rules presence.
            2. Iterates through dynamic rules to find interface member types.
            3. For each interface rule:
               - Extracts the nested rules structure
               - Ungroups rules tree into flat list of individual rules
               - Extracts scope rule definition
               - Formats each rule using format_rule_for_playbook
               - Formats scope description using format_scope_description_for_playbook
            4. Returns structured dictionary with transformed rules and scope or None if incomplete.
            5. Skips rules with non-interface memberType.

        Example:
            Input tags_details with nested interface rules:
            {
                "dynamicRules": [
                    {
                        "memberType": "interface",
                        "rules": {
                            "items": [
                                {"name": "portName", "operation": "ILIKE", "value": "%GigabitEthernet%"}
                            ]
                        },
                        "scopeRule": {
                            "groupType": "SITE",
                            "scopeObjectIds": ["site-uuid-1"],
                            "inherit": True
                        }
                    }
                ]
            }

            Output:
            {
                "rule_descriptions": [
                    {
                        "rule_name": "port_name",
                        "search_pattern": "contains",
                        "value": "GigabitEthernet",
                        "operation": "ILIKE"
                    }
                ],
                "scope_description": {
                    "scope_category": "SITE",
                    "scope_members": ["Global/USA/San Jose/Building1"],
                    "inherit": True
                }
            }

        Note:
            - Only processes rules with memberType "interface"
            - Both rule_descriptions and scope_description must be present for a valid return
            - Scope description is transformed from IDs to human-readable names
            - This method is typically used in conjunction with tag_temp_spec for port_rules
        """
        self.log(
            f"Starting transformation of port rules for tags details: {self.pprint(tags_details)}",
            "DEBUG",
        )

        if not tags_details:
            self.log(
                "tags_details is None or empty. Returning None.",
                "DEBUG",
            )
            return None

        if "dynamicRules" not in tags_details:
            self.log(
                "'dynamicRules' key not found in tags_details. Returning None.",
                "DEBUG",
            )
            return None

        dynamic_rules_in_ccc = tags_details.get("dynamicRules")
        if not dynamic_rules_in_ccc:
            self.log(
                "No dynamicRules found in tags_details (empty or None). Returning None.",
                "DEBUG",
            )
            return None

        self.log(
            f"Found {len(dynamic_rules_in_ccc)} dynamic rule(s) to process for port rules.",
            "INFO",
        )

        transformed_rule_descriptions = []
        transformed_scope_description = {}

        for rule_index, dynamic_rule_in_ccc in enumerate(dynamic_rules_in_ccc, start=1):
            member_type_in_ccc = dynamic_rule_in_ccc.get("memberType")
            self.log(
                f"Processing dynamic rule {rule_index}/{len(dynamic_rules_in_ccc)}: memberType='{member_type_in_ccc}'",
                "DEBUG",
            )

            if member_type_in_ccc == "interface":
                self.log(
                    f"Dynamic rule {rule_index} is for interfaces (ports). Processing rules.",
                    "DEBUG",
                )

                rules_in_ccc = dynamic_rule_in_ccc.get("rules")
                self.log(
                    f"Extracting rules structure from dynamic rule {rule_index}",
                    "DEBUG",
                )

                ungrouped_rules_in_ccc = self.ungroup_rules_tree_into_list(rules_in_ccc)
                self.log(
                    f"Ungrouped {len(ungrouped_rules_in_ccc) if ungrouped_rules_in_ccc else 0} rule(s) from rule tree for interface rules.",
                    "INFO",
                )

                scope_description_in_ccc = dynamic_rule_in_ccc.get("scopeRule")
                self.log(
                    f"Extracted scope rule from dynamic rule {rule_index}: {self.pprint(scope_description_in_ccc)}",
                    "DEBUG",
                )

                if ungrouped_rules_in_ccc:
                    for ungrouped_rule_index, ungrouped_rule in enumerate(
                        ungrouped_rules_in_ccc, start=1
                    ):
                        self.log(
                            f"Processing ungrouped port rule {ungrouped_rule_index}/{len(ungrouped_rules_in_ccc)}: {self.pprint(ungrouped_rule)}",
                            "DEBUG",
                        )
                        playbook_format_rule = self.format_rule_for_playbook(
                            ungrouped_rule
                        )
                        transformed_rule_descriptions.append(playbook_format_rule)
                        self.log(
                            f"Added transformed port rule to descriptions. Total count: {len(transformed_rule_descriptions)}",
                            "DEBUG",
                        )
                else:
                    self.log(
                        f"No ungrouped rules found for dynamic rule {rule_index}",
                        "WARNING",
                    )

                self.log(
                    f"Transforming scope description for dynamic rule {rule_index}",
                    "DEBUG",
                )
                transformed_scope_description = (
                    self.format_scope_description_for_playbook(scope_description_in_ccc)
                )

                if transformed_scope_description:
                    self.log(
                        f"Successfully transformed scope description: {self.pprint(transformed_scope_description)}",
                        "INFO",
                    )
                else:
                    self.log(
                        f"Scope description transformation returned None for dynamic rule {rule_index}",
                        "WARNING",
                    )
            else:
                self.log(
                    f"Skipping dynamic rule {rule_index} with memberType='{member_type_in_ccc}' (not 'interface')",
                    "DEBUG",
                )

        if not transformed_rule_descriptions or not transformed_scope_description:
            self.log(
                f"Port rules transformation incomplete. "
                f"Rule descriptions: {len(transformed_rule_descriptions) if transformed_rule_descriptions else 0}, "
                f"Scope description: {'present' if transformed_scope_description else 'missing'}. Returning None.",
                "INFO",
            )
            return None

        result = {
            "rule_descriptions": transformed_rule_descriptions,
            "scope_description": transformed_scope_description,
        }

        self.log(
            f"Successfully transformed {len(transformed_rule_descriptions)} port rule(s) with scope description. "
            f"Returning result: {self.pprint(result)}",
            "INFO",
        )

        return result

    def yaml_config_generator(self, yaml_config_generator):
        """
        Generates a YAML configuration file based on the provided parameters.
        This function retrieves network element details using global and component-specific filters, processes the data,
        and writes the YAML content to a specified file. It dynamically handles multiple network elements and their respective filters.

        Args:
            yaml_config_generator (dict): Contains file_path, and component_specific_filters.

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
            if yaml_config_generator.get("component_specific_filters"):
                self.log(
                    "Warning: component_specific_filters provided but will be ignored due to generate_all_configurations=True",
                    "WARNING",
                )

            # Set empty filters to retrieve everything
            component_specific_filters = {}
        else:
            # Checking if generate_all_configurations is False but filters are missing or empty, and logging a warning
            if (
                not yaml_config_generator.get("component_specific_filters")
                and "generate_all_configurations" in yaml_config_generator
                and not yaml_config_generator["generate_all_configurations"]
            ):
                self.msg = (
                    "component_specific_filters must be provided with components_list key "
                    "when generate_all_configurations is set to False."
                )
                self.log(self.msg, "ERROR")
                self.fail_and_exit(self.msg)

            # Use provided filters or default to empty
            component_specific_filters = (
                yaml_config_generator.get("component_specific_filters") or {}
            )

        # Retrieve the supported network elements for the module
        self.log("Retrieving supported network elements schema for the module", "DEBUG")
        module_supported_network_elements = self.module_schema.get(
            "network_elements", {}
        )
        components_list = component_specific_filters.get(
            "components_list", module_supported_network_elements.keys()
        )
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
                    f"Component {component} not supported by module, skipping processing",
                    "WARNING",
                )
                skipped_count += 1
                continue

            filters = component_specific_filters.get(component, [])
            operation_func = network_element.get("get_function_name")

            if not callable(operation_func):
                self.log(
                    f"No retrieval function defined for component: {component}", "ERROR"
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

            modified_details = [
                {f"{component}": detail} for detail in component_data.get(component, [])
            ]
            self.log(
                "Details retrieved for {0}: {1}".format(component, component_data),
                "DEBUG",
            )
            processed_count += 1
            final_config_list.extend(modified_details)

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

        if self.write_dict_to_yaml(yaml_config_dict, file_path):
            self.msg = (
                f"YAML configuration file generated successfully for module '{self.module_name}'. "
                f"File: {file_path}, "
                f"Components processed: {processed_count}, "
                f"Components skipped: {skipped_count}, "
                f"Configurations count: {len(final_config_list)}"
            )
            self.set_operation_result("success", True, self.msg, "INFO")
            self.log(
                f"YAML configuration generation completed. File: {file_path}, "
                f"Components: {processed_count}/{len(components_list)}, "
                f"Configs: {len(final_config_list)}",
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

    def get_want(self, config, state):
        """
        Creates parameters for API calls based on the specified state.
        This method prepares the parameters required for adding, updating, or deleting
        network configurations such as SSIDs and interfaces in the Cisco Catalyst Center
        based on the desired state. It logs detailed information for each operation.

        Args:
            config (dict): The configuration data for the network elements.
            state (str): The desired state of the network elements ('gathered' or 'deleted').
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
        self.msg = "Successfully collected all parameters from the playbook for Tags operations."
        self.status = "success"
        return self

    def get_diff_gathered(self):
        """
        Executes the gather operations for tag configurations in the Cisco Catalyst Center.
        This method processes YAML configuration generation for tags and their associated rules,
        memberships, and scope definitions. It logs detailed information about each operation,
        updates the result status, and returns a consolidated result.
        """

        start_time = time.time()
        self.log("Starting 'get_diff_gathered' operation.", "DEBUG")
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
            "Completed 'get_diff_gathered' operation in {0:.2f} seconds.".format(
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
        "dnac_api_task_timeout": {"type": "int", "default": 1200},
        "dnac_task_poll_interval": {"type": "int", "default": 2},
        "config": {"required": True, "type": "list", "elements": "dict"},
        "state": {"default": "gathered", "choices": ["gathered"]},
    }

    # Initialize the Ansible module with the provided argument specifications
    module = AnsibleModule(argument_spec=element_spec, supports_check_mode=True)
    # Initialize the NetworkCompliance object with the module
    ccc_tags_playbook_generator = TagsPlaybookGenerator(module)
    if (
        ccc_tags_playbook_generator.compare_dnac_versions(
            ccc_tags_playbook_generator.get_ccc_version(), "2.3.7.9"
        )
        < 0
    ):
        ccc_tags_playbook_generator.msg = (
            "The specified version '{0}' does not support the YAML Playbook generation "
            "for tags_playbook_config_generator Module. Supported versions start from '2.3.7.9' onwards. ".format(
                ccc_tags_playbook_generator.get_ccc_version()
            )
        )
        ccc_tags_playbook_generator.set_operation_result(
            "failed", False, ccc_tags_playbook_generator.msg, "ERROR"
        ).check_return_status()

    # Get the state parameter from the provided parameters
    state = ccc_tags_playbook_generator.params.get("state")

    # Check if the state is valid
    if state not in ccc_tags_playbook_generator.supported_states:
        ccc_tags_playbook_generator.status = "invalid"
        ccc_tags_playbook_generator.msg = "State {0} is invalid".format(state)
        ccc_tags_playbook_generator.check_return_status()

    # Validate the input parameters and check the return statusk
    ccc_tags_playbook_generator.validate_input().check_return_status()
    config = ccc_tags_playbook_generator.validated_config

    # Iterate over the validated configuration parameters
    for config in ccc_tags_playbook_generator.validated_config:
        ccc_tags_playbook_generator.reset_values()
        ccc_tags_playbook_generator.get_want(config, state).check_return_status()
        ccc_tags_playbook_generator.get_diff_state_apply[state]().check_return_status()

    module.exit_json(**ccc_tags_playbook_generator.result)


if __name__ == "__main__":
    main()
