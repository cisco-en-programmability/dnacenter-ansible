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

# Make coding more python3-ish
from __future__ import absolute_import, division, print_function

__metaclass__ = type
from unittest.mock import patch
from ansible_collections.cisco.dnac.plugins.modules import sda_extranet_policies_workflow_manager
from .dnac_module import TestDnacModule, set_module_args, loadPlaybookData


class SDAExtranetPolicies(TestDnacModule):

    module = sda_extranet_policies_workflow_manager

    test_data = loadPlaybookData("sda_extranet_policies_workflow_manager_intent")

    def setUp(self):
        super(SDAExtranetPolicies, self).setUp()

        self.mock_dnac_init = patch(
            "ansible_collections.cisco.dnac.plugins.module_utils.dnac.DNACSDK.__init__")
        self.run_dnac_init = self.mock_dnac_init.start()
        self.run_dnac_init.side_effect = [None]
        self.mock_dnac_exec = patch(
            "ansible_collections.cisco.dnac.plugins.module_utils.dnac.DNACSDK._exec"
        )
        self.run_dnac_exec = self.mock_dnac_exec.start()
        print(f"Mock for DNACSDK._exec: {self.run_dnac_exec}")

    def tearDown(self):
        super(SDAExtranetPolicies, self).tearDown()
        self.mock_dnac_init.stop()
        self.mock_dnac_exec.stop()

    def load_fixtures(self, response=None, device=""):
        print("Inside load_fixtures")

        # FIXTURE FOR SUCCESS TESTCASES ############################################################

        if "create_sda_extranet_policies" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("response_get_extranet_policies_1"),
                self.test_data.get("response_get_sites"),
                self.test_data.get("response_get_fabric_sites"),
                self.test_data.get("response_get_task_id"),
                self.test_data.get("response_get_task_status_by_id"),
                self.test_data.get("response_get_extranet_policies_2"),
            ]

        if "update_sda_extranet_policies" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("response_get_extranet_policies_2"),
                self.test_data.get("response_get_sites"),
                self.test_data.get("response_get_fabric_sites"),
                self.test_data.get("response_get_task_id"),
                self.test_data.get("response_get_task_status_by_id"),
                self.test_data.get("response_get_extranet_policies_3"),
            ]

        if "delete_sda_extranet_policies" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("response_get_extranet_policies_3"),
                self.test_data.get("response_get_task_id"),
                self.test_data.get("response_get_task_status_by_id"),
                self.test_data.get("response_get_extranet_policies_1"),
            ]
        # FIXTURES FOR FAILURE TESTCASES ############################################################

        if "create_sda_extranet_policies_failure_1" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                Exception("Simulated exception")
            ]

        if "create_sda_extranet_policies_failure_2" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("response_get_extranet_policies_1"),
                Exception("Simulated exception")
            ]

        if "create_sda_extranet_policies_failure_3" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("response_get_extranet_policies_1"),
                self.test_data.get("response_get_sites"),
                Exception("Simulated exception")
            ]

        if "create_sda_extranet_policies_failure_4" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("response_get_extranet_policies_1"),
                self.test_data.get("response_get_sites"),
                self.test_data.get("response_get_fabric_sites"),
                Exception("Simulated exception")
            ]

        if "create_sda_extranet_policies_failure_5" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("response_get_extranet_policies_1"),
                self.test_data.get("response_get_sites"),
                self.test_data.get("response_get_fabric_sites"),
                self.test_data.get("response_get_task_id"),
                Exception("Simulated exception")
            ]

        if "create_sda_extranet_policies_failure_6" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("response_get_extranet_policies_1"),
                self.test_data.get("response_get_sites"),
                self.test_data.get("response_get_fabric_sites"),
                self.test_data.get("response_get_task_id"),
                self.test_data.get("response_get_task_status_by_id"),
                Exception("Simulated exception")
            ]

        if "update_sda_extranet_policies_failure_1" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("response_get_extranet_policies_2"),
                self.test_data.get("response_get_sites"),
                self.test_data.get("response_get_fabric_sites"),
                Exception("Simulated exception")
            ]

        if "delete_sda_extranet_policies_failure_1" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                Exception("Simulated exception")
            ]

        if "delete_sda_extranet_policies_failure_2" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("response_get_extranet_policies_3"),
                Exception("Simulated exception")
            ]

        if "delete_sda_extranet_policies_failure_3" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("response_get_extranet_policies_3"),
                self.test_data.get("response_get_task_id"),
                Exception("Simulated exception")
            ]

        if "delete_sda_extranet_policies_failure_4" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("response_get_extranet_policies_3"),
                self.test_data.get("response_get_task_id"),
                self.test_data.get("response_get_task_status_by_id"),
                Exception("Simulated exception")
            ]

