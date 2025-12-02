#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright (c) 2025, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

"""Ansible module to generate YAML configurations for Application Policy Module."""
from __future__ import absolute_import, division, print_function

__metaclass__ = type
__author__ = "Syed Khadeer Ahmed, Madhan Sankaranarayanan"

DOCUMENTATION = r"""
---
module: brownfield_application_policy_playbook_generator
short_description: Generate YAML configurations playbook for 'application_policy_workflow_manager' module.
description:
- Generates YAML configurations compatible with the 'application_policy_workflow_manager'
  module, reducing the effort required to manually create Ansible playbooks.
- The YAML configurations generated represent the application policies and queuing
  profiles deployed in the Cisco Catalyst Center.
- Supports extraction of Queuing Profiles and Application Policies.
version_added: 6.40.0
extends_documentation_fragment:
- cisco.dnac.workflow_manager_params
author:
- Syed Khadeer Ahmed (@syed-khadeerahmed)
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
    choices: [merged]
    default: merged
  config:
    description:
      - A list of filters for generating YAML playbook compatible with the 'application_policy_workflow_manager'
        module.
      - Filters specify which components to include in the YAML configuration file.
    type: list
    elements: dict
    required: true
    suboptions:
      generate_all_configurations:
        description:
          - When set to True, automatically generates YAML configurations for all application policies and queuing profiles.
          - This mode discovers all configured policies and profiles in Cisco Catalyst Center.
          - When enabled, the config parameter becomes optional and will use default values if not specified.
          - A default filename will be generated automatically if file_path is not specified.
        type: bool
        required: false
        default: false
      file_path:
        description:
          - Path where the YAML configuration file will be saved.
          - If not provided, the file will be saved in the current working directory with
            a default file name "application_policy_workflow_manager_playbook_<DD_Mon_YYYY_HH_MM_SS_MS>.yml".
        type: str
        required: false
      component_specific_filters:
        description:
          - Filters to specify which application policy components to include in the YAML configuration file.
          - Allows granular selection of specific components and their parameters.
        type: dict
        required: false
        suboptions:
          components_list:
            description:
              - List of components to include in the YAML configuration file.
              - Valid values are ["queuing_profile", "application_policy"]
              - If not specified, all supported components are included.
            type: list
            elements: str
            required: false
            choices: ["queuing_profile", "application_policy"]
          queuing_profile:
            description:
              - Specific queuing profile filtering options.
              - Allows extraction of only specific queuing profiles by name.
            type: dict
            required: false
            suboptions:
              profile_names_list:
                description:
                  - List of specific queuing profile names to extract.
                  - Only profiles in this list will be included in the generated configuration.
                  - Example ["Enterprise-QoS-Profile", "Wireless-QoS-Profile"]
                type: list
                elements: str
                required: false
          application_policy:
            description:
              - Specific application policy filtering options.
              - Allows extraction of only specific policies by name.
            type: dict
            required: false
            suboptions:
              policy_names_list:
                description:
                  - List of specific application policy names to extract.
                  - Only policies in this list will be included in the generated configuration.
                  - Example ["wired_traffic_policy", "wireless_traffic_policy"]
                type: list
                elements: str
                required: false
requirements:
- dnacentersdk >= 2.9.3
- python >= 3.9
notes:
- SDK Methods used are
  - application_policy.ApplicationPolicy.get_application_policy
  - application_policy.ApplicationPolicy.get_application_policy_queuing_profile
- Paths used are
  - GET /dna/intent/api/v1/app-policy
  - GET /dna/intent/api/v1/app-policy-queuing-profile
"""

EXAMPLES = r"""
- name: Generate all application policy configurations
  cisco.dnac.brownfield_application_policy_playbook_generator:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    dnac_log: true
    dnac_log_level: "{{dnac_log_level}}"
    state: merged
    config:
      - generate_all_configurations: true

- name: Generate configurations with custom file path
  cisco.dnac.brownfield_application_policy_playbook_generator:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    dnac_log: true
    dnac_log_level: "{{dnac_log_level}}"
    state: merged
    config:
      - file_path: "/tmp/app_policy_config.yml"

- name: Generate specific queuing profiles
  cisco.dnac.brownfield_application_policy_playbook_generator:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    dnac_log: true
    dnac_log_level: "{{dnac_log_level}}"
    state: merged
    config:
      - file_path: "/tmp/queuing_profiles.yml"
        component_specific_filters:
          components_list: ["queuing_profile"]
          queuing_profile:
            profile_names_list: ["Enterprise-QoS-Profile", "Wireless-QoS"]

- name: Generate specific application policies
  cisco.dnac.brownfield_application_policy_playbook_generator:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    dnac_log: true
    dnac_log_level: "{{dnac_log_level}}"
    state: merged
    config:
      - file_path: "/tmp/app_policies.yml"
        component_specific_filters:
          components_list: ["application_policy"]
          application_policy:
            policy_names_list: ["wired_traffic_policy"]

- name: Generate both queuing profiles and policies with filters
  cisco.dnac.brownfield_application_policy_playbook_generator:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    dnac_log: true
    dnac_log_level: "{{dnac_log_level}}"
    state: merged
    config:
      - file_path: "/tmp/complete_app_policy_config.yml"
        component_specific_filters:
          components_list: ["queuing_profile", "application_policy"]
          queuing_profile:
            profile_names_list: ["Enterprise-QoS-Profile"]
          application_policy:
            policy_names_list: ["wired_traffic_policy", "wireless_traffic_policy"]
"""

