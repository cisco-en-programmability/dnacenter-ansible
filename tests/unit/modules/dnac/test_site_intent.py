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

from ansible_collections.cisco.dnac.plugins.modules import site_intent
from .dnac_module import TestDnacModule, set_module_args, loadPlaybookData

import json
import copy


class TestDnacSiteIntent(TestDnacModule):

    module = site_intent

    test_data = loadPlaybookData("site_intent")

    playbook_config = test_data.get("playbook_config")
    playbook_config_missing_param = test_data.get("playbook_config_missing_param")

    def setUp(self):
        super(TestDnacSiteIntent, self).setUp()

        self.mock_dnac_init = patch(
            "ansible_collections.cisco.dnac.plugins.module_utils.dnac.DNACSDK.__init__")
        self.run_dnac_init = self.mock_dnac_init.start()
        self.run_dnac_init.side_effect = [None]
        self.mock_dnac_exec = patch(
            "ansible_collections.cisco.dnac.plugins.module_utils.dnac.DNACSDK.exec"
        )
        self.run_dnac_exec = self.mock_dnac_exec.start()

    def tearDown(self):
        super(TestDnacSiteIntent, self).tearDown()
        self.mock_dnac_exec.stop()
        self.mock_dnac_init.stop()

    def load_fixtures(self, response=None, device=""):
        if "create_site" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                Exception(),
                self.test_data.get("create_site_response"),
                self.test_data.get("get_business_api_execution_details_response"),
                self.test_data.get("get_site_response")
            ]

        elif "update_not_needed" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("update_not_needed_get_site_response"),
            ]

        elif "update_needed" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("update_needed_get_site_response"),
                self.test_data.get("update_needed_update_site_response"),
                self.test_data.get("get_business_api_execution_details_response")
            ]
        elif "delete_existing_site" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("delete_get_site_response"),
                self.test_data.get("delete_delete_site_response"),
                self.test_data.get("get_business_api_execution_details_response")
            ]
        elif "delete_non_existing_site" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                Exception()
            ]
        elif "error_delete" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("delete_error_get_site_response"),
                self.test_data.get("delete_delete_site_response"),
                self.test_data.get("delete_execution_details_error")
            ]
        elif "error_create" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                Exception(),
                self.test_data.get("create_site_response"),
                self.test_data.get("delete_execution_details_error")
            ]

    def test_site_intent_create_site(self):
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
            result.get('msg'),
            "Site Created Successfully"
        )

    def test_site_intent_update_not_needed(self):
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
        result = self.execute_module(changed=False, failed=False)
        self.assertEqual(
            result.get('msg'),
            "Site does not need update"
        )

    def test_site_intent_update_needed(self):
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
            result.get('msg'),
            "Site Updated Successfully"
        )

    def test_site_intent_delete_existing_site(self):
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
            result.get('response').get('status'),
            "SUCCESS"
        )

    def test_site_intent_delete_non_existing_site(self):
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
            "Site Not Found"
        )

    def test_site_intent_invalid_param(self):
        set_module_args(
            dict(
                dnac_host="1.1.1.1",
                dnac_username="dummy",
                dnac_password="dummy",
                dnac_log=True,
                state="merged",
                config=self.test_data.get("playbook_config_invalid_param")
            )
        )
        result = self.execute_module(changed=False, failed=True)
        self.assertTrue(
            "Invalid parameters in playbook:" in result.get('msg')
        )

    def test_site_intent_error_delete(self):
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
            "True"
        )

    def test_site_intent_error_create(self):
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
            "True"
        )

    def test_site_intent_invalid_state(self):

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
