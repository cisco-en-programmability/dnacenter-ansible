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
from unittest.mock import patch
from ansible_collections.cisco.dnac.plugins.modules import network_compliance_workflow_manager
from .dnac_module import TestDnacModule, set_module_args, loadPlaybookData


class TestNetworkCompliance(TestDnacModule):

    module = network_compliance_workflow_manager

    test_data = loadPlaybookData("network_compliance_workflow_manager")

    def setUp(self):
        super(TestNetworkCompliance, self).setUp()

        self.mock_dnac_init = patch(
            "ansible_collections.cisco.dnac.plugins.module_utils.dnac.DNACSDK.__init__")
        self.run_dnac_init = self.mock_dnac_init.start()
        self.run_dnac_init.side_effect = [None]
        self.mock_dnac_exec = patch(
            "ansible_collections.cisco.dnac.plugins.module_utils.dnac.DNACSDK._exec"
        )
        self.run_dnac_exec = self.mock_dnac_exec.start()
        self.load_fixtures()

        print(f"Mock for DNACSDK._exec: {self.run_dnac_exec}")

    def tearDown(self):
        super(TestNetworkCompliance, self).tearDown()
        self.mock_dnac_init.stop()
        self.mock_dnac_exec.stop()

    def load_fixtures(self, response=None, device=""):
        print("Inside load_fixtures")
        # FIXTURE FOR SUCCESS TESTCASES ############################################################

        # Run full compliance using an IP Address list
        if "run_compliance_with_iplist" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("response_get_device_list_success"),
                self.test_data.get("response_get_compliance_details_of_device_1"),
                self.test_data.get("response_run_compliance_success"),
                self.test_data.get("response_get_task_by_id_success"),
                self.test_data.get("response_get_compliance_details_of_device_1"),
            ]

        # Run full compliance using Site
        if "run_compliance_with_site" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("response_get_site_success"),
                self.test_data.get("response_get_membership_success"),
                self.test_data.get("response_get_compliance_details_of_device_1"),
                self.test_data.get("response_get_compliance_details_of_device_2"),
                self.test_data.get("response_get_compliance_details_of_device_3"),
                self.test_data.get("response_get_compliance_details_of_device_4"),
                self.test_data.get("response_get_compliance_details_of_device_5"),
                self.test_data.get("response_get_compliance_details_of_device_6"),
                self.test_data.get("response_run_compliance_success"),
                self.test_data.get("response_get_task_by_id_success"),
                self.test_data.get("response_get_compliance_details_of_device_1"),
                self.test_data.get("response_get_compliance_details_of_device_2"),
                self.test_data.get("response_get_compliance_details_of_device_3"),
                self.test_data.get("response_get_compliance_details_of_device_4"),
                self.test_data.get("response_get_compliance_details_of_device_5"),
                self.test_data.get("response_get_compliance_details_of_device_6"),
            ]

        # Run full compliance using both IP Address and Site
        if "run_compliance_with_iplist_site" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("response_get_site_success"),
                self.test_data.get("response_get_membership_success"),
                self.test_data.get("response_get_device_list_success"),
                self.test_data.get("response_get_compliance_details_of_device_1"),
                self.test_data.get("response_get_compliance_details_of_device_2"),
                self.test_data.get("response_get_compliance_details_of_device_3"),
                self.test_data.get("response_get_compliance_details_of_device_4"),
                self.test_data.get("response_get_compliance_details_of_device_5"),
                self.test_data.get("response_get_compliance_details_of_device_6"),
                self.test_data.get("response_run_compliance_success"),
                self.test_data.get("response_get_task_by_id_success"),
                self.test_data.get("response_get_compliance_details_of_device_1"),
                self.test_data.get("response_get_compliance_details_of_device_2"),
                self.test_data.get("response_get_compliance_details_of_device_3"),
                self.test_data.get("response_get_compliance_details_of_device_4"),
                self.test_data.get("response_get_compliance_details_of_device_5"),
                self.test_data.get("response_get_compliance_details_of_device_6"),
            ]

        # Run compliance against specific categories using IP Address List
        if "run_compliance_categories_iplist" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("response_get_device_list_success"),
                self.test_data.get("response_get_compliance_details_of_device_category_1_1"),
                self.test_data.get("response_get_compliance_details_of_device_category_1_2"),
                self.test_data.get("response_get_compliance_details_of_device_category_1_3"),
                self.test_data.get("response_get_compliance_details_of_device_category_1_4"),
                self.test_data.get("response_run_compliance_success"),
                self.test_data.get("response_get_task_by_id_success"),
                self.test_data.get("response_get_compliance_details_of_device_category_1_1"),
                self.test_data.get("response_get_compliance_details_of_device_category_1_2"),
                self.test_data.get("response_get_compliance_details_of_device_category_1_3"),
                self.test_data.get("response_get_compliance_details_of_device_category_1_4"),
            ]

        # Scale - Run full compliance operation
        if "scale_run_compliance" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("response_get_device_list_success"),
                self.test_data.get("response_get_device_list_success_2"),
                self.test_data.get("response_get_compliance_details_of_device_1"),
                self.test_data.get("response_get_compliance_details_of_device_2"),
                self.test_data.get("response_run_compliance_success"),
                self.test_data.get("response_run_compliance_success_2"),
                self.test_data.get("response_get_task_by_id_success"),
                self.test_data.get("response_get_task_by_id_success_2"),
                self.test_data.get("response_get_compliance_details_of_device_1"),
                self.test_data.get("response_get_compliance_details_of_device_2"),
            ]

        # Run Sync Device Config using IP Address list - Sync Required (Devices with RUNNING_CONFIG status - 'NON_COMPLIANT')
        if "sync_device_config_iplist" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("response_get_device_list_success"),
                self.test_data.get("response_get_compliance_details_of_device_1_running_config"),
                self.test_data.get("response_commit_device_configuration"),
                self.test_data.get("response_get_task_tree_success"),
                self.test_data.get("response_get_compliance_details_of_device_1_running_config_2")
            ]

        # Run Sync Device Config using Site - Sync Required (Devices with RUNNING_CONFIG status - 'NON_COMPLIANT')
        if "sync_device_config_site" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("response_get_site_success"),
                self.test_data.get("response_get_membership_success"),
                self.test_data.get("response_get_compliance_details_of_device_1_running_config"),
                self.test_data.get("response_get_compliance_details_of_device_2_running_config"),
                self.test_data.get("response_get_compliance_details_of_device_3_running_config"),
                self.test_data.get("response_get_compliance_details_of_device_4_running_config"),
                self.test_data.get("response_get_compliance_details_of_device_5_running_config"),
                self.test_data.get("response_get_compliance_details_of_device_6_running_config"),
                self.test_data.get("response_commit_device_configuration"),
                self.test_data.get("response_get_task_tree_success"),
                self.test_data.get("response_get_compliance_details_of_device_1_running_config_2"),
                self.test_data.get("response_get_compliance_details_of_device_2_running_config_2"),
                self.test_data.get("response_get_compliance_details_of_device_3_running_config_2"),
                self.test_data.get("response_get_compliance_details_of_device_4_running_config_2"),
                self.test_data.get("response_get_compliance_details_of_device_5_running_config_2"),
                self.test_data.get("response_get_compliance_details_of_device_6_running_config_2")
            ]

        # Run Sync Device Config using both IP Address List and Site - Sync Required (Devices with RUNNING_CONFIG status - 'NON_COMPLIANT')
        if "sync_device_config_iplist_site" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("response_get_site_success"),
                self.test_data.get("response_get_membership_success"),
                self.test_data.get("response_get_device_list_success"),
                self.test_data.get("response_get_compliance_details_of_device_1_running_config"),
                self.test_data.get("response_get_compliance_details_of_device_2_running_config"),
                self.test_data.get("response_get_compliance_details_of_device_3_running_config"),
                self.test_data.get("response_get_compliance_details_of_device_4_running_config"),
                self.test_data.get("response_get_compliance_details_of_device_5_running_config"),
                self.test_data.get("response_get_compliance_details_of_device_6_running_config"),
                self.test_data.get("response_commit_device_configuration"),
                self.test_data.get("response_get_task_tree_success"),
                self.test_data.get("response_get_compliance_details_of_device_1_running_config_2"),
                self.test_data.get("response_get_compliance_details_of_device_2_running_config_2"),
                self.test_data.get("response_get_compliance_details_of_device_3_running_config_2"),
                self.test_data.get("response_get_compliance_details_of_device_4_running_config_2"),
                self.test_data.get("response_get_compliance_details_of_device_5_running_config_2"),
                self.test_data.get("response_get_compliance_details_of_device_6_running_config_2")
            ]

        # Run Sync Device Config using both IP Address List and Site - Not required (All devices with RUNNING_CONFIG status - 'COMPLIANT' or other)
        if "sync_device_config_iplist_site_nr" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("response_get_site_success"),
                self.test_data.get("response_get_membership_success"),
                self.test_data.get("response_get_device_list_success"),
                self.test_data.get("response_get_compliance_details_of_device_1_running_config_2"),
                self.test_data.get("response_get_compliance_details_of_device_2_running_config_2"),
                self.test_data.get("response_get_compliance_details_of_device_3_running_config_2"),
                self.test_data.get("response_get_compliance_details_of_device_4_running_config_2"),
                self.test_data.get("response_get_compliance_details_of_device_5_running_config_2"),
                self.test_data.get("response_get_compliance_details_of_device_6_running_config_2")
            ]

        # FIXTURES FOR FAILURE TESTCASES ############################################################
        # Run full compliance using an IP Address list - Failure 1
        if "run_compliance_with_iplist_failure_1" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                Exception("Simulated exception")
            ]

        # Run full compliance using an IP Address list - Failure 2
        if "run_compliance_with_iplist_failure_2" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("response_get_device_list_success"),
                Exception("Simulated exception")
            ]

        # Run full compliance using an IP Address list - Failure 3
        if "run_compliance_with_iplist_failure_3" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("response_get_device_list_success"),
                self.test_data.get("response_get_compliance_details_of_device_1"),
                Exception("Simulated exception"),
            ]

        # Run full compliance using an IP Address list - Failure 4
        if "run_compliance_with_iplist_failure_4" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("response_get_device_list_success"),
                self.test_data.get("response_get_compliance_details_of_device_1"),
                self.test_data.get("response_run_compliance_success"),
                Exception("Simulated exception"),
            ]

        # Run full compliance using an IP Address list - Failure 5
        if "run_compliance_with_iplist_failure_5" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("response_get_device_list_success"),
                self.test_data.get("response_get_compliance_details_of_device_1"),
                self.test_data.get("response_run_compliance_success"),
                self.test_data.get("response_get_task_by_id_success"),
                Exception("Simulated exception"),
            ]

        # Run full compliance using Site - Failure 1
        if "run_compliance_with_site_failure_1" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                Exception("Simulated exception")
            ]

        # Run full compliance using Site - Failure 2
        if "run_compliance_with_site_failure_2" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("response_get_site_success"),
                Exception("Simulated exception")
            ]

        # Run full compliance using Site - Failure 3
        if "run_compliance_with_site_failure_3" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("response_get_site_success"),
                self.test_data.get("response_get_membership_success"),
                self.test_data.get("response_get_compliance_details_of_device_1"),
                self.test_data.get("response_get_compliance_details_of_device_2"),
                self.test_data.get("response_get_compliance_details_of_device_3"),
                Exception("Simulated exception")
            ]

        # Run full compliance using Site - Failure 4
        if "run_compliance_with_site_failure_4" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("response_get_site_success"),
                self.test_data.get("response_get_membership_success"),
                self.test_data.get("response_get_compliance_details_of_device_1"),
                self.test_data.get("response_get_compliance_details_of_device_2"),
                self.test_data.get("response_get_compliance_details_of_device_3"),
                self.test_data.get("response_get_compliance_details_of_device_4"),
                self.test_data.get("response_get_compliance_details_of_device_5"),
                self.test_data.get("response_get_compliance_details_of_device_6"),
                Exception("Simulated exception")
            ]

        # Run full compliance using Site - Failure 5
        if "run_compliance_with_site_failure_5" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("response_get_site_success"),
                self.test_data.get("response_get_membership_success"),
                self.test_data.get("response_get_compliance_details_of_device_1"),
                self.test_data.get("response_get_compliance_details_of_device_2"),
                self.test_data.get("response_get_compliance_details_of_device_3"),
                self.test_data.get("response_get_compliance_details_of_device_4"),
                self.test_data.get("response_get_compliance_details_of_device_5"),
                self.test_data.get("response_get_compliance_details_of_device_6"),
                self.test_data.get("response_run_compliance_success"),
                Exception("Simulated exception")
            ]

        # Run full compliance using Site - Failure 6
        if "run_compliance_with_site_failure_6" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("response_get_site_success"),
                self.test_data.get("response_get_membership_success"),
                self.test_data.get("response_get_compliance_details_of_device_1"),
                self.test_data.get("response_get_compliance_details_of_device_2"),
                self.test_data.get("response_get_compliance_details_of_device_3"),
                self.test_data.get("response_get_compliance_details_of_device_4"),
                self.test_data.get("response_get_compliance_details_of_device_5"),
                self.test_data.get("response_get_compliance_details_of_device_6"),
                self.test_data.get("response_run_compliance_success"),
                self.test_data.get("response_get_task_by_id_success"),
                Exception("Simulated exception")
            ]

        # Run Sync Device Config using IP Address list - Failure 1
        if "sync_device_config_iplist_failure_1" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("response_get_device_list_success"),
                self.test_data.get("response_get_compliance_details_of_device_1_running_config"),
                Exception("Simulated exception")
            ]

        # Run Sync Device Config using IP Address list - Failure 2
        if "sync_device_config_iplist_failure_2" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("response_get_device_list_success"),
                self.test_data.get("response_get_compliance_details_of_device_1_running_config"),
                self.test_data.get("response_commit_device_configuration"),
                Exception("Simulated exception")
            ]

