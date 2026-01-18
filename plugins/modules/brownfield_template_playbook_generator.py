#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright (c) 2026, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

"""Ansible module to generate YAML configurations for Template Module."""
from __future__ import absolute_import, division, print_function

__metaclass__ = type
__author__ = "Sunil Shatagopa, Madhan Sankaranarayanan"

DOCUMENTATION = r"""
---
module: brownfield_template_playbook_generator
short_description: Generate YAML playbook for C(template_workflow_manager) module.
description:
- Generates YAML configurations compatible with the C(template_workflow_manager)
  module, reducing the effort required to manually create Ansible playbooks and
  enabling programmatic modifications.
- The YAML configurations generated represent the template projects and configuration templates
  configured on the Cisco Catalyst Center.
version_added: 6.44.0
extends_documentation_fragment:
- cisco.dnac.workflow_manager_params
author:
- Sunil Shatagopa (@shatagopasunil)
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
    - A list of filters for generating YAML playbook compatible with the `template_workflow_manager` module.
    - Filters specify which components to include in the YAML configuration file.
    - If C(components_list) is specified, only those components are included, regardless of the filters.
    type: list
    elements: dict
    required: true
    suboptions:
      generate_all_configurations:
        description:
        - When set to C(true), the module generates configurations for all templates and projects
          in the Cisco Catalyst Center, ignoring any provided filters.
        - When enabled, the config parameter becomes optional and will use default values if not provided.
        - A default filename will be generated automatically if file_path is not specified.
        - This is useful for complete brownfield infrastructure discovery and documentation.
        - When set to false, the module uses provided filters to generate a targeted YAML configuration.
        - IMPORTANT NOTE - When generate_all_configurations is enabled, it will only retrieve committed templates.
          It does not include uncommitted templates. To include uncommitted templates, set generate_all_configurations to false
          and use the appropriate filters such as include_uncommitted under configuration_templates.
        type: bool
        required: false
        default: false
      file_path:
        description:
        - Path where the YAML configuration file will be saved.
        - If not provided, the file will be saved in the current working directory with
          a default file name  C(<module_name>_playbook_<DD_Mon_YYYY_HH_MM_SS_MS>.yml).
        - For example, C(template_workflow_manager_playbook_22_Apr_2025_21_43_26_379.yml).
        type: str
      component_specific_filters:
        description:
        - Filters to specify which components to include in the YAML configuration
            file.
        - If C(components_list) is specified, only those components are included,
            regardless of other filters.
        type: dict
        suboptions:
          components_list:
            description:
            - List of components to include in the YAML configuration file.
            - Valid values are
              - Template Projects C(projects)
              - Templates C(configuration_templates)
            - For example, ["projects", "configuration_templates"].
            - If not specified, all components are included.
            type: list
            elements: str
          projects:
            description:
            - Template project filters to apply when retrieving template projects.
            type: list
            elements: dict
            suboptions:
              name:
                description:
                - Name of the template project.
                type: str
          configuration_templates:
            description:
            - Configuration template filters to apply when retrieving configuration templates.
            type: list
            elements: dict
            suboptions:
              template_name:
                description:
                - Name of the configuration template.
                type: str
              id:
                description:
                - ID of the configuration template.
                type: str
              project_name:
                description:
                - Name of the project associated with the configuration template.
                type: str
              include_uncommitted:
                description:
                - Whether to include uncommitted templates.
                type: bool
requirements:
- dnacentersdk >= 2.10.10
- python >= 3.9
notes:
- SDK Methods used are
    - configuration_templates.ConfigurationTemplates.get_projects_details
    - configuration_templates.ConfigurationTemplates.get_templates_details
- Paths used are
    - /dna/intent/api/v2/template-programmer/project
    - /dna/intent/api/v2/template-programmer/template
"""

