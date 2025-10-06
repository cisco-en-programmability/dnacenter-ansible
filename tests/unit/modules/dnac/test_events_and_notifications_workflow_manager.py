#  Copyright (c) 2025 Cisco and/or its affiliates.
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

# Authors:
#   Abhishek Maheswari <abmahesh@cisco.com>
#
# Description:
#   Unit tests for the Ansible module `events_and_notifications_workflow_manager`.
#   These tests cover the configuration of various destination like Syslog, SNMP,
#   Webhook, Email and ITSM and also the same for the notification subscription
#   of Email, Syslog and Webhook with create,update, deletion, and
#   validation logic using mocked Catalyst Center responses.
from __future__ import absolute_import, division, print_function

__metaclass__ = type
from unittest.mock import patch
from ansible_collections.cisco.dnac.plugins.modules import events_and_notifications_workflow_manager
from .dnac_module import TestDnacModule, set_module_args, loadPlaybookData


class TestEventsWorkflow(TestDnacModule):

    module = events_and_notifications_workflow_manager
    test_data = loadPlaybookData("events_and_notifications_workflow_manager")
    playbook_config_create_webhook_destination_with_verify = test_data.get("playbook_config_create_webhook_destination_with_verify")
    playbook_config_no_webhook_destination_update = test_data.get("playbook_config_no_webhook_destination_update")
    playbook_config_update_webhook_destination = test_data.get("playbook_config_update_webhook_destination")
    playbook_config_update_email_destination = test_data.get("playbook_config_update_email_destination")
    playbook_config_no_email_destination_update = test_data.get("playbook_config_no_email_destination_update")
    playbook_config_create_syslog_destination_with_verify = test_data.get("playbook_config_create_syslog_destination_with_verify")
    playbook_config_syslog_destination_no_update = test_data.get("playbook_config_syslog_destination_no_update")
    playbook_config_update_syslog_destination = test_data.get("playbook_config_update_syslog_destination")
    playbook_config_create_snmp_dest_with_verify = test_data.get("playbook_config_create_snmp_dest_with_verify")
    playbook_config_snmp_dest_no_update = test_data.get("playbook_config_snmp_dest_no_update")
    playbook_config_update_snmp_dest = test_data.get("playbook_config_update_snmp_dest")
    playbook_config_invalid_url_in_itsm = test_data.get("playbook_config_invalid_url_in_itsm")
    playbook_config_create_itsm_with_verify = test_data.get("playbook_config_create_itsm_with_verify")
    playbook_config_no_itsm_update = test_data.get("playbook_config_no_itsm_update")
    playbook_config_update_itsm_setting = test_data.get("playbook_config_update_itsm_setting")
    playbook_config_delete_itsm_with_verfiy = test_data.get("playbook_config_delete_itsm_with_verfiy")
    playbook_config_create_webhook_subscription_with_verify = test_data.get("playbook_config_create_webhook_subscription_with_verify")
    playbook_config_no_update_need_webhook_subscription = test_data.get("playbook_config_no_update_need_webhook_subscription")
    playbook_config_update_webhook_subscription = test_data.get("playbook_config_update_webhook_subscription")
    playbook_config_delete_webhook_subscription_with_verify = test_data.get("playbook_config_delete_webhook_subscription_with_verify")
    playbook_config_absent_webhook_subscription = test_data.get("playbook_config_absent_webhook_subscription")
    playbook_config_create_email_subscription_with_verify = test_data.get("playbook_config_create_email_subscription_with_verify")
    playbook_config_no_update_email_subscription = test_data.get("playbook_config_no_update_email_subscription")
    playbook_config_update_email_subscription = test_data.get("playbook_config_update_email_subscription")
    playbook_config_delete_email_subscription_with_verify = test_data.get("playbook_config_delete_email_subscription_with_verify")
    playbook_config_delete_absent_email_subscription = test_data.get("playbook_config_delete_absent_email_subscription")
    playbook_config_create_syslog_subscription_with_verify = test_data.get("playbook_config_create_syslog_subscription_with_verify")
    playbook_config_no_update_syslog_subscription = test_data.get("playbook_config_no_update_syslog_subscription")
    playbook_config_update_syslog_subscription = test_data.get("playbook_config_update_syslog_subscription")
    playbook_config_delete_syslog_subscription_with_verify = test_data.get("playbook_config_delete_syslog_subscription_with_verify")
    playbook_config_absent_syslog_subscription = test_data.get("playbook_config_absent_syslog_subscription")

    def setUp(self):
        super(TestEventsWorkflow, self).setUp()

        self.mock_dnac_init = patch(
            "ansible_collections.cisco.dnac.plugins.module_utils.dnac.DNACSDK.__init__")
        self.run_dnac_init = self.mock_dnac_init.start()
        self.run_dnac_init.side_effect = [None]
        self.mock_dnac_exec = patch(
            "ansible_collections.cisco.dnac.plugins.module_utils.dnac.DNACSDK._exec"
        )
        self.run_dnac_exec = self.mock_dnac_exec.start()
        self.load_fixtures()

    def tearDown(self):
        super(TestEventsWorkflow, self).tearDown()
        self.mock_dnac_exec.stop()
        self.mock_dnac_init.stop()

    def load_fixtures(self, response=None, device=""):
        """
        Load fixtures for user.
        """

        if "create_webhook_destination_with_verify" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("get_all_webhook_destinations"),
                Exception(),
                self.test_data.get("get_api_execution_response"),
                self.test_data.get("get_api_execution_response"),
                self.test_data.get("get_webhook_destinations_response"),
                Exception()
            ]

        elif "no_webhook_destination_update" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("get_webhook_destinations_response")
            ]

        elif "update_webhook_destination" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("get_webhook_destinations_response"),
                self.test_data.get("get_update_webhook_destination_response")
            ]

        elif "update_email_destination" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("get_email_destination_in_ccc"),
                self.test_data.get("get_events_status_url"),
                self.test_data.get("get_update_email_destination_response")
            ]

        elif "no_email_destination_update" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("get_updated_email_destination")
            ]

        elif "create_syslog_destination_with_verify" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("get_empty_syslog_destination"),
                self.test_data.get("create_syslog_destination_response"),
                self.test_data.get("get_syslog_details")
            ]

        elif "syslog_destination_no_update" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("get_syslog_details")
            ]

        elif "update_syslog_destination" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("get_syslog_details"),
                self.test_data.get("update_syslog_destination_response")
            ]

        elif "create_snmp_dest_with_verify" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("get_snmp_destinations"),
                self.test_data.get("get_empty_snmp_destination"),
                self.test_data.get("create_snmp_destination_response"),
                self.test_data.get("get_all_snmp_destinations")
            ]

        elif "snmp_dest_no_update" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("get_all_snmp_destinations")
            ]

        elif "update_snmp_dest" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("get_all_snmp_destinations"),
                self.test_data.get("update_snmp_destination_response")
            ]

        elif "invalid_url_in_itsm" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("get_empty_itsm_settings")
            ]

        elif "create_itsm_with_verify" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("get_empty_itsm_settings"),
                self.test_data.get("create_itsm_setting"),
                self.test_data.get("get_created_itsm_setting")
            ]

        elif "no_itsm_update" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("get_created_itsm_setting"),
                self.test_data.get("get_itsm_setting_by_id")
            ]

        elif "update_itsm_setting" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("get_created_itsm_setting"),
                self.test_data.get("get_itsm_setting_by_id"),
                self.test_data.get("update_itsm_setting")
            ]

        elif "delete_itsm_with_verfiy" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("get_updated_itsm_settings"),
                self.test_data.get("deleted_itsm_response"),
                self.test_data.get("get_empty_itsm_settings")
            ]

        elif "create_webhook_subscription_with_verify" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("empty_event_subscription"),
                self.test_data.get("get_rest_webhook_destination"),
                self.test_data.get("get_event_details_for_AP_Flap"),
                self.test_data.get("get_event_details_for_AP_reboot"),
                self.test_data.get("get_site_detail_india"),
                self.test_data.get("get_site_detail_usa"),
                self.test_data.get("create_webhook_status_url"),
                self.test_data.get("get_status_api_for_webhook_subs"),
                self.test_data.get("get_created_webhook_subscription")
            ]

        elif "no_update_need_webhook_subscription" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("get_created_webhook_subscription"),
                self.test_data.get("get_rest_webhook_destination"),
                self.test_data.get("get_event_details_for_AP_Flap"),
                self.test_data.get("get_event_details_for_AP_reboot"),
                self.test_data.get("get_site_detail_india"),
                self.test_data.get("get_site_detail_usa")
            ]

        elif "update_webhook_subscription" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("get_created_webhook_subscription"),
                self.test_data.get("get_rest_webhook_destination"),
                self.test_data.get("get_event_details_for_AP_Flap"),
                self.test_data.get("get_event_details_for_AP_reboot"),
                self.test_data.get("get_site_detail_india"),
                self.test_data.get("get_site_detail_usa"),
                self.test_data.get("create_webhook_status_url"),
                self.test_data.get("get_status_api_update_detail_webhook_subs")
            ]

        elif "delete_webhook_subscription_with_verify" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("get_updated_webhook_subs_details"),
                self.test_data.get("create_webhook_status_url"),
                self.test_data.get("delete_webhook_subscription"),
                self.test_data.get("empty_event_subscription")
            ]

        elif "absent_webhook_subscription" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("empty_event_subscription")
            ]

        elif "create_email_subscription_with_verify" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("empty_event_subscription"),
                self.test_data.get("get_email_instance_details"),
                self.test_data.get("get_event_details_for_AP_Flap"),
                self.test_data.get("get_event_details_for_AP_reboot"),
                self.test_data.get("get_site_detail_india"),
                self.test_data.get("get_site_detail_usa"),
                self.test_data.get("create_email_status_url"),
                self.test_data.get("get_email_subscription_creation_details"),
                self.test_data.get("created_email_subscription_details")
            ]

        elif "no_update_email_subscription" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("get_email_subscription_no_update_1"),
                self.test_data.get("get_email_instance_details"),
                self.test_data.get("get_event_details_for_AP_Flap"),
                self.test_data.get("get_event_details_for_AP_reboot"),
                self.test_data.get("get_site_detail_india"),
                self.test_data.get("get_site_detail_usa")
            ]

        elif "update_email_subscription" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("get_email_subscription_no_update_1"),
                self.test_data.get("get_email_instance_details"),
                self.test_data.get("get_event_details_for_AP_Flap"),
                self.test_data.get("get_event_details_for_AP_reboot"),
                self.test_data.get("get_site_detail_india"),
                self.test_data.get("get_site_detail_usa"),
                self.test_data.get("create_email_status_url"),
                self.test_data.get("get_status_api_update_detail_email_subs")
            ]

        elif "delete_email_subscription_with_verify" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("get_email_subscription_no_update_1"),
                self.test_data.get("create_email_status_url"),
                self.test_data.get("delete_email_subscription"),
                self.test_data.get("empty_event_subscription")
            ]

        elif "delete_absent_email_subscription" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("empty_event_subscription")
            ]

        elif "create_syslog_subscription_with_verify" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("empty_event_subscription"),
                self.test_data.get("get_syslog_destination_details"),
                self.test_data.get("get_event_details_for_AP_Flap"),
                self.test_data.get("get_event_details_for_AP_reboot"),
                self.test_data.get("get_site_detail_india"),
                self.test_data.get("get_site_detail_usa"),
                self.test_data.get("create_syslog_status_url"),
                self.test_data.get("get_status_api_for_syslog_subs"),
                self.test_data.get("get_created_syslog_subscription_details")
            ]

        elif "no_update_syslog_subscription" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("get_created_syslog_subscription_details"),
                self.test_data.get("get_syslog_destination_details"),
                self.test_data.get("get_event_details_for_AP_Flap"),
                self.test_data.get("get_event_details_for_AP_reboot"),
                self.test_data.get("get_site_detail_india"),
                self.test_data.get("get_site_detail_usa")
            ]

        elif "update_syslog_subscription" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("get_created_syslog_subscription_details"),
                self.test_data.get("get_syslog_destination_details"),
                self.test_data.get("get_event_details_for_AP_Flap"),
                self.test_data.get("get_event_details_for_AP_reboot"),
                self.test_data.get("get_site_detail_india"),
                self.test_data.get("get_site_detail_usa"),
                self.test_data.get("create_syslog_status_url"),
                self.test_data.get("get_status_api_update_detail_syslog_subs")
            ]

        elif "delete_syslog_subscription_with_verify" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("get_updated_syslog_subscription_details"),
                self.test_data.get("create_syslog_status_url"),
                self.test_data.get("get_delete_syslog_subscription_delete"),
                self.test_data.get("empty_event_subscription")
            ]

        elif "absent_syslog_subscription" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("empty_event_subscription")
            ]

    def test_events_and_notifications_workflow_manager_create_webhook_destination_with_verify(self):
        """
        Test case for events and notifications workflow manager when creating a webhook destination along with the verification.

        This test case checks the behavior of the events and notifications workflow manager when creating a new webhook destination
        along with the verification in the specified Catalyst Center.
        """

        set_module_args(
            dict(
                dnac_host="1.1.1.1",
                dnac_username="dummy",
                dnac_password="dummy",
                dnac_version="2.3.7.9",
                dnac_log=True,
                config_verify=True,
                state="merged",
                config=self.playbook_config_create_webhook_destination_with_verify
            )
        )
        result = self.execute_module(changed=True, failed=False)
        print(result)
        self.assertIn(
            "added successfully",
            result.get('msg')
        )

    def test_events_and_notifications_workflow_manager_no_webhook_destination_update(self):
        """
        Test case for events and notifications workflow manager when a webhook destination needs no update.

        This test case checks the behavior of the events and notifications workflow manager when a webhook destination
        needs no update in the specified Catalyst Center.
        """

        set_module_args(
            dict(
                dnac_host="1.1.1.1",
                dnac_username="dummy",
                dnac_password="dummy",
                dnac_version="2.3.7.9",
                dnac_log=True,
                config_verify=False,
                state="merged",
                config=self.playbook_config_no_webhook_destination_update
            )
        )
        result = self.execute_module(changed=False, failed=False)
        print(result)
        self.assertIn(
            "need no update",
            result.get('response')
        )

    def test_events_and_notifications_workflow_manager_update_webhook_destination(self):
        """
        Test case for events and notifications workflow manager when updating a webhook destination.

        This test case checks the behavior of the events and notifications workflow manager when updating a webhook destination
        in the specified Catalyst Center.
        """

        set_module_args(
            dict(
                dnac_host="1.1.1.1",
                dnac_username="dummy",
                dnac_password="dummy",
                dnac_version="2.3.7.9",
                dnac_log=True,
                config_verify=False,
                state="merged",
                config=self.playbook_config_update_webhook_destination
            )
        )
        result = self.execute_module(changed=True, failed=False)
        print(result)
        self.assertIn(
            "updated successfully",
            result.get('msg')
        )

    def test_events_and_notifications_workflow_manager_update_email_destination(self):
        """
        Test case for events and notifications workflow manager when updating an email destination.

        This test case checks the behavior of the events and notifications workflow manager when updating an email destination
        in the specified Catalyst Center.
        """

        set_module_args(
            dict(
                dnac_host="1.1.1.1",
                dnac_username="dummy",
                dnac_password="dummy",
                dnac_version="2.3.7.9",
                dnac_log=True,
                config_verify=False,
                state="merged",
                config=self.playbook_config_update_email_destination
            )
        )
        result = self.execute_module(changed=True, failed=False)
        print(result)
        self.assertIn(
            "updated successfully",
            result.get('response')
        )

    def test_events_and_notifications_workflow_manager_no_email_destination_update(self):
        """
        Test case for events and notifications workflow manager when an email destination needs no update.

        This test case checks the behavior of the events and notifications workflow manager when an email destination
        needs no update in the specified Catalyst Center.
        """

        set_module_args(
            dict(
                dnac_host="1.1.1.1",
                dnac_username="dummy",
                dnac_password="dummy",
                dnac_version="2.3.7.9",
                dnac_log=True,
                config_verify=False,
                state="merged",
                config=self.playbook_config_no_email_destination_update
            )
        )
        result = self.execute_module(changed=False, failed=False)
        print(result)
        self.assertIn(
            "need no update",
            result.get('response')
        )

    def test_events_and_notifications_workflow_manager_create_syslog_destination_with_verify(self):
        """
        Test case for events and notifications workflow manager when creating a syslog destination along with the verification.

        This test case checks the behavior of the events and notifications workflow manager when creating a new syslog destination
        along with the verification in the specified Catalyst Center.
        """

        set_module_args(
            dict(
                dnac_host="1.1.1.1",
                dnac_username="dummy",
                dnac_password="dummy",
                dnac_version="2.3.7.9",
                dnac_log=True,
                config_verify=True,
                state="merged",
                config=self.playbook_config_create_syslog_destination_with_verify
            )
        )
        result = self.execute_module(changed=True, failed=False)
        print(result)
        self.assertIn(
            "created successfully",
            result.get('response')
        )

    def test_events_and_notifications_workflow_manager_syslog_destination_no_update(self):
        """
        Test case for events and notifications workflow manager when a syslog destination needs no update.

        This test case checks the behavior of the events and notifications workflow manager when a syslog destination
        needs no update in the specified Catalyst Center.
        """

        set_module_args(
            dict(
                dnac_host="1.1.1.1",
                dnac_username="dummy",
                dnac_password="dummy",
                dnac_version="2.3.7.9",
                dnac_log=True,
                config_verify=False,
                state="merged",
                config=self.playbook_config_syslog_destination_no_update
            )
        )
        result = self.execute_module(changed=False, failed=False)
        print(result)
        self.assertIn(
            "need no update",
            result.get('response')
        )

    def test_events_and_notifications_workflow_manager_update_syslog_destination(self):
        """
        Test case for events and notifications workflow manager when updating a syslog destination.

        This test case checks the behavior of the events and notifications workflow manager when updating a syslog destination
        in the specified Catalyst Center.
        """

        set_module_args(
            dict(
                dnac_host="1.1.1.1",
                dnac_username="dummy",
                dnac_password="dummy",
                dnac_version="2.3.7.9",
                dnac_log=True,
                config_verify=False,
                state="merged",
                config=self.playbook_config_update_syslog_destination
            )
        )
        result = self.execute_module(changed=True, failed=False)
        print(result)
        self.assertIn(
            "updated successfully",
            result.get('response')
        )

    def test_events_and_notifications_workflow_manager_create_snmp_dest_with_verify(self):
        """
        Test case for events and notifications workflow manager when creating a snmp destination along with the verification.

        This test case checks the behavior of the events and notifications workflow manager when creating a new snmp destination
        along with the verification in the specified Catalyst Center.
        """

        set_module_args(
            dict(
                dnac_host="1.1.1.1",
                dnac_username="dummy",
                dnac_password="dummy",
                dnac_version="2.3.7.9",
                dnac_log=True,
                config_verify=True,
                state="merged",
                config=self.playbook_config_create_snmp_dest_with_verify
            )
        )
        result = self.execute_module(changed=True, failed=False)
        print(result)
        self.assertIn(
            "created successfully",
            result.get('response')
        )

    def test_events_and_notifications_workflow_manager_snmp_dest_no_update(self):
        """
        Test case for events and notifications workflow manager when a snmp destination needs no update.

        This test case checks the behavior of the events and notifications workflow manager when a snmp destination
        needs no update in the specified Catalyst Center.
        """

        set_module_args(
            dict(
                dnac_host="1.1.1.1",
                dnac_username="dummy",
                dnac_password="dummy",
                dnac_version="2.3.7.9",
                dnac_log=True,
                config_verify=False,
                state="merged",
                config=self.playbook_config_snmp_dest_no_update
            )
        )
        result = self.execute_module(changed=False, failed=False)
        print(result)
        self.assertIn(
            "need no update",
            result.get('response')
        )

    def test_events_and_notifications_workflow_manager_update_snmp_dest(self):
        """
        Test case for events and notifications workflow manager when updating a snmp destination.

        This test case checks the behavior of the events and notifications workflow manager when updating a snmp destination
        in the specified Catalyst Center.
        """

        set_module_args(
            dict(
                dnac_host="1.1.1.1",
                dnac_username="dummy",
                dnac_password="dummy",
                dnac_version="2.3.7.9",
                dnac_log=True,
                config_verify=False,
                state="merged",
                config=self.playbook_config_update_snmp_dest
            )
        )
        result = self.execute_module(changed=True, failed=False)
        print(result)
        self.assertIn(
            "updated successfully",
            result.get('response')
        )

    def test_events_and_notifications_workflow_manager_invalid_url_in_itsm(self):
        """
        Test case for events and notifications workflow manager when an invalid URL is provided for ITSM.

        This test case checks the behavior of the events and notifications workflow manager when an invalid URL is provided
        for ITSM in the specified Catalyst Center.
        """

        set_module_args(
            dict(
                dnac_host="1.1.1.1",
                dnac_username="dummy",
                dnac_password="dummy",
                dnac_version="2.3.7.9",
                dnac_log=True,
                config_verify=True,
                state="merged",
                config=self.playbook_config_invalid_url_in_itsm
            )
        )
        result = self.execute_module(changed=False, failed=True)
        print(result)
        self.assertIn(
            "is invalid url for ITSM",
            result.get('msg')
        )

    def test_events_and_notifications_workflow_manager_create_itsm_with_verify(self):
        """
        Test case for events and notifications workflow manager when creating an ITSM along with the verification.

        This test case checks the behavior of the events and notifications workflow manager when creating a new ITSM
        along with the verification in the specified Catalyst Center.
        """

        set_module_args(
            dict(
                dnac_host="1.1.1.1",
                dnac_username="dummy",
                dnac_password="dummy",
                dnac_version="2.3.7.9",
                dnac_log=True,
                config_verify=True,
                state="merged",
                config=self.playbook_config_create_itsm_with_verify
            )
        )
        result = self.execute_module(changed=True, failed=False)
        print(result)
        self.assertIn(
            "created successfully",
            result.get('response')
        )

    def test_events_and_notifications_workflow_manager_no_itsm_update(self):
        """
        Test case for events and notifications workflow manager when an ITSM needs no update.

        This test case checks the behavior of the events and notifications workflow manager when an ITSM
        needs no update in the specified Catalyst Center.
        """

        set_module_args(
            dict(
                dnac_host="1.1.1.1",
                dnac_username="dummy",
                dnac_password="dummy",
                dnac_version="2.3.7.9",
                dnac_log=True,
                config_verify=False,
                state="merged",
                config=self.playbook_config_no_itsm_update
            )
        )
        result = self.execute_module(changed=False, failed=False)
        print(result)
        self.assertIn(
            "need no update",
            result.get('response')
        )

    def test_events_and_notifications_workflow_manager_update_itsm_setting(self):
        """
        Test case for events and notifications workflow manager when updating an ITSM setting.

        This test case checks the behavior of the events and notifications workflow manager when updating an ITSM setting
        in the specified Catalyst Center.
        """

        set_module_args(
            dict(
                dnac_host="1.1.1.1",
                dnac_username="dummy",
                dnac_password="dummy",
                dnac_version="2.3.7.9",
                dnac_log=True,
                config_verify=False,
                state="merged",
                config=self.playbook_config_update_itsm_setting
            )
        )
        result = self.execute_module(changed=True, failed=False)
        print(result)
        self.assertIn(
            "updated successfully",
            result.get('response')
        )

    def test_events_and_notifications_workflow_manager_delete_itsm_with_verfiy(self):
        """
        Test case for events and notifications workflow manager when deleting an ITSM along with the verification.

        This test case checks the behavior of the events and notifications workflow manager when deleting an ITSM
        along with the verification in the specified Catalyst Center.
        """

        set_module_args(
            dict(
                dnac_host="1.1.1.1",
                dnac_username="dummy",
                dnac_password="dummy",
                dnac_version="2.3.7.9",
                dnac_log=True,
                config_verify=True,
                state="deleted",
                config=self.playbook_config_delete_itsm_with_verfiy
            )
        )
        result = self.execute_module(changed=True, failed=False)
        print(result)
        self.assertIn(
            "deleted successfully",
            result.get('response')
        )

    def test_events_and_notifications_workflow_manager_create_webhook_subscription_with_verify(self):
        """
        Test case for events and notifications workflow manager when creating a webhook subscription along with the verification.

        This test case checks the behavior of the events and notifications workflow manager when creating a new webhook subscription
        along with the verification in the specified Catalyst Center.
        """

        set_module_args(
            dict(
                dnac_host="1.1.1.1",
                dnac_username="dummy",
                dnac_password="dummy",
                dnac_version="2.3.7.9",
                dnac_log=True,
                config_verify=True,
                state="merged",
                config=self.playbook_config_create_webhook_subscription_with_verify
            )
        )
        result = self.execute_module(changed=True, failed=False)
        print(result)
        self.assertIn(
            "created successfully",
            result.get('response')
        )

    def test_events_and_notifications_workflow_manager_no_update_need_webhook_subscription(self):
        """
        Test case for events and notifications workflow manager when the webhook subscription does not need any update.

        This test case checks the behavior of the events and notifications workflow manager when the webhook subscription
        does not need any update in the specified Catalyst Center.
        """

        set_module_args(
            dict(
                dnac_host="1.1.1.1",
                dnac_username="dummy",
                dnac_password="dummy",
                dnac_version="2.3.7.9",
                dnac_log=True,
                config_verify=False,
                state="merged",
                config=self.playbook_config_no_update_need_webhook_subscription
            )
        )
        result = self.execute_module(changed=False, failed=False)
        print(result)
        self.assertIn(
            "need no update",
            result.get('response')
        )

    def test_events_and_notifications_workflow_manager_update_webhook_subscription(self):
        """
        Test case for events and notifications workflow manager when updating a webhook subscription.

        This test case checks the behavior of the events and notifications workflow manager when updating a webhook
        subscription in the specified Catalyst Center.
        """

        set_module_args(
            dict(
                dnac_host="1.1.1.1",
                dnac_username="dummy",
                dnac_password="dummy",
                dnac_version="2.3.7.9",
                dnac_log=True,
                config_verify=False,
                state="merged",
                config=self.playbook_config_update_webhook_subscription
            )
        )
        result = self.execute_module(changed=True, failed=False)
        print(result)
        self.assertIn(
            "updated successfully",
            result.get('response')
        )

    def test_events_and_notifications_workflow_manager_delete_webhook_subscription_with_verify(self):
        """
        Test case for events and notifications workflow manager when deleting a webhook subscription along with the verification.

        This test case checks the behavior of the events and notifications workflow manager when deleting a webhook subscription
        along with the verification in the specified Catalyst Center.
        """

        set_module_args(
            dict(
                dnac_host="1.1.1.1",
                dnac_username="dummy",
                dnac_password="dummy",
                dnac_version="2.3.7.9",
                dnac_log=True,
                config_verify=True,
                state="deleted",
                config=self.playbook_config_delete_webhook_subscription_with_verify
            )
        )
        result = self.execute_module(changed=True, failed=False)
        print(result)
        self.assertIn(
            "deleted successfully",
            result.get('response')
        )

    def test_events_and_notifications_workflow_manager_absent_webhook_subscription(self):
        """
        Test case for events and notifications workflow manager when the given webhook subscription is not present
        in the specified Catalyst Center..

        This test case checks the behavior of the events and notifications workflow manager when the given webhook
        subscription is not present in the specified Catalyst Center.
        """

        set_module_args(
            dict(
                dnac_host="1.1.1.1",
                dnac_username="dummy",
                dnac_password="dummy",
                dnac_version="2.3.7.9",
                dnac_log=True,
                config_verify=False,
                state="deleted",
                config=self.playbook_config_absent_webhook_subscription
            )
        )
        result = self.execute_module(changed=False, failed=False)
        print(result)
        self.assertIn(
            "Unable to delete",
            result.get('response')
        )

    def test_events_and_notifications_workflow_manager_create_email_subscription_with_verify(self):
        """
        Test case for events and notifications workflow manager when creating an email subscription along with the verification.

        This test case checks the behavior of the events and notifications workflow manager when creating a new email subscription
        along with the verification in the specified Catalyst Center.
        """

        set_module_args(
            dict(
                dnac_host="1.1.1.1",
                dnac_username="dummy",
                dnac_password="dummy",
                dnac_version="2.3.7.9",
                dnac_log=True,
                config_verify=True,
                state="merged",
                config=self.playbook_config_create_email_subscription_with_verify
            )
        )
        result = self.execute_module(changed=True, failed=False)
        print(result)
        self.assertIn(
            "created successfully",
            result.get('response')
        )

    def test_events_and_notifications_workflow_manager_no_update_email_subscription(self):
        """
        Test case for events and notifications workflow manager when an email subscription needs no update.

        This test case checks the behavior of the events and notifications workflow manager when an email subscription
        needs no update in the specified Catalyst Center.
        """

        set_module_args(
            dict(
                dnac_host="1.1.1.1",
                dnac_username="dummy",
                dnac_password="dummy",
                dnac_version="2.3.7.9",
                dnac_log=True,
                config_verify=False,
                state="merged",
                config=self.playbook_config_no_update_email_subscription
            )
        )
        result = self.execute_module(changed=False, failed=False)
        print(result)
        self.assertIn(
            "need no update",
            result.get('response')
        )

    def test_events_and_notifications_workflow_manager_update_email_subscription(self):
        """
        Test case for events and notifications workflow manager when updating an email subscription.

        This test case checks the behavior of the events and notifications workflow manager when updating an email subscription
        in the specified Catalyst Center.
        """

        set_module_args(
            dict(
                dnac_host="1.1.1.1",
                dnac_username="dummy",
                dnac_password="dummy",
                dnac_version="2.3.7.9",
                dnac_log=True,
                config_verify=False,
                state="merged",
                config=self.playbook_config_update_email_subscription
            )
        )
        result = self.execute_module(changed=True, failed=False)
        print(result)
        self.assertIn(
            "updated successfully",
            result.get('response')
        )

    def test_events_and_notifications_workflow_manager_delete_email_subscription_with_verify(self):
        """
        Test case for events and notifications workflow manager when deleting an email subscription along with the verification.

        This test case checks the behavior of the events and notifications workflow manager when deleting an email subscription
        along with the verification in the specified Catalyst Center.
        """

        set_module_args(
            dict(
                dnac_host="1.1.1.1",
                dnac_username="dummy",
                dnac_password="dummy",
                dnac_version="2.3.7.9",
                dnac_log=True,
                config_verify=True,
                state="deleted",
                config=self.playbook_config_delete_email_subscription_with_verify
            )
        )
        result = self.execute_module(changed=True, failed=False)
        print(result)
        self.assertIn(
            "deleted successfully",
            result.get('response')
        )

    def test_events_and_notifications_workflow_manager_delete_absent_email_subscription(self):
        """
        Test case for events and notifications workflow manager when the given email subscription is not present
        in the specified Catalyst Center.

        This test case checks the behavior of the events and notifications workflow manager when the given email
        subscription is not present in the specified Catalyst Center.
        """

        set_module_args(
            dict(
                dnac_host="1.1.1.1",
                dnac_username="dummy",
                dnac_password="dummy",
                dnac_version="2.3.7.9",
                dnac_log=True,
                config_verify=False,
                state="deleted",
                config=self.playbook_config_delete_absent_email_subscription
            )
        )
        result = self.execute_module(changed=False, failed=False)
        print(result)
        self.assertIn(
            "Unable to delete",
            result.get('response')
        )

    def test_events_and_notifications_workflow_manager_create_syslog_subscription_with_verify(self):
        """
        Test case for events and notifications workflow manager when creating a syslog subscription along with the verification.

        This test case checks the behavior of the events and notifications workflow manager when creating a new syslog subscription
        along with the verification in the specified Catalyst Center.
        """

        set_module_args(
            dict(
                dnac_host="1.1.1.1",
                dnac_username="dummy",
                dnac_password="dummy",
                dnac_version="2.3.7.9",
                dnac_log=True,
                config_verify=True,
                state="merged",
                config=self.playbook_config_create_syslog_subscription_with_verify
            )
        )
        result = self.execute_module(changed=True, failed=False)
        print(result)
        self.assertIn(
            "created successfully",
            result.get('response')
        )

    def test_events_and_notifications_workflow_manager_no_update_syslog_subscription(self):
        """
        Test case for events and notifications workflow manager when a syslog subscription needs no update.

        This test case checks the behavior of the events and notifications workflow manager when a syslog subscription
        needs no update in the specified Catalyst Center.
        """

        set_module_args(
            dict(
                dnac_host="1.1.1.1",
                dnac_username="dummy",
                dnac_password="dummy",
                dnac_version="2.3.7.9",
                dnac_log=True,
                config_verify=False,
                state="merged",
                config=self.playbook_config_no_update_syslog_subscription
            )
        )
        result = self.execute_module(changed=False, failed=False)
        print(result)
        self.assertIn(
            "need no update",
            result.get('response')
        )

    def test_events_and_notifications_workflow_manager_update_syslog_subscription(self):
        """
        Test case for events and notifications workflow manager when updating a syslog subscription.

        This test case checks the behavior of the events and notifications workflow manager when updating a syslog subscription
        in the specified Catalyst Center.
        """

        set_module_args(
            dict(
                dnac_host="1.1.1.1",
                dnac_username="dummy",
                dnac_password="dummy",
                dnac_version="2.3.7.9",
                dnac_log=True,
                config_verify=False,
                state="merged",
                config=self.playbook_config_update_syslog_subscription
            )
        )
        result = self.execute_module(changed=True, failed=False)
        print(result)
        self.assertIn(
            "updated successfully",
            result.get('response')
        )

    def test_events_and_notifications_workflow_manager_delete_syslog_subscription_with_verify(self):
        """
        Test case for events and notifications workflow manager when deleting a syslog subscription along with the verification.

        This test case checks the behavior of the events and notifications workflow manager when deleting a syslog subscription
        along with the verification in the specified Catalyst Center.
        """

        set_module_args(
            dict(
                dnac_host="1.1.1.1",
                dnac_username="dummy",
                dnac_password="dummy",
                dnac_version="2.3.7.9",
                dnac_log=True,
                config_verify=True,
                state="deleted",
                config=self.playbook_config_delete_syslog_subscription_with_verify
            )
        )
        result = self.execute_module(changed=True, failed=False)
        print(result)
        self.assertIn(
            "deleted successfully",
            result.get('response')
        )

    def test_events_and_notifications_workflow_manager_absent_syslog_subscription(self):
        """
        Test case for events and notifications workflow manager when the given syslog subscription is not present
        in the specified Catalyst Center.

        This test case checks the behavior of the events and notifications workflow manager when the given syslog
        subscription is not present in the specified Catalyst Center.
        """

        set_module_args(
            dict(
                dnac_host="1.1.1.1",
                dnac_username="dummy",
                dnac_password="dummy",
                dnac_version="2.3.7.9",
                dnac_log=True,
                config_verify=False,
                state="deleted",
                config=self.playbook_config_absent_syslog_subscription
            )
        )
        result = self.execute_module(changed=False, failed=False)
        print(result)
        self.assertIn(
            "Unable to delete",
            result.get('response')
        )