# SUCCESS TESTCASES ########################################################################################

# Run full compliance using an IP Address list
    def test_run_compliance_with_iplist(self):

        set_module_args(
            dict(
                dnac_host="1.1.1.1",
                dnac_username="dummy",
                dnac_password="dummy",
                dnac_log=False,
                dnac_log_level="DEBUG",
                dnac_log_append=False,
                state="merged",
                config=self.test_data.get("playbook_config_run_compliance_iplist")
            )
        )
        result = self.execute_module(changed=True, failed=False)
        self.assertEqual(
            result.get('msg'),
            "Run Compliance Check has completed successfully on 1 device(s): 192.168.0.0"
        )

# Run full compliance using Site
    def test_run_compliance_with_site(self):

        set_module_args(
            dict(
                dnac_host="1.1.1.1",
                dnac_username="dummy",
                dnac_password="dummy",
                dnac_log=False,
                dnac_log_level="DEBUG",
                dnac_log_append=False,
                state="merged",
                config=self.test_data.get("playbook_config_run_compliance_site")
            )
        )
        result = self.execute_module(changed=True, failed=False)
        self.assertIn(
            "Run Compliance Check has completed successfully on 6 device(s):",
            result.get('msg')
        )

# Run full compliance using both IP Address and Site
    def test_run_compliance_with_iplist_site(self):

        set_module_args(
            dict(
                dnac_host="1.1.1.1",
                dnac_username="dummy",
                dnac_password="dummy",
                dnac_log=True,
                dnac_log_level="DEBUG",
                dnac_log_append=False,
                state="merged",
                config=self.test_data.get("playbook_config_run_compliance_iplist_site")
            )
        )
        result = self.execute_module(changed=True, failed=False)
        self.assertIn(
            "Run Compliance Check has completed successfully on 6 device(s):",
            result.get('msg')
        )