EXAMPLES = r"""
- name: Auto-generate YAML Configuration for all components which
     includes template projects and configuration templates.
  cisco.dnac.brownfield_template_playbook_generator:
    dnac_host: "{{ dnac_host }}"
    dnac_username: "{{ dnac_username }}"
    dnac_password: "{{ dnac_password }}"
    dnac_verify: "{{ dnac_verify }}"
    dnac_port: "{{ dnac_port }}"
    dnac_version: "{{ dnac_version }}"
    dnac_debug: "{{ dnac_debug }}"
    dnac_log: true
    dnac_log_level: "{{ dnac_log_level }}"
    state: gathered
    config:
      - generate_all_configurations: true

- name: Generate YAML Configuration with File Path specified
  cisco.dnac.brownfield_template_playbook_generator:
    dnac_host: "{{ dnac_host }}"
    dnac_username: "{{ dnac_username }}"
    dnac_password: "{{ dnac_password }}"
    dnac_verify: "{{ dnac_verify }}"
    dnac_port: "{{ dnac_port }}"
    dnac_version: "{{ dnac_version }}"
    dnac_debug: "{{ dnac_debug }}"
    dnac_log: true
    dnac_log_level: "{{ dnac_log_level }}"
    state: gathered
    config:
      - file_path: "tmp/catc_templates_config.yml"

- name: Generate YAML Configuration with specific template projects only
  cisco.dnac.brownfield_template_playbook_generator:
    dnac_host: "{{ dnac_host }}"
    dnac_username: "{{ dnac_username }}"
    dnac_password: "{{ dnac_password }}"
    dnac_verify: "{{ dnac_verify }}"
    dnac_port: "{{ dnac_port }}"
    dnac_version: "{{ dnac_version }}"
    dnac_debug: "{{ dnac_debug }}"
    dnac_log: true
    dnac_log_level: "{{ dnac_log_level }}"
    state: gathered
    config:
      - file_path: "tmp/catc_templates_config.yml"
        component_specific_filters:
          components_list: ["projects"]

- name: Generate YAML Configuration with specific configuration templates only
  cisco.dnac.brownfield_template_playbook_generator:
    dnac_host: "{{ dnac_host }}"
    dnac_username: "{{ dnac_username }}"
    dnac_password: "{{ dnac_password }}"
    dnac_verify: "{{ dnac_verify }}"
    dnac_port: "{{ dnac_port }}"
    dnac_version: "{{ dnac_version }}"
    dnac_debug: "{{ dnac_debug }}"
    dnac_log: true
    dnac_log_level: "{{ dnac_log_level }}"
    state: gathered
    config:
      - file_path: "tmp/catc_templates_config.yml"
        component_specific_filters:
          components_list: ["configuration_templates"]

- name: Generate YAML Configuration for projects with project name filter
  cisco.dnac.brownfield_template_playbook_generator:
    dnac_host: "{{ dnac_host }}"
    dnac_username: "{{ dnac_username }}"
    dnac_password: "{{ dnac_password }}"
    dnac_verify: "{{ dnac_verify }}"
    dnac_port: "{{ dnac_port }}"
    dnac_version: "{{ dnac_version }}"
    dnac_debug: "{{ dnac_debug }}"
    dnac_log: true
    dnac_log_level: "{{ dnac_log_level }}"
    state: gathered
    config:
      - file_path: "tmp/catc_templates_config.yml"
        component_specific_filters:
          components_list: ["projects"]
          projects:
            - name: "Project_A"
            - name: "Project_B"

- name: Generate YAML Configuration for templates with template name filter
  cisco.dnac.brownfield_template_playbook_generator:
    dnac_host: "{{ dnac_host }}"
    dnac_username: "{{ dnac_username }}"
    dnac_password: "{{ dnac_password }}"
    dnac_verify: "{{ dnac_verify }}"
    dnac_port: "{{ dnac_port }}"
    dnac_version: "{{ dnac_version }}"
    dnac_debug: "{{ dnac_debug }}"
    dnac_log: true
    dnac_log_level: "{{ dnac_log_level }}"
    state: gathered
    config:
      - file_path: "tmp/catc_templates_config.yml"
        component_specific_filters:
          components_list: ["configuration_templates"]
          configuration_templates:
            - template_name: "Template_1"
            - template_name: "Template_2"

- name: Generate YAML Configuration for templates with project name filter
  cisco.dnac.brownfield_template_playbook_generator:
    dnac_host: "{{ dnac_host }}"
    dnac_username: "{{ dnac_username }}"
    dnac_password: "{{ dnac_password }}"
    dnac_verify: "{{ dnac_verify }}"
    dnac_port: "{{ dnac_port }}"
    dnac_version: "{{ dnac_version }}"
    dnac_debug: "{{ dnac_debug }}"
    dnac_log: true
    dnac_log_level: "{{ dnac_log_level }}"
    state: gathered
    config:
      - file_path: "tmp/catc_templates_config.yml"
        component_specific_filters:
          components_list: ["configuration_templates"]
          configuration_templates:
            - project_name: "Project_A"
            - project_name: "Project_B"

- name: Generate YAML Configuration for templates with uncommitted filter
  cisco.dnac.brownfield_template_playbook_generator:
    dnac_host: "{{ dnac_host }}"
    dnac_username: "{{ dnac_username }}"
    dnac_password: "{{ dnac_password }}"
    dnac_verify: "{{ dnac_verify }}"
    dnac_port: "{{ dnac_port }}"
    dnac_version: "{{ dnac_version }}"
    dnac_debug: "{{ dnac_debug }}"
    dnac_log: true
    dnac_log_level: "{{ dnac_log_level }}"
    state: gathered
    config:
      - file_path: "tmp/catc_templates_config.yml"
        component_specific_filters:
          components_list: ["configuration_templates"]
          configuration_templates:
            - include_uncommitted: true

- name: Generate YAML Configuration for templates with template name and project name
  cisco.dnac.brownfield_template_playbook_generator:
    dnac_host: "{{ dnac_host }}"
    dnac_username: "{{ dnac_username }}"
    dnac_password: "{{ dnac_password }}"
    dnac_verify: "{{ dnac_verify }}"
    dnac_port: "{{ dnac_port }}"
    dnac_version: "{{ dnac_version }}"
    dnac_debug: "{{ dnac_debug }}"
    dnac_log: true
    dnac_log_level: "{{ dnac_log_level }}"
    state: gathered
    config:
      - file_path: "tmp/catc_templates_config.yml"
        component_specific_filters:
          components_list: ["configuration_templates"]
          configuration_templates:
            - project_name: "Project_A"
              template_name: "Template_1"

- name: Generate YAML Configuration for templates with comprehensive filters
  cisco.dnac.brownfield_template_playbook_generator:
    dnac_host: "{{ dnac_host }}"
    dnac_username: "{{ dnac_username }}"
    dnac_password: "{{ dnac_password }}"
    dnac_verify: "{{ dnac_verify }}"
    dnac_port: "{{ dnac_port }}"
    dnac_version: "{{ dnac_version }}"
    dnac_debug: "{{ dnac_debug }}"
    dnac_log: true
    dnac_log_level: "{{ dnac_log_level }}"
    state: gathered
    config:
      - file_path: "tmp/catc_templates_config.yml"
        component_specific_filters:
          components_list: ["configuration_templates"]
          configuration_templates:
            - template_name: "Template_1"
              project_name: "Project_A"
              include_uncommitted: true
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
    DnacBase
)
from ansible_collections.cisco.dnac.plugins.module_utils.validation import (
    validate_list_of_dicts
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

        def str_presenter(self, data):
            if '\n' in data:
                trailing_newlines = len(data) - len(data.rstrip('\n'))
                # PyYAML only preserves one, so we append the extras as literal newlines
                if trailing_newlines > 1:
                    data = data + ('\n' * (trailing_newlines - 1))
                return self.represent_scalar('tag:yaml.org,2002:str', data, style='|')
            return self.represent_scalar('tag:yaml.org,2002:str', data)

    OrderedDumper.add_representer(OrderedDict, OrderedDumper.represent_dict)
    OrderedDumper.add_representer(str, OrderedDumper.str_presenter)
else:
    OrderedDumper = None


class TemplatePlaybookGenerator(DnacBase, BrownFieldHelper):
    """
    A class for generator playbook files for templates deployed within the Cisco Catalyst Center using the GET APIs.
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
        self.module_schema = self.get_workflow_elements_schema()
        self.module_name = "template_workflow_manager"

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
            "component_specific_filters": {"type": "dict", "required": False}
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

    def get_workflow_elements_schema(self):
        """
        Description:
            Constructs and returns a structured mapping for managing template information
            such as configuration_templates and projects. This mapping includes
            associated filters, temporary specification functions, API details, and fetch function references
            used in the template workflow orchestration process.

        Args:
            self: Refers to the instance of the class containing definitions of helper methods like
                `projects_temp_spec`, `templates_temp_spec`, etc.

        Return:
            dict: A dictionary with the following structure:
                - "network_elements": A nested dictionary where each key represents a network component
                (e.g., 'configuration_templates', 'projects') and maps to:
                    - "filters": List of filter keys relevant to the component.
                    - "reverse_mapping_function": Reference to the function that generates temp specs for the component.
                    - "api_function": Name of the API to be called for the component.
                    - "api_family": API family name (e.g., 'configuration_templates').
                    - "get_function_name": Reference to the internal function used to retrieve the component data.
        """

        self.log(
            "Retrieving workflow filters schema for template module.", "DEBUG"
        )

        schema = {
            "network_elements": {
                "projects": {
                    "filters": ["name"],
                    "reverse_mapping_function": self.projects_temp_spec,
                    "api_function": "get_projects_details",
                    "api_family": "configuration_templates",
                    "get_function_name": self.get_template_projects_details
                },
                "configuration_templates": {
                    "filters": [
                        "template_name",
                        "id",
                        "project_name",
                        "include_uncommitted"
                    ],
                    "reverse_mapping_function": self.templates_temp_spec,
                    "api_function": "get_templates_details",
                    "api_family": "configuration_templates",
                    "get_function_name": self.get_template_details
                }
            }
        }

        network_elements = list(schema["network_elements"].keys())
        self.log(
            f"Workflow filters schema generated successfully with {len(network_elements)} network element(s): {network_elements}",
            "INFO",
        )

        return schema

    def transform_device_types(self, template_details):
        """
        Transforms device types information for a given template by extracting and mapping
        the product family, series, and type based on the template details.

        Args:
            template_details (dict): A dictionary containing template-specific information.

        Returns:
            list: A list containing a single dictionary with the following keys:
                - "product_family" (str): Device family type
                - "product_series" (str): Device series type
                - "product_type" (str): Device type
        """

        self.log(
            "Transforming device types for template details: \n{0}".format(self.pprint(template_details)),
            "DEBUG"
        )
        device_types = template_details.get("deviceTypes", [])

        final_device_types = []
        for device_type in device_types:
            final_device_types.append({
                k: v for k, v in {
                    "product_family": device_type.get("productFamily"),
                    "product_series": device_type.get("productSeries"),
                    "product_type": device_type.get("productType")
                }.items() if v is not None
            })

        self.log("Transformed Device Types: {0}".format(final_device_types), "INFO")

        return final_device_types

    def transform_tags(self, template_details):
        """
        Transforms tags information for a given template by extracting and mapping
        the tag id and tag name based on the template details.

        Args:
            template_details (dict): A dictionary containing template-specific information.

        Returns:
            list: A list containing a single dictionary with the following keys:
                - "id" (str): Tag ID
                - "name" (str): Tag Name
        """

        self.log(
            "Transforming tags for template details: \n{0}".format(self.pprint(template_details)),
            "DEBUG"
        )
        tags = template_details.get("tags", [])

        final_tags = []
        for tag in tags:
            final_tags.append({
                k: v for k, v in {
                    "id": tag.get("id"),
                    "name": tag.get("name")
                }.items() if v is not None
            })

        self.log("Transformed Tags: {0}".format(final_tags), "INFO")

        return final_tags

    def transform_template_content(self, template_details):
        """
        Transforms template content for a given template by processing the content
        based on its language type.

        Args:
            template_details (dict): A dictionary containing template-specific information.

        Returns:
            str: The transformed template content, wrapped in Jinja raw tags if the language is JINJA.
        """
        self.log(
            "Transforming template content for template details: \n{0}".format(self.pprint(template_details)),
            "DEBUG"
        )
        template_language = template_details.get("language")
        template_content = template_details.get("templateContent")

        if template_content and template_language == "JINJA":
            # Strip leading/trailing whitespace and ensure exactly one newline at the end
            template_content = f'{{% raw %}}{template_content}{{% endraw %}}'

        self.log("Transformed Template Content: {0}".format(template_content), "INFO")

        return template_content

    def transform_containing_templates(self, template_details):
        """
        Transforms containing templates information for a given template by extracting and mapping
        the relevant attributes based on the template details.

        Args:
            template_details (dict): A dictionary containing template-specific information.

        Returns:
            list: A list of dictionaries, each containing attributes of a containing template.
        """
        self.log(
            "Transforming containing templates for template details: {0}".format(template_details),
            "DEBUG"
        )

        containing_templates = template_details.get("containingTemplates", [])
        containing_templates_temp_spec = self.containing_templates_temp_spec()
        containing_templates_final = self.modify_parameters(
            containing_templates_temp_spec, containing_templates)

        self.log("Transformed Containing Templates: {0}".format(containing_templates_final), "INFO")

        return containing_templates_final

    def containing_templates_temp_spec(self):
        """
        Constructs a temporary specification for containing templates, defining the structure and types of attributes
        that will be used in the YAML configuration file. This specification includes details such as template name,
        template description, project name, composite status, and language attributes.

        Returns:
            OrderedDict: An ordered dictionary defining the structure of containing templates attributes.
        """

        self.log("Generating temporary specification for containing templates.", "DEBUG")
        containing_templates = OrderedDict(
            {
                "name": {"type": "str"},
                "description": {"type": "str"},
                "project_name": {"type": "str", "source_key": "projectName"},
                "composite": {"type": "bool"},
                "language": {"type": "str"}
            }
        )
        return containing_templates

    def projects_temp_spec(self):
        """
        Constructs a temporary specification for template projects, defining the structure and types of attributes
        that will be used in the YAML configuration file. This specification includes details such as project name
        and description attributes.

        Returns:
            OrderedDict: An ordered dictionary defining the structure of template projects attributes.
        """

        self.log("Generating temporary specification for template projects.", "DEBUG")
        template_projects = OrderedDict(
            {
                "name": {"type": "str"},
                "description": {"type": "str"}
            }
        )
        return template_projects

    def templates_temp_spec(self):
        """
        Constructs a temporary specification for templates, defining the structure and types of attributes
        that will be used in the YAML configuration file. This specification includes details such as template name,
        template description, project name, author, language and various other attributes.

        Returns:
            OrderedDict: An ordered dictionary defining the structure of template attributes.
        """

        self.log("Generating temporary specification for templates.", "DEBUG")
        template_details = OrderedDict(
            {
                "template_name": {"type": "str", "source_key": "name"},
                "template_description": {"type": "str", "source_key": "description"},
                "project_name": {"type": "str", "source_key": "projectName"},
                "author": {"type": "str"},
                "language": {"type": "str"},
                "composite": {"type": "bool"},
                "containing_templates": {
                    "type": "list",
                    "element": "dict",
                    "special_handling": True,
                    "transform": self.transform_containing_templates,
                },
                "failure_policy": {"type": "str", "source_key": "failurePolicy"},
                "software_type": {"type": "str", "source_key": "softwareType"},
                "software_version": {"type": "str", "source_key": "softwareVersion"},
                "custom_params_order": {"type": "bool", "source_key": "customParamsOrder"},
                "device_types": {
                    "type": "list",
                    "element": "dict",
                    "special_handling": True,
                    "transform": self.transform_device_types
                },
                "template_content": {
                    "type": "str",
                    "special_handling": True,
                    "transform": self.transform_template_content,
                },
                "template_tag": {
                    "type": "list",
                    "element": "dict",
                    "special_handling": True,
                    "transform": self.transform_tags
                }
            }
        )
        return template_details

    def get_template_projects_details(self, network_element, component_specific_filters=None):
        """
        Retrieves template projects based on the provided network element and component-specific filters.

        Args:
            network_element (dict): A dictionary containing the API family and function for retrieving template projects.
            component_specific_filters (list, optional): A list of dictionaries containing filters for template projects.

        Returns:
            dict: A dictionary containing the modified details of template projects.
        """

        self.log(
            "Starting to retrieve template projects with network element: {0} and component-specific filters: {1}".format(
                network_element, component_specific_filters
            ),
            "DEBUG",
        )
        final_template_projects = []
        api_family = network_element.get("api_family")
        api_function = network_element.get("api_function")
        self.log(
            "Getting template projects using family '{0}' and function '{1}'.".format(
                api_family, api_function
            ),
            "INFO",
        )

        params = {}
        if component_specific_filters:
            for filter_param in component_specific_filters:
                for key, value in filter_param.items():
                    if key == "name":
                        params["name"] = value
                    else:
                        self.log(
                            "Ignoring unsupported filter parameter: {0}".format(key),
                            "DEBUG",
                        )
                template_project_details = self.execute_get_with_pagination(
                    api_family, api_function, params
                )
                self.log("Retrieved template project details: {0}".format(template_project_details), "INFO")
                final_template_projects.extend(template_project_details)
            self.log("Using component-specific filters for API call.", "INFO")
        else:
            # Execute API call to retrieve Template Project details
            template_project_details = self.execute_get_with_pagination(
                api_family, api_function, params
            )
            self.log("Retrieved template project details: {0}".format(template_project_details), "INFO")
            final_template_projects.extend(template_project_details)

        # Modify Template Project details using temp_spec
        template_projects_temp_spec = self.projects_temp_spec()
        template_project_details = self.modify_parameters(
            template_projects_temp_spec, final_template_projects
        )
        modified_template_project_details = {}
        modified_template_project_details['projects'] = template_project_details

        self.log(
            "Modified Template Project details: {0}".format(
                modified_template_project_details
            ),
            "INFO",
        )

        return modified_template_project_details

    def get_template_details(self, network_element, component_specific_filters=None):
        """
        Retrieves template details based on the provided network element and component-specific filters.

        Args:
            network_element (dict): A dictionary containing the API family and function for retrieving template details.
            component_specific_filters (list, optional): A list of dictionaries containing filters for template details.

        Returns:
            list: A list containing the modified details of template details.
        """

        self.log(
            "Starting to retrieve template details with network element: {0} and component-specific filters: {1}".format(
                network_element, component_specific_filters
            ),
            "DEBUG",
        )
        final_template_details = []
        api_family = network_element.get("api_family")
        api_function = network_element.get("api_function")
        self.log(
            "Getting template details using family '{0}' and function '{1}'.".format(
                api_family, api_function
            ),
            "INFO",
        )

        params = {}
        if component_specific_filters:
            for filter_param in component_specific_filters:
                for key, value in filter_param.items():
                    if key == "template_name":
                        params["name"] = value
                    elif key == "id":
                        params["id"] = value
                    elif key == "project_name":
                        params["project_name"] = value
                    elif key == "include_uncommitted":
                        params["un_committed"] = value
                    else:
                        self.log(
                            "Ignoring unsupported filter parameter: {0}".format(key),
                            "DEBUG",
                        )

                self.log(f"Calling API with params: {params}", "DEBUG")
                template_details = self.execute_get_with_pagination(
                    api_family, api_function, params
                )
                self.log("Retrieved template details: {0}".format(template_details), "INFO")
                final_template_details.extend(template_details)
            self.log("Using component-specific filters for API call.", "INFO")
        else:
            # Execute API call to retrieve Template Project details
            template_details = self.execute_get_with_pagination(
                api_family, api_function, params
            )
            self.log("Retrieved template details: {0}".format(template_details), "INFO")
            final_template_details.extend(template_details)

        # Modify Template Project details using temp_spec
        template_projects_temp_spec = self.templates_temp_spec()
        template_details = self.modify_parameters(
            template_projects_temp_spec, final_template_details
        )
        modified_template_details = []
        for template in template_details:
            modified_template_details.append({"configuration_templates": template})

        self.log(
            "Modified Template details: {0}".format(
                modified_template_details
            ),
            "INFO",
        )

        return modified_template_details

    def write_dict_to_yaml(self, data_dict, file_path):
        """
        Converts a dictionary to YAML format and writes it to a specified file path.
        Args:
            data_dict (dict): The dictionary to convert to YAML format.
            file_path (str): The path where the YAML file will be written.
        Returns:
            bool: True if the YAML file was successfully written, False otherwise.
        """

        self.log(
            "Starting to write dictionary to YAML file at: {0}".format(file_path), "DEBUG"
        )
        try:
            self.log("Starting conversion of dictionary to YAML format.", "INFO")
            yaml_content = yaml.dump(
                data_dict,
                Dumper=OrderedDumper,
                default_flow_style=False,
                indent=2,
                allow_unicode=True,
                sort_keys=False  # Important: Don't sort keys to preserve order
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
        self.log("Components to process: {0}".format(components_list), "DEBUG")

        self.log("Initializing final configuration list and operation summary tracking", "DEBUG")
        final_list = []
        for component in components_list:
            self.log("Processing component: {0}".format(component), "DEBUG")
            network_element = module_supported_network_elements.get(component)
            if not network_element:
                self.log(
                    "Component {0} not supported by module, skipping processing".format(component),
                    "WARNING",
                )
                continue

            filters = component_specific_filters.get(component, [])
            operation_func = network_element.get("get_function_name")
            if callable(operation_func):
                details = operation_func(network_element, filters)
                self.log(
                    "Details retrieved for {0}: {1}".format(component, details), "DEBUG"
                )
                if component == "configuration_templates" and isinstance(details, list):
                    final_list.extend(details)  # Flatten the list
                else:
                    final_list.append(details)

        if not final_list:
            self.log("No configurations found to process, setting appropriate result", "WARNING")
            self.msg = {
                "message": "No configurations or components to process for module '{0}'. Verify input filters or configuration.".format(
                    self.module_name
                )
            }
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
        This method prepares the parameters required for adding, updating, or deleting
        network configurations such as SSIDs and interfaces in the Cisco Catalyst Center
        based on the desired state. It logs detailed information for each operation.
        Args:
            config (dict): The configuration data for the network elements.
            state (str): The desired state of the network elements ('merged' or 'deleted').
        """

        self.log(
            "Creating Parameters for API Calls with state: {0}".format(state), "INFO"
        )

        self.validate_params(config)

        # Set generate_all_configurations after validation
        self.generate_all_configurations = config.get("generate_all_configurations", False)
        self.log("Set generate_all_configurations mode: {0}".format(self.generate_all_configurations), "DEBUG")

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
        self.msg = "Successfully collected all parameters from the playbook for Wireless Design operations."
        self.status = "success"
        return self

    def get_diff_gathered(self):
        """
        Executes the merge operations for various network configurations in the Cisco Catalyst Center.
        This method processes additions and updates for SSIDs, interfaces, power profiles, access point profiles,
        radio frequency profiles, and anchor groups. It logs detailed information about each operation,
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
        "config_verify": {"type": "bool", "default": False},
        "dnac_api_task_timeout": {"type": "int", "default": 1200},
        "dnac_task_poll_interval": {"type": "int", "default": 2},
        "config": {"required": True, "type": "list", "elements": "dict"},
        "state": {"default": "gathered", "choices": ["gathered"]},
    }

    # Initialize the Ansible module with the provided argument specifications
    module = AnsibleModule(argument_spec=element_spec, supports_check_mode=True)
    # Initialize the NetworkCompliance object with the module
    ccc_template_playbook_generator = TemplatePlaybookGenerator(module)
    if (
        ccc_template_playbook_generator.compare_dnac_versions(
            ccc_template_playbook_generator.get_ccc_version(), "2.3.7.9"
        )
        < 0
    ):
        ccc_template_playbook_generator.msg = (
            "The specified version '{0}' does not support the YAML Playbook generation "
            "for TEMPLATE Module. Supported versions start from '2.3.7.9' onwards. ".format(
                ccc_template_playbook_generator.get_ccc_version()
            )
        )
        ccc_template_playbook_generator.set_operation_result(
            "failed", False, ccc_template_playbook_generator.msg, "ERROR"
        ).check_return_status()

    # Get the state parameter from the provided parameters
    state = ccc_template_playbook_generator.params.get("state")

    # Check if the state is valid
    if state not in ccc_template_playbook_generator.supported_states:
        ccc_template_playbook_generator.status = "invalid"
        ccc_template_playbook_generator.msg = "State {0} is invalid".format(
            state
        )
        ccc_template_playbook_generator.check_return_status()

    # Validate the input parameters and check the return statusk
    ccc_template_playbook_generator.validate_input().check_return_status()

    # Iterate over the validated configuration parameters
    for config in ccc_template_playbook_generator.validated_config:
        ccc_template_playbook_generator.reset_values()
        ccc_template_playbook_generator.get_want(
            config, state
        ).check_return_status()
        ccc_template_playbook_generator.get_diff_state_apply[
            state
        ]().check_return_status()

    module.exit_json(**ccc_template_playbook_generator.result)


if __name__ == "__main__":
    main()
