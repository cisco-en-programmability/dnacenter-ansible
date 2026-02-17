#  Copyright (c) 2026 Cisco and/or its affiliates.
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
#   Unit tests for the Ansible module `ise_radius_integration_playbook_config_generator`.
#   These tests cover various scenarios for generating YAML configuration files
#   for ISE RADIUS authentication server configurations in Cisco Catalyst Center.

from __future__ import absolute_import, division, print_function

__metaclass__ = type
from unittest.mock import patch, mock_open
from ansible_collections.cisco.dnac.plugins.modules import (
    ise_radius_integration_playbook_config_generator,
)
from .dnac_module import TestDnacModule, set_module_args, loadPlaybookData


class TestIseRadiusIntegrationPlaybookConfigGenerator(TestDnacModule):

    module = ise_radius_integration_playbook_config_generator
    test_data = loadPlaybookData("ise_radius_integration_playbook_config_generator")

    # Load all playbook configurations
    playbook_config_generate_all_configurations = test_data.get(
        "playbook_config_generate_all_configurations"
    )
    playbook_config_with_file_path = test_data.get("playbook_config_with_file_path")
    playbook_config_filter_by_server_type = test_data.get(
        "playbook_config_filter_by_server_type"
    )
    playbook_config_filter_by_server_ip = test_data.get(
        "playbook_config_filter_by_server_ip"
    )
    playbook_config_filter_by_both = test_data.get("playbook_config_filter_by_both")
    playbook_config_no_filters = test_data.get("playbook_config_no_filters")
    playbook_config_invalid_server_type = test_data.get(
        "playbook_config_invalid_server_type"
    )
    playbook_config_no_file_path = test_data.get("playbook_config_no_file_path")

    def setUp(self):
        super(TestIseRadiusIntegrationPlaybookConfigGenerator, self).setUp()

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
        super(TestIseRadiusIntegrationPlaybookConfigGenerator, self).tearDown()
        self.mock_dnac_exec.stop()
        self.mock_dnac_init.stop()

    def load_fixtures(self, response=None, device=""):
        """
        Load fixtures for ISE RADIUS integration generator tests.
        """
        test_method_with_all_data_mapping = [
            "generate_all_configurations",
            "with_file_path",
            "filter_by_server_type",
            "filter_by_server_ip",
            "filter_by_both",
            "no_filters",
            "no_file_path",
        ]

        for method_name in test_method_with_all_data_mapping:
            if method_name in self._testMethodName:
                self.run_dnac_exec.side_effect = [
                    self.test_data.get("get_authentication_and_policy_servers"),
                ]
                break
        if "invalid_server_type" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get(
                    "get_authentication_and_policy_servers_with_invalid_server_type"
                ),
            ]

    @patch("builtins.open", new_callable=mock_open)
    @patch("os.path.exists")
    def test_ise_radius_integration_playbook_config_generator_generate_all_configurations(
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
        self.assertEqual(str(result.get("response").get("status")), "success")
        self.assertIn(
            "YAML configuration file generated successfully for module",
            str(result.get("response").get("message")),
        )

    @patch("builtins.open", new_callable=mock_open)
    @patch("os.path.exists")
    def test_ise_radius_integration_playbook_config_generator_with_file_path(
        self, mock_exists, mock_file
    ):
        """
        Test case for generating YAML configuration with specific file path.

        This test verifies that the generator creates a YAML configuration file
        at the specified file path containing ISE RADIUS server configurations.
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
                config=self.playbook_config_with_file_path,
            )
        )
        result = self.execute_module(changed=True, failed=False)
        self.assertEqual(str(result.get("response").get("status")), "success")
        self.assertIn(
            "YAML configuration file generated successfully for module",
            str(result.get("response").get("message")),
        )

    @patch("builtins.open", new_callable=mock_open)
    @patch("os.path.exists")
    def test_ise_radius_integration_playbook_config_generator_filter_by_server_type(
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
        self.assertEqual(str(result.get("response").get("status")), "success")
        self.assertIn(
            "YAML configuration file generated successfully for module",
            str(result.get("response").get("message")),
        )

    @patch("builtins.open", new_callable=mock_open)
    @patch("os.path.exists")
    def test_ise_radius_integration_playbook_config_generator_filter_by_server_ip(
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
        self.assertEqual(str(result.get("response").get("status")), "success")
        self.assertIn(
            "YAML configuration file generated successfully for module",
            str(result.get("response").get("message")),
        )

    @patch("builtins.open", new_callable=mock_open)
    @patch("os.path.exists")
    def test_ise_radius_integration_playbook_config_generator_filter_by_both(
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
        self.assertEqual(str(result.get("response").get("status")), "success")
        self.assertIn(
            "YAML configuration file generated successfully for module",
            str(result.get("response").get("message")),
        )

    @patch("builtins.open", new_callable=mock_open)
    @patch("os.path.exists")
    def test_ise_radius_integration_playbook_config_generator_no_filters(
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
        self.assertEqual(str(result.get("response").get("status")), "success")
        self.assertIn(
            "YAML configuration file generated successfully for module",
            str(result.get("response").get("message")),
        )

    @patch("builtins.open", new_callable=mock_open)
    @patch("os.path.exists")
    def test_ise_radius_integration_playbook_config_generator_invalid_server_type(
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
        self.assertIn("Invalid filters provided for module", str(result.get("msg")))

    @patch("builtins.open", new_callable=mock_open)
    @patch("os.path.exists")
    def test_ise_radius_integration_playbook_config_generator_no_file_path(
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
        self.assertEqual(str(result.get("response").get("status")), "success")
        self.assertIn(
            "YAML configuration file generated successfully for module",
            str(result.get("response").get("message")),
        )
