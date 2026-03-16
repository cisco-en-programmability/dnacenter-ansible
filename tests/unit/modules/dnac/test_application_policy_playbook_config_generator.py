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

from ansible_collections.cisco.dnac.plugins.modules import application_policy_playbook_config_generator
from .dnac_module import TestDnacModule, set_module_args, loadPlaybookData


class TestDnacApplicationPolicyPlaybookGenerator(TestDnacModule):

    module = application_policy_playbook_config_generator
    test_data = loadPlaybookData("application_policy_playbook_config_generator")

    playbook_queuing_profile = test_data.get("playbook_queuing_profile")
    playbook_application_policy = test_data.get("playbook_application_policy")
    playbook_different_bandwidth = test_data.get("playbook_different_bandwidth")
    playbook_wireless_policy = test_data.get("playbook_wireless_policy")

    def setUp(self):
        super(TestDnacApplicationPolicyPlaybookGenerator, self).setUp()

        self.mock_dnac_init = patch(
            "ansible_collections.cisco.dnac.plugins.module_utils.dnac.DNACSDK.__init__")
        self.run_dnac_init = self.mock_dnac_init.start()
        self.run_dnac_init.side_effect = [None]
        self.mock_dnac_exec = patch(
            "ansible_collections.cisco.dnac.plugins.module_utils.dnac.DNACSDK._exec"
        )
        self.run_dnac_exec = self.mock_dnac_exec.start()

    def tearDown(self):
        super(TestDnacApplicationPolicyPlaybookGenerator, self).tearDown()
        self.mock_dnac_exec.stop()
        self.mock_dnac_init.stop()

    def load_fixtures(self, response=None, device=""):
        """
        Load fixtures for user.
        """
        if "playbook_queuing_profile" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("queuing_profile")
            ]
        elif "playbook_application_policy" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("response1"),
                self.test_data.get("response2"),
                self.test_data.get("response3"),
                self.test_data.get("response4"),
                self.test_data.get("response5"),
                self.test_data.get("response6"),
                self.test_data.get("response7"),
                self.test_data.get("response8"),
                self.test_data.get("response9"),
                self.test_data.get("response10"),
                self.test_data.get("response11"),
                self.test_data.get("response12"),
                self.test_data.get("response13"),
                self.test_data.get("response14"),
                self.test_data.get("response15"),
                self.test_data.get("response16"),
                self.test_data.get("response17"),
                self.test_data.get("response18"),
                self.test_data.get("response19"),
                self.test_data.get("response20"),
                self.test_data.get("response21"),
                self.test_data.get("response22"),
                self.test_data.get("response23"),
                self.test_data.get("response24"),
                self.test_data.get("response25"),
                self.test_data.get("response26"),
                self.test_data.get("response27"),
                self.test_data.get("response28"),
                self.test_data.get("response29"),
                self.test_data.get("response30"),
                self.test_data.get("response31"),
                self.test_data.get("response32"),
                self.test_data.get("response33")
            ]

        elif "playbook_different_bandwidth" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("get_queuing_profile")
            ]

        elif "playbook_wireless_policy" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("response50"),
                self.test_data.get("response51"),
                self.test_data.get("response52"),
                self.test_data.get("response53"),
                self.test_data.get("response54"),
                self.test_data.get("response55"),
                self.test_data.get("response56"),
                self.test_data.get("response57"),
                self.test_data.get("response58"),
                self.test_data.get("response59"),
                self.test_data.get("response60"),
                self.test_data.get("response61"),
                self.test_data.get("response62"),
                self.test_data.get("response63"),
                self.test_data.get("response64"),
                self.test_data.get("response65"),
                self.test_data.get("response66"),
                self.test_data.get("response67"),
                self.test_data.get("response68"),
                self.test_data.get("response69"),
                self.test_data.get("response70"),
                self.test_data.get("response71"),
                self.test_data.get("response72"),
                self.test_data.get("response73"),
                self.test_data.get("response74"),
                self.test_data.get("response75"),
                self.test_data.get("response76"),
                self.test_data.get("response77"),
                self.test_data.get("response78"),
                self.test_data.get("response79"),
                self.test_data.get("response80"),
            ]

    def test_backup_and_restore_workflow_manager_playbook_queuing_profile(self):
        """
        Test case for creating a scheduled backup in Cisco Catalyst Center.
        Verifies that the workflow manager correctly creates and schedules
        a backup when the specified configuration is applied.
        """

        set_module_args(
            dict(
                dnac_host="1.1.1.1",
                dnac_username="dummy",
                dnac_password="dummy",
                dnac_log=True,
                state="gathered",
                dnac_version="3.1.3.0",
                config=self.playbook_queuing_profile
            )
        )
        result = self.execute_module(changed=True, failed=False)
        print(result)
        self.assertEqual(
            result.get("msg"),
            "YAML config generation succeeded for module 'application_policy_workflow_manager'."
        )

    def test_backup_and_restore_workflow_manager_playbook_application_policy(self):
        """
        Test case for creating a scheduled backup in Cisco Catalyst Center.
        Verifies that the workflow manager correctly creates and schedules
        a backup when the specified configuration is applied.
        """

        set_module_args(
            dict(
                dnac_host="1.1.1.1",
                dnac_username="dummy",
                dnac_password="dummy",
                dnac_log=True,
                state="gathered",
                dnac_version="3.1.3.0",
                config=self.playbook_application_policy
            )
        )
        result = self.execute_module(changed=True, failed=False)
        print(result)
        self.assertEqual(
            result.get("msg"),
            "YAML config generation succeeded for module 'application_policy_workflow_manager'."
        )

    def test_backup_and_restore_workflow_manager_playbook_different_bandwidth(self):
        """
        Test case for creating a scheduled backup in Cisco Catalyst Center.
        Verifies that the workflow manager correctly creates and schedules
        a backup when the specified configuration is applied.
        """

        set_module_args(
            dict(
                dnac_host="1.1.1.1",
                dnac_username="dummy",
                dnac_password="dummy",
                dnac_log=True,
                state="gathered",
                dnac_version="3.1.3.0",
                config=self.playbook_different_bandwidth
            )
        )
        result = self.execute_module(changed=True, failed=False)
        print(result)
        self.assertEqual(
            result.get("msg"),
            "YAML config generation succeeded for module 'application_policy_workflow_manager'."
        )

    def test_backup_and_restore_workflow_manager_playbook_wireless_policy(self):
        """
        Test case for creating a scheduled backup in Cisco Catalyst Center.
        Verifies that the workflow manager correctly creates and schedules
        a backup when the specified configuration is applied.
        """

        set_module_args(
            dict(
                dnac_host="1.1.1.1",
                dnac_username="dummy",
                dnac_password="dummy",
                dnac_log=True,
                state="gathered",
                dnac_version="3.1.3.0",
                config=self.playbook_wireless_policy
            )
        )
        result = self.execute_module(changed=True, failed=False)
        print(result)
        self.assertEqual(
            result.get("msg"),
            "YAML config generation succeeded for module 'application_policy_workflow_manager'."
        )