# Run compliance against specific categories using IP Address List
    def test_run_compliance_categories_iplist(self):

        set_module_args(
            dict(
                dnac_host="1.1.1.1",
                dnac_username="dummy",
                dnac_password="dummy",
                dnac_log=True,
                dnac_log_level="DEBUG",
                dnac_log_append=False,
                state="merged",
                config=self.test_data.get("playbook_config_run_compliance_categories_iplist")
            )
        )
        result = self.execute_module(changed=True, failed=False)
        self.assertEqual(
            result.get('msg'),
            "Run Compliance Check has completed successfully on 1 device(s): 192.168.0.0"
        )

# Scale - Run full compliance operation using both IP Address List and Site
    def test_scale_run_compliance(self):

        set_module_args(
            dict(
                dnac_host="1.1.1.1",
                dnac_username="dummy",
                dnac_password="dummy",
                dnac_log=True,
                dnac_log_level="DEBUG",
                dnac_log_append=False,
                state="merged",
                config=self.test_data.get("playbook_config_run_compliance_scale_iplist")
            )
        )
        result = self.execute_module(changed=True, failed=False)
        self.assertIn(
            "Run Compliance Check has completed successfully on 2 device(s):",
            result.get('msg')

        )

# Run Sync Device Config using IP Address list - Sync Required (Devices with RUNNING_CONFIG status - 'NON_COMPLIANT')
    def test_sync_device_config_iplist(self):

        set_module_args(
            dict(
                dnac_host="1.1.1.1",
                dnac_username="dummy",
                dnac_password="dummy",
                dnac_log=True,
                dnac_log_level="DEBUG",
                dnac_log_append=False,
                state="merged",
                config=self.test_data.get("playbook_config_sync_device_config_iplist")
            )
        )
        result = self.execute_module(changed=True, failed=False)
        self.assertEqual(
            result.get('msg'),
            "Sync Device Configuration has completed successfully on 1 device(s): 192.168.0.0"
        )

