# Copyright (c) 2020 Cisco and/or its affiliates.
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
    playbook_config_site = test_data.get("playbook_config_site")
    playbook_update_site = test_data.get("playbook_update_site")
    playbook_config_invalid_param = test_data.get("playbook_config_invalid_param")

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
        if "create_site" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                Exception(),
                self.test_data.get("create_site_area_response"),
                self.test_data.get("currentExecution"),
                self.test_data.get("get_site_area"),
                self.test_data.get("get_site_building"),
                self.test_data.get("get_site_floor")
            ]
        if "update_site" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("get_site_area"),
                self.test_data.get("get_site_building"),
                self.test_data.get("update_site_building"),
                self.test_data.get("building_updation_execution"),
                self.test_data.get("get_site_floor"),
                self.test_data.get("update_site_floor_response"),
                self.test_data.get("floor_updation_execution"),
                self.test_data.get("get_site_updated_floor")
            ]
        if "delete_existing_site" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("get_site_area"),
                self.test_data.get("get_membership"),
                self.test_data.get("get_single_floor_deletion_response"),
                self.test_data.get("delete_site_execution_detail"),
                self.test_data.get("get_single_building_deletion_response"),
                self.test_data.get("delete_site_execution_detail"),
                self.test_data.get("get_single_area_deletion_response"),
                self.test_data.get("delete_site_execution_detail"),
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
                dnac_log=True,
                state="merged",
                config=self.playbook_config_site
            )
        )
        result = self.execute_module(changed=True, failed=False)
        self.assertEqual(
            result.get('msg'),
            "Site(s) '['Global/Mysore']' created successfully and some site(s) '['Global/Mysore/Mod-x'," +
            " 'Global/Mysore/Mod-x/Mezzanine']' not needs any update in Cisco Catalyst\n"
            "                                Center."
        )

    def test_Site_workflow_manager_update_site(self):
        """
        Test case for site workflow manager when an update is needed.

        This test case checks the behavior of the site workflow manager when an

        update is required for the specified site in the DNAC.
        """
        set_module_args(
            dict(
                dnac_host="1.1.1.1",
                dnac_username="dummy",
                dnac_password="dummy",
                dnac_log=True,
                state="merged",
                # config_verify=True,
                config=self.playbook_update_site
            )
        )
        result = self.execute_module(changed=True, failed=False)
        self.assertEqual(
            result.get("msg"),
            "Site(s) '['Global/Mysore/Mod-x', 'Global/Mysore/Mod-x/Mezzanine']' updated successfully and some site(s)"
            " '['Global/Mysore']' not needs any update in Cisco Catalyst\n" +
            "                                Center."
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
                dnac_log=True,
                state="merged",
                config=self.test_data.get("playbook_config_invalid_param")
            )
        )
        result = self.execute_module(changed=False, failed=True)
        self.assertFalse(
            "Invalid parameters in playbook:" in result.get('msg')
        )

    def test_site_workflow_manager_delete_existing_site(self):

        """
        Test case for site workflow manager when deleting an existing site.

        This test case checks the behavior of the site workflow manager when deleting an existing site in the DNAC.
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
        result = self.execute_module(changed=True, failed=False)

        self.assertEqual(
            result.get('msg'),
            "Given site(s) '['Mezzanine', 'Mod-x', 'Global/Mysore']' deleted successfully from Cisco Catalyst Center" +
            " and unable to deleted some site(s) '['Global/Mysore/Mod-x', 'Global/Mysore/Mod-x/Mezzanine']' as they\n" +
            "                    are not found in Cisco Catalyst Center."
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
