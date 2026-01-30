#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright (c) 2026, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

"""Ansible module to generate YAML configurations for Wired Campus Automation Module."""
from __future__ import absolute_import, division, print_function

__metaclass__ = type
__author__ = "Mridul Saurabh, Madhan Sankaranarayanan"

DOCUMENTATION = r"""
---
module: brownfield_inventory_playbook_generator
short_description: Generate YAML configurations playbook for 'inventory_workflow_manager' module.
description:
- Generates YAML configurations compatible with the 'inventory_workflow_manager'
  module, reducing the effort required to manually create Ansible playbooks and
  enabling programmatic modifications.
- The YAML configurations generated represent the network device inventory configurations
  such as device credentials, management IP addresses, device types, and other device-specific
  attributes configured on the Cisco Catalyst Center.
- Note: Devices with type 'NETWORK_DEVICE' are automatically excluded from all generated configurations.
version_added: 6.44.0
extends_documentation_fragment:
- cisco.dnac.workflow_manager_params
author:
- Mridul Saurabh (@msaurabh)
- Madhan Sankaranarayanan (@madhansansel)
options:
  state:
    description: The desired state of Cisco Catalyst Center after module execution.
    type: str
    choices: [gathered]
    default: gathered
  config:
    description:
    - A list of filters for generating YAML playbook compatible with the 'inventory_workflow_manager'
      module.
    - Filters specify which devices and credentials to include in the YAML configuration file.
    - If "components_list" is specified, only those components are included, regardless of the filters.
    type: list
    elements: dict
    required: true
    suboptions:
      generate_all_configurations:
        description:
          - When set to True, automatically generates YAML configurations for all devices in Cisco Catalyst Center.
          - This mode discovers all managed devices in Cisco Catalyst Center and extracts all device inventory configurations.
          - When enabled, the config parameter becomes optional and will use default values if not provided.
          - A default filename will be generated automatically if file_path is not specified.
          - This is useful for complete brownfield infrastructure discovery and documentation.
          - Note - Devices with type 'NETWORK_DEVICE' are excluded from output.
        type: bool
        required: false
        default: false
      file_path:
        description:
        - Path where the YAML configuration file will be saved.
        - If not provided, the file will be saved in the current working directory with
          a default file name  C(inventory_workflow_manager_playbook_<YYYY-MM-DD_HH-MM-SS>.yml).
        - For example, C(inventory_workflow_manager_playbook_2026-01-24_12-33-20.yml).
        type: str
      global_filters:
        description:
        - Global filters to apply when generating the YAML configuration file.
        - These filters apply to all components unless overridden by component-specific filters.
        - Supports filtering devices by IP address, hostname, or serial number.
        type: dict
        suboptions:
          ip_address_list:
            description:
            - List of device IP addresses to include in the YAML configuration file.
            - When specified, only devices with matching management IP addresses will be included.
            - For example, ["192.168.1.1", "192.168.1.2", "192.168.1.3"]
            type: list
            elements: str
          hostname_list:
            description:
            - List of device hostnames to include in the YAML configuration file.
            - When specified, only devices with matching hostnames will be included.
            - For example, ["switch-1", "router-1", "firewall-1"]
            type: list
            elements: str
          serial_number_list:
            description:
            - List of device serial numbers to include in the YAML configuration file.
            - When specified, only devices with matching serial numbers will be included.
            - For example, ["ABC123456789", "DEF987654321"]
            type: list
            elements: str
      component_specific_filters:
        description:
        - Filters to specify which components and device attributes to include in the YAML configuration file.
        - If "components_list" is specified, only those components are included.
        - Additional filters can be applied to narrow down device selection based on role, type, etc.
        type: dict
        suboptions:
          components_list:
            description:
            - List of components to include in the YAML configuration file.
            - Valid values are "inventory_workflow_manager".
            - If not specified, all components are included.
            type: list
            elements: str
            choices: ["role"]
          inventory_workflow_manager:
            description:
            - Specific filters for inventory_workflow_manager component.
            - These filters apply after global filters to further refine device selection.
            - Supports both single filter dict and list of filter dicts with OR logic.
            - Note - Devices with type 'NETWORK_DEVICE' are excluded from results.
            type: list
            elements: dict
            suboptions:
              role:
                description:
                - Filter devices by network role.
                - Valid values are ACCESS, CORE, DISTRIBUTION, BORDER_ROUTER, UNKNOWN.
                type: str
                choices: [ACCESS, CORE, DISTRIBUTION, BORDER_ROUTER, UNKNOWN]
requirements:
- dnacentersdk >= 2.10.10
- python >= 3.9
notes:
- SDK Methods used are
    - devices.Devices.get_device_list
    - devices.Devices.get_network_device_by_ip
- Paths used are
    - GET /dna/intent/api/v2/devices
    - GET /dna/intent/api/v2/network-device
- Devices with type 'NETWORK_DEVICE' are automatically excluded from all generated configurations.
seealso:
- module: cisco.dnac.inventory_workflow_manager
  description: Module for managing inventory configurations in Cisco Catalyst Center.
"""

