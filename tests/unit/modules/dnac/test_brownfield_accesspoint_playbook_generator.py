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
#   Unit tests for the Ansible module `brownfield_accesspoint_playbook_generator`.
#   These tests cover various scenarios for generating YAML playbooks from brownfield
#   access point configurations in Cisco DNA Center.

# Make coding more python3-ish
from __future__ import absolute_import, division, print_function

__metaclass__ = type
from unittest.mock import patch, mock_open
from ansible_collections.cisco.dnac.plugins.modules import brownfield_accesspoint_playbook_generator
from .dnac_module import TestDnacModule, set_module_args, loadPlaybookData


class TestBrownfieldAccesspointPlaybookGenerator(TestDnacModule):
    """
    Docstring for TestBrownfieldAccesspointLocationPlaybookGenerator
    """
    module = brownfield_accesspoint_playbook_generator
    test_data = loadPlaybookData("brownfield_accesspoint_playbook_generator")

    # Load all playbook configurations
    playbook_config_generate_all_config = test_data.get("playbook_config_generate_all_config")
    playbook_global_filter_apconfig_base = test_data.get("playbook_global_filter_apconfig_base")
    playbook_global_filter_provision_base = test_data.get("playbook_global_filter_provision_base")
    playbook_global_filter_site_base = test_data.get("playbook_global_filter_site_base")
    playbook_global_filter_hostname_base = test_data.get("playbook_global_filter_hostname_base")
    playbook_global_filter_mac_base = test_data.get("playbook_global_filter_mac_base")

    def setUp(self):
        super(TestBrownfieldAccesspointPlaybookGenerator, self).setUp()

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
        super(TestBrownfieldAccesspointPlaybookGenerator, self).tearDown()
        self.mock_dnac_exec.stop()
        self.mock_dnac_init.stop()

    def load_fixtures(self, response=None, device=""):
        """
        Load fixtures for brownfield accesspoint configuration playbook generator tests.
        """
        for each_filter_type in ["generate_all_configurations",
                                 "generate_global_filter_apconfig",
                                 "generate_global_filter_provision",
                                 "generate_global_filter_site",
                                 "generate_global_filter_provision_config",
                                 "generate_global_filter_mac"]:
            if each_filter_type in self._testMethodName:
                self.run_dnac_exec.side_effect = [
                    self.test_data.get("all_devices_details"),
                    self.test_data.get("ap_configuration_1"),
                    self.test_data.get("ap_configuration_2"),
                    self.test_data.get("ap_configuration_3")
                ]

    @patch('builtins.open', new_callable=mock_open)
    @patch('os.path.exists')
    def test_brownfield_accesspoint_playbook_generate_all_configurations(self, mock_exists, mock_file):
        """
        Test case for brownfield accesspoint playbook generator when generating all profiles.
        This test case checks the behavior when generate_all_configurations is set to True,
        which should retrieve all access point configuration with Provision access points
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
                config=self.playbook_config_generate_all_config
            )
        )
        result = self.execute_module(changed=True, failed=False)
        self.maxDiff = None
        self.assertIn("YAML config generation Task succeeded", str(result.get('msg')))

    @patch('builtins.open', new_callable=mock_open)
    @patch('os.path.exists')
    def test_brownfield_accesspoint_playbook_generate_global_filter_apconfig(self, mock_exists, mock_file):
        """
        Test case for the brownfield access point playbook generator when the global
        filter is based on real access points.

        This test case verifies the behavior when the global filter is set to True.
        In this scenario, all access point configurations associated access points configurations
        should be retrieved, and a complete YAML playbook for access point configurations
        should be generated.
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
                config=self.playbook_global_filter_apconfig_base
            )
        )
        result = self.execute_module(changed=True, failed=False)
        self.assertIn("YAML config generation Task succeeded", str(result.get('msg')))

    @patch('builtins.open', new_callable=mock_open)
    @patch('os.path.exists')
    def test_brownfield_accesspoint_playbook_generate_global_filter_provision(self, mock_exists, mock_file):
        """
        Test case for the brownfield access point playbook generator when the global
        filter is based on planned access points.

        This test case verifies the behavior when the global filter is set to True.
        In this scenario, all provisioned access points should be retrieved, and a complete
        YAML playbook for access point configurations should be generated.
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
                config=self.playbook_global_filter_provision_base
            )
        )
        result = self.execute_module(changed=True, failed=False)
        self.assertIn("YAML config generation Task succeeded", str(result.get('msg')))

    @patch('builtins.open', new_callable=mock_open)
    @patch('os.path.exists')
    def test_brownfield_accesspoint_playbook_generate_global_filter_site(self, mock_exists, mock_file):
        """
        Test case for the brownfield access point generator when the global
        filter is based on floors.

        This test case verifies the behavior when the global filter is set to True.
        In this scenario, access point configurations should be retrieved
        based on floors, and a complete YAML playbook for access point configurations
        should be generated.
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
        self.assertIn("Some access point configurations were not processed:", str(result.get('msg')))

    @patch('builtins.open', new_callable=mock_open)
    @patch('os.path.exists')
    def test_brownfield_accesspoint_playbook_generate_global_filter_provision_config(self, mock_exists, mock_file):
        """
        Test case for the brownfield access point playbook generator when the global
        filter is based on access point models.

        This test case verifies the behavior when the global filter is set to True.
        In this scenario, all access point configurations associated with
        specific models should be retrieved, and a complete YAML playbook for access
        point configurations should be generated.
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
                config=self.playbook_global_filter_hostname_base
            )
        )
        result = self.execute_module(changed=True, failed=False)
        self.assertIn("YAML config generation Task succeeded", str(result.get('msg')))

    @patch('builtins.open', new_callable=mock_open)
    @patch('os.path.exists')
    def test_brownfield_accesspoint_playbook_generate_global_filter_mac(self, mock_exists, mock_file):
        """
        Test case for the brownfield access point playbook generator when the global
        filter is based on access point mac address.

        This test case verifies the behavior when the global filter is set to True.
        In this scenario, all access point configurations associated with
        specific mac addresses should be retrieved, and a complete YAML playbook for access
        point configurations should be generated.
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
                config=self.playbook_global_filter_mac_base
            )
        )
        result = self.execute_module(changed=True, failed=False)
        self.assertIn("YAML config generation Task succeeded", str(result.get('msg')))
