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
#   Megha Kandari <kandarimegha@cisco.com>
#   Madhan Sankaranarayanan <madhansansel@cisco.com>
#
# Description:
#   Unit tests for the Ansible module `network_settings_playbook_config_generator`.
#   These tests cover various scenarios for generating YAML playbooks from network
#   settings configurations including global pools, reserve pools, network management settings,
#   device controllability settings, and AAA settings.

from __future__ import absolute_import, division, print_function

__metaclass__ = type
from unittest.mock import patch, mock_open
from ansible_collections.cisco.dnac.plugins.modules import network_settings_playbook_config_generator
from .dnac_module import TestDnacModule, set_module_args, loadPlaybookData


class TestNetworkSettingsPlaybookGenerator(TestDnacModule):

    module = network_settings_playbook_config_generator
    test_data = loadPlaybookData("network_settings_playbook_config_generation")

    # Load all playbook configurations
    playbook_config_generate_all_configurations = test_data.get("playbook_config_generate_all_configurations")
    playbook_config_global_pools_single = test_data.get("playbook_config_global_pools_single")
    playbook_config_global_pools_multiple = test_data.get("playbook_config_global_pools_multiple")
    playbook_config_reserve_pools_by_site_single = test_data.get("playbook_config_reserve_pools_by_site_single")
    playbook_config_reserve_pools_by_pool_name = test_data.get("playbook_config_reserve_pools_by_pool_name")
    playbook_config_network_management_by_site = test_data.get("playbook_config_network_management_by_site")
    playbook_config_device_controllability_by_site = test_data.get("playbook_config_device_controllability_by_site")
    playbook_config_aaa_settings_by_network = test_data.get("playbook_config_aaa_settings_by_network")
    playbook_config_aaa_settings_by_server_type = test_data.get("playbook_config_aaa_settings_by_server_type")
    playbook_config_global_filters_by_site = test_data.get("playbook_config_global_filters_by_site")
    playbook_config_global_filters_by_pool_name = test_data.get("playbook_config_global_filters_by_pool_name")
    playbook_config_global_filters_by_pool_type = test_data.get("playbook_config_global_filters_by_pool_type")
    playbook_config_multiple_components = test_data.get("playbook_config_multiple_components")
    playbook_config_all_components = test_data.get("playbook_config_all_components")
    playbook_config_combined_filters = test_data.get("playbook_config_combined_filters")
    playbook_config_empty_filters = test_data.get("playbook_config_empty_filters")
    playbook_config_no_file_path = test_data.get("playbook_config_no_file_path")

    def setUp(self):
        super(TestNetworkSettingsPlaybookGenerator, self).setUp()

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
        super(TestNetworkSettingsPlaybookGenerator, self).tearDown()
        self.mock_dnac_exec.stop()
        self.mock_dnac_init.stop()

    def load_fixtures(self, response=None, device=""):
        """
        Load fixtures for network settings playbook config generator tests.
        """

        if "auto_discovery" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("get_site_details"),
                self.test_data.get("get_global_pool_response"),
                self.test_data.get("get_reserve_ip_pool_details"),
                self.test_data.get("get_network_management_response"),
                self.test_data.get("get_device_controllability_response"),
                self.test_data.get("get_aaa_settings_response"),
            ]

        elif "global_pools_single" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("get_global_pool_response"),
            ]

        elif "global_pools_multiple" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("get_global_pool_response"),
                self.test_data.get("get_global_pool_response"),
            ]

        elif "reserve_pools_by_site_single" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("get_site_details"),
                self.test_data.get("get_reserve_ip_pool_details"),
            ]

        elif "reserve_pools_by_pool_name" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("get_site_details"),
                self.test_data.get("get_reserve_ip_pool_details"),
            ]

        elif "network_management_by_site" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("get_site_details"),
                self.test_data.get("get_network_management_response"),
                self.test_data.get("get_network_management_response"),
            ]

        elif "device_controllability_by_site" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("get_device_controllability_response"),
            ]

        elif "aaa_settings_by_network" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("get_aaa_settings_response"),
            ]

        elif "aaa_settings_by_server_type" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("get_aaa_settings_response"),
                self.test_data.get("get_aaa_settings_response"),
            ]

        elif "global_filters_by_site" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("get_site_details"),
                self.test_data.get("get_global_pool_response"),
                self.test_data.get("get_reserve_ip_pool_details"),
                self.test_data.get("get_network_management_response"),
                self.test_data.get("get_device_controllability_response"),
            ]

        elif "global_filters_by_pool_name" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("get_global_pool_response"),
                self.test_data.get("get_reserve_ip_pool_details"),
                self.test_data.get("get_network_management_response"),
                self.test_data.get("get_device_controllability_response"),
            ]

        elif "global_filters_by_pool_type" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("get_global_pool_response"),
                self.test_data.get("get_reserve_ip_pool_details"),
                self.test_data.get("get_network_management_response"),
                self.test_data.get("get_device_controllability_response"),
                self.test_data.get("get_global_pool_response"),
            ]

        elif "multiple_components" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("get_site_details"),
                self.test_data.get("get_global_pool_response"),
                self.test_data.get("get_reserve_ip_pool_details"),
                self.test_data.get("get_network_management_response"),
            ]

        elif "all_components" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("get_site_details"),
                self.test_data.get("get_global_pool_response"),
                self.test_data.get("get_reserve_ip_pool_details"),
                self.test_data.get("get_network_management_response"),
                self.test_data.get("get_device_controllability_response"),
            ]

        elif "combined_filters" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("get_site_details"),
                self.test_data.get("get_global_pool_response"),
                self.test_data.get("get_reserve_ip_pool_details"),
            ]

        elif "empty_filters" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("get_global_pool_response"),
            ]

        elif "no_file_path" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("get_global_pool_response"),
            ]

    @patch('builtins.open', new_callable=mock_open)
    @patch('os.path.exists')
    def test_network_settings_playbook_config_generator_auto_discovery(self, mock_exists, mock_file):
        """
        Test case for network settings playbook config generator auto-discovery.

        This test case checks the behavior when config is omitted, which should retrieve all
        supported components and generate a YAML playbook configuration file.
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
                file_path="/tmp/test_demo.yaml",
                file_mode="overwrite"
            )
        )
        result = self.execute_module(changed=True, failed=False)
        self.assertIn("YAML config generation succeeded", str(result.get('msg')))

    @patch('builtins.open', new_callable=mock_open)
    @patch('os.path.exists')
    def test_network_settings_playbook_config_generator_global_pools_single(self, mock_exists, mock_file):
        """
        Test case for generating YAML configuration for a single global pool by pool name.

        This test verifies that the generator correctly retrieves and generates configuration
        for a single global pool when filtered by pool name.
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
                config=self.playbook_config_global_pools_single
            )
        )
        result = self.execute_module(changed=True, failed=False)
        self.assertIn("YAML config generation succeeded", str(result.get('msg')))

    @patch('builtins.open', new_callable=mock_open)
    @patch('os.path.exists')
    def test_network_settings_playbook_config_generator_global_pools_multiple(self, mock_exists, mock_file):
        """
        Test case for generating YAML configuration for multiple global pools by pool names.

        This test verifies that the generator correctly retrieves and generates configuration
        for multiple global pools when filtered by multiple pool names.
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
                config=self.playbook_config_global_pools_multiple
            )
        )
        result = self.execute_module(changed=True, failed=False)
        self.assertIn("YAML config generation succeeded", str(result.get('msg')))

    @patch('builtins.open', new_callable=mock_open)
    @patch('os.path.exists')
    def test_network_settings_playbook_config_generator_reserve_pools_by_site_single(self, mock_exists, mock_file):
        """
        Test case for reserve pools filtered by a single site when the site is not found.

        This test verifies that the generator correctly skips the component
        when the specified site is not found and returns no data.
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
                config=self.playbook_config_reserve_pools_by_site_single
            )
        )
        result = self.execute_module(changed=False, failed=False)
        self.assertIn("No configurations or components to process", str(result.get('msg')))

    @patch('builtins.open', new_callable=mock_open)
    @patch('os.path.exists')
    def test_network_settings_playbook_config_generator_reserve_pools_by_pool_name(self, mock_exists, mock_file):
        """
        Test case for reserve pools filtered by pool names when no pools match.

        This test verifies that the generator correctly skips the component
        when no reserve pools match the specified pool name filters.
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
                config=self.playbook_config_reserve_pools_by_pool_name
            )
        )
        result = self.execute_module(changed=False, failed=False)
        self.assertIn("No configurations or components to process", str(result.get('msg')))

    @patch('builtins.open', new_callable=mock_open)
    @patch('os.path.exists')
    def test_network_settings_playbook_config_generator_network_management_by_site(self, mock_exists, mock_file):
        """
        Test case for network management settings when specified sites are not found.

        This test verifies that the generator correctly skips the component
        when the specified sites are not found and returns no data.
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
                config=self.playbook_config_network_management_by_site
            )
        )
        result = self.execute_module(changed=False, failed=False)
        self.assertIn("No configurations or components to process", str(result.get('msg')))

    @patch('builtins.open', new_callable=mock_open)
    @patch('os.path.exists')
    def test_network_settings_playbook_config_generator_device_controllability_by_site(self, mock_exists, mock_file):
        """
        Test case for generating YAML configuration for device controllability settings filtered by sites.

        This test verifies that the generator correctly retrieves and generates configuration
        for device controllability settings when filtered by specific site names.
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
                config=self.playbook_config_device_controllability_by_site
            )
        )
        result = self.execute_module(changed=True, failed=False)
        self.assertIn("YAML config generation succeeded", str(result.get('msg')))

    @patch('builtins.open', new_callable=mock_open)
    @patch('os.path.exists')
    def test_network_settings_playbook_config_generator_aaa_settings_by_network(self, mock_exists, mock_file):
        """
        Test case for generating YAML configuration for AAA settings filtered by network type.

        This test verifies that the generator correctly rejects aaa_settings as an invalid
        component since it has been removed from the valid components list.
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
                config=self.playbook_config_aaa_settings_by_network
            )
        )
        result = self.execute_module(changed=False, failed=True)
        self.assertIn("Invalid network components", str(result.get('msg', '')))

    @patch('builtins.open', new_callable=mock_open)
    @patch('os.path.exists')
    def test_network_settings_playbook_config_generator_aaa_settings_by_server_type(self, mock_exists, mock_file):
        """
        Test case for generating YAML configuration for AAA settings filtered by server types.

        This test verifies that the generator correctly rejects aaa_settings as an invalid
        component since it has been removed from the valid components list.
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
                config=self.playbook_config_aaa_settings_by_server_type
            )
        )
        result = self.execute_module(changed=False, failed=True)
        self.assertIn("Invalid network components", str(result.get('msg', '')))

    @patch('builtins.open', new_callable=mock_open)
    @patch('os.path.exists')
    def test_network_settings_playbook_config_generator_global_filters_by_site(self, mock_exists, mock_file):
        """
        Test case for generating YAML configuration using global filters by site names.

        This test verifies that global_filters is rejected by strict config validation.
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
                config=self.playbook_config_global_filters_by_site
            )
        )
        result = self.execute_module(changed=False, failed=True)
        self.assertTrue(result.get("failed"))

    @patch('builtins.open', new_callable=mock_open)
    @patch('os.path.exists')
    def test_network_settings_playbook_config_generator_global_filters_by_pool_name(self, mock_exists, mock_file):
        """
        Test case for generating YAML configuration using global filters by pool names.

        This test verifies that generate_all_configurations is rejected by strict config validation.
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
                config=self.playbook_config_global_filters_by_pool_name
            )
        )
        result = self.execute_module(changed=False, failed=True)
        self.assertTrue(result.get("failed"))

    @patch('builtins.open', new_callable=mock_open)
    @patch('os.path.exists')
    def test_network_settings_playbook_config_generator_global_filters_by_pool_type(self, mock_exists, mock_file):
        """
        Test case for generating YAML configuration using global filters by pool types.

        This test verifies that config without component_specific_filters fails validation.
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
                config=self.playbook_config_global_filters_by_pool_type
            )
        )
        result = self.execute_module(changed=False, failed=True)
        self.assertTrue(result.get("failed"))

    @patch('builtins.open', new_callable=mock_open)
    @patch('os.path.exists')
    def test_network_settings_playbook_config_generator_multiple_components(self, mock_exists, mock_file):
        """
        Test case for multiple components when all return empty data.

        This test verifies that the generator correctly skips all components
        when none return meaningful data and does not generate a file.
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
        self.assertIn("YAML config generation succeeded", str(result.get('msg')))

    @patch('builtins.open', new_callable=mock_open)
    @patch('os.path.exists')
    def test_network_settings_playbook_config_generator_all_components(self, mock_exists, mock_file):
        """
        Test case for generating YAML configuration for all network settings components.

        This test verifies that the generator correctly retrieves and generates configuration
        for all available network settings components.
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
        self.assertIn("YAML config generation succeeded", str(result.get('msg')))

    @patch('builtins.open', new_callable=mock_open)
    @patch('os.path.exists')
    def test_network_settings_playbook_config_generator_combined_filters(self, mock_exists, mock_file):
        """
        Test case for combined filters when all filtered components return empty data.

        This test verifies that the generator correctly skips all components
        when combined filters result in no matching data.
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
                config=self.playbook_config_combined_filters
            )
        )
        result = self.execute_module(changed=True, failed=False)
        self.assertIn("YAML config generation succeeded", str(result.get('msg')))

    @patch('builtins.open', new_callable=mock_open)
    @patch('os.path.exists')
    def test_network_settings_playbook_config_generator_empty_filters(self, mock_exists, mock_file):
        """
        Test case for generating YAML configuration with minimal filters.

        This test verifies that the generator correctly handles scenarios where only
        basic component selection is provided without detailed filters.
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
        self.assertIn("YAML config generation succeeded", str(result.get('msg')))

    @patch('builtins.open', new_callable=mock_open)
    @patch('os.path.exists')
    def test_network_settings_playbook_config_generator_no_file_path(self, mock_exists, mock_file):
        """
        Test case for generating YAML configuration without specifying a file path.

        This test verifies that the generator correctly generates a default filename
        when no explicit file path is provided in the configuration.
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
        self.assertIn("YAML config generation succeeded", str(result.get('msg')))

    @patch('builtins.open', new_callable=mock_open)
    @patch('os.path.exists')
    def test_network_settings_playbook_config_generator_empty_components_list_fails(self, mock_exists, mock_file):
        """
        Test case for validation failure when component_specific_filters has only an empty components_list.
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
                config={
                    "component_specific_filters": {
                        "components_list": []
                    }
                }
            )
        )
        result = self.execute_module(changed=False, failed=True)
        self.assertIn("must include a non-empty components_list", str(result.get("msg", "")))
