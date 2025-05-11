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
from ansible_collections.cisco.dnac.plugins.modules import sda_host_port_onboarding_workflow_manager
from .dnac_module import TestDnacModule, set_module_args, loadPlaybookData


class SDAHostPortOnboarding(TestDnacModule):

    module = sda_host_port_onboarding_workflow_manager

    test_data = loadPlaybookData("sda_host_onboarding_workflow_manager_intent")

    def setUp(self):
        super(SDAHostPortOnboarding, self).setUp()

        self.mock_dnac_init = patch(
            "ansible_collections.cisco.dnac.plugins.module_utils.dnac.DNACSDK.__init__")
        self.run_dnac_init = self.mock_dnac_init.start()
        self.run_dnac_init.side_effect = [None]
        self.mock_dnac_exec = patch(
            "ansible_collections.cisco.dnac.plugins.module_utils.dnac.DNACSDK._exec"
        )
        self.run_dnac_exec = self.mock_dnac_exec.start()
        self.load_fixtures()

        print(f"Mock for DNACSDK._exec: {self.run_dnac_exec}")

    def tearDown(self):
        super(SDAHostPortOnboarding, self).tearDown()
        self.mock_dnac_init.stop()
        self.mock_dnac_exec.stop()

    def load_fixtures(self, response=None, device=""):
        print("Inside load_fixtures")
        # FIXTURE FOR SUCCESS TESTCASES ############################################################

        # Add Port Assignments
        if "add_port_assignments" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("response_get_device_list"),
                self.test_data.get("response_get_sites"),
                self.test_data.get("response_get_fabric_sites"),
                self.test_data.get("response_get_device_list"),
                self.test_data.get("response_get_device_info"),
                self.test_data.get("response_get_port_assignments"),
                self.test_data.get("response_get_task_id"),
                self.test_data.get("response_get_task_status_by_id"),
                self.test_data.get("response_get_port_assignments_2")
            ]

        # Update Port Assignments
        if "update_port_assignments" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("response_get_device_list"),
                self.test_data.get("response_get_sites"),
                self.test_data.get("response_get_fabric_sites"),
                self.test_data.get("response_get_device_list"),
                self.test_data.get("response_get_device_info"),
                self.test_data.get("response_get_port_assignments_3"),
                self.test_data.get("response_get_task_id"),
                self.test_data.get("response_get_task_status_by_id"),
                self.test_data.get("response_get_port_assignments_4")
            ]

        # Delete Port Assignments
        if "delete_port_assignments" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("response_get_device_list"),
                self.test_data.get("response_get_sites"),
                self.test_data.get("response_get_fabric_sites"),
                self.test_data.get("response_get_device_list"),
                self.test_data.get("response_get_device_info"),
                self.test_data.get("response_get_port_assignments_5"),
                self.test_data.get("response_get_port_assignments_6"),
                self.test_data.get("response_get_task_id"),
                self.test_data.get("response_get_task_status_by_id"),
                self.test_data.get("response_get_task_id"),
                self.test_data.get("response_get_task_status_by_id"),
                self.test_data.get("response_get_port_assignments")
            ]

        # Add Port Channels
        if "add_port_channels" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("response_get_device_list"),
                self.test_data.get("response_get_sites"),
                self.test_data.get("response_get_fabric_sites"),
                self.test_data.get("response_get_device_list"),
                self.test_data.get("response_get_device_info"),
                self.test_data.get("response_get_port_channels"),
                self.test_data.get("response_get_task_id"),
                self.test_data.get("response_get_task_status_by_id"),
                self.test_data.get("response_get_port_channels_2"),
                self.test_data.get("response_get_port_channels_2")
            ]

        # Update Port Channels
        if "update_port_channels" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("response_get_device_list"),
                self.test_data.get("response_get_sites"),
                self.test_data.get("response_get_fabric_sites"),
                self.test_data.get("response_get_device_list"),
                self.test_data.get("response_get_device_info"),
                self.test_data.get("response_get_port_channels_2"),
                self.test_data.get("response_get_task_id"),
                self.test_data.get("response_get_task_status_by_id"),
                self.test_data.get("response_get_port_channels_3"),
            ]

        # Delete Port Channels
        if "delete_port_channels" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("response_get_device_list"),
                self.test_data.get("response_get_sites"),
                self.test_data.get("response_get_fabric_sites"),
                self.test_data.get("response_get_device_list"),
                self.test_data.get("response_get_device_info"),
                self.test_data.get("response_get_port_channels_3"),
                self.test_data.get("response_get_task_id"),
                self.test_data.get("response_get_task_status_by_id"),
                self.test_data.get("response_get_task_id"),
                self.test_data.get("response_get_task_status_by_id"),
                self.test_data.get("response_get_task_id"),
                self.test_data.get("response_get_task_status_by_id"),
                self.test_data.get("response_get_task_id"),
                self.test_data.get("response_get_task_status_by_id"),
                self.test_data.get("response_get_port_channels"),
                self.test_data.get("response_get_port_channels"),
                self.test_data.get("response_get_port_channels"),
                self.test_data.get("response_get_port_channels"),
            ]

        # Add SSIDs
        if "add_ssids" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("response_get_sites"),
                self.test_data.get("response_get_fabric_sites"),
                self.test_data.get("response_get_wireless_ssids"),
                self.test_data.get("response_get_task_id"),
                self.test_data.get("response_get_task_status_by_id"),
                self.test_data.get("response_get_wireless_ssids_2")
            ]

        # Update SSIDs
        if "update_ssids" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("response_get_sites"),
                self.test_data.get("response_get_fabric_sites"),
                self.test_data.get("response_get_wireless_ssids_2"),
                self.test_data.get("response_get_task_id"),
                self.test_data.get("response_get_task_status_by_id"),
                self.test_data.get("response_get_wireless_ssids_3"),
            ]

        # Delete SSIDs
        if "delete_ssids" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("response_get_sites"),
                self.test_data.get("response_get_fabric_sites"),
                self.test_data.get("response_get_wireless_ssids_3"),
                self.test_data.get("response_get_task_id"),
                self.test_data.get("response_get_task_status_by_id"),
                self.test_data.get("response_get_wireless_ssids_4"),
            ]

        # Add SSIDs
        if "test_add_all_hosts" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("response_get_device_list"),
                self.test_data.get("response_get_sites"),
                self.test_data.get("response_get_fabric_sites"),
                self.test_data.get("response_get_device_list"),
                self.test_data.get("response_get_device_info"),
                self.test_data.get("response_get_port_assignments"),
                self.test_data.get("response_get_port_channels"),
                self.test_data.get("response_get_wireless_ssids"),
                self.test_data.get("response_get_task_id"),
                self.test_data.get("response_get_task_status_by_id"),
                self.test_data.get("response_get_task_id"),
                self.test_data.get("response_get_task_status_by_id"),
                self.test_data.get("response_get_port_channels_2"),
                self.test_data.get("response_get_task_id"),
                self.test_data.get("response_get_task_status_by_id"),
                self.test_data.get("response_get_port_assignments_2"),
                self.test_data.get("response_get_port_channels_2"),
                self.test_data.get("response_get_wireless_ssids_2")
            ]

        # Update SSIDs
        if "test_update_all_hosts" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("response_get_device_list"),
                self.test_data.get("response_get_sites"),
                self.test_data.get("response_get_fabric_sites"),
                self.test_data.get("response_get_device_list"),
                self.test_data.get("response_get_device_info"),
                self.test_data.get("response_get_port_assignments_3"),
                self.test_data.get("response_get_port_channels_2"),
                self.test_data.get("response_get_wireless_ssids_2"),
                self.test_data.get("response_get_task_id"),
                self.test_data.get("response_get_task_status_by_id"),
                self.test_data.get("response_get_task_id"),
                self.test_data.get("response_get_task_status_by_id"),
                self.test_data.get("response_get_task_id"),
                self.test_data.get("response_get_task_status_by_id"),
                self.test_data.get("response_get_port_assignments_4"),
                self.test_data.get("response_get_port_channels_3"),
                self.test_data.get("response_get_wireless_ssids_3"),
            ]

        # Delete SSIDs
        if "test_delete_all_hosts" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("response_get_device_list"),
                self.test_data.get("response_get_sites"),
                self.test_data.get("response_get_fabric_sites"),
                self.test_data.get("response_get_device_list"),
                self.test_data.get("response_get_device_info"),
                self.test_data.get("response_get_port_assignments_5"),
                self.test_data.get("response_get_port_assignments_6"),
                self.test_data.get("response_get_port_channels_3"),
                self.test_data.get("response_get_wireless_ssids_3"),
                self.test_data.get("response_get_task_id"),
                self.test_data.get("response_get_task_status_by_id"),
                self.test_data.get("response_get_task_id"),
                self.test_data.get("response_get_task_status_by_id"),
                self.test_data.get("response_get_task_id"),
                self.test_data.get("response_get_task_status_by_id"),
                self.test_data.get("response_get_task_id"),
                self.test_data.get("response_get_task_status_by_id"),
                self.test_data.get("response_get_task_id"),
                self.test_data.get("response_get_task_status_by_id"),
                self.test_data.get("response_get_task_id"),
                self.test_data.get("response_get_task_status_by_id"),
                self.test_data.get("response_get_task_id"),
                self.test_data.get("response_get_task_status_by_id"),
                self.test_data.get("response_get_port_assignments"),
                self.test_data.get("response_get_port_channels"),
                self.test_data.get("response_get_port_channels"),
                self.test_data.get("response_get_port_channels"),
                self.test_data.get("response_get_port_channels"),
                self.test_data.get("response_get_wireless_ssids_4"),
            ]

