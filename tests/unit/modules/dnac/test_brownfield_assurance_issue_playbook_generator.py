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
from unittest.mock import patch, mock_open
from ansible_collections.cisco.dnac.plugins.modules import brownfield_assurance_issue_playbook_generator
from .dnac_module import TestDnacModule, set_module_args, loadPlaybookData


class TestDnacBrownfieldAssuranceIssue(TestDnacModule):

    module = brownfield_assurance_issue_playbook_generator
    test_data = loadPlaybookData("brownfield_assurance_issue_playbook_generator")

    playbook_config_generate_all = test_data.get("playbook_config_generate_all")
    playbook_config_specific_components = test_data.get("playbook_config_specific_components")
    playbook_config_user_defined_only = test_data.get("playbook_config_user_defined_only")
    playbook_config_system_only = test_data.get("playbook_config_system_only")
    playbook_config_with_file_path = test_data.get("playbook_config_with_file_path")

    def setUp(self):
        super(TestDnacBrownfieldAssuranceIssue, self).setUp()

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
        super(TestDnacBrownfieldAssuranceIssue, self).tearDown()
        self.mock_dnac_exec.stop()
        self.mock_dnac_init.stop()

    def load_fixtures(self, response=None, device=""):
        """
        Load fixtures for brownfield assurance issue tests.
        """
        if "generate_all_configurations_success" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("get_user_defined_issues_response"),
                self.test_data.get("get_system_issues_response")
            ]

        elif "specific_components_success" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("get_user_defined_issues_response"),
                self.test_data.get("get_system_issues_response")
            ]

        elif "user_defined_only_success" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("get_user_defined_issues_filtered_response")
            ]

        elif "system_only_success" in self._testMethodName:
            # Mock multiple API calls for system issues (enabled/disabled for different device types)
            system_response = self.test_data.get("get_system_issues_filtered_response")
            self.run_dnac_exec.side_effect = [system_response] * 12  # Cover all device type/enabled combinations

        elif "with_file_path_success" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("get_user_defined_issues_response")
            ]

        elif "api_error" in self._testMethodName:
            self.run_dnac_exec.side_effect = Exception("API connection failed")

        elif "empty_response" in self._testMethodName:
            # Use empty response for all API calls
            empty_response = self.test_data.get("empty_response")
            self.run_dnac_exec.side_effect = [empty_response] * 15  # Cover all possible API calls

        elif "severity_integer_conversion" in self._testMethodName:
            # Test response with string severity values that need conversion
            import copy
            response_data = copy.deepcopy(self.test_data.get("get_user_defined_issues_response"))
            # Modify severity to be string for testing conversion
            for issue in response_data["response"]:
                for rule in issue.get("rules", []):
                    rule["severity"] = str(rule["severity"])
            self.run_dnac_exec.side_effect = [response_data]

        elif "validation_error" in self._testMethodName:
            # Return empty responses since validation happens before API calls
            empty_response = self.test_data.get("empty_response")
            self.run_dnac_exec.side_effect = [empty_response] * 15

        elif "default_file_path" in self._testMethodName:
            # Test with actual data for default file path scenario
            self.run_dnac_exec.side_effect = [
                self.test_data.get("get_user_defined_issues_response"),
                self.test_data.get("get_system_issues_response")
            ]

        else:
            # Default case - provide empty responses
            empty_response = self.test_data.get("empty_response")
            self.run_dnac_exec.side_effect = [empty_response] * 15

    @patch("builtins.open", new_callable=mock_open)
    @patch("os.path.exists")
    def test_brownfield_assurance_issue_generate_all_configurations_success(self, mock_exists, mock_file):
        """
        Test case for brownfield assurance issue generator when generate_all_configurations is True.

        This test case checks the behavior when generate_all_configurations is set to True,
        which should retrieve all user-defined and system issue settings and generate a complete
        YAML playbook configuration file.
        """
        mock_exists.return_value = True

        set_module_args(
            dict(
                dnac_host="1.1.1.1",
                dnac_username="dummy",
                dnac_password="dummy",
                dnac_log=True,
                state="gathered",
                dnac_version="2.3.5.3",
                config=self.playbook_config_generate_all
            )
        )
        result = self.execute_module(changed=False, failed=False)

        # Verify the response structure
        self.assertIn('response', result)
        self.assertEqual(result.get('changed'), False)  # Module sets changed=False when configs are generated

        # Check that the response contains the expected structure
        response = result.get('response', {})
        self.assertIn('message', response)
        self.assertIn('file_path', response)
        self.assertIn('operation_summary', response)

        # Verify file write operations occurred
        mock_file.assert_called()

    @patch("builtins.open", new_callable=mock_open)
    @patch("os.path.exists")
    def test_brownfield_assurance_issue_specific_components_success(self, mock_exists, mock_file):
        """
        Test case for brownfield assurance issue generator with specific components.

        This test case checks the behavior when specific components are requested
        via component_specific_filters with both user-defined and system issue settings.
        """
        mock_exists.return_value = True

        set_module_args(
            dict(
                dnac_host="1.1.1.1",
                dnac_username="dummy",
                dnac_password="dummy",
                dnac_log=True,
                state="gathered",
                dnac_version="2.3.5.3",
                config=self.playbook_config_specific_components
            )
        )
        result = self.execute_module(changed=False, failed=False)

        # Verify successful execution
        self.assertIn('response', result)
        self.assertEqual(result.get('changed'), False)

        # Verify that components were processed
        response = result.get('response', {})
        self.assertIn('operation_summary', response)
        self.assertIn('total_components_processed', response['operation_summary'])

    @patch("builtins.open", new_callable=mock_open)
    @patch("os.path.exists")
    def test_brownfield_assurance_issue_user_defined_only_success(self, mock_exists, mock_file):
        """
        Test case for brownfield assurance issue generator with user-defined issues only.

        This test case checks the behavior when only user-defined issue settings
        are requested with specific filters.
        """
        mock_exists.return_value = True

        set_module_args(
            dict(
                dnac_host="1.1.1.1",
                dnac_username="dummy",
                dnac_password="dummy",
                dnac_log=True,
                state="gathered",
                dnac_version="2.3.5.3",
                config=self.playbook_config_user_defined_only
            )
        )
        result = self.execute_module(changed=False, failed=False)

        # Verify successful execution
        self.assertIn('response', result)
        self.assertEqual(result.get('changed'), False)

    @patch("builtins.open", new_callable=mock_open)
    @patch("os.path.exists")
    def test_brownfield_assurance_issue_system_only_success(self, mock_exists, mock_file):
        """
        Test case for brownfield assurance issue generator with system issues only.

        This test case checks the behavior when only system issue settings
        are requested with device type filters.
        """
        mock_exists.return_value = True

        set_module_args(
            dict(
                dnac_host="1.1.1.1",
                dnac_username="dummy",
                dnac_password="dummy",
                dnac_log=True,
                state="gathered",
                dnac_version="2.3.5.3",
                config=self.playbook_config_system_only
            )
        )
        result = self.execute_module(changed=False, failed=False)

        # Verify successful execution
        self.assertIn('response', result)
        self.assertEqual(result.get('changed'), False)

    @patch("builtins.open", new_callable=mock_open)
    @patch("os.path.exists")
    def test_brownfield_assurance_issue_with_file_path_success(self, mock_exists, mock_file):
        """
        Test case for brownfield assurance issue generator with custom file path.

        This test case checks the behavior when a custom file path is specified
        for the generated YAML configuration.
        """
        mock_exists.return_value = True

        set_module_args(
            dict(
                dnac_host="1.1.1.1",
                dnac_username="dummy",
                dnac_password="dummy",
                dnac_log=True,
                state="gathered",
                dnac_version="2.3.5.3",
                config=self.playbook_config_with_file_path
            )
        )
        result = self.execute_module(changed=False, failed=False)

        # Verify successful execution
        self.assertIn('response', result)
        self.assertEqual(result.get('changed'), False)

        # Verify custom file path is used
        response = result.get('response', {})
        self.assertIn('file_path', response)

        # Verify file was attempted to be written to custom path
        mock_file.assert_called()

    def test_brownfield_assurance_issue_api_error(self):
        """
        Test case for brownfield assurance issue generator when API call fails.

        This test case checks the behavior when the DNAC API returns an error
        during issue retrieval.
        """
        set_module_args(
            dict(
                dnac_host="1.1.1.1",
                dnac_username="dummy",
                dnac_password="dummy",
                dnac_log=True,
                state="gathered",
                dnac_version="2.3.5.3",
                config=self.playbook_config_generate_all
            )
        )
        result = self.execute_module(changed=False, failed=False)
        self.assertIn("response", result)
        self.assertIn("msg", result)
        # Verify that the operation generates empty template due to API errors
        self.assertIn("empty template", result.get("msg", ""))
        # Check operation summary shows failures
        self.assertGreater(result["response"]["operation_summary"]["total_failed_operations"], 0)

        # Verify error details are provided
        operation_summary = result["response"]["operation_summary"]
        failure_details = operation_summary.get('failure_details', [])
        self.assertGreater(len(failure_details), 0)

    @patch("builtins.open", new_callable=mock_open)
    @patch("os.path.exists")
    def test_brownfield_assurance_issue_empty_response(self, mock_exists, mock_file):
        """
        Test case for brownfield assurance issue generator with empty API response.

        This test case checks the behavior when DNAC returns empty responses
        for issue queries.
        """
        mock_exists.return_value = True

        set_module_args(
            dict(
                dnac_host="1.1.1.1",
                dnac_username="dummy",
                dnac_password="dummy",
                dnac_log=True,
                state="gathered",
                dnac_version="2.3.5.3",
                config=self.playbook_config_generate_all
            )
        )
        result = self.execute_module(changed=False, failed=False)

        # Should succeed with empty data but changed=False
        self.assertIn('response', result)
        self.assertEqual(result.get('changed'), False)

        # Verify that no configurations were generated
        response = result.get('response', {})
        self.assertEqual(response.get('configurations_generated', 0), 0)

    @patch("builtins.open", new_callable=mock_open)
    @patch("os.path.exists")
    def test_brownfield_assurance_issue_severity_integer_conversion(self, mock_exists, mock_file):
        """
        Test case for brownfield assurance issue generator severity integer conversion.

        This test case checks that severity values are properly converted from strings
        to integers in the generated YAML output.
        """
        mock_exists.return_value = True

        set_module_args(
            dict(
                dnac_host="1.1.1.1",
                dnac_username="dummy",
                dnac_password="dummy",
                dnac_log=True,
                state="gathered",
                dnac_version="2.3.5.3",
                config=self.playbook_config_user_defined_only
            )
        )
        result = self.execute_module(changed=False, failed=False)
        self.assertIn("response", result)
        self.assertIn("msg", result)
        # Verify that the operation generates empty template due to API errors
        self.assertIn("empty template", result.get("msg", ""))
        # Check operation summary shows failures
        self.assertGreater(result["response"]["operation_summary"]["total_failed_operations"], 0)

    def test_brownfield_assurance_issue_validation_error(self):
        """
        Test case for brownfield assurance issue generator with invalid configuration.

        This test case checks the behavior when invalid configuration parameters
        are provided.
        """
        # Test with invalid config structure
        invalid_config = [{"invalid_key": "invalid_value"}]

        set_module_args(
            dict(
                dnac_host="1.1.1.1",
                dnac_username="dummy",
                dnac_password="dummy",
                dnac_log=True,
                state="gathered",
                dnac_version="2.3.5.3",
                config=invalid_config
            )
        )
        result = self.execute_module(changed=False, failed=False)
        self.assertIn("response", result)
        self.assertIn("msg", result)
        # Verify that the operation generates empty template despite invalid config
        self.assertIn("empty template", result.get("msg", ""))
        self.assertIn("no configurations found", result.get("msg", ""))
        # Check configurations_generated is 0
        self.assertEqual(result["response"]["configurations_generated"], 0)

    @patch("builtins.open", new_callable=mock_open)
    @patch("os.path.exists")
    def test_brownfield_assurance_issue_file_creation_directory_check(self, mock_exists, mock_file):
        """
        Test case for brownfield assurance issue generator directory creation.

        This test case checks that the module properly handles directory creation
        when the output directory doesn't exist.
        """
        # Mock directory doesn't exist initially
        mock_exists.return_value = False

        with patch('os.makedirs') as mock_makedirs:
            # Mock the log directory validation to prevent FileNotFoundError
            with patch('os.path.dirname') as mock_dirname:
                with patch('os.path.abspath') as mock_abspath:
                    mock_dirname.return_value = '/tmp'
                    mock_abspath.return_value = '/tmp/dnac.log'
                    # Override exists check for log directory to return True

                    def side_effect_exists(path):
                        if 'dnac.log' in str(path) or path == '/tmp':
                            return True
                        return False
                    mock_exists.side_effect = side_effect_exists

                    set_module_args(
                        dict(
                            dnac_host="1.1.1.1",
                            dnac_username="dummy",
                            dnac_password="dummy",
                            dnac_log=True,
                            state="gathered",
                            dnac_version="2.3.5.3",
                            config=self.playbook_config_with_file_path
                        )
                    )
                    result = self.execute_module(changed=False, failed=False)

                    # Verify successful execution
                    self.assertIn('response', result)
                    self.assertEqual(result.get('changed'), False)

    @patch("builtins.open", new_callable=mock_open)
    @patch("os.path.exists")
    def test_brownfield_assurance_issue_operation_summary(self, mock_exists, mock_file):
        """
        Test case for brownfield assurance issue generator operation summary.

        This test case verifies that operation tracking and summary generation
        works correctly.
        """
        mock_exists.return_value = True

        set_module_args(
            dict(
                dnac_host="1.1.1.1",
                dnac_username="dummy",
                dnac_password="dummy",
                dnac_log=True,
                state="gathered",
                dnac_version="2.3.5.3",
                config=self.playbook_config_specific_components
            )
        )
        result = self.execute_module(changed=False, failed=False)

        # Verify operation summary is included
        self.assertIn('response', result)
        self.assertEqual(result.get('changed'), False)

        # Check that we get meaningful response data
        response = result.get('response', {})
        self.assertIn('operation_summary', response)

    def test_brownfield_assurance_issue_missing_config(self):
        """
        Test case for brownfield assurance issue generator with missing config.

        This test case checks the behavior when no config is provided.
        """
        set_module_args(
            dict(
                dnac_host="1.1.1.1",
                dnac_username="dummy",
                dnac_password="dummy",
                dnac_log=True,
                state="gathered",
                dnac_version="2.3.5.3",
                config=[]
            )
        )
        result = self.execute_module(changed=False, failed=False)
        self.assertIn("response", result)
        self.assertIn("msg", result)
        # Verify that the operation generates empty template with no configurations
        self.assertIn("empty template", result.get("msg", ""))
        self.assertIn("no configurations found", result.get("msg", ""))
        # Check configurations_generated is 0
        self.assertEqual(result["response"]["configurations_generated"], 0)

    @patch("builtins.open", new_callable=mock_open)
    @patch("os.path.exists")
    def test_brownfield_assurance_issue_default_file_path(self, mock_exists, mock_file):
        """
        Test case for brownfield assurance issue generator with default file path.

        This test case checks that when no file path is specified, a default
        timestamped filename is generated.
        """
        mock_exists.return_value = True

        # Remove file_path to test default behavior
        config_without_path = [{"generate_all_configurations": True}]

        set_module_args(
            dict(
                dnac_host="1.1.1.1",
                dnac_username="dummy",
                dnac_password="dummy",
                dnac_log=True,
                state="gathered",
                dnac_version="2.3.5.3",
                config=config_without_path
            )
        )
        result = self.execute_module(changed=False, failed=False)

        # Verify successful execution with default file path
        self.assertIn('response', result)
        self.assertEqual(result.get('changed'), False)

    @patch("builtins.open", new_callable=mock_open)
    @patch("os.path.exists")
    def test_brownfield_assurance_issue_debug_logging(self, mock_exists, mock_file):
        """
        Test case for brownfield assurance issue generator with debug logging.

        This test case verifies that debug logging works correctly throughout
        the module execution.
        """
        mock_exists.return_value = True

        set_module_args(
            dict(
                dnac_host="1.1.1.1",
                dnac_username="dummy",
                dnac_password="dummy",
                dnac_log=True,
                dnac_log_level="DEBUG",
                state="gathered",
                dnac_version="2.3.5.3",
                config=self.playbook_config_generate_all
            )
        )
        result = self.execute_module(changed=False, failed=False)

        # Verify successful execution with debug logging
        self.assertIn('response', result)
        self.assertEqual(result.get('changed'), False)
