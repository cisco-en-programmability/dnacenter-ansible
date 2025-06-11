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

# Authors:
#   A Mohamed Rafeek <mabdulk2@cisco.com>
#   Sonali Deepthi Kesali <skesali@cisco.com>
#
# Description:
#   Manage operation create, bulk create, update and delete of the resource Sites.
#   Creates site with area/building/floor with specified hierarchy.
#   Create multiple sites (area, building, or floor) with specified hierarchies in bulk.
#   Updates site with area/building/floor with specified hierarchy.
#   Deletes site with area/building/floor with specified hierarchy.

from __future__ import absolute_import, division, print_function

__metaclass__ = type
from unittest.mock import patch
from ansible_collections.cisco.dnac.plugins.modules import site_workflow_manager
from .dnac_module import TestDnacModule, set_module_args, loadPlaybookData


class TestDnacSiteWorkflow(TestDnacModule):

    module = site_workflow_manager
    test_data = loadPlaybookData("site_workflow_manager")
    playbook_config_bulk_site_2376 = test_data.get("playbook_config_bulk_site_2376")
    playbook_config_site = test_data.get("playbook_config_site")
    playbook_config_site_creation = test_data.get("playbook_config_site_creation")
    playbook_config_update_site = test_data.get("playbook_config_update_site")
    update_a_playbook = test_data.get("update_a_playbook")
    playbook_config_invalid_param = test_data.get("playbook_config_invalid_param")
    playbook_config_empty = test_data.get("playbook_config_empty")
    playbook_config_invalid_bulk_site = test_data.get("playbook_config_invalid_bulk_site")
    playbook_config_delete = test_data.get("playbook_config_delete")
    playbook_config_update1_site = test_data.get("playbook_config_update1_site")
    delete_playbook_config = test_data.get("delete_playbook_config")
    upload_floor_map_playbook = test_data.get("upload_floor_map_playbook")
    delete_config_playbook = test_data.get("delete_config_playbook")
    playbook_site_delete_2376 = test_data.get("playbook_site_delete_2376")
    playbook_config_update_site_2376 = test_data.get("playbook_config_update_site_2376")

    def setUp(self):
        super(TestDnacSiteWorkflow, self).setUp()

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
        super(TestDnacSiteWorkflow, self).tearDown()
        self.mock_dnac_exec.stop()
        self.mock_dnac_init.stop()

    def load_fixtures(self, response=None, device=""):
        """
        Load fixtures for user.
        """

        if "invalid_delete_config" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
            ]

        elif "playbook_config_bulk_site_2376" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("get_sites"),
                self.test_data.get("get_sites1"),
                self.test_data.get("get_sites2"),
                self.test_data.get("create_bulk_site_response"),
                self.test_data.get("create_bulk_site_response_details1"),
                self.test_data.get("create_bulk_site_response_details2"),
                self.test_data.get("get_sites3"),
                self.test_data.get("upload_floor_image"),
            ]

        elif "invalid_create_bulk_site_type" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("create_bulk_site_response"),
                self.test_data.get("create_bulk_site_response_details1"),
                self.test_data.get("create_bulk_site_response_details2"),
                self.test_data.get("get_sites_area"),
                self.test_data.get("get_sites_building"),
                self.test_data.get("get_sites_floor"),

            ]

        elif "create_site" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                Exception(),
                Exception(),
                self.test_data.get("get_site_response"),
                self.test_data.get("get_site_response1"),
                self.test_data.get("get_site_create_area"),
                Exception(),
                Exception(),
                self.test_data.get("create_site_response_area"),
                self.test_data.get("create_site_response_area_details"),
                self.test_data.get("get_site_create_building"),
                Exception(),
                Exception(),
                self.test_data.get("create_site_response_area"),
                self.test_data.get("create_site_response_area_details"),
                self.test_data.get("get_site_create_floor"),
            ]

        elif "update_site" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("get_site_area_update"),
                self.test_data.get("get_site_building_update"),
                self.test_data.get("update_site_building_response"),
                self.test_data.get("update_site_building_response_details"),
                self.test_data.get("get_site_floor_update"),
                self.test_data.get("update_site_floor_response"),
                self.test_data.get("update_site_floor_response_details"),
                self.test_data.get("get_site_updated_floor"),
            ]

        elif "playbook_config_update_site" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                Exception(),
                self.test_data.get("get_sites_area"),
                self.test_data.get("get_sites_building"),
                self.test_data.get("get_sites_floor"),
                Exception(),
                self.test_data.get("get_sites_building"),
                self.test_data.get("update_a_task_id_building"),
                self.test_data.get("update_a_task_id_building_details"),
                Exception(),
                self.test_data.get("get_sites_floor"),
                self.test_data.get("update_a_task_id_floor"),
                self.test_data.get("update_a_task_id_floor_details"),
            ]

        elif "playbook_config_update_site_2376" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("get_site_update"),
                self.test_data.get("get_site_update1"),
                self.test_data.get("get_site_update2"),
                self.test_data.get("get_site_update_task"),
                self.test_data.get("get_site_update_task_deatils"),
                self.test_data.get("get_site_update_task1"),
                self.test_data.get("get_site_update_task_deatils1"),
            ]

        elif "update_not_needed_site" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("update_not_needed_get_site_area"),
                self.test_data.get("update_not_needed_get_sites_building"),
                self.test_data.get("update_not_needed_get_sites_floor"),
            ]

        elif "delete_a_site" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("get_site_floor_a_delete"),
                self.test_data.get("get_sites_assigned_devices_network"),
                self.test_data.get("delete_a_floor_response"),
                self.test_data.get("delete_a_floor_response_details"),
                self.test_data.get("get_site_building_a_delete"),
                self.test_data.get("delete_a_building_response"),
                self.test_data.get("delete_a_building_response_details"),
                self.test_data.get("get_site_area_a_delete"),
                self.test_data.get("delete_an_area_response"),
                self.test_data.get("delete_an_area_response_details"),
            ]

        elif "playbook_site_delete_2376" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("get_sites_response1"),
                self.test_data.get("get_sites_response2"),
                self.test_data.get("get_sites_response3"),
                self.test_data.get("delete_floor_response1"),
                self.test_data.get("task_response1"),
                self.test_data.get("get_sites_response4"),
                self.test_data.get("delete_response22"),
                self.test_data.get("task_response2"),
                self.test_data.get("get_sites_response5"),
                self.test_data.get("get_sites_response6"),
                self.test_data.get("delete_response3"),
                self.test_data.get("delete_response4"),
                self.test_data.get("task_response_3"),
                self.test_data.get("response_site_delete"),
            ]

        elif "delete_site" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("delete_get_site_response"),
                self.test_data.get("delete_get_membership"),
                self.test_data.get("delete_response"),
                self.test_data.get("delete_response_details"),
                self.test_data.get("delete_get_site_response"),
                self.test_data.get("delete_get_membership"),
                self.test_data.get("delete_response1"),
                self.test_data.get("delete_response_details1"),
                self.test_data.get("delete_get_site_response"),
                self.test_data.get("delete_get_membership"),
                self.test_data.get("delete_response2"),
                self.test_data.get("delete_response_details2"),
            ]

        elif "invalid_delete_site" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("delete_get_site_response"),
                self.test_data.get("delete_get_membership"),
                self.test_data.get("delete_response"),
                self.test_data.get("delete_response_detail_invalid"),
                self.test_data.get("delete_get_site_response"),
                self.test_data.get("delete_get_membership"),
                self.test_data.get("delete_response1"),
                self.test_data.get("delete_response_details1"),
                self.test_data.get("delete_get_site_response"),
                self.test_data.get("delete_get_membership"),
                self.test_data.get("delete_response2"),
                self.test_data.get("delete_response_detail_invalid"),
            ]

        if "verify_diff" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("get_site_area"),
                self.test_data.get("get_site_area"),
                self.test_data.get("get_site_building"),
                self.test_data.get("get_site_building"),
                self.test_data.get("get_site_floor"),
                self.test_data.get("get_site_floor"),
            ]

        if "playbook_config_site_creation" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                Exception(),
                Exception(),
                self.test_data.get("get_site"),
                self.test_data.get("create_site"),
                self.test_data.get("business"),
                Exception(),
                Exception(),
                self.test_data.get("get_site1"),
                self.test_data.get("create_site1"),
                self.test_data.get("business1"),
                Exception(),
                Exception(),
                self.test_data.get("get_site2"),
                self.test_data.get("create_site3"),
                self.test_data.get("business2"),
                Exception(),
                self.test_data.get("get_site3"),
            ]

        elif "upload_floor_map" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("upload_for_get_site"),
                self.test_data.get("upload_for_get_site2"),
                self.test_data.get("upload_for_get_site3"),
                self.test_data.get("upload_site_creation"),
                self.test_data.get("upload_task_id"),
                self.test_data.get("upload_task_id2"),
                self.test_data.get("upload_task_id_details"),
                self.test_data.get("upload_floor_map"),
            ]

    def test_Site_workflow_manager_playbook_config_bulk_site_2376(self):
        """
        Test case for verifying site creation using the site workflow manager in Cisco Catalyst Center (version 2.3.7.6).

        This test ensures that the site workflow manager correctly processes a bulk site configuration,
        resulting in successful creation of an area, building, and floor with associated details and image upload.
        """
        set_module_args(
            dict(
                dnac_host="1.1.1.1",
                dnac_username="dummy",
                dnac_password="dummy",
                dnac_version="2.3.7.6",
                dnac_log=True,
                state="merged",
                config_verify=True,
                config=self.playbook_config_bulk_site_2376
            )
        )
        result = self.execute_module(changed=True, failed=True)
        self.maxDiff = None
        self.assertEqual(
            result.get('msg'),
            "An exception occurred: {'msg': 'Site created successfully.', " +
            "'response': 'File path does not exist: /Users/mabdulk2/pngegg.png', 'failed': True}"
        )

    def test_Site_workflow_manager_non_create_bulk_site(self):
        """
        Test case for site workflow manager when site creation fails.

        This test verifies the behavior of the site workflow manager when attempting to create a bulk site that
        cannot be processed, ensuring the module correctly fails and returns the expected error message.
        """
        set_module_args(
            dict(
                dnac_host="1.1.1.1",
                dnac_username="dummy",
                dnac_password="dummy",
                dnac_version="2.3.7.6",
                dnac_log=True,
                state="merged",
                config_verify=True,
                config=self.playbook_config_site
            )
        )
        result = self.execute_module(changed=False, failed=True)
        self.assertEqual(
            result.get('msg'),
            "Unable to proceed to create bulk site 'Global/japan8888/blossom'."
        )

    def test_Site_workflow_manager_non_playbook_config_site_creation(self):
        """
        Test case for site workflow manager when site creation fails due to missing parent site.

        This test verifies that the site workflow manager correctly fails with an appropriate error message
        when attempting to create a site whose parent (e.g., 'Global') does not exist in the Cisco Catalyst Center.
        """
        set_module_args(
            dict(
                dnac_host="1.1.1.1",
                dnac_username="dummy",
                dnac_password="dummy",
                dnac_version="2.3.5.3",
                dnac_log=True,
                state="merged",
                config_verify=True,
                config=self.playbook_config_site_creation
            )
        )
        result = self.execute_module(changed=False, failed=True)
        self.assertEqual(
            result.get('msg'),
            "Parent name 'Global' does not exist in the Cisco Catalyst Center."
        )

    def test_Site_workflow_manager_invalid_create_site(self):
        """
        Test case for site workflow manager failure due to invalid parent site during site creation.

        This test verifies that the site workflow manager correctly handles the failure scenario
        when attempting to create a site with an invalid or non-existent parent site (e.g., 'Global')
        in Cisco Catalyst Center version 2.3.5.3.
        """
        set_module_args(
            dict(
                dnac_host="1.1.1.1",
                dnac_username="dummy",
                dnac_password="dummy",
                dnac_version="2.3.5.3",
                dnac_log=True,
                state="merged",
                config_verify=True,
                config=self.playbook_config_site
            )
        )
        result = self.execute_module(changed=False, failed=True)
        self.assertEqual(
            result.get('msg'),
            "Parent name 'Global' does not exist in the Cisco Catalyst Center."
        )

    def test_site_workflow_manager_invalid_param(self):

        """
        Test case for site workflow manager with invalid parameters in the playbook.

        This test case checks the behavior of the site workflow manager when the playbook contains invalid parameters.
        """

        set_module_args(
            dict(
                dnac_host="1.1.1.1",
                dnac_username="dummy",
                dnac_password="dummy",
                dnac_version="2.3.7.6",
                dnac_log=True,
                state="merged",
                config_verify=True,
                config=self.playbook_config_invalid_param
            )
        )
        result = self.execute_module(changed=False, failed=True)
        self.assertFalse(
            "Invalid parameters in playbook:" in result.get('msg')
        )

    def test_site_workflow_manager_invalid_delete_site(self):
        """
        Test case to validate failure of site workflow manager when playbook contains invalid parameters.

        This test ensures that the site workflow manager module correctly fails and returns an appropriate error
        message when the provided playbook configuration includes invalid parameters during a site deletion operation.
        """
        set_module_args(
            dict(
                dnac_host="1.1.1.1",
                dnac_username="dummy",
                dnac_password="dummy",
                dnac_version="2.3.7.6",
                dnac_log=True,
                state="merged",
                config_verify=True,
                config=self.playbook_site_delete_2376
            )
        )
        result = self.execute_module(changed=False, failed=True)
        self.assertFalse(
            "Invalid parameters in playbook:" in result.get('msg')
        )

    def test_Site_workflow_manager_invalid_delete_config_exception(self):
        """
        Test case for site workflow manager when deleting a site with invalid configuration.

        This test checks the behavior of the site workflow manager when an exception occurs
        during the validation step (e.g., GET API call to 'get_sites') due to invalid site configuration.
        """
        set_module_args(
            dict(
                dnac_host="1.1.1.1",
                dnac_username="dummy",
                dnac_password="dummy",
                dnac_version="2.3.7.6",
                dnac_log=True,
                state="merged",
                config_verify=True,
                config=self.playbook_site_delete_2376
            )
        )
        result = self.execute_module(changed=False, failed=True)
        self.maxDiff = None
        self.assertEqual(
            result.get('msg'),
            "An error occurred while executing GET API call to Function: 'get_sites' from Family: 'site_design'. "
            "Parameters: {'name_hierarchy': 'Global/bangalore/s1/cherry', 'offset': 1, 'limit': 500}. Exception: ."
        )

    def test_Site_workflow_manager_create_site_bulk_invalid(self):
        """
        Test case for site workflow manager when creating a site.

        This test case checks the behavior of the site workflow manager when creating a new site in the specified DNAC.
        """
        set_module_args(
            dict(
                dnac_host="1.1.1.1",
                dnac_username="dummy",
                dnac_password="dummy",
                dnac_version="2.3.7.6",
                dnac_log=True,
                state="merged",
                config_verify=True,
                config=self.playbook_config_site
            )
        )
        result = self.execute_module(changed=False, failed=True)
        self.assertEqual(
            result.get('msg'),
            "An error occurred while executing GET API call to Function: 'get_sites' "
            "from Family: 'site_design'. "
            "Parameters: {'name_hierarchy': 'Global/japan8888/blossom', 'offset': 1, 'limit': 500}. "
            "Exception: ."
        )

    def test_Site_workflow_manager_verify_diff_merged_site(self):
        """
        Test case for verify parameters in site workflow manager after applying merged state.

        This test case checks the behavior of the site workflow manager after applying merged state Cisco Catalyst Center.
        """
        set_module_args(
            dict(
                dnac_host="1.1.1.1",
                dnac_username="dummy",
                dnac_password="dummy",
                dnac_log=True,
                state="merged",
                config_verify=True,
                config=self.playbook_config_site
            )
        )
        result = self.execute_module(changed=False, failed=True)
        self.maxDiff = None
        self.assertEqual(
            result.get('msg'),
            "The specified version '2.2.3.3' does not support the site workflow feature. "
            "Supported versions start from '2.3.5.3' onwards. Version '2.3.5.3' introduces APIs for creating, updating, "
            "and deleting sites. Version '2.3.7.6' expands support to include APIs for bulk site creating, updating, and deleting sites."
        )

    def test_Site_workflow_manager_verify_diff_deleted_site(self):
        """
        Test case to check error when deleting a site using an unsupported DNAC version.

        This test verifies that the site workflow manager returns an appropriate error message
        if the DNAC version does not support site deletion operations.
        """
        set_module_args(
            dict(
                dnac_host="1.1.1.1",
                dnac_username="dummy",
                dnac_password="dummy",
                dnac_log=True,
                state="deleted",
                config_verify=True,
                config=self.playbook_config_site
            )
        )
        result = self.execute_module(changed=False, failed=True)
        self.maxDiff = None
        self.assertEqual(
            result.get('msg'),
            "The specified version '2.2.3.3' does not support the site workflow feature. "
            "Supported versions start from '2.3.5.3' onwards. Version '2.3.5.3' introduces APIs for creating, updating, "
            "and deleting sites. Version '2.3.7.6' expands support to include APIs for bulk site creating, updating, and deleting sites."
        )

    def test_Site_workflow_manager_delete_a_site(self):
        """
        Test case for site workflow manager when failing to create a bulk site.

        This test checks the behavior of the site workflow manager when an error occurs
        while trying to create a site using the 'merged' state.
        """
        set_module_args(
            dict(
                dnac_host="1.1.1.1",
                dnac_username="dummy",
                dnac_password="dummy",
                dnac_version="2.3.7.6",
                dnac_log=True,
                state="merged",
                config_verify=True,
                config=self.playbook_config_delete
            )
        )
        result = self.execute_module(changed=False, failed=True)
        self.assertEqual(
            result.get('msg'),
            "Unable to proceed to create bulk site 'Global/japan8888'."
        )

    def test_Site_workflow_manager_playbook_site_delete_2376(self):
        """
        Test case for site workflow manager when deleting sites with playbook version 2.3.7.6.

        This test verifies that the site workflow manager successfully deletes the specified
        sites using the provided playbook configuration and reports success.
        """
        set_module_args(
            dict(
                dnac_host="1.1.1.1",
                dnac_username="dummy",
                dnac_password="dummy",
                dnac_version="2.3.7.6",
                dnac_log=True,
                state="deleted",
                config_verify=True,
                config=self.playbook_site_delete_2376
            )
        )
        result = self.execute_module(changed=True, failed=False)
        self.assertEqual(
            result.get('msg'),
            "Given site(s) '['floor: Global/bangalore/s1/cherry', 'building: Global/bangalore/s1', "
            "'area: Global/bangalore']' deleted successfully from Cisco Catalyst Center"
        )

    def test_Site_workflow_manager_delete_site(self):
        """
        Test case for site workflow manager when deleting a site.

        This test verifies that the site workflow manager successfully deletes the specified
        sites in the given DNAC version using the provided playbook configuration.
        """
        set_module_args(
            dict(
                dnac_host="1.1.1.1",
                dnac_username="dummy",
                dnac_password="dummy",
                dnac_version="2.3.5.3",
                dnac_log=True,
                state="deleted",
                config_verify=True,
                config=self.delete_config_playbook
            )
        )
        result = self.execute_module(changed=True, failed=False)
        self.assertEqual(
            result.get('msg'),
            "Given site(s) '['Global/bangalore/s1/cherry4', 'Global/bangalore/s1', 'Global/bangalore']' deleted successfully from Cisco Catalyst Center"
        )

    def test_Site_workflow_manager_playbook_config_update_site(self):
        """
        Test case for site workflow manager when updating sites.

        This test verifies that the site workflow manager correctly updates specified sites
        and identifies sites that do not require any updates in the given DNAC version.
        """
        set_module_args(
            dict(
                dnac_host="1.1.1.1",
                dnac_username="dummy",
                dnac_password="dummy",
                dnac_version="2.3.5.3",
                dnac_log=True,
                state="merged",
                config_verify=True,
                config=self.playbook_config_update_site
            )
        )
        result = self.execute_module(changed=True, failed=False)
        self.maxDiff = None
        self.assertEqual(
            result.get('msg'),
            "Site(s) '['building: Global/japan8888/blossom', 'floor: Global/japan8888/blossom/cherry']' updated successfully and some site(s)"
            " '['area: Global/japan8888']' not needs any update in Cisco Catalyst\n" +
            "                                Center."
        )

    def test_Site_workflow_manager_playbook_config_not_update_site(self):
        """
        Test case for site workflow manager when no site updates are needed.

        This test verifies that the site workflow manager correctly identifies when a site
        does not require any update and returns the appropriate message.
        """
        set_module_args(
            dict(
                dnac_host="1.1.1.1",
                dnac_username="dummy",
                dnac_password="dummy",
                dnac_version="2.3.7.6",
                dnac_log=True,
                state="merged",
                config_verify=True,
                config=self.playbook_config_update_site
            )
        )
        result = self.execute_module(changed=False, failed=True)
        self.maxDiff = None
        self.assertEqual(
            result.get('msg'),
            "Site - Global/japan8888/blossom does not need any update"
        )
