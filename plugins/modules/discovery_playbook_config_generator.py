#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright (c) 2026, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

"""Ansible module to generate YAML configurations for Discovery Workflow Manager Module."""
from __future__ import absolute_import, division, print_function

__metaclass__ = type
__author__ = "Megha Kandari, Madhan Sankaranarayanan"

DOCUMENTATION = r"""
---
module: discovery_playbook_config_generator
short_description: Generate YAML configurations playbook for 'discovery_workflow_manager' module.
description:
- Generates YAML playbooks compatible with the
  C(discovery_workflow_manager) module by extracting
  existing discovery configurations from Cisco Catalyst
  Center.
- Reduces manual effort by programmatically retrieving
  discovery tasks including IP ranges, credential
  mappings, discovery types, protocol orders, and
  task-specific settings.
- Supports selective filtering by discovery name,
  discovery type, or discovery status to generate
  targeted playbooks.
- Enables complete infrastructure discovery with
  auto-generation mode when
  C(generate_all_configurations) is enabled.
- Resolves credential IDs to human-readable descriptions
  and usernames for generated playbooks.
- Requires Cisco Catalyst Center version 2.3.7.9 or
  higher for discovery API support.
version_added: 6.44.0
extends_documentation_fragment:
- cisco.dnac.workflow_manager_params
author:
- Megha Kandari (@mekandar)
- Madhan Sankaranarayanan (@madhansansel)
options:
  state:
    description:
    - The desired state for the module operation.
    - Only C(gathered) state is supported to generate
      YAML playbooks from existing configurations.
    type: str
    choices: [gathered]
    default: gathered
  config:
    description:
      - A list of filters for generating YAML playbook compatible with the 'discovery_workflow_manager'
        module.
      - Filters specify which discovery tasks and configurations to include in the YAML configuration file.
      - Global filters identify target discoveries by name or discovery type.
      - Component-specific filters allow selection of specific discovery features and detailed filtering.
    type: list
    elements: dict
    required: true
    suboptions:
      generate_all_configurations:
        description:
          - When set to True, automatically generates YAML configurations for all discovery tasks.
          - This mode discovers all existing discovery configurations in Cisco Catalyst Center.
          - When enabled, the config parameter becomes optional and will use default values if not provided.
          - A default filename will be generated automatically if file_path is not specified.
          - This is useful for complete discovery playbook configuration infrastructure documentation.
          - Note - This will include all discovery tasks regardless of their current status.
          - When set to False, at least one of 'global_filters' or 'component_specific_filters' must be provided.
        type: bool
        required: false
        default: false
      file_path:
        description:
          - Path where the YAML configuration file will be saved.
          - If not provided, the file will be saved in the current working directory with
            a default file name C(<module_name>playbook<YYYY-MM-DD_HH-MM-SS>.yml).
          - For example, C(discovery_workflow_manager_playbook_2026-01-24_12-33-20.yml).
        type: str
        required: false
      global_filters:
        description:
          - Global filters to apply when generating the YAML configuration file.
          - These filters identify which discovery tasks to extract configurations from.
          - If not specified, all discovery tasks will be included.
        type: dict
        required: false
        suboptions:
          discovery_name_list:
            description:
              - List of discovery task names to extract configurations from.
              - HIGHEST PRIORITY - If provided, discovery types will be ignored.
              - Discovery names must match those configured in Catalyst Center.
              - Case-sensitive and must be exact matches.
              - Example ["Multi_global", "Single IP Discovery", "CDP_Test_1"]
            type: list
            elements: str
            required: false
          discovery_type_list:
            description:
              - List of discovery types to filter by.
              - LOWER PRIORITY - Only used if discovery_name_list is not provided.
              - Valid values are SINGLE, RANGE, MULTI RANGE, CDP, LLDP, CIDR.
              - Will include all discoveries matching any of the specified types.
              - Example ["MULTI RANGE", "CDP", "LLDP"]
            type: list
            elements: str
            required: false
            choices:
            - SINGLE
            - RANGE
            - MULTI RANGE
            - CDP
            - LLDP
            - CIDR

requirements:
- dnacentersdk >= 2.4.5
- python >= 3.9
- Cisco Catalyst Center >= 2.3.7.9
notes:
- Requires minimum Cisco Catalyst Center version
  2.3.7.9 for discovery API support.
- Module will fail with an error if connected to an
  unsupported version.
- Generated playbooks are compatible with the
  C(discovery_workflow_manager) module for discovery
  task operations.
- Credential IDs are automatically resolved to
  descriptions and usernames using global credentials
  API.
- Discovery-specific credentials are excluded from
  generated playbooks for security reasons.
- The module operates in check mode but does not make
  any changes to Cisco Catalyst Center.
- Use C(dnac_log) and C(dnac_log_level) parameters for
  detailed operation logging and troubleshooting.

- SDK Methods used are
  - discovery.Discovery.get_discoveries_by_range
  - discovery.Discovery.get_discovery_by_id
  - discovery.Discovery.get_all_global_credentials
  - discovery.Discovery.get_all_global_credentials_v2
  - discovery.Discovery.get_discovered_network_devices_by_discovery_id
- Paths used are
  - GET /dna/intent/api/v1/discovery/{startIndex}/{recordsToReturn}
  - GET /dna/intent/api/v1/discovery/{id}
  - GET /dna/intent/api/v1/global-credential
  - GET /dna/intent/api/v2/global-credential
  - GET /dna/intent/api/v1/discovery/{id}/network-device

seealso:
- module: cisco.dnac.discovery_workflow_manager
  description: Manage discovery workflows in Cisco
    Catalyst Center.
"""

EXAMPLES = r"""
# Generate YAML configurations for all discovery tasks
- name: Generate all discovery configurations
  cisco.dnac.discovery_playbook_config_generator:
    dnac_host: "{{ dnac_host }}"
    dnac_username: "{{ dnac_username }}"
    dnac_password: "{{ dnac_password }}"
    dnac_verify: "{{ dnac_verify }}"
    dnac_port: "{{ dnac_port }}"
    dnac_version: "{{ dnac_version }}"
    dnac_debug: "{{ dnac_debug }}"
    state: gathered
    config:
      - generate_all_configurations: true

# Generate configurations for specific discovery tasks by name
- name: Generate specific discovery configurations by name
  cisco.dnac.discovery_playbook_config_generator:
    dnac_host: "{{ dnac_host }}"
    dnac_username: "{{ dnac_username }}"
    dnac_password: "{{ dnac_password }}"
    dnac_verify: "{{ dnac_verify }}"
    dnac_port: "{{ dnac_port }}"
    dnac_version: "{{ dnac_version }}"
    dnac_debug: "{{ dnac_debug }}"
    state: gathered
    config:
      - file_path: "/tmp/specific_discoveries.yml"
        global_filters:
          discovery_name_list:
            - "Multi_global"
            - "Single IP Discovery"
            - "CDP_Test_1"

# Generate configurations for specific discovery types
- name: Generate configurations by discovery type
  cisco.dnac.discovery_playbook_config_generator:
    dnac_host: "{{ dnac_host }}"
    dnac_username: "{{ dnac_username }}"
    dnac_password: "{{ dnac_password }}"
    dnac_verify: "{{ dnac_verify }}"
    dnac_port: "{{ dnac_port }}"
    dnac_version: "{{ dnac_version }}"
    dnac_debug: "{{ dnac_debug }}"
    state: gathered
    config:
      - file_path: "/tmp/cdp_lldp_discoveries.yml"
        global_filters:
          discovery_type_list:
            - "CDP"
            - "LLDP"
"""

RETURN = r"""
# Case 1: Successful generation of discovery YAML configuration
response_1:
  description: A dictionary with the details of the generated YAML configuration
  returned: always
  type: dict
  sample: >
    {
      "response": {
        "status": "success",
        "file_path": "/path/to/discovery_workflow_manager_playbook_22_Dec_2024_21_43_26_379.yml",
        "total_discoveries_processed": 5,
        "discoveries_found": [
          {
            "discovery_name": "Multi_global",
            "discovery_type": "MULTI RANGE",
            "status": "Complete"
          },
          {
            "discovery_name": "Single IP Discovery",
            "discovery_type": "SINGLE",
            "status": "Complete"
          }
        ],
        "discoveries_skipped": [],
        "component_summary": {
          "discovery_details": {
            "total_processed": 5,
            "total_successful": 5,
            "total_failed": 0
          }
        }
      },
      "msg": "Discovery YAML configuration generated successfully"
    }

# Case 2: No discoveries found matching the criteria
response_2:
  description: A dictionary indicating no discoveries were found
  returned: when no discoveries match the filtering criteria
  type: dict
  sample: >
    {
      "response": {
        "status": "no_data",
        "message": "No discoveries found matching the specified criteria"
      },
      "msg": "No discoveries found to generate configuration"
    }

# Case 3: Error during generation
response_3:
  description: A dictionary with error details
  returned: when an error occurs during generation
  type: dict
  sample: >
    {
      "response": {
        "status": "failed",
        "error": "Failed to retrieve discovery data from Catalyst Center"
      },
      "msg": "Error occurred during YAML generation"
    }
"""

