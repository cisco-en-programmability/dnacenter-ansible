#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright (c) 2026, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

"""Ansible module to generate YAML configurations for SD-Access Fabric Sites Zones Module."""
from __future__ import absolute_import, division, print_function

__metaclass__ = type
__author__ = "Abhishek Maheshwari, Sunil Shatagopa, Madhan Sankaranarayanan"

DOCUMENTATION = r"""
---
module: sda_fabric_sites_zones_playbook_config_generator
short_description: Generate YAML playbook for C(sda_fabric_sites_zones_workflow_manager) module.
description:
- Generates YAML configurations compatible with the C(sda_fabric_sites_zones_workflow_manager)
  module, reducing the effort required to manually create Ansible playbooks and
  enabling programmatic modifications.
- The YAML configurations generated represent the fabric sites and fabric zones
  configured on the Cisco Catalyst Center.
version_added: 6.44.0
extends_documentation_fragment:
- cisco.dnac.workflow_manager_params
author:
- Abhishek Maheshwari (@abmahesh)
- Sunil Shatagopa (@shatagopasunil)
- Madhan Sankaranarayanan (@madhansansel)
options:
  state:
    description: The desired state of Cisco Catalyst Center after module execution.
    type: str
    choices: [gathered]
    default: gathered
  file_path:
    description:
    - Path where the YAML configuration file will be saved.
    - If not provided, the file will be saved in the current working directory with
        a default file name C(sda_fabric_sites_zones_playbook_config_<YYYY-MM-DD_HH-MM-SS>.yml).
    - For example, C(sda_fabric_sites_zones_playbook_config_2026-02-20_13-42-45.yml).
    type: str
  file_mode:
    description:
    - Controls how config is written to the YAML file.
    - C(overwrite) replaces existing file content.
    - C(append) appends generated YAML content to the existing file.
    - This parameter is only relevant when C(file_path) is specified. Defaults to C(overwrite).
    type: str
    choices: ["overwrite", "append"]
    default: "overwrite"
  config:
    description:
    - A dictionary of filters for generating YAML playbook compatible with the C(sda_fabric_sites_zones_workflow_manager)
      module.
    - Filters specify which components to include in the YAML configuration file.
    - If config is not provided (omitted entirely), all configurations for all fabric sites and fabric zones will be generated.
    - This is useful for complete brownfield infrastructure discovery and documentation.
    - Important - An empty dictionary {} is not valid. Either omit 'config' entirely to generate
      all configurations, or provide specific filters within 'config'.
    type: dict
    required: false
    suboptions:
      component_specific_filters:
        description:
        - Filters to specify which components to include in the YAML configuration file.
        - If filters for specific components (e.g., fabric_sites or fabric_zones) are provided
          without explicitly including them in components_list, those components will be
          automatically added to components_list.
        - At least one of components_list or component filters must be provided.
        type: dict
        suboptions:
          components_list:
            description:
            - List of components to include in the YAML configuration file.
            - For example, ["fabric_sites", "fabric_zones"]
            - If not specified but component specific filters are provided,
              those components are automatically added to this list.
            - If neither components_list nor any component filters are provided,
              an error will be raised.
            type: list
            elements: str
            choices: ["fabric_sites", "fabric_zones"]
          fabric_sites:
            description:
            - Fabric Sites filters to apply when retrieving fabric sites.
            type: list
            elements: dict
            suboptions:
              site_name_hierarchy:
                description:
                - Site name hierarchy filter to apply when retrieving fabric sites.
                type: str
          fabric_zones:
            description:
            - Fabric Zones filters to apply when retrieving fabric zones.
            type: list
            elements: dict
            suboptions:
              site_name_hierarchy:
                description:
                - Site name hierarchy filter to apply when retrieving fabric zones.
                type: str

requirements:
- dnacentersdk >= 2.3.7.9
- python >= 3.9
notes:
- Cisco Catalyst Center >= 2.3.7.9
- |-
  SDK Methods used are
  sites.Sites.get_site
  site_design.SiteDesigns.get_sites
  sda.Sda.get_fabric_sites
  sda.Sda.get_fabric_zones
  sda.Sda.get_fabric_sites_by_id
  sda.Sda.get_fabric_zones_by_id
- |-
  SDK Paths used are
  GET /dna/intent/api/v1/sites
  GET /dna/intent/api/v1/sda/fabric-sites
  GET /dna/intent/api/v1/sda/fabric-zones
  GET /dna/intent/api/v1/sda/fabric-sites/{id}
  GET /dna/intent/api/v1/sda/fabric-zones/{id}
- |
  Auto-population of components_list:
  If component-specific filters (such as 'fabric_sites' or 'fabric_zones') are provided
  without explicitly including them in 'components_list', those components will be
  automatically added to 'components_list'.
- |-
  Module result behavior (changed/ok/failed):
  The module result reflects local file state only, not Catalyst Center state.
  In overwrite mode, the full file content is compared (excluding volatile
  fields like timestamps and playbook path). In append mode, only the last
  YAML document in the file is compared against the newly generated
  configuration. If a file contains multiple config entries from previous
  appends, only the most recent entry is used for the idempotency check.
  - changed=true (status: success): The generated YAML configuration differs
    from the existing output file (or the file does not exist). The file was
    written and the configuration was updated.
  - changed=false (status: ok): The generated YAML configuration matches the
    existing output file content. The write was skipped as the file is
    already up-to-date.
  - failed=true (status: failed): The module encountered a validation error,
    API failure, or file write error. No file was written or modified.
  Note: Re-running with identical inputs and unchanged Catalyst Center state
  will produce changed=false, ensuring idempotent playbook behavior.
seealso:
- module: cisco.dnac.sda_fabric_sites_zones_workflow_manager
  description: Module to manage SD-Access Fabric Sites and Zones in Cisco Catalyst Center.
"""

