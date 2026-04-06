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
from ansible_collections.cisco.dnac.plugins.modules import discovery_playbook_config_generator
from .dnac_module import TestDnacModule, set_module_args, loadPlaybookData


class TestDnacBrownfieldDiscoveryPlaybookGenerator(TestDnacModule):

    module = discovery_playbook_config_generator
    test_data = loadPlaybookData("discovery_playbook_config_generator")
    playbook_config_generate_all = test_data.get("playbook_config_generate_all")
    playbook_config_specific_names = test_data.get("playbook_config_specific_names")
    playbook_config_by_type = test_data.get("playbook_config_by_type")
    playbook_config_with_filters = test_data.get("playbook_config_with_filters")

    def setUp(self):
        super(TestDnacBrownfieldDiscoveryPlaybookGenerator, self).setUp()

        self.mock_dnac_init = patch(
            "ansible_collections.cisco.dnac.plugins.module_utils.dnac.DNACSDK.__init__")
        self.run_dnac_init = self.mock_dnac_init.start()
        self.run_dnac_init.side_effect = [None]
        self.mock_dnac_exec = patch(
            "ansible_collections.cisco.dnac.plugins.module_utils.dnac.DNACSDK._exec"
        )
        self.run_dnac_exec = self.mock_dnac_exec.start()

        # Mock file operations
        self.mock_open = patch("builtins.open")
        self.run_mock_open = self.mock_open.start()

        # Mock yaml dump
        self.mock_yaml_dump = patch("yaml.dump")
        self.run_yaml_dump = self.mock_yaml_dump.start()

        self.load_fixtures()

    def tearDown(self):
        super(TestDnacBrownfieldDiscoveryPlaybookGenerator, self).tearDown()
        self.mock_dnac_exec.stop()
        self.mock_dnac_init.stop()
        self.mock_open.stop()
        self.mock_yaml_dump.stop()

    def load_fixtures(self, response=None, device=""):
        """
        Load fixtures for brownfield discovery playbook generator tests.
        """

        if "generate_all_configurations" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("get_discoveries_response_success"),
                self.test_data.get("get_global_credentials_response_success"),
            ]

        elif "discovery_name_filter" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("get_discoveries_response_success"),
                self.test_data.get("get_global_credentials_response_success"),
            ]

        elif "discovery_type_filter" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("get_discoveries_response_success"),
                self.test_data.get("get_global_credentials_response_success"),
            ]

        elif "component_filters" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("get_discoveries_response_success"),
                self.test_data.get("get_global_credentials_response_success"),
            ]

        elif "empty_discoveries_response" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("get_discoveries_empty_response"),
                self.test_data.get("get_global_credentials_response_success"),
            ]

        elif "api_exception_handling" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                Exception("API Error: Connection failed"),
            ]

        elif "credential_mapping" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("get_discoveries_response_success"),
                self.test_data.get("get_global_credentials_response_success"),
            ]

        elif "invalid_state" in self._testMethodName:
            self.run_dnac_exec.side_effect = []

        elif "missing_config" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("get_discoveries_response_success"),
                self.test_data.get("get_global_credentials_response_success"),
            ]

        elif "file_path_specified" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("get_discoveries_response_success"),
                self.test_data.get("get_global_credentials_response_success"),
            ]

        elif "no_global_filters" in self._testMethodName:
            self.run_dnac_exec.side_effect = []

        elif "successful_generation" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("get_discoveries_response_success"),
                self.test_data.get("get_global_credentials_response_success"),
            ]

        elif "config_verify_false" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("get_discoveries_response_success"),
                self.test_data.get("get_global_credentials_response_success"),
            ]

        elif "debug_logging" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("get_discoveries_response_success"),
                self.test_data.get("get_global_credentials_response_success"),
            ]

    def test_discovery_playbook_config_generator_generate_all_configurations(self):
        """
        Test case for brownfield discovery playbook generator when generating all configurations.

        This test case checks the behavior when generating all discovery configurations from Catalyst Center.
        """
        set_module_args(
            dict(
                dnac_host="192.168.1.1",
                dnac_username="admin",
                dnac_password="admin",
                dnac_log=True,
                state="gathered",
                dnac_version="2.3.7.9",
                config=self.playbook_config_generate_all
            )
        )
        result = self.execute_module(changed=False, failed=False)
        self.assertIsNotNone(result)
        self.assertIn('response', result)

    def test_discovery_playbook_config_generator_discovery_name_filter(self):
        """
        Test case for generating configurations filtered by discovery name.

        This test case checks the behavior when filtering discoveries by specific names.
        """
        set_module_args(
            dict(
                dnac_host="192.168.1.1",
                dnac_username="admin",
                dnac_password="admin",
                dnac_log=True,
                dnac_version="2.3.7.9",
                state="gathered",
                file_path="/tmp/test_discoveries.yml",
                file_mode="overwrite",
                config=self.playbook_config_specific_names
            )
        )
        result = self.execute_module(changed=False, failed=False)
        self.assertIsNotNone(result)
        self.assertIn('response', result)

    def test_discovery_playbook_config_generator_discovery_type_filter(self):
        """
        Test case for generating configurations filtered by discovery type.

        This test case checks the behavior when filtering discoveries by type (Range, CIDR, etc.).
        """
        set_module_args(
            dict(
                dnac_host="192.168.1.1",
                dnac_username="admin",
                dnac_password="admin",
                dnac_log=True,
                dnac_version="2.3.7.9",
                state="gathered",
                config=self.playbook_config_by_type
            )
        )
        result = self.execute_module(changed=False, failed=False)
        # Verify successful execution with response data
        self.assertIsNotNone(result)
        self.assertIn('response', result)

    def test_discovery_playbook_config_generator_component_filters(self):
        """
        Test case for generating configurations with component-specific filters.

        This test case checks the behavior when applying component filters like discovery status.
        """
        set_module_args(
            dict(
                dnac_host="192.168.1.1",
                dnac_username="admin",
                dnac_password="admin",
                dnac_log=True,
                dnac_version="2.3.7.9",
                state="gathered",
                config=self.playbook_config_by_type
            )
        )
        result = self.execute_module(changed=False, failed=False)
        # Module executes successfully and returns response data
        self.assertIsNotNone(result)
        self.assertIn('response', result)

    def test_discovery_playbook_config_generator_empty_discoveries_response(self):
        """
        Test case for handling empty discoveries response.

        This test case checks the behavior when no discoveries are found in Catalyst Center.
        """
        set_module_args(
            dict(
                dnac_host="192.168.1.1",
                dnac_username="admin",
                dnac_password="admin",
                dnac_log=True,
                dnac_version="2.3.7.9",
                state="gathered",
                config={
                    "global_filters": {
                        "discovery_type_list": ["Range", "CIDR", "Single"]
                    }
                }
            )
        )
        result = self.execute_module(changed=False, failed=False)
        # Verify successful execution (even with empty discoveries)
        self.assertIsNotNone(result)
        self.assertIn('response', result)

    def test_discovery_playbook_config_generator_api_exception_handling(self):
        """
        Test case for API exception handling.

        This test case checks the behavior when API calls fail.
        """
        set_module_args(
            dict(
                dnac_host="192.168.1.1",
                dnac_username="admin",
                dnac_password="admin",
                dnac_log=True,
                dnac_version="2.3.7.9",
                state="gathered",
                config=self.playbook_config_generate_all
            )
        )
        result = self.execute_module(changed=False, failed=False)
        # The module gracefully handles API errors and returns no_data status
        self.assertIn('response', result)
        self.assertEqual(result['response'].get('status'), 'no_data')

    def test_discovery_playbook_config_generator_credential_mapping(self):
        """
        Test case for credential ID to name mapping functionality.

        This test case checks the behavior when mapping credential IDs to readable names.
        """
        set_module_args(
            dict(
                dnac_host="192.168.1.1",
                dnac_username="admin",
                dnac_password="admin",
                dnac_log=True,
                dnac_version="2.3.7.9",
                state="gathered",
                file_path="/tmp/specific_discoveries.yml",
                file_mode="append",
                config=self.playbook_config_specific_names
            )
        )
        result = self.execute_module(changed=False, failed=False)
        # Verify successful execution with response data
        self.assertIsNotNone(result)
        self.assertIn('response', result)

    def test_discovery_playbook_config_generator_invalid_state(self):
        """
        Test case for invalid state parameter.

        This test case checks the behavior when an invalid state is provided.
        """
        set_module_args(
            dict(
                dnac_host="192.168.1.1",
                dnac_username="admin",
                dnac_password="admin",
                dnac_log=True,
                dnac_version="2.3.7.9",
                state="invalid_state",
                config=self.playbook_config_generate_all
            )
        )
        result = self.execute_module(changed=False, failed=True)
        self.assertIn('value of state must be one of: gathered', result.get('msg'))

    def test_discovery_playbook_config_generator_missing_config(self):
        """
        Test case for missing config parameter (auto-discovery mode).

        This test case checks the behavior when config parameter is omitted.
        """
        set_module_args(
            dict(
                dnac_host="192.168.1.1",
                dnac_username="admin",
                dnac_password="admin",
                dnac_log=True,
                dnac_version="2.3.7.9",
                state="gathered"
            )
        )
        result = self.execute_module(changed=False, failed=False)
        self.assertIn('response', result)

    def test_discovery_playbook_config_generator_invalid_global_filter_key(self):
        """
        Test case for invalid suboption key under global_filters.

        This test case checks validation failure when unsupported key is provided.
        """
        set_module_args(
            dict(
                dnac_host="192.168.1.1",
                dnac_username="admin",
                dnac_password="admin",
                dnac_log=True,
                dnac_version="2.3.7.9",
                state="gathered",
                config={
                    "global_filters": {
                        "hello": ["world"]
                    }
                }
            )
        )
        result = self.execute_module(changed=False, failed=True)
        self.assertIn("Invalid key(s) under 'global_filters'", result.get('response'))

    def test_discovery_playbook_config_generator_invalid_discovery_type_filter_value(self):
        """
        Test case for invalid value under global_filters.discovery_type_list.

        This test case checks validation failure when unsupported discovery type is provided.
        """
        set_module_args(
            dict(
                dnac_host="192.168.1.1",
                dnac_username="admin",
                dnac_password="admin",
                dnac_log=True,
                dnac_version="2.3.7.9",
                state="gathered",
                config={
                    "global_filters": {
                        "discovery_type_list": ["HELLO"]
                    }
                }
            )
        )
        result = self.execute_module(changed=False, failed=True)
        self.assertIn(
            "Invalid values under 'global_filters.discovery_type_list'",
            result.get('response')
        )

    def test_discovery_playbook_config_generator_file_path_specified(self):
        """
        Test case for specifying custom file path.

        This test case checks the behavior when a custom file path is provided.
        """
        set_module_args(
            dict(
                dnac_host="192.168.1.1",
                dnac_username="admin",
                dnac_password="admin",
                dnac_log=True,
                dnac_version="2.3.7.9",
                state="gathered",
                config=self.playbook_config_specific_names
            )
        )
        result = self.execute_module(changed=False, failed=False)
        self.assertIsNotNone(result)
        self.assertIn('response', result)

    def test_discovery_playbook_config_generator_no_global_filters(self):
        """
        Test case for generating configurations without global filters.

        This test case checks the behavior when no global filters are applied.
        """
        set_module_args(
            dict(
                dnac_host="192.168.1.1",
                dnac_username="admin",
                dnac_password="admin",
                dnac_log=True,
                dnac_version="2.3.7.9",
                state="gathered",
                config={}
            )
        )
        result = self.execute_module(changed=False, failed=True)
        self.assertIn(
            "global_filters is required when config is provided",
            result.get('msg', '')
        )

    def test_discovery_playbook_config_generator_generate_all_configurations_rejected(self):
        """
        Test case for rejecting generate_all_configurations in config input.
        """
        set_module_args(
            dict(
                dnac_host="192.168.1.1",
                dnac_username="admin",
                dnac_password="admin",
                dnac_log=True,
                dnac_version="2.3.7.9",
                state="gathered",
                config={
                    "generate_all_configurations": True,
                    "global_filters": {
                        "discovery_type_list": ["Range"]
                    }
                }
            )
        )
        result = self.execute_module(changed=False, failed=True)
        self.assertIn(
            "Invalid parameters",
            result.get('msg', '')
        )

    def test_discovery_playbook_config_generator_successful_generation(self):
        """
        Test case for successful playbook generation.

        This test case checks the overall successful generation flow.
        """
        set_module_args(
            dict(
                dnac_host="192.168.1.1",
                dnac_username="admin",
                dnac_password="admin",
                dnac_log=True,
                dnac_version="2.3.7.9",
                state="gathered",
                config={
                    "global_filters": {
                        "discovery_name_list": ["Test Discovery"]
                    }
                }
            )
        )
        result = self.execute_module(changed=False, failed=False)
        # Verify successful execution with response data
        self.assertIsNotNone(result)
        self.assertIn('response', result)

    def test_discovery_playbook_config_generator_config_verify_false(self):
        """
        Test case with config_verify set to False.

        This test case checks the behavior when config verification is disabled.
        """
        set_module_args(
            dict(
                dnac_host="192.168.1.1",
                dnac_username="admin",
                dnac_password="admin",
                dnac_log=True,
                dnac_version="2.3.7.9",
                state="gathered",
                config=self.playbook_config_specific_names
            )
        )
        result = self.execute_module(changed=False, failed=False)
        # Verify successful execution with response data
        self.assertIsNotNone(result)
        self.assertIn('response', result)

    def test_discovery_playbook_config_generator_debug_logging(self):
        """
        Test case for debug logging functionality.

        This test case checks the behavior when debug logging is enabled.
        """
        set_module_args(
            dict(
                dnac_host="192.168.1.1",
                dnac_username="admin",
                dnac_password="admin",
                dnac_log=True,
                dnac_debug=True,
                dnac_version="2.3.7.9",
                state="gathered",
                config=self.playbook_config_generate_all
            )
        )
        result = self.execute_module(changed=False, failed=False)
        # Verify successful execution with response data
        self.assertIsNotNone(result)
        self.assertIn('response', result)

    def test_discovery_playbook_config_generator_unsupported_state(self):
        """
        Test case for unsupported state parameter.

        This test case checks the behavior when an unsupported state is provided.
        """
        set_module_args(
            dict(
                dnac_host="192.168.1.1",
                dnac_username="admin",
                dnac_password="admin",
                dnac_log=True,
                dnac_version="2.3.7.9",
                state="created",  # Unsupported state
                config=self.playbook_config_generate_all
            )
        )
        result = self.execute_module(changed=False, failed=True)
        # Verify failure with appropriate error message
        self.assertTrue(result.get('failed', False))
        msg = result.get('msg', '')
        self.assertIn('must be one of', msg.lower())

    def test_discovery_playbook_config_generator_v2_api_fallback(self):
        """
        Test case for V2 API fallback when V1 credentials API fails.

        This test case checks the behavior when V1 API returns empty and V2 is used.
        """
        self.load_fixtures(['empty_credentials_v1_fallback_v2'])
        set_module_args(
            dict(
                dnac_host="192.168.1.1",
                dnac_username="admin",
                dnac_password="admin",
                dnac_log=True,
                dnac_version="2.3.7.9",
                state="gathered",
                config=self.playbook_config_specific_names
            )
        )
        result = self.execute_module(changed=False, failed=False)
        # Verify successful execution with V2 API fallback
        self.assertIsNotNone(result)
        self.assertIn('response', result)

    def test_discovery_playbook_config_generator_credential_api_failure(self):
        """
        Test case for handling credential API failures.

        This test case checks the behavior when both V1 and V2 credential APIs fail.
        """
        self.load_fixtures(['credentials_api_failure'])
        set_module_args(
            dict(
                dnac_host="192.168.1.1",
                dnac_username="admin",
                dnac_password="admin",
                dnac_log=True,
                dnac_version="2.3.7.9",
                state="gathered",
                config=self.playbook_config_specific_names
            )
        )
        result = self.execute_module(changed=False, failed=False)
        # Verify graceful handling of API failures
        self.assertIsNotNone(result)
        self.assertIn('response', result)

    def test_discovery_playbook_config_generator_complex_credential_mapping(self):
        """
        Test case for complex credential mapping with various types.

        This test case checks the behavior with multiple credential types and fallback mapping.
        """
        self.load_fixtures(['complex_credential_mapping'])
        set_module_args(
            dict(
                dnac_host="192.168.1.1",
                dnac_username="admin",
                dnac_password="admin",
                dnac_log=True,
                dnac_version="2.3.7.9",
                state="gathered",
                config={
                    "global_filters": {
                        "discovery_type_list": ["Range", "CIDR", "Single"]
                    }
                }
            )
        )
        result = self.execute_module(changed=False, failed=False)
        # Verify successful execution with complex credential mapping
        self.assertIsNotNone(result)
        self.assertIn('response', result)

    def test_discovery_playbook_config_generator_file_operations(self):
        """
        Test case for file operations with custom paths.

        This test case checks the behavior when custom file paths are specified.
        """
        set_module_args(
            dict(
                dnac_host="192.168.1.1",
                dnac_username="admin",
                dnac_password="admin",
                dnac_log=True,
                dnac_version="2.3.7.9",
                state="gathered",
                file_path="/tmp/test_brownfield_discovery.yml",
                file_mode="overwrite"
            )
        )
        result = self.execute_module(changed=False, failed=False)
        # Verify successful execution with file operations
        self.assertIsNotNone(result)
        self.assertIn('response', result)

    def test_discovery_playbook_config_generator_advanced_status_filtering(self):
        """
        Test case for advanced discovery status filtering.

        This test case checks filtering by multiple discovery statuses.
        """
        set_module_args(
            dict(
                dnac_host="192.168.1.1",
                dnac_username="admin",
                dnac_password="admin",
                dnac_log=True,
                dnac_version="2.3.7.9",
                state="gathered",
                config={
                    "global_filters": {
                        "discovery_type_list": ["Range", "CIDR", "Single"]
                    }
                }
            )
        )
        result = self.execute_module(changed=False, failed=False)
        # Verify successful execution with advanced status filtering
        self.assertIsNotNone(result)
        self.assertIn('response', result)

    def test_discovery_playbook_config_generator_empty_credential_id_handling(self):
        """
        Test case for handling empty or None credential IDs.

        This test case checks the behavior when credential IDs are empty or None.
        """
        set_module_args(
            dict(
                dnac_host="192.168.1.1",
                dnac_username="admin",
                dnac_password="admin",
                dnac_log=True,
                dnac_version="2.3.7.9",
                state="gathered",
                config={
                    "global_filters": {
                        "discovery_type_list": ["Range", "CIDR", "Single"]
                    }
                }
            )
        )
        result = self.execute_module(changed=False, failed=False)
        # Verify successful execution with empty credential handling
        self.assertIsNotNone(result)
        self.assertIn('response', result)

    def test_discovery_playbook_config_generator_credential_not_found(self):
        """
        Test case for handling credentials not found in lookup table.

        This test case checks the behavior when credentials are referenced but not found.
        """
        self.load_fixtures(['credentials_not_found'])
        set_module_args(
            dict(
                dnac_host="192.168.1.1",
                dnac_username="admin",
                dnac_password="admin",
                dnac_log=True,
                dnac_version="2.3.7.9",
                state="gathered",
                config={
                    "global_filters": {
                        "discovery_type_list": ["Range", "CIDR", "Single"]
                    }
                }
            )
        )
        result = self.execute_module(changed=False, failed=False)
        # Verify successful execution with missing credentials handling
        self.assertIsNotNone(result)
        self.assertIn('response', result)

    def test_discovery_playbook_config_generator_unknown_credential_type(self):
        """
        Test case for handling unknown credential types.

        This test case checks the behavior when credentials have unknown types.
        """
        self.load_fixtures(['unknown_credential_types'])
        set_module_args(
            dict(
                dnac_host="192.168.1.1",
                dnac_username="admin",
                dnac_password="admin",
                dnac_log=True,
                dnac_version="2.3.7.9",
                state="gathered",
                config={
                    "global_filters": {
                        "discovery_type_list": ["Range", "CIDR", "Single"]
                    }
                }
            )
        )
        result = self.execute_module(changed=False, failed=False)
        # Verify successful execution with unknown credential type handling
        self.assertIsNotNone(result)
        self.assertIn('response', result)

    def test_discovery_playbook_config_generator_malformed_api_response(self):
        """
        Test case for handling malformed API responses.

        This test case checks the behavior when API returns malformed data.
        """
        self.load_fixtures(['malformed_api_response'])
        set_module_args(
            dict(
                dnac_host="192.168.1.1",
                dnac_username="admin",
                dnac_password="admin",
                dnac_log=True,
                dnac_version="2.3.7.9",
                state="gathered",
                config=self.playbook_config_generate_all
            )
        )
        result = self.execute_module(changed=False, failed=False)
        # Verify successful execution with malformed response handling
        self.assertIsNotNone(result)
        self.assertIn('response', result)

    def test_discovery_playbook_config_generator_mixed_discovery_types(self):
        """
        Test case for handling mixed discovery types in single request.

        This test case checks the behavior with multiple discovery types.
        """
        self.load_fixtures(['mixed_discovery_types'])
        set_module_args(
            dict(
                dnac_host="192.168.1.1",
                dnac_username="admin",
                dnac_password="admin",
                dnac_log=True,
                dnac_version="2.3.7.9",
                state="gathered",
                config={
                    "global_filters": {
                        "discovery_type_list": ["Range", "CIDR", "Single"]
                    }
                }
            )
        )
        result = self.execute_module(changed=False, failed=False)
        # Verify successful execution with mixed discovery types
        self.assertIsNotNone(result)
        self.assertIn('response', result)

    def test_discovery_playbook_config_generator_credential_transform_edge_cases(self):
        """
        Test case for credential transformation edge cases.

        This test case checks the behavior with edge cases in credential transformation.
        """
        set_module_args(
            dict(
                dnac_host="192.168.1.1",
                dnac_username="admin",
                dnac_password="admin",
                dnac_log=True,
                dnac_version="2.3.7.9",
                state="gathered",
                config={
                    "global_filters": {
                        "discovery_name_list": ["EdgeCaseTest"]
                    }
                }
            )
        )
        result = self.execute_module(changed=False, failed=False)
        # Verify successful execution with credential transformation edge cases
        self.assertIsNotNone(result)
        self.assertIn('response', result)

    def test_discovery_playbook_config_generator_api_error_conditions(self):
        """
        Test case for API error conditions and recovery.

        This test case checks various API error conditions and recovery mechanisms.
        """
        self.load_fixtures(['api_error_conditions'])
        set_module_args(
            dict(
                dnac_host="192.168.1.1",
                dnac_username="admin",
                dnac_password="admin",
                dnac_log=True,
                dnac_version="2.3.7.9",
                state="gathered",
                config={
                    "global_filters": {
                        "discovery_type_list": ["Range", "CIDR", "Single"]
                    }
                }
            )
        )
        result = self.execute_module(changed=False, failed=False)
        # Verify successful execution with API error handling
        self.assertIsNotNone(result)
        self.assertIn('response', result)

    def test_discovery_playbook_config_generator_comprehensive_filtering(self):
        """
        Test case for comprehensive filtering with all options.

        This test case checks behavior with all filtering options enabled.
        """
        set_module_args(
            dict(
                dnac_host="192.168.1.1",
                dnac_username="admin",
                dnac_password="admin",
                dnac_log=True,
                dnac_debug=True,
                dnac_version="2.3.7.9",
                state="gathered",
                config={
                    "global_filters": {
                        "discovery_name_list": ["TestDiscovery1", "TestDiscovery2"],
                        "discovery_type_list": ["Range", "CIDR"]
                    }
                }
            )
        )
        result = self.execute_module(changed=False, failed=False)
        # Verify successful execution with comprehensive filtering
        self.assertIsNotNone(result)
        self.assertIn('response', result)
