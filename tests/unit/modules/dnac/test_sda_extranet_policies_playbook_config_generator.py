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
#   Unit tests for the Ansible module `brownfield_sda_extranet_policies_playbook_generator`.
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
    brownfield_sda_extranet_policies_playbook_generator,
)
from .dnac_module import TestDnacModule, set_module_args, loadPlaybookData


class TestDnacBrownfieldSdaExtranetPoliciesPlaybookGenerator(TestDnacModule):

    module = brownfield_sda_extranet_policies_playbook_generator
    test_data = loadPlaybookData("brownfield_sda_extranet_policies_playbook_generator")

    playbook_config_generate_all_configurations = test_data.get(
        "generate_all_configurations_case"
    )
    playbook_config_component_specific_filters = test_data.get(
        "component_specific_filters_case"
    )

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
