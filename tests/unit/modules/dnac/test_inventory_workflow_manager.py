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

from ansible_collections.cisco.dnac.plugins.modules import inventory_workflow_manager
from .dnac_module import TestDnacModule, set_module_args, loadPlaybookData


class TestDnacInventoryWorkflow(TestDnacModule):

    module = inventory_workflow_manager

    test_data = loadPlaybookData("inventory_workflow_manager")

    playbook_add_device = test_data.get("playbook_add_device")


    def setUp(self):
        super(TestDnacInventoryWorkflow, self).setUp()

        self.mock_dnac_init = patch(
            "ansible_collections.cisco.dnac.plugins.module_utils.dnac.DNACSDK.__init__")
        self.run_dnac_init = self.mock_dnac_init.start()
        self.run_dnac_init.side_effect = [None]
        self.mock_dnac_exec = patch(
            "ansible_collections.cisco.dnac.plugins.module_utils.dnac.DNACSDK._exec"
        )
        self.run_dnac_exec = self.mock_dnac_exec.start()

    def tearDown(self):
        super(TestDnacInventoryWorkflow, self).tearDown()
        self.mock_dnac_exec.stop()
        self.mock_dnac_init.stop()

    def load_fixtures(self, response=None, device=""):
        """
        Load fixtures for user.
        """ 
        if "playbook_add_device" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("get_device_list_add_device"),
                self.test_data.get("get_device_list_add_device_2"),
                self.test_data.get("add_device_add_device"),
                self.test_data.get("TaskDetails_add_device_start"),
                self.test_data.get("TaskDetails_add_device_end"),
                self.test_data.get("get_device_list_add_device_3"),
                self.test_data.get("get_device_list_add_device_5"),
                self.test_data.get("add_device_response"),
                ]


    def test_inventory_workflow_manager_playbook_add_device(self):
        """
        Test case for add device with full crendentials.

        This test case checks the addition of new network device added with full credentials in Cisco Catalyst Center.
        """
        set_module_args(
            dict(
                dnac_host="1.1.1.1",
                dnac_username="dummy",
                dnac_password="dummy",
                dnac_log=True,
                state="merged",
                config_verify = True,
                config = self.playbook_add_device
            )
        )
        result = self.execute_module(changed=True, failed=False)
        print(result)
        self.assertEqual(
            result.get('msg'),
            "Device(s) '['60.1.1.1', '50.1.1.1']' added to Cisco Catalyst Center"
        )