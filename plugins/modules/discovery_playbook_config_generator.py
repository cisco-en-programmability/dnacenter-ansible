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
- Enables complete infrastructure discovery through
  internal auto-discovery mode when C(config) is not
  provided.
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
  file_path:
    description:
      - Path where the YAML configuration file will be saved.
      - If not provided, a default filename is generated.
    type: str
    required: false
  file_mode:
    description:
      - File write mode for YAML output.
      - Relevant only when C(file_path) is provided.
    type: str
    required: false
    default: overwrite
    choices:
      - overwrite
      - append
  config:
    description:
      - A dictionary of filters for generating YAML playbook compatible with the 'discovery_workflow_manager'
        module.
      - If config is provided, C(global_filters) is mandatory.
      - If config is omitted, module runs in internal auto-discovery mode.
      - Global filters identify target discoveries by name or discovery type.
      - Component-specific filters remain supported internally.
    type: dict
    required: false
    suboptions:
      global_filters:
        description:
          - Global filters to apply when generating the YAML configuration file.
          - These filters identify which discovery tasks to extract configurations from.
          - Mandatory when C(config) is provided.
        type: dict
        required: true
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
              - Valid values are Single, Range, CDP, LLDP, CIDR.
              - Will include all discoveries matching any of the specified types.
              - Example ["CDP", "LLDP"]
            type: list
            elements: str
            required: false
            choices:
            - Single
            - Range
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
    file_path: "/tmp/specific_discoveries.yml"
    file_mode: overwrite
    config:
      global_filters:
        discovery_name_list:
          - "Multi_global"
          - "Single IP Discovery"
          - "CDP_Test_1"

