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

from ansible_collections.cisco.dnac.plugins.modules import backup_and_restore_workflow_manager
from .dnac_module import TestDnacModule, set_module_args, loadPlaybookData


class TestDnacApplicationPolicyWorkflowManager(TestDnacModule):

    module = backup_and_restore_workflow_manager
    test_data = loadPlaybookData("backup_and_restore_workflow_manager")

    playbook_create_schedule_backup = test_data.get("playbook_create_schedule_backup")
    playbook_nfs_config_alreadyexists = test_data.get("playbook_nfs_config_alreadyexists")
    playbook_nfs_config_delete = test_data.get("playbook_nfs_config_delete")
    playbook_create_nfs_config = test_data.get("playbook_create_nfs_config")
    playbook_backup_configuration_exception_dataretention_period = test_data.get("playbook_backup_configuration_exception_dataretention_period")
    playbook_negative_scenario1 = test_data.get("playbook_negative_scenario1")
    playbook_negative_scenario2 = test_data.get("playbook_negative_scenario2")
    playbook_negative_scenario3 = test_data.get("playbook_negative_scenario3")
    playbook_negative_scenario4 = test_data.get("playbook_negative_scenario4")
    playbook_negative_scenario6 = test_data.get("playbook_negative_scenario6")
    playbook_negative_scenario8 = test_data.get("playbook_negative_scenario8")
    playbook_negative_scenario9 = test_data.get("playbook_negative_scenario9")
    playbook_negative_scenario10 = test_data.get("playbook_negative_scenario10")
    playbook_negative_scenario12 = test_data.get("playbook_negative_scenario12")
    playbook_negative_scenario13 = test_data.get("playbook_negative_scenario13")
    playbook_negative_scenario14 = test_data.get("playbook_negative_scenario14")
    playbook_update_backup_config = test_data.get("playbook_update_backup_config")
    playbook_backup_config_alreadyexists1 = test_data.get("playbook_backup_config_alreadyexists1")
    playbook_backup_config_password_exception = test_data.get("playbook_backup_config_password_exception")
    playbook_mountpath_notfound = test_data.get("playbook_mountpath_notfound")
    playbook_restore_exception = test_data.get("playbook_restore_exception")
    playbook_backup_schedule_alreadydeleted1 = test_data.get("playbook_backup_schedule_alreadydeleted1")
    playbook_delete_backup_schedule = test_data.get("playbook_delete_backup_schedule")
    playbook_backup_schedule_alreadyexists = test_data.get("playbook_backup_schedule_alreadyexists")

    def setUp(self):
        super(TestDnacApplicationPolicyWorkflowManager, self).setUp()

        self.mock_dnac_init = patch(
            "ansible_collections.cisco.dnac.plugins.module_utils.dnac.DNACSDK.__init__")
        self.run_dnac_init = self.mock_dnac_init.start()
        self.run_dnac_init.side_effect = [None]
        self.mock_dnac_exec = patch(
            "ansible_collections.cisco.dnac.plugins.module_utils.dnac.DNACSDK._exec"
        )
        self.run_dnac_exec = self.mock_dnac_exec.start()

    def tearDown(self):
        super(TestDnacApplicationPolicyWorkflowManager, self).tearDown()
        self.mock_dnac_exec.stop()
        self.mock_dnac_init.stop()

    def load_fixtures(self, response=None, device=""):
        """
        Load fixtures for user.
        """
        if "playbook_create_schedule_backup" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("get_all_backup2"),
                self.test_data.get("create_backup1"),
                self.test_data.get("get_backup_and_restore_execution4"),
                self.test_data.get("get_backup_and_restore_execution5"),
                self.test_data.get("get_all_backup3"),
            ]

        elif "playbook_nfs_config_alreadyexists" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("get_all_n_f_s_configurations1"),
                self.test_data.get("get_all_n_f_s_configurations2"),
            ]

        elif "playbook_nfs_config_delete" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("get_all_n_f_s_configurations3"),
                self.test_data.get("get_all_n_f_s_configurations2"),
            ]

        elif "playbook_create_nfs_config" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("get_all_n_f_s_configurations8"),
                self.test_data.get("create_n_f_s_configuration"),
                self.test_data.get("get_all_n_f_s_configurations9"),
            ]

        elif "playbook_backup_configuration_exception_dataretention_period" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("get_backup_configuration5"),
                self.test_data.get("get_all_n_f_s_configurations7"),
            ]

        elif "playbook_negative_scenario1" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("get_all_backup6"),
            ]

        elif "playbook_negative_scenario3" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("get_all_backup7"),
            ]

        elif "playbook_negative_scenario4" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("get_all_n_f_s_configurations"),
            ]

        elif "playbook_negative_scenario8" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("get_all_backup8"),
            ]

        elif "playbook_negative_scenario9" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("get_all_n_f_s_configurations6"),
            ]

        elif "playbook_update_backup_config" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("get_all_n_f_s_configurations10"),
                self.test_data.get("get_backup_configuration"),
                self.test_data.get("get_all_n_f_s_configurations11"),
                self.test_data.get("create_backup_configuration"),
                self.test_data.get("get_all_n_f_s_configurations12"),
                self.test_data.get("get_backup_configuration7"),
            ]

        elif "playbook_backup_config_alreadyexists1" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("get_all_n_f_s_configurations13"),
                self.test_data.get("get_backup_configuration8"),
                self.test_data.get("get_all_n_f_s_configurations14"),
                self.test_data.get("get_all_n_f_s_configurations15"),
                self.test_data.get("get_backup_configuration9"),
            ]

        elif "playbook_backup_config_password_exception" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("get_all_n_f_s_configurations16"),
                self.test_data.get("get_backup_configuration10"),
                self.test_data.get("get_all_n_f_s_configurations17"),
            ]

        elif "playbook_mountpath_notfound" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("get_all_n_f_s_configurations18"),
                self.test_data.get("get_backup_configuration11"),
                self.test_data.get("get_all_n_f_s_configurations19"),
            ]

        elif "playbook_restore_exception" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("get_all_n_f_s_configurations21"),
                self.test_data.get("get_all_backup"),
            ]

        elif "playbook_backup_schedule_alreadydeleted1" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("get_all_n_f_s_configurations24"),
                self.test_data.get("get_all_backup12"),
                self.test_data.get("get_all_n_f_s_configurations25"),
                self.test_data.get("get_all_backup13"),
            ]

        elif "playbook_delete_backup_schedule" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("get_all_n_f_s_configurations26"),
                self.test_data.get("get_all_backup14"),
                self.test_data.get("delete_backup"),
                self.test_data.get("get_backup_and_restore_execution"),
                self.test_data.get("get_backup_and_restore_execution1"),
                self.test_data.get("get_all_n_f_s_configurations27"),
                self.test_data.get("get_all_backup15"),
            ]

        elif "playbook_backup_schedule_alreadyexists" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("get_all_n_f_s_configurations28"),
                self.test_data.get("get_all_backup16"),
                self.test_data.get("get_all_n_f_s_configurations29"),
                self.test_data.get("get_all_backup17"),
            ]

    def test_backup_and_restore_workflow_manager_playbook_create_schedule_backup(self):
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
                state="merged",
                config_verify=True,
                dnac_version="3.1.3.0",
                config=self.playbook_create_schedule_backup
            )
        )
        result = self.execute_module(changed=True, failed=False)
        print(result)
        self.assertEqual(
            result.get("response"),
            "Backup(s) 'BACKUP24_07' created successfully in Cisco Catalyst Center."
        )

    def test_backup_and_restore_workflow_manager_playbook_nfs_config_alreadyexists(self):
        """
        Test case for handling an already existing NFS configuration in Cisco Catalyst Center.
        Verifies that the workflow manager does not reconfigure NFS and correctly
        returns a message indicating that the configuration already exists.
        """
        set_module_args(
            dict(
                dnac_host="1.1.1.1",
                dnac_username="dummy",
                dnac_password="dummy",
                dnac_log=True,
                state="merged",
                config_verify=True,
                dnac_version="3.1.3.0",
                config=self.playbook_nfs_config_alreadyexists
            )
        )
        result = self.execute_module(changed=False, failed=False)
        print(result)
        self.assertEqual(
            result.get("response"),
            "NFS Configuration(s) '/home/nfsshare/backups/TB19' already exist in Cisco Catalyst Center."
        )

    def test_backup_and_restore_workflow_manager_playbook_nfs_config_delete(self):
        """
        Test case for deleting an existing NFS configuration in Cisco Catalyst Center.
        Verifies that the workflow manager correctly removes the specified configuration
        and returns the expected success message upon deletion.
        """
        set_module_args(
            dict(
                dnac_host="1.1.1.1",
                dnac_username="dummy",
                dnac_password="dummy",
                dnac_log=True,
                state="deleted",
                config_verify=True,
                dnac_version="3.1.3.0",
                config=self.playbook_nfs_config_delete
            )
        )
        result = self.execute_module(changed=True, failed=False)
        print(result)
        self.assertEqual(
            result.get("response"),
            "NFS Configuration(s) '/home/nfsshare/backups/TB19' deleted successfully from Cisco Catalyst Center."
        )

    def test_backup_and_restore_workflow_manager_playbook_create_nfs_config(self):
        """
        Test case for creating an NFS configuration in Cisco Catalyst Center.
        Verifies that the workflow manager successfully creates the NFS configuration
        when the specified parameters are applied.
        """
        set_module_args(
            dict(
                dnac_host="1.1.1.1",
                dnac_username="dummy",
                dnac_password="dummy",
                dnac_log=True,
                state="merged",
                config_verify=True,
                dnac_version="3.1.3.0",
                config=self.playbook_create_nfs_config
            )
        )
        result = self.execute_module(changed=True, failed=False)
        print(result)
        self.assertEqual(
            result.get("response"),
            "NFS Configuration(s) '/home/nfsshare/backups/TB22' created successfully in Cisco Catalyst Center."
        )

    def test_backup_and_restore_workflow_manager_playbook_backup_configuration_exception_dataretention_period(self):
        """
        Test case for handling invalid data retention period in backup configuration.
        Verifies that the workflow manager raises an error when the retention period
        exceeds the allowed maximum.
        """
        set_module_args(
            dict(
                dnac_host="1.1.1.1",
                dnac_username="dummy",
                dnac_password="dummy",
                dnac_log=True,
                state="merged",
                config_verify=True,
                dnac_version="3.1.3.0",
                config=self.playbook_backup_configuration_exception_dataretention_period
            )
        )
        result = self.execute_module(changed=False, failed=True)
        print(result)
        self.assertEqual(
            result.get("response"),
            "Configuration validation failed with invalid parameters: ['data_retention_period: 61 : The item exceeds the allowed range of min: 3 and max: 60']"
        )

    def test_backup_and_restore_workflow_manager_playbook_negative_scenario1(self):
        """
        Negative test case for missing required fields in backup schedule.
        Verifies that the workflow manager raises an error when 'name' and 'scope'
        are not provided.
        """
        set_module_args(
            dict(
                dnac_host="1.1.1.1",
                dnac_username="dummy",
                dnac_password="dummy",
                dnac_log=True,
                state="merged",
                config_verify=True,
                dnac_version="3.1.3.0",
                config=self.playbook_negative_scenario1
            )
        )
        result = self.execute_module(changed=False, failed=True)
        print(result)
        self.assertEqual(
            result.get("response"),
            "Mandatory fields 'name', 'scope' must be specified for backups."
        )

    def test_backup_and_restore_workflow_manager_playbook_negative_scenario2(self):
        """
        Negative test case for unsupported Cisco Catalyst Center version.
        Verifies that the workflow manager raises an error when the version does not
        support the Backup and Restore feature.
        """
        set_module_args(
            dict(
                dnac_host="1.1.1.1",
                dnac_username="dummy",
                dnac_password="dummy",
                dnac_log=True,
                state="merged",
                config_verify=True,
                dnac_version="2.3.7.6",
                config=self.playbook_negative_scenario2
            )
        )
        result = self.execute_module(changed=False, failed=True)
        print(result)
        self.assertEqual(
            result.get("msg"),
            "The specified version '2.3.7.6' does not support the 'Backup and restore' feature. Supported version(s) start from '3.1.3.0' onwards."
        )

    def test_backup_and_restore_workflow_manager_playbook_negative_scenario3(self):
        """
        Negative test case for restoring a non-existent backup.
        Verifies that the workflow manager raises an error when the specified backup
        name does not exist in Cisco Catalyst Center.
        """
        set_module_args(
            dict(
                dnac_host="1.1.1.1",
                dnac_username="dummy",
                dnac_password="dummy",
                dnac_log=True,
                state="merged",
                config_verify=True,
                dnac_version="3.1.3.0",
                config=self.playbook_negative_scenario3
            )
        )
        result = self.execute_module(changed=False, failed=True)
        print(result)
        self.assertEqual(
            result.get("response"),
            "No backup found with the name 'BACKUP25_07'."
        )

    def test_backup_and_restore_workflow_manager_playbook_negative_scenario4(self):
        """
        Negative test case for missing fields in NFS configuration.
        Verifies that the workflow manager raises an error when 'server_ip' or
        'source_path' is not specified.
        """
        set_module_args(
            dict(
                dnac_host="1.1.1.1",
                dnac_username="dummy",
                dnac_password="dummy",
                dnac_log=True,
                state="merged",
                config_verify=True,
                dnac_version="3.1.3.0",
                config=self.playbook_negative_scenario4
            )
        )
        result = self.execute_module(changed=False, failed=True)
        print(result)
        self.assertEqual(
            result.get("response"),
            "Configuration validation failed with invalid parameters: ['source_path : Required parameter not found']"
        )

    def test_backup_and_restore_workflow_manager_playbook_negative_scenario6(self):
        """
        Negative test case for missing fields in restore configuration.
        Verifies that the workflow manager raises an error when 'name' or
        'encryption_passphrase' is not specified for restore.
        """
        set_module_args(
            dict(
                dnac_host="1.1.1.1",
                dnac_username="dummy",
                dnac_password="dummy",
                dnac_log=True,
                state="merged",
                config_verify=True,
                dnac_version="3.1.3.0",
                config=self.playbook_negative_scenario6
            )
        )
        result = self.execute_module(changed=False, failed=True)
        print(result)
        self.assertEqual(
            result.get("response"),
            "Configuration validation failed with invalid parameters: ['encryption_passphrase : Required parameter not found']"
        )

    def test_backup_and_restore_workflow_manager_playbook_negative_scenario8(self):
        """
        Negative test case for deleting a backup schedule without specifying 'name'.
        Verifies that the workflow manager raises an error when 'name' is missing
        in the delete request.
        """
        set_module_args(
            dict(
                dnac_host="1.1.1.1",
                dnac_username="dummy",
                dnac_password="dummy",
                dnac_log=True,
                state="deleted",
                config_verify=True,
                dnac_version="3.1.3.0",
                config=self.playbook_negative_scenario8
            )
        )
        result = self.execute_module(changed=False, failed=True)
        print(result)
        self.assertEqual(
            result.get("response"),
            "Configuration validation failed with invalid parameters: ['name : Required parameter not found']"
        )

    def test_backup_and_restore_workflow_manager_playbook_negative_scenario9(self):
        """
        Negative test case for deleting an NFS configuration without required fields.
        Verifies that the workflow manager raises an error when 'server_ip' or
        'source_path' is missing in the delete request.
        """
        set_module_args(
            dict(
                dnac_host="1.1.1.1",
                dnac_username="dummy",
                dnac_password="dummy",
                dnac_log=True,
                state="deleted",
                config_verify=True,
                dnac_version="3.1.3.0",
                config=self.playbook_negative_scenario9
            )
        )
        result = self.execute_module(changed=False, failed=True)
        print(result)
        self.assertEqual(
            result.get("response"),
            "Configuration validation failed with invalid parameters: ['source_path : Required parameter not found']"
        )

    def test_backup_and_restore_workflow_manager_playbook_negative_scenario10(self):
        """
        Negative test case for invalid backup name format.
        Verifies that the workflow manager raises an error when the backup name does
        not meet the required naming rules.
        """
        set_module_args(
            dict(
                dnac_host="1.1.1.1",
                dnac_username="dummy",
                dnac_password="dummy",
                dnac_log=True,
                state="merged",
                config_verify=True,
                dnac_version="3.1.3.0",
                config=self.playbook_negative_scenario10
            )
        )
        result = self.execute_module(changed=False, failed=True)
        print(result)
        self.assertEqual(
            result.get("response"),
            "Backup name must begin with an alphabet and can contain letters, digits, and the following special characters: @, #, _, -, and space."
        )

    def test_backup_and_restore_workflow_manager_playbook_negative_scenario12(self):
        """
        Negative test case for missing configuration in playbook.
        Verifies that the workflow manager raises an error when none of
        'backup_configuration', 'nfs_configuration', 'backup_schedule',
        or 'restore_details' is provided.
        """

        set_module_args(
            dict(
                dnac_host="1.1.1.1",
                dnac_username="dummy",
                dnac_password="dummy",
                dnac_log=True,
                state="merged",
                config_verify=True,
                dnac_version="3.1.3.0",
                config=self.playbook_negative_scenario12
            )
        )
        result = self.execute_module(changed=False, failed=True)
        print(result)
        self.assertEqual(
            result.get("response"),
            "Backup and restore workflow requires at least one configuration section: "
            "'backup_storage_configuration', 'nfs_configuration', 'backup_job_creation', or 'restore_operations'"
        )

    def test_backup_and_restore_workflow_manager_playbook_negative_scenario13(self):
        """
        Negative test case for invalid parameter type in backup configuration.
        Verifies that the workflow manager raises an error when a dict is provided
        instead of the expected list.
        """
        set_module_args(
            dict(
                dnac_host="1.1.1.1",
                dnac_username="dummy",
                dnac_password="dummy",
                dnac_log=True,
                state="merged",
                config_verify=True,
                dnac_version="3.1.3.0",
                config=self.playbook_negative_scenario13
            )
        )
        result = self.execute_module(changed=False, failed=True)

        print(result)
        self.maxDiff = None
        self.assertEqual(
            result.get("response"),
            'Configuration validation failed with invalid parameters: '
            '["\'backup_storage_configuration\': \'{\'data_retention_period\': 53, \'encryption_passphrase\': '
            '\'Karthick@zigzag333\', \'nfs_details\': {\'nfs_port\': 2049, \'nfs_portmapper_port\': 111, '
            '\'nfs_version\': \'nfs4\', \'server_ip\': \'172.27.17.90\', \'source_path\': '
            '\'/home/nfsshare/backups/TB19\'}, \'server_type\': \'NFS\'}\' is invalid. '
            'Reason: expected type: \'list\'. Provided type: \'dict\'. "]'
        )

    def test_backup_and_restore_workflow_manager_playbook_update_backup_config(self):
        """
        Test case for updating backup configuration in Cisco Catalyst Center.
        Verifies that the workflow manager correctly updates the configuration
        when the specified parameters are applied.
        """
        set_module_args(
            dict(
                dnac_host="1.1.1.1",
                dnac_username="dummy",
                dnac_password="dummy",
                dnac_log=True,
                state="merged",
                config_verify=True,
                dnac_version="3.1.3.0",
                config=self.playbook_update_backup_config
            )
        )
        result = self.execute_module(changed=True, failed=False)

        print(result)
        self.assertEqual(
            result.get("response"),
            "Backup Configuration(s) '/home/nfsshare/backups/TB18' updated successfully in Cisco Catalyst Center."
        )

    def test_backup_and_restore_workflow_manager_playbook_backup_config_alreadyexists1(self):
        """
        Test case for handling already existing backup configuration.
        Verifies that the workflow manager detects existing configurations and
        avoids reconfiguring them unnecessarily.
        """
        set_module_args(
            dict(
                dnac_host="1.1.1.1",
                dnac_username="dummy",
                dnac_password="dummy",
                dnac_log=True,
                state="merged",
                config_verify=True,
                dnac_version="3.1.3.0",
                config=self.playbook_backup_config_alreadyexists1
            )
        )
        result = self.execute_module(changed=False, failed=False)

        print(result)
        self.assertEqual(
            result.get("response"),
            "Backup Configuration(s) '/home/nfsshare/backups/TB17' already exist in Cisco Catalyst Center."
        )

    def test_backup_and_restore_workflow_manager_playbook_backup_config_password_exception(self):
        """
        Negative test case for backup configuration update failure due to password issue.
        Verifies that the workflow manager raises an error when updating backup
        configuration fails because of an invalid or missing encryption passphrase.
        """
        set_module_args(
            dict(
                dnac_host="1.1.1.1",
                dnac_username="dummy",
                dnac_password="dummy",
                dnac_log=True,
                state="merged",
                config_verify=True,
                dnac_version="3.1.3.0",
                config=self.playbook_backup_config_password_exception
            )
        )
        result = self.execute_module(changed=False, failed=True)
        print(result)
        self.assertEqual(
            result.get("response"),
            "An error occurred while updating backup configuration: "
        )

    def test_backup_and_restore_workflow_manager_playbook_mountpath_notfound(self):
        """
        Negative test case for NFS mount path retrieval failure.
        Verifies that the workflow manager raises an error when the NFS node is unhealthy
        and the mount path cannot be retrieved.
        """
        set_module_args(
            dict(
                dnac_host="1.1.1.1",
                dnac_username="dummy",
                dnac_password="dummy",
                dnac_log=True,
                state="merged",
                config_verify=True,
                dnac_version="3.1.3.0",
                config=self.playbook_mountpath_notfound
            )
        )
        result = self.execute_module(changed=False, failed=True)
        print(result)
        self.assertEqual(
            result.get("response"),
            "Mount path not retrievable as NFS node is unhealthy for server IP '172.27.17.90', source path '/home/nfsshare/backups/TB22'."
        )

    def test_backup_and_restore_workflow_manager_playbook_negative_scenario14(self):
        """
        Negative test case for missing restore parameters.
        Verifies that the workflow manager raises an error when both 'name' and
        'encryption_passphrase' are not specified for restore.
        """
        set_module_args(
            dict(
                dnac_host="1.1.1.1",
                dnac_username="dummy",
                dnac_password="dummy",
                dnac_log=True,
                state="merged",
                config_verify=True,
                dnac_version="3.1.3.0",
                config=self.playbook_negative_scenario14
            )
        )
        result = self.execute_module(changed=False, failed=True)
        print(result)
        self.assertEqual(
            result.get("response"),
            "Configuration validation failed with invalid parameters: "
            "['name : Required parameter not found', "
            "'encryption_passphrase : Required parameter not found']"
        )

    def test_backup_and_restore_workflow_manager_playbook_restore_exception(self):
        """
        Negative test case for restore operation failure.
        Verifies that the workflow manager raises an error when restoring a backup
        fails unexpectedly.
        """
        set_module_args(
            dict(
                dnac_host="1.1.1.1",
                dnac_username="dummy",
                dnac_password="dummy",
                dnac_log=True,
                state="merged",
                config_verify=True,
                dnac_version="3.1.3.0",
                config=self.playbook_restore_exception
            )
        )
        result = self.execute_module(changed=False, failed=True)
        print(result)
        self.assertEqual(
            result.get("response"),
            "An error occurred while restoring backup: "
        )

    def test_backup_and_restore_workflow_manager_playbook_backup_schedule_alreadydeleted1(self):
        """
        Test case for handling already deleted backup schedule.
        Verifies that the workflow manager correctly identifies that a backup schedule
        is not present and confirms deletion.
        """
        set_module_args(
            dict(
                dnac_host="1.1.1.1",
                dnac_username="dummy",
                dnac_password="dummy",
                dnac_log=True,
                state="deleted",
                config_verify=True,
                dnac_version="3.1.3.0",
                config=self.playbook_backup_schedule_alreadydeleted1
            )
        )
        result = self.execute_module(changed=False, failed=False)
        print(result)
        self.assertEqual(
            result.get("response"),
            "Backups with name 'BACKUP25_07' does not exist in the Cisco Catalyst Center or has already been deleted."
        )

    def test_backup_and_restore_workflow_manager_playbook_delete_backup_schedule(self):
        """
        Test case for deleting a backup schedule in Cisco Catalyst Center.
        Verifies that the workflow manager successfully deletes the backup schedule
        when the specified configuration is applied.
        """
        set_module_args(
            dict(
                dnac_host="1.1.1.1",
                dnac_username="dummy",
                dnac_password="dummy",
                dnac_log=True,
                state="deleted",
                config_verify=True,
                dnac_version="3.1.3.0",
                config=self.playbook_delete_backup_schedule
            )
        )
        result = self.execute_module(changed=True, failed=False)
        print(result)
        self.assertEqual(
            result.get("response"),
            "Backup(s) 'BACKUP24_07' deleted successfully from Cisco Catalyst Center."
        )

    def test_backup_and_restore_workflow_manager_playbook_backup_schedule_alreadyexists(self):
        """
        Test case for handling already existing backup schedule.
        Verifies that the workflow manager correctly identifies the presence of an
        existing backup schedule and confirms that no changes are needed.
        """
        set_module_args(
            dict(
                dnac_host="1.1.1.1",
                dnac_username="dummy",
                dnac_password="dummy",
                dnac_log=True,
                state="merged",
                config_verify=True,
                dnac_version="3.1.3.0",
                config=self.playbook_backup_schedule_alreadyexists
            )
        )
        result = self.execute_module(changed=False, failed=False)
        print(result)
        self.assertEqual(
            result.get("response"),
            "Backup 'BACKUP24_07' already exists."
        )
