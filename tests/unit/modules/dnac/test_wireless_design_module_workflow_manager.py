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
from ansible_collections.cisco.dnac.plugins.modules import wireless_design_workflow_manager
from .dnac_module import TestDnacModule, set_module_args, loadPlaybookData


class TestWirelessDesign(TestDnacModule):
    module = wireless_design_workflow_manager
    test_data = loadPlaybookData("wireless_design_workflow_manager_intent")
    # playbooks for wireless_design_workflow_manager enhancements (feature_template)
    playbook_aaa_radius_attribute = test_data.get("playbook_aaa_radius_attribute")
    playbook_aaa_radius_attribute_update = test_data.get("playbook_aaa_radius_attribute_update")
    playbook_aaa_radius_attribute_delete = test_data.get("playbook_aaa_radius_attribute_delete")

    playbook_advanced_ssid_create = test_data.get("playbook_advanced_ssid_create")
    playbook_advanced_ssid_update = test_data.get("playbook_advanced_ssid_update")
    playbook_advanced_ssid_delete = test_data.get("playbook_advanced_ssid_delete")

    playbook_clean_air_create = test_data.get("playbook_clean_air_create")
    playbook_clean_air_update = test_data.get("playbook_clean_air_update")
    playbook_clean_air_delete = test_data.get("playbook_clean_air_delete")

    playbook_dot11ax_add = test_data.get("playbook_dot11ax_add")
    playbook_dot11ax_update = test_data.get("playbook_dot11ax_update")
    playbook_dot11ax_delete = test_data.get("playbook_dot11ax_delete")

    playbook_dot11be_add = test_data.get("playbook_dot11be_add")
    playbook_dot11be_update = test_data.get("playbook_dot11be_update")
    playbook_dot11be_delete = test_data.get("playbook_dot11be_delete")

    playbook_flexconnect_add = test_data.get("playbook_flexconnect_add")
    playbook_flexconnect_update = test_data.get("playbook_flexconnect_update")
    playbook_flexconnect_delete = test_data.get("playbook_flexconnect_delete")

    playbook_multicast_add = test_data.get("playbook_multicast_add")
    playbook_multicast_update = test_data.get("playbook_multicast_update")
    playbook_multicast_delete = test_data.get("playbook_multicast_delete")

    playbook_rrm_general_add = test_data.get("playbook_rrm_general_add")
    playbook_rrm_general_update = test_data.get("playbook_rrm_general_update")
    playbook_rrm_general_delete = test_data.get("playbook_rrm_general_delete")

    playbook_rrm_fra_add = test_data.get("playbook_rrm_fra_add")
    playbook_rrm_fra_update = test_data.get("playbook_rrm_fra_update")
    playbook_rrm_fra_delete = test_data.get("playbook_rrm_fra_delete")

    playbook_event_driven_rrm_add = test_data.get("playbook_event_driven_rrm_add")
    playbook_event_driven_rrm_update = test_data.get("playbook_event_driven_rrm_update")
    playbook_event_driven_rrm_delete = test_data.get("playbook_event_driven_rrm_delete")

    def setUp(self):
        super(TestWirelessDesign, self).setUp()

        self.mock_dnac_init = patch(
            "ansible_collections.cisco.dnac.plugins.module_utils.dnac.DNACSDK.__init__"
        )
        self.run_dnac_init = self.mock_dnac_init.start()
        self.run_dnac_init.side_effect = [None]
        self.mock_dnac_exec = patch(
            "ansible_collections.cisco.dnac.plugins.module_utils.dnac.DNACSDK._exec"
        )
        self.run_dnac_exec = self.mock_dnac_exec.start()
        self.load_fixtures()

        print(f"Mock for DNACSDK._exec: {self.run_dnac_exec}")

    def tearDown(self):
        super(TestWirelessDesign, self).tearDown()
        self.mock_dnac_init.stop()
        self.mock_dnac_exec.stop()

    def load_fixtures(self, response=None, device=""):
        print("Inside load_fixtures")
        # FIXTURE FOR SUCCESS TESTCASES ############################################################

        if "create_ssid" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("respone_get_sites_success"),
                self.test_data.get("response_get_ssid_by_site_iteration_1_success"),
                self.test_data.get("response_get_task_id_success"),
                self.test_data.get("response_get_task_status_by_id_success"),
                self.test_data.get("response_get_task_id_success"),
                self.test_data.get("response_get_task_status_by_id_success"),
                self.test_data.get("response_get_task_id_success"),
                self.test_data.get("response_get_task_status_by_id_success"),
                self.test_data.get("response_get_task_id_success"),
                self.test_data.get("response_get_task_status_by_id_success"),
                self.test_data.get("response_get_task_id_success"),
                self.test_data.get("response_get_task_status_by_id_success"),
                self.test_data.get("response_get_task_id_success"),
                self.test_data.get("response_get_task_status_by_id_success"),
                self.test_data.get("response_get_task_id_success"),
                self.test_data.get("response_get_task_status_by_id_success"),
                self.test_data.get("response_get_task_id_success"),
                self.test_data.get("response_get_task_status_by_id_success"),
                self.test_data.get("response_get_task_id_success"),
                self.test_data.get("response_get_task_status_by_id_success"),
                self.test_data.get("response_get_task_id_success"),
                self.test_data.get("response_get_task_status_by_id_success"),
                self.test_data.get("respone_get_sites_success"),
                self.test_data.get("response_get_ssids_post_creation_success"),
            ]

        if "update_ssid" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("respone_get_sites_success"),
                self.test_data.get("response_get_ssid_by_site_update_iteration_1_success"),
                self.test_data.get("response_get_sites_2_success"),
                self.test_data.get("response_get_ssid_by_site_empty_success"),
                self.test_data.get("response_get_task_id_success"),
                self.test_data.get("response_get_task_status_by_id_success"),
                self.test_data.get("response_get_task_id_success"),
                self.test_data.get("response_get_task_status_by_id_success"),
                self.test_data.get("response_get_task_id_success"),
                self.test_data.get("response_get_task_status_by_id_success"),
                self.test_data.get("respone_get_sites_success"),
                self.test_data.get("response_get_ssids_post_update_success"),
                self.test_data.get("response_get_sites_2_success"),
                self.test_data.get("response_get_ssids_post_update_success"),
            ]

        if "delete_ssid" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("respone_get_sites_success"),
                self.test_data.get("response_get_ssid_by_site_delete_iteration_1_success"),
                self.test_data.get("response_get_task_id_success"),
                self.test_data.get("response_get_task_status_by_id_success"),
                self.test_data.get("response_get_task_id_success"),
                self.test_data.get("response_get_task_status_by_id_success"),
                self.test_data.get("response_get_task_id_success"),
                self.test_data.get("response_get_task_status_by_id_success"),
                self.test_data.get("response_get_task_id_success"),
                self.test_data.get("response_get_task_status_by_id_success"),
                self.test_data.get("response_get_task_id_success"),
                self.test_data.get("response_get_task_status_by_id_success"),
                self.test_data.get("response_get_task_id_success"),
                self.test_data.get("response_get_task_status_by_id_success"),
                self.test_data.get("response_get_task_id_success"),
                self.test_data.get("response_get_task_status_by_id_success"),
                self.test_data.get("response_get_task_id_success"),
                self.test_data.get("response_get_task_status_by_id_success"),
                self.test_data.get("response_get_task_id_success"),
                self.test_data.get("response_get_task_status_by_id_success"),
                self.test_data.get("response_get_task_id_success"),
                self.test_data.get("response_get_task_status_by_id_success"),
                self.test_data.get("response_get_ssids_post_delete_success"),
            ]

        if "create_interfaces" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("response_get_interfaces_1_success"),
                self.test_data.get("response_get_task_id_success"),
                self.test_data.get("response_get_task_status_by_id_success"),
                self.test_data.get("response_get_task_id_success"),
                self.test_data.get("response_get_task_status_by_id_success"),
                self.test_data.get("response_get_task_id_success"),
                self.test_data.get("response_get_task_status_by_id_success"),
                self.test_data.get("response_get_task_id_success"),
                self.test_data.get("response_get_task_status_by_id_success"),
                self.test_data.get("response_get_task_id_success"),
                self.test_data.get("response_get_task_status_by_id_success"),
                self.test_data.get("response_get_task_id_success"),
                self.test_data.get("response_get_task_status_by_id_success"),
                self.test_data.get("response_get_interfaces_post_create_success"),
            ]

        if "update_interfaces" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("response_get_interfaces_2_success"),
                self.test_data.get("response_get_task_id_success"),
                self.test_data.get("response_get_task_status_by_id_success"),
                self.test_data.get("response_get_task_id_success"),
                self.test_data.get("response_get_task_status_by_id_success"),
                self.test_data.get("response_get_task_id_success"),
                self.test_data.get("response_get_task_status_by_id_success"),
                self.test_data.get("response_get_task_id_success"),
                self.test_data.get("response_get_task_status_by_id_success"),
                self.test_data.get("response_get_interfaces_2_post_update_success"),
            ]

        if "delete_interfaces" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("response_get_interfaces_3_success"),
                self.test_data.get("response_get_task_id_success"),
                self.test_data.get("response_get_task_status_by_id_success"),
                self.test_data.get("response_get_task_id_success"),
                self.test_data.get("response_get_task_status_by_id_success"),
                self.test_data.get("response_get_task_id_success"),
                self.test_data.get("response_get_task_status_by_id_success"),
                self.test_data.get("response_get_task_id_success"),
                self.test_data.get("response_get_task_status_by_id_success"),
                self.test_data.get("response_get_task_id_success"),
                self.test_data.get("response_get_task_status_by_id_success"),
                self.test_data.get("response_get_task_id_success"),
                self.test_data.get("response_get_task_status_by_id_success"),
                self.test_data.get("response_get_interfaces_3_post_delete_success"),
            ]

        if "add_power_profiles" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("response_get_power_profiles_1_success"),
                self.test_data.get("response_get_task_id_success"),
                self.test_data.get("response_get_task_status_by_id_success"),
                self.test_data.get("response_get_task_id_success"),
                self.test_data.get("response_get_task_status_by_id_success"),
                self.test_data.get("response_get_task_id_success"),
                self.test_data.get("response_get_task_status_by_id_success"),
                self.test_data.get("response_get_task_id_success"),
                self.test_data.get("response_get_task_status_by_id_success"),
                self.test_data.get("response_get_task_id_success"),
                self.test_data.get("response_get_task_status_by_id_success"),
                self.test_data.get("response_get_task_id_success"),
                self.test_data.get("response_get_task_status_by_id_success"),
                self.test_data.get("response_get_power_profiles_1_post_create_success"),
            ]

        if "update_power_profiles" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("response_get_power_profiles_2_success"),
                self.test_data.get("response_get_task_id_success"),
                self.test_data.get("response_get_task_status_by_id_success"),
                self.test_data.get("response_get_task_id_success"),
                self.test_data.get("response_get_task_status_by_id_success"),
                self.test_data.get("response_get_task_id_success"),
                self.test_data.get("response_get_task_status_by_id_success"),
                self.test_data.get("response_get_task_id_success"),
                self.test_data.get("response_get_task_status_by_id_success"),
                self.test_data.get("response_get_task_id_success"),
                self.test_data.get("response_get_task_status_by_id_success"),
                self.test_data.get("response_get_task_id_success"),
                self.test_data.get("response_get_task_status_by_id_success"),
                self.test_data.get("response_get_task_id_success"),
                self.test_data.get("response_get_task_status_by_id_success"),
                self.test_data.get("response_get_power_profiles_2_post_update_success"),
            ]

        if "delete_power_profiles" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("response_get_power_profiles_3_success"),
                self.test_data.get("response_get_task_id_success"),
                self.test_data.get("response_get_task_status_by_id_success"),
                self.test_data.get("response_get_task_id_success"),
                self.test_data.get("response_get_task_status_by_id_success"),
                self.test_data.get("response_get_task_id_success"),
                self.test_data.get("response_get_task_status_by_id_success"),
                self.test_data.get("response_get_task_id_success"),
                self.test_data.get("response_get_task_status_by_id_success"),
                self.test_data.get("response_get_task_id_success"),
                self.test_data.get("response_get_task_status_by_id_success"),
                self.test_data.get("response_get_task_id_success"),
                self.test_data.get("response_get_task_status_by_id_success"),
                self.test_data.get("response_get_power_profiles_3_post_delete_success"),
            ]

        if "create_ap_profiles" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("response_get_ap_profiles_1_success"),
                self.test_data.get("response_get_task_id_success"),
                self.test_data.get("response_get_task_status_by_id_success"),
                self.test_data.get("response_get_task_id_success"),
                self.test_data.get("response_get_task_status_by_id_success"),
                self.test_data.get("response_get_task_id_success"),
                self.test_data.get("response_get_task_status_by_id_success"),
                self.test_data.get("response_get_task_id_success"),
                self.test_data.get("response_get_task_status_by_id_success"),
                self.test_data.get("response_get_task_id_success"),
                self.test_data.get("response_get_task_status_by_id_success"),
                self.test_data.get("response_get_task_id_success"),
                self.test_data.get("response_get_task_status_by_id_success"),
                self.test_data.get("response_get_task_id_success"),
                self.test_data.get("response_get_task_status_by_id_success"),
                self.test_data.get("response_get_task_id_success"),
                self.test_data.get("response_get_task_status_by_id_success"),
                self.test_data.get("response_get_task_id_success"),
                self.test_data.get("response_get_task_status_by_id_success"),
                self.test_data.get("response_get_task_id_success"),
                self.test_data.get("response_get_task_status_by_id_success"),
                self.test_data.get("response_get_task_id_success"),
                self.test_data.get("response_get_task_status_by_id_success"),
                self.test_data.get("response_get_task_id_success"),
                self.test_data.get("response_get_task_status_by_id_success"),
                self.test_data.get("response_get_task_id_success"),
                self.test_data.get("response_get_task_status_by_id_success"),
                self.test_data.get("response_get_task_id_success"),
                self.test_data.get("response_get_task_status_by_id_success"),
                self.test_data.get("response_get_task_id_success"),
                self.test_data.get("response_get_task_status_by_id_success"),
                self.test_data.get("response_get_task_id_success"),
                self.test_data.get("response_get_task_status_by_id_success"),
                self.test_data.get("response_get_task_id_success"),
                self.test_data.get("response_get_task_status_by_id_success"),
                self.test_data.get("response_get_task_id_success"),
                self.test_data.get("response_get_task_status_by_id_success"),
                self.test_data.get("response_get_task_id_success"),
                self.test_data.get("response_get_task_status_by_id_success"),
                self.test_data.get("response_get_task_id_success"),
                self.test_data.get("response_get_task_status_by_id_success"),
                self.test_data.get("response_get_task_id_success"),
                self.test_data.get("response_get_task_status_by_id_success"),
                self.test_data.get("response_get_task_id_success"),
                self.test_data.get("response_get_task_status_by_id_success"),
                self.test_data.get("response_get_task_id_success"),
                self.test_data.get("response_get_task_status_by_id_success"),
                self.test_data.get("response_get_task_id_success"),
                self.test_data.get("response_get_task_status_by_id_success"),
                self.test_data.get("response_get_task_id_success"),
                self.test_data.get("response_get_task_status_by_id_success"),
                self.test_data.get("response_get_task_id_success"),
                self.test_data.get("response_get_task_status_by_id_success"),
                self.test_data.get("response_get_task_id_success"),
                self.test_data.get("response_get_task_status_by_id_success"),
                self.test_data.get("response_get_task_id_success"),
                self.test_data.get("response_get_task_status_by_id_success"),
                self.test_data.get("response_get_task_id_success"),
                self.test_data.get("response_get_task_status_by_id_success"),
                self.test_data.get("response_get_task_id_success"),
                self.test_data.get("response_get_task_status_by_id_success"),
                self.test_data.get("response_get_task_id_success"),
                self.test_data.get("response_get_task_status_by_id_success"),
                self.test_data.get("response_get_task_id_success"),
                self.test_data.get("response_get_task_status_by_id_success"),
                self.test_data.get("response_get_task_id_success"),
                self.test_data.get("response_get_task_status_by_id_success"),
                self.test_data.get("response_get_ap_profiles_1_post_create_success"),
            ]

        if "update_ap_profiles" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("response_get_ap_profiles_2_success"),
                self.test_data.get("response_get_task_id_success"),
                self.test_data.get("response_get_task_status_by_id_success"),
                self.test_data.get("response_get_task_id_success"),
                self.test_data.get("response_get_task_status_by_id_success"),
                self.test_data.get("response_get_task_id_success"),
                self.test_data.get("response_get_task_status_by_id_success"),
                self.test_data.get("response_get_task_id_success"),
                self.test_data.get("response_get_task_status_by_id_success"),
                self.test_data.get("response_get_task_id_success"),
                self.test_data.get("response_get_task_status_by_id_success"),
                self.test_data.get("response_get_task_id_success"),
                self.test_data.get("response_get_task_status_by_id_success"),
                self.test_data.get("response_get_task_id_success"),
                self.test_data.get("response_get_task_status_by_id_success"),
                self.test_data.get("response_get_ap_profiles_2_post_update_success"),
            ]

        if "delete_ap_profiles" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("response_get_ap_profiles_3_success"),
                self.test_data.get("response_get_task_id_success"),
                self.test_data.get("response_get_task_status_by_id_success"),
                self.test_data.get("response_get_task_id_success"),
                self.test_data.get("response_get_task_status_by_id_success"),
                self.test_data.get("response_get_task_id_success"),
                self.test_data.get("response_get_task_status_by_id_success"),
                self.test_data.get("response_get_task_id_success"),
                self.test_data.get("response_get_task_status_by_id_success"),
                self.test_data.get("response_get_task_id_success"),
                self.test_data.get("response_get_task_status_by_id_success"),
                self.test_data.get("response_get_task_id_success"),
                self.test_data.get("response_get_task_status_by_id_success"),
                self.test_data.get("response_get_task_id_success"),
                self.test_data.get("response_get_task_status_by_id_success"),
                self.test_data.get("response_get_task_id_success"),
                self.test_data.get("response_get_task_status_by_id_success"),
                self.test_data.get("response_get_task_id_success"),
                self.test_data.get("response_get_task_status_by_id_success"),
                self.test_data.get("response_get_task_id_success"),
                self.test_data.get("response_get_task_status_by_id_success"),
                self.test_data.get("response_get_task_id_success"),
                self.test_data.get("response_get_task_status_by_id_success"),
                self.test_data.get("response_get_task_id_success"),
                self.test_data.get("response_get_task_status_by_id_success"),
                self.test_data.get("response_get_task_id_success"),
                self.test_data.get("response_get_task_status_by_id_success"),
                self.test_data.get("response_get_task_id_success"),
                self.test_data.get("response_get_task_status_by_id_success"),
                self.test_data.get("response_get_task_id_success"),
                self.test_data.get("response_get_task_status_by_id_success"),
                self.test_data.get("response_get_task_id_success"),
                self.test_data.get("response_get_task_status_by_id_success"),
                self.test_data.get("response_get_task_id_success"),
                self.test_data.get("response_get_task_status_by_id_success"),
                self.test_data.get("response_get_task_id_success"),
                self.test_data.get("response_get_task_status_by_id_success"),
                self.test_data.get("response_get_task_id_success"),
                self.test_data.get("response_get_task_status_by_id_success"),
                self.test_data.get("response_get_task_id_success"),
                self.test_data.get("response_get_task_status_by_id_success"),
                self.test_data.get("response_get_task_id_success"),
                self.test_data.get("response_get_task_status_by_id_success"),
                self.test_data.get("response_get_task_id_success"),
                self.test_data.get("response_get_task_status_by_id_success"),
                self.test_data.get("response_get_task_id_success"),
                self.test_data.get("response_get_task_status_by_id_success"),
                self.test_data.get("response_get_task_id_success"),
                self.test_data.get("response_get_task_status_by_id_success"),
                self.test_data.get("response_get_task_id_success"),
                self.test_data.get("response_get_task_status_by_id_success"),
                self.test_data.get("response_get_task_id_success"),
                self.test_data.get("response_get_task_status_by_id_success"),
                self.test_data.get("response_get_task_id_success"),
                self.test_data.get("response_get_task_status_by_id_success"),
                self.test_data.get("response_get_task_id_success"),
                self.test_data.get("response_get_task_status_by_id_success"),
                self.test_data.get("response_get_task_id_success"),
                self.test_data.get("response_get_task_status_by_id_success"),
                self.test_data.get("response_get_task_id_success"),
                self.test_data.get("response_get_task_status_by_id_success"),
                self.test_data.get("response_get_task_id_success"),
                self.test_data.get("response_get_task_status_by_id_success"),
                self.test_data.get("response_get_task_id_success"),
                self.test_data.get("response_get_task_status_by_id_success"),
                self.test_data.get("response_get_task_id_success"),
                self.test_data.get("response_get_task_status_by_id_success"),
                self.test_data.get("response_get_ap_profiles_3_post_delete_success"),
            ]

        if "create_rf_profiles" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("response_get_rf_profiles_1_success"),
                self.test_data.get("response_get_task_id_success"),
                self.test_data.get("response_get_task_status_by_id_success"),
                self.test_data.get("response_get_task_id_success"),
                self.test_data.get("response_get_task_status_by_id_success"),
                self.test_data.get("response_get_task_id_success"),
                self.test_data.get("response_get_task_status_by_id_success"),
                self.test_data.get("response_get_task_id_success"),
                self.test_data.get("response_get_task_status_by_id_success"),
                self.test_data.get("response_get_task_id_success"),
                self.test_data.get("response_get_task_status_by_id_success"),
                self.test_data.get("response_get_task_id_success"),
                self.test_data.get("response_get_task_status_by_id_success"),
                self.test_data.get("response_get_task_id_success"),
                self.test_data.get("response_get_task_status_by_id_success"),
                self.test_data.get("response_get_task_id_success"),
                self.test_data.get("response_get_task_status_by_id_success"),
                self.test_data.get("response_get_task_id_success"),
                self.test_data.get("response_get_task_status_by_id_success"),
                self.test_data.get("response_get_task_id_success"),
                self.test_data.get("response_get_task_status_by_id_success"),
                self.test_data.get("response_get_task_id_success"),
                self.test_data.get("response_get_task_status_by_id_success"),
                self.test_data.get("response_get_task_id_success"),
                self.test_data.get("response_get_task_status_by_id_success"),
                self.test_data.get("response_get_task_id_success"),
                self.test_data.get("response_get_task_status_by_id_success"),
                self.test_data.get("response_get_task_id_success"),
                self.test_data.get("response_get_task_status_by_id_success"),
                self.test_data.get("response_get_task_id_success"),
                self.test_data.get("response_get_task_status_by_id_success"),
                self.test_data.get("response_get_task_id_success"),
                self.test_data.get("response_get_task_status_by_id_success"),
                self.test_data.get("response_get_task_id_success"),
                self.test_data.get("response_get_task_status_by_id_success"),
                self.test_data.get("response_get_rf_profiles_1_post_create_success"),
            ]

        if "update_rf_profiles" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("response_get_rf_profiles_2_success"),
                self.test_data.get("response_get_task_id_success"),
                self.test_data.get("response_get_task_status_by_id_success"),
                self.test_data.get("response_get_task_id_success"),
                self.test_data.get("response_get_task_status_by_id_success"),
                self.test_data.get("response_get_task_id_success"),
                self.test_data.get("response_get_task_status_by_id_success"),
                self.test_data.get("response_get_task_id_success"),
                self.test_data.get("response_get_task_status_by_id_success"),
                self.test_data.get("response_get_task_id_success"),
                self.test_data.get("response_get_task_status_by_id_success"),
                self.test_data.get("response_get_task_id_success"),
                self.test_data.get("response_get_task_status_by_id_success"),
                self.test_data.get("response_get_task_id_success"),
                self.test_data.get("response_get_task_status_by_id_success"),
                self.test_data.get("response_get_task_id_success"),
                self.test_data.get("response_get_task_status_by_id_success"),
                self.test_data.get("response_get_task_id_success"),
                self.test_data.get("response_get_task_status_by_id_success"),
                self.test_data.get("response_get_task_id_success"),
                self.test_data.get("response_get_task_status_by_id_success"),
                self.test_data.get("response_get_task_id_success"),
                self.test_data.get("response_get_task_status_by_id_success"),
                self.test_data.get("response_get_task_id_success"),
                self.test_data.get("response_get_task_status_by_id_success"),
                self.test_data.get("response_get_task_id_success"),
                self.test_data.get("response_get_task_status_by_id_success"),
                self.test_data.get("response_get_task_id_success"),
                self.test_data.get("response_get_task_status_by_id_success"),
                self.test_data.get("response_get_task_id_success"),
                self.test_data.get("response_get_task_status_by_id_success"),
                self.test_data.get("response_get_rf_profiles_2_post_update_success"),
            ]

        if "delete_rf_profiles" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("response_get_rf_profiles_3_success"),
                self.test_data.get("response_get_task_id_success"),
                self.test_data.get("response_get_task_status_by_id_success"),
                self.test_data.get("response_get_task_id_success"),
                self.test_data.get("response_get_task_status_by_id_success"),
                self.test_data.get("response_get_task_id_success"),
                self.test_data.get("response_get_task_status_by_id_success"),
                self.test_data.get("response_get_task_id_success"),
                self.test_data.get("response_get_task_status_by_id_success"),
                self.test_data.get("response_get_task_id_success"),
                self.test_data.get("response_get_task_status_by_id_success"),
                self.test_data.get("response_get_task_id_success"),
                self.test_data.get("response_get_task_status_by_id_success"),
                self.test_data.get("response_get_task_id_success"),
                self.test_data.get("response_get_task_status_by_id_success"),
                self.test_data.get("response_get_task_id_success"),
                self.test_data.get("response_get_task_status_by_id_success"),
                self.test_data.get("response_get_task_id_success"),
                self.test_data.get("response_get_task_status_by_id_success"),
                self.test_data.get("response_get_task_id_success"),
                self.test_data.get("response_get_task_status_by_id_success"),
                self.test_data.get("response_get_task_id_success"),
                self.test_data.get("response_get_task_status_by_id_success"),
                self.test_data.get("response_get_task_id_success"),
                self.test_data.get("response_get_task_status_by_id_success"),
                self.test_data.get("response_get_task_id_success"),
                self.test_data.get("response_get_task_status_by_id_success"),
                self.test_data.get("response_get_task_id_success"),
                self.test_data.get("response_get_task_status_by_id_success"),
                self.test_data.get("response_get_task_id_success"),
                self.test_data.get("response_get_task_status_by_id_success"),
                self.test_data.get("response_get_task_id_success"),
                self.test_data.get("response_get_task_status_by_id_success"),
                self.test_data.get("response_get_task_id_success"),
                self.test_data.get("response_get_task_status_by_id_success"),
                self.test_data.get("response_get_rf_profiles_3_post_delete_success"),
            ]

        if "create_anchor_groups" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("response_get_anchor_groups_1_success"),
                self.test_data.get("response_get_task_id_success"),
                self.test_data.get("response_get_task_status_by_id_success"),
                self.test_data.get("response_get_task_id_success"),
                self.test_data.get("response_get_task_status_by_id_success"),
                self.test_data.get("response_get_task_id_success"),
                self.test_data.get("response_get_task_status_by_id_success"),
                self.test_data.get("response_get_anchor_groups_1_post_create_success"),
            ]

        if "update_anchor_groups" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("response_get_anchor_groups_2_success"),
                self.test_data.get("response_get_task_id_success"),
                self.test_data.get("response_get_task_status_by_id_success"),
                self.test_data.get("response_get_task_id_success"),
                self.test_data.get("response_get_task_status_by_id_success"),
                self.test_data.get("response_get_task_id_success"),
                self.test_data.get("response_get_task_status_by_id_success"),
                self.test_data.get("response_get_anchor_groups_2_post_update_success"),
            ]

        if "delete_anchor_groups" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("response_get_anchor_groups_3_success"),
                self.test_data.get("response_get_task_id_success"),
                self.test_data.get("response_get_task_status_by_id_success"),
                self.test_data.get("response_get_task_id_success"),
                self.test_data.get("response_get_task_status_by_id_success"),
                self.test_data.get("response_get_task_id_success"),
                self.test_data.get("response_get_task_status_by_id_success"),
                self.test_data.get("response_get_anchor_groups_3_post_delete_success"),
            ]

        if "playbook_aaa_radius_attribute" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("Get_AAA_RADIUS_ATTRIBUTES_CONFIGURATION"),
                self.test_data.get("Create_AAA_Radius_Attribute"),
                self.test_data.get("task_019a0599-07b7-7f20-a2e2-cffc4eccb372"),
            ]

        if "playbook_aaa_radius_attribute_update" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("Get_AAA_RADIUS_ATTRIBUTES_CONFIGURATION_update"),
                self.test_data.get("Update_AAA_Radius_Attribute"),
                self.test_data.get("Update_AAA_Radius_Attribute_"),
                self.test_data.get("task_019a05af-03ca-78c2-afde-264247f40bad"),
            ]

        if "playbook_aaa_radius_attribute_delete" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("Get_AAA_RADIUS_ATTRIBUTES_CONFIGURATION_delete"),
                self.test_data.get("delete_AAA_RADIUS_ATTRIBUTES_CONFIGURATION"),
                self.test_data.get("task_019a05c6-1eee-7459-9ac8-d09c60c33845"),
            ]

        if "playbook_advanced_ssid_create" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("ADVANCED_SSID_CONFIGURATION"),
                self.test_data.get("create_ADVANCED_SSID_CONFIGURATION"),
                self.test_data.get("task_019a05e4-e2cd-7fe9-895a-3a86eaae5514"),
            ]

        if "playbook_advanced_ssid_update" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("ADVANCED_SSID_CONFIGURATION_update"),
                self.test_data.get("ADVANCED_SSID_CONFIGURATION_update_"),
                self.test_data.get("update_ADVANCED_SSID_CONFIGURATION"),
                self.test_data.get("task_019a05ff-25bb-7464-aa52-ae50f9ea6e11"),
            ]
        if "playbook_advanced_ssid_delete" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("ADVANCED_SSID_CONFIGURATION_delete"),
                self.test_data.get("delete_ADVANCED_SSID_CONFIGURATION"),
                self.test_data.get("task_019a0616-094f-7d81-9d8c-2d371bf1daed"),
            ]

        if "playbook_clean_air_create" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("get_CLEANAIR_CONFIGURATION"),
                self.test_data.get("CLEANAIR_CONFIGURATION_create"),
                self.test_data.get("task_019a0b14-1380-7afc-a82e-a27c917eff36"),
            ]

        if "playbook_clean_air_update" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("CLEANAIR_CONFIGURATION_get_update"),
                self.test_data.get("CLEANAIR_CONFIGURATION_update_get"),
                self.test_data.get("CLEANAIR_CONFIGURATION_update"),
                self.test_data.get("task_019a0b1f-1e68-7d22-a6e5-4edb47eeb423"),
            ]

        if "playbook_clean_air_delete" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("CLEANAIR_CONFIGURATION_get_delete"),
                self.test_data.get("CLEANAIR_CONFIGURATION_delete_get"),
                self.test_data.get("task_019a0b25-4304-70f0-a684-889e06e10841"),
            ]

        if "playbook_dot11ax_add" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("DOT11AX_CONFIGURATION_get"),
                self.test_data.get("DOT11AX_CONFIGURATION_create"),
                self.test_data.get("task_019a0b40-98f2-7d60-b662-1fa7b0d18246"),
            ]

        if "playbook_dot11ax_update" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("DOT11AX_CONFIGURATION_get_update"),
                self.test_data.get("DOT11AX_CONFIGURATION_update_get"),
                self.test_data.get("DOT11AX_CONFIGURATION_update"),
                self.test_data.get("task_019a0b4b-4ddd-7717-95dc-d224a3dc0213"),
            ]
        if "playbook_dot11ax_delete" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("DOT11AX_CONFIGURATION_get_delete"),
                self.test_data.get("DOT11AX_CONFIGURATION_delete"),
                self.test_data.get("task_019a29a3-4d36-780a-b2bd-45e38d2ddb00"),
            ]

        if "playbook_dot11be_add" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("DOT11BE_CONFIGURATION_get"),
                self.test_data.get("DOT11BE_CONFIGURATION_create"),
                self.test_data.get("task_019a29c6-76c4-723b-adca-9c41a52bc23f"),
            ]
        if "playbook_dot11be_update" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("DOT11BE_CONFIGURATION_get_update"),
                self.test_data.get("DOT11BE_CONFIGURATION_update_get"),
                self.test_data.get("DOT11BE_CONFIGURATION_update"),
                self.test_data.get("task_019a29d7-6baf-78ad-906b-c42cbb62f5e8"),
            ]
        if "playbook_dot11be_delete" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("DOT11BE_CONFIGURATION_get_delete"),
                self.test_data.get("DOT11BE_CONFIGURATION_delete"),
                self.test_data.get("task_019a2e2c-389d-7d06-92f8-ca1006c0ea1e"),
            ]
        if "playbook_flexconnect_add" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("FLEXCONNECT_CONFIGURATION_get"),
                self.test_data.get("FLEXCONNECT_CONFIGURATION_create"),
                self.test_data.get("task_019a2e76-244a-7840-9640-76b56fa5e186"),
            ]
        if "playbook_flexconnect_update" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("FLEXCONNECT_CONFIGURATION_get_update"),
                self.test_data.get("FLEXCONNECT_CONFIGURATION_update_get"),
                self.test_data.get("FLEXCONNECT_CONFIGURATION_update"),
                self.test_data.get("task_019a2ebf-ece0-7a8e-9e9e-056c4468bb41"),
            ]
        if "playbook_flexconnect_delete" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("FLEXCONNECT_CONFIGURATION_get_delete"),
                self.test_data.get("FLEXCONNECT_CONFIGURATION_delete"),
                self.test_data.get("task_019a334d-5108-7a5d-8839-cf681a0ca9cb"),
            ]
        if "playbook_multicast_add" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("MULTICAST_CONFIGURATION_get"),
                self.test_data.get("MULTICAST_CONFIGURATION_create"),
                self.test_data.get("task_19a335f-4d3c-7e25-9dd6-e2bbbc617f97"),
            ]
        if "playbook_multicast_update" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("MULTICAST_CONFIGURATION_get_update"),
                self.test_data.get("MULTICAST_CONFIGURATION_update_get"),
                self.test_data.get("MULTICAST_CONFIGURATION_update"),
                self.test_data.get("task_019a336a-2168-7d5a-8318-958415147f3c"),
            ]
        if "playbook_multicast_delete" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("MULTICAST_CONFIGURATION_get_delete"),
                self.test_data.get("MULTICAST_CONFIGURATION_delete"),
                self.test_data.get("task_019a3414-6351-7b3a-84bb-c6aa30b87535"),
            ]
        if "playbook_multicast_delete" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("MULTICAST_CONFIGURATION_get_delete"),
                self.test_data.get("MULTICAST_CONFIGURATION_delete"),
                self.test_data.get("task_019a3414-6351-7b3a-84bb-c6aa30b87535"),
            ]
        if "playbook_rrm_general_add" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("RRM_GENERAL_CONFIGURATION_get"),
                self.test_data.get("RRM_GENERAL_CONFIGURATION_create"),
                self.test_data.get("task_019a35ba-13ef-7798-931e-0dc93f23ee7a"),
            ]
        if "playbook_rrm_general_update" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("RRM_GENERAL_CONFIGURATION_get_update"),
                self.test_data.get("RRM_GENERAL_CONFIGURATION_update_get"),
                self.test_data.get("RRM_GENERAL_CONFIGURATION_update"),
                self.test_data.get("task_019a35cc-9b8c-79ce-ba69-4e4db86feb19"),
            ]
        if "playbook_rrm_general_delete" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("RRM_GENERAL_CONFIGURATION_get_delete"),
                self.test_data.get("RRM_GENERAL_CONFIGURATION_delete"),
                self.test_data.get("task_019a35d4-1afc-798a-b874-ea489e4bffbf-"),
            ]
        if "playbook_rrm_fra_add" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("RRM_FRA_CONFIGURATION_get"),
                self.test_data.get("RRM_FRA_CONFIGURATION_create"),
                self.test_data.get("task_019a35d4-1afc-798a-b874-ea489e4bffbf"),
            ]
        if "playbook_rrm_fra_update" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("RRM_FRA_CONFIGURATION_get_update"),
                self.test_data.get("RRM_FRA_CONFIGURATION_update_get"),
                self.test_data.get("RRM_FRA_CONFIGURATION_update"),
                self.test_data.get("task_019a35ea-e355-7ad5-8ae1-333ed157b695"),
            ]
        if "playbook_rrm_fra_delete" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("RRM_FRA_CONFIGURATION_get_delete"),
                self.test_data.get("RRM_FRA_CONFIGURATION_delete"),
                self.test_data.get("task_019a360f-4667-7c0c-85b4-b510fe43023b"),
            ]
        if "playbook_event_driven_rrm_add" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("EVENT_DRIVEN_RRM_CONFIGURATION_get"),
                self.test_data.get("EVENT_DRIVEN_RRM_CONFIGURATION_create"),
                self.test_data.get("task_019a3872-5799-7481-b3d2-e7c6a7f2d202"),
            ]
        if "playbook_event_driven_rrm_update" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("EVENT_DRIVEN_RRM_CONFIGURATION_get_update"),
                self.test_data.get("EVENT_DRIVEN_RRM_CONFIGURATION_update_get"),
                self.test_data.get("EVENT_DRIVEN_RRM_CONFIGURATION_update"),
                self.test_data.get("task_019a387c-909d-725e-a537-da31c6666fb8"),
            ]
        if "playbook_event_driven_rrm_delete" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("EVENT_DRIVEN_RRM_CONFIGURATION_get_delete"),
                self.test_data.get("EVENT_DRIVEN_RRM_CONFIGURATION_delete"),
                self.test_data.get("task_019a3888-0d37-7585-9b41-4af1a8797dec"),
            ]
    # SUCCESS TESTCASES ########################################################################################

    def test_create_ssid(self):
        print("Test Data: {test_data}".format(test_data=self.test_data.get("playbook_config_create_ssids")))

        set_module_args(
            dict(
                dnac_host="1.1.1.1",
                dnac_username="dummy",
                dnac_password="dummy",
                dnac_log=False,
                dnac_log_level="DEBUG",
                dnac_version="2.3.7.9",
                config_verify=True,
                dnac_log_append=False,
                state="merged",
                config=self.test_data.get("playbook_config_create_ssids"),
            )
        )
        result = self.execute_module(changed=True, failed=False)
        self.assertIn(
            "Create SSID(s) Task succeeded for the following SSID(s)",
            result.get("msg"),
        )

    def test_update_ssid(self):
        set_module_args(
            dict(
                dnac_host="1.1.1.1",
                dnac_username="dummy",
                dnac_password="dummy",
                dnac_log=False,
                dnac_log_level="DEBUG",
                dnac_version="2.3.7.9",
                config_verify=True,
                dnac_log_append=False,
                state="merged",
                config=self.test_data.get("playbook_config_update_ssids"),
            )
        )
        result = self.execute_module(changed=True, failed=False)
        self.assertIn(
            "Update SSID(s) Task succeeded for the following SSID(s)",
            result.get("msg"),
        )

    def test_delete_ssid(self):
        set_module_args(
            dict(
                dnac_host="1.1.1.1",
                dnac_username="dummy",
                dnac_password="dummy",
                dnac_log=False,
                dnac_log_level="DEBUG",
                dnac_version="2.3.7.9",
                config_verify=True,
                dnac_log_append=False,
                state="deleted",
                config=self.test_data.get("playbook_config_delete_ssids"),
            )
        )
        result = self.execute_module(changed=True, failed=False)
        self.assertIn(
            "Delete SSID(s) Task succeeded for the following SSID(s)",
            result.get("msg"),
        )

    def test_create_interfaces(self):
        set_module_args(
            dict(
                dnac_host="1.1.1.1",
                dnac_username="dummy",
                dnac_password="dummy",
                dnac_log=False,
                dnac_log_level="DEBUG",
                dnac_version="2.3.7.9",
                config_verify=True,
                dnac_log_append=False,
                state="merged",
                config=self.test_data.get("playbook_config_create_interfaces"),
            )
        )
        result = self.execute_module(changed=True, failed=False)
        self.assertIn(
            "Create Interface(s) Task succeeded for the following interface(s)",
            result.get("msg"),
        )

    def test_update_interfaces(self):
        set_module_args(
            dict(
                dnac_host="1.1.1.1",
                dnac_username="dummy",
                dnac_password="dummy",
                dnac_log=False,
                dnac_log_level="DEBUG",
                dnac_version="2.3.7.9",
                config_verify=True,
                dnac_log_append=False,
                state="merged",
                config=self.test_data.get("playbook_config_update_interfaces"),
            )
        )
        result = self.execute_module(changed=True, failed=False)
        self.assertIn(
            "Update Interface(s) Task succeeded for the following interface(s)",
            result.get("msg"),
        )

    def test_delete_interfaces(self):
        set_module_args(
            dict(
                dnac_host="1.1.1.1",
                dnac_username="dummy",
                dnac_password="dummy",
                dnac_log=False,
                dnac_log_level="DEBUG",
                dnac_version="2.3.7.9",
                config_verify=True,
                dnac_log_append=False,
                state="deleted",
                config=self.test_data.get("playbook_config_delete_interfaces"),
            )
        )
        result = self.execute_module(changed=True, failed=False)
        self.assertIn(
            "Delete Interface(s) Task succeeded for the following interface(s)",
            result.get("msg"),
        )

    def test_add_power_profiles(self):
        set_module_args(
            dict(
                dnac_host="1.1.1.1",
                dnac_username="dummy",
                dnac_password="dummy",
                dnac_log=False,
                dnac_log_level="DEBUG",
                dnac_version="2.3.7.9",
                config_verify=True,
                dnac_log_append=False,
                state="merged",
                config=self.test_data.get("playbook_config_create_power_profiles"),
            )
        )
        result = self.execute_module(changed=True, failed=False)
        self.assertIn(
            "Create Power Profile(s) Task succeeded for the following power profile(s)",
            result.get("msg"),
        )

    def test_update_power_profiles(self):
        set_module_args(
            dict(
                dnac_host="1.1.1.1",
                dnac_username="dummy",
                dnac_password="dummy",
                dnac_log=False,
                dnac_log_level="DEBUG",
                dnac_version="2.3.7.9",
                config_verify=True,
                dnac_log_append=False,
                state="merged",
                config=self.test_data.get("playbook_config_update_power_profiles"),
            )
        )
        result = self.execute_module(changed=True, failed=False)
        self.assertIn(
            "Update Power Profile(s) Task succeeded for the following power profile(s)",
            result.get("msg"),
        )

    def test_delete_power_profiles(self):
        set_module_args(
            dict(
                dnac_host="1.1.1.1",
                dnac_username="dummy",
                dnac_password="dummy",
                dnac_log=False,
                dnac_log_level="DEBUG",
                dnac_version="2.3.7.9",
                config_verify=True,
                dnac_log_append=False,
                state="deleted",
                config=self.test_data.get("playbook_config_delete_power_profiles"),
            )
        )
        result = self.execute_module(changed=True, failed=False)
        self.assertIn(
            "Delete Power Profile(s) Task succeeded for the following power profile(s)",
            result.get("msg"),
        )

    def test_create_ap_profiles(self):
        set_module_args(
            dict(
                dnac_host="1.1.1.1",
                dnac_username="dummy",
                dnac_password="dummy",
                dnac_log=False,
                dnac_log_level="DEBUG",
                dnac_version="2.3.7.9",
                config_verify=True,
                dnac_log_append=False,
                state="merged",
                config=self.test_data.get("playbook_config_create_ap_profiles"),
            )
        )
        result = self.execute_module(changed=True, failed=False)
        self.assertIn(
            "Create Access Point Profile(s) Task succeeded for the following access point profile(s)",
            result.get("msg"),
        )

    def test_update_ap_profiles(self):
        set_module_args(
            dict(
                dnac_host="1.1.1.1",
                dnac_username="dummy",
                dnac_password="dummy",
                dnac_log=False,
                dnac_log_level="DEBUG",
                dnac_version="2.3.7.9",
                config_verify=True,
                dnac_log_append=False,
                state="merged",
                config=self.test_data.get("playbook_config_update_ap_profiles"),
            )
        )
        result = self.execute_module(changed=True, failed=False)
        self.assertIn(
            "Update Access Point Profile(s) Task succeeded for the following access point profile(s)",
            result.get("msg"),
        )

    def test_delete_ap_profiles(self):
        set_module_args(
            dict(
                dnac_host="1.1.1.1",
                dnac_username="dummy",
                dnac_password="dummy",
                dnac_log=False,
                dnac_log_level="DEBUG",
                dnac_version="2.3.7.9",
                config_verify=True,
                dnac_log_append=False,
                state="deleted",
                config=self.test_data.get("playbook_config_delete_ap_profiles"),
            )
        )
        result = self.execute_module(changed=True, failed=False)
        self.assertIn(
            "Delete Access Point Profile(s) Task succeeded for the following access point profile(s)",
            result.get("msg"),
        )

    def test_create_rf_profiles(self):
        set_module_args(
            dict(
                dnac_host="1.1.1.1",
                dnac_username="dummy",
                dnac_password="dummy",
                dnac_log=False,
                dnac_log_level="DEBUG",
                dnac_version="2.3.7.9",
                config_verify=True,
                dnac_log_append=False,
                state="merged",
                config=self.test_data.get("playbook_config_create_rf_profiles"),
            )
        )
        result = self.execute_module(changed=True, failed=False)
        self.assertIn(
            "Create Radio Frequency Profile(s) Task succeeded for the following radio frequency profile(s)",
            result.get("msg"),
        )

    def test_update_rf_profiles(self):
        set_module_args(
            dict(
                dnac_host="1.1.1.1",
                dnac_username="dummy",
                dnac_password="dummy",
                dnac_log=False,
                dnac_log_level="DEBUG",
                dnac_version="2.3.7.9",
                config_verify=True,
                dnac_log_append=False,
                state="merged",
                config=self.test_data.get("playbook_config_update_rf_profiles"),
            )
        )
        result = self.execute_module(changed=True, failed=False)
        self.assertIn(
            "Update Radio Frequency Profile(s) Task succeeded for the following radio frequency profile(s)",
            result.get("msg"),
        )

    def test_delete_rf_profiles(self):
        set_module_args(
            dict(
                dnac_host="1.1.1.1",
                dnac_username="dummy",
                dnac_password="dummy",
                dnac_log=False,
                dnac_log_level="DEBUG",
                dnac_version="2.3.7.9",
                config_verify=True,
                dnac_log_append=False,
                state="deleted",
                config=self.test_data.get("playbook_config_delete_rf_profiles"),
            )
        )
        result = self.execute_module(changed=True, failed=False)
        self.assertIn(
            "Delete Radio Frequency Profile(s) Task succeeded for the following radio frequency profile(s)",
            result.get("msg"),
        )

    def test_create_anchor_groups(self):
        set_module_args(
            dict(
                dnac_host="1.1.1.1",
                dnac_username="dummy",
                dnac_password="dummy",
                dnac_log=False,
                dnac_log_level="DEBUG",
                dnac_version="2.3.7.9",
                config_verify=True,
                dnac_log_append=False,
                state="merged",
                config=self.test_data.get("playbook_config_create_anchor_groups"),
            )
        )
        result = self.execute_module(changed=True, failed=False)
        self.assertIn(
            "Create Anchor Group(s) Task succeeded for the following anchor group(s)",
            result.get("msg"),
        )

    def test_update_anchor_groups(self):
        set_module_args(
            dict(
                dnac_host="1.1.1.1",
                dnac_username="dummy",
                dnac_password="dummy",
                dnac_log=False,
                dnac_log_level="DEBUG",
                dnac_version="2.3.7.9",
                config_verify=True,
                dnac_log_append=False,
                state="merged",
                config=self.test_data.get("playbook_config_update_anchor_groups"),
            )
        )
        result = self.execute_module(changed=True, failed=False)
        self.assertIn(
            "Update Anchor Group(s) Task succeeded for the following anchor group(s)",
            result.get("msg"),
        )

    def test_delete_anchor_groups(self):
        set_module_args(
            dict(
                dnac_host="1.1.1.1",
                dnac_username="dummy",
                dnac_password="dummy",
                dnac_log=False,
                dnac_log_level="DEBUG",
                dnac_version="2.3.7.9",
                config_verify=True,
                dnac_log_append=False,
                state="deleted",
                config=self.test_data.get("playbook_config_delete_anchor_groups"),
            )
        )
        result = self.execute_module(changed=True, failed=False)
        self.assertIn(
            "Delete Anchor Group(s) Task succeeded for the following anchor group(s)",
            result.get("msg"),
        )

    def test_wireless_design_workflow_manager_playbook_aaa_radius_attribute(self):
        set_module_args(
            dict(
                dnac_version='3.1.3.0',
                dnac_host="1.1.1.1",
                dnac_username="dummy",
                dnac_password="dummy",
                dnac_log=True,
                state="merged",
                config=self.playbook_aaa_radius_attribute
            )
        )
        result = self.execute_module(changed=True, failed=False)
        self.assertEqual(
            result.get('msg'),
            {
                "aaa_radius_attributes_add": {
                    "sample_design": "Successfully created AAA Radius Attribute."
                }
            }
        )

    def test_wireless_design_workflow_manager_playbook_aaa_radius_attribute_update(self):
        set_module_args(
            dict(
                dnac_version='3.1.3.0',
                dnac_host="1.1.1.1",
                dnac_username="dummy",
                dnac_password="dummy",
                dnac_log=True,
                state="merged",
                config=self.playbook_aaa_radius_attribute_update
            )
        )
        result = self.execute_module(changed=True, failed=False)
        self.assertEqual(
            result.get('msg'),
            {
                "aaa_radius_attributes_update": {
                    "sample_design": "Successfully updated AAA Radius Attribute."
                }
            }
        )

    def test_wireless_design_workflow_manager_playbook_aaa_radius_attribute_delete(self):
        set_module_args(
            dict(
                dnac_version='3.1.3.0',
                dnac_host="1.1.1.1",
                dnac_username="dummy",
                dnac_password="dummy",
                dnac_log=True,
                state="deleted",
                config=self.playbook_aaa_radius_attribute_delete
            )
        )
        result = self.execute_module(changed=True, failed=False)
        self.assertEqual(
            result.get('msg'),
            {
                "aaa_radius_attributes_delete": {
                    "sample_design": "Successfully deleted AAA Radius Attribute."
                }
            }
        )

    def test_wireless_design_workflow_manager_playbook_advanced_ssid_create(self):
        set_module_args(
            dict(
                dnac_version='3.1.3.0',
                dnac_host="1.1.1.1",
                dnac_username="dummy",
                dnac_password="dummy",
                dnac_log=True,
                state="merged",
                config=self.playbook_advanced_ssid_create
            )
        )
        result = self.execute_module(changed=True, failed=False)
        self.assertEqual(
            result.get('msg'),
            {
                "advanced_ssids_add": {
                    "sample_advanced_ssid_design": "Successfully created Advanced SSID."
                }
            }
        )

    def test_wireless_design_workflow_manager_playbook_advanced_ssid_update(self):
        set_module_args(
            dict(
                dnac_version='3.1.3.0',
                dnac_host="1.1.1.1",
                dnac_username="dummy",
                dnac_password="dummy",
                dnac_log=True,
                state="merged",
                config=self.playbook_advanced_ssid_update
            )
        )
        result = self.execute_module(changed=True, failed=False)
        self.assertEqual(
            result.get('msg'),
            {
                "advanced_ssids_update": {
                    "sample_advanced_ssid_design": "Successfully updated Advanced SSID."
                }
            }
        )

    def test_wireless_design_workflow_manager_playbook_advanced_ssid_delete(self):
        set_module_args(
            dict(
                dnac_version='3.1.3.0',
                dnac_host="1.1.1.1",
                dnac_username="dummy",
                dnac_password="dummy",
                dnac_log=True,
                state="deleted",
                config=self.playbook_advanced_ssid_delete
            )
        )
        result = self.execute_module(changed=True, failed=False)
        self.assertEqual(
            result.get('msg'),
            {
                "advanced_ssids_delete": {
                    "sample_advanced_ssid_design": "Successfully deleted Advanced SSID."
                }
            }
        )

    def test_wireless_design_workflow_manager_playbook_clean_air_create(self):
        set_module_args(
            dict(
                dnac_version='3.1.3.0',
                dnac_host="1.1.1.1",
                dnac_username="dummy",
                dnac_password="dummy",
                dnac_log=True,
                state="merged",
                config=self.playbook_clean_air_create
            )
        )
        result = self.execute_module(changed=True, failed=False)
        self.assertEqual(
            result.get('msg'),
            {
                "clean_air_add": {
                    "sample_cleanair_design_24ghz": "Successfully created CleanAir Profile."
                }
            }
        )

    def test_wireless_design_workflow_manager_playbook_clean_air_update(self):
        set_module_args(
            dict(
                dnac_version='3.1.3.0',
                dnac_host="1.1.1.1",
                dnac_username="dummy",
                dnac_password="dummy",
                dnac_log=True,
                state="merged",
                config=self.playbook_clean_air_update
            )
        )
        result = self.execute_module(changed=True, failed=False)
        self.assertEqual(
            result.get('msg'),
            {
                "clean_air_update": {
                    "sample_cleanair_design_24ghz": "Successfully updated CleanAir Profile."
                }
            }
        )

    def test_wireless_design_workflow_manager_playbook_clean_air_delete(self):
        set_module_args(
            dict(
                dnac_version='3.1.3.0',
                dnac_host="1.1.1.1",
                dnac_username="dummy",
                dnac_password="dummy",
                dnac_log=True,
                state="deleted",
                config=self.playbook_clean_air_delete
            )
        )
        result = self.execute_module(changed=True, failed=False)
        self.assertEqual(
            result.get('msg'),
            {
                "clean_air_delete": {
                    "sample_cleanair_design_24ghz": "Successfully deleted CleanAir Profile."
                }
            }
        )

    def test_wireless_design_workflow_manager_playbook_dot11ax_add(self):
        set_module_args(
            dict(
                dnac_version='3.1.3.0',
                dnac_host="1.1.1.1",
                dnac_username="dummy",
                dnac_password="dummy",
                dnac_log=True,
                state="merged",
                config=self.playbook_dot11ax_add
            )
        )
        result = self.execute_module(changed=True, failed=False)
        self.assertEqual(
            result.get('msg'),
            {
                "dot11ax_add": {
                    "dot11ax_24ghz_design": "Successfully created dot11ax configuration."
                }
            }
        )

    def test_wireless_design_workflow_manager_playbook_dot11ax_update(self):
        set_module_args(
            dict(
                dnac_version='3.1.3.0',
                dnac_host="1.1.1.1",
                dnac_username="dummy",
                dnac_password="dummy",
                dnac_log=True,
                state="merged",
                config=self.playbook_dot11ax_update
            )
        )
        result = self.execute_module(changed=True, failed=False)
        self.assertEqual(
            result.get('msg'),
            {
                "dot11ax_update": {
                    "dot11ax_24ghz_design": "Successfully updated dot11ax configuration."
                }
            }
        )

    def test_wireless_design_workflow_manager_playbook_dot11ax_delete(self):
        set_module_args(
            dict(
                dnac_version='3.1.3.0',
                dnac_host="1.1.1.1",
                dnac_username="dummy",
                dnac_password="dummy",
                dnac_log=True,
                state="deleted",
                config=self.playbook_dot11ax_delete
            )
        )
        result = self.execute_module(changed=True, failed=False)
        self.assertEqual(
            result.get('msg'),
            {
                "dot11ax_delete": {
                    "dot11ax_24ghz_design": "Successfully deleted dot11ax configuration."
                }
            }
        )

    def test_wireless_design_workflow_manager_playbook_dot11be_add(self):
        set_module_args(
            dict(
                dnac_version='3.1.3.0',
                dnac_host="1.1.1.1",
                dnac_username="dummy",
                dnac_password="dummy",
                dnac_log=True,
                state="merged",
                config=self.playbook_dot11be_add
            )
        )
        result = self.execute_module(changed=True, failed=False)
        self.assertEqual(
            result.get('msg'),
            {
                "dot11be_add": {
                    "dot11be_24ghz_design": "Successfully created dot11be configuration."
                }
            }
        )

    def test_wireless_design_workflow_manager_playbook_dot11be_update(self):
        set_module_args(
            dict(
                dnac_version='3.1.3.0',
                dnac_host="1.1.1.1",
                dnac_username="dummy",
                dnac_password="dummy",
                dnac_log=True,
                state="merged",
                config=self.playbook_dot11be_update
            )
        )
        result = self.execute_module(changed=True, failed=False)
        self.assertEqual(
            result.get('msg'),
            {
                "dot11be_update": {
                    "dot11be_24ghz_design": "Successfully updated dot11be configuration."
                }
            }
        )

    def test_wireless_design_workflow_manager_playbook_dot11be_delete(self):
        set_module_args(
            dict(
                dnac_version='3.1.3.0',
                dnac_host="1.1.1.1",
                dnac_username="dummy",
                dnac_password="dummy",
                dnac_log=True,
                state="deleted",
                config=self.playbook_dot11be_delete
            )
        )
        result = self.execute_module(changed=True, failed=False)
        self.assertEqual(
            result.get('msg'),
            {
                "dot11be_delete": {
                    "dot11be_24ghz_design": "Successfully deleted dot11be configuration."
                }
            }
        )

    def test_wireless_design_workflow_manager_playbook_flexconnect_add(self):
        set_module_args(
            dict(
                dnac_version='3.1.3.0',
                dnac_host="1.1.1.1",
                dnac_username="dummy",
                dnac_password="dummy",
                dnac_log=True,
                state="merged",
                config=self.playbook_flexconnect_add
            )
        )
        result = self.execute_module(changed=True, failed=False)
        self.assertEqual(
            result.get('msg'),
            {
                "flexconnect_add": {
                    "flexconnect_branch_office": "Successfully created FlexConnect."
                }
            }
        )

    def test_wireless_design_workflow_manager_playbook_flexconnect_update(self):
        set_module_args(
            dict(
                dnac_version='3.1.3.0',
                dnac_host="1.1.1.1",
                dnac_username="dummy",
                dnac_password="dummy",
                dnac_log=True,
                state="merged",
                config=self.playbook_flexconnect_update
            )
        )
        result = self.execute_module(changed=True, failed=False)
        self.assertEqual(
            result.get('msg'),
            {
                "flexconnect_update": {
                    "flexconnect_branch_office": "Successfully updated FlexConnect."
                }
            }
        )

    def test_wireless_design_workflow_manager_playbook_flexconnect_delete(self):
        set_module_args(
            dict(
                dnac_version='3.1.3.0',
                dnac_host="1.1.1.1",
                dnac_username="dummy",
                dnac_password="dummy",
                dnac_log=True,
                state="deleted",
                config=self.playbook_flexconnect_delete
            )
        )
        result = self.execute_module(changed=True, failed=False)
        self.assertEqual(
            result.get('msg'),
            {
                "flexconnect_delete": {
                    "flexconnect_branch_office": "Successfully deleted FlexConnect."
                }
            }
        )

    def test_wireless_design_workflow_manager_playbook_multicast_add(self):
        set_module_args(
            dict(
                dnac_version='3.1.3.0',
                dnac_host="1.1.1.1",
                dnac_username="dummy",
                dnac_password="dummy",
                dnac_log=True,
                state="merged",
                config=self.playbook_multicast_add
            )
        )
        result = self.execute_module(changed=True, failed=False)
        self.assertEqual(
            result.get('msg'),
            {
                "multicast_add": {
                    "Unknown": "Successfully created Multicast configuration."
                }
            }
        )

    def test_wireless_design_workflow_manager_playbook_multicast_update(self):
        set_module_args(
            dict(
                dnac_version='3.1.3.0',
                dnac_host="1.1.1.1",
                dnac_username="dummy",
                dnac_password="dummy",
                dnac_log=True,
                state="merged",
                config=self.playbook_multicast_update
            )
        )
        result = self.execute_module(changed=True, failed=False)
        self.assertEqual(
            result.get('msg'),
            {
                "multicast_update": {
                    "multicast_office_profile_1": "Successfully updated Multicast configuration."
                }
            }
        )

    def test_wireless_design_workflow_manager_playbook_rrm_general_add(self):
        set_module_args(
            dict(
                dnac_version='3.1.3.0',
                dnac_host="1.1.1.1",
                dnac_username="dummy",
                dnac_password="dummy",
                dnac_log=True,
                state="merged",
                config=self.playbook_rrm_general_add
            )
        )
        result = self.execute_module(changed=True, failed=False)
        self.assertEqual(
            result.get('msg'),
            {
                "rrm_general_add": {
                    "rrm_general_5ghz_default": "Successfully created RRM General configuration."
                }
            }
        )

    def test_wireless_design_workflow_manager_playbook_rrm_general_update(self):
        set_module_args(
            dict(
                dnac_version='3.1.3.0',
                dnac_host="1.1.1.1",
                dnac_username="dummy",
                dnac_password="dummy",
                dnac_log=True,
                state="merged",
                config=self.playbook_rrm_general_update
            )
        )
        result = self.execute_module(changed=True, failed=False)
        self.assertEqual(
            result.get('msg'),
            {
                "rrm_general_update": {
                    "rrm_general_5ghz_default": "Successfully updated RRM General configuration."
                }
            }
        )

    def test_wireless_design_workflow_manager_playbook_rrm_general_delete(self):
        set_module_args(
            dict(
                dnac_version='3.1.3.0',
                dnac_host="1.1.1.1",
                dnac_username="dummy",
                dnac_password="dummy",
                dnac_log=True,
                state="deleted",
                config=self.playbook_rrm_general_delete
            )
        )
        result = self.execute_module(changed=True, failed=False)
        self.assertEqual(
            result.get('msg'),
            {
                "rrm_general_delete": {
                    "rrm_general_5ghz_default": "Successfully deleted RRM General configuration."
                }
            }
        )

    def test_wireless_design_workflow_manager_playbook_rrm_fra_add(self):
        set_module_args(
            dict(
                dnac_version='3.1.3.0',
                dnac_host="1.1.1.1",
                dnac_username="dummy",
                dnac_password="dummy",
                dnac_log=True,
                state="merged",
                config=self.playbook_rrm_fra_add
            )
        )
        result = self.execute_module(changed=True, failed=False)
        self.assertEqual(
            result.get('msg'),
            {
                "rrm_fra_add": {
                    "fra_design_1": "Successfully created RRM-FRA configuration."
                }
            }
        )

    def test_wireless_design_workflow_manager_playbook_rrm_fra_update(self):
        set_module_args(
            dict(
                dnac_version='3.1.3.0',
                dnac_host="1.1.1.1",
                dnac_username="dummy",
                dnac_password="dummy",
                dnac_log=True,
                state="merged",
                config=self.playbook_rrm_fra_update
            )
        )
        result = self.execute_module(changed=True, failed=False)
        self.assertEqual(
            result.get('msg'),
            {
                "rrm_fra_update": {
                    "fra_design_1": "Successfully updated RRM-FRA configuration."
                }
            }
        )

    def test_wireless_design_workflow_manager_playbook_rrm_fra_delete(self):
        set_module_args(
            dict(
                dnac_version='3.1.3.0',
                dnac_host="1.1.1.1",
                dnac_username="dummy",
                dnac_password="dummy",
                dnac_log=True,
                state="deleted",
                config=self.playbook_rrm_fra_delete
            )
        )
        result = self.execute_module(changed=True, failed=False)
        self.assertEqual(
            result.get('msg'),
            {
                "rrm_fra_delete": {
                    "fra_design_1": "Successfully deleted RRM-FRA configuration."
                }
            }
        )

    def test_wireless_design_workflow_manager_playbook_event_driven_rrm_add(self):
        set_module_args(
            dict(
                dnac_version='3.1.3.0',
                dnac_host="1.1.1.1",
                dnac_username="dummy",
                dnac_password="dummy",
                dnac_log=True,
                state="merged",
                config=self.playbook_event_driven_rrm_add
            )
        )
        result = self.execute_module(changed=True, failed=False)
        self.assertEqual(
            result.get('msg'),
            {
                "event_driven_rrm_add": {
                    "edrrm_2_4ghz_design": "Successfully created Event-Driven RRM configuration."
                }
            }
        )

    def test_wireless_design_workflow_manager_playbook_event_driven_rrm_update(self):
        set_module_args(
            dict(
                dnac_version='3.1.3.0',
                dnac_host="1.1.1.1",
                dnac_username="dummy",
                dnac_password="dummy",
                dnac_log=True,
                state="merged",
                config=self.playbook_event_driven_rrm_update
            )
        )
        result = self.execute_module(changed=True, failed=False)
        self.assertEqual(
            result.get('msg'),
            {
                "event_driven_rrm_update": {
                    "edrrm_2_4ghz_design": "Successfully updated Event-Driven RRM configuration."
                }
            }
        )

    def test_wireless_design_workflow_manager_playbook_event_driven_rrm_delete(self):
        set_module_args(
            dict(
                dnac_version='3.1.3.0',
                dnac_host="1.1.1.1",
                dnac_username="dummy",
                dnac_password="dummy",
                dnac_log=True,
                state="deleted",
                config=self.playbook_event_driven_rrm_delete
            )
        )
        result = self.execute_module(changed=True, failed=False)
        self.assertEqual(
            result.get('msg'),
            {
                "event_driven_rrm_delete": {
                    "edrrm_2_4ghz_design": "Successfully deleted Event-Driven RRM configuration."
                }
            }
        )
