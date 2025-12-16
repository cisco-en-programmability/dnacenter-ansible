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
          a default file name  "<module_name>_playbook_<DD_Mon_YYYY_HH_MM_SS_MS>.yml".
        - For example, "events_and_notifications_workflow_manager_playbook_22_Apr_2025_21_43_26_379.yml".
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
"""

RETURN = r"""
# Case_1: Success Scenario
response_1:
  description: A dictionary with the response returned by the Cisco Catalyst Center Python SDK
  returned: always
  type: dict
  sample: >
    {
      "response":
        {
          "response": String,
          "version": String
        },
      "msg": String
    }
# Case_2: Error Scenario
response_2:
  description: A string with the response returned by the Cisco Catalyst Center Python SDK
  returned: always
  type: list
  sample: >
    {
      "response": [],
      "msg": String
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
        Initialize an instance of the class.
        Args:
            module: The module associated with the class instance.
        Returns:
            The method does not return a value.
        """
        self.supported_states = ["gathered"]
        self.get_diff_state_apply = {"gathered": self.get_diff_gathered}
        super().__init__(module)
        self.module_schema = self.events_notifications_workflow_manager_mapping()
        self.module_name = "events_and_notifications_workflow_manager"

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

        # Check if configuration is available
        if not self.config:
            self.status = "success"
            self.msg = "Configuration is not available in the playbook for validation"
            self.log(self.msg, "ERROR")
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
        Constructs and returns a structured mapping for managing events and notifications configuration elements.
        """
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
    def webhook_destinations_reverse_mapping_function(self, requested_features=None):
        """Returns the reverse mapping specification for webhook destination details."""
        self.log("Generating reverse mapping specification for webhook destination details", "DEBUG")
        return self.webhook_destinations_temp_spec()

    def email_destinations_reverse_mapping_function(self, requested_features=None):
        """Returns the reverse mapping specification for email destination details."""
        self.log("Generating reverse mapping specification for email destination details", "DEBUG")
        return self.email_destinations_temp_spec()

    def syslog_destinations_reverse_mapping_function(self, requested_features=None):
        """Returns the reverse mapping specification for syslog destination details."""
        self.log("Generating reverse mapping specification for syslog destination details", "DEBUG")
        return self.syslog_destinations_temp_spec()

    def snmp_destinations_reverse_mapping_function(self, requested_features=None):
        """Returns the reverse mapping specification for SNMP destination details."""
        self.log("Generating reverse mapping specification for SNMP destination details", "DEBUG")
        return self.snmp_destinations_temp_spec()

    def itsm_settings_reverse_mapping_function(self, requested_features=None):
        """Returns the reverse mapping specification for ITSM settings details."""
        self.log("Generating reverse mapping specification for ITSM settings details", "DEBUG")
        return self.itsm_settings_temp_spec()

    def webhook_event_notifications_reverse_mapping_function(self, requested_features=None):
        """Returns the reverse mapping specification for webhook event notification details."""
        self.log("Generating reverse mapping specification for webhook event notification details", "DEBUG")
        return self.webhook_event_notifications_temp_spec()

    def email_event_notifications_reverse_mapping_function(self, requested_features=None):
        """Returns the reverse mapping specification for email event notification details."""
        self.log("Generating reverse mapping specification for email event notification details", "DEBUG")
        return self.email_event_notifications_temp_spec()

    def syslog_event_notifications_reverse_mapping_function(self, requested_features=None):
        """Returns the reverse mapping specification for syslog event notification details."""
        self.log("Generating reverse mapping specification for syslog event notification details", "DEBUG")
        return self.syslog_event_notifications_temp_spec()

    # Temp spec functions
    def webhook_destinations_temp_spec(self):
        """Constructs a temporary specification for webhook destination details."""
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
        """Constructs a temporary specification for email destination details."""
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
        """Constructs a temporary specification for syslog destination details."""
        self.log("Generating temporary specification for syslog destination details.", "DEBUG")
        return OrderedDict({
            "name": {"type": "str", "source_key": "name"},
            "description": {"type": "str", "source_key": "description"},
            "server_address": {"type": "str", "source_key": "host"},
            "protocol": {"type": "str", "source_key": "protocol"},
            "port": {"type": "int", "source_key": "port"},
        })

    def snmp_destinations_temp_spec(self):
        """Constructs a temporary specification for SNMP destination details."""
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
        """Constructs a temporary specification for ITSM settings details."""
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
        """Constructs a temporary specification for webhook event notification details."""
        self.log("Generating temporary specification for webhook event notification details.", "DEBUG")
        return OrderedDict({
            "name": {"type": "str", "source_key": "name"},
            "description": {"type": "str", "source_key": "description"},
            "sites": {"type": "list", "source_key": "filter", "transform": self.extract_sites_from_filter},
            "events": {"type": "list", "source_key": "subscriptionEventTypes", "transform": self.extract_event_names},
            "destination": {"type": "str", "source_key": "webhookEndpointIds", "transform": self.extract_webhook_destination_name},
        })

    def email_event_notifications_temp_spec(self):
        """Constructs a temporary specification for email event notification details."""
        self.log("Generating temporary specification for email event notification details.", "DEBUG")
        return OrderedDict({
            "name": {"type": "str", "source_key": "name"},
            "description": {"type": "str", "source_key": "description"},
            "sites": {"type": "list", "source_key": "filter", "transform": self.extract_sites_from_filter},
            "events": {"type": "list", "source_key": "filter", "transform": self.extract_event_names},
            "sender_email": {"type": "str", "source_key": "subscriptionEndpoints", "transform": self.extract_sender_email},
            "recipient_emails": {"type": "list", "source_key": "subscriptionEndpoints", "transform": self.extract_recipient_emails},
            "subject": {"type": "str", "source_key": "subscriptionEndpoints", "transform": self.extract_subject},
            "instance": {"type": "str", "source_key": "name", "transform": self.create_instance_name},
            "instance_description": {"type": "str", "source_key": "description", "transform": self.create_instance_description},
        })

    def syslog_event_notifications_temp_spec(self):
        """Constructs a temporary specification for syslog event notification details."""
        self.log("Generating temporary specification for syslog event notification details.", "DEBUG")
        return OrderedDict({
            "name": {"type": "str", "source_key": "name"},
            "description": {"type": "str", "source_key": "description"},
            "sites": {"type": "list", "source_key": "filter", "transform": self.extract_sites_from_filter},
            "events": {"type": "list", "source_key": "subscriptionEventTypes", "transform": self.extract_event_names},
            "destination": {"type": "str", "source_key": "syslogConfigId", "transform": self.extract_syslog_destination_name},
        })

    def redact_password(self, password):
        """Redacts password for security."""
        return "***REDACTED***" if password else None

    def create_instance_name(self, notification):
        """Creates instance name from subscription endpoints EMAIL details."""
        if not notification or not isinstance(notification, dict):
            return None

        # Extract from subscriptionEndpoints for EMAIL connector
        subscription_endpoints = notification.get("subscriptionEndpoints", [])
        for endpoint in subscription_endpoints:
            subscription_details = endpoint.get("subscriptionDetails", {})
            if subscription_details.get("connectorType") == "EMAIL":
                return subscription_details.get("name")

        return None

    def create_instance_description(self, notification):
        """Creates instance description from subscription endpoints EMAIL details."""
        if not notification or not isinstance(notification, dict):
            return None

        # Extract from subscriptionEndpoints for EMAIL connector
        subscription_endpoints = notification.get("subscriptionEndpoints", [])
        for endpoint in subscription_endpoints:
            subscription_details = endpoint.get("subscriptionDetails", {})
            if subscription_details.get("connectorType") == "EMAIL":
                return subscription_details.get("description")

        return None

    def extract_event_names(self, notification):
        """Extract event names from filter.eventIds and resolve using Get Event Artifacts API."""
        if not notification or not isinstance(notification, dict):
            return []

        # Get event IDs from filter
        filter_obj = notification.get("filter", {})
        event_ids = filter_obj.get("eventIds", [])

        if not event_ids:
            return []

        # Resolve event IDs to event names using Get Event Artifacts API
        event_names = []
        for event_id in event_ids:
            try:
                event_name = self.get_event_name_from_api(event_id)
                if event_name:
                    event_names.append(event_name)
                else:
                    event_names.append(event_id)  # Fallback to event ID
            except Exception as e:
                self.log("Error resolving event ID {0}: {1}".format(event_id, str(e)), "WARNING")
                event_names.append(event_id)  # Fallback to event ID

        return event_names

    def get_event_name_from_api(self, event_id):
        """Get event name from event ID using Get Event Artifacts API."""
        if not event_id:
            return None

        try:
            # Try the Get Event Artifacts API
            response = self.dnac._exec(
                family="event_management",
                function="get_event_artifacts",
                op_modifies=False,
                params={"event_ids": event_id}
            )
            self.log("Received API response for get_event_artifacts {0}".format(response), "DEBUG")

            self.log("Event Artifacts API response for {0}: {1}".format(event_id, response), "DEBUG")

            # Parse the response for event name
            # The response is directly a list, not wrapped in a "response" key
            if isinstance(response, list) and len(response) > 0:
                event_info = response[0]  # Get the first item from the list
                event_name = event_info.get("name")  # Extract the "name" field
                if event_name:
                    self.log("Successfully resolved event ID {0} to name: {1}".format(event_id, event_name), "INFO")
                    return event_name

            # If response is a dict (fallback)
            elif isinstance(response, dict):
                events = response.get("response") or response.get("events") or []
                if events and len(events) > 0:
                    event_info = events[0] if isinstance(events, list) else events
                    event_name = event_info.get("name")
                    if event_name:
                        self.log("Successfully resolved event ID {0} to name: {1}".format(event_id, event_name), "INFO")
                        return event_name

            # If no event name found, return the event_id itself
            self.log("No event name found in API response for {0}, returning event ID".format(event_id), "WARNING")
            return event_id

        except Exception as e:
            self.log("Error calling event artifacts API for event ID {0}: {1}".format(event_id, str(e)), "WARNING")
            # Return the event_id itself if API fails
            return event_id

    def extract_sites_from_filter(self, filter_data):
        """Extract site names from filter data."""
        if not filter_data:
            return []
        try:
            if isinstance(filter_data, dict):
                sites = filter_data.get("sites", [])
                if sites:
                    return sites
                site_ids = filter_data.get("siteIds", [])
                if site_ids:
                    site_names = []
                    site_mapping = self.get_site_id_name_mapping()
                    for site_id in site_ids:
                        site_name = site_mapping.get(site_id)
                        if site_name:
                            site_names.append(site_name)
                    return site_names
            elif isinstance(filter_data, list):
                return filter_data
        except Exception as e:
            self.log("Error extracting sites from filter: {0}".format(str(e)), "WARNING")
        return []

    def extract_webhook_destination_name(self, notification):
        """Extract webhook destination name from subscriptionEndpoints."""
        if not notification:
            return None

        subscription_endpoints = notification.get("subscriptionEndpoints", [])
        for endpoint in subscription_endpoints:
            subscription_details = endpoint.get("subscriptionDetails", {})
            if subscription_details.get("connectorType") == "REST":
                return subscription_details.get("name")
        return None

    def extract_syslog_destination_name(self, notification):
        """Extract syslog destination name from subscriptionEndpoints."""
        if not notification:
            return None

        subscription_endpoints = notification.get("subscriptionEndpoints", [])
        for endpoint in subscription_endpoints:
            subscription_details = endpoint.get("subscriptionDetails", {})
            if subscription_details.get("connectorType") == "SYSLOG":
                return subscription_details.get("name")
        return None

    def extract_sender_email(self, notification):
        """Extract sender email from subscriptionEndpoints."""
        if not notification:
            return None

        subscription_endpoints = notification.get("subscriptionEndpoints", [])
        for endpoint in subscription_endpoints:
            subscription_details = endpoint.get("subscriptionDetails", {})
            if subscription_details.get("connectorType") == "EMAIL":
                return subscription_details.get("fromEmailAddress")
        return None

    def extract_recipient_emails(self, notification):
        """Extract recipient emails from subscriptionEndpoints."""
        if not notification:
            return []

        subscription_endpoints = notification.get("subscriptionEndpoints", [])
        for endpoint in subscription_endpoints:
            subscription_details = endpoint.get("subscriptionDetails", {})
            if subscription_details.get("connectorType") == "EMAIL":
                return subscription_details.get("toEmailAddresses", [])
        return []

    def extract_subject(self, notification):
        """Extract subject from subscriptionEndpoints."""
        if not notification:
            return None

        subscription_endpoints = notification.get("subscriptionEndpoints", [])
        for endpoint in subscription_endpoints:
            subscription_details = endpoint.get("subscriptionDetails", {})
            if subscription_details.get("connectorType") == "EMAIL":
                return subscription_details.get("subject")
        return None

    def modify_parameters(self, temp_spec, details_list):
        """
        Transforms API response data according to the provided specification.
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

                # Handle nested options (like headers in webhook destinations)
                if spec_def.get("options") and isinstance(value, list):
                    nested_list = []
                    for item in value:
                        if isinstance(item, dict):
                            nested_mapped = OrderedDict()
                            for nested_key, nested_spec in spec_def["options"].items():
                                nested_source_key = nested_spec.get("source_key", nested_key)
                                nested_value = item.get(nested_source_key)

                                if nested_value is not None:
                                    # Apply transformation if specified
                                    transform = nested_spec.get("transform")
                                    if transform and callable(transform):
                                        nested_value = transform(nested_value)
                                    nested_mapped[nested_key] = nested_value

                            if nested_mapped:
                                nested_list.append(nested_mapped)

                    if nested_list:
                        mapped_config[key] = nested_list

                # Handle nested dictionaries (like SMTP configs in email destinations)
                elif spec_def.get("options") and isinstance(value, dict):
                    nested_mapped = OrderedDict()
                    for nested_key, nested_spec in spec_def["options"].items():
                        nested_source_key = nested_spec.get("source_key", nested_key)
                        nested_value = value.get(nested_source_key)

                        if nested_value is not None:
                            # Apply transformation if specified
                            transform = nested_spec.get("transform")
                            if transform and callable(transform):
                                nested_value = transform(nested_value)
                            nested_mapped[nested_key] = nested_value

                    if nested_mapped:
                        mapped_config[key] = nested_mapped

                else:
                    # Handle simple values and transform functions
                    if value is not None:
                        # Apply transformation if specified
                        transform = spec_def.get("transform")
                        if transform and callable(transform):
                            value = transform(detail)  # Changed from transform(value) to transform(detail)
                        mapped_config[key] = value
                    # CRITICAL FIX: Handle transform functions even when source value is None/missing
                    elif spec_def.get("transform"):
                        transform = spec_def.get("transform")
                        if transform and callable(transform):
                            transformed_value = transform(detail)  # Pass entire detail object
                            if transformed_value is not None:
                                mapped_config[key] = transformed_value

            if mapped_config:
                modified_configs.append(mapped_config)

        self.log("Completed modification of all details.", "INFO")
        return modified_configs

    # Data retrieval functions
    def get_webhook_destinations(self, network_element, filters):
        """Retrieves webhook destination details based on the provided filters."""
        self.log("Starting to retrieve webhook destinations", "DEBUG")

        component_specific_filters = filters.get("component_specific_filters", {})
        destination_filters = component_specific_filters.get("destination_filters", {})
        destination_names = destination_filters.get("destination_names", [])

        try:
            webhook_configs = self.get_all_webhook_destinations()

            if destination_names:
                self.log("Applying destination name filters: {0}".format(destination_names), "DEBUG")
                final_webhook_configs = [config for config in webhook_configs if config.get("name") in destination_names]
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

    def get_all_webhook_destinations(self):
        """Helper method to get all webhook destinations."""
        try:
            offset = 0
            limit = 10
            all_webhooks = []

            while True:
                response = self.dnac._exec(
                    family="event_management",
                    function="get_webhook_destination",
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

            return all_webhooks

        except Exception as e:
            self.log("Error retrieving webhook destinations: {0}".format(str(e)), "WARNING")
            return []

    def get_email_destinations(self, network_element, filters):
        """Retrieves email destination details based on the provided filters."""
        self.log("Starting to retrieve email destinations", "DEBUG")

        try:
            email_configs = self.get_all_email_destinations()

        except Exception as e:
            self.log("Failed to retrieve email destinations: {0}".format(str(e)), "ERROR")
            email_configs = []

        email_destinations_temp_spec = self.email_destinations_temp_spec()
        modified_email_configs = self.modify_parameters(email_destinations_temp_spec, email_configs)

        result = {"email_destinations": modified_email_configs}
        self.log("Final email destinations result: {0} configs transformed".format(len(modified_email_configs)), "INFO")
        return result

    def get_all_email_destinations(self):
        """Helper method to get all email destinations."""
        try:
            response = self.dnac._exec(
                family="event_management",
                function="get_email_destination",
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
            self.log("Error retrieving email destinations: {0}".format(str(e)), "WARNING")
            return []

    def get_syslog_destinations(self, network_element, filters):
        """Retrieves syslog destination details based on the provided filters."""
        self.log("Starting to retrieve syslog destinations", "DEBUG")

        component_specific_filters = filters.get("component_specific_filters", {})
        destination_filters = component_specific_filters.get("destination_filters", {})
        destination_names = destination_filters.get("destination_names", [])

        try:
            syslog_configs = self.get_all_syslog_destinations()

            if destination_names:
                self.log("Applying destination name filters: {0}".format(destination_names), "DEBUG")
                final_syslog_configs = [config for config in syslog_configs if config.get("name") in destination_names]
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

    def get_all_syslog_destinations(self):
        """Helper method to get all syslog destinations."""
        try:
            response = self.dnac._exec(
                family="event_management",
                function="get_syslog_destination",
                op_modifies=False,
                params={},
            )
            self.log("Received API response for syslog destinations: {0}".format(response), "DEBUG")

            syslog_configs = response.get("statusMessage", [])
            return syslog_configs if isinstance(syslog_configs, list) else []

        except Exception as e:
            self.log("Error retrieving syslog destinations: {0}".format(str(e)), "WARNING")
            return []

    def get_snmp_destinations(self, network_element, filters):
        """Retrieves SNMP destination details based on the provided filters."""
        self.log("Starting to retrieve SNMP destinations", "DEBUG")

        component_specific_filters = filters.get("component_specific_filters", {})
        destination_filters = component_specific_filters.get("destination_filters", {})
        destination_names = destination_filters.get("destination_names", [])

        try:
            snmp_configs = self.get_all_snmp_destinations()

            if destination_names:
                self.log("Applying destination name filters: {0}".format(destination_names), "DEBUG")
                final_snmp_configs = [config for config in snmp_configs if config.get("name") in destination_names]
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

    def get_all_snmp_destinations(self):
        """Helper method to get all SNMP destinations."""
        try:
            offset = 0
            limit = 10
            all_snmp = []

            while True:
                try:
                    response = self.dnac._exec(
                        family="event_management",
                        function="get_snmp_destination",
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
                    self.log("Error in pagination for SNMP destinations: {0}".format(str(e)), "WARNING")
                    break

            return all_snmp

        except Exception as e:
            self.log("Error retrieving SNMP destinations: {0}".format(str(e)), "WARNING")
            return []

    def get_itsm_settings(self, network_element, filters):
        """Retrieves ITSM settings details based on the provided filters."""
        self.log("Starting to retrieve ITSM settings", "DEBUG")

        component_specific_filters = filters.get("component_specific_filters", {})
        itsm_filters = component_specific_filters.get("itsm_filters", {})
        instance_names = itsm_filters.get("instance_names", [])

        try:
            itsm_configs = self.get_all_itsm_settings()

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

    def get_all_itsm_settings(self):
        """Helper method to get all ITSM settings."""
        try:
            response = self.dnac._exec(
                family="event_management",
                function="get_all_itsm_integration_settings",
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
            self.log("Error retrieving ITSM settings: {0}".format(str(e)), "WARNING")
            return []

    def get_all_webhook_event_notifications(self):
        """Helper method to get all webhook event notifications."""
        try:
            offset = 0
            limit = 10
            all_notifications = []

            while True:
                try:
                    response = self.dnac._exec(
                        family="event_management",
                        function="get_rest_webhook_event_subscriptions",
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
                    self.log("Error in pagination for webhook event notifications: {0}".format(str(e)), "WARNING")
                    break

            return all_notifications

        except Exception as e:
            self.log("Error retrieving webhook event notifications: {0}".format(str(e)), "WARNING")
            return []

    def get_all_email_event_notifications(self):
        """Helper method to get all email event notifications."""
        try:
            response = self.dnac._exec(
                family="event_management",
                function="get_email_event_subscriptions",
                op_modifies=False,
                params={}
            )
            self.log("Received API response for email event notifications: {0}".format(response), "DEBUG")

            # DEBUG: Log the actual API response structure
            self.log("Email event notifications API response: {0}".format(response), "DEBUG")

            if isinstance(response, list):
                notifications = response
            elif isinstance(response, dict):
                notifications = response.get("response", [])
            else:
                notifications = []

            # DEBUG: Log each notification's structure
            for i, notification in enumerate(notifications):
                self.log("Email notification {0} fields: {1}".format(i, list(notification.keys())), "DEBUG")
                self.log("Full notification data: {0}".format(notification), "DEBUG")

            return notifications

        except Exception as e:
            self.log("Error retrieving email event notifications: {0}".format(str(e)), "WARNING")
            return []

    def get_syslog_event_notifications(self, network_element, filters):
        """Retrieves syslog event notification details based on the provided filters."""
        self.log("Starting to retrieve syslog event notifications", "DEBUG")

        component_specific_filters = filters.get("component_specific_filters", {})
        notification_filters = component_specific_filters.get("notification_filters", {})
        subscription_names = notification_filters.get("subscription_names", [])

        try:
            notification_configs = self.get_all_syslog_event_notifications()

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

    def get_all_syslog_event_notifications(self):
        """Helper method to get all syslog event notifications."""
        try:
            offset = 0
            limit = 10
            all_notifications = []

            while True:
                try:
                    response = self.dnac._exec(
                        family="event_management",
                        function="get_syslog_event_subscriptions",
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
                    self.log("Error in pagination for syslog event notifications: {0}".format(str(e)), "WARNING")
                    break

            return all_notifications

        except Exception as e:
            self.log("Error retrieving syslog event notifications: {0}".format(str(e)), "WARNING")
            return []

    def get_webhook_event_notifications(self, network_element, filters):
        """Retrieves webhook event notification details based on the provided filters."""
        self.log("Starting to retrieve webhook event notifications", "DEBUG")

        component_specific_filters = filters.get("component_specific_filters", {})
        notification_filters = component_specific_filters.get("notification_filters", {})
        subscription_names = notification_filters.get("subscription_names", [])

        try:
            notification_configs = self.get_all_webhook_event_notifications()

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

    def get_email_event_notifications(self, network_element, filters):
        """Retrieves email event notification details based on the provided filters."""
        self.log("Starting to retrieve email event notifications", "DEBUG")

        component_specific_filters = filters.get("component_specific_filters", {})
        notification_filters = component_specific_filters.get("notification_filters", {})
        subscription_names = notification_filters.get("subscription_names", [])

        try:
            notification_configs = self.get_all_email_event_notifications()

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

    def yaml_config_generator(self, yaml_config_generator):
        """
        Generates a YAML configuration file based on the provided parameters.
        """
        self.log("Starting YAML config generation with parameters: {0}".format(yaml_config_generator), "DEBUG")

        # Check if generate_all_configurations is enabled
        generate_all = yaml_config_generator.get("generate_all_configurations", False)
        file_path = yaml_config_generator.get("file_path")

        if not file_path:
            file_path = self.generate_filename()  # ← Uses BrownFieldHelper.generate_filename()
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

        # Generate configurations manually
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
                            # Call the component's get function
                            result = get_function(component, {"component_specific_filters": component_specific_filters})

                            # Merge result into final_config
                            if isinstance(result, dict):
                                for key, value in result.items():
                                    if value:  # Only add non-empty configurations
                                        final_config[key] = value
                                        self.log("Added {0} configurations: {1} items".format(key, len(value) if isinstance(value, list) else 1), "DEBUG")

                        except Exception as e:
                            self.log("Error processing component {0}: {1}".format(component, str(e)), "WARNING")
                            continue
                    else:
                        self.log("No get function found for component: {0}".format(component), "WARNING")
                else:
                    self.log("Unknown component: {0}".format(component), "WARNING")

            if final_config:
                self.log("Successfully generated configurations for {0} components".format(len(final_config)), "INFO")
                playbook_data = self.generate_playbook_structure(final_config, file_path)

                # Use the helper function instead of custom write_yaml_file
                self.write_dict_to_yaml(playbook_data, file_path)  # ← Use BrownFieldHelper method

                self.result["changed"] = True
                self.msg = "YAML config generation Task succeeded for module '{0}'.".format(self.module_name)
                self.result["response"] = {"file_path": file_path}
                self.set_operation_result("success", True, self.msg, "INFO")
            else:
                self.msg = "No configurations found to generate. Verify that the components exist and have data."
                self.set_operation_result("failed", False, self.msg, "INFO")

        except Exception as e:
            self.msg = "Error during YAML config generation: {0}".format(str(e))
            self.set_operation_result("failed", False, self.msg, "ERROR")

        return self

    def generate_playbook_structure(self, configurations, file_path):
        """Generate the complete playbook structure with ALL configurations in ONE single task."""

        # Build ONLY the config list with ALL items
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

        # Return ONLY the config data
        return {"config": config_list}

    def get_want(self, config, state):
        """
        Creates parameters for API calls based on the configuration.
        Args:
            config (dict): The configuration data for events and notifications.
            state (str): The desired state ('gathered').
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
        Generates the YAML configuration based on the provided filters.
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
        "config_verify": {"type": "bool", "default": False},
        "dnac_api_task_timeout": {"type": "int", "default": 1200},
        "dnac_task_poll_interval": {"type": "int", "default": 2},
        "config": {"required": True, "type": "list", "elements": "dict"},
        "state": {"default": "gathered", "choices": ["gathered"]},
    }

    # Initialize the Ansible module with the provided argument specifications
    module = AnsibleModule(argument_spec=element_spec, supports_check_mode=True)

    # Initialize the EventsNotificationsPlaybookGenerator object with the module
    ccc_events_and_notifications_playbook_generator = EventsNotificationsPlaybookGenerator(module)

    # Check version compatibility (add this check)
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

    # Iterate over the validated configuration parameters
    for config in ccc_events_and_notifications_playbook_generator.validated_config:
        ccc_events_and_notifications_playbook_generator.reset_values()
        ccc_events_and_notifications_playbook_generator.get_want(config, state).check_return_status()  # ← This is correct now
        ccc_events_and_notifications_playbook_generator.get_diff_state_apply[state]().check_return_status()

    module.exit_json(**ccc_events_and_notifications_playbook_generator.result)


if __name__ == "__main__":
    main()
