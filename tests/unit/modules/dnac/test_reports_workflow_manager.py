# Copyright (c) 2025 Cisco and/or its affiliates.
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

# common approach when a module relies on optional dependencies that are not available during the validation process.
try:
    import pytz  # pylint: disable=unused-import
    HAS_PYTZ = True
except ImportError:
    HAS_PYTZ = False
    pytz = None
import unittest
from unittest.mock import patch
from ansible_collections.cisco.dnac.plugins.modules import reports_workflow_manager
from .dnac_module import TestDnacModule, set_module_args, loadPlaybookData


class TestDnacreportsWorkflow(TestDnacModule):
    module = reports_workflow_manager
    test_data = loadPlaybookData("reports_workflow_manager")
    playbook_config_create = test_data.get("playbook_config_create")
    playbook_config_missing_schedule_type = test_data.get("playbook_config_missing_schedule_type")
    playbook_config_schedule_later = test_data.get("playbook_config_schedule_later")
    playbook_config_schedule_recurrance = test_data.get("playbook_config_schedule_recurrance")
    playbook_config_schedule_recurrance_weekly = test_data.get("playbook_config_schedule_recurrance_weekly")
    playbook_config_schedule_recurrance_weekly_daily = test_data.get("playbook_config_schedule_recurrance_weekly_daily")

    def setUp(self):
        super(TestDnacreportsWorkflow, self).setUp()
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
        super(TestDnacreportsWorkflow, self).tearDown()
        self.mock_dnac_exec.stop()
        self.mock_dnac_init.stop()

    def load_fixtures(self, response=None, device=""):
        """
        Load fixtures for user.
        """
        if "error_fetching_KPI_detail" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("get_kpi_details"),
            ]

        if "create_n_schedule_reports_download" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("create_get_all_view_groups"),
                self.test_data.get("create_get_views_for_a_given_view_group"),
                self.test_data.get("create_get_list_of_scheduled_reports"),
                self.test_data.get("create_get_view_details_for_a_given_view_group_and_view"),
                self.test_data.get("create_n_schedule_reports"),
                self.test_data.get("download_get_execution_id_for_report"),
                Exception(),
            ]

        if "delete_reports" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("create_get_all_view_groups"),
                self.test_data.get("create_get_views_for_a_given_view_group"),
                self.test_data.get("delete_get_list_of_scheduled_reports"),
                self.test_data.get("delete_report"),
                self.test_data.get("create_get_all_view_groups"),
                self.test_data.get("create_get_views_for_a_given_view_group"),
                self.test_data.get("create_get_list_of_scheduled_reports"),
            ]

        if "download_report" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("create_get_all_view_groups"),
                self.test_data.get("create_get_views_for_a_given_view_group"),
                self.test_data.get("later_create_get_list_of_scheduled_reports"),
                self.test_data.get("create_get_view_details_for_a_given_view_group_and_view"),
                self.test_data.get("download_get_execution_id_for_report"),
            ]

        if "missing_schedule_type " in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("create_get_all_view_groups"),
                self.test_data.get("create_get_views_for_a_given_view_group"),
                self.test_data.get("create_get_list_of_scheduled_reports"),
                self.test_data.get("create_get_view_details_for_a_given_view_group_and_view"),
                self.test_data.get("create_n_schedule_reports"),
                Exception(),
            ]

        if "schedule_later" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("create_get_all_view_groups"),
                self.test_data.get("create_get_views_for_a_given_view_group"),
                self.test_data.get("create_get_list_of_scheduled_reports"),
                self.test_data.get("create_get_view_details_for_a_given_view_group_and_view"),
                self.test_data.get("create_n_schedule_reports"),
                self.test_data.get("create_get_all_view_groups"),
                self.test_data.get("create_get_views_for_a_given_view_group"),
                self.test_data.get("delete_get_list_of_scheduled_reports"),
                self.test_data.get("create_get_view_details_for_a_given_view_group_and_view"),
            ]

        if "RECURRENCE_monthly" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("create_get_all_view_groups"),
                self.test_data.get("create_get_views_for_a_given_view_group"),
                self.test_data.get("create_get_list_of_scheduled_reports"),
                self.test_data.get("create_get_view_details_for_a_given_view_group_and_view"),
                self.test_data.get("create_n_schedule_reports"),
                self.test_data.get("create_get_all_view_groups"),
                self.test_data.get("create_get_views_for_a_given_view_group"),
                self.test_data.get("delete_get_list_of_scheduled_reports"),
                self.test_data.get("create_get_view_details_for_a_given_view_group_and_view"),
            ]

        if "RECURRENCE_weekly" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("create_get_all_view_groups"),
                self.test_data.get("create_get_views_for_a_given_view_group"),
                self.test_data.get("create_get_list_of_scheduled_reports"),
                self.test_data.get("create_get_view_details_for_a_given_view_group_and_view"),
                self.test_data.get("create_n_schedule_reports"),
                self.test_data.get("create_get_all_view_groups"),
                self.test_data.get("create_get_views_for_a_given_view_group"),
                self.test_data.get("delete_get_list_of_scheduled_reports"),
                self.test_data.get("create_get_view_details_for_a_given_view_group_and_view"),
            ]

        if "RECUR_daily" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("create_get_all_view_groups"),
                self.test_data.get("create_get_views_for_a_given_view_group"),
                self.test_data.get("create_get_list_of_scheduled_reports"),
                self.test_data.get("create_get_view_details_for_a_given_view_group_and_view"),
                self.test_data.get("create_n_schedule_reports"),
                self.test_data.get("create_get_all_view_groups"),
                self.test_data.get("create_get_views_for_a_given_view_group"),
                self.test_data.get("delete_get_list_of_scheduled_reports"),
                self.test_data.get("create_get_view_details_for_a_given_view_group_and_view"),
            ]

    @unittest.skipIf(not HAS_PYTZ, "pytz is not installed")
    def test_reports_workflow_manager_create_n_schedule_reports_download(self):
        """
        Test case for reports workflow manager when creating and scheduling reports for download.

        Verifies that the reports workflow manager correctly handles the creation and scheduling of reports
        for download, ensuring the system behaves as expected during this process.
        """

        set_module_args(
            dict(
                dnac_host="1.1.1.1",
                dnac_username="dummy",
                dnac_password="dummy",
                dnac_log=True,
                state="merged",
                dnac_version="3.1.3.0",
                config_verify=True,
                config=self.playbook_config_create
            )
        )
        result = self.execute_module(changed=True, failed=True)
        print(result['response'])
        self.assertIn(
            "Failed to download report 'compliance_report_test1'",
            result['response']
        )

    def test_reports_workflow_manager_delete_reports(self):
        """
        Test case for reports workflow manager when creating and scheduling reports for download.

        Verifies that the reports workflow manager correctly handles the creation and scheduling of reports
        for download, ensuring the system behaves as expected during this process.
        """

        set_module_args(
            dict(
                dnac_host="1.1.1.1",
                dnac_username="dummy",
                dnac_password="dummy",
                dnac_log=True,
                state="deleted",
                dnac_version="3.1.3.0",
                config_verify=True,
                config=self.playbook_config_create
            )
        )
        result = self.execute_module(changed=True, failed=False)
        print(result['response'])
        delete_msg = result["response"][0]["delete_report"]["msg"]
        self.assertIn(
            "Report 'compliance_report_test1' has been successfully deleted.",
            delete_msg
        )

    @unittest.skipUnless(HAS_PYTZ, "pytz is required for timezone validation tests")
    def test_reports_workflow_manager_download_report(self):
        """
        Test case for reports workflow manager when creating and scheduling reports for download.

        Verifies that the reports workflow manager correctly handles the creation and scheduling of reports
        for download, ensuring the system behaves as expected during this process.
        """

        set_module_args(
            dict(
                dnac_host="1.1.1.1",
                dnac_username="dummy",
                dnac_password="dummy",
                dnac_log=True,
                state="merged",
                dnac_version="3.1.3.0",
                config_verify=True,
                config=self.playbook_config_create
            )
        )
        result = self.execute_module(changed=False, failed=True)
        print(result['response'])
        self.assertIn(
            "An error occurred while downloading the report",
            result['response']
        )

    def test_reports_workflow_manager_missing_schedule_type(self):
        """
        Test case for reports workflow manager when creating and scheduling reports for download.

        Verifies that the reports workflow manager correctly handles the creation and scheduling of reports
        for download, ensuring the system behaves as expected during this process.
        """

        set_module_args(
            dict(
                dnac_host="1.1.1.1",
                dnac_username="dummy",
                dnac_password="dummy",
                dnac_log=True,
                state="merged",
                dnac_version="3.1.3.0",
                config_verify=True,
                config=self.playbook_config_missing_schedule_type
            )
        )
        result = self.execute_module(changed=False, failed=True)
        print(result)
        self.assertIn(
            "Invalid parameters in playbook: ['schedule_type : Required parameter not found']",
            result['response']
        )

    @unittest.skipUnless(HAS_PYTZ, "pytz is required for timezone validation tests")
    def test_reports_workflow_manager_schedule_later(self):
        """
        Test case for reports workflow manager when creating and scheduling reports for download.

        Verifies that the reports workflow manager correctly handles the creation and scheduling of reports
        for download, ensuring the system behaves as expected during this process.
        """

        set_module_args(
            dict(
                dnac_host="1.1.1.1",
                dnac_username="dummy",
                dnac_password="dummy",
                dnac_log=True,
                state="merged",
                dnac_version="3.1.3.0",
                config_verify=True,
                config=self.playbook_config_schedule_later
            )
        )
        result = self.execute_module(changed=True, failed=False)
        print(result['response'][0]["create_report"]["msg"])
        self.assertIn(
            "Successfully created or scheduled report 'compliance_report_test1'.",
            result['response'][0]["create_report"]["msg"]
        )

    @unittest.skipUnless(HAS_PYTZ, "pytz is required for timezone validation tests")
    def test_reports_workflow_manager_schedule_RECURRENCE_monthly(self):
        """
        Test case for reports workflow manager when creating and scheduling reports for download.

        Verifies that the reports workflow manager correctly handles the creation and scheduling of reports
        for download, ensuring the system behaves as expected during this process.
        """

        set_module_args(
            dict(
                dnac_host="1.1.1.1",
                dnac_username="dummy",
                dnac_password="dummy",
                dnac_log=True,
                state="merged",
                dnac_version="3.1.3.0",
                config_verify=True,
                config=self.playbook_config_schedule_recurrance
            )
        )
        result = self.execute_module(changed=True, failed=False)
        print(result['response'][0]["create_report"]["msg"])
        self.assertIn(
            "Successfully created or scheduled report 'compliance_report_test1'.",
            result['response'][0]["create_report"]["msg"]
        )

    @unittest.skipUnless(HAS_PYTZ, "pytz is required for timezone validation tests")
    def test_reports_workflow_manager_schedule_RECURRENCE_weekly(self):
        """
        Test case for reports workflow manager when creating and scheduling reports for download.

        Verifies that the reports workflow manager correctly handles the creation and scheduling of reports
        for download, ensuring the system behaves as expected during this process.
        """

        set_module_args(
            dict(
                dnac_host="1.1.1.1",
                dnac_username="dummy",
                dnac_password="dummy",
                dnac_log=True,
                state="merged",
                dnac_version="3.1.3.0",
                config_verify=True,
                config=self.playbook_config_schedule_recurrance_weekly
            )
        )
        result = self.execute_module(changed=True, failed=False)
        print(result['response'][0]["create_report"]["msg"])
        self.assertIn(
            "Successfully created or scheduled report 'compliance_report_test1'.",
            result['response'][0]["create_report"]["msg"]
        )

    @unittest.skipUnless(HAS_PYTZ, "pytz is required for timezone validation tests")
    def test_reports_workflow_manager_schedule_RECUR_daily(self):
        """
        Test case for reports workflow manager when creating and scheduling reports with daily recurrence.
        """

        set_module_args(
            dict(
                dnac_host="1.1.1.1",
                dnac_username="dummy",
                dnac_password="dummy",
                dnac_log=True,
                state="merged",
                dnac_version="3.1.3.0",
                config_verify=False,
                config=self.playbook_config_schedule_recurrance_weekly_daily
            )
        )
        result = self.execute_module(changed=True, failed=False)
        print(result['response'][0]["create_report"]["msg"])
        self.assertIn(
            "Successfully created or scheduled report 'compliance_report_check'.",
            result['response'][0]["create_report"]["msg"]
        )
