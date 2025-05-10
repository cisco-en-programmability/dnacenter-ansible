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

    playbook_provision_wired_device = test_data.get("playbook_provision_wired_device")
    playbook_reprovision_wired_device = test_data.get("playbook_reprovision_wired_device")
    playbook_provision_device = test_data.get("playbook_provision_device")

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
        if "playbook_provision_wired_device" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("device_response"),
                self.test_data.get("get_sites"),
                self.test_data.get("get_network_device_by_ip_10"),
                self.test_data.get("get_sites_1"),
                self.test_data.get("get_sites_2"),
                self.test_data.get("get_device"),
                self.test_data.get("get_provisioned_devices"),
                self.test_data.get("provision_wired_device_response"),
            ]
        elif "playbook_reprovision_wired_device" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("device_response_10"),
                self.test_data.get("get_sites_10"),
                self.test_data.get("get_network_device_by_ip_20"),
                self.test_data.get("get_sites_11"),
                self.test_data.get("re_provision_devices"),
                self.test_data.get("Task_Details_10"),
                self.test_data.get("Task_Details_11"),
                self.test_data.get("re_provision_response"),
            ]

        elif "playbook_provision_device" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("device_response_20"),
                self.test_data.get("get_sites_20"),
                self.test_data.get("get_network_device_by_ip_20"),
                self.test_data.get("get_provisioned_devices_20"),
                self.test_data.get("provision_devices"),
                self.test_data.get("task_details"),
                self.test_data.get("task_details_1"),
                self.test_data.get("provision_device_response"),
            ]

    def test_provision_workflow_manager_playbook_provision_wired_device(self):
        """
        Test case for add device with full crendentials.

        This test case checks the addition of new network device added with full credentials in Cisco Catalyst Center.
        """
        set_module_args(
            dict(
                dnac_host="1.1.1.1",
                dnac_version="2.3.7.9",
                dnac_username="dummy",
                dnac_password="dummy",
                dnac_log=True,
                state="merged",
                config=self.playbook_provision_wired_device
            )
        )
        result = self.execute_module(changed=True, failed=False)
        print(result)
        self.assertEqual(
            result.get('msg'),
            ["Wired Device '204.1.2.6' is already provisioned."]
        )

    def test_provision_workflow_manager_playbook_reprovision_wired_device(self):
        """
        Test case for add device with full crendentials.

        This test case checks the addition of new network device added with full credentials in Cisco Catalyst Center.
        """
        set_module_args(
            dict(
                dnac_host="1.1.1.1",
                dnac_version="2.3.7.9",
                dnac_username="dummy",
                dnac_password="dummy",
                dnac_log=True,
                state="merged",
                config=self.playbook_reprovision_wired_device
            )
        )
        result = self.execute_module(changed=True, failed=False)
        print(result)
        self.assertEqual(
            result.get('msg'),
            ["re-provisioning of the device(s) '['204.1.2.6']' completed successfully."]
        )

    def test_provision_workflow_manager_playbook_provision_device(self):
        """
        Test case for add device with full crendentials.

        This test case checks the addition of new network device added with full credentials in Cisco Catalyst Center.
        """
        set_module_args(
            dict(
                dnac_host="1.1.1.1",
                dnac_version="2.3.7.9",
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
            ["Provisioning of the device(s) '['204.1.2.6']' completed successfully."]
        )
