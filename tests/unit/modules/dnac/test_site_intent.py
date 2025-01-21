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

from ansible_collections.cisco.dnac.plugins.modules import site_intent
from .dnac_module import TestDnacModule, set_module_args


class TestDnacSiteIntent(TestDnacModule):
    def __init__(self):
        """
        Inheriting from the base class of dnac_module
        """

        module = site_intent
        super().__init__(module)

    def load_fixtures(self, response=None, device=""):

        """
        Load fixtures for a specific device.

        Parameters:
        response (list, optional): The expected response data. Defaults to None.
        device (str, optional): The device for which to load fixtures. Defaults to an empty string.
        """

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

        """
        Test case for site intent when creating a site.

        This test case checks the behavior of the site intent when creating a new site in the specified DNAC.
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
            result.get('msg'),
            "Site Created Successfully"
        )

    def test_site_intent_update_not_needed(self):

        """
        Test case for site intent when no update is needed.

        This test case checks the behavior of the site intent when an update is not required for the specified site in the DNAC.
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
        result = self.execute_module(changed=False, failed=False)
        self.assertEqual(
            result.get('msg'),
            "Site does not need update"
        )

    def test_site_intent_update_needed(self):

        """
        Test case for site intent when an update is needed.

        This test case checks the behavior of the site intent when an update is required for the specified site in the DNAC.
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
            result.get('msg'),
            "Site Updated Successfully"
        )

    def test_site_intent_delete_existing_site(self):

        """
        Test case for site intent when deleting an existing site.

        This test case checks the behavior of the site intent when deleting an existing site in the DNAC.
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
            result.get('response').get('status'),
            "SUCCESS"
        )

    def test_site_intent_delete_non_existing_site(self):

        """
        Test case for site intent when attempting to delete a non-existing site.

        This test case checks the behavior of the site intent when trying to delete a site that does not exist in the DNAC.
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
            "Site Not Found"
        )

    def test_site_intent_invalid_param(self):

        """
        Test case for site intent with invalid parameters in the playbook.

        This test case checks the behavior of the site intent when the playbook contains invalid parameters.
        """

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

        """
        Test case for site intent when an error occurs during site deletion.

        This test case checks the behavior of the site intent when an error occurs while deleting a site in the DNAC.
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
            "True"
        )

    def test_site_intent_error_create(self):

        """
        Test case for site intent when an error occurs during site creation.

        This test case checks the behavior of the site intent when an error occurs while creating a site in the DNAC.
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
            "True"
        )

    def test_site_intent_invalid_state(self):

        """
        Test case for site intent with an invalid 'state' parameter.

        This test case checks the behavior of the site intent when an invalid 'state' parameter is provided in the playbook.
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
