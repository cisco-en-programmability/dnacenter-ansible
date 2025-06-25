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

# Authors:
#   A Mohamed Rafeek <mabdulk2@cisco.com>
#
# Description:
#   Unit tests for the Ansible module `network_profile_switching_workflow_manager`.
#   These tests cover various switch profile operations such as creation,
#   update, deletion and validation logic using mocked Catalyst Center responses.

# Make coding more python3-ish
from __future__ import absolute_import, division, print_function

__metaclass__ = type
from unittest.mock import patch
from ansible_collections.cisco.dnac.plugins.modules import network_profile_switching_workflow_manager
from .dnac_module import TestDnacModule, set_module_args, loadPlaybookData


class TestDnacSwitchWorkflow(TestDnacModule):

    module = network_profile_switching_workflow_manager

    test_data = loadPlaybookData("network_profile_switching_workflow_manager")
    playbook_config_creation = test_data.get("playbook_config_creation")
    playbook_config_deletion = test_data.get("playbook_config_deletion")
    playbook_config_unasssign = test_data.get("playbook_config_unasssign")
    playbook_config_switch_profile = test_data.get("playbook_config_switch_profile")
    playbook_update_day_n_template = test_data.get("playbook_update_day_n_template")
    playbook_update_day_n_template1 = test_data.get("playbook_update_day_n_template1")
    playbook_delete_switch_profile = test_data.get("playbook_delete_switch_profile")

    def setUp(self):
        super(TestDnacSwitchWorkflow, self).setUp()

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
        super(TestDnacSwitchWorkflow, self).tearDown()
        self.mock_dnac_exec.stop()
        self.mock_dnac_init.stop()

    def load_fixtures(self, response=None, device=""):
        """
        Load fixtures for user.
        """
        if "creation_switch_fail" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("get_network_profile_not_exist"),
                self.test_data.get("get_templates_details"),
                self.test_data.get("get_site_response1"),
                self.test_data.get("get_site_response1"),
                self.test_data.get("get_site_response2"),
            ]
        elif "delete_switch_profile" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("get_network_profile"),
                self.test_data.get("get_templates_for_profile_delete"),
                self.test_data.get("get_site_for_profile_delete"),
                self.test_data.get("unassign_site_for_delete"),
                self.test_data.get("unassign_site_task_detail_response"),
                self.test_data.get("unassign_site_task_progress"),
                self.test_data.get("unassign_site_for_delete"),
                self.test_data.get("unassign_site_task_detail_response"),
                self.test_data.get("unassign_template_task_progress"),
                self.test_data.get("unassign_site_for_delete"),
                self.test_data.get("unassign_site_task_detail_response"),
                self.test_data.get("profile_delete_task_progress"),
                self.test_data.get("verify_delete_get_network_profile"),
            ]
        elif "delete_switch_profile_success" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("retrieve_cli_templates_attached_to_a_network_profile_delete"),
                self.test_data.get("retrieve_cli_templates_attached_to_a_network_profile_delete11"),
                self.test_data.get("retrieves_the_list_of_sites_that_the_given_network_profile_for_sites_is_assigned_to_delete"),
                self.test_data.get("get_site_lists_for_profile"),
                self.test_data.get("unassigns_a_network_profile_for_sites_from_multiple_sites"),
                self.test_data.get("get_tasks_by_id_delete"),
                self.test_data.get("detach_a_list_of_network_profiles_from_a_day_n_cli_template"),
                self.test_data.get("get_tasks_by_id_delete1"),
                self.test_data.get("deletes_a_network_profile_for_sites"),
                self.test_data.get("get_tasks_by_id_delete3"),
                self.test_data.get("retrieves_the_list_of_network_profiles_for_sites_delete")
            ]
        elif "unassign_site_template" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("get_network_profile"),
                self.test_data.get("get_templates_details"),
                self.test_data.get("get_site_response1"),
                self.test_data.get("get_site_response1"),
                self.test_data.get("get_templates_for_profile_delete"),
                self.test_data.get("get_site_for_profile_delete"),
                self.test_data.get("unassign_site_for_delete"),
                self.test_data.get("unassign_site_task_detail_response"),
                self.test_data.get("unassign_site_task_progress"),
                self.test_data.get("unassign_site_for_delete"),
                self.test_data.get("unassign_site_task_detail_response"),
                self.test_data.get("unassign_template_task_progress"),
                self.test_data.get("get_network_profile"),
                self.test_data.get("get_templates_details"),
                self.test_data.get("get_site_response1"),
                self.test_data.get("get_child_site_with_empty_response"),
                self.test_data.get("get_child_site_with_empty_response"),
            ]
        elif "creation_switch_success_site" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("retrieves_the_list_of_network_profiles_for_sites01"),
                self.test_data.get("get_site_details01"),
                self.test_data.get("get_site_details02"),
                self.test_data.get("retrieve_cli_templates_attached_to_a_network_profile02"),
                self.test_data.get("retrieves_the_list_of_sites_that_the_given_network_profile_for_sites_is_assigned_to01"),
                self.test_data.get("assign_a_network_profile_for_sites_to_the_given_site01"),
            ]
        elif "update_day_n_template" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("retrieves_the_list_of_network_profiles_for_sites1"),
                self.test_data.get("get_templates_details1"),
                self.test_data.get("retrieve_cli_templates_attached_to_a_network_profile2"),
                self.test_data.get("attach_network_profile_to_a_day_n_cli_template"),
                self.test_data.get("get_tasks_by_id"),
                self.test_data.get("get_task_details_by_id11"),
                self.test_data.get("attach_network_profile_to_a_day_n_cli_template1"),
                self.test_data.get("get_tasks_by_id11"),
                self.test_data.get("get_task_details_by_id12")
            ]

        elif "update_day_n_template_success" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("retrieves_the_list_of_network_profiles_for_sites11"),
                self.test_data.get("gets_the_templates_available"),
                self.test_data.get("retrieve_cli_templates_attached_to_a_network_profile12"),
                self.test_data.get("retrieves_the_list_of_sites_that_the_given_network_profile_for_sites_is_assigned_to"),
                self.test_data.get("attach_network_profile_to_a_day_n_cli_template11"),
                self.test_data.get("get_tasks_by_id1"),
                self.test_data.get("get_dn_template")
            ]

    def test_network_profile_switching_workflow_manager_creation_switch_fail(self):
        """
        Test case for creating a switch workflow manager instance.

        This test case checks the behavior of the switch workflow creation
        in the specified Cisco Catalyst Center.
        """
        set_module_args(
            dict(
                dnac_host="1.1.1.1",
                dnac_username="dummy",
                dnac_password="dummy",
                dnac_log=True,
                state="merged",
                dnac_version="2.3.7.9",
                config=self.playbook_config_creation
            )
        )
        result = self.execute_module(changed=False, failed=True)
        self.assertEqual(
            result.get('msg'),
            "Successfully retrieved the details from the system"
        )

    def test_network_profile_switching_workflow_manager_delete_switch_profile(self):
        """
        Test case for deleteion a switch workflow manager instance.

        This test case checks the behavior of the switch workflow deletion
        in the specified Cisco Catalyst Center.
        """
        set_module_args(
            dict(
                dnac_host="1.1.1.1",
                dnac_username="dummy",
                dnac_password="dummy",
                dnac_log=True,
                state="deleted",
                dnac_version="2.3.7.9",
                config_verify=True,
                config=self.playbook_config_deletion
            )
        )
        result = self.execute_module(changed=False, failed=True)
        self.maxDiff = None
        self.assertEqual(
            result.get('msg'),
            "Unable to delete the profile '[{'profile_name': 'switchProfile1', " +
            "'site_names': None, 'onboarding_templates': None, 'day_n_templates': None}]'."
        )

    def test_network_profile_switching_workflow_manager_delete_switch_profile_site(self):
        """
        Test case for deleteion a switch workflow manager instance.

        This test case checks the behavior of the switch workflow deletion
        in the specified Cisco Catalyst Center.
        """
        set_module_args(
            dict(
                dnac_host="1.1.1.1",
                dnac_username="dummy",
                dnac_password="dummy",
                dnac_log=True,
                state="deleted",
                dnac_version="2.3.7.9",
                config_verify=True,
                config=self. playbook_delete_switch_profile
            )
        )
        result = self.execute_module(changed=False, failed=False)
        self.maxDiff = None
        self.assertEqual(
            result.get('msg'),
            "No changes required, profile(s) are already deleted."
        )

    def test_network_profile_switching_workflow_manager_unassign_site_template(self):
        """
        Test case for unassign the site and template from switch profile.

        This test case checks the behavior of the switch workflow unassign the site and template.
        in the specified Cisco Catalyst Center.
        """
        set_module_args(
            dict(
                dnac_host="1.1.1.1",
                dnac_username="dummy",
                dnac_password="dummy",
                dnac_log=True,
                state="deleted",
                dnac_version="2.3.7.9",
                config_verify=True,
                config=self.playbook_config_unasssign
            )
        )
        result = self.execute_module(changed=False, failed=True)
        self.maxDiff = None
        self.assertEqual(
            result.get('msg'),
            "Switch profile(s) deleted/unassigned and verified successfully for '['switchProfile1']'."
        )

    def test_network_profile_switching_workflow_manager_creation_switch_site(self):
        """
        Test case for creating a switch workflow manager instance.

        This test case checks the behavior of the switch workflow creation
        in the specified Cisco Catalyst Center.
        """
        set_module_args(
            dict(
                dnac_host="1.1.1.1",
                dnac_username="dummy",
                dnac_password="dummy",
                dnac_log=True,
                state="merged",
                dnac_version="2.3.7.9",
                config=self.playbook_config_switch_profile
            )
        )
        result = self.execute_module(changed=False, failed=True)
        self.maxDiff = None
        self.assertIn(
            'No site details retrieved for site name: Global/APO',
            result.get('msg')
        )

    def test_network_profile_switching_workflow_manager_creation_switch_site_fail(self):
        """
        Test case for creating a switch workflow manager instance.

        This test case checks the behavior of the switch workflow creation
        in the specified Cisco Catalyst Center.
        """
        set_module_args(
            dict(
                dnac_host="1.1.1.1",
                dnac_username="dummy",
                dnac_password="dummy",
                dnac_log=True,
                state="merged",
                dnac_version="2.3.7.9",
                config_verify=True,
                config=self.playbook_config_switch_profile
            )
        )
        result = self.execute_module(changed=False, failed=True)
        self.assertIn(
            "No site details retrieved for site name: Global/APO",
            result.get('msg')
        )

    def test_network_profile_switching_workflow_manager_update_day_n_template(self):
        """
        Test case for creating a switch workflow manager instance.

        This test case checks the behavior of the switch workflow creation
        in the specified Cisco Catalyst Center.
        """
        set_module_args(
            dict(
                dnac_host="1.1.1.1",
                dnac_username="dummy",
                dnac_password="dummy",
                dnac_log=True,
                state="merged",
                dnac_version="2.3.7.9",
                config_verify=True,
                config=self.playbook_update_day_n_template
            )
        )
        result = self.execute_module(changed=False, failed=False)
        self.assertIn(
            "No changes required, Switch profile(s) are already created and verified",
            result.get('msg')
        )
