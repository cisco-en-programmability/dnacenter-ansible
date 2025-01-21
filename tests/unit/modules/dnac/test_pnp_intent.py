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

from ansible.errors import AnsibleActionFail
from ansible_collections.cisco.dnac.plugins.modules import pnp_intent
from .dnac_module import TestDnacModule, set_module_args


class TestDnacPnPIntent(TestDnacModule):
    def __init__(self):

        """
        Inheriting from the base class of dnac_module
        """

        module = pnp_intent
        super().__init__(module)

    def load_fixtures(self, response=None, device=""):

        """
        Load fixtures for a specific device.

        Parameters:
        response (list, optional): The expected response data. Defaults to None.
        device (str, optional): The device for which to load fixtures. Defaults to an empty string.
        """

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

        """
        Test case for PnP intent when site is not found.

        This test case checks the behavior of the PnP intent when the site is not found in the specified DNAC.
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
            "Site not found"
        )

    def test_pnp_intent_add_new_device(self):

        """
        Test case for PnP intent when adding a new device.

        This test case checks the behavior of the PnP intent when adding a new device in the specified DNAC.
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
            result.get('response').get('response'),
            "Device Claimed"
        )

    def test_pnp_intent_device_exists(self):

        """
        Test case for PnP intent when a device already exists.

        This test case checks the behavior of the PnP intent when a device already exists in the specified DNAC.
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
            result.get('response').get('response'),
            "Device Claimed"
        )

    def test_pnp_intent_image_doesnot_exist(self):

        """
        Test case for PnP intent when an image does not exist.

        This test case checks the behavior of the PnP intent when the specified image is not found in the DNAC.
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
            "Image not found"
        )

    def test_pnp_intent_template_doesnot_exist(self):

        """
        Test case for PnP intent when a template does not exist.

        This test case checks the behavior of the PnP intent when the specified template is not found in the DNAC.
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
            "Template not found"
        )

    def test_pnp_intent_project_not_found(self):

        """
        Test case for PnP intent when a project is not found.

        This test case checks the behavior of the PnP intent when the specified project is not found in the DNAC.
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
            "Project Not Found"
        )

    def test_pnp_intent_missing_param(self):

        """
        Test case for PnP intent with missing parameters in the playbook.

        This test case checks the behavior of the PnP intent when the playbook contains missing required parameters.
        """

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

        """
        Test case for PnP intent when deleting a device.

        This test case checks the behavior of the PnP intent when deleting a device in the DNAC.
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
        result = self.execute_module(changed=True, failed=False)
        self.assertEqual(
            result.get('msg'),
            "Device Deleted Successfully"
        )

    def test_pnp_intent_deletion_error(self):

        """
        Test case for PnP intent when device deletion fails.

        This test case checks the behavior of the PnP intent when device deletion fails in the DNAC.
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
            "Device Deletion Failed"
        )

    def test_pnp_intent_delete_nonexisting_device(self):

        """
        Test case for PnP intent when deleting a non-existing device.

        This test case checks the behavior of the PnP intent when trying to delete a device that doesn't exist in the DNAC.
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
            "Device Not Found"
        )

    def test_pnp_intent_invalid_state(self):

        """
        Test case for PnP intent with an invalid state parameter.

        This test case checks the behavior of the PnP intent when an invalid 'state' parameter is provided in the playbook.
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
