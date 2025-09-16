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
    profile_creation_config = test_data.get("profile_creation_config")
    profile_creation_config_feature_template = test_data.get("profile_creation_config_feature_template")
    playbook_new_feature_template = test_data.get("playbook_new_feature_template")

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
        if "profile_creation_fail" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("wireless_profile_list"),
                self.test_data.get("available_templates"),
                self.test_data.get("get_site_details_mdu"),
                self.test_data.get("get_site_details_mdu_child"),
                self.test_data.get("get_site_details_global"),
                self.test_data.get("get_ssids_for_global"),
                self.test_data.get("get_additional_interface1"),
                self.test_data.get("get_dot11be_profile"),
                self.test_data.get("response_for_profile_creation"),
                self.test_data.get("get_task_details_response"),
                self.test_data.get("get_task_progress"),
                self.test_data.get("assign_site1_response"),
                self.test_data.get("get_site1_task_details"),
                self.test_data.get("get_site1_task_progress"),
                self.test_data.get("assign_site1_response"),
                self.test_data.get("get_site1_task_details"),
                self.test_data.get("get_site1_task_progress"),
                self.test_data.get("assign_site1_response"),
                self.test_data.get("get_site1_task_details"),
                self.test_data.get("get_site1_task_progress"),
                self.test_data.get("assign_template1_response"),
                self.test_data.get("get_template1_task_details"),
                self.test_data.get("verify_wireless_profile_list"),
                self.test_data.get("get_wireless_profile_details"),
                self.test_data.get("available_templates"),
                self.test_data.get("get_site_details_mdu"),
                self.test_data.get("get_site_details_mdu_child"),
                self.test_data.get("get_site_details_global"),
                self.test_data.get("get_ssids_for_global"),
                self.test_data.get("get_additional_interface1"),
                self.test_data.get("get_cli_template_for_profile"),
                self.test_data.get("get_site_list_for_profile"),
                self.test_data.get("get_dot11be_profile")
            ]

        if "profile_creation_feature_template" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("get_network_profile_sites"),
                self.test_data.get("get_Sites"),
                self.test_data.get("no_response_received"),
                self.test_data.get("get_sites2"),
                self.test_data.get("get_enterprise_ssid"),
                self.test_data.get("get_feature_template_summary"),
                self.test_data.get("get_feature_template_summary1"),
                self.test_data.get("get80211be_profiles"),
                self.test_data.get("create_wireless_profile_connectivity"),
                self.test_data.get("get_task_id1"),
                self.test_data.get("get_task_details_by_id"),
                self.test_data.get("retrieves_the_list_of_network_profiles_for_sites"),
                self.test_data.get("get_wireless_profiles_v1"),
                self.test_data.get("get_Sites"),
                self.test_data.get("get_sites1"),
                self.test_data.get("get_sites2"),
                self.test_data.get("get_enterprise_ssid"),
                self.test_data.get("get_feature_template_summary"),
                self.test_data.get("get_feature_template_summary1"),
                self.test_data.get("get_site_lists_for_profile"),
                self.test_data.get("get80211be_profiles")
            ]

        if "profile_creation_fail_feature_template" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("get_network_profile_sites"),
                self.test_data.get("get_Sites"),
                self.test_data.get("no_response_received"),
                self.test_data.get("get_sites2"),
                self.test_data.get("get_enterprise_ssid"),
                self.test_data.get("get_feature_template_summary"),
                self.test_data.get("get_feature_template_summary1")
            ]

        if "profile_creation_feature_template_new" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("retrieves_the_list_of_network_profiles_for_sites"),
                self.test_data.get("get_wireless_profiles_v1"),
                self.test_data.get("get_site_lists_for_profile"),
                self.test_data.get("retrieves_the_list_of_network_profiles_for_sites1"),
                self.test_data.get("gets_the_templates_available"),
                self.test_data.get("get_sites21"),
                self.test_data.get("get_sites11"),
                self.test_data.get("get_sites12"),
                self.test_data.get("get_enterprise_ssid1"),
                self.test_data.get("get_interfaces"),
                self.test_data.get("get_feature_template_summary11"),
                self.test_data.get("get_dot11be_profile1"),
                self.test_data.get("configuration_templates"),
                self.test_data.get("configuration_templates_id"),
                self.test_data.get("dn_template1"),
                self.test_data.get("retrieves_the_list_of_network_profiles_for_sites11"),
                self.test_data.get("get_wireless_profile"),
                self.test_data.get("gets_the_templates_available1"),
                self.test_data.get("get_sites3"),
                self.test_data.get("get_sites4"),
                self.test_data.get("get_sites5"),
                self.test_data.get("get_enterprise_ssid"),
                self.test_data.get("get_interfaces2"),
                self.test_data.get("get_feature_template_summary111"),
                self.test_data.get("retrieve_cli_templates_attached_to_a_network_profile"),
                self.test_data.get("retrieves_the_list_of_sites_that_the_given_network_profile_for_sites_is_assigned_to"),
                self.test_data.get("get80211be_profiles1")


            ]

    def test_network_profile_workflow_manager_profile_creation_fail(self):
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
                dnac_version="3.1.3.0",
                config_verify=True,
                config=self.profile_creation_config
            )
        )

        result = self.execute_module(changed=False, failed=True)
        self.maxDiff = None
        self.assertIn(
            "Unable to create wireless profile",
            result.get('msg')
        )

    def test_network_profile_workflow_manager_profile_creation_feature_template(self):
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
                dnac_version="3.1.3.0",
                config_verify=True,
                config=self.profile_creation_config_feature_template
            )
        )

        result = self.execute_module(changed=False, failed=True)
        self.maxDiff = None
        self.assertIn(
            "Unable to create wireless profile",
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

    def test_network_profile_workflow_manager_profile_creation_feature_template_new(self):
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
                dnac_version="3.1.3.0",
                config_verify=True,
                config=self.playbook_new_feature_template
            )
        )

        result = self.execute_module(changed=False, failed=True)
        self.maxDiff = None
        self.assertIn(
            "An exception occurred while retrieving Site details",
            result.get('response')
        )
