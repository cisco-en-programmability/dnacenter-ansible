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
#   Unit tests for the Ansible module `sda_fabric_virtual_networks_workflow_manager`.
#   These tests cover various SDA virtual network operations such as creation,
#   update, deletion, and validation logic using mocked Catalyst Center responses.
from __future__ import absolute_import, division, print_function

__metaclass__ = type
from unittest.mock import patch
from ansible_collections.cisco.dnac.plugins.modules import sda_fabric_virtual_networks_workflow_manager
from .dnac_module import TestDnacModule, set_module_args, loadPlaybookData


class TestDnacFabricSitesZonesWorkflow(TestDnacModule):

    module = sda_fabric_virtual_networks_workflow_manager
    test_data = loadPlaybookData("sda_fabric_virtual_networks_workflow_manager")
    playbook_config_create_fabric_vlan_with_verify = test_data.get("playbook_config_create_fabric_vlan_with_verify")
    playbook_config_fabric_vlan_need_no_update = test_data.get("playbook_config_fabric_vlan_need_no_update")
    playbook_config_update_fabric_vlan = test_data.get("playbook_config_update_fabric_vlan")
    playbook_config_create_virtual_network_with_verify = test_data.get("playbook_config_create_virtual_network_with_verify")
    playbook_config_create_anchored_virtual_network = test_data.get("playbook_config_create_anchored_virtual_network")
    playbook_config_virtual_network_needs_no_update = test_data.get("playbook_config_virtual_network_needs_no_update")
    playbook_config_update_virtual_network = test_data.get("playbook_config_update_virtual_network")
    playbook_config_delete_virtual_network_with_verify = test_data.get("playbook_config_delete_virtual_network_with_verify")
    playbook_config_create_anycast_gateway_with_verify = test_data.get("playbook_config_create_anycast_gateway_with_verify")
    playbook_config_anycast_gateway_no_update = test_data.get("playbook_config_anycast_gateway_no_update")
    playbook_config_update_anycast_gateway = test_data.get("playbook_config_update_anycast_gateway")
    playbook_config_delete_anycast_gateway = test_data.get("playbook_config_delete_anycast_gateway")
    playbook_config_delete_absent_anycast_gateway = test_data.get("playbook_config_delete_absent_anycast_gateway")
    playbook_config_delete_absent_virtual_network = test_data.get("playbook_config_delete_absent_virtual_network")
    playbook_config_delete_fabric_vlan_with_verify = test_data.get("playbook_config_delete_fabric_vlan_with_verify")
    playbook_config_delete_absent_fabric_vlan = test_data.get("playbook_config_delete_absent_fabric_vlan")
    playbook_config_failed_anchored_virtual_network_creation = test_data.get("playbook_config_failed_anchored_virtual_network_creation")
    playbook_config_invalid_fabric_vlan_id = test_data.get("playbook_config_invalid_fabric_vlan_id")

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

        if "create_fabric_vlan_with_verify" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("get_empty_fabric_vlan_response"),
                self.test_data.get("get_site_details"),
                self.test_data.get("get_fabric_site_details"),
                self.test_data.get("get_empty_fabric_vlan_response"),
                self.test_data.get("response_get_task_id_success"),
                self.test_data.get("response_get_task_status_by_id_success"),
                self.test_data.get("get_fabric_vlan_response"),
                self.test_data.get("get_site_details"),
                self.test_data.get("get_fabric_site_details"),
                self.test_data.get("get_fabric_vlan_response")
            ]

        elif "fabric_vlan_need_no_update" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("get_fabric_vlan_response"),
                self.test_data.get("get_site_details"),
                self.test_data.get("get_fabric_site_details"),
                self.test_data.get("get_fabric_vlan_response")
            ]

        elif "update_fabric_vlan" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("get_fabric_vlan_response"),
                self.test_data.get("get_site_details"),
                self.test_data.get("get_fabric_site_details"),
                self.test_data.get("get_fabric_vlan_response"),
                self.test_data.get("response_get_task_id_success"),
                self.test_data.get("response_get_task_status_by_id_success")
            ]

        elif "delete_fabric_vlan_with_verify" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("get_fabric_vlan_response"),
                self.test_data.get("get_site_details"),
                self.test_data.get("get_fabric_site_details"),
                self.test_data.get("get_fabric_vlan_response"),
                self.test_data.get("response_get_task_id_success"),
                self.test_data.get("response_get_task_status_by_id_success"),
                self.test_data.get("get_empty_fabric_vlan_response"),
                self.test_data.get("get_site_details"),
                self.test_data.get("get_fabric_site_details"),
                self.test_data.get("get_empty_fabric_vlan_response")
            ]

        elif "delete_absent_fabric_vlan" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("get_empty_fabric_vlan_response"),
                self.test_data.get("get_site_details"),
                self.test_data.get("get_fabric_site_details"),
                self.test_data.get("get_empty_fabric_vlan_response")
            ]

        elif "invalid_fabric_vlan_id" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("get_invalid_fabric_vlan_id"),
            ]

        elif "create_virtual_network_with_verify" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("get_empty_virtual_network_response"),
                self.test_data.get("get_site_details"),
                self.test_data.get("get_fabric_site_details"),
                self.test_data.get("response_get_task_id_success"),
                self.test_data.get("response_get_task_status_by_id_success"),
                self.test_data.get("get_virtual_network_response")
            ]

        elif "create_anchored_virtual_network" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("get_empty_virtual_network_response"),
                self.test_data.get("get_site_details"),
                self.test_data.get("get_fabric_site_details"),
                self.test_data.get("get_site_details"),
                self.test_data.get("get_fabric_site_details"),
                self.test_data.get("response_get_task_id_success"),
                self.test_data.get("response_get_task_status_by_id_success"),
                self.test_data.get("get_anchored_virtual_network_response"),
                self.test_data.get("response_get_task_id_success"),
                self.test_data.get("response_get_task_status_by_id_success")
            ]

        elif "failed_anchored_virtual_network_creation" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("get_empty_virtual_network_response"),
                self.test_data.get("get_site_details"),
                self.test_data.get("get_fabric_site_details"),
                self.test_data.get("get_site_details"),
                self.test_data.get("get_fabric_site_details"),
                self.test_data.get("response_get_task_id_success"),
                self.test_data.get("response_get_task_status_by_id_success"),
                self.test_data.get("get_anchored_virtual_network_response"),
                self.test_data.get("response_get_task_id_success"),
                self.test_data.get("response_get_task_status_by_id_failed_anchored_vn")
            ]

        elif "virtual_network_needs_no_update" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("get_virtual_network_response"),
                self.test_data.get("get_virtual_network_response"),
                self.test_data.get("get_site_details"),
                self.test_data.get("get_fabric_site_details")
            ]

        elif "update_virtual_network" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("get_virtual_network_response"),
                self.test_data.get("get_virtual_network_response"),
                self.test_data.get("get_site_details"),
                self.test_data.get("get_fabric_site_details"),
                self.test_data.get("get_zone_site_details"),
                self.test_data.get("get_fabric_zone_details"),
                self.test_data.get("get_site_details"),
                self.test_data.get("get_fabric_site_details"),
                self.test_data.get("get_zone_site_details"),
                self.test_data.get("get_fabric_zone_details"),
                self.test_data.get("response_get_task_id_success"),
                self.test_data.get("response_get_task_status_by_id_success")
            ]

        elif "delete_virtual_network_with_verify" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("get_anycast_vn_response"),
                self.test_data.get("get_anycast_vn_response"),
                self.test_data.get("get_anycast_vn_response"),
                self.test_data.get("response_get_task_id_success"),
                self.test_data.get("response_get_task_status_by_id_success"),
                self.test_data.get("get_empty_virtual_network_response")
            ]

        elif "delete_absent_virtual_network" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("get_empty_virtual_network_response"),
                self.test_data.get("get_empty_virtual_network_response"),
                self.test_data.get("get_empty_virtual_network_response")
            ]

        elif "create_anycast_gateway_with_verify" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("get_anycast_vn_response"),
                self.test_data.get("get_site_details"),
                self.test_data.get("get_reserve_ip_pool_details"),
                self.test_data.get("get_site_details"),
                self.test_data.get("get_fabric_site_details"),
                self.test_data.get("get_empty_anycast_gateway_response"),
                self.test_data.get("get_site_details"),
                self.test_data.get("get_fabric_site_details"),
                self.test_data.get("get_empty_anycast_gateway_response"),
                self.test_data.get("response_get_task_id_success"),
                self.test_data.get("response_get_task_status_by_id_success"),
                self.test_data.get("get_site_details"),
                self.test_data.get("get_fabric_site_details"),
                self.test_data.get("get_anycast_gateway_details"),
                self.test_data.get("get_site_details"),
                self.test_data.get("get_fabric_site_details"),
                self.test_data.get("get_anycast_gateway_details")
            ]

        elif "anycast_gateway_no_update" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("get_anycast_vn_response"),
                self.test_data.get("get_site_details"),
                self.test_data.get("get_reserve_ip_pool_details"),
                self.test_data.get("get_site_details"),
                self.test_data.get("get_fabric_site_details"),
                self.test_data.get("get_anycast_gateway_details"),
                self.test_data.get("get_site_details"),
                self.test_data.get("get_fabric_site_details"),
                self.test_data.get("get_anycast_gateway_details")
            ]

        elif "update_anycast_gateway" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("get_anycast_vn_response"),
                self.test_data.get("get_site_details"),
                self.test_data.get("get_reserve_ip_pool_details"),
                self.test_data.get("get_site_details"),
                self.test_data.get("get_fabric_site_details"),
                self.test_data.get("get_anycast_gateway_details"),
                self.test_data.get("get_site_details"),
                self.test_data.get("get_fabric_site_details"),
                self.test_data.get("get_anycast_gateway_details"),
                self.test_data.get("response_get_task_id_success"),
                self.test_data.get("response_get_task_status_by_id_success")
            ]

        elif "delete_anycast_gateway" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("get_anycast_vn_response"),
                self.test_data.get("get_site_details"),
                self.test_data.get("get_reserve_ip_pool_details"),
                self.test_data.get("get_site_details"),
                self.test_data.get("get_fabric_site_details"),
                self.test_data.get("get_anycast_gateway_details"),
                self.test_data.get("get_site_details"),
                self.test_data.get("get_fabric_site_details"),
                self.test_data.get("get_reserve_ip_pool_details"),
                self.test_data.get("get_anycast_gateway_details"),
                self.test_data.get("get_anycast_vn_response"),
                self.test_data.get("response_get_task_id_success"),
                self.test_data.get("response_get_task_status_by_id_success"),
                self.test_data.get("get_site_details"),
                self.test_data.get("get_fabric_site_details"),
                self.test_data.get("get_empty_anycast_gateway_response"),
                self.test_data.get("get_site_details"),
                self.test_data.get("get_fabric_site_details"),
                self.test_data.get("get_empty_anycast_gateway_response")
            ]

        elif "delete_absent_anycast_gateway" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("get_anycast_vn_response"),
                self.test_data.get("get_site_details"),
                self.test_data.get("get_reserve_ip_pool_details"),
                self.test_data.get("get_site_details"),
                self.test_data.get("get_fabric_site_details"),
                self.test_data.get("get_empty_anycast_gateway_response"),
                self.test_data.get("get_site_details"),
                self.test_data.get("get_fabric_site_details"),
                self.test_data.get("get_empty_anycast_gateway_response"),
                self.test_data.get("get_site_details"),
                self.test_data.get("get_fabric_site_details"),
                self.test_data.get("get_empty_anycast_gateway_response")
            ]

        elif "invalid_testbed_release" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("get_invalid_testbed_release"),
            ]

    def test_sda_fabric_virtual_networks_workflow_manager_create_fabric_vlan_with_verify(self):
        """
        Test case for sda fabric virtual networks workflow manager when creating a fabric vlan along with the verification.

        This test case checks the behavior of the sda fabric virtual networks workflow manager when creating a new fabric vlan
        along with the verification in the specified Catalyst Center.
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
                config=self.playbook_config_create_fabric_vlan_with_verify
            )
        )
        result = self.execute_module(changed=True, failed=False)
        self.assertIn(
            "created successfully",
            result.get('msg')
        )

    def test_sda_fabric_virtual_networks_workflow_manager_fabric_vlan_need_no_update(self):
        """
        Test case for sda fabric virtual networks workflow manager when fabric vlan(layer 2 virtual network) does not need any update.

        This test case checks the behavior of the sda fabric virtual networks workflow manager when fabric vlan(layer 2 virtual network)
        does not need any update in the specified Catalyst Center.
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
                config=self.playbook_config_create_fabric_vlan_with_verify
            )
        )
        result = self.execute_module(changed=False, failed=False)
        self.assertIn(
            "does not need any update",
            result.get('msg')
        )

    def test_sda_fabric_virtual_networks_workflow_manager_update_fabric_vlan(self):
        """
        Test case for sda fabric virtual networks workflow manager when updating a fabric vlan(layer 2 virtual network).

        This test case checks the behavior of the sda fabric virtual networks workflow manager when updating a fabric vlan
        (layer 2 virtual network) in the specified Catalyst Center.
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
                config=self.playbook_config_update_fabric_vlan
            )
        )
        result = self.execute_module(changed=True, failed=False)
        self.assertIn(
            "updated successfully",
            result.get('msg')
        )

    def test_sda_fabric_virtual_networks_workflow_manager_create_virtual_network_with_verify(self):
        """
        Test case for sda fabric virtual networks workflow manager when creating a virtual network(layer3 virtual network)
        along with the verification.

        This test case checks the behavior of the sda fabric virtual networks workflow manager when creating a virtual network
        (layer3 virtual network) along with the verification in the specified Catalyst Center.
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
                config=self.playbook_config_create_virtual_network_with_verify
            )
        )
        result = self.execute_module(changed=True, failed=False)
        self.assertIn(
            "created successfully",
            result.get('msg')
        )

    def test_sda_fabric_virtual_networks_workflow_manager_create_anchored_virtual_network(self):
        """
        Test case for sda fabric virtual networks workflow manager when creating an anchored virtual network with the main site.

        This test case checks the behavior of the sda fabric virtual networks workflow manager creating an anchored virtual network
        with the main site in the specified Catalyst Center.
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
                config=self.playbook_config_create_anchored_virtual_network
            )
        )
        result = self.execute_module(changed=True, failed=False)
        self.assertIn(
            "created successfully",
            result.get('msg')
        )

    def test_sda_fabric_virtual_networks_workflow_manager_failed_anchored_virtual_network_creation(self):
        """
        Test case for sda fabric virtual networks workflow manager when anchored virtual network creation failed as it
        needs atleast one CP and External Node at the given fabric site.

        This test case checks the behavior of the sda fabric virtual networks workflow manager when anchored virtual network
        creation failed as it needs atleast one CP and External Node at the given fabric site in the specified Catalyst Center.
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
                config=self.playbook_config_failed_anchored_virtual_network_creation
            )
        )
        result = self.execute_module(changed=False, failed=True)
        self.assertIn(
            "An error occurred while",
            result.get('msg')
        )

    def test_sda_fabric_virtual_networks_workflow_manager_virtual_network_needs_no_update(self):
        """
        Test case for sda fabric virtual networks workflow manager when regular virtual network(layer3 virtual network) does not
        needs any update.

        This test case checks the behavior of the sda fabric virtual networks workflow manager when regular virtual network(layer3 virtual network) does not
        needs any update in the specified Catalyst Center.
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
                config=self.playbook_config_virtual_network_needs_no_update
            )
        )
        result = self.execute_module(changed=False, failed=False)
        self.assertIn(
            "does not need any update",
            result.get('msg')
        )

    def test_sda_fabric_virtual_networks_workflow_manager_update_virtual_network(self):
        """
        Test case for sda fabric virtual networks workflow manager when updating a virtual network(layer3 virtual network).

        This test case checks the behavior of the sda fabric virtual networks workflow manager when updating a virtual network
        (layer3 virtual network) in the specified Catalyst Center.
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
                config=self.playbook_config_update_virtual_network
            )
        )
        result = self.execute_module(changed=True, failed=False)
        self.assertIn(
            "updated successfully",
            result.get('msg')
        )

    def test_sda_fabric_virtual_networks_workflow_manager_create_anycast_gateway_with_verify(self):
        """
        Test case for sda fabric virtual networks workflow manager when creating an anycast gateway along with the verification.

        This test case checks the behavior of the sda fabric virtual networks workflow manager when creating an anycast gateway
        along with the verification in the specified Catalyst Center.
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
                config=self.playbook_config_create_anycast_gateway_with_verify
            )
        )
        result = self.execute_module(changed=True, failed=False)
        self.assertIn(
            "added successfully",
            result.get('msg')
        )

    def test_sda_fabric_virtual_networks_workflow_manager_anycast_gateway_no_update(self):
        """
        Test case for sda fabric virtual networks workflow manager when an anycast gateway does not needs any update.

        This test case checks the behavior of the sda fabric virtual networks workflow manager when an anycast gateway does
        not needs any updatein the specified Catalyst Center.
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
                config=self.playbook_config_anycast_gateway_no_update
            )
        )
        result = self.execute_module(changed=False, failed=False)
        self.assertIn(
            "does not need any update",
            result.get('msg')
        )

    def test_sda_fabric_virtual_networks_workflow_manager_update_anycast_gateway(self):
        """
        Test case for sda fabric virtual networks workflow manager when an anycast gateway needs any update.

        This test case checks the behavior of the sda fabric virtual networks workflow manager when an anycast gateway does
        needs any update in the specified Catalyst Center.
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
                config=self.playbook_config_update_anycast_gateway
            )
        )
        result = self.execute_module(changed=True, failed=False)
        self.assertIn(
            "updated successfully",
            result.get('msg')
        )

    def test_sda_fabric_virtual_networks_workflow_manager_delete_anycast_gateway(self):
        """
        Test case for sda fabric virtual networks workflow manager to delete an anycast gateway.

        This test case checks the behavior of the sda fabric virtual networks workflow manager when an anycast gateway
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
                config=self.playbook_config_delete_anycast_gateway
            )
        )
        result = self.execute_module(changed=True, failed=False)
        self.assertIn(
            "deleted successfully",
            result.get('msg')
        )

    def test_sda_fabric_virtual_networks_workflow_manager_delete_absent_anycast_gateway(self):
        """
        Test case for sda fabric virtual networks workflow manager to delete an absent anycast gateway.

        This test case checks the behavior of the sda fabric virtual networks workflow manager when an absent anycast gateway
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
                config=self.playbook_config_delete_absent_anycast_gateway
            )
        )
        result = self.execute_module(changed=False, failed=False)
        self.assertIn(
            "Unable to delete",
            result.get('msg')
        )

    def test_sda_fabric_virtual_networks_workflow_manager_delete_absent_virtual_network(self):
        """
        Test case for sda fabric virtual networks workflow manager to delete an absent virtual network.

        This test case checks the behavior of the sda fabric virtual networks workflow manager when an absent virtual
        network needs to be deleted in the specified Catalyst Center.
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
                config=self.playbook_config_delete_absent_virtual_network
            )
        )
        result = self.execute_module(changed=False, failed=False)
        self.assertIn(
            "Unable to delete",
            result.get('msg')
        )

    def test_sda_fabric_virtual_networks_workflow_manager_delete_fabric_vlan_with_verify(self):
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
                config=self.playbook_config_delete_fabric_vlan_with_verify
            )
        )
        result = self.execute_module(changed=True, failed=False)
        self.assertIn(
            "deleted successfully",
            result.get('msg')
        )

    def test_sda_fabric_virtual_networks_workflow_manager_delete_absent_fabric_vlan(self):
        """
        Test case for sda fabric virtual networks workflow manager to delete an absent layer2 fabric vlan.

        This test case checks the behavior of the sda fabric virtual networks workflow manager when an absent layer2
        fabric vlan needs to be deleted in the specified Catalyst Center.
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
                config=self.playbook_config_delete_absent_fabric_vlan
            )
        )
        result = self.execute_module(changed=False, failed=False)
        self.assertIn(
            "Unable to delete",
            result.get('msg')
        )

    def test_sda_fabric_virtual_networks_workflow_manager_invalid_fabric_vlan_id(self):
        """
        Test case for sda fabric virtual networks workflow manager for an invalid layer2 fabric vlan id.

        This test case checks the behavior of the sda fabric virtual networks workflow manager invalid layer2 fabric
        vlan id in the specified Catalyst Center.
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
                config=self.playbook_config_invalid_fabric_vlan_id
            )
        )
        result = self.execute_module(changed=False, failed=True)
        self.assertIn(
            "Invalid vlan_id",
            result.get('msg')
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
                config=self.playbook_config_failed_anchored_virtual_network_creation
            )
        )
        result = self.execute_module(changed=False, failed=True)
        self.assertIn(
            "The specified version",
            result.get('msg')
        )
