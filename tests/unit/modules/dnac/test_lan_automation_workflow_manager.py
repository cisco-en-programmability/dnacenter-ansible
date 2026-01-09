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

# Authors:
#   Archit Soni <soni.archit03@gmail.com>
#
# Description:
#   Unit tests for the Ansible module `lan_automation_workflow_manager`.
#   These tests cover various LAN automation operations using mocked Catalyst Center responses.


from __future__ import absolute_import, division, print_function

# Metadata
__metaclass__ = type
__author__ = "Archit Soni"
__email__ = "soni.archit03@gmail.com"
__version__ = "1.0.0"

from unittest.mock import patch
from ansible_collections.cisco.dnac.plugins.modules import (
    lan_automation_workflow_manager,
)
from .dnac_module import TestDnacModule, set_module_args, loadPlaybookData


class TestDnacLanAutomationWorkflow(TestDnacModule):

    module = lan_automation_workflow_manager
    test_data = loadPlaybookData("lan_automation_workflow_manager")

    playbook_config_delete_port_channel_when_it_doesnot_exist_case_1 = test_data.get(
        "delete_port_channel_when_it_doesnot_exist_playbook_case_1"
    )
    playbook_config_create_port_channel_playbook_case_2 = test_data.get(
        "create_port_channel_playbook_case_2"
    )
    playbook_config_create_second_port_channel_playbook_case_3 = test_data.get(
        "create_second_port_channel_playbook_case_3"
    )
    playbook_config_delete_port_channel_negative_playbook_case_4 = test_data.get(
        "delete_port_channel_negative_playbook_case_4"
    )
    playbook_config_delete_second_port_channel_playbook_case_5 = test_data.get(
        "delete_second_port_channel_playbook_case_5"
    )
    playbook_config_add_links_to_first_port_channel_playbook_case_6 = test_data.get(
        "add_links_to_first_port_channel_playbook_case_6"
    )
    playbook_config_remove_link_from_port_channel_playbook_case_7 = test_data.get(
        "remove_link_from_port_channel_playbook_case_7"
    )
    playbook_config_create_port_channel_negative_testcase_playbook_case_8 = (
        test_data.get("create_port_channel_negative_testcase_playbook_case_8")
    )
    playbook_config_update_port_channel_negative_testcase_playbook_case_9 = (
        test_data.get("update_port_channel_negative_testcase_playbook_case_9")
    )
    playbook_config_add_link_to_port_channel_when_the_order_of_source_and_destination_device_is_reversed_case_10 = test_data.get(
        "add_link_to_port_channel_when_the_order_of_source_and_destination_device_is_reversed_case_10"
    )

    def setUp(self):
        super(TestDnacLanAutomationWorkflow, self).setUp()

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
        super(TestDnacLanAutomationWorkflow, self).tearDown()
        self.mock_dnac_exec.stop()
        self.mock_dnac_init.stop()

    def load_fixtures(self, response=None, device=""):
        """
        Load fixtures for user.
        """
        if "invalid_delete_config" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                # self.test_data.get(""),
            ]
        elif (
            "test_delete_port_channel_when_it_doesnot_exist_case_1"
            in self._testMethodName
        ):
            self.run_dnac_exec.side_effect = [
                self.test_data.get("get_device_list_call_1_case_1"),
                self.test_data.get("get_active_lan_automation_sessions_call_1_case_1"),
                self.test_data.get("get_lan_automation_status_call_1_case_1"),
                self.test_data.get("get_port_channel_call_1_case_1"),
                self.test_data.get("get_active_lan_automation_sessions_call_1_case_1"),
                self.test_data.get("get_lan_automation_status_call_1_case_1"),
                self.test_data.get("get_port_channel_call_1_case_1"),
            ]
        elif "test_create_port_channel_playbook_case_2" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("get_device_list_call_1_case_2"),
                self.test_data.get("get_device_list_call_2_case_2"),
                self.test_data.get("get_lan_automation_status_call_1_case_2"),
                self.test_data.get("get_active_lan_automation_sessions_call_1_case_2"),
                self.test_data.get("get_port_channel_call_1_case_2"),
                self.test_data.get(
                    "create_a_new_port_channel_between_devices_call_1_case_2"
                ),
                self.test_data.get("get_tasks_by_id_call_1_case_2"),
                self.test_data.get("get_lan_automation_status_call_1_case_2"),
                self.test_data.get("get_active_lan_automation_sessions_call_1_case_2"),
                self.test_data.get("get_port_channel_call_2_case_2"),
            ]
        elif "test_create_second_port_channel_playbook_case_3" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("get_device_list_call_1_case_3"),
                self.test_data.get("get_device_list_call_2_case_3"),
                self.test_data.get("get_lan_automation_status_call_1_case_3"),
                self.test_data.get("get_active_lan_automation_sessions_call_1_case_3"),
                self.test_data.get("get_port_channel_call_1_case_3"),
                self.test_data.get(
                    "create_a_new_port_channel_between_devices_call_1_case_3"
                ),
                self.test_data.get("get_tasks_by_id_call_1_case_3"),
                self.test_data.get("get_lan_automation_status_call_1_case_3"),
                self.test_data.get("get_active_lan_automation_sessions_call_1_case_3"),
                self.test_data.get("get_port_channel_call_2_case_3"),
            ]
        elif (
            "test_delete_port_channel_negative_playbook_case_4" in self._testMethodName
        ):
            self.run_dnac_exec.side_effect = [
                self.test_data.get("get_device_list_call_1_case_4"),
            ]
        elif "test_delete_second_port_channel_playbook_case_5" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("get_device_list_call_1_case_5"),
                self.test_data.get("get_device_list_call_2_case_5"),
                self.test_data.get("get_lan_automation_status_call_1_case_5"),
                self.test_data.get("get_active_lan_automation_sessions_call_1_case_5"),
                self.test_data.get("get_port_channel_call_1_case_5"),
                self.test_data.get("delete_port_channel_call_1_case_5"),
                self.test_data.get("get_tasks_by_id_call_1_case_5"),
                self.test_data.get("get_lan_automation_status_call_1_case_5"),
                self.test_data.get("get_active_lan_automation_sessions_call_1_case_5"),
                self.test_data.get("get_port_channel_call_2_case_5"),
            ]
        elif (
            "test_add_links_to_first_port_channel_playbook_case_6"
            in self._testMethodName
        ):
            self.run_dnac_exec.side_effect = [
                self.test_data.get("get_device_list_call_1_case_6"),
                self.test_data.get("get_device_list_call_2_case_6"),
                self.test_data.get("get_lan_automation_status_call_1_case_6"),
                self.test_data.get("get_active_lan_automation_sessions_call_1_case_6"),
                self.test_data.get("get_port_channel_call_1_case_6"),
                self.test_data.get("get_port_channel_information_by_id_call_1_case_6"),
                self.test_data.get("add_links_to_port_channel_call_1_case_6"),
                self.test_data.get("get_tasks_by_id_call_1_case_6"),
                self.test_data.get("get_lan_automation_status_call_1_case_6"),
                self.test_data.get("get_active_lan_automation_sessions_call_1_case_6"),
                self.test_data.get("get_port_channel_call_2_case_6"),
            ]
        elif "remove_link_from_port_channel_playbook_case_7" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("get_device_list_call_1_case_7"),
                self.test_data.get("get_device_list_call_2_case_7"),
                self.test_data.get("get_lan_automation_status_call_1_case_7"),
                self.test_data.get("get_active_lan_automation_sessions_call_1_case_7"),
                self.test_data.get("get_port_channel_call_1_case_7"),
                self.test_data.get("get_port_channel_information_by_id_call_1_case_7"),
                self.test_data.get("remove_a_link_from_port_channel_case_7"),
                self.test_data.get("get_tasks_by_id_call_1_case_7"),
                self.test_data.get("get_lan_automation_status_call_1_case_7"),
                self.test_data.get("get_active_lan_automation_sessions_call_1_case_7"),
                self.test_data.get("get_port_channel_call_2_case_7"),
            ]
        elif (
            "create_port_channel_negative_testcase_playbook_case_8"
            in self._testMethodName
        ):
            self.run_dnac_exec.side_effect = [
                self.test_data.get("get_device_list_call_1_case_8"),
                self.test_data.get("get_device_list_call_2_case_8"),
            ]
        elif (
            "update_port_channel_negative_testcase_playbook_case_9"
            in self._testMethodName
        ):
            self.run_dnac_exec.side_effect = [
                self.test_data.get("get_device_list_call_1_case_9"),
                self.test_data.get("get_device_list_call_2_case_9"),
                self.test_data.get("get_lan_automation_status_call_1_case_9"),
                self.test_data.get("get_active_lan_automation_sessions_call_1_case_9"),
                self.test_data.get("get_port_channel_call_1_case_9"),
            ]
        elif (
            "add_link_to_port_channel_when_the_order_of_source_and_destination_device_is_reversed_case_10"
            in self._testMethodName
        ):
            self.run_dnac_exec.side_effect = [
                self.test_data.get("get_device_list_call_1_case_10"),
                self.test_data.get("get_device_list_call_2_case_10"),
                self.test_data.get("get_lan_automation_status_call_1_case_10"),
                self.test_data.get("get_active_lan_automation_sessions_call_1_case_10"),
                self.test_data.get("get_port_channel_call_1_case_10"),
                self.test_data.get("get_port_channel_information_by_id_call_1_case_10"),
                self.test_data.get("add_a_link_to_port_channel_case_10"),
                self.test_data.get("get_tasks_by_id_call_1_case_10"),
                self.test_data.get("get_lan_automation_status_call_1_case_10"),
                self.test_data.get("get_active_lan_automation_sessions_call_1_case_10"),
                self.test_data.get("get_port_channel_call_2_case_10"),
            ]

    def test_delete_port_channel_when_it_doesnot_exist_case_1(self):
        #  Test Description: Delete port channel when it does not exist between source and destination device.
        #  Expected Result: No change required as port channel does not exist between source and destination
        set_module_args(
            dict(
                dnac_host="1.1.1.1",
                dnac_username="dummy",
                dnac_password="dummy",
                dnac_version="3.1.3.0",
                dnac_log=True,
                state="deleted",
                config_verify=True,
                dnac_log_level="DEBUG",
                config=self.playbook_config_delete_port_channel_when_it_doesnot_exist_case_1,
            )
        )
        result = self.execute_module(changed=False, failed=False)
        self.assertEqual(
            result.get("msg"),
            "No port channel found to delete between source device '172.255.0.64' and destination device 'None' with links: null. No update needed.",
        )

    def test_create_port_channel_playbook_case_2(self):
        #  Test Description: Create port channel between source and destination device when no port channel exists before.
        #  Expected Result: Port channel created successfully between source and destination device.
        set_module_args(
            dict(
                dnac_host="1.1.1.1",
                dnac_username="dummy",
                dnac_password="dummy",
                dnac_version="3.1.3.0",
                dnac_log=True,
                state="merged",
                config_verify=True,
                dnac_log_level="DEBUG",
                config=self.playbook_config_create_port_channel_playbook_case_2,
            )
        )
        result = self.execute_module(changed=True, failed=False)
        self.assertIn(
            "Port channel created successfully between source device '172.255.0.64' and destination device '172.101.1.1'",
            result.get("msg"),
        )

    def test_create_second_port_channel_playbook_case_3(self):
        # Test Description: Create second port channel between source and destination device when one port channel already exists.
        # Expected Result: Second port channel created successfully between source and destination device.
        set_module_args(
            dict(
                dnac_host="1.1.1.1",
                dnac_username="dummy",
                dnac_password="dummy",
                dnac_version="3.1.3.0",
                dnac_log=True,
                state="merged",
                config_verify=True,
                dnac_log_level="DEBUG",
                config=self.playbook_config_create_second_port_channel_playbook_case_3,
            )
        )
        result = self.execute_module(changed=True, failed=False)
        self.assertIn(
            "Port channel created successfully between source device '172.255.0.64' and destination device '172.101.1.1'",
            result.get("msg"),
        )

    def test_delete_port_channel_negative_playbook_case_4(self):
        # Test Description: Negative test case for port channel deletion. Source device is not provided.
        # Expected Result: Fail the module with appropriate error message.
        set_module_args(
            dict(
                dnac_host="1.1.1.1",
                dnac_username="dummy",
                dnac_password="dummy",
                dnac_version="3.1.3.0",
                dnac_log=True,
                state="deleted",
                config_verify=True,
                dnac_log_level="DEBUG",
                config=self.playbook_config_delete_port_channel_negative_playbook_case_4,
            )
        )
        result = self.execute_module(changed=False, failed=True)
        self.assertEqual(
            result.get("msg"),
            "The following required parameters are missing or invalid: Configuration 1: Missing source device identifiers "
            "- at least one of 'source_device_management_ip_address', 'source_device_management_mac_address' or "
            "'source_device_management_serial_number' is required",
        )

    def test_delete_second_port_channel_playbook_case_5(self):
        # Test Description: Delete second port channel between source and destination device.
        # Expected Result: Fail the module with appropriate error message.
        set_module_args(
            dict(
                dnac_host="1.1.1.1",
                dnac_username="dummy",
                dnac_password="dummy",
                dnac_version="3.1.3.0",
                dnac_log=True,
                state="deleted",
                config_verify=True,
                dnac_log_level="DEBUG",
                config=self.playbook_config_delete_second_port_channel_playbook_case_5,
            )
        )
        result = self.execute_module(changed=True, failed=False)
        self.assertIn(
            "Port channel deleted successfully between source device '172.255.0.64' and destination device '172.101.1.1' with links:",
            result.get("msg"),
        )

    def test_add_links_to_first_port_channel_playbook_case_6(self):
        # Test Description: Add links to the first port channel between source and destination device.
        # Expected Result: Links added successfully to the existing port channel.
        set_module_args(
            dict(
                dnac_host="1.1.1.1",
                dnac_username="dummy",
                dnac_password="dummy",
                dnac_version="3.1.3.0",
                dnac_log=True,
                state="merged",
                config_verify=True,
                dnac_log_level="DEBUG",
                config=self.playbook_config_add_links_to_first_port_channel_playbook_case_6,
            )
        )
        result = self.execute_module(changed=True, failed=False)
        self.assertIn(
            "Links added successfully to the port channel between source device '172.255.0.64' and destination device '172.101.1.1'. Added links:",
            result.get("msg"),
        )

    def test_remove_link_from_port_channel_playbook_case_7(self):
        # Test Description: Remove link from port channel between source and destination device.
        # Expected Result: Link removed successfully from the existing port channel.
        set_module_args(
            dict(
                dnac_host="1.1.1.1",
                dnac_username="dummy",
                dnac_password="dummy",
                dnac_version="3.1.3.0",
                dnac_log=True,
                state="deleted",
                config_verify=True,
                dnac_log_level="DEBUG",
                config=self.playbook_config_remove_link_from_port_channel_playbook_case_7,
            )
        )
        result = self.execute_module(changed=True, failed=False)
        self.assertIn(
            "Links removed successfully from the port channel between source device '172.255.0.64' and destination device '172.101.1.1'. Removed links:",
            result.get("msg"),
        )

    def test_create_port_channel_negative_testcase_playbook_case_8(self):
        # Test Description: Create port channel between source and destination device without specifying links in merged state, Invalid case.
        # Expected Result: Module should fail with appropriate error message indicating links are required for merged state.
        set_module_args(
            dict(
                dnac_host="1.1.1.1",
                dnac_username="dummy",
                dnac_password="dummy",
                dnac_version="3.1.3.0",
                dnac_log=True,
                state="merged",
                config_verify=True,
                dnac_log_level="DEBUG",
                config=self.playbook_config_create_port_channel_negative_testcase_playbook_case_8,
            )
        )
        result = self.execute_module(changed=False, failed=True)
        self.assertIn(
            "Missing links parameter for merged state - at least one link must be specified",
            result.get("msg"),
        )

    def test_update_port_channel_negative_testcase_playbook_case_9(self):
        # Test Description: Update port channel by specifying port_channel_number that does not exist.
        # Expected Result: Module should fail with appropriate error message indicating the port channel
        # number does not exist and suggesting to remove the parameter to create a new port channel.
        set_module_args(
            dict(
                dnac_host="1.1.1.1",
                dnac_username="dummy",
                dnac_password="dummy",
                dnac_version="3.1.3.0",
                dnac_log=True,
                state="merged",
                config_verify=True,
                dnac_log_level="DEBUG",
                config=self.playbook_config_update_port_channel_negative_testcase_playbook_case_9,
            )
        )
        result = self.execute_module(changed=False, failed=True)
        self.assertIn(
            "No existing Port Channel configuration found with the provided "
            "port_channel_number: 11. When both port_channel_number and links "
            "are specified, an existing Port Channel is expected for update. "
            "If you want to create a new Port Channel, please remove the "
            "port_channel_number parameter from your playbook configuration "
            "and try again.",
            result.get("msg"),
        )

    def add_link_to_port_channel_when_the_order_of_source_and_destination_device_is_reversed_case_10(
        self,
    ):
        # Test Description: Add link to port channel when the order of source and destination devices
        # is reversed compared to the Catalyst Center configuration. The module should automatically
        # detect the reversed order and swap the interface assignments before calling the API.
        # Expected Result: Module should successfully add links to the port channel by automatically
        # swapping device1Interface and device2Interface to match the Catalyst Center port channel configuration.
        set_module_args(
            dict(
                dnac_host="1.1.1.1",
                dnac_username="dummy",
                dnac_password="dummy",
                dnac_version="3.1.3.0",
                dnac_log=True,
                state="merged",
                config_verify=True,
                dnac_log_level="DEBUG",
                config=self.playbook_config_add_link_to_port_channel_when_the_order_of_source_and_destination_device_is_reversed_case_10,
            )
        )
        result = self.execute_module(changed=True, failed=False)
        self.assertIn(
            "Links added successfully to the port channel between source device '172.254.0.2' and destination device '172.101.1.1'. Added links:",
            result.get("msg"),
        )
