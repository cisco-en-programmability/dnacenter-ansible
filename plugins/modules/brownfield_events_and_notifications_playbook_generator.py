#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright (c) 2025, Cisco Systems
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
- Generates YAML configurations compatible with the `events_and_notifications_workflow_manager`
  module, reducing the effort required to manually create Ansible playbooks and
  enabling programmatic modifications.
- The YAML configurations generated represent the events and notifications configurations
  including destinations (webhook, email, syslog, SNMP), ITSM settings, and event subscriptions
  configured on the Cisco Catalyst Center.
- Supports extraction of webhook destinations, email destinations, syslog destinations,
  SNMP destinations, ITSM settings, and various event subscriptions.
version_added: 6.31.0
extends_documentation_fragment:
- cisco.dnac.workflow_manager_params
author:
- Priyadharshini B (@pbalaku2)
- Madhan Sankaranarayanan (@madhansansel)
options:
  state:
    description: The desired state of Cisco Catalyst Center after module execution.
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
        - Path where the YAML configuration file will be saved.
        - If not provided, the file will be saved in the current working directory with
          a default file name  "<module_name>_playbook_<YYYY-MM-DD_HH-MM-SS>.yml".
        - For example, "events_and_notifications_workflow_manager_playbook_2025-04-22_21-43-26.yml".
        type: str
      generate_all_configurations:
        description:
        - When set to True, automatically generates YAML configurations for all events and notifications.
        - This mode discovers all configured destinations and event subscriptions in Cisco Catalyst Center.
        - When enabled, component_specific_filters becomes optional and will use default values if not provided.
        - A default filename will be generated automatically if file_path is not specified.
        - This is useful for complete brownfield infrastructure discovery and documentation.
        type: bool
        default: false
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
            - Valid values are
              - Webhook Destinations "webhook_destinations"
              - Email Destinations "email_destinations"
              - Syslog Destinations "syslog_destinations"
              - SNMP Destinations "snmp_destinations"
              - ITSM Settings "itsm_settings"
              - Webhook Event Notifications "webhook_event_notifications"
              - Email Event Notifications "email_event_notifications"
              - Syslog Event Notifications "syslog_event_notifications"
            - If not specified, all components are included.
            - For example, ["webhook_destinations", "email_destinations", "webhook_event_notifications"].
            type: list
            elements: str
          destination_filters:
            description:
            - Destination configuration filters to filter destinations by name or type.
            type: dict
            suboptions:
              destination_names:
                description:
                - List of destination names to filter.
                type: list
                elements: str
              destination_types:
                description:
                - List of destination types to filter (webhook, email, syslog, snmp).
                type: list
                elements: str
          notification_filters:
            description:
            - Event notification filters to filter event subscriptions.
            type: dict
            suboptions:
              subscription_names:
                description:
                - List of event subscription names to filter.
                type: list
                elements: str
              notification_types:
                description:
                - List of notification types to filter (webhook, email, syslog).
                type: list
                elements: str
          itsm_filters:
            description:
            - ITSM integration filters to filter ITSM settings.
            type: dict
            suboptions:
              instance_names:
                description:
                - List of ITSM instance names to filter.
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
- Paths used are
    - GET /dna/system/api/v1/event/webhook
    - GET /dna/system/api/v1/event/email-config
    - GET /dna/system/api/v1/event/syslog-config
    - GET /dna/system/api/v1/event/snmp-config
    - GET /dna/system/api/v1/event/itsm-integration-setting
    - GET /dna/system/api/v1/event/subscription/rest
    - GET /dna/system/api/v1/event/subscription/email
    - GET /dna/system/api/v1/event/subscription/syslog
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
      "msg": "YAML config generation Task succeeded for module 'events_and_notifications_workflow_manager'.",
      "response": "YAML config generation Task succeeded for module 'events_and_notifications_workflow_manager'.",
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
      "response": "No configurations found to generate. Verify that the components exist and have data.",
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

    def validate_input(self):
        """
        Validates the input configuration parameters for the events and notifications playbook.

        Description:
            Performs comprehensive validation of input configuration parameters to ensure
            they conform to the expected schema for events and notifications workflow generation.
            Validates parameter types, requirements, and structure for destination and
            notification configuration generation.

        Args:
            None: Uses self.config from the instance.

        Returns:
            object: Self instance with updated attributes:
                - self.msg (str): Message describing the validation result.
                - self.status (str): Status of validation ("success" or "failed").
                - self.validated_config (list): Validated configuration parameters if successful.
        """
        self.log("Starting validation of input configuration parameters.", "DEBUG")

        # Check if configuration is available
        if not self.config:
            self.status = "success"
            self.msg = "Configuration is not available in the playbook for validation"
            self.log(self.msg, "INFO")
            return self

        # Expected schema for configuration parameters
        temp_spec = {
            "file_path": {"type": "str", "required": False},
            "generate_all_configurations": {"type": "bool", "required": False, "default": False},
            "component_specific_filters": {"type": "dict", "required": False},
            "global_filters": {"type": "dict", "required": False},
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
                - network_elements (dict): Component configurations with API details,
                filter specifications, and processing function references.
                - global_filters (dict): Global filter configuration options.
        """
        self.log("Starting mapping for events and notifications.", "DEBUG")
        return {
            "network_elements": {
                "webhook_destinations": {
                    "filters": {
                        "destination_names": {"type": "list", "elements": "str", "required": False},
                        "destination_types": {"type": "list", "elements": "str", "required": False, "choices": ["webhook"]},
                    },
                    "reverse_mapping_function": self.webhook_destinations_reverse_mapping_function,
                    "api_function": "get_webhook_destination",
                    "api_family": "event_management",
                    "get_function_name": self.get_webhook_destinations,
                },
                "email_destinations": {
                    "filters": {
                        "destination_names": {"type": "list", "elements": "str", "required": False},
                        "destination_types": {"type": "list", "elements": "str", "required": False, "choices": ["email"]},
                    },
                    "reverse_mapping_function": self.email_destinations_reverse_mapping_function,
                    "api_function": "get_email_destination",
                    "api_family": "event_management",
                    "get_function_name": self.get_email_destinations,
                },
                "syslog_destinations": {
                    "filters": {
                        "destination_names": {"type": "list", "elements": "str", "required": False},
                        "destination_types": {"type": "list", "elements": "str", "required": False, "choices": ["syslog"]},
                    },
                    "reverse_mapping_function": self.syslog_destinations_reverse_mapping_function,
                    "api_function": "get_syslog_destination",
                    "api_family": "event_management",
                    "get_function_name": self.get_syslog_destinations,
                },
                "snmp_destinations": {
                    "filters": {
                        "destination_names": {"type": "list", "elements": "str", "required": False},
                        "destination_types": {"type": "list", "elements": "str", "required": False, "choices": ["snmp"]},
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
                        "notification_types": {"type": "list", "elements": "str", "required": False, "choices": ["webhook"]},
                    },
                    "reverse_mapping_function": self.webhook_event_notifications_reverse_mapping_function,
                    "api_function": "get_rest_webhook_event_subscriptions",
                    "api_family": "event_management",
                    "get_function_name": self.get_webhook_event_notifications,
                },
                "email_event_notifications": {
                    "filters": {
                        "subscription_names": {"type": "list", "elements": "str", "required": False},
                        "notification_types": {"type": "list", "elements": "str", "required": False, "choices": ["email"]},
                    },
                    "reverse_mapping_function": self.email_event_notifications_reverse_mapping_function,
                    "api_function": "get_email_event_subscriptions",
                    "api_family": "event_management",
                    "get_function_name": self.get_email_event_notifications,
                },
                "syslog_event_notifications": {
                    "filters": {
                        "subscription_names": {"type": "list", "elements": "str", "required": False},
                        "notification_types": {"type": "list", "elements": "str", "required": False, "choices": ["syslog"]},
                    },
                    "reverse_mapping_function": self.syslog_event_notifications_reverse_mapping_function,
                    "api_function": "get_syslog_event_subscriptions",
                    "api_family": "event_management",
                    "get_function_name": self.get_syslog_event_notifications,
                },
            },
            "global_filters": {},
        }

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
            str or None: Returns "***REDACTED***" if password exists, otherwise None.
            This ensures sensitive data is not exposed in configuration files.
        """
        return "***REDACTED***" if password else None

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
            return []

        filter_obj = notification.get("filter", {})
        event_ids = filter_obj.get("eventIds", [])

        if not event_ids:
            return []

        event_names = []
        for event_id in event_ids:
            try:
                event_name = self.get_event_name_from_api(event_id)
                if event_name:
                    event_names.append(event_name)
                else:
                    event_names.append(event_id)
            except Exception as e:
                self.log("Error resolving event ID {0}: {1}".format(event_id, str(e)), "ERROR")
                event_names.append(event_id)

        self.log("Resolved event names: {0}".format(event_names), "DEBUG")

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
            str: The resolved event name if found, otherwise returns the original
            event ID as a fallback. Returns None if the event_id parameter is invalid.
        """
        self.log("Resolving event ID {0} to event name using Event Artifacts API.".format(event_id), "DEBUG")
        if not event_id:
            return None

        try:
            response = self.dnac._exec(
                family="event_management",
                function="get_event_artifacts",
                op_modifies=False,
                params={"event_ids": event_id}
            )
            self.log("Received API response for get_event_artifacts {0}".format(response), "DEBUG")

            self.log("Event Artifacts API response for {0}: {1}".format(event_id, response), "DEBUG")

            if isinstance(response, list) and len(response) > 0:
                event_info = response[0]
                event_name = event_info.get("name")
                if event_name:
                    self.log("Successfully resolved event ID {0} to name: {1}".format(event_id, event_name), "INFO")
                    return event_name

            elif isinstance(response, dict):
                events = response.get("response") or response.get("events") or []
                if events and len(events) > 0:
                    event_info = events[0] if isinstance(events, list) else events
                    event_name = event_info.get("name")
                    if event_name:
                        self.log("Successfully resolved event ID {0} to name: {1}".format(event_id, event_name), "INFO")
                        return event_name

            self.log("No event name found in API response for {0}, returning event ID".format(event_id), "WARNING")
            return event_id

        except Exception as e:
            self.log("Error calling event artifacts API for event ID {0}: {1}".format(event_id, str(e)), "ERROR")
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
            list: A list of site names extracted from the notification data. Returns an
            empty list if no sites are found or if an error occurs during extraction.
        """
        self.log("Extracting site names from notification filter and resource domain.", "DEBUG")

        if not notification or not isinstance(notification, dict):
            return []

        sites = []

        try:
            # Check filter for direct sites
            filter_data = notification.get("filter", {})
            if isinstance(filter_data, dict):
                # Direct site names in filter
                direct_sites = filter_data.get("sites", [])
                if direct_sites:
                    sites.extend(direct_sites)

                # Site IDs in filter - need to resolve to names
                site_ids = filter_data.get("siteIds", [])
                if site_ids:
                    for site_id in site_ids:
                        site_name = self.get_site_name_by_id(site_id)
                        if site_name:
                            sites.append(site_name)
                        else:
                            # If can't resolve, use the ID as fallback
                            sites.append(site_id)

            # Check resourceDomain for site information
            resource_domain = notification.get("resourceDomain", {})
            if resource_domain:
                resource_groups = resource_domain.get("resourceGroups", [])
                for group in resource_groups:
                    if group.get("type") == "site":
                        site_name = group.get("name")
                        if site_name and site_name not in sites:
                            sites.append(site_name)

                        # Also check for srcResourceId if it's not "*"
                        src_resource_id = group.get("srcResourceId")
                        if src_resource_id and src_resource_id != "*":
                            resolved_site = self.get_site_name_by_id(src_resource_id)
                            if resolved_site and resolved_site not in sites:
                                sites.append(resolved_site)

            # Remove duplicates while preserving order
            unique_sites = []
            for site in sites:
                if site not in unique_sites:
                    unique_sites.append(site)
            self.log("Extracted sites: {0}".format(unique_sites), "DEBUG")

            return unique_sites

        except Exception as e:
            self.log("Error extracting sites from notification: {0}".format(str(e)))
            self.set_operation_result("failed", True, self.msg, "ERROR")

    def get_site_name_by_id(self, site_id):
        """
        Resolves site ID to site name using Cisco Catalyst Center Sites API.

        Description:
            This method queries the Cisco Catalyst Center Sites API to resolve a site UUID
            to its hierarchical site name (e.g., "Global/Area/Building/Floor"). It handles
            API errors gracefully and provides fallback behavior.

        Args:
            site_id (str): The UUID of the site to resolve to a name.

        Returns:
            str or None: The hierarchical site name if found, otherwise None.
            Returns None if the API call fails or the site is not found.
        """
        self.log("Resolving site ID {0} to site name using Sites API.".format(site_id), "DEBUG")

        if not site_id or site_id == "*":
            return None

        try:
            response = self.dnac._exec(
                family="sites",
                function="get_site",
                op_modifies=False,
                params={"site_id": site_id}
            )

            self.log("Received API response for ID {0}: {1}".format(site_id, response), "DEBUG")

            if isinstance(response, dict):
                site_info = response.get("response")
                if site_info:
                    # Extract site hierarchy
                    site_name_hierarchy = site_info.get("siteNameHierarchy")
                    if site_name_hierarchy:
                        self.log("Successfully resolved site ID {0} to name: {1}".format(site_id, site_name_hierarchy), "INFO")
                        return site_name_hierarchy

                    # Fallback to additionalInfo if available
                    additional_info = site_info.get("additionalInfo")
                    if additional_info and len(additional_info) > 0:
                        namespace = additional_info[0].get("nameSpace")
                        if namespace == "Location":
                            attributes = additional_info[0].get("attributes", {})
                            site_hierarchy = attributes.get("name")
                            if site_hierarchy:
                                return site_hierarchy

            self.log("Could not resolve site ID {0} to name".format(site_id), "WARNING")
            return None

        except Exception as e:
            self.log("Error resolving site ID {0}: {1}".format(site_id, str(e)), "ERROR")
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
        self.log("Extracting webhook destination name from notification.", "DEBUG")

        if not notification:
            return None

        subscription_endpoints = notification.get("subscriptionEndpoints", [])
        for endpoint in subscription_endpoints:
            subscription_details = endpoint.get("subscriptionDetails", {})
            if subscription_details.get("connectorType") == "REST":
                self.log("Found webhook destination: {0}".format(subscription_details.get("name")), "DEBUG")
                return subscription_details.get("name")
        return None

    def extract_syslog_destination_name(self, notification):
        """
        Extracts syslog destination name from notification subscription endpoints.

        Description:
            This method searches through subscription endpoints in a notification to find
            syslog connector types and extracts the destination name. It processes the
            subscription details to identify syslog-specific configurations.

        Args:
            notification (dict): Notification dictionary containing subscription endpoints
                with connector details.

        Returns:
            str or None: The syslog destination name if found, otherwise None.
            Returns None if the notification is invalid or no syslog destination is found.
        """
        self.log("Extracting syslog destination name from notification.", "DEBUG")

        if not notification:
            return None

        subscription_endpoints = notification.get("subscriptionEndpoints", [])
        for endpoint in subscription_endpoints:
            subscription_details = endpoint.get("subscriptionDetails", {})
            if subscription_details.get("connectorType") == "SYSLOG":
                self.log("Found syslog destination: {0}".format(subscription_details.get("name")), "DEBUG")
                return subscription_details.get("name")
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
        self.log("Extracting sender email from notification.", "DEBUG")
        if not notification:
            return None

        subscription_endpoints = notification.get("subscriptionEndpoints", [])
        for endpoint in subscription_endpoints:
            subscription_details = endpoint.get("subscriptionDetails", {})
            if subscription_details.get("connectorType") == "EMAIL":
                self.log("Found sender email: {0}".format(subscription_details.get("fromEmailAddress")), "DEBUG")
                return subscription_details.get("fromEmailAddress")
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
        self.log("Extracting recipient emails from notification.", "DEBUG")
        if not notification:
            return []

        subscription_endpoints = notification.get("subscriptionEndpoints", [])
        for endpoint in subscription_endpoints:
            subscription_details = endpoint.get("subscriptionDetails", {})
            if subscription_details.get("connectorType") == "EMAIL":
                self.log("Found recipient emails: {0}".format(subscription_details.get("toEmailAddresses", [])), "DEBUG")
                return subscription_details.get("toEmailAddresses", [])
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
        self.log("Extracting subject from notification.", "DEBUG")
        if not notification:
            return None

        subscription_endpoints = notification.get("subscriptionEndpoints", [])
        for endpoint in subscription_endpoints:
            subscription_details = endpoint.get("subscriptionDetails", {})
            if subscription_details.get("connectorType") == "EMAIL":
                self.log("Found email subject: {0}".format(subscription_details.get("subject")), "DEBUG")
                return subscription_details.get("subject")
        return None

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
            str or None: Returns "***REDACTED***" if password exists, otherwise None.
            This ensures sensitive data is not exposed in configuration files.
        """
        return "***REDACTED***" if password else None

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
        self.log("Creating instance name from notification.", "DEBUG")
        if not notification or not isinstance(notification, dict):
            return None

        subscription_endpoints = notification.get("subscriptionEndpoints", [])
        for endpoint in subscription_endpoints:
            subscription_details = endpoint.get("subscriptionDetails", {})
            if subscription_details.get("connectorType") == "EMAIL":
                self.log("Found email instance name: {0}".format(subscription_details.get("name")), "DEBUG")
                return subscription_details.get("name")

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
        self.log("Creating instance description from notification.", "DEBUG")
        if not notification or not isinstance(notification, dict):
            return None

        subscription_endpoints = notification.get("subscriptionEndpoints", [])
        for endpoint in subscription_endpoints:
            subscription_details = endpoint.get("subscriptionDetails", {})
            if subscription_details.get("connectorType") == "EMAIL":
                self.log("Found email instance description: {0}".format(subscription_details.get("description")), "DEBUG")
                return subscription_details.get("description")

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
        self.log("Starting to retrieve webhook destinations", "DEBUG")

        component_specific_filters = filters.get("component_specific_filters", {})
        destination_filters = component_specific_filters.get("destination_filters", {})
        destination_names = destination_filters.get("destination_names", [])

        api_family = network_element.get("api_family")
        api_function = network_element.get("api_function")

        try:
            webhook_configs = self.get_all_webhook_destinations(api_family, api_function)

            if destination_names:
                matching_configs = [config for config in webhook_configs if config.get("name") in destination_names]
                if matching_configs:
                    self.log("Found matching webhook destinations for filter: {0}".format(destination_names), "DEBUG")
                    final_webhook_configs = matching_configs
                else:
                    self.log("No matching webhook destinations found for filter - including all", "DEBUG")
                    final_webhook_configs = webhook_configs
            else:
                final_webhook_configs = webhook_configs

        except Exception as e:
            self.log("Failed to retrieve webhook destinations: {0}".format(str(e)), "ERROR")
            final_webhook_configs = []

        webhook_destinations_temp_spec = self.webhook_destinations_temp_spec()
        modified_webhook_configs = self.modify_parameters(webhook_destinations_temp_spec, final_webhook_configs)

        result = {"webhook_destinations": modified_webhook_configs}
        self.log("Final webhook destinations result: {0} configs transformed".format(len(modified_webhook_configs)), "INFO")
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
        self.log("Starting to retrieve email destinations", "DEBUG")

        component_specific_filters = filters.get("component_specific_filters", {})
        destination_filters = component_specific_filters.get("destination_filters", {})
        destination_names = destination_filters.get("destination_names", [])

        api_family = network_element.get("api_family")
        api_function = network_element.get("api_function")

        try:
            email_configs = self.get_all_email_destinations(api_family, api_function)

            if destination_names:
                matching_configs = [config for config in email_configs if config.get("name") in destination_names]
                if matching_configs:
                    self.log("Found matching email destinations for filter: {0}".format(destination_names), "DEBUG")
                    final_email_configs = matching_configs
                else:
                    self.log("No matching email destinations found for filter - including all", "DEBUG")
                    final_email_configs = email_configs
            else:
                final_email_configs = email_configs

        except Exception as e:
            self.log("Failed to retrieve email destinations: {0}".format(str(e)), "ERROR")
            final_email_configs = []

        email_destinations_temp_spec = self.email_destinations_temp_spec()
        modified_email_configs = self.modify_parameters(email_destinations_temp_spec, final_email_configs)

        result = {"email_destinations": modified_email_configs}
        self.log("Final email destinations result: {0} configs transformed".format(len(modified_email_configs)), "INFO")
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
        self.log("Starting to retrieve syslog destinations", "DEBUG")

        component_specific_filters = filters.get("component_specific_filters", {})
        destination_filters = component_specific_filters.get("destination_filters", {})
        destination_names = destination_filters.get("destination_names", [])

        api_family = network_element.get("api_family")
        api_function = network_element.get("api_function")

        try:
            syslog_configs = self.get_all_syslog_destinations(api_family, api_function)

            if destination_names:
                matching_configs = [config for config in syslog_configs if config.get("name") in destination_names]
                if matching_configs:
                    self.log("Found matching syslog destinations for filter: {0}".format(destination_names), "DEBUG")
                    final_syslog_configs = matching_configs
                else:
                    self.log("No matching syslog destinations found for filter - including all", "DEBUG")
                    final_syslog_configs = syslog_configs
            else:
                final_syslog_configs = syslog_configs

        except Exception as e:
            self.log("Failed to retrieve syslog destinations: {0}".format(str(e)), "ERROR")
            final_syslog_configs = []

        syslog_destinations_temp_spec = self.syslog_destinations_temp_spec()
        modified_syslog_configs = self.modify_parameters(syslog_destinations_temp_spec, final_syslog_configs)

        result = {"syslog_destinations": modified_syslog_configs}
        self.log("Final syslog destinations result: {0} configs transformed".format(len(modified_syslog_configs)), "INFO")
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
        self.log("Starting to retrieve SNMP destinations", "DEBUG")

        component_specific_filters = filters.get("component_specific_filters", {})
        destination_filters = component_specific_filters.get("destination_filters", {})
        destination_names = destination_filters.get("destination_names", [])

        api_family = network_element.get("api_family")
        api_function = network_element.get("api_function")

        try:
            snmp_configs = self.get_all_snmp_destinations(api_family, api_function)

            if destination_names:
                matching_configs = [config for config in snmp_configs if config.get("name") in destination_names]
                if matching_configs:
                    self.log("Found matching SNMP destinations for filter: {0}".format(destination_names), "DEBUG")
                    final_snmp_configs = matching_configs
                else:
                    self.log("No matching SNMP destinations found for filter - including all", "DEBUG")
                    final_snmp_configs = snmp_configs
            else:
                final_snmp_configs = snmp_configs

        except Exception as e:
            self.log("Failed to retrieve SNMP destinations: {0}".format(str(e)), "ERROR")
            final_snmp_configs = []

        snmp_destinations_temp_spec = self.snmp_destinations_temp_spec()
        modified_snmp_configs = self.modify_parameters(snmp_destinations_temp_spec, final_snmp_configs)

        result = {"snmp_destinations": modified_snmp_configs}
        self.log("Final SNMP destinations result: {0} configs transformed".format(len(modified_snmp_configs)), "INFO")
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
        self.log("Retrieving all webhook destinations with pagination.", "DEBUG")
        try:
            offset = 0
            limit = 10
            all_webhooks = []

            while True:
                response = self.dnac._exec(
                    family=api_family,
                    function=api_function,
                    op_modifies=False,
                    params={"offset": offset * limit, "limit": limit},
                )
                self.log("Received API response for webhook destinations: {0}".format(response), "DEBUG")

                webhooks = response.get("statusMessage", [])
                if not webhooks:
                    break

                all_webhooks.extend(webhooks)

                if len(webhooks) < limit:
                    break

                offset += 1
            self.log("Total webhook destinations retrieved: {0}".format(len(all_webhooks)), "INFO")

            return all_webhooks

        except Exception as e:
            self.log("Error retrieving webhook destinations: {0}".format(str(e)), "ERROR")

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
        self.log("Retrieving all email destinations.", "DEBUG")
        try:
            response = self.dnac._exec(
                family=api_family,
                function=api_function,
                op_modifies=False,
            )
            self.log("Received API response for email destinations: {0}".format(response), "DEBUG")

            if isinstance(response, list):
                return response
            elif isinstance(response, dict):
                return response.get("response", [])
            else:
                return []

        except Exception as e:
            self.log("Error retrieving email destinations: {0}".format(str(e)), "ERROR")
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
        self.log("Retrieving all syslog destinations.", "DEBUG")
        try:
            response = self.dnac._exec(
                family=api_family,
                function=api_function,
                op_modifies=False,
                params={},
            )
            self.log("Received API response for syslog destinations: {0}".format(response), "DEBUG")

            syslog_configs = response.get("statusMessage", [])
            return syslog_configs if isinstance(syslog_configs, list) else []

        except Exception as e:
            self.log("Error retrieving syslog destinations: {0}".format(str(e)), "ERROR")
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
        self.log("Retrieving all SNMP destinations with pagination.", "DEBUG")
        try:
            offset = 0
            limit = 10
            all_snmp = []

            while True:
                try:
                    response = self.dnac._exec(
                        family=api_family,
                        function=api_function,
                        op_modifies=False,
                        params={"offset": offset * limit, "limit": limit},
                    )
                    self.log("Received API response for SNMP destinations: {0}".format(response), "DEBUG")

                    snmp_configs = response if isinstance(response, list) else []
                    if not snmp_configs:
                        break

                    all_snmp.extend(snmp_configs)

                    if len(snmp_configs) < limit:
                        break

                    offset += 1

                except Exception as e:
                    self.log("Error in pagination for SNMP destinations: {0}".format(str(e)), "ERROR")
                    break

            return all_snmp

        except Exception as e:
            self.log("Error retrieving SNMP destinations: {0}".format(str(e)), "ERROR")
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
        self.log("Starting to retrieve ITSM settings", "DEBUG")

        component_specific_filters = filters.get("component_specific_filters", {})
        itsm_filters = component_specific_filters.get("itsm_filters", {})
        instance_names = itsm_filters.get("instance_names", [])

        api_family = network_element.get("api_family")
        api_function = network_element.get("api_function")

        try:
            itsm_configs = self.get_all_itsm_settings(api_family, api_function)

            if instance_names:
                self.log("Applying instance name filters: {0}".format(instance_names), "DEBUG")
                final_itsm_configs = [config for config in itsm_configs if config.get("name") in instance_names]
            else:
                final_itsm_configs = itsm_configs

        except Exception as e:
            self.log("Failed to retrieve ITSM settings: {0}".format(str(e)), "ERROR")
            final_itsm_configs = []

        itsm_settings_temp_spec = self.itsm_settings_temp_spec()
        modified_itsm_configs = self.modify_parameters(itsm_settings_temp_spec, final_itsm_configs)

        result = {"itsm_settings": modified_itsm_configs}
        self.log("Final ITSM settings result: {0} configs transformed".format(len(modified_itsm_configs)), "INFO")
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
        self.log("Retrieving all ITSM settings.", "DEBUG")
        try:
            response = self.dnac._exec(
                family=api_family,
                function=api_function,
                op_modifies=False,
            )
            self.log("Received API response for ITSM settings: {0}".format(response), "DEBUG")

            if isinstance(response, dict):
                itsm_settings = response.get("response", [])
                return itsm_settings if isinstance(itsm_settings, list) else []
            elif isinstance(response, list):
                return response
            else:
                return []

        except Exception as e:
            self.log("Error retrieving ITSM settings: {0}".format(str(e)))
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
        self.log("Starting to retrieve webhook event notifications", "DEBUG")

        component_specific_filters = filters.get("component_specific_filters", {})
        notification_filters = component_specific_filters.get("notification_filters", {})
        subscription_names = notification_filters.get("subscription_names", [])

        api_family = network_element.get("api_family")
        api_function = network_element.get("api_function")

        try:
            notification_configs = self.get_all_webhook_event_notifications(api_family, api_function)

            if subscription_names:
                self.log("Applying subscription name filters: {0}".format(subscription_names), "DEBUG")
                final_notification_configs = [config for config in notification_configs if config.get("name") in subscription_names]
            else:
                final_notification_configs = notification_configs

        except Exception as e:
            self.log("Failed to retrieve webhook event notifications: {0}".format(str(e)), "ERROR")
            final_notification_configs = []

        webhook_event_notifications_temp_spec = self.webhook_event_notifications_temp_spec()
        modified_notification_configs = self.modify_parameters(webhook_event_notifications_temp_spec, final_notification_configs)

        result = {"webhook_event_notifications": modified_notification_configs}
        self.log("Final webhook event notifications result: {0} configs transformed".format(len(modified_notification_configs)), "INFO")
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
        self.log("Retrieving all webhook event notifications with pagination.", "DEBUG")
        try:
            offset = 0
            limit = 10
            all_notifications = []

            while True:
                try:
                    response = self.dnac._exec(
                        family=api_family,
                        function=api_function,
                        op_modifies=False,
                        params={"offset": offset, "limit": limit},
                    )
                    self.log("Received API response for webhook event notifications: {0}".format(response), "DEBUG")

                    if isinstance(response, list):
                        notifications = response
                    elif isinstance(response, dict):
                        notifications = response.get("response", [])
                    else:
                        notifications = []

                    if not notifications:
                        break

                    all_notifications.extend(notifications)

                    if len(notifications) < limit:
                        break

                    offset += limit

                except Exception as e:
                    self.log("Error in pagination for webhook event notifications: {0}".format(str(e)), "ERROR")
                    self.set_operation_result("failed", True, self.msg, "ERROR")

            self.log("Total webhook event notifications retrieved: {0}".format(len(all_notifications)), "INFO")
            return all_notifications

        except Exception as e:
            self.log("Error retrieving webhook event notifications: {0}".format(str(e)), "ERROR")
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
        self.log("Starting to retrieve email event notifications", "DEBUG")

        component_specific_filters = filters.get("component_specific_filters", {})
        notification_filters = component_specific_filters.get("notification_filters", {})
        subscription_names = notification_filters.get("subscription_names", [])

        api_family = network_element.get("api_family")
        api_function = network_element.get("api_function")

        try:
            notification_configs = self.get_all_email_event_notifications(api_family, api_function)

            if subscription_names:
                self.log("Applying subscription name filters: {0}".format(subscription_names), "DEBUG")
                final_notification_configs = [config for config in notification_configs if config.get("name") in subscription_names]
            else:
                final_notification_configs = notification_configs

        except Exception as e:
            self.log("Failed to retrieve email event notifications: {0}".format(str(e)), "ERROR")
            final_notification_configs = []

        email_event_notifications_temp_spec = self.email_event_notifications_temp_spec()
        modified_notification_configs = self.modify_parameters(email_event_notifications_temp_spec, final_notification_configs)

        result = {"email_event_notifications": modified_notification_configs}
        self.log("Final email event notifications result: {0} configs transformed".format(len(modified_notification_configs)), "INFO")
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
        try:
            response = self.dnac._exec(
                family=api_family,
                function=api_function,
                op_modifies=False,
                params={}
            )
            self.log("Received API response for email event notifications: {0}".format(response), "DEBUG")

            if isinstance(response, list):
                notifications = response
            elif isinstance(response, dict):
                notifications = response.get("response", [])
            else:
                notifications = []

            return notifications

        except Exception as e:
            self.log("Error retrieving email event notifications: {0}".format(str(e)), "ERROR")
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
        self.log("Starting to retrieve syslog event notifications", "DEBUG")

        component_specific_filters = filters.get("component_specific_filters", {})
        notification_filters = component_specific_filters.get("notification_filters", {})
        subscription_names = notification_filters.get("subscription_names", [])

        api_family = network_element.get("api_family")
        api_function = network_element.get("api_function")

        try:
            notification_configs = self.get_all_syslog_event_notifications(api_family, api_function)

            if subscription_names:
                self.log("Applying subscription name filters: {0}".format(subscription_names), "DEBUG")
                final_notification_configs = [config for config in notification_configs if config.get("name") in subscription_names]
            else:
                final_notification_configs = notification_configs

        except Exception as e:
            self.log("Failed to retrieve syslog event notifications: {0}".format(str(e)), "ERROR")
            final_notification_configs = []

        syslog_event_notifications_temp_spec = self.syslog_event_notifications_temp_spec()
        modified_notification_configs = self.modify_parameters(syslog_event_notifications_temp_spec, final_notification_configs)

        result = {"syslog_event_notifications": modified_notification_configs}
        self.log("Final syslog event notifications result: {0} configs transformed".format(len(modified_notification_configs)), "INFO")
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
        self.log("Retrieving all syslog event notifications with pagination.", "DEBUG")
        try:
            offset = 0
            limit = 10
            all_notifications = []

            while True:
                try:
                    response = self.dnac._exec(
                        family=api_family,
                        function=api_function,
                        op_modifies=False,
                        params={"offset": offset, "limit": limit},
                    )
                    self.log("Received API response for syslog event notifications: {0}".format(response), "DEBUG")

                    if isinstance(response, list):
                        notifications = response
                    elif isinstance(response, dict):
                        notifications = response.get("response", [])
                    else:
                        notifications = []

                    if not notifications:
                        break

                    all_notifications.extend(notifications)

                    if len(notifications) < limit:
                        break

                    offset += limit

                except Exception as e:
                    self.log("Error in pagination for syslog event notifications: {0}".format(str(e)), "ERROR")
                    break

            self.log("Total syslog event notifications retrieved: {0}".format(len(all_notifications)), "INFO")

            return all_notifications

        except Exception as e:
            self.log("Error retrieving syslog event notifications: {0}".format(str(e)), "ERROR")
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
        self.log("Details list: {0}".format(details_list), "DEBUG")
        self.log("Starting modification of parameters based on temp_spec.", "INFO")

        if not details_list:
            self.log("No details to process", "DEBUG")
            return []

        modified_configs = []

        for detail in details_list:
            if not isinstance(detail, dict):
                continue

            mapped_config = OrderedDict()

            for key, spec_def in temp_spec.items():
                source_key = spec_def.get("source_key", key)
                value = detail.get(source_key)

                if spec_def.get("options") and isinstance(value, list):
                    nested_list = []
                    for item in value:
                        if isinstance(item, dict):
                            nested_mapped = OrderedDict()
                            for nested_key, nested_spec in spec_def["options"].items():
                                nested_source_key = nested_spec.get("source_key", nested_key)
                                nested_value = item.get(nested_source_key)

                                transform = nested_spec.get("transform")
                                if transform and callable(transform):
                                    nested_value = transform(nested_value)

                                if nested_value is not None:
                                    nested_mapped[nested_key] = nested_value

                            if nested_mapped:
                                nested_list.append(nested_mapped)

                    if nested_list:
                        mapped_config[key] = nested_list

                elif spec_def.get("options") and isinstance(value, dict):
                    nested_mapped = OrderedDict()
                    has_non_null_values = False

                    for nested_key, nested_spec in spec_def["options"].items():
                        nested_source_key = nested_spec.get("source_key", nested_key)
                        nested_value = value.get(nested_source_key)

                        transform = nested_spec.get("transform")
                        if transform and callable(transform):
                            nested_value = transform(nested_value)

                        if nested_value is not None:
                            nested_mapped[nested_key] = nested_value
                            has_non_null_values = True

                    if has_non_null_values and nested_mapped:
                        mapped_config[key] = nested_mapped

                elif spec_def.get("options") and value is None:
                    if key == "primary_smtp_config":
                        smtp_keys = ["primarySMTPConfig", "fromEmail", "toEmail"]
                        if any(detail.get(smtp_key) for smtp_key in smtp_keys):
                            nested_mapped = OrderedDict()
                            for nested_key, nested_spec in spec_def["options"].items():
                                if nested_key in ["server_address", "smtp_type", "port"]:
                                    nested_mapped[nested_key] = None
                            if nested_mapped:
                                mapped_config[key] = nested_mapped

                else:
                    if value is not None:
                        transform = spec_def.get("transform")
                        if transform and callable(transform):
                            transformed_value = transform(detail)
                            if transformed_value is not None:
                                mapped_config[key] = transformed_value
                        else:
                            mapped_config[key] = value

                    elif spec_def.get("transform"):
                        transform = spec_def.get("transform")
                        if transform and callable(transform):
                            transformed_value = transform(detail)
                            if transformed_value is not None:
                                mapped_config[key] = transformed_value

            if mapped_config:
                modified_configs.append(mapped_config)

        self.log("Completed modification of all details.", "INFO")
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
        self.log("Starting YAML config generation with parameters: {0}".format(yaml_config_generator), "DEBUG")

        # Check if generate_all_configurations is enabled
        generate_all = yaml_config_generator.get("generate_all_configurations", False)
        file_path = yaml_config_generator.get("file_path")

        if not file_path:
            file_path = self.generate_filename()
            self.log("No file_path provided, generated default: {0}".format(file_path), "DEBUG")
        else:
            self.log("File path determined: {0}".format(file_path), "DEBUG")

        component_specific_filters = yaml_config_generator.get("component_specific_filters") or {}

        # Set defaults for generate_all_configurations mode
        if generate_all:
            self.log("Generate all configurations mode enabled", "INFO")
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
                self.log("Set default components list for generate_all_configurations", "DEBUG")

        # Validate components_list
        components_list = component_specific_filters.get("components_list", [])
        if components_list:
            allowed_components = list(self.module_schema["network_elements"].keys())
            invalid_components = [comp for comp in components_list if comp not in allowed_components]

            if invalid_components:
                self.msg = (
                    "Invalid components found in components_list: {0}. "
                    "Only the following components are allowed: {1}. "
                    "Please remove the invalid components and try again.".format(
                        invalid_components, allowed_components
                    )
                )
                self.set_operation_result("failed", True, self.msg, "ERROR")
                return self

        try:
            self.log("Generating configurations for components: {0}".format(components_list), "DEBUG")
            final_config = {}

            for component in components_list:
                if component in self.module_schema["network_elements"]:
                    component_info = self.module_schema["network_elements"][component]
                    get_function = component_info.get("get_function_name")

                    if get_function and callable(get_function):
                        self.log("Processing component: {0}".format(component), "DEBUG")
                        try:
                            result = get_function(component_info, {"component_specific_filters": component_specific_filters})

                            if isinstance(result, dict):
                                for key, value in result.items():
                                    if value:
                                        final_config[key] = value
                                        self.log("Added {0} configurations: {1} items".format(key, len(value) if isinstance(value, list) else 1), "DEBUG")

                        except Exception as e:
                            self.log("Error processing component {0}: {1}".format(component, str(e)), "ERROR")
                            continue
                    else:
                        self.log("No get function found for component: {0}".format(component), "WARNING")
                else:
                    self.log("Unknown component: {0}".format(component), "WARNING")

            if final_config:
                self.log("Successfully generated configurations for {0} components".format(len(final_config)), "INFO")
                playbook_data = self.generate_playbook_structure(final_config, file_path)

                self.write_dict_to_yaml(playbook_data, file_path)

                self.msg = "YAML config generation Task succeeded for module '{0}'.".format(self.module_name)
                self.result["response"] = {"file_path": file_path}
                self.set_operation_result("success", True, self.msg, "INFO")
            else:
                self.msg = "No configurations found to generate. Verify that the components exist and have data."
                self.set_operation_result("success", False, self.msg, "INFO")

        except Exception as e:
            self.msg = "Error during YAML config generation: {0}".format(str(e))
            self.set_operation_result("failed", False, self.msg, "ERROR")

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
        self.log("Generating playbook structure for file: {0}".format(file_path), "DEBUG")
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
            object: Self instance with the 'want' attribute populated and status
            set to success. The 'want' structure contains validated configuration
            ready for processing.
        """
        self.log("Creating Parameters for API Calls with state: {0}".format(state), "INFO")

        want = {}
        want["yaml_config_generator"] = config
        self.log("yaml_config_generator added to want: {0}".format(want["yaml_config_generator"]), "INFO")

        self.want = want
        self.log("Desired State (want): {0}".format(str(self.want)), "INFO")
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
        if not self.want:
            self.msg = "No configuration found in 'want' for processing"
            self.set_operation_result("failed", False, self.msg, "ERROR")
            return self

        yaml_config_generator = self.want.get("yaml_config_generator")
        if yaml_config_generator:
            self.log("Processing yaml_config_generator from want", "DEBUG")
            self.yaml_config_generator(yaml_config_generator).check_return_status()
        else:
            self.msg = "No yaml_config_generator found in want"
            self.set_operation_result("failed", False, self.msg, "ERROR")

        return self


def main():
    """main entry point for module execution"""
    # Define the specification for the module's arguments
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

    ccc_events_and_notifications_playbook_generator = EventsNotificationsPlaybookGenerator(module)

    if (
        ccc_events_and_notifications_playbook_generator.compare_dnac_versions(
            ccc_events_and_notifications_playbook_generator.get_ccc_version(), "2.3.5.3"
        )
        < 0
    ):
        ccc_events_and_notifications_playbook_generator.msg = (
            "The specified version '{0}' does not support the YAML Playbook generation "
            "for Events and Notifications Management Module. Supported versions start from '2.3.5.3' onwards. "
            "Version '2.3.5.3' introduces APIs for retrieving events and notifications settings from "
            "the Catalyst Center".format(
                ccc_events_and_notifications_playbook_generator.get_ccc_version()
            )
        )
        ccc_events_and_notifications_playbook_generator.set_operation_result(
            "failed", False, ccc_events_and_notifications_playbook_generator.msg, "ERROR"
        ).check_return_status()

    # Get the state parameter from the provided parameters
    state = ccc_events_and_notifications_playbook_generator.params.get("state")

    # Check if the state is valid
    if state not in ccc_events_and_notifications_playbook_generator.supported_states:
        ccc_events_and_notifications_playbook_generator.status = "invalid"
        ccc_events_and_notifications_playbook_generator.msg = "State {0} is invalid".format(state)
        ccc_events_and_notifications_playbook_generator.check_return_status()

    # Validate the input parameters and check the return status
    ccc_events_and_notifications_playbook_generator.validate_input().check_return_status()
    config = ccc_events_and_notifications_playbook_generator.validated_config

    # Handle default configuration when no specific config is provided
    if len(config) == 1:
        config_item = config[0]

        # Check if generate_all_configurations is enabled
        if config_item.get("generate_all_configurations", False):
            ccc_events_and_notifications_playbook_generator.log("Generate all configurations mode enabled - setting default components", "INFO")
            if not config_item.get("component_specific_filters"):
                config_item["component_specific_filters"] = {
                    "components_list": [
                        "webhook_destinations", "email_destinations", "syslog_destinations",
                        "snmp_destinations", "itsm_settings", "webhook_event_notifications",
                        "email_event_notifications", "syslog_event_notifications"
                    ]
                }
        elif not config_item.get("component_specific_filters"):
            # Default behavior for normal mode
            ccc_events_and_notifications_playbook_generator.msg = (
                "No valid configurations found in the provided parameters."
            )
            ccc_events_and_notifications_playbook_generator.validated_config = [
                {
                    'component_specific_filters': {
                        'components_list': [
                            "webhook_destinations", "email_destinations", "syslog_destinations",
                            "snmp_destinations", "itsm_settings", "webhook_event_notifications",
                            "email_event_notifications", "syslog_event_notifications"
                        ]
                    }
                }
            ]

    for config in ccc_events_and_notifications_playbook_generator.validated_config:
        ccc_events_and_notifications_playbook_generator.reset_values()
        ccc_events_and_notifications_playbook_generator.get_want(config, state).check_return_status()
        ccc_events_and_notifications_playbook_generator.get_diff_state_apply[state]().check_return_status()

    module.exit_json(**ccc_events_and_notifications_playbook_generator.result)


if __name__ == "__main__":
    main()