# SUCCESS TESTCASES ########################################################################################

    def test_create_sda_extranet_policies(self):
        print("Test Data: {test_data}".format(test_data=self.test_data.get("playbook_config_create_sda_extranet_policies")))

        set_module_args(
            dict(
                dnac_host="1.1.1.1",
                dnac_username="dummy",
                dnac_password="dummy",
                dnac_log=False,
                dnac_log_level="DEBUG",
                dnac_version="2.3.7.9",
                config_verify=True,
                dnac_log_append=False,
                state="merged",
                config=self.test_data.get("playbook_config_create_sda_extranet_policies"),
            )
        )
        result = self.execute_module(changed=True, failed=False)
        self.assertIn(
            "Add Extranet Policy Task Succeeded for the Extranet Policy",
            result.get("msg"),
        )

    def test_update_sda_extranet_policies(self):
        print("Test Data: {test_data}".format(test_data=self.test_data.get("playbook_config_update_sda_extranet_policies")))

        set_module_args(
            dict(
                dnac_host="1.1.1.1",
                dnac_username="dummy",
                dnac_password="dummy",
                dnac_log=False,
                dnac_log_level="DEBUG",
                dnac_version="2.3.7.9",
                config_verify=True,
                dnac_log_append=False,
                state="merged",
                config=self.test_data.get("playbook_config_update_sda_extranet_policies"),
            )
        )
        result = self.execute_module(changed=True, failed=False)
        self.assertIn(
            "Update Extranet Policy Task Succeeded for following Extranet Policy",
            result.get("msg"),
        )

    def test_delete_sda_extranet_policies(self):
        print("Test Data: {test_data}".format(test_data=self.test_data.get("playbook_config_delete_sda_extranet_policies")))

        set_module_args(
            dict(
                dnac_host="1.1.1.1",
                dnac_username="dummy",
                dnac_password="dummy",
                dnac_log=False,
                dnac_log_level="DEBUG",
                dnac_version="2.3.7.9",
                config_verify=True,
                dnac_log_append=False,
                state="deleted",
                config=self.test_data.get("playbook_config_delete_sda_extranet_policies"),
            )
        )
        result = self.execute_module(changed=True, failed=False)
        self.assertIn(
            "Delete Extranet Policy Task Succeeded for following Extranet Policy",
            result.get("msg"),
        )

