# Copyright (c) 2024 Cisco and/or its affiliates.

# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at

# http://www.apache.org/licenses/LICENSE-2.0
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

from ansible_collections.cisco.dnac.plugins.modules import provision_workflow_manager
from .dnac_module import TestDnacModule, set_module_args, loadPlaybookData


class TestDnacProvisionWorkflow(TestDnacModule):

    module = provision_workflow_manager

    test_data = loadPlaybookData("provision_workflow_manager")

    playbook_assign_wired_device_to_site = test_data.get(
        "playbook_assign_wired_device_to_site")
    playbook_del_provision_device = test_data.get(
        "playbook_del_provision_device")
    playbook_provision_device = test_data.get("playbook_provision_device")
    playbook_del_wireless_provision_not_supported = test_data.get(
        "playbook_del_wireless_provision_not_supported")
    playbook_force_provision_device = test_data.get(
        "playbook_force_provision_device")
    playbook_wireless_provision = test_data.get("playbook_wireless_provision")

    def setUp(self):
        super(TestDnacProvisionWorkflow, self).setUp()

        self.mock_dnac_init = patch(
            "ansible_collections.cisco.dnac.plugins.module_utils.dnac.DNACSDK.__init__")
        self.run_dnac_init = self.mock_dnac_init.start()
        self.run_dnac_init.side_effect = [None]
        self.mock_dnac_exec = patch(
            "ansible_collections.cisco.dnac.plugins.module_utils.dnac.DNACSDK._exec"
        )
        self.run_dnac_exec = self.mock_dnac_exec.start()

    def tearDown(self):
        super(TestDnacProvisionWorkflow, self).tearDown()
        self.mock_dnac_exec.stop()
        self.mock_dnac_init.stop()

    def load_fixtures(self, response=None, device=""):
        """
        Load fixtures for user.
        """
        if "playbook_assign_wired_device_to_site" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("get_network_device_by_ip"),
                self.test_data.get("get_site_details"),
                self.test_data.get("get_provisioned_wired_device"),
                self.test_data.get("get_network_device_by_ip1"),
                # self.test_data.get("get_device_id"),
                # self.test_data.get("is_device_assigned_to_site"),
                self.test_data.get("get_device_detail"),
                self.test_data.get("assign_devices_to_site"),
                self.test_data.get("get_business_api_execution_details"),
                self.test_data.get("response_assign_wired_device_to_site"),
            ]
        elif "playbook_del_provision_device" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("get_network_device_by_ip_delete_success"),
                self.test_data.get("get_sites_delete_success"),
                self.test_data.get("get_site_delete_success"),
                self.test_data.get(
                    "get_provisioned_wired_device_delete_success"),
                self.test_data.get(
                    "delete_provisioned_wired_device_delete_success"),
                self.test_data.get("get_task_by_id_delete_success"),
                self.test_data.get("get_task_by_id1_delete_success"),
                self.test_data.get("delete_provision_device_success"),
            ]
        elif "playbook_provision_device" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("get_network_device_by_ip_prov_device"),
                self.test_data.get("get_sites_prov_device"),
                self.test_data.get("get_site_prov_device"),
                self.test_data.get("get_provisioned_wired_device_prov_device"),
                self.test_data.get("provision_wired_device_prov_device"),
                self.test_data.get("get_task_by_id_prov_device"),
                self.test_data.get("get_task_status"),
                self.test_data.get("get_task_status1"),
                self.test_data.get("get_network_device_by_ip1_prov_device"),
                self.test_data.get(
                    "get_provisioned_wired_device1_prov_device"),
                self.test_data.get("provision_device_response"),
            ]
        elif "playbook_del_wireless_provision_not_supported" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                Exception(),
                # self.test_data.get("get_network_device_by_ip_prov_device"),
                #   self.test_data.get("response_del_wireless_provision_not_supported"),
            ]
        elif "playbook_force_provision_device" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("get_network_device_by_ip_force_provision"),
                self.test_data.get("get_sites_force_provision"),
                self.test_data.get("get_site_force_provision"),
                self.test_data.get("get_provisioned_wired_device_force_provision"),
                self.test_data.get("re_provision_wired_device"),
                self.test_data.get("Task_Details_force_provision"),
                self.test_data.get("Task_Details1_force_provision"),
                self.test_data.get("response_force_provision"),
            ]
        elif "playbook_wireless_provision" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("get_network_device_by_ip_wp"),
                self.test_data.get("get_site_type_wp"),
                self.test_data.get("get_network_device_by_ip1_wp"),
                self.test_data.get("get_business_api_execution_details_wp"),
                self.test_data.get("provision_update_wp"),
                self.test_data.get("get_business_api_execution_details1_wp"),
                self.test_data.get("get_network_device_by_ip3_wp"),
                self.test_data.get("wireless_provision_response_wp"),
            ]

    def test_provision_workflow_manager_playbook_assign_wired_device_to_site(self):
        """
        Test case for add device with full crendentials.

        This test case checks the addition of new network device added with full credentials in Cisco Catalyst Center.
        """
        set_module_args(
            dict(
                dnac_host="1.1.1.1",
                dnac_username="dummy",
                dnac_password="dummy",
                dnac_log=True,
                state="merged",
                config_verify=True,
                config=self.playbook_assign_wired_device_to_site
            )
        )
        result = self.execute_module(changed=True, failed=False)
        print(result)
        self.assertEqual(
            result.get('msg'),
            "Site assignment done successfully"
        )

    def test_provision_workflow_manager_playbook_del_provision_device(self):
        """
        Test case for add device with full crendentials.

        This test case checks the addition of new network device added with full credentials in Cisco Catalyst Center.
        """
        set_module_args(
            dict(
                dnac_host="1.1.1.1",
                dnac_username="dummy",
                dnac_password="dummy",
                dnac_log=True,
                state="deleted",
                config_verify=True,
                config=self.playbook_del_provision_device
            )
        )
        result = self.execute_module(changed=True, failed=False)
        print(result)
        self.assertEqual(
            result.get('msg'),
            "Deletion done Successfully"
        )

    def test_provision_workflow_manager_playbook_provision_device(self):
        """
        Test case for add device with full crendentials.

        This test case checks the addition of new network device added with full credentials in Cisco Catalyst Center.
        """
        set_module_args(
            dict(
                dnac_host="1.1.1.1",
                dnac_username="dummy",
                dnac_password="dummy",
                dnac_log=True,
                state="merged",
                config=self.playbook_provision_device
            )
        )
        result = self.execute_module(changed=True, failed=False)
        print(result)
        self.assertEqual(
            result.get('msg'),
            "Provision done Successfully"
        )

    def test_provision_workflow_manager_playbook_del_wireless_provision_not_supported(self):
        """
        Test case for add device with full crendentials.

        This test case checks the addition of new network device added with full credentials in Cisco Catalyst Center.
        """
        set_module_args(
            dict(
                dnac_host="1.1.1.1",
                dnac_username="dummy",
                dnac_password="dummy",
                dnac_log=True,
                state="deleted",
                config_verify=True,
                config=self.playbook_del_wireless_provision_not_supported
            )
        )
        result = self.execute_module(changed=False, failed=True)
        print(result)
        self.assertEqual(
            result.get('msg'),
            ""
            # "Missing Managed AP Locations: Please specify the intended location(s) for the wireless device within the site hierarchy."
            # "APIs are not supported for the device"
        )

    def test_provision_workflow_manager_playbook_force_provision_device(self):
        """
        Test case for add device with full crendentials.

        This test case checks the addition of new network device added with full credentials in Cisco Catalyst Center.
        """
        set_module_args(
            dict(
                dnac_host="1.1.1.1",
                dnac_username="dummy",
                dnac_password="dummy",
                dnac_log=True,
                state="merged",
                config=self.playbook_force_provision_device
            )
        )
        result = self.execute_module(changed=True, failed=False)
        print(result)
        self.assertEqual(
            result.get('msg'),
            "Provision done Successfully"
        )

    def test_provision_workflow_manager_playbook_wireless_provision(self):
        """
        Test case for add device with full crendentials.

        This test case checks the addition of new network device added with full credentials in Cisco Catalyst Center.
        """
        set_module_args(
            dict(
                dnac_host="1.1.1.1",
                dnac_username="dummy",
                dnac_password="dummy",
                dnac_log=True,
                state="merged",
                config=self.playbook_wireless_provisionZ
            )
        )
        result = self.execute_module(changed=True, failed=False)
        print(result)
        self.assertEqual(
            result.get('msg'),
            "Provision done Successfully"
        )
