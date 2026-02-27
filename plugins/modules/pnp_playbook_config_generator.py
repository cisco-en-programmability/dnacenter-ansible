#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright (c) 2026, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

"""
Ansible module for generating PnP device inventory YAML playbooks.

Description:
    Generates YAML playbook files compatible with pnp_workflow_manager module by
    retrieving PnP device registrations from Cisco Catalyst Center, extracting
    essential device attributes including serial numbers, hostnames, device states,
    product IDs, and SUDI requirements, applying intelligent filtering based on
    device state, product family, and site location, transforming API responses to
    playbook-compatible format with proper parameter mapping, and creating structured
    YAML files ready for brownfield device management and documentation workflows.

Core Capabilities:
    - Retrieves PnP device inventory with basic device information from Catalyst
      Center PnP APIs
    - Discovers devices across all workflow states (Unclaimed, Planned, Onboarding,
      Provisioned, Error)
    - Extracts core device attributes (serial_number, hostname, state, pid,
      is_sudi_required, authorize)
    - Supports device state filtering at API level for efficient data retrieval
    - Enables device family filtering during post-retrieval processing
    - Provides site-based filtering with hierarchical name resolution
    - Transforms camelCase API responses to snake_case playbook parameters
    - Generates timestamped filenames when custom path not specified
    - Creates parent directories automatically for file path destinations
    - Provides comprehensive operation statistics with success/failure tracking

Supported Operations:
    - Gathered state for brownfield device discovery and YAML generation
    - Generate all mode for complete PnP inventory documentation
    - Selective filtering with state, family, and site criteria combinations
    - Single component mode supporting only device_info extraction
    - Multi-device processing with individual transformation error handling

API Integration:
    - device_onboarding_pnp.DeviceOnboardingPnp.get_device_list with optional
      state filtering
    - sites.Sites.get_sites for site name resolution during filtering operations

Data Transformation:
    - Maps deviceInfo.serialNumber to serial_number (required field)
    - Maps deviceInfo.hostname to hostname (optional field)
    - Maps deviceInfo.state to state with "Unclaimed" default value
    - Maps deviceInfo.pid to pid (required field)
    - Maps deviceInfo.sudiRequired to is_sudi_required (optional field)
    - Derives authorize flag from authOperation field (optional field)
    - Preserves OrderedDict structure for consistent YAML field ordering
    - Skips devices missing required fields (serial_number, pid)

Filtering Capabilities:
    - device_state: API-level filtering by PnP workflow state (Unclaimed, Planned,
      Onboarding, Provisioned, Error)
    - device_family: Post-retrieval filtering by product category (Switches and
      Hubs, Routers, Wireless Controller)
    - site_name: Post-retrieval filtering by hierarchical site with substring
      matching after UUID resolution
    - Smart validation skips None devices and invalid dictionary structures
    - Comprehensive coverage continues processing after individual device failures

Output Format:
    - YAML playbook compatible with pnp_workflow_manager module structure
    - Single configuration group with device_info key containing device list
    - Each device as separate OrderedDict entry with essential attributes only
    - Site IDs resolved to hierarchical names for human readability
    - Clean structure without site assignments, templates, or projects
    - Proper indentation and formatting for manual modification workflows

Minimum Requirements:
    - Cisco Catalyst Center version 2.3.7.9 or higher for PnP APIs
    - DNA Center SDK 2.9.3 or higher for API compatibility
    - Python 3.9 or higher for OrderedDict and type hint support
    - Read access to PnP and Sites APIs in Catalyst Center
    - Network connectivity to Catalyst Center management interface

Usage Patterns:
    - Brownfield PnP inventory documentation and compliance audits
    - Device discovery before bulk provisioning operations
    - Migration preparation between Catalyst Center instances
    - Compliance reporting with current device registration status
    - Template creation for standardized PnP device management
    - Disaster recovery documentation for PnP infrastructure state

Author: Syed Khadeer Ahmed, Madhan Sankaranarayanan
Version: 6.40.0
"""
from __future__ import absolute_import, division, print_function

__metaclass__ = type
__author__ = "Syed Khadeer Ahmed, Madhan Sankaranarayanan"

