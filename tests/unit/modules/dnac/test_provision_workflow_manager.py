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
    playbook_provision_wireless_device = test_data.get("playbook_provision_wireless_device")
    playbook_application_telemetry_disable = test_data.get("playbook_application_telemetry_disable")
    playbook_application_telemetry_enable = test_data.get("playbook_application_telemetry_enable")
    playbook_delete_provision = test_data.get("playbook_delete_provision")

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

        elif "playbook_provision_wireless_device" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("204.192.13.1"),
                self.test_data.get("get_network_device_by_ip_wireless"),
                self.test_data.get("get_network_device_by_ip_wireless1"),
                self.test_data.get("Global/USA/SAN-FRANCISCO/BLD_SF"),
                self.test_data.get("get_site_wireless"),
                self.test_data.get("Global/USA/SAN-FRANCISCO/BLD_SF"),
                self.test_data.get("get_site_assigned_network_device"),
                self.test_data.get("get_network_device_by_ip_wireless2"),
                self.test_data.get("get_site_assigned_network_device"),
                self.test_data.get("assign_managed_ap_locations_for_w_l_c"),
                self.test_data.get("assign_managed_ap_locations_for_w_l_c_1"),
                self.test_data.get("wireless_controller_provision"),
                self.test_data.get("Task_Detailss"),
                self.test_data.get("Task_Detailss_1"),
                self.test_data.get("wireless_controller_provision"),
                self.test_data.get("Task_Detailss"),
                self.test_data.get("Task_Detailss_1"),
                self.test_data.get("provision_wireless_device_response"),
            ]

        elif "playbook_application_telemetry_disable" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("get_network_device_by_ip_telemetry"),
                self.test_data.get("get_network_device_by_ip_telemetry_1"),
                self.test_data.get("get_network_device_by_ip_telemetry_2"),
                self.test_data.get("get_network_device_by_ip_telemetry_3"),
                self.test_data.get("disable"),
                self.test_data.get("Task_Details"),
                self.test_data.get("disable_response"),
            ]
        elif "playbook_application_telemetry_enable" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("get_network_device_by_ip_telemetry_5"),
                self.test_data.get("get_network_device_by_ip_telemetry_6"),
                self.test_data.get("get_network_device_by_ip_telemetry_7"),
                self.test_data.get("get_network_device_by_ip_telemetry_8"),
                self.test_data.get("enable"),
                self.test_data.get("Task_Details_1"),
                self.test_data.get("enable_response"),
            ]

        elif "playbook_delete_provision" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("204.192.3.40"),
                self.test_data.get("get_network_device_by_ip_delete"),
                self.test_data.get("site_design_delete"),
                self.test_data.get("get_network_device_by_ip_delete1"),
                self.test_data.get("get_provisioned_devices_delete"),
                self.test_data.get("delete_network_device_with_configuration_cleanup"),
                self.test_data.get("Task Details"),
                self.test_data.get("Task Details1"),
                self.test_data.get("delete_provision_response"),

            ]

    def test_provision_workflow_manager_playbook_provision_wired_device(self):
        """
        Test idempotent provisioning behavior for an already provisioned wired device.

        Verifies that attempting to provision a wired network device already configured in
        Cisco Catalyst Center does not result in errors and returns the appropriate status message.
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
        Test re-provisioning of an existing wired network device with full credentials.

        Ensures that an already onboarded wired device can be successfully re-provisioned
        in Cisco Catalyst Center using the playbook workflow when all necessary credentials are provided.
        """
        set_module_args(
            dict(
                dnac_host="1.1.1.1",
                dnac_version="2.3.7.9",
                dnac_username="dummy",
                dnac_password="dummy",
                config_verify=True,
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
        Test provisioning of a network device with full credentials.

        Validates that a wired device can be successfully provisioned in Cisco Catalyst Center
        using the playbook workflow when complete credentials are provided.
        """
        set_module_args(
            dict(
                dnac_host="1.1.1.1",
                dnac_version="2.3.7.9",
                dnac_username="dummy",
                dnac_password="dummy",
                config_verify=True,
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

    def test_provision_workflow_manager_playbook_provision_wireless_device(self):
        """
        Test provisioning of a wireless device with full credentials.

        Validates that a wireless device can be successfully provisioned in Cisco Catalyst Center
        using the playbook workflow when complete credentials are provided.
        """
        set_module_args(
            dict(
                dnac_host="1.1.1.1",
                dnac_version="2.3.7.9",
                dnac_username="dummy",
                dnac_password="dummy",
                dnac_log=True,
                state="merged",
                config=self.playbook_provision_wireless_device
            )
        )
        result = self.execute_module(changed=True, failed=False)
        print(result)
        self.assertEqual(
            result.get('msg'),
            "Provisioning of the wireless device '204.192.13.1' completed successfully."
        )

    def test_provision_workflow_manager_playbook_application_telemetry_disable(self):
        """
        Test disabling of application telemetry using the playbook workflow.

        Validates that application telemetry can be successfully disabled for all devices
        in Cisco Catalyst Center using the playbook workflow when full device credentials are provided.
        """
        set_module_args(
            dict(
                dnac_host="1.1.1.1",
                dnac_version="2.3.7.9",
                dnac_username="dummy",
                dnac_password="dummy",
                dnac_log=True,
                state="merged",
                config=self.playbook_application_telemetry_disable
            )
        )
        result = self.execute_module(changed=True, failed=False)
        print(result)
        self.assertEqual(
            result.get('msg'),
            "Application telemetry disabling successfully for all devices."
        )

    def test_provision_workflow_manager_playbook_application_telemetry_enable(self):
        """
        Test enabling of application telemetry using the playbook workflow.

        Validates that application telemetry can be successfully enabled for all devices
        in Cisco Catalyst Center using the playbook workflow when full device credentials are provided.
        """
        set_module_args(
            dict(
                dnac_host="1.1.1.1",
                dnac_version="2.3.7.9",
                dnac_username="dummy",
                dnac_password="dummy",
                dnac_log=True,
                state="merged",
                config=self.playbook_application_telemetry_enable
            )
        )
        result = self.execute_module(changed=True, failed=False)
        print(result)
        self.assertEqual(
            result.get('msg'),
            "Application telemetry enabling successfully for all devices."
        )

    def test_provision_workflow_manager_playbook_delete_provision(self):
        """
        Test deletion of a provisioned device using the playbook workflow.

        Validates that a previously provisioned network device can be successfully deleted
        from Cisco Catalyst Center using the playbook workflow with full device credentials.
        """
        set_module_args(
            dict(
                dnac_host="1.1.1.1",
                dnac_version="2.3.7.9",
                dnac_username="dummy",
                dnac_password="dummy",
                dnac_log=True,
                config_verify=True,
                state="deleted",
                config=self.playbook_delete_provision
            )
        )
        result = self.execute_module(changed=True, failed=False)
        print(result)
        self.assertEqual(
            result.get('msg'),
            "Deletion done Successfully for the device '204.192.3.40' "
        )
