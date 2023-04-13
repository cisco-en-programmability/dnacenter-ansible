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

from ansible_collections.cisco.dnac.plugins.modules import swim_intent
from .dnac_module import TestDnacModule, set_module_args, loadPlaybookData


class TestDnacSwimIntent(TestDnacModule):

    module = swim_intent
    test_data = loadPlaybookData("swim_intent")
    playbook_config = test_data.get("playbook_config")
    playbook_config_untag_image = test_data.get("playbook_config_untag_golden_image")

    def setUp(self):
        super(TestDnacSwimIntent, self).setUp()

        self.mock_dnac_init = patch(
            "ansible_collections.cisco.dnac.plugins.module_utils.dnac.DNACSDK.__init__")
        self.run_dnac_init = self.mock_dnac_init.start()
        self.run_dnac_init.side_effect = [None]
        self.mock_dnac_exec = patch(
            "ansible_collections.cisco.dnac.plugins.module_utils.dnac.DNACSDK.exec"
        )
        self.run_dnac_exec = self.mock_dnac_exec.start()

    def tearDown(self):
        super(TestDnacSwimIntent, self).tearDown()
        self.mock_dnac_exec.stop()
        self.mock_dnac_init.stop()

    def load_fixtures(self, response=None, device=""):
        if "full_flow" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("task_info_response"),
                self.test_data.get("image_imported_successfully_response"),
                self.test_data.get("image_id_fetched_successfully_response"),
                self.test_data.get("device_family_fetched_successfully"),
                self.test_data.get("device_id_fetched_successfully_response"),
                self.test_data.get("device_id_fetched_successfully_response"),
                self.test_data.get("task_info_response"),
                self.test_data.get("tagging_image_successful_response"),
                self.test_data.get("task_info_response"),
                self.test_data.get("image_distribution_successful_response"),
                self.test_data.get("task_info_response"),
                self.test_data.get("image_activation_successful_response")
            ]
        elif "swim_image_import" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("task_info_response"),
                self.test_data.get("image_already_exists_response"),
            ]
        elif "swim_image_local_import" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("task_info_response"),
                self.test_data.get("image_already_exists_response"),
            ]
        elif "untag_image" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("image_id_fetched_successfully_response"),
                self.test_data.get("fetch_site_id_response"),
                self.test_data.get("device_family_fetched_successfully"),
                self.test_data.get("task_info_response"),
                self.test_data.get("untagging_image_successful_response"),
            ]
        elif "incorrect_site_untag_golden_image" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("image_id_fetched_successfully_response"),
                Exception()
            ]
        elif "image_doesnot_exist_response" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("image_doesnot_exist_response"),
            ]
        elif "tag_golden_incorrect_family_name" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("image_id_fetched_successfully_response"),
                self.test_data.get("fetch_site_id_response"),
                self.test_data.get("device_family_fetched_successfully"),
            ]
        elif "only_image_distribution" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("image_id_fetched_successfully_response"),
                self.test_data.get("device_id_fetched_successfully_response"),
                self.test_data.get("task_info_response"),
                self.test_data.get("image_distribution_successful_response"),
            ]
        elif "only_image_activation" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("image_id_fetched_successfully_response"),
                self.test_data.get("device_id_fetched_successfully_response"),
                self.test_data.get("task_info_response"),
                self.test_data.get("image_activation_successful_response"),
            ]
        elif "device_doesnot_exist" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("image_id_fetched_successfully_response"),
                self.test_data.get("device_doesnot_exist_response"),
            ]

    def test_swim_full_flow(self):
        set_module_args(
            dict(
                dnac_host="1.1.1.1",
                dnac_username="dummy",
                dnac_password="dummy",
                dnac_log=True,
                config=self.playbook_config
            )
        )
        result = self.execute_module(changed=True, failed=False)
        self.assertEqual(
            result.get('msg'),
            "Image activated successfully"
        )

    def test_swim_image_import(self):
        set_module_args(
            dict(
                dnac_host="1.1.1.1",
                dnac_username="dummy",
                dnac_password="dummy",
                dnac_log=True,
                config=self.test_data.get("playbook_config_image_import")
            )
        )
        result = self.execute_module(changed=False, failed=False)
        self.assertEqual(
            result.get('msg'),
            "Image already exists."
        )

    def test_swim_image_local_import(self):
        set_module_args(
            dict(
                dnac_host="1.1.1.1",
                dnac_username="dummy",
                dnac_password="dummy",
                dnac_log=True,
                config=self.test_data.get("playbook_config_local_image_import")
            )
        )
        result = self.execute_module(changed=False, failed=False)
        self.assertEqual(
            result.get('msg'),
            "Image already exists."
        )

    def test_swim_untag_image(self):
        set_module_args(
            dict(
                dnac_host="1.1.1.1",
                dnac_username="dummy",
                dnac_password="dummy",
                dnac_log=True,
                config=self.playbook_config_untag_image
            )
        )
        result = self.execute_module(changed=True, failed=False)
        self.assertEqual(
            result.get('msg'),
            "Un-tagging image as Golden."
        )

    def test_swim_missing_param_tag_golden_image(self):
        set_module_args(
            dict(
                dnac_host="1.1.1.1",
                dnac_username="dummy",
                dnac_password="dummy",
                dnac_log=True,
                config=self.test_data.get("playbook_config_tag_golden_image_missing_param")
            )
        )
        result = self.execute_module(changed=False, failed=True)
        self.assertEqual(
            result.get('msg'),
            "Image details for tagging not provided"
        )

    def test_swim_incorrect_site_untag_golden_image(self):
        set_module_args(
            dict(
                dnac_host="1.1.1.1",
                dnac_username="dummy",
                dnac_password="dummy",
                dnac_log=True,
                config=self.playbook_config_untag_image
            )
        )
        result = self.execute_module(changed=False, failed=True)
        self.assertEqual(
            result.get('msg'),
            "Site not found"
        )

    def test_swim_image_doesnot_exist_response(self):
        set_module_args(
            dict(
                dnac_host="1.1.1.1",
                dnac_username="dummy",
                dnac_password="dummy",
                dnac_log=True,
                config=self.playbook_config_untag_image
            )
        )
        result = self.execute_module(changed=False, failed=True)
        self.assertEqual(
            result.get('msg'),
            "Image not found"
        )

    def test_swim_only_image_distribution(self):
        set_module_args(
            dict(
                dnac_host="1.1.1.1",
                dnac_username="dummy",
                dnac_password="dummy",
                dnac_log=True,
                config=self.test_data.get("playbook_config_distribution")
            )
        )
        result = self.execute_module(changed=True, failed=False)
        self.assertEqual(
            result.get('msg'),
            "Image Distributed Successfully"
        )

    def test_swim_image_distribution_missing_param(self):
        set_module_args(
            dict(
                dnac_host="1.1.1.1",
                dnac_username="dummy",
                dnac_password="dummy",
                dnac_log=True,
                config=self.test_data.get("playbook_config_distribution_missing_param")
            )
        )
        result = self.execute_module(changed=False, failed=True)
        self.assertEqual(
            result.get('msg'),
            "Image details for distribution not provided"
        )

    def test_swim_only_image_activation(self):
        set_module_args(
            dict(
                dnac_host="1.1.1.1",
                dnac_username="dummy",
                dnac_password="dummy",
                dnac_log=True,
                config=self.test_data.get("playbook_config_activation")
            )
        )
        result = self.execute_module(changed=True, failed=False)
        self.assertEqual(
            result.get('msg'),
            "Image activated successfully"
        )

    def test_swim_image_activation_missing_param(self):
        set_module_args(
            dict(
                dnac_host="1.1.1.1",
                dnac_username="dummy",
                dnac_password="dummy",
                dnac_log=True,
                config=self.test_data.get("playbook_config_activation_missing_param")
            )
        )
        result = self.execute_module(changed=False, failed=True)
        self.assertEqual(
            result.get('msg'),
            "Image details for activation not provided"
        )

    def test_swim_tag_golden_incorrect_family_name(self):
        set_module_args(
            dict(
                dnac_host="1.1.1.1",
                dnac_username="dummy",
                dnac_password="dummy",
                dnac_log=True,
                config=self.test_data.get("playbook_config_tag_golden_image_incorrect_family_name")
            )
        )
        result = self.execute_module(changed=False, failed=True)
        self.assertEqual(
            result.get('msg'),
            "Family Device Name not found"
        )

    def test_swim_device_doesnot_exist(self):
        set_module_args(
            dict(
                dnac_host="1.1.1.1",
                dnac_username="dummy",
                dnac_password="dummy",
                dnac_log=True,
                config=self.test_data.get("playbook_config_activation")
            )
        )
        result = self.execute_module(changed=False, failed=True)
        self.assertEqual(
            result.get('msg'),
            "Device not found"
        )

    def test_swim_incorrect_image_import_parameter(self):
        set_module_args(
            dict(
                dnac_host="1.1.1.1",
                dnac_username="dummy",
                dnac_password="dummy",
                dnac_log=True,
                config=self.test_data.get("playbook_config_incorrect_image_import_parameter")
            )
        )
        result = self.execute_module(changed=False, failed=True)
        self.assertEqual(
            result.get('msg'),
            "Incorrect import type. Supported Values: local or url"
        )
