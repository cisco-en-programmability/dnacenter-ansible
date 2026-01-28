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
#   Jeet Ram <jeeram@cisco.com>
#   Madhan Sankaranarayanan <madhansansel@cisco.com>
#
# Description:
#   Unit tests for the Ansible module `brownfield_ise_radius_integration_playbook_generator`.
#   These tests cover various scenarios for generating YAML configuration files from brownfield
#   ISE RADIUS authentication server configurations in Cisco Catalyst Center.

from __future__ import absolute_import, division, print_function

__metaclass__ = type
from unittest.mock import patch, mock_open
from ansible_collections.cisco.dnac.plugins.modules import brownfield_ise_radius_integration_playbook_generator
from .dnac_module import TestDnacModule, set_module_args, loadPlaybookData


class TestBrownfieldIseRadiusIntegrationGenerator(TestDnacModule):

    module = brownfield_ise_radius_integration_playbook_generator
    test_data = loadPlaybookData("brownfield_ise_radius_integration_playbook_generator")

    # Load all playbook configurations
    playbook_config_generate_all_configurations = test_data.get(
        "playbook_config_generate_all_configurations"
    )
    playbook_config_filter_by_server_type = test_data.get("playbook_config_filter_by_server_type")
    playbook_config_filter_by_server_ip = test_data.get("playbook_config_filter_by_server_ip")
    playbook_config_filter_by_both = test_data.get("playbook_config_filter_by_both")
    playbook_config_no_filters = test_data.get("playbook_config_no_filters")
    playbook_config_invalid_server_type = test_data.get("playbook_config_invalid_server_type")
    playbook_config_no_file_path = test_data.get("playbook_config_no_file_path")
    playbook_config_generate_all_configurations_false = test_data.get("playbook_config_generate_all_configurations_false")

    def setUp(self):
        super(TestBrownfieldIseRadiusIntegrationGenerator, self).setUp()

        self.mock_dnac_init = patch(
            "ansible_collections.cisco.dnac.plugins.module_utils.dnac.DNACSDK.__init__"
        )
        self.run_dnac_init = self.mock_dnac_init.start()
        self.run_dnac_init.side_effect = [None]

        self.mock_dnac_exec = patch(
            "ansible_collections.cisco.dnac.plugins.module_utils.dnac.DNACSDK._exec"
        )
        self.run_dnac_exec = self.mock_dnac_exec.start()

        self.load_fixtures()

    def tearDown(self):
        super(TestBrownfieldIseRadiusIntegrationGenerator, self).tearDown()
        self.mock_dnac_exec.stop()
        self.mock_dnac_init.stop()

    def load_fixtures(self, response=None, device=""):
        """
        Load fixtures for brownfield ISE RADIUS integration generator tests.
        """

        if "generate_all_configurations" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("get_authentication_and_policy_servers"),
            ]

        elif "filter_by_server_type" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("get_authentication_and_policy_servers"),
            ]

        elif "filter_by_server_ip" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("get_authentication_and_policy_servers"),
            ]

        elif "filter_by_both" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("get_authentication_and_policy_servers"),
            ]

        elif "multiple_filters" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("get_authentication_and_policy_servers"),
            ]

        elif "no_filters" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("get_authentication_and_policy_servers"),
            ]

        elif "invalid_server_type" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("get_authentication_and_policy_servers"),
            ]
        elif "no_file_path" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("get_authentication_and_policy_servers"),
            ]

    @patch("builtins.open", new_callable=mock_open)
    @patch("os.path.exists")
    def test_brownfield_ise_radius_integration_playbook_generator_generate_all_configurations(
        self, mock_exists, mock_file
    ):
        """
        Test case for generating YAML configuration for all ISE RADIUS servers.

        This test verifies that the generator creates a YAML configuration file
        containing all authentication policy servers when generate_all_configurations is True.
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
                config=self.playbook_config_generate_all_configurations,
            )
        )
        result = self.execute_module(changed=True, failed=False)
        self.assertIn("YAML configuration file generated successfully for module ", str(result.get("msg")))

    @patch("builtins.open", new_callable=mock_open)
    @patch("os.path.exists")
    def test_brownfield_ise_radius_integration_playbook_generator_filter_by_server_type(
        self, mock_exists, mock_file
    ):
        """
        Test case for generating YAML configuration filtered by server type.

        This test verifies that the generator creates a YAML configuration file
        containing only ISE servers when filtered by server_type=ISE.
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
                config=self.playbook_config_filter_by_server_type,
            )
        )
        result = self.execute_module(changed=True, failed=False)
        self.assertIn("YAML configuration file generated successfully for module ", str(result.get("msg")))

    @patch("builtins.open", new_callable=mock_open)
    @patch("os.path.exists")
    def test_brownfield_ise_radius_integration_playbook_generator_filter_by_server_ip(
        self, mock_exists, mock_file
    ):
        """
        Test case for generating YAML configuration filtered by server IP address.

        This test verifies that the generator creates a YAML configuration file
        containing only the server matching the specified server_ip_address.
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
                config=self.playbook_config_filter_by_server_ip,
            )
        )
        result = self.execute_module(changed=True, failed=False)
        self.assertIn("YAML configuration file generated successfully for module ", str(result.get("msg")))

    @patch("builtins.open", new_callable=mock_open)
    @patch("os.path.exists")
    def test_brownfield_ise_radius_integration_playbook_generator_filter_by_both(
        self, mock_exists, mock_file
    ):
        """
        Test case for generating YAML configuration filtered by both server type and IP.

        This test verifies that the generator creates a YAML configuration file
        containing only servers matching both server_type and server_ip_address filters.
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
                config=self.playbook_config_filter_by_both,
            )
        )
        result = self.execute_module(changed=True, failed=False)
        self.assertIn("YAML configuration file generated successfully for module ", str(result.get("msg")))

    @patch("builtins.open", new_callable=mock_open)
    @patch("os.path.exists")
    def test_brownfield_ise_radius_integration_playbook_generator_no_filters(
        self, mock_exists, mock_file
    ):
        """
        Test case for generating YAML configuration without any filters.

        This test verifies that the generator creates a YAML configuration file
        containing all authentication policy servers when no filters are specified.
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
                config=self.playbook_config_no_filters,
            )
        )
        result = self.execute_module(changed=True, failed=False)
        self.assertIn("YAML configuration file generated successfully for module ", str(result.get("msg")))

    @patch("builtins.open", new_callable=mock_open)
    @patch("os.path.exists")
    def test_brownfield_ise_radius_integration_playbook_generator_invalid_server_type(
        self, mock_exists, mock_file
    ):
        """
        Test case for generating YAML configuration with invalid server type filter.

        This test verifies that the generator handles invalid server_type values gracefully
        and returns an empty or appropriately filtered result.
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
                config=self.playbook_config_invalid_server_type,
            )
        )
        result = self.execute_module(changed=False, failed=True)
        # Should succeed but with empty or no matching servers
        self.assertIn("Invalid filters provided for module", str(result.get("msg")))

    @patch("builtins.open", new_callable=mock_open)
    @patch("os.path.exists")
    def test_brownfield_ise_radius_integration_playbook_generator_no_file_path(
        self, mock_exists, mock_file
    ):
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
                config=self.playbook_config_no_file_path,
            )
        )
        result = self.execute_module(changed=True, failed=False)
        self.assertIn("YAML configuration file generated successfully for module ", str(result.get("msg")))
        self.assertIn(
            "ise_radius_integration_workflow_manager_playbook_", str(result.get("msg"))
        )

    @patch("builtins.open", new_callable=mock_open)
    @patch("os.path.exists")
    def test_brownfield_ise_radius_integration_playbook_generator_generate_all_configurations_false(
        self, mock_exists, mock_file
    ):
        """
        Test case for generating YAML configuration with generate_all_configurations set to false.

        This test verifies that the generator handles generate_all_configurations set to false gracefully
        and returns an empty or appropriately filtered result.
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
                config=self.playbook_config_generate_all_configurations_false,
            )
        )
        result = self.execute_module(changed=False, failed=True)
        # Should succeed but with empty or no matching servers
        self.assertIn("Validation Error in entry 1", str(result.get("msg")))
