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
#   Unit tests for the Ansible module `brownfield_accesspoint_location_playbook_generator`.
#   These tests cover various scenarios for generating YAML playbooks from brownfield
#   access point location configurations in Cisco DNA Center.

# Make coding more python3-ish
from __future__ import absolute_import, division, print_function

__metaclass__ = type
from unittest.mock import patch, mock_open
from ansible_collections.cisco.dnac.plugins.modules import brownfield_accesspoint_location_playbook_generator
from .dnac_module import TestDnacModule, set_module_args, loadPlaybookData


class TestBrownfieldAccesspointLocationPlaybookGenerator(TestDnacModule):
    """
    Docstring for TestBrownfieldAccesspointLocationPlaybookGenerator
    """
    module = brownfield_accesspoint_location_playbook_generator
    test_data = loadPlaybookData("brownfield_accesspoint_location_playbook_generator")

    # Load all playbook configurations
    playbook_config_generate_all_config = test_data.get("playbook_config_generate_all_config")
    playbook_global_filter_realap_base = test_data.get("playbook_global_filter_realap_base")
    playbook_global_filter_pap_base = test_data.get("playbook_global_filter_pap_base")
    playbook_global_filter_site_base = test_data.get("playbook_global_filter_site_base")
    playbook_global_filter_model_base = test_data.get("playbook_global_filter_model_base")
    playbook_global_filter_mac_base = test_data.get("playbook_global_filter_mac_base")

    def setUp(self):
        super(TestBrownfieldAccesspointLocationPlaybookGenerator, self).setUp()

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
        super(TestBrownfieldAccesspointLocationPlaybookGenerator, self).tearDown()
        self.mock_dnac_exec.stop()
        self.mock_dnac_init.stop()

    def load_fixtures(self, response=None, device=""):
        """
        Load fixtures for brownfield accesspoint location playbook generator tests.
        """
        for each_filter_type in ["generate_all_configurations",
                                 "generate_global_filter_real",
                                 "generate_global_filter_pap",
                                 "generate_global_filter_site",
                                 "generate_global_filter_model",
                                 "generate_global_filter_mac"]:
            if each_filter_type in self._testMethodName:
                self.run_dnac_exec.side_effect = [
                    self.test_data.get("all_site_details"),
                    self.test_data.get("site_floor_response_planned_1"),
                    self.test_data.get("site_floor_response_real_1"),
                    self.test_data.get("site_floor_response_planned_2"),
                    self.test_data.get("site_empty_response"),
                    self.test_data.get("site_empty_response"),
                    self.test_data.get("site_floor_response_real_3")
                ]

    @patch('builtins.open', new_callable=mock_open)
    @patch('os.path.exists')
    def test_brownfield_accesspoint_location_generate_all_configurations(self, mock_exists, mock_file):
        """
        Test case for brownfield accesspoint location playbook generator when generating all profiles.
        This test case checks the behavior when generate_all_configurations is set to True,
        which should retrieve all access point location with Planned and real access points
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
    def test_brownfield_accesspoint_location_generate_global_filter_real(self, mock_exists, mock_file):
        """
        Test case for the brownfield access point location generator when the global
        filter is based on real access points.

        This test case verifies the behavior when the global filter is set to True.
        In this scenario, all access point locations associated with real access points
        should be retrieved, and a complete YAML playbook for access point locations
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
                config=self.playbook_global_filter_realap_base
            )
        )
        result = self.execute_module(changed=True, failed=False)
        self.assertIn("YAML config generation Task succeeded", str(result.get('msg')))

    @patch('builtins.open', new_callable=mock_open)
    @patch('os.path.exists')
    def test_brownfield_accesspoint_location_generate_global_filter_pap(self, mock_exists, mock_file):
        """
        Test case for the brownfield access point location generator when the global
        filter is based on planned access points.

        This test case verifies the behavior when the global filter is set to True.
        In this scenario, all access point locations associated with planned access
        points should be retrieved, and a complete YAML playbook for access point
        locations should be generated.
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
                config=self.playbook_global_filter_pap_base
            )
        )
        result = self.execute_module(changed=True, failed=False)
        self.assertIn("YAML config generation Task succeeded", str(result.get('msg')))

    @patch('builtins.open', new_callable=mock_open)
    @patch('os.path.exists')
    def test_brownfield_accesspoint_location_generate_global_filter_site(self, mock_exists, mock_file):
        """
        Test case for the brownfield access point location generator when the global
        filter is based on floors.

        This test case verifies the behavior when the global filter is set to True.
        In this scenario, access point location configurations should be retrieved
        based on floors, and a complete YAML playbook for access point locations
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
        self.assertIn("YAML config generation Task succeeded", str(result.get('msg')))

    @patch('builtins.open', new_callable=mock_open)
    @patch('os.path.exists')
    def test_brownfield_accesspoint_location_generate_global_filter_model(self, mock_exists, mock_file):
        """
        Test case for the brownfield access point location generator when the global
        filter is based on access point models.

        This test case verifies the behavior when the global filter is set to True.
        In this scenario, all access point location configurations associated with
        specific models should be retrieved, and a complete YAML playbook for access
        point locations should be generated.
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
                config=self.playbook_global_filter_model_base
            )
        )
        result = self.execute_module(changed=True, failed=False)
        self.assertIn("YAML config generation Task succeeded", str(result.get('msg')))

    @patch('builtins.open', new_callable=mock_open)
    @patch('os.path.exists')
    def test_brownfield_accesspoint_location_generate_global_filter_mac(self, mock_exists, mock_file):
        """
        Test case for the brownfield access point location generator when the global
        filter is based on access point mac address.

        This test case verifies the behavior when the global filter is set to True.
        In this scenario, all access point location configurations associated with
        specific mac addresses should be retrieved, and a complete YAML playbook for access
        point locations should be generated.
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
