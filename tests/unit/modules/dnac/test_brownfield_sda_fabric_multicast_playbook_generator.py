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
#   Unit tests for the Ansible module `brownfield_sda_fabric_multicast_playbook_generator`.
#   These tests cover various playbook generation scenarios for SDA fabric multicast configurations
#   using mocked Catalyst Center responses.

from __future__ import absolute_import, division, print_function

# Metadata
__metaclass__ = type
__author__ = "Archit Soni"
__email__ = "soni.archit03@gmail.com"
__version__ = "1.0.0"

from unittest.mock import patch
from ansible_collections.cisco.dnac.plugins.modules import (
    brownfield_sda_fabric_multicast_playbook_generator,
)
from .dnac_module import TestDnacModule, set_module_args, loadPlaybookData


class TestBrownfieldSdaFabricMulticastPlaybookGenerator(TestDnacModule):

    module = brownfield_sda_fabric_multicast_playbook_generator
    test_data = loadPlaybookData("brownfield_sda_fabric_multicast_playbook_generator")

    playbook_config_generate_all_configurations_case_1 = test_data.get(
        "generate_all_configurations_case_1"
    )
    playbook_config_generate_specific_fabric_site_case_2 = test_data.get(
        "generate_specific_fabric_site_case_2"
    )
    playbook_config_generate_specific_fabric_and_vn_case_3 = test_data.get(
        "generate_specific_fabric_and_vn_case_3"
    )
    playbook_config_generate_multiple_fabric_sites_case_4 = test_data.get(
        "generate_multiple_fabric_sites_case_4"
    )
    playbook_config_invalid_fabric_site_case_5 = test_data.get(
        "invalid_fabric_site_case_5"
    )
    playbook_config_no_multicast_configs_case_6 = test_data.get(
        "no_multicast_configs_case_6"
    )
    playbook_config_fabric_site_not_in_sda_case_7 = test_data.get(
        "fabric_site_not_in_sda_case_7"
    )

    def setUp(self):
        super(TestBrownfieldSdaFabricMulticastPlaybookGenerator, self).setUp()

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
        super(TestBrownfieldSdaFabricMulticastPlaybookGenerator, self).tearDown()
        self.mock_dnac_exec.stop()
        self.mock_dnac_init.stop()

    def load_fixtures(self, response=None, device=""):
        """
        Load fixtures for brownfield SDA fabric multicast playbook generator tests.
        """
        if "test_generate_all_configurations_case_1" in self._testMethodName:
            # Case 1: Generate all configurations
            # Only 1 fabric has multicast VN configs (fabric ID 085089aa-5077-440c-bf98-3028f87ce067)
            self.run_dnac_exec.side_effect = [
                self.test_data.get("get_sites_case_1"),
                self.test_data.get("get_multicast_case_1"),
                self.test_data.get("get_multicast_virtual_networks_case_1"),
                self.test_data.get("get_fabric_sites_case_1_call_1"),
                self.test_data.get("get_device_list_case_1"),
            ]
        elif "test_generate_specific_fabric_site_case_2" in self._testMethodName:
            # Case 2: Specific fabric site with fabric_name filter
            # Reuses case 1 data but with filter
            self.run_dnac_exec.side_effect = [
                self.test_data.get("get_sites_case_1"),
                self.test_data.get("get_fabric_sites_case_1_call_1"),
                self.test_data.get("get_multicast_case_1"),
                self.test_data.get("get_multicast_virtual_networks_case_2"),
                self.test_data.get("get_fabric_sites_case_1_call_1"),
                self.test_data.get("get_device_list_case_1"),
            ]
        elif "test_generate_specific_fabric_and_vn_case_3" in self._testMethodName:
            # Case 3: Specific fabric site and virtual network filters
            # Reuses case 1 data but with both fabric and VN filters
            self.run_dnac_exec.side_effect = [
                self.test_data.get("get_sites_case_1"),
                self.test_data.get("get_fabric_sites_case_1_call_1"),
                self.test_data.get("get_multicast_case_1"),
                self.test_data.get("get_multicast_virtual_networks_case_3"),
                self.test_data.get("get_fabric_sites_case_1_call_1"),
                self.test_data.get("get_device_list_case_1"),
            ]
        elif "test_generate_multiple_fabric_sites_case_4" in self._testMethodName:
            # Case 4: Multiple fabric sites - simulate 2 fabrics with separate VN configs
            # This will create 2 new fabric IDs using modified case 1 data
            self.run_dnac_exec.side_effect = [
                self.test_data.get("get_sites_case_1"),
                self.test_data.get("get_fabric_sites_case_1_call_1"),
                self.test_data.get("get_multicast_case_4"),
                self.test_data.get("get_multicast_virtual_networks_case_1"),
                self.test_data.get("get_fabric_sites_case_1_call_1"),
                self.test_data.get("get_device_list_case_1"),
            ]
        elif "test_invalid_fabric_site_case_5" in self._testMethodName:
            # Case 5: Invalid fabric site name provided in filter
            # Site lookup returns real data but specified site name doesn't match
            self.run_dnac_exec.side_effect = [
                self.test_data.get("get_sites_case_1"),
                self.test_data.get("get_multicast_case_1"),
            ]
        elif "test_no_multicast_configs_case_6" in self._testMethodName:
            # Case 6: No multicast configurations exist in CATC
            # All APIs return empty responses since no multicast configs exist
            self.run_dnac_exec.side_effect = [
                self.test_data.get("get_sites_case_1"),
                self.test_data.get("get_multicast_case_6"),
                self.test_data.get("get_multicast_virtual_networks_case_6"),
                self.test_data.get("get_fabric_sites_case_6"),
                self.test_data.get("get_device_list_case_6"),
            ]
        elif "test_fabric_site_not_in_sda_case_7" in self._testMethodName:
            # Case 7: Site exists but not in SDA (not a fabric site or zone)
            # Site lookup succeeds, but get_fabric_sites returns empty (site not a fabric)
            self.run_dnac_exec.side_effect = [
                self.test_data.get("get_sites_case_1"),
                self.test_data.get("get_fabric_sites_case_7"),
                self.test_data.get("get_multicast_case_6"),
                self.test_data.get("get_multicast_virtual_networks_case_6"),
            ]

    def test_generate_all_configurations_case_1(self):
        """
        Test generating YAML playbook for all SDA fabric multicast configurations.
        """

        set_module_args(
            dict(
                dnac_host="1.1.1.1",
                dnac_username="dummy",
                dnac_password="dummy",
                dnac_version="2.3.7.9",
                dnac_log=True,
                dnac_log_level="DEBUG",
                state="gathered",
                config=self.playbook_config_generate_all_configurations_case_1,
            )
        )
        result = self.execute_module(changed=True, failed=False)
        self.assertIn("YAML config generation Task succeeded", str(result.get("msg")))

    def test_generate_specific_fabric_site_case_2(self):
        """
        Test generating YAML playbook for a specific fabric site.
        """

        set_module_args(
            dict(
                dnac_host="1.1.1.1",
                dnac_username="dummy",
                dnac_password="dummy",
                dnac_version="2.3.7.9",
                dnac_log=True,
                state="gathered",
                config=self.playbook_config_generate_specific_fabric_site_case_2,
            )
        )
        result = self.execute_module(changed=True, failed=False)
        self.assertIn("YAML config generation Task succeeded", str(result.get("msg")))

    def test_generate_specific_fabric_and_vn_case_3(self):
        """
        Test generating YAML playbook for specific fabric site and virtual network.
        """

        set_module_args(
            dict(
                dnac_host="1.1.1.1",
                dnac_username="dummy",
                dnac_password="dummy",
                dnac_version="2.3.7.9",
                dnac_log=True,
                state="gathered",
                config=self.playbook_config_generate_specific_fabric_and_vn_case_3,
            )
        )
        result = self.execute_module(changed=True, failed=False)
        self.assertIn("YAML config generation Task succeeded", str(result.get("msg")))

    def test_generate_multiple_fabric_sites_case_4(self):
        """
        Test generating YAML playbook for multiple fabric sites.
        """

        set_module_args(
            dict(
                dnac_host="1.1.1.1",
                dnac_username="dummy",
                dnac_password="dummy",
                dnac_version="2.3.7.9",
                dnac_log=True,
                state="gathered",
                config=self.playbook_config_generate_multiple_fabric_sites_case_4,
            )
        )
        result = self.execute_module(changed=True, failed=False)
        self.assertIn("YAML config generation Task succeeded", str(result.get("msg")))

    def test_invalid_fabric_site_case_5(self):
        """
        Test handling of invalid fabric site name.
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
                config=self.playbook_config_invalid_fabric_site_case_5,
            )
        )
        result = self.execute_module(changed=True, failed=False)
        self.assertIn("YAML config generation Task succeeded", str(result.get("msg")))

    def test_no_multicast_configs_case_6(self):
        """
        Test handling when no multicast configurations exist in Catalyst Center.
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
                config=self.playbook_config_no_multicast_configs_case_6,
            )
        )
        result = self.execute_module(changed=True, failed=False)
        self.assertIn("YAML config generation Task succeeded", str(result.get("msg")))

    def test_fabric_site_not_in_sda_case_7(self):
        """
        Test handling when specified site is not configured as a fabric site or fabric zone.
        """
        set_module_args(
            dict(
                dnac_host="1.1.1.1",
                dnac_username="dummy",
                dnac_password="dummy",
                dnac_version="2.3.7.9",
                dnac_log=True,
                state="gathered",
                config=self.playbook_config_fabric_site_not_in_sda_case_7,
            )
        )
        result = self.execute_module(changed=True, failed=False)
        self.assertIn("YAML config generation Task succeeded", str(result.get("msg")))
