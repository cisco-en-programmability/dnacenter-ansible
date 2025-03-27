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
from unittest.mock import patch
from ansible_collections.cisco.dnac.plugins.modules import network_profile_switching_workflow_manager
from .dnac_module import TestDnacModule, set_module_args, loadPlaybookData


class TestDnacSwitchWorkflow(TestDnacModule):

    module = network_profile_switching_workflow_manager

    test_data = loadPlaybookData("network_profile_switching_workflow_manager")
    playbook_config_creation = test_data.get("playbook_config_creation")
    playbook_config_update = test_data.get("playbook_config_update")

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
        if "creation_switch" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("playbook_config_creation"),
                self.test_data.get("get_network_profile"),
                self.test_data.get("get_templates_details"),
                self.test_data.get("get_site_response1"),
                self.test_data.get("get_site_response2"),
                self.test_data.get("create_switch_profile"),
                self.test_data.get("get_tasks_by_id1"),
                self.test_data.get("assign_a_network_profile_for_sites1"),
                self.test_data.get("get_tasks_by_id2"),
                self.test_data.get("assign_a_network_profile_for_sites2"),
                self.test_data.get("get_tasks_by_id3")
            ]

        if "deletion_switch" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("playbook_config_creation"),
                self.test_data.get("get_network_profile"),
                self.test_data.get("get_templates_details"),
                self.test_data.get("get_site_response1"),
                self.test_data.get("get_site_response2"),
                self.test_data.get("get_templates_for_profile"),
                self.test_data.get("get_site_response1"),
                self.test_data.get("unassigns_a_network_profile_for_sites1"),
                self.test_data.get("get_tasks_by_id4"),
                self.test_data.get("get_site_response2"),
                self.test_data.get("unassigns_a_network_profile_for_sites2"),
                self.test_data.get("get_tasks_by_id5"),
                self.test_data.get("deletes_a_network_profile_for_sites_v1"),
                self.test_data.get("get_tasks_by_id6")
            ]

        if "update_switch" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("playbook_config_update"),
                self.test_data.get("get_network_profile"),
                self.test_data.get("get_templates_details"),
                self.test_data.get("get_site_response3"),
                self.test_data.get("get_site_response4"),
                self.test_data.get("get_templates_for_profile"),
                self.test_data.get("get_site_lists_for_profile"),
                self.test_data.get("unassigns_a_network_profile_for_sites3"),
                self.test_data.get("get_tasks_by_id7"),
                self.test_data.get("unassigns_a_network_profile_for_sites4"),
                self.test_data.get("get_tasks_by_id8"),
                self.test_data.get("assign_a_network_profile_for_sites3"),
                self.test_data.get("get_tasks_by_id9"),
                self.test_data.get("assign_a_network_profile_for_sites4"),
                self.test_data.get("get_tasks_by_id10"),
            ]

        if "invalid_site" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                Exception(),
            ]

    def test_switch_workflow_manager_creation(self):
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
        result = self.execute_module(changed=True, failed=False)
        self.assertEqual(
            result.get('msg'),
            ""
        )

    def test_switch_workflow_manager_deletion(self):
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
                config=self.playbook_config_creation
            )
        )
        result = self.execute_module(changed=True, failed=False)
        self.assertEqual(
            result.get('msg'),
            ""
        )

    def test_switch_workflow_manager_updation(self):
        """
        Test case for update a switch workflow manager instance.

        This test case checks the behavior of the switch workflow update
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
                config=self.playbook_config_update
            )
        )
        result = self.execute_module(changed=True, failed=False)
        self.assertEqual(
            result.get('msg'),
            ""
        )

    def test_network_switch_profile_workflow_manager_invalid_site(self):
        """
        Test case for network switch profile workflow manager with an invalid site.

        This test verifies the behavior of the network switch profile workflow manager
        when an invalid site response is provided in Cisco Catalyst Center.
        """
        set_module_args(
            dict(
                dnac_host="1.1.1.1",
                dnac_username="dummy",
                dnac_password="dummy",
                dnac_log=True,
                state="merged",
                config=self.playbook_config_invalid
            )
        )
        result = self.execute_module(changed=False, failed=True)
        print(result)
        self.assertEqual(
            result['msg'],
            ""
        )

    def test_switch_workflow_manager_creation_verify(self):
        """
        Test case for switch workflow manager to check verification status for creation.

        This test case checks the behavior of the switch workflow when
        verified the status for creation in the specified Cisco Catalyst Center.
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
                config=self.playbook_config_creation
            )
        )
        result = self.execute_module(changed=True, failed=False)
        self.assertEqual(
            result.get('msg'),
            ""
        )

    def test_switch_workflow_manager_deletion_verify(self):
        """
        Test case for switch workflow manager to check verification status for deletion.

        This test case checks the behavior of the switch workflow when
        verified the status for deletion in the specified Cisco Catalyst Center.
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
                config=self.playbook_config_creation
            )
        )
        result = self.execute_module(changed=True, failed=False)
        self.assertEqual(
            result.get('msg'),
            ""
        )
