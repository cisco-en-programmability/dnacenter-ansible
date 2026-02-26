#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright (c) 2026, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

"""Generate detailed site workflow YAML playbooks from Cisco Catalyst Center inventory data.

This module discovers site hierarchy objects from Catalyst Center, applies optional
filters, normalizes the response payloads into `site_workflow_manager` compatible
structures, and writes the result to a YAML file that can be reused for brownfield
automation workflows.
"""
from __future__ import absolute_import, division, print_function

__metaclass__ = type
__author__ = "Vidhya Rathinam"

DOCUMENTATION = r"""
---
module: site_playbook_config_generator
short_description: Generate YAML playbook for 'site_workflow_manager' module.
description:
- Generates YAML configurations compatible with the `site_workflow_manager`
  module, reducing the effort required to manually create Ansible playbooks and
  enabling programmatic modifications.
- The YAML configurations generated represent the site hierarchy (areas, buildings, floors)
  configured on the Cisco Catalyst Center.
version_added: 6.45.0
extends_documentation_fragment:
- cisco.dnac.workflow_manager_params
author:
- Vidhya Rathinam (@VidhyaGit)
- Archit Soni (@koderchit)
- MOHAMED RAFEEK ABDUL KADHAR (@md-rafeek)
- Madhan Sankaranarayanan (@madhansansel)
options:
  state:
    description: The desired state of Cisco Catalyst Center after module execution.
    type: str
    choices: [gathered]
    default: gathered
  config:
    description:
    - A list of filters for generating YAML playbook compatible with the `site_workflow_manager`
      module.
    - Filters specify which components to include in the YAML configuration file.
    - If "components_list" is specified, only those components are included, regardless of the filters.
    type: list
    elements: dict
    required: true
    suboptions:
      generate_all_configurations:
        description:
          - When set to True, automatically generates YAML configurations for all sites and all supported site types.
          - This mode discovers all managed sites in Cisco Catalyst Center and extracts all supported configurations.
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
          a default file name  "site_playbook_config_<YYYY-MM-DD_HH-MM-SS>.yml".
        - For example, "site_playbook_config_2026-02-24_12-33-20.yml".
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
            - Valid value is C(site), which includes all site components (areas, buildings, floors)
              and supports all filter keys.
            - If not specified, all components are included.
            - For example, ["site"].
            type: list
            elements: str
            choices: ["site"]
          site:
            description:
              - Contains site filter expressions for site hierarchy extraction.
              - Supported keys in each list item are C(site_name_hierarchy),
                C(parent_name_hierarchy), and C(site_type).
            type: list
            elements: dict
            suboptions:
              site_name_hierarchy:
                description:
                  - Site name hierarchy filter.
                type: str
              parent_name_hierarchy:
                description:
                  - Parent site name hierarchy filter.
                type: str
              site_type:
                description:
                  - Site type filter.
                  - Valid values are "area", "building", and "floor".
                  - Can be a list to match multiple site types.
                type: list
                elements: str
requirements:
- dnacentersdk >= 2.3.7.9
- python >= 3.9
notes:
- SDK Methods used are
    - sites.Sites.get_sites
- Paths used are
    - GET /dna/intent/api/v1/sites
seealso:
- module: cisco.dnac.site_workflow_manager
  description: Module for managing site configurations.
- name: Site Management API
  description: Specific documentation for site operations in Catalyst Center version.
  link: https://developer.cisco.com/docs/dna-center/#!sites
"""

EXAMPLES = r"""
- name: Generate YAML configuration with site_name_hierarchy only
  cisco.dnac.site_playbook_config_generator:
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
      - file_path: "/tmp/case1_site_name_hierarchy_only.yaml"
        component_specific_filters:
          components_list: ["site"]
          site:
            - site_name_hierarchy: "Global/USA/San Jose"

- name: Generate YAML configuration with parent_name_hierarchy only
  cisco.dnac.site_playbook_config_generator:
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
      - file_path: "/tmp/case2_parent_name_hierarchy_only.yaml"
        component_specific_filters:
          components_list: ["site"]
          site:
            - parent_name_hierarchy: "Global/USA"

- name: Generate YAML configuration with site_name_hierarchy and parent_name_hierarchy
  cisco.dnac.site_playbook_config_generator:
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
      - file_path: "/tmp/case3_site_and_parent_only.yaml"
        component_specific_filters:
          components_list: ["site"]
          site:
            - site_name_hierarchy: "Global/USA/San Jose"
              parent_name_hierarchy: "Global/USA"

- name: Generate YAML configuration with no hierarchy input
  cisco.dnac.site_playbook_config_generator:
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
      - file_path: "/tmp/case4_no_hierarchy_filters.yaml"
        component_specific_filters:
          components_list: ["site"]

- name: Generate YAML configuration with site_name_hierarchy and site_type list
  cisco.dnac.site_playbook_config_generator:
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
      - file_path: "/tmp/case5_site_name_and_site_type.yaml"
        component_specific_filters:
          components_list: ["site"]
          site:
            - site_name_hierarchy: "Global/USA/San Jose"
              site_type:
                - "building"
                - "floor"

- name: Generate YAML configuration with parent_name_hierarchy and site_type
  cisco.dnac.site_playbook_config_generator:
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
      - file_path: "/tmp/case6_parent_name_and_site_type.yaml"
        component_specific_filters:
          components_list: ["site"]
          site:
            - parent_name_hierarchy: "Global/USA"
              site_type:
                - "building"

- name: Generate YAML configuration with all filters
  cisco.dnac.site_playbook_config_generator:
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
      - file_path: "/tmp/case7_all_filters.yaml"
        component_specific_filters:
          components_list: ["site"]
          site:
            - site_name_hierarchy: "Global/USA/San Jose"
              parent_name_hierarchy: "Global/USA"
              site_type:
                - "building"
                - "floor"

- name: Generate YAML configuration with site_type only
  cisco.dnac.site_playbook_config_generator:
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
      - file_path: "/tmp/case8_site_type_only.yaml"
        component_specific_filters:
          components_list: ["site"]
          site:
            - site_type:
                - "area"

- name: Auto-generate YAML configuration for all sites
  cisco.dnac.site_playbook_config_generator:
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
        file_path: "/tmp/case9_all_sites.yaml"

- name: Auto-generate YAML configuration with default file path
  cisco.dnac.site_playbook_config_generator:
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
"""


RETURN = r"""
# Case_1: Success Scenario
response_1:
  description: A dictionary with the response returned by the Cisco Catalyst Center Python SDK
  returned: always
  type: dict
  sample: >
    {
        "msg": {
            "status": "success",
            "message": "YAML configuration file generated successfully for module 'site_workflow_manager'",
            "file_path": "site_playbook_config_2026-02-02_16-04-06.yml",
            "components_processed": 3,
            "components_skipped": 0,
            "configurations_count": 6
        },
        "response": {
            "status": "success",
            "message": "YAML configuration file generated successfully for module 'site_workflow_manager'",
            "file_path": "site_playbook_config_2026-02-02_16-04-06.yml",
            "components_processed": 3,
            "components_skipped": 0,
            "configurations_count": 6
        },
        "status": "success"
    }
# Case_2: Error Scenario
response_2:
  description: A string with the response returned by the Cisco Catalyst Center Python SDK
  returned: always
  type: list
  sample: >
    {
      "msg": {
        "status": "ok",
        "message": "No configurations found for module 'site_workflow_manager'. Verify filters and component availability. Components attempted: ['site']",
        "components_attempted": 3,
        "components_processed": 0,
        "components_skipped": 0
      },
      "response": {
        "status": "ok",
        "message": "No configurations found for module 'site_workflow_manager'. Verify filters and component availability. Components attempted: ['site']",
        "components_attempted": 3,
        "components_processed": 0,
        "components_skipped": 0
      }
    }
# Case_3: Error Scenario
response_3:
  description: A string with the response returned by the Cisco Catalyst Center Python SDK
  returned: always
  type: list
  sample: >
    {
      "msg": "Invalid parameters in playbook: [\"Invalid 'site_type' values in
      'component_specific_filters.site[1]': ['campus']. Supported values are
      ['area', 'building', 'floor'].\"]",
      "response": "Invalid parameters in playbook: [\"Invalid 'site_type'
      values in 'component_specific_filters.site[1]': ['campus']. Supported
      values are ['area', 'building', 'floor'].\"]"
    }
"""

from ansible.module_utils.basic import AnsibleModule
from ansible_collections.cisco.dnac.plugins.module_utils.brownfield_helper import (
    BrownFieldHelper,
    SingleQuotedStr,
    DoubleQuotedStr,
)
from ansible_collections.cisco.dnac.plugins.module_utils.dnac import (
    DnacBase,
)
from ansible_collections.cisco.dnac.plugins.module_utils.validation import (
    validate_list_of_dicts,
)
import time
import logging
import inspect
import re

try:
    import yaml

    HAS_YAML = True
except ImportError:
    HAS_YAML = False
    yaml = None
from collections import OrderedDict

LOGGER = logging.getLogger(__name__)


if HAS_YAML:

    class OrderedDumper(yaml.Dumper):
        def represent_dict(self, data):
            LOGGER.debug(
                "OrderedDumper.represent_dict started; converting dictionary-like data "
                "into a deterministic YAML mapping while preserving insertion order. "
                "Incoming data type: %s",
                type(data),
            )
            LOGGER.debug(
                "OrderedDumper.represent_dict completed successfully; returning YAML "
                "mapping representation based on OrderedDict item order."
            )
            return self.represent_mapping("tag:yaml.org,2002:map", data.items())

    OrderedDumper.add_representer(OrderedDict, OrderedDumper.represent_dict)
else:
    OrderedDumper = None