DOCUMENTATION = r"""
---
module: pnp_playbook_config_generator
short_description: Generate YAML playbook for PnP workflow with device information
description:
- Generates YAML configurations compatible with the pnp_workflow_manager module
  for brownfield infrastructure discovery and documentation.
- Retrieves existing PnP device information from Cisco Catalyst Center PnP
  inventory including serial numbers, hostnames, device states, product IDs,
  and SUDI requirements.
- Transforms API responses to playbook-compatible YAML format with parameter
  name mapping and structure optimization for Ansible execution.
- Supports comprehensive filtering capabilities including device state filters,
  device family filters, and site-based filtering for targeted device discovery.
- Enables automated brownfield discovery by retrieving all registered PnP
  devices when generate_all_configurations is enabled.
- Resolves site IDs to hierarchical site names for human-readable playbook
  generation.
- Creates structured playbook files ready for modification and redeployment
  through pnp_workflow_manager module.
- Extracts essential device attributes without site assignments, templates,
  projects, or advanced configuration parameters.
- Supports extraction of both claimed and unclaimed devices across all PnP
  workflow states.
version_added: 6.40.0
extends_documentation_fragment:
- cisco.dnac.workflow_manager_params
author:
- Syed Khadeer Ahmed (@syed-khadeerahmed)
- Madhan Sankaranarayanan (@madhansansel)
options:
  state:
    description:
      - Desired state for module execution controlling playbook generation
        workflow.
      - Only 'gathered' state is supported for retrieving configurations from
        Catalyst Center.
      - The 'gathered' state initiates device discovery, API calls,
        transformation, and YAML file generation.
    type: str
    choices: [gathered]
    default: gathered
  config:
    description:
      - List of configuration filters controlling YAML playbook generation
        behavior.
      - Each configuration item defines output file path, component selection,
        and filtering criteria.
      - Supports multiple configuration items for generating separate playbook
        files with different filter combinations.
      - When generate_all_configurations is True, automatically includes all
        PnP devices unless filters are explicitly specified.
    type: list
    elements: dict
    required: true
    suboptions:
      generate_all_configurations:
        description:
          - When True, automatically retrieves all PnP device configurations
            from Catalyst Center.
          - Discovers all devices in PnP inventory and extracts basic device
            information.
          - Makes component_specific_filters optional by using default values
            when not provided.
          - Sets default components_list to ['device_info'] if not explicitly
            specified.
          - Useful for complete brownfield PnP inventory documentation and
            discovery workflows.
          - When False, requires explicit component_specific_filters
            configuration with components_list.
        type: bool
        required: false
        default: false
      file_path:
        description:
          - Absolute or relative path where generated YAML configuration file
            will be saved.
          - If not provided, file is saved in current working directory with
            auto-generated filename.
          - Filename format when auto-generated is
            "pnp_workflow_manager_playbook_<YYYY-MM-DD_HH-MM-SS>.yml".
          - Example auto-generated filename
            "pnp_workflow_manager_playbook_2026-02-06_14-30-45.yml".
          - Parent directories are created automatically if they do not exist.
          - File is overwritten if it already exists at the specified path.
        type: str
        required: false
      component_specific_filters:
        description:
          - Filter configuration controlling which components are included in
            generated YAML playbook.
          - Currently supports only 'device_info' component for basic device
            information extraction.
          - Optional when generate_all_configurations is True, uses defaults if
            not provided.
          - When specified, only listed components are retrieved.
        type: dict
        required: false
        suboptions:
          components_list:
            description:
              - List of component types to include in generated YAML playbook
                file.
              - Only 'device_info' component is currently supported for
                extracting basic device information.
              - Device info includes serial_number, hostname, state, pid,
                is_sudi_required, and authorize fields.
              - When not specified with generate_all_configurations True,
                defaults to ['device_info'].
              - Order of components in list determines order in generated YAML
                playbook structure.
            type: list
            elements: str
            choices: ['device_info']
            default: ['device_info']
      global_filters:
        description:
          - Global filters to apply across PnP device extraction before
            component processing.
          - Allows filtering devices by state, product family, and site
            location.
          - Filters are applied sequentially to reduce dataset before device
            information extraction.
          - All filters are optional and can be combined for precise device
            selection.
        type: dict
        required: false
        suboptions:
          device_state:
            description:
              - Filter devices by their current PnP workflow state.
              - Valid states represent different stages in PnP device lifecycle.
              - Multiple states can be specified to include devices in any of
                the listed states.
              - When not specified, devices in all states are included in
                generated configuration.
              - State filtering applied at API level for efficient data
                retrieval.
            type: list
            elements: str
            required: false
            choices: ["Unclaimed", "Planned", "Onboarding", "Provisioned", "Error"]
          device_family:
            description:
              - Filter devices by product family classification.
              - Family categories group devices by hardware type and
                functionality.
              - Multiple families can be specified to include devices from any
                listed category.
              - Common families include "Switches and Hubs", "Routers",
                "Wireless Controller".
              - When not specified, devices from all families are included.
              - Family filtering applied after API retrieval during post-
                processing.
            type: list
            elements: str
            required: false
          site_name:
            description:
              - Filter devices by site name hierarchy location.
              - Only devices claimed to sites matching this hierarchy are
                included.
              - Site hierarchy must match full path as configured in Catalyst
                Center.
              - Format example "Global/USA/San Francisco" for multi-level site
                hierarchy.
              - Substring matching supported for site hierarchy filtering.
              - When not specified, devices from all sites are included.
              - Site filtering requires site ID resolution and applies after
                API retrieval.
              - Devices without site assignments are excluded when site filter
                specified.
            type: str
            required: false
requirements:
- dnacentersdk >= 2.9.3
- python >= 3.9
notes:
- SDK Methods used are
  - device_onboarding_pnp.DeviceOnboardingPnp.get_device_list
  - sites.Sites.get_sites (for site filtering only)
- Paths used are
  - GET /dna/intent/api/v1/onboarding/pnp-device
  - GET /dna/intent/api/v1/sites (for site filtering only)
- Minimum Catalyst Center version required is 2.3.7.9 for PnP device APIs.
- Module performs read-only operations and does not modify Catalyst Center
  configurations.
- Generated YAML files contain only device_info section with basic device
  attributes.
- Site assignments, templates, projects, and advanced parameters are not
  included in output.
- Site IDs are automatically resolved to hierarchical site names for
  readability.
- Site resolution uses in-memory caching to minimize API calls during
  processing.
- Module supports both check mode and normal execution mode with identical
  behavior.
- Generated playbooks are compatible with pnp_workflow_manager module
  v6.40.0+.
- Device transformation skips devices missing required fields
  (serial_number, pid).
- Operation tracking includes success and failure details for all processed
  devices.
- Device state defaults to "Unclaimed" when not provided by API response.
- Authorization flag set to True when authOperation requires authorization.
"""

EXAMPLES = r"""
- name: Generate basic device info for all PnP devices
  cisco.dnac.pnp_playbook_config_generator:
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

- name: Generate device info with custom file path
  cisco.dnac.pnp_playbook_config_generator:
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
      - file_path: "/tmp/pnp_device_info.yml"
        component_specific_filters:
          components_list: ["device_info"]

- name: Generate device info for unclaimed devices only
  cisco.dnac.pnp_playbook_config_generator:
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
      - file_path: "/tmp/unclaimed_device_info.yml"
        component_specific_filters:
          components_list: ["device_info"]
        global_filters:
          device_state: ["Unclaimed"]

- name: Generate device info for switches only
  cisco.dnac.pnp_playbook_config_generator:
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
      - file_path: "/tmp/switches_device_info.yml"
        component_specific_filters:
          components_list: ["device_info"]
        global_filters:
          device_family: ["Switches and Hubs"]

- name: Generate device info for devices at specific site
  cisco.dnac.pnp_playbook_config_generator:
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
      - file_path: "/tmp/site_device_info.yml"
        component_specific_filters:
          components_list: ["device_info"]
        global_filters:
          site_name: "Global/USA/San Francisco"

- name: Generate device info for provisioned wireless controllers
  cisco.dnac.pnp_playbook_config_generator:
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
      - file_path: "/tmp/wlc_device_info.yml"
        component_specific_filters:
          components_list: ["device_info"]
        global_filters:
          device_family: ["Wireless Controller"]
          device_state: ["Provisioned"]
"""