import time
import os
import datetime
try:
    import yaml
    HAS_YAML = True
except ImportError:
    HAS_YAML = False
    yaml = None
from collections import OrderedDict
from ansible.module_utils.basic import AnsibleModule
from ansible_collections.cisco.dnac.plugins.module_utils.dnac import (
    DnacBase,
    validate_list_of_dicts
)
from ansible_collections.cisco.dnac.plugins.module_utils.brownfield_helper import (
    BrownFieldHelper
)


class DiscoveryPlaybookGenerator(DnacBase, BrownFieldHelper):
    """
    Brownfield playbook generator for discovery
    configurations.

    Attributes:
        module_name (str): Target module name for
            generated playbooks
            ('discovery_playbook_generator').
        supported_states (list): Supported Ansible states
            (only 'gathered').
        _global_credentials_lookup (dict or None): Cached
            mapping of credential IDs to credential details
            (description, username, type).
        module_schema (dict): Workflow filters schema
            defining global_filters and network_elements
            for discovery processing.

    Description:
        Retrieves existing discovery task configurations
        from Cisco Catalyst Center and generates YAML
        playbooks compatible with the
        discovery_workflow_manager module. Supports
        filtering by discovery name, type, or status.
        Transforms credential IDs to human-readable
        descriptions and usernames using global
        credentials API. Requires Cisco Catalyst Center
        version 2.3.7.9 or higher.
    """

    def __init__(self, module):
        """
        Initialize DiscoveryPlaybookGenerator instance.

        Parameters:
            module (AnsibleModule): The Ansible module
                instance.

        Returns:
            None

        Description:
            Sets up supported states, initializes parent
            classes, sets module name, and defines the
            workflow schema for discovery components.
        """
        super().__init__(module)
        self.module_name = "discovery_playbook_generator_config"
        self.supported_states = ["gathered"]
        self._global_credentials_lookup = None

        # Discovery workflow manager module schema
        self.module_schema = {
            "global_filters": {
                "discovery_name_list": {
                    "type": "list",
                    "elements": "str",
                    "description": "List of discovery names to filter by"
                },
                "discovery_type_list": {
                    "type": "list",
                    "elements": "str",
                    "description": "List of discovery types to filter by",
                    "choices": ['SINGLE', 'RANGE', 'MULTI RANGE', 'CDP', 'LLDP', 'CIDR']
                }
            },
            "network_elements": {
                "discovery_details": {
                    "filters": {
                        "components_list": {
                            "type": "list",
                            "elements": "str",
                            "description": "List of components to include"
                        },
                        "include_global_credentials": {
                            "type": "bool",
                            "description": "Include global credential mappings"
                        },
                    }
                }
            }
        }

    def validate_input(self):
        """
        Validate input configuration parameters for
            discovery playbook generation.

            Parameters:
                None

            Returns:
                self: Instance with updated msg, status, and
                    validated_config.

            Description:
                Validates playbook configuration parameters
                against the expected schema. Checks for
                invalid parameter names, validates parameter
                types, and sets validated_config on success
                or returns error status with details on
                failure.
        """
        self.log("Starting input validation for discovery playbook generator", "INFO")

        if not self.config:
            self.msg = "Configuration is required"
            self.log(self.msg, "ERROR")
            self.status = "failed"
            return self.check_return_status()

        # Expected schema for configuration parameters
        temp_spec = {
            "generate_all_configurations": {"type": "bool", "required": False, "default": False},
            "file_path": {"type": "str", "required": False},
            "component_specific_filters": {"type": "dict", "required": False},
            "global_filters": {"type": "dict", "required": False},
        }

        allowed_keys = set(temp_spec.keys())

        # Validate that only allowed keys are present in the configuration
        for config_item in self.config:
            if not isinstance(config_item, dict):
                self.msg = "Configuration item must be a dictionary, got: {0}".format(type(config_item).__name__)
                self.set_operation_result("failed", False, self.msg, "ERROR")
                return self

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
                self.set_operation_result("failed", False, self.msg, "ERROR").check_return_status()

        self.validate_minimum_requirement_for_global_filters(self.config)

        # Validate params
        valid_temp, invalid_params = validate_list_of_dicts(self.config, temp_spec)

        if invalid_params:
            self.msg = "Invalid parameters in playbook: {0}".format(invalid_params)
            self.set_operation_result("failed", False, self.msg, "ERROR")
            return self

        self.log(
            "Input validation completed successfully for "
            "{0} configuration item(s)".format(
                len(self.config)
            ),
            "INFO"
        )

        # Set the validated configuration and update the result with success status
        self.validated_config = valid_temp
        self.msg = "Successfully validated playbook configuration"
        "       parameters using 'validated_input': {0}".format(
            str(valid_temp)
        )
        self.set_operation_result("success", False, self.msg, "INFO")
        return self

    def get_global_credentials_lookup(self):
        """
        Build lookup mapping of global credential IDs to
        their details.

        Parameters:
            None

        Returns:
            dict: Mapping of credential IDs to credential
                information (description, username, type).
                Returns cached value if already built.

        Description:
            Creates a lookup dictionary by querying
            get_all_global_credentials API (v1), then
            falls back to v2 API if no results. Processes
            credential types (CLI, SNMP v2/v3, HTTPS,
            NetConf) and maps IDs to descriptions,
            usernames, and types. Caches the result in
            _global_credentials_lookup.
        """
        if self._global_credentials_lookup is not None:
            self.log(
                "Returning cached global credentials "
                "lookup with {0} entry(ies)".format(
                    len(self._global_credentials_lookup)
                ),
                "DEBUG"
            )
            return self._global_credentials_lookup

        self.log(
            "Building global credentials lookup table "
            "from Catalyst Center API (v1 primary, v2 "
            "fallback)",
            "INFO"
        )
        self._global_credentials_lookup = {}

        try:
            # Use the same approach as discovery_workflow_manager.py
            headers = {}
            response = self.dnac._exec(
                family="discovery",
                function="get_all_global_credentials",
                params=headers,
                op_modifies=True,
            )
            self.log(
                "V1 API call completed, raw response type: "
                "{0}".format(
                    type(response).__name__ if response
                    is not None else "None"
                ),
                "DEBUG"
            )

            # Extract response data
            if response is None:
                self.log(
                    "V1 API returned None response, "
                    "attempting v2 fallback",
                    "WARNING"
                )
                # Jump directly to v2 fallback
                response_data = None
            elif isinstance(response, dict):
                response_data = response.get("response")
                self.log(
                    "V1 API returned dict, extracted "
                    "'response' key: type={0}, "
                    "is_none={1}".format(
                        type(response_data).__name__
                        if response_data is not None
                        else "None",
                        response_data is None
                    ),
                    "DEBUG"
                )

                if response_data is None:
                    self.log(
                        "V1 API dict contains None "
                        "'response' key, using full dict "
                        "as response_data",
                        "DEBUG"
                    )
                    response_data = response
            else:
                self.log(
                    "V1 API returned unexpected type "
                    "{0}, treating as direct "
                    "response_data".format(
                        type(response).__name__
                    ),
                    "WARNING"
                )
                response_data = response

            # Validate response_data structure
            if response_data is None:
                self.log(
                    "V1 API response_data is None after "
                    "extraction, skipping v1 processing",
                    "WARNING"
                )
            elif not isinstance(response_data, dict):
                self.log(
                    "V1 API response_data is not a dict "
                    "(type: {0}), skipping v1 "
                    "processing".format(
                        type(response_data).__name__
                    ),
                    "WARNING"
                )
                response_data = None

            self.log(f"Global credentials API response type: {type(response_data)}", "DEBUG")
            self.log(f"Global credentials API response content: {response_data}", "DEBUG")

            # Process v1 response if valid
            if response_data is not None and isinstance(
                    response_data, dict
            ):
                credential_types = [
                    'cliCredential', 'snmpV2cRead',
                    'snmpV2cWrite', 'snmpV3',
                    'httpsRead', 'httpsWrite',
                    'netconfCredential'
                ]

                self.log(
                    "V1 API response_data is valid dict, "
                    "processing {0} credential "
                    "type(s)".format(
                        len(credential_types)
                    ),
                    "DEBUG"
                )

                for type_index, cred_type in enumerate(
                    credential_types, start=1
                ):
                    credentials_list = response_data.get(
                        cred_type
                    )

                    if credentials_list is None:
                        self.log(
                            "V1 credential type {0}/{1}: "
                            "'{2}' key not found in "
                            "response, skipping".format(
                                type_index,
                                len(credential_types),
                                cred_type
                            ),
                            "DEBUG"
                        )
                        continue

                    if not isinstance(credentials_list, list):
                        self.log(
                            "V1 credential type {0}/{1}: "
                            "'{2}' is not a list (type: "
                            "{3}), skipping".format(
                                type_index,
                                len(credential_types),
                                cred_type,
                                type(credentials_list)
                                .__name__
                            ),
                            "WARNING"
                        )
                        continue

                    if len(credentials_list) == 0:
                        self.log(
                            "V1 credential type {0}/{1}: "
                            "'{2}' list is empty, "
                            "skipping".format(
                                type_index,
                                len(credential_types),
                                cred_type
                            ),
                            "DEBUG"
                        )
                        continue

                    self.log(
                        "V1 credential type {0}/{1}: "
                        "'{2}' found with {3} "
                        "entry(ies), processing".format(
                            type_index,
                            len(credential_types),
                            cred_type,
                            len(credentials_list)
                        ),
                        "DEBUG"
                    )

                    for cred_index, cred in enumerate(
                        credentials_list, start=1
                    ):
                        if cred is None:
                            self.log(
                                "V1 credential type '{0}' "
                                "entry {1}/{2} is None, "
                                "skipping".format(
                                    cred_type, cred_index,
                                    len(credentials_list)
                                ),
                                "WARNING"
                            )
                            continue

                        if not isinstance(cred, dict):
                            self.log(
                                "V1 credential type '{0}' "
                                "entry {1}/{2} is not a "
                                "dict (type: {3}), "
                                "skipping".format(
                                    cred_type, cred_index,
                                    len(credentials_list),
                                    type(cred).__name__
                                ),
                                "WARNING"
                            )
                            continue

                        cred_id = cred.get('id')
                        if not cred_id:
                            self.log(
                                "V1 credential type '{0}' "
                                "entry {1}/{2} has no 'id' "
                                "field, skipping".format(
                                    cred_type, cred_index,
                                    len(credentials_list)
                                ),
                                "WARNING"
                            )
                            continue

                        cred_description = cred.get(
                            'description', ''
                        )
                        cred_username = cred.get(
                            'username', ''
                        )
                        self._global_credentials_lookup[
                            cred_id
                        ] = {
                            "id": cred_id,
                            "description": cred_description,
                            "username": cred_username,
                            "credentialType": cred_type,
                            "comments": cred.get(
                                'comments', ''
                            ),
                            "instanceTenantId": cred.get(
                                'instanceTenantId', ''
                            ),
                            "instanceUuid": cred.get(
                                'instanceUuid', ''
                            )
                        }
                        self.log(
                            "V1 mapped credential {0}/{1} "
                            "in type '{2}': ID='{3}', "
                            "description='{4}', username="
                            "'{5}'".format(
                                cred_index,
                                len(credentials_list),
                                cred_type, cred_id,
                                cred_description,
                                cred_username
                            ),
                            "DEBUG"
                        )

                self.log(
                    "V1 API processing complete: {0} "
                    "total credential(s) mapped".format(
                        len(
                            self._global_credentials_lookup
                        )
                    ),
                    "INFO"
                )

        except Exception as e:
            self.log(
                "V1 API call failed with exception: "
                "{0}".format(str(e)),
                "WARNING"
            )
            self.log(
                "Exception type: {0}, attempting v2 "
                "fallback".format(type(e).__name__),
                "DEBUG"
            )
            self.msg = "Failed to retrieve global credentials using v1 API, error: {0}".format(str(e))
            self.set_operation_result("failed", False, self.msg, "WARNING").check_return_status()

            # Fallback: try v2 API if v1 returns empty results
            if not self._global_credentials_lookup:
                self.log(
                    "V1 API returned {0} credential(s), "
                    "attempting v2 fallback API".format(
                        len(self._global_credentials_lookup)
                    ),
                    "INFO"
                )
                try:
                    self.log(
                        "Calling v2 global credentials API: "
                        "family='discovery', function="
                        "'get_all_global_credentials_v2'",
                        "DEBUG"
                    )

                    headers = {}
                    alt_response = self.dnac._exec(
                        family="discovery",
                        function="get_all_global_credentials_v2",
                        params=headers
                    )

                    self.log(
                        "V2 API call completed, raw response "
                        "type: {0}".format(
                            type(alt_response).__name__
                            if alt_response is not None
                            else "None"
                        ),
                        "DEBUG"
                    )

                    if alt_response is None:
                        self.log(
                            "V2 API returned None response, "
                            "unable to retrieve credentials",
                            "WARNING"
                        )
                        alt_response_data = None
                    elif isinstance(alt_response, dict):
                        alt_response_data = alt_response.get(
                            "response"
                        )
                        self.log(
                            "V2 API returned dict, extracted "
                            "'response' key: type={0}, "
                            "is_none={1}".format(
                                type(alt_response_data).__name__
                                if alt_response_data is not None
                                else "None",
                                alt_response_data is None
                            ),
                            "DEBUG"
                        )

                        if alt_response_data is None:
                            self.log(
                                "V2 API dict contains None "
                                "'response' key, using full "
                                "dict as alt_response_data",
                                "DEBUG"
                            )
                            alt_response_data = alt_response
                    elif isinstance(alt_response, list):
                        self.log(
                            "V2 API returned list directly, "
                            "using as alt_response_data with "
                            "{0} entry(ies)".format(
                                len(alt_response)
                            ),
                            "DEBUG"
                        )
                        alt_response_data = alt_response
                    else:
                        self.log(
                            "V2 API returned unexpected type "
                            "{0}, treating as direct "
                            "alt_response_data".format(
                                type(alt_response).__name__
                            ),
                            "WARNING"
                        )
                        alt_response_data = alt_response

                    # Validate v2 response_data
                    if alt_response_data is None:
                        self.log(
                            "V2 API alt_response_data is None "
                            "after extraction, no credentials "
                            "available",
                            "WARNING"
                        )
                    elif not isinstance(alt_response_data, list):
                        self.log(
                            "V2 API alt_response_data is not a "
                            "list (type: {0}), expected list of "
                            "credentials".format(
                                type(alt_response_data).__name__
                            ),
                            "WARNING"
                        )
                        alt_response_data = None

                    # Process v2 response if valid
                    if (
                        alt_response_data is not None and
                        isinstance(alt_response_data, list)
                    ):
                        if len(alt_response_data) == 0:
                            self.log(
                                "V2 API returned empty list, no "
                                "credentials found in Catalyst "
                                "Center",
                                "WARNING"
                            )
                        else:
                            self.log(
                                "V2 API returned valid list with "
                                "{0} credential(s), "
                                "processing".format(
                                    len(alt_response_data)
                                ),
                                "INFO"
                            )

                            for cred_index, cred in enumerate(
                                alt_response_data, start=1
                            ):
                                if cred is None:
                                    self.log(
                                        "V2 credential entry "
                                        "{0}/{1} is None, "
                                        "skipping".format(
                                            cred_index,
                                            len(alt_response_data)
                                        ),
                                        "WARNING"
                                    )
                                    continue

                                if not isinstance(cred, dict):
                                    self.log(
                                        "V2 credential entry "
                                        "{0}/{1} is not a dict "
                                        "(type: {2}), "
                                        "skipping".format(
                                            cred_index,
                                            len(alt_response_data),
                                            type(cred).__name__
                                        ),
                                        "WARNING"
                                    )
                                    continue
                                cred_id = cred.get('id')
                                if not cred_id:
                                    self.log(
                                        "V2 credential entry "
                                        "{0}/{1} has no 'id' "
                                        "field, skipping".format(
                                            cred_index,
                                            len(alt_response_data)
                                        ),
                                        "WARNING"
                                    )
                                    continue

                                cred_description = cred.get(
                                    'description', ''
                                )
                                cred_username = cred.get(
                                    'username', ''
                                )
                                cred_type = cred.get(
                                    'credentialType', ''
                                )

                                self._global_credentials_lookup[
                                    cred_id
                                ] = {
                                    "id": cred_id,
                                    "description": (
                                        cred_description
                                    ),
                                    "username": cred_username,
                                    "credentialType": cred_type,
                                    "comments": cred.get(
                                        'comments', ''
                                    ),
                                    "instanceTenantId": cred.get(
                                        'instanceTenantId', ''
                                    ),
                                    "instanceUuid": cred.get(
                                        'instanceUuid', ''
                                    )
                                }
                                self.log(
                                    "V2 mapped credential "
                                    "{0}/{1}: ID='{2}', "
                                    "type='{3}', description="
                                    "'{4}', username='{5}'".format(
                                        cred_index,
                                        len(alt_response_data),
                                        cred_id, cred_type,
                                        cred_description,
                                        cred_username
                                    ),
                                    "DEBUG"
                                )
                            self.log(
                                "V2 API processing complete: "
                                "{0} total credential(s) "
                                "mapped".format(
                                    len(
                                        self
                                        ._global_credentials_lookup
                                    )
                                ),
                                "INFO"
                            )

                except (KeyError, TypeError, AttributeError) as alt_e:
                    self.log(
                        "V2 API call failed with exception: "
                        "{0}".format(str(alt_e)),
                        "WARNING"
                    )
                    self.log(
                        "V2 exception type: {0}, no "
                        "credentials available from either "
                        "API".format(type(alt_e).__name__),
                        "DEBUG"
                    )

                    if alt_response_data and isinstance(alt_response_data, list):
                        self.log(f"V2 API returned {len(alt_response_data)} credentials", "DEBUG")
                        for cred in alt_response_data:
                            if isinstance(cred, dict) and cred.get('id'):
                                cred_id = cred.get('id')
                                cred_description = cred.get('description', '')
                                cred_username = cred.get('username', '')
                                cred_type = cred.get('credentialType', '')

                                self._global_credentials_lookup[cred_id] = {
                                    "id": cred_id,
                                    "description": cred_description,
                                    "username": cred_username,
                                    "credentialType": cred_type,
                                    "comments": cred.get('comments', ''),
                                    "instanceTenantId": cred.get('instanceTenantId', ''),
                                    "instanceUuid": cred.get('instanceUuid', '')
                                }
                                self.log(
                                    f"V2_CREDENTIAL_MAPPING: ID={cred_id} -> Type={cred_type}, "
                                    f"Description='{cred_description}', Username='{cred_username}'",
                                    "INFO"
                                )
        except (ImportError, ValueError) as e:  # pylint: disable=bad-except-order
            self.log(f"Error retrieving global credentials: {str(e)}", "WARNING")
            self._global_credentials_lookup = {}

        # Final validation
        if not self._global_credentials_lookup:
            self.log(
                "Both v1 and v2 APIs failed to return "
                "credentials, returning empty lookup "
                "table",
                "WARNING"
            )
        else:
            self.log(
                "Global credentials lookup built "
                "successfully with {0} credential "
                "ID(s) from {1} API".format(
                    len(self._global_credentials_lookup),
                    "v1" if len(
                        self._global_credentials_lookup
                    ) > 0 else "v2"
                ),
                "INFO"
            )

        return self._global_credentials_lookup

    def transform_global_credential_id_to_description(self, cred_id):
        """
        Transform global credential ID to credential description.

        Args:
            cred_id (str): Global credential ID

        Returns:
            str: Credential description or original ID if not found
        """
        self.log(f"Transforming credential ID to description with params: cred_id={cred_id}", "DEBUG")

        if not cred_id:
            self.log("Credential ID is empty or None, returning None", "DEBUG")
            return None

        lookup = self.get_global_credentials_lookup()
        cred_info = lookup.get(cred_id, {})
        description = cred_info.get('description')

        if not description:
            self.log(f"Could not find description for credential ID: {cred_id}, returning original ID", "WARNING")
            self.log(f"Returning credential ID: {cred_id}", "DEBUG")
            return cred_id

        self.log(f"Mapped credential ID {cred_id} to description: {description}", "DEBUG")
        self.log(f"Returning description: {description}", "DEBUG")
        return description

    def transform_global_credential_id_to_username(self, cred_id):
        """
        Transform global credential ID to credential username.

        Args:
            cred_id (str): Global credential ID

        Returns:
            str: Credential username or None if not found
        """
        self.log(f"Transforming credential ID to username with params: cred_id={cred_id}", "DEBUG")

        if not cred_id:
            self.log("Credential ID is empty or None, returning None", "DEBUG")
            return None

        lookup = self.get_global_credentials_lookup()
        cred_info = lookup.get(cred_id, {})
        username = cred_info.get('username')

        if not username:
            self.log(f"Could not find username for credential ID: {cred_id}", "DEBUG")
            return None

        self.log(f"Mapped credential ID {cred_id} to username: {username}", "DEBUG")
        self.log(f"Returning username: {username}", "DEBUG")
        return username

    def transform_global_credentials_list(self, discovery_data):
        """
        Transform global credential ID lists to credential descriptions and usernames.
        Maps credential IDs to their proper names and usernames for playbook generation.

        Args:
            discovery_data (dict): Discovery configuration data

        Returns:
            dict: Transformed global credentials structure compatible with discovery_workflow_manager
        """
        self.log(f"Transforming global credentials list with params: discovery_data keys={list(discovery_data.keys()) if discovery_data else None}", "DEBUG")

        if not discovery_data or not isinstance(discovery_data, dict):
            self.log("Discovery data is empty or not a dictionary, returning empty dict", "DEBUG")
            return {}

        global_cred_ids = discovery_data.get('globalCredentialIdList', [])
        if not global_cred_ids:
            self.log("No global credential IDs found in discovery data, returning empty dict", "DEBUG")
            return {}

        self.log(f"Transforming {len(global_cred_ids)} global credential IDs", "DEBUG")

        # Group credentials by type - using the same structure as discovery_workflow_manager
        credentials = {
            "cli_credentials_list": [],
            "http_read_credential_list": [],
            "http_write_credential_list": [],
            "snmp_v2_read_credential_list": [],
            "snmp_v2_write_credential_list": [],
            "snmp_v3_credential_list": []
        }

        lookup = self.get_global_credentials_lookup()
        self.log(f"Available credential IDs in lookup: {list(lookup.keys())}", "DEBUG")
        self.log(f"Discovery credential IDs to transform: {global_cred_ids}", "DEBUG")

        for idx, cred_id in enumerate(global_cred_ids):
            self.log(f"Processing credential at index {idx}: {cred_id}", "DEBUG")
            cred_info = lookup.get(cred_id, {})
            cred_type = cred_info.get('credentialType', '')
            description = cred_info.get('description', cred_id)
            username = cred_info.get('username', '')

            self.log(f"TRANSFORM_DEBUG: Processing credential ID {cred_id}", "DEBUG")
            self.log(f"TRANSFORM_DEBUG: Found info: {cred_info}", "DEBUG")

            # Skip credentials without proper description (still showing IDs)
            if description == cred_id and not cred_info:
                self.log(f"CREDENTIAL_NOT_FOUND: ID={cred_id} not found in lookup table, skipping", "WARNING")
                continue

            # Build credential entry, excluding username if it's empty
            cred_entry = {"description": description}
            if username:  # Only include username if it's not empty
                cred_entry["username"] = username

            self.log(f"CREDENTIAL_TRANSFORM: ID={cred_id} -> Entry={cred_entry}, Type='{cred_type}'", "INFO")

            # Map credential types based on API field names (same as discovery_workflow_manager.py)
            if cred_type == 'cliCredential':
                credentials["cli_credentials_list"].append(cred_entry)
                self.log(f"MAPPED_TO: cli_credentials_list - {description}", "DEBUG")
                continue

            if cred_type == 'httpsRead':
                credentials["http_read_credential_list"].append(cred_entry)
                self.log(f"MAPPED_TO: http_read_credential_list - {description}", "DEBUG")
                continue

            if cred_type == 'httpsWrite':
                credentials["http_write_credential_list"].append(cred_entry)
                self.log(f"MAPPED_TO: http_write_credential_list - {description}", "DEBUG")
                continue

            if cred_type == 'snmpV2cRead':
                credentials["snmp_v2_read_credential_list"].append(cred_entry)
                self.log(f"MAPPED_TO: snmp_v2_read_credential_list - {description}", "DEBUG")
                continue

            if cred_type == 'snmpV2cWrite':
                credentials["snmp_v2_write_credential_list"].append(cred_entry)
                self.log(f"MAPPED_TO: snmp_v2_write_credential_list - {description}", "DEBUG")
                continue

            if cred_type == 'snmpV3':
                credentials["snmp_v3_credential_list"].append(cred_entry)
                self.log(f"MAPPED_TO: snmp_v3_credential_list - {description}", "DEBUG")
                continue

            cred_type_upper = cred_type.upper()
            self.log(f"FALLBACK_MAPPING: Processing unknown cred_type='{cred_type}' (upper='{cred_type_upper}') for ID={cred_id}", "DEBUG")

            if 'CLI' in cred_type_upper or cred_type_upper == 'GLOBAL':
                credentials["cli_credentials_list"].append(cred_entry)
                self.log(f"FALLBACK_MAPPED_TO: cli_credentials_list (CLI/GLOBAL match) - {description}", "DEBUG")
                continue

            if 'HTTP_READ' in cred_type_upper or 'HTTPS_READ' in cred_type_upper:
                credentials["http_read_credential_list"].append(cred_entry)
                self.log(f"FALLBACK_MAPPED_TO: http_read_credential_list (HTTP_READ match) - {description}", "DEBUG")
                continue

            if 'HTTP_WRITE' in cred_type_upper or 'HTTPS_WRITE' in cred_type_upper:
                credentials["http_write_credential_list"].append(cred_entry)
                self.log(f"FALLBACK_MAPPED_TO: http_write_credential_list (HTTP_WRITE match) - {description}", "DEBUG")
                continue

            if 'SNMPV2_READ' in cred_type_upper or 'SNMPv2_READ' in cred_type_upper:
                credentials["snmp_v2_read_credential_list"].append(cred_entry)
                self.log(f"FALLBACK_MAPPED_TO: snmp_v2_read_credential_list (SNMPV2_READ match) - {description}", "DEBUG")
                continue

            if 'SNMPV2_WRITE' in cred_type_upper or 'SNMPv2_WRITE' in cred_type_upper:
                credentials["snmp_v2_write_credential_list"].append(cred_entry)
                self.log(f"FALLBACK_MAPPED_TO: snmp_v2_write_credential_list (SNMPV2_WRITE match) - {description}", "DEBUG")
                continue

            if 'SNMPV3' in cred_type_upper or 'SNMPv3' in cred_type_upper:
                credentials["snmp_v3_credential_list"].append(cred_entry)
                self.log(f"FALLBACK_MAPPED_TO: snmp_v3_credential_list (SNMPV3 match) - {description}", "DEBUG")
                continue

            self.log(f"FALLBACK_DEFAULT: Unknown credential type '{cred_type}' for ID {cred_id}, defaulting to CLI - {description}", "INFO")
            credentials["cli_credentials_list"].append(cred_entry)

        # Remove empty credential lists to keep output clean
        credentials_before_filter = dict(credentials)
        credentials = {k: v for k, v in credentials.items() if v}

        self.log(f"TRANSFORM_SUMMARY: Input IDs count: {len(global_cred_ids)}", "INFO")
        self.log(f"TRANSFORM_SUMMARY: Credentials before filtering: {credentials_before_filter}", "DEBUG")
        self.log(f"TRANSFORM_SUMMARY: Final transformed credentials: {credentials}", "INFO")

        # Log summary by credential type
        for cred_type, cred_list in credentials.items():
            descriptions = [c.get('description', 'N/A') for c in cred_list]
            self.log(f"FINAL_{cred_type.upper()}: {len(cred_list)} entries - {descriptions}", "INFO")
            self.log(f"Returning transformed credentials with {len(credentials)} credential types", "DEBUG")
            return credentials if credentials else {}

        return credentials if credentials else {}

    def transform_ip_address_list(self, discovery_data):
        """
        Transform IP address list from discovery data.

        Args:
            discovery_data (dict): Discovery configuration data

        Returns:
            list: Formatted IP address list as individual elements
        """
        self.log(f"Transforming IP address list with params: discovery_data keys={list(discovery_data.keys()) if discovery_data else None}", "DEBUG")

        if not discovery_data or not isinstance(discovery_data, dict):
            self.log("Discovery data is empty or not a dictionary, returning empty list", "DEBUG")
            return []

        ip_list = discovery_data.get('ipAddressList', "")
        if isinstance(ip_list, str) and ip_list:
            result = [ip.strip() for ip in ip_list.split(',') if ip.strip()]
            self.log(f"Transformed string IP list to {len(result)} IP addresses", "DEBUG")
            self.log(f"Returning IP address list: {result}", "DEBUG")
            return result

        if isinstance(ip_list, list):
            result = [str(ip) for ip in ip_list if ip]
            self.log(f"Converted list of {len(result)} IP addresses to strings", "DEBUG")
            self.log(f"Returning IP address list: {result}", "DEBUG")
            return result

        self.log("IP address list is empty or invalid type, returning empty list", "DEBUG")
        return []

    def transform_ip_filter_list(self, discovery_data):
        """
        Transform IP filter list from discovery data.

        Args:
            discovery_data (dict): Discovery configuration data

        Returns:
            list: Formatted IP filter list as individual elements
        """
        self.log(f"Transforming IP filter list with params: discovery_data keys={list(discovery_data.keys()) if discovery_data else None}", "DEBUG")

        if not discovery_data or not isinstance(discovery_data, dict):
            self.log("Discovery data is empty or not a dictionary, returning empty list", "DEBUG")
            return []

        filter_list = discovery_data.get('ipFilterList', "")
        if isinstance(filter_list, str) and filter_list:
            result = [ip.strip() for ip in filter_list.split(',') if ip.strip()]
            self.log(f"Transformed string IP filter list to {len(result)} IP filters", "DEBUG")
            self.log(f"Returning IP filter list: {result}", "DEBUG")
            return result

        if isinstance(filter_list, list):
            result = [str(ip) for ip in filter_list if ip]
            self.log(f"Converted list of {len(result)} IP filters to strings", "DEBUG")
            self.log(f"Returning IP filter list: {result}", "DEBUG")
            return result

        self.log("IP filter list is empty or invalid type, returning empty list", "DEBUG")
        return []

    def transform_to_boolean(self, value):
        """
        Transform value to boolean, handling None and string values.

        Args:
            value: Value to transform to boolean

        Returns:
            bool or None: Boolean value or None if conversion not possible
        """
        self.log(f"Transforming value to boolean with params: value={value}, type={type(value).__name__}", "DEBUG")

        if value is None:
            self.log("Value is None, returning None", "DEBUG")
            return None

        if isinstance(value, bool):
            self.log(f"Value is already boolean: {value}", "DEBUG")
            return value

        if isinstance(value, str):
            result = value.lower() in ('true', '1', 'yes', 'on')
            self.log(f"Converted string '{value}' to boolean: {result}", "DEBUG")
            return result

        if isinstance(value, int):
            result = bool(value)
            self.log(f"Converted int {value} to boolean: {result}", "DEBUG")
            return result

        self.log(f"Cannot convert value of type {type(value).__name__} to boolean, returning None", "DEBUG")
        return None

    def discovery_reverse_mapping_function(self, requested_components=None):
        """
        Returns the reverse mapping specification for discovery configurations.

        Args:
            requested_components (list, optional): List of specific components to include

        Returns:
            dict: Reverse mapping specification for discovery details
        """
        self.log("Generating reverse mapping specification for discovery configurations.", "DEBUG")

        return OrderedDict({
            "discovery_name": {"type": "str", "source_key": "name"},
            "discovery_type": {"type": "str", "source_key": "discoveryType"},
            "ip_address_list": {
                "type": "list",
                "source_key": None,
                "special_handling": True,
                "transform": self.transform_ip_address_list
            },
            "ip_filter_list": {
                "type": "list",
                "source_key": None,
                "special_handling": True,
                "transform": self.transform_ip_filter_list
            },
            "global_credentials": {
                "type": "dict",
                "source_key": None,
                "special_handling": True,
                "transform": self.transform_global_credentials_list
            },
            "discovery_specific_credentials": {
                "type": "dict",
                "source_key": None,
                "special_handling": True,
                "transform": lambda x: {}  # Exclude for security
            },
            "protocol_order": {"type": "str", "source_key": "protocolOrder"},
            "cdp_level": {"type": "int", "source_key": "cdpLevel"},
            "lldp_level": {"type": "int", "source_key": "lldpLevel"},
            "preferred_mgmt_ip_method": {"type": "str", "source_key": "preferredMgmtIPMethod"},
            "use_global_credentials": {
                "type": "bool",
                "source_key": None,
                "special_handling": True,
                "transform": lambda x: True  # Default assumption
            },
            "snmp_version": {"type": "str", "source_key": "snmpVersion"},
            "timeout": {"type": "int", "source_key": "timeout"},
            "retry": {"type": "int", "source_key": "retry"},
            # Status and administrative fields (read-only)
            "discovery_condition": {"type": "str", "source_key": "discoveryCondition"},
            "discovery_status": {"type": "str", "source_key": "discoveryStatus"},
            "is_auto_cdp": {
                "type": "bool",
                "source_key": "isAutoCdp",
                "transform": self.transform_to_boolean
            }
        })

    def get_discoveries_data(self, global_filters=None, component_specific_filters=None):
        """
        Retrieve discovery configurations from Cisco Catalyst Center.

        Args:
            global_filters (dict, optional): Global filters to apply
            component_specific_filters (dict, optional): Component-specific filters

        Returns:
            list: List of discovery configurations
        """
        self.log(f"Retrieving discoveries data with params: global_filters={global_filters}, component_specific_filters={component_specific_filters}", "DEBUG")

        self.log(f"Retrieving discoveries data with params: global_filters={global_filters}, component_specific_filters={component_specific_filters}", "DEBUG")

        all_discoveries = []
        start_index = 1
        records_to_return = 500
        total_count = None

        try:
            while True:
                self.log(f"Fetching discoveries: start_index={start_index}, records_to_return={records_to_return}", "DEBUG")

                try:
                    response = self.dnac._exec(
                        family="discovery",
                        function='get_discoveries_by_range',
                        op_modifies=False,
                        params={"start_index": start_index, "records_to_return": records_to_return}
                    )
                except Exception as e:
                    self.log(f"Error calling get_discoveries_by_range API at start_index {start_index}: {str(e)}", "ERROR")
                    break

                if not response:
                    self.log(f"No response received from get_discoveries_by_range API at start_index {start_index}", "WARNING")
                    break

                discoveries_batch = response.get('response', [])

                if total_count is None:
                    total_count = response.get('totalCount', 0)
                    self.log(f"Total discoveries available in Catalyst Center: {total_count}", "INFO")

                if not discoveries_batch:
                    self.log(f"No discoveries in batch at start_index {start_index}, ending pagination", "DEBUG")
                    break

                batch_size = len(discoveries_batch)
                all_discoveries.extend(discoveries_batch)
                self.log(f"Retrieved {batch_size} discoveries in current batch, total so far: {len(all_discoveries)}", "DEBUG")

                if len(all_discoveries) >= total_count:
                    self.log(f"Retrieved all {len(all_discoveries)} discoveries, ending pagination", "INFO")
                    break

                if batch_size < records_to_return:
                    self.log(f"Batch size {batch_size} less than requested {records_to_return}, ending pagination", "DEBUG")
                    break

                start_index += records_to_return

            self.log(f"Retrieved {len(all_discoveries)} total discoveries", "INFO")
            if not all_discoveries:
                self.log("No discoveries found in Catalyst Center", "INFO")
                return []

            self.log(f"Retrieved {len(all_discoveries)} total discoveries from Catalyst Center", "INFO")

            filtered_discoveries = self.apply_global_filters(all_discoveries, global_filters)

            if not filtered_discoveries:
                self.log("No discoveries matched the global filters", "INFO")
                return []

            self.log(f"After global filtering: {len(filtered_discoveries)} discoveries remain", "INFO")

            final_discoveries = self.apply_component_filters(filtered_discoveries, component_specific_filters)

            if not final_discoveries:
                self.log("No discoveries matched the component filters", "INFO")
                return []

            self.log(f"After component filtering: {len(final_discoveries)} discoveries remain", "INFO")
            self.log(f"Returning {len(final_discoveries)} filtered discoveries", "DEBUG")
            return final_discoveries

        except Exception as e:
            self.log(f"Error retrieving discoveries data: {str(e)}", "ERROR")
            return []

    def apply_global_filters(self, discoveries, global_filters):
        """
        Apply global filters to the list of discoveries.

        Args:
            discoveries (list): List of discovery configurations
            global_filters (dict, optional): Global filters to apply

        Returns:
            list: Filtered list of discoveries
        """
        self.log(f"Applying global filters with params: total_discoveries={len(discoveries)}, filters={global_filters}", "DEBUG")

        if not global_filters:
            self.log("No global filters provided, returning all discoveries", "DEBUG")
            return discoveries

        filtered_discoveries = discoveries

        # Filter by discovery names (highest priority)
        discovery_name_list = global_filters.get('discovery_name_list', [])
        discovery_type_list = global_filters.get('discovery_type_list', [])
        if discovery_name_list:
            self.log(f"Filtering by discovery names: {discovery_name_list}", "DEBUG")
            filtered_discoveries = [
                discovery for discovery in filtered_discoveries
                if discovery.get('name') in discovery_name_list
            ]
            self.log(f"After name filtering: {len(filtered_discoveries)} discoveries", "DEBUG")
            # Log which discoveries were found by name
            found_names = [d.get('name') for d in filtered_discoveries]
            self.log(f"Found discoveries by name: {found_names}", "DEBUG")

        # Filter by discovery types (only if names not provided)
        elif discovery_type_list:
            self.log(f"Filtering by discovery types: {discovery_type_list}", "DEBUG")
            filtered_discoveries = [
                discovery for discovery in filtered_discoveries
                if discovery.get('discoveryType') in discovery_type_list
            ]
            self.log(f"After type filtering: {len(filtered_discoveries)} discoveries", "DEBUG")
            # Log which discoveries were found by type
            found_types = [d.get('discoveryType') for d in filtered_discoveries]
            self.log(f"Found discoveries by type: {found_types}", "DEBUG")

        self.log(f"Final filtered discoveries count: {len(filtered_discoveries)}", "INFO")
        return filtered_discoveries

    def apply_component_filters(self, discoveries, component_specific_filters):
        """
        Apply component-specific filters to discovery list.
        Filters discoveries based on component list and discovery-specific criteria.

        Args:
            discoveries (list): List of discovery configurations
            component_specific_filters (dict, optional): Component-specific filters

        Returns:
            list: Filtered list of discoveries
        """
        self.log(f"Applying component filters with params: total_discoveries={len(discoveries)}, filters={component_specific_filters}", "DEBUG")

        if not component_specific_filters:
            self.log("No component filters provided, returning all discoveries", "DEBUG")
            return discoveries

        filtered_discoveries = discoveries

        # Filter by discovery status
        status_filter = component_specific_filters.get('discovery_status_filter')
        if status_filter:
            self.log(f"Filtering by discovery status: {status_filter}", "DEBUG")
            filtered_discoveries = [
                discovery for discovery in filtered_discoveries
                if discovery.get('discoveryCondition') in status_filter
            ]
            self.log(f"After status filtering: {len(filtered_discoveries)} discoveries", "DEBUG")

        return filtered_discoveries

    def generate_yaml_header_comments(self, discoveries_data):
        """
        Generate header comments for the YAML playbook file.

        Builds a summary block that includes Catalyst Center host
        info, generation timestamp, discovery type breakdown,
        IP range counts, and credential type usage. This header
        is prepended to the generated YAML file for documentation.

        Args:
            discoveries_data (list): List of discovery
                configuration dicts retrieved from Catalyst
                Center. Each dict should contain keys like
                'discoveryType', 'ipAddressList', and
                'globalCredentialIdList'.

        Returns:
            str: Multi-line header comment string to prepend
                to the generated YAML file.

        Notes:
            - Malformed (non-dict) entries in discoveries_data
            are skipped with a warning log.
            - If ipAddressList is None or empty, it contributes
            zero to the IP range count.
        """
        self.log(f"Generating YAML header comments with params: total_discoveries={len(discoveries_data)}", "DEBUG")
        # Get Catalyst Center host information
        dnac_host = self.params.get('dnac_host', 'Unknown')
        dnac_version = self.params.get('dnac_version', 'Unknown')

        # Generate summary statistics
        discovery_types = {}
        ip_ranges_count = 0
        credential_types = set()

        for idx, discovery in enumerate(discoveries_data):
            self.log(
                "Processing discovery index={0} for header "
                "summary, discovery={1}".format(
                    idx, discovery.get('name', 'Unknown')
                    if isinstance(discovery, dict)
                    else 'Invalid entry'
                ),
                "DEBUG"
            )
            # Count discovery types
            if not isinstance(discovery, dict):
                self.log(
                    "Skipping non-dict discovery entry at "
                    "index={0} during header generation".format(
                        idx
                    ),
                    "WARNING"
                )
                continue
            disc_type = discovery.get('discoveryType', 'Unknown')
            discovery_types[disc_type] = discovery_types.get(disc_type, 0) + 1

            # Count IP ranges
            ip_ranges = discovery.get('ipAddressList', [])
            if ip_ranges:
                if isinstance(ip_ranges, str):
                    ip_ranges_count += len(ip_ranges.split(','))
                elif isinstance(ip_ranges, list):
                    ip_ranges_count += len(ip_ranges)

            # Collect credential types
            if discovery.get('globalCredentialIdList'):
                credential_types.add('Global Credentials')
            if discovery.get('discoverySpecificCredentials'):
                credential_types.add('Discovery Specific Credentials')

        # Build header comments
        timestamp = datetime.datetime.now().strftime(
            '%Y-%m-%d %H:%M:%S'
        )
        header = [
            "# Generated Discovery Playbook Configuration",
            "# =========================================",
            "#",
            "# Source Catalyst Center: {0}".format(
                dnac_host
            ),
            "# Catalyst Center Version: {0}".format(
                dnac_version
            ),
            "# Generated on: {0}".format(timestamp),
            "#",
            "# Configuration Summary:",
            "# - Total Discoveries: {0}".format(
                len(discoveries_data)
            ),
            "# - Total IP Ranges: {0}".format(
                ip_ranges_count
            ),
        ]

        header.extend([
            "#",
            "# Compatible with the "
            "'discovery_workflow_manager' module.",
            "# Use this playbook to recreate or manage "
            "discovery configurations.",
            "#",
        ])

        if discovery_types:
            header.append("# - Discovery Types:")
            for disc_type, count in discovery_types.items():
                header.append(f"#   - {disc_type}: {count}")

        if credential_types:
            header.append("# - Credential Types: {0}".format(', '.join(sorted(credential_types))))

        result = '\n'.join(header)
        self.log(
            "YAML header comments generated successfully "
            "with total_lines={0}".format(len(header)),
            "DEBUG"
        )

        return result

    def write_yaml_with_comments(self, yaml_data, file_path, header_comments):
        """
        Write YAML data to a file with header comments prepended.

        Combines the generated header comments with the YAML
        configuration data and writes the result to the
        specified file path. Creates parent directories if
        they do not exist.

        Args:
            yaml_data (str): The YAML-formatted configuration
                string to write.
            file_path (str): Absolute or relative path where
                the YAML file will be saved.
            header_comments (str): Multi-line comment string
                to prepend to the YAML content.

        Returns:
            dict: A dictionary containing:
                - "status" (str): "success" or "failed".
                - "file_path" (str): The resolved file path.
                - "error" (str): Error message if failed.
        """
        self.log(
            "Writing YAML configuration to "
            "file_path={0}, yaml_data_length={1}, "
            "header_comments_length={2}".format(
                file_path,
                len(yaml_data) if yaml_data else 0,
                len(header_comments)
                if header_comments else 0
            ),
            "DEBUG"
        )

        if not yaml_data:
            self.log(
                "No YAML data provided to write — "
                "skipping file creation for "
                "file_path={0}".format(file_path),
                "WARNING"
            )
            return {
                "status": "failed",
                "file_path": file_path,
                "error": "No YAML data provided"
            }

        if not file_path:
            self.log(
                "No file path specified — cannot write "
                "YAML configuration",
                "ERROR"
            )
            return {
                "status": "failed",
                "file_path": file_path,
                "error": "No file path specified"
            }

        try:
            # Validate YAML library is available
            if not HAS_YAML:
                self.log("YAML library not available - cannot generate YAML file", "ERROR")
                return {
                    "status": "failed",
                    "file_path": file_path,
                    "error": "YAML library not available"
                }

            # Configure YAML dumper to avoid Python object references
            yaml.add_representer(OrderedDict, lambda dumper, data: dumper.represent_dict(data.items()))

            # Convert OrderedDict to regular dict to avoid Python object serialization
            def convert_ordereddict(obj):
                if isinstance(obj, OrderedDict):
                    return dict(obj)
                elif isinstance(obj, list):
                    return [convert_ordereddict(item) for item in obj]
                elif isinstance(obj, dict):
                    return {key: convert_ordereddict(value) for key, value in obj.items()}
                return obj

            clean_data = convert_ordereddict(yaml_data)

            # Generate clean YAML content
            yaml_content = yaml.dump(
                clean_data,
                default_flow_style=False,
                sort_keys=False,
                indent=2,
                allow_unicode=True
            )

            # Combine header comments with YAML content
            full_content = header_comments + '\n\n' + yaml_content

            # Write to file
            with open(file_path, 'w', encoding='utf-8') as file:
                file.write(full_content)

            self.log(f"Successfully wrote YAML file with comments: {file_path}", "DEBUG")
            return True

        except Exception as e:
            self.log(f"Error writing YAML file with comments: {str(e)}", "ERROR")
            return False

    def get_diff_gathered(self, config):
        """
        Orchestrate the gathering of discovery configurations
        and generation of a YAML playbook file.

        Reads the provided config filters, fetches all matching
        discoveries from Catalyst Center, transforms them into
        playbook-compatible YAML structures, and writes the
        result to a file.

        Args:
            config (dict): A single config entry containing:
                - generate_all_configurations (bool): Whether
                to include all discoveries.
                - file_path (str): Output file path. If not
                provided, a default timestamped path is used.
                - global_filters (dict): Filters by discovery
                name or type.
                - component_specific_filters (dict): Filters
                for specific discovery components.

        Returns:
            self: Returns the instance with updated self.result
                containing status, file_path, and summary of
                processed discoveries.

        Notes:
            - Returns early with a "no_data" status if no
            discoveries match the specified filters.
            - Skips individual discoveries that fail
            transformation and logs a warning.
        """
        self.log("Starting discovery playbook generation", "INFO")

        config = self.config[0] if self.config else {}

        # Determine file path
        file_path = config.get('file_path')

        if not file_path:
            self.log(
                "No file_path parameter provided by user, generating default filename "
                "with timestamp for uniqueness",
                "DEBUG"
            )
            file_path = self.generate_filename()
            self.log(
                "Auto-generated file path: {0}".format(file_path),
                "INFO"
            )
        else:
            # Validate file_path is a string
            if not isinstance(file_path, str):
                error_msg = (
                    "Invalid file_path parameter - expected str, got {0}. "
                    "Cannot proceed with YAML generation.".format(
                        type(file_path).__name__
                    )
                )
                self.log(error_msg, "ERROR")
                self.msg = {
                    "message": "YAML config generation failed for module '{0}' - invalid file_path parameter.".format(
                        self.module_name
                    ),
                    "error": error_msg
                }
                self.set_operation_result("failed", False, self.msg, "ERROR")
                return self

            self.log(
                "Using user-provided file path for YAML output: {0}".format(file_path),
                "INFO"
            )

            # Validate file path is writable
            directory = os.path.dirname(file_path)
            if directory and not os.path.exists(directory):
                self.log(
                    "Output directory does not exist: {0}. Attempting to create it.".format(
                        directory
                    ),
                    "WARNING"
                )
                try:
                    os.makedirs(directory, exist_ok=True)
                    self.log(
                        "Successfully created output directory: {0}".format(directory),
                        "INFO"
                    )
                except Exception as e:
                    error_msg = "Failed to create output directory: {0}. Error: {1}".format(
                        directory, str(e)
                    )
                    self.log(error_msg, "ERROR")
                    self.msg = {
                        "message": "YAML config generation failed for module '{0}' - cannot create output directory.".format(
                            self.module_name
                        ),
                        "error": error_msg
                    }
                    self.set_operation_result("failed", False, self.msg, "ERROR")
                    return self

        # Get filters
        global_filters = config.get('global_filters', {})
        component_specific_filters = config.get('component_specific_filters', {})

        # Handle generate_all_configurations flag
        if config.get('generate_all_configurations', False):
            global_filters = {}  # No filtering when generating all
            self.log("Generate all configurations enabled - including all discoveries", "INFO")
        else:
            # Validate that filters are provided when generate_all_configurations is False
            if not global_filters and not component_specific_filters:
                self.result["response"] = {
                    "status": "validation_error",
                    "message": "Component filters are required when 'generate_all_configurations' is set to false. "
                              "Please provide either 'global_filters' or 'component_specific_filters' to specify which discoveries to include."
                }
                self.msg = "Validation failed: Component filters required when generate_all_configurations=false"
                self.log(self.msg, "ERROR")
                self.status = "failed"
                return self

        # Get discovery data
        discoveries_data = self.get_discoveries_data(global_filters, component_specific_filters)

        if not discoveries_data:
            self.result["response"] = {
                "status": "no_data",
                "message": "No discoveries found matching the specified criteria"
            }
            self.msg = "No discoveries found to generate configuration"
            self.log(self.msg, "WARNING")
            return self

        # Generate reverse mapping
        reverse_mapping_spec = self.discovery_reverse_mapping_function()

        # Process credential inclusion settings
        include_credentials = component_specific_filters.get('include_credentials', True)
        include_global_credentials = component_specific_filters.get('include_global_credentials', True)

        if not include_credentials:
            # Remove credential-related fields
            reverse_mapping_spec.pop('global_credentials', None)
            reverse_mapping_spec.pop('discovery_specific_credentials', None)
            self.log("Credential information excluded from configuration", "INFO")
        elif not include_global_credentials:
            reverse_mapping_spec.pop('global_credentials', None)
            self.log("Global credential information excluded from configuration", "INFO")

        # Transform discovery data
        discovery_details = self.modify_parameters(reverse_mapping_spec, discoveries_data)

        # Build final YAML structure matching discovery_workflow_manager format
        yaml_data = {
            "config": discovery_details
        }

        # Generate header comments
        header_comments = self.generate_yaml_header_comments(discoveries_data)

        # Write YAML file with comments
        success = self.write_yaml_with_comments(yaml_data, file_path, header_comments)

        if success:
            self.result["response"] = {
                "status": "success",
                "file_path": file_path,
                "total_discoveries_processed": len(discoveries_data),
                "discoveries_found": [
                    {
                        "discovery_name": disc.get('name'),
                        "discovery_type": disc.get('discoveryType'),
                        "status": disc.get('discoveryCondition')
                    } for disc in discoveries_data
                ],
                "discoveries_skipped": [],
                "component_summary": {
                    "discovery_details": {
                        "total_processed": len(discoveries_data),
                        "total_successful": len(discovery_details),
                        "total_failed": 0
                    }
                }
            }
            self.msg = "Discovery YAML configuration generated successfully"
            self.status = "success"
            self.log(f"Discovery playbook generated successfully: {file_path}", "INFO")
        else:
            self.result["response"] = {
                "status": "failed",
                "error": "Failed to write YAML configuration file"
            }
            self.msg = "Error occurred during YAML generation"
            self.status = "failed"
            self.log("Failed to write discovery YAML configuration", "ERROR")

        return self


