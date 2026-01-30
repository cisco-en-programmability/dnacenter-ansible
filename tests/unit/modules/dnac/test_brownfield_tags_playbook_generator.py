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
#   Archit Soni <soni.archit03@gmail.com>
#
# Description:
#   Unit tests for the Ansible module `brownfield_tags_playbook_generator`.
#   These tests cover YAML playbook generation for tags and tag memberships,
#   including various filter scenarios and validation logic using mocked
#   Catalyst Center responses.

from __future__ import absolute_import, division, print_function

# Metadata
__metaclass__ = type
__author__ = "Archit Soni"
__email__ = "soni.archit03@gmail.com"
__version__ = "1.0.0"

from unittest.mock import patch
from ansible_collections.cisco.dnac.plugins.modules import (
    brownfield_tags_playbook_generator,
)
from .dnac_module import TestDnacModule, set_module_args, loadPlaybookData


class TestDnacBrownfieldTagsPlaybookGenerator(TestDnacModule):

    module = brownfield_tags_playbook_generator
    test_data = loadPlaybookData("brownfield_tags_playbook_generator")

    playbook_config_generate_all_configurations_case_1 = test_data.get(
        "generate_all_configurations_case_1"
    )

    def setUp(self):
        super(TestDnacBrownfieldTagsPlaybookGenerator, self).setUp()

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
        super(TestDnacBrownfieldTagsPlaybookGenerator, self).tearDown()
        self.mock_dnac_exec.stop()
        self.mock_dnac_init.stop()

    def load_fixtures(self, response=None, device=""):
        """
        Load fixtures for brownfield_tags_playbook_generator tests.
        """
        if "test_generate_all_configurations_case_1" in self._testMethodName:

            self.run_dnac_exec.side_effect = [
                self.test_data.get("get_sites_case_1"),
                self.test_data.get("get_tags_case_1"),
                self.test_data.get("get_tag_members_by_id_empty_response"),
                self.test_data.get("get_tag_members_by_id_empty_response"),
                self.test_data.get("get_tag_members_by_id_empty_response"),
                self.test_data.get("get_tag_members_by_id_empty_response"),
                self.test_data.get("get_tag_members_by_id_empty_response"),
                self.test_data.get("get_tag_members_by_id_empty_response"),
                self.test_data.get("get_tag_members_by_id_empty_response"),
                self.test_data.get("get_tag_members_by_id_empty_response"),
                self.test_data.get("get_tag_members_by_id_empty_response"),
                self.test_data.get("get_tag_members_by_id_empty_response"),
                self.test_data.get("get_tag_members_by_id_empty_response"),
                self.test_data.get("get_tag_members_by_id_empty_response"),
                self.test_data.get("get_tag_members_by_id_empty_response"),
                self.test_data.get("get_tag_members_by_id_empty_response"),
                self.test_data.get("get_tag_members_by_id_empty_response"),
                self.test_data.get("get_tag_members_by_id_empty_response"),
                self.test_data.get("get_tag_members_by_id_empty_response"),
                self.test_data.get("get_tag_members_by_id_empty_response"),
                self.test_data.get("get_tag_members_by_id_empty_response"),
                self.test_data.get("get_tag_members_by_id_empty_response"),
                self.test_data.get("get_tag_members_by_id_empty_response"),
                self.test_data.get("get_tag_members_by_id_empty_response"),
                self.test_data.get("get_tag_members_by_id_empty_response"),
                self.test_data.get("get_tag_members_by_id_case_1_call_1"),
                self.test_data.get("get_tag_members_by_id_case_1_call_2"),
                self.test_data.get("get_tag_members_by_id_case_1_call_3"),
                self.test_data.get("get_tag_members_by_id_empty_response"),
                self.test_data.get("get_tag_members_by_id_empty_response"),
                self.test_data.get("get_tag_members_by_id_empty_response"),
                self.test_data.get("get_tag_members_by_id_case_1_call_4"),
                self.test_data.get("get_tag_members_by_id_case_1_call_5"),
                self.test_data.get("get_tag_members_by_id_empty_response"),
                self.test_data.get("get_tag_members_by_id_case_1_call_6"),
                self.test_data.get("get_tag_members_by_id_case_1_call_7"),
                self.test_data.get("get_tag_members_by_id_empty_response"),
                self.test_data.get("get_tag_members_by_id_empty_response"),
                self.test_data.get("get_tag_members_by_id_empty_response"),
                self.test_data.get("get_tag_members_by_id_empty_response"),
                self.test_data.get("get_device_list_case_1_call_1"),
                self.test_data.get("get_device_list_case_1_call_2"),
                self.test_data.get("get_device_list_case_1_call_3"),
                self.test_data.get("get_device_list_case_1_call_4"),
                self.test_data.get("get_device_list_case_1_call_5"),
                self.test_data.get("get_device_list_case_1_call_6"),
                self.test_data.get("get_device_list_case_1_call_7"),
                self.test_data.get("get_device_list_case_1_call_8"),
            ]

    def test_generate_all_configurations_case_1(self):
        """
        Test Case 1: Generate all configurations (tags and tag memberships) automatically.
        This tests the generate_all_configurations flag which should retrieve
        all tags and all tag memberships from Cisco Catalyst Center.

        Based on real API logs, this test:
        - Generates YAML configuration file with all discovered tags and memberships
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
                config=self.playbook_config_generate_all_configurations_case_1,
            )
        )

        result = self.execute_module(changed=True, failed=False)
        self.assertIn(
            "YAML configuration file generated successfully for module 'tags_workflow_manager'",
            str(result.get("msg")),
        )
