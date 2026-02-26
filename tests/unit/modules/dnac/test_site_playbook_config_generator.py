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
            config (list): Module configuration payload passed directly to
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

        duplicate_site_type_config = [
            {
                "file_path": "/tmp/case_duplicate_site_type.yaml",
                "component_specific_filters": {
                    "components_list": ["site"],
                    "site": [{"site_type": ["area", "area"]}],
                },
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
        invalid_site_type_config = [
            {
                "file_path": "/tmp/case_invalid_site_type.yaml",
                "component_specific_filters": {
                    "components_list": ["site"],
                    "site": [{"site_type": ["campus"]}],
                },
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
