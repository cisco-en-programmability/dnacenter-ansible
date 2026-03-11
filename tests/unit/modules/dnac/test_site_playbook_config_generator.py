#  Copyright (c) 2026 Cisco and/or its affiliates.
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

# Authors:
#   Vidhya Rathinam (VidhyaGit)
#
# Description:
#   Unit tests for the Ansible module `site_playbook_config_generator`.
#   These tests cover various scenarios for generating YAML playbooks from brownfield
#   site configurations including areas, buildings, and floors.

from __future__ import absolute_import, division, print_function

__metaclass__ = type
from unittest.mock import patch, mock_open
from brownfield.collections.ansible_collections.cisco.dnac.plugins.modules import (
    site_playbook_config_generator,
)
from .dnac_module import TestDnacModule, set_module_args, loadPlaybookData


class TestBrownfieldSiteWorkflowManager(TestDnacModule):

    module = site_playbook_config_generator
    test_data = loadPlaybookData("site_playbook_config_generator")
    success_message_fragment = "YAML configuration file generated successfully"

    # Load all playbook configurations
    playbook_config_generate_all_configurations = test_data.get(
        "playbook_config_generate_all_configurations"
    )
    playbook_config_area_by_site_name_single = test_data.get(
        "playbook_config_area_by_site_name_single"
    )
    playbook_config_area_by_site_name_multiple = test_data.get(
        "playbook_config_area_by_site_name_multiple"
    )
    playbook_config_area_by_parent_site = test_data.get(
        "playbook_config_area_by_parent_site"
    )
    playbook_config_building_by_site_name_single = test_data.get(
        "playbook_config_building_by_site_name_single"
    )
    playbook_config_building_by_site_name_multiple = test_data.get(
        "playbook_config_building_by_site_name_multiple"
    )
    playbook_config_building_by_parent_site = test_data.get(
        "playbook_config_building_by_parent_site"
    )
    playbook_config_floor_by_site_name_single = test_data.get(
        "playbook_config_floor_by_site_name_single"
    )
    playbook_config_floor_by_site_name_multiple = test_data.get(
        "playbook_config_floor_by_site_name_multiple"
    )
    playbook_config_floor_by_parent_site = test_data.get(
        "playbook_config_floor_by_parent_site"
    )
    playbook_config_area_combined_filters = test_data.get(
        "playbook_config_area_combined_filters"
    )
    playbook_config_floor_combined_filters = test_data.get(
        "playbook_config_floor_combined_filters"
    )
    playbook_config_areas_and_buildings = test_data.get(
        "playbook_config_areas_and_buildings"
    )
    playbook_config_buildings_and_floors = test_data.get(
        "playbook_config_buildings_and_floors"
    )
    playbook_config_all_components = test_data.get("playbook_config_all_components")
    playbook_config_empty_filters = test_data.get("playbook_config_empty_filters")
    playbook_config_no_file_path = test_data.get("playbook_config_no_file_path")
    playbook_config_direct_filter_components_list_name_hierarchy = test_data.get(
        "playbook_config_direct_filter_components_list_name_hierarchy"
    )
    playbook_config_name_hierarchy_pattern = test_data.get(
        "playbook_config_name_hierarchy_pattern"
    )
    playbook_config_parent_name_hierarchy_pattern = test_data.get(
        "playbook_config_parent_name_hierarchy_pattern"
    )
    playbook_config_combined_hierarchy_patterns = test_data.get(
        "playbook_config_combined_hierarchy_patterns"
    )

    def setUp(self):
        super(TestBrownfieldSiteWorkflowManager, self).setUp()
        self._fixture_response_override = None

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
        super(TestBrownfieldSiteWorkflowManager, self).tearDown()
        self.mock_dnac_exec.stop()
        self.mock_dnac_init.stop()

    def load_fixtures(self, response=None, device=""):
        """
        Load fixtures for brownfield site workflow manager tests.
        """
        if self._fixture_response_override is not None:
            self.run_dnac_exec.side_effect = self._fixture_response_override
            self._fixture_response_override = None
            return

        if response is not None:
            self.run_dnac_exec.side_effect = (
                response if isinstance(response, list) else [response]
            )
            return

        # Default fixture: return the same consolidated payload for each API call.
        self.run_dnac_exec.side_effect = (
            lambda *args, **kwargs: self.test_data.get("get_all_sites_response")
        )

    def run_module_with_config_and_validate_success(self, config):
        """
        Execute the module with a provided configuration and validate success output.

        This helper centralizes the common execution path used by multiple test
        cases so assertions remain consistent and expressive across scenarios.
        It performs complete module invocation, checks for successful completion,
        and returns raw module output for additional scenario-specific assertions.

        Args:
            config (dict): Module configuration payload passed directly to
                `site_playbook_config_generator`.

        Returns:
            dict: Module execution result dictionary returned by
            `execute_module`.
        """
        set_module_args(
            dict(
                dnac_host="1.1.1.1",
                dnac_username="dummy",
                dnac_password="dummy",
                dnac_version="2.3.7.9",
                dnac_log=True,
                dnac_log_level="DEBUG",
                state="gathered",
                config=config,
            )
        )
        result = self.execute_module(changed=True, failed=False)
        self.assert_success_result_message(
            result,
            "run_module_with_config_and_validate_success",
        )
        return result

    def assert_success_result_message(self, result, scenario_name):
        """
        Validate that a module execution result contains the expected success marker.

        Why this helper exists:
        - Keeps assertion behavior uniform for all scenario tests.
        - Produces high-fidelity failure output that includes scenario context and
          full response payload for faster triage.
        - Encapsulates the exact success-token check in one place so message
          contract changes can be updated centrally.

        Args:
            result (dict): Result object returned by `execute_module`.
            scenario_name (str): Human-readable scenario label used in assertion
                failure diagnostics.
        """
        message_value = str(result.get("msg"))
        self.assertIn(
            self.success_message_fragment,
            message_value,
            (
                "Expected success message fragment '{0}' was not found for "
                "scenario '{1}'. Actual msg: {2}. Full result payload: {3}".format(
                    self.success_message_fragment, scenario_name, message_value, result
                )
            ),
        )

    def assert_get_sites_api_call(self, call_index, expected_params):
        """
        Validate one concrete SDK execution call for `site_design.get_sites`.

        Validation scope:
        - Confirms that the mocked SDK invocation exists at the requested index.
        - Verifies immutable invocation contract fields:
          `family`, `function`, and `op_modifies`.
        - Verifies scenario-driven request parameters such as `type`,
          `nameHierarchy`, and pagination markers (`offset`, `limit`).
        - Emits a detailed assertion failure payload containing the mismatched
          call index and full params snapshot to minimize debugging effort.

        Args:
            call_index (int): Zero-based index in call_args_list.
            expected_params (dict): Expected values in params payload.
        """
        self.assertGreater(
            len(self.run_dnac_exec.call_args_list),
            call_index,
            "Expected _exec call index {0} not found. Available calls: {1}".format(
                call_index, len(self.run_dnac_exec.call_args_list)
            ),
        )
        call_kwargs = self.run_dnac_exec.call_args_list[call_index].kwargs
        self.assertEqual(call_kwargs.get("family"), "site_design")
        self.assertEqual(call_kwargs.get("function"), "get_sites")
        self.assertEqual(call_kwargs.get("op_modifies"), False)

        params = call_kwargs.get("params") or {}
        for key, value in expected_params.items():
            self.assertEqual(
                params.get(key),
                value,
                "Mismatch for _exec params['{0}'] in call {1}. Params: {2}".format(
                    key, call_index, params
                ),
            )

    @patch("builtins.open", new_callable=mock_open)
    @patch("os.path.exists")
    def test_site_playbook_config_generator_generate_all_configurations(
        self, mock_exists, mock_file
    ):
        """
        Test case for brownfield site workflow manager when generating all configurations.

        This test case checks the behavior when generate_all_configurations is set to True,
        which should retrieve all areas, buildings, and floors and generate a complete
        YAML playbook configuration file.
        """
        mock_exists.return_value = True

        set_module_args(
            dict(
                dnac_host="1.1.1.1",
                dnac_username="dummy",
                dnac_password="dummy",
                dnac_version="2.3.7.9",
                dnac_log=True,
                dnac_log_level="DEBUG",
                state="gathered",
                config=self.playbook_config_generate_all_configurations,
            )
        )
        result = self.execute_module(changed=True, failed=False)
        self.assert_success_result_message(result, self._testMethodName)

    @patch("builtins.open", new_callable=mock_open)
    @patch("os.path.exists")
    def test_site_playbook_config_generator_generate_all_configurations_api_invocation(
        self, mock_exists, mock_file
    ):
        """
        Verify API calls for generate_all_configurations mode.

        Expected behavior:
        - One GET call to site_design/get_sites
        - Filtering and type partitioning are local post-processing steps
        - Pagination defaults must be present in params
        """
        mock_exists.return_value = True
        self.run_module_with_config_and_validate_success(
            self.playbook_config_generate_all_configurations
        )

        self.assertEqual(self.run_dnac_exec.call_count, 1)
        self.assert_get_sites_api_call(0, {"offset": 1, "limit": 500})

    @patch("builtins.open", new_callable=mock_open)
    @patch("os.path.exists")
    def test_site_playbook_config_generator_generate_all_configurations_pagination_over_500(
        self, mock_exists, mock_file
    ):
        """
        Validate pagination behavior when generate_all_configurations exceeds one page.

        Synthetic response setup:
        - Page 1: 500 area records
        - Page 2: 120 area records

        Expected behavior:
        - Module retrieves both pages via execute_get_with_pagination
        - API calls are issued with offsets 1 and 501
        - Final generated configuration includes all 620 records
        """
        mock_exists.return_value = True

        def build_area_records(start_index, end_index):
            records = []
            for index in range(start_index, end_index + 1):
                records.append(
                    {
                        "id": "area-uuid-{0}".format(index),
                        "siteId": "area-uuid-{0}".format(index),
                        "name": "Area_{0}".format(index),
                        "parentName": "Global",
                        "nameHierarchy": "Global/Area_{0}".format(index),
                        "type": "area",
                        "additionalInfo": [],
                    }
                )
            return records

        synthetic_paginated_response = [
            {"response": build_area_records(1, 500), "version": "1.0"},
            {"response": build_area_records(501, 620), "version": "1.0"},
        ]
        self._fixture_response_override = synthetic_paginated_response

        set_module_args(
            dict(
                dnac_host="1.1.1.1",
                dnac_username="dummy",
                dnac_password="dummy",
                dnac_version="2.3.7.9",
                dnac_log=True,
                dnac_log_level="DEBUG",
                state="gathered",
                config=self.playbook_config_generate_all_configurations,
            )
        )
        result = self.execute_module(changed=True, failed=False)
        self.assert_success_result_message(result, self._testMethodName)

        self.assertEqual(
            self.run_dnac_exec.call_count,
            2,
            "Expected two paginated get_sites calls for 620 synthetic records.",
        )
        self.assert_get_sites_api_call(0, {"offset": 1, "limit": 500})
        self.assert_get_sites_api_call(1, {"offset": 501, "limit": 500})

        result_payload = (
            result.get("msg")
            if isinstance(result.get("msg"), dict)
            else result.get("response")
        )
        self.assertEqual(
            result_payload.get("configurations_count"),
            620,
            (
                "Expected all 620 records to be included in generated payload "
                "when pagination spans more than 500 records."
            ),
        )

    @patch("builtins.open", new_callable=mock_open)
    @patch("os.path.exists")
    def test_site_playbook_config_generator_duplicate_site_type_input_dedupes_api_calls(
        self, mock_exists, mock_file
    ):
        """
        Validate duplicate site_type values are deduped to a single API query.
        """
        mock_exists.return_value = True

        duplicate_site_type_config = {
            "file_path": "/tmp/case_duplicate_site_type.yaml",
            "component_specific_filters": {
                "components_list": ["site"],
                "site": [{"site_type": ["area", "area"]}],
            },
        }
        set_module_args(
            dict(
                dnac_host="1.1.1.1",
                dnac_username="dummy",
                dnac_password="dummy",
                dnac_version="2.3.7.9",
                dnac_log=True,
                dnac_log_level="DEBUG",
                state="gathered",
                config=duplicate_site_type_config,
            )
        )
        result = self.execute_module(changed=True, failed=False)
        self.assert_success_result_message(result, self._testMethodName)
        self.assertEqual(
            self.run_dnac_exec.call_count,
            1,
            "Expected one API call after deduping duplicate site_type values.",
        )
        self.assert_get_sites_api_call(0, {"type": "area", "offset": 1, "limit": 500})

    def test_site_playbook_config_generator_invalid_site_type_value_fails_validation(
        self,
    ):
        """
        Validate invalid site_type values fail with a clear validation error.
        """
        invalid_site_type_config = {
            "file_path": "/tmp/case_invalid_site_type.yaml",
            "component_specific_filters": {
                "components_list": ["site"],
                "site": [{"site_type": ["campus"]}],
            },
        }
        set_module_args(
            dict(
                dnac_host="1.1.1.1",
                dnac_username="dummy",
                dnac_password="dummy",
                dnac_version="2.3.7.9",
                dnac_log=True,
                dnac_log_level="DEBUG",
                state="gathered",
                config=invalid_site_type_config,
            )
        )
        result = self.execute_module(changed=False, failed=True)
        self.assertIn("Invalid 'site_type' values", str(result.get("msg")))
        self.assertIn("campus", str(result.get("msg")))
        self.assertEqual(
            self.run_dnac_exec.call_count,
            0,
            "Expected no API execution for invalid site_type validation failure.",
        )

    def test_site_playbook_config_generator_rejects_list_config_type(self):
        """
        Validate top-level config must be a dictionary.
        """
        list_config = [
            {
                "generate_all_configurations": True,
            }
        ]
        set_module_args(
            dict(
                dnac_host="1.1.1.1",
                dnac_username="dummy",
                dnac_password="dummy",
                dnac_version="2.3.7.9",
                dnac_log=True,
                dnac_log_level="DEBUG",
                state="gathered",
                config=list_config,
            )
        )
        result = self.execute_module(changed=False, failed=True)
        self.assertIn("unable to convert to dict", str(result.get("msg")))
        self.assertEqual(
            self.run_dnac_exec.call_count,
            0,
            "Expected no API execution when top-level config type is invalid.",
        )

    def test_site_playbook_config_generator_rejects_multiple_config_elements_list_type(
        self,
    ):
        """
        Validate multi-item config lists are rejected; config must be a single dict.
        """
        multi_item_list_config = [
            {
                "generate_all_configurations": True,
            },
            {
                "file_path": "/tmp/second_config.yaml",
            },
        ]
        set_module_args(
            dict(
                dnac_host="1.1.1.1",
                dnac_username="dummy",
                dnac_password="dummy",
                dnac_version="2.3.7.9",
                dnac_log=True,
                dnac_log_level="DEBUG",
                state="gathered",
                config=multi_item_list_config,
            )
        )
        result = self.execute_module(changed=False, failed=True)
        self.assertIn("unable to convert to dict", str(result.get("msg")))
        self.assertEqual(
            self.run_dnac_exec.call_count,
            0,
            "Expected no API execution when multiple config elements are provided as a list.",
        )

    def test_site_playbook_config_generator_generate_all_false_without_component_filters_fails_validation(
        self,
    ):
        """
        Validate generate_all_configurations=False requires component_specific_filters.components_list.
        """
        invalid_minimum_requirement_config = {
            "generate_all_configurations": False,
        }
        set_module_args(
            dict(
                dnac_host="1.1.1.1",
                dnac_username="dummy",
                dnac_password="dummy",
                dnac_version="2.3.7.9",
                dnac_log=True,
                dnac_log_level="DEBUG",
                state="gathered",
                config=invalid_minimum_requirement_config,
            )
        )
        result = self.execute_module(changed=False, failed=True)
        self.assertIn(
            "'component_specific_filters' must be provided with 'components_list' key "
            "when 'generate_all_configurations' is set to False",
            str(result.get("msg")),
        )
        self.assertEqual(
            self.run_dnac_exec.call_count,
            0,
            "Expected no API execution when minimum filter requirements are not met.",
        )

    @patch("builtins.open", new_callable=mock_open)
    @patch("os.path.exists")
    def test_site_playbook_config_generator_file_mode_append_uses_append_write_mode(
        self, mock_exists, mock_file
    ):
        """
        Validate file_mode=append writes generated YAML using append mode.
        """
        mock_exists.return_value = True

        append_mode_config = {
            "file_path": "/tmp/case_append_mode.yaml",
            "file_mode": "append",
            "component_specific_filters": {
                "components_list": ["site"],
                "site": [{"site_type": ["area"]}],
            },
        }
        set_module_args(
            dict(
                dnac_host="1.1.1.1",
                dnac_username="dummy",
                dnac_password="dummy",
                dnac_version="2.3.7.9",
                dnac_log=True,
                dnac_log_level="DEBUG",
                state="gathered",
                config=append_mode_config,
            )
        )
        result = self.execute_module(changed=True, failed=False)
        self.assert_success_result_message(result, self._testMethodName)
        mock_file.assert_any_call("/tmp/case_append_mode.yaml", "a")

    @patch("builtins.open", new_callable=mock_open)
    @patch("os.path.exists")
    def test_site_playbook_config_generator_area_by_site_name_single(
        self, mock_exists, mock_file
    ):
        """
        Test case for generating YAML configuration for a single area by name hierarchy.

        This test verifies that the generator correctly retrieves and generates configuration
        for a single area when filtered by name hierarchy.
        """
        mock_exists.return_value = True

        set_module_args(
            dict(
                dnac_host="1.1.1.1",
                dnac_username="dummy",
                dnac_password="dummy",
                dnac_version="2.3.7.9",
                dnac_log=True,
                dnac_log_level="DEBUG",
                state="gathered",
                config=self.playbook_config_area_by_site_name_single,
            )
        )
        result = self.execute_module(changed=True, failed=False)
        self.assert_success_result_message(result, self._testMethodName)

    @patch("builtins.open", new_callable=mock_open)
    @patch("os.path.exists")
    def test_site_playbook_config_generator_area_by_site_name_single_api_invocation(
        self, mock_exists, mock_file
    ):
        """
        Verify API params for exact site_name_hierarchy + site_type query.
        """
        mock_exists.return_value = True
        self.run_module_with_config_and_validate_success(
            self.playbook_config_area_by_site_name_single
        )

        self.assertEqual(self.run_dnac_exec.call_count, 1)
        self.assert_get_sites_api_call(
            0,
            {
                "nameHierarchy": "Global/USA",
                "type": "area",
                "offset": 1,
                "limit": 500,
            },
        )

    @patch("builtins.open", new_callable=mock_open)
    @patch("os.path.exists")
    def test_site_playbook_config_generator_area_by_site_name_multiple(
        self, mock_exists, mock_file
    ):
        """
        Test case for generating YAML configuration for multiple areas by name hierarchies.

        This test verifies that the generator correctly retrieves and generates configuration
        for multiple areas when filtered by multiple name hierarchies.
        """
        mock_exists.return_value = True

        set_module_args(
            dict(
                dnac_host="1.1.1.1",
                dnac_username="dummy",
                dnac_password="dummy",
                dnac_version="2.3.7.9",
                dnac_log=True,
                dnac_log_level="DEBUG",
                state="gathered",
                config=self.playbook_config_area_by_site_name_multiple,
            )
        )
        result = self.execute_module(changed=True, failed=False)
        self.assert_success_result_message(result, self._testMethodName)

    @patch("builtins.open", new_callable=mock_open)
    @patch("os.path.exists")
    def test_site_playbook_config_generator_area_by_parent_site_api_invocation(
        self, mock_exists, mock_file
    ):
        """
        Verify API params for parentNameHierarchy filter scenario.

        parent_name_hierarchy is translated to a nameHierarchy scope pattern.
        """
        mock_exists.return_value = True
        self.run_module_with_config_and_validate_success(
            self.playbook_config_area_by_parent_site
        )

        self.assertEqual(self.run_dnac_exec.call_count, 1)
        self.assert_get_sites_api_call(
            0,
            {
                "nameHierarchy": "Global/.*",
                "type": "area",
                "offset": 1,
                "limit": 500,
            },
        )
        params = self.run_dnac_exec.call_args_list[0].kwargs.get("params") or {}
        self.assertNotIn("parentNameHierarchy", params)

    @patch("builtins.open", new_callable=mock_open)
    @patch("os.path.exists")
    def test_site_playbook_config_generator_area_by_parent_site(
        self, mock_exists, mock_file
    ):
        """
        Test case for generating YAML configuration for areas by parent name hierarchy.

        This test verifies that the generator correctly retrieves and generates configuration
        for areas when filtered by parent name hierarchy.
        """
        mock_exists.return_value = True

        set_module_args(
            dict(
                dnac_host="1.1.1.1",
                dnac_username="dummy",
                dnac_password="dummy",
                dnac_version="2.3.7.9",
                dnac_log=True,
                dnac_log_level="DEBUG",
                state="gathered",
                config=self.playbook_config_area_by_parent_site,
            )
        )
        result = self.execute_module(changed=True, failed=False)
        self.assert_success_result_message(result, self._testMethodName)

    @patch("builtins.open", new_callable=mock_open)
    @patch("os.path.exists")
    def test_site_playbook_config_generator_building_by_site_name_single(
        self, mock_exists, mock_file
    ):
        """
        Test case for generating YAML configuration for a single building by name hierarchy.

        This test verifies that the generator correctly retrieves and generates configuration
        for a single building when filtered by name hierarchy.
        """
        mock_exists.return_value = True

        set_module_args(
            dict(
                dnac_host="1.1.1.1",
                dnac_username="dummy",
                dnac_password="dummy",
                dnac_version="2.3.7.9",
                dnac_log=True,
                dnac_log_level="DEBUG",
                state="gathered",
                config=self.playbook_config_building_by_site_name_single,
            )
        )
        result = self.execute_module(changed=True, failed=False)
        self.assert_success_result_message(result, self._testMethodName)

    @patch("builtins.open", new_callable=mock_open)
    @patch("os.path.exists")
    def test_site_playbook_config_generator_building_by_site_name_multiple(
        self, mock_exists, mock_file
    ):
        """
        Test case for generating YAML configuration for multiple buildings by name hierarchies.

        This test verifies that the generator correctly retrieves and generates configuration
        for multiple buildings when filtered by multiple name hierarchies.
        """
        mock_exists.return_value = True

        set_module_args(
            dict(
                dnac_host="1.1.1.1",
                dnac_username="dummy",
                dnac_password="dummy",
                dnac_version="2.3.7.9",
                dnac_log=True,
                dnac_log_level="DEBUG",
                state="gathered",
                config=self.playbook_config_building_by_site_name_multiple,
            )
        )
        result = self.execute_module(changed=True, failed=False)
        self.assert_success_result_message(result, self._testMethodName)

    @patch("builtins.open", new_callable=mock_open)
    @patch("os.path.exists")
    def test_site_playbook_config_generator_building_by_parent_site(
        self, mock_exists, mock_file
    ):
        """
        Test case for generating YAML configuration for buildings by parent name hierarchy.

        This test verifies that the generator correctly retrieves and generates configuration
        for buildings when filtered by parent name hierarchy.
        """
        mock_exists.return_value = True

        set_module_args(
            dict(
                dnac_host="1.1.1.1",
                dnac_username="dummy",
                dnac_password="dummy",
                dnac_version="2.3.7.9",
                dnac_log=True,
                dnac_log_level="DEBUG",
                state="gathered",
                config=self.playbook_config_building_by_parent_site,
            )
        )
        result = self.execute_module(changed=True, failed=False)
        self.assert_success_result_message(result, self._testMethodName)

    @patch("builtins.open", new_callable=mock_open)
    @patch("os.path.exists")
    def test_site_playbook_config_generator_floor_by_site_name_single(
        self, mock_exists, mock_file
    ):
        """
        Test case for generating YAML configuration for a single floor by name hierarchy.

        This test verifies that the generator correctly retrieves and generates configuration
        for a single floor when filtered by name hierarchy.
        """
        mock_exists.return_value = True

        set_module_args(
            dict(
                dnac_host="1.1.1.1",
                dnac_username="dummy",
                dnac_password="dummy",
                dnac_version="2.3.7.9",
                dnac_log=True,
                dnac_log_level="DEBUG",
                state="gathered",
                config=self.playbook_config_floor_by_site_name_single,
            )
        )
        result = self.execute_module(changed=True, failed=False)
        self.assert_success_result_message(result, self._testMethodName)

    @patch("builtins.open", new_callable=mock_open)
    @patch("os.path.exists")
    def test_site_playbook_config_generator_floor_by_site_name_multiple(
        self, mock_exists, mock_file
    ):
        """
        Test case for generating YAML configuration for multiple floors by name hierarchies.

        This test verifies that the generator correctly retrieves and generates configuration
        for multiple floors when filtered by multiple name hierarchies.
        """
        mock_exists.return_value = True

        set_module_args(
            dict(
                dnac_host="1.1.1.1",
                dnac_username="dummy",
                dnac_password="dummy",
                dnac_version="2.3.7.9",
                dnac_log=True,
                dnac_log_level="DEBUG",
                state="gathered",
                config=self.playbook_config_floor_by_site_name_multiple,
            )
        )
        result = self.execute_module(changed=True, failed=False)
        self.assert_success_result_message(result, self._testMethodName)

    @patch("builtins.open", new_callable=mock_open)
    @patch("os.path.exists")
    def test_site_playbook_config_generator_floor_by_parent_site(
        self, mock_exists, mock_file
    ):
        """
        Test case for generating YAML configuration for floors by parent name hierarchy.

        This test verifies that the generator correctly retrieves and generates configuration
        for floors when filtered by parent name hierarchy.
        """
        mock_exists.return_value = True

        set_module_args(
            dict(
                dnac_host="1.1.1.1",
                dnac_username="dummy",
                dnac_password="dummy",
                dnac_version="2.3.7.9",
                dnac_log=True,
                dnac_log_level="DEBUG",
                state="gathered",
                config=self.playbook_config_floor_by_parent_site,
            )
        )
        result = self.execute_module(changed=True, failed=False)
        self.assert_success_result_message(result, self._testMethodName)

    @patch("builtins.open", new_callable=mock_open)
    @patch("os.path.exists")
    def test_site_playbook_config_generator_area_combined_filters(
        self, mock_exists, mock_file
    ):
        """
        Test case for generating YAML configuration for areas using combined filters.

        This test verifies that the generator correctly retrieves and generates
        configuration for areas when name hierarchy, parent name hierarchy, and
        type filters are provided together.
        """
        mock_exists.return_value = True

        set_module_args(
            dict(
                dnac_host="1.1.1.1",
                dnac_username="dummy",
                dnac_password="dummy",
                dnac_version="2.3.7.9",
                dnac_log=True,
                dnac_log_level="DEBUG",
                state="gathered",
                config=self.playbook_config_area_combined_filters,
            )
        )
        result = self.execute_module(changed=True, failed=False)
        self.assert_success_result_message(result, self._testMethodName)

    @patch("builtins.open", new_callable=mock_open)
    @patch("os.path.exists")
    def test_site_playbook_config_generator_floor_combined_filters(
        self, mock_exists, mock_file
    ):
        """
        Test case for generating YAML configuration for floors using combined filters.

        This test verifies that the generator correctly retrieves and generates
        configuration for floors when parent name hierarchy and type filters
        are provided together.
        """
        mock_exists.return_value = True

        set_module_args(
            dict(
                dnac_host="1.1.1.1",
                dnac_username="dummy",
                dnac_password="dummy",
                dnac_version="2.3.7.9",
                dnac_log=True,
                dnac_log_level="DEBUG",
                state="gathered",
                config=self.playbook_config_floor_combined_filters,
            )
        )
        result = self.execute_module(changed=True, failed=False)
        self.assert_success_result_message(result, self._testMethodName)

    @patch("builtins.open", new_callable=mock_open)
    @patch("os.path.exists")
    def test_site_playbook_config_generator_areas_and_buildings(
        self, mock_exists, mock_file
    ):
        """
        Test case for generating YAML configuration for areas and buildings.

        This test verifies that the generator correctly retrieves and generates configuration
        for both areas and buildings when both component types are requested.
        """
        mock_exists.return_value = True

        set_module_args(
            dict(
                dnac_host="1.1.1.1",
                dnac_username="dummy",
                dnac_password="dummy",
                dnac_version="2.3.7.9",
                dnac_log=True,
                dnac_log_level="DEBUG",
                state="gathered",
                config=self.playbook_config_areas_and_buildings,
            )
        )
        result = self.execute_module(changed=True, failed=False)
        self.assert_success_result_message(result, self._testMethodName)

    @patch("builtins.open", new_callable=mock_open)
    @patch("os.path.exists")
    def test_site_playbook_config_generator_buildings_and_floors(
        self, mock_exists, mock_file
    ):
        """
        Test case for generating YAML configuration for buildings and floors.

        This test verifies that the generator correctly retrieves and generates configuration
        for both buildings and floors when both component types are requested.
        """
        mock_exists.return_value = True

        set_module_args(
            dict(
                dnac_host="1.1.1.1",
                dnac_username="dummy",
                dnac_password="dummy",
                dnac_version="2.3.7.9",
                dnac_log=True,
                dnac_log_level="DEBUG",
                state="gathered",
                config=self.playbook_config_buildings_and_floors,
            )
        )
        result = self.execute_module(changed=True, failed=False)
        self.assert_success_result_message(result, self._testMethodName)

    @patch("builtins.open", new_callable=mock_open)
    @patch("os.path.exists")
    def test_site_playbook_config_generator_all_components(
        self, mock_exists, mock_file
    ):
        """
        Test case for generating YAML configuration for all site components.

        This test verifies that the generator correctly retrieves and generates configuration
        for areas, buildings, and floors when all component types are requested.
        """
        mock_exists.return_value = True

        set_module_args(
            dict(
                dnac_host="1.1.1.1",
                dnac_username="dummy",
                dnac_password="dummy",
                dnac_version="2.3.7.9",
                dnac_log=True,
                dnac_log_level="DEBUG",
                state="gathered",
                config=self.playbook_config_all_components,
            )
        )
        result = self.execute_module(changed=True, failed=False)
        self.assert_success_result_message(result, self._testMethodName)

    @patch("builtins.open", new_callable=mock_open)
    @patch("os.path.exists")
    def test_site_playbook_config_generator_empty_filters(self, mock_exists, mock_file):
        """
        Test case for generating YAML configuration with empty filters.

        This test verifies that the generator correctly handles the case where
        component_specific_filters are provided but no actual filter criteria are specified.
        """
        mock_exists.return_value = True

        set_module_args(
            dict(
                dnac_host="1.1.1.1",
                dnac_username="dummy",
                dnac_password="dummy",
                dnac_version="2.3.7.9",
                dnac_log=True,
                dnac_log_level="DEBUG",
                state="gathered",
                config=self.playbook_config_empty_filters,
            )
        )
        result = self.execute_module(changed=True, failed=False)
        self.assert_success_result_message(result, self._testMethodName)

    @patch("builtins.open", new_callable=mock_open)
    @patch("os.path.exists")
    def test_site_playbook_config_generator_no_file_path(self, mock_exists, mock_file):
        """
        Test case for generating YAML configuration without specifying file path.

        This test verifies that the generator correctly generates a default file name
        when no file_path is provided in the configuration.
        """
        mock_exists.return_value = True

        set_module_args(
            dict(
                dnac_host="1.1.1.1",
                dnac_username="dummy",
                dnac_password="dummy",
                dnac_version="2.3.7.9",
                dnac_log=True,
                dnac_log_level="DEBUG",
                state="gathered",
                config=self.playbook_config_no_file_path,
            )
        )
        result = self.execute_module(changed=True, failed=False)
        self.assert_success_result_message(result, self._testMethodName)

    @patch("builtins.open", new_callable=mock_open)
    @patch("os.path.exists")
    def test_site_playbook_config_generator_direct_filter_components_list_name_hierarchy(
        self, mock_exists, mock_file
    ):
        """
        Test case for using direct filter-style components_list values.

        This validates that components_list entries such as "nameHierarchy"
        are normalized to internal site components before module validation.
        """
        mock_exists.return_value = True

        set_module_args(
            dict(
                dnac_host="1.1.1.1",
                dnac_username="dummy",
                dnac_password="dummy",
                dnac_version="2.3.7.9",
                dnac_log=True,
                dnac_log_level="DEBUG",
                state="gathered",
                config=self.playbook_config_direct_filter_components_list_name_hierarchy,
            )
        )
        result = self.execute_module(changed=True, failed=False)
        self.assert_success_result_message(result, self._testMethodName)

    @patch("builtins.open", new_callable=mock_open)
    @patch("os.path.exists")
    def test_site_playbook_config_generator_direct_filter_components_list_name_hierarchy_api_invocation(
        self, mock_exists, mock_file
    ):
        """
        Verify one-pass API retrieval in direct-filter mode.

        components_list: ["site"] with only site_name_hierarchy should execute a
        single scoped get_sites call without site_type fanout.
        """
        mock_exists.return_value = True
        self.run_module_with_config_and_validate_success(
            self.playbook_config_direct_filter_components_list_name_hierarchy
        )

        self.assertEqual(self.run_dnac_exec.call_count, 1)
        self.assert_get_sites_api_call(
            0,
            {"nameHierarchy": "Global/USA", "offset": 1, "limit": 500},
        )
        params = self.run_dnac_exec.call_args_list[0].kwargs.get("params") or {}
        self.assertNotIn("type", params)
        self.assertNotIn("parentNameHierarchy", params)

    @patch("builtins.open", new_callable=mock_open)
    @patch("os.path.exists")
    def test_site_playbook_config_generator_name_hierarchy_pattern_api_invocation(
        self, mock_exists, mock_file
    ):
        """
        Verify wildcard site_name_hierarchy with site_type list fans out by type.
        """
        mock_exists.return_value = True
        self.run_module_with_config_and_validate_success(
            self.playbook_config_name_hierarchy_pattern
        )

        self.assertEqual(self.run_dnac_exec.call_count, 3)
        expected_site_types = set(["area", "building", "floor"])
        observed_site_types = set()

        for call_index, call in enumerate(self.run_dnac_exec.call_args_list):
            self.assert_get_sites_api_call(
                call_index,
                {"nameHierarchy": "Global/USA/.*", "offset": 1, "limit": 500},
            )
            params = call.kwargs.get("params") or {}
            self.assertNotIn("parentNameHierarchy", params)
            observed_site_types.add(params.get("type"))

        self.assertSetEqual(observed_site_types, expected_site_types)

    @patch("builtins.open", new_callable=mock_open)
    @patch("os.path.exists")
    def test_site_playbook_config_generator_parent_name_hierarchy_pattern_api_invocation(
        self, mock_exists, mock_file
    ):
        """
        Verify parent_name_hierarchy scope with site_type list fans out by type.
        """
        mock_exists.return_value = True
        self.run_module_with_config_and_validate_success(
            self.playbook_config_parent_name_hierarchy_pattern
        )

        self.assertEqual(self.run_dnac_exec.call_count, 3)
        expected_site_types = set(["area", "building", "floor"])
        observed_site_types = set()

        for call_index, call in enumerate(self.run_dnac_exec.call_args_list):
            self.assert_get_sites_api_call(
                call_index,
                {"nameHierarchy": "Global/USA/.*", "offset": 1, "limit": 500},
            )
            params = call.kwargs.get("params") or {}
            self.assertNotIn("parentNameHierarchy", params)
            observed_site_types.add(params.get("type"))

        self.assertSetEqual(observed_site_types, expected_site_types)

    @patch("builtins.open", new_callable=mock_open)
    @patch("os.path.exists")
    def test_site_playbook_config_generator_combined_hierarchy_patterns_api_invocation(
        self, mock_exists, mock_file
    ):
        """
        Verify combined hierarchy + site_type filters are planned as typed calls.
        """
        mock_exists.return_value = True
        self.run_module_with_config_and_validate_success(
            self.playbook_config_combined_hierarchy_patterns
        )

        self.assertEqual(self.run_dnac_exec.call_count, 3)
        expected_site_types = set(["area", "building", "floor"])
        observed_site_types = set()

        for call_index, call in enumerate(self.run_dnac_exec.call_args_list):
            self.assert_get_sites_api_call(
                call_index,
                {"nameHierarchy": "Global/USA/.*", "offset": 1, "limit": 500},
            )
            params = call.kwargs.get("params") or {}
            self.assertNotIn("parentNameHierarchy", params)
            observed_site_types.add(params.get("type"))

        self.assertSetEqual(observed_site_types, expected_site_types)

    def test_parent_name_hierarchy_scope_includes_descendants(self):
        """
        Test hierarchical scope behavior for parentNameHierarchy post-filtering.

        This validates that a scope such as "Global/USA" includes matching node
        and descendant records (for example area, building, and floor paths under
        that hierarchy).
        """
        site_generator = self.module.SitePlaybookGenerator.__new__(
            self.module.SitePlaybookGenerator
        )
        site_generator.log = lambda *args, **kwargs: None

        details = [
            {
                "nameHierarchy": "Global/USA",
                "parentNameHierarchy": "Global",
                "type": "area",
            },
            {
                "nameHierarchy": "Global/USA/San Jose/Building1",
                "parentNameHierarchy": "Global/USA/San Jose",
                "type": "building",
            },
            {
                "nameHierarchy": "Global/USA/San Jose/Building1/Floor1",
                "parentNameHierarchy": "Global/USA/San Jose/Building1",
                "type": "floor",
            },
            {
                "nameHierarchy": "Global/Europe",
                "parentNameHierarchy": "Global",
                "type": "area",
            },
        ]

        filtered = site_generator.apply_site_post_filters(
            details, {"parentNameHierarchy": "Global/USA"}
        )

        filtered_hierarchies = {item.get("nameHierarchy") for item in filtered}
        self.assertIn(
            "Global/USA",
            filtered_hierarchies,
            (
                "Expected root scope hierarchy 'Global/USA' to be retained when "
                "filtering with parentNameHierarchy='Global/USA'."
            ),
        )
        self.assertIn(
            "Global/USA/San Jose/Building1",
            filtered_hierarchies,
            (
                "Expected building hierarchy descendant under 'Global/USA' to be "
                "retained by hierarchical scope filtering."
            ),
        )
        self.assertIn(
            "Global/USA/San Jose/Building1/Floor1",
            filtered_hierarchies,
            (
                "Expected floor hierarchy descendant under "
                "'Global/USA/San Jose/Building1' to be retained by hierarchical "
                "scope filtering."
            ),
        )
        self.assertNotIn("Global/Europe", filtered_hierarchies)

    def test_name_hierarchy_pattern_filter_includes_descendants(self):
        """
        Validate wildcard nameHierarchy filtering for descendant paths.

        This test ensures that `nameHierarchy: Global/USA/.*` matches
        descendants under `Global/USA/` while excluding unrelated hierarchies.
        """
        site_generator = self.module.SitePlaybookGenerator.__new__(
            self.module.SitePlaybookGenerator
        )
        site_generator.log = lambda *args, **kwargs: None

        details = [
            {
                "nameHierarchy": "Global/USA",
                "parentNameHierarchy": "Global",
                "type": "area",
            },
            {
                "nameHierarchy": "Global/USA/San Jose/Building1",
                "parentNameHierarchy": "Global/USA/San Jose",
                "type": "building",
            },
            {
                "nameHierarchy": "Global/USA/San Jose/Building1/Floor1",
                "parentNameHierarchy": "Global/USA/San Jose/Building1",
                "type": "floor",
            },
            {
                "nameHierarchy": "Global/Europe/London",
                "parentNameHierarchy": "Global/Europe",
                "type": "building",
            },
        ]

        filtered = site_generator.apply_site_post_filters(
            details, {"nameHierarchy": "Global/USA/.*"}
        )

        filtered_hierarchies = {item.get("nameHierarchy") for item in filtered}
        self.assertNotIn(
            "Global/USA",
            filtered_hierarchies,
            (
                "Expected 'Global/USA' to be excluded because wildcard filter "
                "'Global/USA/.*' targets descendants with one or more additional "
                "path segments."
            ),
        )
        self.assertIn(
            "Global/USA/San Jose/Building1",
            filtered_hierarchies,
            (
                "Expected building under 'Global/USA/' to match wildcard "
                "nameHierarchy filter."
            ),
        )
        self.assertIn(
            "Global/USA/San Jose/Building1/Floor1",
            filtered_hierarchies,
            (
                "Expected floor under 'Global/USA/' to match wildcard "
                "nameHierarchy filter."
            ),
        )
        self.assertNotIn("Global/Europe/London", filtered_hierarchies)

    def test_build_site_query_context_name_hierarchy_pattern_uses_post_filter(self):
        """
        Ensure wildcard nameHierarchy values are evaluated as local post-filters.

        API params should retain only fixed values (such as component type),
        while the wildcard expression is moved to post-filter evaluation.
        """
        site_generator = self.module.SitePlaybookGenerator.__new__(
            self.module.SitePlaybookGenerator
        )
        site_generator.log = lambda *args, **kwargs: None

        params, post_filters = site_generator.build_site_query_context(
            {"nameHierarchy": "Global/USA/.*", "type": "building"},
            "building",
        )

        self.assertEqual(
            params.get("type"),
            "building",
            "Expected component type to remain in API params for query context.",
        )
        self.assertNotIn(
            "nameHierarchy",
            params,
            (
                "Expected wildcard nameHierarchy filter to be excluded from API "
                "query params and applied locally as a post-filter."
            ),
        )
        self.assertEqual(
            post_filters.get("nameHierarchy"),
            "Global/USA/.*",
            "Expected wildcard nameHierarchy filter to be present in post_filters.",
        )

    def test_build_site_query_context_combined_hierarchy_patterns_use_post_filters(
        self,
    ):
        """
        Validate combined hierarchy patterns are fully retained as post-filters.
        """
        site_generator = self.module.SitePlaybookGenerator.__new__(
            self.module.SitePlaybookGenerator
        )
        site_generator.log = lambda *args, **kwargs: None

        params, post_filters = site_generator.build_site_query_context(
            {
                "nameHierarchy": "Global/USA/.*",
                "parentNameHierarchy": "Global/USA/.*",
                "type": "floor",
            },
            "floor",
        )

        self.assertEqual(params.get("type"), "floor")
        self.assertNotIn("nameHierarchy", params)
        self.assertEqual(post_filters.get("nameHierarchy"), "Global/USA/.*")
        self.assertEqual(post_filters.get("parentNameHierarchy"), "Global/USA/.*")

    def test_parent_name_hierarchy_pattern_filter_includes_descendants(self):
        """
        Validate wildcard parentNameHierarchy filtering for descendant paths.

        This test ensures that `parentNameHierarchy: Global/USA/.*` matches
        descendants below `Global/USA/` and excludes unrelated hierarchies.
        """
        site_generator = self.module.SitePlaybookGenerator.__new__(
            self.module.SitePlaybookGenerator
        )
        site_generator.log = lambda *args, **kwargs: None

        details = [
            {
                "nameHierarchy": "Global/USA",
                "parentNameHierarchy": "Global",
                "type": "area",
            },
            {
                "nameHierarchy": "Global/USA/San Jose",
                "parentNameHierarchy": "Global/USA",
                "type": "area",
            },
            {
                "nameHierarchy": "Global/USA/San Jose/Building1",
                "parentNameHierarchy": "Global/USA/San Jose",
                "type": "building",
            },
            {
                "nameHierarchy": "Global/USA/San Jose/Building1/Floor1",
                "parentNameHierarchy": "Global/USA/San Jose/Building1",
                "type": "floor",
            },
            {
                "nameHierarchy": "Global/Europe/London",
                "parentNameHierarchy": "Global/Europe",
                "type": "area",
            },
        ]

        filtered = site_generator.apply_site_post_filters(
            details, {"parentNameHierarchy": "Global/USA/.*"}
        )

        filtered_hierarchies = {item.get("nameHierarchy") for item in filtered}
        self.assertNotIn(
            "Global/USA",
            filtered_hierarchies,
            (
                "Expected 'Global/USA' to be excluded because wildcard scope "
                "'Global/USA/.*' targets descendants with additional path segments."
            ),
        )
        self.assertIn(
            "Global/USA/San Jose",
            filtered_hierarchies,
            (
                "Expected descendant area under 'Global/USA/' to match wildcard "
                "parentNameHierarchy scope."
            ),
        )
        self.assertIn(
            "Global/USA/San Jose/Building1",
            filtered_hierarchies,
            (
                "Expected building under 'Global/USA/' to match wildcard "
                "parentNameHierarchy scope."
            ),
        )
        self.assertIn(
            "Global/USA/San Jose/Building1/Floor1",
            filtered_hierarchies,
            (
                "Expected floor under 'Global/USA/' to match wildcard "
                "parentNameHierarchy scope."
            ),
        )
        self.assertNotIn("Global/Europe/London", filtered_hierarchies)

    def test_apply_site_post_filters_combined_pattern_filters_intersection(self):
        """
        Ensure combined nameHierarchy and parentNameHierarchy patterns intersect correctly.
        """
        site_generator = self.module.SitePlaybookGenerator.__new__(
            self.module.SitePlaybookGenerator
        )
        site_generator.log = lambda *args, **kwargs: None

        details = [
            {
                "nameHierarchy": "Global/USA/San_Jose/Building1",
                "parentNameHierarchy": "Global/USA/San_Jose",
                "type": "building",
            },
            {
                "nameHierarchy": "Global/USA/Seattle/Building1",
                "parentNameHierarchy": "Global/USA/Seattle",
                "type": "building",
            },
            {
                "nameHierarchy": "Global/USA/San_Jose/Building1/Floor1",
                "parentNameHierarchy": "Global/USA/San_Jose/Building1",
                "type": "floor",
            },
            {
                "nameHierarchy": "Global/Europe/London/Building2",
                "parentNameHierarchy": "Global/Europe/London",
                "type": "building",
            },
        ]
        filtered = site_generator.apply_site_post_filters(
            details,
            {
                "nameHierarchy": "Global/USA/.*",
                "parentNameHierarchy": "Global/USA/San_Jose/.*",
            },
        )

        filtered_hierarchies = {item.get("nameHierarchy") for item in filtered}
        self.assertIn("Global/USA/San_Jose/Building1", filtered_hierarchies)
        self.assertIn("Global/USA/San_Jose/Building1/Floor1", filtered_hierarchies)
        self.assertNotIn("Global/USA/Seattle/Building1", filtered_hierarchies)
        self.assertNotIn("Global/Europe/London/Building2", filtered_hierarchies)

    def test_hierarchy_matches_name_filter_invalid_regex_falls_back_to_exact_match(
        self,
    ):
        """
        Validate invalid regex input does not raise and falls back to exact matching.
        """
        site_generator = self.module.SitePlaybookGenerator.__new__(
            self.module.SitePlaybookGenerator
        )
        site_generator.log = lambda *args, **kwargs: None

        self.assertTrue(
            site_generator.hierarchy_matches_name_filter("Global/USA/[", "Global/USA/[")
        )
        self.assertFalse(
            site_generator.hierarchy_matches_name_filter(
                "Global/USA/San_Jose", "Global/USA/["
            )
        )

    def test_build_site_query_plan_for_filter_dedupes_duplicate_site_type_values(self):
        """
        Ensure duplicate site_type values do not produce duplicate API query params.
        """
        site_generator = self.module.SitePlaybookGenerator.__new__(
            self.module.SitePlaybookGenerator
        )
        site_generator.log = lambda *args, **kwargs: None

        query_plan = site_generator.build_site_query_plan_for_filter(
            {
                "site_name_hierarchy": "Global/USA/San Jose",
                "site_type": ["building", "building", "floor"],
            }
        )

        self.assertEqual(
            len(query_plan),
            2,
            "Expected duplicate site_type values to be deduplicated in query plan.",
        )
        self.assertEqual(query_plan[0].get("type"), "building")
        self.assertEqual(query_plan[1].get("type"), "floor")

    def test_validate_component_specific_filters_structure_invalid_site_type_value(self):
        """
        Ensure invalid site_type values fail validation with explicit value details.
        """
        site_generator = self.module.SitePlaybookGenerator.__new__(
            self.module.SitePlaybookGenerator
        )
        site_generator.log = lambda *args, **kwargs: None

        errors = site_generator.validate_component_specific_filters_structure(
            {
                "component_specific_filters": {
                    "components_list": ["site"],
                    "site": [{"site_type": ["campus"]}],
                }
            }
        )

        self.assertTrue(
            errors,
            "Expected validation errors for unsupported site_type value 'campus'.",
        )
        self.assertIn("Invalid 'site_type' values", errors[0])
        self.assertIn("campus", errors[0])

    def test_build_site_query_plan_for_filter_supports_site_name_hierarchy_list(self):
        """
        Ensure site_name_hierarchy list expands to one API query per hierarchy value.
        """
        site_generator = self.module.SitePlaybookGenerator.__new__(
            self.module.SitePlaybookGenerator
        )
        site_generator.log = lambda *args, **kwargs: None

        query_plan = site_generator.build_site_query_plan_for_filter(
            {
                "site_name_hierarchy": [
                    "Global/USA/San Jose",
                    "Global/India/Bangalore",
                ]
            }
        )

        self.assertEqual(
            query_plan,
            [
                {"nameHierarchy": "Global/USA/San Jose"},
                {"nameHierarchy": "Global/India/Bangalore"},
            ],
        )

    def test_build_site_query_plan_for_filter_supports_parent_name_hierarchy_list(self):
        """
        Ensure parent_name_hierarchy list expands to wildcard scope API queries.
        """
        site_generator = self.module.SitePlaybookGenerator.__new__(
            self.module.SitePlaybookGenerator
        )
        site_generator.log = lambda *args, **kwargs: None

        query_plan = site_generator.build_site_query_plan_for_filter(
            {
                "parent_name_hierarchy": [
                    "Global/USA",
                    "Global/India",
                ]
            }
        )

        self.assertEqual(
            query_plan,
            [
                {"nameHierarchy": "Global/USA/.*"},
                {"nameHierarchy": "Global/India/.*"},
            ],
        )

    def test_validate_component_specific_filters_structure_parent_and_site_list_invalid(
        self,
    ):
        """
        Ensure same-item parent/site hierarchy keys are rejected as ambiguous.
        """
        site_generator = self.module.SitePlaybookGenerator.__new__(
            self.module.SitePlaybookGenerator
        )
        site_generator.log = lambda *args, **kwargs: None

        errors = site_generator.validate_component_specific_filters_structure(
            {
                "component_specific_filters": {
                    "components_list": ["site"],
                    "site": [
                        {
                            "parent_name_hierarchy": [
                                "Global/USA",
                                "Global/India",
                            ],
                            "site_name_hierarchy": [
                                "Global/USA/San Francisco",
                                "Global/India/Bangalore",
                            ],
                        }
                    ],
                }
            }
        )

        self.assertTrue(
            errors,
            "Expected validation errors when parent_name_hierarchy and "
            "site_name_hierarchy are present in the same site filter item.",
        )
        self.assertIn("cannot be provided together", errors[0])

    def test_validate_component_specific_filters_structure_parent_site_prefix_mismatch_invalid(
        self,
    ):
        """
        Ensure same-item parent/site hierarchy keys fail validation, regardless of values.
        """
        site_generator = self.module.SitePlaybookGenerator.__new__(
            self.module.SitePlaybookGenerator
        )
        site_generator.log = lambda *args, **kwargs: None

        errors = site_generator.validate_component_specific_filters_structure(
            {
                "component_specific_filters": {
                    "components_list": ["site"],
                    "site": [
                        {
                            "site_name_hierarchy": "Global/India",
                            "parent_name_hierarchy": "Global/USA/San Jose",
                        }
                    ],
                }
            }
        )
        self.assertTrue(errors)
        self.assertIn("cannot be provided together", errors[0])

    def test_validate_component_specific_filters_structure_site_list_and_single_parent_invalid(
        self,
    ):
        """
        Ensure site_name_hierarchy list with a single parent_name_hierarchy value
        in one item is rejected as ambiguous.
        """
        site_generator = self.module.SitePlaybookGenerator.__new__(
            self.module.SitePlaybookGenerator
        )
        site_generator.log = lambda *args, **kwargs: None

        errors = site_generator.validate_component_specific_filters_structure(
            {
                "component_specific_filters": {
                    "components_list": ["site"],
                    "site": [
                        {
                            "site_name_hierarchy": [
                                "Global/USA/San Francisco",
                                "Global/USA/San Jose",
                            ],
                            "parent_name_hierarchy": ["Global/USA"],
                            "site_type": ["floor"],
                        }
                    ],
                }
            }
        )

        self.assertTrue(errors)
        self.assertIn("cannot be provided together", errors[0])

    def test_build_site_query_plan_for_filter_resolves_relative_site_name_with_parent(
        self,
    ):
        """
        Ensure same-item parent/site hierarchy filter is skipped as ambiguous.
        """
        site_generator = self.module.SitePlaybookGenerator.__new__(
            self.module.SitePlaybookGenerator
        )
        site_generator.log = lambda *args, **kwargs: None

        query_plan = site_generator.build_site_query_plan_for_filter(
            {
                "parent_name_hierarchy": "Global/USA",
                "site_name_hierarchy": ["San Francisco", "Global/USA/San Jose"],
                "site_type": ["floor"],
            }
        )

        self.assertEqual(query_plan, [])

    def test_build_site_query_plan_for_filter_parent_site_prefix_mismatch_returns_empty(
        self,
    ):
        """
        Ensure query plan is empty for parent/site hierarchy prefix mismatch.
        """
        site_generator = self.module.SitePlaybookGenerator.__new__(
            self.module.SitePlaybookGenerator
        )
        site_generator.log = lambda *args, **kwargs: None

        query_plan = site_generator.build_site_query_plan_for_filter(
            {
                "site_name_hierarchy": "Global/India",
                "parent_name_hierarchy": "Global/USA/San Jose",
            }
        )
        self.assertEqual(query_plan, [])

    def test_site_record_matches_filter_expression_with_relative_site_and_parent(self):
        """
        Ensure same-item parent/site hierarchy expression does not match records.
        """
        site_generator = self.module.SitePlaybookGenerator.__new__(
            self.module.SitePlaybookGenerator
        )
        site_generator.log = lambda *args, **kwargs: None

        detail = {
            "nameHierarchy": "Global/USA/San Francisco",
            "parentNameHierarchy": "Global/USA",
            "type": "area",
        }
        self.assertFalse(
            site_generator.site_record_matches_filter_expression(
                detail,
                {
                    "parent_name_hierarchy": "Global/USA",
                    "site_name_hierarchy": ["San Francisco"],
                    "site_type": ["area"],
                },
            )
        )

    @patch("builtins.open", new_callable=mock_open)
    @patch("os.path.exists")
    def test_site_playbook_config_generator_relative_site_name_with_parent_api_invocation(
        self, mock_exists, mock_file
    ):
        """
        Verify module fails validation when parent/site hierarchy keys are used
        together in one site filter item.
        """
        mock_exists.return_value = True

        relative_hierarchy_config = {
            "file_path": "/tmp/case_relative_site_name_parent.yaml",
            "component_specific_filters": {
                "components_list": ["site"],
                "site": [
                    {
                        "parent_name_hierarchy": "Global/USA",
                        "site_name_hierarchy": ["San Jose"],
                        "site_type": ["area"],
                    }
                ],
            },
        }

        set_module_args(
            dict(
                dnac_host="1.1.1.1",
                dnac_username="dummy",
                dnac_password="dummy",
                dnac_version="2.3.7.9",
                dnac_log=True,
                dnac_log_level="DEBUG",
                state="gathered",
                config=relative_hierarchy_config,
            )
        )
        result = self.execute_module(changed=False, failed=True)
        self.assertIn("cannot be provided together", str(result.get("msg")))
        self.assertEqual(
            self.run_dnac_exec.call_count,
            0,
            "Expected no API execution when same-item parent/site hierarchy is provided.",
        )

    def test_site_playbook_config_generator_parent_site_prefix_mismatch_fails_validation(
        self,
    ):
        """
        Validate module fails early when parent/site hierarchy keys are both set
        in one site filter item.
        """
        prefix_mismatch_config = {
            "component_specific_filters": {
                "components_list": ["site"],
                "site": [
                    {
                        "site_name_hierarchy": "Global/India",
                        "parent_name_hierarchy": "Global/USA/San Jose",
                    }
                ],
            }
        }
        set_module_args(
            dict(
                dnac_host="1.1.1.1",
                dnac_username="dummy",
                dnac_password="dummy",
                dnac_version="2.3.7.9",
                dnac_log=True,
                dnac_log_level="DEBUG",
                state="gathered",
                config=prefix_mismatch_config,
            )
        )
        result = self.execute_module(changed=False, failed=True)
        self.assertIn(
            "cannot be provided together",
            str(result.get("msg")),
        )
        self.assertEqual(
            self.run_dnac_exec.call_count,
            0,
            "Expected no API execution for hierarchy prefix mismatch validation failure.",
        )

    @patch("builtins.open", new_callable=mock_open)
    @patch("os.path.exists")
    def test_site_playbook_config_generator_file_mode_default_overwrite_uses_write_mode(
        self, mock_exists, mock_file
    ):
        """
        Validate default file_mode behavior uses overwrite mode when not provided.
        """
        mock_exists.return_value = True
        overwrite_default_config = {
            "file_path": "/tmp/case_default_overwrite_mode.yaml",
            "component_specific_filters": {
                "components_list": ["site"],
                "site": [{"site_type": ["area"]}],
            },
        }

        self.run_module_with_config_and_validate_success(overwrite_default_config)
        mock_file.assert_any_call("/tmp/case_default_overwrite_mode.yaml", "w")

    def test_site_playbook_config_generator_invalid_file_mode_fails_validation(self):
        """
        Validate invalid file_mode values are rejected before API execution.
        """
        invalid_file_mode_config = {
            "file_path": "/tmp/case_invalid_file_mode.yaml",
            "file_mode": "replace",
            "component_specific_filters": {
                "components_list": ["site"],
                "site": [{"site_type": ["area"]}],
            },
        }
        set_module_args(
            dict(
                dnac_host="1.1.1.1",
                dnac_username="dummy",
                dnac_password="dummy",
                dnac_version="2.3.7.9",
                dnac_log=True,
                dnac_log_level="DEBUG",
                state="gathered",
                config=invalid_file_mode_config,
            )
        )
        result = self.execute_module(changed=False, failed=True)
        self.assertIn("Invalid parameters in playbook", str(result.get("msg")))
        self.assertIn("Invalid choice provided", str(result.get("msg")))
        self.assertEqual(
            self.run_dnac_exec.call_count,
            0,
            "Expected no API execution for invalid file_mode value.",
        )

    def test_validate_component_specific_filters_structure_rejects_empty_site_name_hierarchy_list(
        self,
    ):
        """
        Ensure empty site_name_hierarchy list fails validation.
        """
        site_generator = self.module.SitePlaybookGenerator.__new__(
            self.module.SitePlaybookGenerator
        )
        site_generator.log = lambda *args, **kwargs: None

        errors = site_generator.validate_component_specific_filters_structure(
            {
                "component_specific_filters": {
                    "components_list": ["site"],
                    "site": [{"site_name_hierarchy": []}],
                }
            }
        )
        self.assertTrue(errors)
        self.assertIn("must not be an empty list", errors[0])

    def test_validate_component_specific_filters_structure_rejects_empty_parent_name_hierarchy_list(
        self,
    ):
        """
        Ensure empty parent_name_hierarchy list fails validation.
        """
        site_generator = self.module.SitePlaybookGenerator.__new__(
            self.module.SitePlaybookGenerator
        )
        site_generator.log = lambda *args, **kwargs: None

        errors = site_generator.validate_component_specific_filters_structure(
            {
                "component_specific_filters": {
                    "components_list": ["site"],
                    "site": [{"parent_name_hierarchy": []}],
                }
            }
        )
        self.assertTrue(errors)
        self.assertIn("must not be an empty list", errors[0])

    def test_validate_component_specific_filters_structure_rejects_non_string_site_name_hierarchy_list_items(
        self,
    ):
        """
        Ensure non-string items in site_name_hierarchy list fail validation.
        """
        site_generator = self.module.SitePlaybookGenerator.__new__(
            self.module.SitePlaybookGenerator
        )
        site_generator.log = lambda *args, **kwargs: None

        errors = site_generator.validate_component_specific_filters_structure(
            {
                "component_specific_filters": {
                    "components_list": ["site"],
                    "site": [{"site_name_hierarchy": ["Global/USA", 10]}],
                }
            }
        )
        self.assertTrue(errors)
        self.assertIn("must be a string or a list of strings", errors[0])

    def test_build_site_query_plan_for_filter_rejects_absolute_site_outside_parent_scope(
        self,
    ):
        """
        Ensure absolute site_name_hierarchy outside parent scope is rejected.
        """
        site_generator = self.module.SitePlaybookGenerator.__new__(
            self.module.SitePlaybookGenerator
        )
        site_generator.log = lambda *args, **kwargs: None

        query_plan = site_generator.build_site_query_plan_for_filter(
            {
                "parent_name_hierarchy": "Global/USA",
                "site_name_hierarchy": ["Global/India/Bangalore"],
            }
        )
        self.assertEqual(
            query_plan,
            [],
            "Expected query plan to be empty when absolute site hierarchy is outside parent scope.",
        )

    def test_build_site_query_plan_for_filter_dedupes_resolved_relative_site_hierarchy_values(
        self,
    ):
        """
        Ensure same-item parent/site hierarchy query plans are rejected as ambiguous.
        """
        site_generator = self.module.SitePlaybookGenerator.__new__(
            self.module.SitePlaybookGenerator
        )
        site_generator.log = lambda *args, **kwargs: None

        query_plan = site_generator.build_site_query_plan_for_filter(
            {
                "parent_name_hierarchy": "Global/USA",
                "site_name_hierarchy": [
                    "San Jose",
                    "Global/USA/San Jose",
                    "San Jose",
                ],
                "site_type": ["building"],
            }
        )
        self.assertEqual(query_plan, [])

    def test_build_site_query_plan_for_filter_parent_list_with_site_type_cross_product(
        self,
    ):
        """
        Ensure parent_name_hierarchy list with site_type list expands as expected.
        """
        site_generator = self.module.SitePlaybookGenerator.__new__(
            self.module.SitePlaybookGenerator
        )
        site_generator.log = lambda *args, **kwargs: None

        query_plan = site_generator.build_site_query_plan_for_filter(
            {
                "parent_name_hierarchy": ["Global/USA", "Global/India"],
                "site_type": ["area", "floor"],
            }
        )
        self.assertEqual(
            query_plan,
            [
                {"nameHierarchy": "Global/USA/.*", "type": "area"},
                {"nameHierarchy": "Global/USA/.*", "type": "floor"},
                {"nameHierarchy": "Global/India/.*", "type": "area"},
                {"nameHierarchy": "Global/India/.*", "type": "floor"},
            ],
        )

    def test_site_record_matches_filter_expression_with_relative_site_mismatch_returns_false(
        self,
    ):
        """
        Ensure relative site_name_hierarchy mismatch returns False when parent is provided.
        """
        site_generator = self.module.SitePlaybookGenerator.__new__(
            self.module.SitePlaybookGenerator
        )
        site_generator.log = lambda *args, **kwargs: None

        detail = {
            "nameHierarchy": "Global/USA/San Francisco",
            "parentNameHierarchy": "Global/USA",
            "type": "area",
        }
        self.assertFalse(
            site_generator.site_record_matches_filter_expression(
                detail,
                {
                    "parent_name_hierarchy": "Global/USA",
                    "site_name_hierarchy": ["Bangalore"],
                    "site_type": ["area"],
                },
            )
        )

    @patch("builtins.open", new_callable=mock_open)
    @patch("os.path.exists")
    def test_site_playbook_config_generator_site_name_hierarchy_list_api_invocation(
        self, mock_exists, mock_file
    ):
        """
        Verify one API call per site_name_hierarchy list value.
        """
        mock_exists.return_value = True
        site_name_list_config = {
            "file_path": "/tmp/case_site_name_hierarchy_list.yaml",
            "component_specific_filters": {
                "components_list": ["site"],
                "site": [
                    {
                        "site_name_hierarchy": ["Global/USA", "Global/India"],
                        "site_type": ["area"],
                    }
                ],
            },
        }

        self.run_module_with_config_and_validate_success(site_name_list_config)
        self.assertEqual(self.run_dnac_exec.call_count, 2)
        self.assert_get_sites_api_call(
            0,
            {
                "nameHierarchy": "Global/USA",
                "type": "area",
                "offset": 1,
                "limit": 500,
            },
        )
        self.assert_get_sites_api_call(
            1,
            {
                "nameHierarchy": "Global/India",
                "type": "area",
                "offset": 1,
                "limit": 500,
            },
        )

    @patch("builtins.open", new_callable=mock_open)
    @patch("os.path.exists")
    def test_site_playbook_config_generator_parent_name_hierarchy_list_api_invocation(
        self, mock_exists, mock_file
    ):
        """
        Verify one API call per parent_name_hierarchy list value using wildcard scope.
        """
        mock_exists.return_value = True
        parent_name_list_config = {
            "file_path": "/tmp/case_parent_name_hierarchy_list.yaml",
            "component_specific_filters": {
                "components_list": ["site"],
                "site": [
                    {
                        "parent_name_hierarchy": ["Global/USA", "Global/India"],
                        "site_type": ["floor"],
                    }
                ],
            },
        }

        self.run_module_with_config_and_validate_success(parent_name_list_config)
        self.assertEqual(self.run_dnac_exec.call_count, 2)
        self.assert_get_sites_api_call(
            0,
            {
                "nameHierarchy": "Global/USA/.*",
                "type": "floor",
                "offset": 1,
                "limit": 500,
            },
        )
        self.assert_get_sites_api_call(
            1,
            {
                "nameHierarchy": "Global/India/.*",
                "type": "floor",
                "offset": 1,
                "limit": 500,
            },
        )

    @patch("builtins.open", new_callable=mock_open)
    @patch("os.path.exists")
    def test_site_playbook_config_generator_parent_and_site_separate_entries_union_api_invocation(
        self, mock_exists, mock_file
    ):
        """
        Verify union behavior when parent and site filters are provided as separate site entries.
        """
        mock_exists.return_value = True
        separate_entries_union_config = {
            "file_path": "/tmp/case_parent_site_separate_entries_union.yaml",
            "component_specific_filters": {
                "components_list": ["site"],
                "site": [
                    {
                        "parent_name_hierarchy": ["Global/USA", "Global/India"],
                    },
                    {
                        "site_name_hierarchy": [
                            "Global/USA/San Francisco",
                            "Global/India/Bangalore",
                        ],
                        "site_type": ["floor"],
                    },
                ],
            },
        }

        self.run_module_with_config_and_validate_success(separate_entries_union_config)
        self.assertEqual(self.run_dnac_exec.call_count, 4)
        self.assert_get_sites_api_call(
            0,
            {
                "nameHierarchy": "Global/USA/.*",
                "type": "floor",
                "offset": 1,
                "limit": 500,
            },
        )
        self.assert_get_sites_api_call(
            1,
            {
                "nameHierarchy": "Global/India/.*",
                "type": "floor",
                "offset": 1,
                "limit": 500,
            },
        )
        self.assert_get_sites_api_call(
            2,
            {
                "nameHierarchy": "Global/USA/San Francisco",
                "type": "floor",
                "offset": 1,
                "limit": 500,
            },
        )
        self.assert_get_sites_api_call(
            3,
            {
                "nameHierarchy": "Global/India/Bangalore",
                "type": "floor",
                "offset": 1,
                "limit": 500,
            },
        )

    @patch("builtins.open", new_callable=mock_open)
    @patch("os.path.exists")
    def test_site_playbook_config_generator_scenario1_union_parent_and_site_entries_api_invocation(
        self, mock_exists, mock_file
    ):
        """
        Validate updated playbook Scenario 1:
        parent_name_hierarchy and site_name_hierarchy as separate site entries are
        expanded independently and merged as union query plans.
        """
        mock_exists.return_value = True
        scenario1_config = {
            "file_path": "/tmp/case3_site_and_parent_only.yaml",
            "file_mode": "overwrite",
            "component_specific_filters": {
                "components_list": ["site"],
                "site": [
                    {
                        "parent_name_hierarchy": [
                            "Global/USAsdfsfs",
                        ]
                    },
                    {
                        "site_name_hierarchy": [
                            "Global/USA/San Francisco",
                            "Global/USA/San Jose",
                        ]
                    },
                ],
            },
        }

        self.run_module_with_config_and_validate_success(scenario1_config)
        self.assertEqual(self.run_dnac_exec.call_count, 3)
        self.assert_get_sites_api_call(
            0,
            {
                "nameHierarchy": "Global/USAsdfsfs/.*",
                "offset": 1,
                "limit": 500,
            },
        )
        self.assert_get_sites_api_call(
            1,
            {
                "nameHierarchy": "Global/USA/San Francisco",
                "offset": 1,
                "limit": 500,
            },
        )
        self.assert_get_sites_api_call(
            2,
            {
                "nameHierarchy": "Global/USA/San Jose",
                "offset": 1,
                "limit": 500,
            },
        )

    @patch("builtins.open", new_callable=mock_open)
    @patch("os.path.exists")
    def test_site_playbook_config_generator_scenario5_site_and_parent_site_type_union_api_invocation(
        self, mock_exists, mock_file
    ):
        """
        Validate updated playbook Scenario 5:
        site_name_hierarchy and parent_name_hierarchy+site_type entries are expanded
        independently and merged in one execution.
        """
        mock_exists.return_value = True
        scenario5_config = {
            "file_path": "/tmp/case7_all_filters.yaml",
            "file_mode": "overwrite",
            "component_specific_filters": {
                "components_list": ["site"],
                "site": [
                    {"site_name_hierarchy": "Global/USA/San Francisco"},
                    {
                        "parent_name_hierarchy": "Global/USA",
                        "site_type": ["building", "floor"],
                    },
                ],
            },
        }

        self.run_module_with_config_and_validate_success(scenario5_config)
        self.assertEqual(self.run_dnac_exec.call_count, 4)
        self.assert_get_sites_api_call(
            0,
            {
                "nameHierarchy": "Global/USA/San Francisco",
                "type": "building",
                "offset": 1,
                "limit": 500,
            },
        )
        self.assert_get_sites_api_call(
            1,
            {
                "nameHierarchy": "Global/USA/San Francisco",
                "type": "floor",
                "offset": 1,
                "limit": 500,
            },
        )
        self.assert_get_sites_api_call(
            2,
            {
                "nameHierarchy": "Global/USA/.*",
                "type": "building",
                "offset": 1,
                "limit": 500,
            },
        )
        self.assert_get_sites_api_call(
            3,
            {
                "nameHierarchy": "Global/USA/.*",
                "type": "floor",
                "offset": 1,
                "limit": 500,
            },
        )

    @patch("builtins.open", new_callable=mock_open)
    @patch("os.path.exists")
    def test_site_playbook_config_generator_scenario5_floor_site_type_applies_to_union(
        self, mock_exists, mock_file
    ):
        """
        Validate Scenario 5 floor-only expectation:
        parent and exact-site retrievals are unioned first and then constrained
        by floor site_type across both entries.
        """
        mock_exists.return_value = True
        scenario5_floor_only_config = {
            "file_path": "/tmp/case5_all_filters.yaml",
            "file_mode": "overwrite",
            "component_specific_filters": {
                "components_list": ["site"],
                "site": [
                    {"site_name_hierarchy": "Global/USA/San Francisco"},
                    {
                        "parent_name_hierarchy": ["Global/USA", "Global/India"],
                        "site_type": ["floor"],
                    },
                ],
            },
        }

        self.run_module_with_config_and_validate_success(scenario5_floor_only_config)
        self.assertEqual(self.run_dnac_exec.call_count, 3)
        self.assert_get_sites_api_call(
            0,
            {
                "nameHierarchy": "Global/USA/San Francisco",
                "type": "floor",
                "offset": 1,
                "limit": 500,
            },
        )
        self.assert_get_sites_api_call(
            1,
            {
                "nameHierarchy": "Global/USA/.*",
                "type": "floor",
                "offset": 1,
                "limit": 500,
            },
        )
        self.assert_get_sites_api_call(
            2,
            {
                "nameHierarchy": "Global/India/.*",
                "type": "floor",
                "offset": 1,
                "limit": 500,
            },
        )

    def test_site_playbook_config_generator_scenario9_same_item_parent_and_site_fails_validation(
        self,
    ):
        """
        Validate updated playbook Scenario 9:
        a single site filter item containing both site_name_hierarchy and
        parent_name_hierarchy is rejected as ambiguous.
        """
        scenario9_invalid_config = {
            "file_path": "/tmp/case9_fail_test.yaml",
            "file_mode": "overwrite",
            "component_specific_filters": {
                "components_list": ["site"],
                "site": [
                    {
                        "site_name_hierarchy": "Global/USA/San Francisco",
                        "parent_name_hierarchy": "Global/Japan",
                        "site_type": ["building", "floor"],
                    }
                ],
            },
        }
        set_module_args(
            dict(
                dnac_host="1.1.1.1",
                dnac_username="dummy",
                dnac_password="dummy",
                dnac_version="2.3.7.9",
                dnac_log=True,
                dnac_log_level="DEBUG",
                state="gathered",
                config=scenario9_invalid_config,
            )
        )
        result = self.execute_module(changed=False, failed=True)
        self.assertIn("cannot be provided together", str(result.get("msg")))
        self.assertEqual(
            self.run_dnac_exec.call_count,
            0,
            "Expected no API execution for ambiguous same-item parent/site hierarchy filter.",
        )
