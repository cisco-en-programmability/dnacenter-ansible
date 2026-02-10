#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright (c) 2026, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

"""
Ansible brownfield playbook generator for SDA fabric multicast configurations.

Retrieves existing multicast configurations from Cisco Catalyst Center and generates
YAML playbooks compatible with the sda_fabric_multicast_workflow_manager module.
"""
from __future__ import absolute_import, division, print_function

__metaclass__ = type
__author__ = "Archit Soni, Madhan Sankaranarayanan"

DOCUMENTATION = r"""
---
module: brownfield_sda_fabric_multicast_playbook_generator
short_description: Generate YAML configurations playbook for 'sda_fabric_multicast_workflow_manager' module.
description:
- Automates YAML playbook generation from existing SDA fabric multicast
  deployments in Cisco Catalyst Center.
- Creates playbooks compatible with the C(sda_fabric_multicast_workflow_manager)
  module for brownfield infrastructure migration and documentation.
- Reduces manual effort by programmatically extracting current multicast
  configurations including replication modes, SSM ranges, and ASM RPs.
- Supports selective filtering to generate playbooks for specific fabric sites
  or Layer 3 virtual networks.
- Enables complete infrastructure discovery with auto-generation mode when
  C(generate_all_configurations) is enabled.
- Requires Cisco Catalyst Center version 2.3.7.9 or higher.
version_added: 6.44.0
extends_documentation_fragment:
- cisco.dnac.workflow_manager_params
author:
- Archit Soni (@koderchit)
- Madhan Sankaranarayanan (@madhansansel)
options:
  state:
    description:
    - The desired state for the module operation.
    - C(gathered) generates YAML playbooks from existing configurations.
    type: str
    choices: [gathered]
    default: gathered
  config:
    description:
    - A list of configuration filters for generating YAML playbooks compatible
      with the C(sda_fabric_multicast_workflow_manager) module.
    - Each configuration entry can include file path specification, component
      filters, and auto-discovery settings.
    - Multiple configuration entries can be provided to generate separate
      playbooks with different filter criteria.
    type: list
    elements: dict
    required: true
    suboptions:
      generate_all_configurations:
        description:
        - Enables automatic discovery and generation of YAML configurations for
          all fabric multicast deployments.
        - When C(true), retrieves all SDA fabric multicast configurations from
          Cisco Catalyst Center without requiring specific filters.
        - Overrides any provided C(component_specific_filters) to ensure
          complete configuration retrieval.
        - Ideal for complete brownfield infrastructure migration and
          comprehensive documentation.
        - If enabled, a default filename will be auto-generated when
          C(file_path) is not provided.
        - "Default filename format: C(sda_fabric_multicast_workflow_manager_playbook_<DD_Mon_YYYY_HH_MM_SS_MS>.yml)"
        type: bool
        required: false
        default: false
      file_path:
        description:
        - Absolute or relative path where the generated YAML playbook file will be saved.
        - If not specified, the file is saved in the current working directory with an auto-generated filename.
        - Default filename format is C(sda_fabric_multicast_workflow_manager_playbook_<DD_Mon_YYYY_HH_MM_SS_MS>.yml).
        - "Example: C(sda_fabric_multicast_workflow_manager_playbook_22_Apr_2025_21_43_26_379.yml)"
        type: str
        required: false
      component_specific_filters:
        description:
        - Component-level filters to selectively include specific configurations
          in the generated playbook.
        - Allows fine-grained control over which fabric multicast configurations
          are extracted from Cisco Catalyst Center.
        - If C(components_list) is specified, only those components are
          processed regardless of other filters.
        - If C(generate_all_configurations) is C(true), these filters are
          ignored and all configurations are retrieved.
        - Supports filtering by fabric site hierarchy and Layer 3 virtual
          network names.
        type: dict
        required: false
        suboptions:
          components_list:
            description:
            - List of component types to include in the generated YAML playbook.
            - Currently supports C(fabric_multicast) for SDA fabric multicast configurations.
            - If omitted, all supported components are included by default.
            - If specified, only the listed components will be processed.
            type: list
            elements: str
            choices:
            - fabric_multicast
            required: false
          fabric_multicast:
            description:
            - Each filter entry can specify C(fabric_name) and/or
              C(layer3_virtual_network) to narrow results.
            - Retrieved configurations include replication mode, SSM ranges,
              ASM RP details, and IP pool assignments.
            type: list
            elements: dict
            required: false
            suboptions:
              fabric_name:
                description:
                - The hierarchical name of the fabric site from which to
                  retrieve multicast configurations.
                - Must match the exact site hierarchy as configured in Cisco
                  Catalyst Center.
                - Site can be either a fabric site or fabric zone.
                - If the specified site is not configured as a fabric site or
                  fabric zone, the filter entry is skipped with a warning.
                - "Example hierarchical path: C(Global/USA/San Jose/Building1)"
                - Case-sensitive matching is performed against cached site
                  mappings.
                - For detailed parameter usage and configuration examples, refer
                  to the C(sda_fabric_multicast_workflow_manager) module
                  documentation.
                type: str
                required: false
              layer3_virtual_network:
                description:
                - The name of the Layer 3 virtual network (VN) associated with
                  the fabric multicast configuration.
                - Used to filter multicast configurations for a specific virtual
                  network within the fabric site.
                - Can be combined with C(fabric_name) to retrieve multicast
                  settings for a specific VN in a specific fabric.
                - If specified alone without C(fabric_name), retrieves
                  configurations for the VN across all fabric sites.
                - "Example VN names: C(GUEST_VN), C(EMPLOYEE_VN), C(IOT_VN)"
                - For detailed parameter usage and configuration examples, refer
                  to the C(sda_fabric_multicast_workflow_manager) module
                  documentation.
                type: str
                required: false

requirements:
- dnacentersdk >= 2.9.2
- python >= 3.9
- Cisco Catalyst Center >= 2.3.7.9

notes:
- Requires minimum Cisco Catalyst Center version 2.3.7.9 for SDA fabric
  multicast API support.
- Module will fail with an error if connected to an unsupported version.
- Generated playbooks are compatible with the
  C(sda_fabric_multicast_workflow_manager) module for configuration deployment.
- Device IDs in RP configurations are automatically converted to management IP
  addresses in the generated playbook.
- Replication modes are retrieved from cached fabric configurations to ensure
  accurate playbook generation.
- For FABRIC location RPs, external IP address fields are automatically
  excluded from the generated playbook.
- Site hierarchies must exist in Cisco Catalyst Center and be configured as
  fabric sites or zones to be included in results.
- Use C(dnac_log) and C(dnac_log_level) parameters for detailed operation
  logging and troubleshooting.
- The module operates in check mode but does not make any changes to Cisco
  Catalyst Center.
"""

