#  Copyright (c) 2025 Cisco and/or its affiliates.
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
#   Vidhya Rathinam <virathin@cisco.com>
#
# Description:
#   Unit tests for the Ansible module `brownfield_site_workflow_manager`.
#   These tests cover various scenarios for generating YAML playbooks from brownfield
#   site configurations including areas, buildings, and floors.

from __future__ import absolute_import, division, print_function

__metaclass__ = type
from unittest.mock import patch, mock_open
from ansible_collections.cisco.dnac.plugins.modules import (
    brownfield_site_workflow_manager,
)
from .dnac_module import TestDnacModule, set_module_args, loadPlaybookData


class TestBrownfieldSiteWorkflowManager(TestDnacModule):

    module = brownfield_site_workflow_manager
    test_data = loadPlaybookData("brownfield_site_workflow_manager")

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
    playbook_config_floor_by_rf_model = test_data.get(
        "playbook_config_floor_by_rf_model"
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

    def setUp(self):
        super(TestBrownfieldSiteWorkflowManager, self).setUp()

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

        if "generate_all_configurations" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("get_all_sites_response"),
            ]

        elif "area_by_site_name_single" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("get_area_response"),
            ]

        elif "area_by_site_name_multiple" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("get_area_response"),
                self.test_data.get("get_area_response"),
            ]

        elif "area_by_parent_site" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("get_multiple_area_response"),
            ]

        elif "building_by_site_name_single" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("get_building_response"),
            ]

        elif "building_by_site_name_multiple" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("get_building_response"),
                self.test_data.get("get_building_response"),
            ]

        elif "building_by_parent_site" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("get_multiple_building_response"),
            ]

        elif "floor_by_site_name_single" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("get_floor_response"),
            ]

        elif "floor_by_site_name_multiple" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("get_floor_response"),
                self.test_data.get("get_floor_response"),
            ]

        elif "floor_by_parent_site" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("get_multiple_floor_response"),
            ]

        elif "floor_by_rf_model" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("get_multiple_floor_response"),
            ]

        elif "areas_and_buildings" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("get_area_response"),
                self.test_data.get("get_building_response"),
            ]

        elif "buildings_and_floors" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("get_multiple_building_response"),
                self.test_data.get("get_multiple_floor_response"),
            ]

        elif "all_components" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("get_area_response"),
                self.test_data.get("get_multiple_building_response"),
                self.test_data.get("get_multiple_floor_response"),
            ]

        elif "empty_filters" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("get_area_response"),
            ]

        elif "no_file_path" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("get_building_response"),
            ]

    @patch("builtins.open", new_callable=mock_open)
    @patch("os.path.exists")
    def test_brownfield_site_workflow_manager_generate_all_configurations(
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
                state="gathered",
                config=self.playbook_config_generate_all_configurations,
            )
        )
        result = self.execute_module(changed=True, failed=False)
        self.assertIn("YAML config generation Task succeeded", str(result.get("msg")))

    @patch("builtins.open", new_callable=mock_open)
    @patch("os.path.exists")
    def test_brownfield_site_workflow_manager_area_by_site_name_single(
        self, mock_exists, mock_file
    ):
        """
        Test case for generating YAML configuration for a single area by site name.

        This test verifies that the generator correctly retrieves and generates configuration
        for a single area when filtered by site name.
        """
        mock_exists.return_value = True

        set_module_args(
            dict(
                dnac_host="1.1.1.1",
                dnac_username="dummy",
                dnac_password="dummy",
                dnac_version="2.3.7.9",
                dnac_log=True,
                state="gathered",
                config=self.playbook_config_area_by_site_name_single,
            )
        )
        result = self.execute_module(changed=True, failed=False)
        self.assertIn("YAML config generation Task succeeded", str(result.get("msg")))

    @patch("builtins.open", new_callable=mock_open)
    @patch("os.path.exists")
    def test_brownfield_site_workflow_manager_area_by_site_name_multiple(
        self, mock_exists, mock_file
    ):
        """
        Test case for generating YAML configuration for multiple areas by site names.

        This test verifies that the generator correctly retrieves and generates configuration
        for multiple areas when filtered by multiple site names.
        """
        mock_exists.return_value = True

        set_module_args(
            dict(
                dnac_host="1.1.1.1",
                dnac_username="dummy",
                dnac_password="dummy",
                dnac_version="2.3.7.9",
                dnac_log=True,
                state="gathered",
                config=self.playbook_config_area_by_site_name_multiple,
            )
        )
        result = self.execute_module(changed=True, failed=False)
        self.assertIn("YAML config generation Task succeeded", str(result.get("msg")))

    @patch("builtins.open", new_callable=mock_open)
    @patch("os.path.exists")
    def test_brownfield_site_workflow_manager_area_by_parent_site(
        self, mock_exists, mock_file
    ):
        """
        Test case for generating YAML configuration for areas by parent site.

        This test verifies that the generator correctly retrieves and generates configuration
        for areas when filtered by parent site name.
        """
        mock_exists.return_value = True

        set_module_args(
            dict(
                dnac_host="1.1.1.1",
                dnac_username="dummy",
                dnac_password="dummy",
                dnac_version="2.3.7.9",
                dnac_log=True,
                state="gathered",
                config=self.playbook_config_area_by_parent_site,
            )
        )
        result = self.execute_module(changed=True, failed=False)
        self.assertIn("YAML config generation Task succeeded", str(result.get("msg")))

    @patch("builtins.open", new_callable=mock_open)
    @patch("os.path.exists")
    def test_brownfield_site_workflow_manager_building_by_site_name_single(
        self, mock_exists, mock_file
    ):
        """
        Test case for generating YAML configuration for a single building by site name.

        This test verifies that the generator correctly retrieves and generates configuration
        for a single building when filtered by site name.
        """
        mock_exists.return_value = True

        set_module_args(
            dict(
                dnac_host="1.1.1.1",
                dnac_username="dummy",
                dnac_password="dummy",
                dnac_version="2.3.7.9",
                dnac_log=True,
                state="gathered",
                config=self.playbook_config_building_by_site_name_single,
            )
        )
        result = self.execute_module(changed=True, failed=False)
        self.assertIn("YAML config generation Task succeeded", str(result.get("msg")))

    @patch("builtins.open", new_callable=mock_open)
    @patch("os.path.exists")
    def test_brownfield_site_workflow_manager_building_by_site_name_multiple(
        self, mock_exists, mock_file
    ):
        """
        Test case for generating YAML configuration for multiple buildings by site names.

        This test verifies that the generator correctly retrieves and generates configuration
        for multiple buildings when filtered by multiple site names.
        """
        mock_exists.return_value = True

        set_module_args(
            dict(
                dnac_host="1.1.1.1",
                dnac_username="dummy",
                dnac_password="dummy",
                dnac_version="2.3.7.9",
                dnac_log=True,
                state="gathered",
                config=self.playbook_config_building_by_site_name_multiple,
            )
        )
        result = self.execute_module(changed=True, failed=False)
        self.assertIn("YAML config generation Task succeeded", str(result.get("msg")))

    @patch("builtins.open", new_callable=mock_open)
    @patch("os.path.exists")
    def test_brownfield_site_workflow_manager_building_by_parent_site(
        self, mock_exists, mock_file
    ):
        """
        Test case for generating YAML configuration for buildings by parent site.

        This test verifies that the generator correctly retrieves and generates configuration
        for buildings when filtered by parent site name.
        """
        mock_exists.return_value = True

        set_module_args(
            dict(
                dnac_host="1.1.1.1",
                dnac_username="dummy",
                dnac_password="dummy",
                dnac_version="2.3.7.9",
                dnac_log=True,
                state="gathered",
                config=self.playbook_config_building_by_parent_site,
            )
        )
        result = self.execute_module(changed=True, failed=False)
        self.assertIn("YAML config generation Task succeeded", str(result.get("msg")))

    @patch("builtins.open", new_callable=mock_open)
    @patch("os.path.exists")
    def test_brownfield_site_workflow_manager_floor_by_site_name_single(
        self, mock_exists, mock_file
    ):
        """
        Test case for generating YAML configuration for a single floor by site name.

        This test verifies that the generator correctly retrieves and generates configuration
        for a single floor when filtered by site name.
        """
        mock_exists.return_value = True

        set_module_args(
            dict(
                dnac_host="1.1.1.1",
                dnac_username="dummy",
                dnac_password="dummy",
                dnac_version="2.3.7.9",
                dnac_log=True,
                state="gathered",
                config=self.playbook_config_floor_by_site_name_single,
            )
        )
        result = self.execute_module(changed=True, failed=False)
        self.assertIn("YAML config generation Task succeeded", str(result.get("msg")))

    @patch("builtins.open", new_callable=mock_open)
    @patch("os.path.exists")
    def test_brownfield_site_workflow_manager_floor_by_site_name_multiple(
        self, mock_exists, mock_file
    ):
        """
        Test case for generating YAML configuration for multiple floors by site names.

        This test verifies that the generator correctly retrieves and generates configuration
        for multiple floors when filtered by multiple site names.
        """
        mock_exists.return_value = True

        set_module_args(
            dict(
                dnac_host="1.1.1.1",
                dnac_username="dummy",
                dnac_password="dummy",
                dnac_version="2.3.7.9",
                dnac_log=True,
                state="gathered",
                config=self.playbook_config_floor_by_site_name_multiple,
            )
        )
        result = self.execute_module(changed=True, failed=False)
        self.assertIn("YAML config generation Task succeeded", str(result.get("msg")))

    @patch("builtins.open", new_callable=mock_open)
    @patch("os.path.exists")
    def test_brownfield_site_workflow_manager_floor_by_parent_site(
        self, mock_exists, mock_file
    ):
        """
        Test case for generating YAML configuration for floors by parent site.

        This test verifies that the generator correctly retrieves and generates configuration
        for floors when filtered by parent site name.
        """
        mock_exists.return_value = True

        set_module_args(
            dict(
                dnac_host="1.1.1.1",
                dnac_username="dummy",
                dnac_password="dummy",
                dnac_version="2.3.7.9",
                dnac_log=True,
                state="gathered",
                config=self.playbook_config_floor_by_parent_site,
            )
        )
        result = self.execute_module(changed=True, failed=False)
        self.assertIn("YAML config generation Task succeeded", str(result.get("msg")))

    @patch("builtins.open", new_callable=mock_open)
    @patch("os.path.exists")
    def test_brownfield_site_workflow_manager_floor_by_rf_model(
        self, mock_exists, mock_file
    ):
        """
        Test case for generating YAML configuration for floors by RF model.

        This test verifies that the generator correctly retrieves and generates configuration
        for floors when filtered by RF model type.
        """
        mock_exists.return_value = True

        set_module_args(
            dict(
                dnac_host="1.1.1.1",
                dnac_username="dummy",
                dnac_password="dummy",
                dnac_version="2.3.7.9",
                dnac_log=True,
                state="gathered",
                config=self.playbook_config_floor_by_rf_model,
            )
        )
        result = self.execute_module(changed=True, failed=False)
        self.assertIn("YAML config generation Task succeeded", str(result.get("msg")))

    @patch("builtins.open", new_callable=mock_open)
    @patch("os.path.exists")
    def test_brownfield_site_workflow_manager_areas_and_buildings(
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
                state="gathered",
                config=self.playbook_config_areas_and_buildings,
            )
        )
        result = self.execute_module(changed=True, failed=False)
        self.assertIn("YAML config generation Task succeeded", str(result.get("msg")))

    @patch("builtins.open", new_callable=mock_open)
    @patch("os.path.exists")
    def test_brownfield_site_workflow_manager_buildings_and_floors(
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
                state="gathered",
                config=self.playbook_config_buildings_and_floors,
            )
        )
        result = self.execute_module(changed=True, failed=False)
        self.assertIn("YAML config generation Task succeeded", str(result.get("msg")))

    @patch("builtins.open", new_callable=mock_open)
    @patch("os.path.exists")
    def test_brownfield_site_workflow_manager_all_components(
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
                state="gathered",
                config=self.playbook_config_all_components,
            )
        )
        result = self.execute_module(changed=True, failed=False)
        self.assertIn("YAML config generation Task succeeded", str(result.get("msg")))

    @patch("builtins.open", new_callable=mock_open)
    @patch("os.path.exists")
    def test_brownfield_site_workflow_manager_empty_filters(
        self, mock_exists, mock_file
    ):
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
                state="gathered",
                config=self.playbook_config_empty_filters,
            )
        )
        result = self.execute_module(changed=True, failed=False)
        self.assertIn("YAML config generation Task succeeded", str(result.get("msg")))

    @patch("builtins.open", new_callable=mock_open)
    @patch("os.path.exists")
    def test_brownfield_site_workflow_manager_no_file_path(
        self, mock_exists, mock_file
    ):
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
                state="gathered",
                config=self.playbook_config_no_file_path,
            )
        )
        result = self.execute_module(changed=True, failed=False)
        self.assertIn("YAML config generation Task succeeded", str(result.get("msg")))
