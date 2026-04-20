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
#   Mridul Saurabh (@msaurabh12)
#   Sunil Shatagopa (@shatagopasunil)
#   Madhan Sankaranarayanan (@madhansansel)
#
# Description:
#   Unit tests for the Ansible module `inventory_playbook_config_generator`.
#   These tests cover auto-discovery, device filters, role/type filters,
#   combined filters, no-data behavior, idempotency behavior, and validation errors.

from __future__ import absolute_import, division, print_function

__metaclass__ = type

from unittest.mock import patch, mock_open
from ansible_collections.cisco.dnac.plugins.modules import inventory_playbook_config_generator
from .dnac_module import TestDnacModule, set_module_args, loadPlaybookData


class TestInventoryPlaybookConfigGenerator(TestDnacModule):

    module = inventory_playbook_config_generator
    test_data = loadPlaybookData("inventory_playbook_config_generator")

    playbook_config_generate_all_configurations = test_data.get("playbook_config_generate_all_configurations")
    playbook_config_devices_by_ip = test_data.get("playbook_config_devices_by_ip")
    playbook_config_devices_by_hostname = test_data.get("playbook_config_devices_by_hostname")
    playbook_config_devices_by_serial = test_data.get("playbook_config_devices_by_serial")
    playbook_config_devices_by_mac = test_data.get("playbook_config_devices_by_mac")
    playbook_config_filter_by_role = test_data.get("playbook_config_filter_by_role")
    playbook_config_filter_by_type = test_data.get("playbook_config_filter_by_type")
    playbook_config_combined_filters = test_data.get("playbook_config_combined_filters")
    playbook_config_empty_global_filters = test_data.get("playbook_config_empty_global_filters")
    playbook_config_included_component_specific_filters = test_data.get("playbook_config_included_component_specific_filters")
    playbook_config_unknown_filter_ignored = test_data.get("playbook_config_unknown_filter_ignored")
    playbook_config_no_matching_devices = test_data.get("playbook_config_no_matching_devices")
    playbook_config_empty_config = test_data.get("playbook_config_empty_config")
    playbook_config_null_global_filters = test_data.get("playbook_config_null_global_filters")

    def setUp(self):
        super(TestInventoryPlaybookConfigGenerator, self).setUp()

        self.mock_dnac_init = patch(
            "ansible_collections.cisco.dnac.plugins.module_utils.dnac.DNACSDK.__init__"
        )
        self.run_dnac_init = self.mock_dnac_init.start()
        self.run_dnac_init.side_effect = [None]

        self.mock_get_with_pagination = patch(
            "ansible_collections.cisco.dnac.plugins.modules."
            "inventory_playbook_config_generator.InventoryPlaybookConfigGenerator.execute_get_with_pagination"
        )
        self.run_get_with_pagination = self.mock_get_with_pagination.start()

        self.mock_rest_call = patch(
            "ansible_collections.cisco.dnac.plugins.module_utils.dnac.DNACSDK.execute_rest_api_call"
        )
        self.run_rest_call = self.mock_rest_call.start()

        self.mock_write_yaml = patch(
            "ansible_collections.cisco.dnac.plugins.modules."
            "inventory_playbook_config_generator.InventoryPlaybookConfigGenerator.write_dict_to_yaml"
        )
        self.run_write_yaml = self.mock_write_yaml.start()

        self.load_fixtures()

    def tearDown(self):
        super(TestInventoryPlaybookConfigGenerator, self).tearDown()
        self.mock_write_yaml.stop()
        self.mock_rest_call.stop()
        self.mock_get_with_pagination.stop()
        self.mock_dnac_init.stop()

    def load_fixtures(self, response=None, device=""):
        """
        Load fixtures for inventory playbook config generator tests.
        """

        if "no_devices_in_inventory" in self._testMethodName:
            self.run_get_with_pagination.return_value = self.test_data.get("get_empty_device_list_response", {}).get("response", [])
            self.run_rest_call.return_value = self.test_data.get("get_empty_device_credentials_response", {})
            self.run_write_yaml.return_value = True
            return

        if "file_already_up_to_date" in self._testMethodName:
            self.run_get_with_pagination.return_value = self.test_data.get("get_device_list_response", {}).get("response", [])
            self.run_rest_call.return_value = self.test_data.get("get_device_credentials_response", {})
            self.run_write_yaml.return_value = False
            return

        self.run_get_with_pagination.return_value = self.test_data.get("get_device_list_response", {}).get("response", [])
        self.run_rest_call.return_value = self.test_data.get("get_device_credentials_response", {})
        self.run_write_yaml.return_value = True

    @patch("builtins.open", new_callable=mock_open)
    @patch("os.path.exists")
    def test_generate_all_configurations(self, mock_exists, mock_file):
        mock_exists.return_value = True
        set_module_args(dict(
            dnac_host="1.1.1.1",
            dnac_username="dummy",
            dnac_password="dummy",
            dnac_version="2.3.7.9",
            dnac_log=True,
            state="gathered",
            config=self.playbook_config_generate_all_configurations,
        ))
        result = self.execute_module(changed=True, failed=False)
        self.assertIn("YAML configuration file generated successfully", str(result.get("msg", {}).get("message")))

    @patch("builtins.open", new_callable=mock_open)
    @patch("os.path.exists")
    def test_devices_by_ip(self, mock_exists, mock_file):
        mock_exists.return_value = True
        set_module_args(dict(
            dnac_host="1.1.1.1",
            dnac_username="dummy",
            dnac_password="dummy",
            dnac_version="2.3.7.9",
            dnac_log=True,
            state="gathered",
            config=self.playbook_config_devices_by_ip,
        ))
        result = self.execute_module(changed=True, failed=False)
        self.assertIn("YAML configuration file generated successfully", str(result.get("msg", {}).get("message")))

    @patch("builtins.open", new_callable=mock_open)
    @patch("os.path.exists")
    def test_devices_by_hostname(self, mock_exists, mock_file):
        mock_exists.return_value = True
        set_module_args(dict(
            dnac_host="1.1.1.1",
            dnac_username="dummy",
            dnac_password="dummy",
            dnac_version="2.3.7.9",
            dnac_log=True,
            state="gathered",
            config=self.playbook_config_devices_by_hostname,
        ))
        result = self.execute_module(changed=True, failed=False)
        self.assertIn("YAML configuration file generated successfully", str(result.get("msg", {}).get("message")))

    @patch("builtins.open", new_callable=mock_open)
    @patch("os.path.exists")
    def test_devices_by_serial(self, mock_exists, mock_file):
        mock_exists.return_value = True
        set_module_args(dict(
            dnac_host="1.1.1.1",
            dnac_username="dummy",
            dnac_password="dummy",
            dnac_version="2.3.7.9",
            dnac_log=True,
            state="gathered",
            config=self.playbook_config_devices_by_serial,
        ))
        result = self.execute_module(changed=True, failed=False)
        self.assertIn("YAML configuration file generated successfully", str(result.get("msg", {}).get("message")))

    @patch("builtins.open", new_callable=mock_open)
    @patch("os.path.exists")
    def test_devices_by_mac(self, mock_exists, mock_file):
        mock_exists.return_value = True
        set_module_args(dict(
            dnac_host="1.1.1.1",
            dnac_username="dummy",
            dnac_password="dummy",
            dnac_version="2.3.7.9",
            dnac_log=True,
            state="gathered",
            config=self.playbook_config_devices_by_mac,
        ))
        result = self.execute_module(changed=True, failed=False)
        self.assertIn("YAML configuration file generated successfully", str(result.get("msg", {}).get("message")))

    @patch("builtins.open", new_callable=mock_open)
    @patch("os.path.exists")
    def test_filter_by_device_role(self, mock_exists, mock_file):
        mock_exists.return_value = True
        set_module_args(dict(
            dnac_host="1.1.1.1",
            dnac_username="dummy",
            dnac_password="dummy",
            dnac_version="2.3.7.9",
            dnac_log=True,
            state="gathered",
            config=self.playbook_config_filter_by_role,
        ))
        result = self.execute_module(changed=True, failed=False)
        self.assertIn("YAML configuration file generated successfully", str(result.get("msg", {}).get("message")))

    @patch("builtins.open", new_callable=mock_open)
    @patch("os.path.exists")
    def test_filter_by_device_type(self, mock_exists, mock_file):
        mock_exists.return_value = True
        set_module_args(dict(
            dnac_host="1.1.1.1",
            dnac_username="dummy",
            dnac_password="dummy",
            dnac_version="2.3.7.9",
            dnac_log=True,
            state="gathered",
            config=self.playbook_config_filter_by_type,
        ))
        result = self.execute_module(changed=True, failed=False)
        self.assertIn("YAML configuration file generated successfully", str(result.get("msg", {}).get("message")))

    @patch("builtins.open", new_callable=mock_open)
    @patch("os.path.exists")
    def test_combined_filters(self, mock_exists, mock_file):
        mock_exists.return_value = True
        set_module_args(dict(
            dnac_host="1.1.1.1",
            dnac_username="dummy",
            dnac_password="dummy",
            dnac_version="2.3.7.9",
            dnac_log=True,
            state="gathered",
            config=self.playbook_config_combined_filters,
        ))
        result = self.execute_module(changed=True, failed=False)
        self.assertIn("YAML configuration file generated successfully", str(result.get("msg", {}).get("message")))

    @patch("builtins.open", new_callable=mock_open)
    @patch("os.path.exists")
    def test_empty_global_filters(self, mock_exists, mock_file):
        mock_exists.return_value = True
        set_module_args(dict(
            dnac_host="1.1.1.1",
            dnac_username="dummy",
            dnac_password="dummy",
            dnac_version="2.3.7.9",
            dnac_log=True,
            state="gathered",
            config=self.playbook_config_empty_global_filters,
        ))
        result = self.execute_module(changed=False, failed=True)
        self.assertIn("Invalid playbook config: 'global_filters' is empty.", str(result.get("msg", "")))
        self.assertIn("Provide at least one filter or omit 'global_filters'.", str(result.get("msg", "")))

    @patch("builtins.open", new_callable=mock_open)
    @patch("os.path.exists")
    def test_null_global_filters(self, mock_exists, mock_file):
        mock_exists.return_value = True
        set_module_args(dict(
            dnac_host="1.1.1.1",
            dnac_username="dummy",
            dnac_password="dummy",
            dnac_version="2.3.7.9",
            dnac_log=True,
            state="gathered",
            config=self.playbook_config_null_global_filters,
        ))
        result = self.execute_module(changed=False, failed=True)
        self.assertIn("Invalid playbook config: 'global_filters' cannot be null when provided.", str(result.get("msg", "")))
        self.assertIn("Provide at least one filter or omit 'global_filters'.", str(result.get("msg", "")))

    @patch("builtins.open", new_callable=mock_open)
    @patch("os.path.exists")
    def test_included_component_specific_filters_empty(self, mock_exists, mock_file):
        mock_exists.return_value = True
        set_module_args(dict(
            dnac_host="1.1.1.1",
            dnac_username="dummy",
            dnac_password="dummy",
            dnac_version="2.3.7.9",
            dnac_log=True,
            state="gathered",
            config=self.playbook_config_included_component_specific_filters,
        ))
        result = self.execute_module(changed=False, failed=True)
        self.assertIn("Invalid filters found in playbook config", str(result.get("msg", "")))
        self.assertIn("Allowed filters are: ['global_filters'].", str(result.get("msg", "")))

    @patch("builtins.open", new_callable=mock_open)
    @patch("os.path.exists")
    def test_unknown_filter_is_ignored(self, mock_exists, mock_file):
        mock_exists.return_value = True
        set_module_args(dict(
            dnac_host="1.1.1.1",
            dnac_username="dummy",
            dnac_password="dummy",
            dnac_version="2.3.7.9",
            dnac_log=True,
            state="gathered",
            config=self.playbook_config_unknown_filter_ignored,
        ))
        result = self.execute_module(changed=False, failed=True)
        self.assertIn("Filter 'unknown_filter' not supported", str(result.get("msg")))

    @patch("builtins.open", new_callable=mock_open)
    @patch("os.path.exists")
    def test_no_matching_devices(self, mock_exists, mock_file):
        mock_exists.return_value = True
        set_module_args(dict(
            dnac_host="1.1.1.1",
            dnac_username="dummy",
            dnac_password="dummy",
            dnac_version="2.3.7.9",
            dnac_log=True,
            state="gathered",
            config=self.playbook_config_no_matching_devices,
        ))
        result = self.execute_module(changed=False, failed=False)
        self.assertIn("No configurations found", str(result.get("msg", {}).get("message", "")))

    @patch("builtins.open", new_callable=mock_open)
    @patch("os.path.exists")
    def test_no_devices_in_inventory(self, mock_exists, mock_file):
        mock_exists.return_value = True
        self.run_get_with_pagination.return_value = self.test_data.get("get_empty_device_list_response", {}).get("response", [])
        self.run_rest_call.return_value = self.test_data.get("get_empty_device_credentials_response", {})
        set_module_args(dict(
            dnac_host="1.1.1.1",
            dnac_username="dummy",
            dnac_password="dummy",
            dnac_version="2.3.7.9",
            dnac_log=True,
            state="gathered",
            config=self.playbook_config_generate_all_configurations,
        ))
        result = self.execute_module(changed=False, failed=False)
        self.assertIn("No configurations found", str(result.get("msg", {}).get("message", "")))

    @patch("builtins.open", new_callable=mock_open)
    @patch("os.path.exists")
    def test_file_already_up_to_date(self, mock_exists, mock_file):
        mock_exists.return_value = True
        self.run_write_yaml.return_value = False
        set_module_args(dict(
            dnac_host="1.1.1.1",
            dnac_username="dummy",
            dnac_password="dummy",
            dnac_version="2.3.7.9",
            dnac_log=True,
            state="gathered",
            config=self.playbook_config_generate_all_configurations,
        ))
        result = self.execute_module(changed=False, failed=False)
        self.assertIn("already up-to-date", str(result.get("msg", {}).get("message", "")))

    @patch("builtins.open", new_callable=mock_open)
    @patch("os.path.exists")
    def test_empty_config_fails_validation(self, mock_exists, mock_file):
        mock_exists.return_value = True
        set_module_args(dict(
            dnac_host="1.1.1.1",
            dnac_username="dummy",
            dnac_password="dummy",
            dnac_version="2.3.7.9",
            dnac_log=True,
            state="gathered",
            config=self.playbook_config_empty_config,
        ))
        result = self.execute_module(changed=False, failed=True)
        self.assertIn("Configuration cannot be an empty dictionary", str(result.get("msg", "")))