# Generate configurations for specific discovery types with append mode
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
    file_path: "/tmp/cdp_lldp_discoveries.yml"
    file_mode: append
    config:
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
        "file_path": "/path/to/discovery_playbook_config_2026-01-24_12-33-20.yml",
        "total_discoveries_processed": 5,
        "discoveries_found": [
          {
            "discovery_name": "Multi_global",
            "discovery_type": "Range",
            "status": "Complete"
          },
          {
            "discovery_name": "Single IP Discovery",
            "discovery_type": "Single",
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
from collections import OrderedDict
from ansible.module_utils.basic import AnsibleModule
from ansible_collections.cisco.dnac.plugins.module_utils.dnac import (
    DnacBase,
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
        self.module_name = "discovery_workflow_manager"
        self.supported_states = ["gathered"]
        self._global_credentials_lookup = None
        self.valid_global_filter_keys = {"discovery_name_list", "discovery_type_list"}
        self.valid_discovery_types = {"Single", "Range", "CDP", "LLDP", "CIDR"}

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
                    "choices": ['Single', 'Range', 'CDP', 'LLDP', 'CIDR']
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

        config_provided = self.params.get("config") is not None
        if not config_provided:
            self.config = {}
            self.log(
                "Config not provided. Internal auto-discovery mode enabled.",
                "INFO"
            )

        # Expected schema for configuration parameters
        temp_spec = {
            "global_filters": {"type": "dict", "required": False},
        }

        # Step 1: Validate config is a dict and wrap in list for compatibility
        config_list = self.validate_config_dict(self.config, temp_spec)

        # Step 2: Validate that only allowed keys are present
        self.validate_invalid_params(self.config, temp_spec.keys())

        # Step 3: If config is provided, global_filters is mandatory
        if config_provided and not config_list.get("global_filters"):
            self.msg = (
                "Validation failed: global_filters is required when config is provided."
            )
            self.log(self.msg, "ERROR")
            self.status = "failed"
            return self.check_return_status()

        self.validate_global_filters_suboptions(self.config.get("global_filters"))

        self.log(
            "Input validation completed successfully for "
            "discovery playbook configuration",
            "INFO"
        )

        # Set the validated configuration and update the result with success status
        self.validated_config = config_list
        self.msg = "Successfully validated playbook configuration"
        self.set_operation_result("success", False, self.msg, "INFO")
        return self

    def validate_global_filters_suboptions(self, global_filters):
        """
        Validate supported keys and values under global_filters.

        Args:
            global_filters (dict): Global filters provided in input config.
        """
        if global_filters is None:
            return

        if not isinstance(global_filters, dict):
            self.fail_and_exit(
                "Invalid 'global_filters' value. Expected type 'dict', got '{0}'.".format(
                    type(global_filters).__name__
                )
            )

        invalid_keys = sorted(set(global_filters.keys()) - self.valid_global_filter_keys)
        if invalid_keys:
            self.fail_and_exit(
                "Invalid key(s) under 'global_filters': {0}. Valid keys are: {1}.".format(
                    invalid_keys, sorted(self.valid_global_filter_keys)
                )
            )

        discovery_name_list = global_filters.get("discovery_name_list")
        if discovery_name_list is not None:
            if not isinstance(discovery_name_list, list):
                self.fail_and_exit(
                    "Invalid 'global_filters.discovery_name_list' value. Expected type 'list', got '{0}'.".format(
                        type(discovery_name_list).__name__
                    )
                )
            invalid_names = [
                name for name in discovery_name_list
                if not isinstance(name, str) or not name.strip()
            ]
            if invalid_names:
                self.fail_and_exit(
                    "Invalid values under 'global_filters.discovery_name_list': {0}. "
                    "Only non-empty strings are allowed.".format(invalid_names)
                )

        discovery_type_list = global_filters.get("discovery_type_list")
        if discovery_type_list is not None:
            if not isinstance(discovery_type_list, list):
                self.fail_and_exit(
                    "Invalid 'global_filters.discovery_type_list' value. Expected type 'list', got '{0}'.".format(
                        type(discovery_type_list).__name__
                    )
                )

            invalid_types = [
                discovery_type for discovery_type in discovery_type_list
                if not isinstance(discovery_type, str)
                or discovery_type.strip() not in self.valid_discovery_types
            ]
            if invalid_types:
                self.fail_and_exit(
                    "Invalid values under 'global_filters.discovery_type_list': {0}. "
                    "Valid values are: {1}.".format(
                        invalid_types, sorted(self.valid_discovery_types)
                    )
                )

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
            "snmp_v3_credential_list": [],
            "net_conf_port_list": []
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

            if cred_type == 'netconfCredential':
                credentials["net_conf_port_list"].append(cred_entry)
                self.log(f"MAPPED_TO: net_conf_port_list - {description}", "DEBUG")
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

            if 'NETCONF' in cred_type_upper or 'NET_CONF' in cred_type_upper:
                credentials["net_conf_port_list"].append(cred_entry)
                self.log(f"FALLBACK_MAPPED_TO: net_conf_port_list (NETCONF match) - {description}", "DEBUG")
                continue

            self.log(f"FALLBACK_DEFAULT: Unknown credential type '{cred_type}' for ID {cred_id},"
                     f" skipping to avoid misclassification - {description}", "WARNING")
            # Do not default unknown credentials to CLI to prevent misclassification

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

    def transform_discovery_type(self, discovery_data):
        """
        Transform discovery type to workflow-manager compatible values.

        RANGE discoveries can represent either a single range or multiple
        ranges in Catalyst Center API response. The workflow manager expects
        these as RANGE and MULTI RANGE respectively.
        """
        if not discovery_data or not isinstance(discovery_data, dict):
            self.log("Discovery type transformation skipped - invalid or empty discovery data", "DEBUG")
            return None

        discovery_type = str(discovery_data.get("discoveryType", "")).strip()
        if not discovery_type:
            self.log("Discovery type field is absent or empty, skipping type transformation", "DEBUG")
            return None

        normalized_type = discovery_type.upper()
        if normalized_type == "RANGE":
            raw_ip_ranges = discovery_data.get("ipAddressList", "")
            if isinstance(raw_ip_ranges, str):
                range_items = [item.strip() for item in raw_ip_ranges.split(",") if item.strip()]
                if len(range_items) > 1:
                    self.log(
                        "RANGE with {0} IP ranges (str) detected, classifying as 'MULTI RANGE'".format(len(range_items)),
                        "DEBUG"
                    )
                    return "MULTI RANGE"
            elif isinstance(raw_ip_ranges, list):
                range_items = [item for item in raw_ip_ranges if item]
                if len(range_items) > 1:
                    self.log(
                        "RANGE with {0} IP ranges (list) detected, classifying as 'MULTI RANGE'".format(len(range_items)),
                        "DEBUG"
                    )
                    return "MULTI RANGE"
            self.log("Single IP range detected, classifying discovery as 'RANGE'", "DEBUG")
            return "RANGE"

        if normalized_type in {"SINGLE", "CDP", "LLDP", "CIDR"}:
            return normalized_type

        self.log(
            "Unrecognized discovery type '{0}' encountered, passing through without normalization".format(discovery_type),
            "WARNING"
        )

        return discovery_type

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
            "discovery_type": {
                "type": "str",
                "source_key": None,
                "special_handling": True,
                "transform": self.transform_discovery_type,
            },
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
            normalized_discovery_type_list = {
                discovery_type.strip().upper() for discovery_type in discovery_type_list
            }
            filtered_discoveries = [
                discovery for discovery in filtered_discoveries
                if str(discovery.get('discoveryType', '')).upper() in normalized_discovery_type_list
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

        config = self.config if isinstance(self.config, dict) else {}
        auto_discovery_mode = self.params.get("config") is None

        # Determine file mode
        file_mode = self.params.get('file_mode', 'overwrite')
        self.log(
            "File mode set to: {0}".format(file_mode),
            "DEBUG"
        )

        # Determine file path
        file_path = self.params.get('file_path')

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

        # Handle internal auto-discovery when config is omitted
        if auto_discovery_mode:
            global_filters = {}
            self.log("Auto-discovery mode enabled - including all discoveries", "INFO")
        else:
            # Validate that global_filters are provided when config is provided
            if not global_filters:
                self.result["response"] = {
                    "status": "validation_error",
                    "message": "global_filters is required when config is provided."
                }
                self.msg = "Validation failed: global_filters is required when config is provided."
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

        self.log(
            "Writing YAML for {0} discoveries to file '{1}' with mode '{2}'".format(
                len(discoveries_data), file_path, file_mode
            ),
            "INFO"
        )

        # Write YAML file using BrownFieldHelper shared header generation.
        success = self.write_dict_to_yaml(
            yaml_data,
            file_path,
            file_mode=file_mode,
        )

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
        "file_path": {
            "required": False,
            "type": "str",
        },
        "file_mode": {
            "required": False,
            "type": "str",
            "default": "overwrite",
            "choices": ["overwrite", "append"],
        },
        # Playbook Configuration Parameters
        "config": {
            "required": False,
            "type": "dict",
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

    config_params = module.params.get("config") or {}
    config_keys = list(config_params.keys()) if isinstance(config_params, dict) else []

    ccc_discovery_playbook_generator.log(
        "Module initialized with parameters: dnac_host={0}, dnac_port={1}, "
        "dnac_username={2}, dnac_verify={3}, dnac_version={4}, state={5}, "
        "config_keys={6}".format(
            module.params.get("dnac_host"),
            module.params.get("dnac_port"),
            module.params.get("dnac_username"),
            module.params.get("dnac_verify"),
            module.params.get("dnac_version"),
            module.params.get("state"),
            config_keys
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
    # Configuration Processing
    # ============================================
    config = ccc_discovery_playbook_generator.config

    ccc_discovery_playbook_generator.log(
        "Starting configuration processing for discovery playbook generation "
        "with keys: {0}".format(list(config.keys()) if isinstance(config, dict) else "N/A"),
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
        "time: {1:.2f} seconds. Final status: {2}".format(
            completion_timestamp,
            module_duration,
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
