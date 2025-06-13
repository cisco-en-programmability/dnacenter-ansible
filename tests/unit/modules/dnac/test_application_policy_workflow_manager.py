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

    playbook_create_profile = test_data.get("playbook_create_profile")
    playbook_update_profile = test_data.get("playbook_update_profile")
    playbook_create_profile_1 = test_data.get("playbook_create_profile_1")
    playbook_all_speed_update_profile = test_data.get("playbook_all_speed_update_profile")
    playbook_for_application_policy_delete = test_data.get("playbook_for_application_policy_delete")
    playbook_create_policy_wired_error = test_data.get("playbook_create_policy_wired_error")
    playbook_for_application_queuing_profile_delete = test_data.get("playbook_for_application_queuing_profile_delete")
    playbook_for_application_policy_update = test_data.get("playbook_for_application_policy_update")
    playbook_delete_application = test_data.get("playbook_delete_application")
    playbook_for_queuing_profiletrue_noupdate = test_data.get("playbook_for_queuing_profiletrue_noupdate")
    playbook_for_profile_dscp = test_data.get("playbook_for_profile_dscp")
    playbook_dscp_update = test_data.get("playbook_dscp_update")
    playbook_noprofname = test_data.get("playbook_noprofname")
    playbook_failure_profile = test_data.get("playbook_failure_profile")
    playbook_profile_namedesc_update = test_data.get("playbook_profile_namedesc_update")
    playbook_create_application_servername = test_data.get("playbook_create_application_servername")
    playbook_create_application_serverip = test_data.get("playbook_create_application_serverip")
    playbook_update_application_serveriptoname = test_data.get("playbook_update_application_serveriptoname")
    playbook_update_application_nametourl = test_data.get("playbook_update_application_nametourl")
    playbook_multiple_profile_delete = test_data.get("playbook_multiple_profile_delete")
    playbook_application_delete = test_data.get("playbook_application_delete")
    playbook_error_1 = test_data.get("playbook_error_1")
    playbook_error_2 = test_data.get("playbook_error_2")
    playbook_error_3 = test_data.get("playbook_error_3")
    playbook_application_noupdate = test_data.get("playbook_application_noupdate")
    playbook_policy_noupdate = test_data.get("playbook_policy_noupdate")
    playbook_policy_alreadydeleted = test_data.get("playbook_policy_alreadydeleted")
    playbook_application_alreadydeleted = test_data.get("playbook_application_alreadydeleted")
    playbook_profile_alreadydeleted = test_data.get("playbook_profile_alreadydeleted")
    playbook_error_4 = test_data.get("playbook_error_4")
    playbook_error_5 = test_data.get("playbook_error_5")
    playbook_error_6 = test_data.get("playbook_error_6")
    playbook_error_7 = test_data.get("playbook_error_7")
    playbook_error_8 = test_data.get("playbook_error_8")

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

        if "playbook_create_profile" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("get_application_policy_queuing_profile"),
                self.test_data.get("create_application_policy_queuing_profile"),
                self.test_data.get("task_details"),
                self.test_data.get("task_details_1"),
                self.test_data.get("get_application_policy_queuing_profile_1"),
                self.test_data.get("create_profile_response")
            ]

        elif "playbook_for_profile_dscp" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("get_application_policy_queuing_profile_70"),
                self.test_data.get("create_application_policy_queuing_profile_70"),
                self.test_data.get("task_details_70"),
                self.test_data.get("task_details_71"),
                self.test_data.get("get_application_policy_queuing_profile_71"),
                self.test_data.get("dcsp_profile_response")
            ]

        elif "playbook_for_application_queuing_profile_delete" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("get_application_policy_queuing_profile_5"),
                self.test_data.get("delete_application_policy_queuing_profile"),
                self.test_data.get("task_details_5"),
                self.test_data.get("task_details_6"),
                self.test_data.get("get_application_policy_queuing_profile_6"),
                self.test_data.get("app_queuing_profile_delete_response")
            ]

        elif "playbook_create_profile_1" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("get_application_policy_queuing_profile_10"),
                self.test_data.get("create_application_policy_queuing_profile_10"),
                self.test_data.get("task_details_10"),
                self.test_data.get("task_details_11"),
                self.test_data.get("get_application_policy_queuing_profile_11"),
                self.test_data.get("create_profile_response_1")
            ]

        elif "playbook_all_speed_update_profile" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("get_application_policy_queuing_profile_all_speed_15"),
                self.test_data.get("update_application_policy_queuing_profile_all_speed_15"),
                self.test_data.get("task_details_for_all_speed_15"),
                self.test_data.get("task_details_for_all_speed_16"),
                self.test_data.get("get_application_policy_queuing_profile_all_speed_16"),
                self.test_data.get("update_profile_response_1"),
            ]

        elif "playbook_update_profile" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("get_application_policy_queuing_profile_20"),
                self.test_data.get("update_application_policy_queuing_profile_20"),
                self.test_data.get("task_details_20"),
                self.test_data.get("task_details_21"),
                self.test_data.get("get_application_policy_queuing_profile_21"),
                self.test_data.get("update_profile_response")
            ]

        elif "playbook_dscp_update" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("get_application_policy_queuing_profile_75"),
                self.test_data.get("update_application_policy_queuing_profile"),
                self.test_data.get("task_details_75"),
                self.test_data.get("task_details_76"),
                self.test_data.get("get_application_policy_queuing_profile_76"),
                self.test_data.get("dscp_update_response")
            ]

        elif "playbook_for_application_policy_update" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("get_application_policy_queuing_profile_33"),
                self.test_data.get("get_application_policy_10"),
                self.test_data.get("get_sites"),
                self.test_data.get("get_sites_1"),
                self.test_data.get("application_policy_intent_10"),
                self.test_data.get("task_details_30"),
                self.test_data.get("task_details_31"),
                self.test_data.get("get_application_policy_queuing_profile_31"),
                self.test_data.get("get_application_policy_12"),
                self.test_data.get("update_application_policy_response")
            ]

        elif "playbook_for_application_policy_delete" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("get_application_policy_20"),
                self.test_data.get("get_application_policy_21"),
                self.test_data.get("application_policy_intent_30"),
                self.test_data.get("task_details_40"),
                self.test_data.get("task_details_41"),
                self.test_data.get("get_application_policy_31"),
                self.test_data.get("get_application_policy_32"),
                self.test_data.get("app_policy_delete_response"),
            ]

        elif "playbook_for_queuing_profiletrue_noupdate" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("get_application_policy_queuing_profile_50"),
                self.test_data.get("get_application_policy_queuing_profile_51"),
                self.test_data.get("queuing_profile_noupdate_response"),
            ]

        elif "playbook_noprofname" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("response_noprofname_error"),
            ]

        elif "playbook_delete_application" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("get_applications"),
                self.test_data.get("delete_application"),
                self.test_data.get("task_details_80"),
                self.test_data.get("task_details_81"),
                self.test_data.get("get_applications_1"),
                self.test_data.get("delete_application_response")
            ]

        elif "playbook_failure_profile" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("get_applications_profile"),
                self.test_data.get("failure_profile_response"),
            ]

        elif "playbook_create_policy_wired_error" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("get_application_policy_queuing_profile_80"),
                self.test_data.get("get_application_policy_80"),
                self.test_data.get("get_sites_80"),
                self.test_data.get("get_sites_81"),
                self.test_data.get("collaboration-apps"),
                self.test_data.get("email"),
                self.test_data.get("tunneling"),
                self.test_data.get("backup-and-storage"),
                self.test_data.get("general-media"),
                self.test_data.get("file-sharing"),
                self.test_data.get("application_policy_intent_80"),
                self.test_data.get("task_details_82"),
                self.test_data.get("task_details_83"),
                self.test_data.get("get_application_policy_queuing_profile_82"),
                self.test_data.get("get_application_policy_83"),
                self.test_data.get("create_policy_wired_response"),
            ]

        elif "playbook_profile_namedesc_update" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("get_application_policy_queuing_profile_100"),
                self.test_data.get("update_application_policy_queuing_profile_100"),
                self.test_data.get("task_details_100"),
                self.test_data.get("task_details_101"),
                self.test_data.get("get_application_policy_queuing_profile_101"),
                self.test_data.get("namedesc_update_response")
            ]

        elif "playbook_create_application_servername" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("get_applications_20"),
                self.test_data.get("get_application_sets_20"),
                self.test_data.get("get_application_sets_21"),
                self.test_data.get("get_applications_21"),
                self.test_data.get("create_applications_20"),
                self.test_data.get("task_details_25"),
                self.test_data.get("task_details_26"),
                self.test_data.get("get_applications_22"),
                self.test_data.get("get_application_sets_22"),
                self.test_data.get("create_application_servername_response"),
            ]

        elif "playbook_create_application_serverip" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("get_applications_5"),
                self.test_data.get("get_application_set_9"),
                self.test_data.get("get_application_set_10"),
                self.test_data.get("get_applications_11"),
                self.test_data.get("create_applications_1"),
                self.test_data.get("task_details_63"),
                self.test_data.get("task_details_64"),
                self.test_data.get("get_applications_6"),
                self.test_data.get("get_application_set_11"),
                self.test_data.get("create_application_response_serverip"),
            ]

        elif "playbook_update_application_serveriptoname" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("get_applications_v2"),
                self.test_data.get("get_application_sets_v2"),
                self.test_data.get("edit_applications_v2"),
                self.test_data.get("task_details_v2"),
                self.test_data.get("task_details_v3"),
                self.test_data.get("get_applications_v3"),
                self.test_data.get("update_application_response_serveriptoname"),
            ]

        elif "playbook_update_application_nametourl" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("get_applications_35"),
                self.test_data.get("get_application_sets_35"),
                self.test_data.get("edit_applications_35"),
                self.test_data.get("task_details_45"),
                self.test_data.get("task_details_46"),
                self.test_data.get("get_applications_36"),
                self.test_data.get("get_application_sets_36"),
                self.test_data.get("update_application_nametourl"),
            ]

        elif "playbook_multiple_profile_delete" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("get_application_policy_queuing_profile_delete"),
                self.test_data.get("get_application_policy_queuing_profile_delete2"),
                self.test_data.get("delete_application_policy_queuing_profile_1"),
                self.test_data.get("Task_Details_delete"),
                self.test_data.get("Task_Details_delete1"),
                self.test_data.get("get_application_policy_queuing_profile_delete4"),
                self.test_data.get("delete_profile_response"),
            ]

        elif "playbook_application_delete" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("get_applications_v2_delete"),
                self.test_data.get("get_applications_v2_delete1"),
                self.test_data.get("delete_application_v2"),
                self.test_data.get("TaskDetails"),
                self.test_data.get("TaskDetails1"),
                self.test_data.get("get_applications_v2_"),
                self.test_data.get("response"),
            ]

        elif "playbook_error_1" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("response1"),
            ]

        elif "playbook_error_2" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("response1"),
            ]

        elif "playbook_error_3" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("response3"),
            ]

        elif "playbook_application_noupdate" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("get_applications_v2_noupdate"),
                self.test_data.get("get_application_sets_noupdate"),
                self.test_data.get("get_applications_v2_noupdate1"),
                self.test_data.get("get_application_sets_noupdate1"),
                self.test_data.get("response4"),
            ]

        elif "playbook_policy_noupdate" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("get_application_policy_queuing_profile_noupdate"),
                self.test_data.get("get_application_policy_noupdate"),
                self.test_data.get("site_design_noupdate"),
                self.test_data.get("Global/USA/San Jose/BLDG23/FLOOR1_LEVEL1_noupdate"),
                self.test_data.get("get_application_policy_queuing_profile_noupdate1"),
                self.test_data.get("get_application_policy_noupdate1"),
                self.test_data.get("response5"),
            ]

        elif "playbook_policy_alreadydeleted" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("get_application_policy_queuing_profile_alreadydeleted"),
                self.test_data.get("get_application_policy_alreadydeleted"),
                self.test_data.get("get_application_policy_alreadydeleted1"),
                self.test_data.get("get_application_policy_queuing_profile_delete1"),
                self.test_data.get("get_application_policy_alreadydeleted2"),
                self.test_data.get("response7"),
            ]

        elif "playbook_application_alreadydeleted" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("get_application_policy_queuing_profile_alreadydeleted"),
                self.test_data.get("get_applications_v2_alreadydeleted"),
                self.test_data.get("response8"),
            ]

        elif "playbook_profile_alreadydeleted" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("get_application_policy_queuing_profile_alreadydeleted1"),
                self.test_data.get("get_application_policy_queuing_profile_alreadydeleted2"),
                self.test_data.get("response9"),
            ]

        elif "playbook_error_4" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("get_application_policy_queuing_profile_error"),
                self.test_data.get("get_application_policy_error"),
                self.test_data.get("response10"),
            ]

        elif "playbook_error_5" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("get_application_policy_error1"),
                self.test_data.get("response11"),
            ]

        elif "playbook_error_6" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("get_application_policy_queuing_profile_error1"),
                self.test_data.get("get_application_policy_error2"),
                self.test_data.get("response12"),
            ]

        elif "playbook_error_7" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("get_application_policy_queuing_profile_error2"),
                self.test_data.get("get_application_policy_error3"),
                self.test_data.get("site_design_error"),
                self.test_data.get("Global/Chennai/LTTS/FLOOR11"),
                self.test_data.get("response13"),
            ]

        elif "playbook_error_8" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("get_application_policy_queuing_profile_error4"),
                self.test_data.get("get_application_policy_error4"),
                self.test_data.get("site_design_error1"),
                self.test_data.get("Global/AB_Test/AB_Bgl3_error"),
                self.test_data.get("response14"),
            ]

    def test_application_policy_workflow_manager_playbook_create_profile(self):
        """
        Test the Application Policy Workflow Manager's profile creation process.

        This test verifies that the workflow correctly handles the creation of a new
        application policy profile, ensuring proper validation and expected behavior.
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
                config=self.playbook_create_profile
            )
        )
        result = self.execute_module(changed=True, failed=False)
        print(result)
        self.assertEqual(
            result.get("response"),
            "Queuing Profile(s) 'c2' created successfully in Cisco Catalyst Center."
        )

    def test_application_policy_workflow_manager_playbook_for_profile_dscp(self):
        """
        Test the Application Policy Workflow Manager's handling of DSCP profiles.

        This test verifies that the workflow correctly processes DSCP configurations within an application policy profile,
        ensuring expected behavior and proper validation.
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
                config=self.playbook_for_profile_dscp
            )
        )
        result = self.execute_module(changed=True, failed=False)
        print(result)
        self.assertEqual(
            result.get("response"),
            "Queuing Profile(s) 'c8' created successfully in Cisco Catalyst Center."
        )

    def test_application_policy_workflow_manager_playbook_for_application_queuing_profile_delete(self):
        """
        Test the Application Policy Workflow Manager's application queuing profile deletion.

        This test verifies that the workflow correctly handles the deletion of an
        application queuing profile, ensuring proper validation and expected behavior.
        """
        set_module_args(
            dict(
                dnac_host="1.1.1.1",
                dnac_username="dummy",
                dnac_password="dummy",
                dnac_log=True,
                state="deleted",
                config_verify=True,
                dnac_version="2.3.7.6",
                config=self.playbook_for_application_queuing_profile_delete
            )
        )
        result = self.execute_module(changed=False , failed=False)
        print(result)
        self.assertEqual(
            result.get("response"),
            "The requested application queuing profile c2 is not present in the Cisco Catalyst Center and its deletion has been verified."
        )

    def test_application_policy_workflow_manager_playbook_create_profile_1(self):
        """
        Test the Application Policy Workflow Manager's profile creation process.

        This test verifies that the workflow correctly handles the creation of a new
        application policy profile, ensuring proper validation and expected behavior.
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
                config=self.playbook_create_profile_1
            )
        )
        result = self.execute_module(changed=True, failed=False)
        print(result)
        self.assertEqual(
            result.get("response"),
            "Queuing Profile(s) 'c3' created successfully in Cisco Catalyst Center."
        )

    def test_application_policy_workflow_manager_playbook_all_speed_update_profile(self):
        """
        Test the Application Policy Workflow Manager's profile update process.

        This test verifies that the workflow correctly updates an application policy profile
        with new speed settings, ensuring proper validation and expected behavior.
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
                config=self.playbook_all_speed_update_profile
            )
        )
        result = self.execute_module(changed=True, failed=False)
        print(result)
        self.assertEqual(
            result.get("response"),
            "Queuing Profile(s) 'c3' updated successfully in Cisco Catalyst Center."
        )

    def test_application_policy_workflow_manager_playbook_update_profile(self):
        """
        Test the Application Policy Workflow Manager's profile update process.

        This test verifies that the workflow correctly updates an existing application
        policy profile, ensuring proper validation and expected behavior.
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
                config=self.playbook_update_profile
            )
        )
        result = self.execute_module(changed=True, failed=False)
        print(result)
        self.assertEqual(
            result.get("response"),
            "Queuing Profile(s) 'c2' updated successfully in Cisco Catalyst Center."
        )

    def test_application_policy_workflow_manager_playbook_dscp_update(self):
        """
        Test the Application Policy Workflow Manager's DSCP update process.

        This test verifies that the workflow correctly updates the DSCP settings within an application policy profile, ensuring
        proper validation and expected behavior.
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
                config=self.playbook_dscp_update
            )
        )
        result = self.execute_module(changed=True, failed=False)
        print(result)
        self.assertEqual(
            result.get("response"),
            "Queuing Profile(s) 'c8' updated successfully in Cisco Catalyst Center."
        )

    def test_application_policy_workflow_manager_playbook_for_application_policy_update(self):
        """
        Test the Application Policy Workflow Manager's application policy update process.

        This test verifies that the workflow correctly updates an existing application
        policy, ensuring expected behavior.
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
        result = self.execute_module(changed=False, failed=True)
        print(result)
        self.assertEqual(
            result.get("response"),
            "An exception occured while updating the application policy: 'list' object has no attribute 'get'"
        )

    def test_application_policy_workflow_manager_playbook_for_application_policy_delete(self):
        """
        Test the Application Policy Workflow Manager's application policy deletion process.

        This test verifies that the workflow correctly handles the deletion of an existing
        application policy.
        """
        set_module_args(
            dict(
                dnac_host="1.1.1.1",
                dnac_username="dummy",
                dnac_password="dummy",
                dnac_log=True,
                state="deleted",
                config_verify=True,
                dnac_version="2.3.7.6",
                config=self.playbook_for_application_policy_delete
            )
        )
        result = self.execute_module(changed=True, failed=False)
        print(result)
        self.assertEqual(
            result.get("response"),
            "Application Policy(ies) 'policy_1' deleted successfully from Cisco Catalyst Center."
        )

    def test_application_policy_workflow_manager_playbook_for_queuing_profiletrue_noupdate(self):
        """
        Test the Application Policy Workflow Manager's handling of a queuing profile without updates.

        This test verifies that the workflow correctly processes an application policy queuing
        profile when no updates are required, ensuring it maintains expected behavior and stability.
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
                config=self.playbook_for_queuing_profiletrue_noupdate
            )
        )
        result = self.execute_module(changed=False, failed=False)
        print(result)
        self.assertEqual(
            result.get("response"),
            "Queuing Profile(s) 'c2' need no update in Cisco Catalyst Center."
        )

    def test_application_policy_workflow_manager_playbook_noprofname(self):
        """
        Test the Application Policy Workflow Manager's behavior when no profile name is provided.

        This test verifies that the workflow correctly handles scenarios where an application
        policy profile is created or updated without specifying a profile name, ensuring
        proper validation and expected error handling.
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
                config=self.playbook_noprofname
            )
        )
        result = self.execute_module(changed=False, failed=True)
        print(result)
        self.assertEqual(
            result.get("response"),
            "The following parameter(s): 'profile_name' could not be found and are mandatory to create or update application queuing profile."
        )

    def test_application_policy_workflow_manager_playbook_create_policy_wired_error(self):
        """
        Test the Application Policy Workflow Manager's wired policy creation error handling.

        This test verifies that the workflow correctly handles errors encountered
        during the creation of a wired application policy, ensuring proper validation
        and expected failure responses.
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
                config=self.playbook_create_policy_wired_error
            )
        )
        result = self.execute_module(changed=False, failed=True)
        print(result)
        self.assertEqual(
            result.get("response"),
            "An exception occured while creating the application policy: 'list' object has no attribute 'get'"
        )

    def test_application_policy_workflow_manager_playbook_failure_profile(self):
        """
        Test the Application Policy Workflow Manager's handling of profile failures.

        This test verifies that the workflow correctly detects and manages failures
        during the creation, update, or deletion of an application policy profile,
        ensuring proper error handling and expected system responses.
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
                config=self.playbook_failure_profile
            )
        )
        result = self.execute_module(changed=False, failed=True)
        print(result)
        self.assertEqual(
            result.get("response"),
            (
                "The following parameter(s): 'interface_speed' could not be found and are mandatory "
                "to create application queuing profile when 'is_common_between_all_interface_speeds' is true."
            )
        )

    def test_application_policy_workflow_manager_playbook_profile_namedesc_update(self):
        """
        Test the Application Policy Workflow Manager's profile name and description update process.

        This test verifies that the workflow correctly updates the name and description
        of an existing application policy profile, ensuring proper validation and expected behavior.
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
                config=self.playbook_profile_namedesc_update
            )
        )
        result = self.execute_module(changed=True, failed=False)
        print(result)
        self.assertEqual(
            result.get("response"),
            "Queuing Profile(s) 'new' updated successfully in Cisco Catalyst Center."
        )

    def test_application_policy_workflow_manager_playbook_multiple_profile_delete(self):
        """
        Test the Application Policy Workflow Manager's update process from server name to URL.

        This test verifies that the workflow correctly updates an application by replacing
        the server name with a URL, ensuring proper validation and expected behavior.
        """
        set_module_args(
            dict(
                dnac_host="1.1.1.1",
                dnac_username="dummy",
                dnac_password="dummy",
                dnac_log=True,
                state="deleted",
                config_verify=True,
                dnac_version="2.3.7.6",
                config=self.playbook_multiple_profile_delete
            )
        )
        result = self.execute_module(changed=True, failed=False)
        print(result)
        self.assertEqual(
            result.get("response"),
            "Queuing Profile(s) 'b5' deleted successfully from Cisco Catalyst Center."
        )

    def test_application_policy_workflow_manager_playbook_error_1(self):
        """
        Test the Application Policy Workflow Manager's update process from server name to URL.

        This test verifies that the workflow correctly updates an application by replacing
        the server name with a URL, ensuring proper validation and expected behavior.
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
                config=self.playbook_error_1
            )
        )
        result = self.execute_module(changed=False, failed=True)
        print(result)
        self.assertEqual(
            result.get("response"),
            "'queuing_profile' should be a list, found: <class 'dict'>"
        )

    def test_application_policy_workflow_manager_playbook_error_2(self):
        """
        Test the Application Policy Workflow Manager's update process from server name to URL.

        This test verifies that the workflow correctly updates an application by replacing
        the server name with a URL, ensuring proper validation and expected behavior.
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
                config=self.playbook_error_2
            )
        )
        result = self.execute_module(changed=False, failed=True)
        print(result)
        self.assertEqual(
            result.get("response"),
            "At least one of the following parameters must be specified in the playbook: queuing_profile, application, application_policy."
        )

    def test_application_policy_workflow_manager_playbook_error_3(self):
        """
        Test the Application Policy Workflow Manager's update process from server name to URL.

        This test verifies that the workflow correctly updates an application by replacing
        the server name with a URL, ensuring proper validation and expected behavior.
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
                config=self.playbook_error_3
            )
        )
        result = self.execute_module(changed=False, failed=True)
        print(result)
        self.assertEqual(
            result.get("response"),
            "'application_policy' should be a list, found: <class 'dict'>"
        )

    def test_application_policy_workflow_manager_playbook_policy_noupdate(self):
        """
        Test the Application Policy Workflow Manager's update process from server name to URL.

        This test verifies that the workflow correctly updates an application by replacing
        the server name with a URL, ensuring proper validation and expected behavior.
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
                config=self.playbook_policy_noupdate
            )
        )
        result = self.execute_module(changed=False, failed=False)
        print(result)
        self.assertEqual(
            result.get("response"),
            "Application Policy(ies) 'policy_1' need no update in Cisco Catalyst Center."
        )

    def test_application_policy_workflow_manager_playbook_policy_alreadydeleted(self):
        """
        Test the Application Policy Workflow Manager's update process from server name to URL.

        This test verifies that the workflow correctly updates an application by replacing
        the server name with a URL, ensuring proper validation and expected behavior.
        """
        set_module_args(
            dict(
                dnac_host="1.1.1.1",
                dnac_username="dummy",
                dnac_password="dummy",
                dnac_log=True,
                state="deleted",
                config_verify=True,
                dnac_version="2.3.7.6",
                config=self.playbook_policy_alreadydeleted
            )
        )
        result = self.execute_module(changed=False, failed=False)
        print(result)
        self.assertEqual(
            result.get("response"),
            "Application Policy(ies) 'policy_1' do not exist or are already deleted in Cisco Catalyst Center."
        )

    def test_application_policy_workflow_manager_playbook_profile_alreadydeleted(self):
        """
        Test the Application Policy Workflow Manager's update process from server name to URL.

        This test verifies that the workflow correctly updates an application by replacing
        the server name with a URL, ensuring proper validation and expected behavior.
        """
        set_module_args(
            dict(
                dnac_host="1.1.1.1",
                dnac_username="dummy",
                dnac_password="dummy",
                dnac_log=True,
                state="deleted",
                config_verify=True,
                dnac_version="2.3.7.6",
                config=self.playbook_profile_alreadydeleted
            )
        )
        result = self.execute_module(changed=False, failed=False)
        print(result)
        self.assertEqual(
            result.get("response"),
            "Queuing Profile(s) 'c8' do not exist or are already deleted in Cisco Catalyst Center."
        )

    def test_application_policy_workflow_manager_playbook_error_4(self):
        """
        Test the Application Policy Workflow Manager's update process from server name to URL.

        This test verifies that the workflow correctly updates an application by replacing
        the server name with a URL, ensuring proper validation and expected behavior.
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
                config=self.playbook_error_4
            )
        )
        result = self.execute_module(changed=False, failed=True)
        print(result)
        self.assertEqual(
            result.get("response"),
            "Invalid clause_type: BUSINESS_RELEVANCEE. Must be one of ['APPLICATION_POLICY_KNOBS', 'BUSINESS_RELEVANCE']."
        )

    def test_application_policy_workflow_manager_playbook_error_5(self):
        """
        Test the Application Policy Workflow Manager's update process from server name to URL.

        This test verifies that the workflow correctly updates an application by replacing
        the server name with a URL, ensuring proper validation and expected behavior.
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
                config=self.playbook_error_5
            )
        )
        result = self.execute_module(changed=False, failed=True)
        print(result)
        self.assertEqual(
            result.get("response"),
            "Application policy operation failed. The following mandatory parameters are missing or empty: site_names, application_queuing_profile_name."
        )

    def test_application_policy_workflow_manager_playbook_error_6(self):
        """
        Test the Application Policy Workflow Manager's update process from server name to URL.

        This test verifies that the workflow correctly updates an application by replacing
        the server name with a URL, ensuring proper validation and expected behavior.
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
                config=self.playbook_error_6
            )
        )
        result = self.execute_module(changed=False, failed=True)
        print(result)
        self.assertEqual(
            result.get("response"),
            "Invalid clause_type: None or empty. Must be one of ['APPLICATION_POLICY_KNOBS', 'BUSINESS_RELEVANCE']."
        )

    def test_application_policy_workflow_manager_playbook_error_7(self):
        """
        Test the Application Policy Workflow Manager's update process from server name to URL.

        This test verifies that the workflow correctly updates an application by replacing
        the server name with a URL, ensuring proper validation and expected behavior.
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
                config=self.playbook_error_7
            )
        )
        result = self.execute_module(changed=False, failed=True)
        print(result)
        self.assertEqual(
            result.get("response"),
            "no extra application sets can be added to the application policy"
        )

    def test_application_policy_workflow_manager_playbook_error_8(self):
        """
        Test the Application Policy Workflow Manager's update process from server name to URL.

        This test verifies that the workflow correctly updates an application by replacing
        the server name with a URL, ensuring proper validation and expected behavior.
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
                config=self.playbook_error_8
            )
        )
        result = self.execute_module(changed=False, failed=True)
        print(result)
        self.assertEqual(
            result.get("response"),
            "SSID is required for wireless devices"
        )