# Run Sync Device Config using Site - Sync Required (Devices with RUNNING_CONFIG status - 'NON_COMPLIANT')
    def test_sync_device_config_site(self):

        set_module_args(
            dict(
                dnac_host="1.1.1.1",
                dnac_username="dummy",
                dnac_password="dummy",
                dnac_log=True,
                dnac_log_level="DEBUG",
                dnac_log_append=False,
                state="merged",
                config=self.test_data.get("playbook_config_sync_device_config_site")
            )
        )
        result = self.execute_module(changed=True, failed=False)
        self.assertIn(
            "Sync Device Configuration has completed successfully on 6 device(s):",
            result.get('msg')
        )

# Run Sync Device Config using both IP Address List and Site - Sync Required (Devices with RUNNING_CONFIG status - 'NON_COMPLIANT')
    def test_sync_device_config_iplist_site(self):

        set_module_args(
            dict(
                dnac_host="1.1.1.1",
                dnac_username="dummy",
                dnac_password="dummy",
                dnac_log=True,
                dnac_log_level="DEBUG",
                dnac_log_append=False,
                state="merged",
                config=self.test_data.get("playbook_config_sync_device_config_iplist_site")
            )
        )
        result = self.execute_module(changed=True, failed=False)
        self.assertIn(
            "Sync Device Configuration has completed successfully on 6 device(s)",
            result.get('msg')
        )

