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
#   Unit tests for the Ansible module `sda_fabric_devices_playbook_config_generator`.
#   These tests cover YAML playbook generation for SDA fabric devices configurations,
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
    sda_fabric_devices_playbook_config_generator,
)
from .dnac_module import TestDnacModule, set_module_args, loadPlaybookData


class TestDnacBrownfieldSdaFabricDevicesPlaybookGenerator(TestDnacModule):

    module = sda_fabric_devices_playbook_config_generator
    test_data = loadPlaybookData("sda_fabric_devices_playbook_config_generator")

    playbook_config_generate_all_configurations_case_1 = test_data.get(
        "generate_all_configurations_case_1"
    )
    playbook_config_filter_fabric_name_only_case_2 = test_data.get(
        "filter_fabric_name_only_case_2"
    )
    playbook_config_filter_fabric_name_device_ip_case_3 = test_data.get(
        "filter_fabric_name_device_ip_case_3"
    )
    playbook_config_filter_fabric_name_edge_role_case_4 = test_data.get(
        "filter_fabric_name_edge_role_case_4"
    )
    playbook_config_filter_fabric_name_multi_roles_case_5 = test_data.get(
        "filter_fabric_name_multi_roles_case_5"
    )
    playbook_config_filter_all_filters_case_6 = test_data.get(
        "filter_all_filters_case_6"
    )
    playbook_config_filter_fabric_name_cp_role_case_7 = test_data.get(
        "filter_fabric_name_cp_role_case_7"
    )
    playbook_config_filter_fabric_name_border_role_case_8 = test_data.get(
        "filter_fabric_name_border_role_case_8"
    )
    playbook_config_filter_with_components_list_case_9 = test_data.get(
        "filter_with_components_list_case_9"
    )

    def setUp(self):
        super(TestDnacBrownfieldSdaFabricDevicesPlaybookGenerator, self).setUp()

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
        super(TestDnacBrownfieldSdaFabricDevicesPlaybookGenerator, self).tearDown()
        self.mock_dnac_exec.stop()
        self.mock_dnac_init.stop()

    def load_fixtures(self, response=None, device=""):
        """
        Load fixtures for sda_fabric_devices_playbook_config_generator tests.
        """
        if "test_generate_all_configurations_case_1" in self._testMethodName:
            # API call sequence for generate_all_configurations:
            # 1. get_sites - site_design family
            # 2. get_fabric_sites - sda family
            # 3. get_transit_networks - sda family
            # 4. get_fabric_devices - sda family (4 calls, one per fabric site)
            # 5. get_network_device_list - devices family (for device IP lookups)
            # 6. get_fabric_site_wired_settings - sda family (for embedded wireless controller settings)
            # 7. get_fabric_devices_layer2_handoffs - sda family (for each device)
            # 8. get_fabric_devices_layer3_handoffs_with_ip_transit - sda family (for each device)
            # 9. get_fabric_devices_layer3_handoffs_with_sda_transit - sda family (for each device)

            self.run_dnac_exec.side_effect = [
                # 1. get_sites
                self.test_data.get("get_sites_case_1"),
                # 2. get_fabric_sites
                self.test_data.get("get_fabric_sites_case_1"),
                # 3. get_transit_networks
                self.test_data.get("get_transit_networks_case_1"),
                # 4. get_fabric_devices for fabric site 1 (Global/Site_India/Karnataka/Bangalore)
                self.test_data.get("get_fabric_devices_fabric_1_case_1"),
                # 5. get_network_device_list for device 1 (205.1.2.67)
                self.test_data.get("get_device_list_device_1_case_1"),
                # 6. get_network_device_list for device 2 (205.1.1.10)
                self.test_data.get("get_device_list_device_2_case_1"),
                # 7. get_network_device_list for device 3 (205.1.2.68)
                self.test_data.get("get_device_list_device_3_case_1"),
                # 8. get_fabric_devices for fabric site 2 (Global/Site_India/Tamil_Nadu/Chennai) - empty
                self.test_data.get("get_fabric_devices_empty_response"),
                # 9. get_fabric_devices for fabric site 3 (Global/India/Telangana/Hyderabad/BLD_1)
                self.test_data.get("get_fabric_devices_fabric_3_case_1"),
                # 10. get_network_device_list for device 4 (172.27.248.223)
                self.test_data.get("get_device_list_device_4_case_1"),
                # 11. get_network_device_list for device 5 (172.27.248.222)
                self.test_data.get("get_device_list_device_5_case_1"),
                # 12. get_fabric_devices for fabric site 4 (Global/USA) - empty
                self.test_data.get("get_fabric_devices_empty_response"),
                # 13. get_fabric_site_wired_settings for fabric site 1 (embedded wireless controller settings)
                self.test_data.get(
                    "get_embedded_wireless_controller_settings_empty_response"
                ),
                # 14. get_fabric_site_wired_settings for fabric site 3 (embedded wireless controller settings)
                self.test_data.get(
                    "get_embedded_wireless_controller_settings_empty_response"
                ),
                # Border handoff settings for fabric site 1 devices (3 devices)
                # Device 1: layer2, layer3_ip, layer3_sda
                self.test_data.get("get_layer2_handoffs_empty_response"),
                self.test_data.get("get_layer3_ip_transit_handoffs_empty_response"),
                self.test_data.get("get_layer3_sda_transit_handoffs_empty_response"),
                # Device 2: layer2, layer3_ip (has handoffs), layer3_sda
                self.test_data.get("get_layer2_handoffs_empty_response"),
                self.test_data.get("get_layer3_ip_transit_handoffs_device_2_case_1"),
                self.test_data.get("get_layer3_sda_transit_handoffs_empty_response"),
                # Device 3: layer2, layer3_ip, layer3_sda
                self.test_data.get("get_layer2_handoffs_empty_response"),
                self.test_data.get("get_layer3_ip_transit_handoffs_empty_response"),
                self.test_data.get("get_layer3_sda_transit_handoffs_empty_response"),
                # Border handoff settings for fabric site 3 devices (2 devices)
                # Device 4: layer2, layer3_ip, layer3_sda
                self.test_data.get("get_layer2_handoffs_empty_response"),
                self.test_data.get("get_layer3_ip_transit_handoffs_empty_response"),
                self.test_data.get("get_layer3_sda_transit_handoffs_empty_response"),
                # Device 5: layer2, layer3_ip, layer3_sda
                self.test_data.get("get_layer2_handoffs_empty_response"),
                self.test_data.get("get_layer3_ip_transit_handoffs_empty_response"),
                self.test_data.get("get_layer3_sda_transit_handoffs_empty_response"),
            ]

        elif "test_filter_fabric_name_only_case_2" in self._testMethodName:
            # Test Case 2: Filter by fabric_name only
            # API call sequence:
            # 1. get_sites - site_design family (for initialization)
            # 2. get_fabric_sites - sda family (for initialization)
            # 3. get_transit_networks - sda family (for initialization)
            # 4. get_fabric_devices - sda family (for the specific fabric - returns 3 devices)
            # 5. get_network_device_list - devices family (for each device - 3 calls)
            # 6. get_fabric_site_wired_settings - sda family (for embedded wireless controller)
            # 7. Border handoff APIs - for each device (3 devices x 3 handoff types = 9 calls)

            self.run_dnac_exec.side_effect = [
                # Initialization phase
                self.test_data.get("get_sites_case_1"),
                self.test_data.get("get_fabric_sites_case_1"),
                self.test_data.get("get_transit_networks_case_1"),
                # get_fabric_devices for Bangalore fabric (3 devices)
                self.test_data.get("get_fabric_devices_fabric_1_case_1"),
                # get_network_device_list for each device
                self.test_data.get("get_device_list_device_1_case_1"),
                self.test_data.get("get_device_list_device_2_case_1"),
                self.test_data.get("get_device_list_device_3_case_1"),
                # get_fabric_site_wired_settings
                self.test_data.get(
                    "get_embedded_wireless_controller_settings_empty_response"
                ),
                # Border handoff settings for 3 devices
                # Device 1
                self.test_data.get("get_layer2_handoffs_empty_response"),
                self.test_data.get("get_layer3_ip_transit_handoffs_empty_response"),
                self.test_data.get("get_layer3_sda_transit_handoffs_empty_response"),
                # Device 2 (has IP transit handoffs)
                self.test_data.get("get_layer2_handoffs_empty_response"),
                self.test_data.get("get_layer3_ip_transit_handoffs_device_2_case_1"),
                self.test_data.get("get_layer3_sda_transit_handoffs_empty_response"),
                # Device 3
                self.test_data.get("get_layer2_handoffs_empty_response"),
                self.test_data.get("get_layer3_ip_transit_handoffs_empty_response"),
                self.test_data.get("get_layer3_sda_transit_handoffs_empty_response"),
            ]

        elif "test_filter_fabric_name_device_ip_case_3" in self._testMethodName:
            # Test Case 3: Filter by fabric_name + device_ip
            # This filters to a single device (205.1.1.10 - the border/CP node)
            # When device_ip is specified, module first queries device_list to get network_device_id
            # Then queries fabric_devices with both fabric_id and networkDeviceId

            self.run_dnac_exec.side_effect = [
                # Initialization phase
                self.test_data.get("get_sites_case_1"),
                self.test_data.get("get_fabric_sites_case_1"),
                self.test_data.get("get_transit_networks_case_1"),
                # get_device_list to resolve device_ip to network_device_id (EXTRA call for device_ip filter)
                self.test_data.get("get_device_list_device_2_case_1"),
                # get_fabric_devices with fabric_id + networkDeviceId - returns only the matching device
                self.test_data.get("get_fabric_devices_filtered_border_cp_case_1"),
                # get_fabric_site_wired_settings
                self.test_data.get(
                    "get_embedded_wireless_controller_settings_empty_response"
                ),
                # Border handoff settings for 1 filtered device (205.1.1.10)
                self.test_data.get("get_layer2_handoffs_empty_response"),
                self.test_data.get("get_layer3_ip_transit_handoffs_device_2_case_1"),
                self.test_data.get("get_layer3_sda_transit_handoffs_empty_response"),
            ]

        elif "test_filter_fabric_name_edge_role_case_4" in self._testMethodName:
            # Test Case 4: Filter by fabric_name + device_roles (EDGE_NODE)
            # API filters by deviceRoles and returns only 2 edge node devices directly
            # API call sequence from dnac.log:
            # 1. get_sites, get_fabric_sites, get_transit_networks (initialization)
            # 2. get_fabric_devices with deviceRoles=['EDGE_NODE'] - returns 2 edge nodes
            # 3. get_network_device_list for each device (2 calls)
            # 4. get_fabric_site_wired_settings (1 call)
            # 5. Border handoff APIs for each device (2 devices x 3 types = 6 calls)

            self.run_dnac_exec.side_effect = [
                # Initialization phase
                self.test_data.get("get_sites_case_1"),
                self.test_data.get("get_fabric_sites_case_1"),
                self.test_data.get("get_transit_networks_case_1"),
                # get_fabric_devices with deviceRoles filter - returns only edge nodes
                self.test_data.get("get_fabric_devices_filtered_edge_nodes_case_1"),
                # get_network_device_list for 2 edge node devices
                self.test_data.get("get_device_list_device_1_case_1"),  # 205.1.2.67
                self.test_data.get("get_device_list_device_3_case_1"),  # 205.1.2.68
                # get_fabric_site_wired_settings
                self.test_data.get(
                    "get_embedded_wireless_controller_settings_empty_response"
                ),
                # Border handoff settings for 2 edge node devices
                # Device 1 (205.1.2.67 - edge node)
                self.test_data.get("get_layer2_handoffs_empty_response"),
                self.test_data.get("get_layer3_ip_transit_handoffs_empty_response"),
                self.test_data.get("get_layer3_sda_transit_handoffs_empty_response"),
                # Device 3 (205.1.2.68 - edge node)
                self.test_data.get("get_layer2_handoffs_empty_response"),
                self.test_data.get("get_layer3_ip_transit_handoffs_empty_response"),
                self.test_data.get("get_layer3_sda_transit_handoffs_empty_response"),
            ]

        elif "test_filter_fabric_name_multi_roles_case_5" in self._testMethodName:
            # Test Case 5: Filter by fabric_name + device_roles (BORDER_NODE, CONTROL_PLANE_NODE)
            # API filters by deviceRoles and returns only 1 device with both roles
            # API call sequence from dnac.log:
            # 1. get_sites, get_fabric_sites, get_transit_networks (initialization)
            # 2. get_fabric_devices with deviceRoles=['BORDER_NODE','CONTROL_PLANE_NODE'] - returns 1 device
            # 3. get_network_device_list for device (1 call)
            # 4. get_fabric_site_wired_settings (1 call)
            # 5. Border handoff APIs for device (1 device x 3 types = 3 calls)

            self.run_dnac_exec.side_effect = [
                # Initialization phase
                self.test_data.get("get_sites_case_1"),
                self.test_data.get("get_fabric_sites_case_1"),
                self.test_data.get("get_transit_networks_case_1"),
                # get_fabric_devices with deviceRoles filter - returns border/CP node
                self.test_data.get("get_fabric_devices_filtered_border_cp_case_1"),
                # get_network_device_list for 1 border/CP device
                self.test_data.get("get_device_list_device_2_case_1"),  # 205.1.1.10
                # get_fabric_site_wired_settings
                self.test_data.get(
                    "get_embedded_wireless_controller_settings_empty_response"
                ),
                # Border handoff settings for 1 border/CP device (has IP transit handoffs)
                self.test_data.get("get_layer2_handoffs_empty_response"),
                self.test_data.get("get_layer3_ip_transit_handoffs_device_2_case_1"),
                self.test_data.get("get_layer3_sda_transit_handoffs_empty_response"),
            ]

        elif "test_filter_all_filters_case_6" in self._testMethodName:
            # Test Case 6: Filter by fabric_name + device_ip + device_roles
            # This applies all filters together, resulting in 1 device
            # When device_ip is specified, module first queries device_list to get network_device_id

            self.run_dnac_exec.side_effect = [
                # Initialization phase
                self.test_data.get("get_sites_case_1"),
                self.test_data.get("get_fabric_sites_case_1"),
                self.test_data.get("get_transit_networks_case_1"),
                # get_device_list to resolve device_ip to network_device_id (EXTRA call for device_ip filter)
                self.test_data.get("get_device_list_device_2_case_1"),
                # get_fabric_devices with fabric_id + networkDeviceId
                self.test_data.get("get_fabric_devices_filtered_border_cp_case_1"),
                # get_fabric_site_wired_settings
                self.test_data.get(
                    "get_embedded_wireless_controller_settings_empty_response"
                ),
                # Border handoff settings for 1 filtered device
                self.test_data.get("get_layer2_handoffs_empty_response"),
                self.test_data.get("get_layer3_ip_transit_handoffs_device_2_case_1"),
                self.test_data.get("get_layer3_sda_transit_handoffs_empty_response"),
            ]

        elif "test_filter_fabric_name_cp_role_case_7" in self._testMethodName:
            # Test Case 7: Filter by fabric_name (Hyderabad) + device_roles (CONTROL_PLANE_NODE)
            # API filters by deviceRoles and returns only 1 CP node device
            # API call sequence from dnac.log:
            # 1. get_sites, get_fabric_sites, get_transit_networks (initialization)
            # 2. get_fabric_devices with deviceRoles=['CONTROL_PLANE_NODE'] - returns 1 device
            # 3. get_network_device_list for device (1 call)
            # 4. get_fabric_site_wired_settings (1 call)
            # 5. Border handoff APIs for device (1 device x 3 types = 3 calls)

            self.run_dnac_exec.side_effect = [
                # Initialization phase
                self.test_data.get("get_sites_case_1"),
                self.test_data.get("get_fabric_sites_case_1"),
                self.test_data.get("get_transit_networks_case_1"),
                # get_fabric_devices for Hyderabad with CP role filter - returns 1 CP node
                self.test_data.get(
                    "get_fabric_devices_filtered_cp_node_fabric_3_case_1"
                ),
                # get_network_device_list for 1 CP device
                self.test_data.get("get_device_list_device_5_case_1"),  # 172.27.248.222
                # get_fabric_site_wired_settings
                self.test_data.get(
                    "get_embedded_wireless_controller_settings_empty_response"
                ),
                # Border handoff settings for 1 CP node device
                self.test_data.get("get_layer2_handoffs_empty_response"),
                self.test_data.get("get_layer3_ip_transit_handoffs_empty_response"),
                self.test_data.get("get_layer3_sda_transit_handoffs_empty_response"),
            ]

        elif "test_filter_fabric_name_border_role_case_8" in self._testMethodName:
            # Test Case 8: Filter by fabric_name + device_roles (BORDER_NODE)
            # API filters by deviceRoles and returns only 1 border node device
            # API call sequence from dnac.log:
            # 1. get_sites, get_fabric_sites, get_transit_networks (initialization)
            # 2. get_fabric_devices with deviceRoles=['BORDER_NODE'] - returns 1 device
            # 3. get_network_device_list for device (1 call)
            # 4. get_fabric_site_wired_settings (1 call)
            # 5. Border handoff APIs for device (1 device x 3 types = 3 calls)

            self.run_dnac_exec.side_effect = [
                # Initialization phase
                self.test_data.get("get_sites_case_1"),
                self.test_data.get("get_fabric_sites_case_1"),
                self.test_data.get("get_transit_networks_case_1"),
                # get_fabric_devices with BORDER_NODE filter - returns border/CP device
                self.test_data.get("get_fabric_devices_filtered_border_cp_case_1"),
                # get_network_device_list for 1 border device
                self.test_data.get("get_device_list_device_2_case_1"),  # 205.1.1.10
                # get_fabric_site_wired_settings
                self.test_data.get(
                    "get_embedded_wireless_controller_settings_empty_response"
                ),
                # Border handoff settings for 1 border device (has IP transit handoffs)
                self.test_data.get("get_layer2_handoffs_empty_response"),
                self.test_data.get("get_layer3_ip_transit_handoffs_device_2_case_1"),
                self.test_data.get("get_layer3_sda_transit_handoffs_empty_response"),
            ]

        elif "test_filter_with_components_list_case_9" in self._testMethodName:
            # Test Case 9: Filter with explicit components_list + fabric_name (Hyderabad)
            # This tests the components_list parameter

            self.run_dnac_exec.side_effect = [
                # Initialization phase
                self.test_data.get("get_sites_case_1"),
                self.test_data.get("get_fabric_sites_case_1"),
                self.test_data.get("get_transit_networks_case_1"),
                # get_fabric_devices for Hyderabad fabric (2 devices)
                self.test_data.get("get_fabric_devices_fabric_3_case_1"),
                # get_network_device_list for devices in Hyderabad
                self.test_data.get("get_device_list_device_4_case_1"),
                self.test_data.get("get_device_list_device_5_case_1"),
                # get_fabric_site_wired_settings
                self.test_data.get(
                    "get_embedded_wireless_controller_settings_empty_response"
                ),
                # Border handoff settings for 2 devices
                # Device 4
                self.test_data.get("get_layer2_handoffs_empty_response"),
                self.test_data.get("get_layer3_ip_transit_handoffs_empty_response"),
                self.test_data.get("get_layer3_sda_transit_handoffs_empty_response"),
                # Device 5
                self.test_data.get("get_layer2_handoffs_empty_response"),
                self.test_data.get("get_layer3_ip_transit_handoffs_empty_response"),
                self.test_data.get("get_layer3_sda_transit_handoffs_empty_response"),
            ]

    def test_generate_all_configurations_case_1(self):
        """
        Test Case 1: Generate all configurations (fabric devices) automatically.
        This tests the generate_all_configurations flag which should retrieve
        all fabric devices from all fabric sites in Cisco Catalyst Center.

        Based on real API logs, this test:
        - Retrieves all fabric sites
        - Retrieves all fabric devices from each fabric site
        - Retrieves device IPs for each device
        - Retrieves border handoff settings (layer2, layer3 IP transit, layer3 SDA transit)
        - Generates YAML configuration file with all discovered fabric devices
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
            "YAML configuration file generated successfully for module 'sda_fabric_devices_workflow_manager'",
            str(result.get("msg")),
        )

    def test_filter_fabric_name_only_case_2(self):
        """
        Test Case 2: Filter by fabric_name only.
        This tests filtering devices by fabric site name only (Global/Site_India/Karnataka/Bangalore).
        Expected: Returns 3 fabric devices from the specified fabric site.

        API flow:
        - Initialization: get_sites, get_fabric_sites, get_transit_networks
        - get_fabric_devices for the specific fabric
        - get_network_device_list for each device
        - get_fabric_site_wired_settings for embedded wireless controller
        - Border handoff APIs for each device
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
                config=self.playbook_config_filter_fabric_name_only_case_2,
            )
        )

        result = self.execute_module(changed=True, failed=False)
        self.assertIn(
            "YAML configuration file generated successfully for module 'sda_fabric_devices_workflow_manager'",
            str(result.get("msg")),
        )

    def test_filter_fabric_name_device_ip_case_3(self):
        """
        Test Case 3: Filter by fabric_name + device_ip.
        This tests filtering to a single device by IP address (205.1.1.10).
        Expected: Returns 1 fabric device (the border/control plane node).

        API flow:
        - Initialization: get_sites, get_fabric_sites, get_transit_networks
        - get_fabric_devices (returns all, module filters by IP)
        - get_network_device_list for each device to match IP
        - get_fabric_site_wired_settings
        - Border handoff APIs for the filtered device
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
                config=self.playbook_config_filter_fabric_name_device_ip_case_3,
            )
        )

        result = self.execute_module(changed=True, failed=False)
        self.assertIn(
            "YAML configuration file generated successfully for module 'sda_fabric_devices_workflow_manager'",
            str(result.get("msg")),
        )

    def test_filter_fabric_name_edge_role_case_4(self):
        """
        Test Case 4: Filter by fabric_name + device_roles (EDGE_NODE).
        This tests filtering devices by a single role.
        Expected: Returns 2 fabric devices with EDGE_NODE role.

        API flow:
        - Initialization: get_sites, get_fabric_sites, get_transit_networks
        - get_fabric_devices (returns all, module filters by role)
        - get_network_device_list for each device
        - get_fabric_site_wired_settings
        - Border handoff APIs for filtered devices (2 edge nodes)
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
                config=self.playbook_config_filter_fabric_name_edge_role_case_4,
            )
        )

        result = self.execute_module(changed=True, failed=False)
        self.assertIn(
            "YAML configuration file generated successfully for module 'sda_fabric_devices_workflow_manager'",
            str(result.get("msg")),
        )

    def test_filter_fabric_name_multi_roles_case_5(self):
        """
        Test Case 5: Filter by fabric_name + device_roles (BORDER_NODE, CONTROL_PLANE_NODE).
        This tests filtering devices by multiple roles.
        Expected: Returns 1 fabric device that has both BORDER_NODE and CONTROL_PLANE_NODE roles.

        API flow:
        - Initialization: get_sites, get_fabric_sites, get_transit_networks
        - get_fabric_devices (returns all, module filters by roles)
        - get_network_device_list for each device
        - get_fabric_site_wired_settings
        - Border handoff APIs for the filtered device (has IP transit handoffs)
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
                config=self.playbook_config_filter_fabric_name_multi_roles_case_5,
            )
        )

        result = self.execute_module(changed=True, failed=False)
        self.assertIn(
            "YAML configuration file generated successfully for module 'sda_fabric_devices_workflow_manager'",
            str(result.get("msg")),
        )

    def test_filter_all_filters_case_6(self):
        """
        Test Case 6: Filter by fabric_name + device_ip + device_roles.
        This tests applying all available filters together.
        Expected: Returns 1 fabric device matching all criteria.

        API flow:
        - Initialization: get_sites, get_fabric_sites, get_transit_networks
        - get_fabric_devices (returns all)
        - get_network_device_list for each device
        - get_fabric_site_wired_settings
        - Border handoff APIs for the filtered device
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
                config=self.playbook_config_filter_all_filters_case_6,
            )
        )

        result = self.execute_module(changed=True, failed=False)
        self.assertIn(
            "YAML configuration file generated successfully for module 'sda_fabric_devices_workflow_manager'",
            str(result.get("msg")),
        )

    def test_filter_fabric_name_cp_role_case_7(self):
        """
        Test Case 7: Filter by fabric_name (Hyderabad/BLD_1) + device_roles (CONTROL_PLANE_NODE).
        This tests filtering on a different fabric site than the default.
        Expected: Returns 1 fabric device with CONTROL_PLANE_NODE role.

        API flow:
        - Initialization: get_sites, get_fabric_sites, get_transit_networks
        - get_fabric_devices for Hyderabad fabric
        - get_network_device_list for devices
        - get_fabric_site_wired_settings
        - Border handoff APIs for the filtered device
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
                config=self.playbook_config_filter_fabric_name_cp_role_case_7,
            )
        )

        result = self.execute_module(changed=True, failed=False)
        self.assertIn(
            "YAML configuration file generated successfully for module 'sda_fabric_devices_workflow_manager'",
            str(result.get("msg")),
        )

    def test_filter_fabric_name_border_role_case_8(self):
        """
        Test Case 8: Filter by fabric_name + device_roles (BORDER_NODE).
        This tests filtering devices by BORDER_NODE role only.
        Expected: Returns 1 fabric device with BORDER_NODE role (also has CONTROL_PLANE_NODE).

        API flow:
        - Initialization: get_sites, get_fabric_sites, get_transit_networks
        - get_fabric_devices (returns all)
        - get_network_device_list for each device
        - get_fabric_site_wired_settings
        - Border handoff APIs for the filtered device
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
                config=self.playbook_config_filter_fabric_name_border_role_case_8,
            )
        )

        result = self.execute_module(changed=True, failed=False)
        self.assertIn(
            "YAML configuration file generated successfully for module 'sda_fabric_devices_workflow_manager'",
            str(result.get("msg")),
        )

    def test_filter_with_components_list_case_9(self):
        """
        Test Case 9: Filter with explicit components_list + fabric_name.
        This tests the components_list parameter to explicitly specify which components to process.
        Expected: Returns 2 fabric devices from the Hyderabad fabric.

        API flow:
        - Initialization: get_sites, get_fabric_sites, get_transit_networks
        - get_fabric_devices for Hyderabad fabric (2 devices)
        - get_network_device_list for each device
        - get_fabric_site_wired_settings
        - Border handoff APIs for each device (2 devices x 3 handoff types)
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
                config=self.playbook_config_filter_with_components_list_case_9,
            )
        )

        result = self.execute_module(changed=True, failed=False)
        self.assertIn(
            "YAML configuration file generated successfully for module 'sda_fabric_devices_workflow_manager'",
            str(result.get("msg")),
        )
