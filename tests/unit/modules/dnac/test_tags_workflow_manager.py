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

from __future__ import absolute_import, division, print_function

__metaclass__ = type
from unittest.mock import patch
from ansible_collections.cisco.dnac.plugins.modules import tags_workflow_manager
from .dnac_module import TestDnacModule, set_module_args, loadPlaybookData


class TestDnacTagsWorkflow(TestDnacModule):

    module = tags_workflow_manager
    test_data = loadPlaybookData("tags_workflow_manager")

    playbook_config_create_a_tag_with_device_port_rules_case_1 = test_data.get(
        "create_a_tag_with_device_port_rules_case_1"
    )
    playbook_config_delete_a_tag_with_device_port_rules_case_2 = test_data.get(
        "delete_a_tag_with_device_port_rules_case_2"
    )
    playbook_config_force_delete_a_tag_with_device_port_rules_case_3 = test_data.get(
        "force_delete_a_tag_with_device_port_rules_case_3"
    )
    playbook_config_update_scope_of_a_tag_with_only_port_rule = test_data.get(
        "update_scope_of_a_tag_with_only_port_rule"
    )
    playbook_config_update_scope_members_of_tag_with_device_ports_rules = test_data.get(
        "update_scope_members_of_tag_with_device_ports_rules"
    )

    def setUp(self):
        super(TestDnacTagsWorkflow, self).setUp()

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

    def tearDown(self):
        super(TestDnacTagsWorkflow, self).tearDown()
        self.mock_dnac_exec.stop()
        self.mock_dnac_init.stop()

    def load_fixtures(self, response=None, device=""):
        """
        Load fixtures for user.
        """
        if "invalid_delete_config" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                # self.test_data.get(""),
            ]
        elif "test_create_a_tag_with_device_port_rules_case_1" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("get_tag_case_1_call_1"),
                self.test_data.get("get_tag_case_1_call_2"),
                self.test_data.get("get_tag_case_1_call_3"),
                self.test_data.get("create_tag_case_1_call_1"),
                self.test_data.get("get_tasks_by_id_case_1_call_1"),
                self.test_data.get("get_tag_case_1_call_4"),
                self.test_data.get("get_tag_case_1_call_2"),
                self.test_data.get("get_tag_case_1_call_3"),
            ]
        elif "test_delete_a_tag_with_device_port_rules_case_2" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("get_tag_case_2_call_1"),
                self.test_data.get("delete_tag_case_2_call_2"),
                self.test_data.get("get_tasks_by_id_case_2_call_1"),
                self.test_data.get("get_task_details_by_id_case_2_call_1"),
            ]
        elif (
            "test_force_delete_a_tag_with_device_port_rules_case_3"
            in self._testMethodName
        ):
            self.run_dnac_exec.side_effect = [
                self.test_data.get("get_tag_case_3_call_1"),
                self.test_data.get("update_tag_case_3_call_1"),
                self.test_data.get("get_tasks_by_id_case_3_call_1"),
                self.test_data.get("get_tag_members_by_id_case_3_call_1"),
                self.test_data.get("get_device_list_case_3_call_1"),
                self.test_data.get("get_device_list_case_3_call_2"),
                self.test_data.get("get_tag_members_by_id_case_3_call_2"),
                self.test_data.get("get_device_list_case_3_call_3"),
                self.test_data.get(
                    "query_the_tags_associated_with_network_devices_case_3_call_1"
                ),
                self.test_data.get(
                    "update_tags_associated_with_the_network_devices_case_3_call_1"
                ),
                self.test_data.get("get_tasks_by_id_case_3_call_2"),
                self.test_data.get(
                    "query_the_tags_associated_with_interfaces_case_3_call_1"
                ),
                self.test_data.get(
                    "update_tags_associated_with_the_interfaces_case_3_call_1"
                ),
                self.test_data.get("get_tasks_by_id_case_3_call_3"),
                self.test_data.get("delete_tag_case_3_call_1"),
                self.test_data.get("get_tasks_by_id_case_3_call_4"),
                self.test_data.get("get_tag_case_3_call_2"),
            ]
        elif "test_update_scope_of_a_tag_with_only_port_rule" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("get_tag_case_4_call_1"),
                self.test_data.get("get_site_id_case_4_call_1"),
                self.test_data.get("update_tag_case_4_call_1"),
                self.test_data.get("get_tasks_by_id_case_4_call_1"),
                self.test_data.get("get_tag_case_4_call_2"),
                self.test_data.get("get_site_id_case_4_call_2"),
            ]
        elif (
            "test_update_scope_members_of_tag_with_device_ports_rules"
            in self._testMethodName
        ):
            self.run_dnac_exec.side_effect = [
                self.test_data.get("get_tag_case_5_call_1"),
                self.test_data.get("get_tag_case_5_call_2"),
                self.test_data.get("update_tag_case_5_call_1"),
                self.test_data.get("get_tasks_by_id_case_5_call_1"),
                self.test_data.get("get_tag_case_5_call_3"),
                self.test_data.get("get_tag_case_5_call_4"),
            ]

    def test_create_a_tag_with_device_port_rules_case_1(self):

        set_module_args(
            dict(
                dnac_host="1.1.1.1",
                dnac_username="dummy",
                dnac_password="dummy",
                dnac_version="2.3.7.9",
                dnac_log=True,
                state="merged",
                config_verify=True,
                config=self.playbook_config_create_a_tag_with_device_port_rules_case_1,
            )
        )
        result = self.execute_module(changed=True, failed=False)
        self.assertEqual(
            result.get("msg"),
            "Tag 'ServersTag' has been created successfully in the Cisco Catalyst Center.",
        )

    def test_delete_a_tag_with_device_port_rules_case_2(self):

        set_module_args(
            dict(
                dnac_host="1.1.1.1",
                dnac_username="dummy",
                dnac_password="dummy",
                dnac_version="2.3.7.9",
                dnac_log=True,
                state="deleted",
                config_verify=True,
                config=self.playbook_config_delete_a_tag_with_device_port_rules_case_2,
            )
        )

        result = self.execute_module(changed=False, failed=True)
        self.assertEqual(
            result.get("msg"),
            "Failed to execute the task delete_tag with Task ID: 0195232e-717f-71b6-9d00-ce8a130c282d.",
        )

    def test_force_delete_a_tag_with_device_port_rules_case_3(self):

        set_module_args(
            dict(
                dnac_host="1.1.1.1",
                dnac_username="dummy",
                dnac_password="dummy",
                dnac_version="2.3.7.9",
                dnac_log=True,
                state="deleted",
                config_verify=True,
                config=self.playbook_config_force_delete_a_tag_with_device_port_rules_case_3,
            )
        )

        result = self.execute_module(changed=True, failed=False)
        self.assertEqual(
            result.get("msg"),
            (
                "Tag 'ServersTag' has been deleted successfully in the Cisco Catalyst Center.\n"
                "The Device with hostname: S2-VZA-Border-2.cisco.com has been untagged from ServersTag"
                "\nThe Device with hostname: S2-VZA-Border-1 has been untagged from ServersTag"
                "\nThe Interface TenGigabitEthernet1/0/11 of device with hostname: S2-VZA-Edge-1 has been untagged from ServersTag"
            ),
        )

    def test_update_scope_of_a_tag_with_only_port_rule(self):

        set_module_args(
            dict(
                dnac_host="1.1.1.1",
                dnac_username="dummy",
                dnac_password="dummy",
                dnac_version="2.3.7.9",
                dnac_log=True,
                state="merged",
                config_verify=True,
                config=self.playbook_config_update_scope_of_a_tag_with_only_port_rule,
            )
        )

        result = self.execute_module(changed=True, failed=False)
        self.assertEqual(
            result.get("msg"),
            "Tag 'ServersTag' has been updated successfully in the Cisco Catalyst Center.",
        )

    def test_update_scope_members_of_tag_with_device_ports_rules(self):

        set_module_args(
            dict(
                dnac_host="1.1.1.1",
                dnac_username="dummy",
                dnac_password="dummy",
                dnac_version="2.3.7.9",
                dnac_log=True,
                state="merged",
                config_verify=True,
                config=self.playbook_config_update_scope_members_of_tag_with_device_ports_rules,
            )
        )

        result = self.execute_module(changed=True, failed=False)
        self.assertEqual(
            result.get("msg"),
            "Tag 'ServersTag' has been updated successfully in the Cisco Catalyst Center.",
        )
