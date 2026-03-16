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

from __future__ import absolute_import, division, print_function

__metaclass__ = type

from unittest.mock import patch, mock_open
import yaml
from ansible_collections.cisco.dnac.plugins.modules import sda_host_port_onboarding_playbook_config_generator
from .dnac_module import TestDnacModule, set_module_args, loadPlaybookData


class TestSdaHostPortOnboardingPlaybookConfigGenerator(TestDnacModule):
    module = sda_host_port_onboarding_playbook_config_generator
    test_data = loadPlaybookData("sda_host_port_onboarding_playbook_config_generator")

    playbook_config_generate_all_configurations = test_data.get("playbook_config_generate_all_configurations")
    playbook_config_port_assignments_filtered = test_data.get("playbook_config_port_assignments_filtered")
    playbook_config_port_channels_filtered = test_data.get("playbook_config_port_channels_filtered")
    playbook_config_wireless_ssids_filtered = test_data.get("playbook_config_wireless_ssids_filtered")
    playbook_config_all_components_filtered = test_data.get("playbook_config_all_components_filtered")

    def setUp(self):
        super(TestSdaHostPortOnboardingPlaybookConfigGenerator, self).setUp()

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
        super(TestSdaHostPortOnboardingPlaybookConfigGenerator, self).tearDown()
        self.mock_dnac_exec.stop()
        self.mock_dnac_init.stop()

    def load_fixtures(self, response=None, device=""):
        def mock_dnac_exec(family, function, op_modifies, params=None):
            if function == "get_port_assignments":
                return self.test_data.get("get_port_assignments_response")
            elif function == "get_port_channels":
                return self.test_data.get("get_port_channels_response")
            elif function == "retrieve_the_vlans_and_ssids_mapped_to_the_vlan_within_a_fabric_site":
                return self.test_data.get("get_vlans_and_ssids_response")
            elif function == "get_device_by_id":
                # Handle device-specific responses based on device ID in params
                if params and "id" in params:
                    device_id = params["id"]
                    if device_id == "device-001":
                        return self.test_data.get("get_device_by_id_response_device_001")
                    elif device_id == "device-002":
                        return self.test_data.get("get_device_by_id_response_device_002")
                return self.test_data.get("get_device_by_id_response_device_001")
            elif function == "get_fabric_sites":
                return self.test_data.get("get_fabric_sites_response")
            elif function == "get_sites":
                return self.test_data.get("get_sites_response")
            else:
                return self.test_data.get("empty_response", {"response": []})

        self.run_dnac_exec.side_effect = mock_dnac_exec

    def _get_written_yaml(self, mock_file):
        """Collect the YAML string written to the mocked file handle."""
        handle = mock_file()
        writes = [call.args[0] for call in handle.write.call_args_list]
        return "".join(writes)

    @patch('builtins.open', new_callable=mock_open)
    def test_generate_all_configurations(self, mock_file):
        """Test generation of all SDA host port onboarding configurations."""
        set_module_args({
            "dnac_host": "1.2.3.4",
            "dnac_username": "admin",
            "dnac_password": "pass",
            "dnac_version": "2.3.7.9",
            "config": self.playbook_config_generate_all_configurations,
            "state": "gathered",
        })
        result = self.execute_module(changed=True)
        self.assertEqual(result["changed"], True)
        # Ensure file write was attempted and contains expected data
        mock_file.assert_called()
        written_yaml = self._get_written_yaml(mock_file)
        self.assertTrue(len(written_yaml) > 0, "No YAML content was written")
        # Basic YAML parse to validate structure
        data = yaml.safe_load(written_yaml)
        self.assertIsInstance(data, dict)
        # Validate presence of top-level keys written by the module
        self.assertIn("config", data)
        self.assertIsInstance(data.get("config"), list)
        self.assertGreaterEqual(len(data.get("config")), 1)
        # Verify SDK was called
        self.assertGreater(self.run_dnac_exec.call_count, 0)

    @patch('builtins.open', new_callable=mock_open)
    def test_port_assignments_filtered(self, mock_file):
        """Test filtering port assignments by fabric site."""
        set_module_args({
            "dnac_host": "1.2.3.4",
            "dnac_username": "admin",
            "dnac_password": "pass",
            "dnac_version": "2.3.7.9",
            "config": self.playbook_config_port_assignments_filtered,
            "state": "gathered",
        })
        result = self.execute_module(changed=True)
        self.assertEqual(result["changed"], True)
        mock_file.assert_called()
        written_yaml = self._get_written_yaml(mock_file)
        self.assertTrue(len(written_yaml) > 0)
        data = yaml.safe_load(written_yaml)
        self.assertIsInstance(data, dict)
        # Ensure expected block exists
        self.assertIn("config", data)
        self.assertIsInstance(data.get("config"), list)
        # Verify that port assignments are present
        config_blocks = data.get("config")
        has_port_assignments = any(
            "port_assignments" in block for block in config_blocks
        )
        self.assertTrue(has_port_assignments, "Port assignments not found in generated YAML")
        # Verify SDK was called
        self.assertGreater(self.run_dnac_exec.call_count, 0)

    @patch('builtins.open', new_callable=mock_open)
    def test_port_channels_filtered(self, mock_file):
        """Test filtering port channels by fabric site."""
        set_module_args({
            "dnac_host": "1.2.3.4",
            "dnac_username": "admin",
            "dnac_password": "pass",
            "dnac_version": "2.3.7.9",
            "config": self.playbook_config_port_channels_filtered,
            "state": "gathered",
        })
        result = self.execute_module(changed=True)
        self.assertEqual(result["changed"], True)
        mock_file.assert_called()
        written_yaml = self._get_written_yaml(mock_file)
        self.assertTrue(len(written_yaml) > 0)
        data = yaml.safe_load(written_yaml)
        self.assertIsInstance(data, dict)
        # Ensure expected block exists
        self.assertIn("config", data)
        self.assertIsInstance(data.get("config"), list)
        # Verify that port channels are present
        config_blocks = data.get("config")
        has_port_channels = any(
            "port_channels" in block for block in config_blocks
        )
        self.assertTrue(has_port_channels, "Port channels not found in generated YAML")
        # Verify SDK was called
        self.assertGreater(self.run_dnac_exec.call_count, 0)

    @patch('builtins.open', new_callable=mock_open)
    def test_wireless_ssids_filtered(self, mock_file):
        """Test filtering wireless SSIDs by fabric site."""
        set_module_args({
            "dnac_host": "1.2.3.4",
            "dnac_username": "admin",
            "dnac_password": "pass",
            "dnac_version": "2.3.7.9",
            "config": self.playbook_config_wireless_ssids_filtered,
            "state": "gathered",
        })
        result = self.execute_module(changed=True)
        self.assertEqual(result["changed"], True)
        mock_file.assert_called()
        written_yaml = self._get_written_yaml(mock_file)
        self.assertTrue(len(written_yaml) > 0)
        data = yaml.safe_load(written_yaml)
        self.assertIsInstance(data, dict)
        # Ensure expected block exists
        self.assertIn("config", data)
        self.assertIsInstance(data.get("config"), list)
        # Verify that wireless SSIDs are present
        config_blocks = data.get("config")
        has_wireless_ssids = any(
            "wireless_ssids" in block for block in config_blocks
        )
        self.assertTrue(has_wireless_ssids, "Wireless SSIDs not found in generated YAML")
        # Verify SDK was called
        self.assertGreater(self.run_dnac_exec.call_count, 0)

    @patch('builtins.open', new_callable=mock_open)
    def test_all_components_filtered(self, mock_file):
        """Test filtering all components (port assignments, port channels, wireless SSIDs)."""
        set_module_args({
            "dnac_host": "1.2.3.4",
            "dnac_username": "admin",
            "dnac_password": "pass",
            "dnac_version": "2.3.7.9",
            "config": self.playbook_config_all_components_filtered,
            "state": "gathered",
        })
        result = self.execute_module(changed=True)
        self.assertEqual(result["changed"], True)
        mock_file.assert_called()
        written_yaml = self._get_written_yaml(mock_file)
        self.assertTrue(len(written_yaml) > 0)
        data = yaml.safe_load(written_yaml)
        self.assertIsInstance(data, dict)
        # Ensure expected block exists
        self.assertIn("config", data)
        self.assertIsInstance(data.get("config"), list)
        # Verify SDK was called multiple times for all components
        self.assertGreater(self.run_dnac_exec.call_count, 0)

    @patch('builtins.open', new_callable=mock_open)
    def test_no_file_path_generates_default(self, mock_file):
        """Test that default file path is generated when not specified."""
        set_module_args({
            "dnac_host": "1.2.3.4",
            "dnac_username": "admin",
            "dnac_password": "pass",
            "dnac_version": "2.3.7.9",
            "config": self.playbook_config_port_assignments_filtered,
            "state": "gathered",
        })
        result = self.execute_module(changed=True)
        self.assertEqual(result["changed"], True)
        mock_file.assert_called()
        # Verify open was called with a path (provided in config or module default)
        call_args = mock_file.call_args
        self.assertIsNotNone(call_args)
        self.assertIsInstance(call_args[0][0], str)
        self.assertTrue(call_args[0][0].endswith(".yaml") or call_args[0][0].endswith(".yml"))
        written_yaml = self._get_written_yaml(mock_file)
        self.assertTrue(len(written_yaml) > 0)

    @patch('builtins.open', new_callable=mock_open)
    def test_device_id_to_management_ip_resolution(self, mock_file):
        """Test that device IDs are resolved to management IP addresses."""
        set_module_args({
            "dnac_host": "1.2.3.4",
            "dnac_username": "admin",
            "dnac_password": "pass",
            "dnac_version": "2.3.7.9",
            "config": self.playbook_config_port_assignments_filtered,
            "state": "gathered",
        })
        result = self.execute_module(changed=True)
        self.assertEqual(result["changed"], True)
        mock_file.assert_called()
        written_yaml = self._get_written_yaml(mock_file)
        self.assertTrue(len(written_yaml) > 0)
        data = yaml.safe_load(written_yaml)
        # Check that management IP addresses are present in the generated YAML
        config_blocks = data.get("config", [])
        self.assertGreater(len(config_blocks), 0, "No config blocks found")
        for block in config_blocks:
            if "port_assignments" in block:
                # Verify that ip_address field exists in block
                self.assertIn("ip_address", block)
                # Verify the IP address is not empty
                self.assertTrue(len(block.get("ip_address", "")) > 0)
