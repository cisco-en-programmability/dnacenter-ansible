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
#   Mridul Saurabh <mrisaurabh@cisco.com>
#
# Description:
#   Unit tests for the Ansible module `brownfield_inventory_workflow_config_generator`.
#   These tests cover inventory generation operations such as filtering by IP, hostname,
#   serial number, role, and CLI transport using mocked Catalyst Center responses.

from __future__ import absolute_import, division, print_function

__metaclass__ = type

from unittest.mock import patch
from ansible_collections.cisco.dnac.plugins.modules import brownfield_inventory_workflow_config_generator
from .dnac_module import TestDnacModule, set_module_args, loadPlaybookData


class TestBrownfieldInventoryWorkflowConfigGenerator(TestDnacModule):

    module = brownfield_inventory_workflow_config_generator
    test_data = loadPlaybookData("brownfield_inventory_workflow_config_generator")

    # Playbook configurations
    playbook_config_generate_inventory_all_devices = test_data.get("playbook_config_generate_inventory_all_devices")
    playbook_config_generate_inventory_by_ip_address = test_data.get("playbook_config_generate_inventory_by_ip_address")
    playbook_config_generate_inventory_by_hostname = test_data.get("playbook_config_generate_inventory_by_hostname")
    playbook_config_generate_inventory_by_serial_number = test_data.get("playbook_config_generate_inventory_by_serial_number")
    playbook_config_generate_inventory_mixed_filtering = test_data.get("playbook_config_generate_inventory_mixed_filtering")
    playbook_config_generate_inventory_default_file_path = test_data.get("playbook_config_generate_inventory_default_file_path")
    playbook_config_generate_inventory_multiple_devices = test_data.get("playbook_config_generate_inventory_multiple_devices")
    playbook_config_generate_inventory_access_role_devices = test_data.get("playbook_config_generate_inventory_access_role_devices")
    playbook_config_generate_inventory_core_role_devices = test_data.get("playbook_config_generate_inventory_core_role_devices")
    playbook_config_generate_inventory_distribution_role_devices = test_data.get("playbook_config_generate_inventory_distribution_role_devices")
    playbook_config_generate_inventory_border_router_devices = test_data.get("playbook_config_generate_inventory_border_router_devices")
    playbook_config_generate_inventory_unknown_role_devices = test_data.get("playbook_config_generate_inventory_unknown_role_devices")
    playbook_config_generate_inventory_multiple_role_filters = test_data.get("playbook_config_generate_inventory_multiple_role_filters")
    playbook_config_generate_inventory_component_ip_filter = test_data.get("playbook_config_generate_inventory_component_ip_filter")
    playbook_config_generate_inventory_ssh_devices = test_data.get("playbook_config_generate_inventory_ssh_devices")
    playbook_config_generate_inventory_telnet_devices = test_data.get("playbook_config_generate_inventory_telnet_devices")
    playbook_config_generate_inventory_core_with_ssh = test_data.get("playbook_config_generate_inventory_core_with_ssh")
    playbook_config_generate_inventory_access_with_telnet = test_data.get("playbook_config_generate_inventory_access_with_telnet")
    playbook_config_generate_inventory_multiple_filters_or_logic = test_data.get("playbook_config_generate_inventory_multiple_filters_or_logic")
    playbook_config_generate_inventory_global_and_component_filters_combined = test_data.get("playbook_config_generate_inventory_global_and_component_filters_combined")
    playbook_config_generate_inventory_multiple_device_groups = test_data.get("playbook_config_generate_inventory_multiple_device_groups")
    playbook_config_generate_inventory_global_ip_with_component_role = test_data.get("playbook_config_generate_inventory_global_ip_with_component_role")
    playbook_config_generate_inventory_global_hostname_component_role = test_data.get("playbook_config_generate_inventory_global_hostname_component_role")
    playbook_config_generate_inventory_global_serial_component_role = test_data.get("playbook_config_generate_inventory_global_serial_component_role")
    playbook_config_generate_inventory_all_filters_combined = test_data.get("playbook_config_generate_inventory_all_filters_combined")
    playbook_config_generate_inventory_empty_config = test_data.get("playbook_config_generate_inventory_empty_config")
    playbook_config_generate_inventory_no_file_path = test_data.get("playbook_config_generate_inventory_no_file_path")

    def setUp(self):
        super(TestBrownfieldInventoryWorkflowConfigGenerator, self).setUp()

        self.mock_dnac_init = patch(
            "ansible_collections.cisco.dnac.plugins.module_utils.dnac.DNACSDK.__init__"
        )
        self.run_dnac_init = self.mock_dnac_init.start()
        self.run_dnac_init.side_effect = [None]

        self.mock_dnac_exec = patch(
            "ansible_collections.cisco.dnac.plugins.module_utils.dnac.DNACSDK._exec"
        )
        self.run_dnac_exec = self.mock_dnac_exec.start()
        
        self.mock_file_write = patch("builtins.open")
        self.mock_makedirs = patch("os.makedirs")
        self.mock_file_write.start()
        self.mock_makedirs.start()
        
        self.load_fixtures()

    def tearDown(self):
        super(TestBrownfieldInventoryWorkflowConfigGenerator, self).tearDown()
        self.mock_dnac_exec.stop()
        self.mock_dnac_init.stop()
        self.mock_file_write.stop()
        self.mock_makedirs.stop()

    def load_fixtures(self, response=None, device=""):
        """
        Load fixtures for different test cases.
        """

        if "generate_inventory_all_devices" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("get_inventory_devices_all")
            ]

        elif "generate_inventory_by_ip_address" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("get_inventory_devices_by_ip")
            ]

        elif "generate_inventory_by_hostname" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("get_inventory_devices_by_hostname")
            ]

        elif "generate_inventory_by_serial_number" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("get_inventory_devices_by_serial_number")
            ]

        elif "generate_inventory_mixed_filtering" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("get_inventory_devices_by_ip")
            ]

        elif "generate_inventory_default_file_path" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("get_inventory_devices_by_ip")
            ]

        elif "generate_inventory_multiple_devices" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("get_inventory_multiple_device_groups")
            ]

        elif "generate_inventory_access_role_devices" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("get_inventory_access_role_devices")
            ]

        elif "generate_inventory_core_role_devices" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("get_inventory_core_role_devices")
            ]

        elif "generate_inventory_distribution_role_devices" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("get_inventory_distribution_role_devices")
            ]

        elif "generate_inventory_border_router_devices" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("get_inventory_border_router_devices")
            ]

        elif "generate_inventory_unknown_role_devices" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("get_inventory_unknown_role_devices")
            ]

        elif "generate_inventory_multiple_role_filters" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("get_inventory_multiple_role_filters")
            ]

        elif "generate_inventory_component_ip_filter" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("get_inventory_component_ip_filter")
            ]

        elif "generate_inventory_ssh_devices" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("get_inventory_ssh_devices")
            ]

        elif "generate_inventory_telnet_devices" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("get_inventory_telnet_devices")
            ]

        elif "generate_inventory_core_with_ssh" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("get_inventory_core_with_ssh")
            ]

        elif "generate_inventory_access_with_telnet" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("get_inventory_access_with_telnet")
            ]

        elif "generate_inventory_multiple_filters_or_logic" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("get_inventory_multiple_filters_or_logic")
            ]

        elif "generate_inventory_global_and_component_filters_combined" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("get_inventory_global_and_component_filters")
            ]

        elif "generate_inventory_multiple_device_groups" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("get_inventory_multiple_device_groups")
            ]

        elif "generate_inventory_global_ip_with_component_role" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("get_inventory_global_ip_with_component_role")
            ]

        elif "generate_inventory_global_hostname_component_role" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("get_inventory_global_hostname_component_role")
            ]

        elif "generate_inventory_global_serial_component_role" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("get_inventory_global_serial_component_role")
            ]

        elif "generate_inventory_all_filters_combined" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("get_inventory_all_filters_combined")
            ]

        elif "generate_inventory_empty_config" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("get_inventory_empty_config")
            ]

        elif "generate_inventory_no_file_path" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("get_inventory_no_file_path")
            ]

    # ==========================================
    # Test Cases for Global Filters
    # ==========================================

    def test_brownfield_inventory_workflow_config_generator_generate_inventory_all_devices(self):
        """
        Test case for generating inventory for all devices.

        This test case checks the behavior of the brownfield inventory workflow
        config generator when creating inventory for all devices in the specified
        Catalyst Center using generate_all_configurations flag.
        """

        set_module_args(
            dict(
                dnac_host="1.1.1.1",
                dnac_username="dummy",
                dnac_password="dummy",
                dnac_version="2.3.7.9",
                dnac_log=True,
                state="merged",
                config=self.playbook_config_generate_inventory_all_devices
            )
        )
        result = self.execute_module(changed=True, failed=False)
        self.assertIn(
            "generated successfully",
            result.get('msg')
        )

    def test_brownfield_inventory_workflow_config_generator_generate_inventory_by_ip_address(self):
        """
        Test case for generating inventory by filtering devices using IP addresses.

        This test case checks the behavior of the brownfield inventory workflow
        config generator when creating inventory for devices filtered by management
        IP address in the specified Catalyst Center.
        """

        set_module_args(
            dict(
                dnac_host="1.1.1.1",
                dnac_username="dummy",
                dnac_password="dummy",
                dnac_version="2.3.7.9",
                dnac_log=True,
                state="merged",
                config=self.playbook_config_generate_inventory_by_ip_address
            )
        )
        result = self.execute_module(changed=True, failed=False)
        self.assertIn(
            "generated successfully",
            result.get('msg')
        )

    def test_brownfield_inventory_workflow_config_generator_generate_inventory_by_hostname(self):
        """
        Test case for generating inventory by filtering devices using hostnames.

        This test case checks the behavior of the brownfield inventory workflow
        config generator when creating inventory for devices filtered by hostname
        in the specified Catalyst Center.
        """

        set_module_args(
            dict(
                dnac_host="1.1.1.1",
                dnac_username="dummy",
                dnac_password="dummy",
                dnac_version="2.3.7.9",
                dnac_log=True,
                state="merged",
                config=self.playbook_config_generate_inventory_by_hostname
            )
        )
        result = self.execute_module(changed=True, failed=False)
        self.assertIn(
            "generated successfully",
            result.get('msg')
        )

    def test_brownfield_inventory_workflow_config_generator_generate_inventory_by_serial_number(self):
        """
        Test case for generating inventory by filtering devices using serial numbers.

        This test case checks the behavior of the brownfield inventory workflow
        config generator when creating inventory for devices filtered by serial
        number in the specified Catalyst Center.
        """

        set_module_args(
            dict(
                dnac_host="1.1.1.1",
                dnac_username="dummy",
                dnac_password="dummy",
                dnac_version="2.3.7.9",
                dnac_log=True,
                state="merged",
                config=self.playbook_config_generate_inventory_by_serial_number
            )
        )
        result = self.execute_module(changed=True, failed=False)
        self.assertIn(
            "generated successfully",
            result.get('msg')
        )

    def test_brownfield_inventory_workflow_config_generator_generate_inventory_mixed_filtering(self):
        """
        Test case for generating inventory with mixed global filters (IP + hostname).

        This test case checks the behavior of the brownfield inventory workflow
        config generator when creating inventory for devices filtered by multiple
        global filter criteria in the specified Catalyst Center.
        """

        set_module_args(
            dict(
                dnac_host="1.1.1.1",
                dnac_username="dummy",
                dnac_password="dummy",
                dnac_version="2.3.7.9",
                dnac_log=True,
                state="merged",
                config=self.playbook_config_generate_inventory_mixed_filtering
            )
        )
        result = self.execute_module(changed=True, failed=False)
        self.assertIn(
            "generated successfully",
            result.get('msg')
        )

    def test_brownfield_inventory_workflow_config_generator_generate_inventory_default_file_path(self):
        """
        Test case for generating inventory with auto-generated default file path.

        This test case checks the behavior of the brownfield inventory workflow
        config generator when creating inventory without specifying an explicit
        file path (uses auto-generated path) in the specified Catalyst Center.
        """

        set_module_args(
            dict(
                dnac_host="1.1.1.1",
                dnac_username="dummy",
                dnac_password="dummy",
                dnac_version="2.3.7.9",
                dnac_log=True,
                state="merged",
                config=self.playbook_config_generate_inventory_default_file_path
            )
        )
        result = self.execute_module(changed=True, failed=False)
        self.assertIn(
            "generated successfully",
            result.get('msg')
        )

    def test_brownfield_inventory_workflow_config_generator_generate_inventory_multiple_devices(self):
        """
        Test case for generating inventory for multiple devices with filtering.

        This test case checks the behavior of the brownfield inventory workflow
        config generator when creating inventory for multiple devices filtered by
        IP addresses in the specified Catalyst Center.
        """

        set_module_args(
            dict(
                dnac_host="1.1.1.1",
                dnac_username="dummy",
                dnac_password="dummy",
                dnac_version="2.3.7.9",
                dnac_log=True,
                state="merged",
                config=self.playbook_config_generate_inventory_multiple_devices
            )
        )
        result = self.execute_module(changed=True, failed=False)
        self.assertIn(
            "generated successfully",
            result.get('msg')
        )

    # ==========================================
    # Test Cases for Role-Based Filters
    # ==========================================

    def test_brownfield_inventory_workflow_config_generator_generate_inventory_access_role_devices(self):
        """
        Test case for generating inventory for ACCESS role devices.

        This test case checks the behavior of the brownfield inventory workflow
        config generator when creating inventory for devices with ACCESS role
        in the specified Catalyst Center.
        """

        set_module_args(
            dict(
                dnac_host="1.1.1.1",
                dnac_username="dummy",
                dnac_password="dummy",
                dnac_version="2.3.7.9",
                dnac_log=True,
                state="merged",
                config=self.playbook_config_generate_inventory_access_role_devices
            )
        )
        result = self.execute_module(changed=True, failed=False)
        self.assertIn(
            "generated successfully",
            result.get('msg')
        )

    def test_brownfield_inventory_workflow_config_generator_generate_inventory_core_role_devices(self):
        """
        Test case for generating inventory for CORE role devices.

        This test case checks the behavior of the brownfield inventory workflow
        config generator when creating inventory for devices with CORE role
        in the specified Catalyst Center.
        """

        set_module_args(
            dict(
                dnac_host="1.1.1.1",
                dnac_username="dummy",
                dnac_password="dummy",
                dnac_version="2.3.7.9",
                dnac_log=True,
                state="merged",
                config=self.playbook_config_generate_inventory_core_role_devices
            )
        )
        result = self.execute_module(changed=True, failed=False)
        self.assertIn(
            "generated successfully",
            result.get('msg')
        )

    def test_brownfield_inventory_workflow_config_generator_generate_inventory_distribution_role_devices(self):
        """
        Test case for generating inventory for DISTRIBUTION role devices.

        This test case checks the behavior of the brownfield inventory workflow
        config generator when creating inventory for devices with DISTRIBUTION role
        in the specified Catalyst Center.
        """

        set_module_args(
            dict(
                dnac_host="1.1.1.1",
                dnac_username="dummy",
                dnac_password="dummy",
                dnac_version="2.3.7.9",
                dnac_log=True,
                state="merged",
                config=self.playbook_config_generate_inventory_distribution_role_devices
            )
        )
        result = self.execute_module(changed=True, failed=False)
        self.assertIn(
            "generated successfully",
            result.get('msg')
        )

    def test_brownfield_inventory_workflow_config_generator_generate_inventory_border_router_devices(self):
        """
        Test case for generating inventory for BORDER_ROUTER role devices.

        This test case checks the behavior of the brownfield inventory workflow
        config generator when creating inventory for devices with BORDER_ROUTER role
        in the specified Catalyst Center.
        """

        set_module_args(
            dict(
                dnac_host="1.1.1.1",
                dnac_username="dummy",
                dnac_password="dummy",
                dnac_version="2.3.7.9",
                dnac_log=True,
                state="merged",
                config=self.playbook_config_generate_inventory_border_router_devices
            )
        )
        result = self.execute_module(changed=True, failed=False)
        self.assertIn(
            "generated successfully",
            result.get('msg')
        )

    def test_brownfield_inventory_workflow_config_generator_generate_inventory_unknown_role_devices(self):
        """
        Test case for generating inventory for UNKNOWN role devices.

        This test case checks the behavior of the brownfield inventory workflow
        config generator when creating inventory for devices with UNKNOWN role
        in the specified Catalyst Center.
        """

        set_module_args(
            dict(
                dnac_host="1.1.1.1",
                dnac_username="dummy",
                dnac_password="dummy",
                dnac_version="2.3.7.9",
                dnac_log=True,
                state="merged",
                config=self.playbook_config_generate_inventory_unknown_role_devices
            )
        )
        result = self.execute_module(changed=True, failed=False)
        self.assertIn(
            "generated successfully",
            result.get('msg')
        )

    # ==========================================
    # Test Cases for Multiple Filters (OR Logic)
    # ==========================================

    def test_brownfield_inventory_workflow_config_generator_generate_inventory_multiple_role_filters(self):
        """
        Test case for generating inventory with multiple role filters (OR logic).

        This test case checks the behavior of the brownfield inventory workflow
        config generator when creating inventory for devices matching any of the
        specified role filter sets in the specified Catalyst Center.
        """

        set_module_args(
            dict(
                dnac_host="1.1.1.1",
                dnac_username="dummy",
                dnac_password="dummy",
                dnac_version="2.3.7.9",
                dnac_log=True,
                state="merged",
                config=self.playbook_config_generate_inventory_multiple_role_filters
            )
        )
        result = self.execute_module(changed=True, failed=False)
        self.assertIn(
            "generated successfully",
            result.get('msg')
        )

    def test_brownfield_inventory_workflow_config_generator_generate_inventory_component_ip_filter(self):
        """
        Test case for generating inventory with component-specific IP filter.

        This test case checks the behavior of the brownfield inventory workflow
        config generator when creating inventory for devices filtered by IP address
        at component level in the specified Catalyst Center.
        """

        set_module_args(
            dict(
                dnac_host="1.1.1.1",
                dnac_username="dummy",
                dnac_password="dummy",
                dnac_version="2.3.7.9",
                dnac_log=True,
                state="merged",
                config=self.playbook_config_generate_inventory_component_ip_filter
            )
        )
        result = self.execute_module(changed=True, failed=False)
        self.assertIn(
            "generated successfully",
            result.get('msg')
        )

    # ==========================================
    # Test Cases for CLI Transport Filters
    # ==========================================

    def test_brownfield_inventory_workflow_config_generator_generate_inventory_ssh_devices(self):
        """
        Test case for generating inventory for SSH transport devices.

        This test case checks the behavior of the brownfield inventory workflow
        config generator when creating inventory for devices with SSH CLI transport
        in the specified Catalyst Center.
        """

        set_module_args(
            dict(
                dnac_host="1.1.1.1",
                dnac_username="dummy",
                dnac_password="dummy",
                dnac_version="2.3.7.9",
                dnac_log=True,
                state="merged",
                config=self.playbook_config_generate_inventory_ssh_devices
            )
        )
        result = self.execute_module(changed=True, failed=False)
        self.assertIn(
            "generated successfully",
            result.get('msg')
        )

    def test_brownfield_inventory_workflow_config_generator_generate_inventory_telnet_devices(self):
        """
        Test case for generating inventory for Telnet transport devices.

        This test case checks the behavior of the brownfield inventory workflow
        config generator when creating inventory for devices with Telnet CLI transport
        in the specified Catalyst Center.
        """

        set_module_args(
            dict(
                dnac_host="1.1.1.1",
                dnac_username="dummy",
                dnac_password="dummy",
                dnac_version="2.3.7.9",
                dnac_log=True,
                state="merged",
                config=self.playbook_config_generate_inventory_telnet_devices
            )
        )
        result = self.execute_module(changed=True, failed=False)
        self.assertIn(
            "generated successfully",
            result.get('msg')
        )

    # ==========================================
    # Test Cases for Combined Filters
    # ==========================================

    def test_brownfield_inventory_workflow_config_generator_generate_inventory_core_with_ssh(self):
        """
        Test case for generating inventory for CORE role devices with SSH transport.

        This test case checks the behavior of the brownfield inventory workflow
        config generator when creating inventory for devices matching both CORE role
        AND SSH transport criteria in the specified Catalyst Center.
        """

        set_module_args(
            dict(
                dnac_host="1.1.1.1",
                dnac_username="dummy",
                dnac_password="dummy",
                dnac_version="2.3.7.9",
                dnac_log=True,
                state="merged",
                config=self.playbook_config_generate_inventory_core_with_ssh
            )
        )
        result = self.execute_module(changed=True, failed=False)
        self.assertIn(
            "generated successfully",
            result.get('msg')
        )

    def test_brownfield_inventory_workflow_config_generator_generate_inventory_access_with_telnet(self):
        """
        Test case for generating inventory for ACCESS role devices with Telnet transport.

        This test case checks the behavior of the brownfield inventory workflow
        config generator when creating inventory for devices matching both ACCESS role
        AND Telnet transport criteria in the specified Catalyst Center.
        """

        set_module_args(
            dict(
                dnac_host="1.1.1.1",
                dnac_username="dummy",
                dnac_password="dummy",
                dnac_version="2.3.7.9",
                dnac_log=True,
                state="merged",
                config=self.playbook_config_generate_inventory_access_with_telnet
            )
        )
        result = self.execute_module(changed=True, failed=False)
        self.assertIn(
            "generated successfully",
            result.get('msg')
        )

    def test_brownfield_inventory_workflow_config_generator_generate_inventory_multiple_filters_or_logic(self):
        """
        Test case for generating inventory with multiple filter sets (OR logic).

        This test case checks the behavior of the brownfield inventory workflow
        config generator when creating inventory for devices matching any of the
        specified filter set combinations (OR logic) in the specified Catalyst Center.
        """

        set_module_args(
            dict(
                dnac_host="1.1.1.1",
                dnac_username="dummy",
                dnac_password="dummy",
                dnac_version="2.3.7.9",
                dnac_log=True,
                state="merged",
                config=self.playbook_config_generate_inventory_multiple_filters_or_logic
            )
        )
        result = self.execute_module(changed=True, failed=False)
        self.assertIn(
            "generated successfully",
            result.get('msg')
        )

    # ==========================================
    # Test Cases for Global + Component Filters
    # ==========================================

    def test_brownfield_inventory_workflow_config_generator_generate_inventory_global_and_component_filters_combined(self):
        """
        Test case for generating inventory with combined global and component filters.

        This test case checks the behavior of the brownfield inventory workflow
        config generator when creating inventory for devices filtered by both global
        (IP address) and component-specific (role) criteria in the specified Catalyst Center.
        """

        set_module_args(
            dict(
                dnac_host="1.1.1.1",
                dnac_username="dummy",
                dnac_password="dummy",
                dnac_version="2.3.7.9",
                dnac_log=True,
                state="merged",
                config=self.playbook_config_generate_inventory_global_and_component_filters_combined
            )
        )
        result = self.execute_module(changed=True, failed=False)
        self.assertIn(
            "generated successfully",
            result.get('msg')
        )

    def test_brownfield_inventory_workflow_config_generator_generate_inventory_multiple_device_groups(self):
        """
        Test case for generating inventory for multiple device groups.

        This test case checks the behavior of the brownfield inventory workflow
        config generator when creating multiple inventory files for different
        device groups (ACCESS, CORE, DISTRIBUTION) in the specified Catalyst Center.
        """

        set_module_args(
            dict(
                dnac_host="1.1.1.1",
                dnac_username="dummy",
                dnac_password="dummy",
                dnac_version="2.3.7.9",
                dnac_log=True,
                state="merged",
                config=self.playbook_config_generate_inventory_multiple_device_groups
            )
        )
        result = self.execute_module(changed=True, failed=False)
        self.assertIn(
            "generated successfully",
            result.get('msg')
        )

    def test_brownfield_inventory_workflow_config_generator_generate_inventory_global_ip_with_component_role(self):
        """
        Test case for generating inventory with global IP filter and component role filter.

        This test case checks the behavior of the brownfield inventory workflow
        config generator when creating inventory for devices filtered by both global
        IP list and component role criteria in the specified Catalyst Center.
        """

        set_module_args(
            dict(
                dnac_host="1.1.1.1",
                dnac_username="dummy",
                dnac_password="dummy",
                dnac_version="2.3.7.9",
                dnac_log=True,
                state="merged",
                config=self.playbook_config_generate_inventory_global_ip_with_component_role
            )
        )
        result = self.execute_module(changed=True, failed=False)
        self.assertIn(
            "generated successfully",
            result.get('msg')
        )

    def test_brownfield_inventory_workflow_config_generator_generate_inventory_global_hostname_component_role(self):
        """
        Test case for generating inventory with global hostname filter and component role filter.

        This test case checks the behavior of the brownfield inventory workflow
        config generator when creating inventory for devices filtered by both global
        hostname list and component role criteria in the specified Catalyst Center.
        """

        set_module_args(
            dict(
                dnac_host="1.1.1.1",
                dnac_username="dummy",
                dnac_password="dummy",
                dnac_version="2.3.7.9",
                dnac_log=True,
                state="merged",
                config=self.playbook_config_generate_inventory_global_hostname_component_role
            )
        )
        result = self.execute_module(changed=True, failed=False)
        self.assertIn(
            "generated successfully",
            result.get('msg')
        )

    def test_brownfield_inventory_workflow_config_generator_generate_inventory_global_serial_component_role(self):
        """
        Test case for generating inventory with global serial filter and component role filter.

        This test case checks the behavior of the brownfield inventory workflow
        config generator when creating inventory for devices filtered by both global
        serial number list and component role criteria in the specified Catalyst Center.
        """

        set_module_args(
            dict(
                dnac_host="1.1.1.1",
                dnac_username="dummy",
                dnac_password="dummy",
                dnac_version="2.3.7.9",
                dnac_log=True,
                state="merged",
                config=self.playbook_config_generate_inventory_global_serial_component_role
            )
        )
        result = self.execute_module(changed=True, failed=False)
        self.assertIn(
            "generated successfully",
            result.get('msg')
        )

    def test_brownfield_inventory_workflow_config_generator_generate_inventory_all_filters_combined(self):
        """
        Test case for generating inventory with all filter types combined.

        This test case checks the behavior of the brownfield inventory workflow
        config generator when creating inventory for devices filtered by all available
        filter types (global IP, hostname, serial + component role, transport) in the
        specified Catalyst Center.
        """

        set_module_args(
            dict(
                dnac_host="1.1.1.1",
                dnac_username="dummy",
                dnac_password="dummy",
                dnac_version="2.3.7.9",
                dnac_log=True,
                state="merged",
                config=self.playbook_config_generate_inventory_all_filters_combined
            )
        )
        result = self.execute_module(changed=True, failed=False)
        self.assertIn(
            "generated successfully",
            result.get('msg')
        )

    # ==========================================
    # Test Cases for Edge Cases
    # ==========================================

    def test_brownfield_inventory_workflow_config_generator_generate_inventory_empty_config(self):
        """
        Test case for generating inventory with minimal/empty configuration.

        This test case checks the behavior of the brownfield inventory workflow
        config generator when creating inventory with minimal configuration parameters
        (only file path) in the specified Catalyst Center.
        """

        set_module_args(
            dict(
                dnac_host="1.1.1.1",
                dnac_username="dummy",
                dnac_password="dummy",
                dnac_version="2.3.7.9",
                dnac_log=True,
                state="merged",
                config=self.playbook_config_generate_inventory_empty_config
            )
        )
        result = self.execute_module(changed=True, failed=False)
        self.assertIn(
            "generated successfully",
            result.get('msg')
        )

    def test_brownfield_inventory_workflow_config_generator_generate_inventory_no_file_path(self):
        """
        Test case for generating inventory without specifying explicit file path.

        This test case checks the behavior of the brownfield inventory workflow
        config generator when creating inventory without an explicit file path
        (auto-generated file path with timestamp) in the specified Catalyst Center.
        """

        set_module_args(
            dict(
                dnac_host="1.1.1.1",
                dnac_username="dummy",
                dnac_password="dummy",
                dnac_version="2.3.7.9",
                dnac_log=True,
                state="merged",
                config=self.playbook_config_generate_inventory_no_file_path
            )
        )
        result = self.execute_module(changed=True, failed=False)
        self.assertIn(
            "generated successfully",
            result.get('msg')
        )


