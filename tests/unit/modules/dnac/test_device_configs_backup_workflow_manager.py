# Copyright (c) 2020 Cisco and/or its affiliates.
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
from unittest.mock import patch, Mock, MagicMock
import time
import pathlib
from ansible_collections.cisco.dnac.plugins.modules import device_configs_backup_workflow_manager
from .dnac_module import TestDnacModule, set_module_args, loadPlaybookData


class TestDeviceConfigsBackup(TestDnacModule):
    module = device_configs_backup_workflow_manager
    test_data = loadPlaybookData("device_configs_backup_workflow_manager_intent")

    def setUp(self):
        super(TestDeviceConfigsBackup, self).setUp()

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

        # Patch the unzip_data method within the module
        self.mock_unzip_data = patch(
            "ansible_collections.cisco.dnac.plugins.modules.device_configs_backup_workflow_manager.DeviceConfigsBackup.unzip_data"
        )
        self.run_unzip_data = self.mock_unzip_data.start()
        self.run_unzip_data.return_value = True  # Simulate successful unzipping

        # Mock file system interactions
        backup_path = pathlib.Path(
            "/Users/rukapse/ansible/dnac/work/collections/ansible_collections/"
            "cisco/dnac/tests/unit/modules/dnac/backup"
        )

        self.mock_pathlib_resolve = patch(
            "pathlib.Path.resolve",
            return_value=backup_path
        )
        self.mock_iterdir = patch("pathlib.Path.iterdir")
        self.mock_stat = patch("pathlib.Path.stat")
        self.mock_is_dir = patch("pathlib.Path.is_dir", return_value=True)

        self.mock_resolve = self.mock_pathlib_resolve.start()
        self.mock_iterdir = self.mock_iterdir.start()
        self.mock_stat = self.mock_stat.start()
        self.mock_is_dir = self.mock_is_dir.start()

        # Set return values for mocked methods
        mock_file = MagicMock()
        mock_file.name = "backup"
        mock_file.stat.return_value.st_mtime = time.time() - 5

        self.mock_iterdir.return_value = [mock_file]

    def tearDown(self):
        super(TestDeviceConfigsBackup, self).tearDown()
        self.mock_dnac_init.stop()
        self.mock_dnac_exec.stop()
        self.mock_unzip_data.stop()
        self.mock_pathlib_resolve.stop()
        self.mock_iterdir.stop()
        self.mock_stat.stop()
        self.mock_is_dir.stop()

    def load_fixtures(self, response=None, device=""):
        print("Inside load_fixtures")

        self.mock_download_response = Mock()

        if "device_configs_backup_success_scenario_1" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("response_get_devices_list_success"),
                self.test_data.get("response_get_task_id_success"),
                self.test_data.get("response_get_task_status_by_id_success"),
                self.test_data.get("response_get_task_details_response"),
                self.mock_download_response
            ]

        # Run device config backup scenario 2
        if "device_configs_backup_success_scenario_2" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("response_get_devices_list_success"),
                self.test_data.get("response_get_task_id_success"),
                self.test_data.get("response_get_task_status_by_id_success"),
                self.test_data.get("response_get_task_details_response"),
                self.mock_download_response
            ]

        # Run device config backup scenario 3
        if "device_configs_backup_success_scenario_3" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("response_get_devices_list_success_2"),
                self.test_data.get("response_get_task_id_success"),
                self.test_data.get("response_get_task_status_by_id_success"),
                self.test_data.get("response_get_task_details_response"),
                self.mock_download_response
            ]

        # Run device config backup scenario 4
        if "device_configs_backup_success_scenario_4" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("response_get_sites"),
                self.test_data.get("response_get_site_assigned_networks"),
                self.test_data.get("response_get_device_by_id"),
                self.test_data.get("response_get_device_by_id_2"),
                self.test_data.get("response_get_task_id_success"),
                self.test_data.get("response_get_task_status_by_id_success"),
                self.test_data.get("response_get_task_details_response"),
                self.mock_download_response
            ]

        # FIXTURE FOR FAILURE TESTCASES ############################################################
        if "device_configs_backup_failure_scenario_1_1" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                Exception("Simulated exception")
            ]

        if "device_configs_backup_failure_scenario_1_2" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("response_get_devices_list_success"),
                Exception("Simulated exception")
            ]

        if "device_configs_backup_failure_scenario_1_3" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("response_get_devices_list_success"),
                self.test_data.get("response_get_task_id_success"),
                Exception("Simulated exception")
            ]

        if "device_configs_backup_failure_scenario_1_4" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("response_get_devices_list_success"),
                self.test_data.get("response_get_task_id_success"),
                self.test_data.get("response_get_task_status_by_id_success"),
                Exception("Simulated exception")

            ]

        if "device_configs_backup_failure_scenario_1_5" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("response_get_devices_list_success"),
                self.test_data.get("response_get_task_id_success"),
                self.test_data.get("response_get_task_status_by_id_success"),
                self.test_data.get("response_get_task_details_response"),
                Exception("Simulated exception")

            ]

        if "device_configs_backup_success_scenario_4_1" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                Exception("Simulated exception")
            ]

        if "device_configs_backup_success_scenario_4_2" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("response_get_sites"),
                Exception("Simulated exception")
            ]

        if "device_configs_backup_success_scenario_4_3" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("response_get_sites"),
                self.test_data.get("response_get_site_assigned_networks"),
                Exception("Simulated exception")
            ]

        if "device_configs_backup_success_scenario_4_4" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("response_get_sites"),
                self.test_data.get("response_get_site_assigned_networks"),
                self.test_data.get("response_get_device_by_id"),
                Exception("Simulated exception")
            ]

        if "device_configs_backup_success_scenario_4_5" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("response_get_sites"),
                self.test_data.get("response_get_site_assigned_networks"),
                self.test_data.get("response_get_device_by_id"),
                self.test_data.get("response_get_device_by_id_2"),
                Exception("Simulated exception")
            ]

        if "device_configs_backup_success_scenario_4_6" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("response_get_sites"),
                self.test_data.get("response_get_site_assigned_networks"),
                self.test_data.get("response_get_device_by_id"),
                self.test_data.get("response_get_device_by_id_2"),
                self.test_data.get("response_get_task_id_success"),
                Exception("Simulated exception")
            ]

        if "device_configs_backup_success_scenario_4_7" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("response_get_sites"),
                self.test_data.get("response_get_site_assigned_networks"),
                self.test_data.get("response_get_device_by_id"),
                self.test_data.get("response_get_device_by_id_2"),
                self.test_data.get("response_get_task_id_success"),
                self.test_data.get("response_get_task_status_by_id_success"),
                Exception("Simulated exception")
            ]

        if "device_configs_backup_success_scenario_4_8" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("response_get_sites"),
                self.test_data.get("response_get_site_assigned_networks"),
                self.test_data.get("response_get_device_by_id"),
                self.test_data.get("response_get_device_by_id_2"),
                self.test_data.get("response_get_task_id_success"),
                self.test_data.get("response_get_task_status_by_id_success"),
                self.test_data.get("response_get_task_details_response"),
                Exception("Simulated exception")
            ]
