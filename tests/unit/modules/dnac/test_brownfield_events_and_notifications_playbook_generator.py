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

from ansible_collections.cisco.dnac.plugins.modules import brownfield_events_and_notifications_playbook_generator
from .dnac_module import TestDnacModule, set_module_args, loadPlaybookData


class TestDnacBrownfieldEventsAndNotificationsPlaybookGenerator(TestDnacModule):

    module = brownfield_events_and_notifications_playbook_generator

    test_data = loadPlaybookData("brownfield_events_and_notifications_playbook_generator")

    playbook_generate_all_configurations = test_data.get("playbook_generate_all_configurations")
    playbook_component_specific_filters = test_data.get("playbook_component_specific_filters")
    playbook_invalid_filter = test_data.get("playbook_invalid_filter")
    playbook_specific_filter = test_data.get("playbook_specific_filter")

    def setUp(self):
        super(TestDnacBrownfieldEventsAndNotificationsPlaybookGenerator, self).setUp()

        self.mock_dnac_init = patch(
            "ansible_collections.cisco.dnac.plugins.module_utils.dnac.DNACSDK.__init__")
        self.run_dnac_init = self.mock_dnac_init.start()
        self.run_dnac_init.side_effect = [None]
        self.mock_dnac_exec = patch(
            "ansible_collections.cisco.dnac.plugins.module_utils.dnac.DNACSDK._exec"
        )
        self.run_dnac_exec = self.mock_dnac_exec.start()

    def tearDown(self):
        super(TestDnacBrownfieldEventsAndNotificationsPlaybookGenerator, self).tearDown()
        self.mock_dnac_exec.stop()
        self.mock_dnac_init.stop()

    def load_fixtures(self, response=None, device=""):
        """
        Load fixtures for user.
        """

        if "playbook_generate_all_configurations" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("webhook_destinations"),
                self.test_data.get("email_destinations"),
                self.test_data.get("syslog_destinations"),
                self.test_data.get("SNMP_destinations"),
                self.test_data.get("webhook_event_notifications"),
                self.test_data.get("get_event_artifacts"),
                self.test_data.get("email_event_notifications"),
                self.test_data.get("get_event_artifacts1"),
                self.test_data.get("syslog_event_notifications"),
                self.test_data.get("get_event_artifacts2"),
            ]

        if "playbook_invalid_filter" in self._testMethodName:
            pass

        if "playbook_component_specific_filters" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("webhook_destinations1"),
                self.test_data.get("webhook_event_notifications1"),
                self.test_data.get("get_event_artifacts3"),
            ]

        if "playbook_specific_filter" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("webhook"),
            ]

    def test_brownfield_events_and_notifications_playbook_generate_all_configurations(self):
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
                state="gathered",
                config_verify=True,
                dnac_version="2.3.7.6",
                config=self.playbook_generate_all_configurations
            )
        )
        result = self.execute_module(changed=True, failed=False)
        print(result)
        self.assertEqual(
            result.get("response"),
            "YAML config generation Task succeeded for module 'events_and_notifications_workflow_manager'."
        )

    def test_brownfield_events_and_notifications_playbook_component_specific_filters(self):
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
                state="gathered",
                config_verify=True,
                dnac_version="2.3.7.6",
                config=self.playbook_component_specific_filters
            )
        )
        result = self.execute_module(changed=True, failed=False)
        print(result)
        self.assertEqual(
            result.get("response"),
            "YAML config generation Task succeeded for module 'events_and_notifications_workflow_manager'."
        )

    def test_brownfield_events_and_notifications_playbook_invalid_filter(self):
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
                state="gathered",
                config_verify=True,
                dnac_version="2.3.7.6",
                config=self.playbook_invalid_filter
            )
        )
        result = self.execute_module(changed=False, failed=True)
        print(result)
        self.assertEqual(
            result.get("response"),
            "Invalid components found in components_list: ['webhook_destinatio']. "
            "Only the following components are allowed: "
            "['webhook_destinations', 'email_destinations', 'syslog_destinations', "
            "'snmp_destinations', 'itsm_settings', 'webhook_event_notifications', "
            "'email_event_notifications', 'syslog_event_notifications']. "
            "Please remove the invalid components and try again."
        )

    def test_brownfield_events_and_notifications_playbook_specific_filter(self):
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
                state="gathered",
                config_verify=True,
                dnac_version="2.3.7.6",
                config=self.playbook_specific_filter
            )
        )
        result = self.execute_module(changed=True, failed=False)
        print(result)
        self.assertEqual(
            result.get("response"),
            "YAML config generation Task succeeded for module 'events_and_notifications_workflow_manager'."
        )
