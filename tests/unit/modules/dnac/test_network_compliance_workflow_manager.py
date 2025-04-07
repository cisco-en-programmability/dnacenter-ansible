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

    test_data = loadPlaybookData("network_compliance_workflow_manager_intent")

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
                self.test_data.get("response_get_device_list"),
                self.test_data.get("response_compliance_details_of_device"),
                self.test_data.get("response_get_task_id_success"),
                self.test_data.get("response_get_task_status_by_id"),
                self.test_data.get("response_get_compliance_details_of_device_2"),
            ]

        # Run full compliance using site
        if "run_compliance_with_site" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("reponse_get_sites"),
                self.test_data.get("response_get_assigned_network_devices"),
                self.test_data.get("response_get_device_by_id"),
                self.test_data.get("response_get_device_by_id_2"),
                self.test_data.get("response_get_compliance_details_of_device_3"),
                self.test_data.get("response_get_task_id_success"),
                self.test_data.get("response_get_task_status_by_id"),
                self.test_data.get("response_get_compliance_details_of_device_4"),
            ]

        # Run full compliance using an IP Address list and specific categories
        if "run_compliance_with_categories" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("response_get_device_list_2"),
                self.test_data.get("response_get_compliance_details_of_device_5"),
                self.test_data.get("response_get_compliance_details_of_device_6"),
                self.test_data.get("response_get_compliance_details_of_device_7"),
                self.test_data.get("response_get_compliance_details_of_device_8"),
                self.test_data.get("response_get_compliance_details_of_device_9"),
                self.test_data.get("response_get_compliance_details_of_device_10"),
                self.test_data.get("response_get_compliance_details_of_device_11"),
                self.test_data.get("response_get_compliance_details_of_device_12"),
                self.test_data.get("response_get_compliance_details_of_device_13"),
                self.test_data.get("response_get_compliance_details_of_device_14"),
                self.test_data.get("response_get_compliance_details_of_device_15"),
                self.test_data.get("response_get_compliance_details_of_device_16"),
                self.test_data.get("response_get_compliance_details_of_device_17"),
                self.test_data.get("response_get_compliance_details_of_device_18"),
                self.test_data.get("response_get_compliance_details_of_device_19"),
                self.test_data.get("response_get_compliance_details_of_device_20"),
                self.test_data.get("response_get_task_id_success"),
                self.test_data.get("response_get_task_status_by_id"),
                self.test_data.get("response_get_compliance_details_of_device_5"),
                self.test_data.get("response_get_compliance_details_of_device_6"),
                self.test_data.get("response_get_compliance_details_of_device_7"),
                self.test_data.get("response_get_compliance_details_of_device_8"),
                self.test_data.get("response_get_compliance_details_of_device_9"),
                self.test_data.get("response_get_compliance_details_of_device_10"),
                self.test_data.get("response_get_compliance_details_of_device_11"),
                self.test_data.get("response_get_compliance_details_of_device_12"),
                self.test_data.get("response_get_compliance_details_of_device_13"),
                self.test_data.get("response_get_compliance_details_of_device_14"),
                self.test_data.get("response_get_compliance_details_of_device_15"),
                self.test_data.get("response_get_compliance_details_of_device_16"),
                self.test_data.get("response_get_compliance_details_of_device_17"),
                self.test_data.get("response_get_compliance_details_of_device_18"),
                self.test_data.get("response_get_compliance_details_of_device_19"),
                self.test_data.get("response_get_compliance_details_of_device_20")
            ]

        # Run full compliance using site with categories
        if "run_compliance_with_site_categories" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("reponse_get_sites"),
                self.test_data.get("response_get_assigned_network_devices"),
                self.test_data.get("response_get_device_by_id"),
                self.test_data.get("response_get_device_by_id_2"),
                self.test_data.get("response_get_compliance_details_of_device_17"),
                self.test_data.get("response_get_compliance_details_of_device_18"),
                self.test_data.get("response_get_compliance_details_of_device_19"),
                self.test_data.get("response_get_compliance_details_of_device_20"),
                self.test_data.get("response_get_task_id_success"),
                self.test_data.get("response_get_task_status_by_id"),
                self.test_data.get("response_get_compliance_details_of_device_17"),
                self.test_data.get("response_get_compliance_details_of_device_18"),
                self.test_data.get("response_get_compliance_details_of_device_19"),
                self.test_data.get("response_get_compliance_details_of_device_20")
            ]

        # Run Sync Device Config
        if "run_sync_device_config" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("response_get_device_list"),
                self.test_data.get("response_compliance_details_sync_device_config"),
                self.test_data.get("response_get_compliance_details_sync_device_config_2"),
                self.test_data.get("response_get_task_id_success"),
                self.test_data.get("response_get_task_status_by_id"),
                self.test_data.get("response_get_compliance_details_sync_device_config_3"),
                self.test_data.get("response_get_task_id_success"),
                self.test_data.get("response_get_task_status_by_id"),
                self.test_data.get("response_get_compliance_details_sync_device_config_4")
            ]