RETURN = r"""
response_1:
  description: Successful device info YAML generation
  returned: always
  type: dict
  sample: >
    {
      "msg": "YAML config generation succeeded for module 'pnp_workflow_manager'.",
      "response": {
        "status": "success",
        "message": "YAML config generation succeeded for module 'pnp_workflow_manager'.",
        "file_path": "pnp_workflow_manager_playbook_2026-02-06_14-19-07.yml",
        "configurations_count": 8,
        "components_processed": 1,
        "components_skipped": 0
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


class PnPPlaybookGenerator(DnacBase, BrownFieldHelper):
    """
    Class for generating YAML playbooks from PnP device configurations.

    Description:
        Orchestrates brownfield discovery and YAML playbook generation workflow for
        Cisco Catalyst Center PnP infrastructure by retrieving existing device
        registrations through PnP APIs, extracting essential device attributes
        (serial number, hostname, state, PID, SUDI requirements), applying
        intelligent filtering based on device state, family, and site location,
        resolving site IDs to hierarchical names for readability, transforming API
        responses to playbook-compatible format, and generating structured YAML
        files ready for modification and redeployment through pnp_workflow_manager
        module.

    Core Capabilities:
        - Retrieves PnP device inventory with basic device information attributes
        - Fetches device registrations across all workflow states (Unclaimed,
          Planned, Onboarding, Provisioned, Error)
        - Discovers device attributes including serial numbers, hostnames, product
          IDs, and SUDI requirements
        - Extracts authorization requirements from authOperation field
        - Supports device state filtering at API level for efficient retrieval
        - Handles device family filtering during post-retrieval processing
        - Enables site-based filtering with hierarchical name matching
        - Resolves site UUIDs to full hierarchy paths using Sites API
        - Transforms camelCase API responses to snake_case playbook parameters
        - Removes devices missing required fields (serial_number, pid)
        - Generates timestamped filenames when custom path not provided
        - Creates parent directories automatically for specified file paths
        - Provides comprehensive operation statistics in module response

    Supported Operations:
        - Gathered state for device discovery and YAML generation
        - Generate all mode for complete PnP inventory documentation
        - Selective filtering with state, family, and site criteria
        - Single component mode supporting only device_info extraction
        - Multi-device processing with individual transformation tracking

    API Integration:
        - device_onboarding_pnp.DeviceOnboardingPnp.get_device_list with optional
          state parameter
        - sites.Sites.get_sites for site name resolution during filtering

    Data Transformation:
        - Maps deviceInfo.serialNumber to serial_number (required)
        - Maps deviceInfo.hostname to hostname (optional)
        - Maps deviceInfo.state to state with "Unclaimed" default
        - Maps deviceInfo.pid to pid (required)
        - Maps deviceInfo.sudiRequired to is_sudi_required (optional)
        - Derives authorize flag from authOperation field (optional)
        - Preserves OrderedDict structure for consistent YAML field ordering
        - Skips devices without serial_number or pid fields

    Filtering Capabilities:
        - device_state: Filters by PnP workflow state at API level (Unclaimed,
          Planned, Onboarding, Provisioned, Error)
        - device_family: Filters by product category during post-processing
          (Switches and Hubs, Routers, Wireless Controller)
        - site_name: Filters by hierarchical site name with substring matching
          after site ID resolution
        - Smart validation: Skips None devices and invalid structures
        - Comprehensive coverage: Continues processing after individual failures

    Error Handling:
        - Validates Catalyst Center version compatibility (requires >= 2.3.7.9)
        - Handles API errors gracefully with informative error messages
        - Returns empty lists when API calls fail to prevent workflow disruption
        - Logs exceptions with type, message, and context for debugging
        - Sets operation results with success/failure status and statistics
        - Validates device structure and deviceInfo presence
        - Skips devices missing required fields with warning logs

    Output Format:
        - YAML playbook compatible with pnp_workflow_manager module
        - Single configuration group with device_info key
        - Each device as separate OrderedDict entry in device_info list
        - Site IDs resolved to hierarchical names for readability
        - Clean structure with only essential device attributes
        - Proper indentation and formatting for easy manual modification

    Minimum Requirements:
        - Cisco Catalyst Center version 2.3.7.9 or higher
        - DNA Center SDK 2.9.3 or higher for API compatibility
        - Python 3.9 or higher for OrderedDict and type hint support
        - Read access to PnP and Sites APIs in Catalyst Center
        - Network connectivity to Catalyst Center management interface

    Usage Patterns:
        - Brownfield PnP inventory documentation and audit workflows
        - Device discovery before bulk provisioning operations
        - Migration preparation between Catalyst Center instances
        - Compliance reporting with current device registration status
        - Template creation for standardized PnP device management
        - Disaster recovery documentation for PnP infrastructure

    Attributes:
        module_name (str): Target module name for generated playbooks
            (pnp_workflow_manager)
        module_schema (dict): Mapping of components to API details, filters, and
            getter functions
        supported_states (list): Operational states supported by the class
            (currently only 'gathered')
        operation_successes (list): Successful device transformations with serial
            and state
        operation_failures (list): Failed transformations with serial and error
        total_devices_processed (int): Count of devices included in final output
        _site_cache (dict): In-memory cache for site ID to name mappings

    Methods:
        validate_input(): Validates playbook configuration parameters against
            schema
        get_workflow_elements_schema(): Defines comprehensive schema structure
        transform_pnp_device(): Transforms device from API to playbook format
        group_devices_by_config(): Organizes devices into unified configuration
        get_pnp_devices(): Retrieves and filters devices from Catalyst Center
        get_site_name_from_id(): Resolves site UUID to hierarchical name with
            caching
        yaml_config_generator(): Coordinates device retrieval and file generation
        get_want(): Extracts and normalizes configuration from user input
        get_diff_gathered(): Processes gathered state for YAML generation

    Inheritance:
        DnacBase: Provides core DNA Center SDK integration and helper methods
        BrownFieldHelper: Provides YAML generation utilities and file operations

    Returns:
        Generated YAML playbook files with statistics including:
            - config_groups: Count of configuration groups (always 1)
            - total_devices: Total device count in generated file
            - operation_summary: Success/failure details with device serials
            - file_path: Absolute path to generated YAML playbook file
            - status: Success or failure indication with descriptive message
    """

    def __init__(self, module):
        """
        Initialize PnP playbook generator with module configuration.

        Parameters:
          - module: Ansible module instance with connection and configuration parameters.
        Returns:
          None
        Example:
          Called automatically when creating PnPPlaybookGenerator instance.
        """
        self.supported_states = ["gathered"]
        super().__init__(module)
        self.module_schema = self.get_workflow_elements_schema()
        self.module_name = "pnp_workflow_manager"

        # Initialize operation tracking
        self.operation_successes = []
        self.operation_failures = []
        self.total_devices_processed = 0

        # Initialize caches (reduced to only site cache since we're not using templates/images)
        self._site_cache = {}

        # Initialize generate_all_configurations
        self.generate_all_configurations = False

    def validate_input(self):
        """
        Validates playbook configuration parameters against expected schema structure.

        Description:
            Performs comprehensive validation of user-provided playbook configuration by
            checking parameter presence, validating parameter types and values against
            specification, identifying invalid parameters with detailed error reporting,
            and ensuring configuration meets requirements for successful YAML generation
            workflow execution enabling early detection of configuration issues.

        Parameters:
            self: Instance containing config attribute with user-provided playbook
                  configuration parameters requiring validation.

        Returns:
            object: Self instance with updated attributes including:
                - validated_config (list): Successfully validated configuration items
                  ready for processing.
                - msg (str): Validation result message indicating success or specific
                  errors found.
                - status (str): Operation status set to 'success' when validation
                  completes.
                - Exits via check_return_status() if validation fails with invalid
                  parameters.
        """
        self.log(
            "Starting playbook configuration validation. Checking if config parameter "
            "provided in playbook.",
            "DEBUG"
        )
        if not self.config:
            self.msg = "config not available in playbook for validation"
            self.log(
                "No configuration provided in playbook. Validation completed with empty "
                "config requiring generate_all_configurations flag for default values.",
                "WARNING"
            )
            self.status = "success"
            return self

        pnp_brownfield_spec = {
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
                "required": False,
                "options": {
                    "components_list": {
                        "type": "list",
                        "elements": "str",
                        "required": False,
                        "default": ["device_info"]
                    }
                }
            },
            "global_filters": {
                "type": "dict",
                "required": False,
                "options": {
                    "device_state": {
                        "type": "list",
                        "elements": "str",
                        "required": False
                    },
                    "device_family": {
                        "type": "list",
                        "elements": "str",
                        "required": False
                    },
                    "site_name": {
                        "type": "str",
                        "required": False
                    }
                }
            },
        }

        valid_config, invalid_params = validate_list_of_dicts(
            self.config, pnp_brownfield_spec
        )

        if invalid_params:
            self.msg = "Invalid parameters in playbook config: {0}".format(
                "\n".join(invalid_params)
            )
            self.log(
                "Validation failed with {0} invalid parameter(s) detected. Invalid "
                "parameters: {1}. Setting operation result to failed and exiting.".format(
                    len(invalid_params), ", ".join(invalid_params)
                ),
                "ERROR"
            )
            self.set_operation_result("failed", False, self.msg, "ERROR").check_return_status()

        # Additional validation for nested parameters and choice values
        validation_errors = []
        valid_components = ["device_info"]
        valid_states = ["Unclaimed", "Planned", "Onboarding", "Provisioned", "Error"]
        valid_component_filter_keys = ["components_list"]
        valid_global_filter_keys = ["device_state", "device_family", "site_name"]

        for config_index, config_item in enumerate(valid_config, start=1):
            # Validate component_specific_filters keys and values
            component_filters = config_item.get("component_specific_filters", {})
            if component_filters:
                # Check for unknown keys in component_specific_filters
                unknown_comp_keys = [k for k in component_filters.keys() if k not in valid_component_filter_keys]
                if unknown_comp_keys:
                    validation_errors.append(
                        "Config item {0}: Unknown parameter(s) in component_specific_filters: {1}. "
                        "Valid parameters are: {2}".format(
                            config_index, unknown_comp_keys, valid_component_filter_keys
                        )
                    )

                # Validate components_list values
                components_list = component_filters.get("components_list", [])
                if components_list:
                    invalid_components = [c for c in components_list if c not in valid_components]
                    if invalid_components:
                        validation_errors.append(
                            "Config item {0}: Invalid value(s) in components_list: {1}. "
                            "Valid choices are: {2}".format(
                                config_index, invalid_components, valid_components
                            )
                        )

            # Validate global_filters keys and values
            global_filters = config_item.get("global_filters", {})
            if global_filters:
                # Check for unknown keys in global_filters
                unknown_global_keys = [k for k in global_filters.keys() if k not in valid_global_filter_keys]
                if unknown_global_keys:
                    validation_errors.append(
                        "Config item {0}: Unknown parameter(s) in global_filters: {1}. "
                        "Valid parameters are: {2}".format(
                            config_index, unknown_global_keys, valid_global_filter_keys
                        )
                    )

                # Validate device_state values
                device_states = global_filters.get("device_state", [])
                if device_states:
                    invalid_states = [s for s in device_states if s not in valid_states]
                    if invalid_states:
                        validation_errors.append(
                            "Config item {0}: Invalid value(s) in device_state: {1}. "
                            "Valid choices are: {2}".format(
                                config_index, invalid_states, valid_states
                            )
                        )

            # Validate that generate_all_configurations is true OR filters are provided
            generate_all = config_item.get("generate_all_configurations", False)
            has_global_filters = bool(global_filters)
            has_component_filters = bool(component_filters and component_filters.get("components_list"))

            if not generate_all and not has_global_filters and not has_component_filters:
                validation_errors.append(
                    "Config item {0}: 'generate_all_configurations' is set to false but no "
                    "filters are provided. Either set 'generate_all_configurations' to true, "
                    "or specify 'global_filters' (device_state, device_family, site_name) or "
                    "'component_specific_filters' with 'components_list' to control which "
                    "devices are included in the generated playbook.".format(config_index)
                )

        if validation_errors:
            self.msg = "Configuration validation errors:\n{0}".format(
                "\n".join(validation_errors)
            )
            self.log(
                "Validation failed with {0} validation error(s). Errors: {1}. "
                "Setting operation result to failed and exiting.".format(
                    len(validation_errors), "; ".join(validation_errors)
                ),
                "ERROR"
            )
            self.set_operation_result("failed", False, self.msg, "ERROR").check_return_status()

        self.validated_config = valid_config
        self.msg = "Successfully validated playbook config"
        self.log(
            "Playbook configuration validation completed successfully including nested "
            "parameter and choice validation. Validated {0} configuration item(s) ready "
            "for YAML generation workflow processing.".format(
                len(valid_config)
            ),
            "INFO"
        )
        self.status = "success"

        return self

    def get_workflow_elements_schema(self):
        """
        Defines comprehensive schema structure for PnP workflow elements and filters.

        Description:
            Constructs complete schema mapping for PnP brownfield playbook generation by
            defining module metadata, global filter specifications with validation rules,
            component-specific filter options, and network element configurations with
            getter function mappings enabling structured device information extraction,
            filter validation, and component processing orchestration for YAML playbook
            generation workflow.

        Parameters:
            None: Uses class instance to define schema with self-referencing getter
                  function.

        Returns:
            dict: Comprehensive schema structure containing:
                - module_name (str): Target module identifier for generated playbooks
                  ('pnp_workflow_manager').
                - global_filters (dict): Device filtering criteria with type validation
                  and allowed values including device_state choices, device_family options,
                  and site_name hierarchy patterns.
                - component_specific_filters (dict): Component selection filters defining
                  components_list with valid values and defaults for device_info extraction.
                - network_elements (dict): Component processing configuration mapping
                  device_info to getter function enabling automated device retrieval and
                  transformation workflow.
        """
        self.log(
            "Defining workflow elements schema for PnP brownfield playbook generation. "
            "Configuring module metadata, global filters, component filters, and network "
            "element mappings.",
            "DEBUG"
        )

        schema = {
            "module_name": "pnp_workflow_manager",
            "global_filters": {
                "device_state": {
                    "type": "list",
                    "valid_values": [
                        "Unclaimed",
                        "Planned",
                        "Onboarding",
                        "Provisioned",
                        "Error"
                    ]
                },
                "device_family": {
                    "type": "list"
                },
                "site_name": {
                    "type": "str"
                }
            },
            "component_specific_filters": {
                "components_list": {
                    "type": "list",
                    "valid_values": ["device_info"],
                    "default": ["device_info"]
                }
            },
            "network_elements": {
                "device_info": {
                    "get_function_name": self.get_pnp_devices,
                }
            }
        }

        return schema

    def transform_pnp_device(self, device):
        """
        Transforms PnP device from API response format to playbook-compatible device_info structure.

        Description:
            Extracts essential device information from raw Catalyst Center PnP API response by
            retrieving deviceInfo section, validating required fields (serial_number, pid),
            extracting optional attributes (hostname, state, sudi_required), determining
            authorization requirements based on auth_operation field, and constructing
            OrderedDict with snake_case parameter names ready for YAML serialization enabling
            simplified device inventory generation for pnp_workflow_manager module.

        Parameters:
            device (dict): Raw PnP device dictionary from Catalyst Center API containing
                          deviceInfo section with device attributes, state information,
                          and hardware details from get_device_list response.

        Returns:
            OrderedDict: Transformed device information containing:
                - serial_number (str): Device serial number (required field)
                - hostname (str): Device hostname when configured (optional)
                - state (str): PnP state (Unclaimed/Planned/Onboarding/Provisioned/Error)
                - pid (str): Product ID identifying device model (required field)
                - is_sudi_required (bool): SUDI certificate requirement flag (optional)
                - authorize (bool): Authorization required flag when auth_operation not
                  AUTHORIZATION_NOT_REQUIRED (optional)
            None: Returns None when required fields missing (serial_number or pid) enabling
                 graceful skip of invalid devices during processing.
        """
        self.log(
            "Starting device transformation from API format to playbook structure. Extracting "
            "deviceInfo section for parameter mapping.",
            "DEBUG"
        )

        device_info_item = OrderedDict()
        device_info = device.get("deviceInfo", {})

        if not device_info:
            self.log(
                "Device missing deviceInfo section. Skipping transformation for invalid device "
                "structure.",
                "WARNING"
            )
            return None

        # Basic device information - serial_number is required
        serial_number = device_info.get("serialNumber")
        if not serial_number:
            self.log(
                "Device missing required serial_number field. Cannot create device_info entry "
                "without unique identifier. Skipping device transformation.",
                "WARNING"
            )
            return None

        device_info_item["serial_number"] = serial_number

        self.log(
            "Processing device with serial_number: {0}. Extracting optional and required "
            "device attributes.".format(serial_number),
            "DEBUG"
        )

        # Hostname (optional)
        hostname = device_info.get("hostname")
        if hostname:
            device_info_item["hostname"] = hostname
            self.log(
                "Hostname found for device {0}: {1}. Including in device_info.".format(
                    serial_number, hostname
                ),
                "DEBUG"
            )

        # Extract state with default value
        state = device_info.get("state", "Unclaimed")
        device_info_item["state"] = state

        self.log(
            "Device {0} state set to: {1}. Using default 'Unclaimed' if not provided by API.".format(
                serial_number, state
            ),
            "DEBUG"
        )

        # PID is required
        pid = device_info.get("pid")
        if not pid:
            self.log(
                "Device {0} missing required pid (Product ID) field. Cannot create device_info "
                "entry without hardware identifier. Skipping device transformation.".format(
                    serial_number
                ),
                "WARNING"
            )
            return None
        device_info_item["pid"] = pid

        self.log(
            "Product ID found for device {0}: {1}. Including as required field in device_info.".format(
                serial_number, pid
            ),
            "DEBUG"
        )

        # SUDI requirement (optional)
        sudi_required = device_info.get("sudiRequired")
        if sudi_required is not None:
            device_info_item["is_sudi_required"] = sudi_required
            self.log(
                "SUDI requirement flag found for device {0}: {1}. Including in device_info.".format(
                    serial_number, sudi_required
                ),
                "DEBUG"
            )

        # Authorization flag (optional)
        auth_operation = device_info.get("authOperation")
        if auth_operation and auth_operation != "AUTHORIZATION_NOT_REQUIRED":
            device_info_item["authorize"] = True
            self.log(
                "Device {0} requires authorization. auth_operation: {1}. Setting authorize "
                "flag to True in device_info.".format(serial_number, auth_operation),
                "DEBUG"
            )

        self.log(
            "Successfully transformed device {0} with {1} field(s). Device ready for YAML "
            "serialization with state: {2}, pid: {3}.".format(
                serial_number, len(device_info_item), state, pid
            ),
            "INFO"
        )

        return device_info_item

    def group_devices_by_config(self, devices):
        """
        Organizes PnP devices into unified configuration structure for YAML playbook generation.

        Description:
            Creates single configuration group containing all valid PnP devices with essential
            device_info attributes by iterating through raw device list from API, validating
            device structure and required fields, transforming each device to playbook format
            using transform_pnp_device(), tracking successful transformations and failures with
            detailed operation statistics, and returning consolidated configuration group ready
            for YAML serialization enabling simplified device inventory management.

        Parameters:
            devices (list): Raw PnP device dictionaries from Catalyst Center API containing
                           deviceInfo sections with hardware details, state information, and
                           configuration attributes requiring transformation to playbook format.

        Returns:
            list: Single-element list containing OrderedDict configuration group with
                 'device_info' key holding list of transformed device dictionaries, or empty
                 list when no valid devices found enabling graceful handling of empty inventory.
        """
        self.log(
            "Starting device grouping for YAML configuration structure. Processing {0} raw "
            "device(s) from API response.".format(len(devices) if devices else 0),
            "DEBUG"
        )
        # Create a single group for all devices with just device_info
        config_group = OrderedDict()
        config_group["device_info"] = []

        devices_processed = 0
        devices_skipped = 0

        for device_index, device in enumerate(devices, start=1):
            if not device or not isinstance(device, dict):
                devices_skipped += 1
                self.log(
                    "Skipping invalid device entry {0}/{1}. Device is None or not dictionary "
                    "structure. Type: {2}".format(
                        device_index, len(devices), type(device).__name__
                    ),
                    "WARNING"
                )
                continue

            device_info = device.get("deviceInfo", {})
            if not device_info:
                devices_skipped += 1
                self.log(
                    "Skipping device {0}/{1} due to missing deviceInfo section. Device cannot "
                    "be processed without required attributes.".format(device_index, len(devices)),
                    "WARNING"
                )
                continue

            serial_number = device_info.get("serialNumber", "Unknown")
            device_family = device_info.get("family", "Unknown")
            state = device_info.get("state", "Unknown")
            pid = device_info.get("pid", "Unknown")

            self.log(
                "Processing device {0}/{1} with serial_number: {2}, family: {3}, state: {4}, "
                "pid: {5}. Starting device transformation to playbook format.".format(
                    device_index, len(devices), serial_number, device_family, state, pid
                ),
                "DEBUG"
            )

            # Transform and add device info to the group
            try:
                device_info_item = self.transform_pnp_device(device)
                if device_info_item:
                    config_group["device_info"].append(device_info_item)
                    devices_processed += 1

                    self.operation_successes.append({
                        "device_serial": device_info_item.get("serial_number"),
                        "device_state": device_info_item.get("state"),
                        "status": "success"
                    })

                    self.log(
                        "Successfully transformed device {0}/{1} with serial_number: {2}. Added "
                        "to configuration group with {3} field(s).".format(
                            device_index, len(devices), serial_number, len(device_info_item)
                        ),
                        "DEBUG"
                    )
                else:
                    devices_skipped += 1
                    self.log(
                        "Transformation returned None for device {0}/{1} with serial_number: {2}. "
                        "Device skipped due to missing required fields or validation failure.".format(
                            device_index, len(devices), serial_number
                        ),
                        "WARNING"
                    )
            except Exception as e:
                devices_skipped += 1
                error_message = str(e)

                self.operation_failures.append({
                    "device_serial": serial_number,
                    "error": error_message,
                    "status": "failed"
                })

                self.log(
                    "Exception during device transformation for device {0}/{1} with serial_number: "
                    "{2}. Exception type: {3}, Exception message: {4}. Device skipped and added "
                    "to failure tracking.".format(
                        device_index, len(devices), serial_number, type(e).__name__, error_message
                    ),
                    "ERROR"
                )

        # Return single config group containing all devices
        self.log(
            "Device grouping completed. Total devices processed: {0}, Total devices skipped: {1}, "
            "Valid device_info entries in configuration group: {2}".format(
                devices_processed, devices_skipped, len(config_group["device_info"])
            ),
            "INFO"
        )

        self.log(
            "Configuration group structure before return: {0}".format(config_group),
            "DEBUG"
        )

        result = [config_group] if config_group["device_info"] else []

        return result

    def get_pnp_devices(self, network_element, config):
        """
        Retrieves and filters PnP devices from Catalyst Center based on specified criteria.

        Description:
            Fetches PnP device inventory from Cisco Catalyst Center by executing API calls
            with optional state filtering, applying additional device family and site name
            filters on retrieved results, validating device structure and deviceInfo presence,
            tracking total devices processed for operation statistics, and returning filtered
            device list ready for transformation to YAML format enabling targeted device
            discovery and configuration generation.

        Parameters:
            network_element (dict): Network element definition containing processing metadata
                                   and getter function reference for device retrieval.
            config (dict): Configuration dictionary containing global_filters with optional
                          device_state, device_family, and site_name criteria for filtering
                          PnP device list. None or empty dict uses no filters.

        Returns:
            dict: Dictionary containing 'pnp_devices' key with list of filtered raw device
                 dictionaries from API, or empty list when no devices found or API call
                 fails enabling graceful handling in downstream processing.
        """
        self.log(
            "Starting PnP device retrieval from Catalyst Center. Processing configuration "
            "filters for targeted device discovery.",
            "INFO"
        )

        # Handle None config
        if not config:
            self.log(
                "No configuration provided for device retrieval. Using empty filters to "
                "retrieve all available PnP devices.",
                "WARNING"
            )
            config = {}

        # Extract filters from config
        global_filters = config.get("global_filters", {})
        # Ensure global_filters is not None
        if global_filters is None:
            self.log(
                "Global filters is None, defaulting to empty dict. All devices will be "
                "retrieved without filtering criteria.",
                "DEBUG"
            )
            global_filters = {}

        device_state_filter = global_filters.get("device_state", [])
        device_family_filter = global_filters.get("device_family", [])
        site_name_filter = global_filters.get("site_name")

        self.log(
            "Extracted filters - State: {0}, Family: {1}, Site: {2}. Preparing API call "
            "parameters with state filter if provided.".format(
                device_state_filter or "None",
                device_family_filter or "None",
                site_name_filter or "None"
            ),
            "DEBUG"
        )

        try:
            # Get all PnP devices
            params = {}
            if device_state_filter:
                params["state"] = device_state_filter
                self.log(
                    "Applying state filter at API level: {0}. This reduces initial dataset "
                    "size for efficient processing.".format(device_state_filter),
                    "DEBUG"
                )

            response = self.dnac._exec(
                family="device_onboarding_pnp",
                function="get_device_list",
                params=params,
                op_modifies=False
            )
            self.log(
                "Received API response for PnP devices. Response type: {0}, Response "
                "structure: {1}".format(type(response).__name__, response),
                "DEBUG"
            )
            if not response:
                self.log(
                    "No PnP devices found in API response. Empty response returned from "
                    "Catalyst Center indicating no devices match criteria or PnP inventory "
                    "is empty.",
                    "WARNING"
                )
                return {"pnp_devices": []}

            devices = response if isinstance(response, list) else []
            self.log(
                "Retrieved {0} total PnP device(s) from API before applying post-retrieval "
                "filters. Beginning validation and filtering process.".format(len(devices)),
                "INFO"
            )

            # Apply additional filters
            filtered_devices = []
            devices_processed = 0
            devices_skipped = 0

            for device_index, device in enumerate(devices, start=1):
                # Skip None or invalid devices
                if not device or not isinstance(device, dict):
                    devices_skipped += 1
                    self.log(
                        "Skipping invalid device entry {0}/{1}. Device is None or not "
                        "dictionary structure. Type: {2}".format(
                            device_index, len(devices), type(device).__name__
                        ),
                        "WARNING"
                    )
                    continue

                device_info = device.get("deviceInfo", {})

                # Skip if deviceInfo is missing
                if not device_info:
                    devices_skipped += 1
                    self.log(
                        "Skipping device {0}/{1} due to missing deviceInfo section. Device "
                        "cannot be processed without required attributes.".format(
                            device_index, len(devices)
                        ),
                        "WARNING"
                    )
                    continue

                serial_number = device_info.get("serialNumber", "Unknown")

                # Apply device family filter
                if device_family_filter:
                    device_family = device_info.get("family")
                    if device_family not in device_family_filter:
                        devices_skipped += 1
                        self.log(
                            "Skipping device {0}/{1} with serial_number: {2}. Device family "
                            "'{3}' not in filter list: {4}".format(
                                device_index, len(devices), serial_number, device_family,
                                device_family_filter
                            ),
                            "DEBUG"
                        )
                        continue

                # Apply site name filter
                if site_name_filter:
                    site_id = device_info.get("siteId")
                    if site_id:
                        site_name = self.get_site_name_from_id(site_id)
                        if not site_name or site_name_filter not in site_name:
                            devices_skipped += 1
                            self.log(
                                "Skipping device {0}/{1} with serial_number: {2}. Site name "
                                "'{3}' does not match filter: {4}".format(
                                    device_index, len(devices), serial_number, site_name,
                                    site_name_filter
                                ),
                                "DEBUG"
                            )
                            continue
                    else:
                        devices_skipped += 1
                        self.log(
                            "Skipping device {0}/{1} with serial_number: {2}. No site ID "
                            "found but site name filter '{3}' specified.".format(
                                device_index, len(devices), serial_number, site_name_filter
                            ),
                            "DEBUG"
                        )
                        continue

                filtered_devices.append(device)
                devices_processed += 1

                self.log(
                    "Device {0}/{1} with serial_number: {2} passed all filters. Added to "
                    "filtered device list for YAML generation.".format(
                        device_index, len(devices), serial_number
                    ),
                    "DEBUG"
                )

            self.log(
                "Filtering completed. Total devices retrieved: {0}, Devices passed filters: "
                "{1}, Devices skipped: {2}. Filtered devices ready for transformation.".format(
                    len(devices), devices_processed, devices_skipped
                ),
                "INFO"
            )
            self.total_devices_processed = len(filtered_devices)

            return {"pnp_devices": filtered_devices}

        except Exception as e:
            error_message = str(e)
            self.log(
                "Exception occurred during PnP device retrieval. Exception type: {0}, "
                "Exception message: {1}. Returning empty device list for graceful handling.".format(
                    type(e).__name__, error_message
                ),
                "ERROR"
            )
            import traceback
            self.log("Traceback: {0}".format(traceback.format_exc()), "ERROR")
            return {"pnp_devices": []}

    def get_site_name_from_id(self, site_id):
        """
        Resolves site UUID to hierarchical site name with caching for performance optimization.

        Description:
            Retrieves full site name hierarchy from Catalyst Center Sites API by checking
            in-memory cache first for previously resolved site IDs, executing Sites API call
            when cache miss occurs, processing response to locate matching site by UUID,
            extracting siteNameHierarchy or nameHierarchy attribute, caching result for
            subsequent lookups, and returning hierarchical site name enabling human-readable
            site references in generated YAML playbooks with reduced API call overhead.

        Parameters:
            site_id (str): Site UUID identifier requiring resolution to hierarchical name.
                          Expected format is standard UUID string from Catalyst Center.

        Returns:
            str: Full hierarchical site name path (example "Global/USA/San Francisco/Building1")
                 or None when site not found in API response or site_id is None/empty enabling
                 graceful handling of missing site associations.
        """
        self.log(
            "Resolving site name from site UUID. Checking cache for previously resolved "
            "site_id: {0}".format(site_id),
            "DEBUG"
        )

        if not site_id:
            self.log(
                "Site ID is None or empty. Cannot resolve site name without valid identifier. "
                "Returning None for graceful handling.",
                "DEBUG"
            )
            return None

        if site_id in self._site_cache:
            cached_site_name = self._site_cache[site_id]
            self.log(
                "Site name found in cache for site_id: {0}. Cached value: {1}. Returning "
                "cached result without API call for performance optimization.".format(
                    site_id, cached_site_name
                ),
                "DEBUG"
            )
            return cached_site_name

        self.log(
            "Site ID {0} not found in cache. Executing Sites API call to retrieve site "
            "information from Catalyst Center.".format(site_id),
            "DEBUG"
        )

        try:
            response = self.dnac._exec(
                family="site_design",
                function="get_sites",
                params={},
                op_modifies=False
            )

            self.log(
                "Received API response from Sites endpoint. Response type: {0}. Processing "
                "response structure to locate site with UUID: {1}".format(
                    type(response).__name__, site_id
                ),
                "DEBUG"
            )

            if response and response.get("response"):
                site_info = response.get("response")
                # Handle list response - need to find site by ID
                if isinstance(site_info, list):
                    self.log(
                        "Sites API returned list format with {0} site(s). Iterating through "
                        "sites to find matching site_id: {1}".format(len(site_info), site_id),
                        "DEBUG"
                    )

                    for site_index, site in enumerate(site_info, start=1):
                        if site.get("id") == site_id:
                            site_name = site.get("siteNameHierarchy") or site.get("nameHierarchy")

                            if site_name:
                                self._site_cache[site_id] = site_name
                                self.log(
                                    "Site name resolved successfully for site_id: {0}. Hierarchical "
                                    "name: {1}. Cached for future lookups to avoid redundant API "
                                    "calls.".format(site_id, site_name),
                                    "INFO"
                                )
                                return site_name

                    self.log(
                        "Site with UUID '{0}' not found in {1} site(s) returned by API. Site "
                        "may be deleted or UUID invalid. Returning None for graceful handling.".format(
                            site_id, len(site_info)
                        ),
                        "WARNING"
                    )
                    return None
                elif isinstance(site_info, dict):
                    self.log(
                        "Sites API returned dict format for single site. Extracting site name "
                        "hierarchy from response attributes.",
                        "DEBUG"
                    )

                    site_name = site_info.get("siteNameHierarchy") or site_info.get("nameHierarchy")

                    if site_name:
                        self._site_cache[site_id] = site_name
                        self.log(
                            "Site name resolved from dict response for site_id: {0}. Hierarchical "
                            "name: {1}. Cached for future lookups.".format(site_id, site_name),
                            "INFO"
                        )
                        return site_name
                else:
                    self.log(
                        "Unexpected Sites API response format. Expected list or dict, received: "
                        "{0}. Unable to extract site name from unrecognized structure.".format(
                            type(site_info).__name__
                        ),
                        "WARNING"
                    )
                    return None

        except Exception as e:
            self.log(
                "Exception during site name resolution for site_id: {0}. Exception type: {1}, "
                "Exception message: {2}. Returning None to allow device processing to continue.".format(
                    site_id, type(e).__name__, str(e)
                ),
                "WARNING"
            )

        return None

    def yaml_config_generator(self, yaml_config_generator):
        """
        Generates YAML configuration file containing PnP device information.

        Description:
            Orchestrates complete YAML playbook generation workflow by processing configuration
            parameters, determining output file path with auto-generation when not specified,
            retrieving PnP devices through get_pnp_devices() with applied filters, grouping
            devices into unified configuration structure using group_devices_by_config(),
            wrapping grouped configurations in pnp_workflow_manager-compatible format, writing
            structured YAML to file with proper serialization, tracking operation statistics
            including successful and failed device transformations, and returning comprehensive
            result with file path and device counts enabling brownfield PnP inventory documentation.

        Parameters:
            yaml_config_generator (dict): Configuration dictionary containing:
                - file_path (str, optional): Target path for generated YAML file. When not
                  provided, auto-generates filename using generate_filename() with timestamp
                  format "pnp_workflow_manager_playbook_<YYYY-MM-DD_HH-MM-SS>.yml".
                - global_filters (dict, optional): Device filtering criteria including
                  device_state, device_family, and site_name for targeted device retrieval.
                - component_specific_filters (dict, optional): Component selection filters
                  currently supporting only 'device_info' component type.

        Returns:
            object: Self instance with updated attributes including:
                - result (dict): Contains response with file_path, config_groups count,
                  total_devices count, and operation_summary with success/failure details.
                - msg (str): Success or failure message describing outcome.
                - status (str): Operation status ('success' or 'failed').
        """
        self.log(
            "Starting YAML configuration generation workflow for PnP devices. Processing "
            "configuration parameters and determining output file path.",
            "INFO"
        )

        # Track components processing - PnP module only supports device_info component
        components_requested = 1  # Only device_info component is supported
        components_processed = 0
        components_skipped = 0

        # Handle None yaml_config_generator
        if not yaml_config_generator:
            self.log(
                "No configuration provided for YAML generation. Using empty config dict with "
                "default values for all parameters.",
                "WARNING"
            )
            yaml_config_generator = {}

        file_path = yaml_config_generator.get("file_path")
        if not file_path:
            file_path = self.generate_filename()
            self.log(
                "No file path specified in configuration. Auto-generated filename: {0} for "
                "YAML output.".format(file_path),
                "DEBUG"
            )
        else:
            self.log(
                "Using provided file path for YAML output: {0}".format(file_path),
                "DEBUG"
            )

        self.log(
            "Retrieving network element configuration for device_info component from module "
            "schema. Preparing to execute device retrieval function.",
            "DEBUG"
        )

        # Get PnP devices
        network_element = self.module_schema["network_elements"]["device_info"]
        get_function = network_element["get_function_name"]

        self.log(
            "Executing device retrieval function with configuration filters. Fetching PnP "
            "devices from Catalyst Center matching specified criteria.",
            "DEBUG"
        )

        devices_data = get_function(network_element, yaml_config_generator)

        if not devices_data or not devices_data.get("pnp_devices"):
            no_devices_message = (
                "No PnP devices found matching specified filters. Verify device inventory "
                "and filter criteria."
            )
            self.msg = no_devices_message
            # Component was attempted but no data found - mark as skipped
            components_skipped = components_requested
            self.result["response"] = {
                "status": "success",
                "message": self.msg,
                "components_processed": 0,
                "components_skipped": components_skipped
            }
            self.status = "success"

            self.log(
                "Device retrieval returned empty result. No PnP devices available or filters "
                "excluded all devices. Terminating YAML generation with informational status.",
                "WARNING"
            )
            return self

        self.log(
            "Successfully retrieved {0} PnP device(s) from API. Proceeding to group devices "
            "by configuration structure for YAML formatting.".format(
                len(devices_data.get("pnp_devices", []))
            ),
            "INFO"
        )

        # Group devices by their configuration (simplified to single group)
        grouped_configs = self.group_devices_by_config(devices_data["pnp_devices"])

        if not grouped_configs:
            no_valid_devices_message = (
                "No valid devices found after processing. All devices failed validation or "
                "transformation checks."
            )
            self.msg = no_valid_devices_message
            # Component was attempted but all devices failed - mark as skipped
            components_skipped = components_requested
            self.result["response"] = {
                "status": "success",
                "message": self.msg,
                "components_processed": 0,
                "components_skipped": components_skipped
            }
            self.status = "success"

            self.log(
                "Device grouping returned empty result. All devices failed validation or "
                "transformation during processing. Check operation_failures for details.",
                "WARNING"
            )
            return self

        self.log(
            "Device grouping completed successfully. Created {0} configuration group(s) with "
            "total {1} valid device(s). Preparing final output structure.".format(
                len(grouped_configs),
                sum(len(group.get("device_info", [])) for group in grouped_configs)
            ),
            "INFO"
        )

        # Prepare output with grouped configurations
        final_output = []
        for group_index, config_group in enumerate(grouped_configs, start=1):
            final_output.append(config_group)
            self.log(
                "Added configuration group {0}/{1} to final output with {2} device(s).".format(
                    group_index, len(grouped_configs), len(config_group.get("device_info", []))
                ),
                "DEBUG"
            )

        # Wrap in config structure for pnp_workflow_manager
        output_structure = {"config": final_output}

        self.log(
            "Final output structure constructed with pnp_workflow_manager compatible format. "
            "Structure contains {0} top-level config entry(ies). Writing to YAML file: {1}".format(
                len(final_output), file_path
            ),
            "DEBUG"
        )

        # Write to YAML file
        success = self.write_dict_to_yaml([output_structure], file_path)

        if success:
            # Component successfully processed
            components_processed = components_requested
            components_skipped = 0

            self.msg = "YAML config generation succeeded for module '{0}'.".format(self.module_name)
            self.result["msg"] = self.msg
            self.result["response"] = {
                "status": "success",
                "message": self.msg,
                "file_path": file_path,
                "configurations_count": sum(len(g["device_info"]) for g in grouped_configs),
                "components_processed": components_processed,
                "components_skipped": components_skipped
            }
            self.log(
                "{0} File path: {1}, Configurations count: {2}, "
                "Components processed: {3}, Components skipped: {4}".format(
                    self.msg,
                    file_path,
                    sum(len(g["device_info"]) for g in grouped_configs),
                    components_processed,
                    components_skipped
                ),
                "INFO"
            )
            self.result["changed"] = True
            self.status = "success"
        else:
            failure_message = "Failed to write YAML configuration file to path: {0}".format(
                file_path
            )
            self.msg = failure_message
            self.result["msg"] = self.msg
            self.result["response"] = {
                "status": "failed",
                "message": failure_message
            }
            self.status = "failed"

            self.log(
                "YAML file write operation failed. Unable to write configuration to file: {0}. "
                "Check file permissions, disk space, and parent directory existence.".format(
                    file_path
                ),
                "ERROR"
            )

        return self

    def get_diff_gathered(self):
        """
        Execute the PnP device gathering workflow to collect brownfield configurations.

        This method orchestrates the complete brownfield PnP device extraction workflow
        by coordinating YAML configuration generation operations based on user-provided
        parameters and filters. It serves as the main execution entry point for the 'gathered'
        state operation.

        Purpose:
            Coordinates the execution of PnP device extraction operations to generate
            Ansible-compatible YAML playbook configurations from existing Cisco Catalyst
            Center PnP inventory (brownfield environments).

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
            "Starting brownfield PnP device gathering workflow for state 'gathered' "
            "to extract existing PnP device registrations from Cisco Catalyst Center "
            "and generate Ansible-compatible YAML playbooks",
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
            "Brownfield PnP device gathering workflow completed. "
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
            "Brownfield PnP device gathering workflow execution finished at "
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
    Main entry point for Ansible module execution.

    Description:
        Initializes brownfield PnP playbook generator module by defining argument
        specification with connection parameters and config options, creating module
        instance with check mode support, instantiating PnPPlaybookGenerator class,
        validating Catalyst Center version compatibility, processing input configurations,
        orchestrating YAML generation workflow through get_want and get_diff_gathered,
        and returning operation results via module.exit_json enabling automated PnP
        device discovery and playbook generation for brownfield environments.

    Workflow:
        1. Define argument specification with DNAC connection and playbook parameters
        2. Initialize AnsibleModule with argument spec and check mode enabled
        3. Create PnPPlaybookGenerator instance with module configuration
        4. Log initialization with current state and version information
        5. Validate Catalyst Center version against minimum required (2.3.7.9)
        6. Exit with error if version incompatible explaining upgrade requirement
        7. Validate operational state against supported states list
        8. Exit with error if state invalid providing valid state options
        9. Validate input configuration against schema using validate_input
        10. Process each configuration item through get_want transformation
        11. Execute YAML generation workflow via get_diff_gathered
        12. Calculate and log total execution time for performance tracking
        13. Return operation results with file path and statistics

    Version Requirements:
        - Minimum Catalyst Center version 2.3.7.9 for PnP device APIs
        - Earlier versions lack required API endpoints for device retrieval
        - Version check performed before configuration processing
        - Module exits with descriptive error when version incompatible

    State Validation:
        - Only 'gathered' state supported for configuration retrieval
        - Invalid states rejected with error before workflow execution
        - State validation prevents unsupported operations

    Error Handling:
        - Version incompatibility exits via check_return_status with error
        - Invalid state detected and rejected with descriptive message
        - Configuration validation failures reported with specific issues
        - All errors logged and returned through standard error flow

    Returns:
        None: Exits via module.exit_json() with operation results including
            status, message, response with file path and statistics, changed
            flag set to False for gathered state, and execution_time_seconds
            for performance monitoring.

    Example:
        Module invocation triggers main() orchestrating complete workflow from
        initialization through validation, processing, and result reporting.
    """
    # Record module initialization start time for performance tracking
    module_start_time = time.time()

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

    module = AnsibleModule(argument_spec=element_spec, supports_check_mode=True)
    pnp_generator = PnPPlaybookGenerator(module)

    pnp_generator.log(
        "Brownfield PnP Playbook Generator module initialized. Starting execution workflow "
        "for state-based operation processing.",
        "INFO"
    )

    # Version check
    pnp_generator.log(
        "Starting Catalyst Center version compatibility check. Retrieving current version "
        "from DNAC instance.",
        "DEBUG"
    )
    current_version = pnp_generator.get_ccc_version()
    min_supported_version = "2.3.7.9"

    pnp_generator.log(
        "Version check completed. Current Catalyst Center version: {0}, Minimum required "
        "version: {1}. Validating compatibility.".format(current_version, min_supported_version),
        "INFO"
    )

    if pnp_generator.compare_dnac_versions(current_version, min_supported_version) < 0:
        pnp_generator.msg = "PnP features require Cisco Catalyst Center version {0} or later. Current version: {1}".format(
            min_supported_version, current_version
        )
        pnp_generator.log(
            "Version compatibility check failed. Current version {0} is below minimum required "
            "version {1}. PnP device APIs unavailable. Module execution terminated.".format(
                current_version, min_supported_version
            ),
            "ERROR"
        )
        pnp_generator.set_operation_result("failed", False, pnp_generator.msg, "CRITICAL")
        module.fail_json(msg=pnp_generator.msg)

    # Get state
    pnp_generator.log(
        "Version compatibility check passed. Proceeding with state parameter validation.",
        "INFO"
    )
    state = pnp_generator.params.get("state")

    pnp_generator.log(
        "Validating state parameter. Requested state: {0}, Supported states: {1}".format(
            state, pnp_generator.supported_states
        ),
        "DEBUG"
    )

    if state not in pnp_generator.supported_states:
        pnp_generator.msg = "State '{0}' is not supported. Supported states: {1}".format(
            state, pnp_generator.supported_states
        )
        pnp_generator.log(
            "State validation failed. Requested state '{0}' not in supported states list: {1}. "
            "Module execution terminated.".format(state, pnp_generator.supported_states),
            "ERROR"
        )
        pnp_generator.set_operation_result("failed", False, pnp_generator.msg, "ERROR")
        module.fail_json(msg=pnp_generator.msg)

    # Validate input
    pnp_generator.log(
        "State validation passed. State '{0}' is supported. Starting input configuration "
        "validation against schema.".format(state),
        "INFO"
    )
    pnp_generator.validate_input().check_return_status()

    pnp_generator.log(
        "Input validation completed successfully. Processing {0} validated configuration "
        "item(s) through YAML generation workflow.".format(len(pnp_generator.validated_config)),
        "INFO"
    )

    # Process configuration
    for config_index, config in enumerate(pnp_generator.validated_config, start=1):
        pnp_generator.log(
            "Processing configuration item {0}/{1}. Extracting desired state and executing "
            "gathered workflow.".format(config_index, len(pnp_generator.validated_config)),
            "DEBUG"
        )
        pnp_generator.get_want(config, state).check_return_status()
        pnp_generator.get_diff_state_apply[state]().check_return_status()

    # Calculate total execution time
    module_end_time = time.time()
    execution_time = module_end_time - module_start_time

    # Add execution time to result for performance tracking
    pnp_generator.result["execution_time_seconds"] = round(execution_time, 2)

    pnp_generator.log(
        "Module execution completed. Total execution time: {0:.2f} seconds. "
        "Module start: {1}, Module end: {2}".format(
            execution_time, module_start_time, module_end_time
        ),
        "INFO"
    )

    module.exit_json(**pnp_generator.result)


if __name__ == "__main__":
    main()
