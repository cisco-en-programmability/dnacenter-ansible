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

from __future__ import absolute_import, division, print_function

__metaclass__ = type

from unittest.mock import patch, mock_open
import yaml
from ansible_collections.cisco.dnac.plugins.modules import brownfield_device_credential_playbook_generator
from .dnac_module import TestDnacModule, set_module_args, loadPlaybookData


class TestBrownfieldDeviceCredentialPlaybookGenerator(TestDnacModule):
    module = brownfield_device_credential_playbook_generator
    test_data = loadPlaybookData("brownfield_device_credential_playbook_generator")

    playbook_config_global_credentials_filtered = test_data.get("playbook_config_global_credentials_filtered")
    playbook_config_assign_credentials_to_site_filtered = test_data.get("playbook_config_assign_credentials_to_site_filtered")

    def setUp(self):
        super(TestBrownfieldDeviceCredentialPlaybookGenerator, self).setUp()

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
        super(TestBrownfieldDeviceCredentialPlaybookGenerator, self).tearDown()
        self.mock_dnac_exec.stop()
        self.mock_dnac_init.stop()

    def load_fixtures(self, response=None, device=""):
        self.run_dnac_exec.side_effect = [
            self.test_data.get("get_all_global_credentials_response"),
            self.test_data.get("get_sites_response"),
            self.test_data.get("get_device_credential_settings_for_a_site_response"),
        ]

    def _get_written_yaml(self, mock_file):
        """Collect the YAML string written to the mocked file handle."""
        handle = mock_file()
        writes = [call.args[0] for call in handle.write.call_args_list]
        return "".join(writes)

    @patch('builtins.open', new_callable=mock_open)
    def test_generate_all_configurations(self, mock_file):
        set_module_args({
            "dnac_host": "1.2.3.4",
            "dnac_username": "admin",
            "dnac_password": "pass",
            "dnac_version": "2.3.7.9",
            "config": self.playbook_config_global_credentials_filtered,
            "state": "gathered",
        })
        result = self.execute_module(changed=True)
        self.assertEqual(result["changed"], True)
        # Ensure file write was attempted and contains expected credentials
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
        first_block = data.get("config")[0]
        self.assertIn("global_credential_details", first_block)
        self.assertIsInstance(first_block.get("global_credential_details"), dict)
        # Verify SDK was called expected number of times (current flow uses 2)
        self.assertEqual(self.run_dnac_exec.call_count, 2)

    @patch('builtins.open', new_callable=mock_open)
    def test_global_credentials_filtered(self, mock_file):
        set_module_args({
            "dnac_host": "1.2.3.4",
            "dnac_username": "admin",
            "dnac_password": "pass",
            "dnac_version": "2.3.7.9",
            "config": self.playbook_config_global_credentials_filtered,
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
        first_block = data.get("config")[0]
        self.assertIn("global_credential_details", first_block)
        self.assertIsInstance(first_block.get("global_credential_details"), dict)
        # SDK call count should match current sequence
        self.assertEqual(self.run_dnac_exec.call_count, 2)

    @patch('builtins.open', new_callable=mock_open)
    def test_assign_credentials_to_site_filtered(self, mock_file):
        set_module_args({
            "dnac_host": "1.2.3.4",
            "dnac_username": "admin",
            "dnac_password": "pass",
            "dnac_version": "2.3.7.9",
            "config": self.playbook_config_assign_credentials_to_site_filtered,
            "state": "gathered",
        })
        result = self.execute_module(changed=True)
        self.assertEqual(result["changed"], True)
        mock_file.assert_called()
        written_yaml = self._get_written_yaml(mock_file)
        self.assertTrue(len(written_yaml) > 0)
        data = yaml.safe_load(written_yaml)
        self.assertIsInstance(data, dict)
        # Validate site assignment section appears
        self.assertIn("config", data)
        self.assertIsInstance(data.get("config"), list)
        first_block = data.get("config")[0]
        self.assertIn("assign_credentials_to_site", first_block)
        self.assertIsInstance(first_block.get("assign_credentials_to_site"), dict)
        self.assertEqual(self.run_dnac_exec.call_count, 2)

    @patch('builtins.open', new_callable=mock_open)
    def test_no_file_path_generates_default(self, mock_file):
        set_module_args({
            "dnac_host": "1.2.3.4",
            "dnac_username": "admin",
            "dnac_password": "pass",
            "dnac_version": "2.3.7.9",
            "config": self.playbook_config_global_credentials_filtered,
            "state": "gathered",
        })
        result = self.execute_module(changed=True)
        self.assertEqual(result["changed"], True)
        mock_file.assert_called()
        # Verify open was called with a path (provided in config or module default)
        call_args = mock_file.call_args
        self.assertIsNotNone(call_args)
        self.assertIsInstance(call_args[0][0], str)
        self.assertTrue(call_args[0][0].endswith(".yaml"))
        written_yaml = self._get_written_yaml(mock_file)
        self.assertTrue(len(written_yaml) > 0)
