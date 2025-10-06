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
    playbook_onboarding_creation = test_data.get("playbook_onboarding_creation")
    playbook_ota_creation = test_data.get("playbook_ota_creation")
    playbook_invalid_capture = test_data.get("playbook_invalid_capture")

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
                self.test_data.get("existing_icap_configuration"),
                self.test_data.get("icap_creation"),
                self.test_data.get("get_task_by_id"),
                self.test_data.get("get_icap_configuration_status_per_network_device"),
                self.test_data.get("generate_device_cli_of_icap_config"),
                self.test_data.get("generate_cli_task"),
                self.test_data.get("retrieves_the_devices_clis_of_the_icap"),
                self.test_data.get("icap_deployed"),
                self.test_data.get("using_task_id"),
                self.test_data.get("deployment_status"),
            ]

        if "creation_exception" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("get_device_list_for_creation"),
                self.test_data.get("icap_creation")
            ]

        if "deletion_icap" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("get_device_list_for_creation"),
                self.test_data.get("icap_creation"),
                self.test_data.get("get_task_by_id"),
                self.test_data.get("get_icap_configuration_status_per_network_device")
            ]

        if "discard_exception" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("response1"),
                self.test_data.get("response2"),
                self.test_data.get("response3"),
                self.test_data.get("response4"),
                self.test_data.get("response5"),
                self.test_data.get("response6"),
                self.test_data.get("response7"),
                self.test_data.get("response8"),
                self.test_data.get("response9"),
            ]

        if "download" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("get_pcap_id"),
                self.test_data.get("download_response"),
            ]

        if "playbook_onboarding_creation" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("response28"),
                self.test_data.get("response29"),
                self.test_data.get("response30"),
                self.test_data.get("response31"),
                self.test_data.get("response32"),
                self.test_data.get("response33"),
                self.test_data.get("response34"),
                self.test_data.get("response35"),
                self.test_data.get("response36"),
                self.test_data.get("response37"),
                self.test_data.get("response38"),
                self.test_data.get("response39"),
            ]
        if "playbook_ota_creation" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("response1"),
                self.test_data.get("response2"),
                self.test_data.get("response3"),
                self.test_data.get("response4"),
                self.test_data.get("response5"),
                self.test_data.get("response6"),
                self.test_data.get("response7"),
                self.test_data.get("response8"),
                self.test_data.get("response9"),
                self.test_data.get("response10"),
                self.test_data.get("response11"),
                self.test_data.get("response12"),
                self.test_data.get("response13"),
                self.test_data.get("response14"),
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
                config=self.playbook_ota_creation
            )
        )
        result = self.execute_module(changed=False, failed=True)
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
        result = self.execute_module(changed=True, failed=True)
        print(result["msg"])
        self.assertEqual(
            result["msg"],
            "Wireless Client MAC address '50:91:E3:47:AC:9E' not found."
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

    def test_assurance_icap_settings_workflow_manager_playbook_onboarding_creation(self):
        """
        Test case for creating Assurance ICAP Settings in Cisco DNA Center.
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
                config=self.playbook_onboarding_creation
            )
        )
        result = self.execute_module(changed=True, failed=False)
        print(result["msg"])
        self.assertEqual(
            result["msg"],
            "ICAP Configuration 'ICAP 2108' created successfully."
        )

    def test_assurance_icap_settings_workflow_manager_playbook_ota_creation(self):
        """
        Test case for creating Assurance ICAP Settings in Cisco DNA Center.
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
                config=self.playbook_ota_creation
            )
        )
        result = self.execute_module(changed=True, failed=False)
        print(result["msg"])
        self.assertEqual(
            result["msg"],
            "ICAP Configuration 'ICAP 2208' created successfully."
        )

    def test_assurance_icap_settings_workflow_manager_deletion_icap(self):
        """
            Test case for exception while deleting Assurance ICAP Settings in Cisco DNA Center.
        """
        set_module_args(
            dict(
                dnac_host="1.1.1.1",
                dnac_username="dummy",
                dnac_password="dummy",
                dnac_version="2.3.7.9",
                dnac_log=True,
                state="merged",
                config=self.playbook_config_creation
            )
        )
        result = self.execute_module(changed=False, failed=True)
        print(result["msg"])
        self.assertTrue(
            result,
            "An exception occurred while creating ICAP config in Cisco Catalyst Center: "
        )

    def test_assurance_icap_settings_workflow_manager_playbook_invalid_capture(self):
        """
        Test case for invalid capture type ICAP Settings in Cisco DNA Center.
        """
        set_module_args(
            dict(
                dnac_host="1.1.1.1",
                dnac_username="dummy",
                dnac_password="dummy",
                dnac_version="2.3.7.9",
                dnac_log=True,
                state="merged",
                config=self.playbook_invalid_capture
            )
        )
        result = self.execute_module(changed=False, failed=True)
        print(result["msg"])
        self.assertTrue(
            result,
            "Invalid capture type provided in assurance_icap_settings: OTAS. Valid options are: FULL, ONBOARDING, OTA, RFSTATS, ANOMALY."
        )
