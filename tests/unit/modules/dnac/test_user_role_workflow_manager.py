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

from ansible_collections.cisco.dnac.plugins.modules import user_role_workflow_manager
from .dnac_module import TestDnacModule, set_module_args, loadPlaybookData


class TestDnacUserRoleWorkflowManager(TestDnacModule):

    module = user_role_workflow_manager

    test_data = loadPlaybookData("user_role_workflow_manager")

    playbook_config_user = test_data.get("playbook_config_user")
    playbook_config_delete_existing_user = test_data.get("playbook_config_delete_existing_user")
    playbook_config_invalid_param_mandatory_field_not_present = test_data.get("playbook_config_invalid_param_mandatory_field_not_present")
    playbook_config_invalid_param_username_email_not_present = test_data.get("playbook_config_invalid_param_username_email_not_present")
    playbook_config_invalid_param_username_not_correct_formate = test_data.get("playbook_config_invalid_param_username_not_correct_formate")
    playbook_config_invalid_param_user_rolelist_not_type_list = test_data.get("playbook_config_invalid_param_user_rolelist_not_type_list")
    playbook_config_invalid_param_firstname_not_correct_formate = test_data.get("playbook_config_invalid_param_firstname_not_correct_formate")
    playbook_config_invalid_param_lastname_not_correct_formate = test_data.get("playbook_config_invalid_param_lastname_not_correct_formate")
    playbook_config_invalid_param_email_not_correct_formate = test_data.get("playbook_config_invalid_param_email_not_correct_formate")
    playbook_config_invalid_param_password_not_correct_formate = test_data.get("playbook_config_invalid_param_password_not_correct_formate")
    playbook_config_user_invalid_param_rolelist_not_found = test_data.get("playbook_config_user_invalid_param_rolelist_not_found")
    playbook_config_role = test_data.get("playbook_config_role")
    playbook_config_1_role = test_data.get("playbook_config_1_role")
    playbook_config_invalid_param_rolename_not_present = test_data.get("playbook_config_invalid_param_rolename_not_present")
    playbook_config_invalid_param_role_not_type_list = test_data.get("playbook_config_invalid_param_role_not_type_list")
    playbook_config_invalid_param_with_all_permision_deny = test_data.get("playbook_config_invalid_param_with_all_permision_deny")
    playbook_config_invalid_param_rolename_not_correct_formate = test_data.get("playbook_config_invalid_param_rolename_not_correct_formate")
    playbook_config_invalid_param_type_list_missing = test_data.get("playbook_config_invalid_param_type_list_missing")
    playbook_config_invalid_param_role_invalid_permission = test_data.get("playbook_config_invalid_param_role_invalid_permission")
    playbook_config_for_creating_default_role = test_data.get("playbook_config_for_creating_default_role")
    playbook_config_invalid_invalid_param_state = test_data.get("playbook_config_invalid_invalid_param_state")

    def setUp(self):
        super(TestDnacUserRoleWorkflowManager, self).setUp()

        self.mock_dnac_init = patch(
            "ansible_collections.cisco.dnac.plugins.module_utils.dnac.DNACSDK.__init__")
        self.run_dnac_init = self.mock_dnac_init.start()
        self.run_dnac_init.side_effect = [None]
        self.mock_dnac_exec = patch(
            "ansible_collections.cisco.dnac.plugins.module_utils.dnac.DNACSDK._exec"
        )
        self.run_dnac_exec = self.mock_dnac_exec.start()

    def tearDown(self):
        super(TestDnacUserRoleWorkflowManager, self).tearDown()
        self.mock_dnac_exec.stop()
        self.mock_dnac_init.stop()

    def load_fixtures(self, response=None, device=""):
        """
        Load fixtures for user.
        """
        if "create_user" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("create_get_user_response"),
                self.test_data.get("create_user_get_role_response"),
                self.test_data.get("create_user_response")
            ]
        elif "user_update_needed" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("update_needed_get_user_response"),
                self.test_data.get("update_user_needed_get_role_response"),
                self.test_data.get("update_needed_user_response")
            ]
        elif "user_update_not_needed" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("update_not_needed_get_user_response"),
                self.test_data.get("update_user_not_needed_get_role_response"),
                self.test_data.get("update_not_needed_user_response")
            ]
        elif "delete_existing_user" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("delete_existing_get_user_response"),
                self.test_data.get("delete_existing_user_get_role_response"),
                self.test_data.get("delete_existing_user_response")
            ]
        elif "delete_non_existing_user" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("delete_non_existing_get_user_response"),
                self.test_data.get("delete_non_existing_user_get_role_response"),
                self.test_data.get("delete_non_existing_user_response")
            ]
        elif "user_invalid_mandatory_field_not_present_param" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("invalid_param_mandatory_field_not_present_get_user_response"),
                self.test_data.get("invalid_param_mandatory_field_not_present_get_role_response"),
                Exception(),
                self.test_data.get("user_invalid_mandatory_field_not_present_param_responce")
            ]
        elif "user_invalid_username_email_not_present_param" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("user_invalid_username_email_not_present_param_responce")
            ]
        elif "user_invalid_param_not_correct_formate" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("invalid_param_not_correct_formate_get_user_response"),
                self.test_data.get("invalid_param_not_correct_formate_get_role_response"),
                self.test_data.get("user_invalid_param_not_correct_formate_responce")
            ]
        elif "user_invalid_param_not_type_list" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("user_invalid_param_not_type_list_response")
            ]
        elif "user_invalid_param_rolelist_not_found" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("invalid_param_rolelist_not_found_get_user_response"),
                self.test_data.get("invalid_param_rolelist_not_found_get_role_response"),
                self.test_data.get("user_invalid_param_rolelist_not_found_responce")
            ]
        elif "user_invalid_param_update_rolelist_not_found" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("invalid_param_update_rolelist_not_found_get_user_response"),
                self.test_data.get("invalid_param_rolelist_not_found_get_role_response"),
                self.test_data.get("user_invalid_param_update_rolelist_not_found_responce")
            ]
        elif "create_role" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("create_get_role_response"),
                self.test_data.get("create_role_response")
            ]
        elif "create_1_role" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("create_1_get_role_response"),
                self.test_data.get("create_1_role_response")
            ]
        elif "role_update_needed" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("update_needed_get_role_response"),
                self.test_data.get("update_needed_role_response")
            ]
        elif "role_update_not_needed" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("update_not_needed_get_role_response"),
                self.test_data.get("update_not_needed_role_response")
            ]
        elif "delete_existing_role" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("delete_existing_get_role_response"),
                self.test_data.get("delete_existing_role_response")
            ]
        elif "delete_non_existing_role" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("delete_non_existing_get_role_response"),
                self.test_data.get("delete_non_existing_role_response")
            ]
        elif "role_invalid_param_rolename_not_present" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("role_invalid_rolename_not_present_param_response")
            ]
        elif "role_invalid_param_not_type_list" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("role_invalid_param_not_type_list_response")
            ]
        elif "role_param_with_all_permision_deny" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("role_param_with_all_permision_deny_get_role_responce"),
                Exception(),
                self.test_data.get("role_param_with_all_permision_deny_responce")
            ]
        elif "role_invalid_param_rolename_not_correct_formate" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("invalid_param_rolename_not_correct_formate_get_role_responce"),
                self.test_data.get("role_invalid_param_rolename_not_correct_formate_responce")
            ]
        elif "invalid_param_type_list_missing" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("invalid_param_type_list_missing_response")
            ]
        elif "invalid_param_role_invalid_permission" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("invalid_param_invalid_permission_role_get_response"),
                self.test_data.get("invalid_param_role_invalid_permission_response")
            ]
        elif "invalid_param_role_update_invalid_permission" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("invalid_param_invalid_permission_update_role_get_response"),
                self.test_data.get("invalid_param_role_update_invalid_permission_response")
            ]
        elif "create_default_role" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("create_default_get_role_response"),
                self.test_data.get("create_default_role_response")
            ]
        elif "invalid_param_state" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("invalid_param_state_responce"),
            ]

    def test_user_role_workflow_manager_create_user(self):
        """
        Test case for user role workflow manager when creating a user.

        This test case checks the behavior of the user workflow when creating a new user in the specified Cisco Catalyst Center.
        """
        set_module_args(
            dict(
                dnac_host="1.1.1.1",
                dnac_username="dummy",
                dnac_password="dummy",
                dnac_version="2.3.7.9",
                dnac_log=True,
                state="merged",
                config=self.playbook_config_user
            )
        )
        result = self.execute_module(changed=True, failed=False)
        print(result)
        self.assertEqual(
            result.get('response'),
            "User(s) 'ajithandrewj' created successfully in Cisco Catalyst Center."
        )

    def test_user_role_workflow_manager_user_update_needed(self):
        """
        Test case for user role workflow manager when updating a user.

        This test case checks the behavior of the user workflow when updating a user in the specified Cisco Catalyst Center.
        """
        set_module_args(
            dict(
                dnac_host="1.1.1.1",
                dnac_username="dummy",
                dnac_password="dummy",
                dnac_version="2.3.7.9",
                dnac_log=True,
                state="merged",
                config=self.playbook_config_user
            )
        )
        result = self.execute_module(changed=True, failed=False)
        print(result)
        self.assertEqual(
            result.get('response'),
            "User(s) 'ajithandrewj' updated successfully in Cisco Catalyst Center."
        )

    def test_user_role_workflow_manager_user_update_not_needed(self):
        """
        Test case for user role workflow manager when user update not needed.

        This test case checks the behavior of the user workflow when user update not needed in the specified Cisco Catalyst Center.
        """
        set_module_args(
            dict(
                dnac_host="1.1.1.1",
                dnac_username="dummy",
                dnac_password="dummy",
                dnac_version="2.3.7.9",
                dnac_log=True,
                state="merged",
                config=self.playbook_config_user
            )
        )
        result = self.execute_module(changed=False, failed=False)
        print(result)
        self.assertEqual(
            result.get('response'),
            "User(s) 'ajithandrewj' need no update in Cisco Catalyst Center."
        )

    def test_user_role_workflow_manager_delete_existing_user(self):
        """
        Test case for user role workflow manager when deleting a user.

        This test case checks the behavior of the user workflow when deleting a user in the specified Cisco Catalyst Center.
        """
        set_module_args(
            dict(
                dnac_host="1.1.1.1",
                dnac_username="dummy",
                dnac_password="dummy",
                dnac_version="2.3.7.9",
                dnac_log=True,
                state="deleted",
                config=self.playbook_config_delete_existing_user
            )
        )
        result = self.execute_module(changed=True, failed=False)
        print(result)
        self.assertEqual(
            result.get('response'),
            "User(s) 'ajithandrewj' deleted successfully from the Cisco Catalyst Center."
        )

    def test_user_role_workflow_manager_delete_non_existing_user(self):
        """
        Test case for user role workflow manager when deleting a non existing user.

        This test case checks the behavior of the user workflow when deleting a non existing user in the specified Cisco Catalyst Center.
        """
        set_module_args(
            dict(
                dnac_host="1.1.1.1",
                dnac_username="dummy",
                dnac_password="dummy",
                dnac_version="2.3.7.9",
                dnac_log=True,
                state="deleted",
                config=self.playbook_config_user
            )
        )
        result = self.execute_module(changed=False, failed=False)
        print(result)
        self.assertEqual(
            result.get("response"),
            "The specified user 'ajithandrewj' does not exist in Cisco Catalyst Center. Please provide a valid 'username' or 'email' for user deletion."
        )

    def test_user_role_workflow_manager_user_invalid_mandatory_field_not_present_param(self):
        """
        Test case for user workflow manager when invalid user param given.

        This test case checks the behavior of the user workflow when invalid user param given in the specified Cisco Catalyst Center.
        """
        set_module_args(
            dict(
                dnac_host="1.1.1.1",
                dnac_username="dummy",
                dnac_password="dummy",
                dnac_version="2.3.7.9",
                dnac_log=True,
                state="merged",
                config=self.playbook_config_invalid_param_mandatory_field_not_present
            )
        )
        result = self.execute_module(changed=False, failed=True)
        print(result)
        self.assertEqual(
            result.get("msg"),
            "Mandatory parameter(s) 'username, password' not present in the user details."
        )

    def test_user_role_workflow_manager_user_invalid_username_email_not_present_param(self):
        """
        Test case for user workflow manager when invalid user param given.

        This test case checks the behavior of the user workflow when invalid user param given in the specified Cisco Catalyst Center.
        """
        set_module_args(
            dict(
                dnac_host="1.1.1.1",
                dnac_username="dummy",
                dnac_password="dummy",
                dnac_version="2.3.7.9",
                dnac_log=True,
                state="merged",
                config=self.playbook_config_invalid_param_username_email_not_present
            )
        )
        result = self.execute_module(changed=False, failed=True)
        print(result)
        self.assertEqual(
            result.get("msg"),
            "'Configuration parameters such as 'username', 'email', or 'role_name' are missing from the playbook' or 'The 'user_details' \
key is invalid for role creation, updation, or deletion' or 'The 'role_details' key is invalid for user creation, updation, or deletion'"
        )

    def test_user_role_workflow_manager_user_invalid_param_not_correct_formate(self):
        """
        Test case for user workflow manager when invalid user param given.

        This test case checks the behavior of the user workflow when invalid user param given in the specified Cisco Catalyst Center.
        """
        set_module_args(
            dict(
                dnac_host="1.1.1.1",
                dnac_username="dummy",
                dnac_password="dummy",
                dnac_version="2.3.7.9",
                dnac_log=True,
                state="merged",
                config=self.playbook_config_invalid_param_username_not_correct_formate
            )
        )
        result = self.execute_module(changed=False, failed=True)
        print(result.get("msg"))
        self.assertEqual(
            result.get("msg"),
            "Invalid parameters in playbook config: first_name: First name 'ajith ' can have alphanumeric "
            "characters only and must be 2 to 50 characters long., "
            "last_name: Last name 'andrew ' can have alphanumeric characters only and must be 2 to 50 characters long., "
            "The password must be 9 to 20 characters long and include at least three of the following character types: "
            "lowercase letters, uppercase letters, digits, and special characters. "
            "Additionally, the password must not contain repetitive or sequential characters., "
            "username: 'ajithandrewj ' The username must not contain any special characters and must be 3 to 50 characters long."
        )

    def test_user_role_workflow_manager_user_invalid_param_not_type_list(self):
        """
        Test case for user role workflow manager when invalid user param given.

        This test case checks the behavior of the role workflow when invalid user param given in the specified Cisco Calyst Center.
        """
        set_module_args(
            dict(
                dnac_host="1.1.1.1",
                dnac_username="dummy",
                dnac_password="dummy",
                dnac_version="2.3.7.9",
                dnac_log=True,
                state="merged",
                config=self.playbook_config_invalid_param_user_rolelist_not_type_list
            )
        )
        result = self.execute_module(changed=False, failed=True)
        print(result)
        self.assertEqual(
            result.get('msg'),
            "Invalid parameter(s) found in playbook: Super-Admin-Role : is not a valid list"
        )

    def test_user_role_workflow_manager_user_invalid_param_rolelist_not_found(self):
        """
        Test case for user role workflow manager when invalid user param given.

        This test case checks the behavior of the role workflow when invalid user param given in the specified Cisco Calyst Center.
        """
        set_module_args(
            dict(
                dnac_host="1.1.1.1",
                dnac_username="dummy",
                dnac_password="dummy",
                dnac_version="2.3.7.9",
                dnac_log=True,
                state="merged",
                config=self.playbook_config_user_invalid_param_rolelist_not_found
            )
        )
        result = self.execute_module(changed=False, failed=True)
        print(result)
        self.assertEqual(
            result.get('msg'),
            "The role name in the user details role_list is not present in the Cisco Catalyst Center, Please provide a valid role name"
        )

    def test_user_role_workflow_manager_user_invalid_param_update_rolelist_not_found(self):
        """
        Test case for user role workflow manager when invalid user param given.

        This test case checks the behavior of the role workflow when invalid user param given in the specified Cisco Calyst Center.
        """
        set_module_args(
            dict(
                dnac_host="1.1.1.1",
                dnac_username="dummy",
                dnac_password="dummy",
                dnac_version="2.3.7.9",
                dnac_log=True,
                state="merged",
                config=self.playbook_config_user_invalid_param_rolelist_not_found
            )
        )
        result = self.execute_module(changed=False, failed=True)
        print(result)
        self.assertEqual(
            result.get('msg'),
            "The role name in the user details 'role_list' is not present in the Cisco Catalyst Center. Please provide a valid role name."
        )

    def test_user_role_workflow_manager_create_role(self):
        """
        Test case for user role workflow manager when creating a role.

        This test case checks the behavior of the role workflow when creating a new role in the specified Cisco Calyst Center.
        """
        set_module_args(
            dict(
                dnac_host="1.1.1.1",
                dnac_username="dummy",
                dnac_password="dummy",
                dnac_version="2.3.7.9",
                dnac_log=True,
                state="merged",
                config=self.playbook_config_role
            )
        )
        result = self.execute_module(changed=True, failed=False)
        print(result)
        self.assertEqual(
            result.get('response'),
            "Role(s) 'Test_Role_1' created successfully in Cisco Catalyst Center."
        )

    def test_user_role_workflow_manager_create_1_role(self):
        """
        Test case for user role workflow manager when creating a role.

        This test case checks the behavior of the role workflow when creating a new role in the specified Cisco Calyst Center.
        """
        set_module_args(
            dict(
                dnac_host="1.1.1.1",
                dnac_username="dummy",
                dnac_password="dummy",
                dnac_version="2.3.7.9",
                dnac_log=True,
                state="merged",
                config=self.playbook_config_1_role
            )
        )
        result = self.execute_module(changed=True, failed=False)
        print(result)
        self.assertEqual(
            result.get('response'),
            "Role(s) 'Test_Role_1' created successfully in Cisco Catalyst Center."
        )

    def test_user_role_workflow_manager_role_update_needed(self):
        """
        Test case for user role workflow manager when update for a role is needed.

        This test case checks the behavior of the role workflow when updating a existing role in the specified Cisco Calyst Center.
        """
        set_module_args(
            dict(
                dnac_host="1.1.1.1",
                dnac_username="dummy",
                dnac_password="dummy",
                dnac_version="2.3.7.9",
                dnac_log=True,
                state="merged",
                config=self.playbook_config_role
            )
        )
        result = self.execute_module(changed=True, failed=False)
        print(result)
        self.assertEqual(
            result.get('response'),
            "Role(s) 'Test_Role_1' updated successfully in Cisco Catalyst Center."
        )

    def test_user_role_workflow_manager_role_update_not_needed(self):
        """
        Test case for user role workflow manager when update is not needed for a role .

        This test case checks the behavior of the role workflow when update is not needed for a role in the specified Cisco Calyst Center.
        """
        set_module_args(
            dict(
                dnac_host="1.1.1.1",
                dnac_username="dummy",
                dnac_password="dummy",
                dnac_version="2.3.7.9",
                dnac_log=True,
                state="merged",
                config=self.playbook_config_role
            )
        )
        result = self.execute_module(changed=False, failed=False)
        print(result)
        self.assertEqual(
            result.get('response'),
            "Role(s) 'Test_Role_1' need no update in Cisco Catalyst Center."
        )

    def test_user_role_workflow_manager_delete_existing_role(self):
        """
        Test case for user role workflow manager when deleting a role.

        This test case checks the behavior of the role workflow when deleting a role in the specified Cisco Calyst Center.
        """
        set_module_args(
            dict(
                dnac_host="1.1.1.1",
                dnac_username="dummy",
                dnac_password="dummy",
                dnac_version="2.3.7.9",
                dnac_log=True,
                state="deleted",
                config=self.playbook_config_role
            )
        )
        result = self.execute_module(changed=True, failed=False)
        print(result)
        self.assertEqual(
            result.get('response'),
            "Role(s) 'Test_Role_1' deleted successfully from the Cisco Catalyst Center."
        )

    def test_user_role_workflow_manager_delete_non_existing_role(self):
        """
        Test case for user role workflow manager when deleting a non existing role.

        This test case checks the behavior of the role workflow when deleting a non existing role in the specified Cisco Calyst Center.
        """
        set_module_args(
            dict(
                dnac_host="1.1.1.1",
                dnac_username="dummy",
                dnac_password="dummy",
                dnac_version="2.3.7.9",
                dnac_log=True,
                state="deleted",
                config=self.playbook_config_role
            )
        )
        result = self.execute_module(changed=False, failed=False)
        print(result)
        self.assertEqual(
            result.get('response'),
            "The specified role 'Test_Role_1' does not exist in Cisco Catalyst Center. Please provide a valid 'role_name' for user deletion."
        )

    def test_user_role_workflow_manager_role_invalid_param_rolename_not_present(self):
        """
        Test case for user role workflow manager when invalid role param given.

        This test case checks the behavior of the role workflow when invalid role param given in the specified Cisco Calyst Center.
        """
        set_module_args(
            dict(
                dnac_host="1.1.1.1",
                dnac_username="dummy",
                dnac_password="dummy",
                dnac_version="2.3.7.9",
                dnac_log=True,
                state="merged",
                config=self.playbook_config_invalid_param_rolename_not_present
            )
        )
        result = self.execute_module(changed=False, failed=True)
        print(result)
        self.assertEqual(
            result.get('msg'),
            "'Configuration parameters such as 'username', 'email', or 'role_name' are missing from the playbook' or 'The 'user_details' \
key is invalid for role creation, updation, or deletion' or 'The 'role_details' key is invalid for user creation, updation, or deletion'"
        )

    def test_user_role_workflow_manager_role_invalid_param_not_type_list(self):
        """
        Test case for user role workflow manager when invalid role param given.

        This test case checks the behavior of the role workflow when invalid role param given in the specified Cisco Calyst Center.
        """
        set_module_args(
            dict(
                dnac_host="1.1.1.1",
                dnac_username="dummy",
                dnac_password="dummy",
                dnac_version="2.3.7.9",
                dnac_log=True,
                state="merged",
                config=self.playbook_config_invalid_param_role_not_type_list
            )
        )
        result = self.execute_module(changed=False, failed=True)
        print(result)
        self.assertEqual(
            result.get('msg'),
            "Invalid parameter(s) found in playbook: {'overall': 'read'} : is not a valid list"
        )

    def test_user_role_workflow_manager_role_param_with_all_permision_deny(self):
        """
        Test case for user role workflow manager when invalid role param given.

        This test case checks the behavior of the role workflow when invalid role param given in the specified Cisco Calyst Center.
        """
        set_module_args(
            dict(
                dnac_host="1.1.1.1",
                dnac_username="dummy",
                dnac_password="dummy",
                dnac_version="2.3.7.9",
                dnac_log=True,
                state="merged",
                config=self.playbook_config_invalid_param_with_all_permision_deny
            )
        )
        result = self.execute_module(changed=False, failed=True)
        print(result)
        self.assertEqual(
            result.get('msg'),
            "The Catalyst Center user 'dummy' does not have the necessary permissions to 'create a role' through the API."
        )

    def test_user_role_workflow_manager_role_invalid_param_rolename_not_correct_formate(self):
        """
        Test case for user workflow manager when invalid role param given.

        This test case checks the behavior of the user workflow when invalid role param given in the specified Cisco Catalyst Center.
        """
        set_module_args(
            dict(
                dnac_host="1.1.1.1",
                dnac_username="dummy",
                dnac_password="dummy",
                dnac_version="2.3.7.9",
                dnac_log=True,
                state="merged",
                config=self.playbook_config_invalid_param_rolename_not_correct_formate
            )
        )
        result = self.execute_module(changed=False, failed=True)
        print(result)
        self.assertEqual(
            result.get("msg"),
            "Invalid parameters in playbook config: role_name: 'Test_Role_1 ' Role names must be 1 to 25 characters long and should contain only letters, \
numbers, periods, underscores, and hyphens."
        )

    def test_user_role_workflow_manager_invalid_param_type_list_missing(self):
        """
        Test case for user workflow manager when invalid role param given.

        This test case checks the behavior of the user workflow when invalid role param given in the specified Cisco Catalyst Center.
        """
        set_module_args(
            dict(
                dnac_host="1.1.1.1",
                dnac_username="dummy",
                dnac_password="dummy",
                dnac_version="2.3.7.9",
                dnac_log=True,
                state="merged",
                config=self.playbook_config_invalid_param_type_list_missing
            )
        )
        result = self.execute_module(changed=False, failed=True)
        print(result)
        self.assertEqual(
            result.get("msg"),
            "Configuration is not available in the playbook for validation or user/role details are not type list"
        )

    def test_user_role_workflow_manager_invalid_param_role_invalid_permission(self):
        """
        Test case for user workflow manager when invalid role param given.

        This test case checks the behavior of the user workflow when invalid role param given in the specified Cisco Catalyst Center.
        """
        set_module_args(
            dict(
                dnac_host="1.1.1.1",
                dnac_username="dummy",
                dnac_password="dummy",
                dnac_version="2.3.7.9",
                dnac_log=True,
                state="merged",
                config=self.playbook_config_invalid_param_role_invalid_permission
            )
        )
        result = self.execute_module(changed=False, failed=True)
        print(result)
        self.assertEqual(
            result.get("msg"),
            "Invalid permission 'aaa' for assurance resource 'overall' under the role 'None'"
        )

    def test_user_role_workflow_manager_invalid_param_role_update_invalid_permission(self):
        """
        Test case for user workflow manager when invalid role param given.

        This test case checks the behavior of the user workflow when invalid role param given in the specified Cisco Catalyst Center.
        """
        set_module_args(
            dict(
                dnac_host="1.1.1.1",
                dnac_username="dummy",
                dnac_password="dummy",
                dnac_version="2.3.7.9",
                dnac_log=True,
                state="merged",
                config=self.playbook_config_invalid_param_role_invalid_permission
            )
        )
        result = self.execute_module(changed=False, failed=True)
        print(result)
        self.assertEqual(
            result.get("msg"),
            "Invalid permission 'aaa' for assurance resource 'overall' under the role 'Test_Role_1'"
        )

    def test_user_role_workflow_manager_create_default_role(self):
        """
        Test case for user role workflow manager when update is not needed for a role .

        This test case checks the behavior of the role workflow when update is not needed for a role in the specified Cisco Calyst Center.
        """
        set_module_args(
            dict(
                dnac_host="1.1.1.1",
                dnac_username="dummy",
                dnac_password="dummy",
                dnac_version="2.3.7.9",
                dnac_log=True,
                state="merged",
                config=self.playbook_config_for_creating_default_role
            )
        )
        result = self.execute_module(changed=True, failed=False)
        print(f"result --> {result}")
        self.assertEqual(
            result.get('response'),
            "Role(s) 'default_role' created successfully in Cisco Catalyst Center."
        )

    def test_user_role_workflow_manager_invalid_param_state(self):
        """
        Test case for user role workflow manager when update is not needed for a role .

        This test case checks the behavior of the role workflow when update is not needed for a role in the specified Cisco Calyst Center.
        """
        set_module_args(
            dict(
                dnac_host="1.1.1.1",
                dnac_username="dummy",
                dnac_password="dummy",
                dnac_version="2.3.7.9",
                dnac_log=True,
                state="mergeddd",
                config=self.playbook_config_invalid_invalid_param_state
            )
        )
        result = self.execute_module(changed=False, failed=True)
        print(f"result --> {result}")
        self.assertEqual(
            result.get('msg'),
            "value of state must be one of: merged, deleted, got: mergeddd"
        )