# Run Sync Device Config using both IP Address List and Site - Not required (All devices with RUNNING_CONFIG status - 'COMPLIANT' or other)
    def test_sync_device_config_iplist_site_nr(self):

        set_module_args(
            dict(
                dnac_host="1.1.1.1",
                dnac_username="dummy",
                dnac_password="dummy",
                dnac_log=True,
                dnac_log_level="DEBUG",
                dnac_log_append=False,
                state="merged",
                config=self.test_data.get("playbook_config_sync_device_config_iplist_site_nr")
            )
        )
        result = self.execute_module(changed=False, failed=False)
        self.assertIn(
            "the task 'Sync Device Configuration' is not required.",
            result.get('msg')
        )

# FAILURE TESTCASES ########################################################################################

# Run full compliance using an IP Address list - Failure 1
    def test_run_compliance_with_iplist_failure_1(self):

        set_module_args(
            dict(
                dnac_host="1.1.1.1",
                dnac_username="dummy",
                dnac_password="dummy",
                dnac_log=False,
                dnac_log_level="DEBUG",
                dnac_log_append=False,
                state="merged",
                config=self.test_data.get("playbook_config_run_compliance_iplist")
            )
        )
        result = self.execute_module(changed=False, failed=False)
        self.assertEqual(
            result.get('msg'),
            "No reachable devices found among the provided IP addresses: 192.168.0.0"
        )

