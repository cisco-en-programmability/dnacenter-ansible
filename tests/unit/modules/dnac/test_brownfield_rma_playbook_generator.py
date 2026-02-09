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

from ansible_collections.cisco.dnac.plugins.modules import brownfield_rma_playbook_generator
from .dnac_module import TestDnacModule, set_module_args, loadPlaybookData


class TestDnacRmaPlaybookGenerator(TestDnacModule):

    module = brownfield_rma_playbook_generator

    test_data = loadPlaybookData("brownfield_rma_playbook_generator")

    playbook_generate_all_configurations = test_data.get("playbook_generate_all_configurations")
    playbook_component_filters = test_data.get("playbook_component_filters")
    playbook_specifc_filters = test_data.get("playbook_specifc_filters")
    playbook_no_device_found = test_data.get("playbook_no_device_found")
    playbook_component_specific_filters1 = test_data.get("playbook_component_specific_filters1")
    playbook_negative_scenario1 = test_data.get("playbook_negative_scenario1")

    def setUp(self):
        super(TestDnacRmaPlaybookGenerator, self).setUp()

        self.mock_dnac_init = patch(
            "ansible_collections.cisco.dnac.plugins.module_utils.dnac.DNACSDK.__init__")
        self.run_dnac_init = self.mock_dnac_init.start()
        self.run_dnac_init.side_effect = [None]
        self.mock_dnac_exec = patch(
            "ansible_collections.cisco.dnac.plugins.module_utils.dnac.DNACSDK._exec"
        )
        self.run_dnac_exec = self.mock_dnac_exec.start()

    def tearDown(self):
        super(TestDnacRmaPlaybookGenerator, self).tearDown()
        self.mock_dnac_exec.stop()
        self.mock_dnac_init.stop()

    def load_fixtures(self, response=None, device=""):
        """
        Load fixtures for user.
        """

        if "playbook_generate_all_configurations" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("response1"),
                self.test_data.get("response2"),
                self.test_data.get("response3"),
                self.test_data.get("response4"),
            ]

        elif "playbook_component_filters" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("response5"),
                self.test_data.get("response6"),
                self.test_data.get("response7"),
                self.test_data.get("response8"),
            ]

        elif "playbook_specifc_filters" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("response9"),
                self.test_data.get("response11"),
                self.test_data.get("response12"),
                self.test_data.get("response13"),
            ]

        elif "playbook_no_device_found" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("response10"),
            ]

        elif "playbook_component_specific_filters1" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("response14"),
            ]

        elif "playbook_negative_scenario1" in self._testMethodName:
            pass

    def test_brownfield_rma_playbook_generator_playbook_generate_all_configurations(self):
        """
        Test the Brownfield RMA Workflow Manager's playbook generation process.

        This test verifies that the workflow correctly handles the generation of a new
        playbook for all RMA configurations, ensuring proper validation and expected behavior.
        """

        set_module_args(
            dict(
                dnac_host="1.1.1.1",
                dnac_username="dummy",
                dnac_password="dummy",
                dnac_log=True,
                state="gathered",
                dnac_version="2.3.7.6",
                config=self.playbook_generate_all_configurations
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
                "file_path": "/Users/priyadharshini/Downloads/rma_info",
                "message": "YAML configuration file generated successfully for module 'rma_workflow_manager'",
                "status": "success"
            }
        )

    def test_brownfield_rma_playbook_generator_playbook_component_filters(self):
        """
        Test the Brownfield RMA Workflow Manager's playbook generation process.

        This test verifies that the workflow correctly handles the generation of a new
        playbook for all RMA configurations, ensuring proper validation and expected behavior.
        """

        set_module_args(
            dict(
                dnac_host="1.1.1.1",
                dnac_username="dummy",
                dnac_password="dummy",
                dnac_log=True,
                state="gathered",
                dnac_version="2.3.7.6",
                config=self.playbook_component_filters
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
                "file_path": "/Users/priyadharshini/Downloads/rma_info",
                "message": "YAML configuration file generated successfully for module 'rma_workflow_manager'",
                "status": "success"
            }
        )

    def test_brownfield_rma_playbook_generator_playbook_specifc_filters(self):
        """
        Test the Brownfield RMA Workflow Manager's playbook generation process.

        This test verifies that the workflow correctly handles the generation of a new
        playbook for all RMA configurations, ensuring proper validation and expected behavior.
        """

        set_module_args(
            dict(
                dnac_host="1.1.1.1",
                dnac_username="dummy",
                dnac_password="dummy",
                dnac_log=True,
                state="gathered",
                dnac_version="2.3.7.6",
                config=self.playbook_specifc_filters
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
                "file_path": "/Users/priyadharshini/Downloads/rma_info",
                "message": "YAML configuration file generated successfully for module 'rma_workflow_manager'",
                "status": "success"
            }
        )

    def test_brownfield_rma_playbook_generator_playbook_no_device_found(self):
        """
        Test the Brownfield RMA Workflow Manager's playbook generation process.

        This test verifies that the workflow correctly handles the generation of a new
        playbook for all RMA configurations, ensuring proper validation and expected behavior.
        """

        set_module_args(
            dict(
                dnac_host="1.1.1.1",
                dnac_username="dummy",
                dnac_password="dummy",
                dnac_log=True,
                state="gathered",
                dnac_version="2.3.7.6",
                config=self.playbook_no_device_found
            )
        )
        result = self.execute_module(changed=False, failed=False)
        print(result)
        self.assertEqual(
            result.get("response"),
            {
                "components_processed": 0,
                "components_skipped": 1,
                "configurations_count": 0,
                "message": (
                    "No device replacement workflows found to process for module "
                    "'rma_workflow_manager'. Verify that RMA workflows are configured in "
                    "Catalyst Center or check user permissions."
                ),
                "status": "success"
            }
        )

    def test_brownfield_rma_playbook_generator_playbook_component_specific_filters1(self):
        """
        Test the Brownfield RMA Workflow Manager's playbook generation process.

        This test verifies that the workflow correctly handles the generation of a new
        playbook for all RMA configurations, ensuring proper validation and expected behavior.
        """

        set_module_args(
            dict(
                dnac_host="1.1.1.1",
                dnac_username="dummy",
                dnac_password="dummy",
                dnac_log=True,
                state="gathered",
                dnac_version="2.3.7.6",
                config=self.playbook_component_specific_filters1
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
                "file_path": "/Users/priyadharshini/Downloads/rma_info",
                "message": "YAML configuration file generated successfully for module 'rma_workflow_manager'",
                "status": "success"
            }
        )

    def test_brownfield_rma_playbook_generator_playbook_negative_scenario1(self):
        """
        Test the Brownfield RMA Workflow Manager's playbook generation process.

        This test verifies that the workflow correctly handles the generation of a new
        playbook for all RMA configurations, ensuring proper validation and expected behavior.
        """

        set_module_args(
            dict(
                dnac_host="1.1.1.1",
                dnac_username="dummy",
                dnac_password="dummy",
                dnac_log=True,
                state="gathered",
                dnac_version="2.3.7.6",
                config=self.playbook_negative_scenario1
            )
        )
        result = self.execute_module(changed=True, failed=True)
        print(result)
        self.assertEqual(
            result.get("response"),
            (
                "Invalid network components provided for module 'rma_workflow_manager': "
                "['device_replacement_workflow']. "
                "Valid components are: ['device_replacement_workflows']"
            )
        )
