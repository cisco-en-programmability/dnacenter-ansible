#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright (c) 2025, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

"""Ansible module to generate YAML configurations for Discovery Workflow Manager Module."""
from __future__ import absolute_import, division, print_function

__metaclass__ = type
__author__ = "Megha Kandari, Madhan Sankaranarayanan"

DOCUMENTATION = r"""
---
module: brownfield_discovery_playbook_generator
short_description: Generate YAML configurations playbook for 'discovery_workflow_manager' module.
description:
- Generates YAML configurations compatible with the 'discovery_workflow_manager'
  module, reducing the effort required to manually create Ansible playbooks and
  enabling programmatic modifications.
- The YAML configurations generated represent the discovery tasks and configurations
  deployed within the Cisco Catalyst Center.
- Supports extraction of discovery configurations including IP address ranges,
  credential mappings, discovery types, protocol orders, and discovery-specific settings.
version_added: 6.40.0
extends_documentation_fragment:
- cisco.dnac.workflow_manager_params
author:
- Megha Kandari (@mekandar)
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
          - This is useful for complete brownfield discovery infrastructure documentation.
          - Note - This will include all discovery tasks regardless of their current status.
        type: bool
        required: false
        default: false
      file_path:
        description:
          - Path where the YAML configuration file will be saved.
          - If not provided, the file will be saved in the current working directory with
            a default file name "discovery_workflow_manager_playbook_<DD_Mon_YYYY_HH_MM_SS_MS>.yml".
          - For example, "discovery_workflow_manager_playbook_22_Dec_2024_21_43_26_379.yml".
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
            choices: ['SINGLE', 'RANGE', 'MULTI RANGE', 'CDP', 'LLDP', 'CIDR']
      component_specific_filters:
        description:
          - Filters to specify which discovery components and features to include in the YAML configuration file.
          - Allows granular selection of specific features and their parameters.
          - If not specified, all supported discovery features will be extracted.
        type: dict
        required: false
        suboptions:
          components_list:
            description:
              - List of components to include in the YAML configuration file.
              - Valid values are ["discovery_details"]
              - If not specified, all supported components are included.
              - Future versions may support additional component types.
            type: list
            elements: str
            required: false
          include_credentials:
            description:
              - Whether to include credential information in the generated configuration.
              - When set to False, credential details will be excluded for security purposes.
              - When set to True, global credential references will be included but not passwords.
              - Discovery-specific credentials are never included due to security concerns.
            type: bool
            required: false
            default: true
          include_global_credentials:
            description:
              - Whether to include global credential mappings in the generated configuration.
              - When set to True, global credential descriptions and usernames are included.
              - Passwords and sensitive information are never included.
            type: bool
            required: false
            default: true
          discovery_status_filter:
            description:
              - Filter discoveries based on their current status.
              - Valid values are ["Complete", "In Progress", "Aborted", "Failed"]
              - If not specified, discoveries with all statuses will be included.
            type: list
            elements: str
            required: false
            choices: ["Complete", "In Progress", "Aborted", "Failed"]
requirements:
- dnacentersdk >= 2.10.10
- python >= 3.9
notes:
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
"""

