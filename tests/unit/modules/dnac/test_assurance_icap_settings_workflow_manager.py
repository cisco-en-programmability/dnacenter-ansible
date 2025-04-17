# Copyright (c) 2025 Cisco and/or its affiliates.
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

# Make coding more python3-ish
from __future__ import absolute_import, division, print_function

__metaclass__ = type
from unittest.mock import patch
from ansible_collections.cisco.dnac.plugins.modules import assurance_icap_settings_workflow_manager
from .dnac_module import TestDnacModule, set_module_args, loadPlaybookData


class TestDnacAssuranceSettings(TestDnacModule):
    module = assurance_icap_settings_workflow_manager
    test_data = loadPlaybookData("assurance_icap_settings_workflow_manager")
    playbook_config_creation = test_data.get("playbook_config_creation")
    playbook_config_download = test_data.get("playbook_config_download")

    def setUp(self):
        super(TestDnacAssuranceSettings, self).setUp()

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
        super(TestDnacAssuranceSettings, self).tearDown()
        self.mock_dnac_exec.stop()
        self.mock_dnac_init.stop()

    def load_fixtures(self, response=None, device=""):
        """
        Load fixtures for user.
        """
        if "creation" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("get_device_list_for_creation"),
                self.test_data.get("icap_creation"),
                self.test_data.get("get_task_by_id"),
                self.test_data.get("icap_deplyed"),
                self.test_data.get("using_task_id"),
                self.test_data.get("deployment_status"),
            ]

        if "creation_exception" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("get_device_list_for_creation"),
                self.test_data.get("icap_creation")
            ]

        if "discard_exception" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("get_device_list_for_creation"),
                self.test_data.get("icap_creation"),
                self.test_data.get("get_task_by_id"),
            ]

        if "download" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("get_pcap_id"),
                self.test_data.get("download_response"),
            ]

    def test_assurance_icap_settings_workflow_manager_discard_exception(self):
        """
        Test case for exception in discard function while creating Assurance ICAP Settings in Cisco DNA Center.
        """
        set_module_args(
            dict(
                dnac_host="1.1.1.1",
                dnac_username="dummy",
                dnac_password="dummy",
                dnac_version="2.3.7.9",
                dnac_log=True,
                state="merged",
                config=[self.playbook_config_creation]
            )
        )
        result = self.execute_module(changed=True, failed=False)
        print(result["msg"])
        self.assertEqual(
            result["msg"],
            "An exception occurred while discarding ICAP config in Cisco Catalyst Center: "
        )

    def test_assurance_icap_settings_workflow_manager_creation_exception(self):
        """
        Test case for exception while creating Assurance ICAP Settings in Cisco DNA Center.
        """
        set_module_args(
            dict(
                dnac_host="1.1.1.1",
                dnac_username="dummy",
                dnac_password="dummy",
                dnac_version="2.3.7.9",
                dnac_log=True,
                state="merged",
                config=[self.playbook_config_creation]
            )
        )
        result = self.execute_module(changed=True, failed=True)
        print(result["msg"])
        self.assertTrue(
            result["msg"],
            "An exception occurred while creating ICAP config in Cisco Catalyst Center: "
        )

    def test_assurance_icap_settings_workflow_manager_creation(self):
        """
        Test case for creating Assurance ICAP Settings in Cisco DNA Center.
        Verifies that the workflow manager correctly creates ICAP settings
        when a new configuration is applied.
        """
        set_module_args(
            dict(
                dnac_host="1.1.1.1",
                dnac_username="dummy",
                dnac_password="dummy",
                dnac_version="2.3.7.9",
                dnac_log=True,
                state="merged",
                config_verify=True,
                config=[self.playbook_config_creation]
            )
        )
        result = self.execute_module(changed=True, failed=False)
        print(result["msg"])
        self.assertEqual(
            result["msg"],
            "ICAP Configuration 'skibidi' created successfully."
        )

    def test_assurance_icap_settings_workflow_manager_download(self):
        """
        Test case for exception in download Assurance ICAP Settings in Cisco DNA Center.
        """
        set_module_args(
            dict(
                dnac_host="1.1.1.1",
                dnac_username="dummy",
                dnac_password="dummy",
                dnac_version="2.3.7.9",
                dnac_log=True,
                state="merged",
                config_verify=True,
                config=[self.playbook_config_download]
            )
        )
        result = self.execute_module(changed=False, failed=True)
        print(result["msg"])
        self.assertEqual(
            result["msg"],
            "Failed to download ICAP packet traces: 'dict' object has no attribute 'data'"
        )
