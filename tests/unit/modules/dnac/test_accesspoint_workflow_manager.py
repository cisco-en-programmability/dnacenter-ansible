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
    reboot_accesspoint = test_data.get("reboot_accesspoint")
    playbook_config_provision_old_version = test_data.get("playbook_config_provision_old_version")
    playbook_config = test_data.get("playbook_config")
    playbook_config_provision = test_data.get("playbook_config_provision")
    playbook_config_complete = test_data.get("playbook_config_complete")
    get_membership_empty = test_data.get("get_membership_empty")
    get_device_detail_all_data = test_data.get("get_device_detail_all_data")
    playbook_config_update_some_missing_data = test_data.get("playbook_config_update_some_missing_data")
    playbook_config_update_some_error_data = test_data.get("playbook_config_update_some_error_data")
    playbook_invalid_config_complete = test_data.get("playbook_invalid_config_complete")

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
        if "provision_device" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("get_device_detail"),
                self.test_data.get("get_site_exist_response"),
                self.test_data.get("get_device_detail"),
                self.test_data.get("verify_get_device_info"),
                self.test_data.get("get_accesspoint_config"),
                self.test_data.get("assign_to_site_response"),
                self.test_data.get("assign_to_site_task_response"),
                self.test_data.get("provision_ap_response"),
                self.test_data.get("provision_ap_task_response"),
                self.test_data.get("ap_update_response"),
                self.test_data.get("ap_task_status"),
                self.test_data.get("get_device_detail"),
                self.test_data.get("get_site_exist_response"),
                self.test_data.get("get_device_detail"),
                self.test_data.get("verify_get_device_info"),
                self.test_data.get("get_accesspoint_config_verify")
            ]
        elif "invalid_wlc_device" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("get_device_detail"),
                self.test_data.get("get_site_exist_response")
            ]
        elif "some_error_data_update_accesspoint" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("get_device_detail")
            ]
        elif "negative_config_input" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("get_device_detail_error"),
                self.test_data.get("get_site_exist_response"),
                self.test_data.get("get_device_detail"),
                self.test_data.get("verify_get_device_info"),
                self.test_data.get("get_accesspoint_config")
            ]
        elif "reboot_accesspoint" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("get_device_detail_reboot"),
                self.test_data.get("ap_reboot_response"),
                self.test_data.get("ap_reboot_task_response"),
                self.test_data.get("ap_reboot_status")
            ]
        elif "provision_old_version" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("get_device_detail"),
                self.test_data.get("get_site_exist_response_old"),
                self.test_data.get("get_membership"),
                self.test_data.get("verify_get_device_info"),
                self.test_data.get("get_accesspoint_config"),
                self.test_data.get("provision_ap_response_old"),
                self.test_data.get("provision_execution_response"),
                self.test_data.get("get_device_detail"),
                self.test_data.get("get_site_exist_response"),
                self.test_data.get("get_device_detail"),
                self.test_data.get("verify_get_device_info")
            ]
        elif "task_error_update_accesspoint" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("get_device_detail_all_data"),
                self.test_data.get("get_accesspoint_config"),
                self.test_data.get("ap_update_response"),
                self.test_data.get("ap_task_error_status")
            ]

    def test_accesspoint_workflow_manager_invalid_provision_device_channel_width(self):
        """
        Test case for access point workfollow manager provision and update device.

        This test case checks the behavior of the access point workflow when provisioned in the specified Cisco Catalyst Center.
        """
        set_module_args(
            dict(
                dnac_host="1.1.1.1",
                dnac_username="dummy",
                dnac_password="dummy",
                dnac_log=True,
                state="merged",
                dnac_version="2.3.7.6",
                config_verify=True,
                config=self.playbook_config_complete
            )
        )
        result = self.execute_module(changed=False, failed=True)
        self.assertIn(
            "channel_width is not applicable for the 2.4GHz radio",
            result.get('msg', '')
        )

    def test_invalid_wlc_device(self):
        """
        Test case for access point workfollow manager check invalid wireless controller.

        This test case checks the behavior of the access point workflow of invalid wlc specified Cisco Catalyst Center.
        """
        set_module_args(
            dict(
                dnac_host="1.1.1.1",
                dnac_username="dummy",
                dnac_password="dummy",
                dnac_log=True,
                state="merged",
                dnac_version="2.3.7.6",
                config=self.playbook_config_provision
            )
        )
        result = self.execute_module(changed=False, failed=True)
        self.maxDiff = None
        self.assertIn(
            "get_site_assigned_network_devices",
            result.get("msg")
        )

    def test_accesspoint_workflow_manager_some_error_data_update_accesspoint(self):
        """
        Test case for access point workfollow manager negative case.

        This test case checks the behavior of the access point workflow when wrong data passed in the specified Cisco Catalyst Center.
        """
        set_module_args(
            dict(
                dnac_host="1.1.1.1",
                dnac_username="dummy",
                dnac_password="dummy",
                dnac_log=True,
                state="merged",
                config_verify=True,
                dnac_version="2.3.7.6",
                config=self.playbook_config_update_some_error_data
            )
        )
        result = self.execute_module(changed=True, failed=True)
        self.maxDiff = None
        self.assertIn(
            'get_sites',
            result.get('msg')
        )

    def test_accesspoint_workflow_manager_negative_config_input(self):
        """
        Test case for access point workfollow manager and negative test verify ap update

        This test case checks the behavior of the update access point data in the specified Cisco Catalyst Center.
        """
        set_module_args(
            dict(
                dnac_host="1.1.1.1",
                dnac_username="dummy",
                dnac_password="dummy",
                dnac_log=True,
                state="merged",
                config_verify=True,
                dnac_version="2.3.7.6",
                config=self.playbook_config_update_some_missing_data
            )
        )
        result = self.execute_module(changed=False, failed=True)
        self.maxDiff = None
        self.assertIn(
            "Invalid parameters in playbook config:",
            result.get('msg')
        )

    def test_accesspoint_workflow_manager_reboot_accesspoint(self):
        """
        Test case for access point workfollow manager to reboot access point.

        This test case checks the behavior of the access point workflow of reboot ap specified Cisco Catalyst Center.
        """
        set_module_args(
            dict(
                dnac_host="1.1.1.1",
                dnac_username="dummy",
                dnac_password="dummy",
                dnac_log=True,
                state="merged",
                dnac_version="2.3.7.6",
                config=self.reboot_accesspoint
            )
        )
        result = self.execute_module(changed=True, failed=False)
        self.maxDiff = None
        self.assertEqual(
            result.get('response').get("accesspoints_updates").get("ap_reboot_status"),
            "APs ['34:b8:83:15:7c:6c'] rebooted successfully"
        )

    def test_accesspoint_workflow_manager_provision_old_version(self):
        """
        Test case for access point workfollow manager provision device old version.

        This test case checks the behavior of the access point workflow when provisioned in the specified Cisco Catalyst Center.
        """
        set_module_args(
            dict(
                dnac_host="1.1.1.1",
                dnac_username="dummy",
                dnac_password="dummy",
                dnac_log=True,
                state="merged",
                dnac_version="2.3.5.3",
                config_verify=True,
                config=self.playbook_config_provision_old_version
            )
        )
        result = self.execute_module(changed=False, failed=True)
        self.maxDiff = None
        self.assertIn(
            "AP LTTS_Test_9124_T2 provisioned successfully",
            result.get('msg')
        )

    def test_accesspoint_workflow_manager_task_error_update_accesspoint(self):
        """
        Test case for access point workfollow manager and negative test verify ap update.

        This test case checks the behavior of the nagative test case of update in the specified Cisco Catalyst Center.
        """
        set_module_args(
            dict(
                dnac_host="1.1.1.1",
                dnac_username="dummy",
                dnac_password="dummy",
                dnac_log=True,
                state="merged",
                config_verify=True,
                dnac_version="2.3.7.6",
                config=self.playbook_config
            )
        )
        result = self.execute_module(changed=False, failed=True)
        self.assertIn(
            "An error occurred while executing API call to Function: 'get_task_details_by_id'",
            result.get('msg')
        )

    def test_invalid_site_exists(self):
        """
        Test case for access point workfollow manager check site exists.

        This test case checks the behavior of the access point workflow when site exist in the specified Cisco Catalyst Center.
        """
        set_module_args(
            dict(
                dnac_host="1.1.1.1",
                dnac_username="dummy",
                dnac_password="dummy",
                dnac_log=True,
                state="merged",
                dnac_version="2.3.7.6",
                config=self.playbook_config_provision
            )
        )
        result = self.execute_module(changed=False, failed=True)
        print(result)
        self.assertEqual(
            result.get('msg'),
            "Provided device is not Access Point."
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
                dnac_version="2.3.7.6",
                config=self.playbook_config
            )
        )
        result = self.execute_module(changed=False, failed=True)
        self.assertEqual(
            result.get('msg'),
            "State deleted is invalid"
        )

    def test_invalid_get_site_device(self):
        """
        Test case for access point workfollow manager get device details from site

        This test case checks the behavior of the access point workflow when check the devices in the site on the specified Cisco Catalyst Center.
        """
        set_module_args(
            dict(
                dnac_host="1.1.1.1",
                dnac_username="dummy",
                dnac_password="dummy",
                dnac_log=True,
                state="merged",
                dnac_version="2.3.7.9",
                config=self.playbook_invalid_config_complete
            )
        )
        result = self.execute_module(changed=False, failed=True)
        print(result)
        self.assertEqual(
            result.get('response'),
            "Required param of mac_address,ip_address or hostname is not in playbook config"
        )
