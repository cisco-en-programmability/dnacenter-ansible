# Copyright (c) 2020-2022 Cisco and/or its affiliates.
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
from ansible.errors import AnsibleActionFail
from ansible_collections.cisco.dnac.plugins.modules import pnp_intent
from .dnac_module import TestDnacModule, set_module_args, loadPlaybookData

import json
import copy


class TestDnacPnPIntent(TestDnacModule):

    module = pnp_intent

    test_data = loadPlaybookData("pnp_intent")

    playbook_config = test_data.get("playbook_config")
    playbook_config_missing_param = test_data.get("playbook_config_missing_param")

    def setUp(self):
        super(TestDnacPnPIntent, self).setUp()

        self.mock_dnac_init = patch(
            "ansible_collections.cisco.dnac.plugins.module_utils.dnac.DNACSDK.__init__")
        self.run_dnac_init = self.mock_dnac_init.start()
        self.run_dnac_init.side_effect = [None]
        self.mock_dnac_exec = patch(
            "ansible_collections.cisco.dnac.plugins.module_utils.dnac.DNACSDK.exec"
        )
        self.run_dnac_exec = self.mock_dnac_exec.start()

    def tearDown(self):
        super(TestDnacPnPIntent, self).tearDown()
        self.mock_dnac_exec.stop()
        self.mock_dnac_init.stop()

    def load_fixtures(self, response=None, device=""):
        if "site_not_found" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("image_exists_response"),
                self.test_data.get("template_exists_response"),
                Exception(),
            ]

        elif "add_new_device" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("image_exists_response"),
                self.test_data.get("template_exists_response"),
                self.test_data.get("site_exists_response"),
                [],
                self.test_data.get("add_device_response"),
                self.test_data.get("claim_response")
            ]

        elif "device_exists" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("image_exists_response"),
                self.test_data.get("template_exists_response"),
                self.test_data.get("site_exists_response"),
                self.test_data.get("device_exists_response"),
                self.test_data.get("claim_response")
            ]

        elif "delete_device" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("device_exists_response"),
                self.test_data.get("delete_device_response")
            ]

        elif "deletion_error" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("device_exists_response"),
                AnsibleActionFail("An error occured when executing operation." +
                                  "The error was: [400] Bad Request - NCOB01313: Delete device(FJC2416U047) from Inventory"),
            ]

        elif "image_doesnot_exist" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("image_doesnot_exist_response")
            ]

        elif "template_doesnot_exist" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("image_exists_response"),
                self.test_data.get("template_doesnot_exist_response")
            ]

        elif "project_not_found" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("image_exists_response"),
                []
            ]
        elif "delete_nonexisting_device" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                []
            ]

    def test_pnp_intent_site_not_found(self):
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
            "Site not found"
        )

    def test_pnp_intent_add_new_device(self):
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
            result.get('response').get('response'),
            "Device Claimed"
        )

    def test_pnp_intent_device_exists(self):
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
            result.get('response').get('response'),
            "Device Claimed"
        )

    def test_pnp_intent_image_doesnot_exist(self):
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
            "Image not found"
        )

    def test_pnp_intent_template_doesnot_exist(self):
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
            "Template not found"
        )

    def test_pnp_intent_project_not_found(self):
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
            "Project Not Found"
        )

    def test_pnp_intent_missing_param(self):
        set_module_args(
            dict(
                dnac_host="1.1.1.1",
                dnac_username="dummy",
                dnac_password="dummy",
                dnac_log=True,
                state="merged",
                config=self.test_data.get("playbook_config_missing_parameter")
            )
        )
        result = self.execute_module(changed=False, failed=True)
        self.assertEqual(
            result.get('msg'),
            "Invalid parameters in playbook: image_name : Required parameter not found"
        )

    def test_pnp_intent_delete_device(self):
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
        result = self.execute_module(changed=True, failed=False)
        self.assertEqual(
            result.get('msg'),
            "Device Deleted Successfully"
        )

    def test_pnp_intent_deletion_error(self):
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
            "Device Deletion Failed"
        )

    def test_pnp_intent_delete_nonexisting_device(self):
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
            "Device Not Found"
        )

    def test_pnp_intent_invalid_state(self):
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
