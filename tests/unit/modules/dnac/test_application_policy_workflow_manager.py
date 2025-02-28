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

from ansible_collections.cisco.dnac.plugins.modules import application_policy_workflow_manager
from .dnac_module import TestDnacModule, set_module_args, loadPlaybookData


class TestDnacApplicationPolicyWorkflowManager(TestDnacModule):

    module = application_policy_workflow_manager

    test_data = loadPlaybookData("application_policy_workflow_manager")

    playbook_create_application = test_data.get("playbook_create_application")
    playbook_create_profile = test_data.get("playbook_create_profile")
    playbook_update_profile = test_data.get("playbook_update_profile")
    playbook_create_profile_1 = test_data.get("playbook_create_profile_1")
    playbook_all_speed_update_profile = test_data.get("playbook_all_speed_update_profile")
    playbook_for_application_policy_delete = test_data.get("playbook_for_application_policy_delete")
    playbook_for_application_policy_create = test_data.get("playbook_for_application_policy_create")
    playbook_for_application_queuing_profile_delete = test_data.get("playbook_for_application_queuing_profile_delete")
    playbook_for_application_policy_update = test_data.get("playbook_for_application_policy_update")
    playbook_for_create_application_server_ip = test_data.get("playbook_for_create_application_server_ip")
    playbook_for_delete_application = test_data.get("playbook_for_delete_application")
    playbook_for_update_application_servername = test_data.get("playbook_for_update_application_servername")
    playbook_for_create_application_policy = test_data.get("playbook_for_create_application_policy")

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
        if "playbook_create_application" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("get_applications"),
                self.test_data.get("get_application_sets"),
                self.test_data.get("get_application_sets_1"),
                self.test_data.get("get_application_1"),
                self.test_data.get("create_applications"),
                self.test_data.get("Task_details"),
                self.test_data.get("Task_details_1"),
                self.test_data.get("create_application_response")
            ]

        elif "playbook_create_profile" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("get_application_policy_queuing_profile"),
                self.test_data.get("create_application_policy_queuing_profile"),
                self.test_data.get("task_details"),
                self.test_data.get("task_details_1"),
                self.test_data.get("get_application_policy_queuing_profile_1"),
                self.test_data.get("create_profile_response")
            ]

        elif "playbook_update_profile" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("get_application_policy_queuing_profile_2"),
                self.test_data.get("update_application_policy_queuing_profile"),
                self.test_data.get("task_details_2"),
                self.test_data.get("task_details_3"),
                self.test_data.get("get_application_policy_queuing_profile_4"),
                self.test_data.get("update_profile_response")
            ]

        elif "playbook_create_profile_1" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("get_application_policy_queuing_profile_3"),
                self.test_data.get("create_application_policy_queuing_profile_1"),
                self.test_data.get("task_details_4"),
                self.test_data.get("task_details_5"),
                self.test_data.get("get_application_policy_queuing_profile_5"),
                self.test_data.get("create_profile_response_1")
            ]

        elif "playbook_all_speed_update_profile" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("get_application_policy_queuing_profile_all_speed"),
                self.test_data.get("update_application_policy_queuing_profile_all_speed"),
                self.test_data.get("task_details_for_all_speed"),
                self.test_data.get("task_details_for_all_speed_1"),
                self.test_data.get("get_application_policy_queuing_profile_all_speed_1"),
                self.test_data.get("update_profile_response_1"),
            ]

        elif "playbook_for_application_policy_delete" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("get_application_policy"),
                self.test_data.get("application_policy_intent"),
                self.test_data.get("task_details_for_app_policy_delete"),
                self.test_data.get("task_details_for_app_policy_delete_1"),
                self.test_data.get("get_application_policy_1"),
                self.test_data.get("app_policy_delete_responce"),
            ]

        elif "playbook_for_application_policy_create" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("get_application_policy_queuing_profile_6"),
                self.test_data.get("get_application_policy_2"),
                self.test_data.get("get_application_sets_"),
                self.test_data.get("get_application_sets_2"),
                self.test_data.get("get_application_sets_3"),
                self.test_data.get("get_application_sets_4"),
                self.test_data.get("get_application_sets_5"),
                self.test_data.get("get_application_sets_6"),
                self.test_data.get("application_policy_intent_1"),
                self.test_data.get("task_details_for_creation"),
                self.test_data.get("task_details_for_creation_1"),
                self.test_data.get("get_application_policy_queuing_profile_7"),
                self.test_data.get("get_application_policy_3"),
                self.test_data.get("app_policy_create_responce"),
            ]

        elif "playbook_for_application_queuing_profile_delete" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("get_application_policy_queuing_profile_20"),
                self.test_data.get("delete_application_policy_queuing_profile"),
                self.test_data.get("task_details_20"),
                self.test_data.get("task_details_21"),
                self.test_data.get("get_application_policy_queuing_profile_21"),
                self.test_data.get("app_queuing_profile_delete_response")
            ]

        elif "playbook_for_application_policy_update" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("get_application_policy_queuing_profile_22"),
                self.test_data.get("get_application_policy_22"),
                self.test_data.get("get_sites"),
                self.test_data.get("get_sites_1"),
                self.test_data.get("application_policy_intent_22"),
                self.test_data.get("task_details_22"),
                self.test_data.get("task_details_23"),
                self.test_data.get("get_application_policy_queuing_profile_23"),
                self.test_data.get("get_application_policy_23"),
                self.test_data.get("update_application_policy_response")
            ]

        elif "playbook_for_create_application_server_ip" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("get_applications_30"),
                self.test_data.get("get_application_sets_30"),
                self.test_data.get("get_application_sets_31"),
                self.test_data.get("get_application_30"),
                self.test_data.get("create_applications_30"),
                self.test_data.get("task_details_30"),
                self.test_data.get("task_details_31"),
                self.test_data.get("get_applications_31"),
                self.test_data.get("get_application_sets_32"),
                self.test_data.get("create_application_serverip_response")
            ]

        elif "playbook_for_delete_application" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("get_applications_40"),
                self.test_data.get("delete_application"),
                self.test_data.get("task_details_40"),
                self.test_data.get("task_details_41"),
                self.test_data.get("get_applications_41"),
                self.test_data.get("delete_application_response")
            ]

        elif "playbook_for_update_application_servername" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("get_applications_50"),
                self.test_data.get("get_application_sets_50"),
                self.test_data.get("edit_applications"),
                self.test_data.get("task_details_50"),
                self.test_data.get("task_details_51"),
                self.test_data.get("get_applications_51"),
                self.test_data.get("get_application_sets_51"),
                self.test_data.get("update_application_response"),
            ]

        elif "playbook_for_create_application_policy" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("get_application_policy_queuing_profile_60"),
                self.test_data.get("get_application_policy_60"),
                self.test_data.get("get_application_sets_60"),
                self.test_data.get("get_application_sets_61"),
                self.test_data.get("get_application_sets_62"),
                self.test_data.get("get_application_sets_63"),
                self.test_data.get("get_application_sets_64"),
                self.test_data.get("get_application_sets_65"),
                self.test_data.get("application_policy_intent_60"),
                self.test_data.get("task_details_60"),
                self.test_data.get("task_details_61"),
                self.test_data.get("get_application_policy_queuing_profile_61"),
                self.test_data.get("get_application_policy_61"),
                self.test_data.get("create_application_policy_response"),
            ]

    def test_application_policy_workflow_manager_playbook_create_application(self):
        """
        Test case for user role workflow manager when creating a user.

        This test case checks the behavior of the user workflow when creating a new user in the specified Cisco Catalyst Center.
        """
        set_module_args(
            dict(
                dnac_host="1.1.1.1",
                dnac_username="dummy",
                dnac_password="dummy",
                dnac_log=True,
                state="merged",
                config=self.playbook_create_application
            )
        )
        result = self.execute_module(changed=True, failed=False)
        print(result)
        self.assertEqual(
            result.get("response"),
            "application 'unit_test_application' created successfully."
        )

    def test_application_policy_workflow_manager_playbook_create_profile(self):
        """
        Test case for user role workflow manager when creating a user.

        This test case checks the behavior of the user workflow when creating a new user in the specified Cisco Catalyst Center.
        """
        set_module_args(
            dict(
                dnac_host="1.1.1.1",
                dnac_username="dummy",
                dnac_password="dummy",
                dnac_log=True,
                state="merged",
                config_verify=True,
                config=self.playbook_create_profile
            )
        )
        result = self.execute_module(changed=True, failed=False)
        print(result)
        self.assertEqual(
            result.get("response"),
            "application queuing profile created successfully."
        )

    def test_application_policy_workflow_manager_playbook_update_profile(self):
        """
        Test case for user role workflow manager when creating a user.

        This test case checks the behavior of the user workflow when creating a new user in the specified Cisco Catalyst Center.
        """
        set_module_args(
            dict(
                dnac_host="1.1.1.1",
                dnac_username="dummy",
                dnac_password="dummy",
                dnac_log=True,
                state="merged",
                config_verify=True,
                config=self.playbook_update_profile
            )
        )
        result = self.execute_module(changed=True, failed=False)
        print(result)
        self.assertEqual(
            result.get("response"),
            "application policy queuing profile 'UT_test_profile' updated successfully."
        )

    def test_application_policy_workflow_manager_playbook_create_profile_1(self):
        """
        Test case for user role workflow manager when creating a user.

        This test case checks the behavior of the user workflow when creating a new user in the specified Cisco Catalyst Center.
        """
        set_module_args(
            dict(
                dnac_host="1.1.1.1",
                dnac_username="dummy",
                dnac_password="dummy",
                dnac_log=True,
                state="merged",
                config_verify=True,
                config=self.playbook_create_profile_1
            )
        )
        result = self.execute_module(changed=True, failed=False)
        print(result)
        self.assertEqual(
            result.get("response"),
            "application queuing profile created successfully."
        )

    def test_application_policy_workflow_manager_playbook_all_speed_update_profile(self):
        """
        Test case for user role workflow manager when creating a user.

        This test case checks the behavior of the user workflow when creating a new user in the specified Cisco Catalyst Center.
        """
        set_module_args(
            dict(
                dnac_host="1.1.1.1",
                dnac_username="dummy",
                dnac_password="dummy",
                dnac_log=True,
                state="merged",
                config_verify=True,
                config=self.playbook_all_speed_update_profile
            )
        )
        result = self.execute_module(changed=True, failed=False)
        print(result)
        self.assertEqual(
            result.get("response"),
            "application policy queuing profile 'uttestprofile' updated successfully."
        )

    def test_application_policy_workflow_manager_playbook_for_application_policy_delete(self):
        """
        Test case for user role workflow manager when creating a user.

        This test case checks the behavior of the user workflow when creating a new user in the specified Cisco Catalyst Center.
        """
        set_module_args(
            dict(
                dnac_host="1.1.1.1",
                dnac_username="dummy",
                dnac_password="dummy",
                dnac_log=True,
                state="deleted",
                config_verify=True,
                config=self.playbook_for_application_policy_delete
            )
        )
        result = self.execute_module(changed=True, failed=False)
        print(result)
        self.assertEqual(
            result.get("response"),
            "application policy 'test_policy_1' deleted successfully."
        )

    def test_application_policy_workflow_manager_playbook_for_application_policy_create(self):
        """
        Test case for user role workflow manager when creating a user.

        This test case checks the behavior of the user workflow when creating a new user in the specified Cisco Catalyst Center.
        """
        set_module_args(
            dict(
                dnac_host="1.1.1.1",
                dnac_username="dummy",
                dnac_password="dummy",
                dnac_log=True,
                state="merged",
                config_verify=True,
                config=self.playbook_for_application_policy_create
            )
        )
        result = self.execute_module(changed=True, failed=False)
        print(result)
        self.assertEqual(
            result.get("response"),
            "application policy 'test_policy_1' created successfully."
        )

    def test_application_policy_workflow_manager_playbook_for_application_queuing_profile_delete(self):
        """
        Test case for user role workflow manager when creating a user.

        This test case checks the behavior of the user workflow when creating a new user in the specified Cisco Catalyst Center.
        """
        set_module_args(
            dict(
                dnac_host="1.1.1.1",
                dnac_username="dummy",
                dnac_password="dummy",
                dnac_log=True,
                state="deleted",
                config_verify=True,
                config=self.playbook_for_application_queuing_profile_delete
            )
        )
        result = self.execute_module(changed=True, failed=False)
        print(result)
        self.assertEqual(
            result.get("response"),
            "application policy queuing profile 'UT_test_profile' deleted successfully."
        )

    def test_application_policy_workflow_manager_playbook_for_application_policy_update(self):
        """
        Test case for user role workflow manager when creating a user.

        This test case checks the behavior of the user workflow when creating a new user in the specified Cisco Catalyst Center.
        """
        set_module_args(
            dict(
                dnac_host="1.1.1.1",
                dnac_username="dummy",
                dnac_password="dummy",
                dnac_log=True,
                state="merged",
                dnac_version="2.3.7.6",
                config_verify=True,
                config=self.playbook_for_application_policy_update
            )
        )
        result = self.execute_module(changed=True, failed=False)
        print(result)
        self.assertEqual(
            result.get("response"),
            "application policy 'test_policy_1' updated successfully."
        )

    def test_application_policy_workflow_manager_playbook_for_create_application_server_ip(self):
        """
        Test case for user role workflow manager when creating a user.

        This test case checks the behavior of the user workflow when creating a new user in the specified Cisco Catalyst Center.
        """
        set_module_args(
            dict(
                dnac_host="1.1.1.1",
                dnac_username="dummy",
                dnac_password="dummy",
                dnac_log=True,
                state="merged",
                dnac_version="2.3.7.6",
                config_verify=True,
                config=self.playbook_for_create_application_server_ip
            )
        )
        result = self.execute_module(changed=True, failed=False)
        print(result)
        self.assertEqual(
            result.get("response"),
            "application 'unittestapp3' created successfully."
        )

    def test_application_policy_workflow_manager_playbook_for_delete_application(self):
        """
        Test case for user role workflow manager when creating a user.

        This test case checks the behavior of the user workflow when creating a new user in the specified Cisco Catalyst Center.
        """
        set_module_args(
            dict(
                dnac_host="1.1.1.1",
                dnac_username="dummy",
                dnac_password="dummy",
                dnac_log=True,
                state="deleted",
                dnac_version="2.3.7.6",
                config_verify=True,
                config=self.playbook_for_delete_application
            )
        )
        result = self.execute_module(changed=True, failed=False)
        print(result)
        self.assertEqual(
            result.get("response"),
            "application 'unittestapp3' deleted successfully."
        )

    def test_application_policy_workflow_manager_playbook_for_update_application_servername(self):
        """
        Test case for user role workflow manager when creating a user.

        This test case checks the behavior of the user workflow when creating a new user in the specified Cisco Catalyst Center.
        """
        set_module_args(
            dict(
                dnac_host="1.1.1.1",
                dnac_username="dummy",
                dnac_password="dummy",
                dnac_log=True,
                state="merged",
                dnac_version="2.3.7.6",
                config_verify=True,
                config=self.playbook_for_update_application_servername
            )
        )
        result = self.execute_module(changed=True, failed=False)
        print(result)
        self.assertEqual(
            result.get("response"),
            "application 'unit_test' updated successfully."
        )

    def test_application_policy_workflow_manager_playbook_for_create_application_policy(self):
        """
        Test case for user role workflow manager when creating a user.

        This test case checks the behavior of the user workflow when creating a new user in the specified Cisco Catalyst Center.
        """
        set_module_args(
            dict(
                dnac_host="1.1.1.1",
                dnac_username="dummy",
                dnac_password="dummy",
                dnac_log=True,
                state="merged",
                dnac_version="2.3.7.6",
                config_verify=True,
                config=self.playbook_for_create_application_policy
            )
        )
        result = self.execute_module(changed=True, failed=False)
        print(result)
        self.assertEqual(
            result.get("response"),
            "application policy 'test_policy_unit' created successfully."
        )
