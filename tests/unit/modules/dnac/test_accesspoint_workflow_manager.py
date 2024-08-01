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
from ansible_collections.cisco.dnac.plugins.modules import accesspoint_workflow_manager
from .dnac_module import TestDnacModule, set_module_args, loadPlaybookData


class TestDnacAccesspointWorkflow(TestDnacModule):

    module = accesspoint_workflow_manager

    test_data = loadPlaybookData("accesspoint_workflow_manager")
    playbook_config_series_error = test_data.get("playbook_config_series_error")
    playbook_config = test_data.get("playbook_config")
    playbook_config_provision = test_data.get("playbook_config_provision")
    playbook_config_missing_rf_profile = test_data.get("playbook_config_missing_rf_profile")
    playbook_config_missing_update = test_data.get("playbook_config_missing_update")
    get_membership_empty = test_data.get("get_membership_empty")
    playbook_invalid_config_provision = test_data.get("playbook_invalid_config_provision")
    get_device_detail_all_data = test_data.get("get_device_detail_all_data")
    playbook_config_update_some_missing_data = test_data.get("playbook_config_update_some_missing_data")

    def setUp(self):
        super(TestDnacAccesspointWorkflow, self).setUp()

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
        super(TestDnacAccesspointWorkflow, self).tearDown()
        self.mock_dnac_exec.stop()
        self.mock_dnac_init.stop()

    def load_fixtures(self, response=None, device=""):
        """
        Load fixtures for user.
        """
        if "already_provision_device" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("get_device_detail"),
                self.test_data.get("get_site_exist_response"),
                self.test_data.get("get_membership"),
                self.test_data.get("verify_get_device_info"),
                self.test_data.get("get_accesspoint_config"),
                self.test_data.get("provision_ap_response")
            ]
        elif "provision_device" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("get_device_detail"),
                self.test_data.get("get_site_exist_response"),
                self.test_data.get("get_membership_empty"),
                self.test_data.get("verify_get_device_info"),
                self.test_data.get("get_accesspoint_config"),
                self.test_data.get("provision_ap_response"),
                self.test_data.get("provision_execution_response")
            ]
        elif "update_accesspoint_series_error" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("get_device_detail_series_error"),
                self.test_data.get("get_site_exist_response"),
                self.test_data.get("get_membership_empty"),
                self.test_data.get("verify_get_device_info"),
                self.test_data.get("get_accesspoint_config"),
                self.test_data.get("provision_ap_response"),
                self.test_data.get("ap_update_response"),
                self.test_data.get("ap_task_status")
            ]
        elif "task_error_update_accesspoint" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("get_device_detail_all_data"),
                self.test_data.get("get_accesspoint_config"),
                self.test_data.get("ap_update_response"),
                self.test_data.get("ap_task_error_status")
            ]
        elif "task_no_error_update_accesspoint" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("get_device_detail_all_data"),
                self.test_data.get("get_accesspoint_config"),
                self.test_data.get("ap_update_response"),
                self.test_data.get("ap_task_status")
            ]
        elif "update_accesspoint" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("get_device_detail_all_data"),
                self.test_data.get("get_accesspoint_config"),
                self.test_data.get("ap_update_response"),
                self.test_data.get("ap_task_status")
            ]
        elif "site_exists" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("get_site_exist_response"),
            ]
        elif "invalid_get_site_device" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("get_membership_empty"),
            ]
        elif "check_verify_diff_merged" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("get_device_detail_all_data"),
                self.test_data.get("get_accesspoint_config"),
                self.test_data.get("ap_update_response"),
                self.test_data.get("ap_task_status"),
                self.test_data.get("ap_update_status"),
            ]
        elif "invalid_wlc_device" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("get_device_detail"),
                self.test_data.get("get_site_exist_response"),
                self.test_data.get("get_membership_empty"),
                Exception(),
            ]

    def test_accesspoint_workflow_manager_update_accesspoint_series_error(self):
        """
        Test case for user role workflow manager when creating a user.

        This test case checks the behavior of the user workflow when creating a new user in the specified Cisco Catalyst Center.
        """
        set_module_args(
            dict(
                dnac_host="1.1.1.1",
                dnac_username="dummy",
                dnac_password="dummy",
                dnac_log=True,
                state="merged",
                config=self.playbook_config_series_error
            )
        )
        result = self.execute_module(changed=False, failed=True)
        self.assertEqual(
            result.get('msg'),
            "Successfully validated config params: {'mac_address': '90:e9:5e:03:f3:40', 'management_ip_address': None, 'hostname': None, 'rf_profile': " +
            "'HIGH', 'site': {'floor': {'name': 'FLOOR2', 'parent_name': 'Global/USA/New York/BLDNYC'}}, 'type': None, 'ap_name': 'LTTS-test1', " +
            "'admin_status': None, 'led_status': 'Enabled', 'led_brightness_level': 5, 'ap_mode': 'Local', 'location': 'LTTS/Cisco/Chennai', " +
            "'failover_priority': 'Low', 'primary_controller_name': None, 'primary_ip_address': None, 'secondary_controller_name': None, " +
            "'secondary_ip_address': None, 'tertiary_controller_name': None, 'tertiary_ip_address': None, 'clean_air_si_2.4ghz': 'Enabled', " +
            "'clean_air_si_5ghz': 'Enabled', 'clean_air_si_6ghz': 'Disabled', '2.4ghz_radio': {'admin_status': 'Enabled', 'antenna_name': " +
            "'C-ANT9104-2.4GHz', 'radio_role_assignment': 'Client-Serving', 'channel_number': 2, 'powerlevel': 2, 'radio_type': 1}, '5ghz_radio': " +
            "{'admin_status': 'Enabled', 'antenna_name': 'AIR-ANT2513P4M-N-5GHz', 'radio_role_assignment': 'Client-Serving', 'channel_number': 44, " +
            "'powerlevel': 2, 'channel_width': '20 MHz', 'radio_type': 2}, '6ghz_radio': None, 'xor_radio': None, 'tri_radio': None, 'ap_selected_fields': " +
            "'id,hostname,family,type,mac_address,management_ip_address,ap_ethernet_mac_address', 'ap_config_selected_fields': " +
            "'mac_address,eth_mac,ap_name,led_brightness_level,led_status,location,radioDTOs'}"
        )

    def test_accesspoint_workflow_manager_task_error_update_accesspoint(self):
        """
        Test case for user role workflow manager when creating a user.

        This test case checks the behavior of the user workflow when creating a new user in the specified Cisco Catalyst Center.
        """
        set_module_args(
            dict(
                dnac_host="1.1.1.1",
                dnac_username="dummy",
                dnac_password="dummy",
                dnac_log=True,
                state="merged",
                config=self.playbook_config
            )
        )
        result = self.execute_module(changed=False, failed=True)
        self.assertEqual(
            result.get('msg'),
            "Unable to get success response, hence AP config not updated"
        )

    def test_accesspoint_workflow_manager_task_no_error_update_accesspoint(self):
        """
        Test case for user role workflow manager when creating a user.

        This test case checks the behavior of the user workflow when creating a new user in the specified Cisco Catalyst Center.
        """
        set_module_args(
            dict(
                dnac_host="1.1.1.1",
                dnac_username="dummy",
                dnac_password="dummy",
                dnac_log=True,
                state="merged",
                config=self.playbook_config
            )
        )
        result = self.execute_module(changed=True, failed=False)
        self.assertEqual(
            result.get("ap_update_msg"),
            "AP Configuration - NY-AP1-9130AXE updated Successfully"
        )

    def test_accesspoint_workflow_manager_missing_rf_profile(self):
        """
        Test case for user role workflow manager when creating a user.

        This test case checks the behavior of the user workflow when creating a new user in the specified Cisco Catalyst Center.
        """
        set_module_args(
            dict(
                dnac_host="1.1.1.1",
                dnac_username="dummy",
                dnac_password="dummy",
                dnac_log=True,
                state="merged",
                config=self.playbook_config_missing_rf_profile
            )
        )
        result = self.execute_module(changed=True, failed=True)
        self.assertEqual(
            result.get('msg'),
            "MAC Address is not Access point"
        )

    def test_accesspoint_workflow_manager_already_provision_device(self):
        """
        Test case for user role workflow manager when creating a user.

        This test case checks the behavior of the user workflow when creating a new user in the specified Cisco Catalyst Center.
        """
        set_module_args(
            dict(
                dnac_host="1.1.1.1",
                dnac_username="dummy",
                dnac_password="dummy",
                dnac_log=True,
                state="merged",
                config=self.playbook_config_provision
            )
        )
        result = self.execute_module(changed=False, failed=False)
        self.assertEqual(
            result.get('ap_update_msg'),
            "AP - NY-AP1-9130AXE does not need any update"
        )

    def test_accesspoint_workflow_manager_provision_device(self):
        """
        Test case for user role workflow manager when creating a user.

        This test case checks the behavior of the user workflow when creating a new user in the specified Cisco Catalyst Center.
        """
        set_module_args(
            dict(
                dnac_host="1.1.1.1",
                dnac_username="dummy",
                dnac_password="dummy",
                dnac_log=True,
                state="merged",
                config=self.playbook_config_provision
            )
        )
        result = self.execute_module(changed=False, failed=False)
        self.assertEqual(
            result.get('response').get('accesspoints_updates').get('provision_message'),
            "AP NFW-AP2-3802I provisioned successfully."
        )

    def test_invalid_site_exists(self):
        set_module_args(
            dict(
                dnac_host="1.1.1.1",
                dnac_username="dummy",
                dnac_password="dummy",
                dnac_log=True,
                state="merged",
                config=self.playbook_config_provision
            )
        )
        result = self.execute_module(changed=False, failed=True)
        print(result)
        self.assertEqual(
            result.get('msg'),
            "The provided site name 'Global/USA/New York/BLDNYC/FLOOR1' is either invalid or not present in the                         Cisco Catalyst Center."
        )

    def test_invalid_get_site_device(self):
        set_module_args(
            dict(
                dnac_host="1.1.1.1",
                dnac_username="dummy",
                dnac_password="dummy",
                dnac_log=True,
                state="merged",
                config=self.get_membership_empty
            )
        )
        result = self.execute_module(changed=False, failed=True)
        print(result)
        self.assertEqual(
            result.get('msg'),
            "Required param of mac_address,ip_address or hostname is not in playbook config"
        )

    def test_accesspoint_workflow_invalid_state(self):

        """
        Test case for access point workflow with an invalid 'state' parameter.

        This test case checks the behavior of the access point workflow when an invalid 'state' parameter is provided in the playbook.
        """

        set_module_args(
            dict(
                dnac_host="1.1.1.1",
                dnac_username="dummy",
                dnac_password="dummy",
                dnac_log=True,
                state="deleted",
                config=self.playbook_config
            )
        )
        result = self.execute_module(changed=False, failed=True)
        self.assertEqual(
            result.get('msg'),
            "State deleted is invalid"
        )

    def test_accesspoint_workflow_manager_Failure_provision_device(self):
        """
        Test case for user role workflow manager when creating a user.

        This test case checks the behavior of the user workflow when creating a new user in the specified Cisco Catalyst Center.
        """
        set_module_args(
            dict(
                dnac_host="1.1.1.1",
                dnac_username="dummy",
                dnac_password="dummy",
                dnac_log=True,
                state="merged",
                config=self.playbook_invalid_config_provision
            )
        )
        result = self.execute_module(changed=False, failed=True)
        self.assertEqual(
            result.get('msg'),
            # result.get('ap_update_msg'),
            "AP - NY-AP1-9130AXE does not need any update"
        )

    def test_accesspoint_workflow_manager_check_verify_diff_merged(self):
        """
        Test case for user role workflow manager when creating a user.

        This test case checks the behavior of the user workflow when creating a new user in the specified Cisco Catalyst Center.
        """
        set_module_args(
            dict(
                dnac_host="1.1.1.1",
                dnac_username="dummy",
                dnac_password="dummy",
                dnac_log=True,
                state="merged",
                config_verify=True,
                config=self.playbook_config_missing_update
            )
        )
        result = self.execute_module(changed=False, failed=True)
        self.assertEqual(
            result.get('msg'),
            'Invalid parameters in playbook config: \'[["Access Point series \'Cisco 9164I Series Unified Access Points\' not ' +
            'supported for the radio type 6ghz_radio allowed series [\'9136I\', \'9162I\', \'9163E\', \'9164I\', \'IW9167IH\', ' +
            '\'9178I\', \'9176I\', \'9176D1\']", "Access Point series \'Cisco 9164I Series Unified Access Points\' not supported ' +
            'for the radio type 6ghz_radio allowed series [\'9136I\', \'9162I\', \'9163E\', \'9164I\', \'IW9167IH\', \'9178I\', ' +
            '\'9176I\', \'9176D1\']", "Access Point series \'Cisco 9164I Series Unified Access Points\' not supported for the radio ' +
            'type 6ghz_radio allowed series [\'9136I\', \'9162I\', \'9163E\', \'9164I\', \'IW9167IH\', \'9178I\', \'9176I\', \'9176D1\']"]]\' '
        )

    def test_accesspoint_workflow_manager_some_missing_data_update_accesspoint(self):
        """
        Test case for user role workflow manager when creating a user.

        This test case checks the behavior of the user workflow when creating a new user in the specified Cisco Catalyst Center.
        """
        set_module_args(
            dict(
                dnac_host="1.1.1.1",
                dnac_username="dummy",
                dnac_password="dummy",
                dnac_log=True,
                state="merged",
                config=self.playbook_config_update_some_missing_data
            )
        )
        result = self.execute_module(changed=False, failed=True)
        self.assertEqual(
            result.get('msg'),
            'Invalid parameters in playbook config: \'[["Access Point series \'Cisco 9164I Series Unified Access Points\' not supported ' +
            'for the radio type xor_radio allowed series [\'2800\', \'3800\', \'4800\', \'9120\', \'9166\']", "Access Point series \'Cisco ' +
            '9164I Series Unified Access Points\' not supported for the radio type xor_radio allowed series [\'2800\', \'3800\', \'4800\', ' +
            '\'9120\', \'9166\']", "Access Point series \'Cisco 9164I Series Unified Access Points\' not supported for the radio type ' +
            'xor_radio allowed series [\'2800\', \'3800\', \'4800\', \'9120\', \'9166\']", "Access Point series \'Cisco 9164I Series Unified ' +
            'Access Points\' not supported for the radio type xor_radio allowed series [\'2800\', \'3800\', \'4800\', \'9120\', \'9166\']", "Access ' +
            'Point series \'Cisco 9164I Series Unified Access Points\' not supported for the radio type xor_radio allowed series [\'2800\', \'3800\', ' +
            '\'4800\', \'9120\', \'9166\']"], "management_ip_address: Invalid Management IP Address \'204.192.12.201dsd\'                            in ' +
            'playbook.", \'name: Invalid type or length > 32 characters in playbook.\', \'parent_name: Invalid type or length > 64 characters in ' +
            'playbook.\', "led_brightness_level: Invalid LED Brightness level \'10\' in playbook.", "led_status: Invalid LED Status \'Enableddd\' in ' +
            'playbook.", "ap_mode: Invalid value \'Monitorw\' for ap_mode in playbook. Must be one of: Local, Monitor, Sniffer or Bridge.", ' +
            '"failover_priority: Invalid value \'Lossw\' for failover_priority in playbook. Must be one of: Low, Medium, High or Critical.", ' +
            '"clean_air_si_2.4ghz: Invalid value \'Disableds\' in playbook. Must be either \'Enabled\' or \'Disabled\'.", "clean_air_si_5ghz: ' +
            'Invalid value \'Disableds\' in playbook. Must be either \'Enabled\' or \'Disabled\'.", "clean_air_si_6ghz: Invalid value \'Enableds\' ' +
            'in playbook. Must be either \'Enabled\' or \'Disabled\'.", "primary_ip_address: Invalid primary_ip_address \'{\'address\': ' +
            '\'204.192.4.20dfasd0\'}\' in playbook", "secondary_ip_address: Invalid secondary_ip_address \'{\'address\': \'204.192.4.20dfasd0\'}\' ' +
            'in playbook", "tertiary_ip_address: Invalid tertiary_ip_address \'{\'address\': \'204.192.4.20dfasd0\'}\' in playbook", \'Radio Params ' +
            'cannot be changed when AP mode is in None.\', "admin_status: Invalid value \'Enabledsds\' for admin_status in playbook. Must be ' +
            'either \'Enabled\' or \'Disabled\'.", "channel_assignment_mode: Invalid value \'any\' for Channel Assignment Mode in playbook. Must be ' +
            'either \'Global\' or \'Custom\'.", "channel_number: Invalid value \'22\' for Channel Number in playbook. Must be one of: ' +
            '[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11].", "channel_width: Invalid value \'50\' for Channel width in playbook. Must be one of: \'20 MHz\', ' +
            '\'40 MHz\', \'80 MHz\', or \'160 MHz\'.", "power_assignment_mode: Invalid value \'any\' for Power assignment mode in playbook. Must be ' +
            'either \'Global\' or \'Custom\'.", "powerlevel: Invalid Power level \'23\' in playbook. Must be between 1 to 8.", "radio_band: ' +
            'Invalid value \'2\' in playbook. Must be either \'2.4 GHz\' or \'5 GHz\'.", "radio_role_assignment: Invalid value \'any\' for radio ' +
            'role assignment in playbook. Must be one of: \'Auto\', \'Monitor\' or \'Client-Serving\'.", \'Radio Params cannot be changed when AP mode ' +
            'is in None.\', "admin_status: Invalid value \'Enabledsds\' for admin_status in playbook. Must be either \'Enabled\' or \'Disabled\'.", ' +
            '"antenna_gain: Invalid \'15\' in playbook", "channel_assignment_mode: Invalid value \'any\' for Channel Assignment Mode in playbook. Must ' +
            'be either \'Global\' or \'Custom\'.", "radio_role_assignment: Invalid value \'Client-Serving\'. Hence, AP mode is not Local. Kindly change ' +
            'the AP mode to Local then change the radio_role_assignment to Auto."]\' '
        )

    def test_invalid_wlc_device(self):
        set_module_args(
            dict(
                dnac_host="1.1.1.1",
                dnac_username="dummy",
                dnac_password="dummy",
                dnac_log=True,
                state="merged",
                config=self.playbook_config_provision
            )
        )
        result = self.execute_module(changed=False, failed=True)
        print(result)
        self.assertEqual(
            result.get('msg'),
            "Wireles controller is not provisioned:"
        )
