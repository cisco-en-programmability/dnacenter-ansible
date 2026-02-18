#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright (c) 2026, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

"""Ansible module to generate YAML configurations for SDA Fabric Devices Workflow Manager Module."""
from __future__ import absolute_import, division, print_function

__metaclass__ = type
__author__ = "Archit Soni, Madhan Sankaranarayanan"

DOCUMENTATION = r"""
---
module: sda_fabric_devices_playbook_config_generator
short_description: Generate YAML configurations playbook for 'sda_fabric_devices_workflow_manager' module.
description:
- Generates YAML configurations compatible with the 'sda_fabric_devices_workflow_manager'
  module, reducing the effort required to manually create Ansible playbooks and
  enabling programmatic modifications.
- Captures SDA fabric device configurations including fabric roles, border settings,
  L2/L3 handoffs, and wireless controller settings from existing deployments.
version_added: 6.49.0
extends_documentation_fragment:
- cisco.dnac.workflow_manager_params
author:
- Archit Soni (@koderchit)
- Madhan Sankaranarayanan (@madhansansel)
options:
  state:
    description: The desired state of Cisco Catalyst Center after module execution.
    type: str
    choices: [gathered]
    default: gathered
  config:
    description:
    - A list of filters for generating YAML playbook compatible with the `sda_fabric_devices_workflow_manager`
      module.
    - Filters specify which components to include in the YAML configuration file.
    - If "components_list" is specified, only those components are included, regardless of the filters.
    type: list
    elements: dict
    required: true
    suboptions:
      generate_all_configurations:
        description:
          - When set to True, automatically generates YAML configurations for all fabric sites and all supported features.
          - This mode discovers all SDA fabric sites in Cisco Catalyst Center and extracts all fabric device configurations.
          - When enabled, the config parameter becomes optional and will use default values if not provided.
          - A default filename will be generated automatically if file_path is not specified.
          - Useful for complete infrastructure discovery and documentation.
        type: bool
        required: false
        default: false
      file_path:
        description:
        - Path where the YAML configuration file will be saved.
        - If not provided, the file will be saved in the current working directory with
          a default file name "sda_fabric_devices_workflow_manager_playbook_<YYYY-MM-DD_HH-MM-SS>.yml".
        - For example, "sda_fabric_devices_workflow_manager_playbook_2026-01-30_19-16-01.yml".
        type: str
        required: false
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
            - Valid values are - "fabric_devices".
            - If specified, only the listed components will be included in the generated YAML file.
            - If not specified, all supported components will be included by default.
            type: list
            elements: str
            choices:
              - fabric_devices
          fabric_devices:
            description:
            - Filters specific to fabric device configuration retrieval.
            - Used to narrow down which fabric sites and devices should be included in the generated YAML file.
            - If no filters are provided, all fabric devices from all fabric sites in Cisco Catalyst Center will be retrieved.
            type: dict
            suboptions:
              fabric_name:
                description:
                - Name of the fabric site to filter by.
                - Retrieves all fabric devices configured in this fabric site.
                - This parameter is required when using fabric_devices filters.
                - Example Global/USA/SAN-JOSE, Global/India/Bangalore.
                type: str
                required: true
              device_ip:
                description:
                - IPv4 address of a specific device to filter by.
                - Retrieves configuration for the specific device within the fabric site.
                - The fabric_name parameter must be provided when using this filter.
                - Example 10.0.0.1, 192.168.1.100.
                type: str
              device_roles:
                description:
                - List of device roles to filter by.
                - Retrieves only devices with the specified fabric roles.
                - The fabric_name parameter must be provided when using this filter.
                - Can be combined with device_ip filter for more specific results.
                type: list
                elements: str
                choices:
                  - CONTROL_PLANE_NODE
                  - EDGE_NODE
                  - BORDER_NODE
                  - WIRELESS_CONTROLLER_NODE
                  - EXTENDED_NODE
requirements:
- dnacentersdk >= 2.4.5
- python >= 3.9
notes:
- Cisco Catalyst Center >= 2.3.7.6
- |-
  SDK Methods used are
  site_design.Sites.get_sites
  sda.SDA.get_fabric_sites
  sda.SDA.get_transit_networks
  sda.SDA.get_fabric_devices
  sda.SDA.get_fabric_devices_layer2_handoffs
  sda.SDA.get_fabric_devices_layer3_handoffs_with_ip_transit
  sda.SDA.get_fabric_devices_layer3_handoffs_with_sda_transit
  fabric_wireless.FabricWireless.get_sda_wireless_details_from_switches
  wireless.Wireless.get_primary_managed_ap_locations_for_specific_wireless_controller
  wireless.Wireless.get_secondary_managed_ap_locations_for_specific_wireless_controller
  devices.Devices.get_device_list
- |-
  SDK Paths used are
  GET /dna/intent/api/v1/sites
  GET /dna/intent/api/v1/sda/fabricSites
  GET /dna/intent/api/v1/sda/transitNetworks
  GET /dna/intent/api/v1/sda/fabricDevices
  GET /dna/intent/api/v1/sda/fabricDevices/layer2Handoffs
  GET /dna/intent/api/v1/sda/fabricDevices/layer3Handoffs/ipTransits
  GET /dna/intent/api/v1/sda/fabricDevices/layer3Handoffs/sdaTransits
  GET /dna/intent/api/v1/sda/fabricSites/{id}/wirelessSettings
  GET /dna/intent/api/v1/wirelessControllers/{networkDeviceId}/managedApLocations/primary
  GET /dna/intent/api/v1/wirelessControllers/{networkDeviceId}/managedApLocations/secondary
  GET /dna/intent/api/v1/network-device
seealso:
- module: cisco.dnac.sda_fabric_devices_workflow_manager
  description: Module for managing SDA fabric devices and their configurations.
"""

EXAMPLES = r"""
# Example 1: Generate all fabric device configurations for all fabric sites
- name: Generate complete SDA fabric devices configuration
  hosts: dnac_servers
  vars_files:
    - credentials.yml
  gather_facts: false
  connection: local
  tasks:
    - name: Generate all SDA fabric device configurations from Cisco Catalyst Center
      cisco.dnac.sda_fabric_devices_playbook_config_generator:
        dnac_host: "{{ dnac_host }}"
        dnac_port: "{{ dnac_port }}"
        dnac_username: "{{ dnac_username }}"
        dnac_password: "{{ dnac_password }}"
        dnac_verify: "{{ dnac_verify }}"
        dnac_debug: "{{ dnac_debug }}"
        dnac_version: "{{ dnac_version }}"
        dnac_log: true
        dnac_log_level: DEBUG
        dnac_log_append: false
        dnac_log_file_path: "{{ dnac_log_file_path }}"
        state: gathered
        config:
          - generate_all_configurations: true

# Example 2: Generate all configurations with custom file path
- name: Generate complete SDA fabric devices configuration with custom filename
  hosts: dnac_servers
  vars_files:
    - credentials.yml
  gather_facts: false
  connection: local
  tasks:
    - name: Generate all SDA fabric device configurations to a specific file
      cisco.dnac.sda_fabric_devices_playbook_config_generator:
        dnac_host: "{{ dnac_host }}"
        dnac_port: "{{ dnac_port }}"
        dnac_username: "{{ dnac_username }}"
        dnac_password: "{{ dnac_password }}"
        dnac_verify: "{{ dnac_verify }}"
        dnac_debug: "{{ dnac_debug }}"
        dnac_version: "{{ dnac_version }}"
        dnac_log: true
        dnac_log_level: DEBUG
        dnac_log_append: false
        dnac_log_file_path: "{{ dnac_log_file_path }}"
        state: gathered
        config:
          - file_path: "/tmp/complete_sda_fabric_devices_config.yaml"
            generate_all_configurations: true

# Example 3: Generate fabric device configurations for a specific fabric site
- name: Generate fabric device configurations for one fabric site
  hosts: dnac_servers
  vars_files:
    - credentials.yml
  gather_facts: false
  connection: local
  tasks:
    - name: Export fabric devices from San Jose fabric
      cisco.dnac.sda_fabric_devices_playbook_config_generator:
        dnac_host: "{{ dnac_host }}"
        dnac_port: "{{ dnac_port }}"
        dnac_username: "{{ dnac_username }}"
        dnac_password: "{{ dnac_password }}"
        dnac_verify: "{{ dnac_verify }}"
        dnac_debug: "{{ dnac_debug }}"
        dnac_version: "{{ dnac_version }}"
        dnac_log: true
        dnac_log_level: DEBUG
        dnac_log_append: false
        dnac_log_file_path: "{{ dnac_log_file_path }}"
        state: gathered
        config:
          - file_path: "/tmp/san_jose_fabric_devices.yaml"
            component_specific_filters:
              components_list: ["fabric_devices"]
              fabric_devices:
                fabric_name: "Global/USA/SAN-JOSE"

# Example 4: Generate configuration for devices with specific roles in a fabric site
- name: Generate configuration for border and control plane devices
  hosts: dnac_servers
  vars_files:
    - credentials.yml
  gather_facts: false
  connection: local
  tasks:
    - name: Export border and control plane fabric devices from San Jose fabric
      cisco.dnac.sda_fabric_devices_playbook_config_generator:
        dnac_host: "{{ dnac_host }}"
        dnac_port: "{{ dnac_port }}"
        dnac_username: "{{ dnac_username }}"
        dnac_password: "{{ dnac_password }}"
        dnac_verify: "{{ dnac_verify }}"
        dnac_debug: "{{ dnac_debug }}"
        dnac_version: "{{ dnac_version }}"
        dnac_log: true
        dnac_log_level: DEBUG
        dnac_log_append: false
        dnac_log_file_path: "{{ dnac_log_file_path }}"
        state: gathered
        config:
          - file_path: "/tmp/border_and_cp_devices.yaml"
            component_specific_filters:
              components_list: ["fabric_devices"]
              fabric_devices:
                fabric_name: "Global/USA/SAN-JOSE"
                device_roles: ["BORDER_NODE", "CONTROL_PLANE_NODE"]

# Example 5: Generate configuration for a specific device in a fabric site
- name: Generate configuration for a specific fabric device
  hosts: dnac_servers
  vars_files:
    - credentials.yml
  gather_facts: false
  connection: local
  tasks:
    - name: Export specific fabric device configuration
      cisco.dnac.sda_fabric_devices_playbook_config_generator:
        dnac_host: "{{ dnac_host }}"
        dnac_port: "{{ dnac_port }}"
        dnac_username: "{{ dnac_username }}"
        dnac_password: "{{ dnac_password }}"
        dnac_verify: "{{ dnac_verify }}"
        dnac_debug: "{{ dnac_debug }}"
        dnac_version: "{{ dnac_version }}"
        dnac_log: true
        dnac_log_level: DEBUG
        dnac_log_append: false
        dnac_log_file_path: "{{ dnac_log_file_path }}"
        state: gathered
        config:
          - file_path: "/tmp/specific_fabric_device.yaml"
            component_specific_filters:
              components_list: ["fabric_devices"]
              fabric_devices:
                fabric_name: "Global/USA/SAN-JOSE"
                device_ip: "10.0.0.1"

# Example 6: Generate multiple configuration files in a single playbook run
- name: Generate multiple SDA fabric device configuration files
  hosts: dnac_servers
  vars_files:
    - credentials.yml
  gather_facts: false
  connection: local
  tasks:
    - name: Generate multiple SDA fabric device configurations
      cisco.dnac.sda_fabric_devices_playbook_config_generator:
        dnac_host: "{{ dnac_host }}"
        dnac_port: "{{ dnac_port }}"
        dnac_username: "{{ dnac_username }}"
        dnac_password: "{{ dnac_password }}"
        dnac_verify: "{{ dnac_verify }}"
        dnac_debug: "{{ dnac_debug }}"
        dnac_version: "{{ dnac_version }}"
        dnac_log: true
        dnac_log_level: DEBUG
        dnac_log_append: false
        dnac_log_file_path: "{{ dnac_log_file_path }}"
        state: gathered
        config:
          - file_path: "/tmp/all_fabric_devices.yaml"
            generate_all_configurations: true
          - file_path: "/tmp/san_jose_only.yaml"
            component_specific_filters:
              components_list: ["fabric_devices"]
              fabric_devices:
                fabric_name: "Global/USA/SAN-JOSE"
          - file_path: "/tmp/bangalore_border_devices.yaml"
            component_specific_filters:
              components_list: ["fabric_devices"]
              fabric_devices:
                fabric_name: "Global/India/Bangalore"
                device_roles: ["BORDER_NODE"]
"""

