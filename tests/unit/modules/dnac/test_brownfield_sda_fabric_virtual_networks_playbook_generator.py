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
#   Abhishek Maheswari <abmahesh@cisco.com>
#   Madhan Sankaranarayanan <madhansansel@cisco.com>
#
# Description:
#   Unit tests for the Ansible module `brownfield_sda_fabric_virtual_networks_playbook_generator`.
#   These tests cover various scenarios for generating YAML playbooks from brownfield
#   SDA fabric configurations including fabric VLANs, virtual networks, and anycast gateways.

from __future__ import absolute_import, division, print_function

__metaclass__ = type
from unittest.mock import patch, mock_open
from ansible_collections.cisco.dnac.plugins.modules import brownfield_sda_fabric_virtual_networks_playbook_generator
from .dnac_module import TestDnacModule, set_module_args, loadPlaybookData


class TestBrownfieldFabricVirtualNetworksGenerator(TestDnacModule):

    module = brownfield_sda_fabric_virtual_networks_playbook_generator
    test_data = loadPlaybookData("brownfield_sda_fabric_virtual_networks_playbook_generator")

    # Load all playbook configurations
    playbook_config_generate_all_configurations = test_data.get("playbook_config_generate_all_configurations")
    playbook_config_fabric_vlan_by_vlan_name_single = test_data.get("playbook_config_fabric_vlan_by_vlan_name_single")
    playbook_config_fabric_vlan_by_vlan_name_multiple = test_data.get("playbook_config_fabric_vlan_by_vlan_name_multiple")
    playbook_config_fabric_vlan_by_vlan_id_single = test_data.get("playbook_config_fabric_vlan_by_vlan_id_single")
    playbook_config_fabric_vlan_by_vlan_id_multiple = test_data.get("playbook_config_fabric_vlan_by_vlan_id_multiple")
    playbook_config_fabric_vlan_by_vlan_name_and_id = test_data.get("playbook_config_fabric_vlan_by_vlan_name_and_id")
    playbook_config_fabric_vlan_by_vlan_id_large_values = test_data.get("playbook_config_fabric_vlan_by_vlan_id_large_values")
    playbook_config_virtual_networks_by_vn_name_single = test_data.get("playbook_config_virtual_networks_by_vn_name_single")
    playbook_config_virtual_networks_by_vn_name_multiple = test_data.get("playbook_config_virtual_networks_by_vn_name_multiple")
    playbook_config_anycast_gateways_by_vn_name = test_data.get("playbook_config_anycast_gateways_by_vn_name")
    playbook_config_anycast_gateways_by_ip_pool_name = test_data.get("playbook_config_anycast_gateways_by_ip_pool_name")
    playbook_config_anycast_gateways_by_vlan_id = test_data.get("playbook_config_anycast_gateways_by_vlan_id")
    playbook_config_anycast_gateways_by_vlan_name = test_data.get("playbook_config_anycast_gateways_by_vlan_name")
    playbook_config_anycast_gateways_by_vlan_name_and_id = test_data.get("playbook_config_anycast_gateways_by_vlan_name_and_id")
    playbook_config_anycast_gateways_all_filters = test_data.get("playbook_config_anycast_gateways_all_filters")
    playbook_config_multiple_components = test_data.get("playbook_config_multiple_components")
    playbook_config_all_components = test_data.get("playbook_config_all_components")
    playbook_config_empty_filters = test_data.get("playbook_config_empty_filters")
    playbook_config_no_file_path = test_data.get("playbook_config_no_file_path")

    def setUp(self):
        super(TestBrownfieldFabricVirtualNetworksGenerator, self).setUp()

        self.mock_dnac_init = patch(
            "ansible_collections.cisco.dnac.plugins.module_utils.dnac.DNACSDK.__init__")
        self.run_dnac_init = self.mock_dnac_init.start()
        self.run_dnac_init.side_effect = [None]

        self.mock_dnac_exec = patch(
            "ansible_collections.cisco.dnac.plugins.module_utils.dnac.DNACSDK._exec"
        )
        self.run_dnac_exec = self.mock_dnac_exec.start()

        self.load_fixtures()

    def tearDown(self):
        super(TestBrownfieldFabricVirtualNetworksGenerator, self).tearDown()
        self.mock_dnac_exec.stop()
        self.mock_dnac_init.stop()

    def load_fixtures(self, response=None, device=""):
        """
        Load fixtures for brownfield fabric virtual networks generator tests.
        """

        if "generate_all_configurations" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("get_fabric_vlan_response"),
                self.test_data.get("get_site_details"),
                self.test_data.get("get_fabric_site_details"),
                self.test_data.get("get_virtual_network_response"),
                self.test_data.get("get_site_details"),
                self.test_data.get("get_fabric_site_details"),
                self.test_data.get("get_anycast_gateway_details"),
                self.test_data.get("get_site_details"),
                self.test_data.get("get_fabric_site_details"),
                self.test_data.get("get_reserve_ip_pool_details"),
            ]

        elif "fabric_vlan_by_vlan_name_single" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("get_fabric_vlan_response"),
                self.test_data.get("get_site_details"),
                self.test_data.get("get_fabric_site_details"),
            ]

        elif "fabric_vlan_by_vlan_name_multiple" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("get_fabric_vlan_response"),
                self.test_data.get("get_site_details"),
                self.test_data.get("get_fabric_site_details"),
                self.test_data.get("get_fabric_vlan_response"),
                self.test_data.get("get_site_details"),
                self.test_data.get("get_fabric_site_details"),
            ]

        elif "fabric_vlan_by_vlan_id_single" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("get_fabric_vlan_response"),
                self.test_data.get("get_site_details"),
                self.test_data.get("get_fabric_site_details"),
            ]

        elif "fabric_vlan_by_vlan_id_multiple" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("get_fabric_vlan_response"),
                self.test_data.get("get_site_details"),
                self.test_data.get("get_fabric_site_details"),
                self.test_data.get("get_fabric_vlan_response"),
                self.test_data.get("get_site_details"),
                self.test_data.get("get_fabric_site_details"),
            ]

        elif "fabric_vlan_by_vlan_name_and_id" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("get_fabric_vlan_response"),
                self.test_data.get("get_site_details"),
                self.test_data.get("get_fabric_site_details"),
                self.test_data.get("get_fabric_vlan_response"),
                self.test_data.get("get_site_details"),
                self.test_data.get("get_fabric_site_details"),
            ]

        elif "fabric_vlan_by_vlan_id_large_values" in self._testMethodName:
            # No side effects needed - validation happens before API calls
            pass

        elif "virtual_networks_by_vn_name_single" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("get_virtual_network_response"),
                self.test_data.get("get_site_details"),
                self.test_data.get("get_fabric_site_details"),
            ]

        elif "virtual_networks_by_vn_name_multiple" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("get_virtual_network_response"),
                self.test_data.get("get_site_details"),
                self.test_data.get("get_fabric_site_details"),
                self.test_data.get("get_virtual_network_response"),
                self.test_data.get("get_site_details"),
                self.test_data.get("get_fabric_site_details"),
            ]

        elif "anycast_gateways_by_vn_name" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("get_anycast_gateway_details"),
                self.test_data.get("get_site_details"),
                self.test_data.get("get_fabric_site_details"),
                self.test_data.get("get_reserve_ip_pool_details"),
                self.test_data.get("get_anycast_gateway_details"),
                self.test_data.get("get_site_details"),
                self.test_data.get("get_fabric_site_details"),
                self.test_data.get("get_reserve_ip_pool_details"),
            ]

        elif "anycast_gateways_by_ip_pool_name" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("get_anycast_gateway_details"),
                self.test_data.get("get_site_details"),
                self.test_data.get("get_fabric_site_details"),
                self.test_data.get("get_reserve_ip_pool_details"),
                self.test_data.get("get_anycast_gateway_details"),
                self.test_data.get("get_site_details"),
                self.test_data.get("get_fabric_site_details"),
                self.test_data.get("get_reserve_ip_pool_details"),
            ]

        elif "anycast_gateways_by_vlan_id" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("get_anycast_gateway_details"),
                self.test_data.get("get_site_details"),
                self.test_data.get("get_fabric_site_details"),
                self.test_data.get("get_reserve_ip_pool_details"),
                self.test_data.get("get_anycast_gateway_details"),
                self.test_data.get("get_site_details"),
                self.test_data.get("get_fabric_site_details"),
                self.test_data.get("get_reserve_ip_pool_details"),
                self.test_data.get("get_anycast_gateway_details"),
                self.test_data.get("get_site_details"),
                self.test_data.get("get_fabric_site_details"),
                self.test_data.get("get_reserve_ip_pool_details"),
            ]

        elif "anycast_gateways_by_vlan_name" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("get_anycast_gateway_details"),
                self.test_data.get("get_site_details"),
                self.test_data.get("get_fabric_site_details"),
                self.test_data.get("get_reserve_ip_pool_details"),
                self.test_data.get("get_anycast_gateway_details"),
                self.test_data.get("get_site_details"),
                self.test_data.get("get_fabric_site_details"),
                self.test_data.get("get_reserve_ip_pool_details"),
            ]

        elif "anycast_gateways_by_vlan_name_and_id" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("get_anycast_gateway_details"),
                self.test_data.get("get_site_details"),
                self.test_data.get("get_fabric_site_details"),
                self.test_data.get("get_reserve_ip_pool_details"),
                self.test_data.get("get_anycast_gateway_details"),
                self.test_data.get("get_site_details"),
                self.test_data.get("get_fabric_site_details"),
                self.test_data.get("get_reserve_ip_pool_details"),
            ]

        elif "anycast_gateways_all_filters" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("get_anycast_gateway_details"),
                self.test_data.get("get_site_details"),
                self.test_data.get("get_fabric_site_details"),
                self.test_data.get("get_reserve_ip_pool_details"),
                self.test_data.get("get_anycast_gateway_details"),
                self.test_data.get("get_site_details"),
                self.test_data.get("get_fabric_site_details"),
                self.test_data.get("get_reserve_ip_pool_details"),
            ]

        elif "multiple_components" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("get_fabric_vlan_response"),
                self.test_data.get("get_site_details"),
                self.test_data.get("get_fabric_site_details"),
                self.test_data.get("get_virtual_network_response"),
                self.test_data.get("get_site_details"),
                self.test_data.get("get_fabric_site_details"),
                self.test_data.get("get_anycast_gateway_details"),
                self.test_data.get("get_site_details"),
                self.test_data.get("get_fabric_site_details"),
                self.test_data.get("get_reserve_ip_pool_details"),
            ]

        elif "all_components" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("get_fabric_vlan_response"),
                self.test_data.get("get_site_details"),
                self.test_data.get("get_fabric_site_details"),
                self.test_data.get("get_virtual_network_response"),
                self.test_data.get("get_site_details"),
                self.test_data.get("get_fabric_site_details"),
                self.test_data.get("get_anycast_gateway_details"),
                self.test_data.get("get_site_details"),
                self.test_data.get("get_fabric_site_details"),
                self.test_data.get("get_reserve_ip_pool_details"),
            ]

        elif "empty_filters" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("get_site_details"),
                self.test_data.get("get_fabric_vlan_response"),
                self.test_data.get("get_fabric_site_details"),
                self.test_data.get("get_fabric_site_details"),
            ]

        elif "no_file_path" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("get_fabric_vlan_response"),
                self.test_data.get("get_site_details"),
                self.test_data.get("get_fabric_site_details"),
            ]

    @patch('builtins.open', new_callable=mock_open)
    @patch('os.path.exists')
    def test_brownfield_sda_fabric_virtual_networks_config_generator_generate_all_configurations(self, mock_exists, mock_file):
        """
        Test case for brownfield fabric virtual networks generator when generating all configurations.

        This test case checks the behavior when generate_all_configurations is set to True,
        which should retrieve all fabric VLANs, virtual networks, and anycast gateways and
        generate a complete YAML playbook configuration file.
        """
        mock_exists.return_value = True

        set_module_args(
            dict(
                dnac_host="1.1.1.1",
                dnac_username="dummy",
                dnac_password="dummy",
                dnac_version="2.3.7.9",
                dnac_log=True,
                state="gathered",
                config=self.playbook_config_generate_all_configurations
            )
        )
        result = self.execute_module(changed=True, failed=False)
        self.assertIn("YAML configuration file generated successfully", str(result.get('msg').get("message")))

    @patch('builtins.open', new_callable=mock_open)
    @patch('os.path.exists')
    def test_brownfield_sda_fabric_virtual_networks_config_generator_fabric_vlan_by_vlan_name_single(self, mock_exists, mock_file):
        """
        Test case for generating YAML configuration for a single fabric VLAN by VLAN name.

        This test verifies that the generator correctly retrieves and generates configuration
        for a single fabric VLAN when filtered by VLAN name.
        """
        mock_exists.return_value = True

        set_module_args(
            dict(
                dnac_host="1.1.1.1",
                dnac_username="dummy",
                dnac_password="dummy",
                dnac_version="2.3.7.9",
                dnac_log=True,
                state="gathered",
                config=self.playbook_config_fabric_vlan_by_vlan_name_single
            )
        )
        result = self.execute_module(changed=True, failed=False)
        self.assertIn("YAML configuration file generated successfully", str(result.get('msg').get("message")))

    @patch('builtins.open', new_callable=mock_open)
    @patch('os.path.exists')
    def test_brownfield_sda_fabric_virtual_networks_config_generator_fabric_vlan_by_vlan_name_multiple(self, mock_exists, mock_file):
        """
        Test case for generating YAML configuration for multiple fabric VLANs by VLAN names.

        This test verifies that the generator correctly retrieves and generates configuration
        for multiple fabric VLANs when filtered by multiple VLAN names.
        """
        mock_exists.return_value = True

        set_module_args(
            dict(
                dnac_host="1.1.1.1",
                dnac_username="dummy",
                dnac_password="dummy",
                dnac_version="2.3.7.9",
                dnac_log=True,
                state="gathered",
                config=self.playbook_config_fabric_vlan_by_vlan_name_multiple
            )
        )
        result = self.execute_module(changed=True, failed=False)
        self.assertIn("YAML configuration file generated successfully", str(result.get('msg').get("message")))

    @patch('builtins.open', new_callable=mock_open)
    @patch('os.path.exists')
    def test_brownfield_sda_fabric_virtual_networks_config_generator_fabric_vlan_by_vlan_id_single(self, mock_exists, mock_file):
        """
        Test case for generating YAML configuration for a single fabric VLAN by VLAN ID.

        This test verifies that the generator correctly retrieves and generates configuration
        for a single fabric VLAN when filtered by VLAN ID.
        """
        mock_exists.return_value = True

        set_module_args(
            dict(
                dnac_host="1.1.1.1",
                dnac_username="dummy",
                dnac_password="dummy",
                dnac_version="2.3.7.9",
                dnac_log=True,
                state="gathered",
                config=self.playbook_config_fabric_vlan_by_vlan_id_single
            )
        )
        result = self.execute_module(changed=True, failed=False)
        self.assertIn("YAML configuration file generated successfully", str(result.get('msg').get("message")))

    @patch('builtins.open', new_callable=mock_open)
    @patch('os.path.exists')
    def test_brownfield_sda_fabric_virtual_networks_config_generator_fabric_vlan_by_vlan_id_multiple(self, mock_exists, mock_file):
        """
        Test case for generating YAML configuration for multiple fabric VLANs by VLAN IDs.

        This test verifies that the generator correctly retrieves and generates configuration
        for multiple fabric VLANs when filtered by multiple VLAN IDs.
        """
        mock_exists.return_value = True

        set_module_args(
            dict(
                dnac_host="1.1.1.1",
                dnac_username="dummy",
                dnac_password="dummy",
                dnac_version="2.3.7.9",
                dnac_log=True,
                state="gathered",
                config=self.playbook_config_fabric_vlan_by_vlan_id_multiple
            )
        )
        result = self.execute_module(changed=True, failed=False)
        self.assertIn("YAML configuration file generated successfully", str(result.get('msg').get("message")))

    @patch('builtins.open', new_callable=mock_open)
    @patch('os.path.exists')
    def test_brownfield_sda_fabric_virtual_networks_config_generator_fabric_vlan_by_vlan_name_and_id(self, mock_exists, mock_file):
        """
        Test case for generating YAML configuration for fabric VLANs by both VLAN name and ID.

        This test verifies that the generator correctly retrieves and generates configuration
        when filtering by both VLAN name and VLAN ID combinations.
        """
        mock_exists.return_value = True

        set_module_args(
            dict(
                dnac_host="1.1.1.1",
                dnac_username="dummy",
                dnac_password="dummy",
                dnac_version="2.3.7.9",
                dnac_log=True,
                state="gathered",
                config=self.playbook_config_fabric_vlan_by_vlan_name_and_id
            )
        )
        result = self.execute_module(changed=True, failed=False)
        self.assertIn("YAML configuration file generated successfully", str(result.get('msg').get("message")))

    def test_brownfield_sda_fabric_virtual_networks_config_generator_fabric_vlan_by_vlan_id_large_values(self):
        """
        Test case for validating invalid VLAN ID values.

        This test verifies that the generator properly validates and handles VLAN IDs
        that are outside the acceptable range (2-4094, excluding reserved VLANs).
        """

        set_module_args(
            dict(
                dnac_host="1.1.1.1",
                dnac_username="dummy",
                dnac_password="dummy",
                dnac_version="2.3.7.9",
                dnac_log=True,
                state="gathered",
                config=self.playbook_config_fabric_vlan_by_vlan_id_large_values
            )
        )
        result = self.execute_module(changed=False, failed=True)
        self.assertIn("Invalid vlan_id", result.get('msg'))

    @patch('builtins.open', new_callable=mock_open)
    @patch('os.path.exists')
    def test_brownfield_sda_fabric_virtual_networks_config_generator_virtual_networks_by_vn_name_single(self, mock_exists, mock_file):
        """
        Test case for generating YAML configuration for a single virtual network by VN name.

        This test verifies that the generator correctly retrieves and generates configuration
        for a single virtual network when filtered by VN name.
        """
        mock_exists.return_value = True

        set_module_args(
            dict(
                dnac_host="1.1.1.1",
                dnac_username="dummy",
                dnac_password="dummy",
                dnac_version="2.3.7.9",
                dnac_log=True,
                state="gathered",
                config=self.playbook_config_virtual_networks_by_vn_name_single
            )
        )
        result = self.execute_module(changed=True, failed=False)
        self.assertIn("YAML configuration file generated successfully", str(result.get('msg').get("message")))

    @patch('builtins.open', new_callable=mock_open)
    @patch('os.path.exists')
    def test_brownfield_sda_fabric_virtual_networks_config_generator_virtual_networks_by_vn_name_multiple(self, mock_exists, mock_file):
        """
        Test case for generating YAML configuration for multiple virtual networks by VN names.

        This test verifies that the generator correctly retrieves and generates configuration
        for multiple virtual networks when filtered by multiple VN names.
        """
        mock_exists.return_value = True

        set_module_args(
            dict(
                dnac_host="1.1.1.1",
                dnac_username="dummy",
                dnac_password="dummy",
                dnac_version="2.3.7.9",
                dnac_log=True,
                state="gathered",
                config=self.playbook_config_virtual_networks_by_vn_name_multiple
            )
        )
        result = self.execute_module(changed=True, failed=False)
        self.assertIn("YAML configuration file generated successfully", str(result.get('msg').get("message")))

    @patch('builtins.open', new_callable=mock_open)
    @patch('os.path.exists')
    def test_brownfield_sda_fabric_virtual_networks_config_generator_anycast_gateways_by_vn_name(self, mock_exists, mock_file):
        """
        Test case for generating YAML configuration for anycast gateways by VN name.

        This test verifies that the generator correctly retrieves and generates configuration
        for anycast gateways when filtered by virtual network name.
        """
        mock_exists.return_value = True

        set_module_args(
            dict(
                dnac_host="1.1.1.1",
                dnac_username="dummy",
                dnac_password="dummy",
                dnac_version="2.3.7.9",
                dnac_log=True,
                state="gathered",
                config=self.playbook_config_anycast_gateways_by_vn_name
            )
        )
        result = self.execute_module(changed=True, failed=False)
        self.assertIn("YAML configuration file generated successfully", str(result.get('msg').get("message")))

    @patch('builtins.open', new_callable=mock_open)
    @patch('os.path.exists')
    def test_brownfield_sda_fabric_virtual_networks_config_generator_anycast_gateways_by_ip_pool_name(self, mock_exists, mock_file):
        """
        Test case for generating YAML configuration for anycast gateways by IP pool name.

        This test verifies that the generator correctly retrieves and generates configuration
        for anycast gateways when filtered by IP pool name.
        """
        mock_exists.return_value = True

        set_module_args(
            dict(
                dnac_host="1.1.1.1",
                dnac_username="dummy",
                dnac_password="dummy",
                dnac_version="2.3.7.9",
                dnac_log=True,
                state="gathered",
                config=self.playbook_config_anycast_gateways_by_ip_pool_name
            )
        )
        result = self.execute_module(changed=True, failed=False)
        self.assertIn("YAML configuration file generated successfully", str(result.get('msg').get("message")))

    @patch('builtins.open', new_callable=mock_open)
    @patch('os.path.exists')
    def test_brownfield_sda_fabric_virtual_networks_config_generator_anycast_gateways_by_vlan_id(self, mock_exists, mock_file):
        """
        Test case for generating YAML configuration for anycast gateways by VLAN ID.

        This test verifies that the generator correctly retrieves and generates configuration
        for anycast gateways when filtered by VLAN ID.
        """
        mock_exists.return_value = True

        set_module_args(
            dict(
                dnac_host="1.1.1.1",
                dnac_username="dummy",
                dnac_password="dummy",
                dnac_version="2.3.7.9",
                dnac_log=True,
                state="gathered",
                config=self.playbook_config_anycast_gateways_by_vlan_id
            )
        )
        result = self.execute_module(changed=True, failed=False)
        self.assertIn("YAML configuration file generated successfully", str(result.get('msg').get("message")))

    @patch('builtins.open', new_callable=mock_open)
    @patch('os.path.exists')
    def test_brownfield_sda_fabric_virtual_networks_config_generator_anycast_gateways_by_vlan_name(self, mock_exists, mock_file):
        """
        Test case for generating YAML configuration for anycast gateways by VLAN name.

        This test verifies that the generator correctly retrieves and generates configuration
        for anycast gateways when filtered by VLAN name.
        """
        mock_exists.return_value = True

        set_module_args(
            dict(
                dnac_host="1.1.1.1",
                dnac_username="dummy",
                dnac_password="dummy",
                dnac_version="2.3.7.9",
                dnac_log=True,
                state="gathered",
                config=self.playbook_config_anycast_gateways_by_vlan_name
            )
        )
        result = self.execute_module(changed=True, failed=False)
        self.assertIn("YAML configuration file generated successfully", str(result.get('msg').get("message")))

    @patch('builtins.open', new_callable=mock_open)
    @patch('os.path.exists')
    def test_brownfield_sda_fabric_virtual_networks_config_generator_anycast_gateways_by_vlan_name_and_id(self, mock_exists, mock_file):
        """
        Test case for generating YAML configuration for anycast gateways by VLAN name and ID.

        This test verifies that the generator correctly retrieves and generates configuration
        for anycast gateways when filtered by both VLAN name and ID.
        """
        mock_exists.return_value = True

        set_module_args(
            dict(
                dnac_host="1.1.1.1",
                dnac_username="dummy",
                dnac_password="dummy",
                dnac_version="2.3.7.9",
                dnac_log=True,
                state="gathered",
                config=self.playbook_config_anycast_gateways_by_vlan_name_and_id
            )
        )
        result = self.execute_module(changed=True, failed=False)
        self.assertIn("YAML configuration file generated successfully", str(result.get('msg').get("message")))

    @patch('builtins.open', new_callable=mock_open)
    @patch('os.path.exists')
    def test_brownfield_sda_fabric_virtual_networks_config_generator_anycast_gateways_all_filters(self, mock_exists, mock_file):
        """
        Test case for generating YAML configuration for anycast gateways with all filters.

        This test verifies that the generator correctly handles comprehensive filter combinations
        including VN name, VLAN name, VLAN ID, and IP pool name.
        """
        mock_exists.return_value = True

        set_module_args(
            dict(
                dnac_host="1.1.1.1",
                dnac_username="dummy",
                dnac_password="dummy",
                dnac_version="2.3.7.9",
                dnac_log=True,
                state="gathered",
                config=self.playbook_config_anycast_gateways_all_filters
            )
        )
        result = self.execute_module(changed=True, failed=False)
        self.assertIn("YAML configuration file generated successfully", str(result.get('msg').get("message")))

    @patch('builtins.open', new_callable=mock_open)
    @patch('os.path.exists')
    def test_brownfield_sda_fabric_virtual_networks_config_generator_multiple_components(self, mock_exists, mock_file):
        """
        Test case for generating YAML configuration for multiple component types.

        This test verifies that the generator correctly handles configurations for
        fabric VLANs, virtual networks, and anycast gateways simultaneously.
        """
        mock_exists.return_value = True

        set_module_args(
            dict(
                dnac_host="1.1.1.1",
                dnac_username="dummy",
                dnac_password="dummy",
                dnac_version="2.3.7.9",
                dnac_log=True,
                state="gathered",
                config=self.playbook_config_multiple_components
            )
        )
        result = self.execute_module(changed=True, failed=False)
        self.assertIn("YAML configuration file generated successfully", str(result.get('msg').get("message")))

    @patch('builtins.open', new_callable=mock_open)
    @patch('os.path.exists')
    def test_brownfield_sda_fabric_virtual_networks_config_generator_all_components(self, mock_exists, mock_file):
        """
        Test case for generating YAML configuration for all components.

        This test verifies that the generator correctly handles all component types
        (fabric VLANs, virtual networks, and anycast gateways).
        """
        mock_exists.return_value = True

        set_module_args(
            dict(
                dnac_host="1.1.1.1",
                dnac_username="dummy",
                dnac_password="dummy",
                dnac_version="2.3.7.9",
                dnac_log=True,
                state="gathered",
                config=self.playbook_config_all_components
            )
        )
        result = self.execute_module(changed=True, failed=False)
        self.assertIn("YAML configuration file generated successfully", str(result.get('msg').get("message")))

    @patch('builtins.open', new_callable=mock_open)
    @patch('os.path.exists')
    def test_brownfield_sda_fabric_virtual_networks_config_generator_empty_filters(self, mock_exists, mock_file):
        """
        Test case for generating YAML configuration with empty component filters.

        This test verifies that the generator correctly handles scenarios where
        component filters are specified but empty.
        """
        mock_exists.return_value = True

        set_module_args(
            dict(
                dnac_host="1.1.1.1",
                dnac_username="dummy",
                dnac_password="dummy",
                dnac_version="2.3.7.9",
                dnac_log=True,
                state="gathered",
                config=self.playbook_config_empty_filters
            )
        )
        result = self.execute_module(changed=True, failed=False)
        self.assertIn("YAML configuration file generated successfully", str(result.get('msg').get("message")))

    @patch('builtins.open', new_callable=mock_open)
    @patch('os.path.exists')
    def test_brownfield_sda_fabric_virtual_networks_config_generator_no_file_path(self, mock_exists, mock_file):
        """
        Test case for generating YAML configuration without specifying file path.

        This test verifies that the generator creates a default filename when
        no file path is provided in the configuration.
        """
        mock_exists.return_value = True

        set_module_args(
            dict(
                dnac_host="1.1.1.1",
                dnac_username="dummy",
                dnac_password="dummy",
                dnac_version="2.3.7.9",
                dnac_log=True,
                state="gathered",
                config=self.playbook_config_no_file_path
            )
        )
        result = self.execute_module(changed=True, failed=False)
        self.assertIn("YAML configuration file generated successfully", str(result.get('msg').get("message")))