class SitePlaybookGenerator(DnacBase, BrownFieldHelper):
    """
    Orchestrates brownfield site playbook generation for Catalyst Center inventories.

    This class is responsible for end-to-end processing of site hierarchy export:
    input validation, component filter normalization, API query construction,
    post-processing and de-duplication of site records, reverse mapping of API
    fields to `site_workflow_manager` schema, and YAML file generation.

    Inheritance:
    - `DnacBase`: provides Catalyst Center client/session utilities, standardized
      result handling, and framework-level lifecycle hooks.
    - `BrownFieldHelper`: provides reusable transformation helpers used by the
      brownfield workflow modules for schema mapping and YAML serialization.

    Operational scope:
    - Site components: areas, buildings, floors
    - Supported filters: `site_name_hierarchy`, `parent_name_hierarchy`, `site_type`
    - State mode: `gathered`
    """

    values_to_nullify = ["NOT CONFIGURED"]
    filter_list_fields = (
        "site_name_hierarchy",
        "parent_name_hierarchy",
        "site_type",
    )

    def __init__(self, module):
        """
        Initialize generator state and precompute module schema metadata.

        Args:
            module (AnsibleModule): Active Ansible module instance containing user
                parameters, runtime options, and connection credentials.

        Side effects:
            - Registers supported states for this module implementation.
            - Initializes inherited base/helper layers.
            - Builds and stores workflow element schema definitions.
            - Sets module identity used in result and logging messages.
        """
        LOGGER.debug(
            "SitePlaybookGenerator.__init__ invoked; initializing module-specific "
            "runtime state and preparing static schema definitions."
        )
        self.supported_states = ["gathered"]
        super().__init__(module)
        self.module_schema = self.get_workflow_elements_schema()
        self.module_name = "site_workflow_manager"
        self._compiled_regex_cache = {}
        self._direct_filter_mode = False
        self.unified_filter_mode_enabled = False
        self._normalized_component_specific_filters = {}
        self._unified_site_records_cache = None
        self._unified_site_records_cache_key = None
        self.log(
            "Initialization complete. Supported states, module schema, and module "
            "identity are ready for request processing. "
            f"Resolved module_name={self.module_name}.",
            "INFO",
        )
        self.log(
            "Execution context: this module collects and transforms site hierarchy "
            "data for YAML playbook generation. Diagnostic guidance: validate input "
            "schema, filter processing, API retrieval outcomes, and YAML "
            "serialization when troubleshooting failures.",
            "DEBUG",
        )

    def log(self, msg, level="INFO"):
        """Emit a normalized, context-rich log message for this module.

        This override ensures that every class-level log call carries actionable
        runtime metadata in a consistent format, so troubleshooting can be done
        without guessing the active state or input mode.

        Args:
            msg (str): The base log message generated at the call site.
            level (str): Severity level passed through to the base logger.

        Returns:
            Any: The return value from `DnacBase.log`.
        """
        module_name = getattr(self, "module_name", "site_workflow_manager")
        status = getattr(self, "status", "unset")
        generate_all = getattr(self, "generate_all_configurations", "unset")
        base_message = str(msg)
        caller_name = "unknown"
        caller_line = "unknown"
        caller_frame = inspect.currentframe()
        if caller_frame and caller_frame.f_back:
            caller_name = caller_frame.f_back.f_code.co_name
            caller_line = caller_frame.f_back.f_lineno
        del caller_frame

        interpreted_message = base_message

        detailed_msg = (
            f"[module={module_name}] [class={self.__class__.__name__}] "
            f"[status={status}] [generate_all_configurations={generate_all}] "
            f"[caller={caller_name}:{caller_line}] "
            f"{interpreted_message}"
        )
        return super().log(detailed_msg, level)

    def validate_input(self):
        """
        Validate top-level configuration objects before workflow execution begins.

        Validation includes required container structure checks and field-type
        enforcement for known keys such as `generate_all_configurations`,
        `file_path`, `component_specific_filters`, and `global_filters`.

        Args:
            self: Instance context containing module params and result setters.

        Returns:
            SitePlaybookGenerator: The same instance with updated status fields.

        Side effects:
            - Sets `self.validated_config` on success.
            - Sets `self.msg`/`self.status` for both success and failure paths.
            - Calls `set_operation_result` to persist operation outcomes.
        """
        # Begin module-level payload validation so downstream execution can assume
        # a predictable structure and avoid defensive checks in every method.
        self.log("Starting validation of input configuration parameters.", "INFO")

        # If the user did not provide config entries, this module chooses a
        # non-failing success path and records a descriptive status message.
        if not self.config:
            self.log(
                "Configuration payload is not available in playbook input; "
                "skipping schema validation.",
                "INFO",
            )
            self.status = "success"
            self.msg = "Configuration is not available in the playbook for validation"
            self.log(f"{self.msg}", "ERROR")
            self.log(
                "Validation stopped because configuration payload is missing.",
                "INFO",
            )
            return self

        # Declare the minimal accepted schema for one config dictionary so the
        # shared validator can catch unknown keys and type mismatches early.
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

        # Execute schema validation over the complete config list and collect
        # invalid keys in one pass.
        self.log("Validating configuration against schema.", "INFO")
        valid_temp, invalid_params = validate_list_of_dicts(self.config, temp_spec)

        for config_entry in valid_temp:
            structure_errors = self.validate_component_specific_filters_structure(
                config_entry
            )
            if structure_errors:
                invalid_params.extend(structure_errors)

        # Fail fast when unknown/invalid keys are present to prevent ambiguous
        # runtime behavior later in normalization and API execution.
        if invalid_params:
            self.log(
                "Validation detected invalid parameters in configuration payload.",
                "INFO",
            )
            self.msg = f"Invalid parameters in playbook: {invalid_params}"
            self.set_operation_result("failed", False, self.msg, "ERROR")
            self.log(
                "Validation failed because invalid configuration parameters were found.",
                "INFO",
            )
            return self

        # Persist normalized validator output for subsequent processing stages
        # (`get_want` and gather execution workflow).
        self.validated_config = valid_temp
        self.msg = (
            "Successfully validated playbook configuration parameters using 'validated_input': "
            f"{valid_temp}"
        )
        self.set_operation_result("success", False, self.msg, "INFO")
        self.log(
            "Validation completed successfully for all configuration entries.", "INFO"
        )
        return self

    def get_workflow_elements_schema(self):
        """
        Build canonical schema metadata for supported site workflow components.

        The returned structure defines, per component, which filters are supported,
        which API family/function should be invoked, and which transformation
        function should convert raw API responses into module output shape. This
        schema is used as the single source of truth by the orchestration path.

        Args:
            self: Instance context used for binding callable handler references.

        Returns:
            dict: Structured map with component definitions for:
                - `site`
            and top-level `global_filters` metadata.
        """
        self.log(
            "Building workflow element schema for site retrieval operations.", "INFO"
        )

        schema = {
            "network_elements": {
                "site": {
                    "filters": [
                        "site_name_hierarchy",
                        "parent_name_hierarchy",
                        "site_type",
                    ],
                    "reverse_mapping_function": None,
                    "api_function": "get_sites",
                    "api_family": "site_design",
                    "get_function_name": self.get_sites_configuration,
                },
            },
            "global_filters": [],
        }
        self.log("Workflow element schema prepared successfully.", "INFO")
        return schema

    def get_parent_name(self, detail):
        """
        Resolve `parent_name` value for output serialization.

        Args:
            detail (dict): Raw or partially normalized site record.

        Returns:
            SingleQuotedStr | None: Parent site identifier in single-quoted wrapper,
            or `None` when no valid parent value can be resolved.
        """
        self.log("Resolving parent name from site record", "INFO")

        if not isinstance(detail, dict):
            self.log(
                "Cannot extract parent name because the "
                "site record is not a dict (type={0}). "
                "Returning None.".format(type(detail).__name__),
                "WARNING",
            )
            return None

        parent_name = detail.get("parentName")
        if parent_name:
            self.log(
                "Resolved parent name from 'parentName' field: {0}.".format(
                    parent_name
                ),
                "INFO",
            )
            return SingleQuotedStr(parent_name)

        parent_name_hierarchy = detail.get("parentNameHierarchy")
        if parent_name_hierarchy:
            self.log(
                "Resolved parent name hierarchy from 'parentNameHierarchy' field: {0}.".format(
                    parent_name_hierarchy
                ),
                "INFO",
            )
            return SingleQuotedStr(parent_name_hierarchy)

        name = detail.get("name")
        name_hierarchy = detail.get("nameHierarchy")

        if not name or not name_hierarchy:
            self.log(
                "Unable to derive parent name; 'name' or "
                "'nameHierarchy' is missing "
                "(name={0}, nameHierarchy={1}). "
                "Returning None.".format(name, name_hierarchy),
                "INFO",
            )
            return None

        token = "/" + str(name)
        if token not in name_hierarchy:
            self.log(
                "Unable to derive parent name; terminal "
                "token '{0}' not found in "
                "nameHierarchy '{1}'. "
                "Returning None.".format(token, name_hierarchy),
                "INFO",
            )
            return None

        derived_parent = name_hierarchy.rsplit(token, 1)[0]
        self.log(
            "Derived parent name by stripping terminal "
            "node '{0}' from nameHierarchy '{1}': "
            "resolved={2}.".format(name, name_hierarchy, derived_parent),
            "INFO",
        )

        if derived_parent:
            return SingleQuotedStr(derived_parent)

        self.log(
            "Cannot resolve parent name from the site record. Returning None.", "INFO"
        )
        return None

    def get_name_hierarchy(self, detail):
        """
        Fetch the site hierarchy path from a detail payload.

        This helper accepts both current and legacy naming keys so downstream
        filter and post-filter functions can operate on a stable value.

        Args:
            detail (dict): Site payload returned from Catalyst Center API.

        Returns:
            str | None: Hierarchy string such as `Global/USA/SanJose` when present.
        """
        if not isinstance(detail, dict):
            self.log(
                "Cannot resolve nameHierarchy because the "
                "site record is not a dict (type={0}). "
                "Returning None.".format(type(detail).__name__),
                "WARNING",
            )
            return None

        name_hierarchy = detail.get("nameHierarchy")
        if name_hierarchy:
            self.log(
                "Resolved nameHierarchy from site "
                "record: '{0}'.".format(name_hierarchy),
                "INFO",
            )
            return name_hierarchy

        self.log(
            "Cannot resolve nameHierarchy because key "
            "'nameHierarchy' is absent or empty in the site record. "
            "Returning None.",
            "INFO",
        )
        return None

    def get_parent_name_hierarchy(self, detail):
        """
        Resolve `parentNameHierarchy` from a site payload, with derivation fallback.

        Resolution priority:
        1. Explicit ``parentNameHierarchy`` key from the API response.
        2. Derived by stripping the terminal node from
        ``nameHierarchy`` (requires at least one ``/`` separator).
        3. Fallback to the ``parentName`` key when neither of the
        above yields a value.

        Root-level records whose ``nameHierarchy`` contains no ``/``
        separator (e.g. ``Global``) skip derivation and fall through
        to the ``parentName`` fallback.

        Args:
            detail (dict): Site payload candidate for parent hierarchy resolution.

        Returns:
            str | None: Parent hierarchy string if available or derivable.
        """
        self.log(
            "Resolving parent name hierarchy from site "
            "record with keys={0}.".format(
                list(detail.keys())
                if isinstance(detail, dict)
                else type(detail).__name__
            ),
            "INFO",
        )

        if not isinstance(detail, dict):
            self.log(
                "Cannot resolve parent name hierarchy "
                "because the site record is not a dict "
                "(type={0}). Returning None.".format(type(detail).__name__),
                "WARNING",
            )
            return None

        parent_name_hierarchy = detail.get("parentNameHierarchy")
        if parent_name_hierarchy:
            self.log(
                "Resolved parentNameHierarchy from site record: "
                "'{0}'.".format(parent_name_hierarchy),
                "INFO",
            )
            return parent_name_hierarchy

        name_hierarchy = self.get_name_hierarchy(detail)
        if name_hierarchy and "/" in name_hierarchy:
            derived_parent = name_hierarchy.rsplit("/", 1)[0]
            self.log(
                "Derived parent name hierarchy '{0}' from "
                "nameHierarchy '{1}'.".format(derived_parent, name_hierarchy),
                "INFO",
            )
            return derived_parent

        parent_name = detail.get("parentName")
        if parent_name:
            self.log(
                "Resolved parent name hierarchy from parentName "
                "field: '{0}'.".format(parent_name),
                "INFO",
            )
            return parent_name

        self.log(
            "Cannot resolve parent name hierarchy because keys "
            "'parentNameHierarchy', 'nameHierarchy', and 'parentName' "
            "did not provide a usable value. Returning None.",
            "INFO",
        )
        return None

    def get_site_type_value(self, detail):
        """
        Extracts the ``type`` field from the supplied site payload
        dictionary. Returns None when the record is not a dict or
        the key is absent/empty.

        Args:
            detail (dict): Site record expected to contain `type` or `siteType`.

        Returns:
            str | None: Canonical type label (`area`, `building`, `floor`) when found.
        """
        if not isinstance(detail, dict):
            self.log(
                "Cannot resolve site type because the "
                "site record is not a dict (type={0}). "
                "Returning None.".format(type(detail).__name__),
                "WARNING",
            )
            return None

        site_type = detail.get("type")
        if site_type:
            self.log(
                "Resolved site type from site record: '{0}'.".format(site_type),
                "INFO",
            )
            return site_type

        self.log(
            "Cannot resolve site type because key 'type' is absent or empty "
            "in the site record. Returning None.",
            "INFO",
        )
        return None

    def get_site_type_area(self, detail):
        """Return fixed type label for area records.

        Args:
            detail (dict): Ignored input retained for transform function signature
                compatibility.

        Returns:
            str: Literal value `area`.
        """
        self.log(
            "Returning fixed site type value 'area' for area record mapping.", "INFO"
        )
        return "area"

    def get_site_type_building(self, detail):
        """Return fixed type label for building records.

        Args:
            detail (dict): Ignored input retained for transform function signature
                compatibility.

        Returns:
            str: Literal value `building`.
        """
        self.log(
            "Returning fixed site type value 'building' for building record mapping.",
            "INFO",
        )
        return "building"

    def get_site_type_floor(self, detail):
        """Return fixed type label for floor records.

        Args:
            detail (dict): Ignored input retained for transform function signature
                compatibility.

        Returns:
            str: Literal value `floor`.
        """
        self.log(
            "Returning fixed site type value 'floor' for floor record mapping.", "INFO"
        )
        return "floor"

    def normalize_site_filter_param(self, filter_param):
        """
        Normalize incoming filter input into canonical dictionary representation.

        String filters are interpreted as `nameHierarchy` values. Dictionary
        filters are shallow-copied so callers can mutate the returned object
        safely without affecting the original payload.

        Args:
            filter_param (dict | str): User-supplied filter object.

        Returns:
            dict: Canonical filter map suitable for query context construction.
        """
        if isinstance(filter_param, dict):
            return dict(filter_param)

        return {"nameHierarchy": filter_param}

    def freeze_filter_value(self, value, _depth=0):
        """
        Recursively convert a mutable filter value into a
        hashable, immutable representation.

        Dicts become sorted tuples of ``(key, frozen_value)``
        pairs, lists become tuples of frozen elements, and
        scalar values are returned unchanged. The result is
        suitable for use as a dict key or set member when
        deduplicating filter combinations.

        Args:
            value: Filter value to freeze. May be a dict, list,
                or any hashable scalar (str, int, bool, None).
            _depth (int): Internal recursion depth tracker used
                to restrict logging to the top-level call only.
                Callers should not supply this argument.

        Returns:
            tuple | scalar: An immutable, hashable equivalent of
                the input value.
        """
        if _depth == 0:
            self.log(
                "Freezing filter value of type "
                "'{0}' into a hashable "
                "representation: {1}.".format(type(value).__name__, value),
                "DEBUG",
            )

        if isinstance(value, dict):
            result = tuple(
                sorted(
                    (k, self.freeze_filter_value(v, _depth + 1))
                    for k, v in value.items()
                )
            )
            if _depth == 0:
                self.log(
                    "Frozen dict filter value " "to: {0}.".format(result),
                    "DEBUG",
                )
            return result

        if isinstance(value, list):
            result = tuple(self.freeze_filter_value(item, _depth + 1) for item in value)
            if _depth == 0:
                self.log(
                    "Frozen list filter value " "to: {0}.".format(result),
                    "DEBUG",
                )
            return result

        if _depth == 0:
            self.log(
                "Filter value is a scalar "
                "(type={0}); returning "
                "unchanged: {1}.".format(type(value).__name__, value),
                "DEBUG",
            )
        return value

    def build_filter_signature(self, filter_item):
        """
        Build a stable signature for one filter expression.

        Args:
            filter_item (Any): Filter expression entry.

        Returns:
            tuple: Canonical signature tuple.
        """
        return ("filter_item", self.freeze_filter_value(filter_item))

    def dedupe_filter_expressions(self, filters, context_name):
        """
        Remove duplicate filter expressions while preserving
        original insertion order.

        Each expression is recursively frozen into an immutable
        hashable form via ``freeze_filter_value`` and tracked in
        a set. Only the first occurrence of each unique expression
        is retained.

        Args:
            filter_expressions (list[dict]): List of filter
                expression dicts to deduplicate. May be None
                or empty.

        Returns:
            list[dict]: Deduplicated filter expressions in
                their original order. Returns an empty list
                when the input is None or empty.
        """
        self.log(
            "Deduplicating filter expressions; received {0} expression(s).".format(
                len(filters) if filters else 0
            ),
            "INFO",
        )

        if not filters:
            self.log("No filter expressions provided; returning empty list.", "INFO")
            return []

        if not isinstance(filters, list):
            return filters

        seen_signatures = set()
        deduped_filters = []
        duplicates_ignored = 0
        for index, filter_item in enumerate(filters):
            self.log(
                "Processing filter expression at "
                "index {0}: {1}.".format(index, filter_item),
                "DEBUG",
            )
            signature = self.build_filter_signature(filter_item)
            if signature in seen_signatures:
                duplicates_ignored += 1
                continue
            seen_signatures.add(signature)
            deduped_filters.append(filter_item)

        self.log(
            "Filter dedupe summary for {0}: incoming_filters={1}, "
            "duplicates_ignored={2}, output_filters={3}.".format(
                context_name,
                len(filters),
                duplicates_ignored,
                len(deduped_filters),
            ),
            "INFO",
        )
        return deduped_filters

    def get_compiled_regex(self, regex_pattern):
        """
        Retrieve compiled regex from cache or compile and cache it.

        Args:
            regex_pattern (str): Regex pattern string.

        Returns:
            Pattern | None: Compiled regex object or None when invalid.
        """
        regex_cache = getattr(self, "_compiled_regex_cache", None)
        if regex_cache is None:
            regex_cache = {}
            self._compiled_regex_cache = regex_cache

        if regex_pattern in regex_cache:
            return regex_cache.get(regex_pattern)

        try:
            compiled_pattern = re.compile(regex_pattern)
        except re.error:
            compiled_pattern = None

        regex_cache[regex_pattern] = compiled_pattern
        return compiled_pattern

    def build_site_query_context(self, filter_param, component_type):
        """
        Build API request parameters and local post-filter criteria per component.

        Catalyst Center supports part of the filtering server-side. Any filter
        that cannot be passed directly in request parameters is returned as a
        post-filter entry to be evaluated locally after retrieval.

        Args:
            filter_param (dict): Canonical or pre-normalized filter map.
            component_type (str): Target component type for the current query.

        Returns:
            tuple: `(params, post_filters)` where:
                - `params`: API query params
                - `post_filters`: additional predicates for local filtering
            Returns `(None, None)` when filter type conflicts with component type.
        """
        self.log(
            "Building site query context using provided filter payload for "
            "component type '{0}'.".format(component_type),
            "INFO",
        )
        # Convert user-provided filter expression to canonical dictionary form.
        normalized_param = self.normalize_site_filter_param(filter_param)
        # Every component query always includes a type constraint to avoid
        # cross-component payload mixing in API responses.
        params = {"type": component_type}
        # Some filters are intentionally applied post-retrieval for hierarchical
        # scope semantics that are not pushed directly to the API call.
        post_filters = {}
        applied_query_filters = 1  # `type` is always set to component type.
        applied_post_filters = 0
        ignored_filters = 0

        # Apply nameHierarchy directly only for exact-value matches. Pattern-like
        # filters are intentionally evaluated as local post-filters because
        # endpoint behavior for wildcard/regex expressions may vary by release.
        name_hierarchy = normalized_param.get("nameHierarchy")
        if name_hierarchy:
            if self.is_pattern_based_hierarchy_filter(name_hierarchy):
                post_filters["nameHierarchy"] = name_hierarchy
                applied_post_filters += 1
            else:
                params["nameHierarchy"] = name_hierarchy
                applied_query_filters += 1

        # Validate explicit type filter against currently processed component.
        # Non-matching values are skipped instead of silently broadening results.
        filter_type = normalized_param.get("type")
        if filter_type:
            if filter_type != component_type:
                ignored_filters += 1
                self.log(
                    "Skipping filter because type '{0}' does not match "
                    "component type '{1}'.".format(filter_type, component_type),
                    "WARNING",
                )
                self.log(
                    "Site query context resolution failed due to type mismatch "
                    "between filter and component target. "
                    "applied_query_filters={0}, applied_post_filters={1}, "
                    "ignored_filters={2}.".format(
                        applied_query_filters,
                        applied_post_filters,
                        ignored_filters,
                    ),
                    "INFO",
                )
                return None, None
            params["type"] = filter_type

        # Preserve parentNameHierarchy for post-filter evaluation so hierarchical
        # descendant matching is handled in local processing.
        parent_name_hierarchy = normalized_param.get("parentNameHierarchy")
        if parent_name_hierarchy:
            post_filters["parentNameHierarchy"] = parent_name_hierarchy
            applied_post_filters += 1

        self.log(
            "Resolved site query context with API params and "
            "post-filter criteria. applied_query_filters={0}, "
            "applied_post_filters={1}, ignored_filters={2}, "
            "resolved_query_params={3}, resolved_post_filters={4}.".format(
                applied_query_filters,
                applied_post_filters,
                ignored_filters,
                params,
                post_filters,
            ),
            "INFO",
        )
        return params, post_filters

    def apply_site_post_filters(self, details, post_filters):
        """
        Apply local filter predicates to site detail records after API retrieval.

        This stage enforces `parentNameHierarchy` in hierarchical scope mode:
        records are retained when the filter value matches the record itself or
        any descendant path under that value.

        Args:
            details (list): Raw list returned from API calls.
            post_filters (dict): Locally enforced predicates.

        Returns:
            list: Filtered record list preserving original order.
        """
        self.log(
            "Applying site post-filters to candidate record set.",
            "INFO",
        )
        start_time = time.time()
        input_records = self.get_record_count(details)
        # If no post-filter constraints were provided, return records as-is to
        # avoid unnecessary traversal and preserve API ordering.
        if not post_filters:
            end_time = time.time()
            self.log(
                "No post-filters were provided; returning records unchanged. "
                "start_time={start_time:.6f}, end_time={end_time:.6f}, "
                "duration_seconds={duration_seconds:.6f}, input_records={input_records}, "
                "output_records={output_records}, filtered_out_records=0, "
                "processed_filter_keys=0, skipped_filter_keys=2.".format(
                    start_time=start_time,
                    end_time=end_time,
                    duration_seconds=end_time - start_time,
                    input_records=input_records,
                    output_records=input_records,
                ),
                "INFO",
            )
            return details

        # Start from the full candidate set and narrow down incrementally per
        # supported post-filter key.
        filtered_details = details
        processed_filter_keys = 0
        skipped_filter_keys = 0
        filtered_out_by_name_hierarchy = 0
        filtered_out_by_parent_hierarchy = 0
        name_hierarchy = post_filters.get("nameHierarchy")
        if name_hierarchy:
            processed_filter_keys += 1
            # Apply regex/pattern-aware filtering against full hierarchy path.
            before_name_hierarchy_filter = self.get_record_count(filtered_details)
            filtered_details = [
                detail
                for detail in filtered_details
                if self.matches_name_hierarchy_filter(detail, name_hierarchy)
            ]
            after_name_hierarchy_filter = self.get_record_count(filtered_details)
            filtered_out_by_name_hierarchy = max(
                0, before_name_hierarchy_filter - after_name_hierarchy_filter
            )
        else:
            skipped_filter_keys += 1

        parent_name_hierarchy = post_filters.get("parentNameHierarchy")
        if parent_name_hierarchy:
            processed_filter_keys += 1
            # Enforce hierarchical scope semantics by retaining records that
            # match the scope root or any descendants.
            before_parent_name_hierarchy_filter = self.get_record_count(
                filtered_details
            )
            filtered_details = [
                detail
                for detail in filtered_details
                if self.matches_parent_name_hierarchy_scope(
                    detail, parent_name_hierarchy
                )
            ]
            after_parent_name_hierarchy_filter = self.get_record_count(filtered_details)
            filtered_out_by_parent_hierarchy = max(
                0,
                before_parent_name_hierarchy_filter
                - after_parent_name_hierarchy_filter,
            )
        else:
            skipped_filter_keys += 1

        output_records = self.get_record_count(filtered_details)
        end_time = time.time()
        total_filtered_out_records = max(0, input_records - output_records)

        self.log(
            "Completed site post-filter evaluation. "
            "start_time={0:.6f}, end_time={1:.6f}, "
            "duration_seconds={2:.6f}, input_records={3}, output_records={4}, "
            "filtered_out_records={5}, processed_filter_keys={6}, "
            "skipped_filter_keys={7}, filtered_out_by_name_hierarchy={8}, "
            "filtered_out_by_parent_name_hierarchy={9}.".format(
                start_time,
                end_time,
                end_time - start_time,
                input_records,
                output_records,
                total_filtered_out_records,
                processed_filter_keys,
                skipped_filter_keys,
                filtered_out_by_name_hierarchy,
                filtered_out_by_parent_hierarchy,
            ),
            "INFO",
        )
        return filtered_details

    def normalize_hierarchy_path(self, hierarchy_value):
        """
        Normalize hierarchy string values for stable prefix comparison.

        Args:
            hierarchy_value (Any): Candidate hierarchy value from filters or API.

        Returns:
            str | None: Normalized hierarchy without surrounding spaces or slashes.
        """
        # Treat explicit None as missing input to keep helper behavior predictable.
        if hierarchy_value is None:
            return None

        # Normalize formatting differences so matching logic is resilient to
        # user input variance (whitespace or leading/trailing slash).
        normalized_value = str(hierarchy_value).strip().strip("/")
        if not normalized_value:
            return None

        return normalized_value

    def hierarchy_matches_scope(self, hierarchy_value, scope_value):
        """
        Determine whether a hierarchy value satisfies a scope expression.

        Supported scope expression styles:
        - Plain hierarchy string (for example `Global/USA`): match scope node
          itself and descendants.
        - Pattern hierarchy (for example `Global/USA/.*`): evaluated with the
          same wildcard/regex logic used for nameHierarchy pattern matching.

        Args:
            hierarchy_value (str): Candidate hierarchy from site record.
            scope_value (str): Filter scope hierarchy value.

        Returns:
            bool: True when candidate matches the scope expression.
        """
        # Standardize both values before comparing to avoid format artifacts.
        normalized_hierarchy = self.normalize_hierarchy_path(hierarchy_value)
        normalized_scope = self.normalize_hierarchy_path(scope_value)

        # Reject empty values quickly to avoid false-positive prefix matches.
        if not normalized_hierarchy or not normalized_scope:
            return False

        # If scope contains wildcard/regex intent, evaluate using hierarchy
        # pattern matcher so expressions like `Global/USA/.*` work as expected.
        if self.is_pattern_based_hierarchy_filter(normalized_scope):
            return self.hierarchy_matches_name_filter(
                normalized_hierarchy, normalized_scope
            )

        # Exact match means the node itself is in scope.
        if normalized_hierarchy == normalized_scope:
            return True

        # Prefix-with-separator means descendant under requested scope.
        return normalized_hierarchy.startswith(normalized_scope + "/")

    def is_pattern_based_hierarchy_filter(self, hierarchy_filter):
        """
        Detect whether hierarchy filter expression contains wildcard/regex intent.

        Args:
            hierarchy_filter (Any): User-provided hierarchy filter value.

        Returns:
            bool: True when local regex/pattern evaluation should be used.
        """
        normalized_filter = self.normalize_hierarchy_path(hierarchy_filter)
        if not normalized_filter:
            return False

        # Treat common wildcard/regex symbols as pattern intent indicators.
        pattern_tokens = ("*", "?", "[", "]", "(", ")", "{", "}", "|", "^", "$", "+")
        return ".*" in normalized_filter or any(
            token in normalized_filter for token in pattern_tokens
        )

    def hierarchy_matches_name_filter(self, hierarchy_value, hierarchy_filter):
        """
        Match a hierarchy value against exact or pattern-based nameHierarchy filter.

        Matching behavior:
        - Exact filter (no pattern tokens): strict equality
        - `.../.*` filter: descendant prefix match (`scope/child...`)
        - Generic pattern filter: Python regex full-match

        Args:
            hierarchy_value (Any): Candidate site hierarchy value from API payload.
            hierarchy_filter (Any): User-provided nameHierarchy filter expression.

        Returns:
            bool: True when candidate satisfies the filter expression.
        """
        normalized_hierarchy = self.normalize_hierarchy_path(hierarchy_value)
        normalized_filter = self.normalize_hierarchy_path(hierarchy_filter)
        if not normalized_hierarchy or not normalized_filter:
            return False

        if not self.is_pattern_based_hierarchy_filter(normalized_filter):
            return normalized_hierarchy == normalized_filter

        # Fast path for hierarchy wildcard syntax used in playbooks:
        # `Global/USA/.*` means every descendant path under `Global/USA`.
        if normalized_filter.endswith("/.*"):
            scope_prefix = normalized_filter[:-3]
            return normalized_hierarchy.startswith(scope_prefix + "/")

        # Fallback to regex evaluation for advanced expressions.
        compiled_pattern = self.get_compiled_regex(normalized_filter)
        if compiled_pattern is None:
            self.log(
                "Invalid hierarchy regular expression provided in filter; "
                "falling back to exact string comparison.",
                "WARNING",
            )
            return normalized_hierarchy == normalized_filter
        return compiled_pattern.fullmatch(normalized_hierarchy) is not None

    def matches_name_hierarchy_filter(self, detail, name_hierarchy_filter):
        """
        Evaluate whether a site record matches the provided nameHierarchy filter.

        Args:
            detail (dict): Site payload from API response.
            name_hierarchy_filter (str): nameHierarchy filter expression.

        Returns:
            bool: True when the record hierarchy satisfies the filter.
        """
        detail_name_hierarchy = self.get_name_hierarchy(detail)
        return self.hierarchy_matches_name_filter(
            detail_name_hierarchy, name_hierarchy_filter
        )

    def matches_parent_name_hierarchy_scope(self, detail, parent_name_hierarchy):
        """
        Match a site record against parentNameHierarchy in hierarchical scope mode.

        Matching is evaluated against both `parentNameHierarchy` and
        `nameHierarchy` so the filtered node itself and all descendants are
        included when applicable.

        Args:
            detail (dict): Site record to evaluate.
            parent_name_hierarchy (str): Scope value from filter criteria.

        Returns:
            bool: True when record is within requested hierarchy scope.
        """
        # Evaluate both parent and full hierarchy fields so parent nodes and
        # descendants are both included for scope-based filtering.
        detail_parent_hierarchy = self.get_parent_name_hierarchy(detail)
        detail_name_hierarchy = self.get_name_hierarchy(detail)

        return self.hierarchy_matches_scope(
            detail_parent_hierarchy, parent_name_hierarchy
        ) or self.hierarchy_matches_scope(detail_name_hierarchy, parent_name_hierarchy)

    def dedupe_site_details(self, details, component_name):
        """
        Remove duplicate site records while preserving first-seen ordering.

        Deduplication key is `(name, parent_name)` where parent is resolved using
        explicit parent fields first and derivation fallback second. Non-dict
        items are passed through unchanged to avoid data loss.

        Args:
            details (list): Candidate records for deduplication.
            component_name (str): Component label included in telemetry/logging.

        Returns:
            list: Deduplicated list preserving input order.
        """
        dedupe_start_time = time.time()
        incoming_records = self.get_record_count(details)
        # Preserve empty/None inputs exactly; dedupe is only meaningful for
        # non-empty iterables.
        if not details:
            dedupe_end_time = time.time()
            self.log(
                "Dedupe summary for {0}: start_time={1:.6f}, end_time={2:.6f}, "
                "duration_seconds={3:.6f}, incoming_records={4}, processed_records=0, "
                "duplicates_skipped=0, non_dict_passthrough=0, "
                "incomplete_key_passthrough=0, output_records=0.".format(
                    component_name,
                    dedupe_start_time,
                    dedupe_end_time,
                    dedupe_end_time - dedupe_start_time,
                    incoming_records,
                ),
                "INFO",
            )
            return details

        # Track seen `(name, parent)` combinations while preserving first-seen
        # ordering for deterministic output generation.
        seen = set()
        deduped = []
        processed_records = 0
        duplicates_skipped = 0
        non_dict_passthrough = 0
        incomplete_key_passthrough = 0
        for detail in details:
            processed_records += 1
            # Pass through non-dict records unchanged because they do not expose
            # stable dedupe keys.
            if not isinstance(detail, dict):
                non_dict_passthrough += 1
                deduped.append(detail)
                continue

            # Resolve dedupe key components from explicit fields first, then
            # fallback helper for derived parent resolution.
            name = detail.get("name")
            parent = detail.get("parentName")
            if not parent:
                parent = self.get_parent_name(detail)
            parent_value = str(parent) if parent is not None else None

            # Keep records that do not provide a complete dedupe key so no
            # potentially relevant payload is dropped.
            if not name or parent_value is None:
                incomplete_key_passthrough += 1
                deduped.append(detail)
                continue

            key = (name, parent_value)
            # Skip duplicates once key is already seen.
            if key in seen:
                duplicates_skipped += 1
                continue

            seen.add(key)
            deduped.append(detail)
        dedupe_end_time = time.time()
        self.log(
            "Dedupe summary for {0}: start_time={1:.6f}, end_time={2:.6f}, "
            "duration_seconds={3:.6f}, incoming_records={4}, processed_records={5}, "
            "duplicates_skipped={6}, non_dict_passthrough={7}, "
            "incomplete_key_passthrough={8}, output_records={9}.".format(
                component_name,
                dedupe_start_time,
                dedupe_end_time,
                dedupe_end_time - dedupe_start_time,
                incoming_records,
                processed_records,
                duplicates_skipped,
                non_dict_passthrough,
                incomplete_key_passthrough,
                self.get_record_count(deduped),
            ),
            "INFO",
        )
        return deduped

    def validate_component_specific_filters_structure(self, config):
        """
        Validate component-specific filters using the new site-only input shape.

        Supported structure:
        component_specific_filters:
          components_list: ["site"]
          site:
            - site_name_hierarchy: <str>            # optional
              parent_name_hierarchy: <str>          # optional
              site_type: ["area"|"building"|"floor"]  # optional

        Args:
            config (dict): One validated config entry from playbook input.

        Returns:
            list: Validation error messages. Empty list means valid.
        """
        errors = []
        component_specific_filters = config.get("component_specific_filters")
        if not component_specific_filters:
            return errors

        if not isinstance(component_specific_filters, dict):
            return ["'component_specific_filters' must be a dictionary when provided."]

        allowed_top_level_keys = {"components_list", "site"}
        unknown_top_level_keys = sorted(
            set(component_specific_filters.keys()) - allowed_top_level_keys
        )
        if unknown_top_level_keys:
            errors.append(
                "Invalid keys in 'component_specific_filters': {0}. Allowed keys are {1}.".format(
                    unknown_top_level_keys, sorted(allowed_top_level_keys)
                )
            )

        components_list = component_specific_filters.get("components_list")
        if components_list is not None:
            if not isinstance(components_list, list):
                errors.append("'components_list' must be a list when provided.")
            else:
                invalid_components = [
                    component for component in components_list if component != "site"
                ]
                if invalid_components:
                    errors.append(
                        "Invalid values in 'components_list': {0}. Only ['site'] is supported.".format(
                            invalid_components
                        )
                    )

        site_filters = component_specific_filters.get("site")
        if site_filters is None:
            return errors

        if not isinstance(site_filters, list):
            errors.append("'component_specific_filters.site' must be a list.")
            return errors

        allowed_filter_keys = {
            "site_name_hierarchy",
            "parent_name_hierarchy",
            "site_type",
        }
        valid_site_types = set(self.get_supported_components())
        for index, filter_entry in enumerate(site_filters, start=1):
            if not isinstance(filter_entry, dict):
                errors.append(
                    "Each item in 'component_specific_filters.site' must be a dict. Invalid entry at index {0}.".format(
                        index
                    )
                )
                continue

            unknown_filter_keys = sorted(set(filter_entry.keys()) - allowed_filter_keys)
            if unknown_filter_keys:
                errors.append(
                    "Invalid keys in 'component_specific_filters.site[{0}]': {1}. Allowed keys are {2}.".format(
                        index, unknown_filter_keys, sorted(allowed_filter_keys)
                    )
                )

            site_name_hierarchy = filter_entry.get("site_name_hierarchy")
            if site_name_hierarchy is not None and not isinstance(
                site_name_hierarchy, str
            ):
                errors.append(
                    "'site_name_hierarchy' in 'component_specific_filters.site[{0}]' must be a string.".format(
                        index
                    )
                )

            parent_name_hierarchy = filter_entry.get("parent_name_hierarchy")
            if parent_name_hierarchy is not None and not isinstance(
                parent_name_hierarchy, str
            ):
                errors.append(
                    "'parent_name_hierarchy' in 'component_specific_filters.site[{0}]' must be a string.".format(
                        index
                    )
                )

            site_type = filter_entry.get("site_type")
            if site_type is not None:
                if not isinstance(site_type, list):
                    errors.append(
                        "'site_type' in 'component_specific_filters.site[{0}]' must be a list.".format(
                            index
                        )
                    )
                else:
                    invalid_site_types = [
                        site_type_value
                        for site_type_value in site_type
                        if not isinstance(site_type_value, str)
                        or site_type_value not in valid_site_types
                    ]
                    if invalid_site_types:
                        errors.append(
                            "Invalid 'site_type' values in 'component_specific_filters.site[{0}]': {1}. "
                            "Supported values are {2}.".format(
                                index,
                                invalid_site_types,
                                sorted(valid_site_types),
                            )
                        )
                    duplicate_site_types = []
                    seen_site_types = set()
                    for site_type_value in site_type:
                        if not isinstance(site_type_value, str):
                            continue
                        if site_type_value in seen_site_types:
                            if site_type_value not in duplicate_site_types:
                                duplicate_site_types.append(site_type_value)
                            continue
                        seen_site_types.add(site_type_value)
                    if duplicate_site_types:
                        self.log(
                            "Duplicate 'site_type' values found in "
                            "'component_specific_filters.site[{0}]': {1}. "
                            "Duplicates will be deduplicated before API query execution.".format(
                                index, duplicate_site_types
                            ),
                            "INFO",
                        )

        return errors

    def area_temp_spec(self):
        """
        Build reverse-mapping specification for `area` component serialization.

        The resulting `OrderedDict` describes how raw Catalyst Center site fields
        are transformed into the YAML payload structure expected by
        `site_workflow_manager`. Field transforms are declared declaratively so
        downstream mapping stays consistent and testable.

        Args:
            self: Instance context used to bind transform callables.

        Returns:
            OrderedDict: Deterministic schema map for area records.
        """

        self.log("Building temporary mapping specification for area records.", "INFO")
        self.log("Generating temporary specification for areas.", "INFO")
        area = OrderedDict(
            {
                "site": {
                    "type": "dict",
                    "options": OrderedDict(
                        {
                            "area": {
                                "type": "dict",
                                "options": OrderedDict(
                                    {
                                        "name": {"type": "str", "source_key": "name"},
                                        "parent_name": {
                                            "type": "str",
                                            "special_handling": True,
                                            "transform": self.get_parent_name,
                                        },
                                    }
                                ),
                            }
                        }
                    ),
                },
                "site_type": {
                    "type": "str",
                    "special_handling": True,
                    "transform": self.get_site_type_area,
                },
            }
        )
        self.log("Area temporary mapping specification built successfully.", "INFO")
        return area

    def building_temp_spec(self):
        """
        Build reverse-mapping specification for `building` component serialization.

        The schema maps location and geo attributes (address, latitude, longitude,
        country) and ensures output formatting wrappers are applied consistently
        for quoted YAML fields.

        Args:
            self: Instance context used to bind field transform callables.

        Returns:
            OrderedDict: Deterministic schema map for building records.
        """

        self.log(
            "Building temporary mapping specification for building records.", "INFO"
        )
        self.log("Generating temporary specification for buildings.", "INFO")
        building = OrderedDict(
            {
                "site": {
                    "type": "dict",
                    "options": OrderedDict(
                        {
                            "building": {
                                "type": "dict",
                                "options": OrderedDict(
                                    {
                                        "name": {"type": "str", "source_key": "name"},
                                        "parent_name": {
                                            "type": "str",
                                            "special_handling": True,
                                            "transform": self.get_parent_name,
                                        },
                                        "address": {
                                            "type": "str",
                                            "source_key": "address",
                                        },
                                        "latitude": {
                                            "type": "float",
                                            "source_key": "latitude",
                                        },
                                        "longitude": {
                                            "type": "float",
                                            "source_key": "longitude",
                                        },
                                        "country": {
                                            "type": "str",
                                            "source_key": "country",
                                            "transform": DoubleQuotedStr,
                                        },
                                    }
                                ),
                            }
                        }
                    ),
                },
                "site_type": {
                    "type": "str",
                    "special_handling": True,
                    "transform": self.get_site_type_building,
                },
            }
        )
        self.log("Building temporary mapping specification built successfully.", "INFO")
        return building

    def floor_temp_spec(self):
        """
        Build reverse-mapping specification for `floor` component serialization.

        This schema captures floor-level metadata such as RF model, dimensions,
        floor number, and unit information so generated YAML is directly consumable
        by the downstream workflow manager module.

        Args:
            self: Instance context used to bind transform callables.

        Returns:
            OrderedDict: Deterministic schema map for floor records.
        """

        self.log("Building temporary mapping specification for floor records.", "INFO")
        self.log("Generating temporary specification for floors.", "INFO")
        floor = OrderedDict(
            {
                "site": {
                    "type": "dict",
                    "options": OrderedDict(
                        {
                            "floor": {
                                "type": "dict",
                                "options": OrderedDict(
                                    {
                                        "name": {
                                            "type": "str",
                                            "source_key": "name",
                                        },
                                        "parent_name": {
                                            "type": "str",
                                            "special_handling": True,
                                            "transform": self.get_parent_name,
                                        },
                                        "rf_model": {
                                            "type": "str",
                                            "source_key": "rfModel",
                                            "transform": SingleQuotedStr,
                                        },
                                        "length": {
                                            "type": "float",
                                            "source_key": "length",
                                        },
                                        "width": {
                                            "type": "float",
                                            "source_key": "width",
                                        },
                                        "height": {
                                            "type": "float",
                                            "source_key": "height",
                                        },
                                        "floor_number": {
                                            "type": "int",
                                            "source_key": "floorNumber",
                                        },
                                        "units_of_measure": {
                                            "type": "str",
                                            "source_key": "unitsOfMeasure",
                                            "transform": DoubleQuotedStr,
                                        },
                                    }
                                ),
                            }
                        }
                    ),
                },
                "site_type": {
                    "type": "str",
                    "special_handling": True,
                    "transform": self.get_site_type_floor,
                },
            }
        )
        self.log("Floor temporary mapping specification built successfully.", "INFO")
        return floor

    def get_record_count(self, records):
        """
        Return a stable count for list-like API response payloads.

        Args:
            records (Any): Candidate response payload.

        Returns:
            int: Number of records represented by the payload.
        """
        if isinstance(records, list):
            return len(records)
        if records is None:
            return 0
        return 1

    def get_supported_components(self):
        """
        Return canonical site type values used in payload partitioning.

        Returns:
            tuple: Supported site type values.
        """
        return ("area", "building", "floor")

    def should_use_unified_site_fetch(self):
        """
        Determine whether unified one-pass fetch/filter mode should be used.

        Returns:
            bool: True when direct-filter mode targets more than one component.
        """
        if not self.unified_filter_mode_enabled:
            return False
        component_specific_filters = self._normalized_component_specific_filters or {}
        active_components = [
            component
            for component in self.get_supported_components()
            if component in component_specific_filters
            and component_specific_filters.get(component) is not None
        ]
        return len(active_components) > 1

    def get_unified_filter_expressions(self):
        """
        Collect de-duplicated filter expressions across active components.

        Returns:
            list: Union of component filter expressions.
        """
        component_specific_filters = self._normalized_component_specific_filters or {}
        filter_expressions = []
        for component in self.get_supported_components():
            component_filters = component_specific_filters.get(component)
            if isinstance(component_filters, list):
                filter_expressions.extend(component_filters)
        return self.dedupe_filter_expressions(
            filter_expressions, "unified_filter_expressions"
        )

    def site_record_matches_filter_expression(self, detail, filter_expression):
        """
        Evaluate whether a site record matches one filter expression.

        Args:
            detail (dict): Site record from API response.
            filter_expression (dict): One filter expression.

        Returns:
            bool: True when record satisfies the expression.
        """
        if not isinstance(filter_expression, dict):
            return False

        site_type_filters = filter_expression.get("site_type")
        if site_type_filters:
            detail_type = self.get_site_type_value(detail)
            if not isinstance(site_type_filters, list):
                return False
            if detail_type not in site_type_filters:
                return False

        expression_name_hierarchy = filter_expression.get("site_name_hierarchy")
        if expression_name_hierarchy:
            if not self.matches_name_hierarchy_filter(
                detail, expression_name_hierarchy
            ):
                return False

        # When site_name_hierarchy is provided, it is treated as the primary
        # hierarchy selector and parent filter is not additionally applied.
        if expression_name_hierarchy:
            return True

        expression_parent_hierarchy = filter_expression.get("parent_name_hierarchy")
        if expression_parent_hierarchy:
            if not self.matches_parent_name_hierarchy_scope(
                detail, expression_parent_hierarchy
            ):
                return False

        return True

    def get_unified_filtered_site_records(self, api_family, api_function):
        """
        Fetch all candidate sites once, then apply direct filters once globally.

        Args:
            api_family (str): SDK API family name.
            api_function (str): SDK function name.

        Returns:
            tuple: `(records_by_type, summary)` where:
                - `records_by_type` contains `area/building/floor` lists
                - `summary` contains fetch/filter counters
        """
        filter_expressions = self.get_unified_filter_expressions()
        cache_key = self.build_filter_signature(
            {"mode": "unified", "filters": filter_expressions}
        )

        if (
            self._unified_site_records_cache is not None
            and self._unified_site_records_cache_key == cache_key
        ):
            summary = {
                "cache_hit": 1,
                "api_calls": 0,
                "records_collected_before_filter": self.get_record_count(
                    self._unified_site_records_cache.get("all_records")
                ),
                "records_after_filter": self.get_record_count(
                    self._unified_site_records_cache.get("filtered_records")
                ),
                "records_filtered_out": self._unified_site_records_cache.get(
                    "records_filtered_out", 0
                ),
                "filter_expressions_processed": self.get_record_count(
                    filter_expressions
                ),
            }
            return self._unified_site_records_cache.get("by_type", {}), summary

        all_records = self.execute_sites_api_with_timing(
            api_family,
            api_function,
            {},
            "sites_unified",
            "unified_direct_filter_mode",
        )
        records_collected_before_filter = self.get_record_count(all_records)

        if not filter_expressions:
            filtered_records = (
                list(all_records) if isinstance(all_records, list) else []
            )
        else:
            filtered_records = []
            for detail in all_records:
                for filter_expression in filter_expressions:
                    if self.site_record_matches_filter_expression(
                        detail, filter_expression
                    ):
                        filtered_records.append(detail)
                        break

        records_after_filter = self.get_record_count(filtered_records)
        records_filtered_out = max(
            0, records_collected_before_filter - records_after_filter
        )

        by_type = {component: [] for component in self.get_supported_components()}
        unknown_type_records = 0
        for detail in filtered_records:
            detail_type = self.get_site_type_value(detail)
            if detail_type in by_type:
                by_type[detail_type].append(detail)
            else:
                unknown_type_records += 1

        self._unified_site_records_cache = {
            "all_records": all_records,
            "filtered_records": filtered_records,
            "by_type": by_type,
            "records_filtered_out": records_filtered_out,
            "unknown_type_records": unknown_type_records,
        }
        self._unified_site_records_cache_key = cache_key

        summary = {
            "cache_hit": 0,
            "api_calls": 1,
            "records_collected_before_filter": records_collected_before_filter,
            "records_after_filter": records_after_filter,
            "records_filtered_out": records_filtered_out,
            "filter_expressions_processed": self.get_record_count(filter_expressions),
            "unknown_type_records": unknown_type_records,
        }
        self.log(
            "Unified site fetch summary: api_calls={0}, cache_hit={1}, "
            "records_collected_before_filter={2}, records_after_filter={3}, "
            "records_filtered_out={4}, filter_expressions_processed={5}, "
            "unknown_type_records={6}.".format(
                summary["api_calls"],
                summary["cache_hit"],
                summary["records_collected_before_filter"],
                summary["records_after_filter"],
                summary["records_filtered_out"],
                summary["filter_expressions_processed"],
                summary["unknown_type_records"],
            ),
            "INFO",
        )
        self.log(
            "Unified filtered records payload (debug): {0}".format(filtered_records),
            "DEBUG",
        )
        return by_type, summary

    def execute_sites_api_with_timing(
        self, api_family, api_function, params, component_name, filter_context=None
    ):
        """
        Execute a site API call with explicit entry/exit timing telemetry.

        Args:
            api_family (str): SDK API family name.
            api_function (str): SDK function name.
            params (dict): Query parameters passed to the API.
            component_name (str): Component label (`areas`, `buildings`, `floors`).
            filter_context (dict | str | None): Filter context used for this query.

        Returns:
            list: Retrieved site records.
        """
        start_time = time.time()
        self.log(
            "API entry for {0} retrieval: invoking {1}.{2} with params={3}, "
            "filter_context={4}, start_time={5:.6f}.".format(
                component_name,
                api_family,
                api_function,
                params,
                filter_context,
                start_time,
            ),
            "INFO",
        )
        records = self.execute_get_with_pagination(api_family, api_function, params)
        end_time = time.time()
        collected_count = self.get_record_count(records)
        self.log(
            "API exit for {0} retrieval: {1}.{2} completed with params={3}, "
            "end_time={4:.6f}, duration_seconds={5:.6f}, collected_records={6}.".format(
                component_name,
                api_family,
                api_function,
                params,
                end_time,
                end_time - start_time,
                collected_count,
            ),
            "INFO",
        )
        return records

    def is_valid_parent_site_hierarchy(
        self, parent_name_hierarchy, site_name_hierarchy
    ):
        """
        Validate that parent hierarchy is a strict hierarchy prefix of site hierarchy.

        Args:
            parent_name_hierarchy (str): Parent hierarchy expression.
            site_name_hierarchy (str): Site hierarchy expression.

        Returns:
            bool: True when parent is a strict prefix of site path.
        """
        normalized_parent = self.normalize_hierarchy_path(parent_name_hierarchy)
        normalized_site = self.normalize_hierarchy_path(site_name_hierarchy)
        if not normalized_parent or not normalized_site:
            return False
        return normalized_site.startswith(normalized_parent + "/")

    def build_site_query_plan_for_filter(self, filter_expression):
        """
        Build API query params from one site filter expression.

        The filter expression is interpreted using one common rule set:
        - `site_name_hierarchy` is used directly as `nameHierarchy`.
        - `parent_name_hierarchy` becomes `nameHierarchy=<parent>/.*` when
          `site_name_hierarchy` is absent.
        - When both hierarchy keys are present, parent must be a strict prefix
          of site; then parent is ignored and site is used.
        - `site_type` expands query params to one API call per type value.

        Args:
            filter_expression (dict): One item from component_specific_filters.site.

        Returns:
            list: List of API params dictionaries for get_sites.
        """
        if not isinstance(filter_expression, dict):
            return []

        site_name_hierarchy = self.normalize_hierarchy_path(
            filter_expression.get("site_name_hierarchy")
        )
        parent_name_hierarchy = self.normalize_hierarchy_path(
            filter_expression.get("parent_name_hierarchy")
        )
        site_type_list = filter_expression.get("site_type")
        deduped_site_type_list = site_type_list

        if site_name_hierarchy and parent_name_hierarchy:
            if not self.is_valid_parent_site_hierarchy(
                parent_name_hierarchy, site_name_hierarchy
            ):
                self.log(
                    "Skipping site filter because parent_name_hierarchy '{0}' is not "
                    "a valid strict prefix of site_name_hierarchy '{1}'.".format(
                        parent_name_hierarchy, site_name_hierarchy
                    ),
                    "WARNING",
                )
                return []
            parent_name_hierarchy = None

        effective_name_hierarchy = None
        if site_name_hierarchy:
            effective_name_hierarchy = site_name_hierarchy
        elif parent_name_hierarchy:
            normalized_parent = self.normalize_hierarchy_path(parent_name_hierarchy)
            if normalized_parent:
                effective_name_hierarchy = normalized_parent + "/.*"

        if isinstance(site_type_list, list) and site_type_list:
            deduped_site_type_list = []
            duplicate_site_types = []
            seen_site_types = set()
            for site_type in site_type_list:
                if site_type in seen_site_types:
                    if site_type not in duplicate_site_types:
                        duplicate_site_types.append(site_type)
                    continue
                seen_site_types.add(site_type)
                deduped_site_type_list.append(site_type)
            if duplicate_site_types:
                self.log(
                    "Duplicate 'site_type' values detected in one site filter "
                    "expression: {0}. Duplicates are ignored for API query planning.".format(
                        duplicate_site_types
                    ),
                    "INFO",
                )

        query_plan = []
        type_values = (
            deduped_site_type_list
            if isinstance(deduped_site_type_list, list) and deduped_site_type_list
            else [None]
        )
        for site_type in type_values:
            params = {}
            if effective_name_hierarchy:
                params["nameHierarchy"] = effective_name_hierarchy
            if site_type:
                params["type"] = site_type
            query_plan.append(params)
        return query_plan

    def get_sites_configuration(self, network_element, component_specific_filters=None):
        """
        Retrieve site hierarchy records using one common filter-to-query pipeline.

        The method builds API query params from every filter expression, deduplicates
        query params, retrieves matching site records, deduplicates records, and
        finally maps them to area/building/floor output payloads.

        Args:
            network_element (dict): API metadata containing family and function names.
            component_specific_filters (list | dict | None): Optional site filter set.

        Returns:
            list: Combined mapped configuration entries for area, building, and floor.
        """
        self.log(
            "Starting site retrieval workflow with unified query planning.", "INFO"
        )
        self.log(
            "Starting site retrieval with common query planning and network element: {0} and "
            "component-specific filters: {1}".format(
                network_element, component_specific_filters
            ),
            "INFO",
        )

        component_specific_filters = self.resolve_component_filters(
            component_specific_filters
        )

        site_counters = {
            "filters_received": (
                len(component_specific_filters) if component_specific_filters else 0
            ),
            "filters_processed": 0,
            "filters_skipped": 0,
            "api_calls": 0,
            "records_collected_before_filter": 0,
            "records_filtered_out": 0,
            "records_after_filter": 0,
            "unknown_type_records": 0,
            "records_ignored_as_duplicates": 0,
            "area_records_transformed": 0,
            "building_records_transformed": 0,
            "floor_records_transformed": 0,
            "output_records_total": 0,
        }

        api_family = network_element.get("api_family")
        api_function = network_element.get("api_function")
        self.log(
            "Getting sites using family '{0}' and function '{1}'.".format(
                api_family, api_function
            ),
            "INFO",
        )

        site_query_plan = []
        if component_specific_filters:
            site_counters["filters_processed"] = self.get_record_count(
                component_specific_filters
            )
            for filter_expression in component_specific_filters:
                filter_query_plan = self.build_site_query_plan_for_filter(
                    filter_expression
                )
                if not filter_query_plan:
                    site_counters["filters_skipped"] += 1
                    continue
                site_query_plan.extend(filter_query_plan)
        else:
            site_query_plan = [{}]
            site_counters["filters_skipped"] += 1

        site_query_plan = self.dedupe_filter_expressions(
            site_query_plan, "site_query_plan"
        )
        self.log(
            "Prepared site query plan with {0} API call candidate(s): {1}.".format(
                self.get_record_count(site_query_plan), site_query_plan
            ),
            "INFO",
        )

        all_site_details = []
        for query_params in site_query_plan:
            site_counters["api_calls"] += 1
            site_records = self.execute_sites_api_with_timing(
                api_family,
                api_function,
                query_params,
                "sites",
                query_params,
            )
            site_counters["records_collected_before_filter"] += self.get_record_count(
                site_records
            )
            if isinstance(site_records, list):
                all_site_details.extend(site_records)
            elif site_records:
                all_site_details.append(site_records)

        records_before_global_dedupe = self.get_record_count(all_site_details)
        filtered_site_details = self.dedupe_site_details(all_site_details, "sites")
        records_after_global_dedupe = self.get_record_count(filtered_site_details)
        site_counters["records_after_filter"] = records_after_global_dedupe
        site_counters["records_filtered_out"] = max(
            0, records_before_global_dedupe - records_after_global_dedupe
        )
        site_counters["records_ignored_as_duplicates"] += max(
            0, records_before_global_dedupe - records_after_global_dedupe
        )

        records_by_type = {
            component: [] for component in self.get_supported_components()
        }
        for detail in filtered_site_details:
            detail_type = self.get_site_type_value(detail)
            if detail_type in records_by_type:
                records_by_type[detail_type].append(detail)
            else:
                site_counters["unknown_type_records"] += 1

        mapped_configurations = []
        for component in self.get_supported_components():
            records_before_dedupe = self.get_record_count(records_by_type[component])
            deduped_records = self.dedupe_site_details(
                records_by_type[component], "{0}s".format(component)
            )
            records_after_dedupe = self.get_record_count(deduped_records)
            site_counters["records_ignored_as_duplicates"] += max(
                0, records_before_dedupe - records_after_dedupe
            )

            if component == "area":
                mapped_records = self.modify_parameters(
                    self.area_temp_spec(), deduped_records
                )
                site_counters["area_records_transformed"] = self.get_record_count(
                    mapped_records
                )
            elif component == "building":
                mapped_records = self.modify_parameters(
                    self.building_temp_spec(), deduped_records
                )
                site_counters["building_records_transformed"] = self.get_record_count(
                    mapped_records
                )
            else:
                mapped_records = self.modify_parameters(
                    self.floor_temp_spec(), deduped_records
                )
                site_counters["floor_records_transformed"] = self.get_record_count(
                    mapped_records
                )

            mapped_configurations.extend(mapped_records)

        site_counters["output_records_total"] = self.get_record_count(
            mapped_configurations
        )
        self.log(
            "Site processing counters: filters_received={0}, "
            "filters_processed={1}, filters_skipped={2}, api_calls={3}, "
            "records_collected_before_filter={4}, records_filtered_out={5}, "
            "records_after_filter={6}, unknown_type_records={7}, "
            "records_ignored_as_duplicates={8}, area_records_transformed={9}, "
            "building_records_transformed={10}, floor_records_transformed={11}, "
            "output_records_total={12}.".format(
                site_counters["filters_received"],
                site_counters["filters_processed"],
                site_counters["filters_skipped"],
                site_counters["api_calls"],
                site_counters["records_collected_before_filter"],
                site_counters["records_filtered_out"],
                site_counters["records_after_filter"],
                site_counters["unknown_type_records"],
                site_counters["records_ignored_as_duplicates"],
                site_counters["area_records_transformed"],
                site_counters["building_records_transformed"],
                site_counters["floor_records_transformed"],
                site_counters["output_records_total"],
            ),
            "INFO",
        )
        self.log(
            "Mapped site payload (debug): {0}".format(mapped_configurations),
            "DEBUG",
        )

        self.log(
            "Site retrieval workflow completed and mapped payload assembled.", "INFO"
        )
        return mapped_configurations

    def get_areas_configuration(self, network_element, component_specific_filters=None):
        """
        Retrieve and transform area records for YAML output.

        The method applies query construction, optional post-filter evaluation,
        deduplication, and schema-based parameter mapping in sequence.

        Args:
            network_element (dict): API metadata containing family and function names.
            component_specific_filters (list | None): Optional list of filter
                expressions targeted at area retrieval.

        Returns:
            list: Mapped area configuration objects ready for YAML serialization.
        """

        self.log("Starting area retrieval workflow.", "INFO")
        self.log(
            f"Starting to retrieve areas with network element: {network_element} and component-specific filters: {component_specific_filters}",
            "INFO",
        )

        # Normalize filters payload so this retrieval function can be called both
        # from module-local flow and shared helper flow.
        component_specific_filters = self.resolve_component_filters(
            component_specific_filters
        )

        # Collect all retrieved area records across filter iterations before
        # dedupe and schema mapping.
        final_areas = []
        area_counters = {
            "filters_received": (
                len(component_specific_filters) if component_specific_filters else 0
            ),
            "filters_processed": 0,
            "filters_skipped": 0,
            "api_calls": 0,
            "query_plan_buckets": 0,
            "query_plan_entries_collapsed": 0,
            "adaptive_one_fetch_mode": 0,
            "records_collected_before_post_filter": 0,
            "records_filtered_out_post_filter": 0,
            "records_collected_after_post_filter": 0,
            "records_ignored_as_duplicates": 0,
        }
        # Resolve SDK family/function metadata for API invocation.
        api_family = network_element.get("api_family")
        api_function = network_element.get("api_function")

        self.log(
            f"Getting areas using family '{api_family}' and function '{api_function}'.",
            "INFO",
        )

        if (
            self.should_use_unified_site_fetch()
            and component_specific_filters is not None
        ):
            self.log(
                "Unified one-pass direct-filter retrieval mode is enabled for areas.",
                "INFO",
            )
            unified_records_by_type, unified_summary = (
                self.get_unified_filtered_site_records(api_family, api_function)
            )
            area_details = unified_records_by_type.get("area") or []
            collected_area_count = self.get_record_count(area_details)
            area_counters["filters_processed"] = unified_summary.get(
                "filter_expressions_processed", 0
            )
            area_counters["api_calls"] += unified_summary.get("api_calls", 0)
            area_counters["query_plan_buckets"] = 1
            area_counters["adaptive_one_fetch_mode"] = 1
            area_counters[
                "records_collected_before_post_filter"
            ] += collected_area_count
            area_counters["records_collected_after_post_filter"] += collected_area_count
            final_areas.extend(area_details)
            self.log(
                "Unified fetch consumption summary for areas: cache_hit={0}, "
                "api_calls={1}, records_collected_before_global_filter={2}, "
                "records_after_global_filter={3}, component_records={4}.".format(
                    unified_summary.get("cache_hit", 0),
                    unified_summary.get("api_calls", 0),
                    unified_summary.get("records_collected_before_filter", 0),
                    unified_summary.get("records_after_filter", 0),
                    collected_area_count,
                ),
                "INFO",
            )
        elif component_specific_filters is None:
            self.log(
                "Area component retrieval is skipped due to "
                "type-aware filter pruning.",
                "INFO",
            )
            area_counters["filters_skipped"] += 1
        elif component_specific_filters:
            self.log(
                "Component-specific filters were provided for area retrieval.", "INFO"
            )
            # Build a query plan keyed by API params so identical queries are
            # executed once and post-filters are applied from the shared payload.
            query_plan = OrderedDict()
            for filter_param in component_specific_filters:
                area_counters["filters_processed"] += 1
                self.log(
                    "Processing area filter expression at query-planning stage: "
                    "{0}".format(filter_param),
                    "DEBUG",
                )
                params, post_filters = self.build_site_query_context(
                    filter_param, "area"
                )
                if not params:
                    area_counters["filters_skipped"] += 1
                    self.log(
                        "Skipping area filter due to invalid parameters.", "WARNING"
                    )
                    continue

                query_cache_key = tuple(sorted(params.items()))
                if query_cache_key not in query_plan:
                    query_plan[query_cache_key] = {
                        "params": params,
                        "entries": OrderedDict(),
                    }

                post_filter_signature = self.build_filter_signature(post_filters)
                if post_filter_signature in query_plan[query_cache_key]["entries"]:
                    area_counters["query_plan_entries_collapsed"] += 1
                    continue

                query_plan[query_cache_key]["entries"][post_filter_signature] = {
                    "post_filters": post_filters,
                    "source_filter": filter_param,
                }

            area_counters["query_plan_buckets"] = len(query_plan)
            if len(query_plan) == 1 and area_counters["filters_processed"] > 1:
                only_bucket = next(iter(query_plan.values()))
                only_params = only_bucket.get("params") or {}
                if set(only_params.keys()) == {"type"}:
                    area_counters["adaptive_one_fetch_mode"] = 1
                    self.log(
                        "Adaptive one-fetch mode enabled for areas: "
                        "single type-only query bucket with multiple "
                        "post-filter expressions.",
                        "INFO",
                    )

            for bucket in query_plan.values():
                area_counters["api_calls"] += 1
                area_details = self.execute_sites_api_with_timing(
                    api_family,
                    api_function,
                    bucket.get("params"),
                    "areas",
                    "bucketed_filters",
                )
                collected_before_post_filter = self.get_record_count(area_details)
                area_counters[
                    "records_collected_before_post_filter"
                ] += collected_before_post_filter
                self.log(
                    "Retrieved area details summary: query_params={0}, "
                    "collected_records={1}.".format(
                        bucket.get("params"),
                        collected_before_post_filter,
                    ),
                    "INFO",
                )
                self.log(
                    "Area detail payload (debug): {0}".format(area_details), "DEBUG"
                )

                for entry in bucket.get("entries", {}).values():
                    post_filters = entry.get("post_filters") or {}
                    if post_filters:
                        self.log(
                            "Applying post filters to area details: {0}".format(
                                post_filters
                            ),
                            "INFO",
                        )
                        pre_post_filter_count = self.get_record_count(area_details)
                        filtered_area_details = self.apply_site_post_filters(
                            area_details, post_filters
                        )
                        post_post_filter_count = self.get_record_count(
                            filtered_area_details
                        )
                        area_counters["records_filtered_out_post_filter"] += max(
                            0, pre_post_filter_count - post_post_filter_count
                        )
                    else:
                        filtered_area_details = area_details
                        post_post_filter_count = collected_before_post_filter

                    area_counters[
                        "records_collected_after_post_filter"
                    ] += post_post_filter_count
                    final_areas.extend(filtered_area_details)
        else:
            self.log(
                "No component-specific filters provided for areas; using default type filter.",
                "INFO",
            )
            default_params = {"type": "area"}
            area_counters["query_plan_buckets"] = 1
            area_counters["api_calls"] += 1
            area_details = self.execute_sites_api_with_timing(
                api_family,
                api_function,
                default_params,
                "areas",
                "default_type_filter",
            )
            collected_default_count = self.get_record_count(area_details)
            area_counters[
                "records_collected_before_post_filter"
            ] += collected_default_count
            area_counters[
                "records_collected_after_post_filter"
            ] += collected_default_count
            self.log(
                "Retrieved area details summary: query_params={0}, "
                "collected_records={1}.".format(
                    default_params,
                    collected_default_count,
                ),
                "INFO",
            )
            self.log("Area detail payload (debug): {0}".format(area_details), "DEBUG")
            final_areas.extend(area_details)

        # Remove duplicates from merged result set so generated YAML remains stable.
        records_before_dedupe = self.get_record_count(final_areas)
        final_areas = self.dedupe_site_details(final_areas, "areas")
        records_after_dedupe = self.get_record_count(final_areas)
        area_counters["records_ignored_as_duplicates"] = max(
            0, records_before_dedupe - records_after_dedupe
        )

        # Convert raw API response dictionaries into module output schema.
        area_temp_spec = self.area_temp_spec()
        areas_details = self.modify_parameters(area_temp_spec, final_areas)
        transformed_records = self.get_record_count(areas_details)

        self.log(
            "Area processing counters: filters_received={0}, filters_processed={1}, "
            "filters_skipped={2}, api_calls={3}, query_plan_buckets={4}, "
            "query_plan_entries_collapsed={5}, adaptive_one_fetch_mode={6}, "
            "records_collected_before_post_filter={7}, "
            "records_filtered_out_post_filter={8}, "
            "records_collected_after_post_filter={9}, "
            "records_ignored_as_duplicates={10}, final_records_after_dedupe={11}, "
            "transformed_records={12}.".format(
                area_counters["filters_received"],
                area_counters["filters_processed"],
                area_counters["filters_skipped"],
                area_counters["api_calls"],
                area_counters["query_plan_buckets"],
                area_counters["query_plan_entries_collapsed"],
                area_counters["adaptive_one_fetch_mode"],
                area_counters["records_collected_before_post_filter"],
                area_counters["records_filtered_out_post_filter"],
                area_counters["records_collected_after_post_filter"],
                area_counters["records_ignored_as_duplicates"],
                records_after_dedupe,
                transformed_records,
            ),
            "INFO",
        )

        self.log(
            "Modified area details payload (debug): {0}".format(areas_details), "DEBUG"
        )

        self.log("Area retrieval workflow completed.", "INFO")
        return areas_details

    def get_buildings_configuration(
        self, network_element, component_specific_filters=None
    ):
        """
        Retrieve and transform building records for YAML output.

        Processing includes API pagination handling, filter evaluation,
        deduplication, and conversion through the building temp-spec mapper.

        Args:
            network_element (dict): API metadata containing family and function names.
            component_specific_filters (list | None): Optional building filter set.

        Returns:
            list: Mapped building configuration objects for YAML serialization.
        """

        self.log("Starting building retrieval workflow.", "INFO")
        self.log(
            f"Starting to retrieve buildings with network element: {network_element} and component-specific filters: {component_specific_filters}",
            "INFO",
        )

        # Normalize filters payload so this retrieval function can be called both
        # from module-local flow and shared helper flow.
        component_specific_filters = self.resolve_component_filters(
            component_specific_filters
        )

        # Collect all retrieved building records across all filter expressions.
        final_buildings = []
        building_counters = {
            "filters_received": (
                len(component_specific_filters) if component_specific_filters else 0
            ),
            "filters_processed": 0,
            "filters_skipped": 0,
            "api_calls": 0,
            "query_plan_buckets": 0,
            "query_plan_entries_collapsed": 0,
            "adaptive_one_fetch_mode": 0,
            "records_collected_before_post_filter": 0,
            "records_filtered_out_post_filter": 0,
            "records_collected_after_post_filter": 0,
            "records_ignored_as_duplicates": 0,
        }
        # Resolve SDK family/function metadata used by pagination helper.
        api_family = network_element.get("api_family")
        api_function = network_element.get("api_function")

        self.log(
            f"Getting buildings using family '{api_family}' and function '{api_function}'.",
            "INFO",
        )

        if (
            self.should_use_unified_site_fetch()
            and component_specific_filters is not None
        ):
            self.log(
                "Unified one-pass direct-filter retrieval mode is enabled for buildings.",
                "INFO",
            )
            unified_records_by_type, unified_summary = (
                self.get_unified_filtered_site_records(api_family, api_function)
            )
            building_details = unified_records_by_type.get("building") or []
            collected_building_count = self.get_record_count(building_details)
            building_counters["filters_processed"] = unified_summary.get(
                "filter_expressions_processed", 0
            )
            building_counters["api_calls"] += unified_summary.get("api_calls", 0)
            building_counters["query_plan_buckets"] = 1
            building_counters["adaptive_one_fetch_mode"] = 1
            building_counters[
                "records_collected_before_post_filter"
            ] += collected_building_count
            building_counters[
                "records_collected_after_post_filter"
            ] += collected_building_count
            final_buildings.extend(building_details)
            self.log(
                "Unified fetch consumption summary for buildings: cache_hit={0}, "
                "api_calls={1}, records_collected_before_global_filter={2}, "
                "records_after_global_filter={3}, component_records={4}.".format(
                    unified_summary.get("cache_hit", 0),
                    unified_summary.get("api_calls", 0),
                    unified_summary.get("records_collected_before_filter", 0),
                    unified_summary.get("records_after_filter", 0),
                    collected_building_count,
                ),
                "INFO",
            )
        elif component_specific_filters is None:
            self.log(
                "Building component retrieval is skipped due to "
                "type-aware filter pruning.",
                "INFO",
            )
            building_counters["filters_skipped"] += 1
        elif component_specific_filters:
            self.log(
                "Component-specific filters were provided for building retrieval.",
                "INFO",
            )
            # Build a query plan keyed by API params so identical queries are
            # executed once and post-filters are applied from the shared payload.
            query_plan = OrderedDict()
            for filter_param in component_specific_filters:
                building_counters["filters_processed"] += 1
                self.log(
                    "Processing building filter expression at query-planning "
                    "stage: {0}".format(filter_param),
                    "DEBUG",
                )
                params, post_filters = self.build_site_query_context(
                    filter_param, "building"
                )
                if not params:
                    building_counters["filters_skipped"] += 1
                    self.log(
                        "Skipping building filter due to invalid parameters.",
                        "WARNING",
                    )
                    continue

                query_cache_key = tuple(sorted(params.items()))
                if query_cache_key not in query_plan:
                    query_plan[query_cache_key] = {
                        "params": params,
                        "entries": OrderedDict(),
                    }

                post_filter_signature = self.build_filter_signature(post_filters)
                if post_filter_signature in query_plan[query_cache_key]["entries"]:
                    building_counters["query_plan_entries_collapsed"] += 1
                    continue

                query_plan[query_cache_key]["entries"][post_filter_signature] = {
                    "post_filters": post_filters,
                    "source_filter": filter_param,
                }

            building_counters["query_plan_buckets"] = len(query_plan)
            if len(query_plan) == 1 and building_counters["filters_processed"] > 1:
                only_bucket = next(iter(query_plan.values()))
                only_params = only_bucket.get("params") or {}
                if set(only_params.keys()) == {"type"}:
                    building_counters["adaptive_one_fetch_mode"] = 1
                    self.log(
                        "Adaptive one-fetch mode enabled for buildings: "
                        "single type-only query bucket with multiple "
                        "post-filter expressions.",
                        "INFO",
                    )

            for bucket in query_plan.values():
                building_counters["api_calls"] += 1
                building_details = self.execute_sites_api_with_timing(
                    api_family,
                    api_function,
                    bucket.get("params"),
                    "buildings",
                    "bucketed_filters",
                )
                collected_before_post_filter = self.get_record_count(building_details)
                building_counters[
                    "records_collected_before_post_filter"
                ] += collected_before_post_filter
                self.log(
                    "Retrieved building details summary: query_params={0}, "
                    "collected_records={1}.".format(
                        bucket.get("params"),
                        collected_before_post_filter,
                    ),
                    "INFO",
                )
                self.log(
                    "Building detail payload (debug): {0}".format(building_details),
                    "DEBUG",
                )

                for entry in bucket.get("entries", {}).values():
                    post_filters = entry.get("post_filters") or {}
                    if post_filters:
                        self.log(
                            "Applying post filters to building details: {0}".format(
                                post_filters
                            ),
                            "INFO",
                        )
                        pre_post_filter_count = self.get_record_count(building_details)
                        filtered_building_details = self.apply_site_post_filters(
                            building_details, post_filters
                        )
                        post_post_filter_count = self.get_record_count(
                            filtered_building_details
                        )
                        building_counters["records_filtered_out_post_filter"] += max(
                            0, pre_post_filter_count - post_post_filter_count
                        )
                    else:
                        filtered_building_details = building_details
                        post_post_filter_count = collected_before_post_filter

                    building_counters[
                        "records_collected_after_post_filter"
                    ] += post_post_filter_count
                    final_buildings.extend(filtered_building_details)
        else:
            self.log(
                "No component-specific filters provided for buildings; using default type filter.",
                "INFO",
            )
            default_params = {"type": "building"}
            building_counters["query_plan_buckets"] = 1
            building_counters["api_calls"] += 1
            building_details = self.execute_sites_api_with_timing(
                api_family,
                api_function,
                default_params,
                "buildings",
                "default_type_filter",
            )
            collected_default_count = self.get_record_count(building_details)
            building_counters[
                "records_collected_before_post_filter"
            ] += collected_default_count
            building_counters[
                "records_collected_after_post_filter"
            ] += collected_default_count
            self.log(
                "Retrieved building details summary: query_params={0}, "
                "collected_records={1}.".format(
                    default_params,
                    collected_default_count,
                ),
                "INFO",
            )
            self.log(
                "Building detail payload (debug): {0}".format(building_details),
                "DEBUG",
            )
            final_buildings.extend(building_details)

        # Remove duplicate building records before transformation.
        records_before_dedupe = self.get_record_count(final_buildings)
        final_buildings = self.dedupe_site_details(final_buildings, "buildings")
        records_after_dedupe = self.get_record_count(final_buildings)
        building_counters["records_ignored_as_duplicates"] = max(
            0, records_before_dedupe - records_after_dedupe
        )

        # Apply reverse mapping to convert API keys into YAML schema keys.
        building_temp_spec = self.building_temp_spec()
        buildings_details = self.modify_parameters(building_temp_spec, final_buildings)
        transformed_records = self.get_record_count(buildings_details)

        self.log(
            "Building processing counters: filters_received={0}, "
            "filters_processed={1}, filters_skipped={2}, api_calls={3}, "
            "query_plan_buckets={4}, query_plan_entries_collapsed={5}, "
            "adaptive_one_fetch_mode={6}, "
            "records_collected_before_post_filter={7}, "
            "records_filtered_out_post_filter={8}, "
            "records_collected_after_post_filter={9}, "
            "records_ignored_as_duplicates={10}, final_records_after_dedupe={11}, "
            "transformed_records={12}.".format(
                building_counters["filters_received"],
                building_counters["filters_processed"],
                building_counters["filters_skipped"],
                building_counters["api_calls"],
                building_counters["query_plan_buckets"],
                building_counters["query_plan_entries_collapsed"],
                building_counters["adaptive_one_fetch_mode"],
                building_counters["records_collected_before_post_filter"],
                building_counters["records_filtered_out_post_filter"],
                building_counters["records_collected_after_post_filter"],
                building_counters["records_ignored_as_duplicates"],
                records_after_dedupe,
                transformed_records,
            ),
            "INFO",
        )

        self.log(
            "Modified building details payload (debug): {0}".format(buildings_details),
            "DEBUG",
        )

        self.log("Building retrieval workflow completed.", "INFO")
        return buildings_details

    def get_floors_configuration(
        self, network_element, component_specific_filters=None
    ):
        """
        Retrieve and transform floor records for YAML output.

        The method mirrors area/building processing behavior while applying floor
        specific schema mapping for geometry and RF attributes.

        Args:
            network_element (dict): API metadata containing family and function names.
            component_specific_filters (list | None): Optional floor filter set.

        Returns:
            list: Mapped floor configuration objects for YAML serialization.
        """

        self.log("Starting floor retrieval workflow.", "INFO")
        self.log(
            f"Starting to retrieve floors with network element: {network_element} and component-specific filters: {component_specific_filters}",
            "INFO",
        )

        # Normalize filters payload so this retrieval function can be called both
        # from module-local flow and shared helper flow.
        component_specific_filters = self.resolve_component_filters(
            component_specific_filters
        )

        # Collect floor records fetched for each normalized filter expression.
        final_floors = []
        floor_counters = {
            "filters_received": (
                len(component_specific_filters) if component_specific_filters else 0
            ),
            "filters_processed": 0,
            "filters_skipped": 0,
            "api_calls": 0,
            "query_plan_buckets": 0,
            "query_plan_entries_collapsed": 0,
            "adaptive_one_fetch_mode": 0,
            "records_collected_before_post_filter": 0,
            "records_filtered_out_post_filter": 0,
            "records_collected_after_post_filter": 0,
            "records_ignored_as_duplicates": 0,
        }
        # Resolve SDK family/function for paginated API execution.
        api_family = network_element.get("api_family")
        api_function = network_element.get("api_function")

        self.log(
            f"Getting floors using family '{api_family}' and function '{api_function}'.",
            "INFO",
        )

        if (
            self.should_use_unified_site_fetch()
            and component_specific_filters is not None
        ):
            self.log(
                "Unified one-pass direct-filter retrieval mode is enabled for floors.",
                "INFO",
            )
            unified_records_by_type, unified_summary = (
                self.get_unified_filtered_site_records(api_family, api_function)
            )
            floor_details = unified_records_by_type.get("floor") or []
            collected_floor_count = self.get_record_count(floor_details)
            floor_counters["filters_processed"] = unified_summary.get(
                "filter_expressions_processed", 0
            )
            floor_counters["api_calls"] += unified_summary.get("api_calls", 0)
            floor_counters["query_plan_buckets"] = 1
            floor_counters["adaptive_one_fetch_mode"] = 1
            floor_counters[
                "records_collected_before_post_filter"
            ] += collected_floor_count
            floor_counters[
                "records_collected_after_post_filter"
            ] += collected_floor_count
            final_floors.extend(floor_details)
            self.log(
                "Unified fetch consumption summary for floors: cache_hit={0}, "
                "api_calls={1}, records_collected_before_global_filter={2}, "
                "records_after_global_filter={3}, component_records={4}.".format(
                    unified_summary.get("cache_hit", 0),
                    unified_summary.get("api_calls", 0),
                    unified_summary.get("records_collected_before_filter", 0),
                    unified_summary.get("records_after_filter", 0),
                    collected_floor_count,
                ),
                "INFO",
            )
        elif component_specific_filters is None:
            self.log(
                "Floor component retrieval is skipped due to "
                "type-aware filter pruning.",
                "INFO",
            )
            floor_counters["filters_skipped"] += 1
        elif component_specific_filters:
            self.log(
                "Component-specific filters were provided for floor retrieval.", "INFO"
            )
            # Build a query plan keyed by API params so identical queries are
            # executed once and post-filters are applied from the shared payload.
            query_plan = OrderedDict()
            for filter_param in component_specific_filters:
                floor_counters["filters_processed"] += 1
                self.log(
                    "Processing floor filter expression at query-planning "
                    "stage: {0}".format(filter_param),
                    "DEBUG",
                )
                params, post_filters = self.build_site_query_context(
                    filter_param, "floor"
                )
                if not params:
                    floor_counters["filters_skipped"] += 1
                    self.log(
                        "Skipping floor filter due to invalid parameters.",
                        "WARNING",
                    )
                    continue

                query_cache_key = tuple(sorted(params.items()))
                if query_cache_key not in query_plan:
                    query_plan[query_cache_key] = {
                        "params": params,
                        "entries": OrderedDict(),
                    }

                post_filter_signature = self.build_filter_signature(post_filters)
                if post_filter_signature in query_plan[query_cache_key]["entries"]:
                    floor_counters["query_plan_entries_collapsed"] += 1
                    continue

                query_plan[query_cache_key]["entries"][post_filter_signature] = {
                    "post_filters": post_filters,
                    "source_filter": filter_param,
                }

            floor_counters["query_plan_buckets"] = len(query_plan)
            if len(query_plan) == 1 and floor_counters["filters_processed"] > 1:
                only_bucket = next(iter(query_plan.values()))
                only_params = only_bucket.get("params") or {}
                if set(only_params.keys()) == {"type"}:
                    floor_counters["adaptive_one_fetch_mode"] = 1
                    self.log(
                        "Adaptive one-fetch mode enabled for floors: "
                        "single type-only query bucket with multiple "
                        "post-filter expressions.",
                        "INFO",
                    )

            for bucket in query_plan.values():
                floor_counters["api_calls"] += 1
                floor_details = self.execute_sites_api_with_timing(
                    api_family,
                    api_function,
                    bucket.get("params"),
                    "floors",
                    "bucketed_filters",
                )
                collected_before_post_filter = self.get_record_count(floor_details)
                floor_counters[
                    "records_collected_before_post_filter"
                ] += collected_before_post_filter
                self.log(
                    "Retrieved floor details summary: query_params={0}, "
                    "collected_records={1}.".format(
                        bucket.get("params"),
                        collected_before_post_filter,
                    ),
                    "INFO",
                )
                self.log(
                    "Floor detail payload (debug): {0}".format(floor_details), "DEBUG"
                )

                for entry in bucket.get("entries", {}).values():
                    post_filters = entry.get("post_filters") or {}
                    if post_filters:
                        self.log(
                            "Applying post filters to floor details: {0}".format(
                                post_filters
                            ),
                            "INFO",
                        )
                        pre_post_filter_count = self.get_record_count(floor_details)
                        filtered_floor_details = self.apply_site_post_filters(
                            floor_details, post_filters
                        )
                        post_post_filter_count = self.get_record_count(
                            filtered_floor_details
                        )
                        floor_counters["records_filtered_out_post_filter"] += max(
                            0, pre_post_filter_count - post_post_filter_count
                        )
                    else:
                        filtered_floor_details = floor_details
                        post_post_filter_count = collected_before_post_filter

                    floor_counters[
                        "records_collected_after_post_filter"
                    ] += post_post_filter_count
                    final_floors.extend(filtered_floor_details)
        else:
            self.log(
                "No component-specific filters provided for floors; using default type filter.",
                "INFO",
            )
            default_params = {"type": "floor"}
            floor_counters["query_plan_buckets"] = 1
            floor_counters["api_calls"] += 1
            floor_details = self.execute_sites_api_with_timing(
                api_family,
                api_function,
                default_params,
                "floors",
                "default_type_filter",
            )
            collected_default_count = self.get_record_count(floor_details)
            floor_counters[
                "records_collected_before_post_filter"
            ] += collected_default_count
            floor_counters[
                "records_collected_after_post_filter"
            ] += collected_default_count
            self.log(
                "Retrieved floor details summary: query_params={0}, "
                "collected_records={1}.".format(
                    default_params,
                    collected_default_count,
                ),
                "INFO",
            )
            self.log("Floor detail payload (debug): {0}".format(floor_details), "DEBUG")
            final_floors.extend(floor_details)

        # Remove duplicates before final output mapping.
        records_before_dedupe = self.get_record_count(final_floors)
        final_floors = self.dedupe_site_details(final_floors, "floors")
        records_after_dedupe = self.get_record_count(final_floors)
        floor_counters["records_ignored_as_duplicates"] = max(
            0, records_before_dedupe - records_after_dedupe
        )

        # Convert raw floor payloads into downstream YAML schema.
        floor_temp_spec = self.floor_temp_spec()
        floors_details = self.modify_parameters(floor_temp_spec, final_floors)
        transformed_records = self.get_record_count(floors_details)

        self.log(
            "Floor processing counters: filters_received={0}, filters_processed={1}, "
            "filters_skipped={2}, api_calls={3}, query_plan_buckets={4}, "
            "query_plan_entries_collapsed={5}, adaptive_one_fetch_mode={6}, "
            "records_collected_before_post_filter={7}, "
            "records_filtered_out_post_filter={8}, "
            "records_collected_after_post_filter={9}, "
            "records_ignored_as_duplicates={10}, final_records_after_dedupe={11}, "
            "transformed_records={12}.".format(
                floor_counters["filters_received"],
                floor_counters["filters_processed"],
                floor_counters["filters_skipped"],
                floor_counters["api_calls"],
                floor_counters["query_plan_buckets"],
                floor_counters["query_plan_entries_collapsed"],
                floor_counters["adaptive_one_fetch_mode"],
                floor_counters["records_collected_before_post_filter"],
                floor_counters["records_filtered_out_post_filter"],
                floor_counters["records_collected_after_post_filter"],
                floor_counters["records_ignored_as_duplicates"],
                records_after_dedupe,
                transformed_records,
            ),
            "INFO",
        )

        self.log(
            "Modified floor details payload (debug): {0}".format(floors_details),
            "DEBUG",
        )

        self.log("Floor retrieval workflow completed.", "INFO")
        return floors_details

    def resolve_component_filters(self, component_specific_filters):
        """
        Resolve component filter payload shape for retrieval functions.

        Supported payload:
        - Helper-wrapped form from BrownFieldHelper:
          `{"global_filters": {...}, "component_specific_filters": [...]}`.
        - Direct list form for internal/unit-test invocation:
          `[{"site_name_hierarchy": ...}, ...]`.

        Args:
            component_specific_filters (Any): Incoming filter payload.

        Returns:
            list: Component-specific filter expressions list.
        """
        total_filters_collected = 0
        ignored_filter_container = 0
        if component_specific_filters is None:
            ignored_filter_container = 1
            self.log(
                "Resolved component filters from empty payload: "
                "filters_collected=0, ignored_filter_container={0}.".format(
                    ignored_filter_container
                ),
                "INFO",
            )
            return []

        # BrownFieldHelper.yaml_config_generator passes a wrapped dictionary.
        if isinstance(component_specific_filters, dict):
            wrapped_filters = component_specific_filters.get(
                "component_specific_filters"
            )
            if wrapped_filters is None:
                ignored_filter_container = 1
                self.log(
                    "Resolved component filters from wrapped payload: "
                    "filters_collected=0, ignored_filter_container={0}, "
                    "explicit_component_skip=True.".format(ignored_filter_container),
                    "INFO",
                )
                return None
            if not isinstance(wrapped_filters, list):
                self.fail_and_exit(
                    "'component_specific_filters.site' must be a list of filter dictionaries."
                )
            total_filters_collected = self.get_record_count(wrapped_filters)
            self.log(
                "Resolved component filters from wrapped payload: "
                "filters_collected={0}, ignored_filter_container={1}.".format(
                    total_filters_collected, ignored_filter_container
                ),
                "INFO",
            )
            return wrapped_filters

        if not isinstance(component_specific_filters, list):
            self.fail_and_exit(
                "Resolved component filters must be a list of filter dictionaries."
            )

        total_filters_collected = self.get_record_count(component_specific_filters)
        self.log(
            "Resolved component filters from direct payload: "
            "filters_collected={0}, ignored_filter_container={1}.".format(
                total_filters_collected, ignored_filter_container
            ),
            "INFO",
        )
        return component_specific_filters

    def get_want(self, config, state):
        """
        Build normalized desired-state payload (`want`) for operation dispatch.

        This method is the preparation stage prior to `get_diff_gathered`, and is
        responsible for filter normalization, parameter validation, and assembly
        of operation-specific argument objects.

        Args:
            config (dict): Single validated config object from playbook input.
            state (str): Requested state, expected to be `gathered`.

        Returns:
            SitePlaybookGenerator: Instance with `self.want` initialized.
        """

        self.log(
            "Preparing desired-state payload from validated configuration.", "INFO"
        )
        self.log(f"Creating Parameters for API Calls with state: {state}", "INFO")

        # Reset cached unified payload so each config entry is processed
        # independently.
        self._normalized_component_specific_filters = {}
        self._unified_site_records_cache = None
        self._unified_site_records_cache_key = None

        # Validate payload against shared schema rules.
        self.validate_params(config)

        self._normalized_component_specific_filters = (
            config.get("component_specific_filters") or {}
        )
        self.log(
            "Resolved component_specific_filters keys for execution: {0}.".format(
                list(self._normalized_component_specific_filters.keys())
            ),
            "INFO",
        )

        # Store mode flag for contextual logging and downstream decisions.
        self.generate_all_configurations = config.get(
            "generate_all_configurations", False
        )
        self.log(
            f"Set generate_all_configurations mode: {self.generate_all_configurations}",
            "INFO",
        )

        # Build desired-state dictionary consumed by gather execution loop.
        want = {}

        # Register YAML generation operation payload under expected key.
        want["yaml_config_generator"] = config
        self.log(
            f"yaml_config_generator added to want: {want['yaml_config_generator']}",
            "INFO",
        )

        self.want = want
        self.log(f"Desired State (want): {self.want}", "INFO")
        self.msg = "Successfully collected all parameters from the playbook for Site operations."
        self.status = "success"
        self.log("Desired-state payload preparation completed.", "INFO")
        return self

    def get_diff_gathered(self):
        """
        Execute gather-mode operations and collect output artifacts.

        The method iterates a declared operation table, resolves parameter blocks
        from `self.want`, executes each operation function, and records timing.

        Args:
            self: Instance carrying prepared desired-state payload.

        Returns:
            SitePlaybookGenerator: Instance with refreshed operation result status.
        """

        # Capture execution start time for high-level performance telemetry.
        start_time = time.time()
        self.log("Starting gather-state diff processing workflow.", "INFO")
        # Declare gather operations in execution order.
        operations = [
            (
                "yaml_config_generator",
                "YAML Config Generator",
                self.yaml_config_generator,
            )
        ]

        # Iterate through operation table and execute only operations that have
        # prepared parameters in `self.want`.
        self.log("Beginning iteration over defined operations for processing.", "INFO")
        for index, (param_key, operation_name, operation_func) in enumerate(
            operations, start=1
        ):
            self.log(
                f"Iteration {index}: Checking parameters for {operation_name} operation with param_key '{param_key}'.",
                "INFO",
            )
            params = self.want.get(param_key)
            if params:
                self.log(
                    f"Iteration {index}: Parameters found for {operation_name}. Starting processing.",
                    "INFO",
                )
                operation_func(params).check_return_status()
            else:
                self.log(
                    f"Iteration {index}: No parameters found for {operation_name}. Skipping operation.",
                    "WARNING",
                )

        # Capture execution end time to log total gather duration.
        end_time = time.time()
        self.log(
            f"Completed 'get_diff_gathered' operation in {end_time - start_time:.2f} seconds.",
            "INFO",
        )

        self.log("Gather-state diff processing workflow completed.", "INFO")
        return self


