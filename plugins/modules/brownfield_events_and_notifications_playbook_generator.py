#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright (c) 2026, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

"""Ansible module to generate YAML playbook for Events and Notifications Configuration in Cisco Catalyst Center."""
from __future__ import absolute_import, division, print_function

__metaclass__ = type
__author__ = "Priyadharshini B, Madhan Sankaranarayanan"

DOCUMENTATION = r"""
---
module: brownfield_events_and_notifications_playbook_generator
short_description: Generate YAML playbook for 'events_and_notifications_workflow_manager' module.
description:
- Generates YAML configurations compatible with the
  events_and_notifications_workflow_manager module for brownfield infrastructure
  discovery and documentation.
- Retrieves existing events and notifications configurations from Cisco Catalyst
  Center including webhook destinations, email destinations, syslog destinations,
  SNMP destinations, ITSM integration settings, and event subscriptions.
- Transforms API responses to playbook-compatible YAML format with parameter
  name mapping, password redaction, and structure optimization for Ansible
  execution.
- Supports comprehensive filtering capabilities including component-specific
  filters, destination name filters, and notification subscription filters.
- Enables automated brownfield discovery by retrieving all configured
  components when generate_all_configurations is enabled.
- Resolves site IDs to hierarchical site names and event IDs to event names
  for human-readable playbook generation.
- Creates structured playbook files ready for modification and redeployment
  through events_and_notifications_workflow_manager module.
version_added: 6.44.0
extends_documentation_fragment:
- cisco.dnac.workflow_manager_params
author:
- Priyadharshini B (@pbalaku2)
- Madhan Sankaranarayanan (@madhansansel)
options:
  state:
    description:
    - Desired state for module execution controlling playbook generation
      workflow.
    - Only 'gathered' state is supported for retrieving configurations from
      Catalyst Center.
    - The 'gathered' state initiates configuration discovery, API calls,
      transformation, and YAML file generation.
    type: str
    choices: [gathered]
    default: gathered
  config:
    description:
    - A list of filters for generating YAML playbook compatible with the `events_and_notifications_workflow_manager`
      module.
    - Filters specify which components to include in the YAML configuration file.
    - If "components_list" is specified, only those components are included, regardless of the filters.
    type: list
    elements: dict
    required: true
    suboptions:
      file_path:
        description:
        - Absolute or relative path where generated YAML configuration file
          will be saved.
        - If not provided, file is saved in current working directory with
          auto-generated filename.
        - Filename format when auto-generated is
          "<module_name>_playbook_<YYYY-MM-DD_HH-MM-SS>.yml".
        - Example auto-generated filename
          "events_and_notifications_workflow_manager_playbook_2025-04-22_21-43-26.yml".
        - Parent directories are created automatically if they do not exist.
        - File is overwritten if it already exists at the specified path.
        type: str
      generate_all_configurations:
        description:
        - When True, automatically retrieves all events and notifications
          configurations from Catalyst Center.
        - Discovers all webhook destinations, email destinations, syslog
          destinations, SNMP destinations, ITSM settings, and event
          subscriptions.
        - Makes component_specific_filters optional by using default values
          when not provided.
        - Sets default components_list to all supported component types if
          not explicitly specified.
        - Useful for complete brownfield infrastructure documentation and
          discovery workflows.
        - When False, requires explicit component_specific_filters
          configuration with components_list.
        type: bool
        default: false
      component_specific_filters:
        description:
        - Filter configuration controlling which components are included in
          generated YAML playbook.
        - When components_list is specified, only listed components are
          retrieved regardless of other filters.
        - Destination and notification filters provide name-based filtering
          within selected components.
        - Optional when generate_all_configurations is True, uses defaults if
          not provided.
        - Required when generate_all_configurations is False to specify which
          components to retrieve.
        type: dict
        suboptions:
          components_list:
            description:
            - List of component types to include in generated YAML playbook
              file.
            - Each component type corresponds to specific API endpoint and
              configuration structure.
            - Valid component types
              - C(webhook_destinations) - REST webhook destination
                configurations
              - C(email_destinations) - Email destination with SMTP
                settings
              - C(syslog_destinations) - Syslog server configurations
              - C(snmp_destinations) - SNMP trap receiver configurations
              - C(itsm_settings) - ITSM integration connection settings
              - C(webhook_event_notifications) - Webhook event subscription
                configurations
              - C(email_event_notifications) - Email event subscription
                configurations
              - C(syslog_event_notifications) - Syslog event subscription
                configurations
            - When not specified with generate_all_configurations True, all
              component types are included.
            - Order of components in list determines order in generated YAML
              playbook structure.
            type: list
            elements: str
            choices:
            - webhook_destinations
            - email_destinations
            - syslog_destinations
            - snmp_destinations
            - itsm_settings
            - webhook_event_notifications
            - email_event_notifications
            - syslog_event_notifications
          destination_filters:
            description:
            - Filters for destination configurations based on name or type
              matching.
            - Applies to webhook_destinations, email_destinations,
              syslog_destinations, and snmp_destinations components.
            - When destination_names provided and matches found, only matching
              destinations are included.
            - When destination_names provided but no matches found, all
              destinations are included for comprehensive coverage.
            - Destination type filters currently informational, type-specific
              filtering handled by components_list.
            type: dict
            suboptions:
              destination_names:
                description:
                - List of exact destination names to filter from retrieved
                  configurations.
                - Names must match exactly as configured in Catalyst Center
                  (case-sensitive).
                - Applies smart filtering - includes all destinations when
                  specified names not found.
                - Works across all destination types selected in
                  components_list.
                - Empty list or not specified retrieves all destinations for
                  selected component types.
                type: list
                elements: str
              destination_types:
                description:
                - List of destination types for documentation and validation
                  purposes.
                - Valid types correspond to component categories - webhook,
                  email, syslog, snmp.
                - Type-specific filtering achieved through components_list
                  selection.
                - Included for playbook clarity and future extensibility.
                type: list
                elements: str
                choices: [webhook, email, syslog, snmp]
          notification_filters:
            description:
            - Filters for event notification subscription configurations based
              on name or type.
            - Applies to webhook_event_notifications,
              email_event_notifications, and syslog_event_notifications.
            - When subscription_names provided, filters notifications to
              include only matching subscriptions.
            - Notification type filters align with components_list selection
              for type-specific retrieval.
            type: dict
            suboptions:
              subscription_names:
                description:
                - List of exact event subscription names to filter from
                  retrieved configurations.
                - Names must match exactly as configured in Catalyst Center
                  event subscriptions.
                - Filters webhook, email, and syslog event notifications based
                  on subscription name.
                - Empty list or not specified retrieves all event subscriptions
                  for selected types.
                type: list
                elements: str
              notification_types:
                description:
                - List of notification types for documentation and filtering
                  context.
                - Valid types - webhook, email, syslog corresponding to event
                  subscription types.
                - Type-specific filtering primarily controlled through
                  components_list selection.
                - Included for playbook documentation and future filtering
                  enhancements.
                type: list
                elements: str
                choices: [webhook, email, syslog]
          itsm_filters:
            description:
            - Filters for ITSM integration settings based on instance name
              matching.
            - Applies only to itsm_settings component when included in
              components_list.
            - Filters ITSM integration instances by configured instance names.
            - Empty list or not specified retrieves all configured ITSM
              integration instances.
            type: dict
            suboptions:
              instance_names:
                description:
                - List of exact ITSM instance names to filter from retrieved
                  configurations.
                - Names must match exactly as configured in Catalyst Center
                  ITSM integration settings.
                - Filters ServiceNow, BMC Remedy, or custom ITSM integration
                  instances.
                - Empty list or not specified retrieves all ITSM integration
                  instances.
                type: list
                elements: str
requirements:
- dnacentersdk >= 2.7.2
- python >= 3.9
notes:
- SDK Methods used are
    - event_management.Events.get_webhook_destination
    - event_management.Events.get_email_destination
    - event_management.Events.get_syslog_destination
    - event_management.Events.get_snmp_destination
    - event_management.Events.get_all_itsm_integration_settings
    - event_management.Events.get_rest_webhook_event_subscriptions
    - event_management.Events.get_email_event_subscriptions
    - event_management.Events.get_syslog_event_subscriptions
    - event_management.Events.get_event_artifacts
    - sites.Sites.get_site
- Paths used are
    - GET /dna/system/api/v1/event/webhook
    - GET /dna/system/api/v1/event/email-config
    - GET /dna/system/api/v1/event/syslog-config
    - GET /dna/system/api/v1/event/snmp-config
    - GET /dna/system/api/v1/event/itsm-integration-setting
    - GET /dna/system/api/v1/event/subscription/rest
    - GET /dna/system/api/v1/event/subscription/email
    - GET /dna/system/api/v1/event/subscription/syslog
    - GET /dna/intent/api/v1/event-artifact
    - GET /dna/intent/api/v1/site
- Minimum Catalyst Center version required is 2.3.5.3 for events and
  notifications APIs.
- Module performs read-only operations and does not modify Catalyst Center
  configurations.
- Generated YAML files contain password placeholders marked as
  "***REDACTED***" for security.
- Site IDs are automatically resolved to hierarchical site names for
  readability.
- Event IDs are automatically resolved to event names using Event Artifacts
  API.
- Pagination is automatically handled for large datasets in webhook, SNMP,
  and event subscriptions.
- Module supports both check mode and normal execution mode with identical
  behavior.
- Generated playbooks are compatible with
  events_and_notifications_workflow_manager module v6.44.0+.

seealso:
- module: cisco.dnac.events_and_notifications_workflow_manager
  description: Module to manage Events and Notifications configurations in Cisco Catalyst Center.
"""

EXAMPLES = r"""
- name: Generate YAML Configuration with all events and notifications components
  cisco.dnac.brownfield_events_and_notifications_playbook_generator:
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
        file_path: "/tmp/catc_events_notifications_config.yaml"

- name: Generate YAML Configuration for destinations only
  cisco.dnac.brownfield_events_and_notifications_playbook_generator:
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
      - file_path: "/tmp/catc_destinations_config.yaml"
        component_specific_filters:
          components_list: ["webhook_destinations", "email_destinations", "syslog_destinations"]

- name: Generate YAML Configuration for specific webhook destinations
  cisco.dnac.brownfield_events_and_notifications_playbook_generator:
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
      - file_path: "/tmp/catc_webhook_config.yaml"
        component_specific_filters:
          components_list: ["webhook_destinations", "webhook_event_notifications"]
          destination_filters:
            destination_names: ["webhook-dest-1", "webhook-dest-2"]
            destination_types: ["webhook"]

- name: Generate YAML Configuration with combined filters
  cisco.dnac.brownfield_events_and_notifications_playbook_generator:
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
      - file_path: "/tmp/combined_filters_config.yaml"
        component_specific_filters:
          components_list: ["webhook_destinations", "webhook_event_notifications", "email_destinations", "email_event_notifications"]
          destination_filters:
            destination_names: ["Production Webhook", "Alert Email Server"]
            destination_types: ["webhook", "email"]
          notification_filters:
            subscription_names: ["Critical System Alerts", "Network Health Monitoring"]
            notification_types: ["webhook", "email"]
"""

