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
#   Unit tests for the Ansible module `sda_fabric_transits_workflow_manager`.
#   These tests cover various SDA fabric transits type such as ip based, BGP LISP based,
#   LISP Pub Sub based and deletion, and validation of these transits logic using mocked
#   Catalyst Center responses.
from __future__ import absolute_import, division, print_function

__metaclass__ = type
from unittest.mock import patch
from ansible_collections.cisco.dnac.plugins.modules import sda_fabric_transits_workflow_manager
from .dnac_module import TestDnacModule, set_module_args, loadPlaybookData


class TestDnacSdaFabricTransits(TestDnacModule):

    module = sda_fabric_transits_workflow_manager
    test_data = loadPlaybookData("sda_fabric_transits_workflow_manager")
    playbook_config_create_fabric_ip_based_transits_with_verify = test_data.get("playbook_config_create_fabric_ip_based_transits_with_verify")
    playbook_config_no_update_for_fabric_ip_based_transits_with_verify = test_data.get("playbook_config_no_update_for_fabric_ip_based_transits_with_verify")
    playbook_config_create_fabric_lisp_bgp_based_transits = test_data.get("playbook_config_create_fabric_lisp_bgp_based_transits")
    playbook_config_create_fabric_lisp_pub_sub_based_transits = test_data.get("playbook_config_create_fabric_lisp_pub_sub_based_transits")
    playbook_config_delete_sda_fabric_transits_with_verify = test_data.get("playbook_config_delete_sda_fabric_transits_with_verify")
    playbook_config_delete_absent_sda_fabric_transits = test_data.get("playbook_config_delete_absent_sda_fabric_transits")
    playbook_config_failed_fabric_lisp_bgp_based_transits_creation = test_data.get("playbook_config_failed_fabric_lisp_bgp_based_transits_creation")

    def setUp(self):
        super(TestDnacSdaFabricTransits, self).setUp()

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
        super(TestDnacSdaFabricTransits, self).tearDown()
        self.mock_dnac_exec.stop()
        self.mock_dnac_init.stop()

    def load_fixtures(self, response=None, device=""):
        """
        Load fixtures for user.
        """

        if "create_fabric_ip_based_transits_with_verify" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("get_available_transit_networks"),
                self.test_data.get("get_empty_available_transit_networks"),
                self.test_data.get("add_transit_api_task_id_response"),
                self.test_data.get("success_task_id_response"),
                self.test_data.get("get_created_transits_networks")
            ]

        elif "no_update_for_fabric_ip_based_transits_with_verify" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("get_created_transits_networks"),
                self.test_data.get("get_created_transits_networks")
            ]

        elif "create_fabric_lisp_bgp_based_transits" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("get_created_transits_networks"),
                self.test_data.get("get_empty_available_transit_networks"),
                self.test_data.get("get_device_details"),
                self.test_data.get("add_transit_api_task_id_response"),
                self.test_data.get("success_task_id_response")
            ]

        elif "failed_fabric_lisp_bgp_based_transits_creation" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("get_created_transits_networks"),
                self.test_data.get("get_empty_available_transit_networks"),
                self.test_data.get("get_device_details"),
                self.test_data.get("add_transit_api_task_id_response"),
                self.test_data.get("failed_task_id_response"),
                self.test_data.get("get_failed_task_details")
            ]

        elif "create_fabric_lisp_pub_sub_based_transits" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("get_created_transits_networks"),
                self.test_data.get("get_empty_available_transit_networks"),
                self.test_data.get("get_device_details"),
                self.test_data.get("add_transit_api_task_id_response"),
                self.test_data.get("success_task_id_response")
            ]

        elif "delete_sda_fabric_transits_with_verify" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("get_created_transits_networks"),
                self.test_data.get("delete_transit_api_task_id_response"),
                self.test_data.get("success_task_id_response"),
                self.test_data.get("get_transits_after_deletion"),
                self.test_data.get("get_empty_available_transit_networks")
            ]

        elif "delete_absent_sda_fabric_transits" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("get_transits_after_deletion"),
                self.test_data.get("get_empty_available_transit_networks")
            ]

        elif "invalid_testbed_release" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("get_invalid_testbed_release"),
            ]

    def test_sda_fabric_transits_workflow_manager_create_fabric_ip_based_transits_with_verify(self):
        """
        Test case for sda fabric virtual networks workflow manager to delete a layer2 fabric vlan.

        This test case checks the behavior of the sda fabric virtual networks workflow manager when a layer2 fabric vlan
        needs to be deleted in the specified Catalyst Center.
        """

        set_module_args(
            dict(
                dnac_host="1.1.1.1",
                dnac_username="dummy",
                dnac_password="dummy",
                dnac_version="2.3.7.9",
                dnac_log=True,
                config_verify=True,
                state="merged",
                config=self.playbook_config_create_fabric_ip_based_transits_with_verify
            )
        )
        result = self.execute_module(changed=True, failed=False)
        print(result)
        self.assertIn(
            "Successfully created",
            result.get('msg')
        )

    def test_sda_fabric_transits_workflow_manager_no_update_for_fabric_ip_based_transits_with_verify(self):
        set_module_args(
            dict(
                dnac_host="1.1.1.1",
                dnac_username="dummy",
                dnac_password="dummy",
                dnac_version="2.3.7.9",
                dnac_log=True,
                config_verify=True,
                state="merged",
                config=self.playbook_config_no_update_for_fabric_ip_based_transits_with_verify
            )
        )
        result = self.execute_module(changed=False, failed=False)
        print(result)
        self.assertIn(
            "Success",
            result.get('response')[0].get('fabric_transits').get('Validation')
        )

    def test_sda_fabric_transits_workflow_manager_create_fabric_lisp_bgp_based_transits(self):
        """
        Test case for sda fabric virtual networks workflow manager to delete a layer2 fabric vlan.

        This test case checks the behavior of the sda fabric virtual networks workflow manager when a layer2 fabric vlan
        needs to be deleted in the specified Catalyst Center.
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
                config=self.playbook_config_create_fabric_lisp_bgp_based_transits
            )
        )
        result = self.execute_module(changed=True, failed=False)
        print(result)
        self.assertIn(
            "Successfully created",
            result.get('msg')
        )

    def test_sda_fabric_transits_workflow_manager_create_fabric_lisp_pub_sub_based_transits(self):
        """
        Test case for sda fabric virtual networks workflow manager to delete a layer2 fabric vlan.

        This test case checks the behavior of the sda fabric virtual networks workflow manager when a layer2 fabric vlan
        needs to be deleted in the specified Catalyst Center.
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
                config=self.playbook_config_create_fabric_lisp_pub_sub_based_transits
            )
        )
        result = self.execute_module(changed=True, failed=False)
        print(result)
        self.assertIn(
            "Successfully created",
            result.get('msg')
        )

    def test_sda_fabric_transits_workflow_manager_delete_sda_fabric_transits_with_verify(self):
        """
        Test case for sda fabric virtual networks workflow manager to delete a layer2 fabric vlan.

        This test case checks the behavior of the sda fabric virtual networks workflow manager when a layer2 fabric vlan
        needs to be deleted in the specified Catalyst Center.
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
                config=self.playbook_config_delete_sda_fabric_transits_with_verify
            )
        )
        result = self.execute_module(changed=True, failed=False)
        print(result)
        self.assertIn(
            "Successfully deleted",
            result.get('msg')
        )

    def test_sda_fabric_transits_workflow_manager_delete_absent_sda_fabric_transits(self):
        """
        Test case for sda fabric virtual networks workflow manager to delete a layer2 fabric vlan.

        This test case checks the behavior of the sda fabric virtual networks workflow manager when a layer2 fabric vlan
        needs to be deleted in the specified Catalyst Center.
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
                config=self.playbook_config_delete_absent_sda_fabric_transits
            )
        )
        result = self.execute_module(changed=False, failed=False)
        print(result)
        self.assertIn(
            "transit not found",
            result.get('response')[0].get('fabric_transits').get('msg').get("Sample1")
        )

    def test_sda_fabric_virtual_networks_workflow_manager_invalid_testbed_release(self):
        """
        Test case for sda fabric virtual networks workflow manager for an invalid testbed release.

        This test case checks the behavior of the sda fabric virtual networks workflow manager invalid testbed release
        in the specified Catalyst Center.
        """

        set_module_args(
            dict(
                dnac_host="1.1.1.1",
                dnac_username="dummy",
                dnac_password="dummy",
                dnac_version="2.3.5.3",
                dnac_log=True,
                config_verify=False,
                state="merged",
                config=self.playbook_config_delete_absent_sda_fabric_transits
            )
        )
        result = self.execute_module(changed=False, failed=True)
        self.assertIn(
            "The specified version",
            result.get('msg')
        )

    def test_sda_fabric_virtual_networks_workflow_manager_failed_fabric_lisp_bgp_based_transits_creation(self):
        """
        Test case for sda fabric virtual networks workflow manager for an invalid testbed release.

        This test case checks the behavior of the sda fabric virtual networks workflow manager invalid testbed release
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
                config=self.playbook_config_failed_fabric_lisp_bgp_based_transits_creation
            )
        )
        result = self.execute_module(changed=False, failed=True)
        self.assertIn(
            "Failed to execute",
            result.get('msg')
        )
