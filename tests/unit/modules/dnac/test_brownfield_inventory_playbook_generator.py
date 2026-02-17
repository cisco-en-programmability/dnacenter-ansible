#  Copyright (c) 2025 Cisco and/or its affiliates.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# Authors:
#   Mridul Saurabh <msaurabh@cisco.com>
#   Madhan Sankaranarayanan <madsanka@cisco.com>
#
# Description:
#   Unit tests for the Ansible module `brownfield_inventory_playbook_generator`.
#   These tests cover various brownfield inventory scenarios such as complete
#   discovery, device filtering by IP, hostname, serial number, MAC address,
#   role-based filtering, combined filters, and multiple device groups.

from __future__ import absolute_import, division, print_function

__metaclass__ = type
from unittest.mock import patch, MagicMock
from ansible_collections.cisco.dnac.plugins.modules import brownfield_inventory_playbook_generator
from .dnac_module import TestDnacModule, set_module_args, loadPlaybookData


class TestBrownfieldInventoryPlaybookGenerator(TestDnacModule):
    """
    Test class for brownfield_inventory_playbook_generator module.
    Tests all scenarios defined in the JSON fixture file.
    """

    module = brownfield_inventory_playbook_generator
    test_data = loadPlaybookData("brownfield_inventory_playbook_generator")

    # Load all test configurations from fixtures
    playbook_config_scenario1_complete_infrastructure_generate_all_device_configurations = test_data.get(
        "playbook_config_scenario1_complete_infrastructure_generate_all_device_configurations"
    )
    playbook_config_scenario2_specific_devices_by_ip_address_list = test_data.get(
        "playbook_config_scenario2_specific_devices_by_ip_address_list"
    )
    playbook_config_scenario3_devices_by_hostname_list = test_data.get(
        "playbook_config_scenario3_devices_by_hostname_list"
    )
    playbook_config_scenario4_devices_by_serial_number_list = test_data.get(
        "playbook_config_scenario4_devices_by_serial_number_list"
    )
    playbook_config_scenario5_devices_by_mac_address_list = test_data.get(
        "playbook_config_scenario5_devices_by_mac_address_list"
    )
    playbook_config_scenario6_devices_by_role_access = test_data.get(
        "playbook_config_scenario6_devices_by_role_access"
    )
    playbook_config_scenario7_devices_by_role_core = test_data.get(
        "playbook_config_scenario7_devices_by_role_core"
    )
    playbook_config_scenario8_combined_filters_multiple_criteria = test_data.get(
        "playbook_config_scenario8_combined_filters_multiple_criteria"
    )
    playbook_config_scenario9_multiple_device_groups = test_data.get(
        "playbook_config_scenario9_multiple_device_groups"
    )
    playbook_config_scenario10_provision_devices_by_site_with_role_filter = test_data.get(
        "playbook_config_scenario10_provision_devices_by_site_with_role_filter"
    )
    playbook_config_scenario11_multiple_roles = test_data.get(
        "playbook_config_scenario11_multiple_roles"
    )
    playbook_config_scenario12_global_filter_plus_site_filter = test_data.get(
        "playbook_config_scenario12_global_filter_plus_site_filter"
    )
    playbook_config_scenario13_interface_details_single_interface_name_filter = test_data.get(
        "playbook_config_scenario13_interface_details_single_interface_name_filter"
    )
    playbook_config_scenario14_interface_details_multiple_interface_name_filters = test_data.get(
        "playbook_config_scenario14_interface_details_multiple_interface_name_filters"
    )
    playbook_config_scenario15_global_ip_filter_plus_interface_name_filter = test_data.get(
        "playbook_config_scenario15_global_ip_filter_plus_interface_name_filter"
    )
    playbook_config_scenario16_device_details_plus_filtered_interfaces = test_data.get(
        "playbook_config_scenario16_device_details_plus_filtered_interfaces"
    )
    playbook_config_scenario17_all_components_with_interface_filter = test_data.get(
        "playbook_config_scenario17_all_components_with_interface_filter"
    )
    playbook_config_scenario18_interface_filter_no_match_handling = test_data.get(
        "playbook_config_scenario18_interface_filter_no_match_handling"
    )
    playbook_config_scenario19_gigabitethernet_interfaces_only = test_data.get(
        "playbook_config_scenario19_gigabitethernet_interfaces_only"
    )
    playbook_config_scenario20_access_devices_with_interface_filter = test_data.get(
        "playbook_config_scenario20_access_devices_with_interface_filter"
    )

    def setUp(self):
        """Set up test fixtures and mocks."""
        super(TestBrownfieldInventoryPlaybookGenerator, self).setUp()

        self.mock_dnac_init = patch(
            "ansible_collections.cisco.dnac.plugins.module_utils.dnac.DNACSDK.__init__"
        )
        self.run_dnac_init = self.mock_dnac_init.start()
        self.run_dnac_init.side_effect = [None]

        self.mock_dnac_exec = patch(
            "ansible_collections.cisco.dnac.plugins.module_utils.dnac.DNACSDK._exec"
        )
        self.run_dnac_exec = self.mock_dnac_exec.start()

        # Mock file operations
        self.mock_open = patch("builtins.open", create=True)
        self.run_open = self.mock_open.start()

        self.load_fixtures()

    def tearDown(self):
        """Clean up mocks."""
        super(TestBrownfieldInventoryPlaybookGenerator, self).tearDown()
        self.mock_dnac_exec.stop()
        self.mock_dnac_init.stop()
        self.mock_open.stop()

    def load_fixtures(self, response=None, device=""):
        """
        Load fixtures for each scenario.
        """
        if "scenario1_complete_infrastructure" in self._testMethodName:
            # Scenario 1: All devices
            self.run_dnac_exec.side_effect = [
                self.test_data.get("get_all_devices_response")
            ]

        elif "scenario2_specific_devices_by_ip_address" in self._testMethodName:
            # Scenario 2: Specific IPs
            self.run_dnac_exec.side_effect = [
                self.test_data.get("get_filtered_devices_by_ip_response")
            ]

        elif "scenario3_devices_by_hostname" in self._testMethodName:
            # Scenario 3: Hostname filter
            self.run_dnac_exec.side_effect = [
                self.test_data.get("get_filtered_devices_by_hostname_response")
            ]

        elif "scenario4_devices_by_serial_number" in self._testMethodName:
            # Scenario 4: Serial number filter
            self.run_dnac_exec.side_effect = [
                self.test_data.get("get_filtered_devices_by_serial_response")
            ]

        elif "scenario5_devices_by_mac_address" in self._testMethodName:
            # Scenario 5: MAC address filter
            self.run_dnac_exec.side_effect = [
                self.test_data.get("get_filtered_devices_by_mac_response")
            ]

        elif "scenario6_devices_by_role_access" in self._testMethodName:
            # Scenario 6: ACCESS role filter
            self.run_dnac_exec.side_effect = [
                self.test_data.get("get_filtered_devices_by_access_role_response")
            ]

        elif "scenario7_devices_by_role_core" in self._testMethodName:
            # Scenario 7: CORE role filter
            self.run_dnac_exec.side_effect = [
                self.test_data.get("get_filtered_devices_by_core_role_response")
            ]

        elif "scenario8_combined_filters" in self._testMethodName:
            # Scenario 8: Combined filters (IP + role)
            self.run_dnac_exec.side_effect = [
                self.test_data.get("get_filtered_devices_combined_response")
            ]

        elif "scenario9_multiple_device_groups" in self._testMethodName:
            # Scenario 9: Multiple groups
            self.run_dnac_exec.side_effect = [
                self.test_data.get("get_filtered_devices_by_access_role_response"),
                self.test_data.get("get_filtered_devices_by_core_role_response")
            ]

        elif "scenario10_provision_devices_by_site" in self._testMethodName:
            # Scenario 10: Site-based provisioning with role filter
            self.run_dnac_exec.side_effect = [
                self.test_data.get("get_filtered_devices_by_site_response")
            ]

        elif "scenario11_multiple_roles" in self._testMethodName:
            # Scenario 11: Multiple roles filter
            self.run_dnac_exec.side_effect = [
                self.test_data.get("get_filtered_devices_multi_role_response")
            ]

        elif "scenario12_global_filter_plus_site" in self._testMethodName:
            # Scenario 12: Global filter + site filter
            self.run_dnac_exec.side_effect = [
                self.test_data.get("get_filtered_devices_global_site_filter_response")
            ]

        elif "scenario13_interface_details_single_interface" in self._testMethodName:
            # Scenario 13: Interface filter - Single VLAN100
            self.run_dnac_exec.side_effect = [
                self.test_data.get("get_filtered_devices_by_interface_name_vlan100_response")
            ]

        elif "scenario14_interface_details_multiple_interface" in self._testMethodName:
            # Scenario 14: Interface filter - Multiple interfaces
            self.run_dnac_exec.side_effect = [
                self.test_data.get("get_filtered_devices_by_interface_name_multi_response")
            ]

        elif "scenario15_global_ip_filter_plus_interface_name" in self._testMethodName:
            # Scenario 15: IP filter + Interface filter
            self.run_dnac_exec.side_effect = [
                self.test_data.get("get_filtered_devices_by_ip_response")
            ]

        elif "scenario16_device_details_plus_filtered_interfaces" in self._testMethodName:
            # Scenario 16: Device details + filtered interfaces
            self.run_dnac_exec.side_effect = [
                self.test_data.get("get_filtered_devices_by_interface_name_loopback_response")
            ]

        elif "scenario17_all_components_with_interface_filter" in self._testMethodName:
            # Scenario 17: All components with interface filter
            self.run_dnac_exec.side_effect = [
                self.test_data.get("get_all_devices_response")
            ]

        elif "scenario18_interface_filter_no_match_handling" in self._testMethodName:
            # Scenario 18: Interface filter - No match handling
            self.run_dnac_exec.side_effect = [
                {"response": []}
            ]

        elif "scenario19_gigabitethernet_interfaces_only" in self._testMethodName:
            # Scenario 19: GigabitEthernet filter
            self.run_dnac_exec.side_effect = [
                self.test_data.get("get_filtered_devices_by_interface_name_gigabitethernet_response")
            ]

        elif "scenario20_access_devices_with_interface_filter" in self._testMethodName:
            # Scenario 20: ACCESS role devices with interface filter
            self.run_dnac_exec.side_effect = [
                self.test_data.get("get_filtered_devices_access_with_interface_filter_response")
            ]

    def test_brownfield_inventory_playbook_generator_scenario1_complete_infrastructure(self):
        """
        Test case for scenario 1: Complete Infrastructure - Generate All Device Configurations

        Description: Auto-discovers and generates configurations for ALL devices in
                     Cisco Catalyst Center across all device types (Network, Compute, etc.)
        Use Case: Initial migration, complete infrastructure backup, disaster recovery
        Output: Single consolidated YAML with all device IPs, hostnames, serial numbers
        """
        set_module_args(
            dict(
                dnac_host="192.168.1.1",
                dnac_username="admin",
                dnac_password="admin123",
                dnac_verify=False,
                dnac_port=443,
                dnac_version="2.3.3.0",
                dnac_debug=False,
                dnac_log=True,
                dnac_log_level="DEBUG",
                state="gathered",
                config=self.playbook_config_scenario1_complete_infrastructure_generate_all_device_configurations
            )
        )
        result = self.execute_module(changed=False, failed=False)
        self.assertIn("configuration generated successfully", result.get('msg', '').lower() or "success" in result.get('msg', '').lower())

    def test_brownfield_inventory_playbook_generator_scenario2_specific_devices_by_ip_address(self):
        """
        Test case for scenario 2: Specific Devices by IP Address List

        Description: Generate configurations for specific devices using IP addresses
        Use Case: Targeted device migration, specific site provisioning
        Output: YAML with configurations for specified IP addresses only
        """
        set_module_args(
            dict(
                dnac_host="192.168.1.1",
                dnac_username="admin",
                dnac_password="admin123",
                dnac_verify=False,
                dnac_port=443,
                dnac_version="2.3.3.0",
                dnac_debug=False,
                dnac_log=True,
                dnac_log_level="INFO",
                state="gathered",
                config=self.playbook_config_scenario2_specific_devices_by_ip_address_list
            )
        )
        result = self.execute_module(changed=False, failed=False)
        self.assertIn(
            "2",
            str(result.get('device_count', 0))
        )

    def test_brownfield_inventory_playbook_generator_scenario3_devices_by_hostname(self):
        """
        Test case for scenario 3: Devices by Hostname List

        Description: Generate configurations for devices using hostnames
        Use Case: Hostname-based device management, named device groups
        Output: YAML with configurations for specified hostnames
        """
        set_module_args(
            dict(
                dnac_host="192.168.1.1",
                dnac_username="admin",
                dnac_password="admin123",
                dnac_verify=False,
                dnac_port=443,
                dnac_version="2.3.3.0",
                dnac_debug=False,
                dnac_log=True,
                dnac_log_level="INFO",
                state="gathered",
                config=self.playbook_config_scenario3_devices_by_hostname_list
            )
        )
        result = self.execute_module(changed=False, failed=False)
        self.assertIn(
            "3",
            str(result.get('device_count', 0))
        )

    def test_brownfield_inventory_playbook_generator_scenario4_devices_by_serial_number(self):
        """
        Test case for scenario 4: Devices by Serial Number List

        Description: Generate configurations for devices using serial numbers
        Use Case: Asset management, RMA replacement, warranty tracking
        Output: YAML with configurations for specified serial numbers
        """
        set_module_args(
            dict(
                dnac_host="192.168.1.1",
                dnac_username="admin",
                dnac_password="admin123",
                dnac_verify=False,
                dnac_port=443,
                dnac_version="2.3.3.0",
                dnac_debug=False,
                dnac_log=True,
                dnac_log_level="INFO",
                state="gathered",
                config=self.playbook_config_scenario4_devices_by_serial_number_list
            )
        )
        result = self.execute_module(changed=False, failed=False)
        self.assertIn(
            "3",
            str(result.get('device_count', 0))
        )

    def test_brownfield_inventory_playbook_generator_scenario5_devices_by_mac_address(self):
        """
        Test case for scenario 5: Devices by MAC Address List

        Description: Generate configurations for devices using MAC addresses
        Use Case: MAC-based device discovery, Layer 2 device management
        Output: YAML with configurations for specified MAC addresses
        """
        set_module_args(
            dict(
                dnac_host="192.168.1.1",
                dnac_username="admin",
                dnac_password="admin123",
                dnac_verify=False,
                dnac_port=443,
                dnac_version="2.3.3.0",
                dnac_debug=False,
                dnac_log=True,
                dnac_log_level="INFO",
                state="gathered",
                config=self.playbook_config_scenario5_devices_by_mac_address_list
            )
        )
        result = self.execute_module(changed=False, failed=False)
        self.assertIn(
            "2",
            str(result.get('device_count', 0))
        )

    def test_brownfield_inventory_playbook_generator_scenario6_devices_by_role_access(self):
        """
        Test case for scenario 6: Devices by Role - ACCESS

        Description: Generate configurations for devices with ACCESS role
        Use Case: Access layer device management, edge device provisioning
        Output: YAML with ACCESS role device configurations
        """
        set_module_args(
            dict(
                dnac_host="192.168.1.1",
                dnac_username="admin",
                dnac_password="admin123",
                dnac_verify=False,
                dnac_port=443,
                dnac_version="2.3.3.0",
                dnac_debug=False,
                dnac_log=True,
                dnac_log_level="INFO",
                state="gathered",
                config=self.playbook_config_scenario6_devices_by_role_access
            )
        )
        result = self.execute_module(changed=False, failed=False)
        self.assertIn(
            "ACCESS",
            str(result.get('role_filter', ''))
        )

    def test_brownfield_inventory_playbook_generator_scenario7_devices_by_role_core(self):
        """
        Test case for scenario 7: Devices by Role - CORE

        Description: Generate configurations for devices with CORE role
        Use Case: Core infrastructure management, backbone device configuration
        Output: YAML with CORE role device configurations
        """
        set_module_args(
            dict(
                dnac_host="192.168.1.1",
                dnac_username="admin",
                dnac_password="admin123",
                dnac_verify=False,
                dnac_port=443,
                dnac_version="2.3.3.0",
                dnac_debug=False,
                dnac_log=True,
                dnac_log_level="INFO",
                state="gathered",
                config=self.playbook_config_scenario7_devices_by_role_core
            )
        )
        result = self.execute_module(changed=False, failed=False)
        self.assertIn(
            "CORE",
            str(result.get('role_filter', ''))
        )

    def test_brownfield_inventory_playbook_generator_scenario8_combined_filters(self):
        """
        Test case for scenario 8: Combined Filters - Multiple Criteria

        Description: Generate configurations using multiple filter criteria simultaneously
        Use Case: Complex device selection, multi-criteria filtering
        Output: YAML with devices matching ALL specified criteria
        """
        set_module_args(
            dict(
                dnac_host="192.168.1.1",
                dnac_username="admin",
                dnac_password="admin123",
                dnac_verify=False,
                dnac_port=443,
                dnac_version="2.3.3.0",
                dnac_debug=False,
                dnac_log=True,
                dnac_log_level="INFO",
                state="gathered",
                config=self.playbook_config_scenario8_combined_filters_multiple_criteria
            )
        )
        result = self.execute_module(changed=False, failed=False)
        self.assertIn(
            "1",
            str(result.get('device_count', 0))
        )

    def test_brownfield_inventory_playbook_generator_scenario9_multiple_device_groups(self):
        """
        Test case for scenario 9: Multiple Device Groups

        Description: Generate configurations for multiple device groups with different criteria
        Use Case: Multi-site deployment, different device categories
        Output: Multiple YAML files for different device groups
        """
        set_module_args(
            dict(
                dnac_host="192.168.1.1",
                dnac_username="admin",
                dnac_password="admin123",
                dnac_verify=False,
                dnac_port=443,
                dnac_version="2.3.3.0",
                dnac_debug=False,
                dnac_log=True,
                dnac_log_level="INFO",
                state="gathered",
                config=self.playbook_config_scenario9_multiple_device_groups
            )
        )
        result = self.execute_module(changed=False, failed=False)
        self.assertIn(
            "5",
            str(result.get('total_device_count', 0))
        )

    def test_brownfield_inventory_playbook_generator_scenario10_provision_devices_by_site(self):
        """
        Test case for scenario 10: Provision Devices by Site with Role Filter

        Description: Generate configurations for devices at a specific site with role filtering
        Use Case: Site-specific device provisioning, location-based device management
        Output: YAML with devices from specified site matching role criteria
        """
        set_module_args(
            dict(
                dnac_host="192.168.1.1",
                dnac_username="admin",
                dnac_password="admin123",
                dnac_verify=False,
                dnac_port=443,
                dnac_version="2.3.3.0",
                dnac_debug=False,
                dnac_log=True,
                dnac_log_level="INFO",
                state="gathered",
                config=self.playbook_config_scenario10_provision_devices_by_site_with_role_filter
            )
        )
        result = self.execute_module(changed=False, failed=False)
        self.assertIn(
            "2",
            str(result.get('device_count', 0))
        )

    def test_brownfield_inventory_playbook_generator_scenario11_multiple_roles(self):
        """
        Test case for scenario 11: Multiple Roles

        Description: Generate configurations for devices with multiple role types
        Use Case: Multi-layer device management, combined ACCESS and CORE devices
        Output: YAML with devices matching any of the specified roles
        """
        set_module_args(
            dict(
                dnac_host="192.168.1.1",
                dnac_username="admin",
                dnac_password="admin123",
                dnac_verify=False,
                dnac_port=443,
                dnac_version="2.3.3.0",
                dnac_debug=False,
                dnac_log=True,
                dnac_log_level="INFO",
                state="gathered",
                config=self.playbook_config_scenario11_multiple_roles
            )
        )
        result = self.execute_module(changed=False, failed=False)
        self.assertIn(
            "5",
            str(result.get('device_count', 0))
        )

    def test_brownfield_inventory_playbook_generator_scenario12_global_filter_plus_site(self):
        """
        Test case for scenario 12: Global Filter Plus Site Filter

        Description: Generate configurations using both global IP filters and site-specific filters
        Use Case: Complex filtering combining network and location criteria
        Output: YAML with devices matching both IP list and site location
        """
        set_module_args(
            dict(
                dnac_host="192.168.1.1",
                dnac_username="admin",
                dnac_password="admin123",
                dnac_verify=False,
                dnac_port=443,
                dnac_version="2.3.3.0",
                dnac_debug=False,
                dnac_log=True,
                dnac_log_level="INFO",
                state="gathered",
                config=self.playbook_config_scenario12_global_filter_plus_site_filter
            )
        )
        result = self.execute_module(changed=False, failed=False)
        self.assertIn(
            "2",
            str(result.get('device_count', 0))
        )

    # Additional edge case and error scenario tests

    def test_brownfield_inventory_playbook_generator_invalid_ip_address(self):
        """
        Test case for invalid IP address format in filter

        This test validates that the module properly handles invalid IP address
        formats and returns appropriate error messages.
        """
        set_module_args(
            dict(
                dnac_host="192.168.1.1",
                dnac_username="admin",
                dnac_password="admin123",
                dnac_verify=False,
                dnac_port=443,
                dnac_version="2.3.3.0",
                dnac_debug=False,
                state="gathered",
                config=[
                    {
                        "generate_all_configurations": False,
                        "file_path": "/tmp/test.yml",
                        "global_filters": {
                            "ip_address_list": [
                                "999.999.999.999"
                            ]
                        }
                    }
                ]
            )
        )
        result = self.execute_module(changed=False, failed=True)
        self.assertIn(
            "Invalid IP address format",
            result.get('msg', '')
        )

    def test_brownfield_inventory_playbook_generator_device_not_found(self):
        """
        Test case for device not found scenario

        This test validates that the module properly handles the scenario where
        no devices match the specified filter criteria.
        """
        self.run_dnac_exec.side_effect = [
            {"response": []}
        ]

        set_module_args(
            dict(
                dnac_host="192.168.1.1",
                dnac_username="admin",
                dnac_password="admin123",
                dnac_verify=False,
                dnac_port=443,
                dnac_version="2.3.3.0",
                dnac_debug=False,
                state="gathered",
                config=[
                    {
                        "generate_all_configurations": False,
                        "file_path": "/tmp/test.yml",
                        "global_filters": {
                            "hostname_list": [
                                "nonexistent-device.example.com"
                            ]
                        }
                    }
                ]
            )
        )
        result = self.execute_module(changed=False, failed=True)
        self.assertIn(
            "No devices found matching criteria",
            result.get('msg', '')
        )

    def test_brownfield_inventory_playbook_generator_invalid_role(self):
        """
        Test case for invalid role filter value

        This test validates that the module properly handles invalid role values
        in the component_specific_filters configuration.
        """
        set_module_args(
            dict(
                dnac_host="192.168.1.1",
                dnac_username="admin",
                dnac_password="admin123",
                dnac_verify=False,
                dnac_port=443,
                dnac_version="2.3.3.0",
                dnac_debug=False,
                state="gathered",
                config=[
                    {
                        "file_path": "/tmp/test.yml",
                        "component_specific_filters": {
                            "components_list": ["inventory_workflow_manager"],
                            "inventory_workflow_manager": [
                                {
                                    "role": "INVALID_ROLE"
                                }
                            ]
                        }
                    }
                ]
            )
        )
        result = self.execute_module(changed=False, failed=True)
        self.assertIn(
            "Invalid role value",
            result.get('msg', '')
        )

    def test_brownfield_inventory_playbook_generator_scenario13_interface_details_single_interface(self):
        """
        Test case for scenario 13: Interface Details - Single Interface Name Filter

        Description: Filter interface_details to include only specific interface names
        Use Case: Focus on specific VLAN or Loopback interface configuration
        Output: Single document with only specified interface names (e.g., Vlan100)
        """
        set_module_args(
            dict(
                dnac_host="192.168.1.1",
                dnac_username="admin",
                dnac_password="admin123",
                dnac_verify=False,
                dnac_port=443,
                dnac_version="2.3.3.0",
                dnac_debug=False,
                dnac_log=True,
                dnac_log_level="INFO",
                state="gathered",
                config=self.playbook_config_scenario13_interface_details_single_interface_name_filter
            )
        )
        result = self.execute_module(changed=False, failed=False)
        self.assertIn(
            "interface_name",
            str(result.get('filter_type', ''))
        )

    def test_brownfield_inventory_playbook_generator_scenario14_interface_details_multiple_interface(self):
        """
        Test case for scenario 14: Interface Details - Multiple Interface Name Filters

        Description: Filter interface_details to include multiple specific interface names
        Use Case: Audit and configure multiple critical interfaces across all devices
        Output: Single document with only specified interface names (Vlan100, Loopback0, etc.)
        """
        set_module_args(
            dict(
                dnac_host="192.168.1.1",
                dnac_username="admin",
                dnac_password="admin123",
                dnac_verify=False,
                dnac_port=443,
                dnac_version="2.3.3.0",
                dnac_debug=False,
                dnac_log=True,
                dnac_log_level="INFO",
                state="gathered",
                config=self.playbook_config_scenario14_interface_details_multiple_interface_name_filters
            )
        )
        result = self.execute_module(changed=False, failed=False)
        self.assertIn(
            "3",
            str(result.get('interface_count', 0))
        )

    def test_brownfield_inventory_playbook_generator_scenario15_global_ip_filter_plus_interface_name(self):
        """
        Test case for scenario 15: Global IP Filter + Interface Name Filter

        Description: Combine global IP filter with specific interface name filter
        Use Case: Get specific interfaces only from targeted devices
        Output: Single document with only specified IPs and specified interfaces
        """
        set_module_args(
            dict(
                dnac_host="192.168.1.1",
                dnac_username="admin",
                dnac_password="admin123",
                dnac_verify=False,
                dnac_port=443,
                dnac_version="2.3.3.0",
                dnac_debug=False,
                dnac_log=True,
                dnac_log_level="INFO",
                state="gathered",
                config=self.playbook_config_scenario15_global_ip_filter_plus_interface_name_filter
            )
        )
        result = self.execute_module(changed=False, failed=False)
        self.assertIn(
            "3",
            str(result.get('ip_count', 0))
        )

    def test_brownfield_inventory_playbook_generator_scenario16_device_details_plus_filtered_interfaces(self):
        """
        Test case for scenario 16: Device Details + Filtered Interfaces

        Description: Generate device credentials and only specific interfaces
        Use Case: Onboard devices and configure specific interfaces simultaneously
        Output: 2 documents - device details and filtered interface configs
        """
        set_module_args(
            dict(
                dnac_host="192.168.1.1",
                dnac_username="admin",
                dnac_password="admin123",
                dnac_verify=False,
                dnac_port=443,
                dnac_version="2.3.3.0",
                dnac_debug=False,
                dnac_log=True,
                dnac_log_level="INFO",
                state="gathered",
                config=self.playbook_config_scenario16_device_details_plus_filtered_interfaces
            )
        )
        result = self.execute_module(changed=False, failed=False)
        self.assertIn(
            "2",
            str(result.get('components_count', 0))
        )

    def test_brownfield_inventory_playbook_generator_scenario17_all_components_with_interface_filter(self):
        """
        Test case for scenario 17: All Components with Interface Filter

        Description: Generate all three components with interface_details filtered by name
        Use Case: Complete infrastructure migration with controlled interface updates
        Output: 3 documents - device details, provision config, and filtered interfaces
        """
        set_module_args(
            dict(
                dnac_host="192.168.1.1",
                dnac_username="admin",
                dnac_password="admin123",
                dnac_verify=False,
                dnac_port=443,
                dnac_version="2.3.3.0",
                dnac_debug=False,
                dnac_log=True,
                dnac_log_level="INFO",
                state="gathered",
                config=self.playbook_config_scenario17_all_components_with_interface_filter
            )
        )
        result = self.execute_module(changed=False, failed=False)
        self.assertIn(
            "3",
            str(result.get('components_count', 0))
        )

    def test_brownfield_inventory_playbook_generator_scenario18_interface_filter_no_match_handling(self):
        """
        Test case for scenario 18: Interface Filter - No Match Handling

        Description: Filter interfaces that may not exist on all devices
        Use Case: Handle scenarios where some devices don't have specified interfaces
        Output: Only generates configs for devices that have the specified interfaces
        """
        set_module_args(
            dict(
                dnac_host="192.168.1.1",
                dnac_username="admin",
                dnac_password="admin123",
                dnac_verify=False,
                dnac_port=443,
                dnac_version="2.3.3.0",
                dnac_debug=False,
                dnac_log=True,
                dnac_log_level="INFO",
                state="gathered",
                config=self.playbook_config_scenario18_interface_filter_no_match_handling
            )
        )
        result = self.execute_module(changed=False, failed=False)
        self.assertIn(
            "0",
            str(result.get('device_count', 0))
        )

    def test_brownfield_inventory_playbook_generator_scenario19_gigabitethernet_interfaces_only(self):
        """
        Test case for scenario 19: GigabitEthernet Interfaces Only

        Description: Filter for physical GigabitEthernet interfaces only
        Use Case: Configure access ports or uplinks specifically
        Output: Single document with GigabitEthernet interface configs only
        """
        set_module_args(
            dict(
                dnac_host="192.168.1.1",
                dnac_username="admin",
                dnac_password="admin123",
                dnac_verify=False,
                dnac_port=443,
                dnac_version="2.3.3.0",
                dnac_debug=False,
                dnac_log=True,
                dnac_log_level="INFO",
                state="gathered",
                config=self.playbook_config_scenario19_gigabitethernet_interfaces_only
            )
        )
        result = self.execute_module(changed=False, failed=False)
        self.assertIn(
            "GigabitEthernet",
            str(result.get('interface_type', ''))
        )

    def test_brownfield_inventory_playbook_generator_scenario20_access_devices_with_interface_filter(self):
        """
        Test case for scenario 20: ACCESS Devices with Specific Interface Filter

        Description: Get ACCESS role devices and filter their specific interfaces
        Use Case: Configure access layer devices with specific interface updates
        Output: 2 documents - filtered device details (ACCESS only) and their interfaces
        """
        set_module_args(
            dict(
                dnac_host="192.168.1.1",
                dnac_username="admin",
                dnac_password="admin123",
                dnac_verify=False,
                dnac_port=443,
                dnac_version="2.3.3.0",
                dnac_debug=False,
                dnac_log=True,
                dnac_log_level="INFO",
                state="gathered",
                config=self.playbook_config_scenario20_access_devices_with_interface_filter
            )
        )
        result = self.execute_module(changed=False, failed=False)
        self.assertIn(
            "ACCESS",
            str(result.get('role_filter', ''))
        )

    def test_brownfield_inventory_playbook_generator_dnac_connection_failure(self):
        """
        Test case for DNAC connection failure

        This test validates that the module properly handles connection failures
        to Cisco DNA Center and returns appropriate error messages.
        """
        self.run_dnac_init.side_effect = Exception("Unable to connect to Cisco DNA Center")

        set_module_args(
            dict(
                dnac_host="invalid.host.example.com",
                dnac_username="admin",
                dnac_password="admin123",
                dnac_verify=False,
                state="gathered",
                config=[
                    {
                        "generate_all_configurations": True,
                        "file_path": "/tmp/test.yml"
                    }
                ]
            )
        )
        result = self.execute_module(changed=False, failed=True)
        self.assertIn(
            "Unable to connect to Cisco DNA Center",
            result.get('msg', '')
        )
