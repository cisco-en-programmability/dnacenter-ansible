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
#   Abhishek Maheswari <abmahesh@cisco.com>
#
# Description:
#   Unit tests for the Ansible module `sda_fabric_sites_zones_workflow_manager`.
#   These tests cover various SDA fabric sites zones operations such as creation,
#   update, deletion, and validation logic using mocked Catalyst Center responses.
from __future__ import absolute_import, division, print_function

__metaclass__ = type
from unittest.mock import patch
from ansible_collections.cisco.dnac.plugins.modules import sda_fabric_sites_zones_workflow_manager
from .dnac_module import TestDnacModule, set_module_args, loadPlaybookData


class TestDnacFabricSitesZonesWorkflow(TestDnacModule):

    module = sda_fabric_sites_zones_workflow_manager
    test_data = loadPlaybookData("sda_fabric_sites_zones_workflow_manager")
    playbook_config_create_fabric_site_without_data_collection = test_data.get("playbook_config_create_fabric_site_without_data_collection")
    playbook_config_create_fabric_site_with_data_collection_and_verify = test_data.get("playbook_config_create_fabric_site_with_data_collection_and_verify")
    playbook_config_create_fabric_zone = test_data.get("playbook_config_create_fabric_zone")
    playbook_config_update_fabric_site_with_data_collection = test_data.get("playbook_config_update_fabric_site_with_data_collection")
    playbook_config_update_authentication_profile_for_fabric_site = test_data.get("playbook_config_update_authentication_profile_for_fabric_site")
    playbook_config_apply_pending_fabric_events = test_data.get("playbook_config_apply_pending_fabric_events")
    playbook_config_delete_fabric_zone = test_data.get("playbook_config_delete_fabric_zone")
    playbook_config_delete_fabric_site_with_verify = test_data.get("playbook_config_delete_fabric_site_with_verify")
    playbook_config_invalid_authentication_profile = test_data.get("playbook_config_invalid_authentication_profile")

    def setUp(self):
        super(TestDnacFabricSitesZonesWorkflow, self).setUp()

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
        super(TestDnacFabricSitesZonesWorkflow, self).tearDown()
        self.mock_dnac_exec.stop()
        self.mock_dnac_init.stop()

    def load_fixtures(self, response=None, device=""):
        """
        Load fixtures for user.
        """

        if "create_fabric_site_without_data_collection" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("get_site_details"),
                self.test_data.get("get_empty_fabric_site_details"),
                self.test_data.get("get_site_details_2"),
                self.test_data.get("get_wired_data_collection_details_disable"),
                self.test_data.get("get_wired_data_collection_details_disable"),
                self.test_data.get("response_get_task_id_success"),
                self.test_data.get("response_get_task_status_by_id_success"),
                self.test_data.get("get_site_details_3"),
                self.test_data.get("response_get_task_id_success_add_fabric_site"),
                self.test_data.get("response_get_task_status_by_id_success_add_fabric_site"),
            ]

        elif "create_fabric_site_with_data_collection_and_verify" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("get_site_details"),
                self.test_data.get("get_empty_fabric_site_details"),
                self.test_data.get("get_site_details_2"),
                self.test_data.get("get_wired_data_collection_details_enable"),
                self.test_data.get("get_site_details_3"),
                self.test_data.get("response_get_task_id_success_add_fabric_site"),
                self.test_data.get("response_get_task_status_by_id_success_add_fabric_site"),
                self.test_data.get("get_site_details"),
                self.test_data.get("get_fabric_site_details"),
                self.test_data.get("get_site_details")
            ]

        elif "update_fabric_site_with_data_collection" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("get_site_details"),
                self.test_data.get("get_fabric_site_details"),
                self.test_data.get("get_site_details_2"),
                self.test_data.get("get_wired_data_collection_details_enable"),
                self.test_data.get("get_fabric_site_details"),
                self.test_data.get("response_get_task_id_success_update_fabric_site"),
                self.test_data.get("response_get_task_status_by_id_success_update_fabric_site")
            ]

        elif "apply_pending_fabric_events" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("get_site_details"),
                self.test_data.get("get_fabric_site_details"),
                self.test_data.get("get_site_details_2"),
                self.test_data.get("get_wired_data_collection_details_enable"),
                self.test_data.get("get_fabric_site_details"),
                self.test_data.get("response_get_pending_fabric_events"),
                self.test_data.get("response_get_task_id_success_apply_pending_event"),
                self.test_data.get("response_get_task_status_by_id_success_apply_pending_event"),
                self.test_data.get("response_get_task_id_success_update_fabric_site"),
                self.test_data.get("response_get_task_status_by_id_success_update_fabric_site")
            ]

        elif "create_fabric_zone" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("get_site_details"),
                self.test_data.get("get_empty_fabric_zone_details"),
                self.test_data.get("get_site_details_2"),
                self.test_data.get("get_wired_data_collection_details_enable"),
                self.test_data.get("get_site_details_3"),
                self.test_data.get("response_get_task_id_success_add_fabric_zone"),
                self.test_data.get("response_get_task_status_by_id_success_add_fabric_zone")
            ]

        elif "update_authentication_profile_for_fabric_site" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("get_site_details"),
                self.test_data.get("get_fabric_site_details"),
                self.test_data.get("get_site_details_2"),
                self.test_data.get("get_wired_data_collection_details_enable"),
                self.test_data.get("get_fabric_site_details"),
                self.test_data.get("response_get_task_id_success_update_fabric_site"),
                self.test_data.get("response_get_task_status_by_id_success_update_fabric_site"),
                self.test_data.get("get_fabric_site_details"),
                self.test_data.get("response_get_authentication_profile"),
                self.test_data.get("response_get_task_id_success_update_auth_profile"),
                self.test_data.get("response_get_task_status_by_id_success_update_auth_profile")
            ]

        elif "delete_fabric_zone" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("get_zone_site_details"),
                self.test_data.get("get_fabric_zone_details"),
                self.test_data.get("get_zone_site_details"),
                self.test_data.get("get_fabric_zone_details"),
                self.test_data.get("response_get_task_id_success_delete_fabric_zone"),
                self.test_data.get("response_get_task_status_by_id_success_delete_fabric_zone")
            ]

        elif "delete_fabric_site_with_verify" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("get_site_details"),
                self.test_data.get("get_fabric_site_details"),
                self.test_data.get("get_site_details_2"),
                self.test_data.get("get_fabric_site_details"),
                self.test_data.get("response_get_task_id_success_delete_fabric_zone"),
                self.test_data.get("response_get_task_status_by_id_success_delete_fabric_zone"),
                self.test_data.get("get_site_details"),
                self.test_data.get("get_empty_fabric_site_details"),
                self.test_data.get("get_site_details")
            ]

        elif "invalid_authentication_profile" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("get_site_details"),
                self.test_data.get("get_fabric_site_details"),
                self.test_data.get("get_site_details_2")
            ]

    def test_sda_fabric_sites_zones_workflow_manager_create_fabric_site_without_data_collection(self):
        """
        Test case for sda fabric sites zones workflow manager when creating a fabric site by enable the wired data collection.

        This test case checks the behavior of the sda fabric sites zones workflow manager when creating a new fabric site by enabling
        the wired data collection in the specified Catalyst Center.
        """

        set_module_args(
            dict(
                dnac_host="1.1.1.1",
                dnac_username="dummy",
                dnac_password="dummy",
                dnac_version="2.3.7.9",
                dnac_log=True,
                config_verify=False,
                state="merged",
                config=self.playbook_config_create_fabric_site_without_data_collection
            )
        )
        result = self.execute_module(changed=True, failed=False)
        self.assertIn(
            "created successfully",
            result.get('msg')
        )

    def test_sda_fabric_sites_zones_workflow_manager_create_fabric_site_with_data_collection_and_verify(self):
        """
        Test case for sda fabric sites zones workflow manager when creating a fabric site when wired data collection is already enabled.

        This test case checks the behavior of the sda fabric sites zones workflow manager when creating a new fabric site without enabling
        the wired data collection in the specified Catalyst Center.
        """

        set_module_args(
            dict(
                dnac_host="1.1.1.1",
                dnac_username="dummy",
                dnac_password="dummy",
                dnac_version="2.3.7.6",
                dnac_log=True,
                config_verify=True,
                state="merged",
                config=self.playbook_config_create_fabric_site_with_data_collection_and_verify
            )
        )
        result = self.execute_module(changed=True, failed=False)
        self.assertIn(
            "created successfully",
            result.get('msg')
        )

    def test_sda_fabric_sites_zones_workflow_manager_update_fabric_site_with_data_collection(self):
        """
        Test case for sda fabric sites zones workflow manager when updating a site.

        This test case checks the behavior of the sda fabric sites zones workflow manager when updating a new site
        with enabling wired end point data collection in the specified Catalyst Center.
        """

        set_module_args(
            dict(
                dnac_host="1.1.1.1",
                dnac_username="dummy",
                dnac_password="dummy",
                dnac_version="2.3.7.9",
                dnac_log=True,
                config_verify=False,
                state="merged",
                config=self.playbook_config_update_fabric_site_with_data_collection
            )
        )
        result = self.execute_module(changed=True, failed=False)
        self.assertIn(
            "updated successfully",
            result.get('msg')
        )

    def test_sda_fabric_sites_zones_workflow_manager_apply_pending_fabric_events(self):
        """
        Test case for sda fabric sites zones workflow manager when reconfigure the fabric site.

        This test case checks the behavior of the sda fabric sites zones workflow manager when reconfiguring the fabric site
        site in the specified Catalyst Center.
        """
        set_module_args(
            dict(
                dnac_host="1.1.1.1",
                dnac_username="dummy",
                dnac_password="dummy",
                dnac_version="2.3.7.9",
                dnac_log=True,
                config_verify=False,
                state="merged",
                config=self.playbook_config_apply_pending_fabric_events
            )
        )
        result = self.execute_module(changed=True, failed=False)
        self.assertIn(
            "applied successfully",
            result.get('msg')
        )

    def test_sda_fabric_sites_zones_workflow_manager_update_authentication_profile_for_fabric_site(self):
        """
        Test case for sda fabric sites zones workflow manager when updating an authentication profile for a fabric site or zone.

        This test case checks the behavior of the sda fabric sites zones workflow manager when updating an authentication profile
        for a fabric site or zone in the specified Catalyst Center.
        """

        set_module_args(
            dict(
                dnac_host="1.1.1.1",
                dnac_username="dummy",
                dnac_password="dummy",
                dnac_version="2.3.7.9",
                dnac_log=True,
                config_verify=False,
                state="merged",
                config=self.playbook_config_update_authentication_profile_for_fabric_site
            )
        )
        result = self.execute_module(changed=True, failed=False)
        self.assertIn(
            "updated successfully",
            result.get('msg')
        )

    def test_sda_fabric_sites_zones_workflow_manager_create_fabric_zone(self):
        """
        Test case for sda fabric sites zones workflow manager when creating a fabric zone.

        This test case checks the behavior of the sda fabric sites zones workflow manager when creating a fabric zone
        in the specified Catalyst Center.
        """

        set_module_args(
            dict(
                dnac_host="1.1.1.1",
                dnac_username="dummy",
                dnac_password="dummy",
                dnac_version="2.3.7.9",
                dnac_log=True,
                config_verify=False,
                state="merged",
                config=self.playbook_config_create_fabric_zone
            )
        )
        result = self.execute_module(changed=True, failed=False)
        self.assertIn(
            "created successfully",
            result.get('msg')
        )

    def test_sda_fabric_sites_zones_workflow_manager_delete_fabric_zone(self):
        """
        Test case for sda fabric sites zones workflow manager when deleting a fabric zone.

        This test case checks the behavior of the sda fabric sites zones workflow manager when deleting a fabric zone
        in the specified Catalyst Center.
        """

        set_module_args(
            dict(
                dnac_host="1.1.1.1",
                dnac_username="dummy",
                dnac_password="dummy",
                dnac_version="2.3.7.9",
                dnac_log=True,
                config_verify=False,
                state="deleted",
                config=self.playbook_config_delete_fabric_zone
            )
        )
        result = self.execute_module(changed=True, failed=False)
        self.assertIn(
            "deleted successfully",
            result.get('msg')
        )

    def test_sda_fabric_sites_zones_workflow_manager_delete_fabric_site_with_verify(self):
        """
        Test case for sda fabric sites zones workflow manager when deleting a fabric site.

        This test case checks the behavior of the sda fabric sites zones workflow manager when deleting a fabric site
        in the specified Catalyst Center.
        """

        set_module_args(
            dict(
                dnac_host="1.1.1.1",
                dnac_username="dummy",
                dnac_password="dummy",
                dnac_version="2.3.7.9",
                dnac_log=True,
                config_verify=True,
                state="deleted",
                config=self.playbook_config_delete_fabric_site_with_verify
            )
        )
        result = self.execute_module(changed=True, failed=False)
        self.assertIn(
            "deleted successfully",
            result.get('msg')
        )

    def test_sda_fabric_sites_zones_workflow_manager_invalid_authentication_profile(self):
        """
        Test case for sda fabric sites zones workflow manager when an invalid authentication profile is provided in the input playbook.

        This test case checks the behavior of the sda fabric sites zones workflow manager when an invalid authentication profile is
        provided in the input playbook in the specified Catalyst Center.
        """

        set_module_args(
            dict(
                dnac_host="1.1.1.1",
                dnac_username="dummy",
                dnac_password="dummy",
                dnac_version="2.3.7.9",
                dnac_log=True,
                config_verify=False,
                state="merged",
                config=self.playbook_config_invalid_authentication_profile
            )
        )
        result = self.execute_module(changed=False, failed=True)
        self.assertIn(
            "Invalid authentication_profile",
            result.get('msg')
        )
