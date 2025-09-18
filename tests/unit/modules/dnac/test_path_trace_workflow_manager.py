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
            # "An error occurred during create path trace: "
            "Path trace created successfully for '[{'request': {'sourceIP': '204.1.2.3', 'sourcePort': '4020', 'destIP': " +
            "'204.1.2.4', 'destPort': '4021', 'protocol': 'TCP', 'periodicRefresh': False, " +
            "'id': 'd5a39a16-2e8f-425d-b5d4-38f97aeff066', 'status': 'COMPLETED', 'createTime': 1743740457394," +
            " 'lastUpdateTime': 1743740458591, 'controlPath': False}, 'lastUpdate': 'Fri Apr 04 04:21:00 GMT 2025', " +
            "'networkElementsInfo': [{'id': 'e62e6405-13e4-4f1b-ae1c-580a28a96a88', 'name': 'SJ-BN-9301', 'type': " +
            "'Switches and Hubs', 'ip': '204.1.2.3', 'egressInterface': {'physicalInterface': " +
            "{'id': 'b65f159e-b67d-49d4-92d0-801a0eda6426', 'name': 'TenGigabitEthernet1/1/7', 'vrfName': 'global', " +
            "'usedVlan': 'NA'}}, 'role': 'DISTRIBUTION', 'linkInformationSource': 'ISIS'}, {'id': " +
            "'820bd13a-f565-4778-a320-9ec9f23b4725', 'name': 'DC-T-9300', 'type': 'Switches and Hubs', 'ip': " +
            "'204.1.1.22', 'ingressInterface': {'physicalInterface': {'id': 'c98d09f3-b57e-468f-a9a1-65e75249e94f', " +
            "'name': 'TenGigabitEthernet1/1/8', 'vrfName': 'global', 'usedVlan': 'NA'}}, 'egressInterface': " +
            "{'physicalInterface': {'id': '2897a064-9079-4c9c-adf2-3e0b5cf22724', 'name': 'TenGigabitEthernet1/1/7', " +
            "'vrfName': 'global', 'usedVlan': 'NA'}}, 'role': 'ACCESS', 'linkInformationSource': 'ISIS'}, {'id': " +
            "'0be10e21-34c7-4c76-b217-56327ed1f418', 'name': 'NY-BN-9300', 'type': 'Switches and Hubs', 'ip': '204.1.2.4', " +
            "'ingressInterface': {'physicalInterface': {'id': 'f24b433c-8388-453e-a034-fcaf516bc749', 'name': " +
            "'TenGigabitEthernet2/1/8', 'vrfName': 'global', 'usedVlan': 'NA'}}, 'role': 'DISTRIBUTION'}]}, {'request': " +
            "{'sourceIP': '204.1.1.2', 'destIP': '204.1.2.4', 'periodicRefresh': False, 'id': " +
            "'da08dbb7-86d5-4b69-adab-d83c322265a9', 'status': 'COMPLETED', 'createTime': 1743740260451, 'lastUpdateTime': " +
            "1743740261793, 'controlPath': False}, 'lastUpdate': 'Fri Apr 04 04:21:00 GMT 2025', 'networkElementsInfo': " +
            "[{'id': '99b62ead-51d6-4bfc-9b0c-dab087f184e9', 'name': 'SJ-BN-9301', 'type': 'Switches and Hubs', 'ip': " +
            "'204.1.1.2', 'egressInterface': {'physicalInterface': {'id': '44aafd2d-5822-4ce5-95c5-11909e9425f6', 'name': " +
            "'TenGigabitEthernet1/1/1', 'vrfName': 'global', 'usedVlan': 'NA'}}, 'role': 'ACCESS', 'linkInformationSource': " +
            "'ISIS'}, {'id': 'e62e6405-13e4-4f1b-ae1c-580a28a96a88', 'name': 'SJ-BN-9301', 'type': 'Switches and Hubs', " +
            "'ip': '204.1.2.3', 'ingressInterface': {'physicalInterface': {'id': '0610f80e-09fc-4083-8aaa-7cf318b211de', " +
            "'name': 'TenGigabitEthernet1/1/2', 'vrfName': 'global', 'usedVlan': 'NA'}}, 'egressInterface': " +
            "{'physicalInterface': {'id': 'b65f159e-b67d-49d4-92d0-801a0eda6426', 'name': 'TenGigabitEthernet1/1/7', " +
            "'vrfName': 'global', 'usedVlan': 'NA'}}, 'role': 'DISTRIBUTION', 'linkInformationSource': 'ISIS'}, " +
            "{'id': '820bd13a-f565-4778-a320-9ec9f23b4725', 'name': 'DC-T-9300', 'type': 'Switches and Hubs', " +
            "'ip': '204.1.1.22', 'ingressInterface': {'physicalInterface': {'id': 'c98d09f3-b57e-468f-a9a1-65e75249e94f', " +
            "'name': 'TenGigabitEthernet1/1/8', 'vrfName': 'global', 'usedVlan': 'NA'}}, 'egressInterface': " +
            "{'physicalInterface': {'id': '2897a064-9079-4c9c-adf2-3e0b5cf22724', 'name': 'TenGigabitEthernet1/1/7', " +
            "'vrfName': 'global', 'usedVlan': 'NA'}}, 'role': 'ACCESS', 'linkInformationSource': 'ISIS'}, {'id': " +
            "'0be10e21-34c7-4c76-b217-56327ed1f418', 'name': 'NY-BN-9300', 'type': 'Switches and Hubs', 'ip': " +
            "'204.1.2.4', 'ingressInterface': {'physicalInterface': {'id': 'f24b433c-8388-453e-a034-fcaf516bc749', " +
            "'name': 'TenGigabitEthernet2/1/8', 'vrfName': 'global', 'usedVlan': 'NA'}}, 'role': 'DISTRIBUTION'}]}]'. " +
            "Unable to create the following path '['9e7f5c5b-58b7-4bcd-8771-021629f076b3', {'flow_analysis_id': " +
            "'9e7f5c5b-58b7-4bcd-8771-021629f076b3', 'delete_on_completion': True}]'."
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
