# Copyright (c) 2026 Cisco and/or its affiliates.
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
#   Apoorv Bansal (@Apoorv74-dot)

# Description:
#   Unit tests for the Ansible module `sda_extranet_policies_playbook_config_generator`.
#   These tests cover YAML playbook generation for SDA extranet policies,
#   including various filter scenarios and validation logic using mocked
#   Catalyst Center responses.

from __future__ import absolute_import, division, print_function

# Metadata
__metaclass__ = type
__author__ = "Apoorv Bansal, Madhan Sankaranarayanan"
__version__ = "1.0.0"

from unittest.mock import patch
from ansible_collections.cisco.dnac.plugins.modules import (
    sda_extranet_policies_playbook_config_generator,
)
from .dnac_module import TestDnacModule, set_module_args, loadPlaybookData


class TestDnacBrownfieldSdaExtranetPoliciesPlaybookGenerator(TestDnacModule):

    module = sda_extranet_policies_playbook_config_generator
    test_data = loadPlaybookData("sda_extranet_policies_playbook_config_generator")

    playbook_config_generate_all_configurations = test_data.get(
        "generate_all_configurations_case"
    )
    playbook_config_empty_config = test_data.get("empty_config_case")
    playbook_config_empty_component_specific_filters = test_data.get(
        "empty_component_specific_filters_case"
    )
    playbook_config_component_specific_filters = test_data.get(
        "component_specific_filters_case"
    )
    playbook_config_filter_not_found = test_data.get("filter_not_found_case")

    def setUp(self):
        super(TestDnacBrownfieldSdaExtranetPoliciesPlaybookGenerator, self).setUp()

        self.mock_dnac_init = patch(
            "ansible_collections.cisco.dnac.plugins.module_utils.dnac.DNACSDK.__init__"
        )
        self.run_dnac_init = self.mock_dnac_init.start()
        self.run_dnac_init.side_effect = [None]
        self.mock_dnac_exec = patch(
            "ansible_collections.cisco.dnac.plugins.module_utils.dnac.DNACSDK._exec"
        )
        self.run_dnac_exec = self.mock_dnac_exec.start()
        self.load_fixtures()

    def tearDown(self):
        super(TestDnacBrownfieldSdaExtranetPoliciesPlaybookGenerator, self).tearDown()
        self.mock_dnac_exec.stop()
        self.mock_dnac_init.stop()

    def load_fixtures(self, response=None, device=""):
        """
        Load fixtures for brownfield_sda_extranet_policies_playbook_generator tests.
        """
        if "test_generate_all_configurations" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("get_sites_response"),
                self.test_data.get("get_extranet_policies_all_response"),
            ]
        elif "test_component_specific_filters" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("get_sites_response"),
                self.test_data.get("get_extranet_policies_filtered_response"),
            ]
        elif "test_filter_not_found_in_catalyst_center" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("get_sites_response"),
                self.test_data.get("get_extranet_policies_not_found_response"),
            ]

    def test_generate_all_configurations(self):
        """
        Test Case 1: Generate all SDA extranet policies configurations automatically.
        This tests the generate_all_configurations flag which should retrieve
        all extranet policies from Cisco Catalyst Center.

        This test:
        - Generates YAML configuration file with all discovered extranet policies
        - Validates successful YAML generation
        """
        set_module_args(
            dict(
                dnac_host="1.1.1.1",
                dnac_username="dummy",
                dnac_password="dummy",
                dnac_version="2.3.7.9",
                dnac_log=True,
                state="gathered",
                dnac_log_level="DEBUG",
                config=self.playbook_config_generate_all_configurations,
            )
        )

        result = self.execute_module(changed=True, failed=False)
        self.assertIn(
            "YAML configuration file generated successfully",
            str(result.get("msg")),
        )

    def test_component_specific_filters(self):
        """
        Test Case 2: Generate extranet policies with component-specific filters.
        This tests filtering extranet policies by policy name.

        This test:
        - Uses component_specific_filters with extranet_policy_name
        - Generates YAML configuration file with filtered extranet policies
        - Validates successful YAML generation with specific policy
        """
        set_module_args(
            dict(
                dnac_host="1.1.1.1",
                dnac_username="dummy",
                dnac_password="dummy",
                dnac_version="2.3.7.9",
                dnac_log=True,
                state="gathered",
                dnac_log_level="DEBUG",
                config=self.playbook_config_component_specific_filters,
            )
        )

        result = self.execute_module(changed=True, failed=False)
        self.assertIn(
            "YAML configuration file generated successfully",
            str(result.get("msg")),
        )

    def test_empty_config_raises_error(self):
        """
        Test Case 3: Passing an empty config dict should raise a validation error.
        An empty dict is not the same as omitting config; the module should
        reject it with a clear error message rather than silently generating
        all configurations.
        """
        set_module_args(
            dict(
                dnac_host="1.1.1.1",
                dnac_username="dummy",
                dnac_password="dummy",
                dnac_version="2.3.7.9",
                dnac_log=True,
                state="gathered",
                dnac_log_level="DEBUG",
                config=self.playbook_config_empty_config,
            )
        )

        result = self.execute_module(changed=False, failed=True)
        self.assertIn(
            "Configuration cannot be an empty dictionary",
            str(result.get("msg")),
        )

    def test_empty_component_specific_filters_raises_error(self):
        """
        Test Case 4: Passing component_specific_filters as an empty dict should
        raise a validation error requiring at least components_list or a component
        filter block.
        """
        set_module_args(
            dict(
                dnac_host="1.1.1.1",
                dnac_username="dummy",
                dnac_password="dummy",
                dnac_version="2.3.7.9",
                dnac_log=True,
                state="gathered",
                dnac_log_level="DEBUG",
                config=self.playbook_config_empty_component_specific_filters,
            )
        )

        result = self.execute_module(changed=False, failed=True)
        self.assertIn(
            "component_specific_filters",
            str(result.get("msg")),
        )

    def test_filter_not_found_in_catalyst_center(self):
        """
        Test Case 5: Filter specifies a policy name that does not exist in Catalyst Center.
        The API returns an empty response, so no configurations are found.
        The module should succeed (not fail) and report that no configurations
        were found, including the list of components attempted.
        """
        set_module_args(
            dict(
                dnac_host="1.1.1.1",
                dnac_username="dummy",
                dnac_password="dummy",
                dnac_version="2.3.7.9",
                dnac_log=True,
                state="gathered",
                dnac_log_level="DEBUG",
                config=self.playbook_config_filter_not_found,
            )
        )

        result = self.execute_module(changed=False, failed=False)
        self.assertIn(
            "No configurations found for module 'sda_extranet_policies_workflow_manager'",
            str(result.get("msg")),
        )
        self.assertIn(
            "extranet_policies",
            str(result.get("msg")),
        )
