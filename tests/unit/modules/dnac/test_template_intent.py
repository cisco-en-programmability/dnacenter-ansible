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

from ansible_collections.cisco.dnac.plugins.modules import template_intent
from .dnac_module import TestDnacModule, set_module_args


class TestDnacTemplateIntent(TestDnacModule):
    def __init__(self):
        """
        Inheriting from the base class of dnac_module
        """

        module = template_intent
        super().__init__(module)

    def load_fixtures(self, response=None, device=""):

        """
        Load fixtures for a specific device.

        Parameters:
        response (list, optional): The expected response data. Defaults to None.
        device (str, optional): The device for which to load fixtures. Defaults to an empty string.
        """

        if "create_template" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("create_template_list_response"),
                self.test_data.get("create_template_get_project_response"),
                self.test_data.get("create_template_response"),
                self.test_data.get("create_template_task_details_for_create"),
                self.test_data.get("create_template_version_template_response"),
                self.test_data.get("create_template_task_details_for_versioning")
            ]
        elif "update_not_needed" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("update_template_list"),
                self.test_data.get("update_template_existing_template"),
            ]
        elif "update_needed" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("update_template_list"),
                self.test_data.get("update_template_existing_template_needs_update"),
                self.test_data.get("update_template_response"),
                self.test_data.get("update_template_version_template_response"),
                self.test_data.get("update_template_task_details_for_versioning")
            ]
        elif "project_not_found" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                [],
            ]
        elif "delete_non_existing_template" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("create_template_list_response")
            ]
        elif "delete_template" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("update_template_list"),
                self.test_data.get("update_template_existing_template_needs_update"),
                self.test_data.get("delete_template_response"),
                self.test_data.get("delete_template_task_details"),
            ]

    def test_template_intent_create_template(self):

        """
        Test case for template intent when creating a template.

        This test case checks the behavior of the template intent when creating a new template in the specified DNAC.
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
            result.get('response').get('progress'),
            "Successfully committed template ANSIBLE-TEST to version 1"
        )

    def test_template_intent_update_not_needed(self):

        """
        Test case for template intent when no update is needed.

        This test case checks the behavior of the template intent when an update is not required for the specified template in the DNAC.
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
            "Template does not need update"
        )

    def test_template_intent_update_needed(self):

        """
        Test case for template intent when an update is needed.

        This test case checks the behavior of the template intent when an update is required for the specified template in the DNAC.
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
            result.get('response').get('progress'),
            "Successfully committed template ANSIBLE-TEST to version 2"
        )

    def test_template_intent_project_not_found(self):

        """
        Test case for template intent when the project is not found.

        This test case checks the behavior of the template intent when the specified project is not found in the DNAC.
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

    def test_template_intent_delete_non_existing_template(self):

        """
        Test case for template intent when trying to delete a non-existing template.

        This test case checks the behavior of the template intent when trying to delete a template that does not exist in the DNAC.
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
            "Template not found"
        )

    def test_template_intent_delete_template(self):

        """
        Test case for template intent when deleting a template.

        This test case checks the behavior of the template intent when deleting an existing template in the DNAC.
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
            result.get('response').get('progress'),
            "Successfully deleted template with name fd74ab6c-fdda-465e-9f59-fb7eac7d6b15"
        )

    def test_template_intent_missing_param(self):

        """
        Test case for template intent with missing parameters in the playbook.

        This test case checks the behavior of the template intent when the playbook contains missing required parameters.
        """

        set_module_args(
            dict(
                dnac_host="1.1.1.1",
                dnac_username="dummy",
                dnac_password="dummy",
                dnac_log=True,
                state="merged",
                config=self.playbook_config_missing_param
            )
        )
        result = self.execute_module(changed=False, failed=True)
        self.assertEqual(
            result.get('msg'),
            "missing required arguments: language or deviceTypes or softwareType"
        )

    def test_template_intent_invalid_state(self):

        """
        Test case for template intent with an invalid 'state' parameter.

        This test case checks the behavior of the template intent when an invalid 'state' parameter is provided in the playbook.
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

    def test_template_intent_invalid_param(self):

        """
        Test case for template intent with invalid parameters in the playbook.

        This test case checks the behavior of the template intent when the playbook contains invalid parameters.
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
        self.assertEqual(
            result.get('msg'),
            "Invalid parameters in playbook: velocty : Invalid choice provided"
        )