EXAMPLES = r"""
- name: Auto-generate YAML Configuration for all components which includes fabric sites and fabric zones.
  cisco.dnac.sda_fabric_sites_zones_playbook_config_generator:
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
    # No config provided - generates all configurations

- name: Generate YAML Configuration with File Path specified
  cisco.dnac.sda_fabric_sites_zones_playbook_config_generator:
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
    file_path: "tmp/catc_sda_fabric_sites_zones_config.yml"
    file_mode: "overwrite"

- name: Generate YAML Configuration with specific fabric sites components only
  cisco.dnac.sda_fabric_sites_zones_playbook_config_generator:
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
    file_path: "tmp/catc_sda_fabric_sites_config.yml"
    file_mode: "append"
    config:
      component_specific_filters:
        components_list: ["fabric_sites"]

- name: Generate YAML Configuration with specific fabric sites components only
     using site_name_hierarchy filter
  cisco.dnac.sda_fabric_sites_zones_playbook_config_generator:
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
    file_path: "tmp/catc_sda_fabric_sites_config.yml"
    config:
      component_specific_filters:
        components_list: ["fabric_sites"] # Optional
        fabric_sites:
          - site_name_hierarchy: "Global/USA/California/San Jose"

- name: Generate YAML Configuration with specific fabric zones components only
  cisco.dnac.sda_fabric_sites_zones_playbook_config_generator:
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
    file_path: "tmp/catc_sda_fabric_zones_config.yml"
    config:
      component_specific_filters:
        components_list: ["fabric_zones"]

- name: Generate YAML Configuration with site_name_hierarchy filter
  cisco.dnac.sda_fabric_sites_zones_playbook_config_generator:
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
    file_path: "tmp/catc_sda_fabric_zones_config.yml"
    config:
      component_specific_filters:
        components_list: ["fabric_zones"] # Optional
        fabric_zones:
          - site_name_hierarchy: "Global/USA/California/San Jose"

- name: Generate YAML Configuration for all components
  cisco.dnac.sda_fabric_sites_zones_playbook_config_generator:
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
    file_path: "tmp/catc_sda_fabric_sites_zones_config.yml"
    config:
      component_specific_filters:
        components_list: ["fabric_sites", "fabric_zones"]
"""

