# Copyright (c) 2025 Cisco and/or its affiliates.
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
from ansible_collections.cisco.dnac.plugins.modules import network_profile_wireless_workflow_manager
from .dnac_module import TestDnacModule, set_module_args, loadPlaybookData


class TestDnacNetworkWirelessProfileWorkflow(TestDnacModule):
    """
    Unit test class for the network wireless profile module
    """
    module = network_profile_wireless_workflow_manager

    test_data = loadPlaybookData("network_wireless_profile_workflow_manager")
    profile_creation_config = test_data.get("profile_creation_config")

    def setUp(self):
        super(TestDnacNetworkWirelessProfileWorkflow, self).setUp()

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
        super(TestDnacNetworkWirelessProfileWorkflow, self).tearDown()
        self.mock_dnac_exec.stop()
        self.mock_dnac_init.stop()

    def load_fixtures(self, response=None, device=""):
        """
        Load fixtures for user.
        """
        if "profile_creation" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("profile_creation_config"),
                self.test_data.get("wireless_profile_list"),
                self.test_data.get("no_response_received"),
                self.test_data.get("available_templates"),
                self.test_data.get("available_templates"),
                self.test_data.get("get_site_details1"),
                self.test_data.get("get_site_details2"),
                self.test_data.get("get_ssid_list"),
                self.test_data.get("get_site_details3"),
                self.test_data.get("get_ssid_list"),
                self.test_data.get("task_id_response"),
                self.test_data.get("task_details"),
                self.test_data.get("assign_site_task1"),
                self.test_data.get("assign_site_task_details1"),
                self.test_data.get("assign_site_task2"),
                self.test_data.get("assign_site_task_details2"),
                self.test_data.get("assign_template_task1"),
                self.test_data.get("assign_template_task_details1"),
                self.test_data.get("recreate_profile_task"),
                self.test_data.get("recreate_profile_task_details")
            ]

    def test_wireless_profile_creation(self):
        """
        Test case for wireless profile workfollow manager provision and update device.

        This test case checks the behavior of the wireless profile workflow when creation
        in the specified Cisco Catalyst Center.
        """
        set_module_args(
            dict(
                dnac_host="1.1.1.1",
                dnac_username="dummy",
                dnac_password="dummy",
                dnac_log=True,
                state="merged",
                dnac_version="2.3.7.9",
                config_verify=True,
                config=self.profile_creation_config
            )
        )

        result = self.execute_module(changed=True, failed=False)
        self.maxDiff = None
        self.assertEqual(
            result.get('msg'),
            "AP Configuration - LTTS_Test_9124_T2 updated Successfully"
        )