# SUCCESS TESTCASES ########################################################################################

# Run full compliance using an IP Address list
    def test_run_compliance_with_iplist(self):
        print("Test Data: {test_data}".format(test_data=self.test_data.get("playbook_config_run_compliance_iplist")))

        set_module_args(
            dict(
                dnac_host="1.1.1.1",
                dnac_username="dummy",
                dnac_password="dummy",
                dnac_log=False,
                dnac_log_level="DEBUG",
                dnac_version="2.3.7.9",
                config_verify=True,
                dnac_log_append=False,
                state="merged",
                config=self.test_data.get("playbook_config_run_compliance_iplist")
            )
        )
        result = self.execute_module(changed=True, failed=False)
        self.assertIn(
            "Run Compliance Check Succeeded for following device(s)",
            result.get('msg')
        )

# Run full compliance using site name
    def test_run_compliance_with_site(self):
        print("Test Data: {test_data}".format(test_data=self.test_data.get("playbook_config_run_compliance_site")))

        set_module_args(
            dict(
                dnac_host="1.1.1.1",
                dnac_username="dummy",
                dnac_password="dummy",
                dnac_log=False,
                dnac_log_level="DEBUG",
                dnac_version="2.3.7.9",
                config_verify=True,
                dnac_log_append=False,
                state="merged",
                config=self.test_data.get("playbook_config_run_compliance_site")
            )
        )
        result = self.execute_module(changed=True, failed=False)
        self.assertIn(
            "Run Compliance Check Succeeded for following device(s)",
            result.get('msg')
        )

# Run full compliance using categories
    def test_run_compliance_with_categories(self):
        print("Test Data: {test_data}".format(test_data=self.test_data.get("playbook_config_run_compliance_with_categories")))

        set_module_args(
            dict(
                dnac_host="1.1.1.1",
                dnac_username="dummy",
                dnac_password="dummy",
                dnac_log=False,
                dnac_log_level="DEBUG",
                dnac_version="2.3.7.9",
                config_verify=True,
                dnac_log_append=False,
                state="merged",
                config=self.test_data.get("playbook_config_run_compliance_with_categories")
            )
        )
        result = self.execute_module(changed=True, failed=False)
        self.assertIn(
            "Run Compliance Check Succeeded for following device(s)",
            result.get('msg')
        )

# Run full compliance using categories
    def test_run_compliance_with_site_categories(self):
        print("Test Data: {test_data}".format(test_data=self.test_data.get("playbook_config_run_compliance_with_site_categories")))

        set_module_args(
            dict(
                dnac_host="1.1.1.1",
                dnac_username="dummy",
                dnac_password="dummy",
                dnac_log=False,
                dnac_log_level="DEBUG",
                dnac_version="2.3.7.9",
                config_verify=True,
                dnac_log_append=False,
                state="merged",
                config=self.test_data.get("playbook_config_run_compliance_with_site_categories")
            )
        )
        result = self.execute_module(changed=True, failed=False)
        self.assertIn(
            "Run Compliance Check Succeeded for following device(s)",
            result.get('msg')
        )

# Run sync device config
    def test_run_sync_device_config(self):
        print("Test Data: {test_data}".format(test_data=self.test_data.get("playbook_config_sync_device_config")))

        set_module_args(
            dict(
                dnac_host="1.1.1.1",
                dnac_username="dummy",
                dnac_password="dummy",
                dnac_log=False,
                dnac_log_level="DEBUG",
                dnac_version="2.3.7.9",
                config_verify=True,
                dnac_log_append=False,
                state="merged",
                config=self.test_data.get("playbook_config_sync_device_config")
            )
        )
        result = self.execute_module(changed=True, failed=False)
        self.assertIn(
            "Sync Device Configuration Succeeded for following device(s)",
            result.get('msg')
        )
