# Copyright (c) 2024 Cisco and/or its affiliates.
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
from ansible_collections.cisco.dnac.plugins.modules import device_credential_workflow_manager
from .dnac_module import TestDnacModule, set_module_args, loadPlaybookData


class TestDnacCredentialWorkflow(TestDnacModule):

    module = device_credential_workflow_manager
    test_data = loadPlaybookData("device_credential_workflow_manager")
    playbook_config_creation = test_data.get("playbook_config_creation")
    playbook_config_deletion = test_data.get("playbook_config_deletion")
    playbook_config_assign = test_data.get("playbook_config_assign")
    playbook_config_apply = test_data.get("playbook_config_apply")
    playbook_invalid_cli = test_data.get("playbook_invalid_cli")

    def setUp(self):
        super(TestDnacCredentialWorkflow, self).setUp()

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
        super(TestDnacCredentialWorkflow, self).tearDown()
        self.mock_dnac_exec.stop()
        self.mock_dnac_init.stop()

    def load_fixtures(self, response=None, device=""):
        """
        Load fixtures for user.
        """
        if "creation" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("creation_task_details"),
                self.test_data.get("create_task_response_1"),
                self.test_data.get("create_task_response_2"),
                self.test_data.get("create_task_response_1"),
                self.test_data.get("create_task_response_2"),
                self.test_data.get("create_task_response_1"),
                self.test_data.get("create_task_response_2"),
                self.test_data.get("create_task_response_1"),
                self.test_data.get("create_task_response_2"),
                self.test_data.get("create_task_response_1"),
                self.test_data.get("create_task_response_2"),
                self.test_data.get("create_task_response_1"),
                self.test_data.get("create_task_response_2"),
            ]

        if "deletion" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("global_credentials"),
                self.test_data.get("deletion_task_detail"),
                self.test_data.get("deletion_task_response"),
                self.test_data.get("deletion_task_detail"),
                self.test_data.get("deletion_task_response"),
                self.test_data.get("deletion_task_detail"),
                self.test_data.get("deletion_task_response"),
                self.test_data.get("deletion_task_detail"),
                self.test_data.get("deletion_task_response"),
                self.test_data.get("deletion_task_detail"),
                self.test_data.get("deletion_task_response"),
                self.test_data.get("deletion_task_detail"),
                self.test_data.get("deletion_task_response"),
                self.test_data.get("deletion_task_response"),
                self.test_data.get("deletion_task_response"),
            ]

        if "assign_cred_1" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("get_site_1"),
                self.test_data.get("get_site_2"),
                self.test_data.get("global_assign_cred"),
                self.test_data.get("assign_task_details"),
                self.test_data.get("assign_task_response_1"),
                self.test_data.get("assign_task_response_2"),
                self.test_data.get("assign_task_response_1"),
                self.test_data.get("assign_task_response_2"),
                self.test_data.get("assign_task_response_1"),
                self.test_data.get("assign_task_response_2"),
                self.test_data.get("assign_task_response_1"),
                self.test_data.get("assign_task_response_2"),
                self.test_data.get("assign_task_response_1"),
                self.test_data.get("assign_task_response_2"),
                self.test_data.get("assign_task_response_1"),
                self.test_data.get("assign_task_response_2"),
            ]

        if "assign_cred_2" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("get_site_1"),
                self.test_data.get("get_site_2"),
                self.test_data.get("global_assign_cred"),
                self.test_data.get("assign_task_details"),
                self.test_data.get("assign_task_response_1"),
                self.test_data.get("assign_task_response_2"),
                self.test_data.get("assign_task_response_1"),
                self.test_data.get("assign_task_response_2"),
                self.test_data.get("assign_task_response_1"),
                self.test_data.get("assign_task_response_2"),
                self.test_data.get("assign_task_response_1"),
                self.test_data.get("assign_task_response_2"),
                self.test_data.get("assign_task_response_1"),
                self.test_data.get("assign_task_response_2"),
                self.test_data.get("assign_task_response_1"),
                self.test_data.get("assign_task_response_2"),

            ]

        if "already_sync_cred" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("get_site_1"),
                self.test_data.get("global_assign_cred"),
                self.test_data.get("get_site_assigned_network_devices"),
                self.test_data.get("get_sync_status"),
                self.test_data.get("sync_network_devices_credential"),
                self.test_data.get("get_assigned_cred"),
                self.test_data.get("get_assigned_cred"),
                self.test_data.get("get_assigned_cred"),
            ]

        if "update_verify" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("global_credential_updation"),
                self.test_data.get("updation_task_details"),
                self.test_data.get("update_task_response"),
                self.test_data.get("global_assign_cred"),
            ]

        if "apply_sync" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("apply_get_sites"),
                self.test_data.get("global_assign_cred"),
                self.test_data.get("apply_get_site_assigned_network_devices"),
                self.test_data.get("sync_status"),
                self.test_data.get("assigned_cred_to apply"),
                self.test_data.get("sync_network_devices_credential_2"),
                self.test_data.get("sync_task_response_1"),
                self.test_data.get("sync_task_response_2"),
                self.test_data.get("sync_task_response_1"),
                self.test_data.get("sync_task_response_2"),
                self.test_data.get("sync_task_response_1"),
                self.test_data.get("sync_task_response_2"),
                self.test_data.get("sync_task_response_1"),
                self.test_data.get("sync_task_response_2"),
            ]

        if "null_sync_status" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                Exception(),
                self.test_data.get("global_credential_updation"),
                self.test_data.get("global_assign_cred"),
            ]

        if "invalid_site" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                Exception(),
            ]

        if "invalid_cli" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
            ]

        if "invalid_site_response" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("get_site_3"),
            ]
        if "invalid_site_response_2" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("get_site_4"),
            ]

    def test_device_credentials_workflow_manager_creation(self):
        """
        Test case for device credential workflow manager when creating a device credential.

        This test case checks the behavior of the device credential workflow manager when creating a new device credentials in the specified DNAC.
        """
        set_module_args(
            dict(
                dnac_host="1.1.1.1",
                dnac_username="dummy",
                dnac_password="dummy",
                dnac_log=True,
                state="merged",
                config=self.playbook_config_creation
            )
        )
        result = self.execute_module(changed=True, failed=False)
        print(result)
        self.assertEqual(
            result['response'][0]['globalCredential']['Creation']['msg'],
            "Global Credential Created Successfully"
        )

    def test_device_credentials_workflow_manager_deletion(self):
        """
        Test case for device credential workflow manager when deleting a device credential.

        This test case checks the behavior of the device credential workflow manager when deleting a device credentials in the specified DNAC.
        """
        set_module_args(
            dict(
                dnac_host="1.1.1.1",
                dnac_username="dummy",
                dnac_password="dummy",
                dnac_log=True,
                state="deleted",
                config_verify=True,
                config=self.playbook_config_deletion
            )
        )
        result = self.execute_module(changed=True, failed=False)
        print(result)
        self.assertEqual(
            result['response'][0]['globalCredential']['Deletion']['msg'],
            "Global Device Credentials Deleted Successfully"
        )

    def test_device_credentials_workflow_manager_assign_cred_1(self):
        """
        Test case for device credential workflow manager when assigning a device credential to site in dnac_version="2.3.7.6".

        This test case checks the behavior of the device credential workflow manager when assigning a device credential to site in the specified DNAC.
        """
        set_module_args(
            dict(
                dnac_host="1.1.1.1",
                dnac_username="dummy",
                dnac_password="dummy",
                dnac_version="2.3.7.6",
                dnac_log=True,
                state="merged",
                config=self.playbook_config_assign
            )
        )
        result = self.execute_module(changed=True, failed=False)
        print(result)
        self.assertEqual(
            result['response'][0]['assignCredential']['Assign Credentials']['msg'],
            "Device Credential Assigned to a site is Successfully"
        )

    def test_device_credentials_workflow_manager_assign_cred_2(self):
        """
        Test case for device credential workflow manager when assigning a device credential to site in dnac_version="2.3.5.3".

        This test case checks the behavior of the device credential workflow manager when assigning a device credential to site in the specified DNAC.
        """
        set_module_args(
            dict(
                dnac_host="1.1.1.1",
                dnac_username="dummy",
                dnac_password="dummy",
                dnac_version="2.3.5.3",
                dnac_log=True,
                state="merged",
                config=self.playbook_config_assign
            )
        )
        result = self.execute_module(changed=True, failed=False)
        print(result)
        self.assertEqual(
            result['response'][0]['assignCredential']['Assign Credentials']['msg'],
            "Device Credential Assigned to a site is Successfully"
        )

    def test_device_credentials_workflow_manager_already_sync_cred(self):
        """
        Test case for device credential workflow manager when applying a device credential to site devices where sync is already applied.

        This test case checks the behavior of the device credential workflow manager when applying a device credential to site devices

        where sync is already applied in the specified DNAC.
        """
        set_module_args(
            dict(
                dnac_host="1.1.1.1",
                dnac_username="dummy",
                dnac_password="dummy",
                dnac_version="2.3.7.6",
                dnac_log=True,
                state="merged",
                config=self.playbook_config_apply
            )
        )
        result = self.execute_module(changed=False, failed=False)
        print(result)
        self.assertEqual(
            result['response'][0]['applyCredential']['Applied Credentials']['msg'],
            "Provided credentials category is/are already synced."
        )

    def test_device_credentials_workflow_manager_update_verify(self):
        """
        Test case for device credential workflow manager when updating a device credential.

        This test case checks the behavior of the device credential workflow manager when updating a new device credentials in the specified DNAC.
        """
        set_module_args(
            dict(
                dnac_host="1.1.1.1",
                dnac_username="dummy",
                dnac_password="dummy",
                dnac_version="2.3.7.6",
                dnac_log=True,
                state="merged",
                config_verify=True,
                config=self.playbook_config_creation
            )
        )
        result = self.execute_module(changed=True, failed=False)
        print(result)
        self.assertEqual(
            result['response'][0]['globalCredential']['Updation']['msg'],
            "Global Device Credential Updated Successfully"
        )

    def test_device_credentials_workflow_manager_apply_sync(self):
        """
        Test case for device credential workflow manager when applying a device credential to site devices.

        This test case checks the behavior of the device credential workflow manager when applying a device credential

        to site devices in the specified DNAC.
        """
        set_module_args(
            dict(
                dnac_host="1.1.1.1",
                dnac_username="dummy",
                dnac_password="dummy",
                dnac_version="2.3.7.6",
                dnac_log=True,
                state="merged",
                config=self.playbook_config_apply
            )
        )
        result = self.execute_module(changed=True, failed=False)
        print(result)
        self.assertEqual(
            result['response'][0]['applyCredential']['Applied Credentials']['msg'],
            "Successfully applied credential."
        )

    def test_device_credentials_workflow_manager_invalid_state(self):
        """
        Test case for device credential workflow manager when state is invalid.

        This test case checks the behavior of the device credential workflow manager when state is invalid for the specified DNAC.
        """
        set_module_args(
            dict(
                dnac_host="1.1.1.1",
                dnac_username="dummy",
                dnac_password="dummy",
                dnac_version="2.3.7.6",
                dnac_log=True,
                config=self.playbook_config_apply
            )
        )
        result = self.execute_module(changed=False, failed=True)
        print(result)
        self.assertEqual(
            result['msg'],
            "The username and description of the CLI credential are invalid"
        )

    def test_device_credentials_workflow_manager_null_sync_status(self):
        """
        Test case for device credential workflow manager when exception occured during sync credential.

        This test case checks the behavior of the device credential workflow manager, when exception occured during sync credential in the specified DNAC.
        """
        set_module_args(
            dict(
                dnac_host="1.1.1.1",
                dnac_username="dummy",
                dnac_password="dummy",
                dnac_version="2.3.7.6",
                dnac_log=True,
                state="merged",
                config=self.playbook_config_apply
            )
        )
        result = self.execute_module(changed=False, failed=True)
        print(result)
        self.assertEqual(
            result['msg'],
            "Exception occurred while getting global device credentials sync status: "
        )

    def test_device_credentials_workflow_manager_invalid_site(self):
        """
        Test case for device credential workflow manager when provided site is invalid.

        This test case checks the behavior of the device credential workflow manager, when provided site is invalid in the specified DNAC.
        """
        set_module_args(
            dict(
                dnac_host="1.1.1.1",
                dnac_username="dummy",
                dnac_password="dummy",
                dnac_version="2.3.7.6",
                dnac_log=True,
                state="merged",
                config=self.playbook_config_assign
            )
        )
        result = self.execute_module(changed=False, failed=True)
        print(result)
        self.assertEqual(
            result['msg'],
            "The site_name 'Global/Vietnam/halong/Hanoi' is invalid in 'assign_credentials_to_site'"
        )

    def test_device_credentials_workflow_manager_invalid_cli(self):
        """
        Test case for device credential workflow manager when provided cli is invalid.

        This test case checks the behavior of the device credential workflow manager when when provided cli is invalid in the specified DNAC.
        """
        set_module_args(
            dict(
                dnac_host="1.1.1.1",
                dnac_username="dummy",
                dnac_password="dummy",
                dnac_log=True,
                state="merged",
                config=self.playbook_invalid_cli
            )
        )
        result = self.execute_module(changed=False, failed=True)
        print(result)
        self.assertEqual(
            result['msg'],
            "Exception occurred while getting global device credentials: "
        )

    def test_device_credentials_workflow_manager_invalid_site_response(self):
        """
        Test case for device credential workflow manager when provided site response is invalid.

        This test case checks the behavior of the device credential workflow manager when provided site response is invalid in the specified DNAC.
        """
        set_module_args(
            dict(
                dnac_host="1.1.1.1",
                dnac_username="dummy",
                dnac_password="dummy",
                dnac_log=True,
                state="merged",
                config=self.playbook_config_apply
            )
        )
        result = self.execute_module(changed=False, failed=True)
        print(result)
        self.assertEqual(
            result['msg'],
            "Exception occurred while getting global device credentials: "
        )

    def test_device_credentials_workflow_manager_invalid_site_response_2(self):
        """
        Test case for device credential workflow manager when provided site response is invalid.

        This test case checks the behavior of the device credential workflow manager when provided site response is invalid in the specified DNAC.
        """
        set_module_args(
            dict(
                dnac_host="1.1.1.1",
                dnac_username="dummy",
                dnac_password="dummy",
                dnac_log=True,
                state="merged",
                config=self.playbook_config_apply
            )
        )
        result = self.execute_module(changed=False, failed=True)
        print(result)
        self.assertEqual(
            result['msg'],
            "Exception occurred while getting global device credentials: "
        )