EXAMPLES = r"""
# Generate YAML configurations for all discovery tasks
- name: Generate all discovery configurations
  cisco.dnac.brownfield_discovery_playbook_generator:
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
  cisco.dnac.brownfield_discovery_playbook_generator:
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
  cisco.dnac.brownfield_discovery_playbook_generator:
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

# Generate configurations with specific component filters
- name: Generate discovery configurations with component filtering
  cisco.dnac.brownfield_discovery_playbook_generator:
    dnac_host: "{{ dnac_host }}"
    dnac_username: "{{ dnac_username }}"
    dnac_password: "{{ dnac_password }}"
    dnac_verify: "{{ dnac_verify }}"
    dnac_port: "{{ dnac_port }}"
    dnac_version: "{{ dnac_version }}"
    dnac_debug: "{{ dnac_debug }}"
    state: gathered
    config:
      - file_path: "/tmp/filtered_discoveries.yml"
        component_specific_filters:
          components_list: ["discovery_details"]
          include_credentials: false
          discovery_status_filter: ["Complete"]

# Generate configurations excluding credential information
- name: Generate discovery configurations without credentials
  cisco.dnac.brownfield_discovery_playbook_generator:
    dnac_host: "{{ dnac_host }}"
    dnac_username: "{{ dnac_username }}"
    dnac_password: "{{ dnac_password }}"
    dnac_verify: "{{ dnac_verify }}"
    dnac_port: "{{ dnac_port }}"
    dnac_version: "{{ dnac_version }}"
    dnac_debug: "{{ dnac_debug }}"
    state: gathered
    config:
      - file_path: "/tmp/discoveries_no_creds.yml"
        component_specific_filters:
          include_credentials: false
          include_global_credentials: false
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
    A class for generating playbook files for discovery configurations deployed within the Cisco Catalyst Center using the GET APIs.
    """

    def __init__(self, module):
        super().__init__(module)
        self.module_name = "brownfield_discovery_playbook_generator"
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
                        "include_credentials": {
                            "type": "bool",
                            "description": "Include credential information"
                        },
                        "include_global_credentials": {
                            "type": "bool",
                            "description": "Include global credential mappings"
                        },
                        "discovery_status_filter": {
                            "type": "list",
                            "elements": "str",
                            "description": "Filter by discovery status",
                            "choices": ["Complete", "In Progress", "Aborted", "Failed"]
                        }
                    }
                }
            }
        }

    def validate_input(self):
        """
        Validates the input parameters for the discovery playbook generator.
        """
        self.log("Starting input validation for discovery playbook generator", "INFO")

        if not self.config:
            self.msg = "Configuration is required"
            self.log(self.msg, "ERROR")
            self.status = "failed"
            return self.check_return_status()

        # Validate state
        state = self.params.get("state")
        if state not in self.supported_states:
            self.msg = f"State '{state}' is not supported. Supported states: {self.supported_states}"
            self.log(self.msg, "ERROR")
            self.status = "failed"
            return self.check_return_status()

        # Validate configuration parameters
        for config_item in self.config:
            self.validate_params(config_item)

        self.log("Input validation completed successfully", "INFO")
        return self

    def get_global_credentials_lookup(self):
        """
        Create a lookup mapping of global credential IDs to their details.
        Uses the same approach as discovery_workflow_manager.py for consistency.

        Returns:
            dict: Mapping of credential IDs to credential information
        """
        if self._global_credentials_lookup is not None:
            return self._global_credentials_lookup

        self.log("Building global credentials lookup table", "INFO")
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

            # Extract response data
            response_data = response
            if isinstance(response, dict) and "response" in response:
                response_data = response.get("response")

            self.log(f"Global credentials API response type: {type(response_data)}", "DEBUG")
            self.log(f"Global credentials API response content: {response_data}", "DEBUG")

            if response_data and isinstance(response_data, dict):
                # Process different credential types
                credential_types = [
                    'cliCredential', 'snmpV2cRead', 'snmpV2cWrite',
                    'snmpV3', 'httpsRead', 'httpsWrite', 'netconfCredential'
                ]

                for cred_type in credential_types:
                    credentials_list = response_data.get(cred_type, [])
                    self.log(f"Processing {cred_type} credentials: found {len(credentials_list) if credentials_list else 0} entries", "DEBUG")
                    if credentials_list and isinstance(credentials_list, list):
                        for cred in credentials_list:
                            if isinstance(cred, dict) and cred.get('id'):
                                cred_id = cred.get('id')
                                cred_description = cred.get('description', '')
                                cred_username = cred.get('username', '')

                                self._global_credentials_lookup[cred_id] = {
                                    "id": cred_id,
                                    "description": cred_description,
                                    "username": cred_username,
                                    "credentialType": cred_type,  # Use the API field name as type
                                    "comments": cred.get('comments', ''),
                                    "instanceTenantId": cred.get('instanceTenantId', ''),
                                    "instanceUuid": cred.get('instanceUuid', '')
                                }
                                self.log(
                                    f"CREDENTIAL_MAPPING: ID={cred_id} -> Type={cred_type}, "
                                    f"Description='{cred_description}', Username='{cred_username}'",
                                    "INFO"
                                )

            # Fallback: try v2 API if v1 returns empty results
            if not self._global_credentials_lookup:
                self.log("Trying v2 global credentials API as fallback", "DEBUG")
                try:
                    alt_response = self.dnac._exec(
                        family="discovery",
                        function="get_all_global_credentials_v2",
                        params=headers
                    )

                    alt_response_data = alt_response
                    if isinstance(alt_response, dict) and "response" in alt_response:
                        alt_response_data = alt_response.get("response")

                    self.log(f"V2 API response: {alt_response_data}", "DEBUG")

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
                except Exception as alt_e:
                    self.log(f"V2 API also failed: {str(alt_e)}", "DEBUG")

        except Exception as e:
            self.log(f"Error retrieving global credentials: {str(e)}", "WARNING")
            # Log the full response for debugging if possible
            try:
                if 'response' in locals():
                    self.log(f"Full response that caused error: {response}", "DEBUG")
            except Exception:
                self.log("Could not log the problematic response", "DEBUG")
            self._global_credentials_lookup = {}

        self.log(f"Global credentials lookup built with {len(self._global_credentials_lookup)} entries", "INFO")
        return self._global_credentials_lookup

    def transform_global_credential_id_to_description(self, cred_id):
        """
        Transform global credential ID to credential description.

        Args:
            cred_id (str): Global credential ID

        Returns:
            str: Credential description or original ID if not found
        """
        if not cred_id:
            return None

        lookup = self.get_global_credentials_lookup()
        cred_info = lookup.get(cred_id, {})
        description = cred_info.get('description')

        if description:
            self.log(f"Mapped credential ID {cred_id} to description: {description}", "DEBUG")
            return description
        else:
            self.log(f"Could not find description for credential ID: {cred_id}", "WARNING")
            return cred_id

    def transform_global_credential_id_to_username(self, cred_id):
        """
        Transform global credential ID to credential username.

        Args:
            cred_id (str): Global credential ID

        Returns:
            str: Credential username or None if not found
        """
        if not cred_id:
            return None

        lookup = self.get_global_credentials_lookup()
        cred_info = lookup.get(cred_id, {})
        username = cred_info.get('username')

        if username:
            self.log(f"Mapped credential ID {cred_id} to username: {username}", "DEBUG")
            return username
        else:
            self.log(f"Could not find username for credential ID: {cred_id}", "DEBUG")
            return None

    def transform_global_credentials_list(self, discovery_data):
        """
        Transform global credential ID lists to credential descriptions and usernames.
        Maps credential IDs to their proper names and usernames for playbook generation.

        Args:
            discovery_data (dict): Discovery configuration data

        Returns:
            dict: Transformed global credentials structure compatible with discovery_workflow_manager
        """
        if not discovery_data or not isinstance(discovery_data, dict):
            return {}

        global_cred_ids = discovery_data.get('globalCredentialIdList', [])
        if not global_cred_ids:
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

        for cred_id in global_cred_ids:
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
            elif cred_type == 'httpsRead':
                credentials["http_read_credential_list"].append(cred_entry)
                self.log(f"MAPPED_TO: http_read_credential_list - {description}", "DEBUG")
            elif cred_type == 'httpsWrite':
                credentials["http_write_credential_list"].append(cred_entry)
                self.log(f"MAPPED_TO: http_write_credential_list - {description}", "DEBUG")
            elif cred_type == 'snmpV2cRead':
                credentials["snmp_v2_read_credential_list"].append(cred_entry)
                self.log(f"MAPPED_TO: snmp_v2_read_credential_list - {description}", "DEBUG")
            elif cred_type == 'snmpV2cWrite':
                credentials["snmp_v2_write_credential_list"].append(cred_entry)
                self.log(f"MAPPED_TO: snmp_v2_write_credential_list - {description}", "DEBUG")
            elif cred_type == 'snmpV3':
                credentials["snmp_v3_credential_list"].append(cred_entry)
                self.log(f"MAPPED_TO: snmp_v3_credential_list - {description}", "DEBUG")
            else:
                # Try to infer from description or fallback to CLI
                cred_type_upper = cred_type.upper()
                self.log(f"FALLBACK_MAPPING: Processing unknown cred_type='{cred_type}' (upper='{cred_type_upper}') for ID={cred_id}", "DEBUG")

                if 'CLI' in cred_type_upper or cred_type_upper == 'GLOBAL':
                    credentials["cli_credentials_list"].append(cred_entry)
                    self.log(f"FALLBACK_MAPPED_TO: cli_credentials_list (CLI/GLOBAL match) - {description}", "DEBUG")
                elif 'HTTP_READ' in cred_type_upper or 'HTTPS_READ' in cred_type_upper:
                    credentials["http_read_credential_list"].append(cred_entry)
                    self.log(f"FALLBACK_MAPPED_TO: http_read_credential_list (HTTP_READ match) - {description}", "DEBUG")
                elif 'HTTP_WRITE' in cred_type_upper or 'HTTPS_WRITE' in cred_type_upper:
                    credentials["http_write_credential_list"].append(cred_entry)
                    self.log(f"FALLBACK_MAPPED_TO: http_write_credential_list (HTTP_WRITE match) - {description}", "DEBUG")
                elif 'SNMPV2_READ' in cred_type_upper or 'SNMPv2_READ' in cred_type_upper:
                    credentials["snmp_v2_read_credential_list"].append(cred_entry)
                    self.log(f"FALLBACK_MAPPED_TO: snmp_v2_read_credential_list (SNMPV2_READ match) - {description}", "DEBUG")
                elif 'SNMPV2_WRITE' in cred_type_upper or 'SNMPv2_WRITE' in cred_type_upper:
                    credentials["snmp_v2_write_credential_list"].append(cred_entry)
                    self.log(f"FALLBACK_MAPPED_TO: snmp_v2_write_credential_list (SNMPV2_WRITE match) - {description}", "DEBUG")
                elif 'SNMPV3' in cred_type_upper or 'SNMPv3' in cred_type_upper:
                    credentials["snmp_v3_credential_list"].append(cred_entry)
                    self.log(f"FALLBACK_MAPPED_TO: snmp_v3_credential_list (SNMPV3 match) - {description}", "DEBUG")
                else:
                    # Default to CLI if type is unknown but we have valid description
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

        return credentials if credentials else {}

    def transform_ip_address_list(self, discovery_data):
        """
        Transform IP address list from discovery data.

        Args:
            discovery_data (dict): Discovery configuration data

        Returns:
            list: Formatted IP address list as individual elements
        """
        if not discovery_data or not isinstance(discovery_data, dict):
            return []

        ip_list = discovery_data.get('ipAddressList', "")
        if isinstance(ip_list, str) and ip_list:
            # Split comma-separated string into individual IP addresses/ranges
            return [ip.strip() for ip in ip_list.split(',') if ip.strip()]
        elif isinstance(ip_list, list):
            # Return list as-is, ensuring strings
            return [str(ip) for ip in ip_list if ip]
        else:
            return []

    def transform_ip_filter_list(self, discovery_data):
        """
        Transform IP filter list from discovery data.

        Args:
            discovery_data (dict): Discovery configuration data

        Returns:
            list: Formatted IP filter list as individual elements
        """
        if not discovery_data or not isinstance(discovery_data, dict):
            return []

        filter_list = discovery_data.get('ipFilterList', "")
        if isinstance(filter_list, str) and filter_list:
            # Split comma-separated string into individual IP addresses
            return [ip.strip() for ip in filter_list.split(',') if ip.strip()]
        elif isinstance(filter_list, list):
            # Return list as-is, ensuring strings
            return [str(ip) for ip in filter_list if ip]
        else:
            return []

    def transform_to_boolean(self, value):
        """
        Transform value to boolean, handling None and string values.

        Args:
            value: Value to transform to boolean

        Returns:
            bool or None: Boolean value or None if conversion not possible
        """
        if value is None:
            return None
        elif isinstance(value, bool):
            return value
        elif isinstance(value, str):
            return value.lower() in ('true', '1', 'yes', 'on')
        elif isinstance(value, int):
            return bool(value)
        else:
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
        self.log("Retrieving discovery configurations from Catalyst Center", "INFO")

        try:
            # Use execute_get_with_pagination helper function with proper parameter mapping
            # The discovery API expects 'startIndex' and 'recordsToReturn' parameters
            api_family = "discovery"
            api_function = "get_discoveries_by_range"

            # Base parameters - the pagination helper will add offset/limit
            # but we need to map them to startIndex/recordsToReturn for this specific API
            params = {}

            # Get all discoveries using manual pagination since discovery API has specific parameter names
            all_discoveries = []
            start_index = 1  # Discovery API starts from 1
            records_per_page = 500

            while True:
                # Build parameters specific to discovery API
                api_params = {
                    "start_index": start_index,
                    "records_to_return": records_per_page
                }

                self.log(f"Calling discovery API with startIndex={start_index}, recordsToReturn={records_per_page}", "DEBUG")

                response = self.dnac._exec(
                    family=api_family,
                    function=api_function,
                    params=api_params
                )

                discoveries = response.get("response", [])
                if not discoveries:
                    self.log("No more discoveries found, ending pagination", "DEBUG")
                    break

                all_discoveries.extend(discoveries)
                self.log(f"Retrieved {len(discoveries)} discoveries in this batch", "DEBUG")

                # If we got fewer than requested, we've reached the end
                if len(discoveries) < records_per_page:
                    self.log("Received fewer records than requested, ending pagination", "DEBUG")
                    break

                start_index += records_per_page

            self.log(f"Retrieved {len(all_discoveries)} total discoveries", "INFO")

            # Apply global filters
            filtered_discoveries = self.apply_global_filters(all_discoveries, global_filters)

            # Apply component-specific filters
            filtered_discoveries = self.apply_component_filters(filtered_discoveries, component_specific_filters)

            self.log(f"After filtering: {len(filtered_discoveries)} discoveries selected", "INFO")
            return filtered_discoveries

        except Exception as e:
            self.log(f"Error retrieving discovery data: {str(e)}", "ERROR")
            self.msg = f"Failed to retrieve discovery data: {str(e)}"
            self.status = "failed"
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
        if not global_filters:
            return discoveries

        filtered_discoveries = discoveries

        # Filter by discovery names (highest priority)
        discovery_name_list = global_filters.get('discovery_name_list')
        if discovery_name_list:
            self.log(f"Filtering by discovery names: {discovery_name_list}", "DEBUG")
            filtered_discoveries = [
                discovery for discovery in filtered_discoveries
                if discovery.get('name') in discovery_name_list
            ]
            self.log(f"After name filtering: {len(filtered_discoveries)} discoveries", "DEBUG")

        # Filter by discovery types (if names not provided)
        elif global_filters.get('discovery_type_list'):
            discovery_type_list = global_filters.get('discovery_type_list')
            self.log(f"Filtering by discovery types: {discovery_type_list}", "DEBUG")
            filtered_discoveries = [
                discovery for discovery in filtered_discoveries
                if discovery.get('discoveryType') in discovery_type_list
            ]
            self.log(f"After type filtering: {len(filtered_discoveries)} discoveries", "DEBUG")

        return filtered_discoveries

    def apply_component_filters(self, discoveries, component_specific_filters):
        """
        Apply component-specific filters to the list of discoveries.

        Args:
            discoveries (list): List of discovery configurations
            component_specific_filters (dict, optional): Component-specific filters

        Returns:
            list: Filtered list of discoveries
        """
        if not component_specific_filters:
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
        Generate header comments for the YAML file.

        Args:
            discoveries_data (list): List of discovery configurations

        Returns:
            str: Header comments to be added to the YAML file
        """
        import datetime

        # Get Catalyst Center host information
        dnac_host = self.params.get('dnac_host', 'Unknown')
        dnac_version = self.params.get('dnac_version', 'Unknown')

        # Generate summary statistics
        discovery_types = {}
        ip_ranges_count = 0
        credential_types = set()

        for discovery in discoveries_data:
            # Count discovery types
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
        header = []
        header.append("# Generated Discovery Playbook Configuration")
        header.append("# ===========================================")
        header.append("#")
        header.append(f"# Source Catalyst Center: {dnac_host}")
        header.append(f"# Catalyst Center Version: {dnac_version}")
        header.append(f"# Generated on: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        header.append("#")
        header.append("# Configuration Summary:")
        header.append(f"# - Total Discoveries: {len(discoveries_data)}")
        header.append(f"# - Total IP Ranges: {ip_ranges_count}")

        if discovery_types:
            header.append("# - Discovery Types:")
            for disc_type, count in discovery_types.items():
                header.append(f"#   - {disc_type}: {count}")

        if credential_types:
            header.append("# - Credential Types: {0}".format(', '.join(sorted(credential_types))))

        header.append("#")
        header.append("# This configuration is compatible with the 'discovery_workflow_manager' module.")
        header.append("# Use this playbook to recreate or manage discovery configurations in Catalyst Center.")
        header.append("#")

        return '\n'.join(header)

    def write_yaml_with_comments(self, yaml_data, file_path, header_comments):
        """
        Write YAML data to file with header comments and proper formatting.

        Args:
            yaml_data (dict): The data to write as YAML
            file_path (str): Path to the output file
            header_comments (str): Header comments to add at the beginning

        Returns:
            bool: True if successful, False otherwise
        """
        try:
            import yaml

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

    def generate_discovery_playbook(self):
        """
        Generate YAML playbook for discovery configurations.

        Returns:
            self: Instance with updated result
        """
        self.log("Starting discovery playbook generation", "INFO")

        config = self.config[0] if self.config else {}

        # Determine file path
        file_path = config.get('file_path')
        if not file_path:
            file_path = self.generate_filename()
            self.log(f"Using auto-generated filename: {file_path}", "INFO")

        # Get filters
        global_filters = config.get('global_filters', {})
        component_specific_filters = config.get('component_specific_filters', {})

        # Handle generate_all_configurations flag
        if config.get('generate_all_configurations', False):
            global_filters = {}  # No filtering when generating all
            self.log("Generate all configurations enabled - including all discoveries", "INFO")

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
            "config": discovery_details,
            "operation_summary": {
                "total_discoveries_processed": len(discoveries_data),
                "total_components_processed": 1,
                "total_successful_operations": 1,
                "total_failed_operations": 0,
                "component_summary": {
                    "discovery_details": {
                        "total_processed": len(discoveries_data),
                        "total_successful": len(discovery_details),
                        "total_failed": 0
                    }
                }
            }
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
                "component_summary": yaml_data["operation_summary"]["component_summary"]
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

    def get_diff_gathered(self):
        """
        Process gathered state for discovery configurations.

        Returns:
            self: Instance with updated result
        """
        self.log("Processing gathered state for discovery configurations", "INFO")
        return self.generate_discovery_playbook()

    def verify_diff_gathered(self, config):
        """
        Verify gathered state for discovery configurations.

        Args:
            config (dict): Configuration to verify

        Returns:
            self: Instance with updated result
        """
        self.log("Verifying gathered state for discovery configurations", "INFO")
        return self

    def run(self):
        """
        Main execution method for the discovery playbook generator.

        Returns:
            self: Instance with updated result
        """
        self.log("Starting discovery playbook generator execution", "INFO")

        # Validate input
        self.validate_input()
        if self.status == "failed":
            return self

        # Process based on state
        state = self.params.get("state", "gathered")

        if state == "gathered":
            self.get_diff_gathered()
            if self.params.get("config_verify"):
                self.verify_diff_gathered(self.config)

        return self


def main():
    """
    Main function for the discovery playbook generator module.
    """
    # Define module argument specification
    argument_spec = {
        "config": {"type": "list", "required": True, "elements": "dict"},
        "config_verify": {"type": "bool", "default": False},
        "state": {
            "type": "str",
            "default": "gathered",
            "choices": ["gathered"]
        },
        "dnac_host": {"type": "str", "required": True},
        "dnac_port": {"type": "str", "default": "443"},
        "dnac_username": {"type": "str", "default": "admin", "aliases": ["user"]},
        "dnac_password": {"type": "str", "no_log": True},
        "dnac_verify": {"type": "bool", "default": True},
        "dnac_version": {"type": "str", "default": "2.2.3.3"},
        "dnac_debug": {"type": "bool", "default": False},
        "dnac_log": {"type": "bool", "default": False},
        "dnac_log_level": {"type": "str", "default": "WARNING"},
        "dnac_log_file_path": {"type": "str", "default": "dnac.log"},
        "dnac_log_append": {"type": "bool", "default": True},
        "dnac_api_task_timeout": {"type": "int", "default": 1200},
        "dnac_task_poll_interval": {"type": "int", "default": 2},
        "validate_response_schema": {"type": "bool", "default": True}
    }

    # Create the module
    module = AnsibleModule(
        argument_spec=argument_spec,
        supports_check_mode=False
    )

    # Create an instance of the discovery playbook generator class
    discovery_generator = DiscoveryPlaybookGenerator(module)

    # Get the state parameter from the module; default to 'gathered'
    state = module.params.get("state")

    # Check if the state is valid
    if state not in discovery_generator.supported_states:
        discovery_generator.status = "failed"
        discovery_generator.msg = "State '{0}' is not supported. Supported states: {1}".format(
            state, discovery_generator.supported_states
        )
        discovery_generator.result["msg"] = discovery_generator.msg
        discovery_generator.module.fail_json(**discovery_generator.result)

    # Validate the input parameters and run the generator
    discovery_generator.validate_input().check_return_status()
    discovery_generator.run().check_return_status()

    # Exit with the result
    discovery_generator.module.exit_json(**discovery_generator.result)


if __name__ == "__main__":
    main()
