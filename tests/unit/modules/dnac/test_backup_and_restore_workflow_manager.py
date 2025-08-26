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
    playbook_nfs_delete = test_data.get("playbook_nfs_delete")
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
            "Backup Schedule(s) 'BACKUP24_07' created/scheduled successfully in Cisco Catalyst Center."
        )

    def test_backup_and_restore_workflow_manager_playbook_nfs_config_alreadyexists(self):
        """
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
            "Invalid parameters in playbook: ['data_retention_period: 61 : The item exceeds the allowed range of min: 3 and max: 60']"
        )

    def test_backup_and_restore_workflow_manager_playbook_negative_scenario1(self):
        """
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
            "Mandatory fields 'name', 'scope' must be specified for backup schedule."
        )

    def test_backup_and_restore_workflow_manager_playbook_negative_scenario2(self):
        """
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
            "Both 'server_ip' and 'source_path' must be specified to create an NFS configuration."
        )

    def test_backup_and_restore_workflow_manager_playbook_negative_scenario6(self):
        """
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
            "Both 'name' and 'encryption_passphrase' must be specified for restore."
        )

    def test_backup_and_restore_workflow_manager_playbook_negative_scenario8(self):
        """
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
            "'name' must be specified to delete a backup schedule."
        )

    def test_backup_and_restore_workflow_manager_playbook_negative_scenario9(self):
        """
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
            "Both 'server_ip' and 'source_path' must be specified to delete an NFS configuration."
        )

    def test_backup_and_restore_workflow_manager_playbook_negative_scenario10(self):
        """
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
            "At least one of 'backup_configuration', 'nfs_configuration', 'backup_schedule', or 'restore_details' must be specified."
        )

    def test_backup_and_restore_workflow_manager_playbook_negative_scenario13(self):
        """
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
        self.assertEqual(
            result.get("response"),
            '''Invalid parameters in playbook: ["\'backup_configuration\': \'{\'data_retention_period\': 53, \'encryption_passphrase\': \'Karthick@zigzag333\', \'nfs_details\': {\'nfs_port\': 2049, \'nfs_port_mapper\': 111, \'nfs_version\': \'nfs4\', \'server_ip\': \'172.27.17.90\', \'source_path\': \'/home/nfsshare/backups/TB19\'}, \'server_type\': \'NFS\'}\' is invalid. Reason: expected type: \'list\'. Provided type: \'dict\'. "]'''        
        )
    
    def test_backup_and_restore_workflow_manager_playbook_update_backup_config(self):
        """
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
            "Both 'name' and 'encryption_passphrase' must be specified for restore."
        )

    def test_backup_and_restore_workflow_manager_playbook_restore_exception(self):
        """
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

    def test_backup_and_restore_workflow_manager_playbook_nfs_delete(self):
        """
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
                config=self.playbook_nfs_delete
            )
        )
        result = self.execute_module(changed=True, failed=False)
        print(result)
        self.assertEqual(
            result.get("response"),
            "NFS Configuration(s) '/home/nfsshare/backups/TB22' deleted successfully from Cisco Catalyst Center."
        )

    def test_backup_and_restore_workflow_manager_playbook_backup_schedule_alreadydeleted1(self):
        """
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
            "The backup schedule 'BACKUP25_07' is not present in Cisco Catalyst Center and its deletion has been verified."
        )

    def test_backup_and_restore_workflow_manager_playbook_delete_backup_schedule(self):
        """
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
            "Backup Schedule(s) 'BACKUP24_07' deleted successfully from Cisco Catalyst Center."
        )

    def test_backup_and_restore_workflow_manager_playbook_backup_schedule_alreadyexists(self):
        """
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
            "The requested backup schedule with name 'BACKUP24_07' and scope 'CISCO_DNA_DATA_WITHOUT_ASSURANCE' is present in the Cisco Catalyst Center and its creation has been verified."
        )


    