RETURN = r"""
# Case_1: Success Scenario
response_1:
  description: A dictionary with the response returned by the Cisco Catalyst Center Python SDK
  returned: always
  type: dict
  sample: >
    {
      "response": {
        "status": "success",
        "message": "YAML configuration file generated successfully for module 'sda_fabric_devices_workflow_manager'",
        "file_path": "sda_fabric_devices_workflow_manager_playbook_2026-02-18_11-01-59.yml",
        "configurations_count": 1,
        "components_processed": 1,
        "components_skipped": 0
      },
      "msg": {
        "status": "success",
        "message": "YAML configuration file generated successfully for module 'sda_fabric_devices_workflow_manager'",
        "file_path": "sda_fabric_devices_workflow_manager_playbook_2026-02-18_11-01-59.yml",
        "configurations_count": 1,
        "components_processed": 1,
        "components_skipped": 0
      },
      "status": "success"
    }
# Case_2: Error Scenario
response_2:
  description: A dictionary with the error response returned by the Cisco Catalyst Center Python SDK
  returned: on failure
  type: dict
  sample: >
    {
      "response": "Invalid filters provided for module 'sda_fabric_devices_workflow_manager':
        [\"Filter 'fabric_roles' not valid for component 'fabric_devices'\"]",
      "msg": "Invalid filters provided for module 'sda_fabric_devices_workflow_manager':
        [\"Filter 'fabric_roles' not valid for component 'fabric_devices'\"]"
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


class SdaFabricDevicesPlaybookGenerator(DnacBase, BrownFieldHelper):
    """
    A class for generator playbook files for infrastructure deployed within the Cisco Catalyst Center using the GET APIs.
    """

    values_to_nullify = ["NOT CONFIGURED"]

    def __init__(self, module):
        """
        Initialize the SdaFabricDevicesPlaybookGenerator instance.

        Parameters:
            module (AnsibleModule): The Ansible module instance.

        Returns:
            None

        Description:
            Sets up the generator with schema, site mappings, and transit mappings.
        """
        self.supported_states = ["gathered"]
        super().__init__(module)
        self.log("Initializing SdaFabricDevicesPlaybookGenerator", "INFO")
        self.log(f"Supported states: {self.supported_states}", "DEBUG")

        self.log("Retrieving workflow filters schema", "DEBUG")
        self.module_schema = self.get_workflow_filters_schema()

        self.log("Retrieving site ID to name mapping", "DEBUG")
        self.site_id_name_dict = self.get_site_id_name_mapping()
        self.log(f"Retrieved {len(self.site_id_name_dict)} site(s) in mapping", "DEBUG")

        self.log("Retrieving fabric site name to ID mapping", "DEBUG")
        self.fabric_site_name_to_id_dict, self.fabric_site_id_to_name_dict = (
            self.get_fabric_site_name_to_id_mapping()
        )
        self.log(
            f"Retrieved {len(self.fabric_site_name_to_id_dict)} fabric site(s) in mapping",
            "DEBUG",
        )

        self.log("Retrieving transit ID to name mapping", "DEBUG")
        self.transit_id_to_name_dict = self.get_transit_id_to_name_mapping()
        self.log(
            f"Retrieved {len(self.transit_id_to_name_dict)} transit network(s) in mapping",
            "DEBUG",
        )

        self.module_name = "sda_fabric_devices_workflow_manager"
        self.log(
            "Initialization complete for SdaFabricDevicesPlaybookGenerator", "INFO"
        )

    def validate_input(self):
        """
        Validate input configuration parameters for the playbook.

        Parameters:
            None

        Returns:
            self: Instance with updated msg, status, and validated_config attributes.

        Description:
            Validates config against expected schema and sets validation status.
        """
        self.log("Starting validation of input configuration parameters.", "DEBUG")

        # Check if configuration is available
        if not self.config:
            self.status = "success"
            self.msg = "Configuration is not available in the playbook for validation"
            self.log(self.msg, "WARNING")
            self.log("Exiting validate_input method - no config provided", "DEBUG")
            return self

        self.log(f"Configuration to validate: {len(self.config)} item(s)", "DEBUG")

        # Expected schema for configuration parameters
        temp_spec = {
            "generate_all_configurations": {
                "type": "bool",
                "required": False,
                "default": False,
            },
            "file_path": {"type": "str", "required": False},
            "component_specific_filters": {"type": "dict", "required": False},
        }
        self.log("Expected schema for validation defined", "DEBUG")

        # Validate params
        self.log("Validating configuration parameters against schema", "DEBUG")
        valid_temp, invalid_params = validate_list_of_dicts(self.config, temp_spec)

        if invalid_params:
            self.msg = f"Invalid parameters in playbook: {invalid_params}"
            self.log(self.msg, "ERROR")
            self.set_operation_result("failed", False, self.msg, "ERROR")
            self.log("Exiting validate_input method - validation failed", "DEBUG")
            return self

        # Set the validated configuration and update the result with success status
        self.validated_config = valid_temp
        self.log(
            f"Successfully validated {len(valid_temp)} configuration item(s)", "INFO"
        )
        self.msg = f"Successfully validated playbook configuration parameters using 'validated_input': {str(valid_temp)}"
        self.set_operation_result("success", False, self.msg, "INFO")
        self.log("Exiting validate_input method - validation successful", "DEBUG")
        return self

    def get_transit_id_to_name_mapping(self):
        """
        Retrieve transit networks and create ID to name mapping.

        Parameters:
            None

        Returns:
            dict: Mapping of transit IDs to transit names.

        Description:
            Fetches all transit networks from Catalyst Center and builds a lookup dictionary.
        """

        self.log(
            "Starting transit ID-to-name mapping build (no input parameters)", "INFO"
        )
        transit_id_to_name = {}

        try:
            self.log(
                "Executing API call to get_transit_networks (offset=1, limit=500)",
                "DEBUG",
            )
            response = self.dnac._exec(
                family="sda",
                function="get_transit_networks",
                params={"offset": 1, "limit": 500},
            )

            if not response or not isinstance(response, dict):
                self.log(
                    "Transit networks API returned no data or invalid format",
                    "WARNING",
                )
                self.log(
                    f"Returning transit mapping with {len(transit_id_to_name)} item(s)",
                    "DEBUG",
                )
                return transit_id_to_name

            transits = response.get("response", [])
            self.log(f"API returned {len(transits)} transit network(s)", "DEBUG")

            for idx, transit in enumerate(transits, 1):
                transit_id = transit.get("id")
                transit_name = transit.get("name")
                self.log(
                    f"Processing transit item {idx}/{len(transits)}: id='{transit_id}', name='{transit_name}'",
                    "DEBUG",
                )
                if not transit_id or not transit_name:
                    self.log(
                        f"Transit {idx}/{len(transits)}: Skipping - missing ID or name",
                        "WARNING",
                    )
                    continue

                transit_id_to_name[transit_id] = transit_name
                self.log(
                    f"Transit {idx}/{len(transits)}: Mapped ID '{transit_id}' to name '{transit_name}'",
                    "DEBUG",
                )

            self.log(
                f"Successfully retrieved {len(transit_id_to_name)} transit network(s) for ID to name mapping",
                "INFO",
            )

        except Exception as e:
            self.log(
                f"Transit networks retrieval failed, Error: {str(e)}",
                "ERROR",
            )

        self.log(
            f"Returning transit mapping with {len(transit_id_to_name)} item(s)",
            "DEBUG",
        )
        return transit_id_to_name

    def get_workflow_filters_schema(self):
        """
        Generate the workflow filters schema for fabric devices.

        Parameters:
            None

        Returns:
            dict: Schema containing network elements, filters, and API mappings.

        Description:
            Defines the structure for filtering and retrieving fabric device configurations.
        """
        schema = {
            "network_elements": {
                "fabric_devices": {
                    "filters": {
                        "fabric_name": {"type": "str", "required": True},
                        "device_ip": {
                            "type": "str",
                            "pattern": r"^(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$",
                        },
                        "device_roles": {
                            "type": "list",
                            "choices": [
                                "CONTROL_PLANE_NODE",
                                "EDGE_NODE",
                                "BORDER_NODE",
                                "WIRELESS_CONTROLLER_NODE",
                                "EXTENDED_NODE",
                            ],
                        },
                    },
                    "reverse_mapping_function": self.fabric_devices_temp_spec,
                    "api_function": "get_fabric_devices",
                    "api_family": "sda",
                    "get_function_name": self.get_fabric_devices_configuration,
                },
            },
        }

        network_elements = list(schema["network_elements"].keys())
        self.log(
            f"Workflow filters schema generated successfully with {len(network_elements)} network elements: {network_elements}",
            "INFO",
        )

        return schema

    def fabric_devices_temp_spec(self):
        """
        Generate temporary specification for fabric devices.

        Parameters:
            None

        Returns:
            OrderedDict: Specification defining fabric device structure and transformations.

        Description:
            Creates the mapping spec for transforming API response to playbook format.
        """
        self.log("Entering fabric_devices_temp_spec method", "DEBUG")
        self.log("Generating temporary specification for fabric devices", "INFO")
        fabric_devices = OrderedDict(
            {
                "fabric_name": {
                    "type": "str",
                    "required": True,
                },
                "device_config": {
                    "type": "list",
                    "elements": "dict",
                    "required": True,
                    "special_handling": True,
                    "transform": self.transform_device_config,
                    "device_ip": {
                        "type": "str",
                        "required": True,
                    },
                    "device_roles": {
                        "type": "list",
                        "elements": "str",
                        "source_key": "fabricDeviceRoles",
                    },
                    "wireless_controller_settings": {
                        "type": "dict",
                        "enable": {"type": "bool"},
                        "reload": {"type": "bool", "default": False},
                        "primary_managed_ap_locations": {
                            "type": "list",
                            "elements": "str",
                        },
                        "secondary_managed_ap_locations": {
                            "type": "list",
                            "elements": "str",
                        },
                        "rolling_ap_upgrade": {
                            "type": "dict",
                            "enable": {"type": "bool"},
                            "ap_reboot_percentage": {
                                "type": "int",
                            },
                        },
                    },
                    "borders_settings": {
                        "type": "dict",
                        "layer3_settings": {
                            "type": "dict",
                            "local_autonomous_system_number": {
                                "type": "str",
                                "source_key": "localAutonomousSystemNumber",
                            },
                            "is_default_exit": {
                                "type": "bool",
                                "source_key": "isDefaultExit",
                                "default": True,
                            },
                            "import_external_routes": {
                                "type": "bool",
                                "source_key": "importExternalRoutes",
                                "default": True,
                            },
                            "border_priority": {
                                "type": "int",
                                "source_key": "borderPriority",
                                "default": 10,
                            },
                            "prepend_autonomous_system_count": {
                                "type": "int",
                                "source_key": "prependAutonomousSystemCount",
                                "default": 0,
                            },
                        },
                        "layer3_handoff_ip_transit": {
                            "type": "list",
                            "elements": "dict",
                            "transit_network_name": {
                                "type": "str",
                                "source_key": "transitNetworkName",
                            },
                            "interface_name": {
                                "type": "str",
                                "source_key": "interfaceName",
                            },
                            "external_connectivity_ip_pool_name": {
                                "type": "str",
                            },
                            "virtual_network_name": {
                                "type": "str",
                                "source_key": "virtualNetworkName",
                            },
                            "vlan_id": {
                                "type": "int",
                                "source_key": "vlanId",
                            },
                            "tcp_mss_adjustment": {
                                "type": "int",
                                "source_key": "tcpMssAdjustment",
                            },
                            "local_ip_address": {
                                "type": "str",
                                "source_key": "localIpAddress",
                            },
                            "remote_ip_address": {
                                "type": "str",
                                "source_key": "remoteIpAddress",
                            },
                            "local_ipv6_address": {
                                "type": "str",
                                "source_key": "localIpv6Address",
                            },
                            "remote_ipv6_address": {
                                "type": "str",
                                "source_key": "remoteIpv6Address",
                            },
                        },
                        "layer3_handoff_sda_transit": {
                            "type": "dict",
                            "transit_network_name": {
                                "type": "str",
                                "source_key": "transitNetworkName",
                            },
                            "affinity_id_prime": {
                                "type": "int",
                                "source_key": "affinityIdPrime",
                            },
                            "affinity_id_decider": {
                                "type": "int",
                                "source_key": "affinityIdDecider",
                            },
                            "connected_to_internet": {
                                "type": "bool",
                                "source_key": "connectedToInternet",
                                "default": False,
                            },
                            "is_multicast_over_transit_enabled": {
                                "type": "bool",
                                "source_key": "isMulticastOverTransitEnabled",
                                "default": False,
                            },
                        },
                        "layer2_handoff": {
                            "type": "list",
                            "elements": "dict",
                            "interface_name": {
                                "type": "str",
                                "source_key": "interfaceName",
                            },
                            "internal_vlan_id": {
                                "type": "int",
                                "source_key": "internalVlanId",
                            },
                            "external_vlan_id": {
                                "type": "int",
                                "source_key": "externalVlanId",
                            },
                        },
                    },
                },
            }
        )
        self.log(
            "Temporary specification for fabric devices generated successfully", "DEBUG"
        )
        self.log("Exiting fabric_devices_temp_spec method", "DEBUG")
        return fabric_devices

    def group_fabric_devices_by_fabric_name(self, all_fabric_devices):
        """
        Group fabric devices by their fabric name.

        Parameters:
            all_fabric_devices (list): List of device entries with fabric_name, device_config, device_ip.

        Returns:
            dict: Mapping of fabric_name to list of device entries.

        Description:
            Organizes devices into groups based on their parent fabric site.
        """

        self.log("Entering group_fabric_devices_by_fabric_name method", "DEBUG")
        total_devices = len(all_fabric_devices) if all_fabric_devices else 0
        self.log(
            f"Grouping {total_devices} fabric device(s) by fabric_name",
            "INFO",
        )
        fabric_devices_by_fabric_name = {}

        if not all_fabric_devices:
            self.log(
                "No fabric devices provided for grouping; returning empty mapping",
                "WARNING",
            )
            self.log(
                "Grouping completed (output_fabrics=0, output_devices=0)",
                "DEBUG",
            )
            return fabric_devices_by_fabric_name

        for idx, device_entry in enumerate(all_fabric_devices, 1):
            self.log(
                f"Processing device {idx}/{len(all_fabric_devices)} for grouping",
                "DEBUG",
            )
            fabric_name = device_entry.get("fabric_name")
            device = device_entry.get("device_config")
            device_ip = device_entry.get("device_ip")

            if not fabric_name or not device:
                self.log(
                    f"Skipping device entry {idx} due to missing fabric_name or device_config: {self.pprint(device_entry)}",
                    "WARNING",
                )
                continue

            if fabric_name and device:
                if fabric_name not in fabric_devices_by_fabric_name:
                    self.log(f"Creating new group for fabric: '{fabric_name}'", "DEBUG")
                    fabric_devices_by_fabric_name[fabric_name] = []

                # Store the entire device_entry (includes device_config, device_ip, fabric_name, fabric_id)
                fabric_devices_by_fabric_name[fabric_name].append(device_entry)
                self.log(
                    f"Added device '{device_ip}' to fabric '{fabric_name}' group",
                    "DEBUG",
                )

        output_fabrics = len(fabric_devices_by_fabric_name)
        output_devices = sum(
            len(devices) for devices in fabric_devices_by_fabric_name.values()
        )
        self.log(
            f"Grouping completed (output_fabrics={output_fabrics}, output_devices={output_devices})",
            "INFO",
        )
        self.log(
            f"Grouped fabric names and counts: {dict((fname, len(devices)) for fname, devices in fabric_devices_by_fabric_name.items())}",
            "DEBUG",
        )

        return fabric_devices_by_fabric_name

    def process_fabric_device_for_batch(
        self, device, device_id_to_ip_map, batch_idx, device_idx, total_devices
    ):
        """
        Process a single fabric device and format it for results.

        Parameters:
            device (dict): Device data from API response.
            device_id_to_ip_map (dict): Mapping of device IDs to IP addresses.
            batch_idx (int): Current batch index for logging.
            device_idx (int): Current device index for logging.
            total_devices (int): Total devices in the batch.

        Returns:
            dict: Formatted device with fabric_id, device_config, fabric_name, device_ip.

        Description:
            Formats raw API device data into a standardized structure.
        """
        self.log(
            f"Entering process_fabric_device_for_batch method - batch {batch_idx}, device {device_idx}/{total_devices}",
            "DEBUG",
        )

        network_device_id = device.get("networkDeviceId")
        fabric_id = device.get("fabricId")
        fabric_name = self.fabric_site_id_to_name_dict.get(fabric_id, "Unknown")
        device_ip = (
            device_id_to_ip_map.get(network_device_id) if network_device_id else None
        )

        self.log(
            f"Device details: network_device_id='{network_device_id}', device_ip='{device_ip}', "
            f"fabric_name='{fabric_name}', fabric_id='{fabric_id}'",
            "DEBUG",
        )

        if not device_ip:
            self.log(
                f"Warning: No IP address found for device with network_device_id "
                f"'{network_device_id}' in fabric '{fabric_name}' (fabric_id: '{fabric_id}') in batch {batch_idx}",
                "WARNING",
            )

        formatted_device_response = {
            "fabric_id": device.get("fabricId"),
            "device_config": device,
            "fabric_name": fabric_name,
            "device_ip": device_ip,
        }
        self.log(
            f"Formatted device response ready (fabric_name='{fabric_name}', device_ip='{device_ip}')",
            "DEBUG",
        )
        return formatted_device_response

    def retrieve_all_fabric_devices_from_api(
        self, fabric_devices_params_list_to_query, api_family, api_function
    ):
        """
        Execute API calls to retrieve fabric devices.

        Parameters:
            fabric_devices_params_list_to_query (list): List of query parameter dicts.
            api_family (str): API family name (e.g., 'sda').
            api_function (str): API function name (e.g., 'get_fabric_devices').

        Returns:
            list: Device entries with fabric_id, device_config, fabric_name, device_ip.

        Description:
            Iterates through query params and retrieves all matching fabric devices.
        """
        self.log("Entering retrieve_all_fabric_devices_from_api method", "DEBUG")
        self.log(
            f"Starting API calls to retrieve fabric devices - {len(fabric_devices_params_list_to_query)} query/queries to execute",
            "INFO",
        )
        all_fabric_devices = []

        if not fabric_devices_params_list_to_query:
            self.log(
                "No query parameters provided; returning empty device list",
                "WARNING",
            )
            self.log(
                "Returning fabric device list (count=0)",
                "DEBUG",
            )
            return all_fabric_devices

        for idx, query_params in enumerate(fabric_devices_params_list_to_query, 1):
            self.log(
                f"Executing API call {idx}/{len(fabric_devices_params_list_to_query)} to get fabric device details with params: {self.pprint(query_params)}",
                "DEBUG",
            )

            try:
                response = self.dnac._exec(
                    family=api_family,
                    function=api_function,
                    params=query_params,
                )

                self.log(
                    f"API call {idx} response received: {self.pprint(response)}",
                    "DEBUG",
                )

                if not response or not isinstance(response, dict):
                    self.log(
                        f"API call {idx} returned unexpected response format",
                        "WARNING",
                    )
                    continue

                devices = response.get("response", [])
                if not devices:
                    self.log(
                        f"API call {idx} returned no fabric devices",
                        "DEBUG",
                    )
                    continue

                self.log(
                    f"API call {idx} returned {len(devices)} fabric device(s)",
                    "INFO",
                )

                # Get device IDs for IP mapping
                device_ids_in_batch = [
                    device.get("networkDeviceId")
                    for device in devices
                    if device.get("networkDeviceId")
                ]

                # Get device ID to IP mapping for this batch
                device_id_to_ip_map = {}
                if device_ids_in_batch:
                    self.log(
                        f"Retrieving device IPs for {len(device_ids_in_batch)} device(s) in this batch",
                        "DEBUG",
                    )
                    device_id_to_ip_map = self.get_device_ips_from_device_ids(
                        device_ids_in_batch
                    )
                    self.log(
                        f"Device ID to IP mapping for batch: {self.pprint(device_id_to_ip_map)}",
                        "DEBUG",
                    )
                else:
                    self.log(
                        "No device IDs found in this batch for IP mapping",
                        "WARNING",
                    )

                for device_idx, device in enumerate(devices, 1):
                    formatted_device_response = self.process_fabric_device_for_batch(
                        device,
                        device_id_to_ip_map,
                        idx,
                        device_idx,
                        len(devices),
                    )
                    all_fabric_devices.append(formatted_device_response)

            except Exception as e:
                self.log(
                    f"API call {idx} failed with params {query_params}: {str(e)}",
                    "ERROR",
                )
                continue

        self.log(
            f"Completed fabric devices retrieval (total_devices={len(all_fabric_devices)})",
            "INFO",
        )
        self.log(
            f"Returning fabric device list (count={len(all_fabric_devices)})",
            "DEBUG",
        )

        return all_fabric_devices

    def get_fabric_devices_configuration(self, network_element, filters=None):
        """
        Retrieve and transform fabric devices configuration.

        Parameters:
            network_element (dict): Network element schema with API and transform details.
            filters (dict, optional): Dictionary containing 'component_specific_filters'.
                - component_specific_filters (list/dict): Filters for fabric_name, device_ip, device_roles.

        Returns:
            dict: Dictionary with 'fabric_devices' key containing transformed device configs.

        Description:
            Main function to fetch fabric devices and transform them to playbook format.
        """
        self.log("Entering get_fabric_devices_configuration method", "DEBUG")
        self.log("Starting retrieval of fabric devices configuration", "INFO")

        # Extract component_specific_filters from the filters dict
        # brownfield_helper passes: {"component_specific_filters": [...]}
        component_specific_filters = None
        if filters:
            component_specific_filters = filters.get("component_specific_filters")
            self.log(
                f"Extracted component_specific_filters from filters: {component_specific_filters}",
                "DEBUG",
            )

        if not self.fabric_site_name_to_id_dict:
            self.log("No fabric sites found in Cisco Catalyst Center", "WARNING")
            return {"fabric_devices": []}

        fabric_devices_params_list_to_query = []

        if component_specific_filters:
            self.log(
                "Processing component-specific filters",
                "DEBUG",
            )
            params_for_query = {}

            fabric_name = component_specific_filters.get("fabric_name")
            if fabric_name:
                self.log(f"Applying fabric_name filter: '{fabric_name}'", "DEBUG")
                fabric_site_id = self.fabric_site_name_to_id_dict.get(fabric_name)

                if not fabric_site_id:
                    self.log(
                        f"Fabric site '{fabric_name}' not found in Cisco Catalyst Center.",
                        "WARNING",
                    )
                    return {"fabric_devices": []}

                self.log(
                    f"Fabric site '{fabric_name}' found with fabric_id '{fabric_site_id}'",
                    "DEBUG",
                )
                params_for_query["fabric_id"] = fabric_site_id

            device_ip = component_specific_filters.get("device_ip")
            if device_ip:
                self.log(
                    f"Applying device_ip filter: '{device_ip}'",
                    "DEBUG",
                )
                device_list_params = self.get_device_list_params(
                    ip_address_list=device_ip
                )
                device_info_map = self.get_device_list(device_list_params)
                if not device_info_map or device_ip not in device_info_map:
                    self.log(
                        f"Device with IP '{device_ip}' not found in Cisco Catalyst Center.",
                        "WARNING",
                    )
                    return {"fabric_devices": []}

                network_device_id = device_info_map[device_ip].get("device_id")
                self.log(
                    f"Device with IP '{device_ip}' found with network_device_id '{network_device_id}'",
                    "DEBUG",
                )
                self.log(f"Adding device_id filter: {network_device_id}", "DEBUG")
                params_for_query["networkDeviceId"] = network_device_id

            device_roles = component_specific_filters.get("device_roles")
            if device_roles:
                self.log(
                    f"Applying device_roles filter: {device_roles}",
                    "DEBUG",
                )
                params_for_query["deviceRoles"] = device_roles

            if not params_for_query:
                self.log(
                    "No valid filters provided after processing component-specific filters.",
                    "WARNING",
                )
                return {"fabric_devices": []}

            self.log(
                f"Adding query parameters to list: {params_for_query}",
                "DEBUG",
            )
            fabric_devices_params_list_to_query.append(params_for_query)
        else:
            self.log(
                "No component-specific filters provided. Retrieving all fabric devices from all fabric sites.",
                "INFO",
            )
            for fabric_name, fabric_id in self.fabric_site_name_to_id_dict.items():
                self.log(
                    f"Adding fabric site '{fabric_name}' with fabric_id '{fabric_id}' to query list",
                    "DEBUG",
                )
                fabric_devices_params_list_to_query.append({"fabric_id": fabric_id})

        self.log(
            f"Total fabric device queries to execute: {len(fabric_devices_params_list_to_query)}",
            "INFO",
        )
        # Pretty print the params
        self.log(
            f"Fabric device queries to execute:\n{self.pprint(fabric_devices_params_list_to_query)}",
            "DEBUG",
        )

        api_family = network_element.get("api_family")
        api_function = network_element.get("api_function")
        self.log(
            f"Getting fabric devices using API family '{api_family}' and function '{api_function}'",
            "INFO",
        )

        # Execute API calls to get fabric devices
        all_fabric_devices = self.retrieve_all_fabric_devices_from_api(
            fabric_devices_params_list_to_query, api_family, api_function
        )

        if not all_fabric_devices:
            self.log(
                "No fabric devices found matching the provided filters",
                "WARNING",
            )
            return {"fabric_devices": []}

        self.log(
            f"Successfully retrieved {len(all_fabric_devices)} fabric device(s) for the provided filters",
            "INFO",
        )
        self.log(
            f"Details retrieved - all_fabric_devices:\n{self.pprint(all_fabric_devices)}",
            "DEBUG",
        )

        # Group fabric devices by fabric_name
        fabric_devices_by_fabric_name = self.group_fabric_devices_by_fabric_name(
            all_fabric_devices
        )

        ccc_version = self.get_ccc_version()
        if self.compare_dnac_versions(ccc_version, "2.3.7.9") < 0:
            self.log(
                f"Embedded wireless controller settings are not available in Catalyst Center version '{ccc_version}'. "
                f"Minimum required version is 2.3.7.9. Skipping embedded wireless controller settings retrieval.",
                "DEBUG",
            )
        else:
            self.log(
                f"Catalyst Center version '{ccc_version}' supports embedded wireless controller settings. "
                "Retrieving the embedded wireless controller settings details.",
                "INFO",
            )

            # Retrieve embedded wireless controller settings for all fabric sites
            wireless_settings_by_fabric_name = (
                self.retrieve_wireless_controller_settings_for_all_fabrics(
                    fabric_devices_by_fabric_name
                )
            )

            # Check if any embedded wireless controller settings were found
            if not wireless_settings_by_fabric_name:
                self.log(
                    "No embedded wireless controller settings found for any fabric site. Skipping managed AP locations retrieval.",
                    "INFO",
                )
            else:
                # Retrieve managed AP locations for all wireless controllers
                self.retrieve_managed_ap_locations_for_wireless_controllers(
                    wireless_settings_by_fabric_name
                )

            # Populate embedded wireless controller settings for each fabric site to its devices
            self.populate_wireless_controller_settings_to_devices(
                wireless_settings_by_fabric_name, fabric_devices_by_fabric_name
            )

        # Retrieve and populate border handoff settings for all devices
        self.log(
            "Retrieving border handoff settings (layer2, layer3 IP transit, layer3 SDA transit) for all devices",
            "INFO",
        )
        self.retrieve_and_populate_border_handoff_settings(
            fabric_devices_by_fabric_name
        )

        # Transform the data using the temp_spec and modify_parameters
        self.log("Starting transformation of fabric devices data", "INFO")
        temp_spec = network_element.get("reverse_mapping_function")()

        # Prepare data for modify_parameters - each entry represents a fabric with its devices
        fabric_entries_for_transformation = []
        for fabric_name, device_entries in fabric_devices_by_fabric_name.items():
            self.log(
                f"Preparing fabric '{fabric_name}' with {len(device_entries)} device(s) for transformation",
                "INFO",
            )
            # Create a fabric entry with fabric_name and device_entries (for transform_device_config)
            fabric_entry = {
                "fabric_name": fabric_name,
                "device_entries": device_entries,
            }
            fabric_entries_for_transformation.append(fabric_entry)

        # Use modify_parameters to apply the temp_spec transformations
        self.log(
            f"Applying modify_parameters with temp_spec to {len(fabric_entries_for_transformation)} fabric entries",
            "DEBUG",
        )
        transformed_fabric_devices_list = self.modify_parameters(
            temp_spec, fabric_entries_for_transformation
        )

        self.log(
            f"Transformation complete. Generated {len(transformed_fabric_devices_list)} fabric site(s) with devices",
            "INFO",
        )
        self.log("Exiting get_fabric_devices_configuration method", "DEBUG")

        return {"fabric_devices": transformed_fabric_devices_list}

    def transform_fabric_name(self, details):
        """
        Transform fabric_id to fabric_name using reverse mapping.

        Parameters:
            details (dict): Dictionary containing fabric_id.

        Returns:
            str: Fabric name corresponding to the fabric_id, or None if not found.

        Description:
            Performs a lookup to convert internal fabric ID to human-readable name.
        """

        self.log(
            f"Starting fabric_id to fabric_name transformation with details: {self.pprint(details)}",
            "DEBUG",
        )
        fabric_id = details.get("fabric_id")
        if not fabric_id:
            self.log("No fabric_id found in details", "WARNING")
            return None

        # Use reverse mapping dictionary for efficient lookup
        fabric_name = self.fabric_site_id_to_name_dict.get(fabric_id)
        if fabric_name:
            self.log(
                f"Transformed fabric_id '{fabric_id}' to fabric_name '{fabric_name}'",
                "DEBUG",
            )
            return fabric_name

        self.log(
            f"No fabric_name found for fabric_id '{fabric_id}'",
            "WARNING",
        )
        self.log("Exiting transform_fabric_name method - no fabric_name found", "DEBUG")
        return None

    def transform_device_config(self, details):
        """
        Transform device configuration to playbook-ready format.

        Parameters:
            details (dict): Dictionary with device_entries (list of devices) from modify_parameters.

        Returns:
            list: List of transformed device configurations for playbook use.

        Description:
            Converts API response format to Ansible playbook compatible structure.
            Called via modify_parameters with the full fabric entry containing device_entries.
        """
        self.log("Entering transform_device_config method", "DEBUG")
        self.log(
            f"Starting device_config transformation with details: {self.pprint(details)}",
            "DEBUG",
        )

        device_entries = details.get("device_entries")
        if not device_entries:
            self.log("No device_entries found in details", "WARNING")
            return None

        self.log(
            f"Processing {len(device_entries)} device entries for transformation",
            "DEBUG",
        )
        transformed_devices = []
        for idx, device_entry in enumerate(device_entries, 1):
            transformed_device = self._transform_single_device(device_entry)
            if transformed_device:
                transformed_devices.append(transformed_device)
            self.log(
                f"Skipping device entry {idx} due to empty transform result",
                "WARNING",
            )

        if not transformed_devices:
            self.log("No device configs transformed; returning None", "WARNING")
            self.log("Transform result: device_configs=None", "DEBUG")
            return None

        self.log(
            f"Device config transformation completed (count={len(transformed_devices)})",
            "INFO",
        )
        self.log(
            f"Transform result: device_configs_count={len(transformed_devices)}",
            "DEBUG",
        )
        return transformed_devices

    def _transform_single_device(self, details):
        """
        Transform a single device configuration to playbook-ready format.

        Parameters:
            details (dict): Dictionary with device_config and device information.

        Returns:
            dict: Transformed device configuration for playbook use.

        Description:
            Converts a single API device response to Ansible playbook compatible structure.
        """
        self.log(
            f"Preparing single device transformation (details={self.pprint(details)})",
            "DEBUG",
        )

        device_config = details.get("device_config")
        if not device_config:
            self.log("No device_config found in details", "WARNING")
            return None

        # Initialize playbook-ready device configuration
        transformed_device_config = {}

        # Add device_ip
        device_ip = details.get("device_ip")
        if device_ip:
            transformed_device_config["device_ip"] = device_ip
            self.log(
                f"Added device_ip '{device_ip}' to transformed_device_config",
                "DEBUG",
            )
        else:
            self.log(
                "No device_ip found in details - this is a required field",
                "WARNING",
            )

        # Transform device_roles from fabricDeviceRoles
        fabric_device_roles = device_config.get("deviceRoles", [])
        if fabric_device_roles:
            transformed_device_config["device_roles"] = fabric_device_roles
            self.log(
                f"Transformed deviceRoles to device_roles: {fabric_device_roles}",
                "DEBUG",
            )

        # Transform border settings if present
        border_settings = device_config.get("borderDeviceSettings")
        if border_settings:
            self.log(
                "Processing border settings",
                "DEBUG",
            )

            borders_settings = {}

            # Transform layer3Settings using camel_to_snake_case
            layer3_settings = border_settings.get("layer3Settings")
            if layer3_settings:
                borders_settings["layer3_settings"] = self.camel_to_snake_case(
                    layer3_settings
                )
                self.log(
                    "Added and transformed layer3_settings",
                    "DEBUG",
                )

            # Transform layer3HandoffIpTransit - filter out internal IDs
            layer3_handoff_ip_transit = border_settings.get("layer3HandoffIpTransit")
            if layer3_handoff_ip_transit:
                borders_settings["layer3_handoff_ip_transit"] = (
                    self.transform_layer3_ip_transit_handoffs(layer3_handoff_ip_transit)
                )
                self.log(
                    "Added and transformed layer3_handoff_ip_transit",
                    "DEBUG",
                )

            # Transform layer3HandoffSdaTransit - filter out internal IDs
            layer3_handoff_sda_transit = border_settings.get("layer3HandoffSdaTransit")
            if layer3_handoff_sda_transit:
                borders_settings["layer3_handoff_sda_transit"] = (
                    self.transform_layer3_sda_transit_handoff(
                        layer3_handoff_sda_transit
                    )
                )
                self.log(
                    "Added and transformed layer3_handoff_sda_transit settings",
                    "DEBUG",
                )

            # Transform layer2Handoff - filter out internal IDs
            layer2_handoff = border_settings.get("layer2Handoff")
            if layer2_handoff:
                borders_settings["layer2_handoff"] = self.transform_layer2_handoffs(
                    layer2_handoff
                )
                self.log(
                    "Added and transformed layer2_handoff",
                    "DEBUG",
                )

            # Only add borders_settings if it has content
            if borders_settings:
                transformed_device_config["borders_settings"] = borders_settings
                self.log(
                    "Successfully transformed and added borders_settings to device_config",
                    "DEBUG",
                )
        else:
            self.log(
                "No border settings found in device_config",
                "DEBUG",
            )

        # Transform embedded wireless controller settings if present
        self.transform_wireless_controller_settings(
            device_config, transformed_device_config
        )

        self.log(
            "Single device transformation complete",
            "DEBUG",
        )
        self.log("Exiting _transform_single_device method", "DEBUG")

        return transformed_device_config

    def transform_wireless_controller_settings(
        self, device_config, transformed_device_config
    ):
        """
        Transform embedded wireless controller settings from device config.

        Parameters:
            device_config (dict): Original device config with embeddedWirelessControllerSettings.
            transformed_device_config (dict): Target dict to update in place.

        Returns:
            None: Modifies transformed_device_config in place.

        Description:
            Extracts and transforms wireless controller settings to playbook format.
        """
        self.log("Entering transform_wireless_controller_settings method", "DEBUG")
        self.log(
            "Processing embedded wireless controller settings",
            "DEBUG",
        )
        embedded_wireless_settings = device_config.get(
            "embeddedWirelessControllerSettings"
        )
        if not embedded_wireless_settings:
            self.log(
                "No embedded wireless controller settings found in device_config",
                "DEBUG",
            )
            self.log(
                "Exiting transform_wireless_controller_settings method - no settings found",
                "DEBUG",
            )
            return

        # Transform to wireless_controller_settings format
        wireless_controller_settings = {}

        # Map basic settings
        wireless_controller_settings["enable"] = embedded_wireless_settings.get(
            "enableWireless"
        )
        primary_ap_locations = (
            embedded_wireless_settings.get("primaryManagedApLocations") or []
        )
        wireless_controller_settings["primary_managed_ap_locations"] = [
            site_details.get("siteNameHierarchy")
            for site_details in primary_ap_locations
        ]
        secondary_ap_locations = (
            embedded_wireless_settings.get("secondaryManagedApLocations") or []
        )
        wireless_controller_settings["secondary_managed_ap_locations"] = [
            site_details.get("siteNameHierarchy")
            for site_details in secondary_ap_locations
        ]

        rolling_ap_upgrade = embedded_wireless_settings.get("rollingApUpgrade")
        if rolling_ap_upgrade:
            wireless_controller_settings["rolling_ap_upgrade"] = {
                "enable": rolling_ap_upgrade.get("enableRollingApUpgrade"),
                "ap_reboot_percentage": rolling_ap_upgrade.get("apRebootPercentage"),
            }
            self.log(
                "Added rolling_ap_upgrade settings",
                "DEBUG",
            )
        else:
            self.log(
                "No rolling_ap_upgrade settings found",
                "WARNING",
            )

        transformed_device_config["wireless_controller_settings"] = (
            wireless_controller_settings
        )
        self.log(
            "Successfully transformed and added wireless_controller_settings to device_config",
            "INFO",
        )
        self.log(
            "Exiting transform_wireless_controller_settings method - transformation successful",
            "DEBUG",
        )
        return

    def transform_layer3_ip_transit_handoffs(self, layer3_ip_transit_list):
        """
        Transform layer3 IP transit handoffs to playbook format.

        Parameters:
            layer3_ip_transit_list (list): Layer3 IP transit handoff configs from API.

        Returns:
            list: Transformed list with playbook-relevant parameters only.

        Description:
            Filters internal IDs and converts camelCase to snake_case format.
        """
        self.log(
            "Transforming layer3 IP transit handoffs "
            f"(input_count={len(layer3_ip_transit_list) if layer3_ip_transit_list else 0})",
            "DEBUG",
        )
        if not layer3_ip_transit_list:
            self.log("No layer3 IP transit handoffs to transform", "DEBUG")
            self.log(
                "Exiting transform_layer3_ip_transit_handoffs method - empty list",
                "DEBUG",
            )
            return []

        # Fields to keep according to the spec (direct copy, no ID conversion)
        direct_fields = {
            "interfaceName": "interface_name",
            "externalConnectivityIpPoolName": "external_connectivity_ip_pool_name",
            "virtualNetworkName": "virtual_network_name",
            "vlanId": "vlan_id",
            "tcpMssAdjustment": "tcp_mss_adjustment",
            "localIpAddress": "local_ip_address",
            "remoteIpAddress": "remote_ip_address",
            "localIpv6Address": "local_ipv6_address",
            "remoteIpv6Address": "remote_ipv6_address",
        }

        self.log(
            f"Transforming {len(layer3_ip_transit_list)} layer3 IP transit handoff(s)",
            "DEBUG",
        )
        transformed_list = []
        for idx, handoff in enumerate(layer3_ip_transit_list, 1):
            self.log(
                f"Transforming layer3 IP transit handoff {idx}/{len(layer3_ip_transit_list)}",
                "DEBUG",
            )
            transformed_handoff = {}

            # Copy direct fields, skip empty values
            for api_key, playbook_key in direct_fields.items():
                value = handoff.get(api_key)
                # Skip None, empty strings, and empty collections
                if value is not None and value != "" and value != []:
                    transformed_handoff[playbook_key] = value

            # Convert transitNetworkId to transit_network_name
            transit_id = handoff.get("transitNetworkId")
            if transit_id:
                transit_name = self.transit_id_to_name_dict.get(transit_id)
                if transit_name:
                    transformed_handoff["transit_network_name"] = transit_name
                else:
                    self.log(
                        f"Warning: Transit ID '{transit_id}' not found in transit mapping",
                        "WARNING",
                    )

            if transformed_handoff:
                transformed_list.append(transformed_handoff)
            else:
                self.log(
                    f"Skipping handoff {idx} due to no transferable fields",
                    "WARNING",
                )

        self.log(
            f"Transformed {len(layer3_ip_transit_list)} layer3 IP transit handoff(s) to {len(transformed_list)} playbook entries",
            "INFO",
        )
        self.log("Exiting transform_layer3_ip_transit_handoffs method", "DEBUG")
        return transformed_list

    def transform_layer3_sda_transit_handoff(self, layer3_sda_transit):
        """
        Transform layer3 SDA transit handoff to playbook format.

        Parameters:
            layer3_sda_transit (dict): Layer3 SDA transit handoff config from API.

        Returns:
            dict: Transformed dict with playbook-relevant parameters only.

        Description:
            Filters internal IDs and converts transit ID to transit name.
        """
        self.log(
            "Transforming layer3 SDA transit handoff "
            f"(input_keys={list(layer3_sda_transit.keys()) if layer3_sda_transit else []})",
            "DEBUG",
        )
        if not layer3_sda_transit:
            self.log("No layer3 SDA transit handoff to transform", "DEBUG")
            self.log(
                "Exiting transform_layer3_sda_transit_handoff method - empty dict",
                "DEBUG",
            )
            return {}

        # Fields to keep according to the spec (direct copy, no ID conversion)
        direct_fields = {
            "affinityIdPrime": "affinity_id_prime",
            "affinityIdDecider": "affinity_id_decider",
            "connectedToInternet": "connected_to_internet",
            "isMulticastOverTransitEnabled": "is_multicast_over_transit_enabled",
        }

        transformed_handoff = {}

        # Copy direct fields, skip empty values
        for api_key, playbook_key in direct_fields.items():
            value = layer3_sda_transit.get(api_key)
            # Skip None, empty strings, and empty collections
            if value is not None and value != "" and value != []:
                transformed_handoff[playbook_key] = value

        # Convert transitNetworkId to transit_network_name
        transit_id = layer3_sda_transit.get("transitNetworkId")
        if transit_id:
            transit_name = self.transit_id_to_name_dict.get(transit_id)
            if transit_name:
                self.log(
                    f"Resolved transitNetworkId '{transit_id}' "
                    f"to transit_network_name '{transit_name}'",
                    "DEBUG",
                )
                transformed_handoff["transit_network_name"] = transit_name
            else:
                self.log(
                    f"Warning: Transit ID '{transit_id}' not found in transit mapping",
                    "WARNING",
                )

        self.log(
            f"Transformed layer3 SDA transit handoff with {len(transformed_handoff)} playbook parameter(s)",
            "INFO",
        )
        self.log("Exiting transform_layer3_sda_transit_handoff method", "DEBUG")
        return transformed_handoff

    def transform_layer2_handoffs(self, layer2_handoff_list):
        """
        Transform layer2 handoffs to playbook format.

        Parameters:
            layer2_handoff_list (list): Layer2 handoff configs from API.

        Returns:
            list: Transformed list with playbook-relevant parameters only.

        Description:
            Filters internal IDs and keeps interface_name, internal/external VLAN IDs.
        """
        self.log(
            "Transforming layer2 handoffs "
            f"(input_count={len(layer2_handoff_list) if layer2_handoff_list else 0})",
            "DEBUG",
        )
        if not layer2_handoff_list:
            self.log("No layer2 handoffs to transform", "DEBUG")
            self.log("Exiting transform_layer2_handoffs method - empty list", "DEBUG")
            return []

        # Fields to keep according to the spec
        # Based on workflow manager usage: interfaceName, internalVlanId, externalVlanId
        allowed_fields = {
            "interfaceName": "interface_name",
            "internalVlanId": "internal_vlan_id",
            "externalVlanId": "external_vlan_id",
        }

        self.log(f"Transforming {len(layer2_handoff_list)} layer2 handoff(s)", "DEBUG")
        transformed_list = []
        for idx, handoff in enumerate(layer2_handoff_list, 1):
            self.log(
                f"Transforming layer2 handoff {idx}/{len(layer2_handoff_list)}", "DEBUG"
            )
            transformed_handoff = {}
            for api_key, playbook_key in allowed_fields.items():
                value = handoff.get(api_key)
                # Skip None, empty strings, and empty collections
                if value is not None and value != "" and value != []:
                    transformed_handoff[playbook_key] = value

            # Only add if we have all required fields
            if transformed_handoff:
                transformed_list.append(transformed_handoff)

        self.log(
            f"Transformed {len(layer2_handoff_list)} layer2 handoff(s) to {len(transformed_list)} playbook entries",
            "INFO",
        )
        self.log("Exiting transform_layer2_handoffs method", "DEBUG")
        return transformed_list

    def retrieve_and_populate_border_handoff_settings(
        self, fabric_devices_by_fabric_name
    ):
        """
        Retrieve and populate border handoff settings for all devices.

        Parameters:
            fabric_devices_by_fabric_name (dict): Mapping of fabric_name to device entries.

        Returns:
            None: Modifies device_config in place with border handoff settings.

        Description:
            Fetches layer2, layer3 IP transit, and layer3 SDA transit handoffs for each device.
        """
        self.log(
            "Entering retrieve_and_populate_border_handoff_settings method", "DEBUG"
        )
        self.log(
            f"Starting retrieval of border handoff settings for devices across {len(fabric_devices_by_fabric_name)} fabric site(s)",
            "INFO",
        )

        total_devices = sum(
            len(device_entries)
            for device_entries in fabric_devices_by_fabric_name.values()
        )
        total_fabrics = len(fabric_devices_by_fabric_name)

        self.log(
            "Retrieving border handoff settings for all devices "
            f"(fabric_count={total_fabrics}, device_count={total_devices})",
            "INFO",
        )
        self.log(
            f"Input fabrics: {list(fabric_devices_by_fabric_name.keys())}",
            "DEBUG",
        )

        for fabric_idx, (fabric_name, device_entries) in enumerate(
            fabric_devices_by_fabric_name.items(), 1
        ):
            fabric_id = self.fabric_site_name_to_id_dict.get(fabric_name)
            self.log(
                "Processing fabric "
                f"{fabric_idx}/{total_fabrics}: name='{fabric_name}', "
                f"id='{fabric_id}', device_count={len(device_entries)}",
                "DEBUG",
            )

            for idx, device_entry in enumerate(device_entries, 1):
                device_config = device_entry.get("device_config")
                device_ip = device_entry.get("device_ip")
                network_device_id = device_config.get("networkDeviceId")

                if not network_device_id:
                    self.log(
                        f"Skipping device {idx}/{len(device_entries)} in fabric '{fabric_name}': No network_device_id found",
                        "WARNING",
                    )
                    continue

                self.log(
                    f"Processing device {idx}/{len(device_entries)} in fabric '{fabric_name}': "
                    f"device_ip='{device_ip}', network_device_id='{network_device_id}'",
                    "DEBUG",
                )

                # Initialize borderDeviceSettings if not present
                if "borderDeviceSettings" not in device_config:
                    device_config["borderDeviceSettings"] = {}
                    self.log(
                        "Initialized borderDeviceSettings for device "
                        f"(device_ip='{device_ip}')",
                        "DEBUG",
                    )

                border_settings = device_config["borderDeviceSettings"]

                # Retrieve layer2 handoffs
                layer2_handoffs = self.get_layer2_handoffs_for_device(
                    fabric_id, network_device_id
                )
                if layer2_handoffs:
                    border_settings["layer2Handoff"] = layer2_handoffs
                    self.log(
                        f"Retrieved {len(layer2_handoffs)} layer2 handoff(s) for device '{device_ip}'",
                        "DEBUG",
                    )

                # Retrieve layer3 IP transit handoffs
                layer3_ip_transit_handoffs = (
                    self.get_layer3_ip_transit_handoffs_for_device(
                        fabric_id, network_device_id
                    )
                )
                if layer3_ip_transit_handoffs:
                    border_settings["layer3HandoffIpTransit"] = (
                        layer3_ip_transit_handoffs
                    )
                    self.log(
                        f"Retrieved {len(layer3_ip_transit_handoffs)} layer3 IP transit handoff(s) for device '{device_ip}'",
                        "DEBUG",
                    )

                # Retrieve layer3 SDA transit handoffs
                layer3_sda_transit_handoff = (
                    self.get_layer3_sda_transit_handoff_for_device(
                        fabric_id, network_device_id
                    )
                )
                if layer3_sda_transit_handoff:
                    border_settings["layer3HandoffSdaTransit"] = (
                        layer3_sda_transit_handoff
                    )
                    self.log(
                        f"Retrieved layer3 SDA transit handoff for device '{device_ip}'",
                        "DEBUG",
                    )

                self.log(
                    f"Completed border handoff settings retrieval for device '{device_ip}'",
                    "DEBUG",
                )

        self.log(
            "Border handoff settings retrieval and population complete for all devices",
            "INFO",
        )
        self.log(
            "Exiting retrieve_and_populate_border_handoff_settings method", "DEBUG"
        )

    def get_layer2_handoffs_for_device(self, fabric_id, network_device_id):
        """
        Retrieve layer2 handoffs for a specific device.

        Parameters:
            fabric_id (str): The fabric site ID.
            network_device_id (str): The network device ID.

        Returns:
            list: Layer2 handoff configurations, or empty list if none found.

        Description:
            Calls API to get layer2 handoffs for a device in a fabric.
        """
        self.log("Entering get_layer2_handoffs_for_device method", "DEBUG")
        self.log(
            f"Retrieving layer2 handoffs for device '{network_device_id}' in fabric '{fabric_id}'",
            "INFO",
        )

        try:
            response = self.dnac._exec(
                family="sda",
                function="get_fabric_devices_layer2_handoffs",
                params={
                    "fabric_id": fabric_id,
                    "network_device_id": network_device_id,
                },
            )

            if response and isinstance(response, dict):
                layer2_handoffs = response.get("response", [])
                self.log(
                    f"Layer2 handoffs API response for device '{network_device_id}': {self.pprint(layer2_handoffs)}",
                    "DEBUG",
                )
                self.log(
                    f"Retrieved {len(layer2_handoffs)} layer2 handoff(s) for device '{network_device_id}'",
                    "INFO",
                )
                self.log(
                    "Exiting get_layer2_handoffs_for_device method - success", "DEBUG"
                )
                return layer2_handoffs if layer2_handoffs else []
            else:
                self.log(
                    f"No layer2 handoffs found for device '{network_device_id}' in fabric '{fabric_id}'",
                    "DEBUG",
                )
                self.log(
                    "Exiting get_layer2_handoffs_for_device method - no handoffs found",
                    "DEBUG",
                )
                return []

        except Exception as e:
            self.log(
                f"Error retrieving layer2 handoffs for device '{network_device_id}' in fabric '{fabric_id}': {str(e)}",
                "ERROR",
            )
            self.log(
                "Exiting get_layer2_handoffs_for_device method - error occurred",
                "DEBUG",
            )
            return []

    def get_layer3_ip_transit_handoffs_for_device(self, fabric_id, network_device_id):
        """
        Retrieve layer3 IP transit handoffs for a specific device.

        Parameters:
            fabric_id (str): The fabric site ID.
            network_device_id (str): The network device ID.

        Returns:
            list: Layer3 IP transit handoff configurations, or empty list if none found.

        Description:
            Calls API to get layer3 IP transit handoffs for a device in a fabric.
        """
        self.log("Entering get_layer3_ip_transit_handoffs_for_device method", "DEBUG")
        self.log(
            f"Retrieving layer3 IP transit handoffs for device '{network_device_id}' in fabric '{fabric_id}'",
            "INFO",
        )

        try:
            response = self.dnac._exec(
                family="sda",
                function="get_fabric_devices_layer3_handoffs_with_ip_transit",
                params={
                    "fabric_id": fabric_id,
                    "network_device_id": network_device_id,
                },
            )

            if response and isinstance(response, dict):
                layer3_ip_transit_handoffs = response.get("response", [])
                self.log(
                    f"Layer3 IP transit handoffs API response for device '{network_device_id}': {self.pprint(layer3_ip_transit_handoffs)}",
                    "DEBUG",
                )
                self.log(
                    f"Retrieved {len(layer3_ip_transit_handoffs)} layer3 IP transit handoff(s) for device '{network_device_id}'",
                    "INFO",
                )
                self.log(
                    "Exiting get_layer3_ip_transit_handoffs_for_device method - success",
                    "DEBUG",
                )
                return layer3_ip_transit_handoffs if layer3_ip_transit_handoffs else []
            else:
                self.log(
                    f"No layer3 IP transit handoffs found for device '{network_device_id}' in fabric '{fabric_id}'",
                    "DEBUG",
                )
                self.log(
                    "Exiting get_layer3_ip_transit_handoffs_for_device method - no handoffs found",
                    "DEBUG",
                )
                return []

        except Exception as e:
            self.log(
                f"Error retrieving layer3 IP transit handoffs for device '{network_device_id}' in fabric '{fabric_id}': {str(e)}",
                "ERROR",
            )
            self.log(
                "Exiting get_layer3_ip_transit_handoffs_for_device method - error occurred",
                "DEBUG",
            )
            return []

    def get_layer3_sda_transit_handoff_for_device(self, fabric_id, network_device_id):
        """
        Retrieve layer3 SDA transit handoff for a specific device.

        Parameters:
            fabric_id (str): The fabric site ID.
            network_device_id (str): The network device ID.

        Returns:
            dict: Layer3 SDA transit handoff config, or None if not found.

        Description:
            Calls API to get layer3 SDA transit handoff for a device in a fabric.
        """
        self.log("Entering get_layer3_sda_transit_handoff_for_device method", "DEBUG")
        self.log(
            f"Retrieving layer3 SDA transit handoff for device '{network_device_id}' in fabric '{fabric_id}'",
            "INFO",
        )

        try:
            response = self.dnac._exec(
                family="sda",
                function="get_fabric_devices_layer3_handoffs_with_sda_transit",
                params={
                    "fabric_id": fabric_id,
                    "network_device_id": network_device_id,
                },
            )

            if response and isinstance(response, dict):
                layer3_sda_transit_handoffs = response.get("response", [])
                self.log(
                    f"Layer3 SDA transit handoff API response for device '{network_device_id}': {self.pprint(layer3_sda_transit_handoffs)}",
                    "DEBUG",
                )
                # For SDA transit, typically only one handoff per device
                if layer3_sda_transit_handoffs:
                    self.log(
                        f"Retrieved layer3 SDA transit handoff for device '{network_device_id}'",
                        "INFO",
                    )
                    self.log(
                        "Exiting get_layer3_sda_transit_handoff_for_device method - success",
                        "DEBUG",
                    )
                    return layer3_sda_transit_handoffs[0]
                self.log("No layer3 SDA transit handoff found in response", "DEBUG")
                self.log(
                    "Exiting get_layer3_sda_transit_handoff_for_device method - no handoff found",
                    "DEBUG",
                )
                return None
            else:
                self.log(
                    f"No layer3 SDA transit handoff found for device '{network_device_id}' in fabric '{fabric_id}'",
                    "DEBUG",
                )
                self.log(
                    "Exiting get_layer3_sda_transit_handoff_for_device method - invalid response",
                    "DEBUG",
                )
                return None

        except Exception as e:
            self.log(
                f"Error retrieving layer3 SDA transit handoff for device '{network_device_id}' in fabric '{fabric_id}': {str(e)}",
                "ERROR",
            )
            self.log(
                "Exiting get_layer3_sda_transit_handoff_for_device method - error occurred",
                "DEBUG",
            )
            return None

    def retrieve_wireless_controller_settings_for_all_fabrics(
        self, fabric_devices_by_fabric_name
    ):
        """
        Retrieve wireless controller settings for all fabric sites.

        Parameters:
            fabric_devices_by_fabric_name (dict): Mapping of fabric_name to device entries.

        Returns:
            dict: Mapping of fabric_name to wireless controller settings.

        Description:
            Iterates through fabrics and retrieves embedded wireless controller settings.
        """
        self.log(
            "Entering retrieve_wireless_controller_settings_for_all_fabrics method",
            "DEBUG",
        )
        self.log(
            f"Iterating through {len(fabric_devices_by_fabric_name)} fabric site(s) to retrieve embedded wireless controller settings",
            "INFO",
        )

        wireless_settings_by_fabric_name = {}
        for idx, (fabric_name, device_entries) in enumerate(
            fabric_devices_by_fabric_name.items(), 1
        ):
            self.log(
                f"Processing fabric {idx}/{len(fabric_devices_by_fabric_name)}: '{fabric_name}'",
                "DEBUG",
            )
            fabric_id = self.fabric_site_name_to_id_dict.get(fabric_name)
            self.log(
                f"Retrieving embedded wireless controller settings for fabric site '{fabric_name}' "
                f"(fabric_id: '{fabric_id}') with {len(device_entries)} device(s)",
                "DEBUG",
            )

            wireless_settings = self.get_wireless_controller_settings_for_fabric(
                fabric_id
            )
            if not wireless_settings:
                self.log(
                    f"No embedded wireless controller settings found for fabric site '{fabric_name}' (fabric_id: '{fabric_id}')",
                    "DEBUG",
                )
                continue

            wireless_settings_by_fabric_name[fabric_name] = wireless_settings
            self.log(
                f"Successfully retrieved and stored embedded wireless controller settings for fabric site '{fabric_name}' (fabric_id: '{fabric_id}')",
                "INFO",
            )

        self.log(
            f"Embedded wireless controller settings retrieval complete. Retrieved settings for {len(wireless_settings_by_fabric_name)} fabric site(s)",
            "INFO",
        )
        self.log(
            f"Embedded wireless controller settings by fabric name:\n{self.pprint(wireless_settings_by_fabric_name)}",
            "DEBUG",
        )

        self.log(
            "Exiting retrieve_wireless_controller_settings_for_all_fabrics method",
            "DEBUG",
        )
        return wireless_settings_by_fabric_name

    def retrieve_managed_ap_locations_for_wireless_controllers(
        self, wireless_settings_by_fabric_id
    ):
        """
        Retrieve managed AP locations for all wireless controllers.

        Parameters:
            wireless_settings_by_fabric_id (dict): Mapping of fabric_id to wireless settings.

        Returns:
            None: Modifies wireless_settings_by_fabric_id in place.

        Description:
            Adds primaryManagedApLocations and secondaryManagedApLocations to each controller.
        """
        self.log(
            "Entering retrieve_managed_ap_locations_for_wireless_controllers method",
            "DEBUG",
        )
        self.log(
            f"Retrieving primary and secondary managed AP locations for {len(wireless_settings_by_fabric_id)} embedded wireless controller(s)",
            "INFO",
        )

        # Get device ID to IP mapping for all embedded wireless controllers
        all_embedded_wireless_controller_device_ids = [
            wireless_settings.get("id")
            for wireless_settings in wireless_settings_by_fabric_id.values()
            if wireless_settings.get("id")
        ]

        if all_embedded_wireless_controller_device_ids:
            self.log(
                f"Retrieving device IPs for {len(all_embedded_wireless_controller_device_ids)} embedded wireless controller device(s)",
                "DEBUG",
            )
            device_id_to_ip_map = self.get_device_ips_from_device_ids(
                all_embedded_wireless_controller_device_ids
            )
            self.log(
                f"Device ID to IP mapping: {self.pprint(device_id_to_ip_map)}",
                "DEBUG",
            )
        else:
            self.log(
                "No embedded wireless controller devices found. Skipping device IP mapping retrieval.",
                "DEBUG",
            )
            device_id_to_ip_map = {}

        for idx, (fabric_id, wireless_settings) in enumerate(
            wireless_settings_by_fabric_id.items(), 1
        ):
            self.log(
                f"Processing wireless controller {idx}/{len(wireless_settings_by_fabric_id)}",
                "DEBUG",
            )
            network_device_id = wireless_settings.get("id")
            device_ip = device_id_to_ip_map.get(network_device_id)
            fabric_name = self.fabric_site_id_to_name_dict.get(fabric_id, "Unknown")
            self.log(
                f"Fetching primary and secondary managed AP locations for the device '{device_ip}' (device_id: '{network_device_id}') "
                f"in fabric site '{fabric_name}' (fabric_id: '{fabric_id}')",
                "DEBUG",
            )

            # Get primary managed AP locations
            primary_ap_locations = self.get_managed_ap_locations_for_device(
                network_device_id, device_ip, ap_type="primary"
            )
            wireless_settings["primaryManagedApLocations"] = primary_ap_locations

            # Get secondary managed AP locations
            secondary_ap_locations = self.get_managed_ap_locations_for_device(
                network_device_id, device_ip, ap_type="secondary"
            )
            wireless_settings["secondaryManagedApLocations"] = secondary_ap_locations

            self.log(
                f"Retrieved {len(primary_ap_locations)} primary and {len(secondary_ap_locations)} secondary AP locations for device '{device_ip}'",
                "INFO",
            )

        self.log(
            "Completed retrieval of managed AP locations for all embedded wireless controllers",
            "INFO",
        )
        self.log(
            "Exiting retrieve_managed_ap_locations_for_wireless_controllers method",
            "DEBUG",
        )

    def populate_wireless_controller_settings_to_devices(
        self, wireless_settings_by_fabric_name, fabric_devices_by_fabric_name
    ):
        """
        Populate wireless controller settings to devices in each fabric.

        Parameters:
            wireless_settings_by_fabric_name (dict): Mapping of fabric_name to wireless settings.
            fabric_devices_by_fabric_name (dict): Mapping of fabric_name to device entries.

        Returns:
            None: Modifies fabric_devices_by_fabric_name in place.

        Description:
            Adds embeddedWirelessControllerSettings to each matching device config.
        """
        fabric_count = len(wireless_settings_by_fabric_name)
        self.log(
            "Populating embedded wireless controller settings "
            f"(fabric_count={fabric_count})",
            "INFO",
        )
        self.log(
            f"Input fabric names: {list(wireless_settings_by_fabric_name.keys())}",
            "DEBUG",
        )

        if not wireless_settings_by_fabric_name:
            self.log(
                "No wireless settings provided; nothing to populate",
                "WARNING",
            )
            self.log("Population result: updated_devices=0", "DEBUG")
            return

        total_fabric_sites_to_process = len(wireless_settings_by_fabric_name)
        for idx, (fabric_name, wireless_settings) in enumerate(
            wireless_settings_by_fabric_name.items(), 1
        ):
            device_entries = fabric_devices_by_fabric_name.get(fabric_name)
            fabric_id = self.fabric_site_name_to_id_dict.get(fabric_name, "Unknown")
            device_count = len(device_entries) if device_entries else 0

            self.log(
                f"Processing fabric {idx}/{total_fabric_sites_to_process}: '{fabric_name}' "
                f"(fabric_id: '{fabric_id}') with {len(device_entries) if device_entries else 0} device(s)",
                "DEBUG",
            )

            if not device_entries:
                self.log(
                    f"No devices found for fabric site '{fabric_name}' (fabric_id: '{fabric_id}'). Skipping.",
                    "WARNING",
                )
                continue

            devices_with_wireless_settings = 0
            devices_without_wireless_settings = 0

            total_devices = len(device_entries)
            for device_idx, device_entry in enumerate(device_entries, 1):
                device = device_entry.get("device_config")
                network_device_id = device.get("networkDeviceId")

                self.log(
                    f"Processing device {device_idx}/{total_devices} with network_device_id '{network_device_id}' in fabric '{fabric_name}'",
                    "DEBUG",
                )
                if not device:
                    self.log(
                        "Skipping device entry due to missing device_config",
                        "WARNING",
                    )
                    continue

                # Check if wireless settings exist for this fabric and if this device has embedded wireless controller settings
                if wireless_settings.get("id") == network_device_id:
                    device["embeddedWirelessControllerSettings"] = wireless_settings
                    devices_with_wireless_settings += 1
                    self.log(
                        f"Added embedded wireless controller settings to device '{network_device_id}' "
                        f"in fabric site '{fabric_name}' (fabric_id: '{fabric_id}')",
                        "DEBUG",
                    )
                else:
                    device["embeddedWirelessControllerSettings"] = None
                    devices_without_wireless_settings += 1
                    self.log(
                        f"No embedded wireless controller settings found for device '{network_device_id}' "
                        f"in fabric site '{fabric_name}' (fabric_id: '{fabric_id}')",
                        "DEBUG",
                    )

            self.log(
                f"Completed processing fabric '{fabric_name}': {devices_with_wireless_settings} device(s) with wireless settings, "
                f"{devices_without_wireless_settings} device(s) without wireless settings",
                "INFO",
            )

        self.log(
            f"Completed populating embedded wireless controller settings for all {total_fabric_sites_to_process} fabric site(s)",
            "INFO",
        )
        self.log(
            f"Fabric devices with populated embedded wireless controller settings:\n{self.pprint(fabric_devices_by_fabric_name)}",
            "DEBUG",
        )
        self.log(
            "Exiting populate_wireless_controller_settings_to_devices method", "DEBUG"
        )

    def get_wireless_controller_settings_for_fabric(self, fabric_id):
        """
        Retrieve wireless controller settings for a specific fabric.

        Parameters:
            fabric_id (str): The fabric site ID.

        Returns:
            dict: Wireless controller settings, or None if not found/error.

        Description:
            Calls API to get embedded wireless controller settings for a fabric site.
        """
        self.log("Entering get_wireless_controller_settings_for_fabric method", "DEBUG")
        self.log(
            f"Retrieving wireless controller settings for fabric_id '{fabric_id}'",
            "INFO",
        )

        try:
            wireless_response = self.dnac._exec(
                family="fabric_wireless",
                function="get_sda_wireless_details_from_switches",
                params={"fabric_id": fabric_id},
            )

            self.log(
                f"Raw embedded wireless controller settings API response for fabric_id '{fabric_id}':\n{self.pprint(wireless_response)}",
                "DEBUG",
            )

        except Exception as e:
            self.log(
                f"Error retrieving embedded wireless controller settings for fabric_id '{fabric_id}': {str(e)}",
                "ERROR",
            )
            self.log(
                "Exiting get_wireless_controller_settings_for_fabric method - error occurred",
                "DEBUG",
            )
            return None

        # Extract the response data
        if not wireless_response or not isinstance(wireless_response, dict):
            self.log(
                "Unexpected response format for embedded wireless controller settings "
                f"(fabric_id='{fabric_id}')",
                "WARNING",
            )
            self.log("Fetch result: settings_found=no", "DEBUG")
            return None

        response_data = wireless_response.get("response")
        if not response_data or not isinstance(response_data, list):
            self.log(
                "No embedded wireless controller settings found "
                f"(fabric_id='{fabric_id}')",
                "DEBUG",
            )
            self.log("Fetch result: settings_found=no", "DEBUG")
            return None

        wireless_settings = response_data[0]
        if not wireless_settings:
            self.log(
                "Embedded wireless controller settings list was empty "
                f"(fabric_id='{fabric_id}')",
                "DEBUG",
            )
            self.log("Fetch result: settings_found=no", "DEBUG")
            return None

        self.log(
            "Embedded wireless controller settings retrieved "
            f"(fabric_id='{fabric_id}', keys={list(wireless_settings.keys())})",
            "INFO",
        )
        self.log("Fetch result: settings_found=yes", "DEBUG")
        return wireless_settings

    def get_managed_ap_locations_for_device(
        self, network_device_id, device_ip, ap_type="primary"
    ):
        """
        Retrieve managed AP locations for a specific wireless controller.

        Parameters:
            network_device_id (str): Network device ID of the wireless controller.
            device_ip (str): IP address of the wireless controller.
            ap_type (str): 'primary' or 'secondary'. Defaults to 'primary'.

        Returns:
            list: Managed AP location dicts, or empty list if not found/error.

        Description:
            Fetches AP locations with pagination support.
        """
        self.log("Entering get_managed_ap_locations_for_device method", "DEBUG")
        self.log(
            f"Starting retrieval of {ap_type} managed AP locations for device '{device_ip}' (network_device_id: '{network_device_id}')",
            "INFO",
        )

        allowed_ap_types = ["primary", "secondary"]
        if ap_type not in allowed_ap_types:
            self.log(
                f"Invalid ap_type: '{ap_type}' provided. Allowed types: {', '.join(allowed_ap_types)}",
                "ERROR",
            )
            return []

        api_function = (
            f"get_{ap_type}_managed_ap_locations_for_specific_wireless_controller"
        )
        managed_ap_locations_all = []
        offset = 1
        limit = 500
        batch_count = 0

        while True:
            batch_count += 1
            self.log(
                f"Batch {batch_count}: Requesting {ap_type} managed AP locations (offset={offset}, limit={limit}) for device '{device_ip}'",
                "DEBUG",
            )

            try:
                response = self.dnac._exec(
                    family="wireless",
                    function=api_function,
                    op_modifies=False,
                    params={
                        "network_device_id": network_device_id,
                        "limit": limit,
                        "offset": offset,
                    },
                )

                self.log(
                    f"API response ({ap_type} managed AP locations) for device '{device_ip}' (offset {offset}):\n{self.pprint(response)}",
                    "DEBUG",
                )

                if not isinstance(response, dict):
                    self.log(
                        f"Invalid API response type: {type(response)} received for {ap_type} AP locations",
                        "ERROR",
                    )
                    break

                managed_ap_response = response.get("response")
                if not managed_ap_response:
                    self.log(
                        f"Batch {batch_count}: No {ap_type} managed AP locations found in response for device '{device_ip}'. Stopping pagination",
                        "DEBUG",
                    )
                    break

                managed_ap_locations = managed_ap_response.get("managedApLocations", [])
                count = len(managed_ap_locations)

                self.log(
                    f"Batch {batch_count}: Retrieved {count} {ap_type} managed AP location(s) for device '{device_ip}'",
                    "DEBUG",
                )

                if count == 0:
                    self.log(
                        f"Batch {batch_count}: No more {ap_type} managed AP locations to retrieve. Stopping pagination",
                        "DEBUG",
                    )
                    break

                managed_ap_locations_all.extend(managed_ap_locations)
                offset += count

                # If we received fewer records than the limit, we've reached the end
                if count < limit:
                    self.log(
                        f"Batch {batch_count}: Received {count} records (less than limit {limit}). End of pagination",
                        "DEBUG",
                    )
                    break

            except Exception as e:
                self.log(
                    f"Error retrieving {ap_type} managed AP locations for device '{device_ip}': {str(e)}",
                    "WARNING",
                )
                break

        self.log(
            f"Total {ap_type} managed AP locations retrieved for device '{device_ip}': {len(managed_ap_locations_all)}",
            "INFO",
        )
        self.log("Exiting get_managed_ap_locations_for_device method", "DEBUG")

        return managed_ap_locations_all

    def get_want(self, config, state):
        """
        Create parameters for API calls based on the specified state.

        Parameters:
            config (dict): The configuration data for the network elements.
            state (str): The desired state of the network elements.

        Returns:
            SdaFabricDevicesPlaybookGenerator: Returns self for method chaining.

        Description:
            Prepares and stores the desired configuration in self.want.
        """
        self.log("Entering get_want method", "DEBUG")
        self.log(f"Creating Parameters for API Calls with state: '{state}'", "INFO")

        self.log("Validating input parameters", "DEBUG")
        self.validate_params(config)

        want = {}

        # Add yaml_config_generator to want
        want["yaml_config_generator"] = config
        self.log(
            f"yaml_config_generator added to want: {want['yaml_config_generator']}",
            "DEBUG",
        )

        self.want = want
        self.log(f"Desired State (want): {str(self.want)}", "DEBUG")
        self.msg = "Successfully collected all parameters from the playbook for Wireless Design operations."
        self.status = "success"
        self.log(self.msg, "INFO")
        self.log("Exiting get_want method", "DEBUG")
        return self

    def get_diff_gathered(self):
        """
        Execute gather operations for fabric device configurations.

        Parameters:
            None: Uses self.want internally.

        Returns:
            SdaFabricDevicesPlaybookGenerator: Returns self for method chaining.

        Description:
            Processes YAML config generation and logs operation details.
        """

        start_time = time.time()
        self.log("Entering get_diff_gathered method", "DEBUG")
        self.log("Starting 'get_diff_gathered' operation", "INFO")
        operations = [
            (
                "yaml_config_generator",
                "YAML Config Generator",
                self.yaml_config_generator,
            )
        ]
        self.log(f"Total operations to process: {len(operations)}", "DEBUG")

        # Iterate over operations and process them
        self.log("Beginning iteration over defined operations for processing", "DEBUG")
        for index, (param_key, operation_name, operation_func) in enumerate(
            operations, start=1
        ):
            self.log(
                f"Iteration {index}/{len(operations)}: Checking parameters for '{operation_name}' operation with param_key '{param_key}'",
                "DEBUG",
            )
            params = self.want.get(param_key)
            if params:
                self.log(
                    f"Iteration {index}/{len(operations)}: Parameters found for '{operation_name}'. Starting processing",
                    "INFO",
                )
                operation_func(params).check_return_status()
                self.log(
                    f"Iteration {index}/{len(operations)}: '{operation_name}' operation completed",
                    "DEBUG",
                )
            else:
                self.log(
                    f"Iteration {index}/{len(operations)}: No parameters found for '{operation_name}'. Skipping operation",
                    "WARNING",
                )

        end_time = time.time()
        self.log(
            f"Completed 'get_diff_gathered' operation in {end_time - start_time:.2f} seconds",
            "INFO",
        )
        self.log("Exiting get_diff_gathered method", "DEBUG")

        return self


def main():
    """
    Main entry point for module execution.

    Parameters:
        None: Uses AnsibleModule arguments.

    Returns:
        None: Exits via module.exit_json().

    Description:
        Initializes the module, validates input, and executes YAML generation.
    """
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

    # Initialize the SDA Fabric Devices Playbook Generator object with the module
    ccc_sda_fabric_devices_playbook_generator = SdaFabricDevicesPlaybookGenerator(
        module
    )

    ccc_sda_fabric_devices_playbook_generator.log("Module execution started", "INFO")
    ccc_sda_fabric_devices_playbook_generator.log(
        "Checking Catalyst Center version compatibility", "DEBUG"
    )

    ccc_version = ccc_sda_fabric_devices_playbook_generator.get_ccc_version()
    if (
        ccc_sda_fabric_devices_playbook_generator.compare_dnac_versions(
            ccc_version, "2.3.7.6"
        )
        < 0
    ):
        ccc_sda_fabric_devices_playbook_generator.msg = (
            f"The specified version '{ccc_version}' does not support the YAML Playbook generation "
            f"for SDA Fabric Devices Workflow Manager Module. Supported versions start from '2.3.7.6' onwards. "
        )
        ccc_sda_fabric_devices_playbook_generator.log(
            ccc_sda_fabric_devices_playbook_generator.msg, "ERROR"
        )
        ccc_sda_fabric_devices_playbook_generator.set_operation_result(
            "failed", False, ccc_sda_fabric_devices_playbook_generator.msg, "ERROR"
        ).check_return_status()

    # Get the state parameter from the provided parameters
    state = ccc_sda_fabric_devices_playbook_generator.params.get("state")
    ccc_sda_fabric_devices_playbook_generator.log(f"Requested state: '{state}'", "INFO")

    # Check if the state is valid
    if state not in ccc_sda_fabric_devices_playbook_generator.supported_states:
        ccc_sda_fabric_devices_playbook_generator.status = "invalid"
        ccc_sda_fabric_devices_playbook_generator.msg = (
            f"State '{state}' is invalid. "
            f"Supported states: {ccc_sda_fabric_devices_playbook_generator.supported_states}"
        )
        ccc_sda_fabric_devices_playbook_generator.log(
            ccc_sda_fabric_devices_playbook_generator.msg, "ERROR"
        )
        ccc_sda_fabric_devices_playbook_generator.check_return_status()

    # Validate the input parameters and check the return status
    ccc_sda_fabric_devices_playbook_generator.log(
        "Validating input parameters", "DEBUG"
    )
    ccc_sda_fabric_devices_playbook_generator.validate_input().check_return_status()
    config = ccc_sda_fabric_devices_playbook_generator.validated_config
    ccc_sda_fabric_devices_playbook_generator.log(
        f"Processing {len(config)} validated configuration item(s)", "INFO"
    )

    # Iterate over the validated configuration parameters
    for idx, config_item in enumerate(
        ccc_sda_fabric_devices_playbook_generator.validated_config, 1
    ):
        ccc_sda_fabric_devices_playbook_generator.log(
            f"Processing configuration item {idx}/{len(ccc_sda_fabric_devices_playbook_generator.validated_config)}",
            "DEBUG",
        )
        ccc_sda_fabric_devices_playbook_generator.reset_values()
        ccc_sda_fabric_devices_playbook_generator.get_want(
            config_item, state
        ).check_return_status()
        ccc_sda_fabric_devices_playbook_generator.get_diff_state_apply[
            state
        ]().check_return_status()

    ccc_sda_fabric_devices_playbook_generator.log(
        "Module execution completed successfully", "INFO"
    )
    module.exit_json(**ccc_sda_fabric_devices_playbook_generator.result)


if __name__ == "__main__":
    main()