EXAMPLES = r"""
- name: Generate YAML playbook for all SDA fabric multicast configurations
  cisco.dnac.brownfield_sda_fabric_multicast_playbook_generator:
    dnac_host: "{{ dnac_host }}"
    dnac_username: "{{ dnac_username }}"
    dnac_password: "{{ dnac_password }}"
    dnac_verify: "{{ dnac_verify }}"
    dnac_port: "{{ dnac_port }}"
    dnac_version: "{{ dnac_version }}"
    dnac_debug: "{{ dnac_debug }}"
    dnac_log: true
    dnac_log_level: INFO
    state: gathered
    config:
      - generate_all_configurations: true
        file_path: "/path/to/output/all_fabric_multicast_configs.yml"

- name: Generate YAML playbook for specific fabric site
  cisco.dnac.brownfield_sda_fabric_multicast_playbook_generator:
    dnac_host: "{{ dnac_host }}"
    dnac_username: "{{ dnac_username }}"
    dnac_password: "{{ dnac_password }}"
    dnac_verify: "{{ dnac_verify }}"
    dnac_port: "{{ dnac_port }}"
    dnac_version: "{{ dnac_version }}"
    dnac_debug: "{{ dnac_debug }}"
    dnac_log: true
    state: gathered
    config:
      - file_path: "/path/to/output/site_specific_multicast.yml"
        component_specific_filters:
          components_list:
            - fabric_multicast
          fabric_multicast:
            - fabric_name: "Global/USA/San Jose/Building1"

- name: Generate YAML playbook for specific fabric and virtual network
  cisco.dnac.brownfield_sda_fabric_multicast_playbook_generator:
    dnac_host: "{{ dnac_host }}"
    dnac_username: "{{ dnac_username }}"
    dnac_password: "{{ dnac_password }}"
    dnac_verify: "{{ dnac_verify }}"
    dnac_port: "{{ dnac_port }}"
    dnac_version: "{{ dnac_version }}"
    dnac_debug: "{{ dnac_debug }}"
    state: gathered
    config:
      - component_specific_filters:
          fabric_multicast:
            - fabric_name: "Global/USA/San Jose/Building1"
              layer3_virtual_network: "GUEST_VN"

- name: Generate playbook for multiple fabric sites with auto-generated filename
  cisco.dnac.brownfield_sda_fabric_multicast_playbook_generator:
    dnac_host: "{{ dnac_host }}"
    dnac_username: "{{ dnac_username }}"
    dnac_password: "{{ dnac_password }}"
    dnac_verify: "{{ dnac_verify }}"
    dnac_port: "{{ dnac_port }}"
    dnac_version: "{{ dnac_version }}"
    dnac_debug: "{{ dnac_debug }}"
    state: gathered
    config:
      - component_specific_filters:
          fabric_multicast:
            - fabric_name: "Global/USA/San Jose/Building1"
            - fabric_name: "Global/USA/San Jose/Building2"
            - fabric_name: "Global/Europe/London/DataCenter1"
"""


RETURN = r"""
response:
  description: Details of the YAML playbook generation operation.
  returned: always
  type: dict
  contains:
    response:
      description:
      - Success or failure message indicating the result of the playbook
        generation operation.
      - For successful operations, includes the file path where the YAML
        playbook was saved.
      - For failed operations, includes error details and failure reason.
      type: dict
      returned: always
      sample:
        "YAML config generation Task succeeded for module 'sda_fabric_multicast_workflow_manager'.":
          file_path: "/path/to/output/playbook.yml"
    version:
      description: Cisco Catalyst Center version used during the operation.
      type: str
      returned: always
      sample: "2.3.7.9"
  sample:
    response:
      "YAML config generation Task succeeded for module 'sda_fabric_multicast_workflow_manager'.":
        file_path: "/tmp/sda_fabric_multicast_workflow_manager_playbook_22_Apr_2025_21_43_26_379.yml"
    version: "2.3.7.9"

response_error:
  description: Error response when playbook generation fails.
  returned: on failure
  type: dict
  contains:
    response:
      description: Empty list or error details.
      type: list
      returned: always
      sample: []
    msg:
      description:
      - Detailed error message explaining the failure reason.
      - May include validation errors, API call failures, or file write errors.
      type: str
      returned: always
      sample: "Invalid parameters in playbook: ['unknown_parameter']"
    version:
      description: Cisco Catalyst Center version.
      type: str
      returned: always
      sample: "2.3.7.9"
  sample:
    response: []
    msg: >-
      The specified version '2.3.5.3' does not support the YAML Playbook generation
      for SDA FABRIC MULTICAST Module. Supported versions start from '2.3.7.9' onwards.
    version: "2.3.5.3"

msg:
  description:
  - Status message providing additional context about the operation.
  - Includes details about configurations processed, files generated, or errors
    encountered.
  returned: always
  type: str
  sample: "Successfully collected all parameters from the playbook for SDA Fabric Multicast playbook generation operations."

status:
  description:
  - Current status of the operation (success, failed, invalid).
  returned: always
  type: str
  sample: "success"

changed:
  description:
  - Indicates whether any changes were made.
  - Always C(false) for this module as it only reads configurations and
    generates playbooks.
  returned: always
  type: bool
  sample: false
"""

