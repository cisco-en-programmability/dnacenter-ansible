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
#   Unit tests for the Ansible module `sda_fabric_sites_zones_playbook_config_generator`.
#   These tests cover various scenarios for generating YAML configuration files from playbook config generator
#   SDA fabric sites and zones configurations in Cisco Catalyst Center.

from __future__ import absolute_import, division, print_function

__metaclass__ = type
from unittest.mock import patch, mock_open
from ansible_collections.cisco.dnac.plugins.modules import sda_fabric_sites_zones_playbook_config_generator
from .dnac_module import TestDnacModule, set_module_args, loadPlaybookData


class TestFabricSitesZonesPlaybookConfigGenerator(TestDnacModule):

    module = sda_fabric_sites_zones_playbook_config_generator
    test_data = loadPlaybookData("sda_fabric_sites_zones_playbook_config_generator")

    # Load all playbook configurations
    playbook_config_generate_all_configurations = test_data.get("playbook_config_generate_all_configurations")
    playbook_config_fetch_specific_configurations = test_data.get("playbook_config_fetch_specific_configurations")
    playbook_config_fabric_sites_only = test_data.get("playbook_config_fabric_sites_only")
    playbook_config_fabric_zones_only = test_data.get("playbook_config_fabric_zones_only")
    playbook_config_fabric_sites_and_zones = test_data.get("playbook_config_fabric_sites_and_zones")
    playbook_config_fabric_sites_with_filters = test_data.get("playbook_config_fabric_sites_with_filters")
    playbook_config_fabric_sites_with_multiple_filters = test_data.get("playbook_config_fabric_sites_with_multiple_filters")
    playbook_config_fabric_zones_with_filters = test_data.get("playbook_config_fabric_zones_with_filters")
    playbook_config_fabric_zones_with_multiple_filters = test_data.get("playbook_config_fabric_zones_with_multiple_filters")
    playbook_config_no_file_path = test_data.get("playbook_config_no_file_path")
    playbook_config_empty_filters = test_data.get("playbook_config_empty_filters")

    def setUp(self):
        super(TestFabricSitesZonesPlaybookConfigGenerator, self).setUp()

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
        super(TestFabricSitesZonesPlaybookConfigGenerator, self).tearDown()
        self.mock_dnac_exec.stop()
        self.mock_dnac_init.stop()

    def load_fixtures(self, response=None, device=""):
        """
        Load fixtures for fabric sites and zones playbook config generator tests.
        """

        if "generate_all_configurations" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("get_fabric_site_details"),
                self.test_data.get("get_site_details"),
                self.test_data.get("get_fabric_zone_details"),
                self.test_data.get("get_zone_site_details"),
            ]

        elif "fetch_specific_configurations" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("get_fabric_site_details"),
                self.test_data.get("get_site_details"),
                self.test_data.get("get_fabric_zone_details"),
                self.test_data.get("get_zone_site_details"),
            ]

        elif "fabric_sites_only" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("get_fabric_site_details"),
                self.test_data.get("get_site_details"),
            ]

        elif "fabric_zones_only" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("get_fabric_zone_details"),
                self.test_data.get("get_zone_site_details"),
            ]

        elif "fabric_sites_and_zones" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("get_fabric_site_details"),
                self.test_data.get("get_site_details"),
                self.test_data.get("get_fabric_zone_details"),
                self.test_data.get("get_zone_site_details"),
            ]

        elif "fabric_sites_with_filters" in self._testMethodName and "multiple" not in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("get_site_details"),  # Get site ID from site_name_hierarchy
                self.test_data.get("get_fabric_site_details"),  # Get fabric site with that site ID
                self.test_data.get("get_site_details"),  # Transform site IDs back to hierarchy
            ]

        elif "fabric_sites_with_multiple_filters" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("get_site_details"),  # Get site ID for first filter
                self.test_data.get("get_fabric_site_details"),  # Get fabric site with first site ID
                self.test_data.get("get_site_details_2"),  # Get site ID for second filter
                self.test_data.get("get_fabric_site_details"),  # Get fabric site with second site ID
                self.test_data.get("get_site_details"),  # Transform site IDs back to hierarchy
                self.test_data.get("get_site_details_2"),  # Transform second site ID back to hierarchy
            ]

        elif "fabric_zones_with_filters" in self._testMethodName and "multiple" not in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("get_zone_site_details"),  # Get site ID from site_name_hierarchy
                self.test_data.get("get_fabric_zone_details"),  # Get fabric zone with that site ID
                self.test_data.get("get_zone_site_details"),  # Transform site IDs back to hierarchy
            ]

        elif "fabric_zones_with_multiple_filters" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("get_zone_site_details"),  # Get site ID for first filter
                self.test_data.get("get_fabric_zone_details"),  # Get fabric zone with first site ID
                self.test_data.get("get_zone_site_details"),  # Get site ID for second filter
                self.test_data.get("get_fabric_zone_details"),  # Get fabric zone with second site ID
                self.test_data.get("get_zone_site_details"),  # Transform first site ID back to hierarchy
                self.test_data.get("get_zone_site_details"),  # Transform second site ID back to hierarchy
            ]

        elif "no_file_path" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("get_fabric_site_details"),
                self.test_data.get("get_site_details"),
            ]

        elif "empty_filters" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("get_fabric_site_details"),
                self.test_data.get("get_site_details"),
                self.test_data.get("get_fabric_zone_details"),
                self.test_data.get("get_zone_site_details"),
            ]

    @patch('builtins.open', new_callable=mock_open)
    @patch('os.path.exists')
    def test_sda_fabric_sites_zones_playbook_config_generator_generate_all_configurations(self, mock_exists, mock_file):
        """
        Test case for generating YAML configuration for all fabric sites and zones.

        This test verifies that the generator creates a YAML configuration file
        containing all fabric sites and zones when generate_all_configurations is True.
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
    def test_sda_fabric_sites_zones_playbook_config_generator_fetch_specific_configurations(self, mock_exists, mock_file):
        """
        Test case for generating YAML configuration with specific file path.

        This test verifies that the generator creates a YAML configuration file
        at the specified file path containing all fabric sites and zones.
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
                config=self.playbook_config_fetch_specific_configurations
            )
        )
        result = self.execute_module(changed=True, failed=False)
        self.assertIn("YAML configuration file generated successfully", str(result.get('msg').get("message")))

    @patch('builtins.open', new_callable=mock_open)
    @patch('os.path.exists')
    def test_sda_fabric_sites_zones_playbook_config_generator_fabric_sites_only(self, mock_exists, mock_file):
        """
        Test case for generating YAML configuration with only fabric sites.

        This test verifies that the generator creates a YAML configuration file
        containing only fabric sites when components_list includes only "fabric_sites".
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
                config=self.playbook_config_fabric_sites_only
            )
        )
        result = self.execute_module(changed=True, failed=False)
        self.assertIn("YAML configuration file generated successfully", str(result.get('msg').get("message")))

    @patch('builtins.open', new_callable=mock_open)
    @patch('os.path.exists')
    def test_sda_fabric_sites_zones_playbook_config_generator_fabric_zones_only(self, mock_exists, mock_file):
        """
        Test case for generating YAML configuration with only fabric zones.

        This test verifies that the generator creates a YAML configuration file
        containing only fabric zones when components_list includes only "fabric_zones".
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
                config=self.playbook_config_fabric_zones_only
            )
        )
        result = self.execute_module(changed=True, failed=False)
        self.assertIn("YAML configuration file generated successfully", str(result.get('msg').get("message")))

    @patch('builtins.open', new_callable=mock_open)
    @patch('os.path.exists')
    def test_sda_fabric_sites_zones_playbook_config_generator_fabric_sites_and_zones(self, mock_exists, mock_file):
        """
        Test case for generating YAML configuration with both fabric sites and zones.

        This test verifies that the generator creates a YAML configuration file
        containing both fabric sites and zones when components_list includes both.
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
                config=self.playbook_config_fabric_sites_and_zones
            )
        )
        result = self.execute_module(changed=True, failed=False)
        self.assertIn("YAML configuration file generated successfully", str(result.get('msg').get("message")))

    @patch('builtins.open', new_callable=mock_open)
    @patch('os.path.exists')
    def test_sda_fabric_sites_zones_playbook_config_generator_fabric_sites_with_filters(self, mock_exists, mock_file):
        """
        Test case for generating YAML configuration with fabric sites filtered by site hierarchy.

        This test verifies that the generator creates a YAML configuration file
        containing only fabric sites matching the specified site_name_hierarchy filter.
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
                config=self.playbook_config_fabric_sites_with_filters
            )
        )
        result = self.execute_module(changed=True, failed=False)
        self.assertIn("YAML configuration file generated successfully", str(result.get('msg').get("message")))

    @patch('builtins.open', new_callable=mock_open)
    @patch('os.path.exists')
    def test_sda_fabric_sites_zones_playbook_config_generator_fabric_sites_with_multiple_filters(self, mock_exists, mock_file):
        """
        Test case for generating YAML configuration with multiple fabric sites filters.

        This test verifies that the generator creates a YAML configuration file
        containing fabric sites matching multiple site_name_hierarchy filters.
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
                config=self.playbook_config_fabric_sites_with_multiple_filters
            )
        )
        result = self.execute_module(changed=True, failed=False)
        self.assertIn("YAML configuration file generated successfully", str(result.get('msg').get("message")))

    @patch('builtins.open', new_callable=mock_open)
    @patch('os.path.exists')
    def test_sda_fabric_sites_zones_playbook_config_generator_fabric_zones_with_filters(self, mock_exists, mock_file):
        """
        Test case for generating YAML configuration with fabric zones filtered by site hierarchy.

        This test verifies that the generator creates a YAML configuration file
        containing only fabric zones matching the specified site_name_hierarchy filter.
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
                config=self.playbook_config_fabric_zones_with_filters
            )
        )
        result = self.execute_module(changed=True, failed=False)
        self.assertIn("YAML configuration file generated successfully", str(result.get('msg').get("message")))

    @patch('builtins.open', new_callable=mock_open)
    @patch('os.path.exists')
    def test_sda_fabric_sites_zones_playbook_config_generator_fabric_zones_with_multiple_filters(self, mock_exists, mock_file):
        """
        Test case for generating YAML configuration with multiple fabric zones filters.

        This test verifies that the generator creates a YAML configuration file
        containing fabric zones matching multiple site_name_hierarchy filters.
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
                config=self.playbook_config_fabric_zones_with_multiple_filters
            )
        )
        result = self.execute_module(changed=True, failed=False)
        self.assertIn("YAML configuration file generated successfully", str(result.get('msg').get("message")))

    @patch('builtins.open', new_callable=mock_open)
    @patch('os.path.exists')
    def test_sda_fabric_sites_zones_playbook_config_generator_no_file_path(self, mock_exists, mock_file):
        """
        Test case for generating YAML configuration without specifying file_path.

        This test verifies that the generator creates a default filename when
        file_path is not provided in the configuration.
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
        self.assertIn("sda_fabric_sites_zones_playbook_config", str(result.get('msg')))

    @patch('builtins.open', new_callable=mock_open)
    @patch('os.path.exists')
    def test_sda_fabric_sites_zones_playbook_config_generator_empty_filters(self, mock_exists, mock_file):
        """
        Test case for generating YAML configuration with empty component-specific filters.

        This test verifies that the generator retrieves all fabric sites and zones
        when component-specific filters are empty.
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
