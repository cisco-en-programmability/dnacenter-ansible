# Copyright (c) 2025 Cisco and/or its affiliates.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# You may not use this file except in compliance with the License.
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
#   Mohamed Rafeek  <md.rafeek@gmail.com>
#
# Description:
#   Unit tests for the Ansible module `accesspoint_location_workflow_manager`.
#   These tests cover various access point planned location operations such as creation,
#   update, deletion and assignment logic using mocked Catalyst Center responses.

from __future__ import absolute_import, division, print_function

__metaclass__ = type
from unittest.mock import patch
from ansible_collections.cisco.dnac.plugins.modules import accesspoint_location_workflow_manager
from .dnac_module import TestDnacModule, set_module_args, loadPlaybookData


class TestDnacAccessPointLocationWorkflow(TestDnacModule):

    module = accesspoint_location_workflow_manager
    test_data = loadPlaybookData("accesspoint_location_workflow_manager")

    playbook_config_create_ap_location = test_data.get("create_ap_location")
    playbook_config_update_ap_location = test_data.get("update_ap_location")
    playbook_config_delete_ap_location = test_data.get("delete_ap_location")
    playbook_config_create_assign_ap_location = test_data.get("create_assign_ap_location")

    def setUp(self):
        super(TestDnacAccessPointLocationWorkflow, self).setUp()
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
        super(TestDnacAccessPointLocationWorkflow, self).tearDown()
        self.mock_dnac_exec.stop()
        self.mock_dnac_init.stop()

    def load_fixtures(self, response=None, device=""):
        """
        Load fixtures for user.
        """
        if "test_create_ap_location" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("get_site_floor_response"),
                self.test_data.get("ap_antenna_patterns_response"),
                self.test_data.get("get_planned_location_not_exist"),
                self.test_data.get("get_planned_location_not_exist"),
                self.test_data.get("create_planned_location_task_id"),
                self.test_data.get("create_planned_location_task_details"),
                self.test_data.get("create_planned_location_task_stats")
            ]
        elif "test_update_ap_location" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("get_site_floor_response"),
                self.test_data.get("ap_antenna_patterns_response"),
                self.test_data.get("get_planned_location_exist"),
                self.test_data.get("create_planned_location_task_id"),
                self.test_data.get("create_planned_location_task_details"),
                self.test_data.get("create_planned_location_task_stats")
            ]
        elif "test_delete_ap_location" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("get_site_floor_response"),
                self.test_data.get("ap_antenna_patterns_response"),
                self.test_data.get("get_planned_location_exist"),
                self.test_data.get("create_planned_location_task_id"),
                self.test_data.get("create_planned_location_task_details"),
                self.test_data.get("delete_ap_location_task_status")
            ]
        elif "test_create_assign_ap_location" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("get_site_floor_response"),
                self.test_data.get("ap_antenna_patterns_response"),
                self.test_data.get("get_planned_location_not_exist"),
                self.test_data.get("get_planned_location_not_exist"),
                self.test_data.get("get_ap_device_details"),
                self.test_data.get("create_planned_location_task_id"),
                self.test_data.get("create_planned_location_task_details"),
                self.test_data.get("create_planned_location_task_stats"),
                self.test_data.get("get_planned_location_exist"),
                self.test_data.get("create_planned_location_task_id"),
                self.test_data.get("create_planned_location_task_details"),
                self.test_data.get("assign_task_status")
            ]

    def test_create_ap_location(self):
        set_module_args(
            dict(
                dnac_host="1.1.1.1",
                dnac_username="dummy",
                dnac_password="dummy",
                dnac_version="3.1.3.0",
                dnac_log=True,
                config_verify=True,
                state="merged",
                config=self.playbook_config_create_ap_location,
            )
        )
        result = self.execute_module(changed=True, failed=False)
        self.assertIn(
            "Access point positions created successfully",
            result.get('msg')
        )

    def test_update_ap_location(self):
        set_module_args(
            dict(
                dnac_host="1.1.1.1",
                dnac_username="dummy",
                dnac_password="dummy",
                dnac_version="3.1.3.0",
                dnac_log=True,
                state="merged",
                config_verify=True,
                config=self.playbook_config_update_ap_location,
            )
        )
        result = self.execute_module(changed=True, failed=False)
        self.assertIn(
            "updated successfully",
            result.get('msg')
        )

    def test_delete_ap_location(self):
        set_module_args(
            dict(
                dnac_host="1.1.1.1",
                dnac_username="dummy",
                dnac_password="dummy",
                dnac_version="3.1.3.0",
                dnac_log=True,
                state="deleted",
                config_verify=True,
                config=self.playbook_config_delete_ap_location,
            )
        )
        result = self.execute_module(changed=True, failed=False)
        self.assertIn(
            "Access point positions deleted and verified successfully: IAC-TB4-SJ-AP1",
            result.get('msg')
        )

    def test_create_assign_ap_location(self):
        set_module_args(
            dict(
                dnac_host="1.1.1.1",
                dnac_username="dummy",
                dnac_password="dummy",
                dnac_version="3.1.3.0",
                dnac_log=True,
                state="merged",
                config_verify=True,
                config=self.playbook_config_create_assign_ap_location,
            )
        )
        result = self.execute_module(changed=False, failed=True)
        self.assertIn(
            "Given accesspoint name not available in planned positions",
            result.get('msg')
        )
