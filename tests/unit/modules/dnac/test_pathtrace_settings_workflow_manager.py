# Copyright (c) 2024 Cisco and/or its affiliates.
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
from ansible_collections.cisco.dnac.plugins.modules import pathtrace_settings_workflow_manager
from .dnac_module import TestDnacModule, set_module_args, loadPlaybookData


class TestDnacPathTraceWorkflow(TestDnacModule):

    module = pathtrace_settings_workflow_manager
    test_data = loadPlaybookData("pathtrace_settings_workflow_manager")
    playbook_config_creation = test_data.get("playbook_config_creation")
    playbook_config_deletion = test_data.get("playbook_config_deletion")
    playbook_config_creation_invalid = test_data.get("playbook_config_creation_invalid")
    playbook_config_invalid_validation_input = test_data.get("playbook_config_invalid_validation_input")
    playbook_config_invalid_input = test_data.get("playbook_config_invalid_input")
    playbook_config_not_ipaddress = test_data.get("playbook_config_not_ipaddress")
    playbook_config_creation_with_flow_analaysis_id = test_data.get("playbook_config_creation_with_flow_analaysis_id")

    def setUp(self):
        super(TestDnacPathTraceWorkflow, self).setUp()

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
        super(TestDnacPathTraceWorkflow, self).tearDown()
        self.mock_dnac_exec.stop()
        self.mock_dnac_init.stop()

    def load_fixtures(self, response=None, device=""):
        """
        Load fixtures for user.
        """
        if "creation" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("get_path_trace"),
                self.test_data.get("get_path_trace"),
                self.test_data.get("create_path_trace"),
                self.test_data.get("get_pathtrace_api_response"),
                self.test_data.get("get_path_trace_with_flow_id"),
                self.test_data.get("get_path_trace_with_flow_id1"),
                self.test_data.get("get_path_trace_with_flow_id2"),
                self.test_data.get("get_path_trace_with_flow_id3"),
                self.test_data.get("get_path_trace_with_flow_id4"),
                self.test_data.get("received_path_trace"),
                self.test_data.get("pathtrace_created_successfully"),
            ]

        if "update_with_flow_analysis" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("get_path_trace_with_flow_analaysis"),
                self.test_data.get("get_path_trace_with_flow_analaysis1"),
                self.test_data.get("get_path_trace_with_flow_id5"),
                self.test_data.get("get_path_trace_with_flow_id6"),
                self.test_data.get("received_path_trace_details_1"),
                self.test_data.get("create_path_trace2"),
                self.test_data.get("get_path_trace_with_flow_id7"),
                self.test_data.get("get_path_trace_with_flow_id8"),
                self.test_data.get("get_path_trace_with_flow_id9"),
                self.test_data.get("received_path_trace_details_2"),
                self.test_data.get("get_path_trace"),
                self.test_data.get("get_path_trace")
            ]

        if "deletion" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("delete_get_path_trace"),
                self.test_data.get("retrieves_all_previous_pathtraces_summary"),
                self.test_data.get("deleted_get_path_trace_1"),
                self.test_data.get("delete_path_trace"),
                self.test_data.get("retrieves_all_previous_pathtraces_summary1"),
                self.test_data.get("deleted_get_path_trace_2"),
                self.test_data.get("delete_path_trace1"),
                self.test_data.get("delete_path_trace2"),
            ]

    def test_pathtrace_workflow_manager_creation(self):
        """
        Test case for path trace workflow manager when creating a path trace.

        This test case verifies the behavior of the path trace workflow manager when
        creating a new path trace in the specified DNAC instance.
        """
        set_module_args(
            dict(
                dnac_host="1.1.1.1",
                dnac_username="dummy",
                dnac_password="dummy",
                dnac_version="2.3.7.9",
                dnac_log=True,
                state="merged",
                config=self.playbook_config_creation
            )
        )
        result = self.execute_module(changed=True, failed=False)
        print(result)
        self.assertEqual(
            result.get('msg'),
            'An error occurred during create path trace: '
        )

    def test_pathtrace_workflow_manager_deletion(self):
        """"
        Test case for path trace workflow manager when deleting a path trace.

        This test case verifies the behavior of the path trace workflow manager when
        deleting an existing path trace in the specified DNAC instance.
        """
        set_module_args(
            dict(
                dnac_host="1.1.1.1",
                dnac_username="dummy",
                dnac_password="dummy",
                dnac_version="2.3.7.9",
                dnac_log=True,
                state="deleted",
                config=self.playbook_config_deletion
            )
        )
        result = self.execute_module(changed=True, failed=False)
        print(result)
        self.assertEqual(
            result('msg'),
            ""
        )

    def test_pathtrace_workflow_manager_update_verify(self):
        """
        Test case for path trace workflow manager when verifying an update.

        This test case checks the behavior of the path trace workflow manager
        when verifying the status of an update in the specified DNAC instance.
        """
        set_module_args(
            dict(
                dnac_host="1.1.1.1",
                dnac_username="dummy",
                dnac_password="dummy",
                dnac_version="2.3.7.9",
                dnac_log=True,
                state="merged",
                config_verify=True,
                config=self.playbook_config_creation
            )
        )
        result = self.execute_module(changed=True, failed=True)
        print(result)
        self.assertEqual(
            result['response'][0]['msg'],
            "An error occurred during get path trace for delete: Invalid input for JSON serialization: Object of type MagicMock is not JSON serializable"
        )

    def test_pathtrace_workflow_manager_invalid_feature(self):
        """
        Test case for path trace workflow manager when an invalid feature is provided.

        This test case verifies the behavior of the path trace workflow manager
        when an invalid feature is provided in the specified DNAC instance.
        """
        set_module_args(
            dict(
                dnac_host="1.1.1.1",
                dnac_username="dummy",
                dnac_password="dummy",
                dnac_log=True,
                state="merged",
                config=self.playbook_config_creation_invalid
            )
        )
        result = self.execute_module(changed=False, failed=True)
        print(result)
        self.assertEqual(
            result['msg'],
            "The specified version '2.2.3.3' does not support the path trace workflow feature.Supported version(s) start from '2.3.7.6' onwards."
        )

    def test_pathtrace_workflow_manager_invalid_creation(self):
        """
        Test case for path trace workflow manager when creating an invalid path trace.

        This test case verifies the behavior of the path trace workflow manager
        when attempting to create an invalid path trace in the specified DNAC instance.
        """
        set_module_args(
            dict(
                dnac_host="1.1.1.1",
                dnac_username="dummy",
                dnac_password="dummy",
                dnac_version="2.3.7.9",
                dnac_log=True,
                state="merged",
                config=self.playbook_config_creation
            )
        )
        result = self.execute_module(changed=False, failed=True)
        print(result)
        self.assertEqual(
            result.get['msg'],
            'An error occurred during create path trace: '
        )

    def test_tracepath_workflow_invalid_validate_input(self):

        """
        Test case to validate the behavior of the tracepath workflow when invalid input is provided.

        This test simulates the scenario where invalid input data is passed into the tracepath workflow
        function.
        """

        set_module_args(
            dict(
                dnac_host="1.1.1.1",
                dnac_username="dummy",
                dnac_password="dummy",
                dnac_log=True,
                state="merged",
                dnac_version="2.3.7.9",
                config=self.playbook_config_invalid_validation_input
            )
        )
        result = self.execute_module(changed=False, failed=True)
        self.assertEqual(
            result.get('msg'), "Playbook configuration is missing."
            # "Invalid parameters in playbook config: '['source_ip: Source IP Address is " +
            # "missing in playbook.', 'dest_ip: Destination IP Address is missing in playbook.']' "
        )

    def test_pathtrace_workflow_manager_creation_verification(self):
        """
        Test case for device credential workflow manager when creating a device credential.

        This test case checks the behavior of the device credential workflow manager when creating a new device credentials in the specified DNAC.
        """
        set_module_args(
            dict(
                dnac_host="1.1.1.1",
                dnac_username="dummy",
                dnac_password="dummy",
                dnac_version="2.3.7.9",
                dnac_log=True,
                state="merged",
                config=self.playbook_config_creation,
                config_verify=True
            )
        )
        result = self.execute_module(changed=True, failed=False)
        print(result)
        self.assertEqual(
            result.get('msg'),
            ''
        )

    def test_pathtrace_workflow_manager_deletion_verification(self):
        """"
        Test case for path trace workflow manager when deleting a path trace.

        This test case verifies the behavior of the path trace workflow manager when
        deleting an existing path trace in the specified DNAC instance.
        """
        set_module_args(
            dict(
                dnac_host="1.1.1.1",
                dnac_username="dummy",
                dnac_password="dummy",
                dnac_version="2.3.7.9",
                dnac_log=True,
                state="deleted",
                config_verify=True,
                config=self.playbook_config_deletion
            )
        )
        result = self.execute_module(changed=True, failed=False)
        print(result)
        self.assertEqual(
            result('msg'),
            ""
        )

    def test_device_credentials_workflow_manager_invalid_vaidation(self):
        """
        Test case for device credential workflow manager when provided site response is invalid.

        This test case checks the behavior of the device credential workflow manager when provided site response is invalid in the specified DNAC.
        """
        set_module_args(
            dict(
                dnac_host="1.1.1.1",
                dnac_username="dummy",
                dnac_password="dummy",
                dnac_log=True,
                state="merged",
                config=self.playbook_config_creation_invalid
            )
        )
        result = self.execute_module(changed=False, failed=True)
        print(result)
        self.assertEqual(
            result['msg'],
            "The specified version '2.2.3.3' does not support the path trace workflow feature.Supported version(s) start from '2.3.7.6' onwards."
        )

    def test_pathtrace_workflow_manager_update_with_flow_analysis(self):
        """
        Test case for path trace workflow manager when update with a flow ananlysis id with path trace.

        This test case verifies the behavior of the path trace workflow manager when
        update flow analysis with id for new path trace in the specified DNAC instance.
        """
        set_module_args(
            dict(
                dnac_host="1.1.1.1",
                dnac_username="dummy",
                dnac_password="dummy",
                dnac_version="2.3.7.9",
                dnac_log=True,
                state="merged",
                config=self.playbook_config_creation_with_flow_analaysis_id
            )
        )
        result = self.execute_module(changed=True, failed=False)
        print(result)
        self.assertEqual(
            result.get('msg'),
            'An error occurred during create path trace: '
        )
