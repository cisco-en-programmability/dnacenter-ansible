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
#   Unit tests for the Ansible module `brownfield_network_settings_playbook_generator`.
#   These tests cover various scenarios for generating YAML playbooks from brownfield
#   network settings configurations including global pools, reserve pools, network management settings,
#   device controllability settings, and AAA settings.

from __future__ import absolute_import, division, print_function

__metaclass__ = type
from unittest.mock import patch, mock_open
from ansible_collections.cisco.dnac.plugins.modules import brownfield_network_settings_playbook_generator
from .dnac_module import TestDnacModule, set_module_args, loadPlaybookData


class TestBrownfieldNetworkSettingsGenerator(TestDnacModule):

    module = brownfield_network_settings_playbook_generator
    test_data = loadPlaybookData("brownfield_network_settings_playbook_genration")

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
        super(TestBrownfieldNetworkSettingsGenerator, self).setUp()

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
        super(TestBrownfieldNetworkSettingsGenerator, self).tearDown()
        self.mock_dnac_exec.stop()
        self.mock_dnac_init.stop()

    def load_fixtures(self, response=None, device=""):
        """
        Load fixtures for brownfield network settings generator tests.
        """

        if "generate_all_configurations" in self._testMethodName:
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
                self.test_data.get("get_reserve_ip_pool_details"),
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
                self.test_data.get("get_site_details"),
                self.test_data.get("get_device_controllability_response"),
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
                self.test_data.get("get_aaa_settings_response"),
            ]

        elif "global_filters_by_pool_name" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("get_global_pool_response"),
                self.test_data.get("get_reserve_ip_pool_details"),
            ]

        elif "global_filters_by_pool_type" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("get_global_pool_response"),
                self.test_data.get("get_reserve_ip_pool_details"),
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
                self.test_data.get("get_aaa_settings_response"),
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
    def test_brownfield_network_settings_playbook_generator_generate_all_configurations(self, mock_exists, mock_file):
        """
        Test case for brownfield network settings generator when generating all configurations.

        This test case checks the behavior when generate_all_configurations is set to True,
        which should retrieve all global pools, reserve pools, network management, device
        controllability, and AAA settings and generate a complete YAML playbook configuration file.
        """
        mock_exists.return_value = True

        set_module_args(
            dict(
                dnac_host="1.1.1.1",
                dnac_username="dummy",
                dnac_password="dummy",
                dnac_version="2.3.7.9",
                dnac_log=True,
                state="merged",
                config=self.playbook_config_generate_all_configurations
            )
        )
        result = self.execute_module(changed=True, failed=False)
        self.assertIn("YAML config generation succeeded", str(result.get('msg')))

    @patch('builtins.open', new_callable=mock_open)
    @patch('os.path.exists')
    def test_brownfield_network_settings_playbook_generator_global_pools_single(self, mock_exists, mock_file):
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
                state="merged",
                config=self.playbook_config_global_pools_single
            )
        )
        result = self.execute_module(changed=True, failed=False)
        self.assertIn("YAML config generation succeeded", str(result.get('msg')))

    @patch('builtins.open', new_callable=mock_open)
    @patch('os.path.exists')
    def test_brownfield_network_settings_playbook_generator_global_pools_multiple(self, mock_exists, mock_file):
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
                state="merged",
                config=self.playbook_config_global_pools_multiple
            )
        )
        result = self.execute_module(changed=True, failed=False)
        self.assertIn("YAML config generation succeeded", str(result.get('msg')))

    @patch('builtins.open', new_callable=mock_open)
    @patch('os.path.exists')
    def test_brownfield_network_settings_playbook_generator_reserve_pools_by_site_single(self, mock_exists, mock_file):
        """
        Test case for generating YAML configuration for reserve pools filtered by a single site.

        This test verifies that the generator correctly retrieves and generates configuration
        for reserve pools when filtered by a specific site name.
        """
        mock_exists.return_value = True

        set_module_args(
            dict(
                dnac_host="1.1.1.1",
                dnac_username="dummy",
                dnac_password="dummy",
                dnac_version="2.3.7.9",
                dnac_log=True,
                state="merged",
                config=self.playbook_config_reserve_pools_by_site_single
            )
        )
        result = self.execute_module(changed=True, failed=False)
        self.assertIn("YAML config generation succeeded", str(result.get('msg')))

    @patch('builtins.open', new_callable=mock_open)
    @patch('os.path.exists')
    def test_brownfield_network_settings_playbook_generator_reserve_pools_by_pool_name(self, mock_exists, mock_file):
        """
        Test case for generating YAML configuration for reserve pools filtered by pool names.

        This test verifies that the generator correctly retrieves and generates configuration
        for reserve pools when filtered by specific pool names.
        """
        mock_exists.return_value = True

        set_module_args(
            dict(
                dnac_host="1.1.1.1",
                dnac_username="dummy",
                dnac_password="dummy",
                dnac_version="2.3.7.9",
                dnac_log=True,
                state="merged",
                config=self.playbook_config_reserve_pools_by_pool_name
            )
        )
        result = self.execute_module(changed=True, failed=False)
        self.assertIn("YAML config generation succeeded", str(result.get('msg')))

    @patch('builtins.open', new_callable=mock_open)
    @patch('os.path.exists')
    def test_brownfield_network_settings_playbook_generator_network_management_by_site(self, mock_exists, mock_file):
        """
        Test case for generating YAML configuration for network management settings filtered by sites.

        This test verifies that the generator correctly retrieves and generates configuration
        for network management settings when filtered by specific site names.
        """
        mock_exists.return_value = True

        set_module_args(
            dict(
                dnac_host="1.1.1.1",
                dnac_username="dummy",
                dnac_password="dummy",
                dnac_version="2.3.7.9",
                dnac_log=True,
                state="merged",
                config=self.playbook_config_network_management_by_site
            )
        )
        result = self.execute_module(changed=True, failed=False)
        self.assertIn("YAML config generation succeeded", str(result.get('msg')))

    @patch('builtins.open', new_callable=mock_open)
    @patch('os.path.exists')
    def test_brownfield_network_settings_playbook_generator_device_controllability_by_site(self, mock_exists, mock_file):
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
                state="merged",
                config=self.playbook_config_device_controllability_by_site
            )
        )
        result = self.execute_module(changed=True, failed=False)
        self.assertIn("YAML config generation succeeded", str(result.get('msg')))

    @patch('builtins.open', new_callable=mock_open)
    @patch('os.path.exists')
    def test_brownfield_network_settings_playbook_generator_aaa_settings_by_network(self, mock_exists, mock_file):
        """
        Test case for generating YAML configuration for AAA settings filtered by network type.

        This test verifies that the generator correctly retrieves and generates configuration
        for AAA settings when filtered by network type.
        """
        mock_exists.return_value = True

        set_module_args(
            dict(
                dnac_host="1.1.1.1",
                dnac_username="dummy",
                dnac_password="dummy",
                dnac_version="2.3.7.9",
                dnac_log=True,
                state="merged",
                config=self.playbook_config_aaa_settings_by_network
            )
        )
        result = self.execute_module(changed=False, failed=False)
        self.assertIn("No configurations", str(result.get('response', {}).get('message', '')))

    @patch('builtins.open', new_callable=mock_open)
    @patch('os.path.exists')
    def test_brownfield_network_settings_playbook_generator_aaa_settings_by_server_type(self, mock_exists, mock_file):
        """
        Test case for generating YAML configuration for AAA settings filtered by server types.

        This test verifies that the generator correctly retrieves and generates configuration
        for AAA settings when filtered by multiple server types.
        """
        mock_exists.return_value = True

        set_module_args(
            dict(
                dnac_host="1.1.1.1",
                dnac_username="dummy",
                dnac_password="dummy",
                dnac_version="2.3.7.9",
                dnac_log=True,
                state="merged",
                config=self.playbook_config_aaa_settings_by_server_type
            )
        )
        result = self.execute_module(changed=False, failed=False)
        self.assertIn("No configurations", str(result.get('response', {}).get('message', '')))

    @patch('builtins.open', new_callable=mock_open)
    @patch('os.path.exists')
    def test_brownfield_network_settings_playbook_generator_global_filters_by_site(self, mock_exists, mock_file):
        """
        Test case for generating YAML configuration using global filters by site names.

        This test verifies that the generator correctly retrieves configurations for all
        components when filtered by specific site names using global filters.
        """
        mock_exists.return_value = True

        set_module_args(
            dict(
                dnac_host="1.1.1.1",
                dnac_username="dummy",
                dnac_password="dummy",
                dnac_version="2.3.7.9",
                dnac_log=True,
                state="merged",
                config=self.playbook_config_global_filters_by_site
            )
        )
        result = self.execute_module(changed=True, failed=False)
        self.assertIn("YAML config generation succeeded", str(result.get('msg')))

    @patch('builtins.open', new_callable=mock_open)
    @patch('os.path.exists')
    def test_brownfield_network_settings_playbook_generator_global_filters_by_pool_name(self, mock_exists, mock_file):
        """
        Test case for generating YAML configuration using global filters by pool names.

        This test verifies that the generator correctly retrieves configurations for
        pools when filtered by specific pool names using global filters.
        """
        mock_exists.return_value = True

        set_module_args(
            dict(
                dnac_host="1.1.1.1",
                dnac_username="dummy",
                dnac_password="dummy",
                dnac_version="2.3.7.9",
                dnac_log=True,
                state="merged",
                config=self.playbook_config_global_filters_by_pool_name
            )
        )
        result = self.execute_module(changed=True, failed=False)
        self.assertIn("YAML config generation succeeded", str(result.get('msg')))

    @patch('builtins.open', new_callable=mock_open)
    @patch('os.path.exists')
    def test_brownfield_network_settings_playbook_generator_global_filters_by_pool_type(self, mock_exists, mock_file):
        """
        Test case for generating YAML configuration using global filters by pool types.

        This test verifies that the generator correctly retrieves configurations for
        pools when filtered by specific pool types using global filters.
        """
        mock_exists.return_value = True

        set_module_args(
            dict(
                dnac_host="1.1.1.1",
                dnac_username="dummy",
                dnac_password="dummy",
                dnac_version="2.3.7.9",
                dnac_log=True,
                state="merged",
                config=self.playbook_config_global_filters_by_pool_type
            )
        )
        result = self.execute_module(changed=True, failed=False)
        self.assertIn("YAML config generation succeeded", str(result.get('msg')))

    @patch('builtins.open', new_callable=mock_open)
    @patch('os.path.exists')
    def test_brownfield_network_settings_playbook_generator_multiple_components(self, mock_exists, mock_file):
        """
        Test case for generating YAML configuration for multiple network settings components.

        This test verifies that the generator correctly retrieves and generates configuration
        for multiple components when specific components are requested.
        """
        mock_exists.return_value = True

        set_module_args(
            dict(
                dnac_host="1.1.1.1",
                dnac_username="dummy",
                dnac_password="dummy",
                dnac_version="2.3.7.9",
                dnac_log=True,
                state="merged",
                config=self.playbook_config_multiple_components
            )
        )
        result = self.execute_module(changed=True, failed=False)
        self.assertIn("YAML config generation succeeded", str(result.get('msg')))

    @patch('builtins.open', new_callable=mock_open)
    @patch('os.path.exists')
    def test_brownfield_network_settings_playbook_generator_all_components(self, mock_exists, mock_file):
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
                state="merged",
                config=self.playbook_config_all_components
            )
        )
        result = self.execute_module(changed=True, failed=False)
        self.assertIn("YAML config generation succeeded", str(result.get('msg')))

    @patch('builtins.open', new_callable=mock_open)
    @patch('os.path.exists')
    def test_brownfield_network_settings_playbook_generator_combined_filters(self, mock_exists, mock_file):
        """
        Test case for generating YAML configuration using combined global and component filters.

        This test verifies that the generator correctly applies both global filters and
        component-specific filters to generate targeted configurations.
        """
        mock_exists.return_value = True

        set_module_args(
            dict(
                dnac_host="1.1.1.1",
                dnac_username="dummy",
                dnac_password="dummy",
                dnac_version="2.3.7.9",
                dnac_log=True,
                state="merged",
                config=self.playbook_config_combined_filters
            )
        )
        result = self.execute_module(changed=True, failed=False)
        self.assertIn("YAML config generation succeeded", str(result.get('msg')))

    @patch('builtins.open', new_callable=mock_open)
    @patch('os.path.exists')
    def test_brownfield_network_settings_playbook_generator_empty_filters(self, mock_exists, mock_file):
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
                state="merged",
                config=self.playbook_config_empty_filters
            )
        )
        result = self.execute_module(changed=True, failed=False)
        self.assertIn("YAML config generation succeeded", str(result.get('msg')))

    @patch('builtins.open', new_callable=mock_open)
    @patch('os.path.exists')
    def test_brownfield_network_settings_playbook_generator_no_file_path(self, mock_exists, mock_file):
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
                state="merged",
                config=self.playbook_config_no_file_path
            )
        )
        result = self.execute_module(changed=True, failed=False)
        self.assertIn("YAML config generation succeeded", str(result.get('msg')))