RETURN = r"""
# Case_1: Success Scenario
response_1:
  description: A dictionary with the response returned by the Cisco Catalyst Center
  returned: always
  type: dict
  sample: >
    {
      "msg": "YAML configuration file generated successfully for module 'events_and_notifications_workflow_manager'",
      "response":
      {
          "components_processed": 1,
          "components_skipped": 0,
          "configurations_count": 1,
          "file_path": "/Users/priyadharshini/Downloads/events_and_notifications_playbook",
          "message": "YAML configuration file generated successfully for module 'events_and_notifications_workflow_manager'",
          "status": "success"
      },
      "status": "success"
    }
# Case_2: Idempotent Scenario
response_2:
  description: A string with the response returned by the Cisco Catalyst Center
  returned: always
  type: list
  sample: >
    {
      "msg": "No configurations found to generate. Verify that the components exist and have data.",
      "response": {
          "components_processed": 0,
          "components_skipped": 1,
          "configurations_count": 0,
          "message": "No configurations found to generate. Verify that the components exist and have data.",
          "status": "success"
      },
      "status": "success"
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


class EventsNotificationsPlaybookGenerator(DnacBase, BrownFieldHelper):
    """
    A class for generating playbook files for events and notifications configurations in Cisco Catalyst Center using the GET APIs.
    """

    def __init__(self, module):
        """
        Initialize an instance of the EventsNotificationsPlaybookGenerator class.

        Description:
            Sets up the class instance with module configuration, supported states,
            module schema mapping, and module name for events and notifications workflow
            operations in Cisco Catalyst Center. Initializes the get_diff_state_apply
            mapping for handling different operational states.

        Args:
            module (AnsibleModule): The Ansible module instance containing configuration
                parameters and methods for module execution.

        Returns:
            None: This is a constructor method that initializes the instance.
        """
        self.supported_states = ["gathered"]
        self.get_diff_state_apply = {"gathered": self.get_diff_gathered}
        super().__init__(module)
        self.module_schema = self.events_notifications_workflow_manager_mapping()
        self.module_name = "events_and_notifications_workflow_manager"
        self.final_webhook_configs = []
        self.final_email_configs = []
        self.final_syslog_configs = []
        self.final_snmp_configs = []
        self.final_itsm_configs = []
        self.final_notification_configs = []

    def validate_input(self):
        """
        Class for generating YAML playbooks from Events and Notifications configurations.

        Description:
            Orchestrates comprehensive brownfield discovery and YAML playbook generation workflow
            for Cisco Catalyst Center Events and Notifications infrastructure by retrieving
            existing configurations through REST APIs, transforming API responses to playbook-
            compatible format, applying intelligent filtering based on component types and names,
            resolving identifiers to human-readable names (sites, events, destinations), redacting
            sensitive credentials for security, and generating structured YAML files ready for
            modification and redeployment through events_and_notifications_workflow_manager module.

        Core Capabilities:
            - Retrieves webhook destinations with URL, headers, SSL, and proxy configurations
            - Fetches email destinations with primary/secondary SMTP server settings
            - Discovers syslog destinations with server addresses, protocols, and ports
            - Collects SNMP destinations with version, community, authentication details
            - Gathers ITSM integration settings with connection and authentication parameters
            - Retrieves webhook event subscriptions with site and event associations
            - Fetches email event subscriptions with sender, recipient, and subject details
            - Discovers syslog event subscriptions with destination mappings
            - Supports component-specific filtering by destination and subscription names
            - Handles pagination automatically for large configuration datasets
            - Resolves site UUIDs to hierarchical site names using Sites API
            - Converts event IDs to event names using Event Artifacts API
            - Redacts passwords and sensitive data with "***REDACTED***" placeholder
            - Transforms camelCase API responses to snake_case playbook parameters
            - Removes null values for clean YAML output without unnecessary fields
            - Generates timestamped filenames when custom path not provided
            - Creates parent directories automatically for specified file paths
            - Validates component selections against supported configuration types
            - Provides comprehensive operation statistics in module response

        Supported Operations:
            - Gathered state for configuration retrieval and YAML generation
            - Generate all mode for complete infrastructure documentation
            - Selective component mode for targeted configuration extraction
            - Name-based filtering with smart fallback to all configurations
            - Multi-file generation with different component selections per file

        API Integration:
            - event_management.Events.get_webhook_destination (paginated)
            - event_management.Events.get_email_destination
            - event_management.Events.get_syslog_destination
            - event_management.Events.get_snmp_destination (paginated)
            - event_management.Events.get_all_itsm_integration_settings
            - event_management.Events.get_rest_webhook_event_subscriptions (paginated)
            - event_management.Events.get_email_event_subscriptions
            - event_management.Events.get_syslog_event_subscriptions (paginated)
            - event_management.Events.get_event_artifacts (for event name resolution)
            - sites.Sites.get_site (for site name resolution)

        Data Transformation:
            - Maps API response keys to playbook parameter names via temp_spec
            - Applies transformation functions for password redaction and ID resolution
            - Handles nested configurations (SMTP settings, headers, resource groups)
            - Preserves OrderedDict structure for consistent YAML field ordering
            - Filters null values while maintaining essential configuration structures
            - Extracts email addresses, subjects, and instance details from endpoints
            - Processes site information from filters and resource domain structures
            - Resolves connector types to determine destination and notification mappings

        Filtering Capabilities:
            - components_list: Selects which configuration types to include
            - destination_names: Filters destinations by exact name matching
            - subscription_names: Filters event subscriptions by name
            - instance_names: Filters ITSM integration instances by name
            - Smart fallback: Returns all configs when filters produce no matches
            - Comprehensive coverage: Ensures no data loss during filtering process

        Output Format:
            - YAML playbook compatible with events_and_notifications_workflow_manager
            - Organized by component type with singular keys (webhook_destination)
            - Each configuration as separate OrderedDict entry in config list
            - Human-readable site names instead of UUIDs for better clarity
            - Event names instead of IDs for improved playbook readability
            - Passwords redacted as "***REDACTED***" for security compliance
            - Clean structure without null values for minimal file size
            - Proper indentation and formatting for easy manual modification

        Minimum Requirements:
            - Cisco Catalyst Center version 2.3.5.3 or higher
            - Cisco Catalyst Center Center SDK 2.7.2 or higher for API compatibility
            - Python 3.9 or higher for OrderedDict and type hint support
            - Read access to Events and Notifications APIs in Catalyst Center
            - Network connectivity to Catalyst Center management interface

        Attributes:
            module_name (str): Target module name for generated playbooks
                (events_and_notifications_workflow_manager)
            module_schema (dict): Comprehensive mapping of components to API details,
                filters, specifications, and getter functions
            supported_states (list): Operational states supported by the class
                (currently only 'gathered' for configuration retrieval)
            get_diff_state_apply (dict): Mapping of states to execution methods
                for workflow orchestration

        Methods:
            validate_input(): Validates playbook configuration parameters against schema
            get_want(): Transforms input config to internal want structure for processing
            get_diff_gathered(): Orchestrates YAML generation workflow execution
            yaml_config_generator(): Coordinates component retrieval and file generation
            generate_playbook_structure(): Formats configurations into playbook structure
            modify_parameters(): Transforms API responses using specifications

            Component Retrieval Methods:
            get_webhook_destinations(): Retrieves and filters webhook configurations
            get_email_destinations(): Retrieves and filters email configurations
            get_syslog_destinations(): Retrieves and filters syslog configurations
            get_snmp_destinations(): Retrieves and filters SNMP configurations
            get_itsm_settings(): Retrieves and filters ITSM integration settings
            get_webhook_event_notifications(): Retrieves webhook event subscriptions
            get_email_event_notifications(): Retrieves email event subscriptions
            get_syslog_event_notifications(): Retrieves syslog event subscriptions

            Helper Methods:
            get_all_webhook_destinations(): Paginated webhook destination retrieval
            get_all_email_destinations(): Email destination retrieval from API
            get_all_syslog_destinations(): Syslog destination retrieval from API
            get_all_snmp_destinations(): Paginated SNMP destination retrieval
            get_all_itsm_settings(): ITSM settings retrieval from API
            get_all_webhook_event_notifications(): Paginated webhook notification retrieval
            get_all_email_event_notifications(): Email notification retrieval from API
            get_all_syslog_event_notifications(): Paginated syslog notification retrieval

            Transformation Functions:
            redact_password(): Masks sensitive password information
            extract_event_names(): Resolves event IDs to human-readable names
            extract_sites_from_filter(): Extracts and resolves site information
            get_event_name_from_api(): Queries Event Artifacts API for names
            get_site_name_by_id(): Resolves site UUID to hierarchical name
            extract_webhook_destination_name(): Extracts webhook destination from endpoints
            extract_syslog_destination_name(): Extracts syslog destination from endpoints
            extract_sender_email(): Extracts sender email from email configurations
            extract_recipient_emails(): Extracts recipient list from email configurations
            extract_subject(): Extracts email subject from configurations
            create_instance_name(): Creates instance identifier for email notifications
            create_instance_description(): Creates instance description for emails

            Specification Methods:
            events_notifications_workflow_manager_mapping(): Constructs component mapping
            webhook_destinations_temp_spec(): Defines webhook transformation rules
            email_destinations_temp_spec(): Defines email transformation rules
            syslog_destinations_temp_spec(): Defines syslog transformation rules
            snmp_destinations_temp_spec(): Defines SNMP transformation rules
            itsm_settings_temp_spec(): Defines ITSM transformation rules
            webhook_event_notifications_temp_spec(): Defines webhook notification rules
            email_event_notifications_temp_spec(): Defines email notification rules
            syslog_event_notifications_temp_spec(): Defines syslog notification rules

        Inheritance:
            DnacBase: Provides core DNA Center SDK integration and helper methods
            BrownFieldHelper: Provides YAML generation utilities and file operations

        Returns:
            Generated YAML playbook files with statistics including:
                - components_processed: Count of successfully processed component types
                - components_skipped: Count of skipped components due to errors
                - configurations_count: Total individual configuration items generated
                - file_path: Absolute path to generated YAML playbook file
                - status: Success or failure indication with descriptive message
        """
        self.log(
            "Starting validation of input configuration parameters for events and notifications "
            "playbook generation. Validation includes schema compliance, allowed keys checking, "
            "nested filter validation, and minimum requirements enforcement.",
            "DEBUG"
        )

        # Check if configuration is available
        if not self.config:
            self.status = "success"
            self.msg = (
                "Configuration is not available in the playbook for validation. No parameters "
                "provided for events and notifications generation workflow."
            )
            self.log(self.msg, "INFO")
            return self

        # Expected schema for configuration parameters
        temp_spec = {
            "file_path": {"type": "str", "required": False},
            "generate_all_configurations": {"type": "bool", "required": False, "default": False},
            "component_specific_filters": {"type": "dict", "required": False},
            "global_filters": {"type": "dict", "required": False},
        }

        # Define allowed nested keys for component_specific_filters
        allowed_component_filter_keys = {
            "components_list",
            "destination_filters",
            "notification_filters",
            "itsm_filters"
        }

        # Define allowed nested keys for each filter type
        allowed_destination_filter_keys = {
            "destination_names",
            "destination_types"
        }

        allowed_notification_filter_keys = {
            "subscription_names",
            "notification_types"
        }

        allowed_itsm_filter_keys = {
            "instance_names"
        }

        allowed_keys = set(temp_spec.keys())

        self.log(
            "Starting iteration over {0} configuration item(s) for validation. Each item will "
            "be checked for type compliance, allowed keys, and nested structure validity.".format(
                len(self.config)
            ),
            "DEBUG"
        )

        # Validate that only allowed keys are present in the configuration
        for config_index, config_item in enumerate(self.config, start=1):
            self.log(
                "Validating configuration item {0}/{1}. Checking item type and structure for "
                "compliance with expected dictionary format.".format(
                    config_index, len(self.config)
                ),
                "DEBUG"
            )
            if not isinstance(config_item, dict):
                self.msg = (
                    "Configuration item {0} must be a dictionary, got: {1}. Each configuration "
                    "item must be a dictionary containing generation parameters and filters.".format(
                        config_index, type(config_item).__name__
                    )
                )
                self.set_operation_result("failed", False, self.msg, "ERROR")
                return self

            # Check for invalid keys at top level
            config_keys = set(config_item.keys())
            self.log(
                "Configuration item {0} top-level keys validation passed. All keys {1} are "
                "allowed. Proceeding with nested component_specific_filters validation.".format(
                    config_index, list(config_keys)
                ),
                "DEBUG"
            )
            invalid_keys = config_keys - allowed_keys

            if invalid_keys:
                self.msg = (
                    "Invalid parameters found in playbook configuration: {0}. "
                    "Only the following parameters are allowed: {1}. "
                    "Please remove the invalid parameters and try again.".format(
                        list(invalid_keys), list(allowed_keys)
                    )
                )
                self.set_operation_result("failed", False, self.msg, "ERROR")
                return self

            # Validate nested component_specific_filters structure
            component_filters = config_item.get("component_specific_filters")
            if component_filters and isinstance(component_filters, dict):
                self.log(
                    "Configuration item {0} contains component_specific_filters with {1} key(s): "
                    "{2}. Validating nested filter keys against allowed component filter keys.".format(
                        config_index, len(component_filters), list(component_filters.keys())
                    ),
                    "DEBUG"
                )

                # Check for invalid keys in component_specific_filters
                component_filter_keys = set(component_filters.keys())
                invalid_component_keys = component_filter_keys - allowed_component_filter_keys

                if invalid_component_keys:
                    self.msg = (
                        "Invalid parameters found in 'component_specific_filters': {0}. "
                        "Only the following parameters are allowed: {1}. "
                        "Please remove the invalid parameters and try again.".format(
                            list(invalid_component_keys), list(allowed_component_filter_keys)
                        )
                    )
                    self.set_operation_result("failed", False, self.msg, "ERROR")
                    return self

                self.log(
                    "Component filter keys validation passed for item {0}. All keys {1} are "
                    "allowed. Proceeding with destination_filters validation.".format(
                        config_index, list(component_filter_keys)
                    ),
                    "DEBUG"
                )

                # Validate destination_filters
                destination_filters = component_filters.get("destination_filters")
                if destination_filters:
                    self.log(
                        "Configuration item {0} contains destination_filters. Type: {1}. "
                        "Processing filter items for key validation supporting both dict and "
                        "list formats.".format(config_index, type(destination_filters).__name__),
                        "DEBUG"
                    )
                    filters_to_check = []
                    if isinstance(destination_filters, dict):
                        filters_to_check = [destination_filters]

                    elif isinstance(destination_filters, list):
                        filters_to_check = destination_filters

                    self.log(
                        "Destination filters converted to list format with {0} filter item(s) "
                        "for validation. Iterating through items to check allowed keys.".format(
                            len(filters_to_check)
                        ),
                        "DEBUG"
                    )

                    # Validate each filter in the list/dict
                    for filter_index, filter_item in enumerate(filters_to_check, start=1):
                        self.log(
                            "Validating destination filter item {0}/{1} with keys: {2}. Checking "
                            "against allowed destination filter keys.".format(
                                filter_index, len(filters_to_check), list(filter_item.keys())
                            ),
                            "DEBUG"
                        )
                        dest_filter_keys = set(filter_item.keys())
                        invalid_dest_keys = dest_filter_keys - allowed_destination_filter_keys

                        if invalid_dest_keys:
                            self.msg = (
                                "Invalid parameters found in 'destination_filters': {0}. "
                                "Only the following parameters are allowed: {1}. "
                                "Please remove the invalid parameters and try again.".format(
                                    list(invalid_dest_keys), list(allowed_destination_filter_keys)
                                )
                            )
                            self.set_operation_result("failed", False, self.msg, "ERROR")
                            return self
                    self.log(
                        "Destination filter item {0}/{1} validation passed. All keys {2} are "
                        "allowed.".format(
                            filter_index, len(filters_to_check), list(dest_filter_keys)
                        ),
                        "DEBUG"
                    )

                # Validate notification_filters (similar fix)
                notification_filters = component_filters.get("notification_filters")
                if notification_filters:
                    # Handle both dict and list formats
                    filters_to_check = []
                    if isinstance(notification_filters, dict):
                        filters_to_check = [notification_filters]

                    elif isinstance(notification_filters, list):
                        filters_to_check = notification_filters

                    self.log(
                        "Notification filters converted to list format with {0} filter item(s) "
                        "for validation. Iterating through items to check allowed keys.".format(
                            len(filters_to_check)
                        ),
                        "DEBUG"
                    )

                    # Validate each filter in the list/dict
                    for filter_index, filter_item in enumerate(filters_to_check, start=1):
                        self.log(
                            "Validating notification filter item {0}/{1} with keys: {2}. Checking "
                            "against allowed notification filter keys.".format(
                                filter_index, len(filters_to_check), list(filter_item.keys())
                            ),
                            "DEBUG"
                        )
                        notif_filter_keys = set(filter_item.keys())
                        invalid_notif_keys = notif_filter_keys - allowed_notification_filter_keys
                        if invalid_notif_keys:
                            self.msg = (
                                "Invalid parameters found in 'notification_filters': {0}. "
                                "Only the following parameters are allowed: {1}. "
                                "Please remove the invalid parameters and try again.".format(
                                    list(invalid_notif_keys), list(allowed_notification_filter_keys)
                                )
                            )
                            self.set_operation_result("failed", False, self.msg, "ERROR")
                            return self
                    self.log(
                        "Notification filter item {0}/{1} validation passed. All keys {2} are "
                        "allowed.".format(
                            filter_index, len(filters_to_check), list(notif_filter_keys)
                        ),
                        "DEBUG"
                    )

                # Validate itsm_filters (similar fix)
                itsm_filters = component_filters.get("itsm_filters")
                if itsm_filters:
                    self.log(
                        "Configuration item {0} contains itsm_filters. Type: {1}. Processing "
                        "filter items for key validation supporting both dict and list "
                        "formats.".format(config_index, type(itsm_filters).__name__),
                        "DEBUG"
                    )
                    filters_to_check = []
                    if isinstance(itsm_filters, dict):
                        filters_to_check = [itsm_filters]

                    elif isinstance(itsm_filters, list):
                        filters_to_check = itsm_filters

                    self.log(
                        "ITSM filters converted to list format with {0} filter item(s) for "
                        "validation. Iterating through items to check allowed keys.".format(
                            len(filters_to_check)
                        ),
                        "DEBUG"
                    )

                    # Validate each filter in the list/dict
                    for filter_index, filter_item in enumerate(filters_to_check, start=1):
                        self.log(
                            "Validating ITSM filter item {0}/{1} with keys: {2}. Checking against "
                            "allowed ITSM filter keys.".format(
                                filter_index, len(filters_to_check), list(filter_item.keys())
                            ),
                            "DEBUG"
                        )
                        itsm_filter_keys = set(filter_item.keys())
                        invalid_itsm_keys = itsm_filter_keys - allowed_itsm_filter_keys

                        if invalid_itsm_keys:
                            self.msg = (
                                "Invalid parameters found in 'itsm_filters': {0}. "
                                "Only the following parameters are allowed: {1}. "
                                "Please remove the invalid parameters and try again.".format(
                                    list(invalid_itsm_keys), list(allowed_itsm_filter_keys)
                                )
                            )
                            self.set_operation_result("failed", False, self.msg, "ERROR")
                            return self
                    self.log(
                        "ITSM filter item {0}/{1} validation passed. All keys {2} are "
                        "allowed.".format(
                            filter_index, len(filters_to_check), list(itsm_filter_keys)
                        ),
                        "DEBUG"
                    )

        self.log(
            "Configuration item {0}/{1} nested filter validation completed successfully. All "
            "nested keys validated against allowed key sets.".format(
                config_index, len(self.config)
            ),
            "DEBUG"
        )

        self.log(
            "All {0} configuration item(s) passed top-level and nested key validation. "
            "Proceeding with minimum requirements validation via validate_minimum_requirements().".format(
                len(self.config)
            ),
            "DEBUG"
        )

        self.log("Validating minimum requirements against provided config: {0}".format(self.config), "DEBUG")
        self.validate_minimum_requirements(self.config)

        # Validate params
        valid_temp, invalid_params = validate_list_of_dicts(self.config, temp_spec)

        if invalid_params:
            self.msg = "Invalid parameters in playbook: {0}".format(invalid_params)
            self.set_operation_result("failed", False, self.msg, "ERROR")
            return self

        self.log(
            "Schema validation completed successfully. All parameters conform to expected types "
            "and requirements. Validated configuration: {0}".format(str(valid_temp)),
            "DEBUG"
        )

        # Set the validated configuration and update the result with success status
        self.validated_config = valid_temp
        self.msg = "Successfully validated playbook configuration parameters using 'validated_input': {0}".format(
            str(valid_temp)
        )
        self.set_operation_result("success", False, self.msg, "INFO")
        self.log(
            "Input validation completed successfully. Returning self instance with validated_config "
            "populated containing {0} configuration item(s) ready for processing in generation "
            "workflow.".format(len(self.validated_config)),
            "INFO"
        )
        return self

    def events_notifications_workflow_manager_mapping(self):
        """
        Constructs comprehensive mapping configuration for events and notifications workflow components.

        Description:
            Creates a structured mapping that defines all supported events and notifications
            workflow components, their associated API functions, filter specifications, and
            processing functions. This mapping serves as the central configuration registry
            for the events and notifications workflow orchestration process.

        Args:
            None: Uses class methods and instance configuration.

        Returns:
                dict: A comprehensive mapping dictionary containing:
                    - network_elements (dict): Component configurations with API details including:
                        - filters (dict): Filter schemas defining allowed parameter types, elements,
                        choices, and requirement flags for each component type
                        - reverse_mapping_function (callable): Function reference for transforming
                        API response data to YAML format using component-specific specifications
                        - api_function (str): Catalyst Center API function name for component
                        data retrieval
                        - api_family (str): API family identifier (event_management) for routing
                        API calls
                        - get_function_name (callable): Function reference for retrieving and
                        processing component data with filtering
                    - global_filters (dict): Global filter configuration options (currently empty
                    as component-specific filters handle all filtering requirements)
        """
        self.log(
            "Starting mapping configuration for events and notifications workflow manager. "
            "Defining component metadata, API associations, filter schemas, and function "
            "references for supported component types.",
            "DEBUG"
        )
        network_elements_mapping = {
            "webhook_destinations": {
                "filters": {
                    "destination_names": {"type": "list", "elements": "str", "required": False},
                    "destination_types": {
                        "type": "list",
                        "elements": "str",
                        "required": False,
                        "choices": ["webhook"]
                    },
                },
                "reverse_mapping_function": self.webhook_destinations_reverse_mapping_function,
                "api_function": "get_webhook_destination",
                "api_family": "event_management",
                "get_function_name": self.get_webhook_destinations,
            },
            "email_destinations": {
                "filters": {
                    "destination_names": {"type": "list", "elements": "str", "required": False},
                    "destination_types": {
                        "type": "list",
                        "elements": "str",
                        "required": False,
                        "choices": ["email"]
                    },
                },
                "reverse_mapping_function": self.email_destinations_reverse_mapping_function,
                "api_function": "get_email_destination",
                "api_family": "event_management",
                "get_function_name": self.get_email_destinations,
            },
            "syslog_destinations": {
                "filters": {
                    "destination_names": {"type": "list", "elements": "str", "required": False},
                    "destination_types": {
                        "type": "list",
                        "elements": "str",
                        "required": False,
                        "choices": ["syslog"]
                    },
                },
                "reverse_mapping_function": self.syslog_destinations_reverse_mapping_function,
                "api_function": "get_syslog_destination",
                "api_family": "event_management",
                "get_function_name": self.get_syslog_destinations,
            },
            "snmp_destinations": {
                "filters": {
                    "destination_names": {"type": "list", "elements": "str", "required": False},
                    "destination_types": {
                        "type": "list",
                        "elements": "str",
                        "required": False,
                        "choices": ["snmp"]
                    },
                },
                "reverse_mapping_function": self.snmp_destinations_reverse_mapping_function,
                "api_function": "get_snmp_destination",
                "api_family": "event_management",
                "get_function_name": self.get_snmp_destinations,
            },
            "itsm_settings": {
                "filters": {
                    "instance_names": {"type": "list", "elements": "str", "required": False},
                },
                "reverse_mapping_function": self.itsm_settings_reverse_mapping_function,
                "api_function": "get_all_itsm_integration_settings",
                "api_family": "event_management",
                "get_function_name": self.get_itsm_settings,
            },
            "webhook_event_notifications": {
                "filters": {
                    "subscription_names": {"type": "list", "elements": "str", "required": False},
                    "notification_types": {
                        "type": "list",
                        "elements": "str",
                        "required": False,
                        "choices": ["webhook"]
                    },
                },
                "reverse_mapping_function": self.webhook_event_notifications_reverse_mapping_function,
                "api_function": "get_rest_webhook_event_subscriptions",
                "api_family": "event_management",
                "get_function_name": self.get_webhook_event_notifications,
            },
            "email_event_notifications": {
                "filters": {
                    "subscription_names": {"type": "list", "elements": "str", "required": False},
                    "notification_types": {
                        "type": "list",
                        "elements": "str",
                        "required": False,
                        "choices": ["email"]
                    },
                },
                "reverse_mapping_function": self.email_event_notifications_reverse_mapping_function,
                "api_function": "get_email_event_subscriptions",
                "api_family": "event_management",
                "get_function_name": self.get_email_event_notifications,
            },
            "syslog_event_notifications": {
                "filters": {
                    "subscription_names": {"type": "list", "elements": "str", "required": False},
                    "notification_types": {
                        "type": "list",
                        "elements": "str",
                        "required": False,
                        "choices": ["syslog"]
                    },
                },
                "reverse_mapping_function": self.syslog_event_notifications_reverse_mapping_function,
                "api_function": "get_syslog_event_subscriptions",
                "api_family": "event_management",
                "get_function_name": self.get_syslog_event_notifications,
            },
        }
        self.log(
            "Defining global filters configuration for cross-component filtering. Currently "
            "empty as component-specific filters provide sufficient granularity for all "
            "filtering requirements in events and notifications workflow.",
            "DEBUG"
        )

        global_filters_config = {}

        mapping_result = {
            "network_elements": network_elements_mapping,
            "global_filters": global_filters_config,
        }

        self.log(
            f"Events and notifications workflow manager mapping completed successfully. "
            f"Mapping includes {len(network_elements_mapping)} network elements with "
            f"complete API associations, filter schemas, and processing functions ready "
            f"for YAML generation workflow orchestration.",
            "INFO"
        )

        return mapping_result

    # Reverse mapping functions for temp specs
    def webhook_destinations_reverse_mapping_function(self):
        """Returns the reverse mapping specification for webhook destination details."""
        self.log("Generating reverse mapping specification for webhook destination details", "DEBUG")
        return self.webhook_destinations_temp_spec()

    def email_destinations_reverse_mapping_function(self):
        """Returns the reverse mapping specification for email destination details."""
        self.log("Generating reverse mapping specification for email destination details", "DEBUG")
        return self.email_destinations_temp_spec()

    def syslog_destinations_reverse_mapping_function(self):
        """Returns the reverse mapping specification for syslog destination details."""
        self.log("Generating reverse mapping specification for syslog destination details", "DEBUG")
        return self.syslog_destinations_temp_spec()

    def snmp_destinations_reverse_mapping_function(self):
        """Returns the reverse mapping specification for SNMP destination details."""
        self.log("Generating reverse mapping specification for SNMP destination details", "DEBUG")
        return self.snmp_destinations_temp_spec()

    def itsm_settings_reverse_mapping_function(self):
        """Returns the reverse mapping specification for ITSM settings details."""
        self.log("Generating reverse mapping specification for ITSM settings details", "DEBUG")
        return self.itsm_settings_temp_spec()

    def webhook_event_notifications_reverse_mapping_function(self):
        """Returns the reverse mapping specification for webhook event notification details."""
        self.log("Generating reverse mapping specification for webhook event notification details", "DEBUG")
        return self.webhook_event_notifications_temp_spec()

    def email_event_notifications_reverse_mapping_function(self):
        """Returns the reverse mapping specification for email event notification details."""
        self.log("Generating reverse mapping specification for email event notification details", "DEBUG")
        return self.email_event_notifications_temp_spec()

    def syslog_event_notifications_reverse_mapping_function(self):
        """Returns the reverse mapping specification for syslog event notification details."""
        self.log("Generating reverse mapping specification for syslog event notification details", "DEBUG")
        return self.syslog_event_notifications_temp_spec()

    def webhook_destinations_temp_spec(self):
        """
        Constructs detailed specification for webhook destination data transformation.

        Description:
            Creates a comprehensive specification that defines how webhook destination
            API response fields should be mapped, transformed, and structured in the final
            YAML configuration. Includes handling for HTTP methods, SSL certificates,
            headers, and proxy routing configurations.

        Args:
            None: Uses logging methods from the instance.

        Returns:
            OrderedDict: A detailed specification containing field mappings, data types,
            and nested structure definitions for webhook destination configurations.
        """
        self.log("Generating temporary specification for webhook destination details.", "DEBUG")
        return OrderedDict({
            "name": {"type": "str", "source_key": "name"},
            "description": {"type": "str", "source_key": "description"},
            "url": {"type": "str", "source_key": "url"},
            "method": {"type": "str", "source_key": "method"},
            "trust_cert": {"type": "bool", "source_key": "trustCert"},
            "is_proxy_route": {"type": "bool", "source_key": "isProxyRoute"},
            "headers": {
                "type": "list",
                "source_key": "headers",
                "options": OrderedDict({
                    "name": {"type": "str", "source_key": "name"},
                    "value": {"type": "str", "source_key": "value"},
                    "default_value": {"type": "str", "source_key": "defaultValue"},
                    "encrypt": {"type": "bool", "source_key": "encrypt"},
                })
            },
        })

    def email_destinations_temp_spec(self):
        """
        Constructs detailed specification for email destination data transformation.

        Description:
            Creates a comprehensive specification that defines how email destination
            API response fields should be mapped, transformed, and structured in the final
            YAML configuration. Includes handling for primary and secondary SMTP configurations,
            authentication details, and password redaction for security.

        Args:
            None: Uses logging methods from the instance.

        Returns:
            OrderedDict: A detailed specification containing field mappings, data types,
            and nested SMTP configuration structures for email destination configurations.
        """
        self.log("Generating temporary specification for email destination details.", "DEBUG")
        return OrderedDict({
            "sender_email": {"type": "str", "source_key": "fromEmail"},
            "recipient_email": {"type": "str", "source_key": "toEmail"},
            "subject": {"type": "str", "source_key": "subject"},
            "primary_smtp_config": {
                "type": "dict",
                "source_key": "primarySMTPConfig",
                "options": OrderedDict({
                    "server_address": {"type": "str", "source_key": "hostName"},
                    "smtp_type": {"type": "str", "source_key": "smtpType"},
                    "port": {"type": "str", "source_key": "port"},
                    "username": {"type": "str", "source_key": "userName"},
                    "password": {"type": "str", "source_key": "password", "transform": self.redact_password},
                })
            },
            "secondary_smtp_config": {
                "type": "dict",
                "source_key": "secondarySMTPConfig",
                "options": OrderedDict({
                    "server_address": {"type": "str", "source_key": "hostName"},
                    "smtp_type": {"type": "str", "source_key": "smtpType"},
                    "port": {"type": "str", "source_key": "port"},
                    "username": {"type": "str", "source_key": "userName"},
                    "password": {"type": "str", "source_key": "password", "transform": self.redact_password},
                })
            },
        })

    def syslog_destinations_temp_spec(self):
        """
        Constructs detailed specification for syslog destination data transformation.

        Description:
            Creates a comprehensive specification that defines how syslog destination
            API response fields should be mapped, transformed, and structured in the final
            YAML configuration. Includes handling for server addresses, protocols (UDP/TCP),
            and port configurations.

        Args:
            None: Uses logging methods from the instance.

        Returns:
            OrderedDict: A detailed specification containing field mappings, data types,
            and protocol configuration structures for syslog destination configurations.
        """
        self.log("Generating temporary specification for syslog destination details.", "DEBUG")
        return OrderedDict({
            "name": {"type": "str", "source_key": "name"},
            "description": {"type": "str", "source_key": "description"},
            "server_address": {"type": "str", "source_key": "host"},
            "protocol": {"type": "str", "source_key": "protocol"},
            "port": {"type": "int", "source_key": "port"},
        })

    def snmp_destinations_temp_spec(self):
        """
        Constructs detailed specification for SNMP destination data transformation.

        Description:
            Creates a comprehensive specification that defines how SNMP destination
            API response fields should be mapped, transformed, and structured in the final
            YAML configuration. Includes handling for server addresses, ports, and SNMP
            versioning.

        Args:
            None: Uses logging methods from the instance.

        Returns:
            OrderedDict: A detailed specification containing field mappings, data types,
            and SNMP configuration structures for SNMP destination configurations.
        """
        self.log("Generating temporary specification for SNMP destination details.", "DEBUG")
        return OrderedDict({
            "name": {"type": "str", "source_key": "name"},
            "description": {"type": "str", "source_key": "description"},
            "server_address": {"type": "str", "source_key": "ipAddress"},
            "port": {"type": "str", "source_key": "port"},
            "snmp_version": {"type": "str", "source_key": "snmpVersion"},
            "community": {"type": "str", "source_key": "community"},
            "username": {"type": "str", "source_key": "userName"},
            "mode": {"type": "str", "source_key": "snmpMode"},
            "auth_type": {"type": "str", "source_key": "snmpAuthType"},
            "auth_password": {"type": "str", "source_key": "authPassword", "transform": self.redact_password},
            "privacy_type": {"type": "str", "source_key": "snmpPrivacyType"},
            "privacy_password": {"type": "str", "source_key": "privacyPassword", "transform": self.redact_password},
        })

    def itsm_settings_temp_spec(self):
        """
        Constructs detailed specification for ITSM settings data transformation.

        Description:
            Creates a comprehensive specification that defines how ITSM integration
            settings API response fields should be mapped, transformed, and structured in the final
            YAML configuration. Includes handling for connection settings, URLs,
            authentication credentials, and password redaction for security.

        Args:
            None: Uses logging methods from the instance.

        Returns:
            OrderedDict: A detailed specification containing field mappings, data types,
            and connection configuration structures for ITSM settings configurations.
        """
        self.log("Generating temporary specification for ITSM settings details.", "DEBUG")
        return OrderedDict({
            "instance_name": {"type": "str", "source_key": "name"},
            "description": {"type": "str", "source_key": "description"},
            "connection_settings": {
                "type": "dict",
                "source_key": "connectionSettings",
                "options": OrderedDict({
                    "url": {"type": "str", "source_key": "url"},
                    "username": {"type": "str", "source_key": "username"},
                    "password": {"type": "str", "source_key": "password", "transform": self.redact_password},
                })
            },
        })

    def webhook_event_notifications_temp_spec(self):
        """
        Constructs detailed specification for webhook event notification data transformation.

        Description:
            Creates a comprehensive specification that defines how webhook event notification
            API response fields should be mapped, transformed, and structured in the final
            YAML configuration. Includes handling for site extraction, event name resolution,
            and destination mapping through transformation functions.

        Args:
            None: Uses logging methods and transformation functions from the instance.

        Returns:
            OrderedDict: A detailed specification containing field mappings, data types,
            transformation functions, and source key references for webhook event notifications.
        """
        self.log("Generating temporary specification for webhook event notification details.", "DEBUG")
        return OrderedDict({
            "name": {"type": "str", "source_key": "name"},
            "description": {"type": "str", "source_key": "description"},
            "sites": {"type": "list", "transform": self.extract_sites_from_filter},
            "events": {"type": "list", "source_key": "subscriptionEventTypes", "transform": self.extract_event_names},
            "destination": {"type": "str", "source_key": "webhookEndpointIds", "transform": self.extract_webhook_destination_name},
        })

    def email_event_notifications_temp_spec(self):
        """
        Constructs detailed specification for email event notification data transformation.

        Description:
            Creates a comprehensive specification that defines how email event notification
            API response fields should be mapped, transformed, and structured in the final
            YAML configuration. Includes handling for email address extraction, subject
            templates, instance creation, and site/event processing through transformation functions.

        Args:
            None: Uses logging methods and transformation functions from the instance.

        Returns:
            OrderedDict: A detailed specification containing field mappings, data types,
            transformation functions, and source key references for email event notifications.
        """
        self.log("Generating temporary specification for email event notification details.", "DEBUG")
        return OrderedDict({
            "name": {"type": "str", "source_key": "name"},
            "description": {"type": "str", "source_key": "description"},
            "sites": {"type": "list", "transform": self.extract_sites_from_filter},
            "events": {"type": "list", "source_key": "filter", "transform": self.extract_event_names},
            "sender_email": {"type": "str", "source_key": "subscriptionEndpoints", "transform": self.extract_sender_email},
            "recipient_emails": {"type": "list", "source_key": "subscriptionEndpoints", "transform": self.extract_recipient_emails},
            "subject": {"type": "str", "source_key": "subscriptionEndpoints", "transform": self.extract_subject},
            "instance": {"type": "str", "source_key": "name", "transform": self.create_instance_name},
            "instance_description": {"type": "str", "source_key": "description", "transform": self.create_instance_description},
        })

    def syslog_event_notifications_temp_spec(self):
        """
        Constructs detailed specification for syslog event notification data transformation.

        Description:
            Creates a comprehensive specification that defines how syslog event notification
            API response fields should be mapped, transformed, and structured in the final
            YAML configuration. Includes handling for site extraction, event name resolution,
            and syslog destination mapping through transformation functions.

        Args:
            None: Uses logging methods and transformation functions from the instance.

        Returns:
            OrderedDict: A detailed specification containing field mappings, data types,
            transformation functions, and source key references for syslog event notifications.
        """
        self.log("Generating temporary specification for syslog event notification details.", "DEBUG")
        return OrderedDict({
            "name": {"type": "str", "source_key": "name"},
            "description": {"type": "str", "source_key": "description"},
            "sites": {"type": "list", "transform": self.extract_sites_from_filter},
            "events": {"type": "list", "source_key": "subscriptionEventTypes", "transform": self.extract_event_names},
            "destination": {"type": "str", "source_key": "syslogConfigId", "transform": self.extract_syslog_destination_name},
        })

    def redact_password(self, password):
        """
        Redacts sensitive password information for security purposes.

        Description:
            This method replaces actual password values with a redacted placeholder
            to prevent sensitive information from appearing in generated YAML files
            or logs. It ensures security by masking credentials while maintaining
            the structure of the configuration.

        Args:
            password (str): The password string to be redacted.

        Returns:
            str | None: Returns "***REDACTED***" placeholder if password exists,
               otherwise None for empty or missing password values. This
               ensures sensitive data protection while preserving YAML
               structure for required password fields.
        """
        self.log(
            "Redacting password field for security. Password exists: {0}. "
            "Replacing actual value with redaction placeholder to prevent credential "
            "exposure in YAML configuration output.".format(bool(password)),
            "DEBUG"
        )

        redacted_value = "***REDACTED***" if password else None

        self.log(
            "Password redaction completed. Redacted value: {0}. Original "
            "password masked for security compliance in configuration generation.".format(
                redacted_value
            ),
            "DEBUG"
        )

        return redacted_value

    def extract_event_names(self, notification):
        """
        Extracts and resolves event names from notification filter event IDs.

        Description:
            This method processes notification filter data to extract event IDs and
            resolves them to human-readable event names using the Event Artifacts API.
            It handles API errors gracefully and provides fallback behavior using
            event IDs when names cannot be resolved.

        Args:
            notification (dict): Notification dictionary containing filter data with
                event IDs to be resolved to names.

        Returns:
            list: A list of resolved event names. If resolution fails, returns the
            original event IDs as fallback values. Returns an empty list if no
            event IDs are found in the notification filter.
        """
        self.log("Extracting event names from notification filter.", "DEBUG")

        if not notification or not isinstance(notification, dict):
            self.log(
                "Event name extraction skipped. Notification invalid or missing - type: {0}. "
                "Returning empty list for graceful handling.".format(type(notification).__name__),
                "WARNING"
            )
            return []

        filter_obj = notification.get("filter", {})
        event_ids = filter_obj.get("eventIds", [])

        if not event_ids:
            self.log(
                "No event IDs found in notification filter. Filter object: {0}. Returning "
                "empty list as no events require resolution.".format(filter_obj),
                "DEBUG"
            )
            return []

        event_names = []
        events_resolved = 0
        events_failed = 0

        for event_index, event_id in enumerate(event_ids, start=1):
            self.log(
                "Processing event {0}/{1} with ID: {2}. Calling get_event_name_from_api() "
                "to resolve event ID to human-readable name.".format(
                    event_index, len(event_ids), event_id
                ),
                "DEBUG"
            )
            try:
                event_name = self.get_event_name_from_api(event_id)
                if event_name:
                    event_names.append(event_name)
                    events_resolved += 1

                    self.log(
                        "Event {0}/{1} resolved successfully. ID: {2} -> Name: {3}. "
                        "Total resolved: {4}".format(
                            event_index, len(event_ids), event_id, event_name, events_resolved
                        ),
                        "DEBUG"
                    )
                else:
                    event_names.append(event_id)
                    events_failed += 1

                    self.log(
                        "Event {0}/{1} resolution returned None. Using event ID {2} as "
                        "fallback value. Total failed: {3}".format(
                            event_index, len(event_ids), event_id, events_failed
                        ),
                        "WARNING"
                    )
            except Exception as e:
                self.log("Error resolving event ID {0}: {1}".format(event_id, str(e)), "ERROR")
                event_names.append(event_id)
                events_failed += 1

                self.log(
                    "Event {0}/{1} resolution failed with exception. ID: {2}, Exception: {3}, "
                    "Type: {4}. Using event ID as fallback. Total failed: {5}".format(
                        event_index, len(event_ids), event_id, str(e), type(e).__name__,
                        events_failed
                    ),
                    "ERROR"
                )

        self.log("Resolved event names: {0}".format(event_names), "DEBUG")
        self.log(
            "Event name extraction completed. Processed {0} event(s): {1} resolved successfully, "
            "{2} failed with fallback to IDs. Final event names: {3}".format(
                len(event_ids), events_resolved, events_failed, event_names
            ),
            "INFO"
        )

        return event_names

    def get_event_name_from_api(self, event_id):
        """
        Resolves event ID to event name using Cisco Catalyst Center Event Artifacts API.

        Description:
            This method queries the Cisco Catalyst Center Event Artifacts API to resolve
            an event ID to its human-readable event name. It handles different response
            formats and provides fallback behavior when event names cannot be retrieved.

        Args:
            event_id (str): The event ID to resolve to a human-readable name.

        Returns:
            str | None: Resolved event name if found in API response, original event
               ID as fallback when name unavailable, None if event_id parameter
               invalid enabling graceful handling in event name extraction.
        """
        self.log(
            "Starting event ID resolution to human-readable name. Event ID: {0}. "
            "Calling Event Artifacts API to retrieve event details.".format(event_id),
            "DEBUG"
        )
        if not event_id:
            self.log(
                "Event ID resolution skipped - invalid event_id parameter (None or empty). "
                "Returning None for graceful handling.",
                "WARNING"
            )
            return None

        try:
            response = self.dnac._exec(
                family="event_management",
                function="get_event_artifacts",
                op_modifies=False,
                params={"event_ids": event_id}
            )
            self.log("Received API response for get_event_artifacts {0}".format(response), "DEBUG")

            self.log(
                "Event Artifacts API response received for event ID {0}. Response type: "
                "{1}. Processing response to extract event name.".format(
                    event_id, type(response).__name__
                ),
                "DEBUG"
            )

            if isinstance(response, list) and len(response) > 0:
                self.log(
                    "API response is list format with {0} item(s). Extracting event "
                    "information from first list item.".format(len(response)),
                    "DEBUG"
                )
                event_info = response[0]
                event_name = event_info.get("name")
                if event_name:
                    self.log(
                        "Event name successfully resolved from list response. Event ID: "
                        "{0} -> Event Name: {1}".format(event_id, event_name),
                        "INFO"
                    )
                    return event_name

            elif isinstance(response, dict):
                self.log(
                    "API response is dictionary format. Checking for response/events keys "
                    "to extract event data.",
                    "DEBUG"
                )
                events = response.get("response") or response.get("events") or []
                if events and len(events) > 0:
                    event_info = events[0] if isinstance(events, list) else events
                    event_name = event_info.get("name")
                    if event_name:
                        self.log(
                            "Event name successfully resolved from dict response. Event ID: "
                            "{0} -> Event Name: {1}".format(event_id, event_name),
                            "INFO"
                        )
                        return event_name

            self.log(
                "Event name field not found in API response for event ID {0}. Response "
                "structure may be incomplete. Using event ID as fallback value for "
                "graceful degradation.".format(event_id),
                "WARNING"
            )
            return event_id

        except Exception as e:
            self.log(
                "Exception occurred during Event Artifacts API call for event ID {0}. "
                "Exception type: {1}, Exception message: {2}. Using event ID as fallback "
                "value for graceful handling.".format(event_id, type(e).__name__, str(e)),
                "ERROR"
            )
            return event_id

    def extract_sites_from_filter(self, notification):
        """
        Extracts site names from filter data and resource domain structures.

        Description:
            This method processes notification data to extract site information from multiple
            sources including filter.siteIds, resourceDomain.resourceGroups, and direct site names.
            It attempts to resolve site IDs to site names using the site hierarchy API.

        Args:
            notification (dict): Complete notification object containing filter data and
                resource domain information with site details.

        Returns:
            list: Unique list of site hierarchical names extracted from notification data.
                Returns empty list if notification invalid, no sites found, or extraction
                error occurs enabling graceful handling in event notification processing.
        """
        self.log(
            "Starting site name extraction from notification filter and resource domain. "
            "Processing multiple site sources including direct names, site IDs, and resource "
            "groups for comprehensive site discovery.",
            "DEBUG"
        )

        if not notification or not isinstance(notification, dict):
            self.log(
                "Site extraction skipped - notification invalid or missing. Notification type: "
                "{0}. Returning empty list for graceful handling.".format(
                    type(notification).__name__
                ),
                "WARNING"
            )
            return []

        sites = []
        sites_from_direct = 0
        sites_from_ids = 0
        sites_from_resource = 0

        try:
            # Check filter for direct sites
            filter_data = notification.get("filter", {})
            if isinstance(filter_data, dict):
                self.log(
                    "Processing filter data for direct site names and site IDs. Filter keys: "
                    "{0}".format(list(filter_data.keys())),
                    "DEBUG"
                )
                direct_sites = filter_data.get("sites", [])
                if direct_sites:
                    sites.extend(direct_sites)
                    sites_from_direct = len(direct_sites)

                self.log(
                    "Extracted {0} direct site name(s) from filter.sites: {1}".format(
                        sites_from_direct, direct_sites
                    ),
                    "DEBUG"
                )

                # Site IDs in filter - need to resolve to names
                site_ids = filter_data.get("siteIds", [])
                if site_ids:
                    self.log(
                        "Found {0} site ID(s) requiring resolution: {1}. Calling site API "
                        "to resolve IDs to hierarchical names.".format(len(site_ids), site_ids),
                        "DEBUG"
                    )

                    for site_index, site_id in enumerate(site_ids, start=1):
                        self.log(
                            "Resolving site ID {0}/{1}: {2}. Calling get_site_name_by_id() "
                            "for hierarchical path retrieval.".format(
                                site_index, len(site_ids), site_id
                            ),
                            "DEBUG"
                        )

                        site_name = self.get_site_name_by_id(site_id)

                        if site_name:
                            sites.append(site_name)
                            sites_from_ids += 1

                            self.log(
                                "Site ID {0}/{1} resolved successfully: {2} -> {3}. Total "
                                "resolved from IDs: {4}".format(
                                    site_index, len(site_ids), site_id, site_name,
                                    sites_from_ids
                                ),
                                "DEBUG"
                            )
                        else:
                            sites.append(site_id)

                            self.log(
                                "Site ID {0}/{1} resolution failed: {2}. Using site ID as "
                                "fallback value in site list.".format(
                                    site_index, len(site_ids), site_id
                                ),
                                "WARNING"
                            )

            self.log(
                "Filter data processing completed. Direct sites: {0}, Resolved from IDs: {1}. "
                "Proceeding with resource domain processing.".format(
                    sites_from_direct, sites_from_ids
                ),
                "DEBUG"
            )

            # Check resourceDomain for site information
            resource_domain = notification.get("resourceDomain", {})
            if resource_domain:
                resource_groups = resource_domain.get("resourceGroups", [])
                self.log(
                    "Processing resource domain with {0} resource group(s). Extracting "
                    "site-type groups for name and srcResourceId fields.".format(
                        len(resource_groups)
                    ),
                    "DEBUG"
                )
                for group_index, group in enumerate(resource_groups, start=1):
                    if group.get("type") == "site":
                        self.log(
                            "Processing site-type resource group {0}/{1}. Extracting name "
                            "and srcResourceId fields.".format(group_index, len(resource_groups)),
                            "DEBUG"
                        )

                        site_name = group.get("name")
                        if site_name and site_name not in sites:
                            sites.append(site_name)
                            sites_from_resource += 1

                            self.log(
                                "Added site name from resource group {0}: {1}. Total from "
                                "resource domain: {2}".format(
                                    group_index, site_name, sites_from_resource
                                ),
                                "DEBUG"
                            )

                        src_resource_id = group.get("srcResourceId")
                        if src_resource_id and src_resource_id != "*":
                            self.log(
                                "Resolving srcResourceId from group {0}: {1}. Calling "
                                "get_site_name_by_id() for resolution.".format(
                                    group_index, src_resource_id
                                ),
                                "DEBUG"
                            )

                            resolved_site = self.get_site_name_by_id(src_resource_id)

                            if resolved_site and resolved_site not in sites:
                                sites.append(resolved_site)
                                sites_from_resource += 1

                                self.log(
                                    "Resolved srcResourceId {0} -> {1} from group {2}. "
                                    "Added to site list.".format(
                                        src_resource_id, resolved_site, group_index
                                    ),
                                    "DEBUG"
                                )

            self.log(
                "Resource domain processing completed. Sites from resource groups: {0}".format(
                    sites_from_resource
                ),
                "DEBUG"
            )

            # Remove duplicates while preserving order
            unique_sites = []
            for site in sites:
                if site not in unique_sites:
                    unique_sites.append(site)

            duplicates_removed = len(sites) - len(unique_sites)

            self.log(
                "Site extraction completed successfully. Total sites found: {0} (direct: {1}, "
                "from IDs: {2}, from resource domain: {3}). Removed {4} duplicate(s). "
                "Final unique sites: {5}".format(
                    len(sites), sites_from_direct, sites_from_ids, sites_from_resource,
                    duplicates_removed, unique_sites
                ),
                "INFO"
            )

            return unique_sites

        except Exception as e:
            self.log(
                "Exception occurred during site extraction from notification. Exception type: "
                "{0}, Exception message: {1}. Returning empty list for graceful handling.".format(
                    type(e).__name__, str(e)
                ),
                "ERROR"
            )
            self.set_operation_result("failed", True, self.msg, "ERROR").check_return_status()

    def get_site_name_by_id(self, site_id):
        """
        Resolves site ID to site name using Cisco Catalyst Center Sites API.

        Description:
            This method queries the Cisco Catalyst Center Sites API to resolve a site UUID
            to its hierarchical site name (e.g., "Global/Area/Building/Floor"). It handles
            API errors gracefully and provides fallback behavior.

        Args:
            site_id (str): Site UUID to resolve to hierarchical name path for event
                        notification site documentation.

        Returns:
            str | None: Hierarchical site name if resolution succeeds, None if site_id
                    invalid (None or "*"), API call fails, or site not found in
                    Catalyst Center enabling graceful handling in notification
                    processing.
        """

        self.log(
            "Starting site UUID resolution to hierarchical name. Site ID: {0}. "
            "Calling Sites API to retrieve site hierarchy information.".format(site_id),
            "DEBUG"
        )

        if not site_id or site_id == "*":
            self.log(
                "Site resolution skipped - invalid site_id (None, empty, or wildcard '*'). "
                "Returning None for graceful handling.",
                "WARNING"
            )
            return None

        if not site_id or site_id == "*":
            return None

        try:
            response = self.dnac._exec(
                family="sites",
                function="get_site",
                op_modifies=False,
                params={"site_id": site_id}
            )

            self.log(
                "Received API response for sites with site ID {0}. Response type: {1}. "
                "Processing response to extract hierarchical site name.".format(
                    site_id, type(response).__name__
                ),
                "DEBUG"
            )

            if isinstance(response, dict):
                site_info = response.get("response")
                if site_info:
                    self.log(
                        "Site information found in response. Extracting siteNameHierarchy "
                        "field for hierarchical path.",
                        "DEBUG"
                    )
                    site_name_hierarchy = site_info.get("siteNameHierarchy")
                    if site_name_hierarchy:
                        self.log(
                            "Successfully resolved site ID {0} to hierarchical name: {1}. "
                            "Returning site name for notification configuration.".format(
                                site_id, site_name_hierarchy
                            ),
                            "INFO"
                        )
                        return site_name_hierarchy
                    self.log(
                        "siteNameHierarchy field not found in site info. Checking "
                        "additionalInfo for fallback site name extraction.",
                        "DEBUG"
                    )

                    # Fallback to additionalInfo if available
                    additional_info = site_info.get("additionalInfo")
                    if additional_info and len(additional_info) > 0:
                        namespace = additional_info[0].get("nameSpace")

                        if namespace == "Location":
                            attributes = additional_info[0].get("attributes", {})
                            site_hierarchy = attributes.get("name")

                            if site_hierarchy:
                                self.log(
                                    "Successfully resolved site ID {0} from additionalInfo "
                                    "attributes: {1}. Using fallback site name extraction.".format(
                                        site_id, site_hierarchy
                                    ),
                                    "INFO"
                                )
                                return site_hierarchy

            self.log(
                "Site name resolution failed for site ID {0}. Response structure incomplete "
                "or site name unavailable in API response. Returning None.".format(site_id),
                "WARNING"
            )
            return None

        except Exception as e:
            self.log(
                "Exception occurred during site name resolution for site ID {0}. "
                "Exception type: {1}, Exception message: {2}. Returning None for "
                "graceful handling.".format(site_id, type(e).__name__, str(e)),
                "ERROR"
            )
            return []

    def extract_webhook_destination_name(self, notification):
        """
        Extracts webhook destination name from notification subscription endpoints.

        Description:
            This method searches through subscription endpoints in a notification to find
            webhook (REST) connector types and extracts the destination name. It iterates
            through all subscription endpoints and returns the first matching webhook destination name.

        Args:
            notification (dict): Notification dictionary containing subscription endpoints
                with connector details.

        Returns:
            str or None: The webhook destination name if found, otherwise None.
            Returns None if the notification is invalid or no webhook destination is found.
        """
        self.log(
            "Starting webhook destination name extraction from notification subscription "
            "endpoints. Searching through endpoints to locate REST connector type for "
            "destination name resolution.",
            "DEBUG"
        )

        if not notification:
            self.log(
                "Webhook destination extraction skipped - notification parameter invalid "
                "or None. Returning None for graceful handling in notification processing.",
                "WARNING"
            )
            return None

        subscription_endpoints = notification.get("subscriptionEndpoints", [])
        if not subscription_endpoints:
            self.log(
                "No subscription endpoints found in notification. subscriptionEndpoints "
                "list is empty. Returning None as no webhook destinations available.",
                "DEBUG"
            )
            return None

        self.log(
            "Found {0} subscription endpoint(s) in notification. Iterating through "
            "endpoints to locate REST connector type.".format(len(subscription_endpoints)),
            "DEBUG"
        )

        for endpoint_index, endpoint in enumerate(subscription_endpoints, start=1):
            self.log(
                "Processing subscription endpoint {0}/{1}. Extracting subscriptionDetails "
                "for connector type validation.".format(
                    endpoint_index, len(subscription_endpoints)
                ),
                "DEBUG"
            )

            subscription_details = endpoint.get("subscriptionDetails", {})
            connector_type = subscription_details.get("connectorType")

            self.log(
                "Endpoint {0}/{1} connector type: {2}. Checking if matches REST for "
                "webhook destination.".format(
                    endpoint_index, len(subscription_endpoints), connector_type
                ),
                "DEBUG"
            )

            if connector_type == "REST":
                destination_name = subscription_details.get("name")

                self.log(
                    "Found webhook (REST) destination at endpoint {0}/{1}. Destination "
                    "name: {2}. Returning destination name for notification configuration.".format(
                        endpoint_index, len(subscription_endpoints), destination_name
                    ),
                    "INFO"
                )

                return destination_name
        self.log(
            "No REST connector type found in {0} subscription endpoint(s). No webhook "
            "destination available in this notification. Returning None.".format(
                len(subscription_endpoints)
            ),
            "WARNING"
        )

        return None

    def extract_syslog_destination_name(self, notification):
        """
        Extracts syslog destination name from notification subscription endpoints.

        Description:
            Searches through subscription endpoints to locate SYSLOG connector types
            and extracts destination name by iterating through subscriptionEndpoints list,
            checking connectorType field for SYSLOG value, and returning first matching
            syslog destination name found enabling destination reference resolution in
            event notification YAML generation workflow.

        Args:
            notification (dict): Notification dictionary containing subscription endpoints
                                with connector configuration details requiring destination
                                name extraction.

        Returns:
            str | None: Syslog destination name if SYSLOG connector found in subscription
                    endpoints, None if notification invalid or no syslog destination
                    exists enabling graceful handling in notification processing.
        """
        self.log(
            "Starting syslog destination name extraction from notification subscription "
            "endpoints. Searching through endpoints to locate SYSLOG connector type for "
            "destination name resolution.",
            "DEBUG"
        )

        if not notification:
            self.log(
                "Syslog destination extraction skipped - notification parameter invalid "
                "or None. Returning None for graceful handling in notification processing.",
                "WARNING"
            )
            return None

        subscription_endpoints = notification.get("subscriptionEndpoints", [])
        if not subscription_endpoints:
            self.log(
                "No subscription endpoints found in notification. subscriptionEndpoints "
                "list is empty. Returning None as no syslog destinations available.",
                "DEBUG"
            )
            return None

        self.log(
            "Found {0} subscription endpoint(s) in notification. Iterating through "
            "endpoints to locate SYSLOG connector type.".format(len(subscription_endpoints)),
            "DEBUG"
        )

        for endpoint_index, endpoint in enumerate(subscription_endpoints, start=1):
            self.log(
                "Processing subscription endpoint {0}/{1}. Extracting subscriptionDetails "
                "for connector type validation.".format(
                    endpoint_index, len(subscription_endpoints)
                ),
                "DEBUG"
            )

            subscription_details = endpoint.get("subscriptionDetails", {})
            connector_type = subscription_details.get("connectorType")

            self.log(
                "Endpoint {0}/{1} connector type: {2}. Checking if matches SYSLOG for "
                "destination.".format(
                    endpoint_index, len(subscription_endpoints), connector_type
                ),
                "DEBUG"
            )

            if connector_type == "SYSLOG":
                destination_name = subscription_details.get("name")

                self.log(
                    "Found syslog (SYSLOG) destination at endpoint {0}/{1}. Destination "
                    "name: {2}. Returning destination name for notification configuration.".format(
                        endpoint_index, len(subscription_endpoints), destination_name
                    ),
                    "INFO"
                )

                return destination_name

        self.log(
            "No SYSLOG connector type found in {0} subscription endpoint(s). No syslog "
            "destination available in this notification. Returning None.".format(
                len(subscription_endpoints)
            ),
            "WARNING"
        )

        return None

    def extract_sender_email(self, notification):
        """
        Extracts sender email address from notification subscription endpoints.

        Description:
            This method processes subscription endpoints to find email connector types
            and extracts the sender email address (fromEmailAddress). It searches through
            all endpoints to locate email-specific configuration details.

        Args:
            notification (dict): Notification dictionary containing subscription endpoints
                with email configuration details.

        Returns:
            str or None: The sender email address if found, otherwise None.
            Returns None if the notification is invalid or no email configuration is found.
        """
        self.log(
            "Starting sender email extraction from notification subscription endpoints. "
            "Searching through endpoints to locate EMAIL connector type for fromEmailAddress "
            "field extraction.",
            "DEBUG"
        )

        if not notification:
            self.log(
                "Sender email extraction skipped - notification parameter invalid or None. "
                "Returning None for graceful handling in notification processing.",
                "WARNING"
            )
            return None

        subscription_endpoints = notification.get("subscriptionEndpoints", [])
        if not subscription_endpoints:
            self.log(
                "No subscription endpoints found in notification. subscriptionEndpoints "
                "list is empty. Returning None as no email configuration available.",
                "DEBUG"
            )
            return None

        self.log(
            "Found {0} subscription endpoint(s) in notification. Iterating through "
            "endpoints to locate EMAIL connector type.".format(len(subscription_endpoints)),
            "DEBUG"
        )

        for endpoint_index, endpoint in enumerate(subscription_endpoints, start=1):
            self.log(
                "Processing subscription endpoint {0}/{1}. Extracting subscriptionDetails "
                "for connector type validation.".format(
                    endpoint_index, len(subscription_endpoints)
                ),
                "DEBUG"
            )

            subscription_details = endpoint.get("subscriptionDetails", {})
            connector_type = subscription_details.get("connectorType")

            self.log(
                "Endpoint {0}/{1} connector type: {2}. Checking if matches EMAIL for "
                "sender address extraction.".format(
                    endpoint_index, len(subscription_endpoints), connector_type
                ),
                "DEBUG"
            )

            if connector_type == "EMAIL":
                sender_email = subscription_details.get("fromEmailAddress")

                self.log(
                    "Found email (EMAIL) configuration at endpoint {0}/{1}. Sender email "
                    "address: {2}. Returning sender email for notification configuration.".format(
                        endpoint_index, len(subscription_endpoints), sender_email
                    ),
                    "INFO"
                )

                return sender_email

        self.log(
            "No EMAIL connector type found in {0} subscription endpoint(s). No sender "
            "email available in this notification. Returning None.".format(
                len(subscription_endpoints)
            ),
            "WARNING"
        )

        return None

    def extract_recipient_emails(self, notification):
        """
        Extracts recipient email addresses from notification subscription endpoints.

        Description:
            This method processes subscription endpoints to find email connector types
            and extracts the list of recipient email addresses (toEmailAddresses). It
            searches through all endpoints to locate email-specific recipient configurations.

        Args:
            notification (dict): Notification dictionary containing subscription endpoints
                with email configuration details.

        Returns:
            list: A list of recipient email addresses if found, otherwise an empty list.
            Returns an empty list if the notification is invalid or no email configuration is found.
        """
        self.log(
            "Starting recipient email extraction from notification subscription endpoints. "
            "Searching through endpoints to locate EMAIL connector type for toEmailAddresses "
            "field extraction.",
            "DEBUG"
        )

        if not notification:
            self.log(
                "Recipient email extraction skipped - notification parameter invalid or None. "
                "Returning empty list for graceful handling in notification processing.",
                "WARNING"
            )
            return []

        subscription_endpoints = notification.get("subscriptionEndpoints", [])
        if not subscription_endpoints:
            self.log(
                "No subscription endpoints found in notification. subscriptionEndpoints "
                "list is empty. Returning empty list as no email configuration available.",
                "DEBUG"
            )
            return []

        self.log(
            "Found {0} subscription endpoint(s) in notification. Iterating through "
            "endpoints to locate EMAIL connector type.".format(len(subscription_endpoints)),
            "DEBUG"
        )

        for endpoint_index, endpoint in enumerate(subscription_endpoints, start=1):
            self.log(
                "Processing subscription endpoint {0}/{1}. Extracting subscriptionDetails "
                "for connector type validation.".format(
                    endpoint_index, len(subscription_endpoints)
                ),
                "DEBUG"
            )

            subscription_details = endpoint.get("subscriptionDetails", {})
            connector_type = subscription_details.get("connectorType")

            self.log(
                "Endpoint {0}/{1} connector type: {2}. Checking if matches EMAIL for "
                "recipient address extraction.".format(
                    endpoint_index, len(subscription_endpoints), connector_type
                ),
                "DEBUG"
            )

            if connector_type == "EMAIL":
                recipient_emails = subscription_details.get("toEmailAddresses", [])

                self.log(
                    "Found email (EMAIL) configuration at endpoint {0}/{1}. Recipient "
                    "email addresses: {2} recipient(s). Returning recipient list for "
                    "notification configuration.".format(
                        endpoint_index, len(subscription_endpoints), len(recipient_emails)
                    ),
                    "INFO"
                )

                return recipient_emails

        self.log(
            "No EMAIL connector type found in {0} subscription endpoint(s). No recipient "
            "emails available in this notification. Returning empty list.".format(
                len(subscription_endpoints)
            ),
            "WARNING"
        )

        return []

    def extract_subject(self, notification):
        """
        Extracts email subject from notification subscription endpoints.

        Description:
            This method processes subscription endpoints to find email connector types
            and extracts the email subject line. It searches through all endpoints to
            locate email-specific subject configuration details.

        Args:
            notification (dict): Notification dictionary containing subscription endpoints
                with email configuration details.

        Returns:
            str or None: The email subject if found, otherwise None.
            Returns None if the notification is invalid or no email configuration is found.
        """
        self.log(
            "Starting email subject extraction from notification subscription endpoints. "
            "Searching through endpoints to locate EMAIL connector type for subject field "
            "extraction.",
            "DEBUG"
        )

        if not notification:
            self.log(
                "Email subject extraction skipped - notification parameter invalid or None. "
                "Returning None for graceful handling in notification processing.",
                "WARNING"
            )
            return None

        subscription_endpoints = notification.get("subscriptionEndpoints", [])
        if not subscription_endpoints:
            self.log(
                "No subscription endpoints found in notification. subscriptionEndpoints "
                "list is empty. Returning None as no email configuration available.",
                "DEBUG"
            )
            return None

        self.log(
            "Found {0} subscription endpoint(s) in notification. Iterating through "
            "endpoints to locate EMAIL connector type.".format(len(subscription_endpoints)),
            "DEBUG"
        )

        for endpoint_index, endpoint in enumerate(subscription_endpoints, start=1):
            self.log(
                "Processing subscription endpoint {0}/{1}. Extracting subscriptionDetails "
                "for connector type validation.".format(
                    endpoint_index, len(subscription_endpoints)
                ),
                "DEBUG"
            )

            subscription_details = endpoint.get("subscriptionDetails", {})
            connector_type = subscription_details.get("connectorType")

            self.log(
                "Endpoint {0}/{1} connector type: {2}. Checking if matches EMAIL for "
                "subject extraction.".format(
                    endpoint_index, len(subscription_endpoints), connector_type
                ),
                "DEBUG"
            )

            if connector_type == "EMAIL":
                subject = subscription_details.get("subject")

                self.log(
                    "Found email (EMAIL) configuration at endpoint {0}/{1}. Email subject: "
                    "{2}. Returning subject for notification configuration.".format(
                        endpoint_index, len(subscription_endpoints), subject
                    ),
                    "INFO"
                )

                return subject

        self.log(
            "No EMAIL connector type found in {0} subscription endpoint(s). No email "
            "subject available in this notification. Returning None.".format(
                len(subscription_endpoints)
            ),
            "WARNING"
        )

        return None

    def create_instance_name(self, notification):
        """
        Creates instance name from email subscription endpoint details.

        Description:
            This method extracts the instance name from email subscription endpoints
            by searching for EMAIL connector types and retrieving the name field.
            This is used to create meaningful instance identifiers for email notifications.

        Args:
            notification (dict): Notification dictionary containing subscription endpoints
                with email instance details.

        Returns:
            str or None: The instance name if found in email subscription details,
            otherwise None if no email connector or name is found.
        """
        self.log(
            "Extracting instance name from email subscription endpoint. Searching through "
            "notification endpoints to locate EMAIL connector type.",
            "DEBUG"
        )

        if not notification or not isinstance(notification, dict):
            self.log(
                "Instance name extraction skipped - notification parameter invalid or not "
                "dictionary type. Notification type: {0}. Returning None for graceful "
                "handling.".format(type(notification).__name__),
                "WARNING"
            )
            return None

        subscription_endpoints = notification.get("subscriptionEndpoints", [])
        if not subscription_endpoints:
            self.log(
                "No subscription endpoints found in notification. subscriptionEndpoints list "
                "is empty. Returning None as no email instance available.",
                "DEBUG"
            )
            return None

        self.log(
            "Found {0} subscription endpoint(s) in notification. Iterating through endpoints "
            "to locate EMAIL connector type for instance name extraction.".format(
                len(subscription_endpoints)
            ),
            "DEBUG"
        )

        for endpoint_index, endpoint in enumerate(subscription_endpoints, start=1):
            self.log(
                "Processing subscription endpoint {0}/{1}. Extracting subscriptionDetails "
                "for connector type validation.".format(
                    endpoint_index, len(subscription_endpoints)
                ),
                "DEBUG"
            )

            subscription_details = endpoint.get("subscriptionDetails", {})
            connector_type = subscription_details.get("connectorType")

            self.log(
                "Endpoint {0}/{1} connector type: {2}. Checking if matches EMAIL for "
                "instance name extraction.".format(
                    endpoint_index, len(subscription_endpoints), connector_type
                ),
                "DEBUG"
            )

            if connector_type == "EMAIL":
                instance_name = subscription_details.get("name")

                self.log(
                    "Found email (EMAIL) configuration at endpoint {0}/{1}. Instance name: "
                    "{2}. Returning instance name for notification configuration.".format(
                        endpoint_index, len(subscription_endpoints), instance_name
                    ),
                    "INFO"
                )

                return instance_name

        self.log(
            "No EMAIL connector type found in {0} subscription endpoint(s). No email "
            "instance name available in this notification. Returning None.".format(
                len(subscription_endpoints)
            ),
            "WARNING"
        )

        return None

    def create_instance_description(self, notification):
        """
        Creates instance description from email subscription endpoint details.

        Description:
            This method extracts the instance description from email subscription endpoints
            by searching for EMAIL connector types and retrieving the description field.
            This provides descriptive information for email notification instances.

        Args:
            notification (dict): Notification dictionary containing subscription endpoints
                with email instance details.

        Returns:
            str or None: The instance description if found in email subscription details,
            otherwise None if no email connector or description is found.
        """
        self.log(
            "Extracting instance description from email subscription endpoint. Searching "
            "through notification endpoints to locate EMAIL connector type.",
            "DEBUG"
        )

        if not notification or not isinstance(notification, dict):
            self.log(
                "Instance description extraction skipped - notification parameter invalid or "
                "not dictionary type. Notification type: {0}. Returning None for graceful "
                "handling.".format(type(notification).__name__),
                "WARNING"
            )
            return None

        subscription_endpoints = notification.get("subscriptionEndpoints", [])
        if not subscription_endpoints:
            self.log(
                "No subscription endpoints found in notification. subscriptionEndpoints list "
                "is empty. Returning None as no email instance description available.",
                "DEBUG"
            )
            return None

        self.log(
            "Found {0} subscription endpoint(s) in notification. Iterating through endpoints "
            "to locate EMAIL connector type for instance description extraction.".format(
                len(subscription_endpoints)
            ),
            "DEBUG"
        )
        for endpoint_index, endpoint in enumerate(subscription_endpoints, start=1):
            self.log(
                "Processing subscription endpoint {0}/{1}. Extracting subscriptionDetails "
                "for connector type validation.".format(
                    endpoint_index, len(subscription_endpoints)
                ),
                "DEBUG"
            )

            subscription_details = endpoint.get("subscriptionDetails", {})
            connector_type = subscription_details.get("connectorType")

            self.log(
                "Endpoint {0}/{1} connector type: {2}. Checking if matches EMAIL for "
                "instance description extraction.".format(
                    endpoint_index, len(subscription_endpoints), connector_type
                ),
                "DEBUG"
            )

            if connector_type == "EMAIL":
                instance_description = subscription_details.get("description")

                self.log(
                    "Found email (EMAIL) configuration at endpoint {0}/{1}. Instance "
                    "description: {2}. Returning description for notification configuration.".format(
                        endpoint_index, len(subscription_endpoints), instance_description
                    ),
                    "INFO"
                )

                return instance_description

        self.log(
            "No EMAIL connector type found in {0} subscription endpoint(s). No email "
            "instance description available in this notification. Returning None.".format(
                len(subscription_endpoints)
            ),
            "WARNING"
        )

        return None

    def get_webhook_destinations(self, network_element, filters):
        """
        Retrieves webhook destination configurations from Cisco Catalyst Center.

        Description:
            This method fetches webhook destination details from the Cisco Catalyst Center using the API.
            It applies smart filtering where if destination names are provided and matches are found,
            only matching destinations are returned. If no matches are found, all webhook destinations
            are returned to ensure comprehensive configuration coverage.

        Args:
            network_element (dict): Configuration mapping containing API family and function details.
            filters (dict): Filter criteria containing component-specific filters for destinations.

        Returns:
            dict: A dictionary containing:
                - webhook_destinations (list): List of webhook destination configurations with transformed
                parameters according to the webhook destinations specification.
        """
        self.log(
            "Starting webhook destination retrieval. Extracting component filters and "
            "destination names for filtering webhook configurations.",
            "DEBUG"
        )

        component_specific_filters = filters.get("component_specific_filters", {})
        destination_filters = component_specific_filters.get("destination_filters", {})
        destination_names = destination_filters.get("destination_names", [])
        self.log(
            "Destination name filters extracted: {0} name(s) specified. Filter mode: {1}".format(
                len(destination_names),
                "name-based filtering" if destination_names else "retrieve all"
            ),
            "DEBUG"
        )

        api_family = network_element.get("api_family")
        api_function = network_element.get("api_function")
        self.log(
            "API details extracted - Family: {0}, Function: {1}. Calling API to retrieve "
            "webhook destinations.".format(api_family, api_function),
            "DEBUG"
        )

        try:
            webhook_configs = self.get_all_webhook_destinations(api_family, api_function)
            self.log(
                "Retrieved {0} webhook destination(s) from Catalyst Center. Processing "
                "filtering logic based on destination_names.".format(len(webhook_configs)),
                "INFO"
            )

            if destination_names:
                self.log(
                    "Applying destination name filter: {0}. Searching for matching "
                    "webhooks in retrieved configurations.".format(destination_names),
                    "DEBUG"
                )
                matching_configs = [config for config in webhook_configs if config.get("name") in destination_names]
                if matching_configs:
                    final_webhook_configs = matching_configs
                    self.log(
                        "Found {0} matching webhook destination(s) for filter criteria. "
                        "Using filtered subset for YAML generation.".format(
                            len(matching_configs)
                        ),
                        "INFO"
                    )
                    final_webhook_configs = matching_configs
                else:
                    self.log("No matching webhook destinations found for filter - including all", "DEBUG")
            else:
                final_webhook_configs = webhook_configs
                self.log(
                    "No destination name filters provided. Including all {0} webhook "
                    "destination(s) for YAML generation.".format(len(webhook_configs)),
                    "DEBUG"
                )

        except Exception as e:
            self.log(
                "Exception occurred during webhook destination retrieval. Exception type: "
                "{0}, Exception message: {1}. Returning empty list for graceful handling.".format(
                    type(e).__name__, str(e)
                ),
                "ERROR"
            )
            self.set_operation_result("failed", True, self.msg, "ERROR").check_return_status()

        self.log(
            "Retrieving webhook destination specification for parameter transformation. "
            "Calling webhook_destinations_temp_spec() for mapping rules.",
            "DEBUG"
        )

        webhook_destinations_temp_spec = self.webhook_destinations_temp_spec()

        self.log(
            "Transforming {0} webhook destination(s) using specification. Converting "
            "camelCase API responses to snake_case YAML format with modify_parameters().".format(
                len(final_webhook_configs)
            ),
            "DEBUG"
        )
        modified_webhook_configs = self.modify_parameters(webhook_destinations_temp_spec, final_webhook_configs)

        result = {"webhook_destinations": modified_webhook_configs}
        self.log(
            "Webhook destination retrieval completed. Final result contains {0} "
            "transformed configuration(s) ready for YAML serialization.".format(
                len(modified_webhook_configs)
            ),
            "INFO"
        )
        return result

    def get_email_destinations(self, network_element, filters):
        """
        Retrieves email destination configurations from Cisco Catalyst Center.

        Description:
            This method fetches email destination details including SMTP configurations from the
            Cisco Catalyst Center API. It applies smart filtering based on destination names if provided.
            The method preserves essential SMTP configuration structures even when some values are None.

        Args:
            network_element (dict): Configuration mapping containing API family and function details.
            filters (dict): Filter criteria containing component-specific filters for destinations.

        Returns:
            dict: A dictionary containing:
                - email_destinations (list): List of email destination configurations including
                primary and secondary SMTP settings with transformed parameters.
        """
        self.log(
            "Starting email destination retrieval. Extracting component filters and "
            "destination names for filtering email configurations.",
            "DEBUG"
        )

        component_specific_filters = filters.get("component_specific_filters", {})
        destination_filters = component_specific_filters.get("destination_filters", {})
        destination_names = destination_filters.get("destination_names", [])

        self.log(
            "Destination name filters extracted: {0} name(s) specified. Filter mode: {1}".format(
                len(destination_names),
                "name-based filtering" if destination_names else "retrieve all"
            ),
            "DEBUG"
        )

        api_family = network_element.get("api_family")
        api_function = network_element.get("api_function")

        self.log(
            "API details extracted - Family: {0}, Function: {1}. Calling API to retrieve "
            "email destinations.".format(api_family, api_function),
            "DEBUG"
        )

        try:
            email_configs = self.get_all_email_destinations(api_family, api_function)
            self.log(
                "Retrieved {0} email destination(s) from Catalyst Center. Processing "
                "filtering logic based on destination_names.".format(len(email_configs)),
                "INFO"
            )

            if destination_names:
                self.log(
                    "Applying destination name filter: {0}. Searching for matching "
                    "emails in retrieved configurations.".format(destination_names),
                    "DEBUG"
                )
                matching_configs = [config for config in email_configs if config.get("name") in destination_names]
                if matching_configs:
                    final_email_configs = matching_configs
                    self.log(
                        "Found {0} matching email destination(s) for filter criteria. "
                        "Using filtered subset for YAML generation.".format(
                            len(matching_configs)
                        ),
                        "INFO"
                    )
                else:
                    final_email_configs = email_configs
                    self.log(
                        "No matching email destinations found for filter: {0}. Including "
                        "all {1} email(s) for comprehensive configuration coverage.".format(
                            destination_names, len(email_configs)
                        ),
                        "WARNING"
                    )
            else:
                self.log(
                    "No destination name filters provided. Including all {0} email "
                    "destination(s) for YAML generation.".format(len(email_configs)),
                    "DEBUG"
                )
                final_email_configs = email_configs

        except Exception as e:
            self.log(
                "Exception occurred during email destination retrieval. Exception type: "
                "{0}, Exception message: {1}. Returning empty list for graceful handling.".format(
                    type(e).__name__, str(e)
                ),
                "ERROR"
            )
            final_email_configs = []

        self.log(
            "Retrieving email destination specification for parameter transformation. "
            "Calling email_destinations_temp_spec() for mapping rules.",
            "DEBUG"
        )

        email_destinations_temp_spec = self.email_destinations_temp_spec()

        self.log(
            "Transforming {0} email destination(s) using specification. Converting "
            "camelCase API responses to snake_case YAML format with modify_parameters().".format(
                len(final_email_configs)
            ),
            "DEBUG"
        )

        modified_email_configs = self.modify_parameters(email_destinations_temp_spec, final_email_configs)

        result = {"email_destinations": modified_email_configs}
        self.log(
            "Email destination retrieval completed. Final result contains {0} "
            "transformed configuration(s) ready for YAML serialization.".format(
                len(modified_email_configs)
            ),
            "INFO"
        )
        return result

    def get_syslog_destinations(self, network_element, filters):
        """
        Retrieves syslog destination configurations from Cisco Catalyst Center.

        Description:
            This method fetches syslog destination details from the Cisco Catalyst Center API.
            It supports filtering by destination names and applies smart matching logic where
            configurations are filtered only when matching destinations exist.

        Args:
            network_element (dict): Configuration mapping containing API family and function details.
            filters (dict): Filter criteria containing component-specific filters for destinations.

        Returns:
            dict: A dictionary containing:
                - syslog_destinations (list): List of syslog destination configurations with
                server details, protocols, and ports according to the syslog specification.
        """
        self.log(
            "Starting syslog destination retrieval. Extracting component filters and "
            "destination names for filtering syslog configurations.",
            "DEBUG"
        )

        component_specific_filters = filters.get("component_specific_filters", {})
        destination_filters = component_specific_filters.get("destination_filters", {})
        destination_names = destination_filters.get("destination_names", [])

        self.log(
            "Destination name filters extracted: {0} name(s) specified. Filter mode: {1}".format(
                len(destination_names),
                "name-based filtering" if destination_names else "retrieve all"
            ),
            "DEBUG"
        )

        api_family = network_element.get("api_family")
        api_function = network_element.get("api_function")
        self.log(
            "API details extracted - Family: {0}, Function: {1}. Calling API to retrieve "
            "syslog destinations.".format(api_family, api_function),
            "DEBUG"
        )

        try:
            syslog_configs = self.get_all_syslog_destinations(api_family, api_function)
            self.log(
                "Retrieved {0} syslog destination(s) from Catalyst Center. Processing "
                "filtering logic based on destination_names.".format(len(syslog_configs)),
                "INFO"
            )

            if destination_names:
                self.log(
                    "Applying destination name filter: {0}. Searching for matching "
                    "syslogs in retrieved configurations.".format(destination_names),
                    "DEBUG"
                )
                matching_configs = [config for config in syslog_configs if config.get("name") in destination_names]
                if matching_configs:
                    final_syslog_configs = matching_configs
                    self.log(
                        "Found {0} matching syslog destination(s) for filter criteria. "
                        "Using filtered subset for YAML generation.".format(
                            len(matching_configs)
                        ),
                        "INFO"
                    )
                else:
                    final_syslog_configs = syslog_configs
                    self.log(
                        "No matching syslog destinations found for filter: {0}. Including "
                        "all {1} syslog(s) for comprehensive configuration coverage.".format(
                            destination_names, len(syslog_configs)
                        ),
                        "WARNING"
                    )
            else:
                self.log(
                    "No destination name filters provided. Including all {0} syslog "
                    "destination(s) for YAML generation.".format(len(syslog_configs)),
                    "DEBUG"
                )
                final_syslog_configs = syslog_configs

        except Exception as e:
            self.log(
                "Exception occurred during syslog destination retrieval. Exception type: "
                "{0}, Exception message: {1}. Returning empty list for graceful handling.".format(
                    type(e).__name__, str(e)
                ),
                "ERROR"
            )
            final_syslog_configs = []

        self.log(
            "Retrieving syslog destination specification for parameter transformation. "
            "Calling syslog_destinations_temp_spec() for mapping rules.",
            "DEBUG"
        )

        syslog_destinations_temp_spec = self.syslog_destinations_temp_spec()

        self.log(
            "Transforming {0} syslog destination(s) using specification. Converting "
            "camelCase API responses to snake_case YAML format with modify_parameters().".format(
                len(final_syslog_configs)
            ),
            "DEBUG"
        )
        modified_syslog_configs = self.modify_parameters(syslog_destinations_temp_spec, final_syslog_configs)

        result = {"syslog_destinations": modified_syslog_configs}
        self.log(
            "Syslog destination retrieval completed. Final result contains {0} "
            "transformed configuration(s) ready for YAML serialization.".format(
                len(modified_syslog_configs)
            ),
            "INFO"
        )
        return result

    def get_snmp_destinations(self, network_element, filters):
        """
        Retrieves SNMP destination configurations from Cisco Catalyst Center.

        Description:
            This method fetches SNMP destination details from the Cisco Catalyst Center API.
            It handles pagination for large datasets and applies destination name filtering
            when matches are found, otherwise returns all available SNMP destinations.

        Args:
            network_element (dict): Configuration mapping containing API family and function details.
            filters (dict): Filter criteria containing component-specific filters for destinations.

        Returns:
            dict: A dictionary containing:
                - snmp_destinations (list): List of SNMP destination configurations including
                version, community strings, authentication, and privacy settings.
        """
        self.log(
            "Starting SNMP destination retrieval. Extracting component filters and "
            "destination names for filtering SNMP configurations.",
            "DEBUG"
        )

        component_specific_filters = filters.get("component_specific_filters", {})
        destination_filters = component_specific_filters.get("destination_filters", {})
        destination_names = destination_filters.get("destination_names", [])

        self.log(
            "Destination name filters extracted: {0} name(s) specified. Filter mode: {1}".format(
                len(destination_names),
                "name-based filtering" if destination_names else "retrieve all"
            ),
            "DEBUG"
        )

        api_family = network_element.get("api_family")
        api_function = network_element.get("api_function")

        self.log(
            "API details extracted - Family: {0}, Function: {1}. Calling API to retrieve "
            "SNMP destinations with pagination support.".format(api_family, api_function),
            "DEBUG"
        )

        try:
            snmp_configs = self.get_all_snmp_destinations(api_family, api_function)
            self.log(
                "Retrieved {0} SNMP destination(s) from Catalyst Center. Processing "
                "filtering logic based on destination_names.".format(len(snmp_configs)),
                "INFO"
            )

            if destination_names:
                self.log(
                    "Applying destination name filter: {0}. Searching for matching "
                    "SNMP configurations in retrieved destinations.".format(destination_names),
                    "DEBUG"
                )
                matching_configs = [config for config in snmp_configs if config.get("name") in destination_names]
                if matching_configs:
                    final_snmp_configs = matching_configs
                    self.log(
                        "Found {0} matching SNMP destination(s) for filter criteria. "
                        "Using filtered subset for YAML generation.".format(
                            len(matching_configs)
                        ),
                        "INFO"
                    )
                else:
                    final_snmp_configs = snmp_configs
                    self.log(
                        "No matching SNMP destinations found for filter: {0}. Including "
                        "all {1} SNMP destination(s) for comprehensive configuration "
                        "coverage.".format(destination_names, len(snmp_configs)),
                        "WARNING"
                    )
            else:
                self.log(
                    "No destination name filters provided. Including all {0} SNMP "
                    "destination(s) for YAML generation.".format(len(snmp_configs)),
                    "DEBUG"
                )
                final_snmp_configs = snmp_configs

        except Exception as e:
            self.log(
                "Exception occurred during SNMP destination retrieval. Exception type: "
                "{0}, Exception message: {1}. Returning empty list for graceful handling.".format(
                    type(e).__name__, str(e)
                ),
                "ERROR"
            )
            final_snmp_configs = []

        self.log(
            "Retrieving SNMP destination specification for parameter transformation. "
            "Calling snmp_destinations_temp_spec() for mapping rules.",
            "DEBUG"
        )

        snmp_destinations_temp_spec = self.snmp_destinations_temp_spec()

        self.log(
            "Transforming {0} SNMP destination(s) using specification. Converting "
            "camelCase API responses to snake_case YAML format with modify_parameters().".format(
                len(final_snmp_configs)
            ),
            "DEBUG"
        )
        modified_snmp_configs = self.modify_parameters(snmp_destinations_temp_spec, final_snmp_configs)

        result = {"snmp_destinations": modified_snmp_configs}
        self.log(
            "SNMP destination retrieval completed. Final result contains {0} "
            "transformed configuration(s) ready for YAML serialization.".format(
                len(modified_snmp_configs)
            ),
            "INFO"
        )
        return result

    def get_all_webhook_destinations(self, api_family, api_function):
        """
        Retrieves all webhook destinations using pagination from the API.

        Description:
            This helper method makes paginated API calls to fetch all webhook destination
            configurations from Cisco Catalyst Center. It handles API response variations
            and continues pagination until all destinations are retrieved.

        Args:
            api_family (str): The API family identifier for webhook destinations.
            api_function (str): The specific API function name for retrieving webhook destinations.

        Returns:
            list: A list of webhook destination dictionaries containing all available
            webhook configurations from the Cisco Catalyst Center.
        """
        self.log(
            "Retrieving all webhook destinations with pagination. API family: {0}, "
            "API function: {1}. Starting pagination loop with limit=10.".format(
                api_family, api_function
            ),
            "DEBUG"
        )
        try:
            offset = 0
            limit = 10
            all_webhooks = []
            page_count = 0

            while True:
                page_count += 1
                current_offset = offset * limit

                self.log(
                    "Fetching webhook destinations page {0} with offset={1}, limit={2}. "
                    "Calling API to retrieve webhook configurations.".format(
                        page_count, current_offset, limit
                    ),
                    "DEBUG"
                )
                response = self.dnac._exec(
                    family=api_family,
                    function=api_function,
                    op_modifies=False,
                    params={"offset": offset * limit, "limit": limit},
                )
                self.log(
                    "Received API response for webhook destinations page {0}. Response "
                    "type: {1}. Processing statusMessage field for webhook data.".format(
                        page_count, type(response).__name__
                    ),
                    "DEBUG"
                )

                webhooks = response.get("statusMessage", [])
                if not webhooks:
                    self.log(
                        "No webhook destinations found in page {0} response. statusMessage "
                        "field empty or missing. Terminating pagination loop.".format(
                            page_count
                        ),
                        "DEBUG"
                    )
                    break

                all_webhooks.extend(webhooks)
                self.log(
                    "Added {0} webhook destination(s) from page {1}. Total accumulated: "
                    "{2}. Checking if more pages available.".format(
                        len(webhooks), page_count, len(all_webhooks)
                    ),
                    "DEBUG"
                )

                if len(webhooks) < limit:
                    self.log(
                        "Received {0} webhook(s) in page {1}, which is less than limit "
                        "{2}. No more pages available. Terminating pagination.".format(
                            len(webhooks), page_count, limit
                        ),
                        "DEBUG"
                    )
                    break

                offset += 1
                self.log(
                    "Webhook destination retrieval completed successfully. Total pages "
                    "fetched: {0}, Total webhooks retrieved: {1}. Returning complete "
                    "webhook list.".format(page_count, len(all_webhooks)),
                    "INFO"
                )

            return all_webhooks

        except Exception as e:
            self.log(
                "Exception occurred during webhook destination retrieval. Exception "
                "type: {0}, Exception message: {1}. Returning empty list for graceful "
                "handling.".format(type(e).__name__, str(e)),
                "ERROR"
            )
            return []

    def get_all_email_destinations(self, api_family, api_function):
        """
        Retrieves all email destinations from the API.

        Description:
            This helper method fetches email destination configurations from Cisco Catalyst Center.
            It handles different response formats and extracts email configuration data including
            SMTP settings from the API response.

        Args:
            api_family (str): The API family identifier for email destinations.
            api_function (str): The specific API function name for retrieving email destinations.

        Returns:
            list: A list of email destination dictionaries containing all available
            email configurations including SMTP server details.
        """
        self.log(
            "Retrieving all email destinations from Catalyst Center. API family: {0}, "
            "API function: {1}. Calling API to fetch email configurations.".format(
                api_family, api_function
            ),
            "DEBUG"
        )
        try:
            response = self.dnac._exec(
                family=api_family,
                function=api_function,
                op_modifies=False,
            )
            self.log(
                "Received API response for email destinations. Response type: {0}. "
                "Processing response structure to extract email configuration data.".format(
                    type(response).__name__
                ),
                "DEBUG"
            )

            if isinstance(response, list):
                self.log(
                    "API response is list format with {0} email destination(s). Returning "
                    "email list directly for processing.".format(len(response)),
                    "INFO"
                )
                return response
            elif isinstance(response, dict):
                email_configs = response.get("response", [])
                self.log(
                    "API response is dictionary format. Extracted {0} email destination(s) "
                    "from response field. Returning email configurations.".format(
                        len(email_configs)
                    ),
                    "INFO"
                )
                return email_configs
            else:
                return []

        except Exception as e:
            self.log(
                "Exception occurred during email destination retrieval. Exception type: "
                "{0}, Exception message: {1}. Returning empty list for graceful handling.".format(
                    type(e).__name__, str(e)
                ),
                "ERROR"
            )
            return []

    def get_all_syslog_destinations(self, api_family, api_function):
        """
        Retrieves all syslog destinations from the API.

        Description:
            This helper method fetches syslog destination configurations from Cisco Catalyst Center.
            It extracts syslog configuration data from the API response and handles various
            response formats to ensure consistent data retrieval.

        Args:
            api_family (str): The API family identifier for syslog destinations.
            api_function (str): The specific API function name for retrieving syslog destinations.

        Returns:
            list: A list of syslog destination dictionaries containing server addresses,
            protocols, ports, and other syslog configuration parameters.
        """
        self.log(
            "Retrieving all syslog destinations from Catalyst Center. API family: {0}, "
            "API function: {1}. Calling API to fetch syslog configurations.".format(
                api_family, api_function
            ),
            "DEBUG"
        )
        try:
            response = self.dnac._exec(
                family=api_family,
                function=api_function,
                op_modifies=False,
                params={},
            )
            self.log(
                "Received API response for syslog destinations. Response type: {0}. "
                "Processing statusMessage field to extract syslog configuration data.".format(
                    type(response).__name__
                ),
                "DEBUG"
            )

            syslog_configs = response.get("statusMessage", [])

            if isinstance(syslog_configs, list):
                self.log(
                    "Extracted {0} syslog destination(s) from statusMessage field. "
                    "Returning syslog configurations for processing.".format(
                        len(syslog_configs)
                    ),
                    "INFO"
                )
                return syslog_configs
            else:
                self.log(
                    "statusMessage field has unexpected format. Expected list, got: {0}. "
                    "Returning empty list for graceful handling.".format(
                        type(syslog_configs).__name__
                    ),
                    "WARNING"
                )
                return []

        except Exception as e:
            self.log(
                "Exception occurred during syslog destination retrieval. Exception type: "
                "{0}, Exception message: {1}. Returning empty list for graceful handling.".format(
                    type(e).__name__, str(e)
                ),
                "ERROR"
            )
            return []

    def get_all_snmp_destinations(self, api_family, api_function):
        """
        Retrieves all SNMP destinations using pagination from the API.

        Description:
            This helper method makes paginated API calls to fetch all SNMP destination
            configurations from Cisco Catalyst Center. It handles pagination limits
            and continues until all SNMP destinations are retrieved.

        Args:
            api_family (str): The API family identifier for SNMP destinations.
            api_function (str): The specific API function name for retrieving SNMP destinations.

        Returns:
            list: A list of SNMP destination dictionaries containing IP addresses,
            ports, SNMP versions, community strings, and authentication details.
        """
        self.log(
            "Retrieving all SNMP destinations with pagination. API family: {0}, "
            "API function: {1}. Starting pagination loop with limit=10.".format(
                api_family, api_function
            ),
            "DEBUG"
        )
        try:
            offset = 0
            limit = 10
            all_snmp = []
            page_count = 0

            while True:
                page_count += 1
                current_offset = offset * limit

                self.log(
                    "Fetching SNMP destinations page {0} with offset={1}, limit={2}. "
                    "Calling API to retrieve SNMP configurations.".format(
                        page_count, current_offset, limit
                    ),
                    "DEBUG"
                )
                try:
                    response = self.dnac._exec(
                        family=api_family,
                        function=api_function,
                        op_modifies=False,
                        params={"offset": offset * limit, "limit": limit},
                    )
                    self.log(
                        "Received API response for SNMP destinations page {0}. Response "
                        "type: {1}. Processing response structure for SNMP data.".format(
                            page_count, type(response).__name__
                        ),
                        "DEBUG"
                    )

                    snmp_configs = response if isinstance(response, list) else []
                    if not snmp_configs:
                        self.log(
                            "No SNMP destinations found in page {0} response. Response "
                            "empty or invalid format. Terminating pagination loop.".format(
                                page_count
                            ),
                            "DEBUG"
                        )
                        break

                    all_snmp.extend(snmp_configs)
                    self.log(
                        "Added {0} SNMP destination(s) from page {1}. Total accumulated: "
                        "{2}. Checking if more pages available.".format(
                            len(snmp_configs), page_count, len(all_snmp)
                        ),
                        "DEBUG"
                    )

                    if len(snmp_configs) < limit:
                        self.log(
                            "Received {0} SNMP destination(s) in page {1}, which is less "
                            "than limit {2}. No more pages available. Terminating "
                            "pagination.".format(len(snmp_configs), page_count, limit),
                            "DEBUG"
                        )
                        break

                    offset += 1

                except Exception as e:
                    self.log(
                        "Exception in pagination loop for SNMP destinations at page {0}. "
                        "Exception type: {1}, Exception message: {2}. Breaking pagination "
                        "loop and returning accumulated results.".format(
                            page_count, type(e).__name__, str(e)
                        ),
                        "ERROR"
                    )
                    break

            self.log(
                "SNMP destination retrieval completed successfully. Total pages fetched: "
                "{0}, Total SNMP destinations retrieved: {1}. Returning complete SNMP "
                "list.".format(page_count, len(all_snmp)),
                "INFO"
            )

            return all_snmp

        except Exception as e:
            self.log(
                "Exception occurred during SNMP destination retrieval. Exception type: "
                "{0}, Exception message: {1}. Returning empty list for graceful "
                "handling.".format(type(e).__name__, str(e)),
                "ERROR"
            )
            return []

    def get_itsm_settings(self, network_element, filters):
        """
        Retrieves ITSM integration settings from Cisco Catalyst Center.

        Description:
            This method fetches ITSM (IT Service Management) integration configurations
            from the Cisco Catalyst Center API. It supports filtering by instance names
            and retrieves connection settings and authentication details.

        Args:
            network_element (dict): Configuration mapping containing API family and function details.
            filters (dict): Filter criteria containing ITSM-specific filters for instance names.

        Returns:
            dict: A dictionary containing:
                - itsm_settings (list): List of ITSM integration configurations including
                connection settings, URLs, and authentication parameters.
        """
        self.log(
            "Starting ITSM settings retrieval. Extracting component filters and instance "
            "names for filtering ITSM configurations.",
            "DEBUG"
        )

        component_specific_filters = filters.get("component_specific_filters", {})
        itsm_filters = component_specific_filters.get("itsm_filters", {})
        instance_names = itsm_filters.get("instance_names", [])

        self.log(
            "Instance name filters extracted: {0} name(s) specified. Filter mode: {1}".format(
                len(instance_names),
                "name-based filtering" if instance_names else "retrieve all"
            ),
            "DEBUG"
        )

        api_family = network_element.get("api_family")
        api_function = network_element.get("api_function")
        self.log(
            "API details extracted - Family: {0}, Function: {1}. Calling API to retrieve "
            "ITSM settings.".format(api_family, api_function),
            "DEBUG"
        )

        try:
            itsm_configs = self.get_all_itsm_settings(api_family, api_function)
            self.log(
                "Retrieved {0} ITSM setting(s) from Catalyst Center. Processing filtering "
                "logic based on instance_names.".format(len(itsm_configs)),
                "INFO"
            )

            if instance_names:
                self.log(
                    "Applying instance name filter: {0}. Searching for matching ITSM "
                    "settings in retrieved configurations.".format(instance_names),
                    "DEBUG"
                )
                final_itsm_configs = [config for config in itsm_configs if config.get("name") in instance_names]
                self.log(
                    "Found {0} matching ITSM setting(s) for filter criteria. Using filtered "
                    "subset for YAML generation.".format(len(final_itsm_configs)),
                    "INFO"
                )
            else:
                final_itsm_configs = itsm_configs
                self.log(
                    "No instance name filters provided. Including all {0} ITSM setting(s) "
                    "for YAML generation.".format(len(itsm_configs)),
                    "DEBUG"
                )

        except Exception as e:
            self.log(
                "Exception occurred during ITSM settings retrieval. Exception type: {0}, "
                "Exception message: {1}. Returning empty list for graceful handling.".format(
                    type(e).__name__, str(e)
                ),
                "ERROR"
            )
            final_itsm_configs = []

        self.log(
            "Retrieving ITSM settings specification for parameter transformation. Calling "
            "itsm_settings_temp_spec() for mapping rules.",
            "DEBUG"
        )

        itsm_settings_temp_spec = self.itsm_settings_temp_spec()

        self.log(
            "Transforming {0} ITSM setting(s) using specification. Converting camelCase "
            "API responses to snake_case YAML format with modify_parameters().".format(
                len(final_itsm_configs)
            ),
            "DEBUG"
        )
        modified_itsm_configs = self.modify_parameters(itsm_settings_temp_spec, final_itsm_configs)

        result = {"itsm_settings": modified_itsm_configs}
        self.log(
            "ITSM settings retrieval completed. Final result contains {0} transformed "
            "configuration(s) ready for YAML serialization.".format(
                len(modified_itsm_configs)
            ),
            "INFO"
        )

        return result

    def get_all_itsm_settings(self, api_family, api_function):
        """
        Retrieves all ITSM integration settings from the API.

        Description:
            This helper method fetches ITSM integration configurations from Cisco Catalyst Center.
            It handles different response formats and extracts ITSM configuration data
            including connection settings and authentication details.

        Args:
            api_family (str): The API family identifier for ITSM settings.
            api_function (str): The specific API function name for retrieving ITSM settings.

        Returns:
            list: A list of ITSM setting dictionaries containing instance names,
            descriptions, and connection configuration details.
        """
        self.log(
            "Retrieving all ITSM settings from Catalyst Center. API family: {0}, "
            "API function: {1}. Calling API to fetch ITSM configurations.".format(
                api_family, api_function
            ),
            "DEBUG"
        )
        try:
            response = self.dnac._exec(
                family=api_family,
                function=api_function,
                op_modifies=False,
            )
            self.log(
                "Received API response for ITSM settings. Response type: {0}. "
                "Processing response structure to extract ITSM configuration data.".format(
                    type(response).__name__
                ),
                "DEBUG"
            )

            if isinstance(response, dict):
                itsm_settings = response.get("response", [])

                if isinstance(itsm_settings, list):
                    self.log(
                        "Extracted {0} ITSM setting(s) from response field. Returning "
                        "ITSM configurations for processing.".format(len(itsm_settings)),
                        "INFO"
                    )
                    return itsm_settings
                else:
                    self.log(
                        "Response field has unexpected format. Expected list, got: {0}. "
                        "Returning empty list for graceful handling.".format(
                            type(itsm_settings).__name__
                        ),
                        "WARNING"
                    )
                    return []
            elif isinstance(response, list):
                self.log(
                    "API response is list format with {0} ITSM setting(s). Returning "
                    "settings list directly for processing.".format(len(response)),
                    "INFO"
                )
                return response

            else:
                self.log(
                    "API response has unexpected format. Response type: {0}. Returning "
                    "empty list for graceful handling.".format(type(response).__name__),
                    "WARNING"
                )
                return []

        except Exception as e:
            self.log(
                "Exception occurred during ITSM settings retrieval. Exception type: {0}, "
                "Exception message: {1}. Returning empty list for graceful handling.".format(
                    type(e).__name__, str(e)
                ),
                "ERROR"
            )
            self.set_operation_result("failed", True, self.msg, "ERROR")

    def get_webhook_event_notifications(self, network_element, filters):
        """
        Retrieves webhook event notification subscriptions from Cisco Catalyst Center.

        Description:
            This method fetches webhook event notification configurations from the API.
            It supports filtering by subscription names and retrieves event subscription
            details including sites, events, and destination mappings.

        Args:
            network_element (dict): Configuration mapping containing API family and function details.
            filters (dict): Filter criteria containing notification-specific filters.

        Returns:
            dict: A dictionary containing:
                - webhook_event_notifications (list): List of webhook event subscription
                configurations with sites, events, and destination details.
        """
        self.log(
            "Starting webhook event notification retrieval. Extracting component filters "
            "and subscription names for filtering webhook event configurations.",
            "DEBUG"
        )

        component_specific_filters = filters.get("component_specific_filters", {})
        notification_filters = component_specific_filters.get("notification_filters", {})
        subscription_names = notification_filters.get("subscription_names", [])
        self.log(
            "Subscription name filters extracted: {0} name(s) specified. Filter mode: {1}".format(
                len(subscription_names),
                "name-based filtering" if subscription_names else "retrieve all"
            ),
            "DEBUG"
        )

        api_family = network_element.get("api_family")
        api_function = network_element.get("api_function")
        self.log(
            "API details extracted - Family: {0}, Function: {1}. Calling API to retrieve "
            "webhook event notifications.".format(api_family, api_function),
            "DEBUG"
        )

        try:
            notification_configs = self.get_all_webhook_event_notifications(api_family, api_function)
            self.log(
                "Retrieved {0} webhook event notification(s) from Catalyst Center. "
                "Processing filtering logic based on subscription_names.".format(
                    len(notification_configs)
                ),
                "INFO"
            )

            if subscription_names:
                self.log(
                    "Applying subscription name filter: {0}. Searching for matching "
                    "webhook event notifications in retrieved configurations.".format(
                        subscription_names
                    ),
                    "DEBUG"
                )

                matching_configs = [
                    config for config in notification_configs
                    if config.get("name") in subscription_names
                ]

                if matching_configs:
                    final_notification_configs = matching_configs
                    self.log(
                        "Found {0} matching webhook event notification(s) for filter "
                        "criteria. Using filtered subset for YAML generation.".format(
                            len(matching_configs)
                        ),
                        "INFO"
                    )
                else:
                    final_notification_configs = notification_configs
                    self.log(
                        "No matching webhook event notifications found for filter: {0}. "
                        "Including all {1} notification(s) for comprehensive configuration "
                        "coverage.".format(subscription_names, len(notification_configs)),
                        "WARNING"
                    )
            else:
                final_notification_configs = notification_configs
                self.log(
                    "No subscription name filters provided. Including all {0} webhook "
                    "event notification(s) for YAML generation.".format(
                        len(notification_configs)
                    ),
                    "DEBUG"
                )

        except Exception as e:
            self.log(
                "Exception occurred during webhook event notification retrieval. Exception "
                "type: {0}, Exception message: {1}. Returning empty list for graceful "
                "handling.".format(type(e).__name__, str(e)),
                "ERROR"
            )
            final_notification_configs = []

        self.log(
            "Retrieving webhook event notification specification for parameter "
            "transformation. Calling webhook_event_notifications_temp_spec() for mapping "
            "rules.",
            "DEBUG"
        )

        webhook_event_notifications_temp_spec = self.webhook_event_notifications_temp_spec()

        self.log(
            "Transforming {0} webhook event notification(s) using specification. Converting "
            "camelCase API responses to snake_case YAML format with modify_parameters().".format(
                len(final_notification_configs)
            ),
            "DEBUG"
        )
        modified_notification_configs = self.modify_parameters(webhook_event_notifications_temp_spec, final_notification_configs)

        result = {"webhook_event_notifications": modified_notification_configs}
        self.log(
            "Webhook event notification retrieval completed. Final result contains {0} "
            "transformed configuration(s) ready for YAML serialization.".format(
                len(modified_notification_configs)
            ),
            "INFO"
        )
        return result

    def get_all_webhook_event_notifications(self, api_family, api_function):
        """
        Retrieves all webhook event notifications using pagination from the API.

        Description:
            This helper method makes paginated API calls to fetch all webhook event
            notification subscriptions from Cisco Catalyst Center. It handles various
            response formats and continues pagination until all notifications are retrieved.

        Args:
            api_family (str): The API family identifier for webhook event notifications.
            api_function (str): The specific API function name for retrieving webhook notifications.

        Returns:
            list: A list of webhook event notification dictionaries containing subscription
            details, event types, sites, and endpoint configurations.
        """
        self.log(
            "Retrieving all webhook event notifications with pagination. API family: {0}, "
            "API function: {1}. Starting pagination loop with limit=10.".format(
                api_family, api_function
            ),
            "DEBUG"
        )
        try:
            offset = 0
            limit = 10
            all_notifications = []
            page_count = 0

            while True:
                page_count += 1

                self.log(
                    "Fetching webhook event notifications page {0} with offset={1}, limit={2}. "
                    "Calling API to retrieve webhook subscription configurations.".format(
                        page_count, offset, limit
                    ),
                    "DEBUG"
                )
                try:
                    response = self.dnac._exec(
                        family=api_family,
                        function=api_function,
                        op_modifies=False,
                        params={"offset": offset, "limit": limit},
                    )
                    self.log(
                        "Received API response for webhook event notifications page {0}. "
                        "Response type: {1}. Processing response structure for subscription data.".format(
                            page_count, type(response).__name__
                        ),
                        "DEBUG"
                    )

                    if isinstance(response, list):
                        self.log(
                            "API response is list format with {0} webhook event notification(s). ".format(
                                len(response)
                            ),
                            "DEBUG"
                        )
                        notifications = response
                    elif isinstance(response, dict):
                        self.log(
                            "API response is dictionary format. Extracting webhook event "
                            "notification(s) from response field.",
                            "DEBUG"
                        )
                        notifications = response.get("response", [])
                    else:
                        self.log(
                            "API response has unexpected format. Response type: {0}. Expected list or dictionary.".format(
                                type(response).__name__
                            ),
                            "ERROR"
                        )
                        notifications = []

                    if not notifications:
                        self.log(
                            "No webhook event notifications found in page {0} response. Response "
                            "empty or invalid format. Terminating pagination loop.".format(page_count),
                            "DEBUG"
                        )
                        break

                    all_notifications.extend(notifications)
                    self.log(
                        "Added {0} webhook event notification(s) from page {1}. Total "
                        "accumulated: {2}. Checking if more pages available.".format(
                            len(notifications), page_count, len(all_notifications)
                        ),
                        "DEBUG"
                    )

                    if len(notifications) < limit:
                        self.log(
                            "Received {0} webhook event notification(s) in page {1}, which is "
                            "less than limit {2}. No more pages available. Terminating pagination.".format(
                                len(notifications), page_count, limit
                            ),
                            "DEBUG"
                        )
                        break

                    offset += limit

                except Exception as e:
                    self.log(
                        "Exception in pagination loop for webhook event notifications at page {0}. "
                        "Exception type: {1}, Exception message: {2}. Breaking pagination loop "
                        "and returning accumulated results.".format(
                            page_count, type(e).__name__, str(e)
                        ),
                        "ERROR"
                    )
                    self.set_operation_result("failed", True, self.msg, "ERROR")

            self.log(
                "Webhook event notification retrieval completed successfully. Total pages "
                "fetched: {0}, Total webhook event notifications retrieved: {1}. Returning "
                "complete notification list.".format(page_count, len(all_notifications)),
                "INFO"
            )

            return all_notifications

        except Exception as e:
            self.log(
                "Exception occurred during webhook event notification retrieval. Exception "
                "type: {0}, Exception message: {1}. Returning empty list for graceful handling.".format(
                    type(e).__name__, str(e)
                ),
                "ERROR"
            )
            return []

    def get_email_event_notifications(self, network_element, filters):
        """
        Retrieves email event notification subscriptions from Cisco Catalyst Center.

        Description:
            This method fetches email event notification configurations from the API.
            It processes subscription endpoints to extract email-specific details including
            sender addresses, recipient lists, and subject templates.

        Args:
            network_element (dict): Configuration mapping containing API family and function details.
            filters (dict): Filter criteria containing notification-specific filters.

        Returns:
            dict: A dictionary containing:
                - email_event_notifications (list): List of email event subscription
                configurations with email addresses, subjects, and event details.
        """
        self.log(
            "Starting email event notification retrieval. Extracting component filters "
            "and subscription names for filtering email event configurations.",
            "DEBUG"
        )
        component_specific_filters = filters.get("component_specific_filters", {})
        notification_filters = component_specific_filters.get("notification_filters", {})
        subscription_names = notification_filters.get("subscription_names", [])

        self.log(
            "Subscription name filters extracted: {0} name(s) specified. Filter mode: {1}".format(
                len(subscription_names),
                "name-based filtering" if subscription_names else "retrieve all"
            ),
            "DEBUG"
        )

        api_family = network_element.get("api_family")
        api_function = network_element.get("api_function")

        self.log(
            "Subscription name filters extracted: {0} name(s) specified. Filter mode: {1}".format(
                len(subscription_names),
                "name-based filtering" if subscription_names else "retrieve all"
            ),
            "DEBUG"
        )

        try:
            notification_configs = self.get_all_email_event_notifications(api_family, api_function)
            self.log(
                "Retrieved {0} email event notification(s) from Catalyst Center. "
                "Processing filtering logic based on subscription_names.".format(
                    len(notification_configs)
                ),
                "INFO"
            )

            if subscription_names:
                self.log(
                    "Applying subscription name filter: {0}. Searching for matching "
                    "email event notifications in retrieved configurations.".format(
                        subscription_names
                    ),
                    "DEBUG"
                )

                matching_configs = [
                    config for config in notification_configs
                    if config.get("name") in subscription_names
                ]

                if matching_configs:
                    final_notification_configs = matching_configs
                    self.log(
                        "Found {0} matching email event notification(s) for filter "
                        "criteria. Using filtered subset for YAML generation.".format(
                            len(matching_configs)
                        ),
                        "INFO"
                    )
                else:
                    final_notification_configs = notification_configs
                    self.log(
                        "No matching email event notifications found for filter: {0}. "
                        "Including all {1} notification(s) for comprehensive configuration "
                        "coverage.".format(subscription_names, len(notification_configs)),
                        "WARNING"
                    )
            else:
                final_notification_configs = notification_configs
                self.log(
                    "No subscription name filters provided. Including all {0} email "
                    "event notification(s) for YAML generation.".format(
                        len(notification_configs)
                    ),
                    "DEBUG"
                )

        except Exception as e:
            self.log(
                "Exception occurred during email event notification retrieval. Exception "
                "type: {0}, Exception message: {1}. Returning empty list for graceful "
                "handling.".format(type(e).__name__, str(e)),
                "ERROR"
            )
            final_notification_configs = []

        self.log(
            "Retrieving email event notification specification for parameter transformation. "
            "Calling email_event_notifications_temp_spec() for mapping rules.",
            "DEBUG"
        )

        email_event_notifications_temp_spec = self.email_event_notifications_temp_spec()

        self.log(
            "Transforming {0} email event notification(s) using specification. Converting "
            "camelCase API responses to snake_case YAML format with modify_parameters().".format(
                len(final_notification_configs)
            ),
            "DEBUG"
        )
        modified_notification_configs = self.modify_parameters(email_event_notifications_temp_spec, final_notification_configs)

        result = {"email_event_notifications": modified_notification_configs}
        self.log(
            "Email event notification retrieval completed. Final result contains {0} "
            "transformed configuration(s) ready for YAML serialization.".format(
                len(modified_notification_configs)
            ),
            "INFO"
        )
        return result

    def get_all_email_event_notifications(self, api_family, api_function):
        """
        Retrieves all email event notifications from the API.

        Description:
            This helper method fetches email event notification configurations from
            Cisco Catalyst Center. It handles different response formats and extracts
            email subscription data from the API response.

        Args:
            api_family (str): The API family identifier for email event notifications.
            api_function (str): The specific API function name for retrieving email notifications.

        Returns:
            list: A list of email event notification dictionaries containing subscription
            endpoints, event filters, and email configuration details.
        """
        self.log(
            "Retrieving all email event notifications from Catalyst Center. API family: {0}, "
            "API function: {1}. Calling API to fetch email subscription configurations.".format(
                api_family, api_function
            ),
            "DEBUG"
        )
        try:
            response = self.dnac._exec(
                family=api_family,
                function=api_function,
                op_modifies=False,
                params={}
            )
            self.log(
                "Received API response for email event notifications. Response type: {0}. "
                "Processing response structure to extract subscription data.".format(
                    type(response).__name__
                ),
                "DEBUG"
            )

            if isinstance(response, list):
                notifications = response
                self.log(
                    "API response is list format with {0} email event notification(s). "
                    "Returning notification list directly for processing.".format(len(response)),
                    "INFO"
                )

            elif isinstance(response, dict):
                notifications = response.get("response", [])
                self.log(
                    "API response is dictionary format. Extracted {0} email event notification(s) "
                    "from response field. Returning subscription configurations.".format(
                        len(notifications)
                    ),
                    "INFO"
                )

            else:
                self.log(
                    "API response has unexpected format. Response type: {0}. Returning empty "
                    "list for graceful handling.".format(type(response).__name__),
                    "WARNING"
                )
                notifications = []

            return notifications

        except Exception as e:
            self.log(
                "Exception occurred during email event notification retrieval. Exception type: "
                "{0}, Exception message: {1}. Returning empty list for graceful handling.".format(
                    type(e).__name__, str(e)
                ),
                "ERROR"
            )
            return []

    def get_syslog_event_notifications(self, network_element, filters):
        """
        Retrieves syslog event notification subscriptions from Cisco Catalyst Center.

        Description:
            This method fetches syslog event notification configurations from the API.
            It supports filtering by subscription names and retrieves event subscription
            details including sites, events, and syslog destination mappings.

        Args:
            network_element (dict): Configuration mapping containing API family and function details.
            filters (dict): Filter criteria containing notification-specific filters.

        Returns:
            dict: A dictionary containing:
                - syslog_event_notifications (list): List of syslog event subscription
                configurations with sites, events, and destination details.
        """
        self.log(
            "Starting syslog event notification retrieval. Extracting component filters "
            "and subscription names for filtering syslog event configurations.",
            "DEBUG"
        )

        component_specific_filters = filters.get("component_specific_filters", {})
        notification_filters = component_specific_filters.get("notification_filters", {})
        subscription_names = notification_filters.get("subscription_names", [])

        self.log(
            "Subscription name filters extracted: {0} name(s) specified. Filter mode: {1}".format(
                len(subscription_names),
                "name-based filtering" if subscription_names else "retrieve all"
            ),
            "DEBUG"
        )

        api_family = network_element.get("api_family")
        api_function = network_element.get("api_function")

        self.log(
            "API details extracted - Family: {0}, Function: {1}. Calling API to retrieve "
            "syslog event notifications.".format(api_family, api_function),
            "DEBUG"
        )

        try:
            notification_configs = self.get_all_syslog_event_notifications(api_family, api_function)
            self.log(
                "Retrieved {0} syslog event notification(s) from Catalyst Center. "
                "Processing filtering logic based on subscription_names.".format(
                    len(notification_configs)
                ),
                "INFO"
            )

            if subscription_names:
                self.log(
                    "Applying subscription name filter: {0}. Searching for matching "
                    "syslog event notifications in retrieved configurations.".format(
                        subscription_names
                    ),
                    "DEBUG"
                )

                matching_configs = [
                    config for config in notification_configs
                    if config.get("name") in subscription_names
                ]

                if matching_configs:
                    final_notification_configs = matching_configs
                    self.log(
                        "Found {0} matching syslog event notification(s) for filter "
                        "criteria. Using filtered subset for YAML generation.".format(
                            len(matching_configs)
                        ),
                        "INFO"
                    )
                else:
                    final_notification_configs = matching_configs
                    self.log(
                        "No matching syslog event notifications found for filter: {0}. "
                        "Including all {1} notification(s) for comprehensive configuration "
                        "coverage.".format(subscription_names, len(notification_configs)),
                        "WARNING"
                    )
            else:
                final_notification_configs = notification_configs
                self.log(
                    "No subscription name filters provided. Including all {0} syslog "
                    "event notification(s) for YAML generation.".format(
                        len(notification_configs)
                    ),
                    "DEBUG"
                )

        except Exception as e:
            self.log(
                "Exception occurred during syslog event notification retrieval. Exception "
                "type: {0}, Exception message: {1}. Returning empty list for graceful "
                "handling.".format(type(e).__name__, str(e)),
                "ERROR"
            )
            final_notification_configs = []

        self.log(
            "Retrieving syslog event notification specification for parameter "
            "transformation. Calling syslog_event_notifications_temp_spec() for mapping "
            "rules.",
            "DEBUG"
        )

        syslog_event_notifications_temp_spec = self.syslog_event_notifications_temp_spec()

        self.log(
            "Transforming {0} syslog event notification(s) using specification. Converting "
            "camelCase API responses to snake_case YAML format with modify_parameters().".format(
                len(final_notification_configs)
            ),
            "DEBUG"
        )
        modified_notification_configs = self.modify_parameters(syslog_event_notifications_temp_spec, final_notification_configs)

        result = {"syslog_event_notifications": modified_notification_configs}
        self.log(
            "Syslog event notification retrieval completed. Final result contains {0} "
            "transformed configuration(s) ready for YAML serialization.".format(
                len(modified_notification_configs)
            ),
            "INFO"
        )

        return result

    def get_all_syslog_event_notifications(self, api_family, api_function):
        """
        Retrieves all syslog event notifications using pagination from the API.

        Description:
            This helper method makes paginated API calls to fetch all syslog event
            notification subscriptions from Cisco Catalyst Center. It handles pagination
            and various response formats until all notifications are retrieved.

        Args:
            api_family (str): The API family identifier for syslog event notifications.
            api_function (str): The specific API function name for retrieving syslog notifications.

        Returns:
            list: A list of syslog event notification dictionaries containing subscription
            details, event types, sites, and syslog destination configurations.
        """
        self.log(
            "Retrieving all syslog event notifications with pagination. API family: {0}, "
            "API function: {1}. Starting pagination loop with limit=10.".format(
                api_family, api_function
            ),
            "DEBUG"
        )
        try:
            offset = 0
            limit = 10
            all_notifications = []
            page_count = 0

            while True:
                page_count += 1

                self.log(
                    "Fetching syslog event notifications page {0} with offset={1}, limit={2}. "
                    "Calling API to retrieve syslog subscription configurations.".format(
                        page_count, offset, limit
                    ),
                    "DEBUG"
                )
                try:
                    response = self.dnac._exec(
                        family=api_family,
                        function=api_function,
                        op_modifies=False,
                        params={"offset": offset, "limit": limit},
                    )
                    self.log(
                        "Received API response for syslog event notifications page {0}. "
                        "Response type: {1}. Processing response structure for subscription data.".format(
                            page_count, type(response).__name__
                        ),
                        "DEBUG"
                    )

                    if isinstance(response, list):
                        self.log(
                            "API response is list format with {0} syslog event notification(s). ".format(
                                len(response)
                            ),
                            "DEBUG"
                        )
                        notifications = response
                    elif isinstance(response, dict):
                        self.log(
                            "API response is dictionary format. Extracting syslog event notifications.",
                            "DEBUG"
                        )
                        notifications = response.get("response", [])
                    else:
                        self.log(
                            "API response is unrecognized format. No syslog event notifications extracted.",
                            "DEBUG"
                        )
                        notifications = []

                    if not notifications:
                        self.log(
                            "No syslog event notifications found in page {0} response. Response "
                            "empty or invalid format. Terminating pagination loop.".format(page_count),
                            "DEBUG"
                        )
                        break

                    all_notifications.extend(notifications)
                    self.log(
                        "Added {0} syslog event notification(s) from page {1}. Total "
                        "accumulated: {2}. Checking if more pages available.".format(
                            len(notifications), page_count, len(all_notifications)
                        ),
                        "DEBUG"
                    )

                    if len(notifications) < limit:
                        self.log(
                            "Received {0} syslog event notification(s) in page {1}, which is "
                            "less than limit {2}. No more pages available. Terminating pagination.".format(
                                len(notifications), page_count, limit
                            ),
                            "DEBUG"
                        )
                        break

                    offset += limit

                except Exception as e:
                    self.log(
                        "Exception in pagination loop for syslog event notifications at page {0}. "
                        "Exception type: {1}, Exception message: {2}. Breaking pagination loop "
                        "and returning accumulated results.".format(
                            page_count, type(e).__name__, str(e)
                        ),
                        "ERROR"
                    )
                    break

            self.log(
                "Syslog event notification retrieval completed successfully. Total pages "
                "fetched: {0}, Total syslog event notifications retrieved: {1}. Returning "
                "complete notification list.".format(page_count, len(all_notifications)),
                "INFO"
            )

            return all_notifications

        except Exception as e:
            self.log(
                "Exception occurred during syslog event notification retrieval. Exception "
                "type: {0}, Exception message: {1}. Returning empty list for graceful handling.".format(
                    type(e).__name__, str(e)
                ),
                "ERROR"
            )
            return []

    def modify_parameters(self, temp_spec, details_list):
        """
        Transforms API response data according to specification while removing null values.

        Description:
            This method converts raw API response data into structured configurations based
            on the provided specification. It removes parameters with null values to keep
            the generated YAML clean and handles nested configurations like SMTP settings
            and headers. The method preserves essential structures while filtering out
            unnecessary null entries.

        Args:
            temp_spec (OrderedDict): Specification defining the structure and transformation
                rules for converting API data to playbook format.
            details_list (list): List of dictionaries containing raw API response data
                to be transformed.

        Returns:
            list: A list of transformed configuration dictionaries with null values removed
            and parameters mapped according to the specification rules.
        """
        self.log(
            "Starting parameter transformation for {0} configuration item(s) using "
            "provided specification. Details list contains: {1}".format(
                len(details_list) if details_list else 0, details_list
            ),
            "DEBUG"
        )

        if not details_list:
            self.log("No configuration details provided for transformation. Returning empty list.", "DEBUG")
            return []

        modified_configs = []
        items_processed = 0
        items_skipped = 0

        for detail_index, detail in enumerate(details_list, start=1):
            self.log(
                "Processing configuration item {0}/{1}. Validating item type and structure.".format(
                    detail_index, len(details_list)
                ),
                "DEBUG"
            )
            if not isinstance(detail, dict):
                items_skipped += 1
                self.log(
                    "Skipping configuration item {0}/{1} - invalid type: {2}. Expected dictionary.".format(
                        detail_index, len(details_list), type(detail).__name__
                    ),
                    "WARNING"
                )
                continue

            mapped_config = OrderedDict()
            fields_mapped = 0

            for spec_key, spec_def in temp_spec.items():
                source_key = spec_def.get("source_key", spec_key)
                value = detail.get(source_key)
                self.log(
                    "Mapping field '{0}' from source key '{1}' in item {2}/{3}. "
                    "Value type: {4}, Has nested options: {5}".format(
                        spec_key, source_key, detail_index, len(details_list),
                        type(value).__name__, bool(spec_def.get("options"))
                    ),
                    "DEBUG"
                )

                if spec_def.get("options") and isinstance(value, list):
                    self.log(
                        "Processing nested list for field '{0}' with {1} item(s). "
                        "Applying nested specification mapping.".format(spec_key, len(value)),
                        "DEBUG"
                    )
                    nested_list = []
                    for nested_index, item in enumerate(value, start=1):
                        if isinstance(item, dict):
                            nested_mapped = OrderedDict()
                            for nested_key, nested_spec in spec_def["options"].items():
                                nested_source_key = nested_spec.get("source_key", nested_key)
                                nested_value = item.get(nested_source_key)

                                transform = nested_spec.get("transform")
                                if transform and callable(transform):
                                    self.log(
                                        "Applying transformation function to nested field '{0}' "
                                        "in item {1}/{2}.".format(
                                            nested_key, nested_index, len(value)
                                        ),
                                        "DEBUG"
                                    )
                                    nested_value = transform(nested_value)

                                if nested_value is not None:
                                    nested_mapped[nested_key] = nested_value

                            if nested_mapped:
                                nested_list.append(nested_mapped)

                    if nested_list:
                        mapped_config[spec_key] = nested_list
                        fields_mapped += 1
                        self.log(
                            "Successfully mapped nested list field '{0}' with {1} valid item(s).".format(
                                spec_key, len(nested_list)
                            ),
                            "DEBUG"
                        )

                elif spec_def.get("options") and isinstance(value, dict):
                    self.log(
                        "Processing nested dictionary for field '{0}'. Applying nested "
                        "specification mapping to configuration structure.".format(spec_key),
                        "DEBUG"
                    )
                    nested_mapped = OrderedDict()
                    has_non_null_values = False

                    for nested_key, nested_spec in spec_def["options"].items():
                        nested_source_key = nested_spec.get("source_key", nested_key)
                        nested_value = value.get(nested_source_key)

                        transform = nested_spec.get("transform")
                        if transform and callable(transform):
                            self.log(
                                "Applying transformation function to nested field '{0}' "
                                "in dict structure.".format(nested_key),
                                "DEBUG"
                            )
                            nested_value = transform(nested_value)

                        if nested_value is not None:
                            nested_mapped[nested_key] = nested_value
                            has_non_null_values = True

                    if has_non_null_values and nested_mapped:
                        mapped_config[spec_key] = nested_mapped
                        fields_mapped += 1
                        self.log(
                            "Successfully mapped nested dict field '{0}' with {1} non-null field(s).".format(
                                spec_key, len(nested_mapped)
                            ),
                            "DEBUG"
                        )

                elif spec_def.get("options") and value is None:
                    if spec_key == "primary_smtp_config":
                        smtp_keys = ["primarySMTPConfig", "fromEmail", "toEmail"]
                        if any(detail.get(smtp_key) for smtp_key in smtp_keys):
                            self.log(
                                "Creating placeholder SMTP config structure for field '{0}' "
                                "due to presence of related email fields.".format(spec_key),
                                "DEBUG"
                            )
                            nested_mapped = OrderedDict()
                            for nested_key, nested_spec in spec_def["options"].items():
                                if nested_key in ["server_address", "smtp_type", "port"]:
                                    nested_mapped[nested_key] = None
                            if nested_mapped:
                                mapped_config[spec_key] = nested_mapped
                                fields_mapped += 1

                else:
                    if value is not None:
                        transform = spec_def.get("transform")
                        if transform and callable(transform):
                            self.log(
                                "Applying transformation function to field '{0}' with "
                                "entire detail object as context.".format(spec_key),
                                "DEBUG"
                            )
                            transformed_value = transform(detail)
                            if transformed_value is not None:
                                mapped_config[spec_key] = transformed_value
                                fields_mapped += 1
                        else:
                            mapped_config[spec_key] = value
                            fields_mapped += 1

                    elif spec_def.get("transform"):
                        transform = spec_def.get("transform")
                        if transform and callable(transform):
                            self.log(
                                "Applying transformation function to field '{0}' with "
                                "null source value using detail context.".format(spec_key),
                                "DEBUG"
                            )
                            transformed_value = transform(detail)
                            if transformed_value is not None:
                                mapped_config[spec_key] = transformed_value
                                fields_mapped += 1

            if mapped_config:
                modified_configs.append(mapped_config)
                items_processed += 1
                self.log(
                    "Successfully processed configuration item {0}/{1} with {2} field(s) "
                    "mapped. Added to final configuration list.".format(
                        detail_index, len(details_list), fields_mapped
                    ),
                    "DEBUG"
                )
            else:
                items_skipped += 1
                self.log(
                    "Skipped configuration item {0}/{1} - no valid fields mapped after "
                    "transformation and null filtering.".format(detail_index, len(details_list)),
                    "WARNING"
                )

        self.log(
            "Parameter transformation completed successfully. Processed {0} item(s), "
            "skipped {1} item(s). Final configuration list contains {2} valid "
            "configuration(s) ready for YAML serialization.".format(
                items_processed, items_skipped, len(modified_configs)
            ),
            "INFO"
        )
        return modified_configs

    def yaml_config_generator(self, yaml_config_generator):
        """
        Generates comprehensive YAML configuration files for events and notifications.

        Description:
            This method orchestrates the complete YAML generation process by processing
            configuration parameters, retrieving data for specified components, and
            creating structured YAML files. It handles component validation, data
            retrieval coordination, and file generation with proper error handling
            and logging throughout the process.

        Args:
            yaml_config_generator (dict): Configuration parameters including file path,
                component filters, and generation options.

        Returns:
            object: Self instance with updated status and results. Sets operation
            result to success with file path information or failure with error details.
        """
        self.log(
            "Starting YAML configuration generation workflow. Configuration parameters: "
            "{0}".format(yaml_config_generator),
            "DEBUG"
        )

        # Check if generate_all_configurations is enabled
        generate_all = yaml_config_generator.get("generate_all_configurations", False)
        file_path = yaml_config_generator.get("file_path")

        if not file_path:
            file_path = self.generate_filename()
            self.log(
                "No file path provided in configuration. Generated default filename: {0} "
                "for YAML output.".format(file_path),
                "DEBUG"
            )
        else:
            self.log(
                "Using provided file path for YAML output: {0}".format(file_path),
                "DEBUG"
            )

        component_specific_filters = yaml_config_generator.get("component_specific_filters") or {}

        # Set defaults for generate_all_configurations mode
        if generate_all:
            self.log(
                "Generate all configurations mode enabled. Automatically including all "
                "supported event and notification components for comprehensive discovery.",
                "INFO"
            )
            if not component_specific_filters.get("components_list"):
                component_specific_filters["components_list"] = [
                    "webhook_destinations",
                    "email_destinations",
                    "syslog_destinations",
                    "snmp_destinations",
                    "itsm_settings",
                    "webhook_event_notifications",
                    "email_event_notifications",
                    "syslog_event_notifications"
                ]
                self.log(
                    "Set default components list with all {0} supported component types "
                    "for complete configuration capture.".format(
                        len(component_specific_filters["components_list"])
                    ),
                    "DEBUG"
                )

        # Validate components_list
        components_list = component_specific_filters.get("components_list", [])
        if components_list:
            self.log(
                "Validating {0} component(s) against allowed component types: {1}".format(
                    len(components_list), components_list
                ),
                "DEBUG"
            )
            allowed_components = list(self.module_schema["network_elements"].keys())
            invalid_components = [comp for comp in components_list if comp not in allowed_components]

            if invalid_components:
                error_message = (
                    "Invalid components found in components_list: {0}. "
                    "Only the following components are allowed: {1}. "
                    "Please remove the invalid components and try again.".format(
                        invalid_components, allowed_components
                    )
                )
                response_data = {
                    "message": error_message,
                    "status": "failed"
                }
                self.msg = response_data
                self.result["response"] = response_data
                self.set_operation_result("failed", False, error_message, "ERROR")
                self.log(
                    "Component validation failed. Found {0} invalid component(s) that do not "
                    "match allowed component types.".format(len(invalid_components)),
                    "ERROR"
                )
                return self

        try:
            self.log(
                "Beginning component processing loop for {0} component(s). Retrieving "
                "configurations from Catalyst Center.".format(len(components_list)),
                "DEBUG"
            )
            final_config = {}

            components_processed = 0
            components_skipped = 0
            total_configurations = 0

            for component_index, component in enumerate(components_list, start=1):
                self.log(
                    "Processing component {0}/{1}: {2}. Checking if component exists in "
                    "module schema mapping.".format(
                        component_index, len(components_list), component
                    ),
                    "DEBUG"
                )
                if component in self.module_schema["network_elements"]:
                    component_info = self.module_schema["network_elements"][component]
                    get_function = component_info.get("get_function_name")

                    if get_function and callable(get_function):
                        self.log(
                            "Calling getter function for component {0}/{1}: {2}. Retrieving "
                            "configurations with applied filters.".format(
                                component_index, len(components_list), component
                            ),
                            "DEBUG"
                        )
                        try:
                            result = get_function(component_info, {"component_specific_filters": component_specific_filters})

                            if isinstance(result, dict):
                                component_has_data = False
                                for key, value in result.items():
                                    if value:
                                        final_config[key] = value
                                        config_count = len(value) if isinstance(value, list) else 1
                                        total_configurations += config_count
                                        component_has_data = True
                                        self.log(
                                            "Added {0} configuration(s) for component key '{1}'. "
                                            "Total configurations so far: {2}".format(
                                                config_count, key, total_configurations
                                            ),
                                            "DEBUG"
                                        )

                                if component_has_data:
                                    components_processed += 1
                                    self.log(
                                        "Successfully processed component {0}/{1}: {2} with data.".format(
                                            component_index, len(components_list), component
                                        ),
                                        "DEBUG"
                                    )
                                else:
                                    components_skipped += 1
                                    self.log(
                                        "Skipped component {0}/{1}: {2} - no data returned from "
                                        "getter function.".format(
                                            component_index, len(components_list), component
                                        ),
                                        "WARNING"
                                    )

                        except Exception as e:
                            self.log(
                                "Exception during component {0}/{1} ({2}) processing. Exception "
                                "type: {3}, Exception message: {4}. Skipping component and "
                                "continuing.".format(
                                    component_index, len(components_list), component,
                                    type(e).__name__, str(e)
                                ),
                                "ERROR"
                            )
                            components_skipped += 1
                            continue
                    else:
                        self.log(
                            "No getter function found for component {0}/{1}: {2}. Skipping "
                            "component processing.".format(
                                component_index, len(components_list), component
                            ),
                            "WARNING"
                        )
                        components_skipped += 1
                else:
                    self.log(
                        "Component {0}/{1}: {2} not found in module schema mapping. Skipping component processing.".format(
                            component_index, len(components_list), component
                        ),
                        "WARNING"
                    )
                    components_skipped += 1

            if final_config:
                self.log(
                    "Configuration retrieval completed successfully. Generated configurations "
                    "for {0} component(s) with {1} total configuration item(s). Proceeding "
                    "with playbook structure generation.".format(
                        len(final_config), total_configurations
                    ),
                    "INFO"
                )
                playbook_data = self.generate_playbook_structure(final_config, file_path)
                self.log(
                    "Playbook structure generated. Writing YAML data to file: {0}".format(
                        file_path
                    ),
                    "DEBUG"
                )

                if self.write_dict_to_yaml(playbook_data, file_path):
                    success_message = "YAML configuration file generated successfully for module '{0}'".format(self.module_name)

                    response_data = {
                        "components_processed": components_processed,
                        "components_skipped": components_skipped,
                        "configurations_count": total_configurations,
                        "file_path": file_path,
                        "message": success_message,
                        "status": "success"
                    }

                    self.set_operation_result("success", True, success_message, "INFO")

                    self.msg = response_data
                    self.result["response"] = response_data
                    self.log(
                        "YAML configuration file generated successfully for module '{0}'".format(self.module_name),
                        "INFO"
                    )

                else:
                    error_message = "Failed to write YAML configuration to file: {0}".format(file_path)

                    response_data = {
                        "message": error_message,
                        "status": "failed"
                    }

                    self.set_operation_result("failed", False, error_message, "ERROR")
                    self.msg = response_data
                    self.result["response"] = response_data
                    self.log(
                        "YAML file write operation failed for file path: {0}. Check file "
                        "permissions and disk space.".format(file_path),
                        "ERROR"
                    )

            else:
                no_config_message = "No configurations found to generate. Verify that the components exist and have data."

                response_data = {
                    "components_processed": components_processed,
                    "components_skipped": components_skipped,
                    "configurations_count": 0,
                    "message": no_config_message,
                    "status": "success"
                }

                self.set_operation_result("success", False, no_config_message, "INFO")

                self.msg = response_data
                self.result["response"] = response_data
                self.log(
                    "No configuration data retrieved. All {0} component(s) returned empty "
                    "results. Possible reasons: no configurations exist in Catalyst Center, "
                    "filters too restrictive, or API access issues.".format(
                        len(components_list)
                    ),
                    "WARNING"
                )

            return self

        except Exception as e:
            error_message = "Error during YAML config generation: {0}".format(str(e))

            response_data = {
                "message": error_message,
                "status": "failed"
            }

            self.msg = response_data
            self.result["response"] = response_data

            self.set_operation_result("failed", False, error_message, "ERROR")
            self.log(
                "Fatal exception during YAML generation workflow. Exception type: {0}, "
                "Exception message: {1}. Returning failure status.".format(
                    type(e).__name__, str(e)
                ),
                "ERROR"
            )

        return self

    def generate_playbook_structure(self, configurations, file_path):
        """
        Generates structured playbook format from configuration data.

        Description:
            This method transforms retrieved configuration data into a properly
            structured playbook format compatible with the events_and_notifications_workflow_manager
            module. It organizes all configuration types (destinations, settings, notifications)
            into a unified structure suitable for Ansible execution.

        Args:
            configurations (dict): Dictionary containing all retrieved configuration
                data organized by component type.
            file_path (str): The target file path for the generated playbook.

        Returns:
            dict: A structured dictionary containing the complete playbook configuration
            with all components organized in the proper format for YAML serialization.
        """
        self.log(
            "Starting playbook structure generation for file path: {0}. Processing {1} "
            "configuration type(s) into unified playbook format.".format(
                file_path, len(configurations)
            ),
            "DEBUG"
        )

        config_list = []

        # Add ALL webhook destinations to the same config block
        if configurations.get("webhook_destinations"):
            webhooks = configurations["webhook_destinations"]
            for webhook in webhooks:
                config_list.append(OrderedDict([
                    ("webhook_destination", webhook)
                ]))

        # Add ALL email destinations to the same config block
        if configurations.get("email_destinations"):
            emails = configurations["email_destinations"]
            for email in emails:
                config_list.append(OrderedDict([
                    ("email_destination", email)
                ]))

        # Add ALL syslog destinations to the same config block
        if configurations.get("syslog_destinations"):
            syslogs = configurations["syslog_destinations"]
            for syslog in syslogs:
                config_list.append(OrderedDict([
                    ("syslog_destination", syslog)
                ]))

        # Add ALL SNMP destinations to the same config block
        if configurations.get("snmp_destinations"):
            snmps = configurations["snmp_destinations"]
            for snmp in snmps:
                config_list.append(OrderedDict([
                    ("snmp_destination", snmp)
                ]))

        # Add ALL ITSM settings to the same config block
        if configurations.get("itsm_settings"):
            itsms = configurations["itsm_settings"]
            for itsm in itsms:
                config_list.append(OrderedDict([
                    ("itsm_setting", itsm)
                ]))

        # Add ALL webhook event notifications to the same config block
        if configurations.get("webhook_event_notifications"):
            webhook_notifs = configurations["webhook_event_notifications"]
            for webhook_notif in webhook_notifs:
                config_list.append(OrderedDict([
                    ("webhook_event_notification", webhook_notif)
                ]))

        # Add ALL email event notifications to the same config block
        if configurations.get("email_event_notifications"):
            email_notifs = configurations["email_event_notifications"]
            for email_notif in email_notifs:
                config_list.append(OrderedDict([
                    ("email_event_notification", email_notif)
                ]))

        # Add ALL syslog event notifications to the same config block
        if configurations.get("syslog_event_notifications"):
            syslog_notifs = configurations["syslog_event_notifications"]
            for syslog_notif in syslog_notifs:
                config_list.append(OrderedDict([
                    ("syslog_event_notification", syslog_notif)
                ]))

        return {"config": config_list}

    def get_want(self, config, state):
        """
        Processes and validates configuration parameters for API operations.

        Description:
            This method transforms input configuration parameters into the internal
            'want' structure used throughout the module. It validates the state
            parameter and prepares configuration data for subsequent processing
            steps in the YAML generation workflow.

        Args:
            config (dict): The configuration data containing generation parameters
                and component filters.
            state (str): The desired state for the operation (should be 'gathered').

        Returns:
            object: Self instance with updated attributes including:
                - self.want (dict): Structured configuration ready for processing with
                yaml_config_generator key containing all generation parameters.
                - self.msg (str): Success message confirming parameter collection.
                - self.status (str): Operation status set to 'success'.
        """
        self.log(
            "Processing configuration parameters for YAML generation workflow. State: {0}, "
            "Configuration provided: {1}".format(state, bool(config)),
            "DEBUG"
        )

        want = {}
        want["yaml_config_generator"] = config
        self.log(
            "Structured 'want' configuration created with yaml_config_generator containing: "
            "file_path={0}, generate_all_configurations={1}, component_filters_present={2}".format(
                config.get("file_path", "not specified"),
                config.get("generate_all_configurations", False),
                bool(config.get("component_specific_filters"))
            ),
            "DEBUG"
        )

        self.want = want
        self.log(
            "Configuration parameters successfully organized into internal 'want' structure. "
            "Ready for YAML generation processing with {0} configuration key(s).".format(
                len(want)
            ),
            "INFO"
        )
        self.msg = "Successfully collected all parameters from the playbook for Events and Notifications operations."
        self.status = "success"
        return self

    def get_diff_gathered(self):
        """
        Executes the configuration gathering and YAML generation process.

        Description:
            This method implements the main execution logic for the 'gathered' state.
            It retrieves the YAML configuration generator from the 'want' structure
            and initiates the complete configuration generation process. This method
            serves as the primary entry point for processing gathered configurations.

        Returns:
            object: Self instance with updated operation results. Returns success
            status when YAML generation completes successfully, or failure status
            with error information when issues occur.
        """
        start_time = time.time()
        self.log(
            "Starting configuration gathering workflow for YAML playbook generation. Preparing "
            "to process workflow operations for Events and Notifications components.",
            "DEBUG"
        )
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
        self.log(
            "Workflow operations defined with {0} operation(s) for processing. Beginning "
            "iteration to check parameter availability and execute operations.".format(
                len(workflow_operations)
            ),
            "DEBUG"
        )

        for index, (param_key, operation_name, operation_func) in enumerate(
            workflow_operations, start=1
        ):
            self.log(
                "Processing workflow operation {0}/{1}: {2}. Checking if parameters exist "
                "for param_key '{3}' in want structure.".format(
                    index, len(workflow_operations), operation_name, param_key
                ),
                "DEBUG"
            )
            params = self.want.get(param_key)
            if params:
                self.log(
                    "Parameters found for {0} operation. Parameter structure contains: "
                    "file_path={1}, generate_all={2}, components={3}. Starting operation "
                    "execution.".format(
                        operation_name,
                        params.get("file_path", "not specified"),
                        params.get("generate_all_configurations", False),
                        len(params.get("component_specific_filters", {}).get(
                            "components_list", []
                        ))
                    ),
                    "INFO"
                )

                try:
                    operation_func(params)
                    operations_executed += 1
                    self.log(
                        "Successfully completed {0} operation {1}/{2}. Operation executed "
                        "without errors and configurations generated.".format(
                            operation_name, index, len(workflow_operations)
                        ),
                        "DEBUG"
                    )
                except Exception as e:
                    self.log(
                        "Exception occurred during {0} operation execution. Exception type: "
                        "{1}, Exception message: {2}. Setting operation result to failed and "
                        "checking return status.".format(
                            operation_name, type(e).__name__, str(e)
                        ),
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
                    "No parameters found for {0} operation in want structure. Skipping "
                    "operation {1}/{2} and continuing to next operation.".format(
                        operation_name, index, len(workflow_operations)
                    ),
                    "WARNING"
                )

        end_time = time.time()
        execution_duration = end_time - start_time

        self.log(
            "Completed configuration gathering workflow successfully. Execution statistics - "
            "Total duration: {0:.2f} seconds, Operations executed: {1}, Operations skipped: {2}. "
            "YAML playbook generation workflow finished.".format(
                execution_duration, operations_executed, operations_skipped
            ),
            "INFO"
        )

        return self


def main():
    """
    Main entry point for the Cisco Catalyst Center brownfield events and notifications playbook generator module.

    This function serves as the primary execution entry point for the Ansible module,
    orchestrating the complete workflow from parameter collection to YAML playbook
    generation for brownfield events and notifications configuration extraction.

    Purpose:
        Initializes and executes the brownfield events and notifications playbook generator
        workflow to extract existing destination configurations, ITSM settings, and event
        subscriptions from Cisco Catalyst Center and generate Ansible-compatible YAML playbook files.

    Workflow Steps:
        1. Define module argument specification with required parameters
        2. Initialize Ansible module with argument validation
        3. Create EventsNotificationsPlaybookGenerator instance
        4. Validate Catalyst Center version compatibility (>= 2.3.5.3)
        5. Validate and sanitize state parameter
        6. Execute input parameter validation
        7. Process each configuration item in the playbook
        8. Handle generate_all_configurations and default component logic
        9. Execute state-specific operations (gathered workflow)
        10. Return results via module.exit_json()

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
        - Minimum Catalyst Center version: 2.3.5.3
        - Introduced APIs for events and notifications retrieval:
            * Webhook Destinations (get_webhook_destination)
            * Email Destinations (get_email_destination)
            * Syslog Destinations (get_syslog_destination)
            * SNMP Destinations (get_snmp_destination)
            * ITSM Settings (get_all_itsm_integration_settings)
            * Event Subscriptions (get_rest_webhook_event_subscriptions, get_email_event_subscriptions, get_syslog_event_subscriptions)

    Supported States:
        - gathered: Extract existing events and notifications configurations and generate YAML playbook
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
            - msg (str/dict): Operation result message or structured response
            - response (dict): Detailed operation results with statistics
            - status (str): Operation status ("success")

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
        # ============================================
        # Catalyst Center Connection Parameters
        # ============================================
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
            "no_log": True  # Prevent password from appearing in logs
        },
        "dnac_verify": {
            "type": "bool",
            "default": True
        },

        # ============================================
        # API Configuration Parameters
        # ============================================
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

        # ============================================
        # Logging Configuration Parameters
        # ============================================
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

        # ============================================
        # Playbook Configuration Parameters
        # ============================================
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

    # Initialize the EventsNotificationsPlaybookGenerator object
    # This creates the main orchestrator for brownfield events and notifications extraction
    ccc_events_and_notifications_playbook_generator = EventsNotificationsPlaybookGenerator(module)

    # Log module initialization after object creation (now logging is available)
    ccc_events_and_notifications_playbook_generator.log(
        "Starting Ansible module execution for brownfield events and notifications playbook "
        "generator at timestamp {0}".format(initialization_timestamp),
        "INFO"
    )

    ccc_events_and_notifications_playbook_generator.log(
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
    # Version Compatibility Check
    # ============================================
    ccc_events_and_notifications_playbook_generator.log(
        "Validating Catalyst Center version compatibility - checking if version {0} "
        "meets minimum requirement of 2.3.5.3 for events and notifications APIs".format(
            ccc_events_and_notifications_playbook_generator.get_ccc_version()
        ),
        "INFO"
    )

    if (ccc_events_and_notifications_playbook_generator.compare_dnac_versions(
            ccc_events_and_notifications_playbook_generator.get_ccc_version(), "2.3.5.3") < 0):

        error_msg = (
            "The specified Catalyst Center version '{0}' does not support the YAML "
            "playbook generation for Events and Notifications Management Module. Supported "
            "versions start from '2.3.5.3' onwards. Version '2.3.5.3' introduces APIs for "
            "retrieving events and notifications settings including webhook destinations "
            "(get_webhook_destination), email destinations (get_email_destination), syslog "
            "destinations (get_syslog_destination), SNMP destinations (get_snmp_destination), "
            "ITSM integration settings (get_all_itsm_integration_settings), and event "
            "subscriptions from the Catalyst Center.".format(
                ccc_events_and_notifications_playbook_generator.get_ccc_version()
            )
        )

        ccc_events_and_notifications_playbook_generator.log(
            "Version compatibility check failed: {0}".format(error_msg),
            "ERROR"
        )

        ccc_events_and_notifications_playbook_generator.msg = error_msg
        ccc_events_and_notifications_playbook_generator.set_operation_result(
            "failed", False, ccc_events_and_notifications_playbook_generator.msg, "ERROR"
        ).check_return_status()

    ccc_events_and_notifications_playbook_generator.log(
        "Version compatibility check passed - Catalyst Center version {0} supports "
        "all required events and notifications APIs".format(
            ccc_events_and_notifications_playbook_generator.get_ccc_version()
        ),
        "INFO"
    )

    # ============================================
    # State Parameter Validation
    # ============================================
    state = ccc_events_and_notifications_playbook_generator.params.get("state")

    ccc_events_and_notifications_playbook_generator.log(
        "Validating requested state parameter: '{0}' against supported states: {1}".format(
            state, ccc_events_and_notifications_playbook_generator.supported_states
        ),
        "DEBUG"
    )

    if state not in ccc_events_and_notifications_playbook_generator.supported_states:
        error_msg = (
            "State '{0}' is invalid for this module. Supported states are: {1}. "
            "Please update your playbook to use one of the supported states.".format(
                state, ccc_events_and_notifications_playbook_generator.supported_states
            )
        )

        ccc_events_and_notifications_playbook_generator.log(
            "State validation failed: {0}".format(error_msg),
            "ERROR"
        )

        ccc_events_and_notifications_playbook_generator.status = "invalid"
        ccc_events_and_notifications_playbook_generator.msg = error_msg
        ccc_events_and_notifications_playbook_generator.check_return_status()

    ccc_events_and_notifications_playbook_generator.log(
        "State validation passed - using state '{0}' for events and notifications workflow execution".format(
            state
        ),
        "INFO"
    )

    # ============================================
    # Input Parameter Validation
    # ============================================
    ccc_events_and_notifications_playbook_generator.log(
        "Starting comprehensive input parameter validation for events and notifications playbook configuration",
        "INFO"
    )

    ccc_events_and_notifications_playbook_generator.validate_input().check_return_status()

    ccc_events_and_notifications_playbook_generator.log(
        "Input parameter validation completed successfully - all configuration "
        "parameters meet events and notifications module requirements",
        "INFO"
    )

    # ============================================
    # Configuration Processing and Default Handling
    # ============================================
    config_list = ccc_events_and_notifications_playbook_generator.validated_config

    ccc_events_and_notifications_playbook_generator.log(
        "Starting configuration processing and default handling - will process {0} configuration "
        "item(s) from playbook".format(len(config_list)),
        "INFO"
    )

    # Handle generate_all_configurations and set component defaults
    for config_index, config_item in enumerate(config_list, start=1):
        ccc_events_and_notifications_playbook_generator.log(
            "Processing configuration item {0}/{1} for generate_all_configurations and default component handling".format(
                config_index, len(config_list)
            ),
            "DEBUG"
        )

        if config_item.get("generate_all_configurations", False):
            ccc_events_and_notifications_playbook_generator.log(
                "Configuration item {0}: generate_all_configurations=True detected. Setting default "
                "components to include all events and notifications components".format(
                    config_index
                ),
                "INFO"
            )

            # Set default components when generate_all_configurations is True
            if not config_item.get("component_specific_filters"):
                config_item["component_specific_filters"] = {
                    "components_list": [
                        "webhook_destinations", "email_destinations", "syslog_destinations",
                        "snmp_destinations", "itsm_settings", "webhook_event_notifications",
                        "email_event_notifications", "syslog_event_notifications"
                    ]
                }
                ccc_events_and_notifications_playbook_generator.log(
                    "Configuration item {0}: Set default component_specific_filters for generate_all mode: {1}".format(
                        config_index, len(config_item["component_specific_filters"]["components_list"])
                    ),
                    "DEBUG"
                )
            else:
                ccc_events_and_notifications_playbook_generator.log(
                    "Configuration item {0}: component_specific_filters already provided in generate_all mode - "
                    "using existing filters: {1}".format(
                        config_index, config_item.get("component_specific_filters")
                    ),
                    "DEBUG"
                )

        elif config_item.get("component_specific_filters") is None:
            ccc_events_and_notifications_playbook_generator.log(
                "Configuration item {0}: No component_specific_filters provided in normal mode. "
                "Applying default configuration to retrieve all events and notifications components".format(
                    config_index
                ),
                "INFO"
            )

            # Existing fallback logic for when no filters are specified
            ccc_events_and_notifications_playbook_generator.msg = (
                "No valid configurations found in the provided parameters."
            )

            config_item["component_specific_filters"] = {
                "components_list": [
                    "webhook_destinations", "email_destinations", "syslog_destinations",
                    "snmp_destinations", "itsm_settings", "webhook_event_notifications",
                    "email_event_notifications", "syslog_event_notifications"
                ]
            }

            ccc_events_and_notifications_playbook_generator.log(
                "Configuration item {0}: Applied default component_specific_filters: {1} components".format(
                    config_index, len(config_item["component_specific_filters"]["components_list"])
                ),
                "DEBUG"
            )
        else:
            ccc_events_and_notifications_playbook_generator.log(
                "Configuration item {0}: component_specific_filters already provided in normal mode - "
                "using existing filters: {1}".format(
                    config_index, config_item.get("component_specific_filters")
                ),
                "DEBUG"
            )

    # Update validated config after default handling
    ccc_events_and_notifications_playbook_generator.validated_config = config_list

    ccc_events_and_notifications_playbook_generator.log(
        "Configuration preprocessing completed. Updated validated_config with default component "
        "handling. Final configuration count: {0}".format(len(config_list)),
        "INFO"
    )

    # ============================================
    # Configuration Processing Loop
    # ============================================
    final_config_list = ccc_events_and_notifications_playbook_generator.validated_config

    ccc_events_and_notifications_playbook_generator.log(
        "Starting configuration processing loop - will process {0} final configuration "
        "item(s) after default handling".format(len(final_config_list)),
        "INFO"
    )

    for config_index, config_item in enumerate(final_config_list, start=1):
        components_list = config_item.get("component_specific_filters", {}).get("components_list", "all")

        ccc_events_and_notifications_playbook_generator.log(
            "Processing configuration item {0}/{1} for state '{2}' with components: {3}".format(
                config_index, len(final_config_list), state,
                len(components_list) if isinstance(components_list, list) else components_list
            ),
            "INFO"
        )

        # Reset values for clean state between configurations
        ccc_events_and_notifications_playbook_generator.log(
            "Resetting module state variables for clean configuration processing",
            "DEBUG"
        )
        ccc_events_and_notifications_playbook_generator.reset_values()

        # Collect desired state (want) from configuration
        ccc_events_and_notifications_playbook_generator.log(
            "Collecting desired state parameters from configuration item {0} - "
            "building want dictionary for events and notifications operations".format(
                config_index
            ),
            "DEBUG"
        )
        ccc_events_and_notifications_playbook_generator.get_want(
            config_item, state
        ).check_return_status()

        # Execute state-specific operation (gathered workflow)
        ccc_events_and_notifications_playbook_generator.log(
            "Executing state-specific operation for '{0}' workflow on "
            "configuration item {1} - will retrieve destinations, ITSM settings, "
            "and event subscriptions from Catalyst Center".format(state, config_index),
            "INFO"
        )
        ccc_events_and_notifications_playbook_generator.get_diff_state_apply[state]().check_return_status()

        ccc_events_and_notifications_playbook_generator.log(
            "Successfully completed processing for configuration item {0}/{1} - "
            "events and notifications data extraction and YAML generation completed".format(
                config_index, len(final_config_list)
            ),
            "INFO"
        )

    # ============================================
    # Module Completion and Exit
    # ============================================
    module_end_time = time.time()
    module_duration = module_end_time - module_start_time

    completion_timestamp = time.strftime(
        "%Y-%m-%d %H:%M:%S",
        time.localtime(module_end_time)
    )

    ccc_events_and_notifications_playbook_generator.log(
        "Events and notifications playbook generator module execution completed successfully "
        "at timestamp {0}. Total execution time: {1:.2f} seconds. Processed {2} "
        "configuration item(s) with final status: {3}".format(
            completion_timestamp,
            module_duration,
            len(final_config_list),
            ccc_events_and_notifications_playbook_generator.status
        ),
        "INFO"
    )

    ccc_events_and_notifications_playbook_generator.log(
        "Final module result summary: changed={0}, msg_type={1}, response_available={2}".format(
            ccc_events_and_notifications_playbook_generator.result.get("changed", False),
            type(ccc_events_and_notifications_playbook_generator.result.get("msg")).__name__,
            "response" in ccc_events_and_notifications_playbook_generator.result
        ),
        "DEBUG"
    )

    # Exit module with results
    # This is a terminal operation - function does not return after this
    ccc_events_and_notifications_playbook_generator.log(
        "Exiting Ansible module with result containing events and notifications extraction results",
        "DEBUG"
    )

    module.exit_json(**ccc_events_and_notifications_playbook_generator.result)


if __name__ == "__main__":
    main()