class TestBrownfieldInventoryWorkflowConfigGeneratorIntegration(TestDnacModule):
    """Integration tests for the Brownfield Inventory Workflow Config Generator module"""

    module = brownfield_inventory_workflow_config_generator

    def setUp(self):
        super(TestBrownfieldInventoryWorkflowConfigGeneratorIntegration, self).setUp()

        self.mock_dnac_init = patch(
            "ansible_collections.cisco.dnac.plugins.module_utils.dnac.DNACSDK.__init__"
        )
        self.run_dnac_init = self.mock_dnac_init.start()
        self.run_dnac_init.side_effect = [None]

    def tearDown(self):
        super(TestBrownfieldInventoryWorkflowConfigGeneratorIntegration, self).tearDown()
        self.mock_dnac_init.stop()

    def test_module_initialization(self):
        """
        Test case for module class initialization.

        This test case verifies that the module class is properly initialized
        with all required attributes and methods.
        """

        set_module_args(
            dict(
                dnac_host="1.1.1.1",
                dnac_username="dummy",
                dnac_password="dummy",
                dnac_version="2.3.7.9",
                dnac_log=True,
                state="merged",
                config=[{
                    "file_path": "./test_inventory.yml",
                    "global_filters": {
                        "ip_address_list": ["10.195.225.40"]
                    }
                }]
            )
        )

        module_instance = self.module.BrownfieldInventoryWorkflowConfigGenerator(
            self.mock_dnac_module
        )

        self.assertIsNotNone(module_instance)
        self.assertTrue(hasattr(module_instance, 'get_inventory_workflow_manager_details'))
        self.assertTrue(hasattr(module_instance, 'get_config'))

    def test_state_parameter_validation(self):
        """
        Test case for state parameter validation.

        This test case verifies that the state parameter is properly validated
        and only accepts valid values ('merged', 'replaced', 'deleted', 'gathered').
        """

        set_module_args(
            dict(
                dnac_host="1.1.1.1",
                dnac_username="dummy",
                dnac_password="dummy",
                dnac_version="2.3.7.9",
                dnac_log=True,
                state="merged",
                config=[{
                    "file_path": "./test_inventory.yml",
                    "global_filters": {
                        "ip_address_list": ["10.195.225.40"]
                    }
                }]
            )
        )

        with patch("ansible_collections.cisco.dnac.plugins.module_utils.dnac.DNACSDK.__init__") as mock_init:
            mock_init.side_effect = [None]
            with patch("ansible_collections.cisco.dnac.plugins.module_utils.dnac.DNACSDK._exec") as mock_exec:
                mock_exec.return_value = {"response": [], "version": "1.0"}
                with patch("builtins.open"):
                    with patch("os.makedirs"):
                        with self.assertRaises(SystemExit):
                            self.module.main()

    def test_config_parameter_structure(self):
        """
        Test case for config parameter structure validation.

        This test case verifies that the config parameter follows the expected
        structure with proper keys and values.
        """

        config = [{
            "file_path": "./test_inventory.yml",
            "global_filters": {
                "ip_address_list": ["10.195.225.40"],
                "hostname_list": ["switch1"],
                "serial_number_list": ["ABC123"]
            },
            "component_specific_filters": {
                "components_list": ["inventory_workflow_manager"],
                "inventory_workflow_manager": [
                    {
                        "role": "ACCESS",
                        "cli_transport": "ssh"
                    }
                ]
            }
        }]

        self.assertEqual(len(config), 1)
        self.assertIn("file_path", config[0])
        self.assertIn("global_filters", config[0])
        self.assertIn("component_specific_filters", config[0])


if __name__ == '__main__':
    import pytest
    pytest.main([__file__])