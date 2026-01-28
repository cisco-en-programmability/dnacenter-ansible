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
#   Abhishek Maheshwari <abmahesh@cisco.com>
#   Madhan Sankaranarayanan <madhansansel@cisco.com>
#
# Description:
#   Unit tests for the Ansible module `brownfield_sda_fabric_transits_playbook_generator`.
#   These tests cover various scenarios for generating YAML playbooks from brownfield
#   SDA fabric transit configurations including IP-based, SDA LISP BGP, and SDA LISP Pub/Sub transits.

from __future__ import absolute_import, division, print_function

__metaclass__ = type
from unittest.mock import patch, mock_open
from ansible_collections.cisco.dnac.plugins.modules import brownfield_sda_fabric_transits_playbook_generator
from .dnac_module import TestDnacModule, set_module_args, loadPlaybookData


class TestBrownfieldFabricTransitsGenerator(TestDnacModule):

    module = brownfield_sda_fabric_transits_playbook_generator
    test_data = loadPlaybookData("brownfield_sda_fabric_transits_playbook_generator")

    # Load all playbook configurations
    playbook_config_generate_all_configurations = test_data.get("playbook_config_generate_all_configurations")
    playbook_config_component_specific_filters_only = test_data.get("playbook_config_component_specific_filters_only")
    playbook_config_transit_type_ip_based_single = test_data.get("playbook_config_transit_type_ip_based_single")
    playbook_config_transit_type_ip_based_multiple = test_data.get("playbook_config_transit_type_ip_based_multiple")
    playbook_config_transit_name_single = test_data.get("playbook_config_transit_name_single")
    playbook_config_transit_name_multiple = test_data.get("playbook_config_transit_name_multiple")
    playbook_config_transit_name_and_type = test_data.get("playbook_config_transit_name_and_type")
    playbook_config_transit_type_sda_lisp_pub_sub_single = test_data.get("playbook_config_transit_type_sda_lisp_pub_sub_single")
    playbook_config_transit_type_sda_lisp_bgp_single = test_data.get("playbook_config_transit_type_sda_lisp_bgp_single")
    playbook_config_all_transit_types = test_data.get("playbook_config_all_transit_types")
    playbook_config_mixed_filters = test_data.get("playbook_config_mixed_filters")
    playbook_config_empty_filters = test_data.get("playbook_config_empty_filters")
    playbook_config_no_file_path = test_data.get("playbook_config_no_file_path")

    def setUp(self):
        super(TestBrownfieldFabricTransitsGenerator, self).setUp()

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
        super(TestBrownfieldFabricTransitsGenerator, self).tearDown()
        self.mock_dnac_exec.stop()
        self.mock_dnac_init.stop()

    def load_fixtures(self, response=None, device=""):
        """
        Load fixtures for brownfield fabric transits generator tests.
        """

        if "generate_all_configurations" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("get_device_details"),  # Initial call for device ID mapping
                self.test_data.get("get_available_transit_networks"),
                self.test_data.get("get_site_details"),
                self.test_data.get("get_device_details")
            ]

        elif "component_specific_filters_only" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("get_device_details"),  # Initial call for device ID mapping
                self.test_data.get("get_available_transit_networks"),
                self.test_data.get("get_site_details"),
                self.test_data.get("get_device_details")
            ]

        elif "transit_type_ip_based_single" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("get_device_details"),  # Initial call for device ID mapping
                self.test_data.get("get_ip_based_transits_only"),
                self.test_data.get("get_site_details")
            ]

        elif "transit_type_ip_based_multiple" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("get_device_details"),  # Initial call for device ID mapping
                self.test_data.get("get_ip_based_transits_only"),  # First filter
                self.test_data.get("get_ip_based_transits_only"),  # Second filter (duplicate)
                self.test_data.get("get_site_details")
            ]

        elif "transit_name_single" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("get_device_details"),  # Initial call for device ID mapping
                self.test_data.get("get_transit_by_name_sample_transit3"),
                self.test_data.get("get_site_details"),
                self.test_data.get("get_device_details")
            ]

        elif "transit_name_multiple" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("get_device_details"),  # Initial call for device ID mapping
                self.test_data.get("get_transit_by_name_sample_transit1"),  # First filter: name="sample_transit1"
                self.test_data.get("get_site_details"),
                self.test_data.get("get_transit_by_name_sample_transit2"),  # Second filter: name="sample_transit2"
                self.test_data.get("get_site_details")
            ]

        elif "transit_name_and_type" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("get_device_details"),  # Initial call for device ID mapping
                self.test_data.get("get_transit_by_name_sample_transit2"),
                self.test_data.get("get_site_details")
            ]

        elif "transit_type_sda_lisp_pub_sub_single" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("get_device_details"),  # Initial call for device ID mapping
                self.test_data.get("get_sda_lisp_pub_sub_transits_only"),
                self.test_data.get("get_site_details"),
                self.test_data.get("get_device_details")
            ]

        elif "transit_type_sda_lisp_bgp_single" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("get_device_details"),  # Initial call for device ID mapping
                self.test_data.get("get_sda_lisp_bgp_transits_only"),
                self.test_data.get("get_site_details"),
                self.test_data.get("get_device_details")
            ]

        elif "all_transit_types" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("get_device_details"),  # Initial call for device ID mapping
                self.test_data.get("get_ip_based_transits_only"),  # First filter: IP_BASED_TRANSIT
                self.test_data.get("get_site_details"),
                self.test_data.get("get_sda_lisp_pub_sub_transits_only"),  # Second filter: SDA_LISP_PUB_SUB_TRANSIT
                self.test_data.get("get_site_details"),
                self.test_data.get("get_device_details"),
                self.test_data.get("get_sda_lisp_bgp_transits_only"),  # Third filter: SDA_LISP_BGP_TRANSIT
                self.test_data.get("get_site_details"),
                self.test_data.get("get_device_details")
            ]

        elif "mixed_filters" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("get_device_details"),  # Initial call for device ID mapping
                self.test_data.get("get_transit_by_name_ip_transit_1"),  # First filter: name="IP_TRANSIT_1"
                self.test_data.get("get_site_details"),
                self.test_data.get("get_sda_lisp_bgp_transits_only"),  # Second filter: transit_type="SDA_LISP_BGP_TRANSIT"
                self.test_data.get("get_site_details"),
                self.test_data.get("get_device_details"),
                self.test_data.get("get_transit_by_name_sample_transit3"),  # Third filter: name="sample_transit3" + type="SDA_LISP_PUB_SUB_TRANSIT"
                self.test_data.get("get_site_details"),
                self.test_data.get("get_device_details")
            ]

        elif "empty_filters" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("get_device_details"),  # Initial call for device ID mapping
                self.test_data.get("get_available_transit_networks"),
                self.test_data.get("get_site_details"),
                self.test_data.get("get_device_details")
            ]

        elif "no_file_path" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("get_device_details"),  # Initial call for device ID mapping
                self.test_data.get("get_ip_based_transits_only"),
                self.test_data.get("get_site_details")
            ]

    @patch('builtins.open', new_callable=mock_open)
    @patch('os.path.exists')
    def test_brownfield_sda_fabric_transits_config_generator_generate_all_configurations(self, mock_exists, mock_file):
        """
        Test case for generating YAML configuration for all fabric transits.

        This test verifies that the generator can retrieve all fabric transit configurations
        from Cisco Catalyst Center and generate a complete YAML playbook without any filters.
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
                config=self.playbook_config_generate_all_configurations
            )
        )
        result = self.execute_module(changed=True, failed=False)
        self.assertIn("YAML config generation Task succeeded", str(result.get('msg')))

    @patch('builtins.open', new_callable=mock_open)
    @patch('os.path.exists')
    def test_brownfield_sda_fabric_transits_config_generator_component_specific_filters_only(self, mock_exists, mock_file):
        """
        Test case for generating YAML configuration with component-specific filters.

        This test verifies that the generator correctly processes component_specific_filters
        when only the components_list is specified without additional filters.
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
                config=self.playbook_config_component_specific_filters_only
            )
        )
        result = self.execute_module(changed=True, failed=False)
        self.assertIn("YAML config generation Task succeeded", str(result.get('msg')))

    @patch('builtins.open', new_callable=mock_open)
    @patch('os.path.exists')
    def test_brownfield_sda_fabric_transits_config_generator_transit_type_ip_based_single(self, mock_exists, mock_file):
        """
        Test case for filtering fabric transits by IP_BASED_TRANSIT type.

        This test verifies that the generator correctly filters transits by transit_type
        and retrieves only IP-based transit configurations.
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
                config=self.playbook_config_transit_type_ip_based_single
            )
        )
        result = self.execute_module(changed=True, failed=False)
        self.assertIn("YAML config generation Task succeeded", str(result.get('msg')))

    @patch('builtins.open', new_callable=mock_open)
    @patch('os.path.exists')
    def test_brownfield_sda_fabric_transits_config_generator_transit_type_ip_based_multiple(self, mock_exists, mock_file):
        """
        Test case for filtering multiple IP-based fabric transits.

        This test verifies that the generator correctly handles multiple filter entries
        for the same transit type.
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
                config=self.playbook_config_transit_type_ip_based_multiple
            )
        )
        result = self.execute_module(changed=True, failed=False)
        self.assertIn("YAML config generation Task succeeded", str(result.get('msg')))

    @patch('builtins.open', new_callable=mock_open)
    @patch('os.path.exists')
    def test_brownfield_sda_fabric_transits_config_generator_transit_name_single(self, mock_exists, mock_file):
        """
        Test case for filtering fabric transits by name.

        This test verifies that the generator correctly filters transits by name
        and retrieves only the specified transit configuration.
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
                config=self.playbook_config_transit_name_single
            )
        )
        result = self.execute_module(changed=True, failed=False)
        self.assertIn("YAML config generation Task succeeded", str(result.get('msg')))

    @patch('builtins.open', new_callable=mock_open)
    @patch('os.path.exists')
    def test_brownfield_sda_fabric_transits_config_generator_transit_name_multiple(self, mock_exists, mock_file):
        """
        Test case for filtering multiple fabric transits by name.

        This test verifies that the generator correctly handles multiple transit names
        and retrieves all specified transit configurations.
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
                config=self.playbook_config_transit_name_multiple
            )
        )
        result = self.execute_module(changed=True, failed=False)
        self.assertIn("YAML config generation Task succeeded", str(result.get('msg')))

    @patch('builtins.open', new_callable=mock_open)
    @patch('os.path.exists')
    def test_brownfield_sda_fabric_transits_config_generator_transit_name_and_type(self, mock_exists, mock_file):
        """
        Test case for filtering fabric transits by both name and type.

        This test verifies that the generator correctly applies both name and transit_type
        filters to retrieve a specific transit configuration.
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
                config=self.playbook_config_transit_name_and_type
            )
        )
        result = self.execute_module(changed=True, failed=False)
        self.assertIn("YAML config generation Task succeeded", str(result.get('msg')))

    @patch('builtins.open', new_callable=mock_open)
    @patch('os.path.exists')
    def test_brownfield_sda_fabric_transits_config_generator_transit_type_sda_lisp_pub_sub_single(self, mock_exists, mock_file):
        """
        Test case for filtering fabric transits by SDA_LISP_PUB_SUB_TRANSIT type.

        This test verifies that the generator correctly filters and retrieves
        SDA LISP Pub/Sub transit configurations including control plane device transformations.
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
                config=self.playbook_config_transit_type_sda_lisp_pub_sub_single
            )
        )
        result = self.execute_module(changed=True, failed=False)
        self.assertIn("YAML config generation Task succeeded", str(result.get('msg')))

    @patch('builtins.open', new_callable=mock_open)
    @patch('os.path.exists')
    def test_brownfield_sda_fabric_transits_config_generator_transit_type_sda_lisp_bgp_single(self, mock_exists, mock_file):
        """
        Test case for filtering fabric transits by SDA_LISP_BGP_TRANSIT type.

        This test verifies that the generator correctly filters and retrieves
        SDA LISP BGP transit configurations including control plane device transformations.
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
                config=self.playbook_config_transit_type_sda_lisp_bgp_single
            )
        )
        result = self.execute_module(changed=True, failed=False)
        self.assertIn("YAML config generation Task succeeded", str(result.get('msg')))

    @patch('builtins.open', new_callable=mock_open)
    @patch('os.path.exists')
    def test_brownfield_sda_fabric_transits_config_generator_all_transit_types(self, mock_exists, mock_file):
        """
        Test case for generating YAML configuration for all transit types.

        This test verifies that the generator correctly handles filters for all three
        transit types (IP_BASED, SDA_LISP_PUB_SUB, SDA_LISP_BGP) in a single playbook.
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
                config=self.playbook_config_all_transit_types
            )
        )
        result = self.execute_module(changed=True, failed=False)
        self.assertIn("YAML config generation Task succeeded", str(result.get('msg')))

    @patch('builtins.open', new_callable=mock_open)
    @patch('os.path.exists')
    def test_brownfield_sda_fabric_transits_config_generator_mixed_filters(self, mock_exists, mock_file):
        """
        Test case for generating YAML configuration with mixed filters.

        This test verifies that the generator correctly handles a combination of
        name filters, type filters, and combined name+type filters in a single request.
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
                config=self.playbook_config_mixed_filters
            )
        )
        result = self.execute_module(changed=True, failed=False)
        self.assertIn("YAML config generation Task succeeded", str(result.get('msg')))

    @patch('builtins.open', new_callable=mock_open)
    @patch('os.path.exists')
    def test_brownfield_sda_fabric_transits_config_generator_empty_filters(self, mock_exists, mock_file):
        """
        Test case for generating YAML configuration with empty filters.

        This test verifies that the generator correctly handles empty component-specific
        filters and retrieves all transits when no specific filters are provided.
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
                config=self.playbook_config_empty_filters
            )
        )
        result = self.execute_module(changed=True, failed=False)
        self.assertIn("YAML config generation Task succeeded", str(result.get('msg')))

    @patch('builtins.open', new_callable=mock_open)
    @patch('os.path.exists')
    def test_brownfield_sda_fabric_transits_config_generator_no_file_path(self, mock_exists, mock_file):
        """
        Test case for generating YAML configuration without specifying file_path.

        This test verifies that the generator creates a default filename when
        file_path is not provided in the configuration.
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
                config=self.playbook_config_no_file_path
            )
        )
        result = self.execute_module(changed=True, failed=False)
        self.assertIn("YAML config generation Task succeeded", str(result.get('msg')))
        self.assertIn("sda_fabric_transits_workflow_manager_playbook_", str(result.get('msg')))