# SUCCESS TESTCASES ########################################################################################

    # Add Port Assignments
    def test_add_port_assignments(self):
        print("Test Data: {test_data}".format(test_data=self.test_data.get("playbook_config_add_port_assignments")))

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
                config=self.test_data.get("playbook_config_add_port_assignments")
            )
        )
        result = self.execute_module(changed=True, failed=False)
        self.assertIn(
            "Add Port Assignment(s) Task Succeeded for following interface(s)",
            result.get('msg')
        )

    # Update Port Assignments
    def test_update_port_assignments(self):
        print("Test Data: {test_data}".format(test_data=self.test_data.get("playbook_config_update_port_assignments")))

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
                config=self.test_data.get("playbook_config_update_port_assignments")
            )
        )
        result = self.execute_module(changed=True, failed=False)
        self.assertIn(
            "Update Port Assignment(s) Task Succeeded for following interface(s)",
            result.get('msg')
        )

    # Delete Port Assignments
    def test_delete_port_assignments(self):
        print("Test Data: {test_data}".format(test_data=self.test_data.get("playbook_config_delete_port_assignments")))

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
                config=self.test_data.get("playbook_config_delete_port_assignments")
            )
        )
        result = self.execute_module(changed=True, failed=False)
        self.assertIn(
            "Delete Port Assignment(s) Task Succeeded for following interface(s)",
            result.get('msg')
        )

    # Add Port Channels
    def test_add_port_channels(self):
        print("Test Data: {test_data}".format(test_data=self.test_data.get("playbook_config_add_port_channels")))

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
                dnac_log_file_path="dnac.log",
                state="merged",
                config=self.test_data.get("playbook_config_add_port_channels")
            )
        )
        result = self.execute_module(changed=True, failed=False)
        self.assertIn(
            "Add Port Channel(s) Task Succeeded for following port channel(s)",
            result.get('msg')
        )

    # Update Port Channels
    def test_update_port_channels(self):
        print("Test Data: {test_data}".format(test_data=self.test_data.get("playbook_config_update_port_channels")))

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
                dnac_log_file_path="dnac.log",
                state="merged",
                config=self.test_data.get("playbook_config_update_port_channels")
            )
        )
        result = self.execute_module(changed=True, failed=False)
        self.assertIn(
            "Update Port Channel(s) Task Succeeded for following port channel(s)",
            result.get('msg')
        )

    # Delete Port Channels
    def test_delete_port_channels(self):
        print("Test Data: {test_data}".format(test_data=self.test_data.get("playbook_config_delete_port_channels")))

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
                config=self.test_data.get("playbook_config_delete_port_channels")
            )
        )
        result = self.execute_module(changed=True, failed=False)
        self.assertIn(
            "Delete Port Channel(s) Task Succeeded for following port channel(s)",
            result.get('msg')
        )

    # Add SSIDs
    def test_add_ssids(self):
        print("Test Data: {test_data}".format(test_data=self.test_data.get("playbook_config_add_ssids")))

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
                config=self.test_data.get("playbook_config_add_ssids")
            )
        )
        result = self.execute_module(changed=True, failed=False)
        self.assertIn(
            "Create VLANs and SSIDs Mapped to VLANs Task Succeeded for following VLAN(s) and SSID(s)",
            result.get('msg')
        )

    # Update SSIDs
    def test_update_ssids(self):
        print("Test Data: {test_data}".format(test_data=self.test_data.get("playbook_config_update_ssids")))

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
                config=self.test_data.get("playbook_config_update_ssids")
            )
        )
        result = self.execute_module(changed=True, failed=False)
        self.assertIn(
            "Update VLANs and SSIDs Mapped to VLANs Task Succeeded for following VLAN(s) and SSID(s)",
            result.get('msg')
        )

    # Delete SSIDs
    def test_delete_ssids(self):
        print("Test Data: {test_data}".format(test_data=self.test_data.get("playbook_config_delete_ssids")))

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
                config=self.test_data.get("playbook_config_delete_ssids")
            )
        )
        result = self.execute_module(changed=True, failed=False)
        self.assertIn(
            "Delete VLAN(s) and SSID(s) Mapped to VLAN(s) Task Succeeded for following VLAN(s) and SSID(s)",
            result.get('msg')
        )

    # Add ALL
    def test_add_all_hosts(self):
        print("Test Data: {test_data}".format(test_data=self.test_data.get("playbook_config_add_all_hosts")))

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
                config=self.test_data.get("playbook_config_add_all_hosts")
            )
        )
        expected_messages = [
            "Add Port Assignment(s) Task Succeeded for following interface(s)",
            "Add Port Channel(s) Task Succeeded for following port channel(s)",
            "Create VLANs and SSIDs Mapped to VLANs Task Succeeded for following VLAN(s) and SSID(s)",
        ]
        result = self.execute_module(changed=True, failed=False)
        for expected_message in expected_messages:
            with self.subTest(expected_message=expected_message):
                self.assertIn(expected_message, result.get('msg'))

    # # Update ALL
    # def test_update_all_hosts(self):
    #     print("Test Data: {test_data}".format(test_data=self.test_data.get("playbook_config_update_all_hosts")))

    #     set_module_args(
    #         dict(
    #             dnac_host="1.1.1.1",
    #             dnac_username="dummy",
    #             dnac_password="dummy",
    #             dnac_log=False,
    #             dnac_log_level="DEBUG",
    #             dnac_version="2.3.7.9",
    #             config_verify=True,
    #             dnac_log_append=False,
    #             state="merged",
    #             config=self.test_data.get("playbook_config_update_all_hosts")
    #         )
    #     )
    #     expected_messages = [
    #         "Update Port Assignment(s) Task Succeeded for following interface(s)",
    #         "Update Port Channel(s) Task Succeeded for following port channel(s)",
    #         "Update VLANs and SSIDs Mapped to VLANs Task Succeeded for following VLAN(s) and SSID(s)",
    #     ]
    #     result = self.execute_module(changed=True, failed=False)
    #     for expected_message in expected_messages:
    #         with self.subTest(expected_message=expected_message):
    #             self.assertIn(expected_message, result.get('msg'))

    # Delete ALL
    def test_delete_all_hosts(self):
        print("Test Data: {test_data}".format(test_data=self.test_data.get("playbook_config_delete_all_hosts")))

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
                config=self.test_data.get("playbook_config_delete_all_hosts")
            )
        )

        expected_messages = [
            "Delete Port Assignment(s) Task Succeeded for following interface(s)",
            "Delete Port Channel(s) Task Succeeded for following port channel(s)",
            "Delete VLAN(s) and SSID(s) Mapped to VLAN(s) Task Succeeded for following VLAN(s) and SSID(s)"
        ]
        result = self.execute_module(changed=True, failed=False)
        for expected_message in expected_messages:
            with self.subTest(expected_message=expected_message):
                self.assertIn(expected_message, result.get('msg'))
