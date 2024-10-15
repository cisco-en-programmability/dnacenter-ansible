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
from ansible_collections.cisco.dnac.plugins.modules import site_workflow_manager
from .dnac_module import TestDnacModule, set_module_args, loadPlaybookData


class TestDnacSiteWorkflow(TestDnacModule):

    module = site_workflow_manager
    test_data = loadPlaybookData("site_workflow_manager")
    playbook_config_bulk_site = test_data.get("playbook_config_bulk_site")
    playbook_config_site = test_data.get("playbook_config_site")
    playbook_config_update_site = test_data.get("playbook_config_update_site")
    playbook_config_update_a_site = test_data.get("playbook_config_update_a_site")
    playbook_config_invalid_param = test_data.get("playbook_config_invalid_param")
    playbook_config_empty = test_data.get("playbook_config_empty")
    playbook_config_invalid_bulk_site = test_data.get("playbook_config_invalid_bulk_site")
    playbook_config_delete = test_data.get("playbook_config_delete")
    playbook_config_update1_site = test_data.get("playbook_config_update1_site")

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
                # self.test_data.get(""),
            ]

        elif "create_bulk_site" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("get_sites"),
                self.test_data.get("create_bulk_site_response"),
                self.test_data.get("create_bulk_site_response_details1"),
                self.test_data.get("create_bulk_site_response_details2"),
                self.test_data.get("get_sites_area"),
                self.test_data.get("get_sites_building"),
                self.test_data.get("get_sites_floor"),

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
                self.test_data.get("create_site_response_area"),
                self.test_data.get("create_site_response_area_details"),
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
                Exception(),
                self.test_data.get("get_site_area_update"),
                Exception(),
                Exception(),
                self.test_data.get("get_site_building_update"),
                self.test_data.get("update_site_building_response"),
                self.test_data.get("update_site_building_response_details"),
                Exception(),
                Exception(),
                self.test_data.get("get_site_floor_update"),
                self.test_data.get("update_site_floor_response"),
                self.test_data.get("update_site_floor_response_details"),
                self.test_data.get("get_site_updated_floor"),
            ]

        elif "update_a_site" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                Exception(),
                self.test_data.get("new_update_site_area"),
                Exception(),
                Exception(),
                self.test_data.get("new_update_site_building"),
                Exception(),
                Exception(),
                self.test_data.get("new_update_site_floor"),
                self.test_data.get("new_update_floor_response"),
                self.test_data.get("new_update_floor_response_details"),
                self.test_data.get("new_update_site_floor"),
            ]

        elif "delete_a_site" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                # Exception(),
                self.test_data.get("get_site_floor_a_delete"),
                self.test_data.get("get_sites_assigned_devices_network"),
                self.test_data.get("delete_a_floor_response"),
                self.test_data.get("delete_a_floor_response_details"),
                Exception(),
                self.test_data.get("get_site_building_a_delete"),
                self.test_data.get("delete_a_building_response"),
                self.test_data.get("delete_a_building_response_details"),
                Exception(),
                self.test_data.get("get_site_area_a_delete"),
                self.test_data.get("delete_an_area_response"),
                self.test_data.get("delete_an_area_response_details"),
            ]

        elif "delete_site" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                Exception(),
                Exception(),
                self.test_data.get("get_new_delete_floor"),
                self.test_data.get("new_get_membership"),
                self.test_data.get("new_floor_delete_response"),
                self.test_data.get("new_floor_delete_response_details"),
                Exception(),
                Exception(),
                self.test_data.get("get_new_delete_building"),
                self.test_data.get("new_get_membership1"),
                self.test_data.get("new_building_delete_response"),
                self.test_data.get("new_floor_building_response_details"),
                Exception(),
                Exception(),
                self.test_data.get("get_new_area_building"),
                self.test_data.get("new_get_membership2"),
                self.test_data.get("new_area_delete_response"),
                self.test_data.get("new_area_delete_response_details"),
            ]

        elif "verify_diff" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                Exception(),
                self.test_data.get("get_site_create_area"),
                Exception(),
                self.test_data.get("get_site_create_building"),
                Exception(),
                self.test_data.get("get_site_create_floor"),
            ]

    def test_Site_workflow_manager_create_bulk_site(self):
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
                config=self.playbook_config_bulk_site
            )
        )
        result = self.execute_module(changed=True, failed=False)
        self.assertEqual(
            result.get('msg'),
            "Site(s) '[['japan151', 'Abc2', 'blossom', 'cherry']]' created successfully in Cisco Catalyst Center."
        )

    def test_Site_workflow_manager_create_site(self):
        """
        Test case for site workflow manager when creating a site.

        This test case checks the behavior of the site workflow manager when creating a new site in the specified DNAC.
        """
        set_module_args(
            dict(
                dnac_host="1.1.1.1",
                dnac_username="dummy",
                dnac_password="dummy",
                dnac_version="2.3.5.3",
                dnac_log=True,
                state="merged",
                config=self.playbook_config_site
            )
        )
        result = self.execute_module(changed=True, failed=False)
        self.assertEqual(
            result.get('msg'),
            "Site(s) '['Global/japan8888', 'Global/japan8888/blossom', 'Global/japan8888/blossom/cherry']' created successfully in Cisco Catalyst Center."
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
                config=self.playbook_config_invalid_param
            )
        )
        result = self.execute_module(changed=False, failed=True)
        self.assertFalse(
            "Invalid parameters in playbook:" in result.get('msg')
        )

    def test_site_workflow_manager_invalid_delete_site(self):

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
                config=self.test_data.get("playbook_config_invalid_param")
            )
        )
        result = self.execute_module(changed=False, failed=True)
        self.assertFalse(
            "Invalid parameters in playbook:" in result.get('msg')
        )

    def test_Site_workflow_manager_invalid_delete_config(self):
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
                config=self.playbook_config_empty
            )
        )
        result = self.execute_module(changed=False, failed=False)
        self.maxDiff = None
        self.assertEqual(
            result.get('msg'),
            "Unable to delete site(s) '[]' as it's not found in Cisco Catalyst Center."
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
                config=self.playbook_config_site
            )
        )
        result = self.execute_module(changed=False, failed=True)
        self.assertEqual(
            result.get('msg'),
            "This version : '2.3.7.6' given yaml format is not applicable to create a site' "
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
        result = self.execute_module(changed=False, failed=False)
        self.assertEqual(
            result.get('msg'),
            "Site(s) '['Global/Mysore', 'Global/Mysore/Mod-x', 'Global/Mysore/Mod-x/Mezzanine']'" +
            " not needs any update in Cisco Catalyst Center."
        )

    def test_Site_workflow_manager_delete_a_site(self):
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
                config=self.playbook_config_delete
            )
        )
        result = self.execute_module(changed=False, failed=True)
        self.assertEqual(
            result.get('msg'),
            "This version : '2.3.7.6' given yaml format is not applicable to create a site' "
        )

    def test_Site_workflow_manager_delete_site(self):
        """
        Test case for site workflow manager when creating a site.

        This test case checks the behavior of the site workflow manager when creating a new site in the specified DNAC.
        """
        set_module_args(
            dict(
                dnac_host="1.1.1.1",
                dnac_username="dummy",
                dnac_password="dummy",
                dnac_version="2.3.5.3",
                dnac_log=True,
                state="merged",
                config=self.playbook_config_site
            )
        )
        result = self.execute_module(changed=True, failed=False)
        self.assertEqual(
            result.get('msg'),
            "Site(s) '['Global/japan8888/blossom', 'Global/japan8888/blossom']' updated successfully in Cisco Catalyst Center."
        )

    def test_Site_workflow_manager_update_site(self):
        """
        Test case for site workflow manager when creating a site.

        This test case checks the behavior of the site workflow manager when creating a new site in the specified DNAC.
        """
        set_module_args(
            dict(
                dnac_host="1.1.1.1",
                dnac_username="dummy",
                dnac_password="dummy",
                dnac_version="2.3.5.3",
                dnac_log=True,
                state="merged",
                config=self.playbook_config_update_site
            )
        )
        result = self.execute_module(changed=True, failed=False)
        self.maxDiff = None
        self.assertEqual(
            result.get('msg'),
            "Site(s) '['Global/japan8888/blossom/cherry', 'Global/japan8888/blossom/cherry']' updated successfully and some site(s)"
            " '['Global/japan8888']' not needs any update in Cisco Catalyst\n" +
            "                                Center."
        )

    def test_Site_workflow_manager_update_a_site(self):
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
                config=self.playbook_config_update_site
            )
        )
        result = self.execute_module(changed=False, failed=True)
        self.assertEqual(
            result.get('msg'),
            "This version : '2.3.7.6' given yaml format is not applicable to create a site' "
        )