from ansible.module_utils.basic import AnsibleModule
from ansible_collections.cisco.dnac.plugins.module_utils.brownfield_helper import (
    BrownFieldHelper,
)
from ansible_collections.cisco.dnac.plugins.module_utils.dnac import (
    DnacBase,
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


class SdaFabricMulticastPlaybookGenerator(DnacBase, BrownFieldHelper):
    """
    Brownfield playbook generator for SDA fabric multicast configurations.

    Attributes:
        supported_states (list): List of supported Ansible states (currently only 'gathered').
        module_schema (dict): Workflow filters schema defining network elements and API mappings.
        site_id_name_dict (dict): Cached mapping of site IDs to hierarchical site names.
        fabric_id_replication_mode_dict (dict): Cached mapping of fabric IDs to replication modes.
        module_name (str): Target module name for generated playbooks ('sda_fabric_multicast_workflow_manager').

    Description:
        Retrieves existing SDA fabric multicast configurations from Cisco Catalyst Center and
        generates YAML playbooks compatible with the sda_fabric_multicast_workflow_manager module.
        Supports selective filtering by fabric sites and Layer 3 virtual networks, or complete
        auto-discovery mode to retrieve all configurations. Transforms API responses using reverse
        parameter mapping to create playbook-ready YAML files with proper parameter names and structure.

        Key capabilities include:
        - Fabric site and zone identification and validation
        - Replication mode transformation (NATIVE_MULTICAST/HEADEND_REPLICATION)
        - Network device ID to management IP address conversion
        - SSM (Source-Specific Multicast) range extraction
        - ASM (Any-Source Multicast) RP configuration processing
        - Component-specific and global filtering support
        - Auto-generated or custom file path specification

        Requires Cisco Catalyst Center version 2.3.7.9 or higher for SDA fabric multicast API support.
    """

    def __init__(self, module):
        """
        Initialize the SdaFabricMulticastPlaybookGenerator instance.

        Parameters:
            module (AnsibleModule): The Ansible module instance.

        Returns:
            None

        Description:
            Initializes the playbook generator by setting up supported states, retrieving
            workflow filters schema, caching site ID mappings, and fabric replication mode mappings.
        """
        self.supported_states = ["gathered"]
        super().__init__(module)
        self.module_schema = self.get_workflow_filters_schema()
        self.log("Retrieved workflow filters schema for module initialization", "DEBUG")
        self.site_id_name_dict = self.get_site_id_name_mapping()
        self.log(
            f"Cached {len(self.site_id_name_dict)} site ID to name mappings", "DEBUG"
        )
        self.fabric_id_replication_mode_dict = (
            self.get_fabric_id_replication_mode_mapping()
        )
        self.log(
            f"Cached {len(self.fabric_id_replication_mode_dict)} fabric ID to replication mode mappings",
            "DEBUG",
        )
        self.module_name = "sda_fabric_multicast_workflow_manager"
        self.log(f"Module initialized: {self.module_name}", "INFO")

    def validate_input(self):
        """
        Validate input configuration parameters for the playbook.

        Parameters:
            None

        Returns:
            self: Instance with updated msg, status, and validated_config attributes.

        Description:
            Validates playbook configuration parameters against the expected schema. Sets
            validated_config on success or returns error status with invalid parameters details.
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
            "global_filters": {"type": "dict", "required": False},
        }

        # Import validate_list_of_dicts function here to avoid circular imports
        from ansible_collections.cisco.dnac.plugins.module_utils.dnac import (
            validate_list_of_dicts,
        )

        # Validate params
        self.log(
            f"Validating configuration against specification schema: {temp_spec}",
            "DEBUG",
        )
        valid_temp, invalid_params = validate_list_of_dicts(self.config, temp_spec)

        if invalid_params:
            self.msg = f"Invalid parameters in playbook: {invalid_params}"
            self.log(self.msg, "ERROR")
            self.set_operation_result("failed", False, self.msg, "ERROR")
            return self

        # Set the validated configuration and update the result with success status
        self.validated_config = valid_temp
        self.msg = f"Successfully validated playbook configuration parameters using 'validated_input': {valid_temp}"
        self.log(self.msg, "DEBUG")
        self.set_operation_result("success", False, self.msg, "INFO")
        return self

    def get_fabric_site_id_from_site_id(self, fabric_name, site_id):
        """
        Convert site_id to fabric_site_id using the get_fabric_sites API.

        Parameters:
            fabric_name (str): The hierarchical name of the fabric site.
            site_id (str): The site ID to convert.

        Returns:
            str: The fabric_site_id if the site is a fabric site, None otherwise.

        Description:
            Queries Cisco Catalyst Center to verify if the specified site is configured as a fabric site.
            If configured, retrieves and returns the fabric site ID. Returns None if the site is not
            a fabric site or if an error occurs during retrieval.
        """
        self.log(
            f"Attempting to retrieve fabric_site_id for site '{fabric_name}' with site_id: {site_id}",
            "DEBUG",
        )
        if not fabric_name or not site_id:
            self.log(
                "Invalid fabric_name or site_id provided for fabric zone lookup",
                "WARNING",
            )
            return None

        try:
            response = self.dnac._exec(
                family="sda",
                function="get_fabric_sites",
                op_modifies=False,
                params={"site_id": site_id},
            )
            self.log(
                f"Response from 'get_fabric_sites' for site '{fabric_name}': {response}",
                "DEBUG",
            )

            if not isinstance(response, dict):
                self.log(
                    f"Invalid response type from 'get_fabric_sites' for site '{fabric_name}'",
                    "WARNING",
                )
                return None

            fabric_sites = response.get("response")
            if not fabric_sites or len(fabric_sites) == 0:
                self.log(
                    f"Site '{fabric_name}' (site_id: {site_id}) is not a fabric site",
                    "DEBUG",
                )
                return None

            fabric_site_id = fabric_sites[0].get("id")
            self.log(
                f"Successfully retrieved fabric_site_id '{fabric_site_id}' for site '{fabric_name}'",
                "DEBUG",
            )
            return fabric_site_id

        except Exception as e:
            self.log(
                f"Error retrieving fabric_site_id for site '{fabric_name}' (site_id: {site_id}): {str(e)}",
                "WARNING",
            )
            return None

    def get_fabric_zone_id_from_site_id(self, fabric_name, site_id):
        """
        Convert site_id to fabric_zone_id using the get_fabric_zones API.

        Parameters:
            fabric_name (str): The hierarchical name of the fabric zone.
            site_id (str): The site ID to convert.

        Returns:
            str: The fabric_zone_id if the site is a fabric zone, None otherwise.

        Description:
            Calls the 'get_fabric_zones' API with the site_id parameter to check if the site
            is configured as a fabric zone and retrieve its fabric_id.
        """
        self.log(
            f"Attempting to retrieve fabric_zone_id for site '{fabric_name}' with site_id: {site_id}",
            "DEBUG",
        )

        if not fabric_name or not site_id:
            self.log(
                "Invalid fabric_name or site_id provided for fabric zone lookup",
                "WARNING",
            )
            return None

        try:
            response = self.dnac._exec(
                family="sda",
                function="get_fabric_zones",
                op_modifies=False,
                params={"site_id": site_id},
            )
            self.log(
                f"Response from 'get_fabric_zones' for site '{fabric_name}': {response}",
                "DEBUG",
            )

            if not isinstance(response, dict):
                self.log(
                    f"Invalid response type from 'get_fabric_zones' for site '{fabric_name}'",
                    "WARNING",
                )
                return None

            fabric_zones = response.get("response")
            if not fabric_zones or len(fabric_zones) == 0:
                self.log(
                    f"Site '{fabric_name}' (site_id: {site_id}) is not a fabric zone",
                    "DEBUG",
                )
                return None

            fabric_zone_id = fabric_zones[0].get("id")
            self.log(
                f"Successfully retrieved fabric_zone_id '{fabric_zone_id}' for site '{fabric_name}'",
                "DEBUG",
            )
            return fabric_zone_id

        except Exception as e:
            self.log(
                f"Error retrieving fabric_zone_id for site '{fabric_name}' (site_id: {site_id}): {str(e)}",
                "WARNING",
            )
            return None

    def get_workflow_filters_schema(self):
        """
        Retrieves the workflow filters schema for the fabric multicast module.

        This method defines and returns a dictionary schema that contains configuration
        for network elements related to fabric multicast. The schema includes
        filters, reverse mapping functions, API functions, API families, and getter
        functions for each network element type.

        Parameters:
            self (object): An instance of the SdaFabricMulticastPlaybookGenerator class.

        Returns:
            dict: A dictionary containing the workflow filters schema with the following structure:
                - network_elements (dict): Contains configuration for different network element types
                    - fabric_multicast (dict): Configuration for fabric multicast operations
                        - filters (list): List of filter parameters (fabric_name, layer3_virtual_network)
                        - reverse_mapping_function (method): Function to map fabric multicast specifications
                        - api_function (str): API function name for retrieving fabric multicast
                        - api_family (str): API family identifier
                        - get_function_name (method): Method to get fabric multicast configuration
                - global_filters (list): List of global filters (currently empty)

        Description:
            Constructs and returns a schema dictionary that defines how fabric multicast data
            should be processed, including filter parameters, API functions, and getter methods
            for retrieving configurations from Cisco Catalyst Center.
        """
        self.log(
            "Retrieving workflow filters schema for fabric multicast module.", "DEBUG"
        )

        schema = {
            "network_elements": {
                "fabric_multicast": {
                    "filters": ["fabric_name", "layer3_virtual_network"],
                    "reverse_mapping_function": self.fabric_multicast_temp_spec,
                    "api_function": "get_multicast_virtual_networks",
                    "api_family": "sda",
                    "get_function_name": self.get_fabric_multicast_configuration,
                },
            },
            "global_filters": [],
        }

        network_elements = list(schema["network_elements"].keys())
        self.log(
            f"Workflow filters schema generated successfully with {len(network_elements)} network element(s): {network_elements}",
            "INFO",
        )

        return schema

    def get_fabric_multicast_configuration(
        self, network_element, component_specific_filters=None
    ):
        """
        Retrieve and process fabric multicast configuration from Cisco Catalyst Center.

        Parameters:
            network_element (dict): Network element configuration containing API details.
            component_specific_filters (list, optional): List of filter dicts with fabric_name
                                                         and/or layer3_virtual_network keys.

        Returns:
            dict: Dictionary with 'fabric_multicast' key containing list of processed multicast
                  configurations modified according to fabric_multicast_temp_spec template.

        Description:
            Fetches fabric multicast details using component-specific filters or retrieves all
            available configurations. Processes the multicast information and transforms it
            using reverse mapping functions to generate playbook-compatible parameters.
        """

        self.log(
            f"Starting to retrieve fabric multicast configuration with network element: {network_element} and "
            f"component-specific filters: {component_specific_filters}",
            "DEBUG",
        )

        # Extract API details from network_element
        api_family = network_element.get("api_family")
        api_function = network_element.get("api_function")

        self.log(
            f"Using API family: {api_family}, function: {api_function}",
            "DEBUG",
        )

        all_multicast_configs = []

        if component_specific_filters:
            self.log(
                f"Processing {len(component_specific_filters)} component-specific filter(s) for fabric multicast configuration.",
                "INFO",
            )

            for filter_index, filter_param in enumerate(
                component_specific_filters, start=1
            ):
                self.log(
                    f"Processing filter {filter_index}/{len(component_specific_filters)}: {filter_param}",
                    "DEBUG",
                )

                # Build API params based on filter
                params = {}
                fabric_name = filter_param.get("fabric_name")
                layer3_vn = filter_param.get("layer3_virtual_network")

                if fabric_name:
                    # Get site ID from cached site_id_name_dict mapping (reverse lookup)
                    site_id = None
                    for (
                        cached_site_id,
                        cached_site_name,
                    ) in self.site_id_name_dict.items():
                        if cached_site_name == fabric_name:
                            self.log(
                                f"Found matching site: fabric_name '{fabric_name}' maps to site_id '{site_id}'",
                                "DEBUG",
                            )
                            site_id = cached_site_id
                            break

                    if not site_id:
                        self.log(
                            f"Site '{fabric_name}' does not exist in Cisco Catalyst Center (not found in cached mapping). Skipping.",
                            "WARNING",
                        )
                        continue

                    self.log(
                        f"Resolved fabric_name '{fabric_name}' to site_id: {site_id} (from cache)",
                        "DEBUG",
                    )

                    # Convert site_id to fabric_id (try fabric_site first, then fabric_zone)
                    fabric_id = self.get_fabric_site_id_from_site_id(
                        fabric_name, site_id
                    )
                    if not fabric_id:
                        self.log(
                            f"Site '{fabric_name}' is not a fabric site. Trying fabric zone...",
                            "DEBUG",
                        )
                        fabric_id = self.get_fabric_zone_id_from_site_id(
                            fabric_name, site_id
                        )

                    if not fabric_id:
                        self.log(
                            f"Site '{fabric_name}' exists but is not configured as a fabric site or fabric zone. Skipping.",
                            "WARNING",
                        )
                        continue

                    params["fabric_id"] = fabric_id
                    self.log(
                        f"Successfully resolved fabric_name '{fabric_name}' to fabric_id: {fabric_id}",
                        "INFO",
                    )

                if layer3_vn:
                    params["virtual_network_name"] = layer3_vn
                    self.log(
                        f"Added Layer 3 virtual network filter: '{layer3_vn}'", "DEBUG"
                    )

                # Call the API to get multicast virtual networks
                try:
                    self.log(
                        f"Querying API with parameters: {params} for filter {filter_index}",
                        "DEBUG",
                    )

                    multicast_response = self.execute_get_with_pagination(
                        api_family, api_function, params
                    )

                    if not multicast_response:
                        self.log(
                            f"No multicast configurations found for filter: {filter_param}",
                            "WARNING",
                        )
                        continue

                    self.log(
                        f"Retrieved {len(multicast_response)} multicast configuration(s) for filter: {filter_param}",
                        "INFO",
                    )
                    all_multicast_configs.extend(multicast_response)

                except Exception as e:
                    self.log(
                        f"Error retrieving multicast configurations for filter {filter_param}: {str(e)}",
                        "ERROR",
                    )

        else:
            # No filters - retrieve all multicast configurations
            self.log(
                "No component-specific filters provided. Retrieving all fabric multicast configurations.",
                "INFO",
            )

            try:
                self.log(
                    "Querying all fabric multicast configurations from Cisco Catalyst Center",
                    "DEBUG",
                )
                multicast_response = self.execute_get_with_pagination(
                    api_family, api_function, {}
                )

                if multicast_response:
                    self.log(
                        f"Retrieved {len(multicast_response)} total multicast configuration(s)",
                        "INFO",
                    )
                    all_multicast_configs.extend(multicast_response)
                else:
                    self.log(
                        "No multicast configurations found in Cisco Catalyst Center",
                        "WARNING",
                    )

            except Exception as e:
                self.log(
                    f"Error retrieving all multicast configurations: {str(e)}", "ERROR"
                )

        self.log(
            f"Total multicast configurations collected for processing: {len(all_multicast_configs)}",
            "INFO",
        )

        if not all_multicast_configs:
            self.log(
                "No multicast configurations to process. Returning empty fabric_multicast list.",
                "WARNING",
            )
            return {"fabric_multicast": []}

        # Modify multicast details using temp_spec
        self.log(
            "Retrieving fabric multicast template specification for parameter transformation",
            "DEBUG",
        )
        fabric_multicast_temp_spec = self.fabric_multicast_temp_spec()

        self.log(
            f"Transforming {len(all_multicast_configs)} multicast configuration(s) using reverse mapping",
            "DEBUG",
        )
        multicast_details = self.modify_parameters(
            fabric_multicast_temp_spec, all_multicast_configs
        )

        self.log(
            f"Successfully transformed {len(multicast_details)} multicast configuration(s)",
            "INFO",
        )

        modified_multicast_details = {"fabric_multicast": multicast_details}

        self.log(
            f"Transformed fabric multicast details (count: {len(multicast_details)}): {self.pprint(modified_multicast_details)}",
            "INFO",
        )

        self.log(
            "Completed fabric multicast configuration retrieval and processing.",
            "DEBUG",
        )

        return modified_multicast_details

    def get_fabric_id_replication_mode_mapping(self):
        """
        Retrieve and cache replication mode for all fabric sites.

        Parameters:
            None

        Returns:
            dict: Mapping of fabric IDs to their replication modes (NATIVE_MULTICAST or HEADEND_REPLICATION).

        Description:
            Calls the get_multicast API to retrieve all multicast configurations and builds
            a cached dictionary mapping fabric IDs to their configured replication modes.
        """
        self.log(
            "Retrieving fabric ID to replication mode mapping from Cisco Catalyst Center.",
            "INFO",
        )

        fabric_replication_map = {}

        try:
            # Call the get_multicast API to retrieve all multicast configurations
            self.log(
                "Calling 'get_multicast' API to retrieve replication mode data.",
                "DEBUG",
            )

            response = self.dnac._exec(
                family="sda", function="get_multicast", params={}
            )

            self.log(f"Response received from 'get_multicast': {response}", "DEBUG")

            multicast_list = response.get("response", [])

            if not multicast_list:
                self.log(
                    "No multicast configurations found in Cisco Catalyst Center.",
                    "WARNING",
                )
                return fabric_replication_map

            self.log(
                f"Processing {len(multicast_list)} multicast configuration(s) for replication mode mapping",
                "DEBUG",
            )

            # Build the mapping dictionary
            for config_index, multicast_config in enumerate(multicast_list, start=1):
                self.log(
                    f"Processing multicast configuration {config_index}/{len(multicast_list)}",
                    "DEBUG",
                )
                fabric_id = multicast_config.get("fabricId")
                replication_mode = multicast_config.get("replicationMode")

                if not fabric_id or not replication_mode:
                    self.log(
                        f"Configuration {config_index} missing fabricId or replicationMode. Skipping entry.",
                        "WARNING",
                    )
                    continue

                fabric_replication_map[fabric_id] = replication_mode
                self.log(
                    f"Mapped fabric_id '{fabric_id}' to replication_mode '{replication_mode}'",
                    "DEBUG",
                )

            self.log(
                f"Successfully cached {len(fabric_replication_map)} fabric replication mode mapping(s).",
                "INFO",
            )

        except Exception as e:
            self.log(
                f"Error retrieving replication mode mappings: {str(e)}",
                "ERROR",
            )

        return fabric_replication_map

    def fabric_multicast_temp_spec(self):
        """
        Generate temporary specification dictionary for fabric multicast configuration.

        Parameters:
            None

        Returns:
            OrderedDict: Structured specification dictionary defining fabric multicast parameters,
                         including replication_mode, fabric_name, layer3_virtual_network, ip_pool_name, ssm, and asm.

        Description:
            Creates an ordered dictionary that defines the parameter structure for fabric multicast
            configurations, including source keys, transform functions, and validation rules for
            reverse mapping API responses to playbook parameters.
        """
        self.log("Generating temporary specification for fabric multicast.", "DEBUG")
        fabric_multicast = OrderedDict(
            {
                "replication_mode": {
                    "type": "str",
                    "choices": ["NATIVE_MULTICAST", "HEADEND_REPLICATION"],
                    "default": "NATIVE_MULTICAST",
                    "special_handling": True,
                    "transform": self.transform_replication_mode,
                },
                "fabric_name": {
                    "type": "str",
                    "required": True,
                    "source_key": "fabricId",
                    "transform": self.transform_fabric_name,
                },
                "layer3_virtual_network": {
                    "type": "str",
                    "source_key": "virtualNetworkName",
                },
                "ip_pool_name": {
                    "type": "str",
                    "source_key": "ipPoolName",
                },
                "ssm": {
                    "type": "dict",
                    "ipv4_ssm_ranges": {
                        "type": "list",
                        "elements": "str",
                        "source_key": "ipv4SsmRanges",
                    },
                    "special_handling": True,
                    "transform": self.transform_ssm_ranges,
                },
                "asm": {
                    "type": "list",
                    "elements": "dict",
                    "source_key": "multicastRPs",
                    "special_handling": True,
                    "transform": self.transform_asm_rps,
                    "options": {
                        "rp_device_location": {
                            "type": "str",
                            "choices": ["FABRIC", "EXTERNAL"],
                            "source_key": "rpDeviceLocation",
                        },
                        "network_device_ips": {
                            "type": "list",
                            "elements": "str",
                            "source_key": "networkDeviceIds",
                        },
                        "ex_rp_ipv4_address": {
                            "type": "str",
                            "source_key": "ipv4Address",
                        },
                        "is_default_v4_rp": {
                            "type": "bool",
                            "source_key": "isDefaultV4RP",
                        },
                        "ipv4_asm_ranges": {
                            "type": "list",
                            "elements": "str",
                            "source_key": "ipv4AsmRanges",
                        },
                        "ex_rp_ipv6_address": {
                            "type": "str",
                            "source_key": "ipv6Address",
                        },
                        "is_default_v6_rp": {
                            "type": "bool",
                            "source_key": "isDefaultV6RP",
                        },
                        "ipv6_asm_ranges": {
                            "type": "list",
                            "elements": "str",
                            "source_key": "ipv6AsmRanges",
                        },
                    },
                },
            }
        )

        parameter_count = len(fabric_multicast)
        self.log(
            f"Successfully built fabric multicast specification with {parameter_count} top-level parameter(s)",
            "DEBUG",
        )

        return fabric_multicast

    def transform_fabric_name(self, fabric_id):
        """
        Transform fabric ID to fabric site name hierarchy.

        Parameters:
            fabric_id (str): The fabric ID to transform.

        Returns:
            str: Hierarchical site name or None if fabric_id is invalid.

        Description:
            Analyzes the fabric ID to extract the site ID and fabric type, then retrieves
            the hierarchical site name from the cached site_id_name_dict mapping.
        """
        self.log(
            f"Transforming fabric name for fabric_id: {fabric_id}",
            "DEBUG",
        )

        if not fabric_id:
            self.log("No fabric ID provided for transformation", "WARNING")
            return None

        self.log(
            f"Analyzing fabric_id '{fabric_id}' to extract site_id and fabric_type",
            "DEBUG",
        )
        site_id, fabric_type = self.analyse_fabric_site_or_zone_details(fabric_id)
        self.log(
            f"Analyzed fabric_id {fabric_id}: site_id={site_id}, fabric_type={fabric_type}",
            "DEBUG",
        )

        site_name_hierarchy = self.site_id_name_dict.get(site_id, None)
        if not site_name_hierarchy:
            self.log(
                f"Site name not found in cache for site_id '{site_id}' (fabric_id: '{fabric_id}')",
                "WARNING",
            )
            return None

        self.log(
            f"Successfully transformed fabric_id '{fabric_id}' to site name '{site_name_hierarchy}'",
            "INFO",
        )
        return site_name_hierarchy

    def transform_replication_mode(self, multicast_details):
        """
        Transform fabric ID to its corresponding replication mode using cached data.

        Parameters:
            multicast_details (dict): Multicast configuration details containing fabricId.

        Returns:
            str: Replication mode (NATIVE_MULTICAST or HEADEND_REPLICATION), defaults to NATIVE_MULTICAST.

        Description:
            Extracts the fabric ID from multicast details and retrieves the replication mode
            from the cached fabric_id_replication_mode_dict mapping.
        """
        self.log(
            f"Transforming replication mode for multicast details: {multicast_details}",
            "DEBUG",
        )

        fabric_id = multicast_details.get("fabricId")
        if not fabric_id:
            self.log(
                "No fabric ID found in multicast details, using default NATIVE_MULTICAST",
                "WARNING",
            )
            return "NATIVE_MULTICAST"  # Default value

        replication_mode = self.fabric_id_replication_mode_dict.get(fabric_id)

        if not replication_mode:
            self.log(
                f"No replication mode found for fabric ID '{fabric_id}', using default NATIVE_MULTICAST",
                "WARNING",
            )
            return "NATIVE_MULTICAST"

        self.log(
            f"Transformed fabric ID '{fabric_id}' to replication mode '{replication_mode}'",
            "DEBUG",
        )
        return replication_mode

    def get_device_ips_from_ids(self, multicast_rp_details):
        """
        Transform network device IDs to their management IP addresses.

        Parameters:
            multicast_rp_details (dict): Multicast RP configuration details containing networkDeviceIds.

        Returns:
            list: Management IP addresses corresponding to the device IDs, or empty list if none found.

        Description:
            Retrieves device ID to management IP mapping and transforms the networkDeviceIds
            from the multicast RP details into their corresponding management IP addresses.
        """
        self.log(
            f"Transforming device IDs to IPs for multicast RP details: {multicast_rp_details}",
            "DEBUG",
        )

        network_device_ids = multicast_rp_details.get("networkDeviceIds", [])
        if not network_device_ids:
            self.log("No network device IDs found in multicast RP details", "DEBUG")
            return []

        device_ips = []

        # Get device ID to management IP mapping
        device_id_to_ip_map = self.get_device_id_management_ip_mapping()
        self.log(
            f"Retrieved device ID to management IP mapping with {len(device_id_to_ip_map)} entries",
            "DEBUG",
        )
        self.log(
            f"Processing {len(network_device_ids)} device ID(s) for IP transformation",
            "DEBUG",
        )

        for device_index, device_id in enumerate(network_device_ids, start=1):
            self.log(
                f"Processing device {device_index}/{len(network_device_ids)}: device_id '{device_id}'",
                "DEBUG",
            )
            device_ip = device_id_to_ip_map.get(device_id)
            if device_ip:
                device_ips.append(device_ip)
                self.log(
                    f"Mapped device ID '{device_id}' to IP '{device_ip}'",
                    "DEBUG",
                )
            else:
                self.log(
                    f"Could not find IP for device ID '{device_id}'",
                    "WARNING",
                )

        self.log(
            f"Transformed {len(network_device_ids)} device ID(s) to {len(device_ips)} IP(s): {device_ips}",
            "DEBUG",
        )
        return device_ips

    def transform_ssm_ranges(self, multicast_details):
        """
        Transform SSM ranges from multicast configuration details.

        Parameters:
            multicast_details (dict): Multicast configuration details containing ipv4SsmRanges.

        Returns:
            dict: Dictionary with 'ipv4_ssm_ranges' key or None if no SSM ranges configured.

        Description:
            Extracts IPv4 SSM (Source-Specific Multicast) ranges from the multicast details
            and transforms them into the playbook-compatible format with ipv4_ssm_ranges key.
        """
        self.log(
            f"Transforming SSM ranges for multicast details: {multicast_details}",
            "DEBUG",
        )

        ipv4_ssm_ranges = multicast_details.get("ipv4SsmRanges", [])

        if not ipv4_ssm_ranges:
            self.log("No IPv4 SSM ranges found in multicast details", "DEBUG")
            return None

        self.log(
            f"Transformed SSM ranges with {len(ipv4_ssm_ranges)} range(s): {ipv4_ssm_ranges}",
            "DEBUG",
        )
        return {"ipv4_ssm_ranges": ipv4_ssm_ranges}

    def transform_asm_rps(self, multicast_details):
        """
        Transform ASM Rendezvous Point configurations from multicast details.

        Parameters:
            multicast_details (dict): Multicast configuration details containing multicastRPs.

        Returns:
            list: Processed multicast RP configurations with reverse-mapped parameters, or None if no RPs configured.

        Description:
            Processes Any-Source Multicast (ASM) Rendezvous Point configurations by applying
            reverse mapping to each RP's parameters, converting device IDs to IPs, and handling
            FABRIC vs EXTERNAL location-specific transformations.
        """
        self.log(
            f"Transforming ASM RPs for multicast details: {multicast_details}",
            "DEBUG",
        )

        multicast_rps = multicast_details.get("multicastRPs", [])

        if not multicast_rps:
            self.log("No multicast RPs found in multicast details", "DEBUG")
            return None

        self.log(
            f"Found {len(multicast_rps)} multicast RP(s) to transform",
            "DEBUG",
        )

        # Get the ASM options spec for reverse mapping
        self.log(
            "Retrieving ASM options specification for reverse parameter mapping",
            "DEBUG",
        )
        asm_spec = self.fabric_multicast_temp_spec().get("asm", {})
        asm_options = asm_spec.get("options", {})

        # Get device ID to management IP mapping once for all RPs
        self.log(
            "Retrieving device ID to management IP mapping for all RPs",
            "DEBUG",
        )
        device_id_to_ip_map = self.get_device_id_management_ip_mapping()
        self.log(
            f"Retrieved mapping dictionary with {len(device_id_to_ip_map)} device entry/entries",
            "DEBUG",
        )

        # Process each multicast RP with reverse mapping
        processed_rps = []
        for rp_index, rp_details in enumerate(multicast_rps, start=1):
            self.log(
                f"Processing multicast RP {rp_index}/{len(multicast_rps)}: {rp_details}",
                "DEBUG",
            )

            # Apply reverse mapping to this RP using the options spec directly
            processed_rp = self.modify_parameters(asm_options, [rp_details])
            self.log(
                f"Applied reverse mapping to RP {rp_index}, result: {self.pprint(processed_rp)}",
                "DEBUG",
            )

            if not processed_rp:
                self.log(
                    f"Reverse mapping returned empty result for RP {rp_index}. Skipping.",
                    "WARNING",
                )
                continue

            self.log(
                f"Successfully applied reverse mapping to RP {rp_index}",
                "DEBUG",
            )
            # Post-process to convert network device IDs to IPs
            for inner_rp_index, rp in enumerate(processed_rp, start=1):
                self.log(
                    f"Post-processing transformed RP {inner_rp_index}/{len(processed_rp)} from source RP {rp_index}",
                    "DEBUG",
                )
                # Check rp_device_location to determine how to handle IP addresses
                rp_device_location = rp.get("rp_device_location")
                self.log(
                    f"RP {rp_index}.{inner_rp_index} device location: {rp_device_location}",
                    "DEBUG",
                )

                if rp_device_location == "FABRIC":
                    # For FABRIC location, ignore/remove ipv4Address and ipv6Address
                    self.log(
                        "RP device location is FABRIC - removing ex_rp_ipv4_address and ex_rp_ipv6_address fields",
                        "DEBUG",
                    )
                    rp.pop("ex_rp_ipv4_address", None)
                    rp.pop("ex_rp_ipv6_address", None)

                # Handle network device IDs to IPs conversion
                if "network_device_ips" in rp and rp["network_device_ips"]:
                    device_ids = rp["network_device_ips"]
                    self.log(
                        f"Converting {len(device_ids)} device ID(s) to IPs", "DEBUG"
                    )
                    device_ips = []
                    for device_index, device_id in enumerate(device_ids, start=1):
                        self.log(
                            f"Processing device {device_index}/{len(device_ids)} for RP {rp_index}.{inner_rp_index}: device_id '{device_id}'",
                            "DEBUG",
                        )
                        device_ip = device_id_to_ip_map.get(device_id)
                        if device_ip:
                            device_ips.append(device_ip)
                            self.log(
                                f"Mapped device ID '{device_id}' to IP '{device_ip}'",
                                "DEBUG",
                            )
                        else:
                            self.log(
                                f"Could not find IP for device ID '{device_id}'",
                                "WARNING",
                            )
                    rp["network_device_ips"] = device_ips if device_ips else None
                    self.log(
                        f"Final network_device_ips for RP: {rp['network_device_ips']}",
                        "DEBUG",
                    )

            processed_rps.extend(processed_rp)
            self.log(
                f"Successfully processed RP {rp_index}: {processed_rp}",
                "DEBUG",
            )

        self.log(
            f"Completed transformation of {len(processed_rps)} multicast RP(s)",
            "INFO",
        )

        return processed_rps if processed_rps else None

    def yaml_config_generator(self, yaml_config_generator):
        """
        Generate YAML configuration file based on provided parameters.

        Parameters:
            yaml_config_generator (dict): Configuration containing file_path, global_filters,
                                          component_specific_filters, and generate_all_configurations.

        Returns:
            self: Instance with updated operation result and message.

        Description:
            Retrieves network element details using filters, processes the data, and writes
            the YAML content to the specified file. Supports auto-discovery mode to retrieve
            all configurations when generate_all_configurations is enabled.
        """

        self.log(
            f"Starting YAML config generation with parameters: {yaml_config_generator}",
            "DEBUG",
        )

        # Check if generate_all_configurations mode is enabled
        generate_all = yaml_config_generator.get("generate_all_configurations", False)
        self.log(f"Generate all configurations mode: {generate_all}", "DEBUG")

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
            self.log(f"Generated default filename: {file_path}", "DEBUG")
        else:
            self.log(f"Using user-provided file_path: {file_path}", "DEBUG")

        self.log(f"YAML configuration file path determined: {file_path}", "INFO")

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

        # Retrieve the supported network elements for the module
        self.log(
            "Retrieving supported network elements from module schema",
            "DEBUG",
        )
        module_supported_network_elements = self.module_schema.get(
            "network_elements", {}
        )

        self.log(
            f"Module supports {len(module_supported_network_elements)} network element type(s): "
            f"{list(module_supported_network_elements.keys())}",
            "DEBUG",
        )

        components_list = component_specific_filters.get(
            "components_list", module_supported_network_elements.keys()
        )
        self.log(f"Components to process: {list(components_list)}", "INFO")

        final_list = []
        for component in components_list:
            self.log(f"Processing component: {component}", "DEBUG")
            network_element = module_supported_network_elements.get(component)
            if not network_element:
                self.log(
                    f"Skipping unsupported network element: {component}",
                    "WARNING",
                )
                continue

            filters = component_specific_filters.get(component, [])
            self.log(f"Filters for component '{component}': {filters}", "DEBUG")
            operation_func = network_element.get("get_function_name")
            if callable(operation_func):
                self.log(
                    f"Calling operation function for component '{component}'", "DEBUG"
                )
                details = operation_func(network_element, filters)
                self.log(f"Details retrieved for '{component}': {details}", "DEBUG")
                final_list.append(details)
            else:
                self.log(
                    f"No callable operation function found for component '{component}'",
                    "WARNING",
                )

        if not final_list:
            self.msg = f"No configurations or components to process for module '{self.module_name}'. Verify input filters or configuration."
            self.log(self.msg, "WARNING")
            self.set_operation_result("ok", False, self.msg, "INFO")
            return self

        final_dict = {"config": final_list}
        self.log(
            f"Final dictionary created with {len(final_list)} component(s): {final_dict}",
            "DEBUG",
        )

        self.log(f"Writing YAML configuration to file: {file_path}", "INFO")
        if self.write_dict_to_yaml(final_dict, file_path):
            self.msg = {
                f"YAML config generation Task succeeded for module '{self.module_name}'.": {
                    "file_path": file_path
                }
            }
            self.log(f"Successfully wrote YAML configuration to {file_path}", "INFO")
            self.set_operation_result("success", True, self.msg, "INFO")
        else:
            self.msg = {
                f"YAML config generation Task failed for module '{self.module_name}'.": {
                    "file_path": file_path
                }
            }
            self.log(f"Failed to write YAML configuration to {file_path}", "ERROR")
            self.set_operation_result("failed", True, self.msg, "ERROR")

        return self

    def get_want(self, config, state):
        """
        Create parameters for API calls based on the specified state.

        Parameters:
            config (dict): Configuration data for the network elements.
            state (str): Desired state of the network elements ('gathered').

        Returns:
            self: Instance with updated want, msg, and status attributes.

        Description:
            Prepares the parameters required for SDA fabric multicast playbook generation
            operations based on the desired state. Sets the yaml_config_generator in the
            want dictionary and logs detailed information for tracking.
        """

        self.log(f"Creating Parameters for API Calls with state: {state}", "INFO")

        want = {}

        # Add yaml_config_generator to want
        want["yaml_config_generator"] = config
        self.log(
            f"yaml_config_generator added to want: {want['yaml_config_generator']}",
            "DEBUG",
        )

        self.want = want
        self.log(f"Desired State (want): {self.want}", "INFO")
        self.msg = "Successfully collected all parameters from the playbook for SDA Fabric Multicast playbook generation operations."
        self.status = "success"
        return self

    def get_diff_gathered(self):
        """
        Execute merge operations for YAML playbook generation.

        Parameters:
            None

        Returns:
            self: Instance with updated operation results.

        Description:
            Processes the yaml_config_generator operation by iterating through defined operations,
            checking for required parameters, and executing the YAML configuration file generation.
            Logs detailed timing and status information for each operation.
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
        self.log(
            f"Beginning iteration over {len(operations)} defined operation(s) for processing.",
            "DEBUG",
        )
        for index, (param_key, operation_name, operation_func) in enumerate(
            operations, start=1
        ):
            self.log(
                f"Iteration {index}/{len(operations)}: Checking parameters for '{operation_name}' operation with param_key '{param_key}'.",
                "DEBUG",
            )
            params = self.want.get(param_key)
            if params:
                self.log(
                    f"Iteration {index}/{len(operations)}: Parameters found for '{operation_name}'. Starting processing.",
                    "INFO",
                )
                operation_func(params).check_return_status()
            else:
                self.log(
                    f"Iteration {index}/{len(operations)}: No parameters found for '{operation_name}'. Skipping operation.",
                    "WARNING",
                )

        end_time = time.time()
        self.log(
            f"Completed 'get_diff_gathered' operation in {end_time - start_time:.2f} seconds.",
            "INFO",
        )

        return self


def main():
    """
    Main entry point for module execution.

    Parameters:
        None

    Returns:
        None

    Description:
        Initializes the Ansible module, creates the SdaFabricMulticastPlaybookGenerator instance,
        validates version compatibility, validates input parameters, processes configurations,
        and executes the playbook generation workflow.
    """
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
    ccc_sda_multicast_playbook_generator = SdaFabricMulticastPlaybookGenerator(module)
    if (
        ccc_sda_multicast_playbook_generator.compare_dnac_versions(
            ccc_sda_multicast_playbook_generator.get_ccc_version(), "2.3.7.9"
        )
        < 0
    ):
        ccc_version = ccc_sda_multicast_playbook_generator.get_ccc_version()
        ccc_sda_multicast_playbook_generator.msg = (
            f"The specified version '{ccc_version}' does not support the YAML Playbook generation "
            "for SDA FABRIC MULTICAST Module. Supported versions start from '2.3.7.9' onwards. "
        )
        ccc_sda_multicast_playbook_generator.set_operation_result(
            "failed", False, ccc_sda_multicast_playbook_generator.msg, "ERROR"
        ).check_return_status()

    # Get the state parameter from the provided parameters
    state = ccc_sda_multicast_playbook_generator.params.get("state")

    # Check if the state is valid
    if state not in ccc_sda_multicast_playbook_generator.supported_states:
        ccc_sda_multicast_playbook_generator.status = "invalid"
        ccc_sda_multicast_playbook_generator.msg = f"State '{state}' is invalid. Supported states: {ccc_sda_multicast_playbook_generator.supported_states}"
        ccc_sda_multicast_playbook_generator.log(
            ccc_sda_multicast_playbook_generator.msg, "ERROR"
        )
        ccc_sda_multicast_playbook_generator.check_recturn_status()

    # Validate the input parameters and check the return status
    ccc_sda_multicast_playbook_generator.validate_input().check_return_status()
    config = ccc_sda_multicast_playbook_generator.validated_config

    # Iterate over the validated configuration parameters
    for config in ccc_sda_multicast_playbook_generator.validated_config:
        ccc_sda_multicast_playbook_generator.reset_values()
        ccc_sda_multicast_playbook_generator.get_want(
            config, state
        ).check_return_status()
        ccc_sda_multicast_playbook_generator.get_diff_state_apply[
            state
        ]().check_return_status()

    ccc_sda_multicast_playbook_generator.log(
        f"All {len(ccc_sda_multicast_playbook_generator.validated_config)} configuration(s) processed successfully. Exiting module.",
        "INFO",
    )

    module.exit_json(**ccc_sda_multicast_playbook_generator.result)


if __name__ == "__main__":
    main()