# SUCCESS TESTCASES ########################################################################################

    def test_device_configs_backup_success_scenario_1(self):
        print("Test Data: {test_data}".format(test_data=self.test_data.get("playbook_config_device_configs_backup_scenario_1")))

        set_module_args(
            dict(
                dnac_host="1.1.1.1",
                dnac_username="dummy",
                dnac_password="dummy",
                dnac_log=False,
                dnac_log_level="DEBUG",
                dnac_version="2.3.7.9",
                config_verify=True,
                dnac_log_append=False,
                state="merged",
                config=self.test_data.get("playbook_config_device_configs_backup_scenario_1"),
            )
        )
        result = self.execute_module(changed=True, failed=False)
        self.assertIn(
            "Backup Device Configuration task has been successfully performed",
            result.get("msg"),
        )

    def test_device_configs_backup_success_scenario_2(self):
        print("Test Data: {test_data}".format(test_data=self.test_data.get("playbook_config_device_configs_backup_scenario_2")))

        set_module_args(
            dict(
                dnac_host="1.1.1.1",
                dnac_username="dummy",
                dnac_password="dummy",
                dnac_log=False,
                dnac_log_level="DEBUG",
                dnac_version="2.3.7.9",
                config_verify=True,
                dnac_log_append=False,
                state="merged",
                config=self.test_data.get("playbook_config_device_configs_backup_scenario_2"),
            )
        )
        result = self.execute_module(changed=True, failed=False)
        self.assertIn(
            "Backup Device Configuration task has been successfully performed",
            result.get("msg"),
        )

    def test_device_configs_backup_success_scenario_3(self):
        print("Test Data: {test_data}".format(test_data=self.test_data.get("playbook_config_device_configs_backup_scenario_3")))

        set_module_args(
            dict(
                dnac_host="1.1.1.1",
                dnac_username="dummy",
                dnac_password="dummy",
                dnac_log=False,
                dnac_log_level="DEBUG",
                dnac_version="2.3.7.9",
                config_verify=True,
                dnac_log_append=False,
                state="merged",
                config=self.test_data.get("playbook_config_device_configs_backup_scenario_3"),
            )
        )
        result = self.execute_module(changed=True, failed=False)
        self.assertIn(
            "Backup Device Configuration task has been successfully performed",
            result.get("msg"),
        )

    def test_device_configs_backup_success_scenario_4(self):
        print("Test Data: {test_data}".format(test_data=self.test_data.get("playbook_config_device_configs_backup_scenario_4")))

        set_module_args(
            dict(
                dnac_host="1.1.1.1",
                dnac_username="dummy",
                dnac_password="dummy",
                dnac_log=False,
                dnac_log_level="DEBUG",
                dnac_version="2.3.7.9",
                config_verify=True,
                dnac_log_append=False,
                state="merged",
                config=self.test_data.get("playbook_config_device_configs_backup_scenario_4"),
            )
        )
        result = self.execute_module(changed=True, failed=False)
        self.assertIn(
            "Backup Device Configuration task has been successfully performed",
            result.get("msg"),
        )

