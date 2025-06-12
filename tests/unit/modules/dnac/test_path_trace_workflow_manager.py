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

from ansible_collections.cisco.dnac.plugins.modules import path_trace_workflow_manager
from .dnac_module import TestDnacModule, set_module_args, loadPlaybookData


class TestDnacPathTraceWorkflowManager(TestDnacModule):

    module = path_trace_workflow_manager

    test_data = loadPlaybookData("path_trace_workflow_manager")

    path_playbook_error_create = test_data.get("path_playbook_error_create")
    playbook_pathtrace_positive_create = test_data.get("playbook_pathtrace_positive_create")
    playbook_pathtrace_positive_delete = test_data.get("playbook_pathtrace_positive_delete")

    def setUp(self):
        super(TestDnacPathTraceWorkflowManager, self).setUp()

        self.mock_dnac_init = patch(
            "ansible_collections.cisco.dnac.plugins.module_utils.dnac.DNACSDK.__init__")
        self.run_dnac_init = self.mock_dnac_init.start()
        self.run_dnac_init.side_effect = [None]
        self.mock_dnac_exec = patch(
            "ansible_collections.cisco.dnac.plugins.module_utils.dnac.DNACSDK._exec"
        )
        self.run_dnac_exec = self.mock_dnac_exec.start()

    def tearDown(self):
        super(TestDnacPathTraceWorkflowManager, self).tearDown()
        self.mock_dnac_exec.stop()
        self.mock_dnac_init.stop()

    def load_fixtures(self, response=None, device=""):
        """
        Load fixtures for user.
        """

        if "path_playbook_error_create" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("retrieves_all_previous_pathtraces_summary"),
                self.test_data.get("retrieves_all_previous_pathtraces_summary_1"),
                self.test_data.get("path_trace_create"),
                self.test_data.get("retrieves_all_previous_pathtraces_summary_2"),
                self.test_data.get("get_path_trace"),
                self.test_data.get("get_path_trace_1"),
                self.test_data.get("get_path_trace_2"),
                self.test_data.get("path_trace_response")
            ]
        elif "playbook_pathtrace_positive_create" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("retrieves_all_previous_pathtraces_summary_10"),
                self.test_data.get("path_trace_create_10"),
                self.test_data.get("get path_trace_10"),
                self.test_data.get("get_path_trace_11"),
                self.test_data.get("path_trace_positive_response"),
            ]
        elif "playbook_pathtrace_positive_delete" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("retrieves_all_previous_pathtraces_20"),
                self.test_data.get("retrieves_all_previous_pathtraces_summary_20"),
                self.test_data.get("delete_path_trace"),
                self.test_data.get("TaskDetails"),
                self.test_data.get("retrieves_all_previous_pathtraces_summary_21"),
                self.test_data.get("pathtrace_positive_delete_response"),
            ]

    def test_path_trace_workflow_manager_path_playbook_error_create(self):
        """
        Test the error handling during the path trace creation.

        This test verifies that the workflow correctly handles errors during the creation
        of a new path trace, ensuring proper validation and the expected behavior in case of errors.
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
                config=self.path_playbook_error_create
            )
        )
        result = self.execute_module(changed=False, failed=True)
        print(result)
        self.assertEqual(
            result.get("response"),
            "An error occurred during get path trace: "
        )

    def test_path_trace_workflow_manager_playbook_pathtrace_positive_create(self):
        """
        Test the successful creation of a path trace.

        This test verifies that the workflow correctly handles the creation of a new
        path trace, ensuring proper validation, correct behavior, and successful completion
        of the creation process.
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
                config=self.playbook_pathtrace_positive_create
            )
        )
        result = self.execute_module(changed=True, failed=False)
        self.maxDiff = None
        self.assertEqual(
            result.get("msg"),
            "Path trace created and verified successfully for '[{'source_ip': '204.1.216.29', " +
            "'dest_ip': '204.1.216.33', 'protocol': 'TCP', 'periodic_refresh': False, " +
            "'include_stats': ['DEVICE_STATS', 'INTERFACE_STATS', " +
            "'QOS_STATS', 'PERFORMANCE_STATS'], 'flow_analysis_id': '75da3867-1e08-4661-9f4e-f8e2740b71b5'}]'."
        )

    def test_path_trace_workflow_manager_playbook_pathtrace_positive_delete(self):
        """
        Test the successful deletion of a path trace.

        This test verifies that the workflow correctly handles the deletion of a new
        path trace, ensuring proper validation, correct behavior, and successful completion
        of the deletion process.
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
                config=self.playbook_pathtrace_positive_delete
            )
        )
        result = self.execute_module(changed=True, failed=False)
        print(result)
        self.assertEqual(
            result.get("msg"),
            "Path trace deleted and verified successfully for '[{'source_ip': '204.1.216.29', " +
            "'dest_ip': '204.1.216.33', 'protocol': 'TCP', 'periodic_refresh': False, " +
            "'include_stats': ['DEVICE_STATS', 'INTERFACE_STATS', 'QOS_STATS', 'PERFORMANCE_STATS']}]'."
        )