def main():
    """
    Main entry point for the Cisco Catalyst Center discovery playbook config generator module.

    This function serves as the primary execution entry point for the Ansible module,
    orchestrating the complete workflow from parameter collection to YAML playbook
    generation for discovery playbook configuration extraction.

    Purpose:
        Initializes and executes the discovery playbook config generator
        workflow to extract existing discovery configurations from Cisco Catalyst Center
        and generate Ansible-compatible YAML playbook files.

    Workflow Steps:
        1. Define module argument specification with required parameters
        2. Initialize Ansible module with argument validation
        3. Create DiscoveryPlaybookGenerator instance
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
        - Introduced APIs for discovery configuration retrieval:
            * Discovery Tasks (get_discovery_jobs_v1)
            * Discovery Credentials (get_global_credential_v2)
            * Discovery Types and Protocol Settings

    Supported States:
        - gathered: Extract existing discovery configurations and generate YAML playbook
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
        # Connection Parameters
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
            "no_log": True  # Prevents password logging for security
        },
        "dnac_verify": {
            "type": "bool",
            "default": True
        },
        # API Configuration Parameters
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
        # Logging Configuration Parameters
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
        # Playbook Configuration Parameters
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

    # Initialize the DiscoveryPlaybookGenerator object
    # This creates the main orchestrator for discovery playbook configuration extraction
    ccc_discovery_playbook_generator = DiscoveryPlaybookGenerator(module)

    # Log module initialization after object creation (now logging is available)
    ccc_discovery_playbook_generator.log(
        "Starting Ansible module execution for discovery playbook config "
        "generator at timestamp {0}".format(initialization_timestamp),
        "INFO"
    )

    ccc_discovery_playbook_generator.log(
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
    # Catalyst Center Version Storage and Compatibility Check
    # ============================================
    stored_ccc_version = ccc_discovery_playbook_generator.get_ccc_version()
    ccc_discovery_playbook_generator.log(
        "Storing Catalyst Center version: {0} for validation and comparison".format(
            stored_ccc_version
        ),
        "INFO"
    )

    ccc_discovery_playbook_generator.log(
        "Validating Catalyst Center version compatibility - checking if version {0} "
        "meets minimum requirement of 2.3.7.9 for discovery configuration APIs".format(
            stored_ccc_version
        ),
        "INFO"
    )

    if (
        ccc_discovery_playbook_generator.compare_dnac_versions(
            stored_ccc_version, "2.3.7.9"
        )
        < 0
    ):
        ccc_discovery_playbook_generator.log(
            "Version compatibility check failed - Catalyst Center version {0} does not "
            "meet minimum requirement of 2.3.7.9 for discovery configuration APIs".format(
                stored_ccc_version
            ),
            "ERROR"
        )

        ccc_discovery_playbook_generator.msg = (
            "The specified version '{0}' does not support the YAML Playbook generation "
            "for Discovery Module. Supported versions start from '2.3.7.9' onwards. "
            "Please upgrade your Catalyst Center to a supported version.".format(
                stored_ccc_version
            )
        )
        ccc_discovery_playbook_generator.set_operation_result(
            "failed", False, ccc_discovery_playbook_generator.msg, "ERROR"
        ).check_return_status()

    ccc_discovery_playbook_generator.log(
        "Version compatibility check passed - Catalyst Center version {0} supports "
        "all required discovery configuration APIs".format(
            stored_ccc_version
        ),
        "INFO"
    )

    # ============================================
    # State Parameter Validation
    # ============================================
    state = ccc_discovery_playbook_generator.params.get("state")

    ccc_discovery_playbook_generator.log(
        "Validating requested state parameter: '{0}' against supported states: {1}".format(
            state, ccc_discovery_playbook_generator.supported_states
        ),
        "DEBUG"
    )

    if state not in ccc_discovery_playbook_generator.supported_states:
        ccc_discovery_playbook_generator.log(
            "State validation failed - unsupported state '{0}' requested. "
            "Supported states: {1}".format(
                state, ccc_discovery_playbook_generator.supported_states
            ),
            "ERROR"
        )

        ccc_discovery_playbook_generator.status = "failed"
        ccc_discovery_playbook_generator.msg = "State '{0}' is not supported. Supported states: {1}".format(
            state, ccc_discovery_playbook_generator.supported_states
        )
        ccc_discovery_playbook_generator.result["msg"] = ccc_discovery_playbook_generator.msg
        ccc_discovery_playbook_generator.module.fail_json(**ccc_discovery_playbook_generator.result)

    ccc_discovery_playbook_generator.log(
        "State validation passed - using state '{0}' for workflow execution".format(
            state
        ),
        "INFO"
    )

    # ============================================
    # Input Parameter Validation
    # ============================================
    ccc_discovery_playbook_generator.log(
        "Starting comprehensive input parameter validation for playbook configuration",
        "INFO"
    )

    ccc_discovery_playbook_generator.validate_input().check_return_status()

    ccc_discovery_playbook_generator.log(
        "Input parameter validation completed successfully - all configuration "
        "parameters meet module requirements",
        "INFO"
    )

    # ============================================
    # Configuration Processing Loop
    # ============================================
    config_list = ccc_discovery_playbook_generator.config

    ccc_discovery_playbook_generator.log(
        "Starting configuration processing loop - will process {0} configuration "
        "item(s) from playbook".format(len(config_list)),
        "INFO"
    )

    for config_index, config in enumerate(config_list, start=1):
        ccc_discovery_playbook_generator.log(
            "Processing configuration item {0}/{1}: Starting discovery configuration "
            "extraction for item with keys: {2}".format(
                config_index, len(config_list), list(config.keys())
            ),
            "INFO"
        )

        # Process the gathered state directly

        ccc_discovery_playbook_generator.get_diff_gathered(config).check_return_status()

    # ============================================
    # Module Completion and Exit
    # ============================================
    module_end_time = time.time()
    module_duration = module_end_time - module_start_time

    completion_timestamp = time.strftime(
        "%Y-%m-%d %H:%M:%S",
        time.localtime(module_end_time)
    )

    ccc_discovery_playbook_generator.log(
        "Module execution completed successfully at timestamp {0}. Total execution "
        "time: {1:.2f} seconds. Processed {2} configuration item(s) with final "
        "status: {3}".format(
            completion_timestamp,
            module_duration,
            len(config_list),
            ccc_discovery_playbook_generator.status
        ),
        "INFO"
    )

    # Exit module with results
    # This is a terminal operation - function does not return after this
    ccc_discovery_playbook_generator.log(
        "Exiting Ansible module with result: {0}".format(
            ccc_discovery_playbook_generator.result
        ),
        "DEBUG"
    )

    module.exit_json(**ccc_discovery_playbook_generator.result)


if __name__ == "__main__":
    main()