EXAMPLES = r"""
- name: Generate inventory playbook for all devices
  cisco.dnac.brownfield_inventory_playbook_generator:
    dnac_host: "{{ dnac_host }}"
    dnac_port: "{{ dnac_port }}"
    dnac_username: "{{ dnac_username }}"
    dnac_password: "{{ dnac_password }}"
    dnac_verify: "{{ dnac_verify }}"
    dnac_version: "{{ dnac_version }}"
    dnac_debug: "{{ dnac_debug }}"
    state: gathered
    config:
      - generate_all_configurations: true
        file_path: "./inventory_devices_all.yml"

- name: Generate inventory playbook for specific devices by IP address
  cisco.dnac.brownfield_inventory_playbook_generator:
    dnac_host: "{{ dnac_host }}"
    dnac_port: "{{ dnac_port }}"
    dnac_username: "{{ dnac_username }}"
    dnac_password: "{{ dnac_password }}"
    dnac_verify: "{{ dnac_verify }}"
    dnac_version: "{{ dnac_version }}"
    dnac_debug: "{{ dnac_debug }}"
    state: gathered
    config:
      - global_filters:
          ip_address_list:
            - "10.195.225.40"
            - "10.195.225.42"
        file_path: "./inventory_devices_by_ip.yml"

- name: Generate inventory playbook for devices by hostname
  cisco.dnac.brownfield_inventory_playbook_generator:
    dnac_host: "{{ dnac_host }}"
    dnac_port: "{{ dnac_port }}"
    dnac_username: "{{ dnac_username }}"
    dnac_password: "{{ dnac_password }}"
    dnac_verify: "{{ dnac_verify }}"
    dnac_version: "{{ dnac_version }}"
    dnac_debug: "{{ dnac_debug }}"
    state: gathered
    config:
      - global_filters:
          hostname_list:
            - "cat9k_1"
            - "cat9k_2"
            - "switch_1"
        file_path: "./inventory_devices_by_hostname.yml"

- name: Generate inventory playbook for devices by serial number
  cisco.dnac.brownfield_inventory_playbook_generator:
    dnac_host: "{{ dnac_host }}"
    dnac_port: "{{ dnac_port }}"
    dnac_username: "{{ dnac_username }}"
    dnac_password: "{{ dnac_password }}"
    dnac_verify: "{{ dnac_verify }}"
    dnac_version: "{{ dnac_version }}"
    dnac_debug: "{{ dnac_debug }}"
    state: gathered
    config:
      - global_filters:
          serial_number_list:
            - "FCW2147L0AR1"
            - "FCW2147L0AR2"
        file_path: "./inventory_devices_by_serial.yml"

- name: Generate inventory playbook for mixed device filtering
  cisco.dnac.brownfield_inventory_playbook_generator:
    dnac_host: "{{ dnac_host }}"
    dnac_port: "{{ dnac_port }}"
    dnac_username: "{{ dnac_username }}"
    dnac_password: "{{ dnac_password }}"
    dnac_verify: "{{ dnac_verify }}"
    dnac_version: "{{ dnac_version }}"
    dnac_debug: "{{ dnac_debug }}"
    state: gathered
    config:
      - global_filters:
          ip_address_list:
            - "10.195.225.40"
          hostname_list:
            - "cat9k_1"
        file_path: "./inventory_devices_mixed_filter.yml"

- name: Generate inventory playbook with default file path
  cisco.dnac.brownfield_inventory_playbook_generator:
    dnac_host: "{{ dnac_host }}"
    dnac_port: "{{ dnac_port }}"
    dnac_username: "{{ dnac_username }}"
    dnac_password: "{{ dnac_password }}"
    dnac_verify: "{{ dnac_verify }}"
    dnac_version: "{{ dnac_version }}"
    dnac_debug: "{{ dnac_debug }}"
    state: gathered
    config:
      - global_filters:
          ip_address_list:
            - "10.195.225.40"

- name: Generate inventory playbook for multiple devices
  cisco.dnac.brownfield_inventory_playbook_generator:
    dnac_host: "{{ dnac_host }}"
    dnac_port: "{{ dnac_port }}"
    dnac_username: "{{ dnac_username }}"
    dnac_password: "{{ dnac_password }}"
    dnac_verify: "{{ dnac_verify }}"
    dnac_version: "{{ dnac_version }}"
    dnac_debug: "{{ dnac_debug }}"
    state: gathered
    config:
      - global_filters:
          ip_address_list:
            - "10.195.225.40"
            - "10.195.225.41"
            - "10.195.225.42"
            - "10.195.225.43"
        file_path: "./inventory_devices_multiple.yml"

- name: Generate inventory playbook for ACCESS role devices only
  cisco.dnac.brownfield_inventory_playbook_generator:
    dnac_host: "{{ dnac_host }}"
    dnac_port: "{{ dnac_port }}"
    dnac_username: "{{ dnac_username }}"
    dnac_password: "{{ dnac_password }}"
    dnac_verify: "{{ dnac_verify }}"
    dnac_version: "{{ dnac_version }}"
    dnac_debug: "{{ dnac_debug }}"
    state: gathered
    config:
      - component_specific_filters:
          components_list: ["inventory_workflow_manager"]
          inventory_workflow_manager:
            - role: "ACCESS"
        file_path: "./inventory_access_role_devices.yml"

"""
RETURN = r"""
# Case_1: Success Scenario
response_1:
  description: A dictionary with the response returned by the Cisco Catalyst Center Python SDK
  returned: success
  type: dict
  sample: >
    {
        "msg": {
            "YAML config generation Task succeeded for module 'inventory_workflow_manager'.": {
            "file_path": "inventory_specific_ips.yml"
            }
        },
        "response": {
            "YAML config generation Task succeeded for module 'inventory_workflow_manager'.": {
            "file_path": "inventory_specific_ips.yml"
            }
        },
        "status": "success"
    }

# Case_2: Error Scenario
response_2:
  description: A string with the error message returned by the Cisco Catalyst Center Python SDK
  returned: on failure
  type: dict
  sample: >
    {
      "msg": "Invalid 'global_filters' found for module 'inventory_workflow_manager': [\"Filter 'ip_address_list' must be a list, got NoneType\"]",
      "response": "Invalid 'global_filters' found for module 'inventory_workflow_manager': [\"Filter 'ip_address_list' must be a list, got NoneType\"]"
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


class InventoryPlaybookGenerator(DnacBase, BrownFieldHelper):
    """
    A class for generator playbook files for infrastructure deployed within the Cisco Catalyst Center using the GET APIs.
    """

    values_to_nullify = ["NOT CONFIGURED"]

    def __init__(self, module):
        """
        Initialize an instance of the class.
        Args:
            module: The module associated with the class instance.
        Returns:
            The method does not return a value.
        """
        self.supported_states = ["gathered"]
        super().__init__(module)
        self.module_schema = self.get_workflow_filters_schema()
        # self.site_id_name_dict = self.get_site_id_name_mapping()
        self.module_name = "inventory_workflow_manager"
        self.generate_all_configurations = False  # Initialize the attribute

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
            "generate_all_configurations": {"type": "bool", "required": False, "default": False},
            "file_path": {"type": "str", "required": False},
            "component_specific_filters": {"type": "dict", "required": False},
            "global_filters": {"type": "dict", "required": False},
        }

        # Import validate_list_of_dicts function here to avoid circular imports
        from ansible_collections.cisco.dnac.plugins.module_utils.dnac import validate_list_of_dicts

        # Validate params
        self.log("Validating configuration against schema.", "DEBUG")
        valid_temp, invalid_params = validate_list_of_dicts(self.config, temp_spec)

        if invalid_params:
            self.msg = "Invalid parameters in playbook: {0}".format(invalid_params)
            self.set_operation_result("failed", False, self.msg, "ERROR")
            return self
        
        self.log("Validating minimum requirements against provided config: {0}".format(self.config), "DEBUG")
        self.validate_minimum_requirements(self.config)

        # Set the validated configuration and update the result with success status
        self.validated_config = valid_temp
        self.msg = "Successfully validated playbook configuration parameters using 'validated_input': {0}".format(
            str(valid_temp)
        )
        self.set_operation_result("success", False, self.msg, "INFO")
        return self

    def get_workflow_filters_schema(self):
        """
        Description: Returns the schema for workflow filters supported by the module.
        Returns:
            dict: A dictionary representing the schema for workflow filters.
        """
        self.log("Inside get_workflow_filters_schema function.", "DEBUG")
        return {
            "network_elements": {
                "inventory_workflow_manager": {
                    "filters" : ["ip_address", "hostname", "serial_number", "role"],
                    "api_function":"get_device_list",
                    "api_family": "devices",
                    "reverse_mapping_function": self.inventory_get_device_reverse_mapping,
                    "get_function_name": self.get_inventory_workflow_manager_details,  
                }
            },
            "global_filters": {
                "ip_address_list": {
                    "type": "list",
                    "required": False,
                    "elements": "str",
                    "validate_ip": True,
                },
                "hostname_list": {"type": "list", "required": False, "elements": "str"},
                "serial_number_list": {
                    "type": "list",
                    "required": False,
                    "elements": "str",
                },
            },
            "component_specific_filters": {
                "inventory_workflow_manager": {
                  "type": {
                    "type": "str",
                    "required": False,
                    "choices": ["NETWORK_DEVICE", "COMPUTE_DEVICE", "MERAKI_DASHBOARD", 
                               "THIRD_PARTY_DEVICE", "FIREPOWER_MANAGEMENT_SYSTEM"]
                  },
                  "role": {
                    "type": "str",
                    "required": False,
                    "choices": ["ACCESS", "CORE", "DISTRIBUTION", "BORDER_ROUTER", "UNKNOWN"]
                  },
                  "snmp_version": {
                    "type": "str",
                    "required": False,
                    "choices": ["v2", "v2c", "v3"]
                  },
                  "cli_transport": {
                    "type": "str",
                    "required": False,
                    "choices": ["ssh", "telnet", "SSH", "TELNET"]
                  }
                }
            }
        }

    def process_global_filters(self, global_filters):
        """
        Process global filters to retrieve device information from Cisco Catalyst Center.
        
        Args:
            global_filters (dict): Dictionary containing ip_address_list, hostname_list, or serial_number_list
            
        Returns:
            dict: Dictionary containing device_ip_to_id_mapping with device details
        """
        self.log("Starting process_global_filters with filters: {0}".format(global_filters), "DEBUG")
        
        device_ip_to_id_mapping = {}
        
        try:
            # Extract filter lists
            ip_address_list = global_filters.get("ip_address_list", [])
            hostname_list = global_filters.get("hostname_list", [])
            serial_number_list = global_filters.get("serial_number_list", [])
            
            self.log(
                "Extracted filters - IPs: {0}, Hostnames: {1}, Serials: {2}".format(
                    len(ip_address_list), len(hostname_list), len(serial_number_list)
                ),
                "INFO",
            )
            
            # If no filters provided, return empty mapping
            # The calling function will handle retrieving all devices
            if not ip_address_list and not hostname_list and not serial_number_list:
                self.log("No specific filters provided", "DEBUG")
                return {"device_ip_to_id_mapping": {}}
            
            # Process IP address filters
            if ip_address_list:
                self.log("Processing {0} IP addresses".format(len(ip_address_list)), "INFO")
                for ip_address in ip_address_list:
                    try:
                        self.log("Fetching device details for IP: {0}".format(ip_address), "DEBUG")
                        response = self.dnac._exec(
                            family="devices",
                            function="get_network_device_by_ip",
                            params={"ip_address": ip_address}
                        )
                        
                        if response and response.get("response"):
                            device_info = response["response"]
                            device_ip = device_info.get("managementIpAddress") or device_info.get("ipAddress")
                            if device_ip:
                                device_ip_to_id_mapping[device_ip] = device_info
                                self.log("Added device with IP: {0}".format(device_ip), "DEBUG")
                        else:
                            self.log("No device found for IP: {0}".format(ip_address), "WARNING")
                            
                    except Exception as e:
                        self.log("Error fetching device by IP {0}: {1}".format(ip_address, str(e)), "ERROR")
            
            # Process hostname filters
            if hostname_list:
                self.log("Processing {0} hostnames".format(len(hostname_list)), "INFO")
                for hostname in hostname_list:
                    try:
                        self.log("Fetching device details for hostname: {0}".format(hostname), "DEBUG")
                        response = self.dnac._exec(
                            family="devices",
                            function="get_device_list",
                            params={"hostname": hostname}
                        )
                        
                        if response and response.get("response"):
                            devices = response["response"]
                            for device_info in devices:
                                device_ip = device_info.get("managementIpAddress") or device_info.get("ipAddress")
                                if device_ip:
                                    device_ip_to_id_mapping[device_ip] = device_info
                                    self.log("Added device with hostname: {0}, IP: {1}".format(hostname, device_ip), "DEBUG")
                        else:
                            self.log("No device found for hostname: {0}".format(hostname), "WARNING")
                            
                    except Exception as e:
                        self.log("Error fetching device by hostname {0}: {1}".format(hostname, str(e)), "ERROR")
            
            # Process serial number filters
            if serial_number_list:
                self.log("Processing {0} serial numbers".format(len(serial_number_list)), "INFO")
                for serial_number in serial_number_list:
                    try:
                        self.log("Fetching device details for serial: {0}".format(serial_number), "DEBUG")
                        response = self.dnac._exec(
                            family="devices",
                            function="get_device_list",
                            params={"serial_number": serial_number}
                        )
                        
                        if response and response.get("response"):
                            devices = response["response"]
                            for device_info in devices:
                                device_ip = device_info.get("managementIpAddress") or device_info.get("ipAddress")
                                if device_ip:
                                    device_ip_to_id_mapping[device_ip] = device_info
                                    self.log("Added device with serial: {0}, IP: {1}".format(serial_number, device_ip), "DEBUG")
                        else:
                            self.log("No device found for serial number: {0}".format(serial_number), "WARNING")
                            
                    except Exception as e:
                        self.log("Error fetching device by serial {0}: {1}".format(serial_number, str(e)), "ERROR")
        
            self.log(
                "Completed process_global_filters. Found {0} unique devices".format(
                    len(device_ip_to_id_mapping)
                ),
                "INFO",
            )
            return {"device_ip_to_id_mapping": device_ip_to_id_mapping}
        
        except Exception as e:
            self.log("Error in process_global_filters: {0}".format(str(e)), "ERROR")
            return {"device_ip_to_id_mapping": {}}

    def inventory_get_device_reverse_mapping(self):
        """
        Returns reverse mapping specification for inventory devices.
        Transforms API response from Catalyst Center to inventory_workflow_manager format.
        Maps device attributes from API response to playbook configuration structure.
        All field names are in snake_case format.
        Includes ONLY fields present in the actual API response.
        """
        return OrderedDict({
            # Device Type and Classification
            "device_type": {
                "type": "str",
                "source_key": "type",
                "transform": lambda x: x if x else None
            },
            "family": {
                "type": "str",
                "source_key": "family",
                "transform": lambda x: x if x else None
            },
            "series": {
                "type": "str",
                "source_key": "series",
                "transform": lambda x: x if x else None
            },
            "role": {
                "type": "str",
                "source_key": "role",
                "transform": lambda x: x if x else None
            },
            "role_source": {
                "type": "str",
                "source_key": "roleSource",
                "transform": lambda x: x if x else None
            },
            
            # Device Identification
            "hostname": {
                "type": "str",
                "source_key": "hostname",
                "transform": lambda x: x if x else None
            },
            "management_ip_address": {
                "type": "str",
                "source_key": "managementIpAddress",
                "transform": lambda x: x if x else None
            },
            "serial_number": {
                "type": "str",
                "source_key": "serialNumber",
                "transform": lambda x: x if x else None
            },
            "mac_address": {
                "type": "str",
                "source_key": "macAddress",
                "transform": lambda x: x if x else None
            },
            "platform_id": {
                "type": "str",
                "source_key": "platformId",
                "transform": lambda x: x if x else None
            },
            "device_id": {
                "type": "str",
                "source_key": "id",
                "transform": lambda x: x if x else None
            },
            "instance_uuid": {
                "type": "str",
                "source_key": "instanceUuid",
                "transform": lambda x: x if x else None
            },
            "instance_tenant_id": {
                "type": "str",
                "source_key": "instanceTenantId",
                "transform": lambda x: x if x else None
            },
            
            # Software Information
            "software_type": {
                "type": "str",
                "source_key": "softwareType",
                "transform": lambda x: x if x else None
            },
            "software_version": {
                "type": "str",
                "source_key": "softwareVersion",
                "transform": lambda x: x if x else None
            },
            "description": {
                "type": "str",
                "source_key": "description",
                "transform": lambda x: x if x else None
            },
            
            # Device Status and Management
            "device_support_level": {
                "type": "str",
                "source_key": "deviceSupportLevel",
                "transform": lambda x: x if x else None
            },
            "reachability_status": {
                "type": "str",
                "source_key": "reachabilityStatus",
                "transform": lambda x: x if x else None
            },
            "reachability_failure_reason": {
                "type": "str",
                "source_key": "reachabilityFailureReason",
                "transform": lambda x: x if x else None
            },
            "collection_status": {
                "type": "str",
                "source_key": "collectionStatus",
                "transform": lambda x: x if x else None
            },
            "collection_interval": {
                "type": "str",
                "source_key": "collectionInterval",
                "transform": lambda x: x if x else None
            },
            "management_state": {
                "type": "str",
                "source_key": "managementState",
                "transform": lambda x: x if x else None
            },
            "managed_atleast_once": {
                "type": "bool",
                "source_key": "managedAtleastOnce",
                "transform": lambda x: x if isinstance(x, bool) else None
            },
            
            # Inventory and Sync Status
            "inventory_status_detail": {
                "type": "str",
                "source_key": "inventoryStatusDetail",
                "transform": lambda x: x if x else None
            },
            "last_update_time": {
                "type": "int",
                "source_key": "lastUpdateTime",
                "transform": lambda x: x if x else None
            },
            "last_updated": {
                "type": "str",
                "source_key": "lastUpdated",
                "transform": lambda x: x if x else None
            },
            "last_managed_resync_reasons": {
                "type": "str",
                "source_key": "lastManagedResyncReasons",
                "transform": lambda x: x if x else None
            },
            "last_device_resync_start_time": {
                "type": "str",
                "source_key": "lastDeviceResyncStartTime",
                "transform": lambda x: x if x else None
            },
            "reasons_for_device_resync": {
                "type": "str",
                "source_key": "reasonsForDeviceResync",
                "transform": lambda x: x if x else None
            },
            "reasons_for_pending_sync_requests": {
                "type": "str",
                "source_key": "reasonsForPendingSyncRequests",
                "transform": lambda x: x if x else None
            },
            "pending_sync_requests_count": {
                "type": "str",
                "source_key": "pendingSyncRequestsCount",
                "transform": lambda x: x if x else None
            },
            "sync_requested_by_app": {
                "type": "str",
                "source_key": "syncRequestedByApp",
                "transform": lambda x: x if x else None
            },
            
            # Network Information
            "dns_resolved_management_address": {
                "type": "str",
                "source_key": "dnsResolvedManagementAddress",
                "transform": lambda x: x if x else None
            },
            
            # Device Hardware Details
            "memory_size": {
                "type": "str",
                "source_key": "memorySize",
                "transform": lambda x: x if x else None
            },
            "line_card_count": {
                "type": "str",
                "source_key": "lineCardCount",
                "transform": lambda x: x if x else None
            },
            "line_card_id": {
                "type": "str",
                "source_key": "lineCardId",
                "transform": lambda x: x if x else None
            },
            "interface_count": {
                "type": "str",
                "source_key": "interfaceCount",
                "transform": lambda x: x if x else None
            },
            
            # Device Uptime
            "up_time": {
                "type": "str",
                "source_key": "upTime",
                "transform": lambda x: x if x else None
            },
            "uptime_seconds": {
                "type": "int",
                "source_key": "uptimeSeconds",
                "transform": lambda x: int(x) if x else None
            },
            "boot_date_time": {
                "type": "str",
                "source_key": "bootDateTime",
                "transform": lambda x: x if x else None
            },
            
            # SNMP Information
            "snmp_contact": {
                "type": "str",
                "source_key": "snmpContact",
                "transform": lambda x: x if x else None
            },
            "snmp_location": {
                "type": "str",
                "source_key": "snmpLocation",
                "transform": lambda x: x if x else None
            },
            
            # Location Information
            "location": {
                "type": "str",
                "source_key": "location",
                "transform": lambda x: x if x else None
            },
            "location_name": {
                "type": "str",
                "source_key": "locationName",
                "transform": lambda x: x if x else None
            },
            
            # Vendor Information
            "vendor": {
                "type": "str",
                "source_key": "vendor",
                "transform": lambda x: x if x else None
            },
            
            # Wireless/AP Related Fields (null in your example but present in API)
            "ap_manager_interface_ip": {
                "type": "str",
                "source_key": "apManagerInterfaceIp",
                "transform": lambda x: x if x else None
            },
            "associated_wlc_ip": {
                "type": "str",
                "source_key": "associatedWlcIp",
                "transform": lambda x: x if x else None
            },
            "ap_ethernet_mac_address": {
                "type": "str",
                "source_key": "apEthernetMacAddress",
                "transform": lambda x: x if x else None
            },
            
            # Error Information
            "error_code": {
                "type": "str",
                "source_key": "errorCode",
                "transform": lambda x: x if x else None
            },
            "error_description": {
                "type": "str",
                "source_key": "errorDescription",
                "transform": lambda x: x if x else None
            },
            
            # Additional Fields
            "tag_count": {
                "type": "str",
                "source_key": "tagCount",
                "transform": lambda x: x if x else None
            },
            "tunnel_udp_port": {
                "type": "str",
                "source_key": "tunnelUdpPort",
                "transform": lambda x: x if x else None
            },
            "waas_device_mode": {
                "type": "str",
                "source_key": "waasDeviceMode",
                "transform": lambda x: x if x else None
            }
        })

    def transform_ip_address_list(self, api_value):
        """
        Transform API ipAddress to ip_address_list format.
        Ensures it's always returned as a list.
        """
        if not api_value:
            return []
        if isinstance(api_value, list):
            return api_value
        return [api_value]

    def get_inventory_workflow_manager_details(self, network_element, filters):
        """
        Retrieves inventory device credentials from Cisco Catalyst Center API.
        Processes the response and transforms it using the reverse mapping specification.
        Captures FULL device response with all available fields.
        """
        self.log("Starting get_inventory_workflow_manager_details", "INFO")
        
        try:
            reverse_mapping_spec = self.inventory_get_device_reverse_mapping()
            
            global_filters = filters.get("global_filters", {})
            component_specific_filters = filters.get("component_specific_filters", {})
            generate_all = filters.get("generate_all_configurations", False)
            
            self.log("Filters received - Global: {0}, Component: {1}, Generate All: {2}".format(
                global_filters, component_specific_filters, generate_all
            ), "DEBUG")
            
            device_response = []
            
            # Step 1: Get devices from API with FULL details
            if generate_all:
                self.log("Retrieving all devices from Catalyst Center with full details", "INFO")
                try:
                    # Use get_device_list to get ALL devices with complete response
                    response = self.dnac._exec(
                        family="devices",
                        function="get_device_list",
                        op_modifies=False,
                        params={}
                    )
                    
                    if response and "response" in response:
                        devices = response.get("response", [])
                        self.log("Retrieved {0} devices from get_device_list".format(len(devices)), "INFO")
                        
                        # Log the first device to see all available fields
                        if devices:
                            self.log("Sample device fields from API: {0}".format(list(devices[0].keys())), "INFO")
                            self.log("Sample device full data: {0}".format(devices[0]), "DEBUG")
                        
                        device_response.extend(devices)
                    else:
                        self.log("No devices returned from get_device_list", "WARNING")
                        
                except Exception as e:
                    self.log("Error fetching all devices: {0}".format(str(e)), "ERROR")
                    
            else:
                self.log("Processing global filters", "DEBUG")
                result = self.process_global_filters(global_filters)
                device_ip_to_id_mapping = result.get("device_ip_to_id_mapping", {})
                
                if device_ip_to_id_mapping:
                    self.log("Retrieved {0} devices from global filters".format(len(device_ip_to_id_mapping)), "INFO")
                    
                    # Log the first device to see what fields are available
                    first_device = list(device_ip_to_id_mapping.values())[0] if device_ip_to_id_mapping else None
                    if first_device:
                        self.log("Sample filtered device fields: {0}".format(list(first_device.keys())), "INFO")
                        self.log("Sample filtered device data: {0}".format(first_device), "DEBUG")
                    
                    for device_ip, device_info in device_ip_to_id_mapping.items():
                        device_response.append(device_info)
    
            self.log("Retrieved {0} devices before component filtering".format(len(device_response)), "INFO")
        
            # ✅ Log what fields are actually available in the device_response
            if device_response:
                sample_device = device_response[0]
                available_fields = list(sample_device.keys())
                self.log("Available fields in device response: {0}".format(available_fields), "INFO")
                self.log("Total fields available: {0}".format(len(available_fields)), "INFO")
                
                # Check which fields from reverse_mapping_spec are missing
                missing_fields = []
                for playbook_key, mapping_spec in reverse_mapping_spec.items():
                    source_key = mapping_spec.get("source_key")
                    if source_key and source_key not in sample_device:
                        missing_fields.append(source_key)
                
                if missing_fields:
                    self.log("WARNING: {0} fields from reverse_mapping_spec are NOT in API response: {1}".format(
                        len(missing_fields), missing_fields
                    ), "WARNING")
                else:
                    self.log("All fields from reverse_mapping_spec are present in API response", "INFO")
            
                # Step 2: Apply component-specific filters (type, role, snmp_version, cli_transport)
                if component_specific_filters:
                    self.log("Applying component-specific filters: {0}".format(component_specific_filters), "DEBUG")
                    device_response = self.apply_component_specific_filters(device_response, component_specific_filters)
                    self.log("After component filtering: {0} devices remain".format(len(device_response)), "INFO")
                else:
                    self.log("No component-specific filters to apply", "DEBUG")
                
                if not device_response:
                    self.log("No devices found matching all filters", "WARNING")
                    return []
                
                # Step 3: Transform devices to playbook format
                self.log("Transforming {0} devices to playbook format".format(len(device_response)), "INFO")
                transformed_devices = self.transform_device_to_playbook_format(
                    reverse_mapping_spec, device_response
                )
                
                self.log("Devices transformed successfully: {0} configurations".format(len(transformed_devices)), "INFO")
                return transformed_devices
        
        except Exception as e:
            self.log("Error in get_inventory_workflow_manager_details: {0}".format(str(e)), "ERROR")
            import traceback
            self.log("Traceback: {0}".format(traceback.format_exc()), "ERROR")
            return []

    def yaml_config_generator(self, yaml_config_generator):
        """
        Generates a YAML configuration file based on the provided parameters.
        This function retrieves network element details using global and component-specific filters, processes the data,
        and writes the YAML content to a specified file. It dynamically handles multiple network elements and their respective filters.

        Args:
            yaml_config_generator (dict): Contains file_path, global_filters, and component_specific_filters.

        Returns:
            self: The current instance with the operation result and message updated.
        """

        self.log(
            "Starting YAML config generation with parameters: {0}".format(
                yaml_config_generator
            ),
            "DEBUG",
        )

        # Check if generate_all_configurations mode is enabled and store as instance attribute
        # THIS MUST BE DONE FIRST before creating filters
        self.generate_all_configurations = yaml_config_generator.get("generate_all_configurations", False)
        if self.generate_all_configurations:
            self.log("Auto-discovery mode enabled - will process all devices and all features", "INFO")

        self.log("Determining output file path for YAML configuration", "DEBUG")
        file_path = yaml_config_generator.get("file_path")
        if not file_path:
            self.log("No file_path provided by user, generating default filename", "DEBUG")
            file_path = self.generate_filename()
        else:
            self.log("Using user-provided file_path: {0}".format(file_path), "DEBUG")

        self.log("YAML configuration file path determined: {0}".format(file_path), "DEBUG")

        self.log("Initializing filter dictionaries", "DEBUG")
        if self.generate_all_configurations:
            # In generate_all_configurations mode, override any provided filters to ensure we get ALL configurations
            self.log("Auto-discovery mode: Overriding any provided filters to retrieve all devices and all features", "INFO")
            if yaml_config_generator.get("global_filters"):
                self.log("Warning: global_filters provided but will be ignored due to generate_all_configurations=True", "WARNING")
            if yaml_config_generator.get("component_specific_filters"):
                self.log("Warning: component_specific_filters provided but will be ignored due to generate_all_configurations=True", "WARNING")
            
            # Set empty filters to retrieve everything
            global_filters = {}
            component_specific_filters = {}
        else:
            # Use provided filters or default to empty
            global_filters = yaml_config_generator.get("global_filters") or {}
            component_specific_filters = yaml_config_generator.get("component_specific_filters") or {}

        self.log(
            "Global filters determined: {0}".format(global_filters),
            "DEBUG",
        )
        self.log(
            "Component-specific filters determined: {0}".format(
                component_specific_filters
            ),
            "DEBUG",
        )

        self.log("Retrieving module-supported network elements", "DEBUG")
        module_supported_network_elements = self.module_schema.get(
            "network_elements", {}
        )

        self.log(
            "Retrieved {0} supported network elements: {1}".format(
                len(module_supported_network_elements),
                list(module_supported_network_elements.keys()),
            ),
            "DEBUG",
        )

        components_list = component_specific_filters.get(
            "components_list", module_supported_network_elements.keys()
        )

        self.log(
            "Components list determined: {0}".format(components_list), "DEBUG"
        )

        final_list = []
        for component in components_list:
            network_element = module_supported_network_elements.get(component)
            if not network_element:
                self.log(
                    "Skipping unsupported network element: {0}".format(component),
                    "WARNING",
                )
                continue

            # Create filters dictionary properly with both global and component-specific filters
            # Include generate_all_configurations flag in the filters
            filters = {
                "global_filters": global_filters,
                "component_specific_filters": component_specific_filters.get(component, {}),
                "generate_all_configurations": self.generate_all_configurations
            }
            
            self.log("Processing component {0} with filters: {1}".format(component, filters), "DEBUG")
            
            operation_func = network_element.get("get_function_name")
            if callable(operation_func):
                details = operation_func(network_element, filters)
                self.log(
                    "Details retrieved for {0}: {1}".format(component, details), "DEBUG"
                )
                # Details is already a list with one consolidated config dict
                # Extend instead of append to flatten the structure
                if details:
                    final_list.extend(details)

        self.log(
            "Completed processing all components. Total configurations: {0}".format(
                len(final_list)
            ),
            "INFO",
        )

        final_dict = {"config": final_list}
        
        self.log("Final dictionary created: {0}".format(final_dict), "DEBUG")

        self.log("Writing final dictionary to file: {0}".format(file_path), "INFO")
        write_result = self.write_dict_to_yaml(final_dict, file_path)
        if write_result:
            self.msg = {
                "YAML config generation Task succeeded for module '{0}'.".format(
                    self.module_name
                ): {"file_path": file_path}
            }
            self.set_operation_result("success", True, self.msg, "INFO")
        else:
            self.msg = {
                "YAML config generation Task failed for module '{0}'.".format(
                    self.module_name
                ): {"file_path": file_path}
            }
            self.set_operation_result("failed", True, self.msg, "ERROR")

        return self


    def get_diff_gathered(self):
        """
        Executes YAML configuration file generation for brownfield Inventory workflow.

        Processes the desired state parameters prepared by get_want() and generates a
        YAML configuration file containing network element details from Catalyst Center.
        This method orchestrates the yaml_config_generator operation and tracks execution
        time for performance monitoring.
        """


        start_time = time.time()
        self.log("Starting 'get_diff_gathered' operation.", "DEBUG")
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
        self.log("Beginning iteration over defined workflow operations for processing.", "DEBUG")
        for index, (param_key, operation_name, operation_func) in enumerate(
            workflow_operations, start=1
        ):
            self.log(
                "Iteration {0}: Checking parameters for {1} operation with param_key '{2}'.".format(
                    index, operation_name, param_key
                ),
                "DEBUG",
            )
            params = self.want.get(param_key)
            if params:
                self.log(
                    "Iteration {0}: Parameters found for {1}. Starting processing.".format(
                        index, operation_name
                    ),
                    "INFO",
                )

                try:
                    operation_func(params).check_return_status()
                    operations_executed += 1
                    self.log(
                        "{0} operation completed successfully".format(operation_name),
                        "DEBUG"
                    )
                except Exception as e:
                    self.log(
                        "{0} operation failed with error: {1}".format(operation_name, str(e)),
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
                    "Iteration {0}: No parameters found for {1}. Skipping operation.".format(
                        index, operation_name
                    ),
                    "WARNING",
                )

        end_time = time.time()
        self.log(
            "Completed 'get_diff_gathered' operation in {0:.2f} seconds.".format(
                end_time - start_time
            ),
            "DEBUG",
        )

        return self

    def transform_device_to_playbook_format(self, reverse_mapping_spec, device_response):
        """
        Transforms raw device data from Catalyst Center to playbook format using reverse mapping spec.
        Creates INDIVIDUAL configuration for each device (not consolidated).
        
        Args:
            reverse_mapping_spec (OrderedDict): Mapping specification for transformation
            device_response (list): List of raw device dictionaries from API
            
        Returns:
            list: List of individual device dictionaries in playbook format (one per device)
        """
        transformed_devices = []
        
        self.log("Starting transformation of {0} devices into INDIVIDUAL configurations".format(
            len(device_response)
        ), "INFO")
        
        for device_index, device in enumerate(device_response):
            self.log("Processing device {0}/{1}: {2}".format(
                device_index + 1, 
                len(device_response), 
                device.get('hostname', 'Unknown')
            ), "DEBUG")
            
            self.log("Available fields in device response: {0}".format(list(device.keys())), "INFO")
            self.log("Full device data: {0}".format(device), "DEBUG")
            
            # Create individual device configuration
            device_config = {}
            
            for playbook_key, mapping_spec in reverse_mapping_spec.items():
                source_key = mapping_spec.get("source_key")
                transform_func = mapping_spec.get("transform")
                
                try:
                    # Get the value from the source device data
                    if source_key:
                        api_value = device.get(source_key)
                        self.log(
                            "Mapping {0} from source_key '{1}': value={2}".format(
                                playbook_key, source_key, api_value
                            ),
                            "DEBUG"
                        )
                    else:
                        api_value = None
                        self.log(
                            "No source_key for {0}, using default transform".format(playbook_key),
                            "DEBUG"
                        )
                    
                    # Apply transformation function
                    if transform_func and callable(transform_func):
                        transformed_value = transform_func(api_value)
                    else:
                        transformed_value = api_value
                    
                    # Add to device configuration
                    device_config[playbook_key] = transformed_value
                    
                    self.log(
                        "Transformed {0}: {1} -> {2}".format(
                            playbook_key, api_value, transformed_value
                        ),
                        "DEBUG"
                    )
                    
                except Exception as e:
                    self.log(
                        "Error transforming {0}: {1}".format(playbook_key, str(e)),
                        "ERROR"
                    )
                    device_config[playbook_key] = None
        
            # Add device config AFTER processing all fields (OUTSIDE inner loop)
            transformed_devices.append(device_config)
            self.log("Device {0} ({1}) transformation complete and added to list".format(
                device_index + 1, device.get('hostname', 'Unknown')
            ), "INFO")
        
    
        self.log("Transformation complete. Created {0} individual device configurations".format(
            len(transformed_devices)
        ), "INFO")
        
        return transformed_devices

    def apply_component_specific_filters(self, devices, component_filters):
        """
        Apply component-specific filters to device list after API retrieval.
        Handles filters that can be:
        - Single dict: {role: "ACCESS"}
        - List of single dict: [{role: "ACCESS"}]
        - List of multiple dicts: [{role: "ACCESS"}, {role: "CORE"}]
        
        Multiple filter dicts use OR logic (device matches ANY filter set).
        
        Args:
            devices (list): List of device dictionaries from API
            component_filters (dict or list): Filters like type, role, snmp_version, cli_transport
                                             Can be nested dict or list of filter dicts
                
        Returns:
            list: Filtered device list
        """
        if not component_filters:
            self.log("No component filters provided, returning all devices", "INFO")
            return devices
        
        self.log("Component filters received: {0}".format(component_filters), "DEBUG")
        
        # Normalize component_filters to a list of filter dicts
        filter_list = []
        
        if isinstance(component_filters, list):
            # Already a list
            filter_list = component_filters
            self.log("Component filters is a list with {0} filter set(s)".format(len(filter_list)), "DEBUG")
        elif isinstance(component_filters, dict):
            # Convert single dict to list
            filter_list = [component_filters]
            self.log("Component filters is a dict, converted to list with 1 filter set", "DEBUG")
        else:
            self.log("Component filters is not dict or list, returning all devices", "WARNING")
            return devices
        
        if not filter_list:
            self.log("Component filters list is empty, returning all devices", "INFO")
            return devices
        
        # Validate and clean filter list
        valid_filters = []
        for idx, filter_item in enumerate(filter_list):
            if isinstance(filter_item, dict):
                valid_filters.append(filter_item)
            else:
                self.log("Filter item {0} is not a dict, skipping: {1}".format(idx, filter_item), "WARNING")
        
        if not valid_filters:
            self.log("No valid filter dicts found, returning all devices", "WARNING")
            return devices
        
        self.log("Processing {0} filter set(s) with OR logic".format(len(valid_filters)), "INFO")
        
        filtered_devices = []
        devices_matched_filters = set()  # Track which devices matched any filter
    
        # Process each filter set (OR logic - device matches ANY filter set)
        for filter_idx, filter_criteria in enumerate(valid_filters):
            self.log("Processing filter set {0}/{1}: {2}".format(
                filter_idx + 1, len(valid_filters), filter_criteria
            ), "INFO")
            
            # Extract filter criteria from this filter set
            device_type = filter_criteria.get("type")
            device_role = filter_criteria.get("role")
            snmp_version = filter_criteria.get("snmp_version")
            cli_transport = filter_criteria.get("cli_transport")
            
            self.log("Filter set {0} - type: {1}, role: {2}, snmp: {3}, cli: {4}".format(
                filter_idx + 1, device_type, device_role, snmp_version, cli_transport
            ), "DEBUG")
            
            # If no actual filter values provided in this set, skip it
            if not any([device_type, device_role, snmp_version, cli_transport]):
                self.log("Filter set {0} has no filter values, skipping".format(filter_idx + 1), "DEBUG")
                continue
            
            # Check each device against THIS filter set
            for device in devices:
                # Skip if device already matched a previous filter set
                device_id = device.get("id", device.get("instanceUuid", ""))
                if device_id in devices_matched_filters:
                    continue
                
                device_hostname = device.get("hostname", "Unknown")
                device_matched = True
                
                # Check device type (AND logic within filter set)
                if device_type:
                    device_type_value = device.get("type")
                    if not device_type_value or device_type_value.upper() != device_type.upper():
                        self.log("Device {0}: type MISMATCH (filter: {1}, device: {2})".format(
                            device_hostname, device_type, device_type_value
                        ), "DEBUG")
                        device_matched = False
                    else:
                        self.log("Device {0}: type MATCH ({1})".format(device_hostname, device_type_value), "DEBUG")
                
                # Check device role (AND logic within filter set)
                if device_role and device_matched:
                    device_role_value = device.get("role")
                    
                    self.log("Device {0}: role check - Filter: '{1}', Device: '{2}'".format(
                        device_hostname, device_role, device_role_value
                    ), "DEBUG")
                    
                    # Handle None or empty role
                    if not device_role_value or device_role_value == "":
                        if device_role.upper() not in ["UNKNOWN", ""]:
                            self.log("Device {0}: role MISMATCH - device role is None/empty (filter: {1})".format(
                                device_hostname, device_role
                            ), "DEBUG")
                            device_matched = False
                        else:
                            self.log("Device {0}: role MATCH - both are UNKNOWN/empty".format(device_hostname), "DEBUG")
                    # Compare roles (case-insensitive)
                    elif device_role_value.upper() == device_role.upper():
                        self.log("Device {0}: role MATCH ({1})".format(device_hostname, device_role_value), "DEBUG")
                    else:
                        self.log("Device {0}: role MISMATCH (filter: {1}, device: {2})".format(
                            device_hostname, device_role, device_role_value
                        ), "DEBUG")
                        device_matched = False
                
                # Check SNMP version (AND logic within filter set)
                if snmp_version and device_matched:
                    device_snmp = device.get("snmpVersion", "")
                    normalized_filter = snmp_version.lower().replace("v2c", "v2")
                    normalized_device = device_snmp.lower().replace("v2c", "v2")
                    
                    if normalized_device == normalized_filter:
                        self.log("Device {0}: SNMP MATCH ({1})".format(device_hostname, device_snmp), "DEBUG")
                    else:
                        self.log("Device {0}: SNMP MISMATCH (filter: {1}, device: {2})".format(
                            device_hostname, snmp_version, device_snmp
                        ), "DEBUG")
                        device_matched = False
                
                # Check CLI transport (AND logic within filter set)
                if cli_transport and device_matched:
                    device_cli = device.get("cliTransport", "")
                    if device_cli.lower() == cli_transport.lower():
                        self.log("Device {0}: CLI transport MATCH ({1})".format(device_hostname, device_cli), "DEBUG")
                    else:
                        self.log("Device {0}: CLI transport MISMATCH (filter: {1}, device: {2})".format(
                            device_hostname, cli_transport, device_cli
                        ), "DEBUG")
                        device_matched = False
                
                # If device passed ALL criteria in THIS filter set, mark it as matched
                if device_matched:
                    devices_matched_filters.add(device_id)
                    self.log("Device {0} PASSED filter set {1} criteria".format(
                        device_hostname, filter_idx + 1
                    ), "DEBUG")
    
        # Collect all devices that matched ANY filter set
        for device in devices:
            device_id = device.get("id", device.get("instanceUuid", ""))
            if device_id in devices_matched_filters:
                filtered_devices.append(device)
                self.log("Device {0} INCLUDED in result (matched a filter set)".format(
                    device.get("hostname", "Unknown")
                ), "INFO")
        
        self.log("Filtering complete: {0} devices matched from {1} total across {2} filter set(s)".format(
            len(filtered_devices), len(devices), len(valid_filters)
        ), "INFO")
        
        return filtered_devices

def main():
    """main entry point for module execution"""
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
    ccc_inventory_playbook_generator = InventoryPlaybookGenerator(module)
    if (
        ccc_inventory_playbook_generator.compare_dnac_versions(
            ccc_inventory_playbook_generator.get_ccc_version(), "2.3.7.9"
        )
        < 0
    ):
        ccc_inventory_playbook_generator.msg = (
            "The specified version '{0}' does not support the YAML Playbook generation "
            "for INVENTORY Module. Supported versions start from '2.3.7.9' onwards. ".format(
                ccc_inventory_playbook_generator.get_ccc_version()
            )
        )
        ccc_inventory_playbook_generator.set_operation_result(
            "failed", False, ccc_inventory_playbook_generator.msg, "ERROR"
        ).check_return_status()

    # Get the state parameter from the provided parameters
    state = ccc_inventory_playbook_generator.params.get("state")

    # Check if the state is valid
    if state not in ccc_inventory_playbook_generator.supported_states:
        ccc_inventory_playbook_generator.status = "invalid"
        ccc_inventory_playbook_generator.msg = "State {0} is invalid".format(
            state
        )
        ccc_inventory_playbook_generator.check_recturn_status()

    # Validate the input parameters and check the return statusk
    ccc_inventory_playbook_generator.validate_input().check_return_status()
    # config = ccc_inventory_playbook_generator.validated_config
    # if len(config) == 1 and config[0].get("component_specific_filters") is None:
    #     ccc_inventory_playbook_generator.msg = (
    #         "No valid configurations found in the provided parameters."
    #     )
    #     ccc_inventory_playbook_generator.validated_config = [
    #         {
    #             'component_specific_filters':
    #             {
    #                 'components_list': []
    #             }
    #         }
    #     ]

    # Iterate over the validated configuration parameters
    for config in ccc_inventory_playbook_generator.validated_config:
        ccc_inventory_playbook_generator.reset_values()
        ccc_inventory_playbook_generator.get_want(
            config, state
        ).check_return_status()
        ccc_inventory_playbook_generator.get_diff_state_apply[
            state
        ]().check_return_status()

    module.exit_json(**ccc_inventory_playbook_generator.result)


if __name__ == "__main__":
    main()