# FAILURE TESTCASES ########################################################################################

    def test_device_configs_backup_failure_scenario_1_1(self):
        print("Test Data: {test_data}".format(test_data=self.test_data.get("playbook_config_device_configs_backup_scenario_1")))

        set_module_args(
            dict(
                dnac_host="1.1.1.1",
                dnac_username="dummy",
                dnac_password="dummy",
                dnac_log=False,
                dnac_log_level="DEBUG",
                dnac_version="2.3.7.9",
                config_verify=True,
                dnac_log_append=False,
                state="merged",
                config=self.test_data.get("playbook_config_device_configs_backup_scenario_1"),
            )
        )
        result = self.execute_module(changed=False, failed=True)
        self.assertIn(
            "No reachable devices found among the provided parameters",
            result.get("msg"),
        )

    def test_device_configs_backup_failure_scenario_1_2(self):
        print("Test Data: {test_data}".format(test_data=self.test_data.get("playbook_config_device_configs_backup_scenario_1")))

        set_module_args(
            dict(
                dnac_host="1.1.1.1",
                dnac_username="dummy",
                dnac_password="dummy",
                dnac_log=False,
                dnac_log_level="DEBUG",
                dnac_version="2.3.7.9",
                config_verify=True,
                dnac_log_append=False,
                state="merged",
                config=self.test_data.get("playbook_config_device_configs_backup_scenario_1"),
            )
        )
        result = self.execute_module(changed=False, failed=True)
        self.assertIn(
            "An error occurred while executing API call to Function: 'export_device_configurations'",
            result.get("msg"),
        )

    def test_device_configs_backup_failure_scenario_1_3(self):
        print("Test Data: {test_data}".format(test_data=self.test_data.get("playbook_config_device_configs_backup_scenario_1")))

        set_module_args(
            dict(
                dnac_host="1.1.1.1",
                dnac_username="dummy",
                dnac_password="dummy",
                dnac_log=False,
                dnac_log_level="DEBUG",
                dnac_version="2.3.7.9",
                config_verify=True,
                dnac_log_append=False,
                state="merged",
                config=self.test_data.get("playbook_config_device_configs_backup_scenario_1"),
            )
        )
        result = self.execute_module(changed=False, failed=True)
        self.assertIn(
            "An error occurred while executing API call to Function: 'get_tasks_by_id'",
            result.get("msg"),
        )

    def test_device_configs_backup_failure_scenario_1_4(self):
        print("Test Data: {test_data}".format(test_data=self.test_data.get("playbook_config_device_configs_backup_scenario_1")))

        set_module_args(
            dict(
                dnac_host="1.1.1.1",
                dnac_username="dummy",
                dnac_password="dummy",
                dnac_log=False,
                dnac_log_level="DEBUG",
                dnac_version="2.3.7.9",
                config_verify=True,
                dnac_log_append=False,
                state="merged",
                config=self.test_data.get("playbook_config_device_configs_backup_scenario_1"),
            )
        )
        result = self.execute_module(changed=False, failed=True)
        self.assertIn(
            "An error occurred while executing API call to Function: 'get_tasks_by_id'",
            result.get("msg"),
        )

    def test_device_configs_backup_failure_scenario_1_5(self):
        print("Test Data: {test_data}".format(test_data=self.test_data.get("playbook_config_device_configs_backup_scenario_1")))

        set_module_args(
            dict(
                dnac_host="1.1.1.1",
                dnac_username="dummy",
                dnac_password="dummy",
                dnac_log=False,
                dnac_log_level="DEBUG",
                dnac_version="2.3.7.9",
                config_verify=True,
                dnac_log_append=False,
                state="merged",
                config=self.test_data.get("playbook_config_device_configs_backup_scenario_1"),
            )
        )
        result = self.execute_module(changed=False, failed=True)
        self.assertIn(
            "could not be downloaded",
            result.get("msg"),
        )

    def test_device_configs_backup_success_scenario_4_1(self):
        print("Test Data: {test_data}".format(test_data=self.test_data.get("playbook_config_device_configs_backup_scenario_4")))

        set_module_args(
            dict(
                dnac_host="1.1.1.1",
                dnac_username="dummy",
                dnac_password="dummy",
                dnac_log=False,
                dnac_log_level="DEBUG",
                dnac_version="2.3.7.9",
                config_verify=True,
                dnac_log_append=False,
                state="merged",
                config=self.test_data.get("playbook_config_device_configs_backup_scenario_4"),
            )
        )
        result = self.execute_module(changed=False, failed=True)
        self.assertIn(
            "An exception occurred while retrieving Site details for Site",
            result.get("msg"),
        )

    def test_device_configs_backup_success_scenario_4_2(self):
        print("Test Data: {test_data}".format(test_data=self.test_data.get("playbook_config_device_configs_backup_scenario_4")))

        set_module_args(
            dict(
                dnac_host="1.1.1.1",
                dnac_username="dummy",
                dnac_password="dummy",
                dnac_log=False,
                dnac_log_level="DEBUG",
                dnac_version="2.3.7.9",
                config_verify=True,
                dnac_log_append=False,
                state="merged",
                config=self.test_data.get("playbook_config_device_configs_backup_scenario_4"),
            )
        )
        result = self.execute_module(changed=False, failed=True)
        self.assertIn(
            "An error occurred while executing GET API call to Function: 'get_site_assig",
            result.get("msg"),
        )

    def test_device_configs_backup_success_scenario_4_3(self):
        print("Test Data: {test_data}".format(test_data=self.test_data.get("playbook_config_device_configs_backup_scenario_4")))

        set_module_args(
            dict(
                dnac_host="1.1.1.1",
                dnac_username="dummy",
                dnac_password="dummy",
                dnac_log=False,
                dnac_log_level="DEBUG",
                dnac_version="2.3.7.9",
                config_verify=True,
                dnac_log_append=False,
                state="merged",
                config=self.test_data.get("playbook_config_device_configs_backup_scenario_4"),
            )
        )
        result = self.execute_module(changed=False, failed=True)
        self.assertIn(
            "An error occurred while executing GET API call to Function: 'get_device_by_id",
            result.get("msg"),
        )

    def test_device_configs_backup_success_scenario_4_4(self):
        print("Test Data: {test_data}".format(test_data=self.test_data.get("playbook_config_device_configs_backup_scenario_4")))

        set_module_args(
            dict(
                dnac_host="1.1.1.1",
                dnac_username="dummy",
                dnac_password="dummy",
                dnac_log=False,
                dnac_log_level="DEBUG",
                dnac_version="2.3.7.9",
                config_verify=True,
                dnac_log_append=False,
                state="merged",
                config=self.test_data.get("playbook_config_device_configs_backup_scenario_4"),
            )
        )
        result = self.execute_module(changed=False, failed=True)
        self.assertIn(
            "An error occurred while executing GET API call to Function: 'get_device_by_id'",
            result.get("msg"),
        )

    def test_device_configs_backup_success_scenario_4_5(self):
        print("Test Data: {test_data}".format(test_data=self.test_data.get("playbook_config_device_configs_backup_scenario_4")))

        set_module_args(
            dict(
                dnac_host="1.1.1.1",
                dnac_username="dummy",
                dnac_password="dummy",
                dnac_log=False,
                dnac_log_level="DEBUG",
                dnac_version="2.3.7.9",
                config_verify=True,
                dnac_log_append=False,
                state="merged",
                config=self.test_data.get("playbook_config_device_configs_backup_scenario_4"),
            )
        )
        result = self.execute_module(changed=False, failed=True)
        self.assertIn(
            "An error occurred while executing API call to Function: 'export_device_configurations'",
            result.get("msg"),
        )

    def test_device_configs_backup_success_scenario_4_6(self):
        print("Test Data: {test_data}".format(test_data=self.test_data.get("playbook_config_device_configs_backup_scenario_4")))

        set_module_args(
            dict(
                dnac_host="1.1.1.1",
                dnac_username="dummy",
                dnac_password="dummy",
                dnac_log=False,
                dnac_log_level="DEBUG",
                dnac_version="2.3.7.9",
                config_verify=True,
                dnac_log_append=False,
                state="merged",
                config=self.test_data.get("playbook_config_device_configs_backup_scenario_4"),
            )
        )
        result = self.execute_module(changed=False, failed=True)
        self.assertIn(
            "An error occurred while executing API call to Function: 'get_tasks_by_id'",
            result.get("msg"),
        )

    def test_device_configs_backup_success_scenario_4_7(self):
        print("Test Data: {test_data}".format(test_data=self.test_data.get("playbook_config_device_configs_backup_scenario_4")))

        set_module_args(
            dict(
                dnac_host="1.1.1.1",
                dnac_username="dummy",
                dnac_password="dummy",
                dnac_log=False,
                dnac_log_level="DEBUG",
                dnac_version="2.3.7.9",
                config_verify=True,
                dnac_log_append=False,
                state="merged",
                config=self.test_data.get("playbook_config_device_configs_backup_scenario_4"),
            )
        )
        result = self.execute_module(changed=False, failed=True)
        self.assertIn(
            "An error occurred while executing API call to Function: 'get_tasks_by_id'",
            result.get("msg"),
        )

    def test_device_configs_backup_success_scenario_4_8(self):
        print("Test Data: {test_data}".format(test_data=self.test_data.get("playbook_config_device_configs_backup_scenario_4")))

        set_module_args(
            dict(
                dnac_host="1.1.1.1",
                dnac_username="dummy",
                dnac_password="dummy",
                dnac_log=False,
                dnac_log_level="DEBUG",
                dnac_version="2.3.7.9",
                config_verify=True,
                dnac_log_append=False,
                state="merged",
                config=self.test_data.get("playbook_config_device_configs_backup_scenario_4"),
            )
        )
        result = self.execute_module(changed=False, failed=True)
        self.assertIn(
            "The Backup Config file with File ID:",
            result.get("msg"),
        )