# Run full compliance using an IP Address list - Failure 2
    def test_run_compliance_with_iplist_failure_2(self):

        set_module_args(
            dict(
                dnac_host="1.1.1.1",
                dnac_username="dummy",
                dnac_password="dummy",
                dnac_log=True,
                dnac_log_level="DEBUG",
                dnac_log_append=False,
                state="merged",
                config=self.test_data.get("playbook_config_run_compliance_iplist")
            )
        )
        result = self.execute_module(changed=False, failed=True)
        self.assertIn(
            "An error occurred while retrieving Compliance Details for device:192.168.0.0 using 'compliance_details_of_device' API call",
            result.get('msg')
        )

# Run full compliance using an IP Address list - Failure 3
    def test_run_compliance_with_iplist_failure_3(self):

        set_module_args(
            dict(
                dnac_host="1.1.1.1",
                dnac_username="dummy",
                dnac_password="dummy",
                dnac_log=True,
                dnac_log_level="DEBUG",
                dnac_log_append=False,
                state="merged",
                config=self.test_data.get("playbook_config_run_compliance_iplist")
            )
        )
        result = self.execute_module(changed=False, failed=True)
        self.assertEqual(
            "An error occurred while retrieving the task_id of the run_compliance operation.",
            result.get('msg')
        )

# Run full compliance using an IP Address list - Failure 4
    def test_run_compliance_with_iplist_failure_4(self):

        set_module_args(
            dict(
                dnac_host="1.1.1.1",
                dnac_username="dummy",
                dnac_password="dummy",
                dnac_log=True,
                dnac_log_level="DEBUG",
                dnac_log_append=False,
                state="merged",
                config=self.test_data.get("playbook_config_run_compliance_iplist")
            )
        )
        result = self.execute_module(changed=False, failed=True)
        self.assertIn(
            "Error occurred while retrieving 'get_task_by_id' for Task Run Compliance Check with Task id",
            result.get('msg')
        )

# Run full compliance using an IP Address list - Failure 5
    def test_run_compliance_with_iplist_failure_5(self):

        set_module_args(
            dict(
                dnac_host="1.1.1.1",
                dnac_username="dummy",
                dnac_password="dummy",
                dnac_log=True,
                dnac_log_level="DEBUG",
                dnac_log_append=False,
                state="merged",
                config=self.test_data.get("playbook_config_run_compliance_iplist")
            )
        )
        result = self.execute_module(changed=False, failed=True)
        self.assertIn(
            "An error occurred while retrieving Compliance Details for device:192.168.0.0 using 'compliance_details_of_device' API call",
            result.get('msg')
        )

# Run full compliance using Site - Failure 1
    def test_run_compliance_with_site_failure_1(self):

        set_module_args(
            dict(
                dnac_host="1.1.1.1",
                dnac_username="dummy",
                dnac_password="dummy",
                dnac_log=False,
                dnac_log_level="DEBUG",
                dnac_log_append=False,
                state="merged",
                config=self.test_data.get("playbook_config_run_compliance_site")
            )
        )
        result = self.execute_module(changed=False, failed=True)
        self.assertIn(
            "An error occurred while retrieving site details for Site 'Global'. Please verify that the site exists.",
            result.get('msg')
        )

# Run full compliance using Site - Failure 2
    def test_run_compliance_with_site_failure_2(self):

        set_module_args(
            dict(
                dnac_host="1.1.1.1",
                dnac_username="dummy",
                dnac_password="dummy",
                dnac_log=False,
                dnac_log_level="DEBUG",
                dnac_log_append=False,
                state="merged",
                config=self.test_data.get("playbook_config_run_compliance_site")
            )
        )
        result = self.execute_module(changed=False, failed=False)
        self.assertIn(
            "",
            result.get('msg')
        )

