# Copyright (c) 2025 Cisco and/or its affiliates.

# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at

# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# Make coding more python3-ish

from __future__ import absolute_import, division, print_function

__metaclass__ = type

import copy
import os
import tempfile
from unittest.mock import patch, mock_open
import yaml

from ansible_collections.cisco.dnac.plugins.modules import pnp_playbook_config_generator
from .dnac_module import TestDnacModule, set_module_args, loadPlaybookData


class TestDnacBrownfieldPnpPlaybookGenerator(TestDnacModule):

    module = pnp_playbook_config_generator

    test_data = loadPlaybookData("pnp_playbook_config_generator")

    playbook_pnp_generate_all_configurations = test_data.get("playbook_pnp_generate_all_configurations")
    playbook_component_global_specific_filter = test_data.get("playbook_component_global_specific_filter")
    playbook_no_config = test_data.get("playbook_no_config")

    def setUp(self):
        super(TestDnacBrownfieldPnpPlaybookGenerator, self).setUp()

        self.mock_dnac_init = patch(
            "ansible_collections.cisco.dnac.plugins.module_utils.dnac.DNACSDK.__init__")
        self.run_dnac_init = self.mock_dnac_init.start()
        self.run_dnac_init.return_value = None
        self.mock_dnac_exec = patch(
            "ansible_collections.cisco.dnac.plugins.module_utils.dnac.DNACSDK._exec"
        )
        self.run_dnac_exec = self.mock_dnac_exec.start()

    def tearDown(self):
        super(TestDnacBrownfieldPnpPlaybookGenerator, self).tearDown()
        self.mock_dnac_exec.stop()
        self.mock_dnac_init.stop()

    def _get_written_yaml(self, mock_file):
        handle = mock_file()
        writes = [call.args[0] for call in handle.write.call_args_list]
        return "".join(writes)

    def _get_base_module_args(self, **kwargs):
        args = dict(
            dnac_host="1.1.1.1",
            dnac_username="dummy",
            dnac_password="dummy",
            dnac_log=True,
            state="gathered",
            dnac_version="2.3.7.9",
        )
        args.update(kwargs)
        return args

    def load_fixtures(self, response=None, device=""):
        """
        Load fixtures for user.
        """

        if "playbook_pnp_generate_all_configurations" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("PnPdevices"),
            ]

        elif "playbook_component_global_specific_filter" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("PnPdevices1"),
                self.test_data.get("site_response1"),
                self.test_data.get("site_response2"),
                self.test_data.get("site_response3"),
            ]

        elif "playbook_no_config" in self._testMethodName:
            pass
        elif "default_file_path" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("PnPdevices"),
            ]

    def test_brownfield_pnp_playbook_generator_playbook_pnp_generate_all_configurations(self):
        """
        Test the PnP Playbook Generator's configuration generation process.

        This test verifies that the generator correctly creates YAML configurations
        from all PnP devices, ensuring proper validation and expected behavior.
        """

        with tempfile.TemporaryDirectory() as temp_dir:
            file_path = os.path.join(temp_dir, "pnp_generate_all.yml")
            set_module_args(
                dict(
                    dnac_host="1.1.1.1",
                    dnac_username="dummy",
                    dnac_password="dummy",
                    dnac_log=True,
                    state="gathered",
                    dnac_version="2.3.7.9",
                    file_path=file_path,
                    config=self.playbook_pnp_generate_all_configurations
                )
            )
            result = self.execute_module(changed=True, failed=False)
        print(result)
        self.assertEqual(
            result.get("response").get("message"),
            "YAML config generation succeeded for module 'pnp_workflow_manager'."
        )

    def test_brownfield_pnp_playbook_generator_playbook_component_global_specific_filter(self):
        """
        Test the PnP Playbook Generator with component and global filters.

        This test verifies that the generator correctly handles specific filtering
        of PnP devices, ensuring proper validation and expected behavior.
        """

        set_module_args(
            dict(
                dnac_host="1.1.1.1",
                dnac_username="dummy",
                dnac_password="dummy",
                dnac_log=True,
                state="gathered",
                dnac_version="2.3.7.9",
                config=self.playbook_component_global_specific_filter
            )
        )
        result = self.execute_module(changed=True, failed=False)
        print(result)
        self.assertEqual(
            result.get("response").get("message"),
            "YAML config generation succeeded for module 'pnp_workflow_manager'."
        )

    def test_brownfield_pnp_playbook_generator_playbook_no_config(self):
        """
        Test the PnP Playbook Generator with no configuration.

        This test verifies that the generator correctly handles scenarios
        where no PnP devices are found, ensuring proper validation and expected behavior.
        """

        set_module_args(
            dict(
                dnac_host="1.1.1.1",
                dnac_username="dummy",
                dnac_password="dummy",
                dnac_log=True,
                state="gathered",
                dnac_version="2.3.7.9",
                file_path="/Users/syedkahm/Downloads/pnp_device_info",
                config=self.playbook_no_config
            )
        )
        result = self.execute_module(changed=False, failed=False)
        print(result)
        self.assertEqual(
            result.get("response").get("message"),
            "No PnP devices found matching specified filters. Verify device inventory and filter criteria."
        )

    @patch("builtins.open", new_callable=mock_open)
    def test_brownfield_pnp_playbook_generator_default_file_path(self, mock_file):
        """
        Test the PnP Playbook Generator default filename path when config and file_path are omitted.
        """

        set_module_args(
            dict(
                dnac_host="1.1.1.1",
                dnac_username="dummy",
                dnac_password="dummy",
                dnac_log=False,
                state="gathered",
                dnac_version="2.3.7.9",
            )
        )
        result = self.execute_module(changed=True, failed=False)

        response = result.get("response")
        self.assertEqual(
            response.get("message"),
            "YAML config generation succeeded for module 'pnp_workflow_manager'."
        )
        self.assertIn("file_path", response)
        self.assertTrue(response.get("file_path").endswith(".yml"))
        mock_file.assert_called()
        written_yaml = self._get_written_yaml(mock_file)
        self.assertIn("#  Generated by", written_yaml)
        self.assertIn("#  Generated from", written_yaml)
        self.assertIn("#  Catalyst Center Version", written_yaml)
        data = yaml.safe_load(written_yaml)
        self.assertIsInstance(data, list)
        self.assertIn("config", data[0])

    def test_brownfield_pnp_playbook_generator_overwrite_mode_idempotent_on_matching_local_file(self):
        """
        Test overwrite mode reports no change when the existing local YAML file already matches.
        """
        with tempfile.TemporaryDirectory() as temp_dir:
            file_path = os.path.join(temp_dir, "pnp_overwrite.yml")
            self.run_dnac_exec.side_effect = [
                self.test_data.get("PnPdevices"),
                self.test_data.get("PnPdevices"),
            ]

            set_module_args(
                self._get_base_module_args(
                    file_path=file_path,
                    file_mode="overwrite",
                    config=self.playbook_pnp_generate_all_configurations,
                )
            )
            self.execute_module(changed=True, failed=False)

            set_module_args(
                self._get_base_module_args(
                    file_path=file_path,
                    file_mode="overwrite",
                    config=self.playbook_pnp_generate_all_configurations,
                )
            )
            result = self.execute_module(changed=False, failed=False)

            self.assertEqual(
                result.get("response").get("message"),
                "YAML configuration file already up-to-date for module 'pnp_workflow_manager'. No changes written."
            )
            self.assertEqual(result.get("response").get("status"), "ok")

    def test_brownfield_pnp_playbook_generator_append_mode_idempotent_on_matching_last_entry(self):
        """
        Test append mode reports no change when the last generated config entry already matches.
        """
        with tempfile.TemporaryDirectory() as temp_dir:
            file_path = os.path.join(temp_dir, "pnp_append.yml")
            self.run_dnac_exec.side_effect = [
                self.test_data.get("PnPdevices"),
                self.test_data.get("PnPdevices"),
            ]

            set_module_args(
                self._get_base_module_args(
                    file_path=file_path,
                    file_mode="append",
                    config=self.playbook_pnp_generate_all_configurations,
                )
            )
            self.execute_module(changed=True, failed=False)

            set_module_args(
                self._get_base_module_args(
                    file_path=file_path,
                    file_mode="append",
                    config=self.playbook_pnp_generate_all_configurations,
                )
            )
            result = self.execute_module(changed=False, failed=False)

            with open(file_path, "r") as yaml_file:
                file_content = yaml_file.read()

            parsed_content = yaml.safe_load(file_content)

            self.assertEqual(
                result.get("response").get("message"),
                "YAML configuration file already up-to-date for module 'pnp_workflow_manager'. No changes written."
            )
            self.assertEqual(result.get("response").get("status"), "ok")
            self.assertEqual(file_content.count("---"), 1)
            self.assertEqual(file_content.count("- config:"), 1)
            self.assertIsInstance(parsed_content, list)
            self.assertEqual(len(parsed_content), 1)

    def test_brownfield_pnp_playbook_generator_append_mode_adds_new_entry_without_new_separator(self):
        """
        Test append mode writes a second config entry without adding another YAML document separator.
        """
        updated_devices = copy.deepcopy(self.test_data.get("PnPdevices"))
        updated_devices[0]["deviceInfo"]["serialNumber"] = "UPDATED123456"

        with tempfile.TemporaryDirectory() as temp_dir:
            file_path = os.path.join(temp_dir, "pnp_append_diff.yml")
            self.run_dnac_exec.side_effect = [
                self.test_data.get("PnPdevices"),
                updated_devices,
            ]

            set_module_args(
                self._get_base_module_args(
                    file_path=file_path,
                    file_mode="append",
                    config=self.playbook_pnp_generate_all_configurations,
                )
            )
            self.execute_module(changed=True, failed=False)

            set_module_args(
                self._get_base_module_args(
                    file_path=file_path,
                    file_mode="append",
                    config=self.playbook_pnp_generate_all_configurations,
                )
            )
            self.execute_module(changed=True, failed=False)

            with open(file_path, "r") as yaml_file:
                file_content = yaml_file.read()

            parsed_content = yaml.safe_load(file_content)

            self.assertEqual(file_content.count("---"), 1)
            self.assertIsInstance(parsed_content, list)
            self.assertEqual(len(parsed_content), 2)
            self.assertEqual(
                parsed_content[-1]["config"][0]["device_info"][0]["serial_number"],
                "UPDATED123456"
            )