# FAILURE TESTCASES ########################################################################################

    def test_create_sda_extranet_policies_failure_1(self):
        print("Test Data: {test_data}".format(test_data=self.test_data.get("playbook_config_create_sda_extranet_policies")))

        set_module_args(
            dict(
                dnac_host="1.1.1.1",
                dnac_username="dummy",
                dnac_password="dummy",
                dnac_log=False,
                dnac_log_level="DEBUG",
                dnac_version="2.3.7.9",
                config_verify=True,
                dnac_log_append=False,
                state="merged",
                config=self.test_data.get("playbook_config_create_sda_extranet_policies"),
            )
        )
        result = self.execute_module(changed=False, failed=True)
        self.assertIn(
            "An error occurred while retrieving Extranet Policy Details:",
            result.get("msg"),
        )

    def test_create_sda_extranet_policies_failure_2(self):
        print("Test Data: {test_data}".format(test_data=self.test_data.get("playbook_config_create_sda_extranet_policies")))

        set_module_args(
            dict(
                dnac_host="1.1.1.1",
                dnac_username="dummy",
                dnac_password="dummy",
                dnac_log=False,
                dnac_log_level="DEBUG",
                dnac_version="2.3.7.9",
                config_verify=True,
                dnac_log_append=False,
                state="merged",
                config=self.test_data.get("playbook_config_create_sda_extranet_policies"),
            )
        )
        result = self.execute_module(changed=False, failed=True)
        self.assertIn(
            "An exception occurred while retrieving Site details for Site",
            result.get("msg"),
        )

    def test_create_sda_extranet_policies_failure_3(self):
        print("Test Data: {test_data}".format(test_data=self.test_data.get("playbook_config_create_sda_extranet_policies")))

        set_module_args(
            dict(
                dnac_host="1.1.1.1",
                dnac_username="dummy",
                dnac_password="dummy",
                dnac_log=False,
                dnac_log_level="DEBUG",
                dnac_version="2.3.7.9",
                config_verify=True,
                dnac_log_append=False,
                state="merged",
                config=self.test_data.get("playbook_config_create_sda_extranet_policies"),
            )
        )
        result = self.execute_module(changed=False, failed=True)
        self.assertIn(
            "An error occurred while retrieving fabric Site 'Id' for Site",
            result.get("msg"),
        )

    def test_create_sda_extranet_policies_failure_4(self):
        print("Test Data: {test_data}".format(test_data=self.test_data.get("playbook_config_create_sda_extranet_policies")))

        set_module_args(
            dict(
                dnac_host="1.1.1.1",
                dnac_username="dummy",
                dnac_password="dummy",
                dnac_log=False,
                dnac_log_level="DEBUG",
                dnac_version="2.3.7.9",
                config_verify=True,
                dnac_log_append=False,
                state="merged",
                config=self.test_data.get("playbook_config_create_sda_extranet_policies"),
            )
        )
        result = self.execute_module(changed=False, failed=True)
        self.assertIn(
            "An error occurred while executing API call to Function: 'add_extranet_policy'",
            result.get("msg"),
        )

    def test_create_sda_extranet_policies_failure_5(self):
        print("Test Data: {test_data}".format(test_data=self.test_data.get("playbook_config_create_sda_extranet_policies")))

        set_module_args(
            dict(
                dnac_host="1.1.1.1",
                dnac_username="dummy",
                dnac_password="dummy",
                dnac_log=False,
                dnac_log_level="DEBUG",
                dnac_version="2.3.7.9",
                config_verify=True,
                dnac_log_append=False,
                state="merged",
                config=self.test_data.get("playbook_config_create_sda_extranet_policies"),
            )
        )
        result = self.execute_module(changed=False, failed=True)
        self.assertIn(
            "An error occurred while executing API call to Function: 'get_tasks_by_id'",
            result.get("msg"),
        )

    def test_create_sda_extranet_policies_failure_6(self):
        print("Test Data: {test_data}".format(test_data=self.test_data.get("playbook_config_create_sda_extranet_policies")))

        set_module_args(
            dict(
                dnac_host="1.1.1.1",
                dnac_username="dummy",
                dnac_password="dummy",
                dnac_log=False,
                dnac_log_level="DEBUG",
                dnac_version="2.3.7.9",
                config_verify=True,
                dnac_log_append=False,
                state="merged",
                config=self.test_data.get("playbook_config_create_sda_extranet_policies"),
            )
        )
        result = self.execute_module(changed=False, failed=True)
        self.assertIn(
            "An error occurred while retrieving Extranet Policy Details",
            result.get("msg"),
        )

    def test_update_sda_extranet_policies_failure_1(self):
        print("Test Data: {test_data}".format(test_data=self.test_data.get("playbook_config_update_sda_extranet_policies")))

        set_module_args(
            dict(
                dnac_host="1.1.1.1",
                dnac_username="dummy",
                dnac_password="dummy",
                dnac_log=False,
                dnac_log_level="DEBUG",
                dnac_version="2.3.7.9",
                config_verify=True,
                dnac_log_append=False,
                state="merged",
                config=self.test_data.get("playbook_config_update_sda_extranet_policies"),
            )
        )
        result = self.execute_module(changed=False, failed=True)
        self.assertIn(
            "An error occurred while executing API call to Function: 'update_extranet_policy'",
            result.get("msg"),
        )

    def test_delete_sda_extranet_policies_failure_1(self):
        print("Test Data: {test_data}".format(test_data=self.test_data.get("playbook_config_delete_sda_extranet_policies")))

        set_module_args(
            dict(
                dnac_host="1.1.1.1",
                dnac_username="dummy",
                dnac_password="dummy",
                dnac_log=False,
                dnac_log_level="DEBUG",
                dnac_version="2.3.7.9",
                config_verify=True,
                dnac_log_append=False,
                state="merged",
                config=self.test_data.get("playbook_config_delete_sda_extranet_policies"),
            )
        )
        result = self.execute_module(changed=False, failed=True)
        self.assertIn(
            "An error occurred while retrieving Extranet Policy Details: 'extranet_policy_1' usin",
            result.get("msg"),
        )

    def test_delete_sda_extranet_policies_failure_2(self):
        print("Test Data: {test_data}".format(test_data=self.test_data.get("playbook_config_delete_sda_extranet_policies")))

        set_module_args(
            dict(
                dnac_host="1.1.1.1",
                dnac_username="dummy",
                dnac_password="dummy",
                dnac_log=False,
                dnac_log_level="DEBUG",
                dnac_version="2.3.7.9",
                config_verify=True,
                dnac_log_append=False,
                state="merged",
                config=self.test_data.get("playbook_config_delete_sda_extranet_policies"),
            )
        )
        self.execute_module(changed=False, failed=True)

    def test_delete_sda_extranet_policies_failure_3(self):
        print("Test Data: {test_data}".format(test_data=self.test_data.get("playbook_config_delete_sda_extranet_policies")))

        set_module_args(
            dict(
                dnac_host="1.1.1.1",
                dnac_username="dummy",
                dnac_password="dummy",
                dnac_log=False,
                dnac_log_level="DEBUG",
                dnac_version="2.3.7.9",
                config_verify=True,
                dnac_log_append=False,
                state="merged",
                config=self.test_data.get("playbook_config_delete_sda_extranet_policies"),
            )
        )
        self.execute_module(changed=False, failed=True)

    def test_delete_sda_extranet_policies_failure_4(self):
        print("Test Data: {test_data}".format(test_data=self.test_data.get("playbook_config_delete_sda_extranet_policies")))

        set_module_args(
            dict(
                dnac_host="1.1.1.1",
                dnac_username="dummy",
                dnac_password="dummy",
                dnac_log=False,
                dnac_log_level="DEBUG",
                dnac_version="2.3.7.9",
                config_verify=True,
                dnac_log_append=False,
                state="merged",
                config=self.test_data.get("playbook_config_delete_sda_extranet_policies"),
            )
        )
        self.execute_module(changed=False, failed=True)
