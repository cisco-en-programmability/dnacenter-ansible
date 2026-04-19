# Copyright (c) 2026 Cisco and/or its affiliates.
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
#   Sunil Shatagopa <shatagopasunil@cisco.com>
#   Madhan Sankaranarayanan <madhansansel@cisco.com>
#
# Description:
#   Unit tests for the Ansible module `wireless_design_playbook_config_generator`.
#   These tests cover targeted component filters for wireless design YAML generation.

from __future__ import absolute_import, division, print_function

__metaclass__ = type
from unittest.mock import patch, mock_open
from ansible_collections.cisco.dnac.plugins.modules import wireless_design_playbook_config_generator
from .dnac_module import TestDnacModule, set_module_args, loadPlaybookData


class TestWirelessDesignPlaybookConfigGenerator(TestDnacModule):
    module = wireless_design_playbook_config_generator
    test_data = loadPlaybookData("wireless_design_playbook_config_generator")

    playbook_config_ssids_with_filters = test_data.get("playbook_config_ssids_with_filters")
    playbook_config_interfaces_with_filters = test_data.get("playbook_config_interfaces_with_filters")
    playbook_config_feature_template_with_filters = test_data.get("playbook_config_feature_template_with_filters")
    playbook_config_flex_connect_with_filters = test_data.get("playbook_config_flex_connect_with_filters")
    playbook_config_invalid_minimum_requirements = test_data.get("playbook_config_invalid_minimum_requirements")
    playbook_config_interfaces_without_filters = test_data.get("playbook_config_interfaces_without_filters")
    playbook_config_feature_template_type_only = test_data.get("playbook_config_feature_template_type_only")
    playbook_config_feature_template_invalid_type = test_data.get("playbook_config_feature_template_invalid_type")
    playbook_config_empty_config = test_data.get("playbook_config_empty_config")
    playbook_config_empty_component_specific_filters = test_data.get("playbook_config_empty_component_specific_filters")
    playbook_config_invalid_component = test_data.get("playbook_config_invalid_component")
    playbook_config_invalid_component_filters = test_data.get("playbook_config_invalid_component_filters")

    def setUp(self):
        super(TestWirelessDesignPlaybookConfigGenerator, self).setUp()
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
        super(TestWirelessDesignPlaybookConfigGenerator, self).tearDown()
        self.mock_dnac_exec.stop()
        self.mock_dnac_init.stop()

    def load_fixtures(self, response=None, device=""):
        """
        Load fixtures for wireless design playbook config generator tests.
        """

        if "ssids_with_filters" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("get_site_response"),
                self.test_data.get("get_ssid_by_site_response"),
            ]
        elif "interfaces_with_filters" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("get_interfaces_response"),
            ]
        elif "interfaces_without_filters" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("get_interfaces_response"),
            ]
        elif "feature_template_with_filters" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("get_feature_template_summary_response"),
                self.test_data.get("get_advanced_ssid_configuration_feature_template_response"),
            ]
        elif "feature_template_type_only" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("get_feature_template_summary_response"),
                self.test_data.get("get_advanced_ssid_configuration_feature_template_response"),
            ]
        elif "feature_template_invalid_type" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("get_feature_template_summary_response"),
            ]
        elif "flex_connect_with_filters" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("get_site_response"),
                self.test_data.get("get_native_vlan_settings_by_site_response"),
            ]
        elif "invalid_minimum_requirements" in self._testMethodName:
            self.run_dnac_exec.side_effect = []
        elif "empty_config" in self._testMethodName:
            # No side effects needed - validation happens before API calls
            pass
        elif "empty_component_specific_filters" in self._testMethodName:
            # No side effects needed - validation happens before API calls
            pass
        elif "invalid_component" in self._testMethodName:
            # No side effects needed - validation happens before API calls
            pass
        elif "invalid_component_filters" in self._testMethodName:
            # No side effects needed - validation happens before API calls
            pass

    @patch("builtins.open", new_callable=mock_open)
    @patch("os.path.exists")
    def test_wireless_design_ssids_with_filters(self, mock_exists, mock_file):
        mock_exists.return_value = True

        set_module_args(
            dict(
                dnac_host="1.1.1.1",
                dnac_username="dummy",
                dnac_password="dummy",
                dnac_version="2.3.7.9",
                dnac_log=True,
                state="gathered",
                config=self.playbook_config_ssids_with_filters,
            )
        )
        result = self.execute_module(changed=True, failed=False)
        self.assertIn(
            "YAML configuration file generated successfully",
            str(result.get("msg").get("message")),
        )

    @patch("builtins.open", new_callable=mock_open)
    @patch("os.path.exists")
    def test_wireless_design_interfaces_with_filters(self, mock_exists, mock_file):
        mock_exists.return_value = True

        set_module_args(
            dict(
                dnac_host="1.1.1.1",
                dnac_username="dummy",
                dnac_password="dummy",
                dnac_version="2.3.7.9",
                dnac_log=True,
                state="gathered",
                config=self.playbook_config_interfaces_with_filters,
            )
        )
        result = self.execute_module(changed=True, failed=False)
        self.assertIn(
            "YAML configuration file generated successfully",
            str(result.get("msg").get("message")),
        )

    @patch("builtins.open", new_callable=mock_open)
    @patch("os.path.exists")
    def test_wireless_design_feature_template_with_filters(self, mock_exists, mock_file):
        mock_exists.return_value = True

        set_module_args(
            dict(
                dnac_host="1.1.1.1",
                dnac_username="dummy",
                dnac_password="dummy",
                dnac_version="2.3.7.9",
                dnac_log=True,
                state="gathered",
                config=self.playbook_config_feature_template_with_filters,
            )
        )
        result = self.execute_module(changed=True, failed=False)
        self.assertIn(
            "YAML configuration file generated successfully",
            str(result.get("msg").get("message")),
        )

    @patch("builtins.open", new_callable=mock_open)
    @patch("os.path.exists")
    def test_wireless_design_flex_connect_with_filters(self, mock_exists, mock_file):
        mock_exists.return_value = True

        set_module_args(
            dict(
                dnac_host="1.1.1.1",
                dnac_username="dummy",
                dnac_password="dummy",
                dnac_version="2.3.7.9",
                dnac_log=True,
                state="gathered",
                config=self.playbook_config_flex_connect_with_filters,
            )
        )
        result = self.execute_module(changed=True, failed=False)
        self.assertIn(
            "YAML configuration file generated successfully",
            str(result.get("msg").get("message")),
        )

    @patch("builtins.open", new_callable=mock_open)
    @patch("os.path.exists")
    def test_wireless_design_invalid_minimum_requirements(self, mock_exists, mock_file):
        mock_exists.return_value = True

        set_module_args(
            dict(
                dnac_host="1.1.1.1",
                dnac_username="dummy",
                dnac_password="dummy",
                dnac_version="2.3.7.9",
                dnac_log=True,
                state="gathered",
                config=self.playbook_config_invalid_minimum_requirements,
            )
        )
        result = self.execute_module(changed=False, failed=True)
        self.assertIn("component_specific_filters", str(result.get("msg")))

    @patch("builtins.open", new_callable=mock_open)
    @patch("os.path.exists")
    def test_wireless_design_interfaces_without_filters(self, mock_exists, mock_file):
        mock_exists.return_value = True

        set_module_args(
            dict(
                dnac_host="1.1.1.1",
                dnac_username="dummy",
                dnac_password="dummy",
                dnac_version="2.3.7.9",
                dnac_log=True,
                state="gathered",
                config=self.playbook_config_interfaces_without_filters,
            )
        )
        result = self.execute_module(changed=True, failed=False)
        self.assertIn(
            "YAML configuration file generated successfully",
            str(result.get("msg").get("message")),
        )

    @patch("builtins.open", new_callable=mock_open)
    @patch("os.path.exists")
    def test_wireless_design_feature_template_type_only(self, mock_exists, mock_file):
        mock_exists.return_value = True

        set_module_args(
            dict(
                dnac_host="1.1.1.1",
                dnac_username="dummy",
                dnac_password="dummy",
                dnac_version="2.3.7.9",
                dnac_log=True,
                state="gathered",
                config=self.playbook_config_feature_template_type_only,
            )
        )
        result = self.execute_module(changed=True, failed=False)
        self.assertIn(
            "YAML configuration file generated successfully",
            str(result.get("msg").get("message")),
        )

    @patch("builtins.open", new_callable=mock_open)
    @patch("os.path.exists")
    def test_wireless_design_feature_template_invalid_type(self, mock_exists, mock_file):
        mock_exists.return_value = True

        set_module_args(
            dict(
                dnac_host="1.1.1.1",
                dnac_username="dummy",
                dnac_password="dummy",
                dnac_version="2.3.7.9",
                dnac_log=True,
                state="gathered",
                config=self.playbook_config_feature_template_invalid_type,
            )
        )
        result = self.execute_module(changed=False, failed=True)
        self.assertIn("Invalid filters provided for module", str(result.get("msg")))

    @patch("builtins.open", new_callable=mock_open)
    @patch("os.path.exists")
    def test_wireless_design_empty_config(self, mock_exists, mock_file):
        mock_exists.return_value = True

        set_module_args(
            dict(
                dnac_host="1.1.1.1",
                dnac_username="dummy",
                dnac_password="dummy",
                dnac_version="2.3.7.9",
                dnac_log=True,
                state="gathered",
                config=self.playbook_config_empty_config,
            )
        )
        result = self.execute_module(changed=False, failed=True)
        self.assertIn(
            "Configuration cannot be an empty dictionary.",
            str(result.get("msg")),
        )

    @patch("builtins.open", new_callable=mock_open)
    @patch("os.path.exists")
    def test_wireless_design_empty_component_specific_filters(self, mock_exists, mock_file):
        mock_exists.return_value = True

        set_module_args(
            dict(
                dnac_host="1.1.1.1",
                dnac_username="dummy",
                dnac_password="dummy",
                dnac_version="2.3.7.9",
                dnac_log=True,
                state="gathered",
                config=self.playbook_config_empty_component_specific_filters,
            )
        )
        result = self.execute_module(changed=False, failed=True)
        self.assertIn(
            "Invalid parameters in playbook config: 'component_specific_filters' is provided but empty.",
            str(result.get("msg")),
        )

    @patch("builtins.open", new_callable=mock_open)
    @patch("os.path.exists")
    def test_wireless_design_invalid_component(self, mock_exists, mock_file):
        mock_exists.return_value = True

        set_module_args(
            dict(
                dnac_host="1.1.1.1",
                dnac_username="dummy",
                dnac_password="dummy",
                dnac_version="2.3.7.9",
                dnac_log=True,
                state="gathered",
                config=self.playbook_config_invalid_component,
            )
        )
        result = self.execute_module(changed=False, failed=True)
        self.assertIn("Invalid network components provided for module", str(result.get("msg")))

    @patch("builtins.open", new_callable=mock_open)
    @patch("os.path.exists")
    def test_wireless_design_invalid_component_filters(self, mock_exists, mock_file):
        mock_exists.return_value = True

        set_module_args(
            dict(
                dnac_host="1.1.1.1",
                dnac_username="dummy",
                dnac_password="dummy",
                dnac_version="2.3.7.9",
                dnac_log=True,
                state="gathered",
                config=self.playbook_config_invalid_component_filters,
            )
        )
        result = self.execute_module(changed=False, failed=True)
        self.assertIn("Invalid filters provided for module", str(result.get("msg")))
