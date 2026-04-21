# Copyright (c) 2026 Cisco and/or its affiliates.
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
#   Archit Soni <soni.archit03@gmail.com>
#
# Description:
#   Unit tests for the Ansible module `sda_fabric_devices_workflow_manager`.
#   These tests cover fabric device and wireless controller operations such as creation,
#   update, and deletion using mocked Catalyst Center responses.

from __future__ import absolute_import, division, print_function

# Metadata
__metaclass__ = type
__author__ = "Archit Soni"
__email__ = "soni.archit03@gmail.com"
__version__ = "1.0.0"

from unittest.mock import patch
from ansible_collections.cisco.dnac.plugins.modules import (
    sda_fabric_devices_workflow_manager,
)
from .dnac_module import TestDnacModule, loadPlaybookData, set_module_args


class TestDnacSdaFabricDevicesWorkflowManager(TestDnacModule):

    module = sda_fabric_devices_workflow_manager
    test_data = loadPlaybookData("sda_fabric_devices_workflow_manager")

    playbook_config_create_fabric_device_case_1 = test_data.get(
        "create_fabric_device_case_1"
    )
    playbook_config_update_fabric_device_case_2 = test_data.get(
        "update_fabric_device_case_2"
    )
    playbook_config_delete_fabric_device_case_3 = test_data.get(
        "delete_fabric_device_case_3"
    )
    playbook_config_create_wireless_controller_case_4 = test_data.get(
        "create_wireless_controller_case_4"
    )
    playbook_config_update_wireless_controller_case_5 = test_data.get(
        "update_wireless_controller_case_5"
    )
    playbook_config_delete_wireless_controller_case_6 = test_data.get(
        "delete_wireless_controller_case_6"
    )

    def setUp(self):
        super(TestDnacSdaFabricDevicesWorkflowManager, self).setUp()

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

    def tearDown(self):
        super(TestDnacSdaFabricDevicesWorkflowManager, self).tearDown()
        self.mock_dnac_exec.stop()
        self.mock_dnac_init.stop()

    def load_fixtures(self, response=None, device=""):
        """
        Load fixtures for user.
        """
        if "test_create_fabric_device_case_1" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("get_sites_sf"),
                self.test_data.get("get_fabric_sites_sf"),
                self.test_data.get("get_device_list"),
                self.test_data.get("get_provisioned_devices"),
                self.test_data.get("get_fabric_devices_empty"),
                self.test_data.get("add_fabric_devices"),
                self.test_data.get("task_success"),
                self.test_data.get("get_sites_sf"),
                self.test_data.get("get_fabric_sites_sf"),
                self.test_data.get("get_device_list"),
                self.test_data.get("get_provisioned_devices"),
                self.test_data.get("get_fabric_devices_border_cp_priority1"),
                self.test_data.get("get_sda_wireless_empty"),
                self.test_data.get("get_primary_ap_locations_empty"),
                self.test_data.get("get_secondary_ap_locations_empty"),
            ]
        elif "test_update_fabric_device_case_2" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("get_sites_sf"),
                self.test_data.get("get_fabric_sites_sf"),
                self.test_data.get("get_device_list"),
                self.test_data.get("get_provisioned_devices"),
                self.test_data.get("get_fabric_devices_border_cp_priority1"),
                self.test_data.get("get_sda_wireless_empty"),
                self.test_data.get("get_primary_ap_locations_empty"),
                self.test_data.get("get_secondary_ap_locations_empty"),
                self.test_data.get("update_fabric_devices"),
                self.test_data.get("task_success"),
                self.test_data.get("get_sites_sf"),
                self.test_data.get("get_fabric_sites_sf"),
                self.test_data.get("get_device_list"),
                self.test_data.get("get_provisioned_devices"),
                self.test_data.get("get_fabric_devices_border_cp_priority2"),
                self.test_data.get("get_sda_wireless_empty"),
                self.test_data.get("get_primary_ap_locations_empty"),
                self.test_data.get("get_secondary_ap_locations_empty"),
            ]
        elif "test_delete_fabric_device_case_3" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("get_sites_sf"),
                self.test_data.get("get_fabric_sites_sf"),
                self.test_data.get("get_device_list"),
                self.test_data.get("get_fabric_devices_border_cp_priority1"),
                self.test_data.get("get_sda_wireless_empty"),
                self.test_data.get("get_primary_ap_locations_empty"),
                self.test_data.get("get_secondary_ap_locations_empty"),
                self.test_data.get("delete_fabric_device"),
                self.test_data.get("task_success"),
            ]
        elif "test_create_wireless_controller_case_4" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("get_sites_sf"),
                self.test_data.get("get_fabric_sites_sf"),
                self.test_data.get("get_device_list"),
                self.test_data.get("get_provisioned_devices"),
                self.test_data.get("get_fabric_devices_empty"),
                self.test_data.get("case_4_call_6"),
                self.test_data.get("case_4_call_7"),
                self.test_data.get("case_4_call_8"),
                self.test_data.get("case_4_call_9"),
                self.test_data.get("case_4_call_10"),
                self.test_data.get("case_4_call_11"),
                self.test_data.get("case_4_call_12"),
                self.test_data.get("case_4_call_13"),
                self.test_data.get("case_4_call_14"),
                self.test_data.get("case_4_call_15"),
                self.test_data.get("case_4_call_16"),
                self.test_data.get("case_4_call_17"),
                self.test_data.get("add_fabric_devices"),
                self.test_data.get("task_success"),
                self.test_data.get("get_sites_sf"),
                self.test_data.get("get_fabric_sites_sf"),
                self.test_data.get("get_device_list"),
                self.test_data.get("get_provisioned_devices"),
                self.test_data.get("get_fabric_devices_border_cp_priority1"),
                self.test_data.get("get_sda_wireless_empty"),
                self.test_data.get("get_primary_ap_locations_empty"),
                self.test_data.get("get_secondary_ap_locations_empty"),
                self.test_data.get("assign_managed_ap_locations"),
                self.test_data.get("task_success"),
                self.test_data.get("switch_wireless_setting"),
                self.test_data.get("task_success"),
            ]
        elif "test_update_wireless_controller_case_5" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("get_sites_sf"),
                self.test_data.get("get_fabric_sites_sf"),
                self.test_data.get("get_device_list"),
                self.test_data.get("get_provisioned_devices"),
                self.test_data.get("get_fabric_devices_wlc_have"),
                self.test_data.get("get_sda_wireless_enabled_25"),
                self.test_data.get("get_primary_ap_locations_three"),
                self.test_data.get("get_secondary_ap_locations_three"),
                self.test_data.get("case_4_call_6"),
                self.test_data.get("case_4_call_7"),
                self.test_data.get("case_4_call_8"),
                self.test_data.get("case_4_call_9"),
                self.test_data.get("case_4_call_12"),
                self.test_data.get("case_4_call_13"),
                self.test_data.get("case_4_call_14"),
                self.test_data.get("case_4_call_15"),
                self.test_data.get("get_sites_sf"),
                self.test_data.get("get_fabric_sites_sf"),
                self.test_data.get("get_device_list"),
                self.test_data.get("get_provisioned_devices"),
                self.test_data.get("get_fabric_devices_wlc_have"),
                self.test_data.get("get_sda_wireless_enabled_25"),
                self.test_data.get("get_primary_ap_locations_three"),
                self.test_data.get("get_secondary_ap_locations_three"),
                self.test_data.get("assign_managed_ap_locations"),
                self.test_data.get("task_success"),
                self.test_data.get("switch_wireless_setting"),
                self.test_data.get("task_success"),
            ]
        elif "test_delete_wireless_controller_case_6" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("get_sites_sf"),
                self.test_data.get("get_fabric_sites_sf"),
                self.test_data.get("get_device_list"),
                self.test_data.get("get_provisioned_devices"),
                self.test_data.get("get_fabric_devices_wlc_have"),
                self.test_data.get("get_sda_wireless_enabled_25"),
                self.test_data.get("get_primary_ap_locations_empty"),
                self.test_data.get("get_secondary_ap_locations_empty"),
                self.test_data.get("get_sites_sf"),
                self.test_data.get("get_fabric_sites_sf"),
                self.test_data.get("get_device_list"),
                self.test_data.get("get_provisioned_devices"),
                self.test_data.get("get_fabric_devices_wlc_have"),
                self.test_data.get("get_sda_wireless_enabled_25"),
                self.test_data.get("get_primary_ap_locations_empty"),
                self.test_data.get("get_secondary_ap_locations_empty"),
                self.test_data.get("switch_wireless_setting"),
                self.test_data.get("task_success"),
                self.test_data.get("reload_switch"),
                self.test_data.get("task_success"),
            ]

    def test_create_fabric_device_case_1(self):
        set_module_args(
            dict(
                dnac_host="1.1.1.1",
                dnac_username="dummy",
                dnac_password="dummy",
                dnac_version="2.3.7.9",
                dnac_log=True,
                state="merged",
                config_verify=False,
                config=self.playbook_config_create_fabric_device_case_1,
            )
        )

        result = self.execute_module(changed=True, failed=False)
        self.assertIn(
            "Successfully added the fabric device",
            result.get("msg"),
        )

    def test_update_fabric_device_case_2(self):
        set_module_args(
            dict(
                dnac_host="1.1.1.1",
                dnac_username="dummy",
                dnac_password="dummy",
                dnac_version="2.3.7.9",
                dnac_log=True,
                state="merged",
                config_verify=False,
                config=self.playbook_config_update_fabric_device_case_2,
            )
        )

        result = self.execute_module(changed=True, failed=False)
        self.assertIn(
            "Successfully updated the fabric device",
            result.get("msg"),
        )

    def test_delete_fabric_device_case_3(self):
        set_module_args(
            dict(
                dnac_host="1.1.1.1",
                dnac_username="dummy",
                dnac_password="dummy",
                dnac_version="2.3.7.9",
                dnac_log=True,
                state="deleted",
                config_verify=False,
                config=self.playbook_config_delete_fabric_device_case_3,
            )
        )

        result = self.execute_module(changed=True, failed=False)
        self.assertEqual(
            result.get("msg"),
            "Successfully deleted the SDA fabric device with IP '204.1.4.1'.",
        )

    def test_create_wireless_controller_case_4(self):
        set_module_args(
            dict(
                dnac_host="1.1.1.1",
                dnac_username="dummy",
                dnac_password="dummy",
                dnac_version="2.3.7.9",
                dnac_log=True,
                state="merged",
                config_verify=False,
                config=self.playbook_config_create_wireless_controller_case_4,
            )
        )

        result = self.execute_module(changed=True, failed=False)
        self.assertEqual(
            result.get("msg"),
            "Wireless Controller Settings for the device with IP address: '204.1.4.1' under fabric: 'Global/USA/SAN_FRANCISCO' "
            "updated successfully in the Cisco Catalyst Center.",
        )

    def test_update_wireless_controller_case_5(self):
        set_module_args(
            dict(
                dnac_host="1.1.1.1",
                dnac_username="dummy",
                dnac_password="dummy",
                dnac_version="2.3.7.9",
                dnac_log=True,
                state="merged",
                config_verify=False,
                config=self.playbook_config_update_wireless_controller_case_5,
            )
        )

        result = self.execute_module(changed=True, failed=False)
        self.assertEqual(
            result.get("msg"),
            "Wireless Controller Settings for the device with IP address: '204.1.4.1' under fabric: 'Global/USA/SAN_FRANCISCO' "
            "updated successfully in the Cisco Catalyst Center.",
        )

    def test_delete_wireless_controller_case_6(self):
        set_module_args(
            dict(
                dnac_host="1.1.1.1",
                dnac_username="dummy",
                dnac_password="dummy",
                dnac_version="2.3.7.9",
                dnac_log=True,
                state="merged",
                config_verify=False,
                config=self.playbook_config_delete_wireless_controller_case_6,
            )
        )

        result = self.execute_module(changed=True, failed=False)
        self.assertEqual(
            result.get("msg"),
            "Reload successful for the device with IP address: '204.1.4.1' under fabric: 'Global/USA/SAN_FRANCISCO' in the Cisco Catalyst Center",
        )
