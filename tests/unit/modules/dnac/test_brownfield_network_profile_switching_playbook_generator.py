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

# Authors:
#   A Mohamed Rafeek <mabdulk2@cisco.com>
#   Madhan Sankaranarayanan <madhansansel@cisco.com>
#
# Description:
#   Unit tests for the Ansible module `brownfield_network_profile_switching_playbook_generator`.
#   These tests cover various scenarios for generating YAML playbooks from brownfield
#   network profile switching configurations in Cisco DNA Center.

# Make coding more python3-ish
from __future__ import absolute_import, division, print_function

__metaclass__ = type
from unittest.mock import patch, mock_open
from ansible_collections.cisco.dnac.plugins.modules import brownfield_network_profile_switching_playbook_generator
from .dnac_module import TestDnacModule, set_module_args, loadPlaybookData


class TestBrownfieldNetworkProfileSwitchingPlaybookGenerator(TestDnacModule):

    module = brownfield_network_profile_switching_playbook_generator
    test_data = loadPlaybookData("brownfield_network_profile_switching_playbook_generator")

    # Load all playbook configurations
    playbook_config_generate_all_profile = test_data.get("playbook_config_generate_all_profile")
    playbook_global_filter_profile_base = test_data.get("playbook_global_filter_profile_base")
    playbook_global_filter_template_base = test_data.get("playbook_global_filter_template_base")
    playbook_global_filter_site_base = test_data.get("playbook_global_filter_site_base")

    def setUp(self):
        super(TestBrownfieldNetworkProfileSwitchingPlaybookGenerator, self).setUp()

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
        super(TestBrownfieldNetworkProfileSwitchingPlaybookGenerator, self).tearDown()
        self.mock_dnac_exec.stop()
        self.mock_dnac_init.stop()

    def load_fixtures(self, response=None, device=""):
        """
        Load fixtures for brownfield network profile switching playbook generator tests.
        """
        if "generate_all_configurations" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("all_switch_profiles"),
                self.test_data.get("cli_template_details_for_profile1"),
                self.test_data.get("get_site_list_for_profile1"),
                self.test_data.get("get_site_all"),
                self.test_data.get("template_attached_profile2"),
                self.test_data.get("site_attached_profile2"),
                self.test_data.get("get_site_all"),
            ]
        elif "generate_global_filter" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("all_switch_profiles"),
                self.test_data.get("template_attached_profile2"),
                self.test_data.get("site_attached_profile2"),
                self.test_data.get("get_site_all"),
            ]
        elif "generate_filter_template_base" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("all_switch_profiles"),
                self.test_data.get("cli_template_details_for_profile1"),
                self.test_data.get("get_site_list_for_profile1"),
                self.test_data.get("get_site_all"),
                self.test_data.get("template_attached_profile2"),
                self.test_data.get("site_attached_profile2"),
                self.test_data.get("get_site_all"),
            ]
        elif "generate_filter_site_base" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("all_switch_profiles"),
                self.test_data.get("cli_template_details_for_profile1"),
                self.test_data.get("get_site_list_for_profile1"),
                self.test_data.get("get_site_all"),
                self.test_data.get("template_attached_profile2"),
                self.test_data.get("site_attached_profile2"),
                self.test_data.get("get_site_all"),
            ]

    @patch('builtins.open', new_callable=mock_open)
    @patch('os.path.exists')
    def test_brownfield_network_switch_profile_generate_all_configurations(self, mock_exists, mock_file):
        """
        Test case for brownfield network switch profile generator when generating all profiles.
        This test case checks the behavior when generate_all_configurations is set to True,
        which should retrieve all switch profile with Day N template and Feature template
        and generate a complete YAML playbook profile file.
        """
        mock_exists.return_value = True

        set_module_args(
            dict(
                dnac_host="1.1.1.1",
                dnac_username="dummy",
                dnac_password="dummy",
                dnac_version="2.3.7.9",
                dnac_log=True,
                state="gathered",
                config=self.playbook_config_generate_all_profile
            )
        )
        result = self.execute_module(changed=True, failed=False)
        self.assertIn("YAML config generation Task succeeded", str(result.get('msg')))

    @patch('builtins.open', new_callable=mock_open)
    @patch('os.path.exists')
    def test_brownfield_network_switch_profile_generate_global_filter(self, mock_exists, mock_file):
        """
        Test case for brownfield network switch profile generator when global filter profiles.
        This test case checks the behavior when generate_all_configurations is set to True,
        which should retrieve all switch profile with Day N template and Feature template
        and generate a complete YAML playbook profile file.
        """
        mock_exists.return_value = True

        set_module_args(
            dict(
                dnac_host="1.1.1.1",
                dnac_username="dummy",
                dnac_password="dummy",
                dnac_version="3.1.3.0",
                dnac_log=True,
                state="gathered",
                config=self.playbook_global_filter_profile_base
            )
        )
        result = self.execute_module(changed=True, failed=False)
        self.assertIn("YAML config generation Task succeeded", str(result.get('msg')))

    @patch('builtins.open', new_callable=mock_open)
    @patch('os.path.exists')
    def test_brownfield_network_switch_profile_generate_filter_template_base(self, mock_exists, mock_file):
        """
        Test case for brownfield network switch profile generator when global filter profiles.
        This test case checks the behavior when generate_all_configurations is set to True,
        which should retrieve all switch profile with Day N template and Feature template
        and generate a complete YAML playbook profile file.
        """
        mock_exists.return_value = True

        set_module_args(
            dict(
                dnac_host="1.1.1.1",
                dnac_username="dummy",
                dnac_password="dummy",
                dnac_version="3.1.3.0",
                dnac_log=True,
                state="gathered",
                config=self.playbook_global_filter_template_base
            )
        )
        result = self.execute_module(changed=True, failed=False)
        self.assertIn("YAML config generation Task succeeded", str(result.get('msg')))

    @patch('builtins.open', new_callable=mock_open)
    @patch('os.path.exists')
    def test_brownfield_network_switch_profile_generate_filter_site_base(self, mock_exists, mock_file):
        """
        Test case for brownfield network switch profile generator when global filter profiles.
        This test case checks the behavior when generate_all_configurations is set to True,
        which should retrieve all switch profile with Day N template and Feature template
        and generate a complete YAML playbook profile file.
        """
        mock_exists.return_value = True

        set_module_args(
            dict(
                dnac_host="1.1.1.1",
                dnac_username="dummy",
                dnac_password="dummy",
                dnac_version="3.1.3.0",
                dnac_log=True,
                state="gathered",
                config=self.playbook_global_filter_site_base
            )
        )
        result = self.execute_module(changed=True, failed=False)
        self.assertIn("YAML config generation Task succeeded", str(result.get('msg')))