def main():
    """Run the Ansible module lifecycle for site playbook config generation.

    Flow summary:
    1. Build Ansible argument schema.
    2. Initialize `SitePlaybookGenerator`.
    3. Enforce minimum Catalyst Center version support.
    4. Validate requested state and user configuration.
    5. Execute gather operation and return standardized module result.
    """
    LOGGER.debug(
        "main() execution started; preparing argument specification and module "
        "runtime bootstrap for site playbook configgeneration."
    )
    # Define module argument contract used by Ansible runtime for parameter
    # parsing, defaults, and type validation.
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

    # Create the AnsibleModule instance that encapsulates parsed params and
    # result/failure handling helpers.
    module = AnsibleModule(argument_spec=element_spec, supports_check_mode=True)

    # Bootstrap module implementation class with connection/runtime context.
    ccc_site_playbook_generator = SitePlaybookGenerator(module)
    ccc_site_playbook_generator.log(
        "Main runtime bootstrap completed: instantiated SitePlaybookGenerator "
        "with validated Ansible module arguments and helper dependencies.",
        "DEBUG",
    )
    # Enforce minimum supported Catalyst Center version before attempting site
    # workflow export operations.
    if (
        ccc_site_playbook_generator.compare_dnac_versions(
            ccc_site_playbook_generator.get_ccc_version(), "2.3.7.6"
        )
        < 0
    ):
        ccc_site_playbook_generator.log(
            "Catalyst Center version check failed for site playbook generation support.",
            "DEBUG",
        )
        ccc_site_playbook_generator.msg = (
            "The specified version '{0}' does not support the YAML Playbook generation "
            "for Site Workflow Manager Module. Supported versions start from '2.3.7.6' onwards. "
            "Version '2.3.7.6' introduces APIs for retrieving site hierarchy including "
            "areas, buildings, and floors from the Catalyst Center".format(
                ccc_site_playbook_generator.get_ccc_version()
            )
        )
        ccc_site_playbook_generator.fail_and_exit(ccc_site_playbook_generator.msg)
    # Read desired state from module params after bootstrap checks.
    state = ccc_site_playbook_generator.params.get("state")

    # Validate state against module-supported states.
    if state not in ccc_site_playbook_generator.supported_states:
        ccc_site_playbook_generator.log(
            "Requested state is not supported by this module implementation.",
            "DEBUG",
        )
        ccc_site_playbook_generator.status = "invalid"
        ccc_site_playbook_generator.msg = "State {0} is invalid".format(state)
        ccc_site_playbook_generator.check_return_status()

    # Validate and normalize incoming config list before per-entry processing.
    ccc_site_playbook_generator.validate_input().check_return_status()
    config = ccc_site_playbook_generator.validated_config

    # Process each validated config entry independently so one entry's internal
    # mutations do not leak into another.
    for config in ccc_site_playbook_generator.validated_config:
        ccc_site_playbook_generator.log(
            "Processing one validated configuration entry from user input. "
            f"Resolved entry payload: {config}",
            "DEBUG",
        )
        # Reset helper state maps, prepare desired state, and execute gathered
        # diff flow for the current config object.
        ccc_site_playbook_generator.reset_values()
        ccc_site_playbook_generator.get_want(config, state).check_return_status()
        ccc_site_playbook_generator.get_diff_state_apply[state]().check_return_status()

    ccc_site_playbook_generator.log(
        "Main workflow completed; final Ansible response payload is ready.",
        "DEBUG",
    )
    module.exit_json(**ccc_site_playbook_generator.result)


if __name__ == "__main__":
    main()