# Run full compliance using Site - Failure 3
    def test_run_compliance_with_site_failure_3(self):

        set_module_args(
            dict(
                dnac_host="1.1.1.1",
                dnac_username="dummy",
                dnac_password="dummy",
                dnac_log=False,
                dnac_log_level="DEBUG",
                dnac_log_append=False,
                state="merged",
                config=self.test_data.get("playbook_config_run_compliance_site")
            )
        )
        result = self.execute_module(changed=False, failed=True)
        self.assertIn(
            "An error occurred while retrieving Compliance Details for device:192.168.0.3 using 'compliance_details_of_device' API call",
            result.get('msg')
        )

# Run full compliance using Site - Failure 4
    def test_run_compliance_with_site_failure_4(self):

        set_module_args(
            dict(
                dnac_host="1.1.1.1",
                dnac_username="dummy",
                dnac_password="dummy",
                dnac_log=False,
                dnac_log_level="DEBUG",
                dnac_log_append=False,
                state="merged",
                config=self.test_data.get("playbook_config_run_compliance_site")
            )
        )
        result = self.execute_module(changed=False, failed=True)
        self.assertIn(
            "An error occurred while retrieving the task_id of the run_compliance operation.",
            result.get('msg')
        )

# Run full compliance using Site - Failure 5
    def test_run_compliance_with_site_failure_5(self):

        set_module_args(
            dict(
                dnac_host="1.1.1.1",
                dnac_username="dummy",
                dnac_password="dummy",
                dnac_log=False,
                dnac_log_level="DEBUG",
                dnac_log_append=False,
                state="merged",
                config=self.test_data.get("playbook_config_run_compliance_site")
            )
        )
        result = self.execute_module(changed=False, failed=True)
        self.assertIn(
            "Error occurred while retrieving 'get_task_by_id' for Task Run Compliance Check with Task id",
            result.get('msg')
        )

# Run full compliance using Site - Failure 6
    def test_run_compliance_with_site_failure_6(self):

        set_module_args(
            dict(
                dnac_host="1.1.1.1",
                dnac_username="dummy",
                dnac_password="dummy",
                dnac_log=False,
                dnac_log_level="DEBUG",
                dnac_log_append=False,
                state="merged",
                config=self.test_data.get("playbook_config_run_compliance_site")
            )
        )
        result = self.execute_module(changed=False, failed=True)
        self.assertIn(
            "An error occurred while retrieving Compliance Details for device:192.168.0.1 using 'compliance_details_of_device' API call",
            result.get('msg')
        )

# Run Sync Device Config using IP Address list - Failure 1
    def test_sync_device_config_iplist_failure_1(self):

        set_module_args(
            dict(
                dnac_host="1.1.1.1",
                dnac_username="dummy",
                dnac_password="dummy",
                dnac_log=True,
                dnac_log_level="DEBUG",
                dnac_log_append=False,
                state="merged",
                config=self.test_data.get("playbook_config_sync_device_config_iplist")
            )
        )
        result = self.execute_module(changed=False, failed=True)
        self.assertIn(
            "Error occurred while synchronizing device configuration for parameters - {'deviceId':",
            result.get('msg')
        )

# Run Sync Device Config using IP Address list - Failure 2
    def test_sync_device_config_iplist_failure_2(self):

        set_module_args(
            dict(
                dnac_host="1.1.1.1",
                dnac_username="dummy",
                dnac_password="dummy",
                dnac_log=True,
                dnac_log_level="DEBUG",
                dnac_log_append=False,
                state="merged",
                config=self.test_data.get("playbook_config_sync_device_config_iplist")
            )
        )
        result = self.execute_module(changed=False, failed=True)
        self.assertIn(
            "Error occurred while retrieving 'get_task_tree' for Task Sync Device Configuration with task id",
            result.get('msg')
        )
