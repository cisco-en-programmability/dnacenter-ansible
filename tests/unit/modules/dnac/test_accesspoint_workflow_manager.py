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
import pdb

from dnacentersdk import exceptions
from unittest.mock import patch

from ansible_collections.cisco.dnac.plugins.modules import accesspoint_workflow_manager
from .dnac_module import TestDnacModule, set_module_args, loadPlaybookData

import json
import copy
import logging

class TestDnacAccesspointWorkflow(TestDnacModule):

    module = accesspoint_workflow_manager

    test_data = loadPlaybookData("accesspoint_workflow_manager")
    playbook_config = test_data.get("playbook_config")
    playbook_config_provision = test_data.get("playbook_config_provision")
    playbook_invalid_config = test_data.get("playbook_invalid_config")
    playbook_config_invalid_site = test_data.get("playbook_config_invalid_site")
    playbook_config_missing_rf_profile = test_data.get("playbook_config_missing_rf_profile")

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
                self.test_data.get("provision_ap_response"),
                self.test_data.get("provision_status"),
                self.test_data.get("camel_to_snake_case"), 
                self.test_data.get("provision_get_ap_response"),
            ]
        elif "provision_device" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("get_device_detail"), 
                self.test_data.get("get_site_exist_response"),
                self.test_data.get("get_membership_empty"),
                self.test_data.get("verify_get_device_info"),
                self.test_data.get("get_accesspoint_config"),
                self.test_data.get("provision_ap_response"),
                self.test_data.get("provision_execution_response"),
                self.test_data.get("provision_status"),
                self.test_data.get("camel_to_snake_case"), 
                self.test_data.get("provision_get_ap_response"),
            ]
        elif "update_accesspoint" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("get_device_detail"), 
                self.test_data.get("get_accesspoint_config"),
                self.test_data.get("get_site_exist_response"),
                self.test_data.get("get_membership_empty"),
                self.test_data.get("verify_get_device_info"),
                self.test_data.get("provision_ap_response"),
                self.test_data.get("provision_execution_response"),
                self.test_data.get("provision_status"),
                self.test_data.get("camel_to_snake_case"),
                self.test_data.get("provision_get_ap_response"),
            ]
        elif "site_exists" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("get_site_exist_response"),
            ]

        elif "accesspoint_workflow_manager_invalid_config" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("get_device_list"), 
            ]
        

    # def test_accesspoint_workflow_manager_invalid_config(self):
    #     """
    #     Test case for user role workflow manager when creating a user.

    #     This test case checks the behavior of the user workflow when creating a new user in the specified Cisco Catalyst Center.
    #     """
    #     set_module_args(
    #         dict(
    #             dnac_host="1.1.1.1",
    #             dnac_username="dummy",
    #             dnac_password="dummy",
    #             dnac_log=True,
    #             state="merged",
    #             config=self.playbook_invalid_config
    #         )
    #     )
    #     result = self.execute_module(changed=True, failed=True)
    #     self.assertEqual(
    #         result.get('msg'),
    #         "Required param of mac_address, management_ip_address or hostname                      is not in playbook config"
    #     )

    # def test_accesspoint_workflow_manager_invalid_Mac_address(self):
    #     """
    #     Test case for user role workflow manager when creating a user.

    #     This test case checks the behavior of the user workflow when creating a new user in the specified Cisco Catalyst Center.
    #     """
    #     set_module_args(
    #         dict(
    #             dnac_host="1.1.1.1",
    #             dnac_username="dummy",
    #             dnac_password="dummy",
    #             dnac_log=True,
    #             state="merged",
    #             config=self.playbook_config
    #         )
    #     )

    #     result = self.execute_module(changed=False, failed=False)
    #     self.assertEqual(
    #         result.get('msg'),
    #         "MAC Address is not Access point"
    #     )

    def test_accesspoint_workflow_manager_invalid_site(self):
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
                config=self.playbook_config_invalid_site
            )
        )
        result = self.execute_module(changed=True, failed=True)
        self.assertEqual(
            result.get('msg'),
            "MAC Address is not Access point"
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
                state="merge",
                config=self.playbook_config
            )
        )
        result = self.execute_module(changed=False, failed=True)
        self.assertEqual(
            result.get('msg'),
            "value of state must be one of: merged, deleted, got: merge"
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
            #result.get('response').get('accesspoints_updates').get('ap_update_msg'),
            result.get('ap_update_msg'),
            "AP - NFW-AP2-3802I does not need any update"
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
            #result.get('ap_update_msg'),
            "AP NFW-AP2-3802I provisioned Successfully"
        )

    def test_accesspoint_workflow_manager_update_accesspoint(self):
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
            result.get('response').get('accesspoints_updates').get('ap_update_msg'),
            #result.get('ap_update_msg'),
            "AP - NFW-AP2-3802I does not need any update"
        )
