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

    test_data = loadPlaybookData("network_profile_wireless_workflow_manager")
    basic_profile_creation_config = test_data.get("basic_profile_creation_config")
    profile_deletion = test_data.get("profile_deletion")
    profile_creation_config_feature_template = test_data.get("profile_creation_config_feature_template")

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
        if "basic_profile_creation" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("wireless_profile_list"),
                self.test_data.get("gets_the_templates_available"),
                self.test_data.get("get_sites_basic"),
                self.test_data.get("get_sites4"),
                self.test_data.get("get_sites2"),
                self.test_data.get("get_enterprise_ssid"),
                self.test_data.get("get_interfaces_basic"),
                self.test_data.get("get_feature_template_summary_basic"),
                self.test_data.get("get80211be_profiles_basic"),
                self.test_data.get("response_for_profile_creation"),
                self.test_data.get("get_task_details_response"),
                self.test_data.get("get_task_progress"),
                self.test_data.get("get_task_details_response"),
                self.test_data.get("get_task_progress"),
                self.test_data.get("get_sites_basic"),
                self.test_data.get("assign_site1_response"),
                self.test_data.get("get_sites_basic"),
                self.test_data.get("get_sites4"),
                self.test_data.get("get_sites2")
            ]
        elif "profile_details_deletion" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("verify_wireless_profile_list"),
                self.test_data.get("verify_profile_details_basic"),
                self.test_data.get("gets_the_templates_available"),
                self.test_data.get("get_sites_basic"),
                self.test_data.get("get_sites4"),
                self.test_data.get("get_sites2"),
                self.test_data.get("get_enterprise_ssid"),
                self.test_data.get("get_interfaces_basic"),
                self.test_data.get("get_feature_template_summary_basic"),
                self.test_data.get("get_cli_template_for_profile_basic"),
                self.test_data.get("get_site_list_for_profile_basic"),
                self.test_data.get("get80211be_profiles_basic"),
                self.test_data.get("assign_template1_response"),
                self.test_data.get("get_template1_task_details"),
                self.test_data.get("get_template1_task_progress"),
                self.test_data.get("assign_site1_response"),
                self.test_data.get("get_site1_task_details"),
                self.test_data.get("get_site1_task_progress"),
                self.test_data.get("response_for_profile_creation"),
                self.test_data.get("get_task_details_response"),
                self.test_data.get("get_task_progress")
            ]
        elif "profile_deletion" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("verify_wireless_profile_list"),
                self.test_data.get("verify_profile_details_basic"),
                self.test_data.get("get_site_list_for_profile_basic"),
                self.test_data.get("assign_site1_response"),
                self.test_data.get("get_site1_task_details"),
                self.test_data.get("get_site1_task_progress"),
                self.test_data.get("response_for_profile_creation"),
                self.test_data.get("get_task_details_response"),
                self.test_data.get("get_task_progress"),
                self.test_data.get("get_sites4")
            ]
        elif "profile_creation_fail_feature_template" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("get_network_profile_sites"),
                self.test_data.get("get_Sites"),
                self.test_data.get("no_response_received"),
                self.test_data.get("get_sites2"),
                self.test_data.get("get_enterprise_ssid"),
                self.test_data.get("get_feature_template_summary"),
                self.test_data.get("get_feature_template_summary1")
            ]

    def test_network_profile_workflow_manager_basic_profile_creation(self):
        """
        Test case for wireless profile workfollow manager create profile with basic information.

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
                dnac_version="3.1.3.0",
                config_verify=False,
                config=self.basic_profile_creation_config
            )
        )

        result = self.execute_module(changed=True, failed=False)
        self.maxDiff = None
        self.assertIn(
            "Wireless profile(s) created/updated and verified successfully",
            result.get('msg')
        )

    def test_network_profile_workflow_manager_profile_details_deletion(self):
        """
        Test case for wireless profile workfollow manager remove profile information.

        This test case checks the behavior of the wireless profile workflow when removal
        in the specified Cisco Catalyst Center.
        """
        set_module_args(
            dict(
                dnac_host="1.1.1.1",
                dnac_username="dummy",
                dnac_password="dummy",
                dnac_log=True,
                state="deleted",
                dnac_version="3.1.3.0",
                config_verify=True,
                config=self.basic_profile_creation_config
            )
        )

        result = self.execute_module(changed=True, failed=False)
        self.maxDiff = None
        self.assertIn(
            "Wireless profile data removed successfully",
            result.get('msg')
        )

    def test_network_profile_workflow_manager_profile_deletion(self):
        """
        Test case for wireless profile workfollow manager remove profile.

        This test case checks the behavior of the wireless profile workflow when removal
        in the specified Cisco Catalyst Center.
        """
        set_module_args(
            dict(
                dnac_host="1.1.1.1",
                dnac_username="dummy",
                dnac_password="dummy",
                dnac_log=True,
                state="deleted",
                dnac_version="3.1.3.0",
                config_verify=True,
                config=self.profile_deletion
            )
        )

        result = self.execute_module(changed=True, failed=False)
        self.maxDiff = None
        self.assertIn(
            "Wireless profile(s) deleted and verified successfully",
            result.get('msg')
        )

    def test_network_profile_workflow_manager_profile_creation_fail_feature_template(self):
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
                config=self.profile_creation_config_feature_template
            )
        )

        result = self.execute_module(changed=False, failed=True)
        self.maxDiff = None
        self.assertIn(
            "Invalid parameters in playbook config:",
            result.get('response')
        )
