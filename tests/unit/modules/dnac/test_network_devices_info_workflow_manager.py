# Copyright (c) 2025 Cisco and/or its affiliates.

# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at

# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# Make coding more python3-ish

from __future__ import absolute_import, division, print_function

__metaclass__ = type

from unittest.mock import patch

from ansible_collections.cisco.dnac.plugins.modules import network_devices_info_workflow_manager
from .dnac_module import TestDnacModule, set_module_args, loadPlaybookData


class TestDnacNetworkDevicesInfoWorkflowManager(TestDnacModule):

    module = network_devices_info_workflow_manager

    test_data = loadPlaybookData("network_devices_info_workflow_manager")

    playbook_connected_details = test_data.get("playbook_connected_details")
    playbook_device_summary_details = test_data.get("playbook_device_summary_details")
    playbook_supervisor_details = test_data.get("playbook_supervisor_details")
    playbook_module_count_details = test_data.get("playbook_module_count_details")
    playbook_polling_details = test_data.get("playbook_polling_details")
    playbook_poe_details = test_data.get("playbook_poe_details")
    playbook_interface_vlan_details = test_data.get("playbook_interface_vlan_details")
    playbook_link_mismatch_details = test_data.get("playbook_link_mismatch_details")
    playbook_linecard_details = test_data.get("playbook_linecard_details")
    playbook_device_details = test_data.get("playbook_device_details")
    playbook_stack_details = test_data.get("playbook_stack_details")
    playbook_config_details = test_data.get("playbook_config_details")
    playbook_interface_details = test_data.get("playbook_interface_details")
    playbook_range_interface_details = test_data.get("playbook_range_interface_details")
    playbook_negative_scenario1 = test_data.get("playbook_negative_scenario1")
    playbook_negative_scenario2 = test_data.get("playbook_negative_scenario2")
    playbook_negative_scenario3 = test_data.get("playbook_negative_scenario3")
    playbook_negative_scenario4 = test_data.get("playbook_negative_scenario4")
    playbook_negative_scenario5 = test_data.get("playbook_negative_scenario5")
    playbook_negative_scenario6 = test_data.get("playbook_negative_scenario6")
    playbook_negative_scenario7 = test_data.get("playbook_negative_scenario7")
    playbook_negative_scenario8 = test_data.get("playbook_negative_scenario8")
    playbook_negative_scenario9 = test_data.get("playbook_negative_scenario9")
    playbook_negative_scenario10 = test_data.get("playbook_negative_scenario10")
    playbook_negative_scenario11 = test_data.get("playbook_negative_scenario11")

    def setUp(self):
        super(TestDnacNetworkDevicesInfoWorkflowManager, self).setUp()

        self.mock_dnac_init = patch(
            "ansible_collections.cisco.dnac.plugins.module_utils.dnac.DNACSDK.__init__")
        self.run_dnac_init = self.mock_dnac_init.start()
        self.run_dnac_init.side_effect = [None]
        self.mock_dnac_exec = patch(
            "ansible_collections.cisco.dnac.plugins.module_utils.dnac.DNACSDK._exec"
        )
        self.run_dnac_exec = self.mock_dnac_exec.start()

    def tearDown(self):
        super(TestDnacNetworkDevicesInfoWorkflowManager, self).tearDown()
        self.mock_dnac_exec.stop()
        self.mock_dnac_init.stop()

    def load_fixtures(self, response=None, device=""):
        """
        Load fixtures for user.
        """

        if "playbook_connected_details" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("get_device_list"),
                self.test_data.get("get_device_list1"),
                self.test_data.get("get_interface_info_by_id"),
                self.test_data.get("get_device_list2"),
                self.test_data.get("get_connected_device_detail"),
                self.test_data.get("get_connected_device_detail1"),
                self.test_data.get("get_connected_device_detail2"),
                self.test_data.get("get_connected_device_detail3"),
                self.test_data.get("get_connected_device_detail4"),
                self.test_data.get("get_connected_device_detail5"),
                self.test_data.get("get_connected_device_detail6"), 
                self.test_data.get("get_connected_device_detail7"),
                self.test_data.get("get_connected_device_detail8"),
            ]
        elif "playbook_device_summary_details" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("get_device_list3"),
                self.test_data.get("get_device_list4"),
                self.test_data.get("get_device_list5"),
                self.test_data.get("get_device_summary"),
            ]
        elif "playbook_supervisor_details" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("get_device_list6"),
                self.test_data.get("get_device_list7"),
                self.test_data.get("get_device_list8"),
                self.test_data.get("get_supervisor_card_detail"),
            ]
        elif "playbook_module_count_details" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("get_device_list12"),
                self.test_data.get("get_device_list13"),
                self.test_data.get("get_device_list14"),
                self.test_data.get("get_module_count"),
            ]
        elif "playbook_polling_details" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("get_device_list15"),
                self.test_data.get("get_device_list16"),
                self.test_data.get("get_device_list17"),
                self.test_data.get("get_device_polling_interval_by_id"),
            ]
        elif "playbook_poe_details" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("get_device_list18"),
                self.test_data.get("get_device_list19"),
                self.test_data.get("get_device_list20"),
                self.test_data.get("poe_details"),
            ]
        elif "playbook_interface_vlan_details" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("get_device_list21"),
                self.test_data.get("get_device_list22"),
                self.test_data.get("get_device_list23"),
                self.test_data.get("get_device_interface_vlans"),
            ]
        elif "playbook_link_mismatch_details" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("get_sites"),
                self.test_data.get("get_sites1"),
                self.test_data.get("get_sites2"),
                self.test_data.get("get_device_list24"),
                self.test_data.get("get_device_list25"),
                self.test_data.get("inventory_insight_device_link_mismatch1"),
                self.test_data.get("inventory_insight_device_link_mismatch2"),
            ]
        elif "playbook_linecard_details" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("get_device_list9"),
                self.test_data.get("get_device_list10"),
                self.test_data.get("get_device_list11"),
                self.test_data.get("get_linecard_detail"),
            ]
        elif "playbook_device_details" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("get_device_list26"),
                self.test_data.get("get_device_list27"),
                self.test_data.get("get_device_list28"),
                self.test_data.get("get_device_list29"),
            ]
        elif "playbook_stack_details" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("get_device_list30"),
                self.test_data.get("get_device_list31"),
                self.test_data.get("get_device_list32"),
                self.test_data.get("get_stack_details_for_device"),
            ]
        elif "playbook_config_details" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("get_device_list33"),
                self.test_data.get("get_device_list34"),
                self.test_data.get("get_device_list35"),
                self.test_data.get("get_device_config_by_id"),
            ]
        elif "playbook_interface_details" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("get_device_list36"),
                self.test_data.get("get_device_list37"),
                self.test_data.get("get_device_list38"),
                self.test_data.get("get_interface_info_by_id1"),
            ]
        elif "playbook_range_interface_details" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("get_device_list39"),
                self.test_data.get("get_device_list40"),
                self.test_data.get("get_device_list41"),
                self.test_data.get("get_device_interfaces_by_specified_range"),
            ]
        elif "playbook_negative_scenario1" in self._testMethodName:
            self.run_dnac_exec.side_effect = []
        elif "playbook_negative_scenario2" in self._testMethodName:
            self.run_dnac_exec.side_effect = []
        elif "playbook_negative_scenario3" in self._testMethodName:
            self.run_dnac_exec.side_effect = []
        elif "playbook_negative_scenario4" in self._testMethodName:
            self.run_dnac_exec.side_effect = []
        elif "playbook_negative_scenario5" in self._testMethodName:
            self.run_dnac_exec.side_effect = [] 
        elif "playbook_negative_scenario6" in self._testMethodName:
            self.run_dnac_exec.side_effect = []
        elif "playbook_negative_scenario7" in self._testMethodName:
            self.run_dnac_exec.side_effect = []
        elif "playbook_negative_scenario8" in self._testMethodName:
            self.run_dnac_exec.side_effect = []
        elif "playbook_negative_scenario9" in self._testMethodName:
            self.run_dnac_exec.side_effect = []
        elif "playbook_negative_scenario10" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("get_device_list42"),
                self.test_data.get("get_device_list43"),
                self.test_data.get("get_device_list44"),
            ]
        elif "playbook_negative_scenario11" in self._testMethodName:
            self.run_dnac_exec.side_effect = []

    def test_network_devices_info_workflow_manager_playbook_connected_details(self):
        """
        Test the Network Devices Info Workflow Manager's device information retrieval process.

        This test verifies that the workflow correctly handles the retrieval of network device information,
        ensuring proper validation and expected behavior.
        """

        set_module_args(
            dict(
                dnac_host="1.1.1.1",
                dnac_username="dummy",
                dnac_password="dummy",
                dnac_log=True,
                state="queried",
                config_verify=True,
                dnac_version="2.3.7.9",
                config=self.playbook_connected_details
            )
        )
        result = self.execute_module(changed=False, failed=False)
        print(result)
        self.assertEqual(
            result.get("response"),
            [
                "The network devices found: ['204.192.4.2']",
                [
                    {
                        "connected_device_info": [
                            {
                                "connected_device_details": [
                                    {
                                        "capabilities": [
                                            "IGMP_CONDITIONAL_FILTERING",
                                            "ROUTER",
                                            "SWITCH"
                                        ],
                                        "neighborDevice": "TB1-DM-Fusion.cisco.com",
                                        "neighborPort": "TenGigabitEthernet1/0/4"
                                    }
                                ],
                                "device_ip": "204.192.4.2"
                            }
                        ]
                    }
                ]
            ]

        )
    def test_network_devices_info_workflow_manager_playbook_device_summary_details(self):
        """
        Test the Network Devices Info Workflow Manager's device information retrieval process.

        This test verifies that the workflow correctly handles the retrieval of network device information,
        ensuring proper validation and expected behavior.
        """

        set_module_args(
            dict(
                dnac_host="1.1.1.1",
                dnac_username="dummy",
                dnac_password="dummy",
                dnac_log=True,
                state="queried",
                config_verify=True,
                dnac_version="2.3.7.9",
                config=self.playbook_device_summary_details
            )
        )
        result = self.execute_module(changed=False, failed=False)
        print(result)
        self.assertEqual(
            result.get("msg"),
            [
            "The network devices found: ['204.192.4.2']",
            [
                {
                    "device_summary_info": [
                        {
                            "device_ip": "204.192.4.2",
                            "device_summary_details": [
                                {
                                    "id": "a2ee1e97-c242-4bfb-b593-81424c4932f2",
                                    "role": "ACCESS",
                                    "roleSource": "MANUAL"
                                }
                            ]
                        }
                    ]
                }
            ]
        ]
    )
    def test_network_devices_info_workflow_manager_playbook_supervisor_details(self):
        """
        Test the Network Devices Info Workflow Manager's device information retrieval process.

        This test verifies that the workflow correctly handles the retrieval of network device information,
        ensuring proper validation and expected behavior.
        """

        set_module_args(
            dict(
                dnac_host="1.1.1.1",
                dnac_username="dummy",
                dnac_password="dummy",
                dnac_log=True,
                state="queried",
                config_verify=True,
                dnac_version="2.3.7.9",
                config=self.playbook_supervisor_details
            )
        )
        result = self.execute_module(changed=False, failed=False)
        print(result)
        self.assertEqual(
            result.get("response"),
            [
            "The network devices found: ['204.192.4.2']",
            [
                {
                    "supervisor_card_info": [
                        {
                            "device_ip": "204.192.4.2",
                            "supervisor_card_details": "No supervisor card details found for 204.192.4.2"
                        }
                    ]
                }
            ]
        ]
    )
    def test_network_devices_info_workflow_manager_playbook_module_count_details(self):
        """
        Test the Network Devices Info Workflow Manager's device information retrieval process.

        This test verifies that the workflow correctly handles the retrieval of network device information,
        ensuring proper validation and expected behavior.
        """

        set_module_args(
            dict(
                dnac_host="1.1.1.1",
                dnac_username="dummy",
                dnac_password="dummy",
                dnac_log=True,
                state="queried",
                config_verify=True,
                dnac_version="2.3.7.9",
                config=self.playbook_module_count_details
            )
        )
        result = self.execute_module(changed=False, failed=False)
        print(result)
        self.assertEqual(
            result.get("response"),
            [
                "The network devices found: ['204.1.2.1']",
                [
                    {
                        "module_count_info": [
                            {
                                "device_ip": "204.1.2.1",
                                "module_count_details": [
                                    2
                                ]
                            }
                        ]
                    }
                ]
            ]
    )
    def test_network_devices_info_workflow_manager_playbook_polling_details(self):
        """
        Test the Network Devices Info Workflow Manager's device information retrieval process.

        This test verifies that the workflow correctly handles the retrieval of network device information,
        ensuring proper validation and expected behavior.
        """

        set_module_args(
            dict(
                dnac_host="1.1.1.1",
                dnac_username="dummy",
                dnac_password="dummy",
                dnac_log=True,
                state="queried",
                config_verify=True,
                dnac_version="2.3.7.9",
                config=self.playbook_polling_details
            )
        )
        result = self.execute_module(changed=False, failed=False)
        print(result)
        self.assertEqual(
            result.get("response"),
            [
                "The network devices found: ['204.1.2.1']",
                [
                    {
                        "device_polling_interval_info": [
                            {
                                "device_ip": "204.1.2.1",
                                "polling_interval_details": [
                                    5400
                                ]
                            }
                        ]
                    }
                ]
            ]
    )
    def test_network_devices_info_workflow_manager_playbook_poe_details(self):
        """
        Test the Network Devices Info Workflow Manager's device information retrieval process.

        This test verifies that the workflow correctly handles the retrieval of network device information,
        ensuring proper validation and expected behavior.
        """

        set_module_args(
            dict(
                dnac_host="1.1.1.1",
                dnac_username="dummy",
                dnac_password="dummy",
                dnac_log=True,
                state="queried",
                config_verify=True,
                dnac_version="2.3.7.9",
                config=self.playbook_poe_details
            )
        )
        result = self.execute_module(changed=False, failed=False)
        print(result)
        self.assertEqual(
            result.get("response"),
            [
                "The network devices found: ['204.1.2.2']",
                [
                    {
                        "poe_info": [
                            {
                                "device_ip": "204.1.2.2",
                                "poe_details": [
                                    {
                                        "powerAllocated": "857",
                                        "powerConsumed": "114",
                                        "powerRemaining": "743"
                                    }
                                ]
                            }
                        ]
                    }
                ]
            ]
    )
    def test_network_devices_info_workflow_manager_playbook_interface_vlan_details(self):
        """
        Test the Network Devices Info Workflow Manager's device information retrieval process.

        This test verifies that the workflow correctly handles the retrieval of network device information,
        ensuring proper validation and expected behavior.
        """

        set_module_args(
            dict(
                dnac_host="1.1.1.1",
                dnac_username="dummy",
                dnac_password="dummy",
                dnac_log=True,
                state="queried",
                config_verify=True,
                dnac_version="2.3.7.9",
                config=self.playbook_interface_vlan_details
            )
        )
        result = self.execute_module(changed=False, failed=False)
        print(result)
        self.assertEqual(
            result.get("response"),
            [
        "The network devices found: ['85.1.1.9']",
        [
        {
            'interface_vlan_info': [
            {
                'device_ip': '85.1.1.9',
                'interface_vlan_details': [
                [
                    {
                    'vlanType': 'SVI interface VLAN0921',
                    'vlanNumber': 921,
                    'interfaceName': 'Vlan921'
                    },
                    {
                    'vlanType': '',
                    'vlanNumber': 1,
                    'interfaceName': 'Vlan1'
                    },
                    {
                    'vlanType': '',
                    'vlanNumber': 20,
                    'interfaceName': 'Vlan20'
                    }
                ]
                ]
            }
            ]
        }
        ]
    ]
    )
    def test_network_devices_info_workflow_manager_playbook_link_mismatch_details(self):
        """
        Test the Network Devices Info Workflow Manager's device information retrieval process.

        This test verifies that the workflow correctly handles the retrieval of network device information,
        ensuring proper validation and expected behavior.
        """

        set_module_args(
            dict(
                dnac_host="1.1.1.1",
                dnac_username="dummy",
                dnac_password="dummy",
                dnac_log=True,
                state="queried",
                config_verify=True,
                dnac_version="2.3.7.9",
                config=self.playbook_link_mismatch_details
            )
        )
        result = self.execute_module(changed=False, failed=False)
        print(result)
        self.assertEqual(
            result.get("response"),
            [
                "The network devices found: []",
                [
                    {
                        "device_link_mismatch_info": [
                            {
                                "device_ip": "204.1.2.1",
                                "speed-duplex": [
                                    {
                                        "device_ip": "204.1.2.1",
                                        "link_mismatch_details": "No link mismatches found"
                                    }
                                ],
                                "vlan": [
                                    {
                                        "device_ip": "204.1.2.1",
                                        "link_mismatch_details": "No link mismatches found"
                                    }
                                ]
                            }
                        ]
                    }
                ]
            ]
    )
    def test_network_devices_info_workflow_manager_playbook_linecard_details(self):
        """
        Test the Network Devices Info Workflow Manager's device information retrieval process.

        This test verifies that the workflow correctly handles the retrieval of network device information,
        ensuring proper validation and expected behavior.
        """

        set_module_args(
            dict(
                dnac_host="1.1.1.1",
                dnac_username="dummy",
                dnac_password="dummy",
                dnac_log=True,
                state="queried",
                config_verify=True,
                dnac_version="2.3.7.9",
                config=self.playbook_linecard_details
            )
        )
        result = self.execute_module(changed=False, failed=False)
        print(result)
        self.assertEqual(
            result.get("response"),
                ["The network devices found: ['85.1.1.9']", None]
        )
    def test_network_devices_info_workflow_manager_playbook_device_details(self):
        """
        Test the Network Devices Info Workflow Manager's device information retrieval process.

        This test verifies that the workflow correctly handles the retrieval of network device information,
        ensuring proper validation and expected behavior.
        """

        set_module_args(
            dict(
                dnac_host="1.1.1.1",
                dnac_username="dummy",
                dnac_password="dummy",
                dnac_log=True,
                state="queried",
                config_verify=True,
                dnac_version="2.3.7.9",
                config=self.playbook_device_details
            )
        )
        result = self.execute_module(changed=False, failed=False)
        print(result)
        self.assertEqual(
            result.get("response"),
            [
    "The network devices found: ['91.1.1.2']",
    [
      {
        'device_info': [
          {
            'device_ip': '91.1.1.2',
            'device_details': [
              [
                {
                  'errorDescription': None,
                  'lastDeviceResyncStartTime': '2025-07-09 05:33:20',
                  'lineCardCount': '0',
                  'lineCardId': '',
                  'managedAtleastOnce': False,
                  'memorySize': 'NA',
                  'tagCount': '0',
                  'tunnelUdpPort': None,
                  'uptimeSeconds': 3614676,
                  'vendor': 'Cisco',
                  'waasDeviceMode': None,
                  'lastUpdateTime': 1752039268180,
                  'macAddress': 'cc:70:ed:e1:c3:00',
                  'softwareType': 'IOS-XE',
                  'softwareVersion': '17.15.2',
                  'deviceSupportLevel': 'Supported',
                  'serialNumber': 'FCW2243F199',
                  'collectionInterval': 'Global Default',
                  'dnsResolvedManagementAddress': '91.1.1.2',
                  'lastManagedResyncReasons': 'Periodic',
                  'managementState': 'Managed',
                  'pendingSyncRequestsCount': '0',
                  'reasonsForDeviceResync': 'Periodic',
                  'reasonsForPendingSyncRequests': '',
                  'inventoryStatusDetail': '<status><general code=SUCCESS/></status>',
                  'syncRequestedByApp': '',
                  'upTime': '41 days, 19:42:15.88',
                  'roleSource': 'MANUAL',
                  'bootDateTime': '2025-05-28 09:52:28',
                  'apManagerInterfaceIp': '',
                  'collectionStatus': 'Managed',
                  'family': 'Switches and Hubs',
                  'hostname': 'SJ-Border2-9500.cisco.com',
                  'locationName': None,
                  'managementIpAddress': '91.1.1.2',
                  'platformId': 'C9500-16X',
                  'reachabilityFailureReason': '',
                  'reachabilityStatus': 'Reachable',
                  'series': 'Cisco Catalyst 9500 Series Switches',
                  'snmpContact': '',
                  'snmpLocation': '',
                  'interfaceCount': '0',
                  'lastUpdated': '2025-07-09 05:34:28',
                  'associatedWlcIp': '',
                  'apEthernetMacAddress': None,
                  'errorCode': None,
                  'description': 'Cisco IOS Software [IOSXE], Catalyst L3 Switch Software (CAT9K_IOSXE), Version 17.15.2, RELEASE SOFTWARE (fc3) Technical Support: http://www.cisco.com/techsupport Copyright (c) 1986-2024 by Cisco Systems, Inc. Compiled Wed 27-Nov-24 23:19 by mcpre netconf enabled',
                  'type': 'Cisco Catalyst 9500 Switch',
                  'location': None,
                  'role': 'BORDER ROUTER',
                  'instanceUuid': '36680b59-39b2-446b-8ceb-5a1e157b5799',
                  'instanceTenantId': '67c18e2a74fcf4001370a56e',
                  'id': '36680b59-39b2-446b-8ceb-5a1e157b5799'
                }
              ]
            ]
          }
        ]
      }
    ]
  ]
)
    def test_network_devices_info_workflow_manager_playbook_stack_details(self):
        """
        Test the Network Devices Info Workflow Manager's stack information retrieval process.

        This test verifies that the workflow correctly handles the retrieval of network stack information,
        ensuring proper validation and expected behavior.
        """

        set_module_args(
            dict(
                dnac_host="1.1.1.1",
                dnac_username="dummy",
                dnac_password="dummy",
                dnac_log=True,
                state="queried",
                config_verify=True,
                dnac_version="2.3.7.9",
                config=self.playbook_stack_details
            )
        )
        result = self.execute_module(changed=False, failed=False)
        print(result)
        self.assertEqual(
            result.get("response"),
    [
  "The network devices found: ['204.1.1.37']",
  [
    {
      'device_stack_info': [
        {
          'device_ip': '204.1.1.37',
          'stack_details': [
            {
              'deviceId': '99c8e9bf-8146-4dae-9449-8ce2d6405191',
              'stackSwitchInfo': [
                {
                  'hwPriority': 0,
                  'macAddress': '0c:75:bd:8f:a3:80',
                  'numNextReload': 1,
                  'role': 'ACTIVE',
                  'softwareImage': '17.16.01',
                  'stackMemberNumber': 1,
                  'state': 'READY',
                  'switchPriority': 1,
                  'entPhysicalIndex': '1000',
                  'serialNumber': 'FJC2336T0SU',
                  'platformId': 'C9300-24UX'
                }
              ],
              'stackPortInfo': [
                {
                  'isSynchOk': 'No',
                  'name': 'StackSub-St1-2',
                  'switchPort': '1/2',
                  'neighborPort': 'null/null',
                  'nrLinkOkChanges': 0,
                  'stackCableLengthInfo': 'NO_CABLE',
                  'stackPortOperStatusInfo': 'DOWN',
                  'linkActive': False,
                  'linkOk': False
                },
                {
                  'isSynchOk': 'No',
                  'name': 'StackSub-St1-1',
                  'switchPort': '1/1',
                  'neighborPort': 'null/null',
                  'nrLinkOkChanges': 0,
                  'stackCableLengthInfo': 'NO_CABLE',
                  'stackPortOperStatusInfo': 'DOWN',
                  'linkActive': False,
                  'linkOk': False
                }
              ],
              'svlSwitchInfo': None
            }
          ]
        }
      ]
    }
  ]
]
)
    def test_network_devices_info_workflow_manager_playbook_config_details(self):
        """
        Test the Network Devices Info Workflow Manager's config information retrieval process.

        This test verifies that the workflow correctly handles the retrieval of network config information,
        ensuring proper validation and expected behavior.
        """

        set_module_args(
            dict(
                dnac_host="1.1.1.1",
                dnac_username="dummy",
                dnac_password="dummy",
                dnac_log=True,
                state="queried",
                config_verify=True,
                dnac_version="2.3.7.9",
                config=self.playbook_config_details
            )
        )
        result = self.execute_module(changed=False, failed=False)
        print(result)
        self.assertEqual(
            result.get("response"),
            [
    "The network devices found: ['204.1.1.37']",
    [
      {
        'device_config_info': [
          {
            'device_ip': '204.1.1.37',
            'device_config_details': [
              '\nBuilding configuration...\n\nCurrent configuration : 56538 bytes\n!\n! Last configuration change at 07:35:53 UTC Mon Jun 2 2025\n!\nversion 17.16\nservice timestamps debug datetime msec\nservice timestamps log datetime msec\nservice password-encryption\nservice sequence-numbers\nplatform wdavc serviceability \n!\nhostname TB17-Transit\n!\n!\nvrf definition Mgmt-vrf\n !\n address-family ipv4\n exit-address-family\n !\n address-family ipv6\n exit-address-family\n!\nno logging console\naaa new-model\n!\n!\naaa group server radius dnac-client-radius-group\n server name dnac-radius_85.1.1.3\n ip radius source-interface Loopback0\n!\naaa group server radius dnac-network-radius-group\n server name dnac-radius_85.1.1.3\n ip radius source-interface Loopback0\n!\naaa authentication login default local\naaa authentication login dnac-cts-list group dnac-client-radius-group local\naaa authentication login VTY_authen group dnac-network-radius-group local\naaa authentication dot1x default group dnac-client-radius-group\naaa authorization exec default local \naaa authorization exec VTY_author group dnac-network-radius-group local if-authenticated \naaa authorization network default group dnac-client-radius-group \naaa authorization network dnac-cts-list group dnac-client-radius-group \naaa accounting update newinfo periodic 2880\naaa accounting identity default start-stop group dnac-client-radius-group\naaa accounting exec default start-stop group dnac-network-radius-group\n!\n!\naaa server radius dynamic-author\n client 85.1.1.3 server-key 7 xxxxxxxx\n client 172.23.9.235 server-key 7 xxxxxxxx\n!\naaa session-id common\nboot system switch all flash:packages.conf\nswitch 1 provision c9300-24ux\nsoftware auto-upgrade enable\n!\n!\n!\n!\n!\nip routing\n!\n!\n!\n!\n!\nip multicast-routing \nip name-server 172.23.9.220 2006:1:1::1\nip domain lookup source-interface Loopback0\nip domain name cisco.com\n!\n!\n!\n login xxxxxx\nipv6 nd cache expire refresh\nipv6 unicast-routing\nvtp mode transparent\n!\n!\n!\n!\n!\n!\n!\nmpls label mode all-vrfs protocol all-afs per-vrf\navc sd-service\n segment AppRecognition\n controller\n  address 85.1.1.2 \n  destination-ports sensor-exporter 21730\n  dscp 16\n  source-interface Loopback0\n  transport application-updates https url-prefix sdavc\n !\n!\n!\n!\nflow record dnacrecord\n match application name\n match connection client ipv4 address\n match connection server ipv4 address\n match connection server transport port\n match flow observation point\n match ipv4 protocol\n match ipv4 version\n collect connection client counter bytes network long\n collect connection client counter packets long\n collect connection initiator\n collect connection new-connections\n collect connection server counter bytes network long\n collect connection server counter packets long\n collect datalink mac source address input\n collect flow direction\n collect timestamp absolute first\n collect timestamp absolute last\n!\n!\nflow record dnacrecord_v6\n match application name\n match connection client ipv6 address\n match connection server ipv6 address\n match connection server transport port\n match flow observation point\n match ipv6 protocol\n match ipv6 version\n collect connection client counter bytes network long\n collect connection client counter packets long\n collect connection initiator\n collect connection new-connections\n collect connection server counter bytes network long\n collect connection server counter packets long\n collect datalink mac source address input\n collect flow direction\n collect timestamp absolute first\n collect timestamp absolute last\n!\n!\nflow record dnacrecord_dns\n match application dns qtype\n match application dns rcode\n match connection client ipv4 address\n match connection server ipv4 address\n match flow observation point\n match ipv4 protocol\n match ipv4 version\n collect application dns delay response sum\n collect application dns requests\n collect connection client counter bytes network long\n collect connection client counter packets long\n collect connection server counter bytes network long\n collect connection server counter packets long\n collect datalink mac source address input\n collect timestamp absolute first\n collect timestamp absolute last\n!\n!\nflow record dnacrecord_dns_v6\n match application dns qtype\n match application dns rcode\n match connection client ipv6 address\n match connection server ipv6 address\n match flow observation point\n match ipv6 protocol\n match ipv6 version\n collect application dns delay response sum\n collect application dns requests\n collect connection client counter bytes network long\n collect connection client counter packets long\n collect connection server counter bytes network long\n collect connection server counter packets long\n collect datalink mac source address input\n collect timestamp absolute first\n collect timestamp absolute last\n!\n!\nflow exporter dnacexporter\n destination 85.1.1.2\n source Loopback0\n transport udp 6007\n export-protocol ipfix\n option interface-table timeout 300\n option vrf-table timeout 300\n option sampler-table\n option application-table timeout 300\n option application-attributes timeout 300\n!\n!\nflow monitor dnacmonitor\n exporter dnacexporter\n cache timeout inactive 10\n cache timeout active 60\n record dnacrecord\n!\n!\nflow monitor dnacmonitor_v6\n exporter dnacexporter\n cache timeout inactive 10\n cache timeout active 60\n record dnacrecord_v6\n!\n!\nflow monitor dnacmonitor_dns\n exporter dnacexporter\n cache timeout inactive 10\n cache timeout active 60\n record dnacrecord_dns\n!\n!\nflow monitor dnacmonitor_dns_v6\n exporter dnacexporter\n cache timeout inactive 10\n cache timeout active 60\n record dnacrecord_dns_v6\n!\naccess-session mac-move deny\n!\ncrypto pki xxxxxxx\n enrollment selfsigned\n subject-name xxxxxxxx\n revocation-check none\n rsakeypair TP-self-signed- xxxxxxxx\n hash sha512\n!\ncrypto pki xxxxxxx\n enrollment pkcs12\n revocation-check crl\n hash sha512\n!\ncrypto pki xxxxxxx\n enrollment mode ra\n enrollment terminal\n usage ssl-client\n revocation-check crl none\n source interface Loopback0\n hash sha512\n!\ncrypto pki xxxxxxx\n enrollment url http://85.1.1.2:80/ejbca/publicweb/apply/scep/sdnscep\n fqdn TB17-Transit\n subject-name xxxxxxxx\n revocation-check crl\n source interface Loopback0\n rsakeypair xxxxxxxx\n auto-enroll 80 regenerate\n hash sha512\n!\n!\ncrypto pki certificate chain xxxxxxx\n certificate self-signed xxxxxxxx\n  xxxx  xxxxx  xxxx  xxxx  xxxx\n  xxxx  xxxxx  xxxx  xxxx  xxxx\n  xxxx  xxxxx  xxxx  xxxx  xxxx\n  xxxx  xxxxx  xxxx  xxxx  xxxx\n  xxxx  xxxxx  xxxx  xxxx  xxxx\n  xxxx  xxxxx  xxxx  xxxx  xxxx\n  xxxx  xxxxx  xxxx  xxxx  xxxx\n  xxxx  xxxxx  xxxx  xxxx  xxxx\n  xxxx  xxxxx  xxxx  xxxx  xxxx\n  xxxx  xxxxx  xxxx  xxxx  xxxx\n  xxxx  xxxxx  xxxx  xxxx  xxxx\n  xxxx  xxxxx  xxxx  xxxx  xxxx\n  xxxx  xxxxx  xxxx  xxxx  xxxx\n  xxxx  xxxxx  xxxx  xxxx  xxxx\n  xxxx  xxxxx  xxxx  xxxx  xxxx\n  xxxx  xxxxx  xxxx  xxxx  xxxx\n  xxxx  xxxxx  xxxx  xxxx  xxxx\n  xxxx  xxxxx  xxxx  xxxx  xxxx\n  xxxx  xxxxx  xxxx  xxxx  xxxx\n  xxxx  xxxxx  xxxx  xxxx  xxxx\n  xxxx  xxxxx  xxxx  xxxx  xxxx\n  xxxx  xxxxx  xxxx  xxxx  xxxx\n  xxxx  xxxxx  xxxx  xxxx  xxxx\n  xxxx  xxxxx  xxxx  xxxx  xxxx\n  xxxx  xxxxx  xxxx  xxxx  xxxx\n  xxxx  xxxxx  xxxx  xxxx  xxxx\nquit\ncrypto pki certificate chain xxxxxxx\n certificate ca xxxxxxxx\n  xxxx  xxxxx  xxxx  xxxx  xxxx\n  xxxx  xxxxx  xxxx  xxxx  xxxx\n  xxxx  xxxxx  xxxx  xxxx  xxxx\n  xxxx  xxxxx  xxxx  xxxx  xxxx\n  xxxx  xxxxx  xxxx  xxxx  xxxx\n  xxxx  xxxxx  xxxx  xxxx  xxxx\n  xxxx  xxxxx  xxxx  xxxx  xxxx\n  xxxx  xxxxx  xxxx  xxxx  xxxx\n  xxxx  xxxxx  xxxx  xxxx  xxxx\n  xxxx  xxxxx  xxxx  xxxx  xxxx\n  xxxx  xxxxx  xxxx  xxxx  xxxx\n  xxxx  xxxxx  xxxx  xxxx  xxxx\n  xxxx  xxxxx  xxxx  xxxx  xxxx\n  xxxx  xxxxx  xxxx  xxxx  xxxx\n  xxxx  xxxxx  xxxx  xxxx  xxxx\n  xxxx  xxxxx  xxxx  xxxx  xxxx\n  xxxx  xxxxx  xxxx  xxxx  xxxx\n  xxxx  xxxxx  xxxx  xxxx  xxxx\n  xxxx  xxxxx  xxxx  xxxx  xxxx\n  xxxx  xxxxx  xxxx  xxxx  xxxx\n  xxxx  xxxxx  xxxx  xxxx  xxxx\n  xxxx  xxxxx  xxxx  xxxx  xxxx\n  xxxx  xxxxx  xxxx  xxxx  xxxx\n  xxxx  xxxxx  xxxx  xxxx  xxxx\n  xxxx  xxxxx  xxxx  xxxx  xxxx\n  xxxx  xxxxx  xxxx  xxxx  xxxx\nquit\ncrypto pki certificate chain xxxxxxx\n certificate ca xxxxxxxx\n  xxxx  xxxxx  xxxx  xxxx  xxxx\n  xxxx  xxxxx  xxxx  xxxx  xxxx\n  xxxx  xxxxx  xxxx  xxxx  xxxx\n  xxxx  xxxxx  xxxx  xxxx  xxxx\n  xxxx  xxxxx  xxxx  xxxx  xxxx\n  xxxx  xxxxx  xxxx  xxxx  xxxx\n  xxxx  xxxxx  xxxx  xxxx  xxxx\n  xxxx  xxxxx  xxxx  xxxx  xxxx\n  xxxx  xxxxx  xxxx  xxxx  xxxx\n  xxxx  xxxxx  xxxx  xxxx  xxxx\n  xxxx  xxxxx  xxxx  xxxx  xxxx\n  xxxx  xxxxx  xxxx  xxxx  xxxx\n  xxxx  xxxxx  xxxx  xxxx  xxxx\n  xxxx  xxxxx  xxxx  xxxx  xxxx\n  xxxx  xxxxx  xxxx  xxxx  xxxx\n  xxxx  xxxxx  xxxx  xxxx  xxxx\n  xxxx  xxxxx  xxxx  xxxx  xxxx\n  xxxx  xxxxx  xxxx  xxxx  xxxx\n  xxxx  xxxxx  xxxx  xxxx  xxxx\n  xxxx  xxxxx  xxxx  xxxx  xxxx\n  xxxx  xxxxx  xxxx  xxxx  xxxx\n  xxxx  xxxxx  xxxx  xxxx  xxxx\n  xxxx  xxxxx  xxxx  xxxx  xxxx\n  xxxx  xxxxx  xxxx  xxxx  xxxx\n  xxxx  xxxxx  xxxx  xxxx  xxxx\n  xxxx  xxxxx  xxxx  xxxx  xxxx\n  xxxx  xxxxx  xxxx  xxxx  xxxx\n  xxxx  xxxxx  xxxx  xxxx  xxxx\n  xxxx  xxxxx  xxxx  xxxx  xxxx\n  xxxx  xxxxx  xxxx  xxxx  xxxx\nquit\ncrypto pki certificate chain xxxxxxx\n  xxxx  xxxxx  xxxx  xxxx  xxxx\n  xxxx  xxxxx  xxxx  xxxx  xxxx\n  xxxx  xxxxx  xxxx  xxxx  xxxx\n  xxxx  xxxxx  xxxx  xxxx  xxxx\n  xxxx  xxxxx  xxxx  xxxx  xxxx\n  xxxx  xxxxx  xxxx  xxxx  xxxx\n  xxxx  xxxxx  xxxx  xxxx  xxxx\n  xxxx  xxxxx  xxxx  xxxx  xxxx\n  xxxx  xxxxx  xxxx  xxxx  xxxx\n  xxxx  xxxxx  xxxx  xxxx  xxxx\n  xxxx  xxxxx  xxxx  xxxx  xxxx\n  xxxx  xxxxx  xxxx  xxxx  xxxx\n  xxxx  xxxxx  xxxx  xxxx  xxxx\n  xxxx  xxxxx  xxxx  xxxx  xxxx\n  xxxx  xxxxx  xxxx  xxxx  xxxx\n  xxxx  xxxxx  xxxx  xxxx  xxxx\n  xxxx  xxxxx  xxxx  xxxx  xxxx\n  xxxx  xxxxx  xxxx  xxxx  xxxx\n  xxxx  xxxxx  xxxx  xxxx  xxxx\n  xxxx  xxxxx  xxxx  xxxx  xxxx\n  xxxx  xxxxx  xxxx  xxxx  xxxx\n  xxxx  xxxxx  xxxx  xxxx  xxxx\n  xxxx  xxxxx  xxxx  xxxx  xxxx\n  xxxx  xxxxx  xxxx  xxxx  xxxx\n  xxxx  xxxxx  xxxx  xxxx  xxxx\n  xxxx  xxxxx  xxxx  xxxx  xxxx\n  xxxx  xxxxx  xxxx  xxxx  xxxx\n  xxxx  xxxxx  xxxx  xxxx  xxxx\n  xxxx  xxxxx  xxxx  xxxx  xxxx\n  xxxx  xxxxx  xxxx  xxxx  xxxx\nquit\n certificate ca xxxxxxxx\n  xxxx  xxxxx  xxxx  xxxx  xxxx\n  xxxx  xxxxx  xxxx  xxxx  xxxx\n  xxxx  xxxxx  xxxx  xxxx  xxxx\n  xxxx  xxxxx  xxxx  xxxx  xxxx\n  xxxx  xxxxx  xxxx  xxxx  xxxx\n  xxxx  xxxxx  xxxx  xxxx  xxxx\n  xxxx  xxxxx  xxxx  xxxx  xxxx\n  xxxx  xxxxx  xxxx  xxxx  xxxx\n  xxxx  xxxxx  xxxx  xxxx  xxxx\n  xxxx  xxxxx  xxxx  xxxx  xxxx\n  xxxx  xxxxx  xxxx  xxxx  xxxx\n  xxxx  xxxxx  xxxx  xxxx  xxxx\n  xxxx  xxxxx  xxxx  xxxx  xxxx\n  xxxx  xxxxx  xxxx  xxxx  xxxx\n  xxxx  xxxxx  xxxx  xxxx  xxxx\n  xxxx  xxxxx  xxxx  xxxx  xxxx\n  xxxx  xxxxx  xxxx  xxxx  xxxx\n  xxxx  xxxxx  xxxx  xxxx  xxxx\n  xxxx  xxxxx  xxxx  xxxx  xxxx\n  xxxx  xxxxx  xxxx  xxxx  xxxx\n  xxxx  xxxxx  xxxx  xxxx  xxxx\n  xxxx  xxxxx  xxxx  xxxx  xxxx\n  xxxx  xxxxx  xxxx  xxxx  xxxx\n  xxxx  xxxxx  xxxx  xxxx  xxxx\n  xxxx  xxxxx  xxxx  xxxx  xxxx\n  xxxx  xxxxx  xxxx  xxxx  xxxx\nquit\n!\ncts authorization list dnac-cts-list\n!\nlicense boot level network-advantage addon dna-advantage\nservice-template DEFAULT_LINKSEC_POLICY_MUST_SECURE\n linksec policy must-secure\nservice-template DEFAULT_LINKSEC_POLICY_SHOULD_SECURE\n linksec policy should-secure\nservice-template DEFAULT_CRITICAL_VOICE_TEMPLATE\n voice vlan\nservice-template DEFAULT_CRITICAL_DATA_TEMPLATE\nservice-template webauth-global-inactive\n inactivity-timer 3600 \narchive\n log config\n  logging enable\n  logging size 500\nmemory free low-watermark processor 104636\n!\nsystem mtu 9100\ndiagnostic bootup level minimal\n!\nspanning-tree mode rapid-pvst\nspanning-tree extend system-id\n!\n!\nerrdisable recovery cause udld\nerrdisable recovery cause bpduguard\nerrdisable recovery cause security-violation\nerrdisable recovery cause channel-misconfig\nerrdisable recovery cause pagp-flap\nerrdisable recovery cause dtp-flap\nerrdisable recovery cause link-flap\nerrdisable recovery cause sfp-config-mismatch\nerrdisable recovery cause gbic-invalid\nerrdisable recovery cause l2ptguard\nerrdisable recovery cause psecure-violation\nerrdisable recovery cause port-mode-failure\nerrdisable recovery cause dhcp-rate-limit\nerrdisable recovery cause pppoe-ia-rate-limit\nerrdisable recovery cause mac-limit\nerrdisable recovery cause storm-control\nerrdisable recovery cause inline-power\nerrdisable recovery cause arp-inspection\nerrdisable recovery cause link-monitor-failure\nerrdisable recovery cause oam-remote-failure\nerrdisable recovery cause loopback\nerrdisable recovery cause psp\nerrdisable recovery cause mrp-miscabling\nerrdisable recovery cause loopdetect\n!\nenable secret 9 xxxxxxxx\n!\nusername wlcaccess privilege 15 secret xxxxxx \n!\nredundancy\n mode sso\ncrypto engine compliance shield disable\n!\n!\n!\n!\n!\ntransceiver type all\n monitoring\n!\n!\nclass-map match-any system-cpp-police-ewlc-control\n description EWLC Control \nclass-map match-any system-cpp-police-topology-control\n description Topology control\nclass-map match-any system-cpp-police-sw-forward\n description Sw forwarding, L2 LVX data packets, LOGGING, Transit Traffic\nclass-map match-any system-cpp-default\n description EWLC Data, Inter FED Traffic \nclass-map match-any system-cpp-police-sys-data\n description Openflow, Exception, EGR Exception, NFL Sampled Data, RPF Failed\nclass-map match-any system-cpp-police-punt-webauth\n description Punt Webauth\nclass-map match-any system-cpp-police-l2lvx-control\n description L2 LVX control packets\nclass-map match-any system-cpp-police-forus\n description Forus traffic\nclass-map match-any system-cpp-police-multicast-end-station\n description MCAST END STATION\nclass-map match-any system-cpp-police-forus-addr-resolution\n description Forus address resolution\nclass-map match-any system-cpp-police-high-rate-app\n description High Rate Applications \nclass-map match-any system-cpp-police-multicast\n description MCAST Data\nclass-map match-any system-cpp-police-meraki-next-tunnel\n description Meraki Next tunnel\nclass-map match-any system-cpp-police-l2-control\n description L2 control\nclass-map match-any system-cpp-police-dot1x-auth\n description DOT1X Auth\nclass-map match-any system-cpp-police-data\n description ICMP redirect, ICMP_GEN and BROADCAST\nclass-map match-any system-cpp-police-stackwise-virt-control\n description Stackwise Virtual OOB\nclass-map match-any non-client-nrt-class\nclass-map match-any system-cpp-police-routing-control\n description Routing control and Low Latency\nclass-map match-any system-cpp-police-protocol-snooping\n description Protocol snooping\nclass-map match-any system-cpp-police-dhcp-snooping\n description DHCP snooping\nclass-map match-any system-cpp-police-ios-routing\n description L2 control, Topology control, Routing control, Low Latency\nclass-map match-any system-cpp-police-system-critical\n description System Critical and Gold Pkt\nclass-map match-any system-cpp-police-ios-feature\n description ICMPGEN,BROADCAST,ICMP,L2LVXCntrl,ProtoSnoop,PuntWebauth,MCASTData,Transit,DOT1XAuth,Swfwd,LOGGING,L2LVXData,ForusTraffic,ForusARP,McastEndStn,Openflow,Exception,EGRExcption,NflSampled,RpfFailed\n!\n!\npolicy-map system-cpp-policy\n!\n! \n!\n!\n!\n!\n!\n!\n!\n!\n!\n!\ninterface Loopback0\n description Fabric Node Router ID\n ip address 204.1.1.37 255.255.255.255\n ip pim sparse-mode\n ip router isis \n clns mtu 1492\n!\ninterface GigabitEthernet0/0\n vrf forwarding Mgmt-vrf\n no ip address\n negotiation auto\n!\ninterface TenGigabitEthernet1/0/1\n ip flow monitor dnacmonitor input\n ip flow monitor dnacmonitor_dns input\n ip flow monitor dnacmonitor output\n ip flow monitor dnacmonitor_dns output\n ipv6 flow monitor dnacmonitor_v6 input\n ipv6 flow monitor dnacmonitor_dns_v6 input\n ipv6 flow monitor dnacmonitor_v6 output\n ipv6 flow monitor dnacmonitor_dns_v6 output\n ip nbar protocol-discovery\n!\ninterface TenGigabitEthernet1/0/2\n ip flow monitor dnacmonitor input\n ip flow monitor dnacmonitor_dns input\n ip flow monitor dnacmonitor output\n ip flow monitor dnacmonitor_dns output\n ipv6 flow monitor dnacmonitor_v6 input\n ipv6 flow monitor dnacmonitor_dns_v6 input\n ipv6 flow monitor dnacmonitor_v6 output\n ipv6 flow monitor dnacmonitor_dns_v6 output\n ip nbar protocol-discovery\n!\ninterface TenGigabitEthernet1/0/3\n description Fabric Physical Link\n no switchport\n dampening\n ip address 204.1.1.135 255.255.255.254\n no ip redirects\n ip pim sparse-mode\n ip router isis \n load-interval 30\n no cts role-based enforcement\n bfd interval 250 min_rx 250 multiplier 3\n clns mtu 1492\n isis network point-to-point \n!\ninterface TenGigabitEthernet1/0/4\n description Fabric Physical Link\n no switchport\n dampening\n ip address 204.1.1.137 255.255.255.254\n no ip redirects\n ip pim sparse-mode\n ip router isis \n load-interval 30\n no cts role-based enforcement\n bfd interval 250 min_rx 250 multiplier 3\n clns mtu 1492\n isis network point-to-point \n!\ninterface TenGigabitEthernet1/0/5\n ip flow monitor dnacmonitor input\n ip flow monitor dnacmonitor_dns input\n ip flow monitor dnacmonitor output\n ip flow monitor dnacmonitor_dns output\n ipv6 flow monitor dnacmonitor_v6 input\n ipv6 flow monitor dnacmonitor_dns_v6 input\n ipv6 flow monitor dnacmonitor_v6 output\n ipv6 flow monitor dnacmonitor_dns_v6 output\n ip nbar protocol-discovery\n!\ninterface TenGigabitEthernet1/0/6\n ip flow monitor dnacmonitor input\n ip flow monitor dnacmonitor_dns input\n ip flow monitor dnacmonitor output\n ip flow monitor dnacmonitor_dns output\n ipv6 flow monitor dnacmonitor_v6 input\n ipv6 flow monitor dnacmonitor_dns_v6 input\n ipv6 flow monitor dnacmonitor_v6 output\n ipv6 flow monitor dnacmonitor_dns_v6 output\n ip nbar protocol-discovery\n!\ninterface TenGigabitEthernet1/0/7\n switchport mode access\n!\ninterface TenGigabitEthernet1/0/8\n ip flow monitor dnacmonitor input\n ip flow monitor dnacmonitor_dns input\n ip flow monitor dnacmonitor output\n ip flow monitor dnacmonitor_dns output\n ipv6 flow monitor dnacmonitor_v6 input\n ipv6 flow monitor dnacmonitor_dns_v6 input\n ipv6 flow monitor dnacmonitor_v6 output\n ipv6 flow monitor dnacmonitor_dns_v6 output\n ip nbar protocol-discovery\n!\ninterface TenGigabitEthernet1/0/9\n ip flow monitor dnacmonitor input\n ip flow monitor dnacmonitor_dns input\n ip flow monitor dnacmonitor output\n ip flow monitor dnacmonitor_dns output\n ipv6 flow monitor dnacmonitor_v6 input\n ipv6 flow monitor dnacmonitor_dns_v6 input\n ipv6 flow monitor dnacmonitor_v6 output\n ipv6 flow monitor dnacmonitor_dns_v6 output\n ip nbar protocol-discovery\n!\ninterface TenGigabitEthernet1/0/10\n ip flow monitor dnacmonitor input\n ip flow monitor dnacmonitor_dns input\n ip flow monitor dnacmonitor output\n ip flow monitor dnacmonitor_dns output\n ipv6 flow monitor dnacmonitor_v6 input\n ipv6 flow monitor dnacmonitor_dns_v6 input\n ipv6 flow monitor dnacmonitor_v6 output\n ipv6 flow monitor dnacmonitor_dns_v6 output\n ip nbar protocol-discovery\n!\ninterface TenGigabitEthernet1/0/11\n ip flow monitor dnacmonitor input\n ip flow monitor dnacmonitor_dns input\n ip flow monitor dnacmonitor output\n ip flow monitor dnacmonitor_dns output\n ipv6 flow monitor dnacmonitor_v6 input\n ipv6 flow monitor dnacmonitor_dns_v6 input\n ipv6 flow monitor dnacmonitor_v6 output\n ipv6 flow monitor dnacmonitor_dns_v6 output\n ip nbar protocol-discovery\n!\ninterface TenGigabitEthernet1/0/12\n ip flow monitor dnacmonitor input\n ip flow monitor dnacmonitor_dns input\n ip flow monitor dnacmonitor output\n ip flow monitor dnacmonitor_dns output\n ipv6 flow monitor dnacmonitor_v6 input\n ipv6 flow monitor dnacmonitor_dns_v6 input\n ipv6 flow monitor dnacmonitor_v6 output\n ipv6 flow monitor dnacmonitor_dns_v6 output\n ip nbar protocol-discovery\n!\ninterface TenGigabitEthernet1/0/13\n ip flow monitor dnacmonitor input\n ip flow monitor dnacmonitor_dns input\n ip flow monitor dnacmonitor output\n ip flow monitor dnacmonitor_dns output\n ipv6 flow monitor dnacmonitor_v6 input\n ipv6 flow monitor dnacmonitor_dns_v6 input\n ipv6 flow monitor dnacmonitor_v6 output\n ipv6 flow monitor dnacmonitor_dns_v6 output\n ip nbar protocol-discovery\n!\ninterface TenGigabitEthernet1/0/14\n ip flow monitor dnacmonitor input\n ip flow monitor dnacmonitor_dns input\n ip flow monitor dnacmonitor output\n ip flow monitor dnacmonitor_dns output\n ipv6 flow monitor dnacmonitor_v6 input\n ipv6 flow monitor dnacmonitor_dns_v6 input\n ipv6 flow monitor dnacmonitor_v6 output\n ipv6 flow monitor dnacmonitor_dns_v6 output\n ip nbar protocol-discovery\n!\ninterface TenGigabitEthernet1/0/15\n ip flow monitor dnacmonitor input\n ip flow monitor dnacmonitor_dns input\n ip flow monitor dnacmonitor output\n ip flow monitor dnacmonitor_dns output\n ipv6 flow monitor dnacmonitor_v6 input\n ipv6 flow monitor dnacmonitor_dns_v6 input\n ipv6 flow monitor dnacmonitor_v6 output\n ipv6 flow monitor dnacmonitor_dns_v6 output\n ip nbar protocol-discovery\n!\ninterface TenGigabitEthernet1/0/16\n ip flow monitor dnacmonitor input\n ip flow monitor dnacmonitor_dns input\n ip flow monitor dnacmonitor output\n ip flow monitor dnacmonitor_dns output\n ipv6 flow monitor dnacmonitor_v6 input\n ipv6 flow monitor dnacmonitor_dns_v6 input\n ipv6 flow monitor dnacmonitor_v6 output\n ipv6 flow monitor dnacmonitor_dns_v6 output\n ip nbar protocol-discovery\n!\ninterface TenGigabitEthernet1/0/17\n ip flow monitor dnacmonitor input\n ip flow monitor dnacmonitor_dns input\n ip flow monitor dnacmonitor output\n ip flow monitor dnacmonitor_dns output\n ipv6 flow monitor dnacmonitor_v6 input\n ipv6 flow monitor dnacmonitor_dns_v6 input\n ipv6 flow monitor dnacmonitor_v6 output\n ipv6 flow monitor dnacmonitor_dns_v6 output\n ip nbar protocol-discovery\n!\ninterface TenGigabitEthernet1/0/18\n ip flow monitor dnacmonitor input\n ip flow monitor dnacmonitor_dns input\n ip flow monitor dnacmonitor output\n ip flow monitor dnacmonitor_dns output\n ipv6 flow monitor dnacmonitor_v6 input\n ipv6 flow monitor dnacmonitor_dns_v6 input\n ipv6 flow monitor dnacmonitor_v6 output\n ipv6 flow monitor dnacmonitor_dns_v6 output\n ip nbar protocol-discovery\n!\ninterface TenGigabitEthernet1/0/19\n ip flow monitor dnacmonitor input\n ip flow monitor dnacmonitor_dns input\n ip flow monitor dnacmonitor output\n ip flow monitor dnacmonitor_dns output\n ipv6 flow monitor dnacmonitor_v6 input\n ipv6 flow monitor dnacmonitor_dns_v6 input\n ipv6 flow monitor dnacmonitor_v6 output\n ipv6 flow monitor dnacmonitor_dns_v6 output\n ip nbar protocol-discovery\n!\ninterface TenGigabitEthernet1/0/20\n ip flow monitor dnacmonitor input\n ip flow monitor dnacmonitor_dns input\n ip flow monitor dnacmonitor output\n ip flow monitor dnacmonitor_dns output\n ipv6 flow monitor dnacmonitor_v6 input\n ipv6 flow monitor dnacmonitor_dns_v6 input\n ipv6 flow monitor dnacmonitor_v6 output\n ipv6 flow monitor dnacmonitor_dns_v6 output\n ip nbar protocol-discovery\n!\ninterface TenGigabitEthernet1/0/21\n ip flow monitor dnacmonitor input\n ip flow monitor dnacmonitor_dns input\n ip flow monitor dnacmonitor output\n ip flow monitor dnacmonitor_dns output\n ipv6 flow monitor dnacmonitor_v6 input\n ipv6 flow monitor dnacmonitor_dns_v6 input\n ipv6 flow monitor dnacmonitor_v6 output\n ipv6 flow monitor dnacmonitor_dns_v6 output\n ip nbar protocol-discovery\n!\ninterface TenGigabitEthernet1/0/22\n ip flow monitor dnacmonitor input\n ip flow monitor dnacmonitor_dns input\n ip flow monitor dnacmonitor output\n ip flow monitor dnacmonitor_dns output\n ipv6 flow monitor dnacmonitor_v6 input\n ipv6 flow monitor dnacmonitor_dns_v6 input\n ipv6 flow monitor dnacmonitor_v6 output\n ipv6 flow monitor dnacmonitor_dns_v6 output\n ip nbar protocol-discovery\n!\ninterface TenGigabitEthernet1/0/23\n ip flow monitor dnacmonitor input\n ip flow monitor dnacmonitor_dns input\n ip flow monitor dnacmonitor output\n ip flow monitor dnacmonitor_dns output\n ipv6 flow monitor dnacmonitor_v6 input\n ipv6 flow monitor dnacmonitor_dns_v6 input\n ipv6 flow monitor dnacmonitor_v6 output\n ipv6 flow monitor dnacmonitor_dns_v6 output\n ip nbar protocol-discovery\n!\ninterface TenGigabitEthernet1/0/24\n description Fabric Physical Link\n no switchport\n dampening\n ip address 204.1.2.2 255.255.255.254\n no ip redirects\n ip pim sparse-mode\n ip router isis \n load-interval 30\n no cts role-based enforcement\n bfd interval 250 min_rx 250 multiplier 3\n clns mtu 1492\n isis network point-to-point \n!\ninterface GigabitEthernet1/1/1\n ip flow monitor dnacmonitor input\n ip flow monitor dnacmonitor_dns input\n ip flow monitor dnacmonitor output\n ip flow monitor dnacmonitor_dns output\n ipv6 flow monitor dnacmonitor_v6 input\n ipv6 flow monitor dnacmonitor_dns_v6 input\n ipv6 flow monitor dnacmonitor_v6 output\n ipv6 flow monitor dnacmonitor_dns_v6 output\n ip nbar protocol-discovery\n!\ninterface GigabitEthernet1/1/2\n ip flow monitor dnacmonitor input\n ip flow monitor dnacmonitor_dns input\n ip flow monitor dnacmonitor output\n ip flow monitor dnacmonitor_dns output\n ipv6 flow monitor dnacmonitor_v6 input\n ipv6 flow monitor dnacmonitor_dns_v6 input\n ipv6 flow monitor dnacmonitor_v6 output\n ipv6 flow monitor dnacmonitor_dns_v6 output\n ip nbar protocol-discovery\n!\ninterface GigabitEthernet1/1/3\n ip flow monitor dnacmonitor input\n ip flow monitor dnacmonitor_dns input\n ip flow monitor dnacmonitor output\n ip flow monitor dnacmonitor_dns output\n ipv6 flow monitor dnacmonitor_v6 input\n ipv6 flow monitor dnacmonitor_dns_v6 input\n ipv6 flow monitor dnacmonitor_v6 output\n ipv6 flow monitor dnacmonitor_dns_v6 output\n ip nbar protocol-discovery\n!\ninterface GigabitEthernet1/1/4\n ip flow monitor dnacmonitor input\n ip flow monitor dnacmonitor_dns input\n ip flow monitor dnacmonitor output\n ip flow monitor dnacmonitor_dns output\n ipv6 flow monitor dnacmonitor_v6 input\n ipv6 flow monitor dnacmonitor_dns_v6 input\n ipv6 flow monitor dnacmonitor_v6 output\n ipv6 flow monitor dnacmonitor_dns_v6 output\n ip nbar protocol-discovery\n!\ninterface TenGigabitEthernet1/1/1\n ip flow monitor dnacmonitor input\n ip flow monitor dnacmonitor_dns input\n ip flow monitor dnacmonitor output\n ip flow monitor dnacmonitor_dns output\n ipv6 flow monitor dnacmonitor_v6 input\n ipv6 flow monitor dnacmonitor_dns_v6 input\n ipv6 flow monitor dnacmonitor_v6 output\n ipv6 flow monitor dnacmonitor_dns_v6 output\n ip nbar protocol-discovery\n!\ninterface TenGigabitEthernet1/1/2\n ip flow monitor dnacmonitor input\n ip flow monitor dnacmonitor_dns input\n ip flow monitor dnacmonitor output\n ip flow monitor dnacmonitor_dns output\n ipv6 flow monitor dnacmonitor_v6 input\n ipv6 flow monitor dnacmonitor_dns_v6 input\n ipv6 flow monitor dnacmonitor_v6 output\n ipv6 flow monitor dnacmonitor_dns_v6 output\n ip nbar protocol-discovery\n!\ninterface TenGigabitEthernet1/1/3\n ip flow monitor dnacmonitor input\n ip flow monitor dnacmonitor_dns input\n ip flow monitor dnacmonitor output\n ip flow monitor dnacmonitor_dns output\n ipv6 flow monitor dnacmonitor_v6 input\n ipv6 flow monitor dnacmonitor_dns_v6 input\n ipv6 flow monitor dnacmonitor_v6 output\n ipv6 flow monitor dnacmonitor_dns_v6 output\n ip nbar protocol-discovery\n!\ninterface TenGigabitEthernet1/1/4\n ip flow monitor dnacmonitor input\n ip flow monitor dnacmonitor_dns input\n ip flow monitor dnacmonitor output\n ip flow monitor dnacmonitor_dns output\n ipv6 flow monitor dnacmonitor_v6 input\n ipv6 flow monitor dnacmonitor_dns_v6 input\n ipv6 flow monitor dnacmonitor_v6 output\n ipv6 flow monitor dnacmonitor_dns_v6 output\n ip nbar protocol-discovery\n!\ninterface TenGigabitEthernet1/1/5\n ip flow monitor dnacmonitor input\n ip flow monitor dnacmonitor_dns input\n ip flow monitor dnacmonitor output\n ip flow monitor dnacmonitor_dns output\n ipv6 flow monitor dnacmonitor_v6 input\n ipv6 flow monitor dnacmonitor_dns_v6 input\n ipv6 flow monitor dnacmonitor_v6 output\n ipv6 flow monitor dnacmonitor_dns_v6 output\n ip nbar protocol-discovery\n!\ninterface TenGigabitEthernet1/1/6\n ip flow monitor dnacmonitor input\n ip flow monitor dnacmonitor_dns input\n ip flow monitor dnacmonitor output\n ip flow monitor dnacmonitor_dns output\n ipv6 flow monitor dnacmonitor_v6 input\n ipv6 flow monitor dnacmonitor_dns_v6 input\n ipv6 flow monitor dnacmonitor_v6 output\n ipv6 flow monitor dnacmonitor_dns_v6 output\n ip nbar protocol-discovery\n!\ninterface TenGigabitEthernet1/1/7\n ip flow monitor dnacmonitor input\n ip flow monitor dnacmonitor_dns input\n ip flow monitor dnacmonitor output\n ip flow monitor dnacmonitor_dns output\n ipv6 flow monitor dnacmonitor_v6 input\n ipv6 flow monitor dnacmonitor_dns_v6 input\n ipv6 flow monitor dnacmonitor_v6 output\n ipv6 flow monitor dnacmonitor_dns_v6 output\n ip nbar protocol-discovery\n!\ninterface TenGigabitEthernet1/1/8\n ip flow monitor dnacmonitor input\n ip flow monitor dnacmonitor_dns input\n ip flow monitor dnacmonitor output\n ip flow monitor dnacmonitor_dns output\n ipv6 flow monitor dnacmonitor_v6 input\n ipv6 flow monitor dnacmonitor_dns_v6 input\n ipv6 flow monitor dnacmonitor_v6 output\n ipv6 flow monitor dnacmonitor_dns_v6 output\n ip nbar protocol-discovery\n!\ninterface FortyGigabitEthernet1/1/1\n ip flow monitor dnacmonitor input\n ip flow monitor dnacmonitor_dns input\n ip flow monitor dnacmonitor output\n ip flow monitor dnacmonitor_dns output\n ipv6 flow monitor dnacmonitor_v6 input\n ipv6 flow monitor dnacmonitor_dns_v6 input\n ipv6 flow monitor dnacmonitor_v6 output\n ipv6 flow monitor dnacmonitor_dns_v6 output\n ip nbar protocol-discovery\n!\ninterface FortyGigabitEthernet1/1/2\n ip flow monitor dnacmonitor input\n ip flow monitor dnacmonitor_dns input\n ip flow monitor dnacmonitor output\n ip flow monitor dnacmonitor_dns output\n ipv6 flow monitor dnacmonitor_v6 input\n ipv6 flow monitor dnacmonitor_dns_v6 input\n ipv6 flow monitor dnacmonitor_v6 output\n ipv6 flow monitor dnacmonitor_dns_v6 output\n ip nbar protocol-discovery\n!\ninterface TwentyFiveGigE1/1/1\n ip flow monitor dnacmonitor input\n ip flow monitor dnacmonitor_dns input\n ip flow monitor dnacmonitor output\n ip flow monitor dnacmonitor_dns output\n ipv6 flow monitor dnacmonitor_v6 input\n ipv6 flow monitor dnacmonitor_dns_v6 input\n ipv6 flow monitor dnacmonitor_v6 output\n ipv6 flow monitor dnacmonitor_dns_v6 output\n ip nbar protocol-discovery\n!\ninterface TwentyFiveGigE1/1/2\n ip flow monitor dnacmonitor input\n ip flow monitor dnacmonitor_dns input\n ip flow monitor dnacmonitor output\n ip flow monitor dnacmonitor_dns output\n ipv6 flow monitor dnacmonitor_v6 input\n ipv6 flow monitor dnacmonitor_dns_v6 input\n ipv6 flow monitor dnacmonitor_v6 output\n ipv6 flow monitor dnacmonitor_dns_v6 output\n ip nbar protocol-discovery\n!\ninterface AppGigabitEthernet1/0/1\n!\ninterface Bluetooth0/4\n vrf forwarding Mgmt-vrf\n no ip address\n shutdown\n negotiation auto\n enable\n!\ninterface Vlan1\n ip dhcp client client-id ascii cisco-0c75.bd8f.a3c7-Vl1\n no ip address\n!\nrouter lisp\n domain-id 561956669\n locator-table default\n service ipv4\n  encapsulation vxlan\n  sgt\n  map-server\n  map-resolver\n  exit-service-ipv4\n !\n service ipv6\n  encapsulation vxlan\n  sgt\n  map-server\n  map-resolver\n  exit-service-ipv6\n !\n map-server rloc members distribute\n site site_uci\n  description map-server configured from Catalyst Center\n  authentication-key 7 xxxxxxxxx\n  eid-record instance-id 4097 0.0.0.0/0 accept-more-specifics\n  eid-record instance-id 4097 ::/0 accept-more-specifics\n  eid-record instance-id 4098 0.0.0.0/0 accept-more-specifics\n  eid-record instance-id 4098 ::/0 accept-more-specifics\n  eid-record instance-id 4099 0.0.0.0/0 accept-more-specifics\n  eid-record instance-id 4099 ::/0 accept-more-specifics\n  eid-record instance-id 4104 0.0.0.0/0 accept-more-specifics\n  eid-record instance-id 4104 ::/0 accept-more-specifics\n  eid-record instance-id 4105 0.0.0.0/0 accept-more-specifics\n  eid-record instance-id 4105 ::/0 accept-more-specifics\n  eid-record instance-id 4106 0.0.0.0/0 accept-more-specifics\n  eid-record instance-id 4106 ::/0 accept-more-specifics\n  eid-record instance-id 4107 0.0.0.0/0 accept-more-specifics\n  eid-record instance-id 4107 ::/0 accept-more-specifics\n  eid-record instance-id 4108 0.0.0.0/0 accept-more-specifics\n  eid-record instance-id 4108 ::/0 accept-more-specifics\n  eid-record instance-id 4109 0.0.0.0/0 accept-more-specifics\n  eid-record instance-id 4109 ::/0 accept-more-specifics\n  eid-record instance-id 4110 0.0.0.0/0 accept-more-specifics\n  eid-record instance-id 4110 ::/0 accept-more-specifics\n  eid-record instance-id 4111 0.0.0.0/0 accept-more-specifics\n  eid-record instance-id 4111 ::/0 accept-more-specifics\n  eid-record instance-id 4112 0.0.0.0/0 accept-more-specifics\n  eid-record instance-id 4112 ::/0 accept-more-specifics\n  eid-record instance-id 4113 0.0.0.0/0 accept-more-specifics\n  eid-record instance-id 4113 ::/0 accept-more-specifics\n  eid-record instance-id 4114 0.0.0.0/0 accept-more-specifics\n  eid-record instance-id 4114 ::/0 accept-more-specifics\n  eid-record instance-id 4115 0.0.0.0/0 accept-more-specifics\n  eid-record instance-id 4115 ::/0 accept-more-specifics\n  eid-record instance-id 4116 0.0.0.0/0 accept-more-specifics\n  eid-record instance-id 4116 ::/0 accept-more-specifics\n  eid-record instance-id 4117 0.0.0.0/0 accept-more-specifics\n  eid-record instance-id 4117 ::/0 accept-more-specifics\n  allow-locator-default-etr instance-id 4097 ipv4\n  allow-locator-default-etr instance-id 4097 ipv6\n  allow-locator-default-etr instance-id 4098 ipv4\n  allow-locator-default-etr instance-id 4098 ipv6\n  allow-locator-default-etr instance-id 4099 ipv4\n  allow-locator-default-etr instance-id 4099 ipv6\n  allow-locator-default-etr instance-id 4104 ipv4\n  allow-locator-default-etr instance-id 4104 ipv6\n  allow-locator-default-etr instance-id 4105 ipv4\n  allow-locator-default-etr instance-id 4105 ipv6\n  allow-locator-default-etr instance-id 4106 ipv4\n  allow-locator-default-etr instance-id 4106 ipv6\n  allow-locator-default-etr instance-id 4107 ipv4\n  allow-locator-default-etr instance-id 4107 ipv6\n  allow-locator-default-etr instance-id 4108 ipv4\n  allow-locator-default-etr instance-id 4108 ipv6\n  allow-locator-default-etr instance-id 4109 ipv4\n  allow-locator-default-etr instance-id 4109 ipv6\n  allow-locator-default-etr instance-id 4110 ipv4\n  allow-locator-default-etr instance-id 4110 ipv6\n  allow-locator-default-etr instance-id 4111 ipv4\n  allow-locator-default-etr instance-id 4111 ipv6\n  allow-locator-default-etr instance-id 4112 ipv4\n  allow-locator-default-etr instance-id 4112 ipv6\n  allow-locator-default-etr instance-id 4113 ipv4\n  allow-locator-default-etr instance-id 4113 ipv6\n  allow-locator-default-etr instance-id 4114 ipv4\n  allow-locator-default-etr instance-id 4114 ipv6\n  allow-locator-default-etr instance-id 4115 ipv4\n  allow-locator-default-etr instance-id 4115 ipv6\n  allow-locator-default-etr instance-id 4116 ipv4\n  allow-locator-default-etr instance-id 4116 ipv6\n  allow-locator-default-etr instance-id 4117 ipv4\n  allow-locator-default-etr instance-id 4117 ipv6\n  exit-site\n !\n ipv4 source-locator Loopback0\n ipv6 source-locator Loopback0\n exit-router-lisp\n!\nrouter isis\n net 49.0000.171f.616e.36b1.00\n is-type level-2-only\n domain-password xxxxxx\n metric-style wide\n log-adjacency-changes\n nsf ietf\n bfd all-interfaces\n!\nip forward-protocol nd\nip forward-protocol udp\nip http server\nip http authentication local\nip http secure-server\nip http client source-interface Loopback0\nip pim rp-address 204.1.1.34\nip pim register-source Loopback0\nip pim ssm default\nip ssh bulk-mode 131072\nip ssh source-interface Loopback0\nip scp server enable\n!\n!\nip access-list extended ACL_WEBAUTH_REDIRECT\n 20 deny ip any host 85.1.1.3\n 500 permit tcp any any eq www\n 600 permit tcp any any eq 443\n 700 permit tcp any any eq 8443\n 800 deny udp any any eq domain\n 900 deny udp any eq bootpc any eq bootps\nip radius source-interface Loopback0 \nlogging source-interface Loopback0\nlogging host 6.6.6.6\nlogging host 85.1.1.2\nsnmp-server group DNACGROUPAuthPriv v3 priv read DNAC-ACCESS write DNAC-ACCESS \nsnmp-server view xxxxxxxx\nsnmp-server trap-source Loopback0\nsnmp-server enable traps snmp authentication linkdown linkup coldstart warmstart\nsnmp-server enable traps flowmon\nsnmp-server enable traps entity-perf throughput-notif\nsnmp-server enable traps call-home message-send-fail server-fail\nsnmp-server enable traps tty\nsnmp-server enable traps eigrp\nsnmp-server enable traps ospf state-change\nsnmp-server enable traps ospf errors\nsnmp-server enable traps ospf retransmit\nsnmp-server enable traps ospf lsa\nsnmp-server enable traps ospf cisco-specific state-change nssa-trans-change\nsnmp-server enable traps ospf cisco-specific state-change shamlink interface\nsnmp-server enable traps ospf cisco-specific state-change shamlink neighbor\nsnmp-server enable traps ospf cisco-specific errors\nsnmp-server enable traps ospf cisco-specific retransmit\nsnmp-server enable traps ospf cisco-specific lsa\nsnmp-server enable traps bfd\nsnmp-server enable traps smart-license\nsnmp-server enable traps auth-framework sec-violation\nsnmp-server enable traps rep\nsnmp-server enable traps memory bufferpeak\nsnmp-server enable traps config-copy\nsnmp-server enable traps config\nsnmp-server enable traps config-ctid\nsnmp-server enable traps fru-ctrl\nsnmp-server enable traps entity\nsnmp-server enable traps flash insertion removal lowspace\nsnmp-server enable traps power-ethernet group 1 threshold 80\nsnmp-server enable traps power-ethernet police\nsnmp-server enable traps cpu threshold\nsnmp-server enable traps syslog\nsnmp-server enable traps udld link-fail-rpt\nsnmp-server enable traps udld status-change\nsnmp-server enable traps vtp\nsnmp-server enable traps vlancreate\nsnmp-server enable traps vlandelete\nsnmp-server enable traps port-security\nsnmp-server enable traps envmon\nsnmp-server enable traps stackwise\nsnmp-server enable traps mvpn\nsnmp-server enable traps pw vc\nsnmp-server enable traps ipsla\nsnmp-server enable traps dhcp\nsnmp-server enable traps event-manager\nsnmp-server enable traps ike policy add\nsnmp-server enable traps ike policy delete\nsnmp-server enable traps ike tunnel start\nsnmp-server enable traps ike tunnel stop\nsnmp-server enable traps ipsec cryptomap add\nsnmp-server enable traps ipsec cryptomap delete\nsnmp-server enable traps ipsec cryptomap attach\nsnmp-server enable traps ipsec cryptomap detach\nsnmp-server enable traps ipsec tunnel start\nsnmp-server enable traps ipsec tunnel stop\nsnmp-server enable traps ipsec too-many-sas\nsnmp-server enable traps ospfv3 state-change\nsnmp-server enable traps ospfv3 errors\nsnmp-server enable traps ipmulticast\nsnmp-server enable traps msdp\nsnmp-server enable traps pim neighbor-change rp-mapping-change invalid-pim-message\nsnmp-server enable traps bridge newroot topologychange\nsnmp-server enable traps stpx inconsistency root-inconsistency loop-inconsistency\nsnmp-server enable traps bgp cbgp2 state-changes all backward-trans limited updown-limited\nsnmp-server enable traps bgp cbgp2 threshold prefix\nsnmp-server enable traps hsrp\nsnmp-server enable traps isis\nsnmp-server enable traps cef resource-failure peer-state-change peer-fib-state-change inconsistency\nsnmp-server enable traps lisp\nsnmp-server enable traps nhrp nhs\nsnmp-server enable traps nhrp nhc\nsnmp-server enable traps nhrp nhp\nsnmp-server enable traps nhrp quota-exceeded\nsnmp-server enable traps local-auth\nsnmp-server enable traps entity-diag boot-up-fail hm-test-recover hm-thresh-reached scheduled-test-fail\nsnmp-server enable traps mpls rfc ldp\nsnmp-server enable traps mpls ldp\nsnmp-server enable traps mpls rfc traffic-eng\nsnmp-server enable traps mpls traffic-eng\nsnmp-server enable traps mpls fast-reroute protected\nsnmp-server enable traps bulkstat collection transfer\nsnmp-server enable traps mac-notification change move threshold\nsnmp-server enable traps errdisable\nsnmp-server enable traps vlan-membership\nsnmp-server enable traps transceiver all\nsnmp-server enable traps vrfmib vrf-up vrf-down vnet-trunk-up vnet-trunk-down\nsnmp-server enable traps rf\nsnmp-server enable traps mpls vpn\nsnmp-server enable traps mpls rfc vpn\nsnmp-server host 8.8.8.8 version 3 priv xxxxxxxx \nsnmp-server host 85.1.1.2 version 3 priv xxxxxxxx \n!\nradius-server attribute 6 on-for-login-auth\nradius-server attribute 6 support-multiple\nradius-server attribute 8 include-in-access-req\nradius-server attribute 25 access-request include\nradius-server attribute 31 mac format ietf upper-case\nradius-server attribute 31 send nas-port-detail mac-only\nradius-server dead-criteria time 5 tries 3\nradius-server deadtime 3\n!\nradius server dnac-radius_85.1.1.3\n address ipv4 85.1.1.3 auth-port 1812 acct-port 1813\n timeout 10\n retransmit 1\n automate-tester username dummy ignore-acct-port probe-on\n  pac key 7 xxxxxxxx\n!\n!\n!\ncontrol-plane\n service-policy input system-cpp-policy\n!\n!\nbanner motd ^CThis Device is part of Solution Sanity Testbed\n Please log off if you are not intended user\n Contact pawansi for further details\n^C\n!\nline con 0\n exec-timeout 0 0\n stopbits 1\nline vty 0 4\n exec-timeout 0 0\n authorization exec VTY_author\n login xxxxxx\n transport preferred none\n transport input ssh\nline vty 5 15\n authorization exec VTY_author\n login xxxxxx\n transport preferred none\n transport input ssh\nline vty 16 31\n transport input ssh\n!\nntp source Loopback0\nntp server 172.23.9.220\n!\n!\n!\n!\n!\n!\ntelemetry ietf subscription 500\n encoding encode-tdl\n filter tdl-uri /services;serviceName=ios_oper/poe_port_detail\n receiver-type protocol\n source-address 204.1.1.37\n stream native\n update-policy periodic 360000\n receiver name DNAC_ASSURANCE_RECEIVER\ntelemetry ietf subscription 501\n encoding encode-tdl\n filter tdl-uri /services;serviceName=ios_oper/poe_module\n receiver-type protocol\n source-address 204.1.1.37\n stream native\n update-policy periodic 360000\n receiver name DNAC_ASSURANCE_RECEIVER\ntelemetry ietf subscription 502\n encoding encode-tdl\n filter tdl-uri /services;serviceName=ios_oper/poe_stack\n receiver-type protocol\n source-address 204.1.1.37\n stream native\n update-policy periodic 360000\n receiver name DNAC_ASSURANCE_RECEIVER\ntelemetry ietf subscription 503\n encoding encode-tdl\n filter tdl-uri /services;serviceName=ios_oper/poe_switch\n receiver-type protocol\n source-address 204.1.1.37\n stream native\n update-policy periodic 360000\n receiver name DNAC_ASSURANCE_RECEIVER\ntelemetry ietf subscription 504\n encoding encode-tdl\n filter nested-uri /services;serviceName=ios_oper/platform_component;cname=0?platform_properties\n receiver-type protocol\n source-address 204.1.1.37\n stream native\n update-policy periodic 30000\n receiver name DNAC_ASSURANCE_RECEIVER\ntelemetry ietf subscription 550\n encoding encode-tdl\n filter tdl-uri /services;serviceName=smevent/sessionevent\n receiver-type protocol\n source-address 204.1.1.37\n stream native\n update-policy on-change\n receiver name DNAC_ASSURANCE_RECEIVER\ntelemetry ietf subscription 551\n encoding encode-tdl\n filter tdl-uri /services;serviceName=sessmgr_oper/session_context_data\n receiver-type protocol\n source-address 204.1.1.37\n stream native\n update-policy periodic 360000\n receiver name DNAC_ASSURANCE_RECEIVER\ntelemetry ietf subscription 552\n encoding encode-tdl\n filter tdl-uri /services;serviceName=iosevent/sisf_mac_oper_state\n receiver-type protocol\n source-address 204.1.1.37\n stream native\n update-policy on-change\n receiver name DNAC_ASSURANCE_RECEIVER\ntelemetry ietf subscription 553\n encoding encode-tdl\n filter tdl-uri /services;serviceName=ios_oper/sisf_db_wired_mac\n receiver-type protocol\n source-address 204.1.1.37\n stream native\n update-policy periodic 360000\n receiver name DNAC_ASSURANCE_RECEIVER\ntelemetry ietf subscription 554\n encoding encode-tdl\n filter tdl-uri /services;serviceName=ios_oper/cdp_neighbor_detail\n receiver-type protocol\n source-address 204.1.1.37\n stream native\n update-policy periodic 360000\n receiver name DNAC_ASSURANCE_RECEIVER\ntelemetry ietf subscription 555\n encoding encode-tdl\n filter tdl-uri /services;serviceName=ios_oper/cdp_neighbor_detail\n receiver-type protocol\n source-address 204.1.1.37\n stream native\n update-policy on-change\n receiver name DNAC_ASSURANCE_RECEIVER\ntelemetry ietf subscription 600\n encoding encode-tdl\n filter tdl-uri /services;serviceName=sessmgr_oper/tbl_aaa_servers_stat\n receiver-type protocol\n source-address 204.1.1.37\n stream native\n update-policy periodic 60000\n receiver name DNAC_ASSURANCE_RECEIVER\ntelemetry ietf subscription 601\n encoding encode-tdl\n filter tdl-uri /services;serviceName=sessmgr_oper/tbl_aaa_servers_stat\n receiver-type protocol\n source-address 204.1.1.37\n stream native\n update-policy on-change\n receiver name DNAC_ASSURANCE_RECEIVER\ntelemetry ietf subscription 602\n encoding encode-tdl\n filter tdl-uri /services;serviceName=ios_emul_oper/lisp_routers;top_id=0/sessions\n receiver-type protocol\n source-address 204.1.1.37\n stream native\n update-policy periodic 360000\n receiver name DNAC_ASSURANCE_RECEIVER\ntelemetry ietf subscription 603\n encoding encode-tdl\n filter tdl-uri /services;serviceName=iosevent/lisp_tcp_session_state\n receiver-type protocol\n source-address 204.1.1.37\n stream native\n update-policy on-change\n receiver name DNAC_ASSURANCE_RECEIVER\ntelemetry ietf subscription 604\n encoding encode-tdl\n filter nested-uri /services;serviceName=ios_emul_oper/lisp_routers;top_id=0/instances;iid=0/af;iaftype=LISP_TDL_IAF_IPV4/lisp_publisher\n receiver-type protocol\n source-address 204.1.1.37\n stream native\n update-policy periodic 360000\n receiver name DNAC_ASSURANCE_RECEIVER\ntelemetry ietf subscription 605\n encoding encode-tdl\n filter tdl-uri /services;serviceName=iosevent/lisp_pubsub_session_state\n receiver-type protocol\n source-address 204.1.1.37\n stream native\n update-policy on-change\n receiver name DNAC_ASSURANCE_RECEIVER\ntelemetry ietf subscription 606\n encoding encode-tdl\n filter nested-uri /services;serviceName=ios_emul_oper/lisp_routers;top_id=0/remote_locator_sets;name=default-etr-locator-set-ipv4/rem_loc_set_rlocs_si\n receiver-type protocol\n source-address 204.1.1.37\n stream native\n update-policy periodic 360000\n receiver name DNAC_ASSURANCE_RECEIVER\ntelemetry ietf subscription 607\n encoding encode-tdl\n filter tdl-uri /services;serviceName=iosevent/lisp_etr_si_type\n receiver-type protocol\n source-address 204.1.1.37\n stream native\n update-policy on-change\n receiver name DNAC_ASSURANCE_RECEIVER\ntelemetry ietf subscription 608\n encoding encode-tdl\n filter tdl-uri /services;serviceName=ios_emul_oper/cts_env_data\n receiver-type protocol\n source-address 204.1.1.37\n stream native\n update-policy periodic 60000\n receiver name DNAC_ASSURANCE_RECEIVER\ntelemetry ietf subscription 609\n encoding encode-tdl\n filter tdl-uri /services;serviceName=ios_emul_oper/bgp_state;singleton_id=0/neighbor\n receiver-type protocol\n source-address 204.1.1.37\n stream native\n update-policy periodic 360000\n receiver name DNAC_ASSURANCE_RECEIVER\ntelemetry ietf subscription 610\n encoding encode-tdl\n filter tdl-uri /services;serviceName=ios_emul_oper/bgp_state;singleton_id=0/neighbor\n receiver-type protocol\n source-address 204.1.1.37\n stream native\n update-policy on-change\n receiver name DNAC_ASSURANCE_RECEIVER\ntelemetry ietf subscription 611\n encoding encode-tdl\n filter tdl-uri /services;serviceName=iosevent/lisp_extranet_policy_state\n receiver-type protocol\n source-address 204.1.1.37\n stream native\n update-policy on-change\n receiver name DNAC_ASSURANCE_RECEIVER\ntelemetry ietf subscription 612\n encoding encode-tdl\n filter nested-uri /services;serviceName=ios_emul_oper/lisp_routers;top_id=0/instances;iid=1/extranets\n receiver-type protocol\n source-address 204.1.1.37\n stream native\n update-policy periodic 360000\n receiver name DNAC_ASSURANCE_RECEIVER\ntelemetry ietf subscription 613\n encoding encode-tdl\n filter nested-uri /services;serviceName=ios_emul_oper/lisp_routers;top_id=0/instances;iid=1/extranets;extranet_name=ext1/extranet_member_instances\n receiver-type protocol\n source-address 204.1.1.37\n stream native\n update-policy periodic 360000\n receiver name DNAC_ASSURANCE_RECEIVER\ntelemetry ietf subscription 614\n encoding encode-tdl\n filter nested-uri /services;serviceName=ios_oper/nve_oper;unit_number=0/nve_vni_oper\n receiver-type protocol\n source-address 204.1.1.37\n stream native\n update-policy periodic 960000\n receiver name DNAC_ASSURANCE_RECEIVER\ntelemetry ietf subscription 615\n encoding encode-tdl\n filter nested-uri /services;serviceName=ios_oper/nve_oper;unit_number=0/nve_peer_oper\n receiver-type protocol\n source-address 204.1.1.37\n stream native\n update-policy periodic 960000\n receiver name DNAC_ASSURANCE_RECEIVER\ntelemetry ietf subscription 616\n encoding encode-tdl\n filter nested-uri /services;serviceName=ios_oper/nve_oper\n receiver-type protocol\n source-address 204.1.1.37\n stream native\n update-policy on-change\n receiver name DNAC_ASSURANCE_RECEIVER\ntelemetry ietf subscription 750\n encoding encode-tdl\n filter tdl-uri /services;serviceName=ios_emul_oper/environment_sensor\n receiver-type protocol\n source-address 204.1.1.37\n stream native\n update-policy periodic 30000\n receiver name DNAC_ASSURANCE_RECEIVER\ntelemetry ietf subscription 751\n encoding encode-tdl\n filter tdl-uri /services;serviceName=ios_oper/platform_component\n receiver-type protocol\n source-address 204.1.1.37\n stream native\n update-policy periodic 30000\n receiver name DNAC_ASSURANCE_RECEIVER\ntelemetry ietf subscription 1020\n encoding encode-tdl\n filter tdl-uri /services;serviceName=iosevent/install_status\n receiver-type protocol\n source-address 204.1.1.37\n stream native\n update-policy on-change\n receiver name DNAC_ASSURANCE_RECEIVER\ntelemetry ietf subscription 8882\n encoding encode-tdl\n filter tdl-transform trustSecCounterDelta\n receiver-type protocol\n source-address 204.1.1.37\n stream native\n update-policy periodic 90000\n receiver name DNAC_ASSURANCE_RECEIVER\ntelemetry receiver protocol DNAC_ASSURANCE_RECEIVER\n host ip-address 85.1.1.2 25103\n protocol tls-native profile sdn-network-infra-iwan\ntelemetry transform trustSecCounterDelta\n input table cts_rolebased_policy\n  field dst_sgt\n  field src_sgt\n  field sgacl_name\n  field monitor_mode\n  field num_of_sgacl\n  field policy_life_time\n  field total_deny_count\n  field last_updated_time\n  field total_permit_count\n  join-key cts_role_based_policy_key\n  logical-op and\n  type mandatory\n  uri /services;serviceName=ios_emul_oper/cts_rolebased_policy\n operation 1\n  output-field 1\n   field cts_rolebased_policy.src_sgt\n  output-field 2\n   field cts_rolebased_policy.dst_sgt\n  output-field 3\n   field cts_rolebased_policy.total_permit_count\n   output-op type delta\n  output-field 4\n   field cts_rolebased_policy.total_deny_count\n   output-op type delta\n  output-field 5\n   field cts_rolebased_policy.sgacl_name\n  output-field 6\n   field cts_rolebased_policy.monitor_mode\n  output-field 7\n   field cts_rolebased_policy.num_of_sgacl\n  output-field 8\n   field cts_rolebased_policy.policy_life_time\n  output-field 9\n   field cts_rolebased_policy.last_updated_time\n specified\nnetconf-yang\nend\n\n'
            ]
          }
        ]
      }
    ]
  ]
)
    def test_network_devices_info_workflow_manager_playbook_interface_details(self):
        """
        Test the Network Devices Info Workflow Manager's device information retrieval process.

        This test verifies that the workflow correctly handles the retrieval of network device information,
        ensuring proper validation and expected behavior.
        """

        set_module_args(
            dict(
                dnac_host="1.1.1.1",
                dnac_username="dummy",
                dnac_password="dummy",
                dnac_log=True,
                state="queried",
                config_verify=True,
                dnac_version="2.3.7.9",
                config=self.playbook_interface_details
            )
        )
        result = self.execute_module(changed=False, failed=False)
        print(result)
        self.assertEqual(
            result.get("response"),
[
  "The network devices found: ['204.1.1.37']",
  [
    {
      'interface_info': [
        {
          'device_ip': '204.1.1.37',
          'interface_details': [
            [
              {
                'addresses': [
                  
                ],
                'adminStatus': 'UP',
                'className': None,
                'deviceId': '99c8e9bf-8146-4dae-9449-8ce2d6405191',
                'duplex': 'AutoNegotiate',
                'ifIndex': '49',
                'interfaceType': 'Physical',
                'ipv4Address': None,
                'ipv4Mask': None,
                'isisSupport': 'false',
                'lastIncomingPacketTime': 1748849620000,
                'lastOutgoingPacketTime': 1752044610000,
                'lastUpdated': None,
                'macAddress': '0c:75:bd:8f:a3:a9',
                'mappedPhysicalInterfaceId': None,
                'mappedPhysicalInterfaceName': None,
                'mediaType': None,
                'mtu': '9100',
                'nativeVlanId': '1',
                'ospfSupport': 'false',
                'pid': 'C9300-24UX',
                'portMode': 'access',
                'portName': 'AppGigabitEthernet1/0/1',
                'portType': 'Ethernet Port',
                'serialNo': 'FJC2336T0SU',
                'series': 'Cisco Catalyst 9300 Series Switches',
                'speed': '1000000',
                'status': 'up',
                'vlanId': '1',
                'voiceVlan': '',
                'description': '',
                'name': None,
                'instanceUuid': '4c230c51-d2c7-41f1-97ed-21c1b50cde3c',
                'instanceTenantId': '67c18e2a74fcf4001370a56e',
                'id': '4c230c51-d2c7-41f1-97ed-21c1b50cde3c'
              },
              {
                'addresses': [
                  
                ],
                'adminStatus': 'DOWN',
                'className': None,
                'deviceId': '99c8e9bf-8146-4dae-9449-8ce2d6405191',
                'duplex': 'AutoNegotiate',
                'ifIndex': '2',
                'interfaceType': 'Physical',
                'ipv4Address': None,
                'ipv4Mask': None,
                'isisSupport': 'false',
                'lastIncomingPacketTime': 1748849620000,
                'lastOutgoingPacketTime': 1748849620000,
                'lastUpdated': None,
                'macAddress': '0c:75:bd:8f:a3:80',
                'mappedPhysicalInterfaceId': None,
                'mappedPhysicalInterfaceName': None,
                'mediaType': None,
                'mtu': '1500',
                'nativeVlanId': '',
                'ospfSupport': 'false',
                'pid': 'C9300-24UX',
                'portMode': 'routed',
                'portName': 'Bluetooth0/4',
                'portType': 'Ethernet Port',
                'serialNo': 'FJC2336T0SU',
                'series': 'Cisco Catalyst 9300 Series Switches',
                'speed': '1000000',
                'status': 'down',
                'vlanId': '0',
                'voiceVlan': '',
                'description': '',
                'name': None,
                'instanceUuid': '7160c245-6fb4-4196-a5e0-6a7ec9ef563a',
                'instanceTenantId': '67c18e2a74fcf4001370a56e',
                'id': '7160c245-6fb4-4196-a5e0-6a7ec9ef563a'
              },
              {
                'addresses': [
                  
                ],
                'adminStatus': 'UP',
                'className': None,
                'deviceId': '99c8e9bf-8146-4dae-9449-8ce2d6405191',
                'duplex': 'AutoNegotiate',
                'ifIndex': '45',
                'interfaceType': 'Physical',
                'ipv4Address': None,
                'ipv4Mask': None,
                'isisSupport': 'false',
                'lastIncomingPacketTime': 1748849620000,
                'lastOutgoingPacketTime': 1748849620000,
                'lastUpdated': None,
                'macAddress': '0c:75:bd:8f:a3:a5',
                'mappedPhysicalInterfaceId': None,
                'mappedPhysicalInterfaceName': None,
                'mediaType': None,
                'mtu': '9100',
                'nativeVlanId': '',
                'ospfSupport': 'false',
                'pid': 'C9300-24UX',
                'portMode': 'dynamic_auto',
                'portName': 'FortyGigabitEthernet1/1/1',
                'portType': 'Ethernet Port',
                'serialNo': 'FJC2336T0SU',
                'series': 'Cisco Catalyst 9300 Series Switches',
                'speed': '40000000',
                'status': 'down',
                'vlanId': '',
                'voiceVlan': '',
                'description': '',
                'name': None,
                'instanceUuid': '97735192-7532-4b12-8f81-13f541bd73ba',
                'instanceTenantId': '67c18e2a74fcf4001370a56e',
                'id': '97735192-7532-4b12-8f81-13f541bd73ba'
              },
              {
                'addresses': [
                  
                ],
                'adminStatus': 'UP',
                'className': None,
                'deviceId': '99c8e9bf-8146-4dae-9449-8ce2d6405191',
                'duplex': 'AutoNegotiate',
                'ifIndex': '46',
                'interfaceType': 'Physical',
                'ipv4Address': None,
                'ipv4Mask': None,
                'isisSupport': 'false',
                'lastIncomingPacketTime': 1748849620000,
                'lastOutgoingPacketTime': 1748849620000,
                'lastUpdated': None,
                'macAddress': '0c:75:bd:8f:a3:a6',
                'mappedPhysicalInterfaceId': None,
                'mappedPhysicalInterfaceName': None,
                'mediaType': None,
                'mtu': '9100',
                'nativeVlanId': '',
                'ospfSupport': 'false',
                'pid': 'C9300-24UX',
                'portMode': 'dynamic_auto',
                'portName': 'FortyGigabitEthernet1/1/2',
                'portType': 'Ethernet Port',
                'serialNo': 'FJC2336T0SU',
                'series': 'Cisco Catalyst 9300 Series Switches',
                'speed': '40000000',
                'status': 'down',
                'vlanId': '',
                'voiceVlan': '',
                'description': '',
                'name': None,
                'instanceUuid': '636fcac7-ec9a-4cea-aabc-d759bbe749f2',
                'instanceTenantId': '67c18e2a74fcf4001370a56e',
                'id': '636fcac7-ec9a-4cea-aabc-d759bbe749f2'
              },
              {
                'addresses': [
                  
                ],
                'adminStatus': 'UP',
                'className': None,
                'deviceId': '99c8e9bf-8146-4dae-9449-8ce2d6405191',
                'duplex': 'FullDuplex',
                'ifIndex': '1',
                'interfaceType': 'Physical',
                'ipv4Address': None,
                'ipv4Mask': None,
                'isisSupport': 'false',
                'lastIncomingPacketTime': 1752044609000,
                'lastOutgoingPacketTime': 1752044587000,
                'lastUpdated': None,
                'macAddress': '0c:75:bd:8f:a3:80',
                'mappedPhysicalInterfaceId': None,
                'mappedPhysicalInterfaceName': None,
                'mediaType': None,
                'mtu': '1500',
                'nativeVlanId': '',
                'ospfSupport': 'false',
                'pid': 'C9300-24UX',
                'portMode': 'routed',
                'portName': 'GigabitEthernet0/0',
                'portType': 'Ethernet Port',
                'serialNo': 'FJC2336T0SU',
                'series': 'Cisco Catalyst 9300 Series Switches',
                'speed': '1000000',
                'status': 'up',
                'vlanId': '0',
                'voiceVlan': '',
                'description': '',
                'name': None,
                'instanceUuid': '7ae7c580-0684-49e1-b5f2-837eb7130815',
                'instanceTenantId': '67c18e2a74fcf4001370a56e',
                'id': '7ae7c580-0684-49e1-b5f2-837eb7130815'
              },
              {
                'addresses': [
                  
                ],
                'adminStatus': 'UP',
                'className': None,
                'deviceId': '99c8e9bf-8146-4dae-9449-8ce2d6405191',
                'duplex': 'AutoNegotiate',
                'ifIndex': '33',
                'interfaceType': 'Physical',
                'ipv4Address': None,
                'ipv4Mask': None,
                'isisSupport': 'false',
                'lastIncomingPacketTime': 1748849620000,
                'lastOutgoingPacketTime': 1748849620000,
                'lastUpdated': None,
                'macAddress': '0c:75:bd:8f:a3:99',
                'mappedPhysicalInterfaceId': None,
                'mappedPhysicalInterfaceName': None,
                'mediaType': None,
                'mtu': '9100',
                'nativeVlanId': '',
                'ospfSupport': 'false',
                'pid': 'C9300-24UX',
                'portMode': 'dynamic_auto',
                'portName': 'GigabitEthernet1/1/1',
                'portType': 'Ethernet Port',
                'serialNo': 'FJC2336T0SU',
                'series': 'Cisco Catalyst 9300 Series Switches',
                'speed': '1000000',
                'status': 'down',
                'vlanId': '',
                'voiceVlan': '',
                'description': '',
                'name': None,
                'instanceUuid': '0215ab8b-c891-4da8-839c-3bfa91b93d0a',
                'instanceTenantId': '67c18e2a74fcf4001370a56e',
                'id': '0215ab8b-c891-4da8-839c-3bfa91b93d0a'
              },
              {
                'addresses': [
                  
                ],
                'adminStatus': 'UP',
                'className': None,
                'deviceId': '99c8e9bf-8146-4dae-9449-8ce2d6405191',
                'duplex': 'AutoNegotiate',
                'ifIndex': '34',
                'interfaceType': 'Physical',
                'ipv4Address': None,
                'ipv4Mask': None,
                'isisSupport': 'false',
                'lastIncomingPacketTime': 1748849620000,
                'lastOutgoingPacketTime': 1748849620000,
                'lastUpdated': None,
                'macAddress': '0c:75:bd:8f:a3:9a',
                'mappedPhysicalInterfaceId': None,
                'mappedPhysicalInterfaceName': None,
                'mediaType': None,
                'mtu': '9100',
                'nativeVlanId': '',
                'ospfSupport': 'false',
                'pid': 'C9300-24UX',
                'portMode': 'dynamic_auto',
                'portName': 'GigabitEthernet1/1/2',
                'portType': 'Ethernet Port',
                'serialNo': 'FJC2336T0SU',
                'series': 'Cisco Catalyst 9300 Series Switches',
                'speed': '1000000',
                'status': 'down',
                'vlanId': '',
                'voiceVlan': '',
                'description': '',
                'name': None,
                'instanceUuid': '63972b22-6c2e-4fee-8a90-37d8dd523330',
                'instanceTenantId': '67c18e2a74fcf4001370a56e',
                'id': '63972b22-6c2e-4fee-8a90-37d8dd523330'
              },
              {
                'addresses': [
                  
                ],
                'adminStatus': 'UP',
                'className': None,
                'deviceId': '99c8e9bf-8146-4dae-9449-8ce2d6405191',
                'duplex': 'AutoNegotiate',
                'ifIndex': '35',
                'interfaceType': 'Physical',
                'ipv4Address': None,
                'ipv4Mask': None,
                'isisSupport': 'false',
                'lastIncomingPacketTime': 1748849620000,
                'lastOutgoingPacketTime': 1748849620000,
                'lastUpdated': None,
                'macAddress': '0c:75:bd:8f:a3:9b',
                'mappedPhysicalInterfaceId': None,
                'mappedPhysicalInterfaceName': None,
                'mediaType': None,
                'mtu': '9100',
                'nativeVlanId': '',
                'ospfSupport': 'false',
                'pid': 'C9300-24UX',
                'portMode': 'dynamic_auto',
                'portName': 'GigabitEthernet1/1/3',
                'portType': 'Ethernet Port',
                'serialNo': 'FJC2336T0SU',
                'series': 'Cisco Catalyst 9300 Series Switches',
                'speed': '1000000',
                'status': 'down',
                'vlanId': '',
                'voiceVlan': '',
                'description': '',
                'name': None,
                'instanceUuid': 'a5a3b8fc-f558-4179-a42c-c4b9e2b0888a',
                'instanceTenantId': '67c18e2a74fcf4001370a56e',
                'id': 'a5a3b8fc-f558-4179-a42c-c4b9e2b0888a'
              },
              {
                'addresses': [
                  
                ],
                'adminStatus': 'UP',
                'className': None,
                'deviceId': '99c8e9bf-8146-4dae-9449-8ce2d6405191',
                'duplex': 'AutoNegotiate',
                'ifIndex': '36',
                'interfaceType': 'Physical',
                'ipv4Address': None,
                'ipv4Mask': None,
                'isisSupport': 'false',
                'lastIncomingPacketTime': 1748849620000,
                'lastOutgoingPacketTime': 1748849620000,
                'lastUpdated': None,
                'macAddress': '0c:75:bd:8f:a3:9c',
                'mappedPhysicalInterfaceId': None,
                'mappedPhysicalInterfaceName': None,
                'mediaType': None,
                'mtu': '9100',
                'nativeVlanId': '',
                'ospfSupport': 'false',
                'pid': 'C9300-24UX',
                'portMode': 'dynamic_auto',
                'portName': 'GigabitEthernet1/1/4',
                'portType': 'Ethernet Port',
                'serialNo': 'FJC2336T0SU',
                'series': 'Cisco Catalyst 9300 Series Switches',
                'speed': '1000000',
                'status': 'down',
                'vlanId': '',
                'voiceVlan': '',
                'description': '',
                'name': None,
                'instanceUuid': '7cad393e-92e9-4f3c-9ed1-e7baee19f7cb',
                'instanceTenantId': '67c18e2a74fcf4001370a56e',
                'id': '7cad393e-92e9-4f3c-9ed1-e7baee19f7cb'
              },
              {
                'addresses': [
                  {
                    'address': {
                      'ipAddress': {
                        'address': '204.1.1.37'
                      },
                      'ipMask': {
                        'address': '255.255.255.255'
                      },
                      'isInverseMask': False
                    },
                    'type': 'IPV4_PRIMARY'
                  }
                ],
                'adminStatus': 'UP',
                'className': None,
                'deviceId': '99c8e9bf-8146-4dae-9449-8ce2d6405191',
                'duplex': 'AutoNegotiate',
                'ifIndex': '54',
                'interfaceType': 'Virtual',
                'ipv4Address': '204.1.1.37',
                'ipv4Mask': '255.255.255.255',
                'isisSupport': 'true',
                'lastIncomingPacketTime': 1752044598000,
                'lastOutgoingPacketTime': 1752041404000,
                'lastUpdated': None,
                'macAddress': '',
                'mappedPhysicalInterfaceId': None,
                'mappedPhysicalInterfaceName': None,
                'mediaType': None,
                'mtu': '1514',
                'nativeVlanId': '',
                'ospfSupport': 'false',
                'pid': 'C9300-24UX',
                'portMode': 'routed',
                'portName': 'Loopback0',
                'portType': 'Service Module Interface',
                'serialNo': 'FJC2336T0SU',
                'series': 'Cisco Catalyst 9300 Series Switches',
                'speed': '8000000',
                'status': 'up',
                'vlanId': '0',
                'voiceVlan': '',
                'description': 'Fabric Node Router ID',
                'name': None,
                'instanceUuid': '77702440-f435-44e4-a5ce-01347ed83546',
                'instanceTenantId': '67c18e2a74fcf4001370a56e',
                'id': '77702440-f435-44e4-a5ce-01347ed83546'
              },
              {
                'addresses': [
                  
                ],
                'adminStatus': 'UP',
                'className': None,
                'deviceId': '99c8e9bf-8146-4dae-9449-8ce2d6405191',
                'duplex': 'AutoNegotiate',
                'ifIndex': '9',
                'interfaceType': 'Physical',
                'ipv4Address': None,
                'ipv4Mask': None,
                'isisSupport': 'false',
                'lastIncomingPacketTime': 1748849620000,
                'lastOutgoingPacketTime': 1748849620000,
                'lastUpdated': None,
                'macAddress': '0c:75:bd:8f:a3:81',
                'mappedPhysicalInterfaceId': None,
                'mappedPhysicalInterfaceName': None,
                'mediaType': None,
                'mtu': '9100',
                'nativeVlanId': '1',
                'ospfSupport': 'false',
                'pid': 'C9300-24UX',
                'portMode': 'dynamic_auto',
                'portName': 'TenGigabitEthernet1/0/1',
                'portType': 'Ethernet Port',
                'serialNo': 'FJC2336T0SU',
                'series': 'Cisco Catalyst 9300 Series Switches',
                'speed': '10000000',
                'status': 'down',
                'vlanId': '1',
                'voiceVlan': '',
                'description': '',
                'name': None,
                'instanceUuid': '3039a12a-573a-4f23-bcee-a585224948c7',
                'instanceTenantId': '67c18e2a74fcf4001370a56e',
                'id': '3039a12a-573a-4f23-bcee-a585224948c7'
              },
              {
                'addresses': [
                  
                ],
                'adminStatus': 'UP',
                'className': None,
                'deviceId': '99c8e9bf-8146-4dae-9449-8ce2d6405191',
                'duplex': 'AutoNegotiate',
                'ifIndex': '10',
                'interfaceType': 'Physical',
                'ipv4Address': None,
                'ipv4Mask': None,
                'isisSupport': 'false',
                'lastIncomingPacketTime': 1748849620000,
                'lastOutgoingPacketTime': 1748849620000,
                'lastUpdated': None,
                'macAddress': '0c:75:bd:8f:a3:82',
                'mappedPhysicalInterfaceId': None,
                'mappedPhysicalInterfaceName': None,
                'mediaType': None,
                'mtu': '9100',
                'nativeVlanId': '1',
                'ospfSupport': 'false',
                'pid': 'C9300-24UX',
                'portMode': 'dynamic_auto',
                'portName': 'TenGigabitEthernet1/0/2',
                'portType': 'Ethernet Port',
                'serialNo': 'FJC2336T0SU',
                'series': 'Cisco Catalyst 9300 Series Switches',
                'speed': '10000000',
                'status': 'down',
                'vlanId': '1',
                'voiceVlan': '',
                'description': '',
                'name': None,
                'instanceUuid': 'f8c5c90b-7ce2-4dd3-ba42-7279be0f6d8b',
                'instanceTenantId': '67c18e2a74fcf4001370a56e',
                'id': 'f8c5c90b-7ce2-4dd3-ba42-7279be0f6d8b'
              },
              {
                'addresses': [
                  {
                    'address': {
                      'ipAddress': {
                        'address': '204.1.1.135'
                      },
                      'ipMask': {
                        'address': '255.255.255.254'
                      },
                      'isInverseMask': False
                    },
                    'type': 'IPV4_PRIMARY'
                  }
                ],
                'adminStatus': 'UP',
                'className': None,
                'deviceId': '99c8e9bf-8146-4dae-9449-8ce2d6405191',
                'duplex': 'FullDuplex',
                'ifIndex': '11',
                'interfaceType': 'Physical',
                'ipv4Address': '204.1.1.135',
                'ipv4Mask': '255.255.255.254',
                'isisSupport': 'true',
                'lastIncomingPacketTime': 1752044611000,
                'lastOutgoingPacketTime': 1752044611000,
                'lastUpdated': None,
                'macAddress': '0c:75:bd:8f:a3:d8',
                'mappedPhysicalInterfaceId': None,
                'mappedPhysicalInterfaceName': None,
                'mediaType': None,
                'mtu': '9100',
                'nativeVlanId': '',
                'ospfSupport': 'false',
                'pid': 'C9300-24UX',
                'portMode': 'routed',
                'portName': 'TenGigabitEthernet1/0/3',
                'portType': 'Ethernet Port',
                'serialNo': 'FJC2336T0SU',
                'series': 'Cisco Catalyst 9300 Series Switches',
                'speed': '1000000',
                'status': 'up',
                'vlanId': '0',
                'voiceVlan': '',
                'description': 'Fabric Physical Link',
                'name': None,
                'instanceUuid': 'fb11bc4a-8af0-4586-a4cc-079053be3e50',
                'instanceTenantId': '67c18e2a74fcf4001370a56e',
                'id': 'fb11bc4a-8af0-4586-a4cc-079053be3e50'
              },
              {
                'addresses': [
                  {
                    'address': {
                      'ipAddress': {
                        'address': '204.1.1.137'
                      },
                      'ipMask': {
                        'address': '255.255.255.254'
                      },
                      'isInverseMask': False
                    },
                    'type': 'IPV4_PRIMARY'
                  }
                ],
                'adminStatus': 'UP',
                'className': None,
                'deviceId': '99c8e9bf-8146-4dae-9449-8ce2d6405191',
                'duplex': 'FullDuplex',
                'ifIndex': '12',
                'interfaceType': 'Physical',
                'ipv4Address': '204.1.1.137',
                'ipv4Mask': '255.255.255.254',
                'isisSupport': 'true',
                'lastIncomingPacketTime': 1752044611000,
                'lastOutgoingPacketTime': 1752044611000,
                'lastUpdated': None,
                'macAddress': '0c:75:bd:8f:a3:f6',
                'mappedPhysicalInterfaceId': None,
                'mappedPhysicalInterfaceName': None,
                'mediaType': None,
                'mtu': '9100',
                'nativeVlanId': '',
                'ospfSupport': 'false',
                'pid': 'C9300-24UX',
                'portMode': 'routed',
                'portName': 'TenGigabitEthernet1/0/4',
                'portType': 'Ethernet Port',
                'serialNo': 'FJC2336T0SU',
                'series': 'Cisco Catalyst 9300 Series Switches',
                'speed': '1000000',
                'status': 'up',
                'vlanId': '0',
                'voiceVlan': '',
                'description': 'Fabric Physical Link',
                'name': None,
                'instanceUuid': '1525e251-33c7-431b-8d6f-20aaf7221374',
                'instanceTenantId': '67c18e2a74fcf4001370a56e',
                'id': '1525e251-33c7-431b-8d6f-20aaf7221374'
              },
              {
                'addresses': [
                  
                ],
                'adminStatus': 'UP',
                'className': None,
                'deviceId': '99c8e9bf-8146-4dae-9449-8ce2d6405191',
                'duplex': 'AutoNegotiate',
                'ifIndex': '13',
                'interfaceType': 'Physical',
                'ipv4Address': None,
                'ipv4Mask': None,
                'isisSupport': 'false',
                'lastIncomingPacketTime': 1748849620000,
                'lastOutgoingPacketTime': 1748849620000,
                'lastUpdated': None,
                'macAddress': '0c:75:bd:8f:a3:85',
                'mappedPhysicalInterfaceId': None,
                'mappedPhysicalInterfaceName': None,
                'mediaType': None,
                'mtu': '9100',
                'nativeVlanId': '1',
                'ospfSupport': 'false',
                'pid': 'C9300-24UX',
                'portMode': 'dynamic_auto',
                'portName': 'TenGigabitEthernet1/0/5',
                'portType': 'Ethernet Port',
                'serialNo': 'FJC2336T0SU',
                'series': 'Cisco Catalyst 9300 Series Switches',
                'speed': '10000000',
                'status': 'down',
                'vlanId': '1',
                'voiceVlan': '',
                'description': '',
                'name': None,
                'instanceUuid': '4d96027b-fa57-441f-b669-4bb5988e1457',
                'instanceTenantId': '67c18e2a74fcf4001370a56e',
                'id': '4d96027b-fa57-441f-b669-4bb5988e1457'
              },
              {
                'addresses': [
                  
                ],
                'adminStatus': 'UP',
                'className': None,
                'deviceId': '99c8e9bf-8146-4dae-9449-8ce2d6405191',
                'duplex': 'AutoNegotiate',
                'ifIndex': '14',
                'interfaceType': 'Physical',
                'ipv4Address': None,
                'ipv4Mask': None,
                'isisSupport': 'false',
                'lastIncomingPacketTime': 1748849620000,
                'lastOutgoingPacketTime': 1748849620000,
                'lastUpdated': None,
                'macAddress': '0c:75:bd:8f:a3:86',
                'mappedPhysicalInterfaceId': None,
                'mappedPhysicalInterfaceName': None,
                'mediaType': None,
                'mtu': '9100',
                'nativeVlanId': '1',
                'ospfSupport': 'false',
                'pid': 'C9300-24UX',
                'portMode': 'dynamic_auto',
                'portName': 'TenGigabitEthernet1/0/6',
                'portType': 'Ethernet Port',
                'serialNo': 'FJC2336T0SU',
                'series': 'Cisco Catalyst 9300 Series Switches',
                'speed': '10000000',
                'status': 'down',
                'vlanId': '1',
                'voiceVlan': '',
                'description': '',
                'name': None,
                'instanceUuid': 'b1ffdbe5-f00c-40a2-b010-bf7f29134548',
                'instanceTenantId': '67c18e2a74fcf4001370a56e',
                'id': 'b1ffdbe5-f00c-40a2-b010-bf7f29134548'
              },
              {
                'addresses': [
                  
                ],
                'adminStatus': 'UP',
                'className': None,
                'deviceId': '99c8e9bf-8146-4dae-9449-8ce2d6405191',
                'duplex': 'FullDuplex',
                'ifIndex': '15',
                'interfaceType': 'Physical',
                'ipv4Address': None,
                'ipv4Mask': None,
                'isisSupport': 'false',
                'lastIncomingPacketTime': 1752044588000,
                'lastOutgoingPacketTime': 1752044610000,
                'lastUpdated': None,
                'macAddress': '0c:75:bd:8f:a3:87',
                'mappedPhysicalInterfaceId': None,
                'mappedPhysicalInterfaceName': None,
                'mediaType': None,
                'mtu': '9100',
                'nativeVlanId': '1',
                'ospfSupport': 'false',
                'pid': 'C9300-24UX',
                'portMode': 'access',
                'portName': 'TenGigabitEthernet1/0/7',
                'portType': 'Ethernet Port',
                'serialNo': 'FJC2336T0SU',
                'series': 'Cisco Catalyst 9300 Series Switches',
                'speed': '1000000',
                'status': 'up',
                'vlanId': '1',
                'voiceVlan': '',
                'description': '',
                'name': None,
                'instanceUuid': 'b8d0a937-b272-4025-a414-7216cdc8d1f1',
                'instanceTenantId': '67c18e2a74fcf4001370a56e',
                'id': 'b8d0a937-b272-4025-a414-7216cdc8d1f1'
              },
              {
                'addresses': [
                  
                ],
                'adminStatus': 'UP',
                'className': None,
                'deviceId': '99c8e9bf-8146-4dae-9449-8ce2d6405191',
                'duplex': 'AutoNegotiate',
                'ifIndex': '16',
                'interfaceType': 'Physical',
                'ipv4Address': None,
                'ipv4Mask': None,
                'isisSupport': 'false',
                'lastIncomingPacketTime': 1748849620000,
                'lastOutgoingPacketTime': 1748849620000,
                'lastUpdated': None,
                'macAddress': '0c:75:bd:8f:a3:88',
                'mappedPhysicalInterfaceId': None,
                'mappedPhysicalInterfaceName': None,
                'mediaType': None,
                'mtu': '9100',
                'nativeVlanId': '1',
                'ospfSupport': 'false',
                'pid': 'C9300-24UX',
                'portMode': 'dynamic_auto',
                'portName': 'TenGigabitEthernet1/0/8',
                'portType': 'Ethernet Port',
                'serialNo': 'FJC2336T0SU',
                'series': 'Cisco Catalyst 9300 Series Switches',
                'speed': '10000000',
                'status': 'down',
                'vlanId': '1',
                'voiceVlan': '',
                'description': '',
                'name': None,
                'instanceUuid': '4cc97044-19f9-4cb3-9eb2-27a4ec29f08e',
                'instanceTenantId': '67c18e2a74fcf4001370a56e',
                'id': '4cc97044-19f9-4cb3-9eb2-27a4ec29f08e'
              },
              {
                'addresses': [
                  
                ],
                'adminStatus': 'UP',
                'className': None,
                'deviceId': '99c8e9bf-8146-4dae-9449-8ce2d6405191',
                'duplex': 'AutoNegotiate',
                'ifIndex': '17',
                'interfaceType': 'Physical',
                'ipv4Address': None,
                'ipv4Mask': None,
                'isisSupport': 'false',
                'lastIncomingPacketTime': 1748849620000,
                'lastOutgoingPacketTime': 1748849620000,
                'lastUpdated': None,
                'macAddress': '0c:75:bd:8f:a3:89',
                'mappedPhysicalInterfaceId': None,
                'mappedPhysicalInterfaceName': None,
                'mediaType': None,
                'mtu': '9100',
                'nativeVlanId': '1',
                'ospfSupport': 'false',
                'pid': 'C9300-24UX',
                'portMode': 'dynamic_auto',
                'portName': 'TenGigabitEthernet1/0/9',
                'portType': 'Ethernet Port',
                'serialNo': 'FJC2336T0SU',
                'series': 'Cisco Catalyst 9300 Series Switches',
                'speed': '10000000',
                'status': 'down',
                'vlanId': '1',
                'voiceVlan': '',
                'description': '',
                'name': None,
                'instanceUuid': '3f91b465-a80a-41d5-9607-908c860ddb48',
                'instanceTenantId': '67c18e2a74fcf4001370a56e',
                'id': '3f91b465-a80a-41d5-9607-908c860ddb48'
              },
              {
                'addresses': [
                  
                ],
                'adminStatus': 'UP',
                'className': None,
                'deviceId': '99c8e9bf-8146-4dae-9449-8ce2d6405191',
                'duplex': 'AutoNegotiate',
                'ifIndex': '18',
                'interfaceType': 'Physical',
                'ipv4Address': None,
                'ipv4Mask': None,
                'isisSupport': 'false',
                'lastIncomingPacketTime': 1748849620000,
                'lastOutgoingPacketTime': 1748849620000,
                'lastUpdated': None,
                'macAddress': '0c:75:bd:8f:a3:8a',
                'mappedPhysicalInterfaceId': None,
                'mappedPhysicalInterfaceName': None,
                'mediaType': None,
                'mtu': '9100',
                'nativeVlanId': '1',
                'ospfSupport': 'false',
                'pid': 'C9300-24UX',
                'portMode': 'dynamic_auto',
                'portName': 'TenGigabitEthernet1/0/10',
                'portType': 'Ethernet Port',
                'serialNo': 'FJC2336T0SU',
                'series': 'Cisco Catalyst 9300 Series Switches',
                'speed': '10000000',
                'status': 'down',
                'vlanId': '1',
                'voiceVlan': '',
                'description': '',
                'name': None,
                'instanceUuid': '6c517c1f-557b-4d12-b96a-7515d6fd8f65',
                'instanceTenantId': '67c18e2a74fcf4001370a56e',
                'id': '6c517c1f-557b-4d12-b96a-7515d6fd8f65'
              },
              {
                'addresses': [
                  
                ],
                'adminStatus': 'UP',
                'className': None,
                'deviceId': '99c8e9bf-8146-4dae-9449-8ce2d6405191',
                'duplex': 'AutoNegotiate',
                'ifIndex': '19',
                'interfaceType': 'Physical',
                'ipv4Address': None,
                'ipv4Mask': None,
                'isisSupport': 'false',
                'lastIncomingPacketTime': 1748849620000,
                'lastOutgoingPacketTime': 1748849620000,
                'lastUpdated': None,
                'macAddress': '0c:75:bd:8f:a3:8b',
                'mappedPhysicalInterfaceId': None,
                'mappedPhysicalInterfaceName': None,
                'mediaType': None,
                'mtu': '9100',
                'nativeVlanId': '1',
                'ospfSupport': 'false',
                'pid': 'C9300-24UX',
                'portMode': 'dynamic_auto',
                'portName': 'TenGigabitEthernet1/0/11',
                'portType': 'Ethernet Port',
                'serialNo': 'FJC2336T0SU',
                'series': 'Cisco Catalyst 9300 Series Switches',
                'speed': '10000000',
                'status': 'down',
                'vlanId': '1',
                'voiceVlan': '',
                'description': '',
                'name': None,
                'instanceUuid': '2df59feb-7d91-4f36-8bd2-124b44c4a2d5',
                'instanceTenantId': '67c18e2a74fcf4001370a56e',
                'id': '2df59feb-7d91-4f36-8bd2-124b44c4a2d5'
              },
              {
                'addresses': [
                  
                ],
                'adminStatus': 'UP',
                'className': None,
                'deviceId': '99c8e9bf-8146-4dae-9449-8ce2d6405191',
                'duplex': 'AutoNegotiate',
                'ifIndex': '20',
                'interfaceType': 'Physical',
                'ipv4Address': None,
                'ipv4Mask': None,
                'isisSupport': 'false',
                'lastIncomingPacketTime': 1748849620000,
                'lastOutgoingPacketTime': 1748849620000,
                'lastUpdated': None,
                'macAddress': '0c:75:bd:8f:a3:8c',
                'mappedPhysicalInterfaceId': None,
                'mappedPhysicalInterfaceName': None,
                'mediaType': None,
                'mtu': '9100',
                'nativeVlanId': '1',
                'ospfSupport': 'false',
                'pid': 'C9300-24UX',
                'portMode': 'dynamic_auto',
                'portName': 'TenGigabitEthernet1/0/12',
                'portType': 'Ethernet Port',
                'serialNo': 'FJC2336T0SU',
                'series': 'Cisco Catalyst 9300 Series Switches',
                'speed': '10000000',
                'status': 'down',
                'vlanId': '1',
                'voiceVlan': '',
                'description': '',
                'name': None,
                'instanceUuid': 'c60a5e2a-ee78-4d75-a27e-98f1d08d32d0',
                'instanceTenantId': '67c18e2a74fcf4001370a56e',
                'id': 'c60a5e2a-ee78-4d75-a27e-98f1d08d32d0'
              },
              {
                'addresses': [
                  
                ],
                'adminStatus': 'UP',
                'className': None,
                'deviceId': '99c8e9bf-8146-4dae-9449-8ce2d6405191',
                'duplex': 'AutoNegotiate',
                'ifIndex': '21',
                'interfaceType': 'Physical',
                'ipv4Address': None,
                'ipv4Mask': None,
                'isisSupport': 'false',
                'lastIncomingPacketTime': 1748849620000,
                'lastOutgoingPacketTime': 1748849620000,
                'lastUpdated': None,
                'macAddress': '0c:75:bd:8f:a3:8d',
                'mappedPhysicalInterfaceId': None,
                'mappedPhysicalInterfaceName': None,
                'mediaType': None,
                'mtu': '9100',
                'nativeVlanId': '1',
                'ospfSupport': 'false',
                'pid': 'C9300-24UX',
                'portMode': 'dynamic_auto',
                'portName': 'TenGigabitEthernet1/0/13',
                'portType': 'Ethernet Port',
                'serialNo': 'FJC2336T0SU',
                'series': 'Cisco Catalyst 9300 Series Switches',
                'speed': '10000000',
                'status': 'down',
                'vlanId': '1',
                'voiceVlan': '',
                'description': '',
                'name': None,
                'instanceUuid': 'e2681a1f-5a14-486b-9781-0843721e583f',
                'instanceTenantId': '67c18e2a74fcf4001370a56e',
                'id': 'e2681a1f-5a14-486b-9781-0843721e583f'
              },
              {
                'addresses': [
                  
                ],
                'adminStatus': 'UP',
                'className': None,
                'deviceId': '99c8e9bf-8146-4dae-9449-8ce2d6405191',
                'duplex': 'AutoNegotiate',
                'ifIndex': '22',
                'interfaceType': 'Physical',
                'ipv4Address': None,
                'ipv4Mask': None,
                'isisSupport': 'false',
                'lastIncomingPacketTime': 1748849620000,
                'lastOutgoingPacketTime': 1748849620000,
                'lastUpdated': None,
                'macAddress': '0c:75:bd:8f:a3:8e',
                'mappedPhysicalInterfaceId': None,
                'mappedPhysicalInterfaceName': None,
                'mediaType': None,
                'mtu': '9100',
                'nativeVlanId': '1',
                'ospfSupport': 'false',
                'pid': 'C9300-24UX',
                'portMode': 'dynamic_auto',
                'portName': 'TenGigabitEthernet1/0/14',
                'portType': 'Ethernet Port',
                'serialNo': 'FJC2336T0SU',
                'series': 'Cisco Catalyst 9300 Series Switches',
                'speed': '10000000',
                'status': 'down',
                'vlanId': '1',
                'voiceVlan': '',
                'description': '',
                'name': None,
                'instanceUuid': '91adb632-c28d-4296-ab3a-956cc38f8758',
                'instanceTenantId': '67c18e2a74fcf4001370a56e',
                'id': '91adb632-c28d-4296-ab3a-956cc38f8758'
              },
              {
                'addresses': [
                  
                ],
                'adminStatus': 'UP',
                'className': None,
                'deviceId': '99c8e9bf-8146-4dae-9449-8ce2d6405191',
                'duplex': 'AutoNegotiate',
                'ifIndex': '23',
                'interfaceType': 'Physical',
                'ipv4Address': None,
                'ipv4Mask': None,
                'isisSupport': 'false',
                'lastIncomingPacketTime': 1748849620000,
                'lastOutgoingPacketTime': 1748849620000,
                'lastUpdated': None,
                'macAddress': '0c:75:bd:8f:a3:8f',
                'mappedPhysicalInterfaceId': None,
                'mappedPhysicalInterfaceName': None,
                'mediaType': None,
                'mtu': '9100',
                'nativeVlanId': '1',
                'ospfSupport': 'false',
                'pid': 'C9300-24UX',
                'portMode': 'dynamic_auto',
                'portName': 'TenGigabitEthernet1/0/15',
                'portType': 'Ethernet Port',
                'serialNo': 'FJC2336T0SU',
                'series': 'Cisco Catalyst 9300 Series Switches',
                'speed': '10000000',
                'status': 'down',
                'vlanId': '1',
                'voiceVlan': '',
                'description': '',
                'name': None,
                'instanceUuid': 'c98d6d64-d1f6-4af8-80d1-a545bc5eb447',
                'instanceTenantId': '67c18e2a74fcf4001370a56e',
                'id': 'c98d6d64-d1f6-4af8-80d1-a545bc5eb447'
              },
              {
                'addresses': [
                  
                ],
                'adminStatus': 'UP',
                'className': None,
                'deviceId': '99c8e9bf-8146-4dae-9449-8ce2d6405191',
                'duplex': 'AutoNegotiate',
                'ifIndex': '24',
                'interfaceType': 'Physical',
                'ipv4Address': None,
                'ipv4Mask': None,
                'isisSupport': 'false',
                'lastIncomingPacketTime': 1748849620000,
                'lastOutgoingPacketTime': 1748849620000,
                'lastUpdated': None,
                'macAddress': '0c:75:bd:8f:a3:90',
                'mappedPhysicalInterfaceId': None,
                'mappedPhysicalInterfaceName': None,
                'mediaType': None,
                'mtu': '9100',
                'nativeVlanId': '1',
                'ospfSupport': 'false',
                'pid': 'C9300-24UX',
                'portMode': 'dynamic_auto',
                'portName': 'TenGigabitEthernet1/0/16',
                'portType': 'Ethernet Port',
                'serialNo': 'FJC2336T0SU',
                'series': 'Cisco Catalyst 9300 Series Switches',
                'speed': '10000000',
                'status': 'down',
                'vlanId': '1',
                'voiceVlan': '',
                'description': '',
                'name': None,
                'instanceUuid': 'd86c849e-8085-46a6-a57a-e2bcef8b6096',
                'instanceTenantId': '67c18e2a74fcf4001370a56e',
                'id': 'd86c849e-8085-46a6-a57a-e2bcef8b6096'
              },
              {
                'addresses': [
                  
                ],
                'adminStatus': 'UP',
                'className': None,
                'deviceId': '99c8e9bf-8146-4dae-9449-8ce2d6405191',
                'duplex': 'AutoNegotiate',
                'ifIndex': '25',
                'interfaceType': 'Physical',
                'ipv4Address': None,
                'ipv4Mask': None,
                'isisSupport': 'false',
                'lastIncomingPacketTime': 1748849620000,
                'lastOutgoingPacketTime': 1748849620000,
                'lastUpdated': None,
                'macAddress': '0c:75:bd:8f:a3:91',
                'mappedPhysicalInterfaceId': None,
                'mappedPhysicalInterfaceName': None,
                'mediaType': None,
                'mtu': '9100',
                'nativeVlanId': '1',
                'ospfSupport': 'false',
                'pid': 'C9300-24UX',
                'portMode': 'dynamic_auto',
                'portName': 'TenGigabitEthernet1/0/17',
                'portType': 'Ethernet Port',
                'serialNo': 'FJC2336T0SU',
                'series': 'Cisco Catalyst 9300 Series Switches',
                'speed': '10000000',
                'status': 'down',
                'vlanId': '1',
                'voiceVlan': '',
                'description': '',
                'name': None,
                'instanceUuid': '7a6f43b6-4bcb-4224-8ee3-76a313ed985e',
                'instanceTenantId': '67c18e2a74fcf4001370a56e',
                'id': '7a6f43b6-4bcb-4224-8ee3-76a313ed985e'
              },
              {
                'addresses': [
                  
                ],
                'adminStatus': 'UP',
                'className': None,
                'deviceId': '99c8e9bf-8146-4dae-9449-8ce2d6405191',
                'duplex': 'AutoNegotiate',
                'ifIndex': '26',
                'interfaceType': 'Physical',
                'ipv4Address': None,
                'ipv4Mask': None,
                'isisSupport': 'false',
                'lastIncomingPacketTime': 1748849620000,
                'lastOutgoingPacketTime': 1748849620000,
                'lastUpdated': None,
                'macAddress': '0c:75:bd:8f:a3:92',
                'mappedPhysicalInterfaceId': None,
                'mappedPhysicalInterfaceName': None,
                'mediaType': None,
                'mtu': '9100',
                'nativeVlanId': '1',
                'ospfSupport': 'false',
                'pid': 'C9300-24UX',
                'portMode': 'dynamic_auto',
                'portName': 'TenGigabitEthernet1/0/18',
                'portType': 'Ethernet Port',
                'serialNo': 'FJC2336T0SU',
                'series': 'Cisco Catalyst 9300 Series Switches',
                'speed': '10000000',
                'status': 'down',
                'vlanId': '1',
                'voiceVlan': '',
                'description': '',
                'name': None,
                'instanceUuid': '6e9807ee-d2f0-4443-8c07-7f7f0b4cf134',
                'instanceTenantId': '67c18e2a74fcf4001370a56e',
                'id': '6e9807ee-d2f0-4443-8c07-7f7f0b4cf134'
              },
              {
                'addresses': [
                  
                ],
                'adminStatus': 'UP',
                'className': None,
                'deviceId': '99c8e9bf-8146-4dae-9449-8ce2d6405191',
                'duplex': 'AutoNegotiate',
                'ifIndex': '27',
                'interfaceType': 'Physical',
                'ipv4Address': None,
                'ipv4Mask': None,
                'isisSupport': 'false',
                'lastIncomingPacketTime': 1748849620000,
                'lastOutgoingPacketTime': 1748849620000,
                'lastUpdated': None,
                'macAddress': '0c:75:bd:8f:a3:93',
                'mappedPhysicalInterfaceId': None,
                'mappedPhysicalInterfaceName': None,
                'mediaType': None,
                'mtu': '9100',
                'nativeVlanId': '1',
                'ospfSupport': 'false',
                'pid': 'C9300-24UX',
                'portMode': 'dynamic_auto',
                'portName': 'TenGigabitEthernet1/0/19',
                'portType': 'Ethernet Port',
                'serialNo': 'FJC2336T0SU',
                'series': 'Cisco Catalyst 9300 Series Switches',
                'speed': '10000000',
                'status': 'down',
                'vlanId': '1',
                'voiceVlan': '',
                'description': '',
                'name': None,
                'instanceUuid': 'bc8109c4-8269-4254-ae1e-ab26e7f869e6',
                'instanceTenantId': '67c18e2a74fcf4001370a56e',
                'id': 'bc8109c4-8269-4254-ae1e-ab26e7f869e6'
              },
              {
                'addresses': [
                  
                ],
                'adminStatus': 'UP',
                'className': None,
                'deviceId': '99c8e9bf-8146-4dae-9449-8ce2d6405191',
                'duplex': 'AutoNegotiate',
                'ifIndex': '28',
                'interfaceType': 'Physical',
                'ipv4Address': None,
                'ipv4Mask': None,
                'isisSupport': 'false',
                'lastIncomingPacketTime': 1748849620000,
                'lastOutgoingPacketTime': 1748849620000,
                'lastUpdated': None,
                'macAddress': '0c:75:bd:8f:a3:94',
                'mappedPhysicalInterfaceId': None,
                'mappedPhysicalInterfaceName': None,
                'mediaType': None,
                'mtu': '9100',
                'nativeVlanId': '1',
                'ospfSupport': 'false',
                'pid': 'C9300-24UX',
                'portMode': 'dynamic_auto',
                'portName': 'TenGigabitEthernet1/0/20',
                'portType': 'Ethernet Port',
                'serialNo': 'FJC2336T0SU',
                'series': 'Cisco Catalyst 9300 Series Switches',
                'speed': '10000000',
                'status': 'down',
                'vlanId': '1',
                'voiceVlan': '',
                'description': '',
                'name': None,
                'instanceUuid': '99a6e54a-4d0a-4703-aa92-fead084a7e0a',
                'instanceTenantId': '67c18e2a74fcf4001370a56e',
                'id': '99a6e54a-4d0a-4703-aa92-fead084a7e0a'
              },
              {
                'addresses': [
                  
                ],
                'adminStatus': 'UP',
                'className': None,
                'deviceId': '99c8e9bf-8146-4dae-9449-8ce2d6405191',
                'duplex': 'AutoNegotiate',
                'ifIndex': '29',
                'interfaceType': 'Physical',
                'ipv4Address': None,
                'ipv4Mask': None,
                'isisSupport': 'false',
                'lastIncomingPacketTime': 1748849620000,
                'lastOutgoingPacketTime': 1748849620000,
                'lastUpdated': None,
                'macAddress': '0c:75:bd:8f:a3:95',
                'mappedPhysicalInterfaceId': None,
                'mappedPhysicalInterfaceName': None,
                'mediaType': None,
                'mtu': '9100',
                'nativeVlanId': '1',
                'ospfSupport': 'false',
                'pid': 'C9300-24UX',
                'portMode': 'dynamic_auto',
                'portName': 'TenGigabitEthernet1/0/21',
                'portType': 'Ethernet Port',
                'serialNo': 'FJC2336T0SU',
                'series': 'Cisco Catalyst 9300 Series Switches',
                'speed': '10000000',
                'status': 'down',
                'vlanId': '1',
                'voiceVlan': '',
                'description': '',
                'name': None,
                'instanceUuid': '39eaddad-cace-4fc6-8bef-3e28f64a81a8',
                'instanceTenantId': '67c18e2a74fcf4001370a56e',
                'id': '39eaddad-cace-4fc6-8bef-3e28f64a81a8'
              },
              {
                'addresses': [
                  
                ],
                'adminStatus': 'UP',
                'className': None,
                'deviceId': '99c8e9bf-8146-4dae-9449-8ce2d6405191',
                'duplex': 'AutoNegotiate',
                'ifIndex': '30',
                'interfaceType': 'Physical',
                'ipv4Address': None,
                'ipv4Mask': None,
                'isisSupport': 'false',
                'lastIncomingPacketTime': 1748849620000,
                'lastOutgoingPacketTime': 1748849620000,
                'lastUpdated': None,
                'macAddress': '0c:75:bd:8f:a3:96',
                'mappedPhysicalInterfaceId': None,
                'mappedPhysicalInterfaceName': None,
                'mediaType': None,
                'mtu': '9100',
                'nativeVlanId': '1',
                'ospfSupport': 'false',
                'pid': 'C9300-24UX',
                'portMode': 'dynamic_auto',
                'portName': 'TenGigabitEthernet1/0/22',
                'portType': 'Ethernet Port',
                'serialNo': 'FJC2336T0SU',
                'series': 'Cisco Catalyst 9300 Series Switches',
                'speed': '10000000',
                'status': 'down',
                'vlanId': '1',
                'voiceVlan': '',
                'description': '',
                'name': None,
                'instanceUuid': '113cfa12-b8d0-4cfa-bd57-99eb0e01fa04',
                'instanceTenantId': '67c18e2a74fcf4001370a56e',
                'id': '113cfa12-b8d0-4cfa-bd57-99eb0e01fa04'
              },
              {
                'addresses': [
                  
                ],
                'adminStatus': 'UP',
                'className': None,
                'deviceId': '99c8e9bf-8146-4dae-9449-8ce2d6405191',
                'duplex': 'AutoNegotiate',
                'ifIndex': '31',
                'interfaceType': 'Physical',
                'ipv4Address': None,
                'ipv4Mask': None,
                'isisSupport': 'false',
                'lastIncomingPacketTime': 1748849620000,
                'lastOutgoingPacketTime': 1748849620000,
                'lastUpdated': None,
                'macAddress': '0c:75:bd:8f:a3:97',
                'mappedPhysicalInterfaceId': None,
                'mappedPhysicalInterfaceName': None,
                'mediaType': None,
                'mtu': '9100',
                'nativeVlanId': '1',
                'ospfSupport': 'false',
                'pid': 'C9300-24UX',
                'portMode': 'dynamic_auto',
                'portName': 'TenGigabitEthernet1/0/23',
                'portType': 'Ethernet Port',
                'serialNo': 'FJC2336T0SU',
                'series': 'Cisco Catalyst 9300 Series Switches',
                'speed': '10000000',
                'status': 'down',
                'vlanId': '1',
                'voiceVlan': '',
                'description': '',
                'name': None,
                'instanceUuid': 'ea3f3221-eaa1-40cc-9451-add983330656',
                'instanceTenantId': '67c18e2a74fcf4001370a56e',
                'id': 'ea3f3221-eaa1-40cc-9451-add983330656'
              },
              {
                'addresses': [
                  {
                    'address': {
                      'ipAddress': {
                        'address': '204.1.2.2'
                      },
                      'ipMask': {
                        'address': '255.255.255.254'
                      },
                      'isInverseMask': False
                    },
                    'type': 'IPV4_PRIMARY'
                  }
                ],
                'adminStatus': 'UP',
                'className': None,
                'deviceId': '99c8e9bf-8146-4dae-9449-8ce2d6405191',
                'duplex': 'FullDuplex',
                'ifIndex': '32',
                'interfaceType': 'Physical',
                'ipv4Address': '204.1.2.2',
                'ipv4Mask': '255.255.255.254',
                'isisSupport': 'true',
                'lastIncomingPacketTime': 1752044611000,
                'lastOutgoingPacketTime': 1752044611000,
                'lastUpdated': None,
                'macAddress': '0c:75:bd:8f:a3:c0',
                'mappedPhysicalInterfaceId': None,
                'mappedPhysicalInterfaceName': None,
                'mediaType': None,
                'mtu': '9100',
                'nativeVlanId': '',
                'ospfSupport': 'false',
                'pid': 'C9300-24UX',
                'portMode': 'routed',
                'portName': 'TenGigabitEthernet1/0/24',
                'portType': 'Ethernet Port',
                'serialNo': 'FJC2336T0SU',
                'series': 'Cisco Catalyst 9300 Series Switches',
                'speed': '1000000',
                'status': 'up',
                'vlanId': '0',
                'voiceVlan': '',
                'description': 'Fabric Physical Link',
                'name': None,
                'instanceUuid': 'a6927a48-666d-47a6-801e-501f777dd62b',
                'instanceTenantId': '67c18e2a74fcf4001370a56e',
                'id': 'a6927a48-666d-47a6-801e-501f777dd62b'
              },
              {
                'addresses': [
                  
                ],
                'adminStatus': 'UP',
                'className': None,
                'deviceId': '99c8e9bf-8146-4dae-9449-8ce2d6405191',
                'duplex': 'AutoNegotiate',
                'ifIndex': '37',
                'interfaceType': 'Physical',
                'ipv4Address': None,
                'ipv4Mask': None,
                'isisSupport': 'false',
                'lastIncomingPacketTime': 1748849620000,
                'lastOutgoingPacketTime': 1748849620000,
                'lastUpdated': None,
                'macAddress': '0c:75:bd:8f:a3:9d',
                'mappedPhysicalInterfaceId': None,
                'mappedPhysicalInterfaceName': None,
                'mediaType': None,
                'mtu': '9100',
                'nativeVlanId': '',
                'ospfSupport': 'false',
                'pid': 'C9300-24UX',
                'portMode': 'dynamic_auto',
                'portName': 'TenGigabitEthernet1/1/1',
                'portType': 'Ethernet Port',
                'serialNo': 'FJC2336T0SU',
                'series': 'Cisco Catalyst 9300 Series Switches',
                'speed': '10000000',
                'status': 'down',
                'vlanId': '',
                'voiceVlan': '',
                'description': '',
                'name': None,
                'instanceUuid': 'ac0a318d-efb1-47fe-bef2-f790166cf867',
                'instanceTenantId': '67c18e2a74fcf4001370a56e',
                'id': 'ac0a318d-efb1-47fe-bef2-f790166cf867'
              },
              {
                'addresses': [
                  
                ],
                'adminStatus': 'UP',
                'className': None,
                'deviceId': '99c8e9bf-8146-4dae-9449-8ce2d6405191',
                'duplex': 'AutoNegotiate',
                'ifIndex': '38',
                'interfaceType': 'Physical',
                'ipv4Address': None,
                'ipv4Mask': None,
                'isisSupport': 'false',
                'lastIncomingPacketTime': 1748849620000,
                'lastOutgoingPacketTime': 1748849620000,
                'lastUpdated': None,
                'macAddress': '0c:75:bd:8f:a3:9e',
                'mappedPhysicalInterfaceId': None,
                'mappedPhysicalInterfaceName': None,
                'mediaType': None,
                'mtu': '9100',
                'nativeVlanId': '',
                'ospfSupport': 'false',
                'pid': 'C9300-24UX',
                'portMode': 'dynamic_auto',
                'portName': 'TenGigabitEthernet1/1/2',
                'portType': 'Ethernet Port',
                'serialNo': 'FJC2336T0SU',
                'series': 'Cisco Catalyst 9300 Series Switches',
                'speed': '10000000',
                'status': 'down',
                'vlanId': '',
                'voiceVlan': '',
                'description': '',
                'name': None,
                'instanceUuid': '3761315e-1dee-46ed-9ca0-f01e72b7e49c',
                'instanceTenantId': '67c18e2a74fcf4001370a56e',
                'id': '3761315e-1dee-46ed-9ca0-f01e72b7e49c'
              },
              {
                'addresses': [
                  
                ],
                'adminStatus': 'UP',
                'className': None,
                'deviceId': '99c8e9bf-8146-4dae-9449-8ce2d6405191',
                'duplex': 'AutoNegotiate',
                'ifIndex': '39',
                'interfaceType': 'Physical',
                'ipv4Address': None,
                'ipv4Mask': None,
                'isisSupport': 'false',
                'lastIncomingPacketTime': 1748849620000,
                'lastOutgoingPacketTime': 1748849620000,
                'lastUpdated': None,
                'macAddress': '0c:75:bd:8f:a3:9f',
                'mappedPhysicalInterfaceId': None,
                'mappedPhysicalInterfaceName': None,
                'mediaType': None,
                'mtu': '9100',
                'nativeVlanId': '',
                'ospfSupport': 'false',
                'pid': 'C9300-24UX',
                'portMode': 'dynamic_auto',
                'portName': 'TenGigabitEthernet1/1/3',
                'portType': 'Ethernet Port',
                'serialNo': 'FJC2336T0SU',
                'series': 'Cisco Catalyst 9300 Series Switches',
                'speed': '10000000',
                'status': 'down',
                'vlanId': '',
                'voiceVlan': '',
                'description': '',
                'name': None,
                'instanceUuid': '9b14d648-9d03-48a6-b7bc-f8fd1125a826',
                'instanceTenantId': '67c18e2a74fcf4001370a56e',
                'id': '9b14d648-9d03-48a6-b7bc-f8fd1125a826'
              },
              {
                'addresses': [
                  
                ],
                'adminStatus': 'UP',
                'className': None,
                'deviceId': '99c8e9bf-8146-4dae-9449-8ce2d6405191',
                'duplex': 'AutoNegotiate',
                'ifIndex': '40',
                'interfaceType': 'Physical',
                'ipv4Address': None,
                'ipv4Mask': None,
                'isisSupport': 'false',
                'lastIncomingPacketTime': 1748849620000,
                'lastOutgoingPacketTime': 1748849620000,
                'lastUpdated': None,
                'macAddress': '0c:75:bd:8f:a3:a0',
                'mappedPhysicalInterfaceId': None,
                'mappedPhysicalInterfaceName': None,
                'mediaType': None,
                'mtu': '9100',
                'nativeVlanId': '',
                'ospfSupport': 'false',
                'pid': 'C9300-24UX',
                'portMode': 'dynamic_auto',
                'portName': 'TenGigabitEthernet1/1/4',
                'portType': 'Ethernet Port',
                'serialNo': 'FJC2336T0SU',
                'series': 'Cisco Catalyst 9300 Series Switches',
                'speed': '10000000',
                'status': 'down',
                'vlanId': '',
                'voiceVlan': '',
                'description': '',
                'name': None,
                'instanceUuid': 'bf14717a-15cc-4b8b-8dc2-86ecb1e1764a',
                'instanceTenantId': '67c18e2a74fcf4001370a56e',
                'id': 'bf14717a-15cc-4b8b-8dc2-86ecb1e1764a'
              },
              {
                'addresses': [
                  
                ],
                'adminStatus': 'UP',
                'className': None,
                'deviceId': '99c8e9bf-8146-4dae-9449-8ce2d6405191',
                'duplex': 'AutoNegotiate',
                'ifIndex': '41',
                'interfaceType': 'Physical',
                'ipv4Address': None,
                'ipv4Mask': None,
                'isisSupport': 'false',
                'lastIncomingPacketTime': 1748849620000,
                'lastOutgoingPacketTime': 1748849620000,
                'lastUpdated': None,
                'macAddress': '0c:75:bd:8f:a3:a1',
                'mappedPhysicalInterfaceId': None,
                'mappedPhysicalInterfaceName': None,
                'mediaType': None,
                'mtu': '9100',
                'nativeVlanId': '',
                'ospfSupport': 'false',
                'pid': 'C9300-24UX',
                'portMode': 'dynamic_auto',
                'portName': 'TenGigabitEthernet1/1/5',
                'portType': 'Ethernet Port',
                'serialNo': 'FJC2336T0SU',
                'series': 'Cisco Catalyst 9300 Series Switches',
                'speed': '10000000',
                'status': 'down',
                'vlanId': '',
                'voiceVlan': '',
                'description': '',
                'name': None,
                'instanceUuid': 'f3eb3ade-0a81-4993-919c-0fc6411f0a01',
                'instanceTenantId': '67c18e2a74fcf4001370a56e',
                'id': 'f3eb3ade-0a81-4993-919c-0fc6411f0a01'
              },
              {
                'addresses': [
                  
                ],
                'adminStatus': 'UP',
                'className': None,
                'deviceId': '99c8e9bf-8146-4dae-9449-8ce2d6405191',
                'duplex': 'AutoNegotiate',
                'ifIndex': '42',
                'interfaceType': 'Physical',
                'ipv4Address': None,
                'ipv4Mask': None,
                'isisSupport': 'false',
                'lastIncomingPacketTime': 1748849620000,
                'lastOutgoingPacketTime': 1748849620000,
                'lastUpdated': None,
                'macAddress': '0c:75:bd:8f:a3:a2',
                'mappedPhysicalInterfaceId': None,
                'mappedPhysicalInterfaceName': None,
                'mediaType': None,
                'mtu': '9100',
                'nativeVlanId': '',
                'ospfSupport': 'false',
                'pid': 'C9300-24UX',
                'portMode': 'dynamic_auto',
                'portName': 'TenGigabitEthernet1/1/6',
                'portType': 'Ethernet Port',
                'serialNo': 'FJC2336T0SU',
                'series': 'Cisco Catalyst 9300 Series Switches',
                'speed': '10000000',
                'status': 'down',
                'vlanId': '',
                'voiceVlan': '',
                'description': '',
                'name': None,
                'instanceUuid': '4457fa9a-a883-473b-bf27-64760ac209d7',
                'instanceTenantId': '67c18e2a74fcf4001370a56e',
                'id': '4457fa9a-a883-473b-bf27-64760ac209d7'
              },
              {
                'addresses': [
                  
                ],
                'adminStatus': 'UP',
                'className': None,
                'deviceId': '99c8e9bf-8146-4dae-9449-8ce2d6405191',
                'duplex': 'AutoNegotiate',
                'ifIndex': '43',
                'interfaceType': 'Physical',
                'ipv4Address': None,
                'ipv4Mask': None,
                'isisSupport': 'false',
                'lastIncomingPacketTime': 1748849620000,
                'lastOutgoingPacketTime': 1748849620000,
                'lastUpdated': None,
                'macAddress': '0c:75:bd:8f:a3:a3',
                'mappedPhysicalInterfaceId': None,
                'mappedPhysicalInterfaceName': None,
                'mediaType': None,
                'mtu': '9100',
                'nativeVlanId': '',
                'ospfSupport': 'false',
                'pid': 'C9300-24UX',
                'portMode': 'dynamic_auto',
                'portName': 'TenGigabitEthernet1/1/7',
                'portType': 'Ethernet Port',
                'serialNo': 'FJC2336T0SU',
                'series': 'Cisco Catalyst 9300 Series Switches',
                'speed': '10000000',
                'status': 'down',
                'vlanId': '',
                'voiceVlan': '',
                'description': '',
                'name': None,
                'instanceUuid': '1d04af19-7706-47ec-9c06-5d1d2eb8098f',
                'instanceTenantId': '67c18e2a74fcf4001370a56e',
                'id': '1d04af19-7706-47ec-9c06-5d1d2eb8098f'
              },
              {
                'addresses': [
                  
                ],
                'adminStatus': 'UP',
                'className': None,
                'deviceId': '99c8e9bf-8146-4dae-9449-8ce2d6405191',
                'duplex': 'AutoNegotiate',
                'ifIndex': '44',
                'interfaceType': 'Physical',
                'ipv4Address': None,
                'ipv4Mask': None,
                'isisSupport': 'false',
                'lastIncomingPacketTime': 1748849620000,
                'lastOutgoingPacketTime': 1748849620000,
                'lastUpdated': None,
                'macAddress': '0c:75:bd:8f:a3:a4',
                'mappedPhysicalInterfaceId': None,
                'mappedPhysicalInterfaceName': None,
                'mediaType': None,
                'mtu': '9100',
                'nativeVlanId': '',
                'ospfSupport': 'false',
                'pid': 'C9300-24UX',
                'portMode': 'dynamic_auto',
                'portName': 'TenGigabitEthernet1/1/8',
                'portType': 'Ethernet Port',
                'serialNo': 'FJC2336T0SU',
                'series': 'Cisco Catalyst 9300 Series Switches',
                'speed': '10000000',
                'status': 'down',
                'vlanId': '',
                'voiceVlan': '',
                'description': '',
                'name': None,
                'instanceUuid': 'a033babf-37d0-4c30-a80f-3cd57016617a',
                'instanceTenantId': '67c18e2a74fcf4001370a56e',
                'id': 'a033babf-37d0-4c30-a80f-3cd57016617a'
              },
              {
                'addresses': [
                  
                ],
                'adminStatus': 'UP',
                'className': None,
                'deviceId': '99c8e9bf-8146-4dae-9449-8ce2d6405191',
                'duplex': 'AutoNegotiate',
                'ifIndex': '47',
                'interfaceType': 'Physical',
                'ipv4Address': None,
                'ipv4Mask': None,
                'isisSupport': 'false',
                'lastIncomingPacketTime': 1748849620000,
                'lastOutgoingPacketTime': 1748849620000,
                'lastUpdated': None,
                'macAddress': '0c:75:bd:8f:a3:a7',
                'mappedPhysicalInterfaceId': None,
                'mappedPhysicalInterfaceName': None,
                'mediaType': None,
                'mtu': '9100',
                'nativeVlanId': '',
                'ospfSupport': 'false',
                'pid': 'C9300-24UX',
                'portMode': 'dynamic_auto',
                'portName': 'TwentyFiveGigE1/1/1',
                'portType': 'Ethernet Port',
                'serialNo': 'FJC2336T0SU',
                'series': 'Cisco Catalyst 9300 Series Switches',
                'speed': '25000000',
                'status': 'down',
                'vlanId': '',
                'voiceVlan': '',
                'description': '',
                'name': None,
                'instanceUuid': 'c28a5300-ae9b-4d53-913d-951550db3ecf',
                'instanceTenantId': '67c18e2a74fcf4001370a56e',
                'id': 'c28a5300-ae9b-4d53-913d-951550db3ecf'
              },
              {
                'addresses': [
                  
                ],
                'adminStatus': 'UP',
                'className': None,
                'deviceId': '99c8e9bf-8146-4dae-9449-8ce2d6405191',
                'duplex': 'AutoNegotiate',
                'ifIndex': '48',
                'interfaceType': 'Physical',
                'ipv4Address': None,
                'ipv4Mask': None,
                'isisSupport': 'false',
                'lastIncomingPacketTime': 1748849620000,
                'lastOutgoingPacketTime': 1748849620000,
                'lastUpdated': None,
                'macAddress': '0c:75:bd:8f:a3:a8',
                'mappedPhysicalInterfaceId': None,
                'mappedPhysicalInterfaceName': None,
                'mediaType': None,
                'mtu': '9100',
                'nativeVlanId': '',
                'ospfSupport': 'false',
                'pid': 'C9300-24UX',
                'portMode': 'dynamic_auto',
                'portName': 'TwentyFiveGigE1/1/2',
                'portType': 'Ethernet Port',
                'serialNo': 'FJC2336T0SU',
                'series': 'Cisco Catalyst 9300 Series Switches',
                'speed': '25000000',
                'status': 'down',
                'vlanId': '',
                'voiceVlan': '',
                'description': '',
                'name': None,
                'instanceUuid': '4197a4d4-acc0-49b1-af35-7f5e6db5c3b9',
                'instanceTenantId': '67c18e2a74fcf4001370a56e',
                'id': '4197a4d4-acc0-49b1-af35-7f5e6db5c3b9'
              },
              {
                'addresses': [
                  
                ],
                'adminStatus': 'UP',
                'className': None,
                'deviceId': '99c8e9bf-8146-4dae-9449-8ce2d6405191',
                'duplex': 'AutoNegotiate',
                'ifIndex': '53',
                'interfaceType': 'Virtual',
                'ipv4Address': None,
                'ipv4Mask': None,
                'isisSupport': 'false',
                'lastIncomingPacketTime': 1748849620000,
                'lastOutgoingPacketTime': 1748849620000,
                'lastUpdated': None,
                'macAddress': '0c:75:bd:8f:a3:c7',
                'mappedPhysicalInterfaceId': None,
                'mappedPhysicalInterfaceName': None,
                'mediaType': None,
                'mtu': '9100',
                'nativeVlanId': '',
                'ospfSupport': 'false',
                'pid': 'C9300-24UX',
                'portMode': 'routed',
                'portName': 'Vlan1',
                'portType': 'Ethernet SVI',
                'serialNo': 'FJC2336T0SU',
                'series': 'Cisco Catalyst 9300 Series Switches',
                'speed': '1000000',
                'status': 'up',
                'vlanId': '1',
                'voiceVlan': '',
                'description': '',
                'name': None,
                'instanceUuid': '7ff6ef25-50d9-421f-98a2-9d8a1161bd8e',
                'instanceTenantId': '67c18e2a74fcf4001370a56e',
                'id': '7ff6ef25-50d9-421f-98a2-9d8a1161bd8e'
              }
            ]
          ]
        }
      ]
    }
  ]
]
        )

    def test_network_devices_info_workflow_manager_playbook_range_interface_details(self):
        """
        Test the Network Devices Info Workflow Manager's device information retrieval process.

        This test verifies that the workflow correctly handles the retrieval of network device information,
        ensuring proper validation and expected behavior.
        """

        set_module_args(
            dict(
                dnac_host="1.1.1.1",
                dnac_username="dummy",
                dnac_password="dummy",
                dnac_log=True,
                state="queried",
                config_verify=True,
                dnac_version="2.3.7.9",
                config=self.playbook_range_interface_details
            )
        )
        result = self.execute_module(changed=False, failed=False)
        print("#############################################")
        print("#############################################")
        print("Test result:")
        print("#############################################")
        print("#############################################")
        print(result)
        self.assertEqual(
            result.get("response"),
        [
    "The network devices found: ['204.1.1.37']",
    [
      {
        'device_interfaces_by_range_info': [
          {
            'device_ip': '204.1.1.37',
            'interface_info': [
              [
                {
                  'addresses': [
                    
                  ],
                  'adminStatus': 'UP',
                  'className': None,
                  'deviceId': '99c8e9bf-8146-4dae-9449-8ce2d6405191',
                  'duplex': 'AutoNegotiate',
                  'ifIndex': '49',
                  'interfaceType': 'Physical',
                  'ipv4Address': None,
                  'ipv4Mask': None,
                  'isisSupport': 'false',
                  'lastIncomingPacketTime': 1748849621000,
                  'lastOutgoingPacketTime': 1752083360000,
                  'lastUpdated': None,
                  'macAddress': '0c:75:bd:8f:a3:a9',
                  'mappedPhysicalInterfaceId': None,
                  'mappedPhysicalInterfaceName': None,
                  'mediaType': None,
                  'mtu': '9100',
                  'nativeVlanId': '1',
                  'ospfSupport': 'false',
                  'pid': 'C9300-24UX',
                  'portMode': 'access',
                  'portName': 'AppGigabitEthernet1/0/1',
                  'portType': 'Ethernet Port',
                  'serialNo': 'FJC2336T0SU',
                  'series': 'Cisco Catalyst 9300 Series Switches',
                  'speed': '1000000',
                  'status': 'up',
                  'vlanId': '1',
                  'voiceVlan': '',
                  'description': '',
                  'name': None,
                  'instanceUuid': '4c230c51-d2c7-41f1-97ed-21c1b50cde3c',
                  'instanceTenantId': '67c18e2a74fcf4001370a56e',
                  'id': '4c230c51-d2c7-41f1-97ed-21c1b50cde3c'
                },
                {
                  'addresses': [
                    
                  ],
                  'adminStatus': 'DOWN',
                  'className': None,
                  'deviceId': '99c8e9bf-8146-4dae-9449-8ce2d6405191',
                  'duplex': 'AutoNegotiate',
                  'ifIndex': '2',
                  'interfaceType': 'Physical',
                  'ipv4Address': None,
                  'ipv4Mask': None,
                  'isisSupport': 'false',
                  'lastIncomingPacketTime': 1748849621000,
                  'lastOutgoingPacketTime': 1748849621000,
                  'lastUpdated': None,
                  'macAddress': '0c:75:bd:8f:a3:80',
                  'mappedPhysicalInterfaceId': None,
                  'mappedPhysicalInterfaceName': None,
                  'mediaType': None,
                  'mtu': '1500',
                  'nativeVlanId': '',
                  'ospfSupport': 'false',
                  'pid': 'C9300-24UX',
                  'portMode': 'routed',
                  'portName': 'Bluetooth0/4',
                  'portType': 'Ethernet Port',
                  'serialNo': 'FJC2336T0SU',
                  'series': 'Cisco Catalyst 9300 Series Switches',
                  'speed': '1000000',
                  'status': 'down',
                  'vlanId': '0',
                  'voiceVlan': '',
                  'description': '',
                  'name': None,
                  'instanceUuid': '7160c245-6fb4-4196-a5e0-6a7ec9ef563a',
                  'instanceTenantId': '67c18e2a74fcf4001370a56e',
                  'id': '7160c245-6fb4-4196-a5e0-6a7ec9ef563a'
                },
                {
                  'addresses': [
                    
                  ],
                  'adminStatus': 'UP',
                  'className': None,
                  'deviceId': '99c8e9bf-8146-4dae-9449-8ce2d6405191',
                  'duplex': 'AutoNegotiate',
                  'ifIndex': '45',
                  'interfaceType': 'Physical',
                  'ipv4Address': None,
                  'ipv4Mask': None,
                  'isisSupport': 'false',
                  'lastIncomingPacketTime': 1748849621000,
                  'lastOutgoingPacketTime': 1748849621000,
                  'lastUpdated': None,
                  'macAddress': '0c:75:bd:8f:a3:a5',
                  'mappedPhysicalInterfaceId': None,
                  'mappedPhysicalInterfaceName': None,
                  'mediaType': None,
                  'mtu': '9100',
                  'nativeVlanId': '',
                  'ospfSupport': 'false',
                  'pid': 'C9300-24UX',
                  'portMode': 'dynamic_auto',
                  'portName': 'FortyGigabitEthernet1/1/1',
                  'portType': 'Ethernet Port',
                  'serialNo': 'FJC2336T0SU',
                  'series': 'Cisco Catalyst 9300 Series Switches',
                  'speed': '40000000',
                  'status': 'down',
                  'vlanId': '',
                  'voiceVlan': '',
                  'description': '',
                  'name': None,
                  'instanceUuid': '97735192-7532-4b12-8f81-13f541bd73ba',
                  'instanceTenantId': '67c18e2a74fcf4001370a56e',
                  'id': '97735192-7532-4b12-8f81-13f541bd73ba'
                },
                {
                  'addresses': [
                    
                  ],
                  'adminStatus': 'UP',
                  'className': None,
                  'deviceId': '99c8e9bf-8146-4dae-9449-8ce2d6405191',
                  'duplex': 'AutoNegotiate',
                  'ifIndex': '46',
                  'interfaceType': 'Physical',
                  'ipv4Address': None,
                  'ipv4Mask': None,
                  'isisSupport': 'false',
                  'lastIncomingPacketTime': 1748849621000,
                  'lastOutgoingPacketTime': 1748849621000,
                  'lastUpdated': None,
                  'macAddress': '0c:75:bd:8f:a3:a6',
                  'mappedPhysicalInterfaceId': None,
                  'mappedPhysicalInterfaceName': None,
                  'mediaType': None,
                  'mtu': '9100',
                  'nativeVlanId': '',
                  'ospfSupport': 'false',
                  'pid': 'C9300-24UX',
                  'portMode': 'dynamic_auto',
                  'portName': 'FortyGigabitEthernet1/1/2',
                  'portType': 'Ethernet Port',
                  'serialNo': 'FJC2336T0SU',
                  'series': 'Cisco Catalyst 9300 Series Switches',
                  'speed': '40000000',
                  'status': 'down',
                  'vlanId': '',
                  'voiceVlan': '',
                  'description': '',
                  'name': None,
                  'instanceUuid': '636fcac7-ec9a-4cea-aabc-d759bbe749f2',
                  'instanceTenantId': '67c18e2a74fcf4001370a56e',
                  'id': '636fcac7-ec9a-4cea-aabc-d759bbe749f2'
                },
                {
                  'addresses': [
                    
                  ],
                  'adminStatus': 'UP',
                  'className': None,
                  'deviceId': '99c8e9bf-8146-4dae-9449-8ce2d6405191',
                  'duplex': 'FullDuplex',
                  'ifIndex': '1',
                  'interfaceType': 'Physical',
                  'ipv4Address': None,
                  'ipv4Mask': None,
                  'isisSupport': 'false',
                  'lastIncomingPacketTime': 1752083360000,
                  'lastOutgoingPacketTime': 1752083317000,
                  'lastUpdated': None,
                  'macAddress': '0c:75:bd:8f:a3:80',
                  'mappedPhysicalInterfaceId': None,
                  'mappedPhysicalInterfaceName': None,
                  'mediaType': None,
                  'mtu': '1500',
                  'nativeVlanId': '',
                  'ospfSupport': 'false',
                  'pid': 'C9300-24UX',
                  'portMode': 'routed',
                  'portName': 'GigabitEthernet0/0',
                  'portType': 'Ethernet Port',
                  'serialNo': 'FJC2336T0SU',
                  'series': 'Cisco Catalyst 9300 Series Switches',
                  'speed': '1000000',
                  'status': 'up',
                  'vlanId': '0',
                  'voiceVlan': '',
                  'description': '',
                  'name': None,
                  'instanceUuid': '7ae7c580-0684-49e1-b5f2-837eb7130815',
                  'instanceTenantId': '67c18e2a74fcf4001370a56e',
                  'id': '7ae7c580-0684-49e1-b5f2-837eb7130815'
                },
                {
                  'addresses': [
                    
                  ],
                  'adminStatus': 'UP',
                  'className': None,
                  'deviceId': '99c8e9bf-8146-4dae-9449-8ce2d6405191',
                  'duplex': 'AutoNegotiate',
                  'ifIndex': '33',
                  'interfaceType': 'Physical',
                  'ipv4Address': None,
                  'ipv4Mask': None,
                  'isisSupport': 'false',
                  'lastIncomingPacketTime': 1748849621000,
                  'lastOutgoingPacketTime': 1748849621000,
                  'lastUpdated': None,
                  'macAddress': '0c:75:bd:8f:a3:99',
                  'mappedPhysicalInterfaceId': None,
                  'mappedPhysicalInterfaceName': None,
                  'mediaType': None,
                  'mtu': '9100',
                  'nativeVlanId': '',
                  'ospfSupport': 'false',
                  'pid': 'C9300-24UX',
                  'portMode': 'dynamic_auto',
                  'portName': 'GigabitEthernet1/1/1',
                  'portType': 'Ethernet Port',
                  'serialNo': 'FJC2336T0SU',
                  'series': 'Cisco Catalyst 9300 Series Switches',
                  'speed': '1000000',
                  'status': 'down',
                  'vlanId': '',
                  'voiceVlan': '',
                  'description': '',
                  'name': None,
                  'instanceUuid': '0215ab8b-c891-4da8-839c-3bfa91b93d0a',
                  'instanceTenantId': '67c18e2a74fcf4001370a56e',
                  'id': '0215ab8b-c891-4da8-839c-3bfa91b93d0a'
                },
                {
                  'addresses': [
                    
                  ],
                  'adminStatus': 'UP',
                  'className': None,
                  'deviceId': '99c8e9bf-8146-4dae-9449-8ce2d6405191',
                  'duplex': 'AutoNegotiate',
                  'ifIndex': '34',
                  'interfaceType': 'Physical',
                  'ipv4Address': None,
                  'ipv4Mask': None,
                  'isisSupport': 'false',
                  'lastIncomingPacketTime': 1748849621000,
                  'lastOutgoingPacketTime': 1748849621000,
                  'lastUpdated': None,
                  'macAddress': '0c:75:bd:8f:a3:9a',
                  'mappedPhysicalInterfaceId': None,
                  'mappedPhysicalInterfaceName': None,
                  'mediaType': None,
                  'mtu': '9100',
                  'nativeVlanId': '',
                  'ospfSupport': 'false',
                  'pid': 'C9300-24UX',
                  'portMode': 'dynamic_auto',
                  'portName': 'GigabitEthernet1/1/2',
                  'portType': 'Ethernet Port',
                  'serialNo': 'FJC2336T0SU',
                  'series': 'Cisco Catalyst 9300 Series Switches',
                  'speed': '1000000',
                  'status': 'down',
                  'vlanId': '',
                  'voiceVlan': '',
                  'description': '',
                  'name': None,
                  'instanceUuid': '63972b22-6c2e-4fee-8a90-37d8dd523330',
                  'instanceTenantId': '67c18e2a74fcf4001370a56e',
                  'id': '63972b22-6c2e-4fee-8a90-37d8dd523330'
                },
                {
                  'addresses': [
                    
                  ],
                  'adminStatus': 'UP',
                  'className': None,
                  'deviceId': '99c8e9bf-8146-4dae-9449-8ce2d6405191',
                  'duplex': 'AutoNegotiate',
                  'ifIndex': '35',
                  'interfaceType': 'Physical',
                  'ipv4Address': None,
                  'ipv4Mask': None,
                  'isisSupport': 'false',
                  'lastIncomingPacketTime': 1748849621000,
                  'lastOutgoingPacketTime': 1748849621000,
                  'lastUpdated': None,
                  'macAddress': '0c:75:bd:8f:a3:9b',
                  'mappedPhysicalInterfaceId': None,
                  'mappedPhysicalInterfaceName': None,
                  'mediaType': None,
                  'mtu': '9100',
                  'nativeVlanId': '',
                  'ospfSupport': 'false',
                  'pid': 'C9300-24UX',
                  'portMode': 'dynamic_auto',
                  'portName': 'GigabitEthernet1/1/3',
                  'portType': 'Ethernet Port',
                  'serialNo': 'FJC2336T0SU',
                  'series': 'Cisco Catalyst 9300 Series Switches',
                  'speed': '1000000',
                  'status': 'down',
                  'vlanId': '',
                  'voiceVlan': '',
                  'description': '',
                  'name': None,
                  'instanceUuid': 'a5a3b8fc-f558-4179-a42c-c4b9e2b0888a',
                  'instanceTenantId': '67c18e2a74fcf4001370a56e',
                  'id': 'a5a3b8fc-f558-4179-a42c-c4b9e2b0888a'
                },
                {
                  'addresses': [
                    
                  ],
                  'adminStatus': 'UP',
                  'className': None,
                  'deviceId': '99c8e9bf-8146-4dae-9449-8ce2d6405191',
                  'duplex': 'AutoNegotiate',
                  'ifIndex': '36',
                  'interfaceType': 'Physical',
                  'ipv4Address': None,
                  'ipv4Mask': None,
                  'isisSupport': 'false',
                  'lastIncomingPacketTime': 1748849621000,
                  'lastOutgoingPacketTime': 1748849621000,
                  'lastUpdated': None,
                  'macAddress': '0c:75:bd:8f:a3:9c',
                  'mappedPhysicalInterfaceId': None,
                  'mappedPhysicalInterfaceName': None,
                  'mediaType': None,
                  'mtu': '9100',
                  'nativeVlanId': '',
                  'ospfSupport': 'false',
                  'pid': 'C9300-24UX',
                  'portMode': 'dynamic_auto',
                  'portName': 'GigabitEthernet1/1/4',
                  'portType': 'Ethernet Port',
                  'serialNo': 'FJC2336T0SU',
                  'series': 'Cisco Catalyst 9300 Series Switches',
                  'speed': '1000000',
                  'status': 'down',
                  'vlanId': '',
                  'voiceVlan': '',
                  'description': '',
                  'name': None,
                  'instanceUuid': '7cad393e-92e9-4f3c-9ed1-e7baee19f7cb',
                  'instanceTenantId': '67c18e2a74fcf4001370a56e',
                  'id': '7cad393e-92e9-4f3c-9ed1-e7baee19f7cb'
                },
                {
                  'addresses': [
                    {
                      'address': {
                        'ipAddress': {
                          'address': '204.1.1.37'
                        },
                        'ipMask': {
                          'address': '255.255.255.255'
                        },
                        'isInverseMask': False
                      },
                      'type': 'IPV4_PRIMARY'
                    }
                  ],
                  'adminStatus': 'UP',
                  'className': None,
                  'deviceId': '99c8e9bf-8146-4dae-9449-8ce2d6405191',
                  'duplex': 'AutoNegotiate',
                  'ifIndex': '54',
                  'interfaceType': 'Virtual',
                  'ipv4Address': '204.1.1.37',
                  'ipv4Mask': '255.255.255.255',
                  'isisSupport': 'true',
                  'lastIncomingPacketTime': 1752083339000,
                  'lastOutgoingPacketTime': 1752079666000,
                  'lastUpdated': None,
                  'macAddress': '',
                  'mappedPhysicalInterfaceId': None,
                  'mappedPhysicalInterfaceName': None,
                  'mediaType': None,
                  'mtu': '1514',
                  'nativeVlanId': '',
                  'ospfSupport': 'false',
                  'pid': 'C9300-24UX',
                  'portMode': 'routed',
                  'portName': 'Loopback0',
                  'portType': 'Service Module Interface',
                  'serialNo': 'FJC2336T0SU',
                  'series': 'Cisco Catalyst 9300 Series Switches',
                  'speed': '8000000',
                  'status': 'up',
                  'vlanId': '0',
                  'voiceVlan': '',
                  'description': 'Fabric Node Router ID',
                  'name': None,
                  'instanceUuid': '77702440-f435-44e4-a5ce-01347ed83546',
                  'instanceTenantId': '67c18e2a74fcf4001370a56e',
                  'id': '77702440-f435-44e4-a5ce-01347ed83546'
                },
                {
                  'addresses': [
                    
                  ],
                  'adminStatus': 'UP',
                  'className': None,
                  'deviceId': '99c8e9bf-8146-4dae-9449-8ce2d6405191',
                  'duplex': 'AutoNegotiate',
                  'ifIndex': '9',
                  'interfaceType': 'Physical',
                  'ipv4Address': None,
                  'ipv4Mask': None,
                  'isisSupport': 'false',
                  'lastIncomingPacketTime': 1748849621000,
                  'lastOutgoingPacketTime': 1748849621000,
                  'lastUpdated': None,
                  'macAddress': '0c:75:bd:8f:a3:81',
                  'mappedPhysicalInterfaceId': None,
                  'mappedPhysicalInterfaceName': None,
                  'mediaType': None,
                  'mtu': '9100',
                  'nativeVlanId': '1',
                  'ospfSupport': 'false',
                  'pid': 'C9300-24UX',
                  'portMode': 'dynamic_auto',
                  'portName': 'TenGigabitEthernet1/0/1',
                  'portType': 'Ethernet Port',
                  'serialNo': 'FJC2336T0SU',
                  'series': 'Cisco Catalyst 9300 Series Switches',
                  'speed': '10000000',
                  'status': 'down',
                  'vlanId': '1',
                  'voiceVlan': '',
                  'description': '',
                  'name': None,
                  'instanceUuid': '3039a12a-573a-4f23-bcee-a585224948c7',
                  'instanceTenantId': '67c18e2a74fcf4001370a56e',
                  'id': '3039a12a-573a-4f23-bcee-a585224948c7'
                },
                {
                  'addresses': [
                    
                  ],
                  'adminStatus': 'UP',
                  'className': None,
                  'deviceId': '99c8e9bf-8146-4dae-9449-8ce2d6405191',
                  'duplex': 'AutoNegotiate',
                  'ifIndex': '10',
                  'interfaceType': 'Physical',
                  'ipv4Address': None,
                  'ipv4Mask': None,
                  'isisSupport': 'false',
                  'lastIncomingPacketTime': 1748849621000,
                  'lastOutgoingPacketTime': 1748849621000,
                  'lastUpdated': None,
                  'macAddress': '0c:75:bd:8f:a3:82',
                  'mappedPhysicalInterfaceId': None,
                  'mappedPhysicalInterfaceName': None,
                  'mediaType': None,
                  'mtu': '9100',
                  'nativeVlanId': '1',
                  'ospfSupport': 'false',
                  'pid': 'C9300-24UX',
                  'portMode': 'dynamic_auto',
                  'portName': 'TenGigabitEthernet1/0/2',
                  'portType': 'Ethernet Port',
                  'serialNo': 'FJC2336T0SU',
                  'series': 'Cisco Catalyst 9300 Series Switches',
                  'speed': '10000000',
                  'status': 'down',
                  'vlanId': '1',
                  'voiceVlan': '',
                  'description': '',
                  'name': None,
                  'instanceUuid': 'f8c5c90b-7ce2-4dd3-ba42-7279be0f6d8b',
                  'instanceTenantId': '67c18e2a74fcf4001370a56e',
                  'id': 'f8c5c90b-7ce2-4dd3-ba42-7279be0f6d8b'
                },
                {
                  'addresses': [
                    {
                      'address': {
                        'ipAddress': {
                          'address': '204.1.1.135'
                        },
                        'ipMask': {
                          'address': '255.255.255.254'
                        },
                        'isInverseMask': False
                      },
                      'type': 'IPV4_PRIMARY'
                    }
                  ],
                  'adminStatus': 'UP',
                  'className': None,
                  'deviceId': '99c8e9bf-8146-4dae-9449-8ce2d6405191',
                  'duplex': 'FullDuplex',
                  'ifIndex': '11',
                  'interfaceType': 'Physical',
                  'ipv4Address': '204.1.1.135',
                  'ipv4Mask': '255.255.255.254',
                  'isisSupport': 'true',
                  'lastIncomingPacketTime': 1752083360000,
                  'lastOutgoingPacketTime': 1752083360000,
                  'lastUpdated': None,
                  'macAddress': '0c:75:bd:8f:a3:d8',
                  'mappedPhysicalInterfaceId': None,
                  'mappedPhysicalInterfaceName': None,
                  'mediaType': None,
                  'mtu': '9100',
                  'nativeVlanId': '',
                  'ospfSupport': 'false',
                  'pid': 'C9300-24UX',
                  'portMode': 'routed',
                  'portName': 'TenGigabitEthernet1/0/3',
                  'portType': 'Ethernet Port',
                  'serialNo': 'FJC2336T0SU',
                  'series': 'Cisco Catalyst 9300 Series Switches',
                  'speed': '1000000',
                  'status': 'up',
                  'vlanId': '0',
                  'voiceVlan': '',
                  'description': 'Fabric Physical Link',
                  'name': None,
                  'instanceUuid': 'fb11bc4a-8af0-4586-a4cc-079053be3e50',
                  'instanceTenantId': '67c18e2a74fcf4001370a56e',
                  'id': 'fb11bc4a-8af0-4586-a4cc-079053be3e50'
                },
                {
                  'addresses': [
                    {
                      'address': {
                        'ipAddress': {
                          'address': '204.1.1.137'
                        },
                        'ipMask': {
                          'address': '255.255.255.254'
                        },
                        'isInverseMask': False
                      },
                      'type': 'IPV4_PRIMARY'
                    }
                  ],
                  'adminStatus': 'UP',
                  'className': None,
                  'deviceId': '99c8e9bf-8146-4dae-9449-8ce2d6405191',
                  'duplex': 'FullDuplex',
                  'ifIndex': '12',
                  'interfaceType': 'Physical',
                  'ipv4Address': '204.1.1.137',
                  'ipv4Mask': '255.255.255.254',
                  'isisSupport': 'true',
                  'lastIncomingPacketTime': 1752083360000,
                  'lastOutgoingPacketTime': 1752083360000,
                  'lastUpdated': None,
                  'macAddress': '0c:75:bd:8f:a3:f6',
                  'mappedPhysicalInterfaceId': None,
                  'mappedPhysicalInterfaceName': None,
                  'mediaType': None,
                  'mtu': '9100',
                  'nativeVlanId': '',
                  'ospfSupport': 'false',
                  'pid': 'C9300-24UX',
                  'portMode': 'routed',
                  'portName': 'TenGigabitEthernet1/0/4',
                  'portType': 'Ethernet Port',
                  'serialNo': 'FJC2336T0SU',
                  'series': 'Cisco Catalyst 9300 Series Switches',
                  'speed': '1000000',
                  'status': 'up',
                  'vlanId': '0',
                  'voiceVlan': '',
                  'description': 'Fabric Physical Link',
                  'name': None,
                  'instanceUuid': '1525e251-33c7-431b-8d6f-20aaf7221374',
                  'instanceTenantId': '67c18e2a74fcf4001370a56e',
                  'id': '1525e251-33c7-431b-8d6f-20aaf7221374'
                },
                {
                  'addresses': [
                    
                  ],
                  'adminStatus': 'UP',
                  'className': None,
                  'deviceId': '99c8e9bf-8146-4dae-9449-8ce2d6405191',
                  'duplex': 'AutoNegotiate',
                  'ifIndex': '13',
                  'interfaceType': 'Physical',
                  'ipv4Address': None,
                  'ipv4Mask': None,
                  'isisSupport': 'false',
                  'lastIncomingPacketTime': 1748849621000,
                  'lastOutgoingPacketTime': 1748849621000,
                  'lastUpdated': None,
                  'macAddress': '0c:75:bd:8f:a3:85',
                  'mappedPhysicalInterfaceId': None,
                  'mappedPhysicalInterfaceName': None,
                  'mediaType': None,
                  'mtu': '9100',
                  'nativeVlanId': '1',
                  'ospfSupport': 'false',
                  'pid': 'C9300-24UX',
                  'portMode': 'dynamic_auto',
                  'portName': 'TenGigabitEthernet1/0/5',
                  'portType': 'Ethernet Port',
                  'serialNo': 'FJC2336T0SU',
                  'series': 'Cisco Catalyst 9300 Series Switches',
                  'speed': '10000000',
                  'status': 'down',
                  'vlanId': '1',
                  'voiceVlan': '',
                  'description': '',
                  'name': None,
                  'instanceUuid': '4d96027b-fa57-441f-b669-4bb5988e1457',
                  'instanceTenantId': '67c18e2a74fcf4001370a56e',
                  'id': '4d96027b-fa57-441f-b669-4bb5988e1457'
                },
                {
                  'addresses': [
                    
                  ],
                  'adminStatus': 'UP',
                  'className': None,
                  'deviceId': '99c8e9bf-8146-4dae-9449-8ce2d6405191',
                  'duplex': 'AutoNegotiate',
                  'ifIndex': '14',
                  'interfaceType': 'Physical',
                  'ipv4Address': None,
                  'ipv4Mask': None,
                  'isisSupport': 'false',
                  'lastIncomingPacketTime': 1748849621000,
                  'lastOutgoingPacketTime': 1748849621000,
                  'lastUpdated': None,
                  'macAddress': '0c:75:bd:8f:a3:86',
                  'mappedPhysicalInterfaceId': None,
                  'mappedPhysicalInterfaceName': None,
                  'mediaType': None,
                  'mtu': '9100',
                  'nativeVlanId': '1',
                  'ospfSupport': 'false',
                  'pid': 'C9300-24UX',
                  'portMode': 'dynamic_auto',
                  'portName': 'TenGigabitEthernet1/0/6',
                  'portType': 'Ethernet Port',
                  'serialNo': 'FJC2336T0SU',
                  'series': 'Cisco Catalyst 9300 Series Switches',
                  'speed': '10000000',
                  'status': 'down',
                  'vlanId': '1',
                  'voiceVlan': '',
                  'description': '',
                  'name': None,
                  'instanceUuid': 'b1ffdbe5-f00c-40a2-b010-bf7f29134548',
                  'instanceTenantId': '67c18e2a74fcf4001370a56e',
                  'id': 'b1ffdbe5-f00c-40a2-b010-bf7f29134548'
                },
                {
                  'addresses': [
                    
                  ],
                  'adminStatus': 'UP',
                  'className': None,
                  'deviceId': '99c8e9bf-8146-4dae-9449-8ce2d6405191',
                  'duplex': 'FullDuplex',
                  'ifIndex': '15',
                  'interfaceType': 'Physical',
                  'ipv4Address': None,
                  'ipv4Mask': None,
                  'isisSupport': 'false',
                  'lastIncomingPacketTime': 1752083348000,
                  'lastOutgoingPacketTime': 1752083360000,
                  'lastUpdated': None,
                  'macAddress': '0c:75:bd:8f:a3:87',
                  'mappedPhysicalInterfaceId': None,
                  'mappedPhysicalInterfaceName': None,
                  'mediaType': None,
                  'mtu': '9100',
                  'nativeVlanId': '1',
                  'ospfSupport': 'false',
                  'pid': 'C9300-24UX',
                  'portMode': 'access',
                  'portName': 'TenGigabitEthernet1/0/7',
                  'portType': 'Ethernet Port',
                  'serialNo': 'FJC2336T0SU',
                  'series': 'Cisco Catalyst 9300 Series Switches',
                  'speed': '1000000',
                  'status': 'up',
                  'vlanId': '1',
                  'voiceVlan': '',
                  'description': '',
                  'name': None,
                  'instanceUuid': 'b8d0a937-b272-4025-a414-7216cdc8d1f1',
                  'instanceTenantId': '67c18e2a74fcf4001370a56e',
                  'id': 'b8d0a937-b272-4025-a414-7216cdc8d1f1'
                },
                {
                  'addresses': [
                    
                  ],
                  'adminStatus': 'UP',
                  'className': None,
                  'deviceId': '99c8e9bf-8146-4dae-9449-8ce2d6405191',
                  'duplex': 'AutoNegotiate',
                  'ifIndex': '16',
                  'interfaceType': 'Physical',
                  'ipv4Address': None,
                  'ipv4Mask': None,
                  'isisSupport': 'false',
                  'lastIncomingPacketTime': 1748849621000,
                  'lastOutgoingPacketTime': 1748849621000,
                  'lastUpdated': None,
                  'macAddress': '0c:75:bd:8f:a3:88',
                  'mappedPhysicalInterfaceId': None,
                  'mappedPhysicalInterfaceName': None,
                  'mediaType': None,
                  'mtu': '9100',
                  'nativeVlanId': '1',
                  'ospfSupport': 'false',
                  'pid': 'C9300-24UX',
                  'portMode': 'dynamic_auto',
                  'portName': 'TenGigabitEthernet1/0/8',
                  'portType': 'Ethernet Port',
                  'serialNo': 'FJC2336T0SU',
                  'series': 'Cisco Catalyst 9300 Series Switches',
                  'speed': '10000000',
                  'status': 'down',
                  'vlanId': '1',
                  'voiceVlan': '',
                  'description': '',
                  'name': None,
                  'instanceUuid': '4cc97044-19f9-4cb3-9eb2-27a4ec29f08e',
                  'instanceTenantId': '67c18e2a74fcf4001370a56e',
                  'id': '4cc97044-19f9-4cb3-9eb2-27a4ec29f08e'
                },
                {
                  'addresses': [
                    
                  ],
                  'adminStatus': 'UP',
                  'className': None,
                  'deviceId': '99c8e9bf-8146-4dae-9449-8ce2d6405191',
                  'duplex': 'AutoNegotiate',
                  'ifIndex': '17',
                  'interfaceType': 'Physical',
                  'ipv4Address': None,
                  'ipv4Mask': None,
                  'isisSupport': 'false',
                  'lastIncomingPacketTime': 1748849621000,
                  'lastOutgoingPacketTime': 1748849621000,
                  'lastUpdated': None,
                  'macAddress': '0c:75:bd:8f:a3:89',
                  'mappedPhysicalInterfaceId': None,
                  'mappedPhysicalInterfaceName': None,
                  'mediaType': None,
                  'mtu': '9100',
                  'nativeVlanId': '1',
                  'ospfSupport': 'false',
                  'pid': 'C9300-24UX',
                  'portMode': 'dynamic_auto',
                  'portName': 'TenGigabitEthernet1/0/9',
                  'portType': 'Ethernet Port',
                  'serialNo': 'FJC2336T0SU',
                  'series': 'Cisco Catalyst 9300 Series Switches',
                  'speed': '10000000',
                  'status': 'down',
                  'vlanId': '1',
                  'voiceVlan': '',
                  'description': '',
                  'name': None,
                  'instanceUuid': '3f91b465-a80a-41d5-9607-908c860ddb48',
                  'instanceTenantId': '67c18e2a74fcf4001370a56e',
                  'id': '3f91b465-a80a-41d5-9607-908c860ddb48'
                },
                {
                  'addresses': [
                    
                  ],
                  'adminStatus': 'UP',
                  'className': None,
                  'deviceId': '99c8e9bf-8146-4dae-9449-8ce2d6405191',
                  'duplex': 'AutoNegotiate',
                  'ifIndex': '18',
                  'interfaceType': 'Physical',
                  'ipv4Address': None,
                  'ipv4Mask': None,
                  'isisSupport': 'false',
                  'lastIncomingPacketTime': 1748849621000,
                  'lastOutgoingPacketTime': 1748849621000,
                  'lastUpdated': None,
                  'macAddress': '0c:75:bd:8f:a3:8a',
                  'mappedPhysicalInterfaceId': None,
                  'mappedPhysicalInterfaceName': None,
                  'mediaType': None,
                  'mtu': '9100',
                  'nativeVlanId': '1',
                  'ospfSupport': 'false',
                  'pid': 'C9300-24UX',
                  'portMode': 'dynamic_auto',
                  'portName': 'TenGigabitEthernet1/0/10',
                  'portType': 'Ethernet Port',
                  'serialNo': 'FJC2336T0SU',
                  'series': 'Cisco Catalyst 9300 Series Switches',
                  'speed': '10000000',
                  'status': 'down',
                  'vlanId': '1',
                  'voiceVlan': '',
                  'description': '',
                  'name': None,
                  'instanceUuid': '6c517c1f-557b-4d12-b96a-7515d6fd8f65',
                  'instanceTenantId': '67c18e2a74fcf4001370a56e',
                  'id': '6c517c1f-557b-4d12-b96a-7515d6fd8f65'
                },
                {
                  'addresses': [
                    
                  ],
                  'adminStatus': 'UP',
                  'className': None,
                  'deviceId': '99c8e9bf-8146-4dae-9449-8ce2d6405191',
                  'duplex': 'AutoNegotiate',
                  'ifIndex': '19',
                  'interfaceType': 'Physical',
                  'ipv4Address': None,
                  'ipv4Mask': None,
                  'isisSupport': 'false',
                  'lastIncomingPacketTime': 1748849621000,
                  'lastOutgoingPacketTime': 1748849621000,
                  'lastUpdated': None,
                  'macAddress': '0c:75:bd:8f:a3:8b',
                  'mappedPhysicalInterfaceId': None,
                  'mappedPhysicalInterfaceName': None,
                  'mediaType': None,
                  'mtu': '9100',
                  'nativeVlanId': '1',
                  'ospfSupport': 'false',
                  'pid': 'C9300-24UX',
                  'portMode': 'dynamic_auto',
                  'portName': 'TenGigabitEthernet1/0/11',
                  'portType': 'Ethernet Port',
                  'serialNo': 'FJC2336T0SU',
                  'series': 'Cisco Catalyst 9300 Series Switches',
                  'speed': '10000000',
                  'status': 'down',
                  'vlanId': '1',
                  'voiceVlan': '',
                  'description': '',
                  'name': None,
                  'instanceUuid': '2df59feb-7d91-4f36-8bd2-124b44c4a2d5',
                  'instanceTenantId': '67c18e2a74fcf4001370a56e',
                  'id': '2df59feb-7d91-4f36-8bd2-124b44c4a2d5'
                },
                {
                  'addresses': [
                    
                  ],
                  'adminStatus': 'UP',
                  'className': None,
                  'deviceId': '99c8e9bf-8146-4dae-9449-8ce2d6405191',
                  'duplex': 'AutoNegotiate',
                  'ifIndex': '20',
                  'interfaceType': 'Physical',
                  'ipv4Address': None,
                  'ipv4Mask': None,
                  'isisSupport': 'false',
                  'lastIncomingPacketTime': 1748849621000,
                  'lastOutgoingPacketTime': 1748849621000,
                  'lastUpdated': None,
                  'macAddress': '0c:75:bd:8f:a3:8c',
                  'mappedPhysicalInterfaceId': None,
                  'mappedPhysicalInterfaceName': None,
                  'mediaType': None,
                  'mtu': '9100',
                  'nativeVlanId': '1',
                  'ospfSupport': 'false',
                  'pid': 'C9300-24UX',
                  'portMode': 'dynamic_auto',
                  'portName': 'TenGigabitEthernet1/0/12',
                  'portType': 'Ethernet Port',
                  'serialNo': 'FJC2336T0SU',
                  'series': 'Cisco Catalyst 9300 Series Switches',
                  'speed': '10000000',
                  'status': 'down',
                  'vlanId': '1',
                  'voiceVlan': '',
                  'description': '',
                  'name': None,
                  'instanceUuid': 'c60a5e2a-ee78-4d75-a27e-98f1d08d32d0',
                  'instanceTenantId': '67c18e2a74fcf4001370a56e',
                  'id': 'c60a5e2a-ee78-4d75-a27e-98f1d08d32d0'
                },
                {
                  'addresses': [
                    
                  ],
                  'adminStatus': 'UP',
                  'className': None,
                  'deviceId': '99c8e9bf-8146-4dae-9449-8ce2d6405191',
                  'duplex': 'AutoNegotiate',
                  'ifIndex': '21',
                  'interfaceType': 'Physical',
                  'ipv4Address': None,
                  'ipv4Mask': None,
                  'isisSupport': 'false',
                  'lastIncomingPacketTime': 1748849621000,
                  'lastOutgoingPacketTime': 1748849621000,
                  'lastUpdated': None,
                  'macAddress': '0c:75:bd:8f:a3:8d',
                  'mappedPhysicalInterfaceId': None,
                  'mappedPhysicalInterfaceName': None,
                  'mediaType': None,
                  'mtu': '9100',
                  'nativeVlanId': '1',
                  'ospfSupport': 'false',
                  'pid': 'C9300-24UX',
                  'portMode': 'dynamic_auto',
                  'portName': 'TenGigabitEthernet1/0/13',
                  'portType': 'Ethernet Port',
                  'serialNo': 'FJC2336T0SU',
                  'series': 'Cisco Catalyst 9300 Series Switches',
                  'speed': '10000000',
                  'status': 'down',
                  'vlanId': '1',
                  'voiceVlan': '',
                  'description': '',
                  'name': None,
                  'instanceUuid': 'e2681a1f-5a14-486b-9781-0843721e583f',
                  'instanceTenantId': '67c18e2a74fcf4001370a56e',
                  'id': 'e2681a1f-5a14-486b-9781-0843721e583f'
                },
                {
                  'addresses': [
                    
                  ],
                  'adminStatus': 'UP',
                  'className': None,
                  'deviceId': '99c8e9bf-8146-4dae-9449-8ce2d6405191',
                  'duplex': 'AutoNegotiate',
                  'ifIndex': '22',
                  'interfaceType': 'Physical',
                  'ipv4Address': None,
                  'ipv4Mask': None,
                  'isisSupport': 'false',
                  'lastIncomingPacketTime': 1748849621000,
                  'lastOutgoingPacketTime': 1748849621000,
                  'lastUpdated': None,
                  'macAddress': '0c:75:bd:8f:a3:8e',
                  'mappedPhysicalInterfaceId': None,
                  'mappedPhysicalInterfaceName': None,
                  'mediaType': None,
                  'mtu': '9100',
                  'nativeVlanId': '1',
                  'ospfSupport': 'false',
                  'pid': 'C9300-24UX',
                  'portMode': 'dynamic_auto',
                  'portName': 'TenGigabitEthernet1/0/14',
                  'portType': 'Ethernet Port',
                  'serialNo': 'FJC2336T0SU',
                  'series': 'Cisco Catalyst 9300 Series Switches',
                  'speed': '10000000',
                  'status': 'down',
                  'vlanId': '1',
                  'voiceVlan': '',
                  'description': '',
                  'name': None,
                  'instanceUuid': '91adb632-c28d-4296-ab3a-956cc38f8758',
                  'instanceTenantId': '67c18e2a74fcf4001370a56e',
                  'id': '91adb632-c28d-4296-ab3a-956cc38f8758'
                },
                {
                  'addresses': [
                    
                  ],
                  'adminStatus': 'UP',
                  'className': None,
                  'deviceId': '99c8e9bf-8146-4dae-9449-8ce2d6405191',
                  'duplex': 'AutoNegotiate',
                  'ifIndex': '23',
                  'interfaceType': 'Physical',
                  'ipv4Address': None,
                  'ipv4Mask': None,
                  'isisSupport': 'false',
                  'lastIncomingPacketTime': 1748849621000,
                  'lastOutgoingPacketTime': 1748849621000,
                  'lastUpdated': None,
                  'macAddress': '0c:75:bd:8f:a3:8f',
                  'mappedPhysicalInterfaceId': None,
                  'mappedPhysicalInterfaceName': None,
                  'mediaType': None,
                  'mtu': '9100',
                  'nativeVlanId': '1',
                  'ospfSupport': 'false',
                  'pid': 'C9300-24UX',
                  'portMode': 'dynamic_auto',
                  'portName': 'TenGigabitEthernet1/0/15',
                  'portType': 'Ethernet Port',
                  'serialNo': 'FJC2336T0SU',
                  'series': 'Cisco Catalyst 9300 Series Switches',
                  'speed': '10000000',
                  'status': 'down',
                  'vlanId': '1',
                  'voiceVlan': '',
                  'description': '',
                  'name': None,
                  'instanceUuid': 'c98d6d64-d1f6-4af8-80d1-a545bc5eb447',
                  'instanceTenantId': '67c18e2a74fcf4001370a56e',
                  'id': 'c98d6d64-d1f6-4af8-80d1-a545bc5eb447'
                },
                {
                  'addresses': [
                    
                  ],
                  'adminStatus': 'UP',
                  'className': None,
                  'deviceId': '99c8e9bf-8146-4dae-9449-8ce2d6405191',
                  'duplex': 'AutoNegotiate',
                  'ifIndex': '24',
                  'interfaceType': 'Physical',
                  'ipv4Address': None,
                  'ipv4Mask': None,
                  'isisSupport': 'false',
                  'lastIncomingPacketTime': 1748849621000,
                  'lastOutgoingPacketTime': 1748849621000,
                  'lastUpdated': None,
                  'macAddress': '0c:75:bd:8f:a3:90',
                  'mappedPhysicalInterfaceId': None,
                  'mappedPhysicalInterfaceName': None,
                  'mediaType': None,
                  'mtu': '9100',
                  'nativeVlanId': '1',
                  'ospfSupport': 'false',
                  'pid': 'C9300-24UX',
                  'portMode': 'dynamic_auto',
                  'portName': 'TenGigabitEthernet1/0/16',
                  'portType': 'Ethernet Port',
                  'serialNo': 'FJC2336T0SU',
                  'series': 'Cisco Catalyst 9300 Series Switches',
                  'speed': '10000000',
                  'status': 'down',
                  'vlanId': '1',
                  'voiceVlan': '',
                  'description': '',
                  'name': None,
                  'instanceUuid': 'd86c849e-8085-46a6-a57a-e2bcef8b6096',
                  'instanceTenantId': '67c18e2a74fcf4001370a56e',
                  'id': 'd86c849e-8085-46a6-a57a-e2bcef8b6096'
                },
                {
                  'addresses': [
                    
                  ],
                  'adminStatus': 'UP',
                  'className': None,
                  'deviceId': '99c8e9bf-8146-4dae-9449-8ce2d6405191',
                  'duplex': 'AutoNegotiate',
                  'ifIndex': '25',
                  'interfaceType': 'Physical',
                  'ipv4Address': None,
                  'ipv4Mask': None,
                  'isisSupport': 'false',
                  'lastIncomingPacketTime': 1748849621000,
                  'lastOutgoingPacketTime': 1748849621000,
                  'lastUpdated': None,
                  'macAddress': '0c:75:bd:8f:a3:91',
                  'mappedPhysicalInterfaceId': None,
                  'mappedPhysicalInterfaceName': None,
                  'mediaType': None,
                  'mtu': '9100',
                  'nativeVlanId': '1',
                  'ospfSupport': 'false',
                  'pid': 'C9300-24UX',
                  'portMode': 'dynamic_auto',
                  'portName': 'TenGigabitEthernet1/0/17',
                  'portType': 'Ethernet Port',
                  'serialNo': 'FJC2336T0SU',
                  'series': 'Cisco Catalyst 9300 Series Switches',
                  'speed': '10000000',
                  'status': 'down',
                  'vlanId': '1',
                  'voiceVlan': '',
                  'description': '',
                  'name': None,
                  'instanceUuid': '7a6f43b6-4bcb-4224-8ee3-76a313ed985e',
                  'instanceTenantId': '67c18e2a74fcf4001370a56e',
                  'id': '7a6f43b6-4bcb-4224-8ee3-76a313ed985e'
                },
                {
                  'addresses': [
                    
                  ],
                  'adminStatus': 'UP',
                  'className': None,
                  'deviceId': '99c8e9bf-8146-4dae-9449-8ce2d6405191',
                  'duplex': 'AutoNegotiate',
                  'ifIndex': '26',
                  'interfaceType': 'Physical',
                  'ipv4Address': None,
                  'ipv4Mask': None,
                  'isisSupport': 'false',
                  'lastIncomingPacketTime': 1748849621000,
                  'lastOutgoingPacketTime': 1748849621000,
                  'lastUpdated': None,
                  'macAddress': '0c:75:bd:8f:a3:92',
                  'mappedPhysicalInterfaceId': None,
                  'mappedPhysicalInterfaceName': None,
                  'mediaType': None,
                  'mtu': '9100',
                  'nativeVlanId': '1',
                  'ospfSupport': 'false',
                  'pid': 'C9300-24UX',
                  'portMode': 'dynamic_auto',
                  'portName': 'TenGigabitEthernet1/0/18',
                  'portType': 'Ethernet Port',
                  'serialNo': 'FJC2336T0SU',
                  'series': 'Cisco Catalyst 9300 Series Switches',
                  'speed': '10000000',
                  'status': 'down',
                  'vlanId': '1',
                  'voiceVlan': '',
                  'description': '',
                  'name': None,
                  'instanceUuid': '6e9807ee-d2f0-4443-8c07-7f7f0b4cf134',
                  'instanceTenantId': '67c18e2a74fcf4001370a56e',
                  'id': '6e9807ee-d2f0-4443-8c07-7f7f0b4cf134'
                },
                {
                  'addresses': [
                    
                  ],
                  'adminStatus': 'UP',
                  'className': None,
                  'deviceId': '99c8e9bf-8146-4dae-9449-8ce2d6405191',
                  'duplex': 'AutoNegotiate',
                  'ifIndex': '27',
                  'interfaceType': 'Physical',
                  'ipv4Address': None,
                  'ipv4Mask': None,
                  'isisSupport': 'false',
                  'lastIncomingPacketTime': 1748849621000,
                  'lastOutgoingPacketTime': 1748849621000,
                  'lastUpdated': None,
                  'macAddress': '0c:75:bd:8f:a3:93',
                  'mappedPhysicalInterfaceId': None,
                  'mappedPhysicalInterfaceName': None,
                  'mediaType': None,
                  'mtu': '9100',
                  'nativeVlanId': '1',
                  'ospfSupport': 'false',
                  'pid': 'C9300-24UX',
                  'portMode': 'dynamic_auto',
                  'portName': 'TenGigabitEthernet1/0/19',
                  'portType': 'Ethernet Port',
                  'serialNo': 'FJC2336T0SU',
                  'series': 'Cisco Catalyst 9300 Series Switches',
                  'speed': '10000000',
                  'status': 'down',
                  'vlanId': '1',
                  'voiceVlan': '',
                  'description': '',
                  'name': None,
                  'instanceUuid': 'bc8109c4-8269-4254-ae1e-ab26e7f869e6',
                  'instanceTenantId': '67c18e2a74fcf4001370a56e',
                  'id': 'bc8109c4-8269-4254-ae1e-ab26e7f869e6'
                },
                {
                  'addresses': [
                    
                  ],
                  'adminStatus': 'UP',
                  'className': None,
                  'deviceId': '99c8e9bf-8146-4dae-9449-8ce2d6405191',
                  'duplex': 'AutoNegotiate',
                  'ifIndex': '28',
                  'interfaceType': 'Physical',
                  'ipv4Address': None,
                  'ipv4Mask': None,
                  'isisSupport': 'false',
                  'lastIncomingPacketTime': 1748849621000,
                  'lastOutgoingPacketTime': 1748849621000,
                  'lastUpdated': None,
                  'macAddress': '0c:75:bd:8f:a3:94',
                  'mappedPhysicalInterfaceId': None,
                  'mappedPhysicalInterfaceName': None,
                  'mediaType': None,
                  'mtu': '9100',
                  'nativeVlanId': '1',
                  'ospfSupport': 'false',
                  'pid': 'C9300-24UX',
                  'portMode': 'dynamic_auto',
                  'portName': 'TenGigabitEthernet1/0/20',
                  'portType': 'Ethernet Port',
                  'serialNo': 'FJC2336T0SU',
                  'series': 'Cisco Catalyst 9300 Series Switches',
                  'speed': '10000000',
                  'status': 'down',
                  'vlanId': '1',
                  'voiceVlan': '',
                  'description': '',
                  'name': None,
                  'instanceUuid': '99a6e54a-4d0a-4703-aa92-fead084a7e0a',
                  'instanceTenantId': '67c18e2a74fcf4001370a56e',
                  'id': '99a6e54a-4d0a-4703-aa92-fead084a7e0a'
                },
                {
                  'addresses': [
                    
                  ],
                  'adminStatus': 'UP',
                  'className': None,
                  'deviceId': '99c8e9bf-8146-4dae-9449-8ce2d6405191',
                  'duplex': 'AutoNegotiate',
                  'ifIndex': '29',
                  'interfaceType': 'Physical',
                  'ipv4Address': None,
                  'ipv4Mask': None,
                  'isisSupport': 'false',
                  'lastIncomingPacketTime': 1748849621000,
                  'lastOutgoingPacketTime': 1748849621000,
                  'lastUpdated': None,
                  'macAddress': '0c:75:bd:8f:a3:95',
                  'mappedPhysicalInterfaceId': None,
                  'mappedPhysicalInterfaceName': None,
                  'mediaType': None,
                  'mtu': '9100',
                  'nativeVlanId': '1',
                  'ospfSupport': 'false',
                  'pid': 'C9300-24UX',
                  'portMode': 'dynamic_auto',
                  'portName': 'TenGigabitEthernet1/0/21',
                  'portType': 'Ethernet Port',
                  'serialNo': 'FJC2336T0SU',
                  'series': 'Cisco Catalyst 9300 Series Switches',
                  'speed': '10000000',
                  'status': 'down',
                  'vlanId': '1',
                  'voiceVlan': '',
                  'description': '',
                  'name': None,
                  'instanceUuid': '39eaddad-cace-4fc6-8bef-3e28f64a81a8',
                  'instanceTenantId': '67c18e2a74fcf4001370a56e',
                  'id': '39eaddad-cace-4fc6-8bef-3e28f64a81a8'
                },
                {
                  'addresses': [
                    
                  ],
                  'adminStatus': 'UP',
                  'className': None,
                  'deviceId': '99c8e9bf-8146-4dae-9449-8ce2d6405191',
                  'duplex': 'AutoNegotiate',
                  'ifIndex': '30',
                  'interfaceType': 'Physical',
                  'ipv4Address': None,
                  'ipv4Mask': None,
                  'isisSupport': 'false',
                  'lastIncomingPacketTime': 1748849621000,
                  'lastOutgoingPacketTime': 1748849621000,
                  'lastUpdated': None,
                  'macAddress': '0c:75:bd:8f:a3:96',
                  'mappedPhysicalInterfaceId': None,
                  'mappedPhysicalInterfaceName': None,
                  'mediaType': None,
                  'mtu': '9100',
                  'nativeVlanId': '1',
                  'ospfSupport': 'false',
                  'pid': 'C9300-24UX',
                  'portMode': 'dynamic_auto',
                  'portName': 'TenGigabitEthernet1/0/22',
                  'portType': 'Ethernet Port',
                  'serialNo': 'FJC2336T0SU',
                  'series': 'Cisco Catalyst 9300 Series Switches',
                  'speed': '10000000',
                  'status': 'down',
                  'vlanId': '1',
                  'voiceVlan': '',
                  'description': '',
                  'name': None,
                  'instanceUuid': '113cfa12-b8d0-4cfa-bd57-99eb0e01fa04',
                  'instanceTenantId': '67c18e2a74fcf4001370a56e',
                  'id': '113cfa12-b8d0-4cfa-bd57-99eb0e01fa04'
                },
                {
                  'addresses': [
                    
                  ],
                  'adminStatus': 'UP',
                  'className': None,
                  'deviceId': '99c8e9bf-8146-4dae-9449-8ce2d6405191',
                  'duplex': 'AutoNegotiate',
                  'ifIndex': '31',
                  'interfaceType': 'Physical',
                  'ipv4Address': None,
                  'ipv4Mask': None,
                  'isisSupport': 'false',
                  'lastIncomingPacketTime': 1748849621000,
                  'lastOutgoingPacketTime': 1748849621000,
                  'lastUpdated': None,
                  'macAddress': '0c:75:bd:8f:a3:97',
                  'mappedPhysicalInterfaceId': None,
                  'mappedPhysicalInterfaceName': None,
                  'mediaType': None,
                  'mtu': '9100',
                  'nativeVlanId': '1',
                  'ospfSupport': 'false',
                  'pid': 'C9300-24UX',
                  'portMode': 'dynamic_auto',
                  'portName': 'TenGigabitEthernet1/0/23',
                  'portType': 'Ethernet Port',
                  'serialNo': 'FJC2336T0SU',
                  'series': 'Cisco Catalyst 9300 Series Switches',
                  'speed': '10000000',
                  'status': 'down',
                  'vlanId': '1',
                  'voiceVlan': '',
                  'description': '',
                  'name': None,
                  'instanceUuid': 'ea3f3221-eaa1-40cc-9451-add983330656',
                  'instanceTenantId': '67c18e2a74fcf4001370a56e',
                  'id': 'ea3f3221-eaa1-40cc-9451-add983330656'
                },
                {
                  'addresses': [
                    {
                      'address': {
                        'ipAddress': {
                          'address': '204.1.2.2'
                        },
                        'ipMask': {
                          'address': '255.255.255.254'
                        },
                        'isInverseMask': False
                      },
                      'type': 'IPV4_PRIMARY'
                    }
                  ],
                  'adminStatus': 'UP',
                  'className': None,
                  'deviceId': '99c8e9bf-8146-4dae-9449-8ce2d6405191',
                  'duplex': 'FullDuplex',
                  'ifIndex': '32',
                  'interfaceType': 'Physical',
                  'ipv4Address': '204.1.2.2',
                  'ipv4Mask': '255.255.255.254',
                  'isisSupport': 'true',
                  'lastIncomingPacketTime': 1752083360000,
                  'lastOutgoingPacketTime': 1752083360000,
                  'lastUpdated': None,
                  'macAddress': '0c:75:bd:8f:a3:c0',
                  'mappedPhysicalInterfaceId': None,
                  'mappedPhysicalInterfaceName': None,
                  'mediaType': None,
                  'mtu': '9100',
                  'nativeVlanId': '',
                  'ospfSupport': 'false',
                  'pid': 'C9300-24UX',
                  'portMode': 'routed',
                  'portName': 'TenGigabitEthernet1/0/24',
                  'portType': 'Ethernet Port',
                  'serialNo': 'FJC2336T0SU',
                  'series': 'Cisco Catalyst 9300 Series Switches',
                  'speed': '1000000',
                  'status': 'up',
                  'vlanId': '0',
                  'voiceVlan': '',
                  'description': 'Fabric Physical Link',
                  'name': None,
                  'instanceUuid': 'a6927a48-666d-47a6-801e-501f777dd62b',
                  'instanceTenantId': '67c18e2a74fcf4001370a56e',
                  'id': 'a6927a48-666d-47a6-801e-501f777dd62b'
                },
                {
                  'addresses': [
                    
                  ],
                  'adminStatus': 'UP',
                  'className': None,
                  'deviceId': '99c8e9bf-8146-4dae-9449-8ce2d6405191',
                  'duplex': 'AutoNegotiate',
                  'ifIndex': '37',
                  'interfaceType': 'Physical',
                  'ipv4Address': None,
                  'ipv4Mask': None,
                  'isisSupport': 'false',
                  'lastIncomingPacketTime': 1748849621000,
                  'lastOutgoingPacketTime': 1748849621000,
                  'lastUpdated': None,
                  'macAddress': '0c:75:bd:8f:a3:9d',
                  'mappedPhysicalInterfaceId': None,
                  'mappedPhysicalInterfaceName': None,
                  'mediaType': None,
                  'mtu': '9100',
                  'nativeVlanId': '',
                  'ospfSupport': 'false',
                  'pid': 'C9300-24UX',
                  'portMode': 'dynamic_auto',
                  'portName': 'TenGigabitEthernet1/1/1',
                  'portType': 'Ethernet Port',
                  'serialNo': 'FJC2336T0SU',
                  'series': 'Cisco Catalyst 9300 Series Switches',
                  'speed': '10000000',
                  'status': 'down',
                  'vlanId': '',
                  'voiceVlan': '',
                  'description': '',
                  'name': None,
                  'instanceUuid': 'ac0a318d-efb1-47fe-bef2-f790166cf867',
                  'instanceTenantId': '67c18e2a74fcf4001370a56e',
                  'id': 'ac0a318d-efb1-47fe-bef2-f790166cf867'
                },
                {
                  'addresses': [
                    
                  ],
                  'adminStatus': 'UP',
                  'className': None,
                  'deviceId': '99c8e9bf-8146-4dae-9449-8ce2d6405191',
                  'duplex': 'AutoNegotiate',
                  'ifIndex': '38',
                  'interfaceType': 'Physical',
                  'ipv4Address': None,
                  'ipv4Mask': None,
                  'isisSupport': 'false',
                  'lastIncomingPacketTime': 1748849621000,
                  'lastOutgoingPacketTime': 1748849621000,
                  'lastUpdated': None,
                  'macAddress': '0c:75:bd:8f:a3:9e',
                  'mappedPhysicalInterfaceId': None,
                  'mappedPhysicalInterfaceName': None,
                  'mediaType': None,
                  'mtu': '9100',
                  'nativeVlanId': '',
                  'ospfSupport': 'false',
                  'pid': 'C9300-24UX',
                  'portMode': 'dynamic_auto',
                  'portName': 'TenGigabitEthernet1/1/2',
                  'portType': 'Ethernet Port',
                  'serialNo': 'FJC2336T0SU',
                  'series': 'Cisco Catalyst 9300 Series Switches',
                  'speed': '10000000',
                  'status': 'down',
                  'vlanId': '',
                  'voiceVlan': '',
                  'description': '',
                  'name': None,
                  'instanceUuid': '3761315e-1dee-46ed-9ca0-f01e72b7e49c',
                  'instanceTenantId': '67c18e2a74fcf4001370a56e',
                  'id': '3761315e-1dee-46ed-9ca0-f01e72b7e49c'
                },
                {
                  'addresses': [
                    
                  ],
                  'adminStatus': 'UP',
                  'className': None,
                  'deviceId': '99c8e9bf-8146-4dae-9449-8ce2d6405191',
                  'duplex': 'AutoNegotiate',
                  'ifIndex': '39',
                  'interfaceType': 'Physical',
                  'ipv4Address': None,
                  'ipv4Mask': None,
                  'isisSupport': 'false',
                  'lastIncomingPacketTime': 1748849621000,
                  'lastOutgoingPacketTime': 1748849621000,
                  'lastUpdated': None,
                  'macAddress': '0c:75:bd:8f:a3:9f',
                  'mappedPhysicalInterfaceId': None,
                  'mappedPhysicalInterfaceName': None,
                  'mediaType': None,
                  'mtu': '9100',
                  'nativeVlanId': '',
                  'ospfSupport': 'false',
                  'pid': 'C9300-24UX',
                  'portMode': 'dynamic_auto',
                  'portName': 'TenGigabitEthernet1/1/3',
                  'portType': 'Ethernet Port',
                  'serialNo': 'FJC2336T0SU',
                  'series': 'Cisco Catalyst 9300 Series Switches',
                  'speed': '10000000',
                  'status': 'down',
                  'vlanId': '',
                  'voiceVlan': '',
                  'description': '',
                  'name': None,
                  'instanceUuid': '9b14d648-9d03-48a6-b7bc-f8fd1125a826',
                  'instanceTenantId': '67c18e2a74fcf4001370a56e',
                  'id': '9b14d648-9d03-48a6-b7bc-f8fd1125a826'
                },
                {
                  'addresses': [
                    
                  ],
                  'adminStatus': 'UP',
                  'className': None,
                  'deviceId': '99c8e9bf-8146-4dae-9449-8ce2d6405191',
                  'duplex': 'AutoNegotiate',
                  'ifIndex': '40',
                  'interfaceType': 'Physical',
                  'ipv4Address': None,
                  'ipv4Mask': None,
                  'isisSupport': 'false',
                  'lastIncomingPacketTime': 1748849621000,
                  'lastOutgoingPacketTime': 1748849621000,
                  'lastUpdated': None,
                  'macAddress': '0c:75:bd:8f:a3:a0',
                  'mappedPhysicalInterfaceId': None,
                  'mappedPhysicalInterfaceName': None,
                  'mediaType': None,
                  'mtu': '9100',
                  'nativeVlanId': '',
                  'ospfSupport': 'false',
                  'pid': 'C9300-24UX',
                  'portMode': 'dynamic_auto',
                  'portName': 'TenGigabitEthernet1/1/4',
                  'portType': 'Ethernet Port',
                  'serialNo': 'FJC2336T0SU',
                  'series': 'Cisco Catalyst 9300 Series Switches',
                  'speed': '10000000',
                  'status': 'down',
                  'vlanId': '',
                  'voiceVlan': '',
                  'description': '',
                  'name': None,
                  'instanceUuid': 'bf14717a-15cc-4b8b-8dc2-86ecb1e1764a',
                  'instanceTenantId': '67c18e2a74fcf4001370a56e',
                  'id': 'bf14717a-15cc-4b8b-8dc2-86ecb1e1764a'
                },
                {
                  'addresses': [
                    
                  ],
                  'adminStatus': 'UP',
                  'className': None,
                  'deviceId': '99c8e9bf-8146-4dae-9449-8ce2d6405191',
                  'duplex': 'AutoNegotiate',
                  'ifIndex': '41',
                  'interfaceType': 'Physical',
                  'ipv4Address': None,
                  'ipv4Mask': None,
                  'isisSupport': 'false',
                  'lastIncomingPacketTime': 1748849621000,
                  'lastOutgoingPacketTime': 1748849621000,
                  'lastUpdated': None,
                  'macAddress': '0c:75:bd:8f:a3:a1',
                  'mappedPhysicalInterfaceId': None,
                  'mappedPhysicalInterfaceName': None,
                  'mediaType': None,
                  'mtu': '9100',
                  'nativeVlanId': '',
                  'ospfSupport': 'false',
                  'pid': 'C9300-24UX',
                  'portMode': 'dynamic_auto',
                  'portName': 'TenGigabitEthernet1/1/5',
                  'portType': 'Ethernet Port',
                  'serialNo': 'FJC2336T0SU',
                  'series': 'Cisco Catalyst 9300 Series Switches',
                  'speed': '10000000',
                  'status': 'down',
                  'vlanId': '',
                  'voiceVlan': '',
                  'description': '',
                  'name': None,
                  'instanceUuid': 'f3eb3ade-0a81-4993-919c-0fc6411f0a01',
                  'instanceTenantId': '67c18e2a74fcf4001370a56e',
                  'id': 'f3eb3ade-0a81-4993-919c-0fc6411f0a01'
                },
                {
                  'addresses': [
                    
                  ],
                  'adminStatus': 'UP',
                  'className': None,
                  'deviceId': '99c8e9bf-8146-4dae-9449-8ce2d6405191',
                  'duplex': 'AutoNegotiate',
                  'ifIndex': '42',
                  'interfaceType': 'Physical',
                  'ipv4Address': None,
                  'ipv4Mask': None,
                  'isisSupport': 'false',
                  'lastIncomingPacketTime': 1748849621000,
                  'lastOutgoingPacketTime': 1748849621000,
                  'lastUpdated': None,
                  'macAddress': '0c:75:bd:8f:a3:a2',
                  'mappedPhysicalInterfaceId': None,
                  'mappedPhysicalInterfaceName': None,
                  'mediaType': None,
                  'mtu': '9100',
                  'nativeVlanId': '',
                  'ospfSupport': 'false',
                  'pid': 'C9300-24UX',
                  'portMode': 'dynamic_auto',
                  'portName': 'TenGigabitEthernet1/1/6',
                  'portType': 'Ethernet Port',
                  'serialNo': 'FJC2336T0SU',
                  'series': 'Cisco Catalyst 9300 Series Switches',
                  'speed': '10000000',
                  'status': 'down',
                  'vlanId': '',
                  'voiceVlan': '',
                  'description': '',
                  'name': None,
                  'instanceUuid': '4457fa9a-a883-473b-bf27-64760ac209d7',
                  'instanceTenantId': '67c18e2a74fcf4001370a56e',
                  'id': '4457fa9a-a883-473b-bf27-64760ac209d7'
                },
                {
                  'addresses': [
                    
                  ],
                  'adminStatus': 'UP',
                  'className': None,
                  'deviceId': '99c8e9bf-8146-4dae-9449-8ce2d6405191',
                  'duplex': 'AutoNegotiate',
                  'ifIndex': '43',
                  'interfaceType': 'Physical',
                  'ipv4Address': None,
                  'ipv4Mask': None,
                  'isisSupport': 'false',
                  'lastIncomingPacketTime': 1748849621000,
                  'lastOutgoingPacketTime': 1748849621000,
                  'lastUpdated': None,
                  'macAddress': '0c:75:bd:8f:a3:a3',
                  'mappedPhysicalInterfaceId': None,
                  'mappedPhysicalInterfaceName': None,
                  'mediaType': None,
                  'mtu': '9100',
                  'nativeVlanId': '',
                  'ospfSupport': 'false',
                  'pid': 'C9300-24UX',
                  'portMode': 'dynamic_auto',
                  'portName': 'TenGigabitEthernet1/1/7',
                  'portType': 'Ethernet Port',
                  'serialNo': 'FJC2336T0SU',
                  'series': 'Cisco Catalyst 9300 Series Switches',
                  'speed': '10000000',
                  'status': 'down',
                  'vlanId': '',
                  'voiceVlan': '',
                  'description': '',
                  'name': None,
                  'instanceUuid': '1d04af19-7706-47ec-9c06-5d1d2eb8098f',
                  'instanceTenantId': '67c18e2a74fcf4001370a56e',
                  'id': '1d04af19-7706-47ec-9c06-5d1d2eb8098f'
                },
                {
                  'addresses': [
                    
                  ],
                  'adminStatus': 'UP',
                  'className': None,
                  'deviceId': '99c8e9bf-8146-4dae-9449-8ce2d6405191',
                  'duplex': 'AutoNegotiate',
                  'ifIndex': '44',
                  'interfaceType': 'Physical',
                  'ipv4Address': None,
                  'ipv4Mask': None,
                  'isisSupport': 'false',
                  'lastIncomingPacketTime': 1748849621000,
                  'lastOutgoingPacketTime': 1748849621000,
                  'lastUpdated': None,
                  'macAddress': '0c:75:bd:8f:a3:a4',
                  'mappedPhysicalInterfaceId': None,
                  'mappedPhysicalInterfaceName': None,
                  'mediaType': None,
                  'mtu': '9100',
                  'nativeVlanId': '',
                  'ospfSupport': 'false',
                  'pid': 'C9300-24UX',
                  'portMode': 'dynamic_auto',
                  'portName': 'TenGigabitEthernet1/1/8',
                  'portType': 'Ethernet Port',
                  'serialNo': 'FJC2336T0SU',
                  'series': 'Cisco Catalyst 9300 Series Switches',
                  'speed': '10000000',
                  'status': 'down',
                  'vlanId': '',
                  'voiceVlan': '',
                  'description': '',
                  'name': None,
                  'instanceUuid': 'a033babf-37d0-4c30-a80f-3cd57016617a',
                  'instanceTenantId': '67c18e2a74fcf4001370a56e',
                  'id': 'a033babf-37d0-4c30-a80f-3cd57016617a'
                },
                {
                  'addresses': [
                    
                  ],
                  'adminStatus': 'UP',
                  'className': None,
                  'deviceId': '99c8e9bf-8146-4dae-9449-8ce2d6405191',
                  'duplex': 'AutoNegotiate',
                  'ifIndex': '47',
                  'interfaceType': 'Physical',
                  'ipv4Address': None,
                  'ipv4Mask': None,
                  'isisSupport': 'false',
                  'lastIncomingPacketTime': 1748849621000,
                  'lastOutgoingPacketTime': 1748849621000,
                  'lastUpdated': None,
                  'macAddress': '0c:75:bd:8f:a3:a7',
                  'mappedPhysicalInterfaceId': None,
                  'mappedPhysicalInterfaceName': None,
                  'mediaType': None,
                  'mtu': '9100',
                  'nativeVlanId': '',
                  'ospfSupport': 'false',
                  'pid': 'C9300-24UX',
                  'portMode': 'dynamic_auto',
                  'portName': 'TwentyFiveGigE1/1/1',
                  'portType': 'Ethernet Port',
                  'serialNo': 'FJC2336T0SU',
                  'series': 'Cisco Catalyst 9300 Series Switches',
                  'speed': '25000000',
                  'status': 'down',
                  'vlanId': '',
                  'voiceVlan': '',
                  'description': '',
                  'name': None,
                  'instanceUuid': 'c28a5300-ae9b-4d53-913d-951550db3ecf',
                  'instanceTenantId': '67c18e2a74fcf4001370a56e',
                  'id': 'c28a5300-ae9b-4d53-913d-951550db3ecf'
                },
                {
                  'addresses': [
                    
                  ],
                  'adminStatus': 'UP',
                  'className': None,
                  'deviceId': '99c8e9bf-8146-4dae-9449-8ce2d6405191',
                  'duplex': 'AutoNegotiate',
                  'ifIndex': '48',
                  'interfaceType': 'Physical',
                  'ipv4Address': None,
                  'ipv4Mask': None,
                  'isisSupport': 'false',
                  'lastIncomingPacketTime': 1748849621000,
                  'lastOutgoingPacketTime': 1748849621000,
                  'lastUpdated': None,
                  'macAddress': '0c:75:bd:8f:a3:a8',
                  'mappedPhysicalInterfaceId': None,
                  'mappedPhysicalInterfaceName': None,
                  'mediaType': None,
                  'mtu': '9100',
                  'nativeVlanId': '',
                  'ospfSupport': 'false',
                  'pid': 'C9300-24UX',
                  'portMode': 'dynamic_auto',
                  'portName': 'TwentyFiveGigE1/1/2',
                  'portType': 'Ethernet Port',
                  'serialNo': 'FJC2336T0SU',
                  'series': 'Cisco Catalyst 9300 Series Switches',
                  'speed': '25000000',
                  'status': 'down',
                  'vlanId': '',
                  'voiceVlan': '',
                  'description': '',
                  'name': None,
                  'instanceUuid': '4197a4d4-acc0-49b1-af35-7f5e6db5c3b9',
                  'instanceTenantId': '67c18e2a74fcf4001370a56e',
                  'id': '4197a4d4-acc0-49b1-af35-7f5e6db5c3b9'
                },
                {
                  'addresses': [
                    
                  ],
                  'adminStatus': 'UP',
                  'className': None,
                  'deviceId': '99c8e9bf-8146-4dae-9449-8ce2d6405191',
                  'duplex': 'AutoNegotiate',
                  'ifIndex': '53',
                  'interfaceType': 'Virtual',
                  'ipv4Address': None,
                  'ipv4Mask': None,
                  'isisSupport': 'false',
                  'lastIncomingPacketTime': 1748849621000,
                  'lastOutgoingPacketTime': 1748849621000,
                  'lastUpdated': None,
                  'macAddress': '0c:75:bd:8f:a3:c7',
                  'mappedPhysicalInterfaceId': None,
                  'mappedPhysicalInterfaceName': None,
                  'mediaType': None,
                  'mtu': '9100',
                  'nativeVlanId': '',
                  'ospfSupport': 'false',
                  'pid': 'C9300-24UX',
                  'portMode': 'routed',
                  'portName': 'Vlan1',
                  'portType': 'Ethernet SVI',
                  'serialNo': 'FJC2336T0SU',
                  'series': 'Cisco Catalyst 9300 Series Switches',
                  'speed': '1000000',
                  'status': 'up',
                  'vlanId': '1',
                  'voiceVlan': '',
                  'description': '',
                  'name': None,
                  'instanceUuid': '7ff6ef25-50d9-421f-98a2-9d8a1161bd8e',
                  'instanceTenantId': '67c18e2a74fcf4001370a56e',
                  'id': '7ff6ef25-50d9-421f-98a2-9d8a1161bd8e'
                }
              ]
            ]
          }
        ]
      }
    ]
  ]
    )
    def test_network_devices_info_workflow_manager_playbook_negative_scenario1(self):
        """
        Test the Network Devices Info Workflow Manager's device information retrieval process.

        This test verifies that the workflow correctly handles the retrieval of network device information,
        ensuring proper validation and expected behavior.
        """

        set_module_args(
            dict(
                dnac_host="1.1.1.1",
                dnac_username="dummy",
                dnac_password="dummy",
                dnac_log=True,
                state="queried",
                config_verify=True,
                dnac_version="2.3.7.9",
                config=self.playbook_negative_scenario1
            )
        )
        result = self.execute_module(changed=False, failed=True)
        print(result)
        self.assertEqual(
            result.get("msg"),
            "Parameter 'network_devices' is mandatory and cannot be empty."
    )
    def test_network_devices_info_workflow_manager_playbook_negative_scenario2(self):
        """
        Test the Network Devices Info Workflow Manager's device information retrieval process.

        This test verifies that the workflow correctly handles the retrieval of network device information,
        ensuring proper validation and expected behavior.
        """

        set_module_args(
            dict(
                dnac_host="1.1.1.1",
                dnac_username="dummy",
                dnac_password="dummy",
                dnac_log=True,
                state="queried",
                config_verify=True,
                dnac_version="2.3.7.9",
                config=self.playbook_negative_scenario2
            )
        )
        result = self.execute_module(changed=False, failed=True)
        print(result)
        self.assertEqual(
            result.get("msg"),
            "Parameter 'network_devices' is mandatory and cannot be empty."    
            )
    def test_network_devices_info_workflow_manager_playbook_negative_scenario3(self):
        """
        Test the Network Devices Info Workflow Manager's device information retrieval process.

        This test verifies that the workflow correctly handles the retrieval of network device information,
        ensuring proper validation and expected behavior.
        """

        set_module_args(
            dict(
                dnac_host="1.1.1.1",
                dnac_username="dummy",
                dnac_password="dummy",
                dnac_log=True,
                state="queried",
                config_verify=True,
                dnac_version="2.3.7.9",
                config=self.playbook_negative_scenario3
            )
        )
        result = self.execute_module(changed=False, failed=True)
        print(result)
        self.assertEqual(
            result.get("msg"),
            "'device_interfaces_by_rane_info' is not a valid option in 'requested_info'." 
            )
    def test_network_devices_info_workflow_manager_playbook_negative_scenario4(self):
        """
        Test the Network Devices Info Workflow Manager's device information retrieval process.

        This test verifies that the workflow correctly handles the retrieval of network device information,
        ensuring proper validation and expected behavior.
        """

        set_module_args(
            dict(
                dnac_host="1.1.1.1",
                dnac_username="dummy",
                dnac_password="dummy",
                dnac_log=True,
                state="queried",
                config_verify=True,
                dnac_version="2.3.7.9",
                config=self.playbook_negative_scenario4
            )
        )
        result = self.execute_module(changed=False, failed=True)
        print(result)
        self.assertEqual(
            result.get("msg"),
            "'file_mode' must be one of: a, w"
            )
    def test_network_devices_info_workflow_manager_playbook_negative_scenario5(self):
        """
        Test the Network Devices Info Workflow Manager's device information retrieval process.

        This test verifies that the workflow correctly handles the retrieval of network device information,
        ensuring proper validation and expected behavior.
        """

        set_module_args(
            dict(
                dnac_host="1.1.1.1",
                dnac_username="dummy",
                dnac_password="dummy",
                dnac_log=True,
                state="queried",
                config_verify=True,
                dnac_version="2.3.7.9",
                config=self.playbook_negative_scenario5
            )
        )
        result = self.execute_module(changed=False, failed=True)
        print(result)
        self.assertEqual(
            result.get("msg"),
            "For 'device_link_mismatch_info', 'site_hierarchy' must be provided."
            )
    def test_network_devices_info_workflow_manager_playbook_negative_scenario6(self):
        """
        Test the Network Devices Info Workflow Manager's device information retrieval process.

        This test verifies that the workflow correctly handles the retrieval of network device information,
        ensuring proper validation and expected behavior.
        """

        set_module_args(
            dict(
                dnac_host="1.1.1.1",
                dnac_username="dummy",
                dnac_password="dummy",
                dnac_log=True,
                state="queried",
                config_verify=True,
                dnac_version="2.3.7.9",
                config=self.playbook_negative_scenario6
            )
        )
        result = self.execute_module(changed=False, failed=True)
        print(result)
        self.assertEqual(
            result.get("msg"),
            "Invalid parameters in playbook: ['204.1.212.152 : is not a valid list']"
            )
    def test_network_devices_info_workflow_manager_playbook_negative_scenario7(self):
        """
        Test the Network Devices Info Workflow Manager's device information retrieval process.

        This test verifies that the workflow correctly handles the retrieval of network device information,
        ensuring proper validation and expected behavior.
        """

        set_module_args(
            dict(
                dnac_host="1.1.1.1",
                dnac_username="dummy",
                dnac_password="dummy",
                dnac_log=True,
                state="queried",
                config_verify=True,
                dnac_version="2.3.7.9",
                config=self.playbook_negative_scenario7
            )
        )
        result = self.execute_module(changed=False, failed=True)
        print(result)
        self.assertEqual(
            result.get("msg"),
            "Invalid parameters in playbook: [\"{'requested_info': ['poe_info']} : is not a valid list\"]"
            )
    def test_network_devices_info_workflow_manager_playbook_negative_scenario8(self):
        """
        Test the Network Devices Info Workflow Manager's device information retrieval process.

        This test verifies that the workflow correctly handles the retrieval of network device information,
        ensuring proper validation and expected behavior.
        """

        set_module_args(
            dict(
                dnac_host="1.1.1.1",
                dnac_username="dummy",
                dnac_password="dummy",
                dnac_log=True,
                state="queried",
                config_verify=True,
                dnac_version="2.3.7.9",
                config=self.playbook_negative_scenario8
            )
        )
        result = self.execute_module(changed=False, failed=True)
        print(result)
        self.assertEqual(
            result.get("msg"),
            "At least one of the following parameters must be specified inside each network device: management_ip_address, mac_address, hostname, serial_number, role, software_type, software_version, site_hierarchy, device_type."
            )
    def test_network_devices_info_workflow_manager_playbook_negative_scenario9(self):
        """
        Test the Network Devices Info Workflow Manager's device information retrieval process.

        This test verifies that the workflow correctly handles the retrieval of network device information,
        ensuring proper validation and expected behavior.
        """

        set_module_args(
            dict(
                dnac_host="1.1.1.1",
                dnac_username="dummy",
                dnac_password="dummy",
                dnac_log=True,
                state="queried",
                config_verify=True,
                dnac_version="2.3.7.9",
                config=self.playbook_negative_scenario9
            )
        )
        result = self.execute_module(changed=False, failed=True)
        print(result)
        self.assertEqual(
            result.get("msg"),
            "'file_format' must be one of: json, yaml"
            )

    def test_network_devices_info_workflow_manager_playbook_negative_scenario11(self):
          """
          Test the Network Devices Info Workflow Manager's device information retrieval process.

          This test verifies that the workflow correctly handles the retrieval of network device information,
          ensuring proper validation and expected behavior.
          """

          set_module_args(
              dict(
                  dnac_host="1.1.1.1",
                  dnac_username="dummy",
                  dnac_password="dummy",
                  dnac_log=True,
                  state="queried",
                  config_verify=True,
                  dnac_version="2.3.5.3",
                  config=self.playbook_negative_scenario11
              )
          )
          result = self.execute_module(changed=False, failed=True)
          self.assertEqual(
              result.get("msg"),
              "The specified version '2.3.5.3' does not support the 'network device info workflow' feature. Supported version(s) start from '2.3.7.6' onwards.",
              )