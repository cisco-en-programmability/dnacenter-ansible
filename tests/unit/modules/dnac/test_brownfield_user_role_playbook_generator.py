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

    def test_brownfield_user_role_playbook_generator_playbook_user_role_details(self):
        """
        Test the Application Policy Workflow Manager's profile creation process.

        This test verifies that the workflow correctly handles the creation of a new
        application policy profile, ensuring proper validation and expected behavior.
        """

        set_module_args(
            dict(
                dnac_host="1.1.1.1",
                dnac_username="dummy",
                dnac_password="dummy",
                dnac_log=True,
                state="merged",
                config_verify=True,
                dnac_version="2.3.7.9",
                config=self.playbook_user_role_details
            )
        )
        result = self.execute_module(changed=True, failed=False)
        print("-------###########----------")
        print(result)
        self.assertEqual(
            result.get("response"),
                {
                    "YAML config generation Task succeeded for module 'user_role_workflow_manager'.": {
                        "file_path": "/Users/priyadharshini/Downloads/specific_userrole_details_info"
                    }
                }
        )