RETURN = r"""
response_1:
  description: Successful YAML configuration generation
  returned: always
  type: dict
  sample: >
    {
      "response": {
        "message": "YAML config generation succeeded for module 'application_policy_workflow_manager'.",
        "file_path": "/tmp/app_policy_config.yml",
        "configurations_generated": 15,
        "operation_summary": {
          "total_queuing_profiles_processed": 5,
          "total_application_policies_processed": 10,
          "total_successful_operations": 15,
          "total_failed_operations": 0,
          "success_details": [
            {
              "component_type": "queuing_profile",
              "component_name": "Enterprise-QoS-Profile",
              "status": "success"
            }
          ],
          "failure_details": []
        }
      },
      "msg": "YAML config generation succeeded for module 'application_policy_workflow_manager'."
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


class ApplicationPolicyPlaybookGenerator(DnacBase, BrownFieldHelper):
    """
    A class for generating playbook files for application policies deployed within the Cisco Catalyst Center.
    """

    def __init__(self, module):
        """
        Initialize an instance of the class.
        Args:
            module: The module associated with the class instance.
        Returns:
            None
        """
        self.supported_states = ["merged"]
        super().__init__(module)
        self.module_schema = self.get_workflow_elements_schema()
        self.module_name = "application_policy_workflow_manager"

        # Initialize operation tracking
        self.operation_successes = []
        self.operation_failures = []
        self.total_components_processed = 0

        # Initialize generate_all_configurations
        self.generate_all_configurations = False

    def validate_input(self):
        """
        Validates the input configuration parameters for the playbook.
        Returns:
            object: An instance of the class with updated attributes.
        """
        self.log("Starting validation of input configuration parameters.", "DEBUG")

        if not self.config:
            self.msg = "config parameter is required for brownfield_application_policy_playbook_generator module"
            self.set_operation_result("failed", False, self.msg, "ERROR")
            return self

        temp_spec = {
            "generate_all_configurations": {"type": "bool", "required": False, "default": False},
            "file_path": {"type": "str", "required": False},
            "component_specific_filters": {"type": "dict", "required": False},
        }

        valid_temp, invalid_params = validate_list_of_dicts(self.config, temp_spec)

        if invalid_params:
            self.msg = "Invalid parameters in playbook: {0}".format(invalid_params)
            self.set_operation_result("failed", False, self.msg, "ERROR")
            return self

        self.validated_config = valid_temp
        self.msg = "Successfully validated playbook configuration parameters"
        self.set_operation_result("success", False, self.msg, "INFO")
        return self

    def get_workflow_elements_schema(self):
        """
        Returns the mapping configuration for application policy workflow manager.
        """
        return {
            "network_elements": {
                "queuing_profile": {
                    "filters": {
                        "profile_names_list": {
                            "type": "list",
                            "required": False,
                            "elements": "str"
                        }
                    },
                    "reverse_mapping_function": self.queuing_profile_reverse_mapping_spec,
                    "api_function": "get_application_policy_queuing_profile",
                    "api_family": "application_policy",
                    "get_function_name": self.get_queuing_profiles,
                },
                "application_policy": {
                    "filters": {
                        "policy_names_list": {
                            "type": "list",
                            "required": False,
                            "elements": "str"
                        }
                    },
                    "reverse_mapping_function": self.application_policy_reverse_mapping_spec,
                    "api_function": "get_application_policy",
                    "api_family": "application_policy",
                    "get_function_name": self.get_application_policies,
                }
            }
        }

    def queuing_profile_reverse_mapping_spec(self):
        """
        Returns reverse mapping specification for queuing profiles.
        """
        return OrderedDict({
            "profile_name": {"type": "str", "source_key": "name"},
            "profile_description": {"type": "str", "source_key": "description"},
            "bandwidth_settings": {
                "type": "dict",
                "source_key": "clause",
                "special_handling": True,
                "transform": self.transform_bandwidth_settings
            },
            "dscp_settings": {
                "type": "dict",
                "source_key": "clause",
                "special_handling": True,
                "transform": self.transform_dscp_settings
            }
        })

    def application_policy_reverse_mapping_spec(self):
        """
        Returns reverse mapping specification for application policies.
        """
        return OrderedDict({
            "name": {"type": "str", "source_key": "policyScope"},
            "policy_status": {
                "type": "str",
                "source_key": "deletePolicyStatus",
                "transform": lambda x: "deployed" if x == "NONE" else x.lower()
            },
            "site_names": {
                "type": "list",
                "elements": "str",
                "source_key": "advancedPolicyScope",
                "special_handling": True,
                "transform": self.transform_site_names
            },
            "device_type": {
                "type": "str",
                "source_key": "advancedPolicyScope",
                "special_handling": True,
                "transform": self.transform_device_type
            },
            "ssid_name": {
                "type": "str",
                "source_key": "advancedPolicyScope",
                "special_handling": True,
                "transform": self.transform_ssid_name
            },
            "application_queuing_profile_name": {
                "type": "str",
                "source_key": "contract",
                "special_handling": True,
                "transform": self.get_queuing_profile_name_from_id
            },
            "clause": {
                "type": "list",
                "elements": "dict",
                "source_key": "consumer",
                "special_handling": True,
                "transform": self.transform_clause
            }
        })

    def transform_bandwidth_settings(self, clause_data):
        """Transform clause data to bandwidth settings format."""
        if not clause_data or not isinstance(clause_data, list):
            return None

        bandwidth_settings = {}
        
        for clause in clause_data:
            if not isinstance(clause, dict):
                continue
                
            clause_type = clause.get("type")
            if clause_type in ["BANDWIDTH", "BANDWIDTH_CUSTOM"]:
                bandwidth_settings["is_common_between_all_interface_speeds"] = (clause_type == "BANDWIDTH")
                
                # Extract interface speed bandwidth clauses if present
                if "interfaceSpeedBandwidthClauses" in clause:
                    interface_clauses = clause.get("interfaceSpeedBandwidthClauses", [])
                    if interface_clauses and len(interface_clauses) > 0:
                        # Get the first interface speed clause (usually "ALL")
                        first_clause = interface_clauses[0]
                        tc_bandwidth_settings = first_clause.get("tcBandwidthSettings", [])
                        
                        # Transform to the expected format
                        bandwidth_list = []
                        for tc_setting in tc_bandwidth_settings:
                            traffic_class = tc_setting.get("trafficClass", "").lower().replace("_", "-")
                            bandwidth_list.append({
                                "traffic_class": traffic_class,
                                "bandwidth_percentage": tc_setting.get("bandwidthPercentage", 0)
                            })
                        
                        if bandwidth_list:
                            bandwidth_settings["bandwidth_by_traffic_class"] = bandwidth_list
                    
        return bandwidth_settings if bandwidth_settings else None

    def transform_dscp_settings(self, clause_data):
        """Transform clause data to DSCP settings format."""
        if not clause_data or not isinstance(clause_data, list):
            return None

        dscp_settings = {}
        
        for clause in clause_data:
            if not isinstance(clause, dict):
                continue
                
            if clause.get("type") == "DSCP_CUSTOMIZATION":
                # Extract DSCP values for each traffic class
                tc_dscp_settings = clause.get("tcDscpSettings", [])
                
                dscp_list = []
                for tc_setting in tc_dscp_settings:
                    traffic_class = tc_setting.get("trafficClass", "").lower().replace("_", "-")
                    dscp_list.append({
                        "traffic_class": traffic_class,
                        "dscp_value": tc_setting.get("dscp", "0")
                    })
                
                if dscp_list:
                    dscp_settings["dscp_by_traffic_class"] = dscp_list
                    
        return dscp_settings if dscp_settings else None

    def transform_site_names(self, advanced_policy_scope):
        """Transform site IDs to site names."""
        if not advanced_policy_scope or not isinstance(advanced_policy_scope, dict):
            return []

        site_ids = []
        advanced_policy_scope_elements = advanced_policy_scope.get("advancedPolicyScopeElement", [])
        
        if not isinstance(advanced_policy_scope_elements, list):
            return []
        
        for element in advanced_policy_scope_elements:
            if not isinstance(element, dict):
                continue
            group_ids = element.get("groupId", [])
            if isinstance(group_ids, list):
                site_ids.extend(group_ids)

        site_names = []
        for site_id in site_ids:
            site_name = self.get_site_name(site_id)
            if site_name:
                site_names.append(site_name)

        return site_names

    def transform_device_type(self, advanced_policy_scope):
        """Determine device type (wired/wireless) from policy scope."""
        if not advanced_policy_scope or not isinstance(advanced_policy_scope, dict):
            return "wired"

        advanced_policy_scope_elements = advanced_policy_scope.get("advancedPolicyScopeElement", [])
        
        if not isinstance(advanced_policy_scope_elements, list):
            return "wired"
        
        for element in advanced_policy_scope_elements:
            if not isinstance(element, dict):
                continue
            if element.get("ssid"):
                return "wireless"

        return "wired"

    def transform_ssid_name(self, advanced_policy_scope):
        """Extract SSID name for wireless policies."""
        if not advanced_policy_scope or not isinstance(advanced_policy_scope, dict):
            return None

        advanced_policy_scope_elements = advanced_policy_scope.get("advancedPolicyScopeElement", [])
        
        if not isinstance(advanced_policy_scope_elements, list):
            return None
        
        for element in advanced_policy_scope_elements:
            if not isinstance(element, dict):
                continue
            ssid = element.get("ssid")
            if ssid:
                return ssid[0] if isinstance(ssid, list) and len(ssid) > 0 else ssid

        return None

    def get_queuing_profile_name_from_id(self, contract_data):
        """Get queuing profile name from contract ID."""
        if not contract_data or not isinstance(contract_data, dict):
            return None

        profile_id = contract_data.get("idRef")
        if not profile_id:
            return None

        try:
            response = self.dnac._exec(
                family="application_policy",
                function="get_application_policy_queuing_profile",
                op_modifies=False,
                params={"id": profile_id}
            )
            
            if response and response.get("response"):
                profiles = response.get("response")
                if profiles and len(profiles) > 0:
                    return profiles[0].get("name")
        except Exception as e:
            self.log("Error getting queuing profile name: {0}".format(str(e)), "ERROR")

        return None

    def get_application_set_name_from_id(self, app_set_id):
        """
        Get application set name from its ID.
        
        Args:
            app_set_id (str): Application set ID
            
        Returns:
            str: Application set name or None if not found
        """
        try:
            self.log("Fetching application set name for ID: {0}".format(app_set_id), "DEBUG")
            
            response = self.dnac._exec(
                family="application_policy",
                function="get_application_sets",
                op_modifies=False
            )
            
            if response and response.get("response"):
                app_sets = response.get("response", [])
                for app_set in app_sets:
                    if isinstance(app_set, dict) and app_set.get("id") == app_set_id:
                        app_set_name = app_set.get("name")
                        self.log("Found application set: {0} -> {1}".format(app_set_id, app_set_name), "INFO")
                        return app_set_name
            
            self.log("Application set not found for ID: {0}".format(app_set_id), "WARNING")
            return None
            
        except Exception as e:
            self.log("Error fetching application set name for ID {0}: {1}".format(app_set_id, str(e)), "ERROR")
            return None

    def transform_clause(self, policy):
        """
        Transform policy data to clause format with relevance details.
        Extracts application sets from producer.scalableGroup and relevance from exclusiveContract.
        
        Args:
            policy (dict): Full policy object from API
            
        Returns:
            list: List containing clause dictionary with relevance details
        """
        self.log("Transforming clause data from policy: {0}".format(policy.get("policyScope")), "DEBUG")
        
        if not policy or not isinstance(policy, dict):
            self.log("Policy data is None or not a dict", "WARNING")
            return []

        policy_name = policy.get("policyScope", "unknown")
        
        # Check if this is a special policy type that shouldn't have application clauses
        name_lower = policy.get("name", "").lower()
        if any(x in name_lower for x in ["queuing_customization", "global_policy_configuration"]):
            self.log("Skipping clause for special policy type: {0}".format(policy_name), "DEBUG")
            return []

        # Dictionary to group application sets by relevance level
        relevance_map = {}

        # Extract producer data (contains app set info)
        producer = policy.get("producer")
        if not producer or not isinstance(producer, dict):
            self.log("No producer data found in policy '{0}'".format(policy_name), "DEBUG")
            return []
        
        scalable_groups = producer.get("scalableGroup", [])
        if not scalable_groups or not isinstance(scalable_groups, list):
            self.log("No scalableGroup found in producer for policy '{0}'".format(policy_name), "DEBUG")
            return []

        self.log("Found {0} scalable groups in policy '{1}'".format(len(scalable_groups), policy_name), "INFO")

        # Get relevance level from exclusiveContract
        relevance_level = "DEFAULT"
        exclusive_contract = policy.get("exclusiveContract")
        if exclusive_contract and isinstance(exclusive_contract, dict):
            clauses = exclusive_contract.get("clause", [])
            if clauses and len(clauses) > 0:
                for clause in clauses:
                    if clause.get("type") == "BUSINESS_RELEVANCE":
                        relevance_level = clause.get("relevanceLevel", "DEFAULT")
                        break
        
        self.log("Relevance level for policy '{0}': {1}".format(policy_name, relevance_level), "INFO")
        
        # Process each scalable group (app set)
        for group in scalable_groups:
            if not isinstance(group, dict):
                continue
            
            app_set_id = group.get("idRef")
            if not app_set_id:
                self.log("No idRef found in scalable group", "DEBUG")
                continue
            
            # Get application set name from ID
            app_set_name = self.get_application_set_name_from_id(app_set_id)
            
            if app_set_name:
                if relevance_level not in relevance_map:
                    relevance_map[relevance_level] = []
                relevance_map[relevance_level].append(app_set_name)
                self.log("Added app set '{0}' to relevance '{1}' for policy '{2}'".format(
                    app_set_name, relevance_level, policy_name), "INFO")
            else:
                self.log("Could not get app set name for ID: {0} in policy '{1}'".format(
                    app_set_id, policy_name), "WARNING")

        # Build relevance_details list
        relevance_details = []
        for relevance in ["BUSINESS_RELEVANT", "BUSINESS_IRRELEVANT", "DEFAULT"]:
            if relevance in relevance_map and relevance_map[relevance]:
                app_sets = sorted(list(set(relevance_map[relevance])))
                relevance_details.append(OrderedDict([
                    ("relevance", relevance),
                    ("application_set_name", app_sets)
                ]))

        if relevance_details:
            self.log("Created clause with {0} relevance levels for policy '{1}'".format(
                len(relevance_details), policy_name), "INFO")
            return [OrderedDict([
                ("clause_type", "BUSINESS_RELEVANCE"),
                ("relevance_details", relevance_details)
            ])]

        self.log("No relevance details found for policy '{0}' - returning empty list".format(policy_name), "INFO")
        return []

    def transform_application_policies(self, policies):
        """Transform application policies to playbook format."""
        if not policies:
            self.log("No policies to transform", "INFO")
            return []

        self.log("Starting transformation of {0} policies".format(len(policies)), "INFO")
        
        # First, group policies by policyScope to consolidate them
        policy_groups = {}
        for policy in policies:
            if not isinstance(policy, dict):
                continue
            
            policy_scope = policy.get("policyScope")
            if not policy_scope:
                continue
            
            if policy_scope not in policy_groups:
                policy_groups[policy_scope] = []
            policy_groups[policy_scope].append(policy)
        
        self.log("Grouped into {0} unique policy scopes".format(len(policy_groups)), "INFO")

        transformed_policies = []
        seen_policies = set()
        
        for policy_scope, policy_list in policy_groups.items():
            self.log("Processing policy scope: {0} with {1} entries".format(policy_scope, len(policy_list)), "INFO")
            
            # Use the first policy as the base (they should all have same scope/site info)
            base_policy = policy_list[0]
            advanced_policy_scope = base_policy.get("advancedPolicyScope")
            
            # Get site IDs for unique identification
            site_ids = []
            if advanced_policy_scope and isinstance(advanced_policy_scope, dict):
                adv_scope_elements = advanced_policy_scope.get("advancedPolicyScopeElement", [])
                for element in adv_scope_elements:
                    if isinstance(element, dict):
                        group_ids = element.get("groupId", [])
                        if isinstance(group_ids, list):
                            site_ids.extend(group_ids)
            
            policy_identifier = (policy_scope, tuple(sorted(site_ids)))
            
            if policy_identifier in seen_policies:
                self.log("Skipping duplicate policy: {0}".format(policy_scope), "DEBUG")
                continue
            
            seen_policies.add(policy_identifier)
            
            policy_data = OrderedDict()
            policy_data["name"] = policy_scope
            
            delete_status = base_policy.get("deletePolicyStatus", "NONE")
            policy_data["policy_status"] = "deployed" if delete_status == "NONE" else delete_status.lower()
            
            site_names = self.transform_site_names(advanced_policy_scope)
            if site_names:
                policy_data["site_names"] = site_names
            
            device_type = self.transform_device_type(advanced_policy_scope)
            policy_data["device_type"] = device_type
            
            if device_type == "wireless":
                ssid_name = self.transform_ssid_name(advanced_policy_scope)
                if ssid_name:
                    policy_data["ssid_name"] = ssid_name
            
            # Get queuing profile from the customization policy
            queuing_profile_name = None
            for policy in policy_list:
                if "queuing_customization" in policy.get("name", "").lower():
                    contract = policy.get("contract")
                    if contract and isinstance(contract, dict):
                        queuing_profile_name = self.get_queuing_profile_name_from_id(contract)
                        break
            
            if queuing_profile_name:
                policy_data["application_queuing_profile_name"] = queuing_profile_name
            
            # Collect all application sets across all sub-policies by relevance
            all_relevance_map = {
                "BUSINESS_RELEVANT": set(),
                "BUSINESS_IRRELEVANT": set(),
                "DEFAULT": set()
            }
            
            for policy in policy_list:
                # Skip special policy types
                name_lower = policy.get("name", "").lower()
                if any(x in name_lower for x in ["queuing_customization", "global_policy_configuration"]):
                    continue
                
                # Get app sets from this sub-policy
                producer = policy.get("producer")
                if not producer or not isinstance(producer, dict):
                    continue
                
                scalable_groups = producer.get("scalableGroup", [])
                if not scalable_groups or not isinstance(scalable_groups, list):
                    continue
                
                # Get relevance level from exclusiveContract
                relevance_level = "DEFAULT"
                exclusive_contract = policy.get("exclusiveContract")
                if exclusive_contract and isinstance(exclusive_contract, dict):
                    clauses = exclusive_contract.get("clause", [])
                    for clause in clauses:
                        if clause.get("type") == "BUSINESS_RELEVANCE":
                            relevance_level = clause.get("relevanceLevel", "DEFAULT")
                            break
                
                # Add app sets to the relevance map
                for group in scalable_groups:
                    if not isinstance(group, dict):
                        continue
                    
                    app_set_id = group.get("idRef")
                    if app_set_id:
                        app_set_name = self.get_application_set_name_from_id(app_set_id)
                        if app_set_name:
                            all_relevance_map[relevance_level].add(app_set_name)
                            self.log("Added '{0}' to {1} for policy '{2}'".format(
                                app_set_name, relevance_level, policy_scope), "DEBUG")
            
            # Build clause if we have any application sets
            relevance_details = []
            for relevance in ["BUSINESS_RELEVANT", "BUSINESS_IRRELEVANT", "DEFAULT"]:
                if all_relevance_map[relevance]:
                    app_sets = sorted(list(all_relevance_map[relevance]))
                    relevance_details.append(OrderedDict([
                        ("relevance", relevance),
                        ("application_set_name", app_sets)
                    ]))
            
            if relevance_details:
                policy_data["clause"] = [OrderedDict([
                    ("clause_type", "BUSINESS_RELEVANCE"),
                    ("relevance_details", relevance_details)
                ])]
                self.log("Successfully added clause to policy '{0}' with {1} relevance levels".format(
                    policy_scope, len(relevance_details)), "INFO")
            else:
                self.log("No clause data found for policy '{0}'".format(policy_scope), "INFO")
            
            if policy_scope and site_names:
                transformed_policies.append(policy_data)
                self.log("Successfully transformed policy: {0} (has clause: {1})".format(
                    policy_scope, "clause" in policy_data), "INFO")
            else:
                self.log("Skipping policy due to missing required fields: name={0}, sites={1}".format(
                    policy_scope, len(site_names) if site_names else 0), "WARNING")
        
        self.log("Transformed {0} policies total".format(len(transformed_policies)), "INFO")
        return transformed_policies

    def get_detailed_application_policy(self, policy_name):
        """
        Fetch detailed application policy data including consumer information.
        
        Args:
            policy_name (str): Name of the policy to fetch
            
        Returns:
            dict: Detailed policy data or None if not found
        """
        try:
            self.log("Fetching detailed policy data for '{0}'".format(policy_name), "INFO")
            
            # Try getting with policy scope parameter
            response = self.dnac._exec(
                family="application_policy",
                function="get_application_policy",
                op_modifies=False,
                params={"policyScope": policy_name}
            )
            
            if response and response.get("response"):
                policies = response.get("response", [])
                if policies and len(policies) > 0:
                    detailed_policy = policies[0]
                    self.log("Retrieved detailed policy data for '{0}'".format(policy_name), "INFO")
                    return detailed_policy
            
            self.log("No detailed policy data found for '{0}'".format(policy_name), "WARNING")
            return None
            
        except Exception as e:
            self.log("Error fetching detailed policy for '{0}': {1}".format(policy_name, str(e)), "ERROR")
            return None

    def get_application_policies(self, network_element, filters):
        """Retrieve application policies from Catalyst Center."""
        self.log("Starting application policy retrieval", "INFO")

        component_specific_filters = filters.get("component_specific_filters", {})
        app_policy_filters = component_specific_filters.get("application_policy", {})
        policy_names_list = app_policy_filters.get("policy_names_list", [])

        try:
            # Get all application policies
            response = self.dnac._exec(
                family="application_policy",
                function="get_application_policy",
                op_modifies=False,
            )

            if not response or not response.get("response"):
                self.log("No application policies found in response", "WARNING")
                return {"application_policy": []}

            policies = response.get("response", [])
            self.log("Retrieved {0} total application policies from API".format(len(policies)), "INFO")

            # Filter by policy names if specified
            if policy_names_list:
                original_count = len(policies)
                policies = [p for p in policies if p.get("policyScope") in policy_names_list]
                self.log("Filtered from {0} to {1} policies based on policy_names_list".format(
                    original_count, len(policies)), "INFO")

            # Log sample policy structure for debugging
            if policies:
                sample_policy = policies[0]
                self.log("Sample policy structure - Keys: {0}".format(list(sample_policy.keys())), "DEBUG")
                self.log("Sample policy has consumer: {0}".format("consumer" in sample_policy), "INFO")
                if "consumer" in sample_policy:
                    self.log("Sample consumer data: {0}".format(sample_policy.get("consumer")), "DEBUG")

            # Transform policies using custom transformation
            transformed_policies = self.transform_application_policies(policies)

            self.log("Successfully transformed {0} application policies".format(len(transformed_policies)), "INFO")
            
            # Log summary of policies with/without clauses
            policies_with_clauses = sum(1 for p in transformed_policies if "clause" in p)
            policies_without_clauses = len(transformed_policies) - policies_with_clauses
            self.log("Policies with clauses: {0}, without clauses: {1}".format(
                policies_with_clauses, policies_without_clauses), "INFO")

            return {"application_policy": transformed_policies}

        except Exception as e:
            self.log("Error retrieving application policies: {0}".format(str(e)), "ERROR")
            import traceback
            self.log("Traceback: {0}".format(traceback.format_exc()), "ERROR")
            return {"application_policy": []}

    def transform_queuing_profiles(self, profiles):
        """Transform queuing profiles to playbook format."""
        if not profiles:
            self.log("No queuing profiles to transform", "INFO")
            return []

        transformed_profiles = []
        
        for profile in profiles:
            if not isinstance(profile, dict):
                continue
            
            profile_data = OrderedDict()
            
            # Basic profile information
            profile_data["profile_name"] = profile.get("name")
            profile_data["profile_description"] = profile.get("description", "")
            
            # Process clauses for bandwidth and DSCP settings
            clauses = profile.get("clause", [])
            
            if clauses:
                bandwidth_settings, dscp_settings = self.extract_settings_from_clauses(clauses)
                
                if bandwidth_settings:
                    profile_data["bandwidth_settings"] = bandwidth_settings
                
                if dscp_settings:
                    profile_data["dscp_settings"] = dscp_settings
            
            transformed_profiles.append(profile_data)
            self.log("Transformed queuing profile: {0}".format(profile_data["profile_name"]), "INFO")
        
        return transformed_profiles

    def extract_settings_from_clauses(self, clauses):
        """
        Extract bandwidth and DSCP settings from queuing profile clauses.
        
        Args:
            clauses (list): List of clause dictionaries from the API response
            
        Returns:
            tuple: (bandwidth_settings dict, dscp_settings dict)
        """
        bandwidth_settings = None
        dscp_settings = OrderedDict()
        
        # Traffic class mapping for bandwidth percentages
        tc_map = {
            "BROADCAST_VIDEO": "broadcast_video",
            "BULK_DATA": "bulk_data",
            "MULTIMEDIA_CONFERENCING": "multimedia_conferencing",
            "MULTIMEDIA_STREAMING": "multimedia_streaming",
            "NETWORK_CONTROL": "network_control",
            "OPS_ADMIN_MGMT": "ops_admin_mgmt",
            "REAL_TIME_INTERACTIVE": "real_time_interactive",
            "SIGNALING": "signaling",
            "TRANSACTIONAL_DATA": "transactional_data",
            "VOIP_TELEPHONY": "voip_telephony",
            "BEST_EFFORT": "best_effort",
            "SCAVENGER": "scavenger"
        }
        
        for clause in clauses:
            if not isinstance(clause, dict):
                continue
                
            clause_type = clause.get("type")
            
            # Process bandwidth settings
            if clause_type == "BANDWIDTH":
                is_common = clause.get("isCommonBetweenAllInterfaceSpeeds", False)
                
                # CRITICAL FIX: Get interfaceSpeedBandwidthClauses first
                interface_speed_clauses = clause.get("interfaceSpeedBandwidthClauses", [])
                
                if not interface_speed_clauses:
                    self.log("No interfaceSpeedBandwidthClauses found in BANDWIDTH clause", "WARNING")
                    continue
                
                if is_common:
                    # Common bandwidth settings across all interface speeds
                    bandwidth_settings = OrderedDict([
                        ("is_common_between_all_interface_speeds", True),
                        ("interface_speed", "ALL"),
                        ("bandwidth_percentages", OrderedDict())
                    ])
                    
                    # Get the first (and should be only) interface speed clause for "ALL"
                    if len(interface_speed_clauses) > 0:
                        first_speed_clause = interface_speed_clauses[0]
                        tc_bandwidth_settings = first_speed_clause.get("tcBandwidthSettings", [])
                        
                        self.log("Found {0} traffic class bandwidth settings".format(len(tc_bandwidth_settings)), "DEBUG")
                        
                        for tc_setting in tc_bandwidth_settings:
                            tc_name = tc_setting.get("trafficClass")
                            bandwidth_percent = tc_setting.get("bandwidthPercentage")
                            
                            if tc_name in tc_map and bandwidth_percent is not None:
                                playbook_tc_name = tc_map[tc_name]
                                bandwidth_settings["bandwidth_percentages"][playbook_tc_name] = str(bandwidth_percent)
                                self.log("Added bandwidth for {0}: {1}%".format(playbook_tc_name, bandwidth_percent), "DEBUG")
                
                else:
                    # Interface-specific bandwidth settings
                    bandwidth_settings = OrderedDict([
                        ("is_common_between_all_interface_speeds", False),
                        ("interface_speed_settings", [])
                    ])
                    
                    for speed_clause in interface_speed_clauses:
                        interface_speed = speed_clause.get("interfaceSpeed")
                        tc_bandwidth_settings = speed_clause.get("tcBandwidthSettings", [])
                        
                        speed_setting = OrderedDict([
                            ("interface_speed", interface_speed),
                            ("bandwidth_percentages", OrderedDict())
                        ])
                        
                        for tc_setting in tc_bandwidth_settings:
                            tc_name = tc_setting.get("trafficClass")
                            bandwidth_percent = tc_setting.get("bandwidthPercentage")
                            
                            if tc_name in tc_map and bandwidth_percent is not None:
                                playbook_tc_name = tc_map[tc_name]
                                speed_setting["bandwidth_percentages"][playbook_tc_name] = str(bandwidth_percent)
                        
                        bandwidth_settings["interface_speed_settings"].append(speed_setting)
            
            # Process DSCP settings
            elif clause_type == "DSCP_CUSTOMIZATION":
                tc_dscp_settings = clause.get("tcDscpSettings", [])
                
                self.log("Found {0} traffic class DSCP settings".format(len(tc_dscp_settings)), "DEBUG")
                
                for tc_setting in tc_dscp_settings:
                    tc_name = tc_setting.get("trafficClass")
                    dscp_value = tc_setting.get("dscp")
                    
                    if tc_name in tc_map and dscp_value is not None:
                        playbook_tc_name = tc_map[tc_name]
                        dscp_settings[playbook_tc_name] = str(dscp_value)
        
        return bandwidth_settings, dscp_settings if dscp_settings else None

    def get_queuing_profiles(self, network_element, config):
        """Get queuing profiles from Catalyst Center."""
        self.log("Starting queuing profile retrieval", "INFO")

        # Extract filters from config
        component_specific_filters = config.get("component_specific_filters", {})
        queuing_profile_filters = component_specific_filters.get("queuing_profile", {})
        profile_names_list = queuing_profile_filters.get("profile_names_list", [])

        try:
            # Get queuing profiles
            response = self.dnac._exec(
                family="application_policy",
                function="get_application_policy_queuing_profile",
                op_modifies=False,
            )

            if not response or not response.get("response"):
                self.log("No queuing profiles found", "WARNING")
                return {"queuing_profile": []}

            profiles = response.get("response", [])
            self.log("Retrieved {0} total queuing profiles from API".format(len(profiles)), "INFO")

            # Filter by profile names if specified
            if profile_names_list:
                original_count = len(profiles)
                profiles = [p for p in profiles if p.get("name") in profile_names_list]
                self.log("Filtered from {0} to {1} profiles based on profile_names_list: {2}".format(
                    original_count, len(profiles), profile_names_list), "INFO")

            if not profiles:
                self.log("No queuing profiles matched the filter criteria", "WARNING")
                return {"queuing_profile": []}

            # Transform profiles
            transformed_profiles = self.transform_queuing_profiles(profiles)
            self.log("Transformed {0} queuing profiles".format(len(transformed_profiles)), "INFO")

            return {"queuing_profile": transformed_profiles}

        except Exception as e:
            self.log("Error retrieving queuing profiles: {0}".format(str(e)), "ERROR")
            import traceback
            self.log("Traceback: {0}".format(traceback.format_exc()), "ERROR")
            return {"queuing_profile": []}

    def yaml_config_generator(self, config):
        """Generate YAML configuration file."""
        self.log("Starting YAML configuration generation", "INFO")

        file_path = config.get("file_path")
        if not file_path:
            file_path = self.generate_filename()

        component_specific_filters = config.get("component_specific_filters", {})
        components_list = component_specific_filters.get("components_list", ["queuing_profile", "application_policy"])

        # Use list of dicts instead of single list
        final_output = []

        # Process each component
        for component_name in components_list:
            if component_name in self.module_schema["network_elements"]:
                network_element = self.module_schema["network_elements"][component_name]
                get_function = network_element["get_function_name"]
                
                component_data = get_function(network_element, config)

                if component_data and component_data.get(component_name):
                    # Add as separate dict entry
                    final_output.append({component_name: component_data[component_name]})

        if not final_output:
            self.msg = "No configurations found to generate"
            self.set_operation_result("success", False, self.msg, "INFO")
            return self

        # Write to YAML file
        success = self.write_dict_to_yaml(final_output, file_path)

        if success:
            self.msg = "YAML config generation succeeded for module '{0}'.".format(self.module_name)
            self.result["response"] = {
                "message": self.msg,
                "file_path": file_path,
                "configurations_generated": sum(len(item[list(item.keys())[0]]) for item in final_output)
            }
            self.set_operation_result("success", True, self.msg, "INFO")
        else:
            self.msg = "Failed to write YAML configuration file"
            self.set_operation_result("failed", False, self.msg, "ERROR")

        return self


    def get_want(self, config, state):
        """Get desired state from config."""
        self.log("Processing configuration for state: {0}".format(state), "INFO")
        
        self.generate_all_configurations = config.get("generate_all_configurations", False)
        
        self.want = {
            "file_path": config.get("file_path"),
            "component_specific_filters": config.get("component_specific_filters", {}),
            "state": state
        }

        return self

    def get_diff_merged(self):
        """Process merge state."""
        self.log("Processing merged state", "INFO")
        
        config = self.validated_config[0] if self.validated_config else {}
        self.yaml_config_generator(config)
        
        return self


def main():
    """Main entry point for module execution."""
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
        "state": {"default": "merged", "choices": ["merged"]},
    }

    module = AnsibleModule(argument_spec=element_spec, supports_check_mode=True)
    app_policy_generator = ApplicationPolicyPlaybookGenerator(module)

    # Version check
    current_version = app_policy_generator.get_ccc_version()
    min_supported_version = "2.3.7.6"

    if app_policy_generator.compare_dnac_versions(current_version, min_supported_version) < 0:
        app_policy_generator.msg = "Application Policy features require Cisco Catalyst Center version {0} or later. Current version: {1}".format(
            min_supported_version, current_version
        )
        app_policy_generator.set_operation_result("failed", False, app_policy_generator.msg, "CRITICAL")
        module.fail_json(msg=app_policy_generator.msg)

    # Get state
    state = app_policy_generator.params.get("state")

    if state not in app_policy_generator.supported_states:
        app_policy_generator.msg = "State '{0}' is not supported. Supported states: {1}".format(
            state, app_policy_generator.supported_states
        )
        app_policy_generator.set_operation_result("failed", False, app_policy_generator.msg, "ERROR")
        module.fail_json(msg=app_policy_generator.msg)

    # Validate input
    app_policy_generator.validate_input().check_return_status()

    # Process configuration
    for config in app_policy_generator.validated_config:
        app_policy_generator.get_want(config, state).check_return_status()
        app_policy_generator.get_diff_merged().check_return_status()

    module.exit_json(**app_policy_generator.result)


if __name__ == "__main__":
    main()