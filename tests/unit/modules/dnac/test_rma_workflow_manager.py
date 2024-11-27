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

from ansible_collections.cisco.dnac.plugins.modules import rma_workflow_manager
from .dnac_module import TestDnacModule, set_module_args, loadPlaybookData


class TestDnacRmaIntent(TestDnacModule):
    module = rma_workflow_manager

    test_data = loadPlaybookData("rma_workflow_manager")

    playbook_config_valid = test_data.get("playbook_config_valid")
    playbook_config_device_name = test_data.get("playbook_config_device_name")
    playbook_config_serial_number = test_data.get("playbook_config_serial_number")
    playbook_config_device_not_found = test_data.get("playbook_config_device_not_found")
    playbook_config_faulty_device_not_found = test_data.get("playbook_config_faulty_device_not_found")
    playbook_invalid_serial = test_data.get("playbook_invalid_serial")
    playbook_config_exception = test_data.get("playbook_config_exception")
    playbook_config_invalid_params = test_data.get("playbook_config_invalid_params")
    playbook_invalid_config = test_data.get("playbook_invalid_config")

    def setUp(self):
        super(TestDnacRmaIntent, self).setUp()

        self.mock_dnac_init = patch(
            "ansible_collections.cisco.dnac.plugins.module_utils.dnac.DNACSDK.__init__")
        self.run_dnac_init = self.mock_dnac_init.start()
        self.run_dnac_init.side_effect = [None]

        self.mock_dnac_exec = patch(
            "ansible_collections.cisco.dnac.plugins.module_utils.dnac.DNACSDK._exec"
        )
        self.run_dnac_exec = self.mock_dnac_exec.start()

    def tearDown(self):
        super(TestDnacRmaIntent, self).tearDown()
        self.mock_dnac_exec.stop()
        self.mock_dnac_init.stop()

    def load_fixtures(self, response=None, device=""):
        if "invalid_serial" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("get_device_invalid_serial")
            ]
        elif "device_no_config" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("get_device_no_config")
            ]
        elif "no_valid_device_info_in_config" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("get_valid_device_info_in_config")
            ]
        elif "replacement_device_not_found" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("get_device_list_response_faulty"),
                self.test_data.get("get_device_replacement_response")
            ]
        elif "invalid_params_in_playbook" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("get_invalid_params_in_playbook")
            ]
        elif "mark_device_for_replacement_exception" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("get_device_list_response_faulty"),
                self.test_data.get("get_device_list_response_replacement"),
                self.test_data.get("get_mark_device_exception")
            ]
        elif "faulty_device_not_found" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("get_device_list_empty_response"),
                self.test_data.get("get_faulty_device_exception")
            ]
        elif "mark_device_failure" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("get_device_list_response_faulty"),
                self.test_data.get("get_device_list_response_replacement"),
                self.test_data.get("mark_device_for_replacement_response"),
                self.test_data.get("get_task_details_failure")
            ]
        elif "deploy_workflow_success" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("get_device_list_response_faulty"),
                self.test_data.get("get_device_list_response_replacement"),
                self.test_data.get("mark_device_for_replacement_response"),
                self.test_data.get("get_task_details_mark_success"),
                self.test_data.get("deploy_device_replacement_response"),
                self.test_data.get("get_task_details_deploy_in_progress"),
                self.test_data.get("get_task_details_deploy_success"),
                self.test_data.get("get_task_details_deploy_success_status")
            ]
        elif "deploy_workflow_failure_unmark_failure" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("get_device_list_response_faulty"),
                self.test_data.get("get_device_list_response_replacement"),
                self.test_data.get("mark_device_for_replacement_response"),
                self.test_data.get("get_task_details_mark_success"),
                self.test_data.get("deploy_device_replacement_response"),
                self.test_data.get("get_task_details_deploy_in_progress"),
                self.test_data.get("get_task_details_failure"),
                self.test_data.get("unmark_device_for_replacement_response"),
                self.test_data.get("get_task_details_unmark_failure"),
                self.test_data.get("get_task_details_unmark_failure_status")
            ]
        elif "deploy_workflow_failure_unmark_success" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("get_device_list_response_faulty"),
                self.test_data.get("get_device_list_response_replacement"),
                self.test_data.get("mark_device_for_replacement_response"),
                self.test_data.get("get_task_details_mark_success"),
                self.test_data.get("deploy_device_replacement_response"),
                self.test_data.get("get_task_details_failure"),
                self.test_data.get("unmark_device_for_replacement_response"),
                self.test_data.get("get_task_details_unmark_success"),
                self.test_data.get("get_task_details_unmark_success_status")
            ]

    def test_rma_workflow_manager_invalid_serial(self):
        set_module_args(
            dict(
                dnac_host="1.1.1.1",
                dnac_username="dummy",
                dnac_password="dummy",
                dnac_log=True,
                state="replaced",
                config=self.playbook_invalid_serial
            )
        )
        result = self.execute_module(changed=False, failed=True)
        print(result)
        self.assertEqual(
            result.get('msg'),
            "Invalid parameters in playbook config: 'faulty_device_serial_number: Invalid Serial Number 'FJC2327U0S2YZ' in playbook.' "
        )

    def test_rma_workflow_manager_device_no_config(self):
        set_module_args(
            dict(
                dnac_host="1.1.1.1",
                dnac_username="dummy",
                dnac_password="dummy",
                dnac_log=True,
                state="replaced",
                config=self.playbook_config_exception
            )
        )
        result = self.execute_module(changed=False, failed=True)
        print(result)
        self.assertEqual(
            result.get('msg'),
            "Invalid or missing 'want' dictionary"
        )

    def test_rma_workflow_manager_no_valid_device_info_in_config(self):
        set_module_args(
            dict(
                dnac_host="1.1.1.1",
                dnac_username="dummy",
                dnac_password="dummy",
                dnac_log=True,
                state="replaced",
                config=self.playbook_invalid_config
            )
        )
        result = self.execute_module(changed=False, failed=True)
        print(result)
        self.assertEqual(
            result.get('msg'),
            "No valid device combination found in config. Provided values in config: {}"
        )

    def test_rma_workflow_manager_faulty_device_not_found(self):
        set_module_args(
            dict(
                dnac_host="1.1.1.1",
                dnac_username="dummy",
                dnac_password="dummy",
                dnac_log=True,
                state="replaced",
                config=self.playbook_config_faulty_device_not_found
            )
        )
        result = self.execute_module(changed=False, failed=True)
        print(result)
        self.assertEqual(
            result.get('msg'),
            "Faulty device '204.1.2.19' not found in Cisco Catalyst Center"
        )

    def test_rma_workflow_manager_replacement_device_not_found(self):
        set_module_args(
            dict(
                dnac_host="1.1.1.1",
                dnac_username="dummy",
                dnac_password="dummy",
                dnac_log=True,
                state="replaced",
                config=self.playbook_config_device_not_found
            )
        )
        result = self.execute_module(changed=False, failed=True)
        print(result)
        self.assertEqual(
            result.get('msg'),
            "Replacement device '204.1.2.19' not found in Cisco Catalyst Center"
        )

    def test_rma_workflow_manager_invalid_params_in_playbook(self):
        set_module_args(
            dict(
                dnac_host="1.1.1.1",
                dnac_username="dummy",
                dnac_password="dummy",
                dnac_log=True,
                state="replaced",
                config=self.playbook_config_invalid_params
            )
        )
        result = self.execute_module(changed=False, failed=True)
        print(result)
        self.assertEqual(
            result.get('msg'),
            "Invalid parameters in playbook config: 'faulty_device_ip_address: Invalid IP Address '204.1.2.9T' in playbook' "
        )

    def test_rma_workflow_manager_mark_device_for_replacement_exception(self):
        set_module_args(
            dict(
                dnac_host="1.1.1.1",
                dnac_username="dummy",
                dnac_password="dummy",
                dnac_log=True,
                state="replaced",
                config=self.playbook_config_valid
            )
        )
        result = self.execute_module(changed=False, failed=True)
        print(result)
        self.assertEqual(
            result.get('msg'),
            "Exception occurred while marking device for replacement: "
        )

    def test_rma_workflow_manager_mark_device_failure(self):
        set_module_args(
            dict(
                dnac_host="1.1.1.1",
                dnac_username="dummy",
                dnac_password="dummy",
                dnac_log=True,
                state="replaced",
                config=self.playbook_config_valid
            )
        )
        result = self.execute_module(changed=False, failed=True)
        print(result)
        self.assertEqual(
            result.get('msg'),
            "An error occurred during the operation"
        )

    def test_rma_workflow_manager_deploy_workflow_success(self):
        set_module_args(
            dict(
                dnac_host="1.1.1.1",
                dnac_username="dummy",
                dnac_password="dummy",
                dnac_log=True,
                state="replaced",
                config=self.playbook_config_valid
            )
        )
        result = self.execute_module(changed=True, failed=False)
        print(result)
        self.assertEqual(
            result.get('msg'),
            "Device replacement completed successfully: RMA deploy workflow with workflowId fff0de41-4f7f-48bb-8cf4-14703a684009 is completed successfully."
        )

    def test_rma_workflow_manager_deploy_workflow_failure_unmark_failure(self):
        set_module_args(
            dict(
                dnac_host="1.1.1.1",
                dnac_username="dummy",
                dnac_password="dummy",
                dnac_log=True,
                state="replaced",
                config=self.playbook_config_valid
            )
        )
        result = self.execute_module(changed=False, failed=True)
        print(result)
        self.assertEqual(
            result.get('msg'),
            "Error while unmarking device for replacement: Task failed. | Unmarking result: Error while unmarking device for replacement: Task failed."
        )

    def test_rma_workflow_manager_deploy_workflow_failure_unmark_success(self):
        set_module_args(
            dict(
                dnac_host="1.1.1.1",
                dnac_username="dummy",
                dnac_password="dummy",
                dnac_log=True,
                state="replaced",
                config=self.playbook_config_valid
            )
        )
        result = self.execute_module(changed=True, failed=False)
        print(result)
        self.assertEqual(
            result.get('msg'),
            "Device replacement task failed: An error occurred during the operation | Unmarking result: Device(s) Unmarked For Replacement successfully."
        )
