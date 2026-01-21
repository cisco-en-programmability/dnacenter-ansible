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
#   Sunil Shatagopa <shatagopasunil@cisco.com>
#   Madhan Sankaranarayanan <madhansansel@cisco.com>
#
# Description:
#   Unit tests for the Ansible module `brownfield_template_playbook_generator`.
#   These tests cover various scenarios for generating YAML playbooks from brownfield
#   template projects and configuration templates in Cisco Catalyst Center.

from __future__ import absolute_import, division, print_function

__metaclass__ = type
from unittest.mock import patch, mock_open
from ansible_collections.cisco.dnac.plugins.modules import brownfield_template_playbook_generator
from .dnac_module import TestDnacModule, set_module_args, loadPlaybookData


class TestBrownfieldTemplateConfigGenerator(TestDnacModule):
    module = brownfield_template_playbook_generator
    test_data = loadPlaybookData("brownfield_template_config_generator")

    playbook_config_generate_all_configurations = test_data.get("playbook_config_generate_all_configurations")
    playbook_config_template_projects_by_name_single = test_data.get("playbook_config_template_projects_by_name_single")
    playbook_config_template_projects_by_name_multiple = test_data.get("playbook_config_template_projects_by_name_multiple")
    playbook_config_template_by_name_single = test_data.get("playbook_config_template_by_name_single")
    playbook_config_template_by_name_multiple = test_data.get("playbook_config_template_by_name_multiple")
    playbook_config_template_projects_empty_filter = test_data.get("playbook_config_template_projects_empty_filter")
    playbook_config_templates_empty_filter = test_data.get("playbook_config_templates_empty_filter")
    playbook_config_templates_includes_uncommitted_filter = test_data.get("playbook_config_templates_includes_uncommitted_filter")
    playbook_config_template_by_project_name_multiple = test_data.get("playbook_config_template_by_project_name_multiple")
    playbook_config_template_by_template_name_and_project_name = test_data.get("playbook_config_template_by_template_name_and_project_name")
    playbook_config_template_all_filters = test_data.get("playbook_config_template_all_filters")
    playbook_invalid_project_details = test_data.get("playbook_invalid_project_details")
    playbook_invalid_template_details = test_data.get("playbook_invalid_template_details")

    def setUp(self):
        super(TestBrownfieldTemplateConfigGenerator, self).setUp()
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
        super(TestBrownfieldTemplateConfigGenerator, self).tearDown()
        self.mock_dnac_exec.stop()
        self.mock_dnac_init.stop()

    def load_fixtures(self, response=None, device=""):
        """
        Load fixtures for brownfield template config generator tests.
        """

        if "generate_all_configurations" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("get_all_projects"),
                self.test_data.get("get_all_templates"),
            ]
        elif "template_projects_by_name_single" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("get_all_projects"),
            ]
        elif "template_projects_by_name_multiple" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("get_all_projects"),
                self.test_data.get("get_all_projects")
            ]
        elif "template_by_name_single" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("get_all_templates"),
            ]
        elif "template_by_name_multiple" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("get_all_templates"),
                self.test_data.get("get_all_templates")
            ]
        elif "template_by_name_and_id" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("get_all_templates"),
            ]
        elif "template_projects_empty_filter" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("get_all_projects"),
            ]
        elif "templates_empty_filter" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("get_all_templates"),
            ]
        elif "templates_includes_uncommitted_filter" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("get_all_templates"),
            ]
        elif "template_by_project_name_multiple" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("get_all_templates"),
                self.test_data.get("get_all_templates"),
            ]
        elif "template_by_template_name_and_project_name" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("get_all_templates"),
                self.test_data.get("get_all_templates"),
            ]
        elif "template_all_filters" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("get_all_templates"),
            ]
        elif "invalid_project_details" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
            ]
        elif "invalid_template_details" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
            ]

    @patch('builtins.open', new_callable=mock_open)
    @patch('os.path.exists')
    def test_generate_all_configurations(self, mock_exists, mock_file):
        mock_exists.return_value = True
        set_module_args(dict(
            dnac_host="1.1.1.1",
            dnac_username="dummy",
            dnac_password="dummy",
            dnac_version="2.3.7.9",
            dnac_log=True,
            state="gathered",
            config=self.playbook_config_generate_all_configurations
        ))
        result = self.execute_module(changed=True, failed=False)
        self.assertIn("YAML configuration file generated successfully", str(result.get('msg').get("message")))

    @patch('builtins.open', new_callable=mock_open)
    @patch('os.path.exists')
    def test_template_projects_by_name_single(self, mock_exists, mock_file):
        mock_exists.return_value = True
        set_module_args(dict(
            dnac_host="1.1.1.1",
            dnac_username="dummy",
            dnac_password="dummy",
            dnac_version="2.3.7.9",
            dnac_log=True,
            state="gathered",
            config=self.playbook_config_template_projects_by_name_single
        ))
        result = self.execute_module(changed=True, failed=False)
        self.assertIn("YAML configuration file generated successfully", str(result.get('msg').get("message")))

    @patch('builtins.open', new_callable=mock_open)
    @patch('os.path.exists')
    def test_template_projects_by_name_multiple(self, mock_exists, mock_file):
        mock_exists.return_value = True
        set_module_args(dict(
            dnac_host="1.1.1.1",
            dnac_username="dummy",
            dnac_password="dummy",
            dnac_version="2.3.7.9",
            dnac_log=True,
            state="gathered",
            config=self.playbook_config_template_projects_by_name_multiple
        ))
        result = self.execute_module(changed=True, failed=False)
        self.assertIn("YAML configuration file generated successfully", str(result.get('msg').get("message")))

    @patch('builtins.open', new_callable=mock_open)
    @patch('os.path.exists')
    def test_template_by_name_single(self, mock_exists, mock_file):
        mock_exists.return_value = True
        set_module_args(dict(
            dnac_host="1.1.1.1",
            dnac_username="dummy",
            dnac_password="dummy",
            dnac_version="2.3.7.9",
            dnac_log=True,
            state="gathered",
            config=self.playbook_config_template_by_name_single
        ))
        result = self.execute_module(changed=True, failed=False)
        self.assertIn("YAML configuration file generated successfully", str(result.get('msg').get("message")))

    @patch('builtins.open', new_callable=mock_open)
    @patch('os.path.exists')
    def test_template_by_name_multiple(self, mock_exists, mock_file):
        mock_exists.return_value = True
        set_module_args(dict(
            dnac_host="1.1.1.1",
            dnac_username="dummy",
            dnac_password="dummy",
            dnac_version="2.3.7.9",
            dnac_log=True,
            state="gathered",
            config=self.playbook_config_template_by_name_multiple
        ))
        result = self.execute_module(changed=True, failed=False)
        self.assertIn("YAML configuration file generated successfully", str(result.get('msg').get("message")))

    @patch('builtins.open', new_callable=mock_open)
    @patch('os.path.exists')
    def test_template_projects_empty_filter(self, mock_exists, mock_file):
        mock_exists.return_value = True
        set_module_args(dict(
            dnac_host="1.1.1.1",
            dnac_username="dummy",
            dnac_password="dummy",
            dnac_version="2.3.7.9",
            dnac_log=True,
            state="gathered",
            config=self.playbook_config_template_projects_empty_filter
        ))
        result = self.execute_module(changed=True, failed=False)
        self.assertIn("YAML configuration file generated successfully", str(result.get('msg').get("message")))

    @patch('builtins.open', new_callable=mock_open)
    @patch('os.path.exists')
    def test_templates_empty_filter(self, mock_exists, mock_file):
        mock_exists.return_value = True
        set_module_args(dict(
            dnac_host="1.1.1.1",
            dnac_username="dummy",
            dnac_password="dummy",
            dnac_version="2.3.7.9",
            dnac_log=True,
            state="gathered",
            config=self.playbook_config_templates_empty_filter
        ))
        result = self.execute_module(changed=True, failed=False)
        self.assertIn("YAML configuration file generated successfully", str(result.get('msg').get("message")))

    @patch('builtins.open', new_callable=mock_open)
    @patch('os.path.exists')
    def test_templates_includes_uncommitted_filter(self, mock_exists, mock_file):
        mock_exists.return_value = True
        set_module_args(dict(
            dnac_host="1.1.1.1",
            dnac_username="dummy",
            dnac_password="dummy",
            dnac_version="2.3.7.9",
            dnac_log=True,
            state="gathered",
            config=self.playbook_config_templates_includes_uncommitted_filter
        ))
        result = self.execute_module(changed=True, failed=False)
        self.assertIn("YAML configuration file generated successfully", str(result.get('msg').get("message")))

    @patch('builtins.open', new_callable=mock_open)
    @patch('os.path.exists')
    def test_template_by_project_name_multiple(self, mock_exists, mock_file):
        mock_exists.return_value = True
        set_module_args(dict(
            dnac_host="1.1.1.1",
            dnac_username="dummy",
            dnac_password="dummy",
            dnac_version="2.3.7.9",
            dnac_log=True,
            state="gathered",
            config=self.playbook_config_template_by_project_name_multiple
        ))
        result = self.execute_module(changed=True, failed=False)
        self.assertIn("YAML configuration file generated successfully", str(result.get('msg').get("message")))

    @patch('builtins.open', new_callable=mock_open)
    @patch('os.path.exists')
    def test_template_by_template_name_and_project_name(self, mock_exists, mock_file):
        mock_exists.return_value = True
        set_module_args(dict(
            dnac_host="1.1.1.1",
            dnac_username="dummy",
            dnac_password="dummy",
            dnac_version="2.3.7.9",
            dnac_log=True,
            state="gathered",
            config=self.playbook_config_template_by_template_name_and_project_name
        ))
        result = self.execute_module(changed=True, failed=False)
        self.assertIn("YAML configuration file generated successfully", str(result.get('msg').get("message")))

    @patch('builtins.open', new_callable=mock_open)
    @patch('os.path.exists')
    def test_template_all_filters(self, mock_exists, mock_file):
        mock_exists.return_value = True
        set_module_args(dict(
            dnac_host="1.1.1.1",
            dnac_username="dummy",
            dnac_password="dummy",
            dnac_version="2.3.7.9",
            dnac_log=True,
            state="gathered",
            config=self.playbook_config_template_all_filters
        ))
        result = self.execute_module(changed=True, failed=False)
        self.assertIn("YAML configuration file generated successfully", str(result.get('msg').get("message")))

    @patch('builtins.open', new_callable=mock_open)
    @patch('os.path.exists')
    def test_invalid_project_details(self, mock_exists, mock_file):
        mock_exists.return_value = True
        set_module_args(dict(
            dnac_host="1.1.1.1",
            dnac_username="dummy",
            dnac_password="dummy",
            dnac_version="2.3.7.9",
            dnac_log=True,
            state="gathered",
            config=self.playbook_invalid_project_details
        ))
        self.execute_module(changed=False, failed=True)

    @patch('builtins.open', new_callable=mock_open)
    @patch('os.path.exists')
    def test_invalid_template_details(self, mock_exists, mock_file):
        mock_exists.return_value = True
        set_module_args(dict(
            dnac_host="1.1.1.1",
            dnac_username="dummy",
            dnac_password="dummy",
            dnac_version="2.3.7.9",
            dnac_log=True,
            state="gathered",
            config=self.playbook_invalid_template_details
        ))
        self.execute_module(changed=False, failed=True)