RETURN = r"""
# Case_1: Success Scenario
response_1:
  description: A dictionary with  with the response returned by the Cisco Catalyst Center Python SDK
  returned: always
  type: dict
  sample: >
    {
        "msg": {
            "components_processed": 2,
            "components_skipped": 0,
            "configurations_count": 7,
            "file_path": "sda_fabric_sites_zones_playbook_config_2026-02-20_13-42-45.yml",
            "message": "YAML configuration file generated successfully for module 'sda_fabric_sites_zones_workflow_manager'",
            "status": "success"
        },
        "response": {
            "components_processed": 2,
            "components_skipped": 0,
            "configurations_count": 7,
            "file_path": "sda_fabric_sites_zones_playbook_config_2026-02-20_13-42-45.yml",
            "message": "YAML configuration file generated successfully for module 'sda_fabric_sites_zones_workflow_manager'",
            "status": "success"
        },
        "status": "success"
    }
# Case_2: Error Scenario
response_2:
  description: A string with the response returned by the Cisco Catalyst Center Python SDK
  returned: always
  type: dict
  sample: >
    {
        "msg":
            "Validation Error: component_specific_filters is provided but no components are specified.
             Either provide 'components_list' with at least one component, or provide filters for specific components.",
        "response":
            "Validation Error: component_specific_filters is provided but no components are specified.
             Either provide 'components_list' with at least one component, or provide filters for specific components."
    }
"""

from ansible.module_utils.basic import AnsibleModule
from ansible_collections.cisco.dnac.plugins.module_utils.brownfield_helper import (
    BrownFieldHelper,
)
from ansible_collections.cisco.dnac.plugins.module_utils.dnac import (
    DnacBase,
)
import time
from collections import OrderedDict


