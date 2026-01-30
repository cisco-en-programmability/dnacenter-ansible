# Copyright (c) 2025 Cisco and/or its affiliates.

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

from ansible_collections.cisco.dnac.plugins.modules import brownfield_user_role_playbook_generator
from .dnac_module import TestDnacModule, set_module_args, loadPlaybookData


class TestDnacBrownfieldUserRolePlaybookGenerator(TestDnacModule):

    module = brownfield_user_role_playbook_generator

    test_data = loadPlaybookData("brownfield_user_role_playbook_generator")

    playbook_user_role_details = test_data.get("playbook_user_role_details")
    playbook_specific_user_details = test_data.get("playbook_specific_user_details")
    playbook_specific_role_details = test_data.get("playbook_specific_role_details")
    playbook_generate_all_configurations = test_data.get("playbook_generate_all_configurations")
    playbook_invalid_components = test_data.get("playbook_invalid_components")
    playbook_all_role_details = test_data.get("playbook_all_role_details")

    def setUp(self):
        super(TestDnacBrownfieldUserRolePlaybookGenerator, self).setUp()

        self.mock_dnac_init = patch(
            "ansible_collections.cisco.dnac.plugins.module_utils.dnac.DNACSDK.__init__")
        self.run_dnac_init = self.mock_dnac_init.start()
        self.run_dnac_init.side_effect = [None]
        self.mock_dnac_exec = patch(
            "ansible_collections.cisco.dnac.plugins.module_utils.dnac.DNACSDK._exec"
        )
        self.run_dnac_exec = self.mock_dnac_exec.start()

    def tearDown(self):
        super(TestDnacBrownfieldUserRolePlaybookGenerator, self).tearDown()
        self.mock_dnac_exec.stop()
        self.mock_dnac_init.stop()

    def load_fixtures(self, response=None, device=""):
        """
        Load fixtures for user.
        """

        if "playbook_user_role_details" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("get_roles"),
                self.test_data.get("get_users"),
                self.test_data.get("get_roles_1"),
            ]

        elif "playbook_specific_user_details" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("get_users1"),
                self.test_data.get("get_roles2"),
            ]

        elif "playbook_specific_role_details" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("get_roles3")
            ]

        elif "playbook_generate_all_configurations" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("get_users2"),
                self.test_data.get("get_roles4"),
                self.test_data.get("get_roles5")
            ]

        elif "playbook_invalid_components" in self._testMethodName:
            pass

        elif "playbook_all_role_details" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("get_roles6"),
            ]

    def test_brownfield_user_role_playbook_generator_playbook_user_role_details(self):
        """
        Test the User Role Playbook Generator's ability to generate both user and role configurations.

        This test verifies that the workflow correctly handles the generation of YAML configuration
        for both user details and role details from Cisco Catalyst Center.
        """

        set_module_args(
            dict(
                dnac_host="1.1.1.1",
                dnac_username="dummy",
                dnac_password="dummy",
                dnac_log=True,
                state="gathered",
                dnac_version="2.3.7.9",
                config=self.playbook_user_role_details
            )
        )
        result = self.execute_module(changed=True, failed=False)
        print(result)
        self.assertEqual(
            result.get("response"),
            {
                "components_processed": 2,
                "components_skipped": 0,
                "configurations_count": 13,
                "file_path": "/Users/priyadharshini/Downloads/specific_userrole_details_info",
                "message": "YAML configuration file generated successfully for module 'user_role_workflow_manager'",
                "status": "success"
            }
        )

    def test_brownfield_user_role_playbook_generator_playbook_specific_user_details(self):
        """
        Test the User Role Playbook Generator's ability to generate specific user details.

        This test verifies that the workflow correctly handles the generation of YAML configuration
        for specific user details from Cisco Catalyst Center.
        """

        set_module_args(
            dict(
                dnac_host="1.1.1.1",
                dnac_username="dummy",
                dnac_password="dummy",
                dnac_log=True,
                state="gathered",
                dnac_version="2.3.7.9",
                config=self.playbook_specific_user_details
            )
        )
        result = self.execute_module(changed=True, failed=False)
        print(result)
        self.assertEqual(
            result.get("response"),
            {
                "components_processed": 1,
                "components_skipped": 0,
                "configurations_count": 1,
                "file_path": "/Users/priyadharshini/Downloads/specific_user_details1",
                "message": "YAML configuration file generated successfully for module 'user_role_workflow_manager'",
                "status": "success"
            }
        )

    def test_brownfield_user_role_playbook_generator_playbook_specific_role_details(self):
        """
        Test the User Role Playbook Generator's ability to generate specific role details.

        This test verifies that the workflow correctly handles the generation of YAML configuration
        for specific role details from Cisco Catalyst Center.
        """

        set_module_args(
            dict(
                dnac_host="1.1.1.1",
                dnac_username="dummy",
                dnac_password="dummy",
                dnac_log=True,
                state="gathered",
                dnac_version="2.3.7.9",
                config=self.playbook_specific_role_details
            )
        )
        result = self.execute_module(changed=True, failed=False)
        print(result)
        self.assertEqual(
            result.get("response"),
            {
                "components_processed": 1,
                "components_skipped": 0,
                "configurations_count": 1,
                "file_path": "/Users/priyadharshini/Downloads/specific_user_details1",
                "message": "YAML configuration file generated successfully for module 'user_role_workflow_manager'",
                "status": "success"
            }
        )

    def test_brownfield_user_role_playbook_generator_playbook_generate_all_configurations(self):
        """
        Test the User Role Playbook Generator's ability to generate all configurations.

        This test verifies that the workflow correctly handles the generation of YAML configuration
        for all user and role details from Cisco Catalyst Center.
        """

        set_module_args(
            dict(
                dnac_host="1.1.1.1",
                dnac_username="dummy",
                dnac_password="dummy",
                dnac_log=True,
                state="gathered",
                dnac_version="2.3.7.9",
                config=self.playbook_generate_all_configurations
            )
        )
        result = self.execute_module(changed=True, failed=False)
        print(result)
        self.assertEqual(
            result.get("response"),
            {
                "components_processed": 2,
                "components_skipped": 0,
                "configurations_count": 13,
                "file_path": "/Users/priyadharshini/Downloads/specific_user_details1",
                "message": "YAML configuration file generated successfully for module 'user_role_workflow_manager'",
                "status": "success"
            }
        )

    def test_brownfield_user_role_playbook_generator_playbook_invalid_components(self):
        """
        Test the User Role Playbook Generator's handling of invalid components.

        This test verifies that the workflow correctly identifies and reports invalid network
        components provided in the configuration.
        """

        set_module_args(
            dict(
                dnac_host="1.1.1.1",
                dnac_username="dummy",
                dnac_password="dummy",
                dnac_log=True,
                state="gathered",
                dnac_version="2.3.7.9",
                config=self.playbook_invalid_components
            )
        )
        result = self.execute_module(changed=False, failed=True)
        print(result)
        self.assertEqual(
            result.get("response"),
            "Invalid network components provided for module 'user_role_workflow_manager': "
            "['role_detailss']. Valid components are: ['user_details', 'role_details']"
        )

    def test_brownfield_user_role_playbook_all_role_details(self):
        """
        Test the User Role Playbook Generator's ability to generate all role details.

        This test verifies that the workflow correctly handles the generation of YAML configuration
        for all role details from Cisco Catalyst Center.
        """

        set_module_args(
            dict(
                dnac_host="1.1.1.1",
                dnac_username="dummy",
                dnac_password="dummy",
                dnac_log=True,
                state="gathered",
                dnac_version="3.1.3.0",
                config=self.playbook_all_role_details
            )
        )
        result = self.execute_module(changed=True, failed=False)
        print(result)
        self.assertEqual(
            result.get("response"),
            {
                "components_processed": 1,
                "components_skipped": 0,
                "configurations_count": 3,
                "file_path": "/Users/priyadharshini/Downloads/specific_user_details1",
                "message": "YAML configuration file generated successfully for module 'user_role_workflow_manager'",
                "status": "success"
            }
        )
