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

from unittest.mock import patch

from ansible_collections.cisco.dnac.plugins.modules import backup_and_restore_playbook_config_generator
from .dnac_module import TestDnacModule, set_module_args, loadPlaybookData


class TestDnacBackupRestorePlaybookGenerator(TestDnacModule):

    module = backup_and_restore_playbook_config_generator
    test_data = loadPlaybookData("backup_and_restore_playbook_config_generator")

    playbook_nfs_configuration_details = test_data.get("playbook_nfs_configuration_details")
    playbook_backup_configuration_details = test_data.get("playbook_backup_configuration_details")
    playbook_specific_nfs_backup_configuration_details = test_data.get("playbook_specific_nfs_backup_configuration_details")
    playbook_generate_all_configuration = test_data.get("playbook_generate_all_configuration")
    playbook_negative_scenario_lower_version = test_data.get("playbook_negative_scenario_lower_version")
    playbook_negative_scenario2 = test_data.get("playbook_negative_scenario2")

    def setUp(self):
        super(TestDnacBackupRestorePlaybookGenerator, self).setUp()

        self.mock_dnac_init = patch(
            "ansible_collections.cisco.dnac.plugins.module_utils.dnac.DNACSDK.__init__")
        self.run_dnac_init = self.mock_dnac_init.start()
        self.run_dnac_init.side_effect = [None]
        self.mock_dnac_exec = patch(
            "ansible_collections.cisco.dnac.plugins.module_utils.dnac.DNACSDK._exec"
        )
        self.run_dnac_exec = self.mock_dnac_exec.start()

    def tearDown(self):
        super(TestDnacBackupRestorePlaybookGenerator, self).tearDown()
        self.mock_dnac_exec.stop()
        self.mock_dnac_init.stop()

    def load_fixtures(self, response=None, device=""):
        """
        Load fixtures for user.
        """
        if "playbook_nfs_configuration_details" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("nfs_server_details")
            ]

        elif "playbook_backup_configuration_details" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("get_backup_configuration_details"),
                self.test_data.get("get_nfs_server_details")
            ]

        elif "playbook_specific_nfs_backup_configuration_details" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("get_nfs_server_details1"),
                self.test_data.get("get_backup_configuration_details1")
            ]

        elif "playbook_generate_all_configuration" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("get_nfs_details"),
                self.test_data.get("get_backup_configuration_details2"),
                self.test_data.get("get_all_n_f_s_configurations")
            ]

        elif "playbook_negative_scenario_lower_version" in self._testMethodName:
            pass

        elif "playbook_negative_scenario2" in self._testMethodName:
            pass

    def test_backup_and_restore_playbook_config_generator_playbook_nfs_configuration_details(self):
        """
        Test case for creating a scheduled backup in Cisco Catalyst Center.
        Verifies that the workflow manager correctly creates and schedules
        a backup when the specified configuration is applied.
        """

        set_module_args(
            dict(
                dnac_host="1.1.1.1",
                dnac_username="dummy",
                dnac_password="dummy",
                dnac_log=True,
                state="gathered",
                dnac_version="3.1.3.0",
                config=self.playbook_nfs_configuration_details
            )
        )
        result = self.execute_module(changed=True, failed=False)
        print(result)
        self.assertEqual(
            result.get("response"),
            {
                "components_processed": 1,
                "components_skipped": 0,
                "configurations_count": 6,
                "file_path": "/Users/priyadharshini/Downloads/configuration_details_info",
                "message": "YAML configuration file generated successfully for module 'backup_and_restore_workflow_manager'",
                "status": "success"
            }
        )

    def test_backup_and_restore_playbook_config_generator_playbook_backup_configuration_details(self):
        """
        Test case for creating a scheduled backup in Cisco Catalyst Center.
        Verifies that the workflow manager correctly creates and schedules
        a backup when the specified configuration is applied.
        """

        set_module_args(
            dict(
                dnac_host="1.1.1.1",
                dnac_username="dummy",
                dnac_password="dummy",
                dnac_log=True,
                state="gathered",
                dnac_version="3.1.3.0",
                config=self.playbook_backup_configuration_details
            )
        )
        result = self.execute_module(changed=True, failed=False)
        print(result)
        self.assertEqual(
            result.get("response"),
            {
                "components_processed": 1,
                "components_skipped": 0,
                "configurations_count": 1,
                "file_path": "/Users/priyadharshini/Downloads/configuration_details_info",
                "message": "YAML configuration file generated successfully for module 'backup_and_restore_workflow_manager'",
                "status": "success"
            }
        )

    def test_backup_and_restore_playbook_config_generator_playbook_specific_nfs_backup_configuration_details(self):
        """
        Test case for creating a scheduled backup in Cisco Catalyst Center.
        Verifies that the workflow manager correctly creates and schedules
        a backup when the specified configuration is applied.
        """

        set_module_args(
            dict(
                dnac_host="1.1.1.1",
                dnac_username="dummy",
                dnac_password="dummy",
                dnac_log=True,
                state="gathered",
                dnac_version="3.1.3.0",
                config=self.playbook_specific_nfs_backup_configuration_details
            )
        )
        result = self.execute_module(changed=True, failed=False)
        print(result)
        self.assertEqual(
            result.get("response"),
            {
                "components_processed": 2,
                "components_skipped": 0,
                "configurations_count": 2,
                "file_path": "/Users/priyadharshini/Downloads/configuration_details_info",
                "message": "YAML configuration file generated successfully for module 'backup_and_restore_workflow_manager'",
                "status": "success"
            }
        )

    def test_backup_and_restore_playbook_config_generator_playbook_generate_all_configuration(self):
        """
        Test case for creating a scheduled backup in Cisco Catalyst Center.
        Verifies that the workflow manager correctly creates and schedules
        a backup when the specified configuration is applied.
        """

        set_module_args(
            dict(
                dnac_host="1.1.1.1",
                dnac_username="dummy",
                dnac_password="dummy",
                dnac_log=True,
                state="gathered",
                dnac_version="3.1.3.0",
                config=self.playbook_generate_all_configuration
            )
        )
        result = self.execute_module(changed=True, failed=False)
        print(result)
        self.assertEqual(
            result.get("response"),
            {
                "components_processed": 2,
                "components_skipped": 0,
                "configurations_count": 7,
                "file_path": "/Users/priyadharshini/Downloads/configuration_details_info1",
                "message": "YAML configuration file generated successfully for module 'backup_and_restore_workflow_manager'",
                "status": "success"
            }
        )

    def test_backup_and_restore_playbook_config_generator_playbook_negative_scenario_lower_version(self):
        """
        Test case for creating a scheduled backup in Cisco Catalyst Center.
        Verifies that the workflow manager correctly creates and schedules
        a backup when the specified configuration is applied.
        """

        set_module_args(
            dict(
                dnac_host="1.1.1.1",
                dnac_username="dummy",
                dnac_password="dummy",
                dnac_log=True,
                state="gathered",
                dnac_version="2.3.7.9",
                config=self.playbook_negative_scenario_lower_version
            )
        )
        result = self.execute_module(changed=False, failed=True)
        print(result)
        self.assertEqual(
            result.get("response"),
            "The specified version '2.3.7.9' does not support the YAML Playbook generation for "
            "Backup and Restore Management Module. Supported versions start from '3.1.3.0' "
            "onwards. Version '3.1.3.0' introduces APIs for retrieving backup and restore "
            "settings from the Catalyst Center"
        )

    def test_backup_and_restore_playbook_config_generator_playbook_negative_scenario2(self):
        """
        Test case for creating a scheduled backup in Cisco Catalyst Center.
        Verifies that the workflow manager correctly creates and schedules
        a backup when the specified configuration is applied.
        """

        set_module_args(
            dict(
                dnac_host="1.1.1.1",
                dnac_username="dummy",
                dnac_password="dummy",
                dnac_log=True,
                state="gathered",
                dnac_version="3.1.3.0",
                config=self.playbook_negative_scenario2
            )
        )
        result = self.execute_module(changed=False, failed=True)
        print(result)
        self.assertEqual(
            result.get("response"),
            "Invalid network components provided for module "
            "'backup_and_restore_workflow_manager': ['nfs_configurations']. "
            "Valid components are: ['nfs_configuration', 'backup_storage_configuration']"
        )