class FabricSiteZonePlaybookConfigGenerator(DnacBase, BrownFieldHelper):
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
        self.module_name = "sda_fabric_sites_zones_workflow_manager"

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

        # Check if config is provided but empty - Error scenario
        if isinstance(self.config, dict) and len(self.config) == 0:
            self.msg = (
                "Configuration cannot be an empty dictionary. "
                "Either omit 'config' entirely to generate all configurations, "
                "or provide specific filters within 'config'."
            )
            self.log(self.msg, "ERROR")
            self.set_operation_result("failed", False, self.msg, "ERROR")
            return self

        # Check if configuration is not provided (None) - treat as generate_all
        if self.config is None:
            self.validated_config = {"generate_all_configurations": True}
            self.msg = "Configuration is not provided - treating as generate all config mode"
            self.log(self.msg, "INFO")
            return self

        # Expected schema for configuration parameters
        temp_spec = {
            "component_specific_filters": {
                "type": "dict",
                "required": False
            }
        }

        # Validate params
        self.log("Validating configuration against schema", "DEBUG")
        valid_temp = self.validate_config_dict(self.config, temp_spec)

        self.log("Validating invalid parameters against provided config", "DEBUG")
        self.validate_invalid_params(self.config, temp_spec.keys())

        # Auto-populate components_list from component filters and validate
        component_specific_filters = valid_temp.get("component_specific_filters")
        if component_specific_filters:
            self.auto_populate_and_validate_components_list(component_specific_filters)
            self.deduplicate_component_filters(component_specific_filters)

        # Set the validated configuration and update the result with success status
        self.validated_config = valid_temp
        self.msg = "Successfully validated playbook configuration parameters using 'validated_input': {0}".format(
            str(valid_temp)
        )
        self.set_operation_result("success", False, self.msg, "INFO")
        return self

    def get_workflow_filters_schema(self):
        """
        Description:
            Constructs and returns a structured mapping for managing various virtual network elements
            such as fabric VLANs, virtual networks, and anycast gateways. This mapping includes
            associated filters, temporary specification functions, API details, and fetch function references
            used in the virtual network workflow orchestration process.

        Args:
            self: Refers to the instance of the class containing definitions of helper methods like
                `fabric_vlan_temp_spec`, `get_fabric_vlans`, etc.

        Return:
            dict: A dictionary with the following structure:
                - "network_elements": A nested dictionary where each key represents a network component
                (e.g., 'fabric_vlan', 'virtual_networks', 'anycast_gateways') and maps to:
                    - "filters": List of filter keys relevant to the component.
                    - "reverse_mapping_function": Reference to the function that generates temp specs for the component.
                    - "api_function": Name of the API to be called for the component.
                    - "api_family": API family name (e.g., 'sda').
                    - "get_function_name": Reference to the internal function used to retrieve the component data.
                - "global_filters": An empty list reserved for global filters applicable across all network elements.
        """

        self.log("Building workflow filters schema for sda fabric sites and zones module", "DEBUG")

        schema = {
            "network_elements": {
                "fabric_sites": {
                    "filters": {"site_name_hierarchy": {"type": "str"}},
                    "reverse_mapping_function": self.fabric_site_temp_spec,
                    "api_function": "get_fabric_sites",
                    "api_family": "sda",
                    "get_function_name": self.get_fabric_sites_from_ccc,
                },
                "fabric_zones": {
                    "filters": {"site_name_hierarchy": {"type": "str"}},
                    "reverse_mapping_function": self.fabric_zone_temp_spec,
                    "api_function": "get_fabric_zones",
                    "api_family": "sda",
                    "get_function_name": self.get_fabric_zones_from_ccc,
                },
            }
        }

        network_elements = list(schema["network_elements"].keys())
        self.log(
            f"Workflow filters schema generated successfully with {len(network_elements)} network element(s): {network_elements}",
            "INFO",
        )

        return schema

    def get_site_id(self, site_name):
        """
        Retrieve the site ID and check if the site exists in Cisco Catalyst Center based on the provided site name.

        Args:
            site_name (str): The name or hierarchy of the site to be retrieved.

        Returns:
            The site ID (str) if the site exists, or None if the site does not exist.
        """
        try:
            response = self.get_site(site_name)

            # Check if the response is empty
            if response is None:
                self.log(
                    "No response from get_site with site_name: {0}".format(site_name),
                    "DEBUG"
                )
                return response

            site_response = response.get("response")
            if not site_response:
                self.log(
                    "No site response found in the response: {0}".format(site_response),
                    "WARNING"
                )
                return site_response

            site_id = site_response[0].get("id")
            self.log(
                "Site details retrieved for site '{0}'': {1}. Retrieved site id: {2}."
                .format(site_name, str(response), site_id),
                "DEBUG"
            )
            return site_id

        except Exception as e:
            self.log(
                "An exception occurred while retrieving site details for site '{0}'. Error: {1}"
                .format(site_name, e),
                "ERROR"
            )
            return None

    def transform_fabric_site_name(self, site_details):
        """
        Transforms site name hierarchy for a given fabric site by extracting and mapping
        the relevant site ID to its corresponding hierarchical name.

        Args:
            site_details (dict): A dictionary containing site details, including the site ID.

        Returns:
            str: The transformed site name hierarchy corresponding to the provided site ID.
        """

        self.log(
            "Starting site name hierarchy transformation for given site id: {0}"
            .format(site_details.get("siteId", "Unknown")),
            "DEBUG"
        )
        site_id = site_details.get("siteId", None)

        if not site_id:
            self.log("No site ID found in site details: {0}".format(site_details), "WARNING")
            return site_id

        self.log("Processing site name hierarchy for site ID: {0}".format(site_id), "DEBUG")
        site_name_hierarchy = self.site_id_name_dict.get(site_id, None)

        if not site_name_hierarchy:
            self.log("Site name hierarchy not found for site ID: {0}".format(site_id), "WARNING")
            return site_name_hierarchy

        self.log(
            "Completed site name hierarchy transformation for site ID: {0}, transformed site name hierarchy: {1}"
            .format(site_id, site_name_hierarchy), "DEBUG"
        )

        return site_name_hierarchy

    def fabric_site_temp_spec(self):
        """
        Constructs a temporary specification for fabric sites, defining the structure and types of attributes
        that will be used in the YAML configuration file. This specification includes details such as site name hierarchy,
        fabric type, pub-sub enablement, and authentication profile.

        Returns:
            OrderedDict: An ordered dictionary defining the structure of fabric site attributes.
        """

        self.log("Generating temporary specification for fabric sites.", "DEBUG")
        fabric_sites = OrderedDict(
            {
                "site_name_hierarchy": {
                    "type": "str",
                    "special_handling": True,
                    "transform": self.transform_fabric_site_name,
                },
                "fabric_type": {"fixed_value": "fabric_site"},
                "is_pub_sub_enabled": {"type": "bool", "source_key": "isPubSubEnabled"},
                "authentication_profile": {"type": "str", "source_key": "authenticationProfileName"}
            }
        )
        return fabric_sites

    def fabric_zone_temp_spec(self):
        """
        Constructs a temporary specification for fabric zones, defining the structure and types of attributes
        that will be used in the YAML configuration file. This specification includes details such as site name hierarchy,
        fabric type and authentication profile.

        Returns:
            OrderedDict: An ordered dictionary defining the structure of fabric zone attributes.
        """

        self.log("Generating temporary specification for fabric zones.", "DEBUG")
        fabric_zones = OrderedDict(
            {
                "site_name_hierarchy": {
                    "type": "str",
                    "special_handling": True,
                    "transform": self.transform_fabric_site_name,
                },
                "fabric_type": {"fixed_value": "fabric_zone"},
                "authentication_profile": {"type": "str", "source_key": "authenticationProfileName"}
            }
        )
        return fabric_zones

    def get_fabric_sites_from_ccc(self, network_element, component_specific_filters=None):
        """
        Retrieves fabric sites from Catalyst Center with pagination support.

        Fetches fabric sites information using network element configuration and optional filters.
        Handles paginated API responses and transforms data into standardized format for
        YAML playbook generation. Supports filtering by site name hierarchy.

        Args:
            network_element (dict): A dictionary containing the API family and function for retrieving fabric sites.
            component_specific_filters (list, optional): A list of dictionaries containing filters for fabric sites.

        Returns:
            list: A list containing the modified details of fabric sites.
        """

        self.log(
            "Starting to retrieve fabric sites with network element: {0} and component-specific filters: {1}".format(
                network_element, component_specific_filters
            ),
            "DEBUG",
        )

        # Extract API family and function from network_element
        api_family = network_element.get("api_family")
        api_function = network_element.get("api_function")
        if not api_family or not api_function:
            self.log(
                "Missing API family or function in network element: {0}".format(network_element),
                "ERROR"
            )
            return []

        final_fabric_sites = []

        self.log(
            "Getting sda fabric sites using API family '{0}' and API function '{1}'.".format(
                api_family, api_function
            ),
            "DEBUG"
        )

        params = {}
        if component_specific_filters:
            self.log(
                "Started Processing {0} filter(s) for fabric sites retrieval".format(
                    len(component_specific_filters)
                ),
                "DEBUG"
            )

            for filter_param in component_specific_filters:
                if "site_name_hierarchy" in filter_param:
                    value = filter_param.get("site_name_hierarchy")
                    site_id = self.get_site_id(value)
                    if not site_id:
                        self.log(
                            "The site '{0}' does not exist in the Catalyst Center, skipping processing."
                            .format(value),
                            "WARNING"
                        )
                        continue

                    self.log(
                        "Mapped site name hierarchy '{0}' to site ID '{1}'.".format(
                            value, site_id
                        ),
                        "DEBUG"
                    )
                    params["siteId"] = site_id

                unsupported_keys = set(filter_param.keys()) - {"site_name_hierarchy"}
                if unsupported_keys:
                    self.log(
                        "Ignoring unsupported filter parameters for fabric sites: {0}".format(unsupported_keys),
                        "WARNING"
                    )

                self.log(
                    "Fetching fabric sites with parameters: {0}".format(params),
                    "DEBUG"
                )
                fabric_sites_details = self.execute_get_with_pagination(
                    api_family, api_function, params
                )

                if fabric_sites_details:
                    final_fabric_sites.extend(fabric_sites_details)
                    self.log(
                        "Retrieved {0} fabric site(s): {1}".format(
                            len(fabric_sites_details), fabric_sites_details
                        ),
                        "DEBUG"
                    )
                else:
                    self.log(
                        "No fabric sites found for parameters: {0}".format(params),
                        "DEBUG"
                    )
                params.clear()

            self.log(
                "Completed Processing {0} filter(s) for fabric sites retrieval".format(
                    len(component_specific_filters)
                ),
                "DEBUG"
            )
        else:
            self.log("Fetching all fabric sites details from Catalyst Center", "DEBUG")

            fabric_sites_details = self.execute_get_with_pagination(
                api_family, api_function, params
            )

            if fabric_sites_details:
                final_fabric_sites.extend(fabric_sites_details)
                self.log(
                    "Retrieved {0} fabric site(s) from Catalyst Center".format(
                        len(fabric_sites_details)
                    ),
                    "DEBUG"
                )
            else:
                self.log("No fabric sites found in Catalyst Center", "DEBUG")

        # Transform using temp spec
        self.log(
            "Transforming {0} fabric site(s) using fabric sites temp spec".format(
                len(final_fabric_sites)
            ),
            "DEBUG"
        )
        fabric_site_temp_spec = self.fabric_site_temp_spec()
        modified_site_details = self.modify_parameters(
            fabric_site_temp_spec, final_fabric_sites
        )
        self.log(
            "Completed retrieving fabric site(s): {0}".format(
                modified_site_details
            ),
            "INFO",
        )

        return modified_site_details

    def get_fabric_zones_from_ccc(self, network_element, component_specific_filters=None):
        """
        Retrieves fabric zones from Catalyst Center with pagination support.

        Fetches fabric zones information using network element configuration and optional filters.
        Handles paginated API responses and transforms data into standardized format for
        YAML playbook generation. Supports filtering by site name hierarchy.

        Args:
            network_element (dict): A dictionary containing the API family and function for retrieving fabric zones.
            component_specific_filters (list, optional): A list of dictionaries containing filters for fabric zones.

        Returns:
            list: A list containing the modified details of fabric zones.
        """

        self.log(
            "Starting to retrieve fabric zones with network element: {0} and component-specific filters: {1}".format(
                network_element, component_specific_filters
            ),
            "DEBUG",
        )

        # Extract API family and function from network_element
        api_family = network_element.get("api_family")
        api_function = network_element.get("api_function")
        if not api_family or not api_function:
            self.log(
                "Missing API family or function in network element: {0}".format(network_element),
                "ERROR"
            )
            return []

        final_fabric_zones = []

        self.log(
            "Getting sda fabric zones using API family '{0}' and API function '{1}'.".format(
                api_family, api_function
            ),
            "DEBUG"
        )

        params = {}
        if component_specific_filters:
            self.log(
                "Started Processing {0} filter(s) for fabric zones retrieval".format(
                    len(component_specific_filters)
                ),
                "DEBUG"
            )

            for filter_param in component_specific_filters:
                if "site_name_hierarchy" in filter_param:
                    value = filter_param.get("site_name_hierarchy")
                    site_id = self.get_site_id(value)
                    if not site_id:
                        self.log(
                            "The site '{0}' does not exist in the Catalyst Center, skipping processing."
                            .format(value),
                            "WARNING"
                        )
                        continue

                    self.log(
                        "Mapped site name hierarchy '{0}' to site ID '{1}'.".format(
                            value, site_id
                        ),
                        "DEBUG"
                    )
                    params["siteId"] = site_id

                unsupported_keys = set(filter_param.keys()) - {"site_name_hierarchy"}
                if unsupported_keys:
                    self.log(
                        "Ignoring unsupported filter parameters for fabric zones: {0}".format(unsupported_keys),
                        "WARNING"
                    )

                self.log(
                    "Fetching fabric zones with parameters: {0}".format(params),
                    "DEBUG"
                )
                fabric_zones_details = self.execute_get_with_pagination(
                    api_family, api_function, params
                )

                if fabric_zones_details:
                    final_fabric_zones.extend(fabric_zones_details)
                    self.log(
                        "Retrieved {0} fabric zone(s): {1}".format(
                            len(fabric_zones_details), fabric_zones_details
                        ),
                        "DEBUG"
                    )
                else:
                    self.log(
                        "No fabric zones found for parameters: {0}".format(params),
                        "DEBUG"
                    )
                params.clear()

            self.log(
                "Completed Processing {0} filter(s) for fabric zones retrieval".format(
                    len(component_specific_filters)
                ),
                "DEBUG"
            )
        else:
            self.log("Fetching all fabric zones details from Catalyst Center", "DEBUG")

            fabric_zones_details = self.execute_get_with_pagination(
                api_family, api_function, params
            )

            if fabric_zones_details:
                final_fabric_zones.extend(fabric_zones_details)
                self.log(
                    "Retrieved {0} fabric zone(s) from Catalyst Center".format(
                        len(fabric_zones_details)
                    ),
                    "DEBUG"
                )
            else:
                self.log("No fabric zones found in Catalyst Center", "DEBUG")

        # Transform using temp spec
        self.log(
            "Transforming {0} fabric zone(s) using fabric zones temp spec".format(
                len(final_fabric_zones)
            ),
            "DEBUG"
        )
        fabric_zone_temp_spec = self.fabric_zone_temp_spec()
        final_fabric_zones = self.modify_parameters(
            fabric_zone_temp_spec, final_fabric_zones
        )
        self.log(
            "Completed retrieving fabric zone(s): {0}".format(
                final_fabric_zones
            ),
            "INFO",
        )

        return final_fabric_zones

    def yaml_config_generator(self, yaml_config_generator):
        """
        Generates a YAML configuration file based on the provided parameters.
        This function retrieves network element details using component-specific filters, processes the data,
        and writes the YAML content to a specified file. It dynamically handles multiple network elements and their respective filters.

        Args:
            yaml_config_generator (dict): Contains component_specific_filters.

        Returns:
            self: The current instance with the operation result and message updated.
        """

        self.log(
            "Starting YAML config generation with parameters: {0}".format(
                self.pprint(yaml_config_generator)
            ),
            "DEBUG",
        )

        # Check if generate_all_configurations mode is enabled
        generate_all = yaml_config_generator.get("generate_all_configurations", False)
        if generate_all:
            self.log("Auto-discovery mode enabled - will process all devices and all features", "INFO")

        self.log("Determining output file path for YAML configuration", "DEBUG")

        # Get file_path and file_mode from self.params (top-level parameters)
        file_path = self.params.get("file_path")
        if not file_path:
            self.log("No file_path provided by user, generating default filename", "DEBUG")
            file_path = self.generate_filename()
        else:
            self.log("Using user-provided file_path: {0}".format(file_path), "DEBUG")

        file_mode = self.params.get("file_mode", "overwrite")
        self.log(
            "YAML configuration file path determined: {0}, file_mode: {1}".format(file_path, file_mode),
            "DEBUG"
        )

        self.log("Initializing filter dictionaries", "DEBUG")
        if generate_all:
            # In generate_all_configurations mode, override any provided filters to ensure we get ALL configurations
            self.log("Auto-discovery mode: Overriding any provided filters to retrieve all devices and all features", "INFO")
            # Set empty filters to retrieve everything
            component_specific_filters = {}
        else:
            self.log(
                "Normal mode: Using provided component_specific_filters from input",
                "DEBUG",
            )
            component_specific_filters = yaml_config_generator.get("component_specific_filters") or {}
            self.log(
                f"Component specific filters initialized: {self.pprint(component_specific_filters)}",
                "DEBUG",
            )

        self.log("Retrieving supported network elements schema for the module", "DEBUG")
        module_supported_network_elements = self.module_schema.get("network_elements", {})

        self.log("Determining components list for processing", "DEBUG")
        components_list = component_specific_filters.get(
            "components_list", list(module_supported_network_elements.keys())
        )

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

            filters = component_specific_filters.get(component, [])
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
            final_config_list.extend(component_data)

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

        yaml_config_dict = {"config": [{"fabric_sites": final_config_list}]}
        self.log(
            "Final config dictionary created: {0}".format(self.pprint(yaml_config_dict)),
            "DEBUG"
        )

        additional_config_headers = [
            "Full configuration generates all fabric sites first, followed by all fabric zones."
        ]

        file_written = self.write_dict_to_yaml(
            yaml_config_dict,
            file_path,
            file_mode,
            notes=additional_config_headers,
        )

        if file_written:
            self.msg = {
                "status": "success",
                "message": "YAML configuration file generated successfully for module '{0}'".format(
                    self.module_name
                ),
                "file_path": file_path,
                "file_mode": file_mode,
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
                "status": "ok",
                "message": "YAML configuration file already up-to-date for module '{0}'. No changes written.".format(
                    self.module_name
                ),
                "file_path": file_path,
                "file_mode": file_mode,
                "components_processed": processed_count,
                "components_skipped": skipped_count,
                "configurations_count": len(final_config_list),
            }
            self.set_operation_result("ok", False, self.msg, "INFO")

            self.log(
                "YAML configuration unchanged. File: {0}, Components: {1}/{2}, Configs: {3}".format(
                    file_path,
                    processed_count,
                    len(components_list),
                    len(final_config_list),
                ),
                "INFO",
            )

        return self

    def get_diff_gathered(self):
        """
        Executes YAML configuration file generation for sda fabric sites zones workflow.

        Processes the desired state parameters prepared by get_want() and generates a
        YAML configuration file containing network element details from Catalyst Center.
        This method orchestrates the yaml_config_generator operation and tracks execution
        time for performance monitoring.
        """

        start_time = time.time()
        self.log("Starting 'get_diff_gathered' operation.", "DEBUG")
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
        self.log("Beginning iteration over defined workflow operations for processing.", "DEBUG")
        for index, (param_key, operation_name, operation_func) in enumerate(
            workflow_operations, start=1
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

                try:
                    operation_func(params).check_return_status()
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
        "state": {"default": "gathered", "choices": ["gathered"]},
        "file_path": {"required": False, "type": "str"},
        "file_mode": {
            "required": False,
            "type": "str",
            "default": "overwrite",
            "choices": ["overwrite", "append"],
        },
        "config": {"required": False, "type": "dict"},
    }

    # Initialize the Ansible module with the provided argument specifications
    module = AnsibleModule(argument_spec=element_spec, supports_check_mode=True)
    # Initialize the NetworkCompliance object with the module
    config_generator = FabricSiteZonePlaybookConfigGenerator(module)
    if (
        config_generator.compare_dnac_versions(
            config_generator.get_ccc_version(), "2.3.7.9"
        )
        < 0
    ):
        config_generator.msg = (
            "The specified version '{0}' does not support the YAML Playbook generation "
            "for FABRIC SITES ZONES Module. Supported versions start from '2.3.7.9' onwards. ".format(
                config_generator.get_ccc_version()
            )
        )
        config_generator.set_operation_result(
            "failed", False, config_generator.msg, "ERROR"
        ).check_return_status()

    # Get the state parameter from the provided parameters
    state = config_generator.params.get("state")

    # Check if the state is valid
    if state not in config_generator.supported_states:
        config_generator.status = "invalid"
        config_generator.msg = "State {0} is invalid".format(
            state
        )
        config_generator.check_return_status()

    # Validate the input parameters and check the return statusk
    config_generator.validate_input().check_return_status()

    config = config_generator.validated_config
    config_generator.get_want(
        config, state
    ).check_return_status()
    config_generator.get_diff_state_apply[
        state
    ]().check_return_status()

    module.exit_json(**config_generator.result)


if __name__ == "__main__":
    main()
